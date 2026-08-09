"""Сервер панели: выбор направления, страница, раздел «Сейчас». Только stdlib + yaml + panel/cards.py.
Запуск: python panel/serve.py [--port N] [--no-open]"""

import argparse
import datetime
import json
import os
import re
import sys
import subprocess
import threading
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import cards
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.join(ROOT, "panel", "app")
LIVE_DIR = os.path.join(ROOT, "live")

def cards_dir(direction):
    """Живые карточки направления. Проекции больше нет: карточки И ЕСТЬ состояние."""
    d = os.path.join(LIVE_DIR, direction, "cards")
    if not os.path.isdir(d):
        raise FileNotFoundError(
            f"у направления «{direction}» нет папки карточек: live/{direction}/cards/. "
            "Состояние живёт в карточках — показывать нечего.")
    return d


CLOSED = "closed"


def load_cards(direction, kind=None):
    """Все карточки направления: живые И закрытые.

    Закрытая карточка — это СДЕЛАННОЕ, а не исчезнувшее. Пока читалась только
    живая папка, закрытие задачи убирало её и из числителя, и из знаменателя:
    семь задач превращались в шесть, из них ноль сделанных.

    Где карточка лежит — кладётся в шапку служебным ключом `_closed`. В файле
    его нет и быть не может: он выводится из папки. Наружу не пишется никогда —
    панель вообще не пишет.
    """
    loaded, unread = {}, []
    live = cards_dir(direction)
    for folder, closed in ((live, False), (os.path.join(live, CLOSED), True)):
        if not os.path.isdir(folder):
            continue
        for name in sorted(f for f in os.listdir(folder) if f.endswith(".md")):
            try:
                head, blocks = cards.read_card(os.path.join(folder, name))
            except (Exception, SystemExit) as e:
                # cards.fail бросает SystemExit — обычный except Exception не ловит.
                unread.append({"file": name, "error": str(e)})
                continue
            if not isinstance(head, dict):
                unread.append({"file": name, "error": "шапка не словарь"})
                continue
            head["_closed"] = closed
            if kind is None or head.get("_kind") == kind:
                loaded[str(head.get("id"))] = (head, blocks)
    return loaded, unread


def read_now(direction):
    """Указатель направления — и проверка, что читатель не пережил свой источник.

    Ключи сверяются с закрытым списком `osctl.NOW_FIELDS` в обе стороны: чужой
    ключ в файле и чтение несуществующего ключа в коде одинаково означают, что
    одна сторона отстала. Молчаливая пустота вместо этого стоила трёх поломок
    подряд (`tracks`, `direction_forecast`, `LOG.md`).
    """
    sys.path.insert(0, ROOT)
    import osctl
    path = os.path.join(LIVE_DIR, direction, "NOW.md")
    with open(path, encoding="utf-8") as fh:
        now = yaml.safe_load(fh.read()) or {}
    if not isinstance(now, dict):
        raise RuntimeError(f"{path}: верхний уровень не отображение")
    now.pop("END_OF_FILE", None)
    unknown = [k for k in now if k not in osctl.NOW_FIELDS]
    if unknown:
        raise RuntimeError(f"{path}: ключи {unknown} не из указателя "
                           f"{sorted(osctl.NOW_FIELDS)} — состояние живёт в карточках")
    return now


def now_field(now, name):
    """Чтение поля указателя ТОЛЬКО по имени из закрытого списка."""
    sys.path.insert(0, ROOT)
    import osctl
    if name not in osctl.NOW_FIELDS:
        raise RuntimeError(f"в указателе нет поля {name!r}; есть {sorted(osctl.NOW_FIELDS)}. "
                           "Если оно было раньше — оно стало карточкой.")
    return now.get(name)


def outcome(head):
    """Чем кончилось — ровно то, что известно, и ни словом больше.

    `done` и `dropped` — разные вещи: одно сделано, другое СНЯТО его решением.
    Карточка может лежать в closed/ вообще без терминального статуса (так снимали
    `t-scale-2`), и называть это «сделано» — врать на экране. Тогда честный
    ответ — «закрыто», и пробел виден, а не замазан.
    """
    if head.get("status") == "done":
        return "done"
    if head.get("status") == "dropped":
        return "dropped"
    return "closed" if head.get("_closed") else None


def is_done(head):
    """Сделано — только это. Живых `done` не бывает по построению: команда
    закрытия уносит карточку, — поэтому счёт идёт и по закрытой папке."""
    return outcome(head) == "done"


SECTIONS = [("now", "СЕЙЧАС"), ("slots", "СЛОТЫ"), ("waiting", "ЖДЁТ ТЕБЯ"), ("wave", "ВОЛНА"),
            ("goals", "ЦЕЛИ"), ("history", "ИСТОРИЯ"), ("knowledge", "ЗНАНИЯ"),
            ("direction", "НАПРАВЛЕНИЕ")]

READY_SECTIONS = ("now", "slots", "wave", "goals")

CONTENT_TYPES = {".html": "text/html; charset=utf-8",
                 ".js": "application/javascript; charset=utf-8",
                 ".css": "text/css; charset=utf-8"}

# Незнакомые статусы идут после всех.
STATUS_ORDER = ["running", "waiting", "blocked", "paused"]
# По одному замку на направление: пересборка стирает папку карточек целиком.
_DIR_LOCKS = {}
_META_LOCK = threading.Lock()


def lock_for(direction):
    with _META_LOCK:
        return _DIR_LOCKS.setdefault(direction, threading.Lock())


def git(*args):
    try:
        out = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                             encoding="utf-8", errors="replace", timeout=10)
        return out.returncode, (out.stdout or "").strip()
    except (OSError, subprocess.SubprocessError):
        return 1, ""


def build_info():
    _, commit = git("rev-parse", "--short", "HEAD")
    _, commit_date = git("log", "-1", "--format=%ad", "--date=short")
    code, count = git("rev-list", "--count", "origin/main..HEAD")
    unpushed = int(count) if code == 0 and count.isdigit() else 0
    return {"commit": commit, "commit_date": commit_date, "unpushed": unpushed, "unread": 0}


def directions():
    names = sorted(n for n in os.listdir(LIVE_DIR) if os.path.isdir(os.path.join(LIVE_DIR, n)))
    return [{"id": n, "sections": [{"id": sid, "label": label, "ready": sid in READY_SECTIONS}
                                    for sid, label in SECTIONS]} for n in names]


def section_slots(direction):
    """Доска аренд плюс измеренное про каждую копию. Ничего не выводим и не оцениваем."""
    sys.path.insert(0, ROOT)
    import osctl
    out = {"direction": direction, "ledger": str(osctl.ledger_path(direction)),
           "slots": [], "error": None}
    try:
        data = osctl.read_ledger(direction)
    except osctl.Stop as e:
        out["error"] = str(e)
        return out
    for name, rec in sorted(data["slots"].items(), key=lambda kv: int(kv[0])):
        lease = rec.get("lease")
        facts = osctl.slot_facts(direction, name)
        out["slots"].append({
            "slot": name,
            "lifecycle": rec.get("lifecycle"),
            "lease": lease,
            "call": lease.rsplit(":", 1)[0] if lease and lease != "none" else None,
            "stage": lease.rsplit(":", 1)[1] if lease and lease != "none" else None,
            "worktree": facts["worktree"],
            "branch": facts["branch"],
            "branch_exists": facts["branch_exists"],
            "clean": facts["clean"],
            "ahead": facts["ahead"],
            "published": facts["published"],
        })
    return out


# Внутренние статусы наружу не показываются: владелец в них не думает.
NODE_STATE = {"active": ("running", "ИДЁТ СЕЙЧАС"), "shaped": ("ahead", "ДАЛЬШЕ"),
              "parked": ("ahead", "ДАЛЬШЕ"), "done": ("closed", "СДЕЛАНО"),
              "dropped": ("closed", "СНЯТО")}


def section_goals(direction):
    """Карта целей. Строит из карточек узлов; имена берёт накладкой, ничего не выдумывает."""
    with lock_for(direction):
        loaded, unread = load_cards(direction, kind="node")

    # Прогноз направления — своя карточка, а не ключ NOW.md: рез унёс оттуда всё,
    # кроме ставки и лимита полос, и чтение старого ключа молча давало пустоту.
    target = None
    forecast, _ = load_cards(direction, kind=cards.EXTRA)
    fc = forecast.get("direction_forecast")
    if fc:
        v = cards.body_value("direction_forecast", "direction_forecast",
                             fc[1].get("direction_forecast") or [])
        if isinstance(v, dict):
            target = v.get("target")

    out = []
    for cid, (h, b) in loaded.items():
        raw = h.get("status")
        state, word = NODE_STATE.get(raw, ("ahead", str(raw or "?").upper()))
        out.append({
            "id": cid, "parent": h.get("_parent"), "pos": h.get("_pos"),
            "state": state, "word": word, "raw_status": raw,
            # имя и крючок — ИЗ КАРТОЧКИ. Накладка `os2/labels/` снята: пока она
            # была, панель показывала её, а карточку игнорировала — переименование
            # командой не дошло бы до экрана и об этом никто бы не узнал.
            "label": h.get("label"), "hook": h.get("hook"),
            "label_by": h.get("label_by"),
            "goal": h.get("goal") or block_text(b, "goal"),
            "why": h.get("why") or block_text(b, "why"),
            "done_when": h.get("done_when") or block_text(b, "done_when"),
            "detail": h.get("detail"),
            "is_root": h.get("_parent") is None,
        })
    out.sort(key=lambda r: (r["pos"] if isinstance(r["pos"], int) else 999))

    groups = {"running": [], "ahead": [], "closed_done": [], "closed_dropped": []}
    root = None
    for r in out:
        if r["is_root"]:
            root = r
            continue
        if r["state"] == "running":
            groups["running"].append(r)
        elif r["state"] == "ahead":
            groups["ahead"].append(r)
        elif r["raw_status"] == "done":
            groups["closed_done"].append(r)
        else:
            groups["closed_dropped"].append(r)

    return {"direction": direction, "root": root, "groups": groups, "target": target,
            "unread": unread, "no_label": [r["id"] for r in out if not r["label"]],
            "counts": {k: len(v) for k, v in groups.items()}}


PLAY_WORD = {
    "map": ("КАРТА", "plan"), "frame": ("УСТАВ", "plan"), "shape": ("НАРЕЗКА", "plan"),
    "converge": ("РАЗБОР", "think"), "converge-arch": ("РАЗБОР", "think"),
    "converge-verify": ("ПРОВЕРКА", "think"), "research": ("ИЗУЧЕНИЕ", "think"),
    "review": ("ИТОГ", "done"), "work": ("РАБОТА", ""), "day": ("ДЕНЬ", ""),
    "repair": ("ПОЧИНКА", "wait"), "pulse": ("ОБХОД", ""), "guide": ("РАЗБОР", "think"),
}

SEP = chr(31)

# Сначала НОМЕР — он есть у каждого условия. Заголовок необязателен: если строка
# не начинается с заглавного зачина, условие всё равно своё, просто без имени.
NUMBERED = re.compile(r"^\s*(\d+)\.\s+(.*)$")
TITLED = re.compile(r"^([А-ЯЁA-Z][А-ЯЁA-Z0-9 ,«»№()/–—-]{2,70}?)\.\s*(.*)$")


def split_conditions(text):
    """Условия закрытия уже пронумерованы в тексте. Раскладываем по номерам;
    заголовок вынимаем, если он есть. Ни один номер не теряется."""
    if not text:
        return []
    out = []
    for line in text.split(chr(10)):
        if not line.strip():
            continue
        m = NUMBERED.match(line)
        if m:
            rest = m.group(2).strip()
            t = TITLED.match(rest)
            name = t.group(1).strip().capitalize() if t else None
            body = (t.group(2) if t else rest).strip()
            out.append({"no": m.group(1), "name": name, "text": body})
        elif out:
            out[-1]["text"] += chr(10) + line.strip()
        else:
            out.append({"no": None, "name": None, "text": line.strip()})
    return out


def node_events(direction, node_id):
    """Лента событий цели — из git. Подпись коммита содержит вид ноги и что сделано."""
    code, out = git("log", "--date=short", SEP.join(["--format=%h","%ad","%s"]),
                    f"--grep={node_id}", "--", f"live/{direction}")
    events = []
    if code != 0 or not out:
        return events
    for line in out.split(chr(10)):
        parts = line.split(SEP)
        if len(parts) != 3:
            continue
        sha, date, subject = parts
        kind, tone = "", ""
        for play, (word, t) in PLAY_WORD.items():
            if f" {play} " in subject:
                kind, tone = word, t
                break
        text = subject.split(":", 1)[1].strip() if ":" in subject else subject
        events.append({"sha": sha, "date": date, "kind": kind or "—",
                       "tone": tone, "text": text})
    return events


def goal_page(direction, node_id):
    with lock_for(direction):
        nodes, _ = load_cards(direction, kind="node")
    if node_id not in nodes:
        return None
    h, b = nodes[node_id]
    state, word = NODE_STATE.get(h.get("status"), ("ahead", str(h.get("status") or "?").upper()))

    def brief(cid):
        hh = (nodes.get(cid) or ({}, {}))[0]
        return {"id": cid, "label": hh.get("label") or cid,
                "dropped": hh.get("status") == "dropped"}

    kids = [brief(i) for i, (hh, _) in nodes.items() if hh.get("_parent") == node_id]
    return {
        "id": node_id, "state": state, "word": word, "raw_status": h.get("status"),
        "label": h.get("label") or node_id, "hook": h.get("hook"),
        "label_by": h.get("label_by"),
        "goal": h.get("goal") or block_text(b, "goal"),
        "why": h.get("why") or block_text(b, "why"),
        "conditions": split_conditions(h.get("done_when") or block_text(b, "done_when")),
        "detail": h.get("detail"),
        "parent": brief(h["_parent"]) if h.get("_parent") else None,
        "children": kids,
        "events": node_events(direction, node_id),
    }


def section_wave(direction):
    """Ставка, полосы и задачи. Принадлежность полосе сегодня живёт списком внутри
    полосы, а не полем задачи — читаем как есть и показываем задачи вне полос отдельно,
    чтобы расхождение было видно, а не съедено."""
    with lock_for(direction):
        loaded, unread = load_cards(direction)
    now = read_now(direction)
    # Полосы — карточки вида `track`, а не ключ NOW.md: после реза его там нет,
    # и `now.get("tracks")` молча возвращал пустоту вместо настоящих полос.
    tracks_raw = [dict(h, tasks=h.get("tasks") or cards.body_value(i, "tasks", b.get("tasks") or []))
                  for i, (h, b) in sorted(loaded.items(), key=lambda kv: kv[0])
                  if h.get("_kind") == "track"]
    tasks = {i: c for i, c in loaded.items() if c[0].get("_kind") == "task"}
    bet_card = next((c for c in loaded.values() if c[0].get("_kind") == "bet"), None)

    def task_view(tid):
        c = tasks.get(tid)
        if c is None:
            return {"id": tid, "missing": True, "status": None, "goal": None,
                    "order": None, "done": False}
        h, b = c
        goal = h.get("goal") or block_text(b, "goal")
        # `done` — однозначный признак, а не догадка по статусу: карточка может
        # быть закрыта и лежать в closed/ вообще без терминального статуса.
        # Блок `closed` рядом — это ТЕКСТ разбора, а не флаг; имена похожи, смысл разный.
        return {"id": tid, "missing": False, "status": h.get("status"),
                "done": is_done(h), "outcome": outcome(h),
                "in_closed": bool(h.get("_closed")),
                "order": h.get("order"), "goal": goal,
                "done_when": block_text(b, "done_when"),
                "closed": block_text(b, "closed"),
                "unblock_when": h.get("unblock_when") or block_text(b, "unblock_when")}

    seen, out_tracks = set(), []
    for t in tracks_raw:
        ids = list(t.get("tasks") or [])
        seen.update(ids)
        rows = sorted((task_view(i) for i in ids),
                      key=lambda r: (r["order"] is None, r["order"] or 0))
        out_tracks.append({
            "id": t.get("id"), "label": t.get("label"),
            "note": t.get("completed") or t.get("emptied") or t.get("frontier_note"),
            "tasks": rows,
            "done": sum(1 for r in rows if r["status"] == "done"),
            "total": len(rows),
        })
    loose = sorted((task_view(i) for i in tasks if i not in seen),
                   key=lambda r: (r["order"] is None, r["order"] or 0))

    bet = None
    if bet_card:
        h, b = bet_card
        bet = {"id": h.get("id"), "opened": h.get("opened"),
               "goal": h.get("goal") or block_text(b, "goal"),
               "description": h.get("description") or block_text(b, "description"),
               "description_by": h.get("description_by") or block_text(b, "description_by"),
               "appetite": block_text(b, "appetite"), "cuts": block_text(b, "cuts")}

    total = len(tasks)
    return {"direction": direction, "bet": bet, "tracks": out_tracks, "loose": loose,
            "unread": unread,
            "numbers": {"tasks_done": sum(1 for c in tasks.values() if is_done(c[0])),
                        "tasks_dropped": sum(1 for c in tasks.values()
                                             if outcome(c[0]) == "dropped"),
                        # закрыто, но чем кончилось — не записано: пробел показываем
                        "tasks_closed_unnamed": sum(1 for c in tasks.values()
                                                    if outcome(c[0]) == "closed"),
                        "tasks_total": total,
                        "tracks_total": len(out_tracks),
                        "tracks_limit": now_field(now, "track_wip_limit")}}


# Всё, из чего строятся карточки. Забыть здесь файл — значит показывать вчерашнее
# и не знать об этом: карточки собраны, папка свежая, а источник ушёл вперёд.
def block_text(blocks, key):
    """Текст блока тела: только объединение строк."""
    lines = blocks.get(key)
    return "\n".join(lines) if isinstance(lines, list) else None


def value_of(head, blocks, key):
    """Значение поля из шапки или из блока тела, дословно; нет или пусто — None."""
    v = head.get(key)
    if v in (None, ""):
        v = block_text(blocks, key)
    return None if v in (None, "") else v


def status_rank(status):
    return STATUS_ORDER.index(status) if status in STATUS_ORDER else len(STATUS_ORDER)


def make_order(direction, head, blocks, tasks):
    """Наряд для раздела «Сейчас» — вид, описанный в контракте этапа."""
    track = head.get("track")
    launch = f"collect next for {direction}/{track}" if track else f"collect next for {direction}"
    title, title_source = head.get("id"), "self"
    task = tasks.get(head.get("for"))
    if task is not None:
        goal = task[0].get("goal") or block_text(task[1], "goal")
        if goal:
            title, title_source = goal, "task"
    fields = [{"name": name, "text": "\n".join(lines)} for name, lines in blocks.items()]
    return {"id": head.get("id"), "status": head.get("status"), "track": track,
            "for": head.get("for"), "title": title, "title_source": title_source,
            "why": value_of(head, blocks, "unblock_when"),
            "description": value_of(head, blocks, "description"),
            "description_by": value_of(head, blocks, "description_by"),
            "fields": fields, "head": head, "launch": launch}


def section_numbers(direction, loaded):
    """Числа верхнего уровня. Считаю буквально из карточек и указателя, не выдумывая."""
    now = read_now(direction)
    heads = [head for head, _ in loaded.values()]
    tasks = [h for h in heads if h.get("_kind") == "task"]
    busy = {h.get("track") for h in heads
            if h.get("_kind") == "call" and h.get("track")
            and not is_done(h) and h.get("status") != "paused"}
    waiting = sum(1 for h in heads if h.get("_kind") == "decision" and not is_done(h))
    waiting += sum(1 for h in heads if h.get("_kind") == "question" and h.get("who") == "владелец")
    bet = next((h for h in heads if h.get("_kind") == "bet"), None)
    opened = bet.get("opened") if bet is not None else None
    if isinstance(opened, datetime.datetime):
        opened = opened.date()
    bet_days = (datetime.date.today() - opened).days if isinstance(opened, datetime.date) else None
    return {"tasks_done": sum(1 for h in tasks if is_done(h)),
            "tasks_total": len(tasks), "tracks_busy": len(busy),
            "tracks_limit": now_field(now, "track_wip_limit"),
            "waiting_for_you": waiting, "bet_days": bet_days}


def section_now(direction):
    with lock_for(direction):
        loaded, unread = load_cards(direction)
        tasks = {cid: v for cid, v in loaded.items() if v[0].get("_kind") == "task"}
        ready, other = [], []
        for cid, (head, blocks) in loaded.items():
            # «Сейчас» — про живое: отработавший наряд здесь не место, его след
            # в журнале сущности и в «Волне», где он считается сделанным.
            if head.get("_kind") != "call" or head.get("_closed"):
                continue
            order = make_order(direction, head, blocks, tasks)
            (ready if head.get("status") == "ready" else other).append(order)
        ready.sort(key=lambda o: (o["track"] or "", str(o["id"])))
        other.sort(key=lambda o: (status_rank(o["status"]), str(o["id"])))
        live_total = sum(1 for h, _ in loaded.values() if not h.get("_closed"))
        return {"direction": direction, "cards_total": live_total,
                "cards_closed": len(loaded) - live_total, "ready": ready,
                "other": other, "unread": unread,
                "numbers": section_numbers(direction, loaded)}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Отказ сборки карточек — это ответ с причиной, а не убитый поток.
        cards.fail бросает SystemExit, обычный except Exception его не ловит."""
        try:
            self.route(self.path.split("?", 1)[0])
        except (Exception, SystemExit) as e:
            sys.stderr.write(f"[panel] {self.path}: {e}\n")
            if self.path.startswith("/api/"):
                self.send_json({"error": str(e),
                                "hint": "проверь карточки: "
                                        "python osctl.py check --direction <направление>"},
                               code=500)
            else:
                self.send_error(500, "internal error")

    def route(self, path):
        if path == "/":
            self.send_file(os.path.join(APP_DIR, "index.html"))
        elif path in ("/app.js", "/md.js", "/style.css"):
            self.send_file(os.path.join(APP_DIR, path.lstrip("/")))
        elif path == "/api/state":
            self.send_json({"build": build_info(), "directions": directions()})
        elif path.startswith("/api/goal/"):
            parts = [urllib.parse.unquote(p) for p in path[len("/api/goal/"):].split("/") if p]
            page = None
            if len(parts) == 2 and os.path.isdir(os.path.join(LIVE_DIR, parts[0])):
                page = goal_page(parts[0], parts[1])
            if page is None:
                self.send_error(404, "not found")
            else:
                self.send_json(page)
        elif path.startswith("/api/section/"):
            parts = [urllib.parse.unquote(p) for p in path[len("/api/section/"):].split("/") if p]
            ok_dir = len(parts) == 2 and os.path.isdir(os.path.join(LIVE_DIR, parts[0]))
            if ok_dir and parts[1] == "now":
                self.send_json(section_now(parts[0]))
            elif ok_dir and parts[1] == "slots":
                self.send_json(section_slots(parts[0]))
            elif ok_dir and parts[1] == "wave":
                self.send_json(section_wave(parts[0]))
            elif ok_dir and parts[1] == "goals" and len(parts) == 2:
                self.send_json(section_goals(parts[0]))
            else:
                self.send_error(404, "not found")
        else:
            self.send_error(404, "not found")

    def send_file(self, full_path):
        if not os.path.isfile(full_path):
            self.send_error(404, "not found")
            return
        with open(full_path, "rb") as fh:
            data = fh.read()
        ext = os.path.splitext(full_path)[1]
        self.send_body(CONTENT_TYPES.get(ext, "application/octet-stream"), data)

    def send_json(self, obj, code=200):
        # default=str: в шапках карточек бывают datetime.date, на них dumps падает.
        self.send_body("application/json; charset=utf-8",
                       json.dumps(obj, ensure_ascii=False, default=str).encode("utf-8"), code)

    def send_body(self, ctype, data, code=200):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        pass


def main():
    parser = argparse.ArgumentParser(description="Панель направлений")
    parser.add_argument("--port", type=int, default=8787)
    parser.add_argument("--no-open", action="store_true", help="не открывать браузер")
    args = parser.parse_args()

    # Прогрева больше нет: карточки лежат готовыми, собирать при старте нечего.
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    url = f"http://127.0.0.1:{args.port}/"
    print(f"панель: {url}  (Ctrl+C — остановить)")
    if not args.no_open:
        webbrowser.open(url)
    try:
        thread.join()
    except KeyboardInterrupt:
        server.shutdown()


if __name__ == "__main__":
    main()
