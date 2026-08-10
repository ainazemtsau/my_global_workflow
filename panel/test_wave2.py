# -*- coding: utf-8 -*-
"""Приёмка волны 2: создание, закрытие, снятие ключа и конец ноги.

Всё гоняется на ВРЕМЕННОЙ папке. Последним делом проверяется, что live/
не изменился ни на байт — команды умеют писать в history/ и в карточки,
поэтому доказательство обязательно.

    python panel/test_wave2.py
"""
import hashlib
import io
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OSCTL = ROOT / "osctl.py"
D = "t-dir"
fails = []


def check(ok, msg):
    print(("OK   " if ok else "FAIL ") + msg)
    if not ok:
        fails.append(msg)


def live_fingerprint():
    """Отпечаток live/ ПОФАЙЛОВО: любая правка любым байтом изменит его.

    Пофайлово, а не одной суммой, ровно по одной причине: в этом репозитории
    рядом идут другие сессии, и они пишут в `live/` прямо во время прогона —
    2026-08-09 так и случилось, соседняя нога положила два файла в `work/`.
    Одна сумма говорит только «разошлось», и на поиск призрака уходит полчаса.
    Здесь падение сразу называет пути, и видно, наши это байты или чужие.
    """
    out = {}
    for p in sorted((ROOT / "live").rglob("*")):
        if p.is_file():
            rel = str(p.relative_to(ROOT)).replace(chr(92), "/")
            out[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def live_diff(before, after):
    """Что именно разошлось: появилось, исчезло, изменилось."""
    return (sorted(set(after) - set(before)),
            sorted(set(before) - set(after)),
            sorted(k for k in set(before) & set(after) if before[k] != after[k]))


class Env:
    def __init__(self):
        self.root = Path(tempfile.mkdtemp(prefix="wave2-"))
        self.cards = self.root / "cards"
        self.cards.mkdir()
        # НИ history/, НИ LOG.md здесь не создаётся, и это главное в фикстуре.
        # Пока она делала себе LOG.md сама, она не могла увидеть, что команда его
        # ТРЕБУЕТ — а рез его удалил. Первая живая нога упала именно на этом
        # (2026-08-08): отчёт записан, журналы нет. Форма приёмки обязана быть
        # той же, что в жизни, иначе приёмка проверяет не то, что работает.

    def run(self, *args):
        env = dict(os.environ, PYTHONIOENCODING="utf-8")
        full = [sys.executable, str(OSCTL), *args, "--direction", D, "--cards", str(self.cards)]
        if args[:2] == ("leg", "close"):
            full += ["--live-root", str(self.root)]
        r = subprocess.run(full, cwd=str(ROOT), capture_output=True, text=True,
                           encoding="utf-8", errors="replace", env=env)
        return r.returncode, (r.stdout + r.stderr).strip()

    def file(self, name, text):
        p = self.root / name
        io.open(p, "w", encoding="utf-8", newline="").write(text)
        return str(p)

    def card(self, cid, closed=False):
        d = self.cards / "closed" if closed else self.cards
        return io.open(d / f"{cid}.md", encoding="utf-8").read()

    def drop(self):
        shutil.rmtree(self.root, ignore_errors=True)


def case_new():
    """Заведение: человеческие поля обязательны, место назначается само."""
    e = Env()
    try:
        rc, out = e.run("card", "new", "--id", "g-1", "--kind", "node")
        check(rc == 1 and "label" in out and "hook" in out,
              f"цель без имени и крючка не заводится: {out.splitlines()[-1][:70]}")

        rc, out = e.run("card", "new", "--id", "c-1", "--kind", "call")
        check(rc == 1 and "description" in out, "наряд без описания не заводится")

        goal = e.file("goal.txt", "Первая\nвторая строка\nтретья")
        rc, out = e.run("card", "new", "--id", "g-1", "--kind", "node",
                        "--field", "label=Играемый кусок", "--field", "hook=Первый заход вдвоём",
                        "--field", "status=parked", "--block", f"goal={goal}")
        check(rc == 0, f"с именем и крючком заводится: {out[:70]}")
        t = e.card("g-1")
        check("label: Играемый кусок" in t and "_kind: node" in t, "поля на месте")
        check("## goal" in t and "вторая строка" in t, "многострочный блок пришёл файлом")
        check("_pos: 0" in t, "первому узлу место 0")

        rc, _ = e.run("card", "new", "--id", "g-2", "--kind", "node",
                      "--field", "label=Второй", "--field", "hook=Второй крючок")
        check(rc == 0 and "_pos: 1" in e.card("g-2"), "второму узлу место 1, никого не сдвинув")

        rc, out = e.run("card", "new", "--id", "g-1", "--kind", "node",
                        "--field", "label=x", "--field", "hook=y")
        check(rc == 1 and "уже есть" in out, "поверх существующей не заводится")

        rc, out = e.run("card", "new", "--id", "x-1", "--kind", "выдумка")
        check(rc == 1 and "не из" in out, "незнакомый вид не заводится")

        rc, out = e.run("card", "new", "--id", "t-1", "--kind", "task",
                        "--field", "_kind=подделка")
        check(rc == 1 and "опора" in out, "служебное имя через --field не задаётся")
    finally:
        e.drop()


def case_close_reopen():
    """Закрытие: причина в журнал, файл в closed/, и обратный ход есть."""
    e = Env()
    try:
        e.run("card", "new", "--id", "t-1", "--kind", "task", "--field", "status=open")

        rc, out = e.run("card", "close", "--id", "t-1")
        check(rc == 1 and "--why" in out, "без причины не закрывается")

        why = e.file("why.txt", "Сделано целиком:\n- первое\n- второе")
        rc, out = e.run("card", "close", "--id", "t-1", "--why-file", why,
                        "--status", "done", "--date", "2026-08-08", "--history", "2026-08-08-s-x.md")
        check(rc == 0, f"закрывается: {out[:60]}")
        check(not (e.cards / "t-1.md").exists(), "из живых убрана")
        t = e.card("t-1", closed=True)
        check("status: done" in t, "терминальный статус записан")
        check("## журнал" in t and "2026-08-08 · Сделано целиком" in t,
              "причина легла записью журнала")
        check("history/2026-08-08-s-x.md" in t, "указатель на отчёт записан")
        tail = t.rstrip().splitlines()[-1].replace("\\", "/")
        check(tail.startswith("END_OF_FILE:") and tail.endswith("closed/t-1.md"),
              f"хвост END_OF_FILE указывает на новое место: ...{tail[-30:]}")

        rc, out = e.run("card", "set", "--id", "t-1", "--field", "status", "--value", "open")
        check(rc == 1 and "reopen" in out, "закрытую не правят молча — говорят, как вернуть")

        rc, out = e.run("card", "show", "--id", "t-1")
        check(rc == 0 and "закрытая" in out, "show достаёт из закрытых и говорит, что она закрыта")

        rc, out = e.run("find", "--text", "Сделано целиком")
        check(rc == 0 and "closed" in out, "find видит закрытые и помечает их")

        rc, out = e.run("card", "reopen", "--id", "t-1", "--why", "вернули: нашлась дырка")
        check(rc == 0 and (e.cards / "t-1.md").exists(), "reopen возвращает в живые")
        check("вернули: нашлась дырка" in e.card("t-1"), "и причина возврата тоже в журнале")
    finally:
        e.drop()


def case_unset():
    """Снятие ключа: раньше --value '' клало null, а это не одно и то же."""
    e = Env()
    try:
        e.run("card", "new", "--id", "i-1", "--kind", "issue",
              "--field", "level=execution", "--field", "route=work")
        e.run("card", "block", "--id", "i-1", "--name", "note", "--text", "заметка")

        e.run("card", "set", "--id", "i-1", "--field", "route", "--value", "")
        check("route: null" in e.card("i-1"), "set --value '' по-прежнему кладёт null")

        rc, _ = e.run("card", "unset", "--id", "i-1", "--field", "route")
        check(rc == 0 and "route" not in e.card("i-1"), "unset убирает ключ совсем")

        rc, _ = e.run("card", "unset", "--id", "i-1", "--block", "note")
        check(rc == 0 and "## note" not in e.card("i-1"), "unset убирает блок тела")

        rc, out = e.run("card", "unset", "--id", "i-1", "--field", "_kind")
        check(rc == 1 and "опора" in out, "служебное имя не снимается")

        rc, out = e.run("card", "unset", "--id", "i-1", "--field", "route")
        check(rc == 1 and "нет" in out, "снять то, чего нет, — стоп с перечнем что есть")

        rc, out = e.run("card", "unset", "--id", "i-1", "--field", "level", "--block", "note")
        check(rc == 1 and "ровно одно" in out, "два за раз не снимаются")
    finally:
        e.drop()


def case_yaml_marker():
    """Забытая метка МОЛЧА превращала список в строку."""
    e = Env()
    try:
        e.run("card", "new", "--id", "t-1", "--kind", "task")
        good = e.file("g.txt", "```yaml\n- один\n- два\n```")
        rc, _ = e.run("card", "block", "--id", "t-1", "--name", "cuts", "--text-file", good)
        check(rc == 0, "список под закрытой меткой принимается")

        bad = e.file("b.txt", "```yaml\n- один\n- два")
        rc, out = e.run("card", "block", "--id", "t-1", "--name", "cuts", "--text-file", bad)
        check(rc == 1 and "не закрыт" in out, "незакрытая метка отбивается")

        bad2 = e.file("b2.txt", "```yaml\nпросто строка\n```")
        rc, out = e.run("card", "block", "--id", "t-1", "--name", "cuts", "--text-file", bad2)
        check(rc == 1 and "список или словарь" in out, "не-список под меткой отбивается")

        rc, out = e.run("card", "block", "--id", "t-1", "--name", "x",
                        "--text", "a", "--text-file", good)
        check(rc == 1 and "выбери одно" in out, "--text и --text-file разом не принимаются")
    finally:
        e.drop()


def case_leg_close():
    """Конец ноги: отчёт и журналы сущностей — одной командой, без LOG.md."""
    e = Env()
    try:
        e.run("card", "new", "--id", "t-1", "--kind", "task")
        e.run("card", "new", "--id", "t-2", "--kind", "task")
        res = e.file("res.md", "outcome: |\n  сделано\nevidence: |\n  ссылка\n")

        check(not (e.root / "LOG.md").exists(), "LOG.md нет — как в жизни после реза")
        rc, out = e.run("leg", "close", "--leg", "s-work-001", "--play", "work",
                        "--scope", "g-5a7c", "--log", "первая  волна   пошла",
                        "--result-file", res, "--id", "t-1", "--id", "t-2",
                        "--date", "2026-08-08")
        check(rc == 0, f"проходит без общего журнала: {out.splitlines()[0][:60]}")

        h = e.root / "history" / "2026-08-08-s-work-001.md"
        check(h.is_file() and "outcome" in h.read_text(encoding="utf-8"),
              "отчёт сохранён в history/")
        check(not (e.root / "LOG.md").exists(), "и LOG.md не воскрешён")

        for cid in ("t-1", "t-2"):
            t = e.card(cid)
            check("2026-08-08 · первая волна пошла · history/2026-08-08-s-work-001.md" in t,
                  f"журнал {cid} получил запись с указателем на отчёт")
        check("t-dir work g-5a7c: первая волна пошла" in out,
              f"напечатано готовое сообщение коммита: {out.splitlines()[-1].strip()[:60]}")

        # повтор той же ноги — доказательство, что запись уже прошла целиком
        rc, out = e.run("leg", "close", "--leg", "s-work-001", "--play", "work",
                        "--log", "первая волна пошла", "--result-file", res,
                        "--id", "t-1", "--date", "2026-08-08")
        check(rc == 0 and "байт в байт" in out and "уже была" in out,
              "повтор ноги — не запись, а подтверждение")
        check(e.card("t-1").count("первая волна пошла") == 1, "и журнал не задвоился")

        other = e.file("other.md", "совсем другой отчёт\n")
        rc, out = e.run("leg", "close", "--leg", "s-work-001", "--play", "work",
                        "--log", "x", "--result-file", other, "--date", "2026-08-08")
        check(rc == 1 and "столкновение" in out,
              "другой текст под тем же именем — столкновение, а не перезапись")

        rc, out = e.run("leg", "close", "--leg", "s-work-002", "--play", "work",
                        "--log", "", "--result", "x", "--date", "2026-08-08")
        check(rc == 1, "нога без строки журнала не закрывается")
    finally:
        e.drop()


def case_leg_close_is_all_or_nothing():
    """Проверки ДО первой записи. Иначе отчёт ложится, а журналы нет — то самое,
    ради чего команда и существует (упало на первой живой ноге 2026-08-08)."""
    e = Env()
    try:
        e.run("card", "new", "--id", "t-1", "--kind", "task")
        rc, out = e.run("leg", "close", "--leg", "s-3", "--play", "work",
                        "--log", "проба", "--result", "x\n",
                        "--id", "t-1", "--id", "нет-такой", "--date", "2026-08-08")
        check(rc == 1 and "нет ни среди живых" in out,
              f"стоп на несуществующей сущности: {out.splitlines()[-1][:60]}")
        check(not (e.root / "history" / "2026-08-08-s-3.md").exists(),
              "отчёт НЕ записан — ни одного байта до того, как всё сошлось")
        check("журнал" not in e.card("t-1"),
              "и журнал уцелевшей сущности тоже не тронут")
    finally:
        e.drop()


def case_places():
    """Место закрытой карточки остаётся занятым, иначе reopen вернёт её на чужое."""
    e = Env()
    try:
        for i in (1, 2):
            e.run("card", "new", "--id", f"t-{i}", "--kind", "task")
        e.run("card", "close", "--id", "t-2", "--why", "кончилась")
        e.run("card", "new", "--id", "t-3", "--kind", "task")
        e.run("card", "reopen", "--id", "t-2", "--why", "вернули")
        import re as _re
        pos = {p.stem: int(_re.search(r"_pos: (\d+)", io.open(p, encoding="utf-8").read()).group(1))
               for p in sorted(e.cards.glob("*.md"))}
        check(len(set(pos.values())) == len(pos), f"после возврата места не столкнулись: {pos}")

        # и если столкновение всё-таки завелось руками — check обязан его назвать
        t = io.open(e.cards / "t-3.md", encoding="utf-8").read()
        io.open(e.cards / "t-3.md", "w", encoding="utf-8", newline="").write(
            t.replace(f"_pos: {pos['t-3']}", f"_pos: {pos['t-1']}"))
        rc, out = e.run("check")
        check(rc == 1 and "уже занято" in out, f"check называет столкновение мест: {out[-70:]}")
    finally:
        e.drop()


def case_prose_stays_prose():
    """Двоеточие в прозе не превращает её в структуру.

    Ровно этот отказ назван в CONCEPT §2 причиной всей переделки — «одно
    двоеточие в прозе валит разбор» — и он воспроизвёлся внутри самой команды:
    `--value "Наряд на t-vert-1: мышь поднимается"` разбиралось YAML'ом в
    отображение, панель печатала `[object Object]`, а слова владельца молча
    меняли форму. В шапке живут только скаляры.
    """
    e = Env()
    try:
        prose = "Наряд исполнителю на t-vert-1: мышь поднимается над полом"
        rc, _ = e.run("card", "new", "--id", "c-1", "--kind", "call",
                      "--field", f"description={prose}")
        check(rc == 0, "наряд с двоеточием в описании заводится")
        sys.path.insert(0, str(ROOT / "panel"))
        import cards as fmt
        h, _b = fmt.read_card(str(e.cards / "c-1.md"))
        check(isinstance(h.get("description"), str),
              f"описание осталось строкой, а не {type(h.get('description')).__name__}")
        check(h.get("description") == prose, f"и текст дословный: {h.get('description')!r}")

        rc, _ = e.run("card", "set", "--id", "c-1", "--field", "note",
                      "--value", "срок: завтра, ответственный: он")
        h, _b = fmt.read_card(str(e.cards / "c-1.md"))
        check(isinstance(h.get("note"), str), "и через set — тоже строка")

        # а настоящие скаляры по-прежнему скаляры
        e.run("card", "set", "--id", "c-1", "--field", "order", "--value", "7")
        e.run("card", "set", "--id", "c-1", "--field", "ready", "--value", "true")
        h, _b = fmt.read_card(str(e.cards / "c-1.md"))
        check(h.get("order") == 7 and h.get("ready") is True,
              f"число осталось числом, булево булевым ({h.get('order')!r}, {h.get('ready')!r})")
    finally:
        e.drop()


def case_closed_edit_is_explicit():
    """Закрытую правят только явным словом — и правка ложится НА МЕСТО."""
    e = Env()
    try:
        e.run("card", "new", "--id", "t-1", "--kind", "task")
        e.run("card", "close", "--id", "t-1", "--why", "кончилась", "--status", "done")
        rc, out = e.run("card", "set", "--id", "t-1", "--field", "note", "--value", "x")
        check(rc == 1 and "--closed" in out, "без флага — отказ, и сказано как быть")

        rc, out = e.run("card", "set", "--id", "t-1", "--field", "note",
                        "--value", "поправлено", "--closed")
        check(rc == 0, f"с флагом проходит: {out[:50]}")
        check(not (e.cards / "t-1.md").exists(),
              "и карточка НЕ всплыла в живой папке — правка легла на место")
        check("поправлено" in e.card("t-1", closed=True), "правка дошла до закрытой карточки")
        rc, out = e.run("check")
        check(rc == 0 and "повторяется" not in out, "дублей id не появилось")
    finally:
        e.drop()


def main():
    before = live_fingerprint()
    for fn in (case_new, case_close_reopen, case_unset, case_yaml_marker,
               case_leg_close, case_leg_close_is_all_or_nothing, case_places,
               case_prose_stays_prose, case_closed_edit_is_explicit):
        print(f"\n--- {fn.__doc__.splitlines()[0]}")
        fn()
    print("\n--- Живое состояние")
    added, removed, changed = live_diff(before, live_fingerprint())
    check(not (added or removed or changed),
          "live/ не изменился ни на байт — а ведь команды умеют писать в history/ и карточки"
          + (f" | появилось: {added} | исчезло: {removed} | изменилось: {changed}"
             if (added or removed or changed) else ""))
    print(f"\n{'ПРИНЯТО' if not fails else 'НЕ ПРИНЯТО: ' + str(len(fails)) + ' упало'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
