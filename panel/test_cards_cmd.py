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

    for f in ("id", "_kind", "_pos"):
        r = run("card", "set", "--id", "t-1", "--field", f, "--value", "zzz", *C)
        check(r.returncode == 1, f"{f} командой set не меняется — это имя носителя")

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

    # --- потолок журнала называется, но не блокирует
    for i in range(25):
        run("log", "add", "--id", "t-1", "--text", f"событие {i}", "--date", f"2026-07-{i%28+1:02d}", *C)
    r = run("check", *C)
    check(r.returncode == 0 and "потолок" in r.stdout,
          "check называет журнал сверх потолка — но НЕ судит по нему (CONCEPT §4)")

    # --- поиск
    r = run("find", "--text", "Другое дело", *C)
    check(r.returncode == 0 and "t-1" in r.stdout, "find находит карточку по тексту")

    print(f"\n{'ПРИНЯТО' if not fails else 'НЕ ПРИНЯТО: ' + str(len(fails)) + ' упало'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
