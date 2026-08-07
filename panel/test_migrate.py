# -*- coding: utf-8 -*-
"""Самопроверка команды переезда. Пишет только во временную папку;
источники (live/) обязаны остаться байт в байт теми же.

    python panel/test_migrate.py
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OSCTL = ROOT / "osctl.py"
D = "indie-game-development"
SOURCES = ("NOW.md", "TREE.md", "LOG.md")

fails = []


def check(ok, msg):
    print(("OK   " if ok else "FAIL ") + msg)
    if not ok:
        fails.append(msg)


def run(*args):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    return subprocess.run([sys.executable, str(OSCTL), *args], cwd=str(ROOT),
                          capture_output=True, text=True, encoding="utf-8",
                          errors="replace", env=env)


def main():
    live = ROOT / "live" / D
    before = {n: (live / n).read_bytes() for n in SOURCES if (live / n).exists()}
    tmp = Path(tempfile.mkdtemp(prefix="osctl-migrate-")) / "cards"

    # --- пробный прогон ничего не пишет
    r = run("migrate", "--direction", D, "--out", str(tmp))
    check(r.returncode == 0, "пробный прогон завершается кодом 0")
    check("ПРОБНЫЙ ПРОГОН" in r.stdout, "пробный прогон назван явно")
    check("СОВПАДАЕТ" in r.stdout, "обратная сборка доказана ДО записи")
    check(not tmp.exists(), "пробный прогон не создал папку")

    # --- запись
    r = run("migrate", "--direction", D, "--out", str(tmp), "--apply")
    check(r.returncode == 0 and tmp.is_dir(), "с --apply карточки записаны")
    files = sorted(tmp.glob("*.md"))
    check(len(files) > 10, f"карточек записано {len(files)}")

    # --- у каждой цели имя, иначе закон 4 нарушен
    import yaml
    nodes, no_label, with_journal = 0, [], 0
    for p in files:
        text = p.read_text(encoding="utf-8")
        head = yaml.safe_load(text.split("---", 2)[1])
        if head.get("kind") == "node":
            nodes += 1
            if not head.get("label"):
                no_label.append(head.get("id"))
        if "## журнал" in text:
            with_journal += 1
        check_tail = text.rstrip().endswith(p.name)
        if not check_tail:
            fails.append(f"{p.name}: нет хвоста END_OF_FILE")
    check(nodes > 0, f"узлы перенесены: {nodes}")
    check(not no_label, f"у всех целей есть короткое имя ({no_label[:3]})")
    check(with_journal > 0, f"журнал засеян у {with_journal} карточек")

    # --- журнал новым вверх
    jp = next((p for p in files if "## журнал" in p.read_text(encoding="utf-8")), None)
    if jp:
        body = jp.read_text(encoding="utf-8").split("## журнал", 1)[1]
        dates = [l.split(" ")[0] for l in body.split("\n")
                 if l[:4].isdigit() and l[4] == "-"]
        check(dates == sorted(dates, reverse=True),
              f"журнал {jp.stem}: новое сверху ({dates[:3]})")

    # --- повторный --apply без --force отказывает
    r = run("migrate", "--direction", D, "--out", str(tmp), "--apply")
    check(r.returncode == 1 and "уже есть" in r.stderr,
          "повторная запись поверх без --force отказывает")

    r = run("migrate", "--direction", D, "--out", str(tmp), "--apply", "--force")
    check(r.returncode == 0, "с --force перезапись проходит")

    # --- ГЛАВНОЕ: источники не тронуты
    for n, b in before.items():
        check((live / n).read_bytes() == b, f"источник {n} не изменился ни на байт")

    # --- на записанных карточках check чист
    r = run("check", "--direction", D, "--cards", str(tmp))
    check(r.returncode == 0 and "механических проблем нет" in r.stdout,
          "check на перенесённых карточках чист")

    shutil.rmtree(tmp.parent, ignore_errors=True)
    print(f"\n{'ПРИНЯТО' if not fails else 'НЕ ПРИНЯТО: ' + str(len(fails)) + ' упало'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
