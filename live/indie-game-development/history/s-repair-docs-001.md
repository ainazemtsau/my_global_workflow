# s-repair-docs-001 — g-9c41 — pre-build documentation hygiene audit + repair

date: 2026-06-22
play: audit → repair (owner-directed canon hygiene before the S0 build)
direction: indie-game-development
node: g-9c41
input: owner — check the documentation for stale/contradictory data before the build session (this bit us before: planned, started passing data + new chats, and because multiple docs held different/contradictory logic, the plan broke). Archive anything outdated; make the files we'll work in clean, complete, non-contradictory.

---

## RESULT

```
play: audit+repair
goal: найти и устранить устаревшие/противоречивые данные в гас-движок документации ПЕРЕД строительной сессией S0; заархивировать устаревшее или пометить; набор чтения S0 сделать непротиворечивым

outcome:
  10-агентный аудит (wf_91c1ccf8: 8 пер-доковых читателей + синтез + скептик), каждый док прочитан полностью vs синтез-авторитет work/gas-cellsize-levelscale-2026-06-22.md §1-§12.
  ГЛАВНАЯ НАХОДКА (подтверждена у источника): набор чтения S0-PLAN ВНУТРЕННЕ ПРОТИВОРЕЧИВ — (a) tie-breaker §1-§12 в наборе ОТСУТСТВОВАЛ (последняя авторитетная версия недостижима из dev-plan-graph «nothing lost»); (b) 2 дока В наборе несли устаревший ПОТИРОВЫЙ 25см — gas-model-decision §0/§3.2 (T0=25см авторитетно) + locked-slices point2 («cell-SIZE LOD») — против «50см ГЛОБАЛЬНО, drop-25cm» (§10 R7/§12). Свежий S0-чат построил бы схему клеток на покомнатном миксе → вернул ловушку №2 (cross-res re-flux) + пропустил day-one розетки cap/tick_divisor → миграция чексуммы позже. ЭТО ровно класс противоречия, ради ловли которого запущен аудит.
  ЧИСТЫЕ (не тронуты): c-exec-013-call.md = ЖИВОЙ S0 CALL, уже совпадает с §1-§12 (build-ready, цель NOW.next); g9c41-drift-guard.md = чист.
  НИЧЕГО НЕ АРХИВИРОВАНО: все доки несут валидный контент (анализ/история = валидный путь, НЕ устаревшая рекомендация) → фикс = SUPERSEDED-баннеры + указатели, НЕ архив.

evidence:
  - Workflow wf_91c1ccf8 (10 агентов, 997k токенов): 8 пер-доковых отчётов + синтез + скептик-верификатор; flag-vs-path split верен; over-reach нет.
  - Источник подтверждён: NOW.md строки 27-28 (SINGLE ENTRY POINT набор без §1-§12); gas-model-decision §0 line17/§3.2; locked-slices point2 line20; INDEX line36; full-audit §5.1/R29; frontier-verdict line43; converge host-single-writer.
  - 12 правок применено (баннеры/указатели, перечислены в state_changes); 2 дока подтверждены чистыми; 0 архивировано.

state_changes:
  - work/dev-plan-graph-2026-06-22.md: + TIE-BREAKER banner (entry doc; газ 50см-global, 4 GAP-розетки, room-rollup S4 обязателен@150, кап опц., высотные полосы S3, поле энергии S6, фаза=строить).
  - work/gas-engine-INDEX.md: + header SUPERSEDED banner + cell-size table row fix (покомнатно→50см global) + ОТКРЫТО-section SUPERSEDED marker.
  - work/gas-model-architecture-decision-2026-06-21.md: + SUPERSEDED-IN-PART banner (§0/§3.2 потировый-25см, §3.6 2.5D-по-тиру, §9 пропущенные GAP-розетки, масштаб; ВАЛИДНЫ D1/D7-D13/химия/§10/§11/§14).
  - knowledge/g9c41-architecture-locked-slices.md: + POINTER (point2 cell-SIZE-LOD / point3 → уточнены §10-12; НЕ правка лока; ратификация = owner re-shape).
  - work/grid-vs-graph-resolution-2026-06-22.md: + SUPERSEDED-IN-PART banner (§8 rollup-timing → обязателен; размер → 50см global).
  - work/detail-authority-cost-model-2026-06-22.md: + SUPERSEDED-IN-PART banner (§4 A/B+3-ведра РЕШЕНЫ; размер; кап).
  - work/gas-architecture-full-audit-2026-06-22.md: + SUPERSEDED-IN-PART banner (§5.1 покомнатный размер; §3 NEEDS-DECISION#3 single-writer→input-lockstep РЕШЕНО; §5.3/§5.5 масштаб→150 rollup обязателен).
  - work/gas-frontier-verdict-2026-06-22.md: + SUPERSEDED-IN-PART banner (§БАЗА размер по комнате→50см global; 40-комнат=артефакт).
  - work/gas-frontier-research-2026-06-22.md: + drop-25cm line (к само-помеченному SUPERSEDED).
  - work/converge-g-9c41.md + work/converge-g-9c41-arch.md: + SUPERSEDED banner (host-single-writer/chunked-delta/«клиенты реконструируют» → input-lockstep; Wave-1/2 история).
  - work/gas-cellsize-levelscale-2026-06-22.md: + self-consistency banner (§10-12=финал; §1-9 ранний per-room=перекрыт).
  - НЕ ТРОНУТЫ: c-exec-013-call.md (живой чистый CALL), g9c41-drift-guard.md (чист).
  - NOW активная ставка/done_when/локед-факты НЕ изменены (только баннеры/указатели; carry-forward §1-§12 в S0 CALL уже добавлен s-research-017).

captures:
  - "ОТКРЫТО для owner re-shape (НЕ этой сессии): locked-slices point2 «cell-SIZE LOD» формально уточнить в «50см-global авторитет + room-rollup как ось LOD»; ратификация = owner-signed re-shape сессия. Сейчас стоит POINTER, лок-факт не изменён."
  - "Если будущая S2-сессия (мультиплеер) — НЕ читать converge-g-9c41/-arch как живой неткод-авторитет (host-single-writer/chunked-delta SUPERSEDED локом input-lockstep); метод converge валиден, replication-модель нет."
  - "Принцип гигиены: SUPERSEDED-баннер называет КОНКРЕТНЫЕ устаревшие места + указывает на §1-§12; валидный анализ/история (путь к решению) НЕ баннерится; ничего не архивируется если ≥90% валидно."

decisions_needed: []   # owner-directed hygiene; no new decisions

play_check:
  1. OPEN — owner-directed audit (доки чисты перед S0?). Read NOW + inventoried work/ + knowledge/.
  2. WORK — 10-агентный read-each-doc аудит vs §1-§12 авторитета; flag устаревшие РЕКОМЕНДАЦИИ, отделить валидный путь; синтез + скептик-верификация. Applied 12 banner/pointer fixes; 0 archived; 2 confirmed clean.
  3. CLOSE — этот RESULT; набор чтения S0 непротиворечив, tie-breaker достижим отовсюду.

log: "2026-06-22 — audit+repair (g-9c41, s-repair-docs-001): пред-строительная гигиена доков. 10-агентный аудит нашёл: набор чтения S0 противоречив (tie-breaker §1-§12 отсутствовал; gas-model-decision+locked-slices несли потировый-25см vs 50см-global). Чистые: c-exec-013 (живой CALL) + drift-guard. 0 архивировано (все валидны). 12 SUPERSEDED-баннеров/указателей применено (+ неткод single-writer→input-lockstep помечен). Набор S0 теперь непротиворечив. → history/s-repair-docs-001.md"

next: |
  Документация чиста + непротиворечива для S0. Следующий шаг (за владельцем) = открыть PLAN слайса S0 в СВЕЖЕЙ сессии
  (GasCoopGame, owner present) через живой c-exec-013-call.md / NOW.next — он первым делом ингестит dev-plan-graph (+ его
  tie-breaker banner → §1-§12) + locked-slices + drift-guard + 3 decision-дока (теперь с SUPERSEDED-баннерами) + синтез §1-§12.
  ОТКРЫТО для будущего owner re-shape: формальная ратификация cell-size-уточнения в locked-slices point2 (сейчас POINTER).
```

END_OF_FILE: live/indie-game-development/history/s-repair-docs-001.md
