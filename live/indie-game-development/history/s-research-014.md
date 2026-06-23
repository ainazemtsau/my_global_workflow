# s-research-014 — g-9c41 — research (Steam-CPU, gas cap, seams-in-base, gas/geometry resolution)

date: 2026-06-22
play: research
direction: indie-game-development
node: g-9c41
input: owner voice message (transcribed/garbled) — echo-numbered R1-R7: R1 target a real Steam-common low-end CPU (super-budget is rare); R2 cap on total gas volume (full-fill rare; what % fills?); R3 breachable rooms vent gas → fill limiter; R4 big halls = 1-2, "big" = medium hall with verticality; R5 don't need full ×10 LOD, ~×3-5 enough, pick cheapest by effort/payoff; R6 (MAIN) lay seams in the base NOW so optimizations are added in code later without rewrite; R7 gas 50cm global, can static geometry/grid be coarser (100cm)?

---

## RESULT

```
play: research
goal: ответить на R1-R7 (Steam-CPU / кап газа / пробои / ×3-5 / швы-в-базу / газ-50-геометрия-100) реальными данными + что заложить в S0 сейчас

outcome:
  6-агентный веер (wf_04d84caa-7f2) + 2 скептика. Выводы:
  R1: целевой CPU = 4-ядерный пол (i5-7400 = минималка Lethal Company; Steam survey май-2026 ≥4 ядра ≈92%, мода 6 ядер, 2-ядра ≈3% игнор). Мультиядро ×4 = гарантия 100% аудитории. 40 комнат @50см (59.5k) = 2-3× запас на полу (~3 раб.ядра × 32-60k = 100-180k) до оптимизаций.
  R2+R3+R4: КАП на объём газа = worst-case из неизвестного → дизайн-КОНСТАНТА N_max (~8-16k @50см) = потолок CPU по построению. Реальное заполнение 5-20% (не 100%); full-fill = вырожденный не-кейс. «+30% запас» выкинуть → «N_max по низу полосы». Breach-вент (R3) = физ.сток, «провентилируй или умри» = геймплей. ⚠ кап ограничивает АВТОРИТЕТНЫЙ сим; пузырь игрока = 2-й член (радиус, не газ) → бюджетировать оба.
  R5: самая дешёвая ×3-5 = room-rollup СТАТИЧНАЯ граница на дверях (смягчает kill-тест №1 — re-flux на неподвижной двери). Полный T0/T1/T2-LOD (×10) НЕ нужен. ⚠ развязать: кап = граница CPU (worst-case константа); rollup = масштаб комнат (код в S4 если нужно). Не дубликаты.
  R6 (главное): 6 розеток УЖЕ в S0. ВОДОРАЗДЕЛ — чексумма = версионир. публичный контракт у 2-8 нод: что меняет её ЗНАЧЕНИЕ, класть полем day-one (заглушка), иначе breaking migration. 4 GAP заложить СЕЙЧАС: cap(в чексумме=∞/0), tick_divisor(=1), void-sink region_id, resolution_tag=ПАРА(geom,gas).
  R7: газ 50см ГЛОБАЛЬНО подтверждено (убирает ловушку №2; 25см = локальный пузырь вне чексуммы). Геометрия 100см ОК при geom=ЦЕЛОЕ КРАТНОЕ gas (50→{50,100}, не 75; не мельче газа). Старт S0 1:1 → 100см сменой конфига. Шов: resolution_tag=пара + openings→faces параметризован + Conformance пинит маппинг 2:1.

evidence:
  - Workflow wf_04d84caa-7f2 (6 агентов + 2 скептика, 645k токенов).
  - STEAM (web, датир. 2026-06-22): Steam Hardware Survey май-2026 ≥4 ядра ≈92% (скептик поправил с 97%), мода 6 ядер, 2-ядра ≈3%; Lethal Company min = i5-7400 (4c/4t), Phasmophobia = i5-4590.
  - КАП: следует из залоченной sparse-active архитектуры (стоимость ∝ активным клеткам, locked §4) — структурный факт; N_max в чексумме (целочисленно, lockstep-safe).
  - ШВЫ: 6 розеток verbatim в S0 done_when (NOW.md 285-304); GAP-cap + GAP-tick_divisor подтверждены ОТСУТСТВУЮЩИМИ грепом → класть заглушками.
  - R7: openings→faces «одинаков у генераторов И размеров клетки» (grid-vs-graph §8 строки 112/124, не S0 done_when напрямую — скептик поправил источник); геометрия-кратна-газу = precondition против VScale-класса.
  - СКЕПТИК-arch HOLDS: противоречий локу НЕТ; все абсолюты на ОДНОМ неизмеренном single-core (32-120k, риск whole-CPU ×4-8) → ангар-проба меняет ЗАПАС не рычаг.
  - Продукт: work/gas-cellsize-levelscale-2026-06-22.md §10.

state_changes:
  - work/gas-cellsize-levelscale-2026-06-22.md: +§10 (R1-R7 + 4 GAP-розетки + 2 поправки скептиков).
  - LOG.md: +1 строка (s-research-014).
  - history/s-research-014.md: этот файл.
  - NOW.md / залоченная архитектура / ставка S0: НЕ ТРОНУТЫ (research информирует; входы = captures для S0-PLAN).

captures:
  - "S0-PLAN заложить 4 GAP-розетки day-one (дёшево как поля-заглушки, дорого ретрофитить): GAP-1 cap (per-region max_mass/rate_limit/dissipation В ЧЕКСУММЕ, заглушка ∞/0 — трогает масс-баланс); GAP-4 tick_divisor на регион в чексумме (=1); GAP-2 void/exterior region_id сток (метка); GAP-3 resolution_tag = ПАРА (geometry_res, gas_res), дефолт (50,50)."
  - "S0-PLAN: газ 50см ГЛОБАЛЬНО (убирает ловушку №2 cross-resolution re-flux из ранних слайсов; 25см = локальный body-tiny пузырь вне чексуммы, не размер комнаты). Геометрия = целое кратное газа (50→{50,100}, НЕ 75, не мельче газа); старт 1:1 → 100см конфигом; Conformance расширить пинить openings→faces на 2:1."
  - "Worst-case = ДВА члена, бюджетировать раздельно: авторитетный газ → КАП N_max; пузырь игрока → РАДИУС. Кап один §A-стену не убирает (пузырь рефайнит объём, не газ)."
  - "Кап vs room-rollup = РАЗНЫЕ рычаги: кап ограничивает пиковую CPU (worst-case константа независимо от размера/игроков); rollup масштабирует число комнат. Кап = архитектурная граница СЕЙЧАС; rollup = код в S4 если нужно >40-60 комнат. Возможно rollup не понадобится."
  - "Ангар-проба должна гонять single-core SCALAR И single-core Burst (+ все ядра, тяжёлый солвер, worst-case игрок-в-зале) — развязать 'полоса 32-120k scalar или Burst' + whole-CPU ×4-8. Гейтит ЗАПАС (N_max value), не выбор рычага."

decisions_needed:
  - d-cellsize-default (УТОЧНЁН): газ = 50см ГЛОБАЛЬНО (не покомнатный микс) — убирает ловушку №2; 25см возвращается локальным пузырём. Рек.: подтвердить 50см глобально.
  - d-geometry-resolution (НОВОЕ): геометрия = 50см или 100см (целое кратное газа)? Рек.: старт 1:1 (50/50) в S0, переключить 100см конфигом после зелёного Conformance. Заложить resolution_tag=пара сейчас.
  - d-gas-cap (НОВОЕ): принять КАП газа как архитектурную границу worst-case (поля в чексумме day-one, значение N_max — после ангар-пробы)? Рек.: да — делает worst-case константой по построению.
  - (несут силу прежние d-vertical-bands, d-sleep-policy, d-hangar-probe-first; d-global-vs-mix переформулирован как «полная S4-LOD vs упростить»).

play_check:
  1. Recite — DONE: голос расшифрован в R1-R7, эхо-нумерован, владельцу на подтверждение парсинга.
  2. Investigate — DONE: 6-агентный веер (Steam-CPU web + кап/заполнение + швы + газ/геометрия + 2 скептика).
  3. Confidence — DONE: Steam-числа HIGH (датир. источники); абсолюты на неизмеренном single-core (ангар-проба меняет запас); 2 поправки скептиков подняты в headline (кап≠весь-worst-case, кап≠rollup).
  4. Close — DONE: этот RESULT; ответ по R1-R7 в формате владельца (таблицы, enterprise-аналогии); продукт §10; captures = вход S0-PLAN; решения в decisions_needed.

log: "2026-06-22 — research (g-9c41, s-research-014): R1-R7 (Steam-CPU/кап/швы/газ-геометрия). CPU=4-ядерный пол (≥4 ядра 92% Steam) → мультиядро ×4 гарантия; 40@50см=2-3× запас. Кап газа = worst-case→константа N_max=потолок CPU; breach-вент=сток. ×3-5 = room-rollup статичная дверь. 6 розеток уже в S0 + 4 GAP заложить (cap/tickrate/void-sink/res-пара) по водоразделу чексумма=публичный-контракт. Газ 50см глобально (убирает ловушку №2); геометрия 100см при целом-кратном. Дополнил work §10. → history/s-research-014.md"

next: awaiting_decision — d-cellsize-default(50см глобально)/d-geometry-resolution/d-gas-cap + прежний батч. Все входы = captures для S0-PLAN (4 GAP-розетки + 50см-глобально + геометрия-кратна + кап-as-граница). S0 не ждёт (открывается PLAN'ом, который ингестит эти доки). Гейт абсолютов = ангар-проба (scalar+Burst, 1 ядро+все ядра, тяжёлый солвер). Ратификация в локед-спек / 4 GAP в done_when S0 = работа S0-PLAN, не research.
```

END_OF_FILE: live/indie-game-development/history/s-research-014.md
