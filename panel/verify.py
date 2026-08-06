"""Приёмка этапов панели. Пишется НЕ той моделью, что пишет код.

Запуск:  python panel/verify.py 00
Возврат: 0 — этап принят, 1 — нет. Никаких «не упало»: только конкретные числа.
"""
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 8787
BASE = f"http://127.0.0.1:{PORT}"

SECTIONS = ["now", "waiting", "wave", "goals", "history", "knowledge", "direction"]
DIRECTIONS = ["indie-game-development", "solmax"]

fails: list[str] = []


def check(ok: bool, msg: str) -> None:
    print(("OK   " if ok else "FAIL ") + msg)
    if not ok:
        fails.append(msg)


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True
    ).stdout.strip()


def fetch(path: str):
    with urllib.request.urlopen(BASE + path, timeout=10) as r:
        return r.status, r.read().decode("utf-8")


def step00() -> None:
    for rel in ("panel/serve.py", "panel/app/index.html", "panel/app/app.js", "panel/app/style.css"):
        check(os.path.isfile(os.path.join(ROOT, rel)), f"файл существует: {rel}")
    if fails:
        return

    css = open(os.path.join(ROOT, "panel/app/style.css"), encoding="utf-8").read()
    check("#c8ff33" in css, "стиль не перекрашен: акцент #c8ff33 на месте")
    check("#000000" in css, "стиль не перекрашен: фон #000000 на месте")

    html = open(os.path.join(ROOT, "panel/app/index.html"), encoding="utf-8").read()
    check("style.css" in html, "index.html подключает style.css")
    check("app.js" in html, "index.html подключает app.js")
    check("<style" not in html.lower(), "в index.html нет своих стилей — весь вид в style.css")

    proc = subprocess.Popen(
        [sys.executable, os.path.join(ROOT, "panel", "serve.py"), "--port", str(PORT), "--no-open"],
        cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    try:
        state = None
        for _ in range(40):
            try:
                st, body = fetch("/api/state")
                if st == 200:
                    state = json.loads(body)
                    break
            except (urllib.error.URLError, ConnectionError, json.JSONDecodeError):
                time.sleep(0.25)
        check(state is not None, "сервер поднялся и отдал /api/state как JSON")
        if state is None:
            return

        st, _ = fetch("/")
        check(st == 200, "корень / отдаёт страницу, код 200")

        b = state.get("build", {})
        check(b.get("commit") == git("rev-parse", "--short", "HEAD"),
              f"build.commit совпадает с git HEAD ({git('rev-parse', '--short', 'HEAD')})")
        check(isinstance(b.get("unpushed"), int), "build.unpushed — целое число")
        check(isinstance(b.get("unread"), int), "build.unread — целое число")

        dirs = state.get("directions", [])
        ids = [d.get("id") for d in dirs]
        check(ids == DIRECTIONS, f"направления ровно {DIRECTIONS}, найдено {ids}")

        for d in dirs:
            secs = [s.get("id") for s in d.get("sections", [])]
            check(secs == SECTIONS, f"{d.get('id')}: разделы в порядке {SECTIONS}, найдено {secs}")
            ready = [s.get("id") for s in d.get("sections", []) if s.get("ready")]
            check(ready == ["now"], f"{d.get('id')}: готов ровно один раздел now, найдено {ready}")

        # негативный контроль: пустой ответ не должен считаться успехом
        check(len(json.dumps(state)) > 200, "ответ не пустая заглушка")
    finally:
        proc.terminate()


def main() -> None:
    step = sys.argv[1] if len(sys.argv) > 1 else "00"
    {"00": step00}[step]()
    print(f"\n{'ПРИНЯТО' if not fails else 'НЕ ПРИНЯТО: ' + str(len(fails)) + ' проверок упало'}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
