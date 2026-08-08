#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Перевод правил `os/**` на карточки: набор правок как ДАННЫЕ плюс применятель,
который никогда не догадывается.

Зачем отдельно от самих правил. Между подготовкой правок и резом ноги продолжают
идти: если правила скажут «пиши в карточки», пока главные ещё `NOW.md`/`TREE.md`,
первая же нога испортит состояние. Поэтому правки лежат здесь и применяются
одним движением вместе с резом.

Почему набор правок — это пары «точный старый текст → новый», а не патч по
номерам строк: за время лежания правила могли поменяться чужой ногой. Пара
привязана к ТЕКСТУ, а не к месту, и если текст изменился — применятель
останавливается и называет место, вместо того чтобы записать наугад.

    python os2/switchover.py check              # все ли якоря на месте
    python os2/switchover.py apply --out <куда> # применить в КОПИЮ и показать разницу
    python os2/switchover.py apply --in-place   # только на волне 4, вместе с резом
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    _s.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
EDITS = Path(__file__).resolve().parent / "switchover.json"

# Бюджеты из AGENTS.md. Превышение — отказ, а не предупреждение.
BUDGETS = {"os/KERNEL.md": 1500}
PLAY_BUDGET = 600

# Файлы состояния, которых после переезда не станет. Оставшееся УКАЗАНИЕ ПИСАТЬ
# в них — это дефект набора правок, и проверка обязана его назвать.
GONE = ("TREE.md", "LOG.md")


class Stop(Exception):
    """Остановка с человеческой причиной. Никогда не догадка."""


def load() -> list:
    if not EDITS.exists():
        raise Stop(f"нет набора правок: {EDITS}")
    data = json.loads(EDITS.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema") != "os2.switchover.v1":
        raise Stop(f"{EDITS}: не тот формат, ожидается schema=os2.switchover.v1")
    edits = data.get("edits")
    if not isinstance(edits, list) or not edits:
        raise Stop(f"{EDITS}: пустой набор правок")
    for i, e in enumerate(edits):
        for k in ("file", "old", "new", "why"):
            if not isinstance(e.get(k), str) or not e[k]:
                raise Stop(f"правка #{i}: нет поля {k}")
        if e["old"] == e["new"]:
            raise Stop(f"правка #{i} ({e['file']}): старое и новое совпадают")
    return edits


def words(text: str) -> int:
    return len(text.split())


def read_norm(p: Path):
    """Читает и возвращает (текст с LF, какие концы строк были).
    Правила лежат вперемешку: 42 файла в CRLF, 10 в LF. Якоря пишутся с LF,
    поэтому для сверки текст приводится к LF, а при записи концы ВОЗВРАЩАЮТСЯ
    свои. Иначе правка одной строки переписала бы весь файл."""
    raw = p.read_bytes().decode("utf-8")
    eol = "\r\n" if "\r\n" in raw else "\n"
    return raw.replace("\r\n", "\n"), eol


def write_norm(p: Path, text: str, eol: str) -> None:
    p.write_bytes(text.replace("\n", eol).encode("utf-8"))


def stage_outside(root: Path, edits: list) -> None:
    """Набор трогает и файлы вне `os/` — например AGENTS.md с тем же бюджетом.
    В пробную копию они кладутся поимённо, иначе якорь там просто не найдётся."""
    for rel in sorted({e["file"] for e in edits if not e["file"].startswith("os/")}):
        dst = root / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / rel, dst)


def anchors(root: Path, edits: list) -> list:
    """Каждый якорь обязан встречаться РОВНО ОДИН раз. Ноль — текст уехал;
    больше одного — неизвестно, какое из мест имелось в виду."""
    problems = []
    seen = {}
    for i, e in enumerate(edits):
        p = root / e["file"]
        if not p.exists():
            problems.append(f"#{i} {e['file']}: файла нет")
            continue
        if e["file"] not in seen:
            seen[e["file"]] = read_norm(p)[0]
        n = seen[e["file"]].count(e["old"])
        if n != 1:
            head = " ".join(e["old"].split())[:70]
            problems.append(f"#{i} {e['file']}: якорь встречается {n} раз — «{head}…»")
    return problems


def apply_to(root: Path, edits: list) -> dict:
    """Применяет по одному, каждый раз перечитывая уже применённое: две правки
    в одном файле не имеют права наступать друг на друга."""
    buf: dict = {}
    eols: dict = {}
    for i, e in enumerate(edits):
        p = root / e["file"]
        if e["file"] not in buf:
            buf[e["file"]], eols[e["file"]] = read_norm(p)
        text = buf[e["file"]]
        n = text.count(e["old"])
        if n != 1:
            raise Stop(f"правка #{i} в {e['file']}: якорь встречается {n} раз "
                       "после предыдущих правок — набор сам себе противоречит")
        buf[e["file"]] = text.replace(e["old"], e["new"], 1)
    for rel, text in buf.items():
        write_norm(root / rel, text, eols[rel])   # концы строк остаются своими
    return buf


def audit(root: Path, touched: dict) -> list:
    """Механические факты о получившихся правилах. Смысл не судит."""
    problems = []
    for rel, text in sorted(touched.items()):
        tail = f"END_OF_FILE: {rel}"
        if not text.rstrip().endswith(tail):
            problems.append(f"{rel}: пропал хвост «{tail}»")
        budget = BUDGETS.get(rel) or (PLAY_BUDGET if rel.startswith("os/plays/") else 0)
        if budget:
            n = words(text)
            if n > budget:
                problems.append(f"{rel}: {n} слов при бюджете {budget}")
        for line_no, line in enumerate(text.split("\n"), 1):
            low = line.strip()
            if low.startswith("Writes:") and any(g in low for g in GONE):
                problems.append(f"{rel}:{line_no}: строка Writes: всё ещё называет "
                                f"исчезающий файл — {low[:80]}")
    return problems


def cmd_check(a) -> int:
    edits = load()
    files = sorted({e["file"] for e in edits})
    print(f"правок: {len(edits)} в {len(files)} файлах")
    problems = anchors(REPO, edits)
    if problems:
        print(f"\nЯКОРЯ НЕ СОШЛИСЬ: {len(problems)}")
        for x in problems:
            print("  " + x)
        print("\n  Правила изменились с тех пор, как набор составлялся.")
        print("  Это ожидаемо при параллельных ногах: перечитай места и поправь якоря.")
        return 1
    print("все якоря на месте, ровно по одному вхождению")

    tmp = Path(a.tmp) if a.tmp else REPO / ".switchover-probe"
    shutil.rmtree(tmp, ignore_errors=True)
    (tmp / "os").mkdir(parents=True)
    shutil.copytree(REPO / "os", tmp / "os", dirs_exist_ok=True)
    stage_outside(tmp, edits)
    try:
        touched = apply_to(tmp, edits)
        bad = audit(tmp, touched)
        for rel in sorted(touched):
            budget = BUDGETS.get(rel) or (PLAY_BUDGET if rel.startswith("os/plays/") else 0)
            before, after = words(read_norm(REPO / rel)[0]), words(touched[rel])
            mark = f"  бюджет {budget}" if budget else ""
            print(f"  {rel:34} {before:5} → {after:5} слов{mark}")
        if bad:
            print(f"\nПОСЛЕ ПРИМЕНЕНИЯ ОСТАЛИСЬ ПРОБЛЕМЫ: {len(bad)}")
            for x in bad:
                print("  " + x)
            return 1
        print("\nпробное применение прошло: хвосты целы, бюджеты соблюдены")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def cmd_apply(a) -> int:
    edits = load()
    if not a.in_place and not a.out:
        raise Stop("нужно --out <папка> или --in-place")
    root = REPO
    if not a.in_place:
        root = Path(a.out)
        shutil.rmtree(root, ignore_errors=True)
        (root / "os").mkdir(parents=True)
        shutil.copytree(REPO / "os", root / "os", dirs_exist_ok=True)
        stage_outside(root, edits)
    problems = anchors(root, edits)
    if problems:
        for x in problems:
            print("  " + x)
        raise Stop(f"{len(problems)} якорей не сошлись — ничего не записано")
    touched = apply_to(root, edits)
    bad = audit(root, touched)
    print(f"применено правок: {len(edits)} в {len(touched)} файлах -> {root}")
    for x in bad:
        print("  ПРОБЛЕМА: " + x)
    return 1 if bad else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="switchover",
                                 description="перевод правил os/** на карточки")
    sub = ap.add_subparsers(dest="cmd", required=True)
    q = sub.add_parser("check", help="сошлись ли якоря и что получится")
    q.add_argument("--tmp"); q.set_defaults(fn=cmd_check)
    q = sub.add_parser("apply", help="применить набор")
    q.add_argument("--out"); q.add_argument("--in-place", action="store_true", dest="in_place")
    q.set_defaults(fn=cmd_apply)
    a = ap.parse_args(argv)
    try:
        return a.fn(a)
    except Stop as e:
        print(f"ОШИБКА: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
