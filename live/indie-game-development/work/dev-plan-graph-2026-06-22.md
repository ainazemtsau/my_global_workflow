# g-9c41 dev plan-graph + decision index (2026-06-22) — the SINGLE entry point

> **Purpose:** the one doc a fresh session reads first. It holds (1) the slice spine + dependency/parallel graph, (2) the
> per-slice ritual, (3) the per-mechanic depth-classification rule, (4) the decision INDEX (pointers — nothing lost), (5) the
> hard rules. Owner-approved methodology 2026-06-22 ("да"). Detail lives in the linked docs; this is the map.

## 0. Where we are (one paragraph)

g-9c41 (the engine) is re-shaped from "build the whole core → then promo" to a **spine of small, visible, deterministic
gas-GAMEPLAY slices** on a test sandbox. Architecture is LOCKED (input-lockstep; ONE integer cell model = grid+face-flow near /
room-graph-rollup far / room=LABEL everywhere; sparse dominant-gas; chemistry table; real-height-3D near; detail = LOCAL
non-authoritative refinement of a coarse-authoritative truth, hard consequences = coarse events; NO late-join; zero-legacy;
reusable-engine dropped). Each slice ends in something the owner SEES; marketing/devlog + lore run in parallel; the storefront
stays gated on visual identity. **Per-mechanic decisions are made AT each slice's PLAN, not all upfront.**

## 1. Slice spine + dependency / parallel graph (the "dev tree")

These are TASKS (rolling wave), NOT tree outcome-nodes. Order = effect × foundation-dependency; foundation-critical first. Exact
order is a best-draft (an adversarial DAG-verify may run as the first execution step if the owner wants).

```
S0 ФУНДАМЕНТ ─┬─> S1 выброс+выдавливание ─┬─> S3 высота/расслоение ──┐
(вокселизатор │                            │                          ├─> S6+ из бэклога
 +грань-поток │  S2 МУЛЬТИПЛЕЕР (lockstep) ─┘   S4 коарс-rollup+LOD ──┤   (по эффекту×ведру)
 +песочница   │  (binding: грубое бит-идентично                       │
 +ОЩУЩЕНИЕ)    │   loopback/1 машина)              S5 базовый пролом ───────┘
              │
              └─ ∥ ВИЗУАЛ (g-7e15) — старт ПОСЛЕ S0 (read-seam есть), на фейк-данных
              └─ ∥ ЛОР (canon track) — всегда параллельно
              └─ ∥ DEVLOG (g-e6f2/g-2f8c) — постит истории по мере видимых слайсов
```

| Slice | что | видимый результат | зависит от | параллель |
|---|---|---|---|---|
| **S0** Фундамент+ОЩУЩЕНИЕ | вокселизатор (генератор-слепой ридер → грид с гранями + region_id) + грань-поток (наполнение комнаты) + §9-швы + дебаг-гизмо + integer/zero-float scan + loopback hash | уровень→грид(грани), газ ползёт/копится; **твой глаз: весело ли** (1 игрок, малый уровень) | — (ведёт) | визуал/лор стартуют после неё |
| **S1** Выброс + выдавливание | спаун = выброс под давлением; игрок/объект раздвигает газ | бросил источник — хлынуло; прошёл — раздвинул | S0 | ∥ визуал |
| **S2** Мультиплеер (lockstep) | тот же грубый сим на 2 ПРОЦЕССАХ (loopback, ОДНА машина — 2 ПК НЕ нужны) даёт одинаковый хеш; integer cross-CPU = GIVEN (не доказываем); реальные 2 ПК = опциональный разовый прогон, НЕ гейт | два окна — одинаковый газ | S0 (S1 желательно) | — (несущая) |
| **S3** Высота/расслоение | реальная высота near; грубому — неск. верт. слоёв для маршрута по высоте | копится в яме, уходит через низкий проём | S0 | ∥ |
| **S4** Коарс-rollup + LOD без рывка | дальние комнаты грубо; шов no-pop; collapse/expand = «выброс на выходе»; граф-как-метка оживает | ходишь — газ не дёргается на переключении | S0, S2 | ∥ |
| **S5** Базовый пролом | пред-объявленный проём открывается → газ течёт (грань-флип) | пробил — пошло | S0 (S3 желательно) | ∥ |
| **S6+** | реакции (телеграф+бах=событие), импульс/раздвоение (ведро 1/3), ветер, температура, типы газа… | по слайсу | из бэклога §3 | ∥ |

**Скрытые зависимости (ловушки):** S2-детерминизм должен стоять рано (вся дешёвая модель на нём держится); S4 нужен S2 (no-pop = свойство сети); промо-машинерия событий нужна ДО любой ведро-2 механики (реакция/урон); ведро-3 механики — только после S4 + сознательное «эта комната считает деталь у всех».

## 2. Ритуал ОДНОГО слайса (= «как работаем»; existing contour + 3 добавки)

1. **PLAN (owner present):** обязательно **впитать-и-ПРИМЕНИТЬ все доки §4** (чек-лист, не «сослаться») + **классифицировать механику(и) слайса в ведро 1/2/3** (§3) → спроектировать + как остаётся детерминированным/чистым/расширяемым → показать ДО кода.
2. **RED-first независимый тест-автор** пишет падающие тесты из спеки (билдер не правит) + binding-проба где нужна.
3. **BUILD:** integer-детерминированно (zero-float в авторитетном пути), **ноль legacy/чисто**, максимально расширяемо (§9 швы, keep-open не заварен).
4. **GATE + adversarial G5** (свежая сессия-рефутация; для тяжёлых — adversarial-прогон).
5. **ВИДИМЫЙ РЕЗУЛЬТАТ** — твой глаз (дебаг-гизмо рано, визуал позже). Слайс не закрыт, пока не УВИДЕЛ. Для коопных слайсов — 2 инстанса, игрок B переживает последствие действий игрока A (SHARED vs LOCAL-only флаг).
6. **INTEGRATE + промоут** новое решение/факт в `knowledge/` → следующий слайс впитывает.

## 3. Per-mechanic depth — классификация в PLAN каждого слайса (НЕ сейчас)

**Дефолт = ВАРИАНТ A** (глубина комнатно-гранулярна; 3D-деталь = ощущение сверху → дёшево + сильный де-риск: деталь может быть
даже float/недетерминированной, re-flux падает до owner-eye). Для КАЖДОЙ выразительной механики в PLAN её слайса — ведро:
- **1 сглаживается** → бесплатное локальное ощущение (вихрь; раздвоение, что сливается в комнате) — вне checksum.
- **2 грубо-промоутируемо** → дешёвое общее СОБЫТИЕ из грубого состояния, у всех, в checksum (реакция-триггер+масса; вентиляция комната-в-комнату; урон-где-газ; высотная маршрутизация потока).
- **3 под-комнатное И общее** → дорогой случай (стойкое раздвоение, меняющее дверь выхода; точный продув-канал, решающий исход) → форсит «эта комната считает деталь у ВСЕХ пиров» или десинк. Брать сознательно, только в нужных комнатах.

Первый проход по примерам владельца (в detail-authority-cost-model §4): наполнение/где-газ=общее; реакция=событие+телеграф-ощущение; урон=событие; высота=событие(грубо)+ощущение(3D); прошёл→раздвоилось=ощущение если сливается / ведро-3 если стойко меняет дверь; продув=событие(вентиляция)/ведро-3(точный канал); выдавливание=ощущение внутри/событие через дверь. Вывод: **в основном A + 2–3 ведро-3 механики.**

## 4. DECISION INDEX (ничего не потеряно — каждый слайс PLAN это впитывает)

- **READ-FIRST: knowledge/g9c41-architecture-locked-slices.md + knowledge/g9c41-drift-guard.md** — залоченные факты + 5 ловушек пересказа (8 пузырей / 2 машины / грид-vs-граф / деталь-в-одну-сторону / float-гард); свериться ДО объяснения владельцу.
- **work/gas-model-architecture-decision-2026-06-21.md** — D1–D13 (input-lockstep, cell-size-LOD, near-3D, D5, sparse-dominant, chemistry-table, real-height, reusable-DROPPED, carve-CUT), R1–R20, §9 seams-to-reserve, §10 depth-properties P1–P10, §11 de-risk, §14 code-ground-truth.
- **(архив) work/archive/aplus-replan-under-locked-arch-v1.md** — re-plan под locked-arch (выводы перенесены: tree-diff #2/#9 → TREE #12; NO late-join / ZERO-legacy / слайсы). НЕ читать при PLAN: его §3 рамил детерминизм как 2-машинный гейт — ОТМЕНЕНО (drift-guard #2).
- **work/grid-vs-graph-resolution-2026-06-22.md** — детальный=грид+грань-поток (площадь/высота/не-сквозь-стену даром); грубый=граф-rollup; **room=LABEL везде, PIPE-наружу-вблизи**; portal=cut-set-аггрегат; collapse/expand+re-flux; keep/delete-ledger; §3.1+§3.6 doc-refinement (ADR-0010); вертикаль=buoyancy-bias-вблизи.
- **work/detail-authority-cost-model-2026-06-22.md** — НЕ 8 пузырей (~8× win); грубое=авторитет-везде, деталь=локальное-выводимое-выбрасываемое-вне-checksum; hard-consequences=coarse-events; wash-out-условие; A/B-fork (дефолт A, классифицируем per-slice); D5-ангар-оговорка; co-located-детерминизм; анти-чит-остаток; ре-классификация детали (binding-проба сменилась: грубое-бит-идентично, НЕ re-flux).
- **(архив) work/archive/aplus-wave-map-v1.md + aplus-breakdown-v1.md** — ДО-lockstep (superseded спайном слайсов). Живой кусок: §4.2 RISK-register R-* + §2 keep-open инварианты — свериться вручную при PLAN (явный заход в архив).

## 5. Hard rules (несущие, в каждый слайс)

- **Детерминизм по конструкции:** integer-only авторитетный путь + zero-float build-scan + loopback hash; single-owner-per-face + gather-then-apply; канонический порядок; seeded RNG. (Кросс-CPU гарантия = «ноль float», проверяется на одной машине; 2-я машина — дешёвый разовый прогон позже.)
- **checksum покрывает СМЫСЛ:** грубое + region_id + состояние граней + промо-события ВНУТРЬ; вся деталь — НАРУЖУ. Локальный tripwire: ближний пир каждый тик проверяет collapse(detail)==coarse-direct, в checksum кормит только согласованное.
- **NO late-join:** лобби/база → старт → рейд с теми, кто есть; в рейд по ходу не входят. → нет обязательства снапшота для первой игры.
- **ZERO legacy на финише:** закончили — в дереве чисто; откат только в git; тесты пересмотреть/переписать.
- **Расширяемость:** §9 швы как DATA с дня первого; ни один keep-open не заварен; ядро максимально расширяемо.
- **Netcode-нейтральность фундамента:** S0/S1 НЕ строят ни lockstep-провод, ни broadcast; сеть появляется в S2.
- **LOCK не вскрывать молча:** D1/D2 + ре-классификация детали = ADR-0010, owner-G9 (через закрытие 2026-06-22).

## 6. Parallelism (что параллельно)

Дев-хребет — основной. ∥: ВИЗУАЛ (g-7e15, после S0 read-seam, на фейк-данных), ЛОР (canon, всегда), DEVLOG/маркетинг
(g-e6f2/g-2f8c, постит по видимым слайсам — владелец брифует маркетинг-трек отдельной сессией). ВНУТРИ дева параллелим только
где граф §1 показал «нет зависимости»; качество выше параллели.

END_OF_FILE: live/indie-game-development/work/dev-plan-graph-2026-06-22.md
