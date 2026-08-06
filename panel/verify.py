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


SECTIONS_TO_CARDS = ("tasks", "open_calls", "issues", "decisions")


def run(*args: str):
    """Дочерний процесс пишет UTF-8; локаль здесь cp1252, поэтому кодировку задаём явно."""
    return subprocess.run(list(args), cwd=ROOT, capture_output=True,
                          text=True, encoding="utf-8", errors="replace")


def head_belongs(v) -> bool:
    """Правило раскладки §4.2 — единственное место, где оно записано кодом."""
    import datetime
    if isinstance(v, str):
        return len(v) <= 120 and "\n" not in v
    return isinstance(v, (int, float, bool, datetime.date)) or v is None


def step01a() -> None:
    import shutil

    import yaml

    script = os.path.join(ROOT, "panel", "cards.py")
    check(os.path.isfile(script), "файл существует: panel/cards.py")
    if fails:
        return

    now_paths = {d: os.path.join(ROOT, "live", d, "NOW.md")
                 for d in ("indie-game-development", "solmax")}
    before_bytes = {d: open(p, "rb").read() for d, p in now_paths.items()}
    git_before = run("git", "status", "--porcelain", "live").stdout

    for direction in ("indie-game-development", "solmax"):
        out = os.path.join(ROOT, "panel", ".cards", direction)
        shutil.rmtree(out, ignore_errors=True)
        os.makedirs(out, exist_ok=True)
        # маркер: build обязан вычистить папку сам, а не дописать в неё
        open(os.path.join(out, "zz-stale.md"), "w", encoding="utf-8").write("stale\n")

        r = run(sys.executable, script, "build", direction)
        check(r.returncode == 0, f"{direction}: build завершился кодом 0")
        if r.returncode != 0:
            print("    ", (r.stdout + r.stderr).strip()[:400])
            continue

        check(os.path.isdir(out), f"{direction}: папка карточек создана даже при нуле карточек")
        if not os.path.isdir(out):
            continue
        names = os.listdir(out)
        check("zz-stale.md" not in names, f"{direction}: build вычистил папку от прошлого прогона")

        now = yaml.safe_load(open(now_paths[direction], encoding="utf-8").read())
        bet = now.get("bet")
        bet_ok = isinstance(bet, dict) and "node" in bet
        want = sum(len(now.get(k) or []) for k in SECTIONS_TO_CARDS) + (1 if bet_ok else 0)
        files = sorted(f for f in names if f.endswith(".md"))
        check(len(files) == want, f"{direction}: карточек {len(files)}, ожидалось {want}")

        # ожидаемая раскладка, посчитанная из исходника независимо от реализации
        expected: dict[str, dict] = {}
        if bet_ok:
            expected[bet["node"]] = dict(bet)
        for sec in SECTIONS_TO_CARDS:
            for rec in (now.get(sec) or []):
                expected[str(rec.get("id"))] = dict(rec)

        heads: dict[str, dict] = {}
        bad_head, bad_trailer, bad_place = [], [], []
        for f in files:
            text = open(os.path.join(out, f), encoding="utf-8").read()
            parts = text.split("---", 2)
            head = yaml.safe_load(parts[1]) if len(parts) > 2 else None
            if not isinstance(head, dict):
                bad_head.append(f + " (шапка не разобралась)")
                continue
            heads[f] = head
            if "id" not in head or "kind" not in head:
                bad_head.append(f + " (нет id или kind)")
            for k, v in head.items():
                if isinstance(v, (list, dict)) or (isinstance(v, str) and (len(v) > 120 or "\n" in v)):
                    bad_head.append(f"{f}:{k} (не место в шапке)")
            if not text.rstrip().endswith(f"END_OF_FILE: panel/.cards/{direction}/{f}"):
                bad_trailer.append(f)

            # §4.2 соблюдён: короткое — в шапке, длинное — в теле, и наоборот
            src = expected.get(f[:-3])
            if src is not None:
                body_names = {ln[3:].strip() for ln in text.splitlines() if ln.startswith("## ")}
                for k, v in src.items():
                    if head.get("kind") == "bet" and k == "node":
                        continue
                    if head_belongs(v):
                        if k not in head:
                            bad_place.append(f"{f}:{k} должно быть в шапке")
                    elif k not in body_names:
                        bad_place.append(f"{f}:{k} должно быть в теле")

        check(not bad_head, f"{direction}: шапки чистые ({bad_head[:3]})")
        check(not bad_trailer, f"{direction}: у всех карточек свой END_OF_FILE ({bad_trailer[:3]})")
        check(not bad_place, f"{direction}: правило раскладки соблюдено ({bad_place[:3]})")

        bad_name = [f for f, h in heads.items() if h.get("id") != f[:-3]]
        check(not bad_name, f"{direction}: имя файла совпадает с id ({bad_name[:3]})")
        check(sorted(heads) == files, f"{direction}: все карточки разобрались ({len(heads)} из {len(files)})")

        r = run(sys.executable, script, "check", direction)
        check(r.returncode == 0 and "СОВПАДАЕТ" in (r.stdout or ""),
              f"{direction}: обратная сборка совпадает с NOW.md")
        if r.returncode != 0:
            print("    ", ((r.stdout or "") + (r.stderr or "")).strip()[:400])

    if fails:
        return

    # три негативных контроля: check обязан упасть на каждом
    out = os.path.join(ROOT, "panel", ".cards", "indie-game-development")
    cards = sorted(f for f in os.listdir(out) if f.endswith(".md"))
    victim = os.path.join(out, next(f for f in cards if f.startswith("t-")))
    saved = open(victim, encoding="utf-8").read()

    def broken_check(label: str, mutate) -> None:
        try:
            mutate()
            r = run(sys.executable, script, "check", "indie-game-development")
            check(r.returncode != 0, f"негативный контроль: {label} роняет check")
        finally:
            open(victim, "w", encoding="utf-8").write(saved)

    broken_check("испорченная шапка",
                 lambda: open(victim, "w", encoding="utf-8").write(saved.replace("status:", "status_X:", 1)))
    broken_check("изменённое тело",
                 lambda: open(victim, "w", encoding="utf-8").write(
                     saved.replace("END_OF_FILE:", "хвост подделан\n\nEND_OF_FILE:", 1)))
    broken_check("удалённая карточка", lambda: os.remove(victim))

    # NOW.md не менялся во время прогона и live/ не тронут
    for d, p in now_paths.items():
        check(open(p, "rb").read() == before_bytes[d], f"{d}: NOW.md не менялся во время прогона")
    check(run("git", "status", "--porcelain", "live").stdout == git_before,
          "live/ не изменился ни на байт")


def main() -> None:
    step = sys.argv[1] if len(sys.argv) > 1 else "00"
    {"00": step00, "01a": step01a}[step]()
    print(f"\n{'ПРИНЯТО' if not fails else 'НЕ ПРИНЯТО: ' + str(len(fails)) + ' проверок упало'}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
