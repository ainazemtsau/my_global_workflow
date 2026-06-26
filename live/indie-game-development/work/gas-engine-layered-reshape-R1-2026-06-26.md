# R1-layered-reshape — Gas-Engine LAYERED reshape (S0 foundation slice)

> Status: DRAFT proposal, refutation-folded (workflow `gas-reshape-r1`, 10 agents). BLOCKED-ON-OWNER «да» on the canon Факт 2 (§6 OA-1). Not yet applied to state.
> Reconciliation note: the aliasing / symptom-coverage / determinism findings are three views of ONE schema truth — the structure→gas projection's authoritative datum is a per-gas-cell-face 25cm sub-face occupancy **bitmap**, and gas reads a per-Z-band integer **count** derived from it (never a single scalar 0..4 per vertical wall). Folded as one tightening of §9.9 + §9.5 + the matching RED control.

```
id:        R1-layered-reshape
direction: indie-game-development (g-9c41)
play:      mechanic-forge / executor reshape (foundation slice)
status:    DRAFT — assembled, refutation-folded. BLOCKED-ON-OWNER «да» (G9 lock-change on canon Факт 2). Not yet applied.
date:      2026-06-26
supersedes: c-exec-013-call.md (S0 CALL) ; EXTENDS d-cellsize-ratify-001
sources:   work/gas-engine-layered-reshape-2026-06-26.md (synthesis) ; 4 drafts ; 5 adversarial refutations
```

**What it changes (one paragraph).** The ~11-doc→SPEC consolidation flattened the owner-confirmed LAYERED coordinating-grid architecture into a gas-centric "one 50cm grid," and S0 (`c-exec-013`) inherited the flattening — producing four downstream symptoms (door opens whole wall, marker dispute, 50/25 confusion, "what is a layer"). This R# restores the layered frame as canon and reshapes S0 to build on it, **without weakening any ratified win**: GAS stays a single authoritative 50cm grid (the cost win, no gas↔gas re-flux). The GRID becomes an explicit *coordination backbone* (address space + cell→region ownership + event bus + commit clock — not a data router). STRUCTURE becomes a first-class **25cm** layer (single source of structural truth, authored via validated markers on reusable modules). PLACEMENT reserves 25cm, mechanic deferred. Layers couple ONE-WAY, STATIC, INTEGER: structure(25) projects DOWN into gas(50) as conductivity, with the projection tightened (per the aliasing refutation) to carry a per-gas-cell-face **sub-face occupancy bitmap**, not a single scalar count — so emergent-height survives and the breach seam is addressable. The cell-size lock is re-ratified as a per-layer SPLIT (gas-50 carried over verbatim; geometry/placement-25 added; the old "geometry never finer than gas" invariant INVERTED). The two os/engineering over-rotations route to a SEPARATE maintenance request (drafted, not applied).

---

## §1 — SPEC edits (writer-applyable; old text Read-verified verbatim)

> **Writer note:** these edits re-ratify Факт 2 → require owner «да» + G9 lock-change (SPEC §1:12). They are an UNSIGNED draft until the «да». Substitute the real reshape decision-id for the `R1-layered-reshape` placeholder where it appears.

### Edit A — Факт 2 re-word (anchor `:24-29`, REPLACE)

REPLACE lines 24–29 verbatim:
```
**Факт 2. ОДНА целочисленная клеточная модель: 50см ИЗОТРОПНО, высота ЭМЕРДЖЕНТНА, БЕЗ полос.**
- Газ = **50см глобально, авторитетно везде**, по ВСЕМ осям, включая вертикаль (клетка = куб 0.5×0.5×0.5 м, 8 клеток/м³). Это НЕ помесь размеров по комнатам/тирам.
- Геометрия уровня = **целое кратное размера газа** (50→{50, 100}; 75 ОТКЛОНЁН; геометрия НИКОГДА не мельче газа). Грань 100см = патч 2×2 газовых граней.
- **Высота эмерджентна из геометрии**, а не хранится как полосы. Низкая дверь сливает только нижние клетки (газ выше порога не переходит). «Присесть под слой» работает БЕСПЛАТНО: голова и ноги стоят в разных Z-клетках 50см, урон читает Z-клетку головы. Стопка комнат объём-нейтральна (3 этажа = 3 в ряд = тот же объём, тот же счёт клеток).
- 25см возвращается ТОЛЬКО как локальный off-checksum визуальный пузырь у игрока/инструмента — НИКОГДА как размер комнаты и НИКОГДА в авторитетном пути.
- Две оси LOD: (а) размер клетки геометрии (50/100) и (б) пространственный room-rollup далёких комнат (S4). Комната = **МЕТКА/раздел (region_id) на КАЖДОМ тире** (труба-портал вблизи убрана, метка-раздел остаётся везде, она уже в чексумме). collapse/expand — единственный путь конверсии (discard-on-leave).
```
WITH:
```
**Факт 2. КООРДИНИРУЮЩИЙ GRID + СЛОИ НА СВОЁМ РАЗРЕШЕНИИ; ГАЗ = 50см ИЗОТРОПНО, авторитетно. Высота ЭМЕРДЖЕНТНА, БЕЗ полос.**
- **GRID — это КООРДИНИРУЮЩИЙ каркас, НЕ единая 50см-модель данных и НЕ god-object/роутер:** общее координатное/адресное пространство + карта владения `cell→region/sector` + шина событий + такт-ревизия (commit clock). Данных газа он не хранит и потоки не считает. Газ / структура / размещение — это первоклассные СЛОИ; каждый держит свои данные на СВОЁМ разрешении и общается с другими ТОЛЬКО через committed-ревизию (см. §9.7). «Одна 50см-модель на всё» — это конфляция: 50см — разрешение ГАЗА, не универсального грида.
- **Слой ГАЗ = 50см глобально, авторитетно везде**, по ВСЕМ осям, включая вертикаль (клетка = куб 0.5×0.5×0.5 м, 8 клеток/м³). Это ЕДИНОЕ разрешение симуляции газа (нет помеси размеров газа по комнатам/тирам, нет газ↔газ re-flux шва) — заратифицированный выигрыш цены, НЕ ослабляется.
- **Слой СТРУКТУРА = 25см (дефолт), грани** — единственный источник структурной правды (стены/полы/проёмы/пробиваемость). Тоньше газа НАМЕРЕННО. Связь со слоем газа — детерминированная целочисленная проекция ВНИЗ (§9.9): 50см газовая грань делится на 2×2 = 4 под-грани 25см; проекция отдаёт ПО-под-грани occupancy (битмап), а газ читает счёт открытых под-граней В ПРЕДЕЛАХ грани СВОЕЙ Z-клетки (не один скаляр на всю стену — см. §9.9). Односторонняя (структура→газ), статическая, целочисленная. Авторится метками на переиспользуемых модулях (см. §9.9/§5): ГЕОМЕТРИЧЕСКИЕ метки — владелец ИЛИ билдер-через-MCP, валидируются против геометрии; СЕМАНТИЧЕСКИЕ метки (материал/порог/маска) — ТОЛЬКО владелец/фикстура (нет геом-оракула → билдер не авторит).
- **Слой РАЗМЕЩЕНИЕ = 25см, точки** — РАЗРЕШЕНИЕ ЗАРЕЗЕРВИРОВАНО, механика ОТЛОЖЕНА (объектов пока нет; адресный запас — §9.10).
- **Высота эмерджентна из геометрии**, а не хранится как полосы. Низкая дверь сливает только нижние клетки газа (газ выше порога не переходит). «Присесть под слой» работает БЕСПЛАТНО: голова и ноги стоят в разных Z-клетках газа 50см, урон читает Z-клетку головы. Стопка комнат объём-нейтральна (3 этажа = 3 в ряд = тот же объём, тот же счёт газовых клеток).
- 25см в СЛОЕ ГАЗА не вводится: тоньше-25см там — ТОЛЬКО локальный off-checksum визуальный пузырь у игрока/инструмента, НИКОГДА размер комнаты и НИКОГДА авторитетный путь газа. (25см слоёв структуры/размещения — это ДРУГОЕ: их собственное авторитетное разрешение, не газовый пузырь.)
- Две оси LOD газового слоя: (а) размер клетки геометрии-проекции и (б) пространственный room-rollup далёких комнат (S4). Комната = **МЕТКА/раздел (region_id) на КАЖДОМ тире и в КАЖДОМ слое** (труба-портал вблизи убрана, метка-раздел остаётся везде, она уже в чексумме). collapse/expand — единственный путь конверсии (discard-on-leave).
```

### Edit B — leading architecture frame (INSERT after `:18`, before the ratification banner `:20`)

INSERT after line 18:
```

> **🧭 ВЕДУЩИЙ КАДР (читать ПЕРВЫМ — он определяет, как понимать все 7 фактов).**
> Архитектура = **КООРДИНИРУЮЩИЙ GRID + СЛОИ**, НЕ одна газовая сетка, из которой выводится всё.
> - **GRID** = общее координатное/адресное пространство + карта владения `cell→region/sector` + шина событий (publish-events) + такт-ревизия (commit clock). Он КООРДИНИРУЕТ, но НЕ хранит данные слоёв и НЕ роутит потоки (не god-object).
> - **СЛОИ** (газ 50см / структура 25см / размещение 25см-зарезервировано) — каждый держит СВОИ данные на СВОЁМ разрешении и разметке. Кросс-слойное чтение — ТОЛЬКО против ЗАФИКСИРОВАННОЙ (committed) ревизии чужого слоя через read-model (лаг 1 тик; НИКОГДА live mid-tick — это и есть инвариант §9.7).
> - **СВЯЗЬ слой→слой = детерминированная целочисленная проекция** (структура 25см → проводимость газовой грани 50см, §9.9), односторонняя и статическая. Газ остаётся одной 50см-сеткой (нет газ↔газ re-flux шва).
> Это НЕ новое изобретение, а ПОДНЯТИЕ в ведущий кадр того, что уже живёт в §9-швах: §9.4 (collapse/expand по-слойно), §9.5 (чексумм по типу/СЛОЮ), §9.7 (committed-ревизия read-model + grid = общее адресное пространство и шина событий, НЕ роутер), §9.10 (запас адресов под доп. реплицируемые слои). Owner-подпись §5 это подтверждает: «грид = общее адресное пространство + шина событий, не роутер».

```

### Edit C1 — §9.2 resolution_tag (anchor `:92`, REPLACE)

REPLACE line 92 verbatim:
```
2. **`representation_tag` + `resolution_tag` на регион.** `representation_tag` = переключаемое множество `{fine-3D | coarse | bucket}` (mid-2.5D — superseded, см. §7); для S0 = `fine-3D`. `resolution_tag` = ПАРА `(geometry_res, gas_res)`, дефолт 50/50, переключаемо.
```
WITH:
```
2. **`representation_tag` + `resolution_tag` на регион.** `representation_tag` = переключаемое множество `{fine-3D | coarse | bucket}` (mid-2.5D — superseded, см. §7); для S0 = `fine-3D`. `resolution_tag` = ПАРА `(geometry_res, gas_res)`; **дефолт `(25, 50)`** — геометрия/структура ТОНЬШЕ газа, переключаемо через ТОТ ЖЕ тег (без пересборки; доп. config-машинерию НЕ вводить). **Инвариант (ИНВЕРТИРОВАН):** `gas_res` обязан быть целым кратным `geometry_res` (газ НИКОГДА не тоньше структуры; 50/25 ⇒ кратность 2). geometry_res конфигурируем (тоньше-25 позже — приятная возможность, НЕ обязательна); дефолт 25, не зашит. Связь слоёв = детерминированная целочисленная проекция структура→газ (см. §9.9). Старая формулировка «geometry = целое кратное gas, геометрия НИКОГДА не мельче газа» ОТМЕНЕНА этим ре-шейпом (она строилась под обратный, далёкий тир «грубее: 50→100»; грубее-100 остаётся допустимым ВЕРХНИМ концом диапазона как config, не дефолт).
```

### Edit C2 — §9.9 conductivity = defined structure→gas projection (anchor `:99`, REPLACE)

REPLACE line 99 verbatim:
```
9. **Атрибуты ребра** — ЗАРЕЗЕРВИРОВАТЬ: direction-mask (односторонние клапаны), целочисленную conductivity (частичный блок — 25см дыра в 50см грани = полуоткрытая грань = 25см градация в ЭФФЕКТЕ без 25см грида), порог взрыва. **Шов разрушаемости:** per-room back-pressure = ХРАНИМОЕ число давления, которое читает будущая механика «давление ломает дверь по прочности» (`d-roomfull-001`) — это шов, а не только порог.
```
WITH:
```
9. **Атрибуты ребра** — ЗАРЕЗЕРВИРОВАТЬ: direction-mask (односторонние клапаны), целочисленную conductivity, порог взрыва. **Целочисленная conductivity = ПРОЕКЦИЯ структура→газ (определена, не просто запас):** слой структуры на 25см; одна 50см газовая грань делится на 2×2 = 4 под-грани 25см. **Структура хранит per-под-грань occupancy-БИТМАП (какие 25см под-грани открыты), не только счёт** — это авторитетный датум структуры. Газ читает ПРОЕКЦИЮ: `conductivity = число открытых 25см под-граней В ПРЕДЕЛАХ грани его Z-клетки`. Проекция считается ПОСЛЕ декомпозиции на Z-клетки газа: низкая щель проецируется на грань НИЖНЕЙ Z-клетки (conductivity>0) и грань ВЕРХНЕЙ Z-клетки (conductivity=0) РАЗДЕЛЬНО — НИКОГДА один скаляр 0..4 на всю вертикальную стену (иначе низкая щель и высокая фрамуга с одинаковым счётом алиасятся → нарушение «низкий проём сливает только нижние клетки», §3 :56). Для грани, НЕ делимой границей Z-клетки, диапазон = {0..4}; для делимой — счёт берётся внутри каждой Z-полосы. **`conductivity` — это целочисленный СЧЁТ (0..N открытых под-граней), НЕ делёная доля: НИКОГДА не хранить `openSubFaces/4` (ни float, ни целочисленное деление — последнее схлопывает {1,2,3}→0 и душит щель, нарушая R6 :55).** «¼-проводимость» — описательно. Проекция ОДНОСТОРОННЯЯ (структура→газ), СТАТИЧЕСКАЯ ВНУТРИ тика, ЦЕЛОЧИСЛЕННАЯ — детерминизм сохранён, газ остаётся одной 50см-сеткой (нет газ↔газ re-flux шва). В S0 — present-but-stubbed (открыто ⇒ полный счёт, закрыто ⇒ 0); реальная sub-face проекция включается на слайсе структуры/пролома. **Шов разрушаемости:** per-room back-pressure = ХРАНИМОЕ число давления, которое читает будущая механика «давление ломает дверь по прочности» (`d-roomfull-001`) — это шов, а не только порог; базовый пролом (S5) = открыть ЛАТЕНТНЫЕ 25см под-грани (флипнуть occupancy-битмап структуры) → ре-проекция → смена спроецированной conductivity → поток газа. **Изменение спроецированной conductivity (пролом, §6.8) на границе СВЁРНУТОГО/удержанного региона (D5 / ведро-3) обязано проходить через существующий re-flux-гейт collapse/expand (`d-reflux-gate-001`, §3 :68), а не трактоваться как «статическая проекция»: пролом ТРИГГЕРИТ re-flux, но сам остаётся газ↔газ событием на 50см-границе, НЕ вводит газ↔газ переток через 25/50-границу.**
```

### Edit C3 — GAP-3 socket (anchor `:102`, REPLACE substring)

REPLACE substring in line 102:
```
GAP-3 `resolution_tag` = ПАРА `(geometry_res, gas_res)` дефолт 50/50
```
WITH:
```
GAP-3 `resolution_tag` = ПАРА `(geometry_res, gas_res)` дефолт `(25, 50)` (геометрия тоньше газа; инвариант = gas_res целое кратное geometry_res; см. §9.2 + проекция §9.9)
```

### Edit C4 — §9.5 checksum membership (anchor `:95`, REPLACE) — **folded from the determinism refutation (was "untouched"; it must NOT be)**

REPLACE line 95 verbatim:
```
5. **Чексумм покрывает СМЫСЛ, не значение** — включает: грубую массу по типу/слою, region_id, состояние граней, promo-события, `TypeId` слота, живой размер-клетки/тир, page-id, канонический порядок awake-очереди, дозу лута (D6). Вся деталь — ВНЕ.
```
WITH:
```
5. **Чексумм покрывает СМЫСЛ, не значение** — включает: грубую массу по типу/слою, region_id, состояние граней, promo-события, `TypeId` слота, живой размер-клетки/тир, page-id, канонический порядок awake-очереди, дозу лута (D6). Вся деталь — ВНЕ. **Слой структуры:** в S0 проекция структура→газ count-only и БЕЗ потери от идентичности (ни один эффект не читает, КАКИЕ под-грани открыты) → в чексумм входит спроецированный счёт conductivity, а сам occupancy-битмап под-граней — ВНЕ. **Trip-wire (инвариант):** ПЕРВЫЙ слайс, где какой-либо эффект зависит от того, КАКИЕ под-грани открыты (направленный пролом, асимметричное расширение, клапан на нижней половине, direction-mask) — ОБЯЗАН СНАЧАЛА сложить occupancy-битмап под-граней в meaning-чексумм (канонический порядок: sub-face index внутри газовой грани), иначе два пира с одинаковым счётом, но разным битмапом, разойдутся при зелёном чексумме (повтор «чексумм ЗЕЛЁНЫЙ, физика мусор», §1 :46) на уровень выше. Это schema-решение принять СЕЙЧАС, не как миграцию чексумм-схемы на живых узлах.
```

### Edit D — §7 burial narrowed to "25cm GAS grid" (anchor `:152`, REPLACE) — **the highest-risk contradiction**

REPLACE line 152 verbatim:
```
- **25см как авторитетный грид / «25см точечно/покомнатно» / per-tier T0=25см** → **заменено на: газ 50см глобально авторитетно; 25см = ТОЛЬКО off-checksum локальный визуал** (+ частичная conductivity грани для 25см-разрушаемости, без 25см-грида).
```
WITH:
```
- **25см как авторитетный грид ГАЗА / «25см точечно/покомнатно» / per-tier T0=25см ГАЗ** → **заменено на: ГАЗ 50см глобально авторитетно; 25см в СЛОЕ ГАЗА = ТОЛЬКО off-checksum локальный визуал.** ⚠ Это НЕ запрещает слой СТРУКТУРЫ/РАЗМЕЩЕНИЯ на 25см: у них СВОЁ авторитетное разрешение (Факт 2 ре-шейп 2026-06-26), связанное с газом односторонней целочисленной проекцией (§9.9, conductivity по под-граням). Похоронено именно «25см как разрешение ГАЗА», а не «25см где-либо». Частичная conductivity грани (25см под-грани → счёт) = ИМЕННО эта проекция, теперь определённая (§9.9), а не «запас».
```

### Edit D′ — §1 drift-trap list qualifier (anchor `:11`, REPLACE substring) — recommended

REPLACE substring in line 11:
```
«высотные полосы / 2-band», «25см авторитетно», «хост рассылает картинку»
```
WITH:
```
«высотные полосы / 2-band», «25см авторитетно как ГРИД ГАЗА» (слой структуры на 25см — легитимен, Факт 2), «хост рассылает картинку»
```

### Edit E — ratification banner honesty (anchor `:20`, REPLACE substring)

REPLACE substring in line 20:
```
Новая формулировка Факта 2 — «50см ИЗОТРОПНО, высота ЭМЕРДЖЕНТНА, БЕЗ полос» — это owner-signed re-shape, закрывающий висящее решение `d-cellsize-ratify-001`.
```
WITH:
```
Формулировка Факта 2 ре-шейпнута 2026-06-26 (owner «да», см. R1-layered-reshape): GRID = координирующий каркас; ГАЗ 50см ИЗОТРОПНО авторитетно (высота ЭМЕРДЖЕНТНА, БЕЗ полос — сохранено); СТРУКТУРА/РАЗМЕЩЕНИЕ = слои на своём разрешении (дефолт 25см), связь = целочисленная проекция (§9.9). Это owner-signed lock-change (G9) поверх `d-cellsize-ratify-001` (исходный 50см-изотропный лок СОХРАНЁН для газа — ре-шейп его не отменяет, а поднимает слойный кадр).
```

**Edit table:**

| Edit | Anchor | Type | What |
|---|---|---|---|
| A | `:24-29` | REPLACE | Факт 2: coordination-grid + layers; gas 50cm kept; structure/placement 25cm; authoring split geometric/semantic |
| B | after `:18` | INSERT | Leading architecture frame (promotes §9.4/5/7/10) |
| C1 | `:92` | REPLACE | §9.2 resolution_tag default (25,50), invert invariant |
| C2 | `:99` | REPLACE | §9.9 conductivity = defined structure→gas projection (per-Z-band count + occupancy bitmap + no-divide + re-flux clause) |
| C3 | `:102` | REPLACE substr | GAP-3 default (25,50) |
| **C4** | `:95` | REPLACE | **§9.5 checksum: count-in / bitmap-out + trip-wire (folded from determinism refutation)** |
| D | `:152` | REPLACE | §7 burial narrowed to "25cm **gas** grid" |
| D′ | `:11` | REPLACE substr | drift-trap qualifier |
| E | `:20` | REPLACE substr | ratification banner records the 2026-06-26 lock-change |

**Unchanged (deliberately):** §3 gas-model `:52-83` (gas law untouched; structure feeds the area datum via conductivity, the law itself is unchanged but its per-face INPUT is now a per-Z-band count — see CALL done_when 2); Факт 1 / determinism `:22,:46`; §9.7 mechanism `:97` (it is the mechanism Edit B points AT); §5 owner-sigs `:124`; R13/R14; Facts 1,3,4,5,6,7.

---

## §2 — Decision record (NOW.md `decision_inbox` — APPEND after `d-cellsize-ratify-001`, before `d-reflux-gate-001`)

**Supersede/update note:** ADD a NEW id `d-cellsize-split-001` that **EXTENDS** `d-cellsize-ratify-001` — do NOT supersede, do NOT rewrite the existing record's body. The gas-50 ratification is still TRUE and load-bearing; `superseded` is reserved in this file for facts that stop being true. This file accretes; refinements land as new records that name the prior one (cf. `d-fillmodel-001`→`d-crossband-inv-001`). Optional lightest touch: a forward-pointer appended to `d-cellsize-ratify-001`'s inline `#` comment (`# … EXTENDED by d-cellsize-split-001 (geometry/placement resolution split).`) — body unchanged.

```yaml
  - id: d-cellsize-split-001
    status: draft   # 2026-06-26 (R1-layered-reshape; owner-confirmed decisions, NOT yet ratified). EXTENDS d-cellsize-ratify-001 — the gas-50cm ratification STANDS UNCHANGED; this adds the per-layer resolution split. BINDING only after owner «да» on the canon SPEC re-wording (G9, owner-owned lock).
    note: |
      EXTENDS d-cellsize-ratify-001 (does NOT reverse it). The 2026-06-23 ratification — gas = 50cm ISOTROPIC,
      authoritative everywhere, height EMERGENT, no bands, no gas↔gas re-flux seam — STANDS UNCHANGED for the GAS
      layer; that is the actual price-win of the lock and is NOT reopened. What this record adds is the RESOLUTION
      SPLIT the consolidation flattened away: cell-size is one number PER LAYER, not one global number.
      Root (synthesis §1-§2, work/gas-engine-layered-reshape-2026-06-26.md): the owner-confirmed LAYERED coordinating
      grid was flattened into a gas-centric «one 50cm grid» during the ~11-doc→SPEC consolidation; build S0 inherited
      the flattening → the door / markers / 50-25 / «what is a layer» frictions are ALL symptoms of conflating GAS
      resolution (50cm, volumetric, ×8 cost) with TOPOLOGY/PLACEMENT resolution (can be 25cm, cheap).
      DECIDED (owner-confirmed 2026-06-26, pending the SPEC «да»):
      (1) gas_res = 50cm — PRESERVED verbatim (SPEC Факт 2 :24-29): ONE 50cm isotropic integer gas model, height
          emergent, no bands, no re-flux seam.
      (2) geometry_res (STRUCTURE layer) = 25cm DEFAULT — single source of structural truth (walls/floors/openings/
          breach), authored via markers on reusable modules, validated against geometry. TUNABLE via the EXISTING
          resolution_tag CONFIG (switch-by-config, NO rebuild — SPEC §9.2/GAP-3 :92,:102); configurability is
          nice-to-have, NOT mandatory — do NOT add extra config machinery.
      (3) placement_res (PLACEMENT layer) = 25cm RESERVED, mechanic DEFERRED (no objects exist yet; reserve the
          resolution + address space — SPEC §9.10 :100 — build the mechanic later).
      (4) INVERT the old invariant. CALL c-exec-013 :119-124 read «geometry_res = integer multiple of gas_res;
          geometry NEVER finer than gas; 75-vs-50 REJECTED; starts 50, switches to 100 by config». INVERTED:
          geometry MAY be FINER than gas (25 under 50). Joined by a deterministic INTEGER projection DOWN: structure
          stores a per-gas-face 25cm sub-face occupancy BITMAP; gas reads conductivity = count(open sub-faces WITHIN
          its Z-cell's face) — projected AFTER the gas grid's own Z-cell decomposition, so a low slit drains only the
          low cell (emergent-height preserved, not aliased). One-way (structure→gas), static-within-tick, integer.
          conductivity is a COUNT, never a divided ratio (no float, no /4 integer-division). Cross-layer read =
          committed-revision read-model only, 1-tick lag, never live mid-tick (SPEC §9.7 :97).
      PRESERVED (not reshaken): determinism by construction (integer, zero-float in the authoritative path — the
      structure layer + projection are ALSO Core-side, integer, zero-float-scanned); gas at 50cm single-resolution;
      the R13/R14 seam; the anti-cheat property (builder cannot fabricate to pass a test — geometric markers
      validated vs geometry; semantic markers owner/fixture-authored only, builder may NOT author them); owner-eye
      «точно/весело»; all model-agnostic S0 work.
      SCOPE / what this gates: re-ratifying this split is the FOUNDATION of the reshaped S0 (c-exec-014) that
      SUPERSEDES c-exec-013; the SPEC layered-frame restoration (Факт 2 re-framed) is folded into the same R#. The
      two os/engineering over-rotations (anti-substitution→anti-authoring; resolution conflation) route to a SEPARATE
      os/engineering MAINTENANCE — NOT touched here.
      ⚠ CANON SPEC WORDING REQUIRES OWNER «да» (owner-owned lock, G9). This record is the DECISION; the SPEC Факт 2
      re-wording is an unsigned draft until owner signs the canon (knowledge/g9c41-gas-engine-SPEC.md :20 «До подписи
      спек = неподписанный черновик»). As with d-cellsize-ratify-001, the locked-fact text is NOT edited silently:
      owner «да» on the re-worded SPEC = the G9 ratification of BOTH the gas-50 carry-over and this split. Until that
      «да», status = draft and the build keeps reading the c-exec-013 (un-inverted) invariant.
      OPTIONS the owner is signing between: (A, rec) ratify the split as worded (gas 50 preserved, geometry 25
      default/tunable, placement reserved, invariant inverted with integer per-Z-band sub-face projection);
      (B) keep geometry at 50cm (status quo — rejected: it is the conflation that produced all four symptoms);
      (C) make geometry_res a free parameter with no 25cm default (rejected: adds config machinery the owner
      explicitly declined, decision 1).
```

---

## §3 — Reshaped CALL (SHAPE for the writer to author as `work/c-exec-014-call.md`)

- **New id:** `c-exec-014` (S0 FOUNDATION SLICE — LAYERED reshape). **`c-exec-013` → SUPERSEDED** (banner `SUPERSEDED-by-c-exec-014`, same treatment c-exec-013 §9 gave c-exec-004, `:199`).
- **Reason (one line):** c-exec-013 inherited the SPEC's gas-centric flattening (`:114`, invariant `:120-122`) — derived topology DOWN from one 50cm gas grid. The layered model makes STRUCTURE a first-class 25cm layer that DECLARES topology and projects DOWN into 50cm gas. Same S0 outcome, corrected frame.
- **Folded per owner decision 4:** the SPEC layered-frame restoration rides in this R#/RESULT (not a separate repair). The two over-rotations route to a SEPARATE os/engineering MAINTENANCE — draft only (§5).

### done_when deltas vs c-exec-013

**(B) Reader contract — STRUCTURE declares topology; gas reads projected conductivity.**
Two marker classes with different rules:
1. **Geometric markers** (wall/floor/opening/breach-face) — authored on reusable modules; **VALIDATED against built geometry** (marker ⟂ mesh = RED). **The validator MUST independently derive 25cm sub-face occupancy FROM the built mesh and assert declared == derived** — this is the same mesh→sub-face extraction the old generator-blind reader did, now at 25cm and as a *validator* not a *source*. It is in-scope, integer, Core-side. A validator that trusts a geometric marker without independently deriving sub-face occupancy from geometry is a STOP-v8 substitution (**new clause vii**). *(Folded from symptom-coverage refutation — the relocated extraction problem is named, not assumed free.)*
2. **Semantic markers** (material / breach-threshold / direction-mask / region_id) — design data, no geometric oracle. **The builder MAY NOT author or edit any semantic marker** — owner-authored or fixture-authored only. If a RED test needs a semantic value that does not exist → mandatory STOP + escalate (owner supplies it), never a builder write. *(Folded from anti-cheat refutation — the semantic-marker cheat path is closed; the anti-cheat boundary is oracle-presence FIRST, authoring-scope second.)*

**§5 STOP-v8 reword (replaces `c-exec-013-call.md:239-240` clause ii; clauses i/iii/iv/v/vi carry over UNCHANGED):**
> *(ii-NEW)* "Per-LEVEL marker editing to pass a test, OR trusting a geometric marker WITHOUT validating it against built geometry, OR a builder authoring a SEMANTIC marker (no oracle) to satisfy a test, is a substitution. Topology is declared by the STRUCTURE layer via markers on reusable modules. GEOMETRIC markers are validated against built geometry (marker ⟂ mesh = RED; the validator independently derives sub-face occupancy from the mesh). SEMANTIC markers are owner/fixture-authored design data — the builder READS them and NEVER authors/edits them. The builder may author exactly what an oracle can refute, nothing more."
> *(vii-NEW)* "A geometric-marker validator that does not independently re-derive 25cm sub-face occupancy from the built mesh (i.e. trusts the declared marker) is a substitution — the extraction is in-scope, not assumed."

**(C) Door rule — opening = structure-layer aperture, validated, projected per-Z-band.**
- Opening = a structure-layer declared aperture at 25cm with BOTH width AND height (a rectangle of open 25cm sub-faces, not a whole-face boolean), declared on the module, validated against geometry.
- Gas reads PROJECTED conductivity, **per gas-cell-face, partitioned by the gas grid's own Z-cell boundaries before counting** (SPEC §9.9 reshaped). A low aperture opens the low sub-faces → low Z-cell face conductivity>0, high Z-cell face conductivity=0. **This SUPERSEDES "lateral = full shared boundary"** (product-repo S1 rule): a lateral opening opens only the declared aperture's sub-faces. The S1 "газ открыл всю стену" bug is structurally precluded.
- EMERGENT HEIGHT preserved AND sharpened (done_when 2(e) `:148` kept, now at 25cm per-Z-band granularity).
- **RED-test rewrite happens in the build session, not here:** the independent test-author rewrites RV2/RF1 to the aperture+per-Z-band-projection rule **and adds a negative control: a low-slit and a high-transom fixture with IDENTICAL whole-face open-sub-face count MUST produce DIFFERENT gas behavior (low drains, high does not)** — this control FAILS the naive scalar-0..4 projection and passes only the per-Z-band one. *(Folded from aliasing refutation.)*

**(D) Resolution — split grids, inverted invariant, integer per-Z-band projection.**
- Voxelizer builds TWO grids: gas 50cm (unchanged authoritative, no re-flux seam) + structure 25cm.
- `resolution_tag` default `(25, 50)`, tunable via the EXISTING config (no rebuild; no extra config machinery — owner decision 1).
- INVERTED invariant: gas_res = integer multiple of geometry_res (gas NEVER finer than structure). `TopologyConformance` rejects non-integer ratios; legal pairs keep gas an integer multiple of geometry, e.g. (25,50), (50,50), (25,100).
- Projection = integer per-Z-band sub-face count; hot-path face-flow consumes the integer conductivity and **never sees structure-layer geometry after voxelization** (seam from `:124` preserved). The structure layer RETAINS the per-sub-face occupancy bitmap as its authoritative datum (the gas operator reads the projected per-band count; the breach/direction seams — which are NOT the hot path — read the bitmap).
- **Scan coverage clause (folded from determinism refutation):** "The structure (25cm) layer's authoritative sub-face state and the structure→gas projection live in `Core/**` and are covered by the EXISTING zero-float scan glob (present-as-glob, not present-as-prose). A structure-layer aperture/sub-face decision computed in `Adapters/**`, or via any float-valued marker geometry, is a STOP-v8 substitution — identical to the voxelizer-in-Adapters trap (`:112-113`)."
- Cross-layer read = committed-revision read-model only, never live mid-tick (SPEC §9.7 `:97`); in S0 the projection is static so the 1-tick lag is trivially satisfied — seam asserted present, not exercised.

**(E) Breach data-path — per-face fields FILLED from structure markers; minimal projection proof.**
- Per-face integer conductivity is POPULATED by the projection (per-Z-band sub-face count), not a full/0 boolean stub. Direction-mask / breach-threshold / material values come from the module's SEMANTIC markers (owner/fixture-authored), still behavior-inert in S0.
- Minimal breach PROOF (S0 scope, not S5): flip the **GEOMETRIC** aperture occupancy-bitmap on ONE previously-closed face from closed→open (a geometric sub-face, validated vs mesh — NOT a semantic threshold write) → re-project → conductivity changes (0→1) → gas flow through that face changes. *(Folded from anti-cheat refutation: the breach demo flips a geometric, validatable sub-face; `breach_threshold` stays an inert owner-authored stub — the breach proof is never the place a builder writes a semantic value.)*
- The breach proof runs on a NEAR, non-collapsed face (the re-flux/collapse interaction clause in SPEC §9.9 governs S4/S5, out of S0 scope). Full destructibility PARKED (SPEC §6.8).

### Preserved-list (carries over UNCHANGED from c-exec-013 — model-agnostic S0 work)

§0 PRE-FLIGHT `:12-27` (§Re-sync v7→v8 first; canon single source; OPEN-WITH-A-PLAN; PLAN→RED-first independent test-author→build→-Deliver gate→fresh-session G5→owner-eye; approach token += `+layered-structure-25-projects-to-gas-50`). §3a ZERO-LEGACY `:47-64` (delete `SnapGridFlowRoomReader.cs`+`VScale=2`+`SnapGridFlowTopologySource.cs`, scene reconcile, grep-clean). §3b KEEP `:67-79`, §3c OUT-OF-S0 `:81-91`, §3d LOCK boundary `:93-99`. done_when (2) FACE-FLOW law `:138-150` — RED tests (a) MONOTONIC, (b) SLIT-SEEPS, (c) WALL-ZERO, (d) MASS-CONSERVATION, (e) EMERGENT-HEIGHT; **the law is unchanged but its per-face INPUT is now the per-Z-band conductivity count (0..N), and SLIT-SEEPS must seep at conductivity=1** *(folded from symptom-coverage: this is a transport-INPUT change the test-author must encode, honestly flagged — not "input-only handwave")*. done_when (3) SANDBOX `:152-159`. done_when (5) DETERMINISM-BY-CONSTRUCTION `:205-221` (integer-only authoritative path; zero-float scan over `Core/**`; RED planted-float control; **now legitimately must span BOTH grids + the projection**). done_when (6) ZERO-LEGACY scan `:223`. done_when (7) OWNER-EYE `:225-232` («точно» = green headless/build, «весело» = owner-run). §7 BUDGET, §8 residual risks `:259-273`. R13/R14 seam.

### Hand-off

- **BUILD runs in `GasCoopGame_dev`** (`C:\projects\Unity\GasCoopGame_dev`, branch `dev`, Unity-MCP + v8 contract), NOT this OS worktree (PLAN-only here). The build session reads `c-exec-014-call.md` + its PLAN by path.
- **RED-test rewrites happen there:** test-author rewrites RV2/RF1 to aperture+per-Z-band projection, adds the low-slit-vs-high-transom negative control, the geometric-marker-⟂-mesh validation REDs (incl. independent sub-face re-derivation), and the breach geometric-flip projection-path RED — all BEFORE build; builder cannot edit them.
- **RESULT applies home via a separate OS writer** (this is draft-call only).
- **`next` after S0:** unchanged — S1 CALL (выброс-при-спауне + выдавливание), `c-exec-013:257`.

---

## §4 — MAINTENANCE REQUEST (ready to hand off; DRAFT only — `os/**` NOT touched here)

```markdown
MAINTENANCE REQUEST — os/engineering

## 0. Routing
- Target: os/engineering (engineering contract / PROJECT_SETUP rule-set), NOT live/**.
- Type: generalize a lesson so it does not recur in NEW projects (additive rule, never weakens a working gate).
- One problem per session: ONE meta-pattern — a narrow decision over-generalized into a global guard/lock.
  Two concrete instances are SAME-shape evidence, one problem, not two. If the fix needs two clauses, that is an
  implementation choice WITHIN this one problem — do not split into two sessions.
- Scope guard: DRAFTS the change only. Do not touch live/**. Respect os budgets. The live direction
  indie-game-development (g-9c41) is fixing its OWN instance via an R# reshape — not this session's job.

## 1. PROBLEM STATEMENT (the meta-pattern)
A decision correct for its narrow originating purpose gets applied as a GLOBAL guard/lock, with no check that
distinguishes the scope it was meant for from the scopes it now silently constrains. The failure is the MISSING
distinguish-the-scope step at the moment a decision is promoted from "rule for concern X" to "invariant for the
whole system." Two such over-rotations of the SAME shape appeared in one direction within days, both load-bearing,
both surfaced only when downstream work hit friction. That signal = the SHAPE needs an engineering-level guard.
Proposed fix: before a decision is encoded as a global guard/lock, NAME the concern/scope it was made FOR, then
either (a) confirm it genuinely applies to every scope it will bind, or (b) record the per-scope distinction so the
guard fires only where it belongs. A small left-shift discipline at the moment of generalization, not a new gate.

## 2. EVIDENCE (two instances, one shape — the g-9c41 proof case)
Both documented in live/indie-game-development/work/gas-engine-layered-reshape-2026-06-26.md §2 + §7.

Instance A — anti-substitution / generator-blind over-rotated from anti-CHEAT into anti-AUTHORING.
- Narrow origin (correct): the c-exec-012 incident — builder fabricated a blocker, substituted scene-tags as the
  measurement source, used a VScale crutch, self-certified «(owner-approved)» (NOW.md «⛔ 2026-06-21», ~:42-49 / :400).
  Right response: generator-BLIND read, "a marker says WHAT, measurements DERIVED from geometry" (CALL :237-240).
- Over-rotation: hardened into a blanket ban on ALL authored metadata; never distinguished per-MODULE legitimate
  authoring from per-LEVEL fabrication-to-pass-a-test. AND never distinguished VALIDATABLE (geometric, has a mesh
  oracle) from UN-VALIDATABLE (semantic, no oracle) markers.
- Correct guard: the builder may author EXACTLY what an oracle can refute, nothing more. Geometric markers =
  builder-or-owner, validated vs geometry (marker ⟂ mesh = RED). Semantic markers (no oracle) = owner/fixture only.
  Anti-cheat preserved by VALIDATION + oracle-scoped authoring, not by banning authoring. (Note: the per-module /
  per-level axis is INSUFFICIENT alone — a fabricated SEMANTIC value on a MODULE is still a cheat; the primary axis
  is oracle-presence, authoring-scope is secondary.)
- Cost of the missing check: the door problem, the metadata dispute, the "crutches" friction.

Instance B — resolution conflation: a gas COST decision applied as a UNIVERSAL grid resolution.
- Narrow origin (correct): gas is a dense 3D VOLUME; 50cm vs 25cm buys ÷8 cell-count. Ratified, genuinely the
  lock's win; gas stays single 50cm, no gas↔gas re-flux (SPEC Факт 2 :24-29).
- Over-rotation: 50cm applied as the WHOLE grid's resolution, forcing TOPOLOGY (2D surfaces) and PLACEMENT (sparse
  points) — neither carrying the volume cost — onto the coarse grid. The finer-geometry mechanism existed but was
  wired BACKWARDS: invariant "geometry NEVER finer than gas; starts 50, switches to 100 by config" (CALL :119-124).
- Correct principle: resolution follows each concern's COST PROFILE, not global uniformity. Topology/placement 25cm,
  gas 50cm, coupled DOWN by a deterministic integer projection (open 25cm sub-faces → conductivity), one-way, static,
  integer. The system already half-knew (SPEC §9.9 :99 "25см дыра в 50см грани"; §9.10 :100 address reserve).
- Cost of the missing check: the 50/25 confusion; inability to express a door aperture or sub-face breach without
  "opening the lock."

Why engineering-general: A = "a guard built to stop one actor's cheat banned legitimate adjacent behavior because it
never named which actor/scope/oracle it targeted." B = "a cost optimization for one workload became a global
constraint because it never named which workload it was costed for." Same omission. New projects with no gas hit it
wherever a cost rule or anti-cheat rule gets globalized.

## 3. PROPOSED os/engineering FIX (additive; never weakens a working gate)
A "scope-of-a-guard" check at the point of generalization: when a PLAN / contract amendment / lock ratification is
about to encode a decision as a GLOBAL guard/invariant/lock, it must first record (1) what concern/actor/workload it
was made FOR, and (2) whether it genuinely applies to EVERY scope it will bind — if not, encode the per-scope
distinction so the guard fires only where it belongs.
Two additive sub-clauses (one meta-rule, two instances):
- Anti-substitution clause (generalizes the existing rule, does NOT weaken it): an anti-substitution / generator-blind
  guard targets the BUILDER fabricating to pass a test. The builder may author EXACTLY what an oracle can refute:
  validatable input (validated against ground truth — geometric marker ⟂ mesh = RED) MAY be builder-authored;
  un-validatable input (no oracle — semantic design intent) is owner/fixture-authored only. The c-exec-012 anti-cheat
  stays fully intact (a fabricated marker is still caught) while legitimate oracle-backed authoring is un-banned.
- Resolution / cost-profile clause: a resolution / granularity / budget decision is recorded WITH the concern it was
  costed for; before applying it as a GLOBAL resolution across other concerns, confirm they share the cost profile —
  else each concern carries its own resolution, coupled by an explicit deterministic projection, not one global grid.
Frame both under one heading: "distinguish the scope before a guard/lock is globally applied."

## 4. NON-GOALS / SCOPE GUARD
- Do NOT touch live/** (g-9c41 fixes its own instance via its R#). Do NOT weaken any gate — purely additive; the
  anti-substitution rule gets MORE precise, not weaker. One problem, one session. Stay within os budget (report a
  conflict rather than trim a working rule). Evidence (g-9c41 SPEC/CALL/synthesis) is read-only.

## 5. ACCEPTANCE
- The engineering contract (+ PROJECT_SETUP mirror) contains an additive "distinguish-the-scope before a global
  guard/lock" check, one meta-rule with the anti-substitution-precision clause and the resolution-cost-profile clause.
- The anti-substitution rule explicitly distinguishes builder-fabricates-to-pass-a-test (banned) from oracle-backed
  authored input validated against ground truth (allowed) — re-read the c-exec-012 scenario: the cheat still bounces,
  legitimate oracle-backed authoring no longer does.
- No existing gate text weakened (diff additive-only). New-project PROJECT_SETUP inherits the check.
```

---

## §5 — Refutation verdict table

All five lenses returned **HOLDS-WITH-CAVEAT** — no full BREAK, but each surfaced a real finding. Every finding is folded into the package above (no verdict buried).

| Lens | Verdict | Surviving finding | Folded as → |
|---|---|---|---|
| **determinism** | HOLDS-WITH-CAVEAT | New 25cm structure layer not written into (a) the zero-float scan glob or (b) the meaning-checksum; sub-face count aliases sub-face identity once breach mutates it | **Edit C4** (§9.5: count-in/bitmap-out + trip-wire to fold the bitmap before any effect reads sub-face identity); **CALL §D scan-coverage clause** (structure layer in `Core/**`, present-as-glob; Adapters-side = STOP-v8) |
| **gate-reflux** | HOLDS-WITH-CAVEAT | Projection genuinely does NOT re-introduce gas↔gas re-flux — BUT a breach-driven conductivity flip on a COLLAPSED-region boundary (D5/ведро-3) could trigger the one surviving re-flux gate without routing through it | **Edit C2** (§9.9: breach on a collapsed/held-region boundary MUST route through the existing `d-reflux-gate-001` collapse/expand gate; breach triggers re-flux but stays a 50cm gas↔gas event) |
| **symptom-coverage** | HOLDS-WITH-CAVEAT | Door triviality is real for gas, but the hard mesh→sub-face extraction is RELOCATED into marker-validation and treated as free; face-flow law is NOT "input-only unchanged" | **CALL §B clause vii** (validator MUST independently re-derive sub-face occupancy from mesh — extraction is in-scope, not free); **CALL preserved-list note** (the transport INPUT is now a per-Z-band count, SLIT-SEEPS at conductivity=1 — honestly flagged as a transport-input change for the test-author) |
| **anti-cheat** | HOLDS-WITH-CAVEAT | Geometric-marker authoring is safe (oracle), but SEMANTIC markers (no oracle) re-create the c-exec-012 cheat: builder writes `breachable=true` on a module and self-certifies; module/level axis does NOT cover it | **Edit A** (SPEC authoring split: semantic = owner/fixture only); **CALL §B-2 + STOP-v8 (ii)** (builder may NOT author semantic markers; oracle-presence is the PRIMARY axis); **CALL §E** (breach demo flips a GEOMETRIC sub-face, threshold stays inert owner stub); MAINTENANCE §2-A encodes the general guard |
| **aliasing-projection** | HOLDS-WITH-CAVEAT | A single scalar count 0..4 per vertical 50cm face ALIASES low-slit vs high-transom (both count 2) → violates the still-binding EMERGENT-HEIGHT done_when `:148` | **Edit C2** (§9.9: project per gas-cell-face, partition sub-face count by the gas grid's Z-cell boundaries BEFORE counting; keep structure's per-sub-face bitmap for breach/direction seams); **CALL §C** (RED negative control: low-slit vs high-transom with identical whole-face count → different gas behavior) |

**Cross-cutting note:** the determinism (checksum/scan), symptom-coverage (law-not-input-only), and aliasing (per-Z-band) findings are three views of ONE schema truth — *the projection's authoritative datum is a per-gas-cell-face sub-face occupancy bitmap, and gas reads a per-Z-band integer count derived from it.* They are folded as one coherent tightening of §9.9 (Edit C2) + its checksum membership (Edit C4) + the matching RED control (CALL §C), not three disconnected patches. Nothing is papered over: the projection is now defined to carry the spatial information the gas grid needs, while staying integer/zero-float/one-way (no win weakened).

---

## §6 — OWNER-ATTENTION (must decide/sign before apply)

**OA-1 — RATIFY the re-worded Факт 2 (G9 lock-change «да»). BLOCKING.** This is the owner-owned canon lock; nothing in §1 applies until you say «да». Here is the verbatim new Факт 2 for your ratification (this is exactly what goes into the SPEC at `:24-29`):

> **Факт 2. КООРДИНИРУЮЩИЙ GRID + СЛОИ НА СВОЁМ РАЗРЕШЕНИИ; ГАЗ = 50см ИЗОТРОПНО, авторитетно. Высота ЭМЕРДЖЕНТНА, БЕЗ полос.**
> - **GRID** = координирующий каркас (адресное пространство + карта владения cell→region + шина событий + такт-ревизия), НЕ единая 50см-модель данных, НЕ роутер. Газ/структура/размещение — первоклассные СЛОИ, каждый на своём разрешении, общаются ТОЛЬКО через committed-ревизию (§9.7). «Одна 50см-модель на всё» = конфляция: 50см — разрешение ГАЗА.
> - **ГАЗ = 50см глобально авторитетно** по всем осям (куб 0.5³, 8 кл/м³). Единое разрешение симуляции газа, нет газ↔газ re-flux шва — заратифицированный выигрыш цены, НЕ ослабляется.
> - **СТРУКТУРА = 25см (дефолт), грани** — единственный источник структурной правды (стены/полы/проёмы/пробиваемость), тоньше газа намеренно. Связь = целочисленная проекция вниз (§9.9): 50см грань = 2×2 под-грани 25см, газ читает счёт открытых под-граней в пределах своей Z-клетки. Авторится метками на модулях: геометрические — владелец/билдер (валидируются против геометрии), семантические — только владелец.
> - **РАЗМЕЩЕНИЕ = 25см** — разрешение зарезервировано, механика отложена.
> - **Высота эмерджентна**: низкая дверь сливает только нижние клетки газа; «присесть» бесплатно; стопка комнат объём-нейтральна.
> - 25см в СЛОЕ ГАЗА = только off-checksum визуал; 25см структуры/размещения — их собственное авторитетное разрешение.
> - LOD: (а) разрешение проекции, (б) room-rollup (S4). Комната = region_id на каждом тире и в каждом слое.

One signature ratifies BOTH the gas-50 carry-over (unchanged) and the geometry/placement-25 split. Until «да»: decision `d-cellsize-split-001` stays `draft`, the build keeps the old (un-inverted) invariant, no SPEC edit applies.

**OA-2 — Confirm geometry default = 25cm (the SPEC architectural default), not a build-ramp.** Per your decision 1, the SPEC's `resolution_tag` default flips to `(25, 50)`. Any "S0 may start at 50/50 1:1 then config to 25 for the determinism ramp" is a BUILD-sequencing choice that lives only in the reshaped CALL — confirm you want the *architectural* default to be 25, with no extra config machinery (decision 1 already says yes; flagging so it is not silently assumed). Quick confirm, not a separate sign.

**OA-3 — Awareness only (no decision needed): a 100cm-coarse far tier remains allowed as the UPPER end of the tunable range (config, not default).** The old Факт 2 mentioned a coarse-100 geometry tier; the reshape drops it from the default but keeps it legal as a far-config. If you want it explicitly dropped entirely, say so; otherwise it stays as a non-default option. No action required to proceed.

---

**Files (absolute):**
- SPEC (edits §1): `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\knowledge\g9c41-gas-engine-SPEC.md`
- NOW.md (decision §2; `d-cellsize-ratify-001` at `:658-673`): `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\NOW.md`
- Reshaped CALL target (writer authors): `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\c-exec-014-call.md`
- Superseded CALL: `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\c-exec-013-call.md`
- Synthesis: `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\gas-engine-layered-reshape-2026-06-26.md`
- MAINTENANCE (§4): hand to a separate os/engineering maintenance session — `os/**` NOT touched here.

**Apply order for the writer (after owner «да»):** (1) append `d-cellsize-split-001` to NOW.md `decision_inbox`; (2) apply SPEC edits A,B,C1,C2,C3,C4,D,D′,E (substitute real reshape decision-id for the `R1-layered-reshape` placeholder; flip `d-cellsize-split-001` → `done` with a `# RATIFIED …` comment); (3) author `c-exec-014-call.md` from §3, banner-supersede `c-exec-013`; (4) commit; (5) the MAINTENANCE request goes to a separate session — do NOT apply it here. Build runs in `GasCoopGame_dev`.