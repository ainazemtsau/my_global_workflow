"""Формат карточки — одно определение на всех, кто её читает.

Читателей двое: `osctl` (пишет и читает) и панель (только читает). Пока их было
два независимых, они расходились: один срезал пустые строки в конце блока, другой
нет — и один и тот же файл разбирался по-разному. Поэтому имена, виды и правила
разбора живут ЗДЕСЬ, а `osctl` берёт их отсюда импортом.

Проекции из `NOW.md`/`TREE.md` больше нет: после реза 2026-08-08 источников не
существует, карточки И ЕСТЬ состояние. Тот конвертер и его приёмка лежат в
истории Git — `git show 4138113c:panel/cards.py`.

Два правила, на которых всё держится:
  1. Служебные имена — с ведущим `_`. Поэтому поле владельца может называться
     как угодно, включая `kind`, `pos`, `parent` и `bet`.
  2. Тело режется только по строкам `## `. Никакого другого разбора: значение
     приносится целиком, место в тексте не ищется никогда.
"""
import os
import sys

import yaml

for _s in (sys.stdout, sys.stderr):
    _s.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Разделы, которые сборка упорядочивает по `_pos`. Имя раздела осталось от
# прежних разделов NOW.md и служит теперь именем вида карточки.
SECTIONS = (("tasks", "task"), ("open_calls", "call"),
            ("issues", "issue"), ("decisions", "decision"),
            ("recurring", "recurring"), ("tracks", "track"))
KINDS = ("bet", "node", "task", "call", "issue", "decision",
         "recurring", "track", "extra")
BET_CARRIERS = ("task", "call", "decision")
# `extra` — вид для того, чему дом ещё не назначен: ключ верхнего уровня едет
# своей карточкой с именем ключа. Так уехали реестр подписей `owner_approved`,
# прогноз направления и самодельный `tree_validity` у solmax.
EXTRA = "extra"
SERVICE = "_"
YAML_MARK = "```yaml"


def fail(msg):
    raise SystemExit("ОШИБКА: " + msg)


def read_card(path):
    """Шапка — yaml между первой и второй строками `---`; тело режется по `## `.

    Пустые строки в конце блока НЕ срезаются: значение, кончающееся переводом
    строки, иначе не отличить от разделителя. Разделителя между блоками у нас
    нет — ровно поэтому неоднозначности тоже (см. `osctl.write_card`).
    """
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    if not lines or lines[0] != "---":
        fail(f"{path}: файл не начинается с ---")
    close = next((i for i in range(1, len(lines)) if lines[i] == "---"), None)
    if close is None:
        fail(f"{path}: нет закрывающего ---")
    try:
        head = yaml.safe_load("\n".join(lines[1:close]))
    except yaml.YAMLError as e:
        fail(f"{path}: шапка не разобралась: {e}")
    if not isinstance(head, dict):
        fail(f"{path}: шапка не словарь")
    rest = lines[close + 1:]
    while rest and rest[-1] == "":
        rest.pop()
    if rest and rest[-1].startswith("END_OF_FILE:"):
        rest.pop()
    blocks, cur = {}, None
    for line in rest:
        if line.startswith("## "):
            cur = line[3:]
            if cur in blocks:
                fail(f"{path}: блок {cur} повторяется")
            blocks[cur] = []
        elif cur is None:
            if line != "":
                fail(f"{path}: содержимое вне блоков: {line[:50]!r}")
        else:
            blocks[cur].append(line)
    return head, blocks


def body_value(path, k, ls):
    """Строка — байт в байт; под меткой ```yaml — список или словарь."""
    if not ls or ls[0] != YAML_MARK:
        return "\n".join(ls)
    if len(ls) < 2 or ls[-1] != "```":
        fail(f"{path}: блок {k} начат меткой {YAML_MARK}, но не закрыт ```")
    try:
        v = yaml.safe_load("\n".join(ls[1:-1]))
    except yaml.YAMLError as e:
        fail(f"{path}: блок {k} не разобрался как YAML: {e}")
    if not isinstance(v, (list, dict)):
        fail(f"{path}: блок {k} под меткой {YAML_MARK} не список и не словарь")
    return v


if __name__ == "__main__":
    raise SystemExit(
        "Это определение формата, а не команда.\n"
        "  Состояние читается и меняется через osctl:\n"
        "    uv run --locked python osctl.py check   --direction <направление>\n"
        "    uv run --locked python osctl.py card show --id <id>\n"
        "  Прежний конвертер из NOW.md/TREE.md снят вместе с источниками "
        "(git show 4138113c:panel/cards.py)."
    )
