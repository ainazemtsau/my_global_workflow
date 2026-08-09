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

SECTIONS = ["now", "slots", "waiting", "wave", "goals", "history", "knowledge", "direction"]
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


def port_is_free() -> bool:
    """Чужой сервер на этом порту — приёмка проверила бы не тот код и не заметила."""
    import socket
    with socket.socket() as s:
        s.settimeout(1)
        return s.connect_ex(("127.0.0.1", PORT)) != 0


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

    check(port_is_free(), f"порт {PORT} свободен — иначе проверялся бы чужой сервер")
    if fails:
        return
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
            check(ready == ["now", "slots", "wave", "goals"], f"{d.get('id')}: готовы now, slots, wave, goals — найдено {ready}")

        # негативный контроль: пустой ответ не должен считаться успехом
        check(len(json.dumps(state)) > 200, "ответ не пустая заглушка")
    finally:
        proc.terminate()




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


def step01b() -> None:
    import yaml

    ORDER = ["running", "waiting", "blocked", "paused"]

    def card_text(blocks, name):
        v = blocks.get(name)
        return "\n".join(v) if isinstance(v, list) else v

    def read_disk(direction):
        """Эталон читаем через cards.read_card — его точность доказана обратной
        сборкой на этапе 1a. Своя копия разбора срезала хвостовой перевод строки
        и уничтожала ровно ту разницу, ради которой формат и делался."""
        sys.path.insert(0, os.path.join(ROOT, "panel"))
        import cards
        live = os.path.join(ROOT, "live", direction, "cards")
        src = {}
        for folder, closed in ((live, False), (os.path.join(live, "closed"), True)):
            if not os.path.isdir(folder):
                continue
            for f in sorted(os.listdir(folder)):
                if not f.endswith(".md"):
                    continue
                head, blocks = cards.read_card(os.path.join(folder, f))
                head["_closed"] = closed   # эталон знает про закрытые, как и панель
                src[head["id"]] = (head, blocks, f)
        return src

    git_live_before = run("git", "status", "--porcelain", "live").stdout

    check(port_is_free(), f"порт {PORT} свободен — иначе проверялся бы чужой сервер")
    if fails:
        return
    proc = subprocess.Popen(
        [sys.executable, os.path.join(ROOT, "panel", "serve.py"), "--port", str(PORT), "--no-open"],
        cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    calls_by_dir = {}
    try:
        for direction in ("indie-game-development", "solmax"):
            data = None
            for _ in range(40):
                try:
                    st, body = fetch("/api/section/" + direction + "/now")
                    if st == 200:
                        data = json.loads(body)
                        break
                except (urllib.error.URLError, ConnectionError, json.JSONDecodeError):
                    time.sleep(0.25)
            check(data is not None, f"{direction}: ручка раздела отдала JSON, код 200")
            if data is None:
                return

            src = read_disk(direction)
            # «Сейчас» — про живое: закрытый наряд отработал, его место в журнале
            # сущности и в «Волне», где он считается сделанным.
            live = {i: v for i, v in src.items() if not v[0].get("_closed")}
            calls = {i: v for i, v in live.items() if v[0].get("_kind") == "call"}
            calls_by_dir[direction] = calls
            tasks = {i: v for i, v in src.items() if v[0].get("_kind") == "task"}
            ready, other = data.get("ready", []), data.get("other", [])
            got = {c["id"]: c for c in ready + other}

            check(data.get("cards_total") == len(live),
                  f"{direction}: cards_total {data.get('cards_total')}, живых на диске {len(live)}")
            check(data.get("cards_closed") == len(src) - len(live),
                  f"{direction}: cards_closed {data.get('cards_closed')}, "
                  f"закрытых на диске {len(src) - len(live)}")
            check(len(ready) + len(other) == len(calls),
                  f"{direction}: нарядов показано {len(ready) + len(other)}, на диске {len(calls)}")
            check(set(got) == set(calls), f"{direction}: показаны все наряды и только они")
            check(data.get("unread") == [], f"{direction}: unread пуст на исправных карточках")
            if set(got) != set(calls):
                continue

            ready_ids = {c["id"] for c in ready}
            want_ready = {i for i, v in calls.items() if v[0].get("status") == "ready"}
            check(ready_ids == want_ready,
                  f"{direction}: ready ровно те, у кого в шапке status ready")

            bad = []
            for cid, c in got.items():
                head, blocks, _ = calls[cid]
                for key in ("status", "for", "track"):
                    if c.get(key) != head.get(key):
                        bad.append(f"{cid}: {key} разошёлся с карточкой")
                tr = head.get("track")
                want_launch = ("collect next for " + direction + "/" + str(tr)) if tr \
                    else ("collect next for " + direction)
                if c.get("launch") != want_launch:
                    bad.append(f"{cid}: launch {c.get('launch')!r}")

                th = tasks.get(head.get("for"))
                goal = None
                if th is not None:
                    goal = th[0].get("goal") or card_text(th[1], "goal")
                want_title, want_src = (goal, "task") if goal else (cid, "self")
                if c.get("title") != want_title:
                    bad.append(f"{cid}: title {str(c.get('title'))[:40]!r} вместо {str(want_title)[:40]!r}")
                if c.get("title_source") != want_src:
                    bad.append(f"{cid}: title_source {c.get('title_source')!r} вместо {want_src!r}")

                want_why = head.get("unblock_when") or card_text(blocks, "unblock_when")
                if (c.get("why") or None) != (want_why or None):
                    bad.append(f"{cid}: why разошёлся с unblock_when")

                names = [f["name"] for f in c.get("fields", [])]
                if names != list(blocks):
                    bad.append(f"{cid}: список полей {names} вместо {list(blocks)}")
                else:
                    for f in c.get("fields", []):
                        if f.get("text") != card_text(blocks, f["name"]):
                            bad.append(f"{cid}:{f['name']} текст не дословный")
            check(not bad, f"{direction}: наряды совпадают с карточками на диске ({bad[:3]})")

            ranked = [ORDER.index(c.get("status")) if c.get("status") in ORDER else len(ORDER)
                      for c in other]
            check(ranked == sorted(ranked), f"{direction}: other отсортирован по статусу")

        for path, mark in (("/app.js", "function"), ("/style.css", "#c8ff33")):
            try:
                st, body = fetch(path)
            except Exception as e:
                st, body = 0, str(e)
            check(st == 200 and mark in body, f"маршрут {path} жив после переписывания")

        code = 0
        try:
            code, _ = fetch("/api/section/no-such-direction/now")
        except urllib.error.HTTPError as e:
            code = e.code
        except Exception as e:
            code = repr(e)
        check(code == 404, f"неизвестное направление отдаёт 404, отдало {code}")

        # Негативный контроль. NOW.md не трогаем — значит пересборки быть не должно
        # и подложенный файл доживёт до чтения. Если он пропал, реализация
        # пересобирает на каждый запрос, что запрещено §4.1.
        out = os.path.join(ROOT, "live", "indie-game-development", "cards")
        broken = os.path.join(out, "zz-broken.md")
        try:
            open(broken, "w", encoding="utf-8").write("---\nне: [ямл\n---\n")
            st, body = fetch("/api/section/indie-game-development/now")
            d2 = json.loads(body)
            names = [u.get("file") for u in d2.get("unread", [])]
            check("zz-broken.md" in names, f"негативный контроль: битая карточка попала в unread ({names})")
            check(len(d2.get("ready", []) + d2.get("other", [])) == len(calls_by_dir["indie-game-development"]),
                  "негативный контроль: остальные наряды всё равно дошли")
        finally:
            if os.path.exists(broken):
                os.remove(broken)
    finally:
        proc.terminate()

    check(run("git", "status", "--porcelain", "live").stdout == git_live_before,
          "live/ не изменился за прогон")


def step01c() -> None:
    import datetime

    import yaml

    def card_text(blocks, name):
        v = blocks.get(name)
        return "\n".join(v) if isinstance(v, list) else v

    def read_disk(direction):
        """Эталон читаем через cards.read_card — его точность доказана обратной
        сборкой на этапе 1a. Своя копия разбора срезала хвостовой перевод строки
        и уничтожала ровно ту разницу, ради которой формат и делался."""
        sys.path.insert(0, os.path.join(ROOT, "panel"))
        import cards
        live = os.path.join(ROOT, "live", direction, "cards")
        src = {}
        for folder, closed in ((live, False), (os.path.join(live, "closed"), True)):
            if not os.path.isdir(folder):
                continue
            for f in sorted(os.listdir(folder)):
                if not f.endswith(".md"):
                    continue
                head, blocks = cards.read_card(os.path.join(folder, f))
                head["_closed"] = closed   # эталон знает про закрытые, как и панель
                src[head["id"]] = (head, blocks)
        return src

    md = os.path.join(ROOT, "panel", "app", "md.js")
    check(os.path.isfile(md), "файл существует: panel/app/md.js")
    html = open(os.path.join(ROOT, "panel", "app", "index.html"), encoding="utf-8").read()
    check("md.js" in html, "index.html подключает md.js")
    if fails:
        return

    check(port_is_free(), f"порт {PORT} свободен — иначе проверялся бы чужой сервер")
    if fails:
        return
    proc = subprocess.Popen(
        [sys.executable, os.path.join(ROOT, "panel", "serve.py"), "--port", str(PORT), "--no-open"],
        cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    try:
        data = None
        for _ in range(40):
            try:
                st, body = fetch("/api/section/indie-game-development/now")
                if st == 200:
                    data = json.loads(body)
                    break
            except (urllib.error.URLError, ConnectionError, json.JSONDecodeError):
                time.sleep(0.25)
        check(data is not None, "ручка раздела отдала JSON")
        if data is None:
            return

        src = read_disk("indie-game-development")
        calls = {i: v for i, v in src.items() if v[0].get("_kind") == "call"}
        got = {c["id"]: c for c in data.get("ready", []) + data.get("other", [])}

        # описание: дословно из карточки, ниоткуда больше
        bad = []
        with_descr = 0
        for cid, c in got.items():
            head, blocks = calls[cid]
            want = head.get("description") or card_text(blocks, "description")
            if (c.get("description") or None) != (want or None):
                bad.append(f"{cid}: description разошёлся с карточкой")
            if want:
                with_descr += 1
            want_by = head.get("description_by") or card_text(blocks, "description_by")
            if (c.get("description_by") or None) != (want_by or None):
                bad.append(f"{cid}: description_by разошёлся")
        check(not bad, f"описания дословны ({bad[:3]})")
        # Наличие описания — свойство ДАННЫХ, а не кода: новый наряд может прийти без него,
        # и панель обязана честно написать «описания нет». Проверяем дословность, не наличие.
        print(f"     справка: описание есть у {with_descr} нарядов из {len(calls)}")

        # числа: считаем сами из карточек и NOW.md
        now = yaml.safe_load(open(os.path.join(ROOT, "live", "indie-game-development", "NOW.md"),
                                  encoding="utf-8").read())
        tasks = {i: v for i, v in src.items() if v[0].get("_kind") == "task"}
        bets = [v for v in src.values() if v[0].get("_kind") == "bet"]
        want_num = {
            "tasks_total": len(tasks),
            # «сделано» — ТОЛЬКО статус done. Закрытая без исхода сделанной не
            # считается: `t-scale-2` сняли его словом, и звать это сделанным —
            # ложь на экране. Прежняя строка считала любую закрытую.
            "tasks_done": sum(1 for v in tasks.values() if v[0].get("status") == "done"),
            "tracks_limit": now.get("track_wip_limit"),
            "tracks_busy": len({v[0].get("track") for v in calls.values()
                                if v[0].get("track") and v[0].get("status") not in ("done", "paused")}),
            "waiting_for_you": sum(1 for v in src.values() if v[0].get("_kind") == "decision")
                               + sum(1 for v in src.values()
                                     if v[0].get("_kind") == "question" and v[0].get("who") == "владелец"),
        }
        n = data.get("numbers") or {}
        for k, v in want_num.items():
            check(n.get(k) == v, f"numbers.{k} = {n.get(k)}, посчитано {v}")

        opened = bets[0][0].get("opened") if bets else None
        if isinstance(opened, datetime.date):
            want_days = (datetime.date.today() - opened).days
            check(n.get("bet_days") == want_days, f"numbers.bet_days = {n.get('bet_days')}, посчитано {want_days}")
        else:
            check(n.get("bet_days") is None, "numbers.bet_days = null, когда ставки или даты нет")

        st, body = fetch("/api/section/solmax/now")
        d2 = json.loads(body)
        n2 = d2.get("numbers") or {}
        check(n2.get("tasks_total") == 0 and n2.get("bet_days") is None,
              f"solmax: числа нулевые и bet_days null ({n2})")

        # СВЕЖЕСТЬ. Раньше проверяли, что правка источника вызывает пересборку
        # кэша. Кэша больше нет — панель читает карточку на каждый запрос.
        # Отсутствие кэша и мёртвых адресов сторожит panel/test_readers.py:
        # у одного правила один хозяин, иначе две копии однажды разойдутся.
        # Здесь остаётся ПОВЕДЕНЧЕСКАЯ половина: правка карточки видна сразу.
        import os as _os
        probe = _os.path.join(ROOT, "live", "indie-game-development", "cards", "g-5a7c.md")
        if _os.path.isfile(probe):
            before_bytes = open(probe, "rb").read()
            _, body_before = fetch("/api/section/indie-game-development/goals")
            marker = "ПРОБА-СВЕЖЕСТИ".encode()
            # Концы строк в рабочей копии бывают и CRLF, и LF — git выдаёт по
            # своим настройкам. Проба, знающая только один вид, молча не находит
            # места правки и «падает» не на том, что проверяет.
            eol = b"\r\n" if b"\r\n" in before_bytes else b"\n"
            head = b"## goal" + eol
            check(head in before_bytes, "свежесть: место правки найдено в карточке")
            try:
                # правим блок `## goal` — его панель читает ИЗ КАРТОЧКИ
                # (имя цели приходит накладкой, на нём проба ничего бы не показала)
                open(probe, "wb").write(
                    before_bytes.replace(head, head + marker + b" ", 1))
                _, body_after = fetch("/api/section/indie-game-development/goals")
                check(marker.decode() in body_after and body_after != body_before,
                      "свежесть: правка карточки видна на следующем же запросе")
            finally:
                open(probe, "wb").write(before_bytes)
                check(open(probe, "rb").read() == before_bytes,
                      "свежесть: байты карточки восстановлены проверкой")

        st, body = fetch("/md.js")
        check(st == 200 and "mdToHtml" in body, "маршрут /md.js отдаёт отрисовщик")

        # отрисовщик markdown: экранирование обязательно, разметка минимальна
        import re
        js = open(md, encoding="utf-8").read()
        check("&lt;" in js or "&amp;" in js or "replace(/&/" in js,
              "md.js экранирует угловые скобки и амперсанд")
        for token in ("<script", "innerHTML = text", "href"):
            check(token not in js.replace(" ", "") or token == "href",
                  f"md.js не собирает опасную разметку ({token})")
        check(not re.search(r"<a\s", js), "md.js не делает ссылок")
    finally:
        proc.terminate()


STEPS = {"00": step00, "01b": step01b, "01c": step01c}


def main() -> None:
    """Без аргумента гоняются ВСЕ шаги. Пока по умолчанию шёл один, три других
    молчали, и «приёмка ПРИНЯТО» означала четверть проверок."""
    names = sys.argv[1:] or list(STEPS)
    for name in names:
        if name not in STEPS:
            print(f"нет такого шага: {name}; есть {list(STEPS)}")
            sys.exit(2)
        print(f"\n=== шаг {name} ===")
        STEPS[name]()
    print(f"  шагов пройдено: {len(names)} ({', '.join(names)})")
    print(f"\n{'ПРИНЯТО' if not fails else 'НЕ ПРИНЯТО: ' + str(len(fails)) + ' проверок упало'}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
