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
    bad = []
    for rel in WATCHED:
        for n, line in code_text(rel):
            for m in re.finditer(r'LIVE_DIR,\s*direction,\s*"([^"]+)"', line):
                for d in dirs:
                    if not (ROOT / "live" / d / m.group(1)).exists():
                        bad.append(f"{rel}:{n} live/{d}/{m.group(1)}")
    check(not bad, f"каждый названный файл направления существует ({bad[:3]})")


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
    for fn in (case_now_fields, case_kinds, case_paths, case_dead_dirs,
               case_closed_is_visible, case_no_second_source,
               case_waiting_is_only_yours, case_idea_keeps_its_author,
               case_service_key_not_written):
        print(f"\n--- {fn.__doc__.splitlines()[0]}")
        fn()
    print(f"\n{'ПРИНЯТО' if not fails else 'НЕ ПРИНЯТО: ' + str(len(fails)) + ' упало'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
