#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""osctl — состояние workflow меняется только этими командами.

Запуск одинаков на Windows и macOS:
    uv run --locked python osctl.py slot list
    uv run --locked python osctl.py slot claim --slot 2 --for c-exec-...-001 --stage BUILD
    uv run --locked python osctl.py slot release --slot 2 --for c-exec-...-001 --stage BUILD

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
        f"  Создай метку: uv run --locked python osctl.py here set --direction <id> [--slot N]"
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
            f"  Создай один раз: uv run --locked python osctl.py slot init --direction {direction} --count 4"
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

# Формат карточки задаётся в одном месте — panel/cards.py. Второй список видов
# здесь был бы ровно тем расхождением, которое мы лечим.
sys.path.insert(0, str(REPO / "panel"))
try:
    import cards as _fmt
except ImportError as _e:                                    # pragma: no cover
    raise SystemExit(f"не найден panel/cards.py — формат карточки берётся оттуда: {_e}")

# Оба вида объявлены в `os2/CONCEPT.md` и описаны в `os/schema/direction-files.md`.
# Здесь они дописываются к списку носителя: в разделах прежнего `NOW.md` их не было,
# и в `panel/cards.py` им взяться неоткуда.
CARD_KINDS = _fmt.KINDS + ("question", "idea", "day")
SERVICE = _fmt.SERVICE                     # ведущий знак служебных имён
KIND_KEY = SERVICE + "kind"
POS_KEY = SERVICE + "pos"
# Виды, которые обратная сборка упорядочивает по месту. Берутся оттуда же,
# где сборка и живёт, — второй список был бы расхождением.
ORDERED = frozenset(k for _, k in _fmt.SECTIONS) | {"node"}
JOURNAL = "журнал"
JOURNAL_CEILING = 20
# Потолок журнала осмыслен только там, где у карточки есть выход из горячего
# состояния своей же командой: `card close` уносит её в closed/, и журнал
# перестаёт расти. У `node` и `bet` такого выхода нет — их закрывает `review`,
# и многоволновой узел живёт волнами по слову владельца. Для них потолок был
# требованием сделать то, чего сделать нечем: переписать журнал запрещено
# (append-only), закрыть узел нельзя. Замечание висело неснимаемым.
LONG_LIVED = ("node", "bet")
# Терминальный статус «перебито». Пишется только вместе с указателем на преемника.
SUPERSEDED = "superseded"
# Служебные ключи делятся надвое, и разницу стоило измерить раньше.
# ЛИЧНОСТЬ носителя — `id`, `_kind`, `_closed`: их не задаёт зовущий никогда.
# `id` приходит из `--id`, `_kind` из `--kind`, `_closed` выводится из папки.
# МЕСТО — `_bet`, `_parent`, `_pos`: это не внутренности носителя, а то, ЧЬЯ
# карточка и где она стоит. Запрет на них скопом стоил живого дефекта: задачу
# заводили штатно, привязать к ставке было нечем (отказывали и `card new`,
# и `card set`), а `osctl context` ходит именно по этим ссылкам — значит
# заведённая по правилам задача не попадала в рабочий набор следующей ноги
# и просто терялась. Убрать место по-прежнему нельзя: `unset` — как раз тот
# способ, которым карточка исчезает из виду.
PLACEMENT = (SERVICE + "bet", SERVICE + "parent", SERVICE + "pos")

# Поля шапки, которые система знает. Список ОДИН и живёт здесь; схема обязана
# ему равняться — за этим следит `panel/test_docs.py`.
#
# `os2/CONCEPT.md` §3 обещал «известные поля только: самодельные ключи в шапке
# становятся невозможны» — и это было неправдой: команда принимала любое имя
# молча. Цена измерена 2026-08-10 на живом состоянии: восемь задач несут `order`
# рядом с `_pos` (значения РАЗНЫЕ) и `kind` рядом с `_kind` (там `executor`,
# то есть слово занято под другой смысл). Запрещать задним числом нельзя — это
# сломало бы работающие ноги; поэтому check НАЗЫВАЕТ незнакомое поле фактом,
# а убрать его есть чем: `card unset --field <имя>`.
KNOWN_HEAD = frozenset({
    "id", "_kind", "_pos", "_parent", "_bet",   # `_closed` тут НЕТ: он
    # выводится из папки и в файл не пишется никогда — сторож `test_readers`
    # поймал это через минуту после того, как я его сюда вписал.
    "status", "label", "hook", "detail", "by", "outcome_kind",
    "goal", "why", "appetite", "kill_by", "track", "for", "to", "issued",
    "call", "description", "description_by", "label_by", "opened", "node",
    "level", "route", "evidence", "review_when", "blocks",
    "repo", "engineering_contract", "play", "slot", "basis", "closed",
    "cadence", "lens", "last_done", "about", "asks", "from", "source",
    "parent", "waiting_on", "receipts", "started", "unblock_when", "date",
    "paused_by", "note", "superseded_by", "at", "updated",
})
HEAD_LIMIT = 120


def cards_dir(direction: str, override: str | None = None) -> Path:
    return Path(override) if override else (REPO / "live" / direction / "cards")


def card_path(direction: str, cid: str, override: str | None = None) -> Path:
    return cards_dir(direction, override) / f"{cid}.md"


def scalar(value: str):
    """Значение поля шапки. Разбирается как YAML — но ТОЛЬКО до скаляра.

    Если разбор дал словарь или список, значит в тексте было двоеточие или тире,
    и это ПРОЗА, а не структура: «Наряд на t-vert-1: мышь поднимается над полом»
    превращалось в отображение из одного ключа, панель печатала `[object Object]`,
    а слова владельца молча меняли форму. Ровно тот отказ, ради которого всё это
    и переделывалось (CONCEPT §2: «одно двоеточие в прозе валит разбор»).
    Структуре место в теле блоком, в шапке живут только скаляры.
    """
    if value in ("", "null", "none"):
        return None
    try:
        v = yaml.safe_load(value)
    except yaml.YAMLError:
        return value          # не разобралось — значит это просто текст
    return value if isinstance(v, (dict, list)) else v


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
    # Пустые строки в конце блока НЕ срезаются: значение, кончающееся переводом
    # строки, иначе не отличить от разделителя, и обратная сборка теряет его.
    # Разделителя между блоками у нас нет — ровно поэтому неоднозначности тоже.
    return head, blocks, order


def write_card(direction: str, cid: str, head: dict, blocks: dict, order: list,
               override: str | None = None, path: Path | None = None) -> None:
    """Атомарно: временный файл, подмена, чтение обратно и сверка."""
    for k, v in head.items():
        if isinstance(v, (dict, list)):
            raise Stop(f"{cid}: поле {k} — {type(v).__name__}, а в шапке живут только скаляры. "
                       "Структуре место в теле блоком: card block --name {k} --text-file <файл>")
        if isinstance(v, str) and (len(v) > HEAD_LIMIT or chr(10) in v):
            raise Stop(f"{cid}: поле {k} длиннее {HEAD_LIMIT} или многострочное — ему место в теле")
    both = sorted(set(head) & set(order))
    if both:
        raise Stop(f"{cid}: имена {both} разом в шапке и в теле — два носителя одного поля, "
                   "при сборке выиграет тело, а шапка станет протухшей уликой")
    path = path or card_path(direction, cid, override)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Раскладка ровно как у panel/cards.py: пустой строки между блоками НЕТ.
    # Она была бы неотличима от значения, кончающегося переводом строки, —
    # и один и тот же файл два читателя разбирали бы по-разному.
    body = "".join(
        f"## {name}{chr(10)}" + chr(10).join(blocks.get(name) or []) + chr(10)
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
    path, is_closed = locate(direction, a.id, a.cards)
    head, blocks, order = read_card(path)
    if is_closed and not a.json:
        print(f"[закрытая, лежит в {CLOSED}/]")
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
    path = live_only(direction, a.id, a.cards, a.closed)
    head, blocks, order = read_card(path)
    if a.field == "id" or (a.field.startswith(SERVICE) and a.field not in PLACEMENT):
        raise Stop(f"{a.field} не меняется командой set — это опора карточки, а не данные")
    if a.field in blocks:
        raise Stop(f"{a.field} уже лежит в теле блоком — правь его командой block, "
                   "иначе у одного поля станет два носителя")
    if len(a.value) > HEAD_LIMIT or chr(10) in a.value:
        raise Stop(f"значение длиннее {HEAD_LIMIT} символов — это блок тела, а не поле шапки")
    head[a.field] = scalar(a.value)
    write_card(direction, a.id, head, blocks, order, a.cards, path=path)
    print(f"{a.id}: {a.field} = {head[a.field]!r}")
    return 0


def cmd_card_block(a) -> int:
    direction = resolve_direction(a.direction)
    path = live_only(direction, a.id, a.cards, a.closed)
    head, blocks, order = read_card(path)
    if a.name == JOURNAL:
        raise Stop(f"«{JOURNAL}» пишется только командой log add")
    text = value_of(a, "text")
    lines = text.split(chr(10))
    if any(l.startswith("## ") for l in lines):
        raise Stop("в тексте есть строка, начинающаяся с '## ' — она разрежет карточку")
    # Метка ```yaml — единственное, чем список отличается от строки, записанной
    # байт в байт. Забытая закрывающая метка МОЛЧА превращала список в строку.
    if lines and lines[0] == _fmt.YAML_MARK:
        if len(lines) < 2 or lines[-1] != "```":
            raise Stop(f"блок начат меткой {_fmt.YAML_MARK}, но не закрыт строкой ```")
        try:
            v = yaml.safe_load(chr(10).join(lines[1:-1]))
        except yaml.YAMLError as e:
            raise Stop(f"под меткой {_fmt.YAML_MARK} не разбирается как YAML: {e}") from None
        if not isinstance(v, (list, dict)):
            raise Stop(f"под меткой {_fmt.YAML_MARK} должен быть список или словарь, "
                       f"а там {type(v).__name__}")
    blocks[a.name] = lines
    if a.name not in order:
        order.append(a.name)
    write_card(direction, a.id, head, blocks, order, a.cards, path=path)
    print(f"{a.id}: блок «{a.name}» переписан целиком, {len(blocks[a.name])} строк")
    return 0


def cmd_log_add(a) -> int:
    """Порядок записи знает команда, а не тот, кто её зовёт. Новое — сверху."""
    direction = resolve_direction(a.direction)
    path = live_only(direction, a.id, a.cards)
    head, blocks, order = read_card(path)
    line = journal_line(a.date, value_of(a, "text"), a.history)
    lines = journal_put(blocks, order, line, a.id)
    write_card(direction, a.id, head, blocks, order, a.cards)
    print(f"{a.id}: записано в журнал, всего {len(lines)}")
    # Факт, а не совет: «пора закрывать» — это суждение о жизни сущности, а
    # команда объявляет, что ничего не оценивает. Решает читающий.
    if len(lines) > JOURNAL_CEILING and head.get(KIND_KEY) not in LONG_LIVED:
        print(f"  потолок {JOURNAL_CEILING} превышен: {len(lines)} строк")
    return 0



# ------------------------------------------------------- живое и закрытое

CLOSED = "closed"
# Человеческие поля, без которых панель показывает машинный id (закон 4).
REQUIRED = {"node": ("label", "hook"), "call": ("description",)}


def closed_dir(direction: str, override: str | None = None) -> Path:
    return cards_dir(direction, override) / CLOSED


def live_root(direction: str, override: str | None = None) -> Path:
    """Папка направления. Переопределяется по той же причине, что и --cards:
    копия может лежать не под этим репозиторием."""
    return Path(override) if override else (REPO / "live" / direction)


def locate(direction: str, cid: str, override: str | None = None):
    """Живое, потом закрытое. Достать из закрытого так же просто, как из живого."""
    for d in (cards_dir(direction, override), closed_dir(direction, override)):
        p = d / f"{cid}.md"
        if p.exists():
            return p, (d.name == CLOSED)
    raise Stop(f"карточки нет ни среди живых, ни среди закрытых: {cid}")


def live_only(direction: str, cid: str, override: str | None = None,
              allow_closed: bool = False) -> Path:
    """Закрытую карточку молча не правят. Но и чинить её иногда надо — например
    когда порчу в неё записал сам инструмент. Тогда правка идёт с ЯВНЫМ `--closed`:
    запрет был на молчаливое, а не на всякое."""
    p, is_closed = locate(direction, cid, override)
    if is_closed and not allow_closed:
        raise Stop(f"{cid} закрыта и лежит в {CLOSED}/." + chr(10)
                   + f"  Вернуть в работу:   uv run --locked python osctl.py card reopen --id {cid} --why ..."
                   + chr(10)
                   + "  Или поправить на месте, не открывая: добавь --closed")
    return p


def value_of(a, name: str, required: bool = True):
    """Значение целиком: строкой или файлом. Многострочное — норма, а не исключение."""
    inline, from_file = getattr(a, name, None), getattr(a, name + "_file", None)
    if inline is not None and from_file:
        raise Stop(f"--{name} и --{name}-file разом — выбери одно")
    if from_file:
        p = Path(from_file)
        if not p.exists():
            raise Stop(f"файла нет: {p}")
        return p.read_text(encoding="utf-8").rstrip(chr(10))
    if inline is None and required:
        raise Stop(f"нужно --{name} или --{name}-file")
    return inline


def journal_line(date: str | None, text: str, history: str | None) -> str:
    today = __import__("datetime").date.today().isoformat()
    text = " ".join((text or "").split())
    if not text:
        raise Stop("пустая запись журнала")
    line = f"{date or today} · {text}"
    if history:
        line += f" · {history}" if history.startswith("history/") else f" · history/{history}"
    return line


def journal_put(blocks: dict, order: list, line: str, cid: str) -> list:
    """Новое — сверху. Порядок знает команда: с этой поломки всё и началось."""
    lines = blocks.get(JOURNAL) or []
    if line in lines:
        raise Stop(f"{cid}: такая запись уже есть — журнал не дублирует")
    lines.insert(0, line)
    blocks[JOURNAL] = lines
    if JOURNAL not in order:
        order.append(JOURNAL)
    return lines


# ------------------------------------------------------------ указатель NOW.md

# После реза `NOW.md` — указатель направления и больше ничего. Список полей
# ЗАКРЫТ: самодельные ключи в горячем состоянии уже были (`exit_decided_2026_08_06`,
# `warning_2026_08_06`), и лечатся они не аккуратностью, а отказом команды.
NOW_FIELDS = {"bet": "id узла активной ставки, или null",
              "track_wip_limit": "сколько полос идёт разом; только когда есть полосы"}


def now_path(direction: str, root: str | None = None) -> Path:
    return live_root(direction, root) / "NOW.md"


def read_now(direction: str, root: str | None = None) -> dict:
    p = now_path(direction, root)
    if not p.exists():
        raise Stop(f"нет указателя направления: {p}")
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise Stop(f"{p}: верхний уровень не отображение")
    data.pop("END_OF_FILE", None)
    return data


def write_now(direction: str, data: dict, root: str | None = None) -> None:
    p = now_path(direction, root)
    rel = str(p.relative_to(REPO)).replace(chr(92), "/") if str(p).startswith(str(REPO)) else str(p)
    # Отображение целиком одним вызовом: safe_dump СКАЛЯРА дописывает маркер
    # конца документа `...`, и следующая строка становится вторым документом.
    keep = {k: data[k] for k in NOW_FIELDS if k in data}
    body = yaml.safe_dump(keep, sort_keys=False, allow_unicode=True,
                          default_flow_style=False) if keep else ""
    text = f"# NOW: {direction}{chr(10)}{chr(10)}{body}{chr(10)}END_OF_FILE: {rel}{chr(10)}"
    tmp = p.with_suffix(".md.tmp")
    tmp.write_text(text, encoding="utf-8", newline="")
    tmp.replace(p)
    if p.read_text(encoding="utf-8") != text:
        raise Stop(f"{p}: запись не сошлась при чтении обратно")


def cmd_now_show(a) -> int:
    direction = resolve_direction(a.direction)
    data = read_now(direction, a.live_root)
    if a.json:
        print(json.dumps(data, ensure_ascii=False, indent=2, default=str))
        return 0
    for k in NOW_FIELDS:
        print(f"{k}: {data.get(k)!r}")
    return 0


def cmd_now_set(a) -> int:
    direction = resolve_direction(a.direction)
    if a.field not in NOW_FIELDS:
        raise Stop(f"поля {a.field!r} в указателе нет. Есть только:{chr(10)}"
                   + chr(10).join(f"  {k} — {v}" for k, v in NOW_FIELDS.items())
                   + f"{chr(10)}  Всё остальное — карточка.")
    data = read_now(direction, a.live_root)
    value = scalar(a.value)
    if a.field == "bet" and value is not None:
        # ставка указывает на карточку; несуществующий id — это молчаливая ложь
        locate(direction, f"bet-{value}", a.cards)
    if value is None:
        data.pop(a.field, None)
    else:
        data[a.field] = value
    write_now(direction, data, a.live_root)
    print(f"{direction}: {a.field} = {value!r}")
    return 0


def cmd_card_new(a) -> int:
    """Заводит карточку. Без человеческих полей отказывает, а не создаёт
    «допишем потом»: дописывать потом некому, и панель показывает машинный id."""
    direction = resolve_direction(a.direction)
    if a.kind not in CARD_KINDS:
        raise Stop(f"вид {a.kind!r} не из {list(CARD_KINDS)}")
    d = cards_dir(direction, a.cards)
    for probe in (d / f"{a.id}.md", d / CLOSED / f"{a.id}.md"):
        if probe.exists():
            raise Stop(f"карточка {a.id} уже есть: {probe}")

    head = {"id": a.id, KIND_KEY: a.kind}
    blocks, order = {}, []
    for pair in (a.field or []):
        if "=" not in pair:
            raise Stop(f"--field ждёт вида имя=значение, получено {pair!r}")
        k, v = pair.split("=", 1)
        if k == "id" or (k.startswith(SERVICE) and k not in PLACEMENT):
            raise Stop(f"{k} не задаётся через --field — это опора карточки")
        head[k] = scalar(v)
    for pair in (a.block or []):
        if "=" not in pair:
            raise Stop(f"--block ждёт вида имя=путь-к-файлу, получено {pair!r}")
        name, path = pair.split("=", 1)
        if name == JOURNAL:
            raise Stop(f"«{JOURNAL}» пишется только командой log add")
        f = Path(path)
        if not f.exists():
            raise Stop(f"файла нет: {f}")
        text = f.read_text(encoding="utf-8").rstrip(chr(10))
        if any(l.startswith("## ") for l in text.split(chr(10))):
            raise Stop(f"{name}: в тексте строка с '## ' — она разрежет карточку")
        blocks[name] = text.split(chr(10))
        order.append(name)

    missing = [k for k in REQUIRED.get(a.kind, ()) if not head.get(k) and k not in blocks]
    if missing:
        raise Stop(f"{a.kind} без {missing} не заводится (закон 4: человеческие поля "
                   f"пишутся при создании).{chr(10)}  Добавь: "
                   + " ".join(f"--field {k}=<...>" for k in missing))

    # Место среди своих: последним, никого не сдвигая. Закрытые СЧИТАЮТСЯ ТОЖЕ —
    # их место остаётся занятым, иначе card reopen вернул бы карточку на чужое.
    pos = -1
    for p, _closed in all_cards(direction, a.cards):
        try:
            h, _, _ = read_card(p)
        except Stop:
            continue
        if h.get(KIND_KEY) == a.kind and isinstance(h.get(POS_KEY), int):
            pos = max(pos, h[POS_KEY])
    head[POS_KEY] = pos + 1

    write_card(direction, a.id, head, blocks, order, a.cards)
    print(f"заведена {a.id} ({a.kind}), место {head[POS_KEY]}, "
          f"блоков {len(order)}")
    return 0


def cmd_card_close(a) -> int:
    """Закрывает карточку: причина в журнал, файл в closed/. Одно действие,
    а не два — иначе останется числиться то, что уже кончилось."""
    direction = resolve_direction(a.direction)
    src = live_only(direction, a.id, a.cards)
    why = value_of(a, "why")
    head, blocks, order = read_card(src)
    # «Перебито» без указателя на преемника неотличимо от «брошено», а вся его
    # ценность в том, что видно, ЧЕМ перебило. Статус объявлен в `os2/CONCEPT.md`
    # и ждал во `FRICTION.md` с 27 июля: поля были узаконены, писателя не было.
    # ВСЁ ПРОВЕРЯЕТСЯ ДО ПЕРВОЙ ЗАПИСИ — отказ не должен оставлять карточку
    # наполовину закрытой.
    if a.status == SUPERSEDED and not a.superseded_by:
        raise Stop(f"статус {SUPERSEDED} без --superseded-by: «перебито» обязано назвать, "
                   "чем именно, иначе оно неотличимо от «брошено»")
    if a.superseded_by and a.status != SUPERSEDED:
        raise Stop(f"--superseded-by ставится только со статусом {SUPERSEDED}")
    if a.status:
        head["status"] = a.status
    if a.superseded_by:
        head["superseded_by"] = a.superseded_by
        # Через `scalar`, как все прочие даты: иначе yaml запишет её строкой
        # в кавычках, и одно и то же поле в разных карточках будет разного вида.
        head["at"] = scalar(a.date or __import__("datetime").date.today().isoformat())
    lines = journal_put(blocks, order, journal_line(a.date, why, a.history), a.id)
    dest = closed_dir(direction, a.cards) / f"{a.id}.md"
    write_card(direction, a.id, head, blocks, order, a.cards, path=dest)
    src.unlink()          # сначала записали, потом убрали: обрыв оставляет копию
    print(f"{a.id}: закрыта, причина записана в журнал ({len(lines)} строк), "
          f"уехала в {CLOSED}/")
    return 0


def cmd_card_reopen(a) -> int:
    direction = resolve_direction(a.direction)
    src = closed_dir(direction, a.cards) / f"{a.id}.md"
    if not src.exists():
        raise Stop(f"среди закрытых нет: {src}")
    why = value_of(a, "why")
    head, blocks, order = read_card(src)
    journal_put(blocks, order, journal_line(a.date, why, a.history), a.id)
    write_card(direction, a.id, head, blocks, order, a.cards)
    src.unlink()
    print(f"{a.id}: возвращена в живые, причина записана в журнал")
    return 0


def cmd_card_unset(a) -> int:
    """Убирает ключ совсем. `set --value ""` клал null — это не то же самое."""
    direction = resolve_direction(a.direction)
    path = live_only(direction, a.id, a.cards, a.closed)
    head, blocks, order = read_card(path)
    if bool(a.field) == bool(a.block):
        raise Stop("нужно ровно одно: --field (шапка) или --block (тело)")
    if a.field:
        if a.field == "id" or a.field.startswith(SERVICE):
            raise Stop(f"{a.field} не убирается — это опора карточки")
        if a.field not in head:
            raise Stop(f"поля {a.field!r} в шапке нет; есть: {sorted(head)}")
        del head[a.field]
        what = f"поле {a.field}"
    else:
        if a.block == JOURNAL:
            raise Stop(f"«{JOURNAL}» не убирается — это история сущности")
        if a.block not in blocks:
            raise Stop(f"блока {a.block!r} в теле нет; есть: {sorted(blocks)}")
        del blocks[a.block]
        order.remove(a.block)
        what = f"блок {a.block}"
    write_card(direction, a.id, head, blocks, order, a.cards, path=path)
    print(f"{a.id}: {what} убран")
    return 0


def cmd_leg_close(a) -> int:
    """Конец ноги: полный отчёт в `history/` и запись в журнал каждой затронутой
    сущности. Порознь их забывают — 107 случаев на 45 отчётов.

    ВСЁ ПРОВЕРЯЕТСЯ ДО ПЕРВОЙ ЗАПИСИ. Пока это было не так, команда успевала
    сохранить отчёт и падала перед журналами — частичная запись ровно там, где
    команда существует, чтобы её не было (2026-08-08, первая живая нога).

    В `LOG.md` больше не пишется: рез его удалил, и правила его не называют.
    Общий журнал направления — это `git log`, поэтому команда печатает готовое
    сообщение коммита: строка журнала и сообщение коммита теперь один текст.

    Поле `updated:` НЕ пишется намеренно: оно живёт в комментарии, дублирует дату
    и ногу из этой же записи, и правка его требовала бы поиска места в тексте.
    """
    direction = resolve_direction(a.direction)
    date = a.date or __import__("datetime").date.today().isoformat()
    result = value_of(a, "result")
    log_text = " ".join(value_of(a, "log").split())
    if not log_text:
        raise Stop("пустая строка журнала — нога без следа не закрывается")

    # --- ПРОВЕРКИ. Ни одного байта на диск, пока не сошлось всё.
    hist_dir = live_root(direction, a.live_root) / "history"
    hist = hist_dir / f"{date}-{a.leg}.md"
    body = result if result.endswith(chr(10)) else result + chr(10)
    saved = "сохранён"
    if hist.exists():
        # повтор ноги: тот же байт в байт — это доказательство, что запись уже
        # прошла целиком; другой текст под тем же именем — логическое столкновение
        if hist.read_text(encoding="utf-8") == body:
            saved = "уже сохранён байт в байт"
        else:
            raise Stop(f"{hist.name} уже есть с ДРУГИМ текстом — это столкновение, "
                       "а не повтор. Разбирайся вручную, перезаписывать нельзя.")

    line = journal_line(date, log_text, hist.name)
    planned, already = [], []
    for cid in (a.id or []):
        path = live_only(direction, cid, a.cards)      # нет карточки — стоп ЗДЕСЬ
        head, blocks, order = read_card(path)
        if line in (blocks.get(JOURNAL) or []):
            already.append(cid)                        # повтор, а не ошибка
            continue
        planned.append((cid, path, head, blocks, order))

    # --- ЗАПИСЬ. Дальше отказать уже нечему.
    if saved == "сохранён":
        hist_dir.mkdir(parents=True, exist_ok=True)
        tmp = hist.with_suffix(".md.tmp")
        tmp.write_text(body, encoding="utf-8", newline="")
        tmp.replace(hist)
        if hist.read_text(encoding="utf-8") != body:
            raise Stop(f"{hist}: запись не сошлась при чтении обратно")
    for cid, path, head, blocks, order in planned:
        journal_put(blocks, order, line, cid)
        write_card(direction, cid, head, blocks, order, a.cards, path=path)

    print(f"отчёт {hist.name}: {saved}")
    for cid, *_ in planned:
        print(f"журнал {cid}: записано")
    for cid in already:
        print(f"журнал {cid}: уже была та же запись")
    if not (planned or already):
        print("журналы сущностей: ни одна не названа (--id) — следом остаётся "
              "только отчёт и коммит")
    scope = a.scope or "direction"
    print(f"{chr(10)}сообщение коммита (оно же строка общего журнала):")
    print(f"  {direction} {a.play} {scope}: {log_text}")
    return 0


def all_cards(direction: str, override: str | None = None):
    """Живые и закрытые вместе. Достать из закрытого должно быть так же просто."""
    for d, closed in ((cards_dir(direction, override), False),
                      (closed_dir(direction, override), True)):
        if d.is_dir():
            for p in sorted(d.glob("*.md")):
                yield p, closed


def cmd_find(a) -> int:
    direction = resolve_direction(a.direction)
    if not cards_dir(direction, a.cards).is_dir():
        raise Stop(f"папки карточек нет: {cards_dir(direction, a.cards)}")
    hits = closed_hits = 0
    for p, closed in all_cards(direction, a.cards):
        text = p.read_text(encoding="utf-8")
        if a.text.lower() in text.lower():
            hits += 1
            closed_hits += 1 if closed else 0
            for i, line in enumerate(text.split(chr(10)), 1):
                if a.text.lower() in line.lower():
                    mark = f" [{CLOSED}]" if closed else ""
                    print(f"{p.stem}{mark}:{i}: {line.strip()[:100]}")
                    break
    tail = f" (из них закрытых: {closed_hits})" if closed_hits else ""
    print(f"{chr(10)}найдено карточек: {hits}{tail}")
    return 0


# Вопрос/решение носит две вещи: к чему привязан и кто отвечает. Без первого
# его негде искать, без второго он либо теряется, либо носится владельцу зря.
ABOUT, ASKS, OWNER = "about", "asks", "владелец"


def rel_path(p: Path) -> str:
    try:
        return str(p.relative_to(REPO)).replace(chr(92), "/")
    except ValueError:
        return str(p)


def words_in(p: Path) -> int:
    return len(p.read_text(encoding="utf-8").split())


def cmd_context(a) -> int:
    """Рабочий набор ноги: что читать и что ждёт слова владельца.

    Замерено 2026-08-09: `Reads: cards/` в плеях означало 27 029 слов состояния
    при рабочем наборе одной задачи около 4 200 — шестикратный перегруз, внутри
    которого реестр подписей на 5 146 слов, читаемый одним гейтом.

    Набор строит КОМАНДА ПО ССЫЛКАМ, которые в карточках уже есть (`_bet`,
    `node`, `_parent`, `for`, `about`), а не модель по вкусу. И остаток называется
    вслух: включённое плюс исключённое = все живые карточки. Молчаливая недостача
    неотличима от «нечего показывать» — это тот самый класс, ради которого
    написан `panel/test_readers.py`.
    """
    direction = resolve_direction(a.direction)
    d = cards_dir(direction, a.cards)
    if not d.is_dir():
        raise Stop(f"папки карточек нет: {d}")
    cards = {}
    for p in sorted(d.glob("*.md")):
        head, blocks, _ = read_card(p)
        cards[p.stem] = (p, head, blocks)

    now_file = now_path(direction, a.live_root)
    now = read_now(direction, a.live_root)
    target = a.for_ or now.get("bet")
    if not target:
        raise Stop("не названа цель (--for), и в указателе направления нет ставки")
    if target not in cards:
        raise Stop(f"нет живой карточки {target} — не с чего собирать набор. "
                   f"Закрытую смотри так: card show --id {target}")

    chosen: dict[str, str] = {}

    def take(cid, why):
        if cid and cid in cards and cid not in chosen:
            chosen[cid] = why

    take(target, "цель этой ноги")
    anchor, head = target, cards[target][1]
    if head.get("for") in cards:                    # наряд тянет свою задачу
        take(head["for"], "задача этого наряда")
        anchor = head["for"]
        head = cards[anchor][1]
    kind = head.get(KIND_KEY)
    node = (head.get("node") if kind == "bet"
            else anchor if kind == "node" else head.get(SERVICE + "bet"))

    for cid, (_, h, _) in cards.items():
        if h.get(KIND_KEY) == "bet" and h.get("node") == node:
            take(cid, "ставка")
    take(node, "цель ставки")
    if node in cards:
        take(cards[node][1].get(SERVICE + "parent"), "родитель цели")
    for cid, (_, h, _) in cards.items():
        if h.get("for") == anchor:
            take(cid, "наряд под эту задачу")
    if kind in ("node", "bet"):                     # ставку берут целиком со списком задач
        for cid, (_, h, _) in cards.items():
            if h.get(SERVICE + "bet") == node and h.get(KIND_KEY) == "task":
                take(cid, "задача ставки")

    waiting = []
    for cid, (_, h, b) in sorted(cards.items()):
        if h.get(KIND_KEY) not in ("question", "decision"):
            continue
        if str(h.get(ASKS) or OWNER).lower() not in (OWNER, "owner"):
            continue                                # отвечает не он — не носим
        about = h.get(ABOUT)
        if about and about not in chosen:
            continue                                # привязан к чужому месту
        text = next((chr(10).join(v).strip() for v in b.values() if any(x.strip() for x in v)), "")
        waiting.append({"id": cid, "about": about or "направление",
                        "text": " ".join(text.split())[:300]})
        take(cid, "ждёт слова владельца")

    rest = [cid for cid in cards if cid not in chosen]
    by_kind: dict[str, int] = {}
    for cid in rest:
        k = str(cards[cid][1].get(KIND_KEY))
        by_kind[k] = by_kind.get(k, 0) + 1
    excluded = {"ids": sorted(rest), "words": sum(words_in(cards[c][0]) for c in rest),
                "by_kind": dict(sorted(by_kind.items()))}

    chosen_set = [{"id": "NOW", "path": rel_path(now_file), "words": words_in(now_file),
                   "why": "указатель направления"}]
    chosen_set += [{"id": cid, "path": rel_path(cards[cid][0]), "words": words_in(cards[cid][0]),
                    "why": why} for cid, why in sorted(chosen.items())]
    out = {"direction": direction, "bet": now.get("bet"), "target": target,
           "set": chosen_set, "waiting": waiting, "excluded": excluded}
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2, default=str))
        return 0

    print(f"направление: {direction} · ставка: {now.get('bet')} · цель ноги: {target}")
    if waiting:
        print(f"{chr(10)}ЖДЁТ СЛОВА ВЛАДЕЛЬЦА ({len(waiting)})")
        for w in waiting:
            print(f"  {w['id']} · про {w['about']}")
            print(f"      {w['text']}")
    else:
        print(f"{chr(10)}ждёт слова владельца: ничего")
    total = sum(x["words"] for x in chosen_set)
    print(f"{chr(10)}РАБОЧИЙ НАБОР ({len(chosen_set)} файлов, {total} слов)")
    for x in chosen_set:
        print(f"  {x['path']:<58} {x['words']:>6}  {x['why']}")
    kinds = " · ".join(f"{k} {n}" for k, n in excluded["by_kind"].items())
    print(f"{chr(10)}НЕ ВКЛЮЧЕНО: {len(rest)} карточек, {excluded['words']} слов — {kinds}")
    print(f"  дочитать: uv run --locked python osctl.py card show --id <id> · "
          f"uv run --locked python osctl.py find --text <текст>")
    return 0


def cmd_check(a) -> int:
    """Только механические факты. Ничего не оценивает и не судит смысл."""
    direction = resolve_direction(a.direction)
    d = cards_dir(direction, a.cards)
    if not d.is_dir():
        raise Stop(f"папки карточек нет: {d}")
    # Поломки не дают собрать состояние. Замечания — факты о содержании
    # (нет имени, длинный журнал): их называют, но не судят по ним (CONCEPT §4).
    problems, notes, seen, places, total, shut = [], [], {}, {}, 0, 0
    roots: list[str] = []
    for p, closed in all_cards(direction, a.cards):
        total += 1
        shut += 1 if closed else 0
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
        if head.get(KIND_KEY) not in CARD_KINDS:
            problems.append(f"{p.name}: {KIND_KEY} {head.get(KIND_KEY)!r} не из {list(CARD_KINDS)}")
        both = sorted(set(head) & set(blocks))
        if both:
            problems.append(f"{p.name}: имена {both} разом в шапке и в теле — два носителя")
        if not p.read_text(encoding="utf-8").rstrip().endswith(f"{p.name}"):
            problems.append(f"{p.name}: нет хвоста END_OF_FILE")
        for k, v in head.items():
            if isinstance(v, (dict, list)):
                problems.append(f"{p.name}: поле {k} — {type(v).__name__}, а не скаляр; "
                                "скорее всего в прозе было двоеточие и её разобрали как структуру")
            if isinstance(v, str) and (len(v) > HEAD_LIMIT or chr(10) in v):
                problems.append(f"{p.name}: поле {k} длинное — ему место в теле")
        # Карточка без МЕСТА не попадает в рабочий набор: `osctl context` ходит
        # ровно по этим ссылкам. Заведённая по правилам задача терялась для
        # следующей ноги, и заметить это было нечем.
        # ТОЛЬКО у живых. Закрытая карточка в рабочий набор и не должна попадать —
        # она отработала; а `card set` её без `--closed` всё равно не тронет, то есть
        # замечание было бы неисполнимым. Первый же прогон поймал `t-vert-1`
        # (`status: done`, лежит в closed/) и заставил владельца чинить не то.
        if not closed:
            if head.get(KIND_KEY) == "task" and not head.get(SERVICE + "bet"):
                notes.append(f"{p.name}: задача без ставки — в рабочий набор не попадёт "
                             f"(card set --field _bet --value <id цели>)")
            if head.get(KIND_KEY) == "node" and not head.get(SERVICE + "parent"):
                roots.append(p.name)
        unknown = sorted(k for k in head if k not in KNOWN_HEAD)
        if unknown:
            notes.append(f"{p.name}: поля шапки вне известных: {', '.join(unknown)} "
                         f"(убрать: card unset --field <имя>)")
        j = blocks.get(JOURNAL) or []
        if len(j) > JOURNAL_CEILING and head.get(KIND_KEY) not in LONG_LIVED:
            notes.append(f"{p.name}: журнал {len(j)} строк, потолок {JOURNAL_CEILING}")
        if head.get(KIND_KEY) == "node" and not head.get("label"):
            notes.append(f"{p.name}: у цели нет короткого имени (label) — "
                         "его пишет владелец или его нога, не команда")
        if closed and head.get(KIND_KEY) in ("task", "node") \
                and head.get("status") not in ("done", "dropped"):
            notes.append(f"{p.name}: закрыта со статусом {head.get('status')!r} — "
                         "чем кончилось, не записано, и панель честно скажет «ЗАКРЫТО» "
                         "вместо «сделано». Закрывать так: card close --status done|dropped")
        if not closed:   # места считаются только среди живых: закрытые не собираются
            # У узла место — среди БРАТЬЕВ, поэтому родитель входит в ключ:
            # два узла у разных родителей законно стоят на одном номере.
            kind, pos = head.get(KIND_KEY), head.get(POS_KEY)
            key = (kind, head.get(SERVICE + "parent"), pos)
            # Место важно только там, где сборка им УПОРЯДОЧИВАЕТ: разделы и узлы.
            # `bet` одна, `extra` адресуется своим именем — там место ничего не значит.
            if kind in ORDERED and isinstance(pos, int) and not isinstance(pos, bool):
                if key in places:
                    among = f"«{kind}» под {key[1]}" if kind == "node" else f"«{kind}»"
                    problems.append(f"{p.name}: место {pos} среди {among} уже занято "
                                    f"карточкой {places[key]} — панель на этом не соберётся")
                places[key] = p.name
    # Корень у дерева один. Второй узел без родителя — не корень, а сирота:
    # он не найдётся ни картой, ни рабочим набором.
    if len(roots) > 1:
        notes.append(f"целей без родителя {len(roots)}: {', '.join(sorted(roots))} — корень один, остальные не найдутся (card set --field _parent --value <id>)")
    print(f"карточек: {total}" + (f" (живых {total - shut}, закрытых {shut})" if shut else ""))
    if notes:
        print(f"замечаний: {len(notes)} (не мешают работе)")
        for x in notes:
            print("  " + x)
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

    def common(q):
        q.add_argument("--id", required=True)
        q.add_argument("--direction")
        q.add_argument("--cards", help="папка карточек, по умолчанию live/<направление>/cards")
        return q

    q = common(card.add_parser("show", help="показать карточку; смотрит и в закрытых"))
    q.add_argument("--json", action="store_true"); q.set_defaults(fn=cmd_card_show)

    q = common(card.add_parser("new", help="завести карточку; человеческие поля обязательны"))
    q.add_argument("--kind", required=True, help=f"один из {list(CARD_KINDS)}")
    q.add_argument("--field", action="append", metavar="ИМЯ=ЗНАЧЕНИЕ",
                   help="короткое поле шапки; можно несколько раз")
    q.add_argument("--block", action="append", metavar="ИМЯ=ФАЙЛ",
                   help="длинный блок тела из файла; можно несколько раз")
    q.set_defaults(fn=cmd_card_new)

    q = common(card.add_parser("set", help="заменить значение поля шапки целиком"))
    q.add_argument("--field", required=True); q.add_argument("--value", required=True)
    q.add_argument("--closed", action="store_true",
                   help="править карточку, лежащую в closed/, не открывая её")
    q.set_defaults(fn=cmd_card_set)

    q = common(card.add_parser("block", help="переписать блок тела целиком"))
    q.add_argument("--name", required=True)
    q.add_argument("--text"); q.add_argument("--text-file", dest="text_file")
    q.add_argument("--closed", action="store_true",
                   help="править карточку, лежащую в closed/, не открывая её")
    q.set_defaults(fn=cmd_card_block)

    q = common(card.add_parser("unset", help="убрать ключ совсем (set --value '' клал null)"))
    q.add_argument("--field"); q.add_argument("--block"); q.add_argument("--closed", action="store_true",
                   help="править карточку, лежащую в closed/, не открывая её")
    q.set_defaults(fn=cmd_card_unset)

    q = common(card.add_parser("close", help="причина в журнал, карточка в closed/"))
    q.add_argument("--why"); q.add_argument("--why-file", dest="why_file")
    q.add_argument("--status", help="терминальный статус, если он у этого вида есть")
    q.add_argument("--superseded-by", dest="superseded_by",
                   help=f"id того, чем перебило; обязателен при --status {SUPERSEDED}")
    q.add_argument("--history"); q.add_argument("--date"); q.set_defaults(fn=cmd_card_close)

    q = common(card.add_parser("reopen", help="вернуть закрытую в живые"))
    q.add_argument("--why"); q.add_argument("--why-file", dest="why_file")
    q.add_argument("--history"); q.add_argument("--date"); q.set_defaults(fn=cmd_card_reopen)

    log = sub.add_parser("log").add_subparsers(dest="verb", required=True)
    q = log.add_parser("add", help="строка в журнал сущности; порядок знает команда")
    q.add_argument("--id", required=True)
    q.add_argument("--text"); q.add_argument("--text-file", dest="text_file")
    q.add_argument("--history"); q.add_argument("--date"); q.add_argument("--direction")
    q.add_argument("--cards"); q.set_defaults(fn=cmd_log_add)

    now = sub.add_parser("now").add_subparsers(dest="verb", required=True)
    for name, fn in (("show", cmd_now_show), ("set", cmd_now_set)):
        q = now.add_parser(name, help="указатель направления: ставка и лимит полос")
        q.add_argument("--direction"); q.add_argument("--cards")
        q.add_argument("--live-root", dest="live_root")
        if name == "show":
            q.add_argument("--json", action="store_true")
        else:
            q.add_argument("--field", required=True); q.add_argument("--value", required=True)
        q.set_defaults(fn=fn)

    leg = sub.add_parser("leg").add_subparsers(dest="verb", required=True)
    q = leg.add_parser("close", help="конец ноги: отчёт, общий журнал и журналы сущностей")
    q.add_argument("--leg", required=True, help="id сессии, например s-work-g-5a7c-001")
    q.add_argument("--play", required=True)
    q.add_argument("--scope", help="direction или id сущности; по умолчанию direction")
    q.add_argument("--log"); q.add_argument("--log-file", dest="log_file")
    q.add_argument("--result"); q.add_argument("--result-file", dest="result_file")
    q.add_argument("--id", action="append", help="затронутая сущность; можно несколько раз")
    q.add_argument("--date"); q.add_argument("--direction"); q.add_argument("--cards")
    q.add_argument("--live-root", dest="live_root",
                   help="папка направления, по умолчанию live/<направление>")
    q.set_defaults(fn=cmd_leg_close)

    q = sub.add_parser("find", help="поиск по карточкам")
    q.add_argument("--text", required=True); q.add_argument("--direction")
    q.add_argument("--cards"); q.set_defaults(fn=cmd_find)

    q = sub.add_parser("context", help="рабочий набор ноги: что читать и что ждёт владельца")
    q.add_argument("--for", dest="for_", help="id задачи/наряда/узла; без него — ставка")
    q.add_argument("--direction"); q.add_argument("--cards")
    q.add_argument("--live-root", dest="live_root")
    q.add_argument("--json", action="store_true"); q.set_defaults(fn=cmd_context)

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
