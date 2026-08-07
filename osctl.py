#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""osctl — состояние workflow меняется только этими командами.

Запуск одинаков на Windows и macOS:
    python osctl.py slot list
    python osctl.py slot claim --slot 2 --for c-exec-...-001 --stage BUILD
    python osctl.py slot release --slot 2 --for c-exec-...-001 --stage BUILD

Доска аренд лежит ВНЕ всех рабочих копий и вне .git — иначе её переписывает
любое слияние или смена ветки (так уже было в GasCoopGame до 2026-07-30).
Путь: ~/.osctl/slots/<направление>.json, переопределяется OSCTL_STATE_DIR.

Правила спеки: os2/CONCEPT.md §6.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import yaml

SCHEMA = "osctl.slot-state.v1"
LIFECYCLES = ("AVAILABLE", "CLAIMED")
LEASE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*:[A-Za-z0-9][A-Za-z0-9._-]*$")
LOCK_DEADLINE = 10.0
MARKER = ".osctl-here.yaml"

REPO = Path(__file__).resolve().parent


class Stop(Exception):
    """Остановка с человеческой причиной. Никогда не догадка."""


def state_dir() -> Path:
    return Path(os.environ.get("OSCTL_STATE_DIR") or (Path.home() / ".osctl"))


def ledger_path(direction: str) -> Path:
    return state_dir() / "slots" / f"{direction}.json"


# ---------------------------------------------------------------- направление

def read_marker(start: Path | None = None) -> dict:
    """Направление берётся из метки в корне рабочей копии, а не из имени папки."""
    p = (start or REPO) / MARKER
    if not p.exists():
        return {}
    out = {}
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def resolve_direction(explicit: str | None) -> str:
    if explicit:
        return explicit
    m = read_marker()
    if m.get("direction"):
        return m["direction"]
    raise Stop(
        f"направление не определено: нет {MARKER} в {REPO} и не передан --direction.\n"
        "  Угадывать по имени папки нельзя — неверная догадка пишет в чужое состояние.\n"
        f"  Создай метку: python osctl.py here set --direction <id> [--slot N]"
    )


# ---------------------------------------------------------------------- ledger

def validate(data: object, path: Path) -> dict:
    if not isinstance(data, dict):
        raise Stop(f"{path}: корень не объект")
    if data.get("schema") != SCHEMA:
        raise Stop(
            f"{path}: схема {data.get('schema')!r}, ожидается {SCHEMA!r}.\n"
            "  Скорее всего твоя рабочая копия устарела — обнови её, а не доску."
        )
    slots = data.get("slots")
    if not isinstance(slots, dict) or not slots:
        raise Stop(f"{path}: нет слотов")
    for name, rec in slots.items():
        if not isinstance(rec, dict):
            raise Stop(f"{path}: слот {name} не объект")
        if rec.get("lifecycle") not in LIFECYCLES:
            raise Stop(f"{path}: слот {name}: lifecycle {rec.get('lifecycle')!r}")
        lease = rec.get("lease")
        if rec["lifecycle"] == "AVAILABLE" and lease != "none":
            raise Stop(f"{path}: слот {name} свободен, но аренда {lease!r}")
        if rec["lifecycle"] == "CLAIMED" and not (isinstance(lease, str) and LEASE_RE.match(lease)):
            raise Stop(f"{path}: слот {name} занят, но аренда {lease!r} не вида <наряд>:<стадия>")
    return data


def read_ledger(direction: str) -> dict:
    p = ledger_path(direction)
    if not p.exists():
        raise Stop(
            f"доски слотов нет: {p}\n"
            f"  Создай один раз: python osctl.py slot init --direction {direction} --count 4"
        )
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise Stop(f"{p}: не разбирается — {e}") from None
    return validate(data, p)


def write_ledger(direction: str, data: dict) -> None:
    """Временный файл, атомарная подмена, чтение обратно и сверка."""
    p = ledger_path(direction)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".json.tmp")
    body = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    tmp.write_text(body, encoding="utf-8")
    tmp.replace(p)
    back = json.loads(p.read_text(encoding="utf-8"))
    if back != data:
        raise Stop(f"{p}: запись не сошлась при чтении обратно — состояние под вопросом")


class lock:
    """Межпроцессный замок через создание файла: работает и на Windows, и на Mac."""

    def __init__(self, direction: str):
        self.path = ledger_path(direction).with_suffix(".json.lock")

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        deadline = time.time() + LOCK_DEADLINE
        while True:
            try:
                fd = os.open(str(self.path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(fd, f"{os.getpid()} {time.strftime('%H:%M:%S')}\n".encode())
                os.close(fd)
                return self
            except FileExistsError:
                if time.time() > deadline:
                    raise Stop(
                        f"доска занята дольше {LOCK_DEADLINE:.0f} с: {self.path}\n"
                        "  Если ты уверен, что никто не пишет — удали этот файл."
                    ) from None
                time.sleep(0.05)

    def __exit__(self, *exc):
        try:
            self.path.unlink()
        except FileNotFoundError:
            pass


# -------------------------------------------------------------------------- git

def git(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=str(cwd or REPO), capture_output=True,
                          text=True, encoding="utf-8", errors="replace")


def slot_branch(direction: str, slot: str) -> str:
    return f"slot/{direction}/{slot}"


def slot_facts(direction: str, slot: str) -> dict:
    """Только измеренное: где копия, на какой ветке, чиста ли, каков разрыв."""
    br = slot_branch(direction, slot)
    exists = git("rev-parse", "--verify", "--quiet", br).returncode == 0
    facts = {"branch": br, "branch_exists": exists, "worktree": None,
             "clean": None, "ahead": None, "published": None}
    if not exists:
        return facts
    for ln in git("worktree", "list", "--porcelain").stdout.split("\n"):
        if ln.startswith("worktree "):
            cur = ln[9:].strip()
        elif ln.strip() == f"branch refs/heads/{br}":
            facts["worktree"] = cur
    if facts["worktree"]:
        st = git("status", "--porcelain", cwd=Path(facts["worktree"]))
        facts["clean"] = st.returncode == 0 and not st.stdout.strip()
    n = git("rev-list", "--count", f"origin/main..{br}").stdout.strip()
    facts["ahead"] = int(n) if n.isdigit() else None
    facts["published"] = git("merge-base", "--is-ancestor", br, "origin/main").returncode == 0
    return facts


# ---------------------------------------------------------------------- команды

def cmd_slot_init(a) -> int:
    direction = resolve_direction(a.direction)
    p = ledger_path(direction)
    if p.exists() and not a.force:
        raise Stop(f"доска уже есть: {p}\n  Перезаписать: добавь --force")
    data = {"schema": SCHEMA,
            "slots": {str(i): {"lifecycle": "AVAILABLE", "lease": "none"}
                      for i in range(1, a.count + 1)}}
    with lock(direction):
        write_ledger(direction, data)
    print(f"доска создана: {p}")
    print(f"слотов: {a.count}, все свободны")
    return 0


def cmd_slot_list(a) -> int:
    direction = resolve_direction(a.direction)
    data = read_ledger(direction)
    rows = []
    for name, rec in sorted(data["slots"].items(), key=lambda kv: int(kv[0])):
        f = slot_facts(direction, name)
        rows.append({"slot": name, "lifecycle": rec["lifecycle"], "lease": rec["lease"],
                     "call": rec["lease"].rsplit(":", 1)[0] if rec["lease"] != "none" else None,
                     "stage": rec["lease"].rsplit(":", 1)[1] if rec["lease"] != "none" else None,
                     **f})
    if a.json:
        print(json.dumps({"direction": direction, "ledger": str(ledger_path(direction)),
                          "slots": rows}, ensure_ascii=False, indent=2))
        return 0
    print(f"направление: {direction}")
    print(f"доска: {ledger_path(direction)}\n")
    for r in rows:
        state = "свободен" if r["lifecycle"] == "AVAILABLE" else f"занят · {r['call']} · {r['stage']}"
        wt = r["worktree"] or "копии нет"
        extra = ""
        if r["ahead"]:
            extra = f" · не опубликовано: {r['ahead']}"
        if r["clean"] is False:
            extra += " · копия грязная"
        print(f"  слот {r['slot']}: {state}")
        print(f"    {wt}{extra}")
    return 0


def cmd_slot_claim(a) -> int:
    direction = resolve_direction(a.direction)
    lease = f"{a.for_}:{a.stage}"
    if not LEASE_RE.match(lease):
        raise Stop(f"аренда {lease!r} не вида <наряд>:<стадия> — двоеточий быть не должно")
    with lock(direction):
        data = read_ledger(direction)          # перечитываем ПОД замком
        slots = data["slots"]
        if a.slot not in slots:
            raise Stop(f"слота {a.slot} нет. Есть: {', '.join(sorted(slots))}")
        # тот же наряд уже взят где-то ещё — вот ради чего всё и затевалось
        for name, rec in slots.items():
            if rec["lifecycle"] == "CLAIMED" and rec["lease"].rsplit(":", 1)[0] == a.for_:
                raise Stop(
                    f"наряд {a.for_} уже взят слотом {name} (аренда {rec['lease']}).\n"
                    "  Двое над одной работой — это то, что мы и не даём. Разберись, чья она."
                )
        rec = slots[a.slot]
        if rec["lifecycle"] != "AVAILABLE":
            raise Stop(f"слот {a.slot} занят: {rec['lease']}")
        f = slot_facts(direction, a.slot)
        if f["worktree"] and f["clean"] is False:
            raise Stop(f"копия слота {a.slot} грязная: {f['worktree']}\n  Прибери её до захвата.")
        slots[a.slot] = {"lifecycle": "CLAIMED", "lease": lease}
        write_ledger(direction, data)
    print(f"слот {a.slot} захвачен под {a.for_} · стадия {a.stage}")
    return 0


def cmd_slot_release(a) -> int:
    direction = resolve_direction(a.direction)
    lease = f"{a.for_}:{a.stage}"
    with lock(direction):
        data = read_ledger(direction)
        slots = data["slots"]
        if a.slot not in slots:
            raise Stop(f"слота {a.slot} нет")
        rec = slots[a.slot]
        if rec["lifecycle"] != "CLAIMED":
            raise Stop(f"слот {a.slot} и так свободен")
        if rec["lease"] != lease:
            raise Stop(f"аренда не совпадает: в доске {rec['lease']!r}, предъявлено {lease!r}")
        f = slot_facts(direction, a.slot)
        if f["worktree"] and f["clean"] is False:
            raise Stop(f"копия слота {a.slot} грязная — сначала закоммить или убери")
        # ГЛАВНОЕ отличие от обкатанной версии: публикация проверяется, а не предписывается
        if f["branch_exists"] and not f["published"] and not a.force:
            raise Stop(
                f"работа слота {a.slot} НЕ опубликована: {f['ahead']} коммитов ветки {f['branch']}\n"
                f"  нет в origin/main. Освободить слот сейчас — похоронить их.\n"
                f"  Опубликуй, либо, если работа не нужна, добавь --force."
            )
        # ветка возвращается на базу тем же действием: иначе мёртвый корень остаётся
        if f["branch_exists"] and f["worktree"]:
            r = git("reset", "--hard", "origin/main", cwd=Path(f["worktree"]))
            if r.returncode != 0:
                raise Stop(f"не удалось вернуть ветку слота на origin/main: {r.stderr.strip()[:200]}")
        slots[a.slot] = {"lifecycle": "AVAILABLE", "lease": "none"}
        write_ledger(direction, data)
    print(f"слот {a.slot} освобождён, ветка возвращена на origin/main")
    return 0


def cmd_slot_create(a) -> int:
    """Рабочая копия слота от origin/main плюс метка направления в её корне."""
    direction = resolve_direction(a.direction)
    read_ledger(direction)                      # доска должна существовать
    root = Path(a.root or (Path(REPO).parent.parent / "workflow-slots"))
    path = root / direction / f"slot-{a.slot}"
    br = slot_branch(direction, a.slot)
    if path.exists():
        raise Stop(f"копия уже есть: {path}")
    git("fetch", "origin", "--quiet")
    exists = git("rev-parse", "--verify", "--quiet", br).returncode == 0
    args = ["worktree", "add", str(path)] + ([br] if exists else ["-b", br, "origin/main"])
    r = git(*args)
    if r.returncode != 0:
        raise Stop(f"не удалось создать копию: {(r.stderr or r.stdout).strip()[:300]}")
    marker = path / MARKER
    marker.write_text(f"direction: {direction}\nslot: {a.slot}\n", encoding="utf-8")
    print(f"слот {a.slot}: копия {path}")
    print(f"  ветка {br}, метка {MARKER} на месте")
    return 0



# ------------------------------------------------------------------- карточки

CARD_KINDS = ("bet", "node", "task", "call", "issue", "question", "decision")
JOURNAL = "журнал"
JOURNAL_CEILING = 20
HEAD_LIMIT = 120


def cards_dir(direction: str, override: str | None = None) -> Path:
    return Path(override) if override else (REPO / "live" / direction / "cards")


def card_path(direction: str, cid: str, override: str | None = None) -> Path:
    return cards_dir(direction, override) / f"{cid}.md"


def read_card(path: Path):
    """Шапка — yaml между первой и второй ---; тело режется по строкам '## '.
    Никакого другого разбора: закон 2."""
    if not path.exists():
        raise Stop(f"карточки нет: {path}")
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise Stop(f"{path.name}: нет шапки между --- и ---")
    try:
        head = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        raise Stop(f"{path.name}: шапка не разбирается — {e}") from None
    if not isinstance(head, dict):
        raise Stop(f"{path.name}: шапка не отображение")
    blocks, order, cur = {}, [], None
    for line in parts[2].split(chr(10)):
        if line.startswith("## "):
            cur = line[3:].strip()
            blocks[cur] = []
            order.append(cur)
        elif line.startswith("END_OF_FILE:"):
            cur = None
        elif cur is not None:
            blocks[cur].append(line)
    for k in blocks:
        while blocks[k] and blocks[k][-1] == "":
            blocks[k].pop()
    return head, blocks, order


def write_card(direction: str, cid: str, head: dict, blocks: dict, order: list,
               override: str | None = None) -> None:
    """Атомарно: временный файл, подмена, чтение обратно и сверка."""
    for k, v in head.items():
        if isinstance(v, str) and (len(v) > HEAD_LIMIT or chr(10) in v):
            raise Stop(f"{cid}: поле {k} длиннее {HEAD_LIMIT} или многострочное — ему место в теле")
    path = card_path(direction, cid, override)
    path.parent.mkdir(parents=True, exist_ok=True)
    body = "".join(
        f"## {name}{chr(10)}" + chr(10).join(blocks.get(name) or []) + chr(10) + chr(10)
        for name in order
    )
    rel = str(path.relative_to(REPO)).replace("\\", "/") if str(path).startswith(str(REPO)) else str(path)
    text = ("---" + chr(10)
            + yaml.safe_dump(head, sort_keys=False, allow_unicode=True, default_flow_style=False)
            + "---" + chr(10) + chr(10) + body
            + f"END_OF_FILE: {rel}" + chr(10))
    tmp = path.with_suffix(".md.tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)
    back = path.read_text(encoding="utf-8")
    if back != text:
        raise Stop(f"{cid}: запись не сошлась при чтении обратно")


def cmd_card_show(a) -> int:
    direction = resolve_direction(a.direction)
    head, blocks, order = read_card(card_path(direction, a.id, a.cards))
    if a.json:
        print(json.dumps({"head": head, "blocks": {k: chr(10).join(v) for k, v in blocks.items()},
                          "order": order}, ensure_ascii=False, indent=2, default=str))
        return 0
    for k, v in head.items():
        print(f"{k}: {v}")
    for name in order:
        print(f"{chr(10)}## {name}")
        print(chr(10).join(blocks[name])[:600])
    return 0


def cmd_card_set(a) -> int:
    """Значение приносится целиком. Команда никогда не правит кусок текста."""
    direction = resolve_direction(a.direction)
    path = card_path(direction, a.id, a.cards)
    head, blocks, order = read_card(path)
    if a.field in ("id", "kind"):
        raise Stop(f"{a.field} не меняется командой set — это опора карточки")
    if len(a.value) > HEAD_LIMIT or chr(10) in a.value:
        raise Stop(f"значение длиннее {HEAD_LIMIT} символов — это блок тела, а не поле шапки")
    head[a.field] = yaml.safe_load(a.value) if a.value not in ("", "null") else None
    write_card(direction, a.id, head, blocks, order, a.cards)
    print(f"{a.id}: {a.field} = {head[a.field]!r}")
    return 0


def cmd_card_block(a) -> int:
    direction = resolve_direction(a.direction)
    path = card_path(direction, a.id, a.cards)
    head, blocks, order = read_card(path)
    if a.name == JOURNAL:
        raise Stop(f"«{JOURNAL}» пишется только командой log add")
    if any(l.startswith("## ") for l in a.text.split(chr(10))):
        raise Stop("в тексте есть строка, начинающаяся с '## ' — она разрежет карточку")
    blocks[a.name] = a.text.split(chr(10))
    if a.name not in order:
        order.append(a.name)
    write_card(direction, a.id, head, blocks, order, a.cards)
    print(f"{a.id}: блок «{a.name}» переписан целиком, {len(blocks[a.name])} строк")
    return 0


def cmd_log_add(a) -> int:
    """Порядок записи знает команда, а не тот, кто её зовёт. Новое — сверху."""
    direction = resolve_direction(a.direction)
    path = card_path(direction, a.id, a.cards)
    head, blocks, order = read_card(path)
    date = a.date or __import__("datetime").date.today().isoformat()
    text = " ".join(a.text.split())
    if not text:
        raise Stop("пустая запись журнала")
    line = f"{date} · {text}"
    if a.history:
        line += f" · history/{a.history}" if not a.history.startswith("history/") else f" · {a.history}"
    lines = blocks.get(JOURNAL) or []
    if line in lines:
        raise Stop("такая запись уже есть — журнал не дублирует")
    lines.insert(0, line)
    blocks[JOURNAL] = lines
    if JOURNAL not in order:
        order.append(JOURNAL)
    write_card(direction, a.id, head, blocks, order, a.cards)
    note = f"  потолок {JOURNAL_CEILING} превышен: {len(lines)} строк — пора закрывать или чистить" \
        if len(lines) > JOURNAL_CEILING else ""
    print(f"{a.id}: записано в журнал, всего {len(lines)}")
    if note:
        print(note)
    return 0


def cmd_find(a) -> int:
    direction = resolve_direction(a.direction)
    d = cards_dir(direction, a.cards)
    if not d.is_dir():
        raise Stop(f"папки карточек нет: {d}")
    hits = 0
    for p in sorted(d.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        if a.text.lower() in text.lower():
            hits += 1
            for i, line in enumerate(text.split(chr(10)), 1):
                if a.text.lower() in line.lower():
                    print(f"{p.stem}:{i}: {line.strip()[:100]}")
                    break
    print(f"{chr(10)}найдено карточек: {hits}")
    return 0


def cmd_check(a) -> int:
    """Только механические факты. Ничего не оценивает и не судит смысл."""
    direction = resolve_direction(a.direction)
    d = cards_dir(direction, a.cards)
    if not d.is_dir():
        raise Stop(f"папки карточек нет: {d}")
    problems, seen, total = [], {}, 0
    for p in sorted(d.glob("*.md")):
        total += 1
        try:
            head, blocks, _ = read_card(p)
        except Stop as e:
            problems.append(f"{p.name}: {e}")
            continue
        cid = str(head.get("id"))
        if cid != p.stem:
            problems.append(f"{p.name}: id {cid!r} не совпадает с именем файла")
        if cid in seen:
            problems.append(f"{p.name}: id повторяется, уже был в {seen[cid]}")
        seen[cid] = p.name
        if head.get("kind") not in CARD_KINDS:
            problems.append(f"{p.name}: kind {head.get('kind')!r} не из {list(CARD_KINDS)}")
        if not p.read_text(encoding="utf-8").rstrip().endswith(f"{p.name}"):
            problems.append(f"{p.name}: нет хвоста END_OF_FILE")
        for k, v in head.items():
            if isinstance(v, str) and (len(v) > HEAD_LIMIT or chr(10) in v):
                problems.append(f"{p.name}: поле {k} длинное — ему место в теле")
        j = blocks.get(JOURNAL) or []
        if len(j) > JOURNAL_CEILING:
            problems.append(f"{p.name}: журнал {len(j)} строк, потолок {JOURNAL_CEILING}")
        if head.get("kind") == "node" and not head.get("label"):
            problems.append(f"{p.name}: у цели нет короткого имени (label)")
    print(f"карточек: {total}")
    if not problems:
        print("механических проблем нет")
        return 0
    print(f"проблем: {len(problems)}")
    for x in problems:
        print("  " + x)
    return 1


def cmd_here_set(a) -> int:
    p = REPO / MARKER
    lines = [f"direction: {a.direction}"]
    if a.slot:
        lines.append(f"slot: {a.slot}")
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"метка записана: {p}")
    for ln in lines:
        print("  " + ln)
    return 0


def cmd_here_show(a) -> int:
    m = read_marker()
    if not m:
        raise Stop(f"метки нет: {REPO / MARKER}")
    print(json.dumps(m, ensure_ascii=False, indent=2) if a.json
          else "\n".join(f"{k}: {v}" for k, v in m.items()))
    return 0


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="osctl", description="состояние меняется только этими командами")
    sub = ap.add_subparsers(dest="noun", required=True)

    slot = sub.add_parser("slot").add_subparsers(dest="verb", required=True)

    p = slot.add_parser("init", help="создать доску слотов один раз")
    p.add_argument("--direction"); p.add_argument("--count", type=int, default=4)
    p.add_argument("--force", action="store_true"); p.set_defaults(fn=cmd_slot_init)

    p = slot.add_parser("list", help="что с каждым слотом прямо сейчас")
    p.add_argument("--direction"); p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_slot_list)

    p = slot.add_parser("create", help="сделать рабочую копию слота от origin/main")
    p.add_argument("--slot", required=True); p.add_argument("--direction")
    p.add_argument("--root", help="куда класть, по умолчанию ../workflow-slots")
    p.set_defaults(fn=cmd_slot_create)

    p = slot.add_parser("claim", help="взять слот под наряд")
    p.add_argument("--slot", required=True); p.add_argument("--for", dest="for_", required=True)
    p.add_argument("--stage", required=True); p.add_argument("--direction")
    p.set_defaults(fn=cmd_slot_claim)

    p = slot.add_parser("release", help="освободить слот; требует опубликованной работы")
    p.add_argument("--slot", required=True); p.add_argument("--for", dest="for_", required=True)
    p.add_argument("--stage", required=True); p.add_argument("--direction")
    p.add_argument("--force", action="store_true", help="выбросить неопубликованную работу")
    p.set_defaults(fn=cmd_slot_release)

    card = sub.add_parser("card").add_subparsers(dest="verb", required=True)
    for name, fn, extra in (("show", cmd_card_show, "show"), ("set", cmd_card_set, "set"),
                            ("block", cmd_card_block, "block")):
        q = card.add_parser(name)
        q.add_argument("--id", required=True)
        q.add_argument("--direction")
        q.add_argument("--cards", help="папка карточек, по умолчанию live/<направление>/cards")
        if extra == "show":
            q.add_argument("--json", action="store_true")
        if extra == "set":
            q.add_argument("--field", required=True)
            q.add_argument("--value", required=True)
        if extra == "block":
            q.add_argument("--name", required=True)
            q.add_argument("--text", required=True)
        q.set_defaults(fn=fn)

    log = sub.add_parser("log").add_subparsers(dest="verb", required=True)
    q = log.add_parser("add", help="строка в журнал сущности; порядок знает команда")
    q.add_argument("--id", required=True); q.add_argument("--text", required=True)
    q.add_argument("--history"); q.add_argument("--date"); q.add_argument("--direction")
    q.add_argument("--cards"); q.set_defaults(fn=cmd_log_add)

    q = sub.add_parser("find", help="поиск по карточкам")
    q.add_argument("--text", required=True); q.add_argument("--direction")
    q.add_argument("--cards"); q.set_defaults(fn=cmd_find)

    q = sub.add_parser("check", help="механические факты о карточках, без оценок")
    q.add_argument("--direction"); q.add_argument("--cards"); q.set_defaults(fn=cmd_check)

    here = sub.add_parser("here").add_subparsers(dest="verb", required=True)
    p = here.add_parser("set", help="пометить рабочую копию направлением")
    p.add_argument("--direction", required=True); p.add_argument("--slot")
    p.set_defaults(fn=cmd_here_set)
    p = here.add_parser("show"); p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_here_show)

    return ap


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.fn(args)
    except Stop as e:
        print(f"СТОП: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
