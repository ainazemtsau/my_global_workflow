"""Носитель: NOW.md и TREE.md направления -> карточки и обратно.

Команды:
    python panel/cards.py build <direction-id>
    python panel/cards.py check <direction-id>

По умолчанию пишет в panel/.cards/<direction-id>/; live/ — только чтение.
Списки и словари пишутся в теле блоком под строкой-меткой ```yaml —
это единственный способ отличить их от строки, записанной байт в байт.

Два правила, на которых всё держится:
  1. Служебные имена — с ведущим `_`. Поэтому поле владельца может называться
     как угодно, включая `kind`, `pos`, `parent` и `bet`.
  2. Ничего не исчезает молча. Ключ без назначенного дома уезжает своей
     карточкой; отменённый схемой — называется; строки-комментарии считаются.
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
            ("issues", "issue"), ("decisions", "decision"),
            ("recurring", "recurring"), ("tracks", "track"))
KINDS = ("bet", "node", "task", "call", "issue", "decision",
         "recurring", "track", "extra")
BET_CARRIERS = ("task", "call", "decision")
# У этих карточек id придуман нами: в источнике такого ключа не было.
SYNTH_ID = ("bet", "extra")
# Всякий ключ верхнего уровня, которому дом не назначен, уезжает СВОЕЙ карточкой
# вида `extra` с именем ключа. Придуманного дома у него ещё нет — но потеряться
# он не может, и каждый прогон его называют вслух. Это и есть замена молчанию:
# `direction_forecast`, `owner_approved` и самодельный `tree_validity` у solmax
# раньше не сверялись вовсе и исчезли бы при срезе источников.
EXTRA = "extra"
# Остаются в файле-указателе. Список ЗАКРЫТЫЙ: незнакомый ключ — это ошибка,
# а не «поедет потом». Молчаливая потеря — тот самый дефект, который мы чиним.
NOW_ONLY = ("bet", "track_wip_limit", "END_OF_FILE")
TREE_ONLY = ("root", "END_OF_FILE")
# Ключи, ОТМЕНЁННЫЕ схемой (direction-files.md, §NOW hygiene: «no removed `next`
# selector: RESULT.next is handoff transport only»). В карточки они не едут
# намеренно — но их называют вслух каждый прогон, а не выбрасывают втихую.
LEGACY_DROPPED = {"next": "селектор отменён схемой: RESULT.next — только транспорт"}
# Всё, что начинается с этого знака, принадлежит носителю, а не данным.
# Поэтому у владельца может быть поле с любым именем, включая `kind` и `pos`.
SERVICE = "_"
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


def make_card(direction, cid, kind, pos, rec, bet_node, parent=None):
    if not isinstance(rec, dict):
        fail(f"{kind} #{pos}: запись не словарь")
    for k in rec:
        if str(k).startswith(SERVICE):
            fail(f"{cid}: поле {k!r} начинается с {SERVICE!r} — это имена носителя")
    head = {"id": cid, "_kind": kind}
    if kind in BET_CARRIERS and bet_node is not None:
        head["_bet"] = bet_node
    if parent is not None:
        head["_parent"] = parent
    head["_pos"] = pos
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


def load_tree(direction):
    """TREE.md как есть. Нет файла — дерева просто нет, это не ошибка."""
    path = os.path.join(ROOT, "live", direction, "TREE.md")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    tail = f"END_OF_FILE: live/{direction}/TREE.md"
    if not raw.rstrip().endswith(tail):
        fail(f"{path}: нет хвоста {tail}")
    try:
        doc = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        fail(f"{path}: не разбирается — {e}")
    if not isinstance(doc, dict) or "root" not in doc:
        fail(f"{path}: нет ключа root")
    return doc


def flatten_tree(doc):
    """Узлы плоским списком: (id, parent, pos среди братьев, запись без children)."""
    out = []

    def walk(nodes, parent):
        for pos, n in enumerate(nodes):
            if not isinstance(n, dict) or "id" not in n:
                fail(f"узел #{pos} под {parent}: нет словаря с id")
            # непустой children — это СТРУКТУРА, она едет в parent/pos;
            # пустой — обычное поле листа, и оно должно вернуться как было
            kids_raw = n.get("children")
            drop = isinstance(kids_raw, list) and len(kids_raw) > 0
            rec = {k: v for k, v in n.items() if not (k == "children" and drop)}
            out.append((str(n["id"]), parent, pos, rec))
            kids = n.get("children")
            if kids:
                if not isinstance(kids, list):
                    fail(f"{n['id']}: children не список")
                walk(kids, str(n["id"]))

    r = doc["root"]
    walk(r if isinstance(r, list) else [r], None)
    return out


def rebuild_tree(nodes):
    """Обратно в дерево: детей собираем по parent и упорядочиваем по pos."""
    by_parent = {}
    for cid, parent, pos, rec in nodes:
        by_parent.setdefault(parent, []).append((pos, cid, rec))
    for k in by_parent:
        poss = [p for p, _, _ in by_parent[k]]
        if len(set(poss)) != len(poss):
            fail(f"узлы под {k}: pos повторяется")
        by_parent[k].sort(key=lambda t: t[0])

    def grow(parent):
        out = []
        for _, cid, rec in by_parent.get(parent, []):
            node = dict(rec)
            kids = grow(cid)
            if kids:
                node["children"] = kids   # структура восстановлена из parent/pos
            out.append(node)
        return out

    return grow(None)


def extra_keys(now, doc):
    """Ключи верхнего уровня без назначенного дома, по источникам.
    Ничего не решает и не выбрасывает — только называет."""
    homed = {"NOW": set(NOW_ONLY) | {s for s, _ in SECTIONS}, "TREE": set(TREE_ONLY)}
    out = []
    for src, data in (("NOW", now), ("TREE", doc)):
        if isinstance(data, dict):
            out += [(src, k) for k in data
                    if k not in homed[src] and k not in LEGACY_DROPPED]
    return out


def count_comments(direction):
    """Строк-комментариев в источниках. Строка, начинающаяся с '#' в НУЛЕВОЙ колонке,
    в YAML однозначно комментарий: содержимое блочного скаляра всегда с отступом.
    Разбор их не видит вовсе — значит в карточки они не едут и должны быть названы."""
    out = {}
    for name in ("NOW.md", "TREE.md"):
        path = os.path.join(ROOT, "live", direction, name)
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8") as f:
            n = sum(1 for line in f if line.startswith("#"))
        if n:
            out[name] = n
    return out


def announce(now, doc, direction=None):
    """Каждый прогон вслух: что уехало своей карточкой и что отменено схемой."""
    if direction:
        for name, n in count_comments(direction).items():
            print(f"СТРОК-КОММЕНТАРИЕВ в {name}: {n} — разбор их не видит, "
                  "в карточки они не едут (их место — журнал сущности)")
    for src, k in extra_keys(now, doc):
        print(f"БЕЗ НАЗНАЧЕННОГО ДОМА {src}.{k} — уехал карточкой {k}.md")
    for src, data in (("NOW", now), ("TREE", doc)):
        if isinstance(data, dict):
            for k in data:
                if k in LEGACY_DROPPED:
                    print(f"ОТМЕНЁННЫЙ КЛЮЧ {src}.{k} — не едет: {LEGACY_DROPPED[k]}")


def build(direction, out=None):
    now = load_now(direction)
    doc = load_tree(direction)
    announce(now, doc, direction)
    out = out or os.path.join(ROOT, "panel", ".cards", direction)
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)  # папка направления создаётся даже при нуле карточек
    bet, bet_node = now.get("bet"), bet_node_of(now)
    cards = []
    if isinstance(bet, dict) and "node" in bet:
        # Свой id: у ставки и у её узла разные карточки, спорить за имя им нечем.
        cid = "bet-" + str(bet["node"])
        cards.append(("bet", cid, make_card(direction, cid, "bet", 0, bet, bet_node)))
    for src, key in extra_keys(now, doc):
        data = now if src == "NOW" else doc
        cards.append((EXTRA, key, make_card(direction, key, EXTRA, 0,
                                            {key: data[key]}, bet_node)))
    if doc is not None:
        for cid, parent, pos, rec in flatten_tree(doc):
            cards.append(("node", cid,
                          make_card(direction, cid, "node", pos, rec, bet_node, parent)))
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


def reassemble(direction, now, src=None):
    d = src or os.path.join(ROOT, "panel", ".cards", direction)
    if not os.path.isdir(d):
        fail(f"нет папки карточек: {d}")
    sections = {kind: [] for _, kind in SECTIONS}
    rebuilt_bet, nodes, extras = None, [], {}
    for name in sorted(os.listdir(d)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(d, name)
        head, blocks = read_card(path)
        kind, pos = head.get("_kind"), head.get("_pos")
        if kind not in KINDS:
            fail(f"{name}: неизвестный _kind {kind!r}")
        if not isinstance(pos, int) or isinstance(pos, bool):
            fail(f"{name}: _pos не целое")
        # Единственное правило разбора: всё служебное — с ведущим знаком.
        rec = {k: v for k, v in head.items() if not str(k).startswith(SERVICE)}
        if kind in SYNTH_ID:
            rec.pop("id", None)  # id придуман нами, в источнике его не было
        for k, ls in blocks.items():
            if k in rec:
                fail(f"{name}: имя {k!r} и в шапке, и в теле — два носителя одного поля")
            rec[k] = body_value(path, k, ls)
        if kind == "node":
            nodes.append((str(head.get("id")), head.get("_parent"), pos, rec))
        elif kind == "bet":
            if rebuilt_bet is not None:
                fail(f"две карточки ставки: {name}")
            rebuilt_bet = rec
        elif kind == EXTRA:
            key = str(head.get("id"))   # id карточки — это и есть имя ключа
            if key not in rec:
                fail(f"{name}: карточка без назначенного дома не несёт ключа {key}")
            extras[key] = rec[key]
        else:
            sections[kind].append((pos, rec))
    for kind, items in sections.items():
        poss = [p for p, _ in items]
        if len(set(poss)) != len(poss):
            fail(f"раздел {kind}: pos повторяется")
        sections[kind] = [rec for _, rec in sorted(items, key=lambda t: t[0])]
    return rebuilt_bet, sections, nodes, extras


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


def check(direction, src=None):
    now = load_now(direction)  # каждый раз заново с диска
    doc = load_tree(direction)
    announce(now, doc, direction)
    rebuilt_bet, sections, nodes, extras = reassemble(direction, now, src)
    bet = now.get("bet")
    exp_bet = bet if (isinstance(bet, dict) and "node" in bet) else None
    found = diff("bet", exp_bet, rebuilt_bet)
    if found is None:
        for sec, kind in SECTIONS:
            found = diff(sec, section_list(now, sec), sections[kind])
            if found:
                break
    if found is None:
        seen = set()
        for s, key in extra_keys(now, doc):  # то, что раньше не сверялось вовсе
            seen.add(key)
            data = now if s == "NOW" else doc
            found = diff(key, data.get(key), extras.get(key))
            if found:
                break
        lost = sorted(set(extras) - seen)
        if found is None and lost:
            found = ("лишние карточки без источника", "<нет в источнике>", lost)
    if found is None and doc is not None:
        r = doc["root"]
        expected = r if isinstance(r, list) else [r]
        found = diff("tree", expected, rebuild_tree(nodes))
    if found:
        path, a, b = found
        print(f"РАСХОЖДЕНИЕ {path}")
        print(f"  в источнике: {repr(a)[:200]}")
        print(f"  в карточках: {repr(b)[:200]}")
        raise SystemExit(1)
    covered = ([s for s, _ in SECTIONS] + [k for _, k in extra_keys(now, doc)]
               + ["bet", "root"])
    print(f"СОВПАДАЕТ — сверено ключей: {len(covered)} ({', '.join(sorted(covered))})")


def main():
    p = argparse.ArgumentParser(description="NOW.md -> карточки и обратно")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("build", "check"):
        sub.add_parser(name).add_argument("direction")
    args = p.parse_args()
    (build if args.cmd == "build" else check)(args.direction)


if __name__ == "__main__":
    main()
