#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Рез: карточки становятся состоянием, источники уходят. Одна транзакция.

Порядок здесь не декоративный — каждый шаг проверяет предыдущий, и ни один
не начинается, пока предыдущий не доказан:

  1. предполётная проверка: копия чиста, чужого в полёте нет;
  2. карточки пересобираются из ПОСЛЕДНЕГО состояния источников;
  3. доказательство: оба читателя видят одно и то же, `check` чист;
  4. правила переводятся на карточки (os2/switchover.py);
  5. `LOG.md` уезжает в `history/LOG-archive-<направление>.md` ЦЕЛИКОМ;
  6. `NOW.md` ужимается до указателя, `TREE.md` удаляется.

Откат — `git revert` того коммита, в который это легло. Источники остаются
в истории Git навсегда: `git show <коммит>:live/<id>/TREE.md`.

ВЫПОЛНЕН ОДИН РАЗ, 2026-08-08. Повторить его нечем и не над чем: источников
больше нет, `osctl migrate` снят вместе с ними, набор правок применён. Файл
остаётся записью того, ЧТО именно было сделано, и отказывается запускаться,
чтобы не выглядеть работающим инструментом.

    python os2/cut.py            # пробный прогон, ничего не меняет
    python os2/cut.py --apply    # рез
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import yaml

for _s in (sys.stdout, sys.stderr):
    _s.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "panel"))
import cards as fmt          # noqa: E402
import osctl                 # noqa: E402

SOURCES = ("NOW.md", "TREE.md", "LOG.md")


class Stop(Exception):
    """Остановка с человеческой причиной."""


def run(*args, cwd=None):
    return subprocess.run(args, cwd=str(cwd or REPO), capture_output=True,
                          text=True, encoding="utf-8", errors="replace")


def directions() -> list:
    return sorted(d.name for d in (REPO / "live").iterdir()
                  if (d / "NOW.md").exists())


def preflight() -> list:
    """Рез поверх чужой незакоммиченной работы — потеря. Проверяется, не считается."""
    problems = []
    # Ищем ЧУЖУЮ работу, а не свой вывод. Правка отслеживаемого файла в live/ —
    # это чужая незакоммиченная нога, и резать поверх неё значит её потерять.
    # Неотслеживаемая папка карточек — вывод самого реза (шаг 2 пересобирает её
    # с --force при каждом прогоне), поэтому она помехой не является.
    st = run("git", "status", "--porcelain", "--untracked-files=no", "live")
    if st.stdout.strip():
        problems.append("отслеживаемые файлы в live/ изменены и не закоммичены — "
                        "чужая нога в полёте:\n    "
                        + "\n    ".join(st.stdout.strip().split("\n")[:5]))
    stray = [l[3:] for l in run("git", "status", "--porcelain", "live").stdout.split("\n")
             if l.startswith("??") and not l.rstrip("/").endswith("/cards")]
    if stray:
        problems.append("в live/ появились неизвестные файлы — разберись до реза:\n    "
                        + "\n    ".join(stray[:5]))
    run("git", "fetch", "-q", "origin")
    n = run("git", "rev-list", "--count", "HEAD..origin/main").stdout.strip()
    if n.isdigit() and int(n) > 0:
        problems.append(f"с origin/main пришло {n} коммитов — сначала влей их")
    return problems


def prove(direction: str) -> list:
    """Карточки читаются одинаково обоими читателями и механически исправны."""
    problems = []
    folder = REPO / "live" / direction / "cards"
    seen = 0
    for p in sorted(folder.rglob("*.md")):
        seen += 1
        try:
            h1, b1, _ = osctl.read_card(p)
            h2, b2 = fmt.read_card(str(p))
        except (SystemExit, osctl.Stop) as e:
            problems.append(f"{p.name}: не читается — {e}")
            continue
        if h1 != h2 or {k: list(v) for k, v in b1.items()} != {k: list(v) for k, v in b2.items()}:
            problems.append(f"{p.name}: два читателя видят разное")
    if not seen:
        problems.append(f"{direction}: карточек нет вообще")
    r = run(sys.executable, "osctl.py", "check", "--direction", direction)
    if r.returncode != 0:
        problems.append(f"{direction}: osctl check не чист — {r.stdout.strip()[:200]}")
    return problems


def archive_log(direction: str, apply: bool) -> str:
    src = REPO / "live" / direction / "LOG.md"
    if not src.exists():
        return "LOG.md уже нет"
    dst = REPO / "live" / direction / "history" / f"LOG-archive-{direction}.md"
    body = src.read_bytes().decode("utf-8")
    lines = len([l for l in body.split("\n") if l.strip()])
    if dst.exists():
        old = dst.read_bytes().decode("utf-8")
        merged = old.rstrip("\n") + "\n\n" + body
        note = f"дописан к существующему архиву ({lines} строк)"
    else:
        merged = body
        note = f"перенесён целиком ({lines} строк)"
    if apply:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(merged.encode("utf-8"))
        if dst.read_bytes().decode("utf-8") != merged:
            raise Stop(f"{dst}: запись не сошлась при чтении обратно")
        src.unlink()
    return f"LOG.md -> history/LOG-archive-{direction}.md, {note}"


def shrink_now(direction: str, apply: bool) -> str:
    p = REPO / "live" / direction / "NOW.md"
    data = yaml.safe_load(p.read_bytes().decode("utf-8"))
    bet = data.get("bet")
    node = bet["node"] if isinstance(bet, dict) and "node" in bet else None
    keep = {}
    if node:
        keep["bet"] = node
    if data.get("track_wip_limit") is not None:
        keep["track_wip_limit"] = data["track_wip_limit"]
    was = len(p.read_bytes().decode("utf-8").split("\n"))
    if apply:
        osctl.write_now(direction, keep)
        back = osctl.read_now(direction)
        if back != keep:
            raise Stop(f"{p}: указатель не сошёлся при чтении обратно")
    return f"NOW.md {was} строк -> указатель {keep or '{}'}"


def drop_tree(direction: str, apply: bool) -> str:
    p = REPO / "live" / direction / "TREE.md"
    if not p.exists():
        return "TREE.md уже нет"
    n = len(p.read_bytes().decode("utf-8").split("\n"))
    if apply:
        p.unlink()
    return f"TREE.md удалён ({n} строк; дерево живёт в карточках через _parent)"


def main() -> int:
    ap = argparse.ArgumentParser(prog="cut", description="карточки становятся состоянием")
    ap.add_argument("--apply", action="store_true", help="без него — пробный прогон")
    a = ap.parse_args()
    mode = "РЕЗ" if a.apply else "ПРОБНЫЙ ПРОГОН"
    print(f"=== {mode} ===\n")

    dirs = directions()
    if not [d for d in dirs if (REPO / "live" / d / "TREE.md").exists()]:
        print("рез уже выполнен: ни у одного направления нет TREE.md.")
        print("  Состояние живёт в карточках; читать и менять его — через osctl.")
        print("  Что именно было сделано — os2/SWITCHOVER.md и этот файл.")
        return 0
    print(f"направлений: {', '.join(dirs)}\n")

    print("1. предполётная проверка")
    bad = preflight()
    for x in bad:
        print("   СТОП: " + x)
    if bad:
        return 1
    print("   копия чиста, входящего нет")

    print("\n2. карточки из последнего состояния источников")
    for d in dirs:
        args = [sys.executable, "osctl.py", "migrate", "--direction", d]
        if a.apply:
            args += ["--apply", "--force"]
        r = run(*args)
        if r.returncode != 0:
            print(f"   СТОП {d}: {(r.stdout + r.stderr).strip()[:300]}")
            return 1
        tail = [l for l in r.stdout.strip().split("\n") if "карточ" in l]
        print(f"   {d}: {tail[-1].strip() if tail else 'ок'}")

    if not a.apply:
        print("\n   (пробный прогон: карточки не записаны, дальше показано намерение)")
    else:
        print("\n3. доказательство: оба читателя видят одно, check чист")
        for d in dirs:
            bad = prove(d)
            for x in bad:
                print(f"   СТОП {d}: {x}")
            if bad:
                return 1
            print(f"   {d}: сходится")

    print("\n4. правила на карточки")
    args = [sys.executable, "os2/switchover.py"]
    args += ["apply", "--in-place"] if a.apply else ["check"]
    r = run(*args)
    if r.returncode != 0:
        # Прогон мог оборваться позже: тогда правила уже переведены, и все якоря
        # пропали разом. Это не поломка, а повтор — но «часть якорей» ею является.
        out = (r.stdout + r.stderr)
        gone = out.count("якорь встречается 0 раз")
        total = len(json.loads((REPO / "os2" / "switchover.json")
                               .read_text(encoding="utf-8"))["edits"])
        if a.apply and gone == total:
            print(f"   правила уже переведены ({total} правок), повтор не нужен")
        else:
            print("   СТОП: " + out.strip()[:400])
            return 1
    else:
        print("   " + [l for l in r.stdout.strip().split("\n") if l.strip()][-1].strip())

    print("\n5-6. источники")
    for d in dirs:
        for fn in (archive_log, shrink_now, drop_tree):
            print(f"   {d}: {fn(d, a.apply)}")

    if not a.apply:
        print("\nПРОБНЫЙ ПРОГОН — ничего не изменено. Резать: добавь --apply")
    else:
        print("\nРЕЗ ВЫПОЛНЕН. Источники остаются в истории Git:")
        print("  git show HEAD~1:live/<направление>/TREE.md")
        print("Откат — git revert коммита с этим резом.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Stop as e:
        print(f"ОШИБКА: {e}", file=sys.stderr)
        sys.exit(1)
