# -*- coding: utf-8 -*-
"""Приёмка на КЛАСС поломки, а не на её случаи: читатель, переживший источник.

Форма отказа одна и та же трижды подряд. Мир менялся — файл удалялся, ключ
переезжал в карточку, папка снималась, — а читающий код оставался и получал
ПУСТОТУ вместо ошибки:

  1. `osctl leg close` писал в удалённый `LOG.md` — падал на половине;
  2. `panel/verify.py` сравнивал панель со снятой папкой-проекцией;
  3. панель читала `NOW.tracks` и `NOW.direction_forecast`, которых там нет,
     и показывала ноль полос при живой ставке.

Пустота не отличима от «нечего показывать», поэтому ни одна приёмка не упала.
Здесь проверяется само СОГЛАСИЕ кода с объявленной моделью — по коду, а не по
поведению, и потому ловится до того, как владелец увидит пустой экран.

    python panel/test_readers.py
"""
import ast
import io
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "panel"))
import cards      # noqa: E402
import osctl      # noqa: E402

WATCHED = ("panel/serve.py", "osctl.py", "panel/verify.py", "panel/cards.py")
fails = []


def check(ok, msg):
    print(("OK   " if ok else "FAIL ") + msg)
    if not ok:
        fails.append(msg)


def source(rel):
    return io.open(ROOT / rel, encoding="utf-8").read()


def code_text(rel):
    """Только КОД: комментарии и строки-описания выброшены токенайзером, а не
    угадыванием по кавычкам. Комментарий, ЦИТИРУЮЩИЙ снятое обращение, — это
    объяснение, а не обращение, и считать его дефектом было бы неправдой."""
    import tokenize
    out = []
    with tokenize.open(ROOT / rel) as fh:
        for tok in tokenize.generate_tokens(fh.readline):
            if tok.type in (tokenize.COMMENT, tokenize.NL):
                continue
            if tok.type == tokenize.STRING and tok.line.strip().startswith(tok.string[:3]):
                continue          # строка-описание, стоящая отдельным выражением
            out.append((tok.start[0], tok.line))
    seen, lines = set(), []
    for n, line in out:
        if n not in seen:
            seen.add(n)
            lines.append((n, line.split("#", 1)[0]))
    return lines


def case_now_fields():
    """Чтение ключа указателя, которого нет в закрытом списке, — тот самый класс."""
    allowed = set(osctl.NOW_FIELDS)
    bad = []
    for rel in WATCHED:
        for n, line in code_text(rel):
            for m in re.finditer(r'now\.get\(\s*"([^"]+)"', line):
                if m.group(1) not in allowed:
                    bad.append(f"{rel}:{n} now.get({m.group(1)!r})")
    check(not bad, f"никто не читает из указателя чужих ключей ({bad[:3]})")

    for d in sorted(p.name for p in (ROOT / "live").iterdir() if p.is_dir()):
        try:
            data = osctl.read_now(d)
        except osctl.Stop as e:
            check(False, f"{d}: указатель не читается — {e}")
            continue
        extra = [k for k in data if k not in allowed]
        check(not extra, f"{d}: в указателе только объявленные поля (лишние: {extra})")


def case_kinds():
    """Сравнение с несуществующим видом карточки даёт вечный ноль и молчит.

    Список берётся у `osctl`, а не переписывается сюда: свой экземпляр уже
    отстал — `idea` появился в `CARD_KINDS`, а здесь стояло `| {"question"}`,
    и живой код пришлось бы обходить стороной вместо того, чтобы писать прямо.
    """
    known = set(osctl.CARD_KINDS)
    bad = []
    for rel in WATCHED:
        for n, line in code_text(rel):
            for m in re.finditer(r'_kind"\)\s*==\s*"([^"]+)"', line):
                if m.group(1) not in known:
                    bad.append(f"{rel}:{n} _kind == {m.group(1)!r}")
    check(not bad, f"никто не сравнивает с неизвестным видом карточки ({bad[:3]})")


def case_paths():
    """Путь под live/, названный строкой, обязан существовать у каждого направления."""
    dirs = sorted(p.name for p in (ROOT / "live").iterdir() if p.is_dir())
    # Обязательны только те, без которых направления нет. `knowledge/`, `history/`
    # и `work/` появляются с первой записью: git не хранит пустых папок, поэтому
    # требовать их у свежего направления значит требовать невозможного. Свежее
    # направление `direction-os` (2026-08-11) поймало это на первом же слиянии,
    # и панель на нём при этом работает — раздел просто отдаёт ноль.
    MUST = ("CHARTER.md", "NOW.md", "cards")
    bad = []
    for rel in WATCHED:
        for n, line in code_text(rel):
            for m in re.finditer(r'LIVE_DIR,\s*direction,\s*"([^"]+)"', line):
                if m.group(1) not in MUST:
                    continue
                for d in dirs:
                    if not (ROOT / "live" / d / m.group(1)).exists():
                        bad.append(f"{rel}:{n} live/{d}/{m.group(1)}")
    check(not bad, f"каждый обязательный файл направления существует ({bad[:3]})")


def case_head_keys_exist():
    """Читатель не спрашивает у карточки поля, которого нет ни в одной карточке.

    Случай 2026-08-11: и панель, и приёмка считали ждущих владельца по полю
    `who`. Поля `who` не существует — отвечающий лежит в `asks`. Обе стороны
    молча получали ноль вопросов, и обе показывали неверное число, СОГЛАСОВАННО
    неверное: приёмка не могла поймать то, что читала так же неправильно.

    Тот же класс, что `NOW.tracks` и `LOG.md`: пустота неотличима от «нечего
    показывать». Список полей берётся у `osctl`, второго экземпляра нет.
    """
    # `order` — не законное поле, а ДРЕЙФ: восемь задач несут его рядом с `_pos`
    # с другим значением. Панель его пока читает, чтобы не сломать эти карточки;
    # `osctl check` называет их каждым прогоном, и когда нога `repair` их почистит,
    # эта поблажка уходит вместе с чтением. Записано здесь, а не в списке известных,
    # чтобы дрейф не стал законным молча.
    known = set(osctl.KNOWN_HEAD) | {"_closed", "order"}
    bad = []
    for rel in WATCHED:
        for n, line in code_text(rel):
            for m in re.finditer(r'\b(?:h|head|card)\.get\(\s*"([a-z_][a-z_0-9]*)"', line):
                if m.group(1) not in known:
                    bad.append(f"{rel}:{n} .get({m.group(1)!r})")
    check(not bad, f"никто не спрашивает у шапки несуществующее поле ({bad[:4]})")


def case_dead_dirs():
    """Снятая папка не должна оставаться адресом ни в одном читателе."""
    dead = (".cards", "TREE.md", "LOG.md")
    bad = []
    for rel in WATCHED:
        for n, line in code_text(rel):
            for token in dead:
                if f'"{token}"' in line or f"'{token}'" in line:
                    bad.append(f"{rel}:{n} {token}")
    check(not bad, f"снятых адресов в коде не осталось ({bad[:4]})")
    check(not (ROOT / "panel" / ".cards").exists(),
          "и папки-проекции нет — кэшу негде отстать")


def case_closed_is_visible():
    """Закрытое видно как закрытое, с НАЗВАННЫМ исходом, а не исчезает из обоих чисел."""
    sys.path.insert(0, str(ROOT / "panel"))
    import serve
    d = "indie-game-development"
    live = {p.stem for p in (ROOT / "live" / d / "cards").glob("*.md")}
    shut = {p.stem for p in (ROOT / "live" / d / "cards" / "closed").glob("*.md")}
    loaded, _ = serve.load_cards(d)
    check(set(loaded) == live | shut,
          f"загружаются обе папки: живых {len(live)}, закрытых {len(shut)}, "
          f"загружено {len(loaded)}")
    if not shut:
        return
    tasks = [h for h, _ in loaded.values() if h.get("_kind") == "task"]
    on_disk = sum(1 for cid in live | shut
                  if (loaded.get(cid) or ({},))[0].get("_kind") == "task")
    check(len(tasks) == on_disk,
          f"задачи считаются из обеих папок: {len(tasks)} из {on_disk} на диске")

    closed_tasks = [h for h in tasks if h.get("_closed")]
    check(closed_tasks, "закрытые задачи вообще есть — иначе проверять нечего")
    # Закрытая задача обязана иметь НАЗВАННЫЙ исход. «Сделано» — только `done`:
    # `t-scale-2` сняли его словом, и звать это сделанным было бы ложью на экране.
    check(all(serve.outcome(h) for h in closed_tasks),
          "у каждой закрытой задачи есть исход (done/dropped/closed)")
    check(all(not serve.is_done(h) for h in tasks if h.get("status") != "done"),
          "«сделано» не приписывается тому, у кого статус не done")
    check(all(serve.outcome(h) is None for h in tasks if not h.get("_closed")
              and h.get("status") not in ("done", "dropped")),
          "у живой незакрытой задачи исхода нет — панель не выдумывает завершения")


def case_no_second_source():
    """У поля карточки не бывает второго источника.

    Накладка `os2/labels/` жила рядом с карточками, и панель читала ЕЁ, а
    карточку игнорировала: переименование командой не дошло бы до экрана, и
    никто бы не узнал. Совпадали они ровно до первого расхождения.
    """
    check(not (ROOT / "os2" / "labels").exists(),
          "накладки имён нет — у неё был назван конец, и он наступил")
    bad = []
    for rel in WATCHED:
        for n, line in code_text(rel):
            if "os2" in line and "labels" in line:
                bad.append(f"{rel}:{n}")
    check(not bad, f"никто её больше не читает ({bad[:3]})")

    sys.path.insert(0, str(ROOT / "panel"))
    import serve
    nodes, _ = serve.load_cards("indie-game-development", kind="node")
    named = [h for h, _ in nodes.values() if h.get("label")]
    check(named, f"имена целей лежат в карточках ({len(named)} из {len(nodes)})")
    # Чьи это слова — обязано ехать вместе с ними: имена писал не владелец.
    check(all(h.get("label_by") for h in named),
          "у каждого имени записано, кем оно написано")


def case_idea_keeps_its_author():
    """У идеи всегда видно, ЧЬЯ она, и незаполненное авторство не выдумывается.

    Это тот же закон, что у имён целей (`label_by`): его отложенное содержание и
    выдумка ноги не имеют права выглядеть одинаково. Проверяется разбор напрямую —
    живых идей сегодня ноль, и без этого случая функция была бы написана и
    никогда не проверена.
    """
    sys.path.insert(0, str(ROOT / "panel"))
    import serve
    row = serve.idea_row("idea-1", {"_kind": "idea", "from": "владелец", "about": "g-1",
                                    "source": "history/x.md"},
                         {"idea": ["музыкальная шкатулка"], "his_words": ["влетела, коснулась"]})
    check(row["from"] == "владелец", "авторство едет в строке дословно")
    check(row["text"] and "шкатулка" in row["text"], "текст идеи доходит")
    check(row["his_words"] and "влетела" in row["his_words"], "и его слова отдельно от пересказа")
    check(row["about"] == "g-1" and row["source"] == "history/x.md",
          "привязка и источник доходят — иначе идею негде найти и нечем проверить")

    bare = serve.idea_row("idea-2", {"_kind": "idea"}, {"idea": ["без автора"]})
    check(bare["from"] is None,
          "автор не проставлен — панель НЕ угадывает, что это его слова")
    check(bare["his_words"] is None, "и цитаты нет, когда её нет")


def case_look_lives_only_in_the_stylesheet():
    """Вид живёт в `style.css` и только там — правило записано, но не проверялось.

    Первой строкой `app.js` стоит «весь вид — только классами из style.css: своих
    классов и инлайн-стилей нет», и держалось это на аккуратности. Один цвет,
    поставленный в разметке, делает стиль незаменяемым целиком — а весь смысл
    отдельного файла в том, чтобы его можно было заменить, не трогая разметку
    (`panel/PLAN.md` §Стиль).
    """
    js = source("panel/app/app.js")
    lines = [(n, l) for n, l in enumerate(js.split("\n"), 1)
             if not l.strip().startswith("//")]
    colors = [f"{n}: {l.strip()[:60]}" for n, l in lines
              if re.search(r"#[0-9a-fA-F]{3,6}\b|rgba?\(", l)]
    check(not colors, f"в разметке нет ни одного цвета ({colors[:3]})")
    inline = [f"{n}: {l.strip()[:60]}" for n, l in lines
              if re.search(r"\.style\s*\.|\.style\s*=|setAttribute\(\s*[\"']style", l)]
    check(not inline, f"и ни одного инлайн-стиля ({inline[:3]})")

    css = source("panel/app/style.css")
    used = set(re.findall(r'el\("[a-z]+",\s*"([a-z][a-z0-9 -]*)"', js))
    used |= set(re.findall(r'mdNode\("[a-z]+",\s*"([a-z][a-z0-9 -]*)"', js))
    names = {c for group in used for c in group.split()}
    missing = sorted(c for c in names if f".{c}" not in css)
    check(not missing, f"каждый класс из разметки описан в стиле ({missing[:6]})")


def case_deadlines_are_transferred_never_computed():
    """Полоса сроков: даты приходят из полей, а «через N дней» считается.

    Замерено 2026-08-09: в направлении шестнадцать дат, и ровно ОДНА лежала
    в машинном поле — остальные прозой. Поэтому строится полоса только из
    `by` у целей и шапки хартии; ни одна дата не вынимается разбором прозы,
    иначе переписанная фраза молча уводит срок с экрана.

    «Просрочено» НЕ рисуется: пропуск октября по хартии провалом не является,
    и красить его красным значило бы судить вместо владельца. Прошедшая дата
    показывает, сколько дней назад она была, и гаснет.
    """
    sys.path.insert(0, str(ROOT / "panel"))
    import serve
    import datetime
    head = serve.charter_head("# CHARTER — x\n\nreview_by: 2026-08-15\n"
                              "review_what: пересмотреть маршрут\n"
                              "review_source: критерий 1\n\n## Миссия\n\nтекст\n")
    check(head.get("review_by") == "2026-08-15", f"дата из шапки хартии читается: {head}")
    check(head.get("review_what") == "пересмотреть маршрут", "и что именно к ней надо")
    check(serve.charter_head("# CHARTER — y\n\n## Миссия\n\nтекст\n") == {},
          "шапки нет — пустой словарь, а не выдумка")

    today = datetime.date(2026, 8, 10)
    rows = serve.deadlines([{"date": "2026-08-31", "title": "Страница в Steam", "what": "х"},
                            {"date": "2026-08-15", "title": "хартия", "what": "у"},
                            {"date": "2026-08-01", "title": "прошлое", "what": "z"}], today)
    check([r["date"] for r in rows] == ["2026-08-01", "2026-08-15", "2026-08-31"],
          f"строки идут по дате, ближайшие раньше: {[r['date'] for r in rows]}")
    check(rows[1]["days"] == 5, f"дней до 15 августа от 10-го: {rows[1]['days']}")
    check(rows[0]["days"] == -9 and rows[0]["past"] is True,
          f"прошедшая дата считается назад и помечена прошедшей: {rows[0]}")
    check(rows[2]["past"] is False, "будущая — не прошедшая")
    check(all("late" not in r and "overdue" not in r for r in rows),
          "никакого «просрочено»: панель не судит, пропуск срока провалом не объявляет")

    # Фразу собирает СЕРВЕР, а не разметка: русское числительное — единственное
    # место экрана, где «21 дней» выглядит как поломка, и на глаз оно и было
    # поймано. Здесь оно закреплено на всех трёх формах и на исключении 11–14.
    p = serve.days_phrase
    check(p(0) == "сегодня", f"ноль дней — «сегодня», а не «через 0 дней»: {p(0)}")
    check(p(1) == "через 1 день", p(1))
    check(p(2) == "через 2 дня", p(2))
    check(p(5) == "через 5 дней", p(5))
    check(p(11) == "через 11 дней", f"одиннадцать — исключение: {p(11)}")
    check(p(14) == "через 14 дней", f"четырнадцать — тоже: {p(14)}")
    check(p(21) == "через 21 день", f"двадцать один — снова «день»: {p(21)}")
    check(p(22) == "через 22 дня", p(22))
    check(p(77) == "через 77 дней", p(77))
    check(p(-1) == "был 1 день назад", f"прошедшее говорит в прошедшем: {p(-1)}")
    check(p(-9) == "было 9 дней назад", p(-9))
    check(p(-2) == "было 2 дня назад", p(-2))
    check(all(x["phrase"] for x in rows), "и каждая строка полосы несёт готовую фразу")


def case_charter_sections_come_from_the_file():
    """Разделы хартии берутся ИЗ ФАЙЛА, а не из списка в коде.

    Замерено 2026-08-09: у indie разделы названы по-русски (Миссия, Критерии
    успеха, Жёсткие ограничения…), у solmax по-английски (Mission, Success
    criteria, Constraints…). Список имён в коде совпал бы ровно с одним
    направлением, а у второго показал бы пустоту — и это была бы та же
    молчаливая недостача, что и всегда.

    Прогноз есть не у всех: у indie карточка `direction_forecast` лежит,
    у solmax её нет вовсе. Отсутствие показывается как отсутствие.
    """
    sys.path.insert(0, str(ROOT / "panel"))
    import serve
    text = ("# CHARTER — x\n\n## Миссия\n\nтекст миссии\n\n"
            "## Критерии успеха\n\n### 1. Первый\n\nподробность\n\n"
            "## Жёсткие ограничения\n\nодно ограничение\n")
    secs = serve.charter_sections(text)
    check([s["title"] for s in secs] == ["Миссия", "Критерии успеха", "Жёсткие ограничения"],
          f"разделы и их порядок — из файла: {[s['title'] for s in secs]}")
    check("текст миссии" in secs[0]["body"], "тело раздела едет вместе с заголовком")
    check("### 1. Первый" in secs[1]["body"],
          "подразделы остаются внутри своего раздела, а не становятся своими")
    check(not any(s["title"].startswith("CHARTER") for s in secs),
          "название файла разделом не считается")

    en = serve.charter_sections("# CHARTER — y\n\n## Mission\n\ntext\n")
    check([s["title"] for s in en] == ["Mission"], "английские имена читаются так же")
    check(serve.charter_sections("") == [], "пустая хартия — пустой список, не выдумка")


def case_knowledge_reads_both_spellings():
    """У «кем читается» ДВА имени на диске, и панель обязана знать оба.

    Замерено 2026-08-09 на 15 записях обоих направлений: `read_by` стоит в 13,
    `reads` — в 2, читателя нет НИ У ОДНОЙ. Знать одно имя значило бы объявить
    читателя неназванным у двух записей, где он назван словом «КАЖДАЯ нога».

    Число получено со второй попытки, и это стоит помнить: первый замер читал
    только первые 1200 байт файла и насчитал 8 — поля, стоящие ниже длинного
    `fact:`, в окно не попали. Замер с произвольной отсечкой — такой же
    ненадёжный источник, как читатель, переживший свой файл.

    Устаревание НЕ вычисляется: `status: current` стоит у всех четырнадцати,
    кто статус имеет, и вывести из этого «протухло» неоткуда.
    """
    sys.path.insert(0, str(ROOT / "panel"))
    import serve
    a = serve.knowledge_row("x.md", "# Как сложена игра\n\naccepted: 2026-08-02 владельцем\n"
                                    "status: current\nreads: КАЖДАЯ нога\n\n## Почему\ntext")
    check(a["title"] == "Как сложена игра", f"заголовок берётся из первой строки: {a['title']}")
    check(a["reader"] and "КАЖДАЯ" in a["reader"], f"`reads:` читается: {a['reader']}")
    check(a["accepted"] and "2026-08-02" in a["accepted"], "дата принятия доходит")
    check(a["status"] == "current", "статус доходит как есть")

    b = serve.knowledge_row("y.md", "# Другое\n\naccepted: 2026-07-01\nread_by: shape, work\n")
    check(b["reader"] == "shape, work", "`read_by:` — то же поле под другим именем")

    bare = serve.knowledge_row("z.md", "# Без шапки\n\nпросто текст\n")
    check(bare["reader"] is None and bare["status"] is None and bare["accepted"] is None,
          "чего нет — то None: панель не подставляет ни читателя, ни статус")
    check(bare["title"] == "Без шапки", "а заголовок всё равно есть")


def case_stale_checkout_announces_itself():
    """Панель, запущенная из отставшей копии, обязана сказать это сама.

    Случай живой: 2026-08-09 владелец не увидел раздела «ИДЕИ», потому что
    `start.cmd` лежит в ОБЕИХ рабочих копиях и запускает панель из своей. Он
    кликнул корневую, отставшую на 16 коммитов, и она молча показывала
    позавчерашние разделы И позавчерашнее состояние направления. Молчаливая
    подмена хуже пустого места — то же правило, что у нечитаемого файла.
    """
    sys.path.insert(0, str(ROOT / "panel"))
    import serve
    check(serve.staleness_note(0, "C:/x") is None, "копия свежая — полосы нет вообще")
    note = serve.staleness_note(16, "C:/my_global_workflow")
    check(note and "16" in note, f"отстала — число коммитов названо: {note}")
    check(note and "my_global_workflow" in note,
          "и названа сама копия — иначе непонятно, какое окно закрывать")

    b = serve.build_info()
    check(isinstance(b.get("behind"), int), f"build.behind — целое число ({b.get('behind')})")
    check(isinstance(b.get("root"), str) and b["root"], "build.root — путь запущенной копии")


def case_history_never_invents():
    """«ИСТОРИЯ» собирается из трёх механических источников и молчит там, где их нет.

    Замерено 2026-08-09 на 303 отчётах обоих направлений: `play:` внутри отчёта
    есть у 298, коммит, добавивший отчёт, находится у 220 из 222 (indie), а вот
    `outcome:` — только у 24 из 221: форматов отчёта два, и поле, которого нет у
    девяти из десяти, показывать нельзя. Поэтому строка несёт ровно то, что
    измеримо, а недостающее показывает как недостающее.
    """
    sys.path.insert(0, str(ROOT / "panel"))
    import serve
    got = serve.leg_from_name("2026-08-09-s-work-g-5a7c-vert-1-close-001.md")
    check(got and got["date"] == "2026-08-09"
          and got["leg"] == "s-work-g-5a7c-vert-1-close-001",
          f"имя файла даёт дату и id ноги: {got}")
    check(serve.leg_from_name("LOG-archive-indie-game-development.md") is None,
          "архив прежнего журнала — не нога, в список ног не идёт")
    check(serve.leg_from_name("что-угодно.md") is None, "мусорное имя — не нога")

    commit = {"sha": "abc1234", "date": "2026-08-09", "subject": "работа: сделано то-то"}
    row = serve.history_row("2026-08-09-s-work-x-001.md", "work", commit)
    check(row["play"] == "work" and row["text"] == "работа: сделано то-то"
          and row["sha"] == "abc1234", f"строка несёт плей, сообщение коммита и его хеш: {row}")
    check(row["path"].endswith("2026-08-09-s-work-x-001.md"), "и путь к отчёту")

    bare = serve.history_row("2026-08-09-s-work-x-001.md", None, None)
    check(bare["text"] is None and bare["sha"] is None,
          "коммита нет — строка молчит, а не сочиняет сообщение")
    check(bare["play"] is None, "плей не записан — так и остаётся пустым")

    # Форматов отчёта ДВА, и разбор обязан брать оба. Якорь на начало строки
    # находил 194 из 300 — остальные 101 молча стали бы «плей не записан».
    check(serve.play_from_text("direction: x\nplay: work\nnode/task: y") == "work",
          "плей своей строкой — читается")
    check(serve.play_from_text("direction: solmax   play: review   node/task: z") == "review",
          "плей внутри строки — читается тоже, иначе треть истории онемеет")
    check(serve.play_from_text("display: none") is None,
          "и `display:` плеем не считается — пробел перед именем обязателен")
    check(serve.play_from_text("ничего похожего") is None, "нет плея — None, не выдумка")


def case_service_key_not_written():
    """`_closed` выводится из папки и НИКОГДА не пишется в файл."""
    bad = [p.name for d in (ROOT / "live").iterdir() if d.is_dir()
           for p in (d / "cards").rglob("*.md")
           if "_closed" in io.open(p, encoding="utf-8").read()]
    check(not bad, f"ключа _closed нет ни в одном файле ({bad[:3]})")
    tree = ast.parse(source("osctl.py"))
    writes = [n for n in ast.walk(tree) if isinstance(n, ast.Constant) and n.value == "_closed"]
    check(not writes, "и команда записи о нём не знает")


def case_waiting_is_only_yours():
    """«ЖДЁТ ТЕБЯ» показывает только то, где отвечает ВЛАДЕЛЕЦ.

    Разбор проверяется напрямую, а не по живым данным: групп «СТОИТ» и
    «ЗАКРЫТО БЕЗ ПРИЧИНЫ» сегодня в состоянии нет, и без этого случая они
    были бы написаны, но никогда не проверены.
    """
    sys.path.insert(0, str(ROOT / "panel"))
    import serve
    cases = [
        ({"_kind": "decision"}, "decision", True),
        ({"_kind": "question"}, "question", True),
        ({"_kind": "call", "to": "owner", "status": "ready"}, "owner_call", True),
        # наряд стоит НЕ на владельце: условие снятия — свободный текст,
        # вычислить «это на нём» нельзя, поэтому в блокирующие он не идёт
        ({"_kind": "call", "to": "exec", "status": "blocked"}, "stalled", False),
        ({"_kind": "call", "to": "exec", "status": "ready"}, None, None),
        ({"_kind": "node", "label": ""}, "unnamed_goal", False),
        ({"_kind": "node", "label": "Есть имя"}, None, None),
        ({"_kind": "issue"}, None, None),          # у записи свой отвечающий
        # Идея НЕ ждёт его слова: это отложенное содержание, а не вопрос. Попади
        # она сюда — «ждёт тебя» станет свалкой, и он перестанет туда смотреть.
        ({"_kind": "idea", "from": "владелец"}, None, None),
        ({"_kind": "task", "_closed": True, "status": "open"}, "closed_unnamed", False),
        ({"_kind": "task", "_closed": True, "status": "done"}, None, None),
        ({"_kind": "task", "_closed": True, "status": "dropped"}, None, None),
    ]
    bad = []
    for head, want, blocking in cases:
        got = serve.waiting_group(head)
        if got != want:
            bad.append(f"{head} -> {got}, ждали {want}")
            continue
        if want and serve.waiting_row("x", head, {}, got)["blocking"] != blocking:
            bad.append(f"{head}: blocking не {blocking}")
    check(not bad, f"разбор по группам сходится на {len(cases)} случаях ({bad[:2]})")

    row = serve.waiting_row("c-1", {"_kind": "call", "to": "e", "status": "blocked",
                                    "unblock_when": "пока он не назовёт слот"}, {}, "stalled")
    check(row.get("unblock") == "пока он не назовёт слот",
          "условие снятия доходит до строки — владелец сам видит, на нём ли это")


def main():
    for fn in (case_now_fields, case_kinds, case_paths, case_head_keys_exist, case_dead_dirs,
               case_closed_is_visible, case_no_second_source,
               case_waiting_is_only_yours, case_idea_keeps_its_author,
               case_stale_checkout_announces_itself, case_history_never_invents,
               case_knowledge_reads_both_spellings, case_charter_sections_come_from_the_file,
               case_deadlines_are_transferred_never_computed, case_look_lives_only_in_the_stylesheet,
               case_service_key_not_written):
        print(f"\n--- {fn.__doc__.splitlines()[0]}")
        fn()
    print(f"\n{'ПРИНЯТО' if not fails else 'НЕ ПРИНЯТО: ' + str(len(fails)) + ' упало'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
