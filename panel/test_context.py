# -*- coding: utf-8 -*-
"""Самопроверка `osctl context` — набора, с которого нога начинает.

Написана ДО команды и против её спеки, а не против того, что получилось.

Зачем команда. `Reads: cards/` в плеях означало «прочитай все карточки»:
замерено 2026-08-09 — 27 029 слов состояния против 3 341 слова правил, при
рабочем наборе одной задачи примерно в 4 200. Шестикратный перегруз, и внутри
него реестр подписей на 5 146 слов, который смотрит один гейт. Связи между
карточками (`_bet`, `node`, `_parent`, `for`, `about`) уже есть — ими просто
никто не пользовался при чтении.

Законы этой команды проверяются ниже:
  1. Набор строит КОМАНДА ПО ССЫЛКАМ, а не модель по вкусу.
  2. Ничто не пропадает молча: включённое плюс исключённое = все карточки,
     и остаток назван вслух. Именно молчаливая недостача — тот класс, который
     эта переделка ловит третий раз (`panel/test_readers.py`).
  3. Обычный payload несёт не больше пяти новых строк журнала; полный
     append-only журнал остаётся в той же карточке и читается только opt-in.

    python panel/test_context.py
"""
import json
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


def card(folder, cid, head, blocks=()):
    p = Path(folder) / f"{cid}.md"
    text = "---\n" + "".join(f"{k}: {v}\n" for k, v in head.items()) + "---\n\n"
    for name, body in blocks:
        text += f"## {name}\n{body}\n"
    p.write_text(text + f"END_OF_FILE: {p}\n", encoding="utf-8")
    return p


def build(tmp):
    """Маленькое направление со всеми связями, которые команда обязана пройти:
    корень → цель → ставка → задача → наряд, плюс чужая ветка и реестр."""
    cards = tmp / "cards"
    cards.mkdir()
    (cards / "closed").mkdir()
    card(cards, "g-root", {"id": "g-root", "_kind": "node", "label": "корень"})
    long_journal = "\n".join(
        f"2026-08-{i:02d} · journal-entry-{i:02d} · history/s-{i:02d}.md"
        for i in range(12, 0, -1)
    )
    card(cards, "g-our", {"id": "g-our", "_kind": "node", "_parent": "g-root",
                          "label": "наша цель"},
         [("goal", "то, ради чего работаем"), ("журнал", long_journal)])
    card(cards, "g-other", {"id": "g-other", "_kind": "node", "_parent": "g-root",
                            "label": "чужая цель"}, [("goal", "к делу не относится")])
    card(cards, "bet-g-our", {"id": "bet-g-our", "_kind": "bet", "node": "g-our"},
         [("appetite", "полдня")])
    card(cards, "t-1", {"id": "t-1", "_kind": "task", "_bet": "g-our", "status": "open"},
         [("goal", "сделать одно дело")])
    card(cards, "t-2", {"id": "t-2", "_kind": "task", "_bet": "g-our", "status": "open"},
         [("goal", "второе дело той же ставки")])
    card(cards, "c-1", {"id": "c-1", "_kind": "call", "for": "t-1", "status": "ready"},
         [("description", "наряд на первое дело")])
    card(cards, "q-our", {"id": "q-our", "_kind": "question", "about": "g-our",
                          "asks": "владелец"}, [("q", "бить грузом — механика или шум?")])
    card(cards, "q-other", {"id": "q-other", "_kind": "question", "about": "g-other",
                            "asks": "владелец"}, [("q", "вопрос не про нашу цель")])
    card(cards, "q-dir", {"id": "q-dir", "_kind": "question", "asks": "владелец"},
         [("q", "вопрос про направление целиком")])
    card(cards, "q-agent", {"id": "q-agent", "_kind": "question", "about": "g-our",
                            "asks": "нога"}, [("q", "это нога решает сама")])
    card(cards, "owner_approved", {"id": "owner_approved", "_kind": "extra"},
         [("подписи", "очень длинный реестр " * 200)])
    # Улики: ссылок на цель у них нет, поэтому в набор они не попадают никогда —
    # и до 2026-08-28 нога не узнавала о них вовсе. Указатель по объявленному
    # полю `route` — единственное, что их показывает.
    card(cards, "i-shaped", {"id": "i-shaped", "_kind": "issue", "level": "objective",
                             "route": "shape"},
         [("issue", "ядро просит переработки, и это замер, а не мнение")])
    card(cards, "i-worked", {"id": "i-worked", "_kind": "issue", "level": "execution",
                             "route": "work"}, [("issue", "наряд писался без правила")])
    card(cards, "i-nomap", {"id": "i-nomap", "_kind": "issue", "level": "direction"},
         [("issue", "у этой улики поля route нет вовсе")])
    (tmp / "NOW.md").write_text(
        f"# NOW: {D}\n\nbet: g-our\n\nEND_OF_FILE: {tmp / 'NOW.md'}\n", encoding="utf-8")
    return cards


def main():
    tmp = Path(tempfile.mkdtemp(prefix="osctl-context-"))
    cards = build(tmp)
    C = ["--direction", D, "--cards", str(cards), "--live-root", str(tmp)]
    canonical = cards / "g-our.md"
    canonical_before = canonical.read_bytes()
    before = {p: p.read_bytes() for p in ROOT.joinpath("live").rglob("*.md")}

    r = run("context", "--for", "t-1", *C, "--json")
    check(r.returncode == 0, f"команда отработала (код {r.returncode}) {r.stderr[:200]}")
    if r.returncode != 0:
        print(f"\nНЕ ПРИНЯТО: {len(fails)} упало")
        return 1
    ctx = json.loads(r.stdout)

    # --- Закон 1: набор собран по ссылкам
    ids = {x["id"] for x in ctx["set"]}
    # Вопросы к владельцу — часть набора, а не приложение к нему: если он ответит,
    # нога пишет ровно в эти карточки. Стоят они десятки слов.
    check(ids == {"NOW", "t-1", "c-1", "bet-g-our", "g-our", "g-root", "q-our", "q-dir"},
          f"набор ровно по ссылкам: указатель, задача, наряд, ставка, цель, родитель, "
          f"два его вопроса — {sorted(ids)}")
    check("t-2" not in ids, "чужая задача той же ставки не втянута — нога делает t-1")
    check("g-other" not in ids, "чужая ветка не втянута")
    check("owner_approved" not in ids, "реестр подписей не втянут — его смотрит гейт, не нога")
    check(any(x["path"].endswith("NOW.md") for x in ctx["set"]),
          "указатель направления в наборе")

    # --- Закон 2: ничто не пропадает молча
    all_ids = {p.stem for p in cards.glob("*.md")}
    card_ids, excl = ids - {"NOW"}, set(ctx["excluded"]["ids"])
    check(excl | card_ids == all_ids,
          f"включённое плюс исключённое = все карточки (потерялись: {sorted(all_ids - excl - card_ids)})")
    check(not (excl & card_ids), "и ни одна не попала в оба списка разом")
    check(ctx["excluded"]["words"] > 0 and ctx["excluded"]["by_kind"],
          f"остаток назван числом и по видам: {ctx['excluded']['by_kind']}")

    # --- Закон 3: context вручает компактный payload, canonical журнал — opt-in
    our = next(x for x in ctx["set"] if x["id"] == "g-our")
    payload = our.get("content", "")
    journal = our.get("journal", {})
    shown = [line for line in payload.splitlines() if "journal-entry-" in line]
    check(len(shown) == 5, f"по умолчанию показано ровно пять новых записей ({len(shown)})")
    check("journal-entry-12" in payload and "journal-entry-08" in payload,
          "в payload именно пять НОВЫХ записей")
    check("journal-entry-07" not in payload and "journal-entry-01" not in payload,
          "более ранние записи в обычный payload не попали")
    check(journal.get("total") == 12 and journal.get("shown") == 5
          and journal.get("hidden") == 7,
          f"точный счёт журнала: {journal}")
    opt_in = our.get("full_journal", {})
    opt_argv = opt_in.get("argv", [])
    check("--full-journal" in opt_argv and "g-our" in opt_argv
          and opt_argv[-2:] == ["--cards", str(cards)],
          "opt-in несёт id и тот же canonical cards root")
    counts = ctx.get("word_counts", {})
    check(counts.get("default_payload", 0) < counts.get("full_sources", 0),
          f"счётчик разделяет предъявленный payload и полные источники: {counts}")
    check(our.get("words") == len(payload.split())
          and our.get("source_words", 0) > our.get("words", 0),
          "слова строки набора считают предъявленный payload, а source назван отдельно")

    osctl_at = opt_argv.index("osctl.py") if "osctl.py" in opt_argv else -1
    full = run(*opt_argv[osctl_at + 1:]) if osctl_at >= 0 else run("нет-такой-команды")
    check(full.returncode == 0, f"opt-in полного журнала отработал: {full.stderr[:120]}")
    check(full.stdout.count("journal-entry-") == 12,
          "opt-in возвращает все двенадцать канонических записей")
    check(full.stdout.find("journal-entry-12") < full.stdout.find("journal-entry-01"),
          "полный журнал сохраняет канонический порядок — новое сверху")
    check(canonical.read_bytes() == canonical_before,
          "default и full reader не изменили каноническую карточку ни на байт")

    # --- Ждёт слова владельца: по привязке, а не по всем подряд
    waiting = {x["id"] for x in ctx["waiting"]}
    check("q-our" in waiting, "вопрос про нашу цель ждёт его слова")
    check("q-dir" in waiting, "вопрос про направление целиком — тоже")
    check("q-other" not in waiting, "вопрос про чужую цель не показывается")
    check("q-agent" not in waiting, "вопрос, который решает нога, владельцу не носится")
    check(all(x.get("text") for x in ctx["waiting"]),
          "у каждого — сам текст вопроса, а не только id")

    # --- Закон 3: улика доезжает до ноги, чей плей её маршрут
    # Заведено 2026-08-28. До этого 81 живая улика направления не попадала ни в
    # набор, ни в остаток по имени: ссылок на цель у улик нет, поэтому нарезка
    # волны резала, не зная того, что система про себя уже записала. Отбор —
    # РАВЕНСТВО ОБЪЯВЛЕННОГО ПОЛЯ, без поиска по прозе и без угадывания.
    routes = ctx["issues_by_route"]
    check(routes.get("shape") and routes["shape"][0]["id"] == "i-shaped",
          f"улика с route: shape стоит под маршрутом shape — {sorted(routes)}")
    check(routes.get("work") and routes["work"][0]["id"] == "i-worked",
          "улика с route: work — под своим")
    check(any(x["id"] == "i-nomap" for g in routes.values() for x in g),
          "улика БЕЗ поля route не пропадает молча, а стоит в названной группе")
    check("i-nomap" not in {x["id"] for k, g in routes.items()
                            if k in ("shape", "work") for x in g},
          "и не приписана к чужому маршруту догадкой")
    check(all(x.get("text") for g in routes.values() for x in g),
          "у каждой — своя строка текста, а не только id")
    check({"i-shaped", "i-worked", "i-nomap"} <= excl,
          "указатель НЕ раздувает набор: улики по-прежнему в остатке")

    # --- Человеческий вывод: он и есть то, что нога кладёт в чат
    r2 = run("context", "--for", "t-1", *C)
    check("бить грузом" in r2.stdout, "без --json печатает текст вопроса словами")
    check("не включено" in r2.stdout.lower(), "и вслух называет, что осталось за бортом")
    check("ядро просит переработки" in r2.stdout,
          "и печатает улики маршрутами словами, а не только в json")
    check("journal-entry-12" in r2.stdout and "journal-entry-07" not in r2.stdout,
          "человеческий context печатает тот же компактный payload")
    check("скрыто более ранних записей: 7" in r2.stdout.lower(),
          "человеческий context вслух называет точное число скрытых записей")

    # --- Отказы
    r3 = run("context", "--for", "нет-такой", *C)
    check(r3.returncode == 1 and "нет" in r3.stderr.lower(),
          "несуществующая цель — стоп с причиной, а не пустой набор")

    r4 = run("context", *C)
    check(r4.returncode == 0 and "g-our" in r4.stdout,
          "без --for берёт ставку из указателя направления")

    # --- Живое состояние
    after = {p: p.read_bytes() for p in ROOT.joinpath("live").rglob("*.md")}
    check(before == after, "live/ не изменился ни на байт — команда только читает")

    print(f"\n{'ПРИНЯТО' if not fails else 'НЕ ПРИНЯТО: ' + str(len(fails)) + ' упало'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
