"""Проверка входа гейта v3 — для входа из ОБЪЯВЛЕННЫХ КАРТОЧЕК.

Почему не v2. `health-gate-leakcheck-v2.sh` проверять этот вход НЕ МОЖЕТ, и это
не мелочь конфигурации: его гейт D требует, чтобы `context/01-current-state.md`
побайтно совпадал с `<срез>:CURRENT.md` старого пакета. То есть сам инструмент
проверки был построен под вход, который done_when 5 не называет. Запуск v2 на
папке карточек оставлен в улике как КРАСНЫЙ — см. раздел «Как проверялось».

Что переносится из v2 без изменений:
  Гейт A (валидность)   — проба ДОЛЖНА встречаться >0 раз в утаённом принятом
                          отчёте. Ноль -> проба негодна -> КРАСНЫЙ, не зелёный.
  Гейт B (специфичность)— проба ДОЛЖНА встречаться 0 раз в законном входе: в
                          срезе состояния ДО дня И в билете. Иначе это
                          унаследованная лексика, а не след ответа -> НЕГОДНА.
  Гейт C (утечка)       — годная проба должна встречаться 0 раз в карточках,
                          то есть в том, что автор ноги СОЧИНИЛ САМ.
  Гейт E (комплаенс)    — возврат прогона содержит блок ПРОЧИТАНО, называющий
                          каждый файл запечатанной папки.
  Гейт F (чистота)      — билет несёт только дословные реплики и нейтральную
                          нумерацию.
  Самотест              — проба, дававшая ложный зелёный в v1, обязана быть
                          отвергнута гейтом A на дне 22 и принята на дне 21.

Что ДОБАВЛЕНО, потому что вход сменил природу:

  Гейт D (объявленный список). Раньше комплект проверялся побайтным равенством
  с файлами старого пакета. Теперь проверяется другое и более сильное: множество
  поданных карточек РАВНО объявленному списку. Все 15 обязательных на месте;
  каждая поданная необязательная входит в {16,17,18} и несёт строку условия;
  ни одного файла сверх списка.

  Гейт P (числовой провенанс). Английские пробы по русским карточкам почти не
  срабатывают — гейт C на смене языка вырождается в тавтологию ровно так же, как
  вырождалась проверка v1. Поэтому вводится проверка, языку безразличная: КАЖДОЕ
  число, стоящее в карточках, обязано встречаться в улике по срезу ДО дня.
  Ответ дня физически появился ПОЗЖЕ среза, поэтому любое число из ответа
  провенанс не пройдёт. Расхождения печатаются поимённо, а не глотаются.

  Гейт G (самотест утечки). Копия карточки намеренно отравляется предложением из
  утаённого ответа. Если C и P на ней не краснеют — проверка деградировала и
  зелёный запрещён.

Зелёный невозможен при нуле годных проб и при непройденном самотесте.

Запуск:  python health-gate-cards-check-v3.py [возврат-day21] [возврат-day22]
"""
import os
import re
import subprocess
import sys
import unicodedata

GATE_DIR = os.environ.get(
    "GATE_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "health-gate-cards"))
EVID = os.environ.get("EVID", "C:/projects/solmax-operating-substrate")
PIN = os.environ.get("PIN", "f1289413bf29eaf9bf205daf0d1506198e8183fd")
W = "packs/health-reclamation/workspace"

SLICE = {"day21": "6192699", "day22": "78f8607"}
DATE = {"day21": "2026-07-21", "day22": "2026-07-22"}

MANDATORY = [
    "owner.profile", "owner.mission", "health.nutrition.menu.current",
    "health.nutrition.budget", "health.nutrition.substitutions",
    "health.nutrition.corrections", "health.training.programme.current",
    "health.training.phase", "health.training.progression",
    "health.training.risk_branches", "health.training.recovery",
    "health.state.next_action", "health.metrics.baseline",
    "health.policy.unknowns", "health.observation.latest_training",
]
OPTIONAL = ["health.nutrition.preferences", "health.nutrition.prep",
            "health.nutrition.deviations_policy"]

# Пробы — строки из утаённого принятого отчёта соответствующего дня.
PROBES = {
    "day21": ["passata", "does not silently rewrite", "no missed-work debt exists",
              "does not establish a comparable", "unpalatable melon",
              "Full-day disposition", "2,400", "190–210 g"],
    "day22": ["durable correction", "known-false stored premise",
              "nutrition-menu-2026-07-22-v2", "180 g drained weight",
              "are not current menu suggestions", "Persistent nutrition correction",
              "550 g raw"],
}

# Авторские русские пробы: гейт A к ним неприменим (отчёт английский), поэтому
# они НЕ засчитываются в число годных. Это дополнительная сеть на смене языка.
PROBES_RU = {
    "day21": ["молча не переписыв", "отдельной операции выбора",
              "невкусн", "тяга к сладкому 2026-07-21"],
    "day22": ["постоянн", "ложн", "-v2", "отцеженн"],
}

FAIL = []


def note(s):
    print(s)


def fail(s):
    print("FAIL  " + s)
    FAIL.append(s)


def show(rev, path):
    r = subprocess.run(["git", "-C", EVID, "show", "%s:%s" % (rev, path)],
                       capture_output=True)
    return r.stdout.decode("utf-8") if r.returncode == 0 else ""


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def count(hay, needle):
    return hay.lower().count(needle.lower())


def card_files(day):
    d = os.path.join(GATE_DIR, day, "context")
    return sorted(os.path.join(d, f) for f in os.listdir(d))


def cards_text(day):
    return "\n".join(read(p) for p in card_files(day))


def evidence_text(day):
    rev = SLICE[day]
    parts = [show(rev, "%s/CURRENT.md" % W),
             show(rev, "%s/CONTINUATION.md" % W),
             show(rev, "%s/versions/first-phase-2026-07-20-v1.md" % W)]
    for d in ("2026-07-20", "2026-07-21"):
        if d < DATE[day]:
            parts.append(show(rev, "%s/reports/day-report-%s.md" % (W, d)))
    return "\n".join(parts)


NUM = re.compile(r"\d+(?:[.,]\d+)?")
ISO = re.compile(r"\d{4}-\d{2}-\d{2}")


def numbers(text):
    """Нормализованные числа: запятая -> точка. ISO-даты вырезаны и проверяются
    отдельно — иначе `2026-07-21` разваливается на обломки 2026/07/21."""
    out = set()
    text = ISO.sub(" ", re.sub(r"ссылка \d+", " ", text))
    for m in NUM.finditer(text.replace("\u00a0", " ").replace("\u202f", " ")):
        v = m.group(0).replace(",", ".")
        if v.endswith("."):
            v = v[:-1]
        try:
            f = float(v)
        except ValueError:
            continue
        out.add(("%g" % f))
    return out


def gate_D(day):
    note("")
    note("========= ГЕЙТ D — поданное множество равно объявленному списку (%s) =========" % day)
    files = card_files(day)
    got = []
    for p in files:
        m = re.match(r"^(\d\d)-(.+)\.md$", os.path.basename(p))
        if not m:
            fail("%s: файл вне формата списка: %s" % (day, os.path.basename(p)))
            continue
        got.append((int(m.group(1)), m.group(2)))
    ids = [cid for _, cid in got]
    for n, cid in enumerate(MANDATORY, 1):
        if cid not in ids:
            fail("%s: обязательная ссылка %d `%s` не подана" % (day, n, cid))
        elif dict((c, i) for i, c in got)[cid] != n:
            fail("%s: `%s` подан под номером %d, а в списке он %d"
                 % (day, cid, dict((c, i) for i, c in got)[cid], n))
    for num, cid in got:
        if cid in MANDATORY:
            continue
        if cid not in OPTIONAL:
            fail("%s: подана карточка ВНЕ объявленного списка: `%s`" % (day, cid))
            continue
        if "условие подачи" not in read(os.path.join(GATE_DIR, day, "context",
                                                     "%02d-%s.md" % (num, cid))):
            fail("%s: необязательная `%s` подана без строки условия" % (day, cid))
        else:
            note("ok    %s: необязательная %d `%s` подана с названным условием"
                 % (day, num, cid))
    extra = [f for f in os.listdir(os.path.join(GATE_DIR, day))
             if f not in ("billet.md", "context")]
    if extra:
        fail("%s: в запечатанной папке лишние объекты: %s" % (day, extra))
    note("-- %s: обязательных %d/15, необязательных %d, посторонних 0"
         % (day, sum(1 for c in ids if c in MANDATORY),
            sum(1 for c in ids if c in OPTIONAL)))


def gate_ABC(day, cards=None, label=""):
    note("")
    note("========= ГЕЙТЫ A/B/C — утечка ответа %s%s =========" % (day, label))
    answer = show(PIN, "%s/reports/day-report-%s.md" % (W, DATE[day]))
    if not answer:
        fail("%s: не читается утаённый принятый отчёт" % day)
        return 0
    billet = read(os.path.join(GATE_DIR, day, "billet.md"))
    evid = evidence_text(day)
    authored = cards if cards is not None else cards_text(day)
    valid = unusable = 0
    for p in PROBES[day]:
        a, e, b, c = count(answer, p), count(evid, p), count(billet, p), count(authored, p)
        if a == 0:
            fail("%s проба «%s»: ГЕЙТ A — в утаённом отчёте 0 вхождений. Проба ничего не проверяет." % (day, p))
            unusable += 1
            continue
        if e > 0 or b > 0:
            note("SKIP  %s проба «%s»: ГЕЙТ B — %d в срезе состояния, %d в билете. Законная лексика, не след ответа."
                 % (day, p, e, b))
            unusable += 1
            continue
        valid += 1
        if c > 0:
            fail("%s проба «%s»: ГЕЙТ C — УТЕЧКА, %d вхожд. в карточках (в ответе %d)." % (day, p, c, a))
        else:
            note("ok    %s проба «%s»: годна (ответ %d) · срез 0 · билет 0 · карточки %d" % (day, p, a, c))
    note("-- %s: годных проб %d, негодных %d" % (day, valid, unusable))
    if valid < 3:
        fail("%s: годных проб %d (<3). Зелёный при нуле годных проб невозможен." % (day, valid))
    ru_hits = 0
    for p in PROBES_RU[day]:
        c = count(authored, p)
        if c > 0:
            ru_hits += 1
            note("     %s русская проба «%s»: %d вхожд. в карточках — смотреть глазами" % (day, p, c))
    note("-- %s: русских проб сработало %d (не засчитываются в годные)" % (day, ru_hits))
    return valid


def gate_P(day, cards=None, label=""):
    note("")
    note("========= ГЕЙТ P — числовой провенанс карточек %s%s =========" % (day, label))
    text = cards if cards is not None else cards_text(day)
    evid = evidence_text(day)
    have = numbers(evid)
    IGNORE = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "0"}
    miss = sorted(n for n in numbers(text) if n not in have and n not in IGNORE)
    # Даты: либо стоят в улике среза, либо это сам проверяемый день и соседний —
    # дату сегодняшнего дня операция знает и без карточек, ответом она не является.
    own = {DATE[day], "2026-07-%02d" % (int(DATE[day][-2:]) + 1)}
    dmiss = sorted(d for d in set(ISO.findall(text)) if d not in evid and d not in own)
    if miss:
        fail("%s: числа в карточках, которых НЕТ в улике по срезу %s: %s"
             % (day, SLICE[day], ", ".join(miss)))
    if dmiss:
        fail("%s: даты в карточках, которых НЕТ в улике по срезу %s: %s"
             % (day, SLICE[day], ", ".join(dmiss)))
    if not miss and not dmiss:
        note("ok    %s: каждое число и каждая дата карточек прослеживаются к срезу %s"
             % (day, SLICE[day]))
    return miss + dmiss


def gate_F(day):
    note("")
    note("========= ГЕЙТ F — структурная чистота билета %s =========" % day)
    bad = 0
    for ln, line in enumerate(read(os.path.join(GATE_DIR, day, "billet.md")).split("\n"), 1):
        if not line.strip():
            continue
        if (line.startswith(">") or re.match(r"^## Сообщение \d", line)
                or line == "# Реплики владельца за день"
                or line.startswith("SEALED-INPUT: ")
                or line.startswith("Ниже дословные сообщения")
                or line.startswith("интерпретации или разметки смысла")):
            continue
        fail("%s billet.md:%d — строка говорит О репликах, а не является репликой: «%s»" % (day, ln, line))
        bad += 1
    if not bad:
        note("ok    %s: билет несёт только дословные реплики и нейтральную нумерацию" % day)


def gate_E(day, runfile):
    note("")
    note("========= ГЕЙТ E — комплаенс %s =========" % day)
    if not runfile or not os.path.isfile(runfile):
        note("SKIP  возврат прогона ещё не сохранён: %s" % runfile)
        return
    run = read(runfile)
    if "ПРОЧИТАНО" not in run:
        fail("%s: в возврате нет блока ПРОЧИТАНО" % day)
        return
    missing = 0
    root = os.path.join(GATE_DIR, day)
    for dirpath, _, names in os.walk(root):
        for n in names:
            rel = os.path.relpath(os.path.join(dirpath, n), root).replace("\\", "/")
            if rel in run:
                note("ok    %s ПРОЧИТАНО называет %s" % (day, rel))
            else:
                fail("%s: ПРОЧИТАНО не называет %s" % (day, rel))
                missing += 1
    if not missing:
        note("-- %s: комплаенс подтверждён присутствием всех имён" % day)


def selftest_v1_probe():
    note("")
    note("========= САМОТЕСТ 1 — регрессия к дефекту v1 =========")
    p = "Accepted observations"
    a21 = count(show(PIN, "%s/reports/day-report-2026-07-21.md" % W), p)
    a22 = count(show(PIN, "%s/reports/day-report-2026-07-22.md" % W), p)
    if a21 > 0:
        note("ok    проба v1 годна на дне 21 (%d вхожд.) — гейт A её пропускает" % a21)
    else:
        fail("самотест: проба v1 неожиданно негодна и на дне 21")
    if a22 == 0:
        note("ok    проба v1 ОТВЕРГНУТА на дне 22 (0 вхожд.) — гейт A сработал")
    else:
        fail("самотест: проба v1 стала годной на дне 22 — проверка деградировала")


def gate_G():
    """Отравленная карточка обязана покраснеть. Иначе проверка ничего не ловит."""
    note("")
    note("========= ГЕЙТ G — самотест утечки на отравленной карточке =========")
    poison = ("\n\nбелая рыба, треска, хек и минтай are not current menu suggestions;"
              " выбрана версия nutrition-menu-2026-07-22-v2 с тунцом 180 g drained weight,"
              " оценка дня 2550 ккал при весе 123,9 кг;"
              " оценка дня 2 200–2 550 ккал\n")
    global FAIL
    clean_p = set(gate_P("day22", label=" [чистая база самотеста]"))
    keep, FAIL = FAIL, []
    gate_ABC("day22", cards=cards_text("day22") + poison, label=" [ОТРАВЛЕНО]")
    miss = gate_P("day22", cards=cards_text("day22") + poison, label=" [ОТРАВЛЕНО]")
    caught_c = any("ГЕЙТ C" in f for f in FAIL)
    caught_p = bool(set(miss) - clean_p)
    FAIL = keep
    if caught_c:
        note("ok    гейт C покраснел на отравленной карточке")
    else:
        fail("самотест: гейт C НЕ поймал отравление — проверка вырождена")
    if caught_p:
        note("ok    гейт P покраснел на отравленной карточке")
    else:
        fail("самотест: гейт P НЕ поймал отравление — проверка вырождена")


for d in ("day21", "day22"):
    gate_D(d)
selftest_v1_probe()
for d in ("day21", "day22"):
    gate_ABC(d)
    gate_P(d)
    gate_F(d)
gate_G()
gate_E("day21", sys.argv[1] if len(sys.argv) > 1 else None)
gate_E("day22", sys.argv[2] if len(sys.argv) > 2 else None)

print("")
if not FAIL:
    print("ИТОГ: ЗЕЛЁНЫЙ — все гейты пройдены.")
    sys.exit(0)
print("ИТОГ: КРАСНЫЙ — см. строки FAIL выше.")
sys.exit(1)
