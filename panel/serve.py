"""Локальный сервер панели: страница выбора направления + страница направления.
Только стандартная библиотека. Запуск: python panel/serve.py [--port N] [--no-open]"""
import argparse
import json
import os
import subprocess
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.join(ROOT, "panel", "app")
LIVE_DIR = os.path.join(ROOT, "live")

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


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/":
            self.send_file(os.path.join(APP_DIR, "index.html"))
        elif path in ("/app.js", "/style.css"):
            self.send_file(os.path.join(APP_DIR, path.lstrip("/")))
        elif path == "/api/state":
            self.send_json({"build": build_info(), "directions": directions()})
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
        data = json.dumps(obj, ensure_ascii=False).encode("utf-8")
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
