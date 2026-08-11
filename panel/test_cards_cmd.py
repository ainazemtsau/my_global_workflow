# -*- coding: utf-8 -*-
"""Самопроверка команд записи в карточки. Гоняется на ВРЕМЕННОЙ папке,
live/ не трогает вообще.

Проверяет три закона:
  1 — состояние меняется только командой (порядок журнала знает она, а не зовущий);
  2 — команда приносит значение целиком и не ищет место в тексте;
  4 — человеческие поля обязательны (check называет тех, у кого их нет).

    python panel/test_cards_cmd.py
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OSCTL = ROOT / "osctl.py"
D = "test-direction"

fails = []


def check(ok, msg):
    print(("OK   " if ok else "FAIL ") + msg)
    if not ok:
        fails.append(msg)


def run(*args):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    return subprocess.run([sys.executable, str(OSCTL), *args], cwd=str(ROOT),
                          capture_output=True, text=True, encoding="utf-8",
                          errors="replace", env=env)


def case_placement_can_be_written(tmp, C):
    """Карточку можно привязать к её месту — и без места она видна как потерянная.

    Живой дефект 2026-08-10: задачу заводили штатно, а привязать к ставке было
    нечем — отказывали ОБЕ команды, потому что запрет стоял на любом ключе с `_`
    скопом. `osctl context` ходит именно по `_bet`/`_parent`, значит заведённая
    по правилам задача не попадала в рабочий набор следующей ноги и просто
    терялась. Личность носителя (`id`, `_kind`) по-прежнему не задаётся никем,
    и убрать место нельзя: `unset` — ровно тот способ, которым карточка исчезает.
    """
    goal = tmp / "goal.txt"
    goal.write_text("дело\n", encoding="utf-8")

    r = run("card", "new", "--id", "t-place", "--kind", "task",
            "--field", "_bet=g-цель", "--field", "status=open",
            "--block", f"goal={goal}", *C)
    check(r.returncode == 0, f"место задаётся при заведении: {r.stderr.strip()[:80]}")
    check("_bet: g-цель" in (tmp / "t-place.md").read_text(encoding="utf-8"),
          "и ссылка действительно легла в файл")

    r = run("card", "new", "--id", "t-loose", "--kind", "task",
            "--field", "status=open", "--block", f"goal={goal}", *C)
    check(r.returncode == 0, "задача без места всё ещё заводится — это не ошибка ввода")
    r = run("card", "set", "--id", "t-loose", "--field", "_bet", "--value", "g-цель", *C)
    check(r.returncode == 0, f"и привязывается после создания: {r.stderr.strip()[:70]}")

    for f in ("id", "_kind"):
        r = run("card", "set", "--id", "t-loose", "--field", f, "--value", "zzz", *C)
        check(r.returncode == 1, f"{f} по-прежнему не задаётся — это личность носителя")

    r = run("card", "unset", "--id", "t-loose", "--field", "_bet", *C)
    check(r.returncode == 1 and "опора" in r.stderr,
          "убрать место нельзя: так карточка и исчезает из виду")

    # И это должно быть ВИДНО, а не только возможно.
    r = run("card", "new", "--id", "t-orphan", "--kind", "task",
            "--field", "status=open", "--block", f"goal={goal}", *C)
    r = run("check", *C)
    check("t-orphan" in r.stdout and "без ставки" in r.stdout,
          "check называет задачу без ставки — иначе потеря молчалива")
    check("t-place" not in r.stdout.split("без ставки")[0].split("\n")[-1],
          "а привязанную не называет")


def case_superseded_names_its_successor(tmp, C):
    """«Эту ногу перебило вот этой» наконец записывается — и только с указателем.

    Статус объявлен в `os2/CONCEPT.md` как недостающий с обязательными
    `superseded_by` и `at`; во `FRICTION.md` он ждал с 27 июля. До сегодня его
    не писал никто: поля были узаконены, писателя не было. Закрытие без
    указателя запрещено — иначе «перебито» неотличимо от «брошено», а вся
    ценность статуса ровно в том, что видно, ЧЕМ перебило.
    """
    src = tmp / "c-old.md"
    src.write_text("---\nid: c-old\n_kind: call\nstatus: ready\n---\n\n"
                   "## description\nстарый наряд\n\n"
                   f"END_OF_FILE: {src}\n", encoding="utf-8")

    r = run("card", "close", "--id", "c-old", "--status", "superseded",
            "--why", "перебит", *C)
    check(r.returncode == 1 and "superseded-by" in r.stderr,
          f"без указателя на преемника закрыть нельзя: {r.stderr.strip()[:90]}")
    check(src.exists(), "и карточка осталась на месте — отказ ничего не тронул")

    r = run("card", "close", "--id", "c-old", "--status", "superseded",
            "--superseded-by", "c-new", "--why", "перебит", "--date", "2026-08-10", *C)
    check(r.returncode == 0, f"с указателем — закрывается ({r.stderr.strip()[:80]})")
    body = (tmp / "closed" / "c-old.md").read_text(encoding="utf-8")
    check("superseded_by: c-new" in body, "преемник записан в шапку")
    check("at: 2026-08-10" in body, "и дата, когда перебило")
    check("status: superseded" in body, "и сам статус")

    # Отдельная живая карточка: прежняя уже уехала в closed/, и стоп пришёл бы
    # не от статуса, а от «карточки нет» — проверка мерила бы не то.
    other = tmp / "c-two.md"
    other.write_text("---\nid: c-two\n_kind: call\nstatus: ready\n---\n\n"
                     "## description\nвторой наряд\n\n"
                     f"END_OF_FILE: {other}\n", encoding="utf-8")
    r = run("card", "close", "--id", "c-two", "--status", "done",
            "--superseded-by", "c-new", "--why", "просто закрыт", *C)
    check(r.returncode == 1 and "superseded" in r.stderr,
          f"указатель без этого статуса — тоже стоп: {r.stderr.strip()[:70]}")


def case_tool_never_advises_in_prose():
    """Инструмент говорит ФАКТ или называет команду. Совета словами не даёт.

    Случай 2026-08-10, стоивший владельцу времени зря: `osctl check` печатал
    «пора закрывать или чистить». Команды чистки в системе нет и не должно быть
    (журнал append-only), но нога прочитала совет, поверила инструменту, принесла
    его владельцу предложением, тот согласился — и работа упёрлась в запрет.

    Совет, названный командой, проверяем: команда либо есть, либо нет — сквозной
    прогон 2026-08-10 нашёл девять таких и все настоящие. Совет, сказанный
    прозой, не проверяем ничем, поэтому его здесь просто нет.
    """
    import io
    import re
    src = io.open(ROOT / "osctl.py", encoding="utf-8").read()
    # Только то, что уходит человеку: строки внутри print(...) и Stop(...).
    said = re.findall(r'(?:print|Stop)\(\s*((?:f?["\'][^"\']*["\']\s*)+)', src)
    # По границам слова, а не по подстроке: «опора карточки» — не «пора».
    banned = re.compile(r"\b(пора|стоит|следует|рекомендуется|лучше бы|надо бы)\b")
    bad = [(banned.search(s).group(1), s[:80]) for s in said if banned.search(s.lower())]
    check(not bad, f"инструмент не советует прозой ({bad[:2]})")

    # А каждая команда, которую он всё-таки называет, обязана существовать.
    # `(?!-)` — иначе «find --text» разбирается как команда «find --text».
    named = {" ".join(x for x in m.groups() if x)
             for m in re.finditer(r"osctl\.py\s+([a-z]+)(?:\s+(?!-)([a-z-]+))?", src)}
    missing = [c for c in sorted(named)
               if run(*c.split(), "--help").returncode != 0]
    check(not missing, f"и каждая названная им команда существует ({missing})")


def main():
    tmp = Path(tempfile.mkdtemp(prefix="osctl-cards-"))
    card = tmp / "t-1.md"
    card.write_text(
        "---\nid: t-1\n_kind: task\nstatus: open\n---\n\n"
        "## goal\nСделать одно дело\n\n"
        f"END_OF_FILE: {card}\n", encoding="utf-8")
    C = ["--direction", D, "--cards", str(tmp)]

    r = run("card", "show", "--id", "t-1", *C)
    check(r.returncode == 0 and "Сделать одно дело" in r.stdout, "show читает карточку")

    r = run("card", "show", "--id", "нет-такой", *C)
    check(r.returncode == 1 and "карточки нет" in r.stderr, "нет карточки — стоп с причиной")

    # --- закон 2: значение целиком, длинное в шапку не лезет
    r = run("card", "set", "--id", "t-1", "--field", "status", "--value", "done", *C)
    check(r.returncode == 0, "set меняет поле шапки")
    check("status: done" in card.read_text(encoding="utf-8"), "новое значение в файле")

    r = run("card", "set", "--id", "t-1", "--field", "note", "--value", "x" * 200, *C)
    check(r.returncode == 1 and "блок тела" in r.stderr,
          "длинное значение в шапку не пускается — ему место в теле")

    # ЛИЧНОСТЬ носителя не задаётся никем. `_pos` сюда больше НЕ входит: он про
    # место среди соседей, а место обязано задаваться — иначе карточку нельзя
    # ни привязать, ни переставить, и она выпадает из рабочего набора (дефект
    # 2026-08-10). Разделение проверяется в case_placement_can_be_written.
    for f in ("id", "_kind"):
        r = run("card", "set", "--id", "t-1", "--field", f, "--value", "zzz", *C)
        check(r.returncode == 1, f"{f} командой set не меняется — это имя носителя")
    r = run("card", "set", "--id", "t-1", "--field", "_pos", "--value", "3", *C)
    check(r.returncode == 0, "а `_pos` меняется: переставить карточку среди соседей — законно")

    # а поле ВЛАДЕЛЬЦА с таким же словом менять можно: имена больше не спорят
    r = run("card", "set", "--id", "t-1", "--field", "kind", "--value", "executor", *C)
    check(r.returncode == 0, "поле данных `kind` живёт рядом со служебным `_kind`")

    r = run("card", "block", "--id", "t-1", "--name", "status", "--text", "другое", *C)
    check(r.returncode == 1 and "два носителя" in r.stderr,
          "одно имя разом в шапке и в теле не заводится")

    # --- блок переписывается целиком
    r = run("card", "block", "--id", "t-1", "--name", "goal", "--text", "Другое дело", *C)
    check(r.returncode == 0 and "Другое дело" in card.read_text(encoding="utf-8"),
          "блок переписан целиком")
    check("Сделать одно дело" not in card.read_text(encoding="utf-8"),
          "старое содержимое блока не осталось рядом")

    r = run("card", "block", "--id", "t-1", "--name", "note", "--text", "a\n## чужой\nb", *C)
    check(r.returncode == 1 and "разрежет карточку" in r.stderr,
          "строка '## ' внутри текста отбивается — она разрезала бы карточку")

    # --- закон 1: порядок журнала знает команда
    run("log", "add", "--id", "t-1", "--text", "первое", "--date", "2026-08-01", *C)
    run("log", "add", "--id", "t-1", "--text", "второе", "--date", "2026-08-05",
        "--history", "2026-08-05-s-x.md", *C)
    text = card.read_text(encoding="utf-8")
    body = text.split("## журнал", 1)[1]
    lines = [l for l in body.split("\n") if l.strip() and not l.startswith("END_OF_FILE")]
    check(len(lines) == 2, f"в журнале две записи, найдено {len(lines)}")
    check(lines[0].startswith("2026-08-05"), "новое сверху — порядок знает команда")
    check("history/2026-08-05-s-x.md" in lines[0], "указатель на отчёт записан")

    r = run("log", "add", "--id", "t-1", "--text", "второе", "--date", "2026-08-05",
            "--history", "2026-08-05-s-x.md", *C)
    check(r.returncode == 1 and "уже есть" in r.stderr, "журнал не дублирует запись")

    r = run("card", "block", "--id", "t-1", "--name", "журнал", "--text", "подделка", *C)
    check(r.returncode == 1 and "log add" in r.stderr,
          "журнал нельзя переписать через block — только командой log add")

    # --- карточка после всех правок цела
    r = run("card", "show", "--id", "t-1", "--json", *C)
    check(r.returncode == 0 and '"_kind": "task"' in r.stdout, "карточка читается после всех правок")
    check(card.read_text(encoding="utf-8").rstrip().endswith("t-1.md"), "хвост END_OF_FILE на месте")

    # --- check: механические факты
    r = run("check", *C)
    check(r.returncode == 0 and "механических проблем нет" in r.stdout, "check на исправной папке чист")

    bad = tmp / "t-2.md"
    bad.write_text("---\nid: ДРУГОЙ\n_kind: task\n---\n\n## goal\nx\n\nEND_OF_FILE: t-2.md\n",
                   encoding="utf-8")
    r = run("check", *C)
    check(r.returncode == 1 and "не совпадает с именем файла" in r.stdout,
          "check ловит id, не совпавший с именем файла")
    bad.unlink()

    bad = tmp / "t-3.md"
    bad.write_text("---\nid: t-3\n_kind: выдумка\n---\n\nEND_OF_FILE: t-3.md\n", encoding="utf-8")
    r = run("check", *C)
    check(r.returncode == 1 and "не из" in r.stdout, "check ловит незнакомый вид карточки")
    bad.unlink()

    bad = tmp / "t-4.md"
    bad.write_text("---\nid: t-4\n_kind: task\n---\n\n## goal\nx\n", encoding="utf-8")
    r = run("check", *C)
    check(r.returncode == 1 and "END_OF_FILE" in r.stdout, "check ловит отсутствие хвоста")
    bad.unlink()

    # --- потолок журнала называется, но не блокирует и НЕ СОВЕТУЕТ
    for i in range(25):
        run("log", "add", "--id", "t-1", "--text", f"событие {i}", "--date", f"2026-07-{i%28+1:02d}", *C)
    r = run("check", *C)
    check(r.returncode == 0 and "потолок" in r.stdout,
          "check называет журнал сверх потолка — но НЕ судит по нему (CONCEPT §4)")
    # Эта строка утверждала «не судит» и принимала «пора закрывать или чистить» —
    # то есть ровно суждение. Теперь она это и проверяет.
    check("пора" not in r.stdout and "чистить" not in r.stdout,
          "и совета в нём нет: решает читающий, а не команда")

    # --- у долгоживущей карточки потолок не называется вовсе
    long_card = tmp / "g-long.md"
    long_card.write_text(
        "---\nid: g-long\n_kind: node\nlabel: цель\nhook: зачем\n---\n\n"
        "## goal\nдолгая цель\n\n"
        f"END_OF_FILE: {long_card}\n", encoding="utf-8")
    for i in range(25):
        run("log", "add", "--id", "g-long", "--text", f"волна {i}",
            "--date", f"2026-07-{i%28+1:02d}", *C)
    r = run("check", *C)
    check("g-long" not in r.stdout,
          "у узла замечания про журнал нет: закрыть его командой нельзя, а переписать "
          "журнал нельзя никому — замечание было бы неснимаемым по построению")
    r = run("log", "add", "--id", "g-long", "--text", "ещё одна", "--date", "2026-07-05", *C)
    check(r.returncode == 0 and "потолок" not in r.stdout,
          "и сама запись в журнал узла про потолок молчит")
    r = run("card", "block", "--id", "g-long", "--name", "журнал", "--text", "переписано", *C)
    check(r.returncode == 1 and "log add" in r.stderr,
          "переписать журнал по-прежнему нельзя ни у кого — append-only не ослаблен")

    # --- поиск
    r = run("find", "--text", "Другое дело", *C)
    check(r.returncode == 0 and "t-1" in r.stdout, "find находит карточку по тексту")

    print("\n--- Место карточки задаётся, а без места она видна как потерянная")
    case_placement_can_be_written(tmp, C)

    print("\n--- «Перебито» записывается и называет, чем именно")
    case_superseded_names_its_successor(tmp, C)

    print("\n--- Инструмент говорит факт или называет команду, но не советует прозой")
    case_tool_never_advises_in_prose()

    print(f"\n{'ПРИНЯТО' if not fails else 'НЕ ПРИНЯТО: ' + str(len(fails)) + ' упало'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
