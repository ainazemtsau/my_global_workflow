"""Этап 1a: NOW.md направления -> карточки и обратно.

Команды:
    python panel/cards.py build <direction-id>
    python panel/cards.py check <direction-id>

Пишет только в panel/.cards/<direction-id>/. live/ — только чтение.
Списки и словари пишутся в теле блоком под строкой-меткой ```yaml —
это единственный способ отличить их от строки, записанной байт в байт.
"""
import argparse
import datetime
import os
import shutil
import sys

import yaml

for _s in (sys.stdout, sys.stderr):
    _s.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECTIONS = (("tasks", "task"), ("open_calls", "call"),
            ("issues", "issue"), ("decisions", "decision"))
KINDS = ("bet", "task", "call", "issue", "decision")
BET_CARRIERS = ("task", "call", "decision")
YAML_MARK = "```yaml"


def fail(msg):
    raise SystemExit("ОШИБКА: " + msg)


def load_now(direction):
    path = os.path.join(ROOT, "live", direction, "NOW.md")
    try:
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f.read())
    except OSError as e:
        fail(f"не читается {path}: {e}")
    if not isinstance(data, dict):
        fail(f"{path}: верхний уровень не словарь")
    return data


def section_list(now, sec):
    """Отсутствующий раздел и null считаются пустым списком."""
    v = now.get(sec)
    if v is None:
        return []
    if not isinstance(v, list):
        fail(f"раздел {sec}: не список")
    return v


def bet_node_of(now):
    bet = now.get("bet")
    return bet["node"] if isinstance(bet, dict) and "node" in bet else None


def in_head(v):
    """Единственное правило раскладки (§4.2): что идёт в шапку."""
    if isinstance(v, str):
        return len(v) <= 120 and "\n" not in v
    return isinstance(v, (bool, int, float, datetime.date)) or v is None


def dump_yaml(v):
    return yaml.safe_dump(v, sort_keys=False, allow_unicode=True,
                          default_flow_style=False)


def make_card(direction, cid, kind, pos, rec, bet_node):
    if not isinstance(rec, dict):
        fail(f"{kind} #{pos}: запись не словарь")
    for k in ("kind", "pos"):
        if k in rec:
            fail(f"{cid}: у записи уже есть ключ {k}, служебный не добавить")
    head = {"id": cid, "kind": kind}
    if kind in BET_CARRIERS and bet_node is not None:
        if "bet" in rec:
            fail(f"{cid}: у записи уже есть ключ bet, служебный не добавить")
        head["bet"] = bet_node
    head["pos"] = pos
    blocks = []
    for k, v in rec.items():
        if in_head(v):
            head[k] = v
        elif isinstance(v, str):
            if any(l == YAML_MARK or l.startswith("## ") for l in v.split("\n")):
                fail(f"{cid}: поле {k} содержит запрещённую строку")
            blocks.append(f"## {k}\n{v}\n")
        elif isinstance(v, (list, dict)):
            blocks.append(f"## {k}\n{YAML_MARK}\n{dump_yaml(v)}```\n")
        else:
            fail(f"{cid}: поле {k} неподдерживаемого типа {type(v).__name__}")
    return ("---\n" + dump_yaml(head) + "---\n\n" + "".join(blocks)
            + f"END_OF_FILE: panel/.cards/{direction}/{cid}.md\n")


def build(direction):
    now = load_now(direction)
    out = os.path.join(ROOT, "panel", ".cards", direction)
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)  # папка направления создаётся даже при нуле карточек
    bet, bet_node = now.get("bet"), bet_node_of(now)
    cards = []
    if isinstance(bet, dict) and "node" in bet:
        cid = str(bet["node"])
        cards.append(("bet", cid, make_card(direction, cid, "bet", 0, bet, bet_node)))
    for sec, kind in SECTIONS:
        for pos, rec in enumerate(section_list(now, sec)):
            if not isinstance(rec, dict) or "id" not in rec:
                fail(f"раздел {sec}, запись #{pos}: нет словаря с id")
            cid = str(rec["id"])
            cards.append((kind, cid, make_card(direction, cid, kind, pos, rec, bet_node)))
    counts, seen = {k: 0 for k in KINDS}, set()
    for kind, cid, text in cards:
        if cid in seen:
            fail(f"два карточных id: {cid}")
        seen.add(cid)
        counts[kind] += 1
        with open(os.path.join(out, cid + ".md"), "w", encoding="utf-8", newline="") as f:
            f.write(text)
    parts = ", ".join(f"{k} {counts[k]}" for k in KINDS)
    print(f"построено {sum(counts.values())} карточек: {parts}")


def read_card(path):
    """Шапка — только yaml.safe_load куска между первой и второй строками ---;
    тело режется по строкам, начинающимся с '## '."""
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


def reassemble(direction, now):
    d = os.path.join(ROOT, "panel", ".cards", direction)
    if not os.path.isdir(d):
        fail(f"нет папки карточек: {d}")
    bet_node = bet_node_of(now)
    sections, rebuilt_bet = {kind: [] for _, kind in SECTIONS}, None
    for name in sorted(os.listdir(d)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(d, name)
        head, blocks = read_card(path)
        kind, pos = head.get("kind"), head.get("pos")
        if kind not in KINDS:
            fail(f"{name}: неизвестный kind {kind!r}")
        if not isinstance(pos, int) or isinstance(pos, bool):
            fail(f"{name}: pos не целое")
        rec = {}
        for k, v in head.items():
            if k in ("kind", "pos"):
                continue
            if k == "id" and kind == "bet":
                continue  # в исходнике его не было, там оно живёт как node
            if k == "bet" and kind in BET_CARRIERS and bet_node is not None:
                continue  # служебный bet
            rec[k] = v
        for k, ls in blocks.items():
            rec[k] = body_value(path, k, ls)
        if kind == "bet":
            if rebuilt_bet is not None:
                fail(f"две карточки ставки: {name}")
            rebuilt_bet = rec
        else:
            sections[kind].append((pos, rec))
    for kind, items in sections.items():
        poss = [p for p, _ in items]
        if len(set(poss)) != len(poss):
            fail(f"раздел {kind}: pos повторяется")
        sections[kind] = [rec for _, rec in sorted(items, key=lambda t: t[0])]
    return rebuilt_bet, sections


def diff(path, a, b):
    """Первое расхождение между ожидаемым a (NOW.md) и собранным b."""
    if a == b:
        return None
    if isinstance(a, dict) and isinstance(b, dict):
        for k in a:
            if k not in b:
                return (f"{path}.{k}", a[k], "<отсутствует>")
            r = diff(f"{path}.{k}", a[k], b[k])
            if r:
                return r
        for k in b:
            if k not in a:
                return (f"{path}.{k}", "<отсутствует>", b[k])
    elif isinstance(a, list) and isinstance(b, list):
        for i in range(min(len(a), len(b))):
            r = diff(f"{path}[{i}]", a[i], b[i])
            if r:
                return r
        if len(a) != len(b):
            i = min(len(a), len(b))
            if len(a) > len(b):
                return (f"{path}[{i}]", a[i], "<отсутствует>")
            return (f"{path}[{i}]", "<отсутствует>", b[i])
    return (path, a, b)


def check(direction):
    now = load_now(direction)  # каждый раз заново с диска
    rebuilt_bet, sections = reassemble(direction, now)
    bet = now.get("bet")
    exp_bet = bet if (isinstance(bet, dict) and "node" in bet) else None
    found = diff("bet", exp_bet, rebuilt_bet)
    if found is None:
        for sec, kind in SECTIONS:
            found = diff(sec, section_list(now, sec), sections[kind])
            if found:
                break
    if found:
        path, a, b = found
        print(f"РАСХОЖДЕНИЕ {path}")
        print(f"  в NOW.md:    {repr(a)[:200]}")
        print(f"  в карточках: {repr(b)[:200]}")
        raise SystemExit(1)
    print("СОВПАДАЕТ")


def main():
    p = argparse.ArgumentParser(description="NOW.md -> карточки и обратно")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("build", "check"):
        sub.add_parser(name).add_argument("direction")
    args = p.parse_args()
    (build if args.cmd == "build" else check)(args.direction)


if __name__ == "__main__":
    main()
