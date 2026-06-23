# s-research-017 — g-9c41 — research/orient handoff (reactions-near-player, process, hand to build)

date: 2026-06-22
play: research (orientation/handoff — no workflow; owner asked to stop analysis and move to practice)
direction: indie-game-development
node: g-9c41
input: owner — (a) quick reaction clarification: I spoke mostly of coarse reactions, but reactions work everywhere incl. NEAR the player where I expect QUALITY — is that laid in? (if yes, no need to answer; optionally a 25cm thin layer later). (b) MAIN: I'm a bit lost on what stage we're at and the next step. Proposes a way to work: lay architecture first; each chunk ends in something testable in a SANDBOX (Odin Inspector settings I change & watch, NOT a script); ensure everything is extensible; AUDIT before each task (weak spots / gameplay blockers / improvements / questions); careful approach because it's core; focus only on this (marketing/visual later); checks at each stage incl. visually (I check in sandbox = one layer, code-assistant audits = another); not super-big chunks — one feature, look at it, close it. Invites me to propose an alternative.

---

## RESULT

```
play: research
goal: ответить (а) реакции у игрока качественно+заложено ли; (б) ориентация на стадии + рекомендованный процесс дальше + следующий конкретный шаг

outcome:
  (а) РЕАКЦИИ У ИГРОКА — заложено: решаются на ГРУБОМ (детерминизм, подход игрока не само-детонирует), но РИСУЮТСЯ мелко-качественно в near-окне (грубое событие → expand → видишь облако/фронт/завиток). Контакт==картинка. 25см опц. визуал сверху — да. Тонкость: авторитетно на уровне клетки/полосы, не на 25см-форме (визуально незаметно).
  (б) ОРИЕНТАЦИЯ: фаза ПРОЕКТИРОВАНИЯ ЗАКРЫТА (6 сессий разбора s-research-012..016 → work/gas-cellsize-levelscale §1-§12; осуществимость приоритета №1 доказана). Дальше = СТРОЙКА маленькими кусками. Гонять разбор дальше не нужно (owner прав).
  ПРОЦЕСС: хотелки владельца (кусок→сэндбокс-тест→ок→код-аудит→след.кусок + аудит-до-задачи + расширяемость + фокус-только-на-этом) = УЖЕ залоченная slice-методология + гейтовый контур. Подтверждено и заострено в петлю (Аудит+План → Строим один кусок → Ты в сэндбоксе крутишь Odin → Код-аудит G5 → Закрыли) + хребет S0→S6. Пометка: S0/S1/S3/S5/S6 = owner-eye глазами в сэндбоксе; S2/S4 (мультиплеер/rollup) = код-ассистент хеши/пробы (глазами не увидишь).
  СЛЕДУЮЩИЙ ШАГ: PLAN слайса S0 (GasCoopGame, owner present, СВЕЖАЯ сессия) — первый кусок = сэндбокс + вокселизатор + грань-поток + розетки; первым делом впитывает §1-§12 + подтверждает решения + классифицирует механики.

evidence:
  - Без workflow (owner явно просил прекратить разбор, перейти к практике) — синтез предыдущих 6 сессий + залоченной методологии.
  - Slice-методология + гейтовый контур = NOW.md (active bet S0, wave_plan slice spine S0-S6, done_when owner-eye gate) + AGENTS.md (PLAN → RED-first → -Deliver → G5).
  - Реакции-у-игрока: gas-model §3.5 (реакция читает грубые тоталы) + контакт==картинка (INDEX hard-constraint #3) + near-окно expand (cost-model §5).

state_changes:
  - NOW.md: S0 CALL context дополнен ОБЯЗАТЕЛЬНЫМ чтением work/gas-cellsize-levelscale-2026-06-22.md §1-§12 + ключевые решения (50см global, drop-25cm-authoritative, room-rollup S4 mandatory@150, кап-опционален, 4 GAP-розетки, geometry=кратно-газу, height-bands→S3, energy→S6, 3 binding probes). CARRY-FORWARD only — active bet/done_when S0 НЕ изменены.
  - LOG.md: +1 строка (s-research-017).
  - history/s-research-017.md: этот файл.
  - work/, залоченная архитектура: НЕ тронуты.

captures:
  - "Реакции у игрока: решение на грубом (тоталы), рендер мелко в near-окне = качественно (контакт==картинка). 25см опц. визуал. Авторитетно на клетке/полосе не на 25см-форме (sub-cell форма решает исход = ведро-3, ≤2-3 комнаты). Подтвердить класс в PLAN слайса."
  - "ПРОЦЕСС подтверждён владельцем = slice-методология: каждый кусок (слайс) кончается видимым результатом в сэндбоксе (Odin-настройки, не скрипт); 2 слоя проверки = owner-eye (сэндбокс) + код-ассистент G5/пробы; аудит-до-задачи = шаг PLAN. S2/S4 = НЕ owner-eye (мультиплеер/rollup проверяются хешами/пробами)."
  - "S0-PLAN (build, свежая сессия) ДОЛЖЕН впитать work/gas-cellsize-levelscale §1-§12 ПЕРВЫМ ДЕЛОМ + подтвердить с владельцем: 50см global, drop-25cm-authoritative, 4 GAP-розетки, кап-опционален, geometry-кратно-газу. Решения slice-specific (height-bands число → S3, energy-accumulator → S6)."

decisions_needed: []   # ориентация + handoff; решения ратифицируются в S0-PLAN

play_check:
  1. Recite — DONE: (а) реакции-у-игрока + (б) как-идти-дальше восстановлены.
  2. Investigate — DONE (без workflow, по просьбе владельца): синтез 6 сессий + залоченной методологии; реакции-у-игрока сверены с каноном.
  3. Confidence — DONE: процесс владельца = уже залоченная методология (высокая увер.); следующий шаг назван конкретно.
  4. Close — DONE: этот RESULT; ответ в формате владельца (петля + хребет-таблица, минимум жаргона); carry-forward в NOW.next; handoff на S0-PLAN.

log: "2026-06-22 — research/orient (g-9c41, s-research-017): owner закрывает проектирование→стройка. Реакции-у-игрока = грубо-решаются/мелко-рисуются (заложено). Процесс владельца = уже залоченная slice-методология + гейтовый контур (подтверждено, заострено в петлю + хребет S0→S6; S2/S4 не owner-eye). Следующий шаг = PLAN слайса S0 (свежая сессия, GasCoopGame), впитывает §1-§12. Carry-forward в NOW.next S0 CALL. → history/s-research-017.md"

next: |
  awaiting_owner «го» → открыть PLAN слайса S0 в СВЕЖЕЙ сессии (GasCoopGame, owner present). Первый кусок = сэндбокс +
  вокселизатор (уровень→3D-сетка по граням) + грань-поток (газ наливает комнату) + §9-швы/4-GAP-розетки day-one. PLAN
  первым делом впитывает work/gas-cellsize-levelscale §1-§12 + 4 decision-дока + locked-slices + drift-guard, подтверждает
  решения с владельцем (50см global / drop-25cm / розетки / кап-опционален), классифицирует механики ведро-1/2/3, §Re-sync
  v7→v8. Контур: PLAN → RED-first независимый test-author → build → -Deliver → fresh-session G5 + owner-eye сэндбокс.
  Это СТРОИТЕЛЬНАЯ сессия (коммиты в GasCoopGame), не research.
```

END_OF_FILE: live/indie-game-development/history/s-research-017.md
