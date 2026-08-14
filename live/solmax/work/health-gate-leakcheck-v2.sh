#!/usr/bin/env bash
# Проверка утечки v2 — построена так, чтобы НЕ МОЧЬ дать ложный зелёный.
#
# Дефект v1: `grep -c 'Accepted observations' <билет>` -> 0 -> «утечки нет».
# Ноль возвращался и когда утечки нет, и когда пробы просто не существует в
# документе такого типа. Для дня 22 верно было второе: секции `## Accepted
# observations` в отчёте за 22-е нет вовсе (в отчётах за 20 и 21 — есть).
# Проверка молча выродилась в тавтологию ровно на том дне, чей билет и протёк.
#
# Принцип v2: зелёный требует СНАЧАЛА доказать, что проба вообще работает —
# то есть НАЙТИ её там, где она обязана быть. Утверждение о присутствии идёт
# первым, утверждение об отсутствии — только после него.
#
#   Гейт A (валидность):    проба ДОЛЖНА встречаться >0 раз в утаённом принятом
#                           отчёте. Ноль -> проба негодна -> КРАСНЫЙ, не зелёный.
#   Гейт B (специфичность): проба ДОЛЖНА встречаться 0 раз в объявленных срезах
#                           состояния 01-04. Иначе это унаследованная лексика
#                           состояния, а не след ответа -> проба НЕГОДНА, о чём
#                           сообщается вслух, а не засчитывается как чистая.
#   Гейт C (утечка):        годная проба должна встречаться 0 раз в том, что
#                           автор ноги СОЧИНИЛ САМ: billet.md + 05-continuity-cards.md.
#                           Именно там жили обе настоящие утечки.
#   Гейт D (комплект):      каждый объявленный файл существует; срезы состояния
#                           побайтно равны заявленным git-блобам.
#   Гейт E (комплаенс):     возврат прогона содержит блок ПРОЧИТАНО, называющий
#                           каждый файл запечатанной папки.
#
# Зелёный невозможен при нуле годных проб.

#
# ПРИМЕНЕНИЕ К СЛЕДУЮЩЕМУ ДНЮ (метод, а не разовый скрипт):
#   1. Собери запечатанную папку dayNN/{billet.md,context/}.
#   2. Добавь строку в MANIFEST и вызов `check_day dayNN <дата>` внизу.
#   3. Заполни PROBES_dayNN строками из УТАЁННОГО принятого отчёта этого дня.
#      Скрипт сам отсеет негодные: пустые в отчёте (гейт A) и унаследованные
#      из состояния (гейт B). Гадать, какая проба хороша, не нужно — он скажет.
#   4. Прогон засчитывается только при `ИТОГ: ЗЕЛЁНЫЙ`.
#
# Переменные окружения: GATE_DIR (папка прогонов), EVID (репозиторий улик), PIN.

set -uo pipefail
GATE_DIR="${GATE_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
EVID="${EVID:-/c/projects/solmax-operating-substrate}"
PIN="${PIN:-f1289413bf29eaf9bf205daf0d1506198e8183fd}"
RPT="packs/health-reclamation/workspace/reports"
FAIL=0
note() { printf '%s\n' "$*"; }
fail() { printf 'FAIL  %s\n' "$*"; FAIL=1; }

# --- пробы: строки из утаённого принятого отчёта соответствующего дня ---
PROBES_day21='passata
does not silently rewrite
no missed-work debt exists
does not establish a comparable
unpalatable melon
Full-day disposition'
PROBES_day22='durable correction
known-false stored premise
nutrition-menu-2026-07-22-v2
180 g drained weight
are not current menu suggestions
Persistent nutrition correction'

# --- САМОТЕСТ: проба, давшая ложный зелёный в v1 ---
# `Accepted observations` есть в отчётах за 20 и 21, но ОТСУТСТВУЕТ в отчёте за 22.
# v1 читала это отсутствие как «утечки нет». v2 обязана отвергнуть её на дне 22
# гейтом A и принять на дне 21. Если самотест когда-нибудь перестанет срабатывать —
# значит проверка деградировала обратно к тавтологии.
selftest() {
  note ""
  note "==================== САМОТЕСТ — регрессия к дефекту v1 ===================="
  local p='Accepted observations' a21 a22
  a21=$(git -C "$EVID" show "$PIN:$RPT/day-report-2026-07-21.md" | grep -ic -- "$p")
  a22=$(git -C "$EVID" show "$PIN:$RPT/day-report-2026-07-22.md" | grep -ic -- "$p")
  if [ "$a21" -gt 0 ]; then note "ok    проба v1 годна на дне 21 ($a21 вхожд.) — гейт A её пропускает"
  else fail "самотест: проба v1 неожиданно негодна и на дне 21"; fi
  if [ "$a22" -eq 0 ]; then note "ok    проба v1 ОТВЕРГНУТА на дне 22 (0 вхожд. в утаённом отчёте) — гейт A сработал"
  else fail "самотест: проба v1 стала годной на дне 22 — проверка деградировала"; fi
  note "-- дефект v1 воспроизведён и перехвачен: ложный зелёный больше невозможен"
}

check_day() {
  local day="$1" date="$2" probes_var="PROBES_$1"
  local probes="${!probes_var}"
  local answer valid=0 unusable=0
  note ""
  note "==================== $day (утаённый ответ: day-report-$date.md) ===================="
  answer="$(git -C "$EVID" show "$PIN:$RPT/day-report-$date.md" 2>/dev/null)"
  [ -n "$answer" ] || { fail "$day: не читается утаённый принятый отчёт"; return; }

  local authored state_ctx
  authored="$(cat "$GATE_DIR/$day/billet.md" "$GATE_DIR/$day/context/05-continuity-cards.md" 2>/dev/null)"
  [ -n "$authored" ] || { fail "$day: не читается сочинённая часть входа"; return; }
  state_ctx="$(cat "$GATE_DIR/$day"/context/0[1-4]-*.md 2>/dev/null)"
  [ -n "$state_ctx" ] || { fail "$day: не читаются срезы состояния 01-04"; return; }

  while IFS= read -r p; do
    [ -n "$p" ] || continue
    local a s c
    a=$(printf '%s' "$answer"    | grep -ic -- "$p")
    s=$(printf '%s' "$state_ctx" | grep -ic -- "$p")
    c=$(printf '%s' "$authored"  | grep -ic -- "$p")
    if [ "$a" -eq 0 ]; then
      fail "$day проба «$p»: ГЕЙТ A — в утаённом отчёте 0 вхождений. Проба ничего не проверяет."
      unusable=$((unusable+1)); continue
    fi
    if [ "$s" -gt 0 ]; then
      note "SKIP  $day проба «$p»: ГЕЙТ B — $s вхожд. в объявленном состоянии. Лексика состояния, не след ответа."
      unusable=$((unusable+1)); continue
    fi
    valid=$((valid+1))
    if [ "$c" -gt 0 ]; then
      fail "$day проба «$p»: ГЕЙТ C — УТЕЧКА, $c вхожд. в сочинённой части входа (ответ: $a)."
    else
      note "ok    $day проба «$p»: годна (ответ $a) · состояние 0 · вход 0"
    fi
  done <<< "$probes"

  note "-- $day: годных проб $valid, негодных $unusable"
  [ "$valid" -ge 3 ] || fail "$day: годных проб $valid (<3). Зелёный при нуле годных проб невозможен."
}

check_manifest() {
  note ""
  note "==================== ГЕЙТ D — комплект и провенанс ===================="
  local ok=1
  while IFS='|' read -r rel rev src; do
    [ -n "$rel" ] || continue
    local f="$GATE_DIR/$rel"
    if [ ! -f "$f" ]; then fail "нет файла $rel"; ok=0; continue; fi
    if [ "$rev" != "-" ]; then
      if git -C "$EVID" show "$rev:packs/health-reclamation/workspace/$src" 2>/dev/null | diff -q - "$f" >/dev/null 2>&1; then
        note "ok    $rel побайтно == $rev:$src"
      else
        fail "$rel НЕ совпадает с $rev:$src"; ok=0
      fi
    else
      note "ok    $rel присутствует (сочинён этой ногой)"
    fi
  done <<'MANIFEST'
day21/billet.md|-|-
day21/context/01-current-state.md|6192699|CURRENT.md
day21/context/02-continuation.md|6192699|CONTINUATION.md
day21/context/03-programme-and-menu.md|-|-
day21/context/04-day-support-procedure.md|-|-
day21/context/05-continuity-cards.md|-|-
day22/billet.md|-|-
day22/context/01-current-state.md|78f8607|CURRENT.md
day22/context/02-continuation.md|78f8607|CONTINUATION.md
day22/context/03-programme-and-menu.md|-|-
day22/context/04-day-support-procedure.md|-|-
day22/context/05-continuity-cards.md|-|-
MANIFEST
  [ "$ok" -eq 1 ] || true
}

# --- ГЕЙТ F: структурная чистота билета ---
# Пробы по словарю недостаточны: ярлык «durable correction authority» в билете 22-го
# не ловится ими, потому что то же словосочетание законно живёт в состоянии как
# процедурная лексика (гейт B его отводит). Поэтому билет проверяется СТРУКТУРНО:
# в нём разрешены только дословные реплики владельца и нейтральная нумерация.
# Любая строка, говорящая О репликах, — нарушение, независимо от словаря.
check_billet_purity() {
  local day="$1" f="$GATE_DIR/$1/billet.md" bad=0 ln=0
  note ""
  note "==================== ГЕЙТ F — структурная чистота билета $day ===================="
  [ -f "$f" ] || { fail "$day: нет billet.md"; return; }
  while IFS= read -r line; do
    ln=$((ln+1))
    [ -z "${line// /}" ] && continue
    case "$line" in
      '>'*)                       continue ;;  # дословная реплика владельца
      '## Сообщение '[0-9]*)      continue ;;  # нейтральная нумерация
      '# Реплики владельца за день') continue ;;
      'SEALED-INPUT: '*)          continue ;;
      'END_OF_FILE: '*)           continue ;;
      'Ниже дословные сообщения'*|'интерпретации или разметки смысла'*) continue ;;
      *) fail "$day billet.md:$ln — строка говорит О репликах, а не является репликой: «$line»"; bad=$((bad+1)) ;;
    esac
  done < "$f"
  [ "$bad" -eq 0 ] && note "ok    $day: билет несёт только дословные реплики и нейтральную нумерацию"
}

# --- ГЕЙТ E: комплаенс возврата прогона (присутствие, а не отсутствие) ---
check_compliance() {
  local day="$1" runfile="$2"
  note ""
  note "==================== ГЕЙТ E — комплаенс $day ===================="
  if [ ! -f "$runfile" ]; then note "SKIP  возврат прогона ещё не сохранён: $runfile"; return; fi
  grep -q 'ПРОЧИТАНО' "$runfile" || { fail "$day: в возврате нет блока ПРОЧИТАНО"; return; }
  local missing=0
  for f in $(cd "$GATE_DIR/$day" && find . -type f | sed 's|^\./||'); do
    if grep -qF "$f" "$runfile"; then note "ok    $day ПРОЧИТАНО называет $f"
    else fail "$day: ПРОЧИТАНО не называет $f"; missing=$((missing+1)); fi
  done
  [ "$missing" -eq 0 ] && note "-- $day: комплаенс подтверждён присутствием всех имён"
}

check_manifest
selftest
check_day day21 2026-07-21
check_day day22 2026-07-22
check_billet_purity day21
check_billet_purity day22
check_compliance day21 "${1:-/nonexistent}"
check_compliance day22 "${2:-/nonexistent}"

note ""
if [ "$FAIL" -eq 0 ]; then note "ИТОГ: ЗЕЛЁНЫЙ — все гейты пройдены."; exit 0
else note "ИТОГ: КРАСНЫЙ — см. строки FAIL выше."; exit 1; fi
