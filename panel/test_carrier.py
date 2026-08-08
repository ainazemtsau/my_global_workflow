# -*- coding: utf-8 -*-
"""Приёмка носителя после реза: один файл — один смысл для обоих читателей.

Проекции из NOW.md/TREE.md больше нет, поэтому её случаи ушли вместе с ней
(`git show 4138113c:panel/test_carrier.py`). Осталось то, что и было в них
несущим: что `osctl` и панель разбирают один и тот же файл ОДИНАКОВО, и что
живое состояние читается целиком.

Ничего не пишет: только читает `live/**` и временные файлы.

    python panel/test_carrier.py
"""
import hashlib
import io
import os
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))
import cards      # noqa: E402
import osctl      # noqa: E402

fails = []


def check(ok, msg):
    print(("OK   " if ok else "FAIL ") + msg)
    if not ok:
        fails.append(msg)


def live_fingerprint():
    h = hashlib.sha256()
    for p in sorted((ROOT / "live").rglob("*")):
        if p.is_file():
            h.update(str(p.relative_to(ROOT)).encode("utf-8"))
            h.update(p.read_bytes())
    return h.hexdigest()


def same(p):
    """Прочитать карточку обоими читателями и сравнить результат."""
    h1, b1, _ = osctl.read_card(Path(p))
    h2, b2 = cards.read_card(str(p))
    return (h1 == h2
            and {k: list(v) for k, v in b1.items()} == {k: list(v) for k, v in b2.items()})


def case_two_readers_agree():
    """Один файл — два читателя. Разошлись — и панель видит не то, что писал osctl."""
    seen = disagree = 0
    for d in sorted((ROOT / "live").iterdir()):
        folder = d / "cards"
        if not folder.is_dir():
            continue
        for p in sorted(folder.rglob("*.md")):
            seen += 1
            try:
                if not same(p):
                    disagree += 1
                    if disagree == 1:
                        print(f"     первое расхождение: {p.name}")
            except (SystemExit, osctl.Stop) as e:
                disagree += 1
                if disagree == 1:
                    print(f"     не читается: {p.name}: {e}")
    check(seen > 0, f"живых карточек найдено: {seen}")
    check(disagree == 0, f"osctl и панель читают их одинаково (расхождений {disagree})")


def case_trailing_newline_survives():
    """Значение, кончающееся переводом строки, не должно теряться при чтении."""
    tmp = Path(tempfile.mkdtemp(prefix="carrier-"))
    try:
        p = tmp / "t-1.md"
        io.open(p, "w", encoding="utf-8", newline="").write(
            "---\nid: t-1\n_kind: task\n---\n\n"
            "## goal\nстрока\n\n## note\nдругое\n"
            f"END_OF_FILE: {p}\n")
        h1, b1, _ = osctl.read_card(p)
        h2, b2 = cards.read_card(str(p))
        check(b1["goal"] == ["строка", ""], f"osctl держит пустую строку: {b1['goal']!r}")
        check(b2["goal"] == ["строка", ""], f"панель держит её же: {b2['goal']!r}")
        check(same(p), "и читатели сходятся на ней")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def case_yaml_block_round_trips():
    """Список под меткой обязан вернуться списком, а не строкой."""
    tmp = Path(tempfile.mkdtemp(prefix="carrier-"))
    try:
        p = tmp / "t-2.md"
        io.open(p, "w", encoding="utf-8", newline="").write(
            "---\nid: t-2\n_kind: task\n---\n\n"
            "## cuts\n```yaml\n- один\n- два\n```\n"
            f"END_OF_FILE: {p}\n")
        _, blocks = cards.read_card(str(p))
        v = cards.body_value(str(p), "cuts", blocks["cuts"])
        check(v == ["один", "два"], f"список вернулся списком: {v!r}")

        io.open(p, "w", encoding="utf-8", newline="").write(
            "---\nid: t-2\n_kind: task\n---\n\n"
            "## cuts\n```yaml\n- один\n"
            f"END_OF_FILE: {p}\n")
        _, blocks = cards.read_card(str(p))
        try:
            cards.body_value(str(p), "cuts", blocks["cuts"])
            check(False, "незакрытая метка должна останавливать")
        except SystemExit as e:
            check("не закрыт" in str(e), f"незакрытая метка останавливает: {str(e)[:60]}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def case_no_projection_left():
    """Конвертер снят вместе с источниками — и говорит об этом человеческим языком."""
    for name in ("build", "check", "load_now", "load_tree", "reassemble"):
        check(not hasattr(cards, name), f"{name} больше нет в определении формата")
    check(not (ROOT / "live" / "indie-game-development" / "TREE.md").exists(),
          "TREE.md действительно нет")
    check(not (ROOT / "live" / "indie-game-development" / "LOG.md").exists(),
          "LOG.md действительно нет")
    arch = ROOT / "live" / "indie-game-development" / "history" / \
        "LOG-archive-indie-game-development.md"
    check(arch.is_file() and arch.stat().st_size > 10000,
          f"а его содержимое лежит в архиве ({arch.stat().st_size if arch.exists() else 0} байт)")


def main():
    before = live_fingerprint()
    for fn in (case_two_readers_agree, case_trailing_newline_survives,
               case_yaml_block_round_trips, case_no_projection_left):
        print(f"\n--- {fn.__doc__.splitlines()[0]}")
        fn()
    print("\n--- Живое состояние")
    check(live_fingerprint() == before, "live/ не изменился ни на байт")
    print(f"\n{'ПРИНЯТО' if not fails else 'НЕ ПРИНЯТО: ' + str(len(fails)) + ' упало'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
