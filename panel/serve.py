"""Локальный сервер панели: выбор направления, страница направления, раздел «Сейчас».
Только стандартная библиотека + panel/cards.py. Запуск: python panel/serve.py [--port N] [--no-open]"""
import argparse
import json
import os
import subprocess
import threading
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import cards

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.join(ROOT, "panel", "app")
LIVE_DIR = os.path.join(ROOT, "live")
CARDS_DIR = os.path.join(ROOT, "panel", ".cards")

# Один общий список разделов для всех направлений: (id, подпись).
SECTIONS = [
    ("now", "СЕЙЧАС"),
    ("waiting", "ЖДЁТ ТЕБЯ"),
    ("wave", "ВОЛНА"),
    ("goals", "ЦЕЛИ"),
    ("history", "ИСТОРИЯ"),
    ("knowledge", "ЗНАНИЯ"),
    ("direction", "НАПРАВЛЕНИЕ"),
]

CONTENT_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".css": "text/css; charset=utf-8",
}

# Порядок статусов в списке «прочие наряды»; незнакомые статусы — после всех.
STATUS_ORDER = ["running", "waiting", "blocked", "paused"]

# По одному замку на направление: пересборка стирает папку карточек целиком,
# и многопоточный сервер без замка мог бы читать папку в момент стирания.
_DIR_LOCKS = {}
_META_LOCK = threading.Lock()


def lock_for(direction):
    with _META_LOCK:
        if direction not in _DIR_LOCKS:
            _DIR_LOCKS[direction] = threading.Lock()
        return _DIR_LOCKS[direction]


def git(*args):
    try:
        out = subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=10
        )
        return out.returncode, out.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return 1, ""


def build_info():
    _, commit = git("rev-parse", "--short", "HEAD")
    _, commit_date = git("log", "-1", "--format=%ad", "--date=short")
    code, count = git("rev-list", "--count", "origin/main..HEAD")
    try:
        unpushed = int(count) if code == 0 else 0
    except ValueError:
        unpushed = 0
    return {"commit": commit, "commit_date": commit_date, "unpushed": unpushed, "unread": 0}


def directions():
    names = sorted(
        name for name in os.listdir(LIVE_DIR)
        if os.path.isdir(os.path.join(LIVE_DIR, name))
    )
    return [
        {
            "id": name,
            "sections": [
                {"id": sid, "label": label, "ready": sid == "now"}
                for sid, label in SECTIONS
            ],
        }
        for name in names
    ]


def ensure_cards(direction):
    """Пересборка только если папки нет или NOW.md новее папки. Вызывать под замком."""
    folder = os.path.join(CARDS_DIR, direction)
    now_path = os.path.join(LIVE_DIR, direction, "NOW.md")
    if (os.path.isdir(folder) and os.path.isfile(now_path)
            and os.path.getmtime(now_path) <= os.path.getmtime(folder)):
        return
    cards.build(direction)  # сама стирает папку и строит заново


def block_text(blocks, key):
    """Текст блока тела: только объединение строк."""
    lines = blocks.get(key)
    return "\n".join(lines) if isinstance(lines, list) else None


def status_rank(status):
    return STATUS_ORDER.index(status) if status in STATUS_ORDER else len(STATUS_ORDER)


def make_order(direction, head, blocks, tasks):
    """Наряд для раздела «Сейчас» — вид, описанный в контракте этапа."""
    track = head.get("track")
    launch = f"collect next for {direction}/{track}" if track \
        else f"collect next for {direction}"
    title, title_source = head.get("id"), "self"
    task = tasks.get(head.get("for"))
    if task is not None:
        goal = task[0].get("goal") or block_text(task[1], "goal")
        if goal:
            title, title_source = goal, "task"
    why = head.get("unblock_when")
    if why is None:
        why = block_text(blocks, "unblock_when")
    fields = [{"name": name, "text": "\n".join(lines)} for name, lines in blocks.items()]
    return {
        "id": head.get("id"),
        "status": head.get("status"),
        "track": track,
        "for": head.get("for"),
        "title": title,
        "title_source": title_source,
        "why": why,
        "fields": fields,
        "head": head,
        "launch": launch,
    }


def section_now(direction):
    with lock_for(direction):
        ensure_cards(direction)
        folder = os.path.join(CARDS_DIR, direction)
        names = sorted(f for f in os.listdir(folder) if f.endswith(".md"))
        loaded, unread = {}, []
        for name in names:
            try:
                head, blocks = cards.read_card(os.path.join(folder, name))
            except (Exception, SystemExit) as e:
                # cards.fail бросает SystemExit — обычный except Exception не ловит.
                unread.append({"file": name, "error": str(e)})
                continue
            if isinstance(head, dict):
                loaded[str(head.get("id"))] = (head, blocks)
            else:
                unread.append({"file": name, "error": "шапка не словарь"})
        tasks = {cid: v for cid, v in loaded.items() if v[0].get("kind") == "task"}
        ready, other = [], []
        for cid, (head, blocks) in loaded.items():
            if head.get("kind") != "call":
                continue
            order = make_order(direction, head, blocks, tasks)
            (ready if head.get("status") == "ready" else other).append(order)
        ready.sort(key=lambda o: (o["track"] or "", str(o["id"])))
        other.sort(key=lambda o: (status_rank(o["status"]), str(o["id"])))
        return {
            "direction": direction,
            "cards_total": len(names),
            "ready": ready,
            "other": other,
            "unread": unread,
        }


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/":
            self.send_file(os.path.join(APP_DIR, "index.html"))
        elif path in ("/app.js", "/style.css"):
            self.send_file(os.path.join(APP_DIR, path.lstrip("/")))
        elif path == "/api/state":
            self.send_json({"build": build_info(), "directions": directions()})
        elif path.startswith("/api/section/"):
            parts = [urllib.parse.unquote(p)
                     for p in path[len("/api/section/"):].split("/") if p]
            if (len(parts) == 2 and parts[1] == "now"
                    and os.path.isdir(os.path.join(LIVE_DIR, parts[0]))):
                self.send_json(section_now(parts[0]))
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
        self.send_response(200)
        self.send_header("Content-Type", CONTENT_TYPES.get(ext, "application/octet-stream"))
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def send_json(self, obj):
        # default=str: в шапках карточек бывают datetime.date, на них dumps падает.
        data = json.dumps(obj, ensure_ascii=False, default=str).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
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

    # Один раз при старте: карточки каждого направления из live/.
    for name in sorted(os.listdir(LIVE_DIR)):
        if os.path.isdir(os.path.join(LIVE_DIR, name)):
            with lock_for(name):
                ensure_cards(name)

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
