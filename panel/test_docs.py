# -*- coding: utf-8 -*-
"""Приёмка на тот же КЛАСС, что и `test_readers.py`, но читатель здесь — человек.

`test_readers` держит согласие КОДА с моделью. Этот держит согласие ДОКУМЕНТА
с диском. Случай, ради которого написан: коммит «точка входа стала точной»
переписал `panel/PLAN.md` сверху и оставил ниже раздел, где `TREE.md` ещё
источник, а переезд «ещё нельзя». Свежий чат прочитал файл сверху вниз и
двадцать минут работал по позавчерашнему миру. Ни одна приёмка не могла упасть:
для машины устаревшее предложение неотличимо от верного.

ЧТО ПРОВЕРЯЕТСЯ — только то, что документ ОБЕЩАЕТ ПРО ДИСК:
  1. названа команда `osctl` — она существует, и ключ у неё существует;
  2. назван путь в репозитории — файл существует;
  3. перечислены виды карточек — набор равен коду;
  4. названы готовые и закрытые разделы панели — равны коду;
  5. перечислены приёмки — равны файлам на диске, и число совпадает со словом.

ЧЕГО ЗДЕСЬ СОЗНАТЕЛЬНО НЕТ, и это не недоделка. Смысл не судится: никакая
проверка не узнает, что предложение «переезд ещё нельзя» стало ложью, — это
работа ИИ и владельца (`os2/CONCEPT.md` §9, «никаких скриптов-судей»). Потолок
механики — заставить человека посмотреть, и он честно назван.

ДОКУМЕНТЫ ДЕЛЯТСЯ НА ДВА РОДА, и проверяется только первый:
  · ИНСТРУКТИРУЮЩИЕ — говорят, как делать сейчас. Устарели — вредят;
  · ЗАПИСИ — говорят, что было. `os/FRICTION.md`, `os/docs/`, `os2/SWITCHOVER.md`,
    `history/`, `work/` называют снятые файлы и снятые команды ПО СВОЕЙ ПРИРОДЕ,
    и требовать от них соответствия диску значило бы переписывать историю.

    python panel/test_docs.py
"""
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "panel"))
import osctl      # noqa: E402
import serve      # noqa: E402

# Инструктирующие. Список явный: папка целиком означала бы, что новый документ
# попадает под проверку молча, а он может оказаться записью.
DOCS = ["AGENTS.md", "CLAUDE.md", "README.md",
        "os/KERNEL.md", "os/MAINTENANCE.md", "os/BOOTSTRAP.md", "os/EXTENDING.md",
        "os2/CONCEPT.md", "panel/PLAN.md", ".pi/README.md"]
for _d in ("os/plays", "os/adapters", "os/schema", "os/engineering"):
    DOCS += [str(p.relative_to(ROOT)).replace("\\", "/") for p in sorted((ROOT / _d).glob("*.md"))]
DOCS = [d for d in DOCS if (ROOT / d).exists()]

CMD = re.compile(r"osctl(?:\.py)?\s+([a-z][a-z-]*)(?:\s+([a-z][a-z-]*))?")
FLAG = re.compile(r"--[a-z][a-z-]*")
# Только инструментальные и правиловые области. `live/` и `work/` НАМЕРЕННО вне:
# правила показывают там примеры с выдуманными id (`work/trailer-script.md`,
# `live/indie-game/NOW.md` — семь таких), и требовать их существования значило бы
# завести шумную проверку. Шумную выключают, а выключенная не ловит ничего.
PATH = re.compile(r"(?<![\w/.-])((?:os|os2|panel|\.pi|\.codex|\.claude)"
                  r"/[A-Za-z0-9_./-]+\.(?:md|py|ts|json|yaml|cjs|cmd|css|js|html))")
СЛОВА = {1: "одна", 2: "две", 3: "три", 4: "четыре", 5: "пять", 6: "шесть",
         7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одиннадцать"}

fails = []


def check(ok, msg):
    print(("OK   " if ok else "FAIL ") + msg)
    if not ok:
        fails.append(msg)


def text(rel):
    return io.open(ROOT / rel, encoding="utf-8").read()


def real_commands():
    """Настоящий разбор `osctl`, а не список, переписанный сюда руками —
    иначе у документа было бы два источника правды вместо нуля."""
    ap = osctl.build_parser()
    top = next(a for a in ap._actions if getattr(a, "choices", None))
    out = {}
    for noun, p in top.choices.items():
        inner = [a for a in p._actions if getattr(a, "choices", None)]
        if inner:
            out[noun] = {verb: {s for act in q._actions for s in act.option_strings}
                         for verb, q in inner[0].choices.items()}
        else:
            out[noun] = {None: {s for act in p._actions for s in act.option_strings}}
    return out


REAL = real_commands()


def scan_commands(body):
    """(номер строки, что не так) для каждого обращения к `osctl` в тексте."""
    bad = []
    for n, line in enumerate(body.split("\n"), 1):
        for m in CMD.finditer(line):
            noun, verb = m.group(1), m.group(2)
            if noun not in REAL:
                bad.append((n, f"osctl {noun} — такой команды нет"))
                continue
            verbs = REAL[noun]
            if list(verbs) == [None]:
                verb, known = None, verbs[None]
            elif verb is None:
                known = set().union(*verbs.values())      # упомянута группа целиком
            elif verb not in verbs:
                bad.append((n, f"osctl {noun} {verb} — такой команды нет"))
                continue
            else:
                known = verbs[verb]
            tail = line[m.end():]
            nxt = tail.find("osctl")
            for f in FLAG.finditer(tail if nxt < 0 else tail[:nxt]):
                if f.group(0) not in known:
                    bad.append((n, f"osctl {noun} {verb or ''}: ключа {f.group(0)} нет"))
    return bad


def scan_paths(body):
    bad = []
    for n, line in enumerate(body.split("\n"), 1):
        for m in PATH.finditer(line):
            if not (ROOT / m.group(1)).exists():
                bad.append((n, f"{m.group(1)} — такого файла нет"))
    return bad


def случай(name, scan, control_ok, control_bad):
    """Прогон по всем инструктирующим плюс два контроля: проверка обязана
    молчать на верном тексте и говорить на неверном. Приёмка, которая не умеет
    падать, зелёная всегда — это уже стоило нам одной слепой фикстуры."""
    bad = [f"{rel}:{n} {msg}" for rel in DOCS for n, msg in scan(text(rel))]
    check(not bad, f"{name}: расхождений нет ({len(bad)}) {bad[:4]}")
    check(not scan(control_ok), f"{name}: контроль — верный текст не ловится")
    check(scan(control_bad), f"{name}: контроль — неверный текст ловится")


def case_commands():
    """Команда, названная в документе, существует — и ключ у неё существует."""
    случай("команды", scan_commands,
           "osctl card set --id x --field status --value done",
           "osctl question add --text x")
    check(scan_commands("osctl card set --evidence x"),
          "команды: контроль — несуществующий ключ у существующей команды ловится")


def case_paths():
    """Путь, названный в документе, существует на диске."""
    случай("пути", scan_paths, "panel/serve.py", "panel/no-such-file.py")


def case_kinds():
    """Виды карточек, перечисленные в основании, равны коду."""
    body = text("os2/CONCEPT.md")
    head = body.index("### Виды карточек")
    chunk = body[head:body.index("\n\n", body.index("\n\n", head) + 2)]
    named = set(re.findall(r"`([a-z_]+)`", chunk))
    real = set(osctl.CARD_KINDS)
    check(named == real,
          f"виды карточек в CONCEPT равны коду (лишние {sorted(named - real)}, "
          f"недостающие {sorted(real - named)})")


def sections_from_plan():
    body = text("panel/PLAN.md")
    i = body.index("Разделы панели:")
    para = body[i:body.index("\n\n", i)].replace("\n", " ")
    para = re.sub(r"\([^)]*\)", "", para)          # пояснения в скобках — не имя
    # Метка — жирное «Закрыт…», а не одна её форма: разделов может остаться
    # и один, и тогда по-русски пишут «Закрыта». Приёмка не должна заставлять
    # писать неграмотно ради своего разбора.
    parts = re.split(r"\*\*Закрыт[аыо]?\*\*", para)
    if len(parts) != 2:
        check(False, f"в плане нет метки «**Закрыты**»/«**Закрыта**»: {para[:90]}")
        return set(), set()
    ready, closed = parts
    def names(s):
        s = s.split("**готовы**")[-1]
        return {x.strip(" .·") for x in s.split("·") if x.strip(" .·")}
    return names(ready), names(closed)


def case_head_fields():
    """Список известных полей шапки один: код и схема обязаны совпасть.

    Два списка одного и того же — это тот же класс, что накладка имён и два
    имени у «кем читается». Здесь он опаснее: разойдясь, схема начнёт называть
    законным поле, которое `check` объявит чужим, и наоборот.
    """
    # Только САМА строка списка, а не абзац вокруг неё: пояснение рядом называет
    # `order` и `_pos` как пример дрейфа, и первая версия этой проверки утащила
    # их в список. Список узнаётся по разделителю «·».
    line = next(l for l in text("os/schema/direction-files.md").split("\n")
                if l.startswith("`id` ·"))
    named = set(re.findall(r"`([a-z_]+)`", line))
    real = set(osctl.KNOWN_HEAD)
    check(named == real,
          f"схема равна коду (лишние в схеме {sorted(named - real)}, "
          f"недостающие {sorted(real - named)})")


def case_sections():
    """Готовые и закрытые разделы, названные в плане, равны коду панели."""
    ready, closed = sections_from_plan()
    labels = dict(serve.SECTIONS)
    real_ready = {labels[i] for i in serve.READY_SECTIONS}
    real_closed = {l for i, l in serve.SECTIONS if i not in serve.READY_SECTIONS}
    check(ready == real_ready, f"готовые совпадают: план {sorted(ready)} "
                               f"против кода {sorted(real_ready)}")
    check(closed == real_closed, f"закрытые совпадают: план {sorted(closed)} "
                                 f"против кода {sorted(real_closed)}")


def case_acceptances():
    """Приёмки, перечисленные в плане, лежат на диске — и число совпадает."""
    body = text("panel/PLAN.md")
    i = body.index("приёмок зелёные")
    para = body[body.rindex("\n", 0, i) + 1:body.index("\n\n", i)]
    named = set(re.findall(r"`(test_[a-z0-9_]+)`", para))
    # Приёмки бывают не только на питоне: отрисовщик markdown проверяется на node,
    # потому что он и сам на node. Считать только `.py` значило бы объявить
    # приёмку несуществующей ровно тогда, когда она есть.
    on_disk = {p.stem for pat in ("test_*.py", "test_*.cjs")
               for p in (ROOT / "panel").glob(pat)}
    check(named == on_disk, f"названные приёмки лежат на диске (лишние "
                            f"{sorted(named - on_disk)}, недостающие {sorted(on_disk - named)})")
    check("`panel/verify.py`" in para, "и verify.py назван вместе с ними")
    word = para.split()[0].lower()
    check(СЛОВА.get(len(on_disk) + 1) == word,
          f"число словом совпадает: сказано «{word}», на диске {len(on_disk) + 1}")


def declared(pattern):
    """Где число объявлено и какое. Одно число живёт в трёх-четырёх файлах —
    ровно тот случай, ради которого приёмка и написана."""
    out = {}
    for rel in DOCS:
        for m in re.finditer(pattern, text(rel)):
            out.setdefault(m.group(1), []).append(rel)
    return out


def case_budgets():
    """Потолки объявлены одним числом везде и посчитаны, а не приняты на слово."""
    kern = declared(r"kernel ≤(\d+) words?")
    check(len(kern) == 1, f"потолок ядра объявлен одним числом: {kern}")
    if len(kern) == 1:
        limit = int(next(iter(kern)))
        words = len(text("os/KERNEL.md").split())
        check(words <= limit, f"ядро {words} слов при потолке {limit}")

    play = declared(r"(?:a play|each play) ≤(\d+)")
    for num, where in declared(r"≤(\d+)-word budget").items():
        play.setdefault(num, []).extend(where)
    check(len(play) == 1, f"потолок плея объявлен одним числом: {play}")
    if len(play) == 1:
        limit = int(next(iter(play)))
        over = [(p.name, n) for p in sorted((ROOT / "os" / "plays").glob("*.md"))
                for n in [len(io.open(p, encoding="utf-8").read().split())] if n > limit]
        check(not over, f"каждый плей в потолке {limit} (перебор: {over})")

    types = declared(r"(\w+) (?:state )?file types")
    check(len(types) == 1, f"число видов файлов состояния одно и то же: {types}")
    # `os/EXTENDING.md` говорил «five state file types» и «six-type budget» в ОДНОМ
    # предложении: рез поправил первое и не заметил второго.
    budget_word = declared(r"(\w+)-type budget")
    check(set(budget_word) <= set(types),
          f"и слово в «...-type budget» то же самое: {budget_word} против {types}")


def main():
    print(f"инструктирующих документов: {len(DOCS)}")
    for fn in (case_commands, case_paths, case_kinds, case_head_fields, case_sections,
               case_acceptances, case_budgets):
        print(f"\n--- {fn.__doc__.splitlines()[0]}")
        fn()
    print(f"\n{'ПРИНЯТО' if not fails else 'НЕ ПРИНЯТО: ' + str(len(fails)) + ' упало'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
