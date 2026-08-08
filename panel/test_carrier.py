# -*- coding: utf-8 -*-
"""Приёмка носителя: карточки переживают живое состояние, а проверка ПАДАЕТ
на том, что раньше теряла молча.

Пишет только во временную папку. live/ — чтение, и то лишь в последнем случае.

    python panel/test_carrier.py
"""
import io
import os
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cards  # noqa: E402

REAL_ROOT = cards.ROOT
D = "t-dir"
fails = []


def check(ok, msg):
    print(("OK   " if ok else "FAIL ") + msg)
    if not ok:
        fails.append(msg)


def make_repo(now_text, tree_text=None):
    """Маленький поддельный репозиторий: только то, что читает конвертер."""
    root = tempfile.mkdtemp(prefix="carrier-")
    d = os.path.join(root, "live", D)
    os.makedirs(d)
    io.open(os.path.join(d, "NOW.md"), "w", encoding="utf-8", newline="").write(now_text)
    if tree_text is not None:
        io.open(os.path.join(d, "TREE.md"), "w", encoding="utf-8", newline="").write(tree_text)
    cards.ROOT = root
    return root


def run(fn, *a, **kw):
    """Вернуть (успех, текст ошибки). cards.fail бросает SystemExit."""
    out = io.StringIO()
    keep, sys.stdout = sys.stdout, out
    try:
        fn(*a, **kw)
        return True, out.getvalue()
    except SystemExit as e:
        return False, str(e)
    finally:
        sys.stdout = keep


TREE = """owner_approved: |-
  root 2026-01-01 — history/x.md
root:
- id: g-root
  goal: корень
  children:
  - id: g-1
    goal: цель
    children: []

END_OF_FILE: live/%s/TREE.md
""" % D


def case_data_may_use_any_name():
    """Поле владельца может называться kind, pos, parent, bet — это его слова."""
    now = """bet:
  node: g-1
  goal: ставка на существующий узел дерева
tasks:
- id: t-1
  kind: executor
  pos: слева
  parent: дом
  bet: своё значение
  status: open
direction_forecast:
  status: no_basis
END_OF_FILE: live/%s/NOW.md
""" % D
    make_repo(now, TREE)
    ok, msg = run(cards.build, D)
    check(ok, f"строится, когда данные заняли служебные имена ({msg.strip()[:60]})")
    if ok:
        ok2, msg2 = run(cards.check, D)
        check(ok2, f"и собирается обратно ({msg2.strip()[:80]})")
        f = os.path.join(cards.ROOT, "panel", ".cards", D, "bet-g-1.md")
        check(os.path.isfile(f), "у ставки свой файл bet-<узел>, с узлом не спорит")


def case_unknown_key_is_carried_and_named():
    """Ключ без назначенного дома уезжает своей карточкой и называется вслух."""
    for src, now_extra, tree_text in (
        ("NOW", "самодельный: значение\n", TREE),
        ("TREE", "", TREE.replace("root:", "самодельный: значение\nroot:")),
    ):
        now = ("bet: null\ntasks: []\n" + now_extra
               + f"END_OF_FILE: live/{D}/NOW.md\n")
        make_repo(now, tree_text)
        ok, out = run(cards.build, D)
        p = os.path.join(cards.ROOT, "panel", ".cards", D, "самодельный.md")
        check(ok and os.path.isfile(p), f"{src}: незнакомый ключ уехал своей карточкой")
        check("БЕЗ НАЗНАЧЕННОГО ДОМА" in out and "самодельный" in out,
              f"{src}: и назван вслух, а не проглочен")
        ok, out = run(cards.check, D)
        check(ok, f"{src}: и собирается обратно ({out.strip().splitlines()[-1][:60]})")


def case_extras_are_compared():
    """Раньше эти ключи не сверялись вовсе — потерять их было нечем поймать."""
    for key, where in (("direction_forecast", "NOW"), ("owner_approved", "TREE")):
        now = (f"bet: null\ntasks: []\ndirection_forecast:\n  status: no_basis\n"
               f"END_OF_FILE: live/{D}/NOW.md\n")
        make_repo(now, TREE)
        run(cards.build, D)
        p = os.path.join(cards.ROOT, "panel", ".cards", D, key + ".md")
        check(os.path.isfile(p), f"{key} ({where}) получил карточку {key}.md")
        t = io.open(p, encoding="utf-8").read()
        io.open(p, "w", encoding="utf-8", newline="").write(t.replace("no_basis", "forecast")
                                                            .replace("2026-01-01", "2026-09-09"))
        ok, msg = run(cards.check, D)
        check(not ok, f"подмена в {key} теперь ловится сверкой")
        os.remove(p)   # пропажа карточки целиком — тоже потеря
        ok, msg = run(cards.check, D)
        check(not ok, f"пропажа карточки {key} ловится сверкой")


def case_abolished_key_is_named():
    """Отменённый схемой ключ не едет — но о нём говорят каждый прогон."""
    now = f"bet: null\ntasks: []\nnext: 'CALL: work/x.md'\nEND_OF_FILE: live/{D}/NOW.md\n"
    make_repo(now, TREE)
    ok, out = run(cards.build, D)
    check(ok and "ОТМЕНЁННЫЙ КЛЮЧ" in out and "next" in out,
          f"отменённый ключ назван: {out.strip().splitlines()[0][:70]}")
    check(not os.path.isfile(os.path.join(cards.ROOT, "panel", ".cards", D, "next.md")),
          "и карточки себе не получил")


def case_two_carriers_one_name():
    """Одно имя в шапке и в теле: раньше выигрывало тело, шапка тухла молча."""
    now = f"bet: null\ntasks:\n- id: t-1\n  route: work\nEND_OF_FILE: live/{D}/NOW.md\n"
    make_repo(now, TREE)
    run(cards.build, D)
    p = os.path.join(cards.ROOT, "panel", ".cards", D, "t-1.md")
    t = io.open(p, encoding="utf-8").read()
    # блок дописывается ДО хвоста, иначе карточка просто ломается на разборе
    t = t.replace("END_OF_FILE:", "## route\nсовсем другое\n\nEND_OF_FILE:")
    io.open(p, "w", encoding="utf-8", newline="").write(t)
    check("route: work" in t and "## route" in t, "имя заведено разом в шапке и в теле")
    ok, msg = run(cards.check, D)
    check(not ok and "два носителя" in msg, f"одно имя в шапке и в теле ловится: {msg.strip()[:70]}")


def case_service_name_in_source():
    """Источник не имеет права занять служебное имя — иначе затрёт метку носителя."""
    now = f"bet: null\ntasks:\n- id: t-1\n  _kind: подделка\nEND_OF_FILE: live/{D}/NOW.md\n"
    make_repo(now, TREE)
    ok, msg = run(cards.build, D)
    check(not ok and "_kind" in msg, f"поле с ведущим _ в источнике останавливает: {msg.strip()[:70]}")


def case_two_readers_agree():
    """Один файл — два читателя. Разошлись — и панель читает не то, что писал osctl."""
    cards.ROOT = REAL_ROOT
    sys.path.insert(0, str(Path(REAL_ROOT)))
    import osctl
    seen = disagree = 0
    for d in sorted(Path(REAL_ROOT, "live").iterdir()):
        folder = d / "cards"
        if not folder.is_dir():
            continue
        for p in sorted(folder.rglob("*.md")):
            seen += 1
            try:
                h1, b1, _ = osctl.read_card(p)
                h2, b2 = cards.read_card(str(p))
            except (SystemExit, Exception) as e:      # noqa: B014 — cards.fail это SystemExit
                disagree += 1
                if disagree == 1:
                    print(f"     не читается: {p.name}: {e}")
                continue
            if h1 != h2 or {k: list(v) for k, v in b1.items()} != {k: list(v) for k, v in b2.items()}:
                disagree += 1
                if disagree == 1:
                    print(f"     первое расхождение: {p.name}")
    check(seen > 0, f"живых карточек найдено: {seen}")
    check(disagree == 0, f"osctl и панель читают их одинаково (расхождений {disagree})")


def case_real_state():
    """Последнее слово — настоящее живое состояние, какое оно сейчас есть."""
    cards.ROOT = REAL_ROOT
    d = "indie-game-development"
    ok, msg = run(cards.build, d)
    check(ok, f"живое состояние строится: {msg.strip()[:80]}")
    ok, msg = run(cards.check, d)
    check(ok, f"живое состояние собирается обратно: {msg.strip()[:110]}")


def main():
    for fn in (case_data_may_use_any_name, case_unknown_key_is_carried_and_named,
               case_extras_are_compared, case_abolished_key_is_named,
               case_two_carriers_one_name, case_service_name_in_source,
               case_two_readers_agree, case_real_state):
        print(f"\n--- {fn.__doc__.splitlines()[0]}")
        try:
            fn()
        finally:
            if cards.ROOT != REAL_ROOT:
                shutil.rmtree(cards.ROOT, ignore_errors=True)
                cards.ROOT = REAL_ROOT
    print(f"\n{'ПРИНЯТО' if not fails else 'НЕ ПРИНЯТО: ' + str(len(fails)) + ' упало'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
