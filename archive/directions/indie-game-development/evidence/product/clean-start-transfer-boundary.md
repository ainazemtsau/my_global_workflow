# Clean-start Transfer Boundary

## purpose

Этот документ фиксирует clean-start boundary текущей игры. Он определяет, что считается реальным transferable foundation для нового старта, что удерживается как `transfer-later`, что остаётся `reference-only`, что явно попадает в `do-not-carry`, и какой `Gas ↔ Grid` contract делает такой перенос честным.

Это boundary document, а не migration plan, implementation plan или полный legacy audit.

## Rules of transfer

- Переносится только тот foundation, без которого gas truth-model перестаёт быть честной и самодостаточной.
- `Gas runtime` и `legacy global Grid` фиксируются как peer transferable foundation и не рассматриваются здесь как независимые линии переноса.
- `Selective transfer` в рамках этого boundary означает разделение на `starting set / transfer-later / reference-only / do-not-carry`, а не урезание Grid substrate, на который реально опирается Gas.
- Активная runtime/code surface имеет приоритет над историческими ветвями, визуальными прототипами и narrative-доками, если они конфликтуют.
- `Gas.Topology` допускается как gas-facing projection / validation layer, но это не делает `room authority`, `room identity` или `room-anchor authoring` собственностью Gas.
- Если required shared spatial surfaces отсутствуют или неконсистентны, корректное поведение — fail-fast, а не hidden fallback, geometry rescan или имитация самодостаточности.
- `GridV2` не считается replacement-path по умолчанию и не может тихо подменить `legacy global Grid` внутри этого boundary.

## Named starting set

Для текущего clean start фиксируется следующий starting set:

`Gas.Config / Gas.Foundation / Gas.Topology / Gas.T1 / Gas.T2 + legacy global Grid substrate required for room topology, room authority, door state, room anchors and room-localization / room-bounds surfaces used by Gas.`

Это minimum peer foundation, который позволяет переносить gas truth-model без hidden fallback, geometry rescan или притворства, что Gas существует отдельно от Grid substrate.

Это boundary document, а не migration sequencing.

## Transferable assets outside starting set

Следующие assets считаются переносимыми, но не входят в текущий carry-now foundation set:

- `Gas.Interest` — transferable asset, current carry status: `transfer-later`
- `Gas.T3.Data` — transferable asset, current carry status: `transfer-later`

Они удерживаются как real transferable assets, но не входят в named starting set текущего boundary.

## Reference-only

Следующие группы удерживаются как `reference-only` и не считаются foundation нового clean start:

- `GasTestLab / lab scenes / debug visualization` — инженерная reference-surface и validation aid
- `benchmark / evidence export` — performance / evidence reference
- `operator UI / engineering control tooling` — later tooling surface, но не minimum foundation

## Do-not-carry

Следующие группы не должны определять новый старт и не входят в foundation:

- `legacy GasV2 / older gas branches`
- `historical visual prototypes`
- `outdated narrative docs when they conflict with active runtime/code`
- `unconfirmed legacy playable-loop assumptions`

При конфликте источником истины остаётся active runtime surface, а не исторический narrative, старая ветка или dev/lab scaffolding.

## GridV2 line

`GridV2` не является replacement-path для `legacy global Grid` в рамках этого boundary.

Для текущего boundary это означает:

- `GridV2` не входит в named starting set;
- `GridV2` не получает статус неявной замены `legacy Grid`;
- `GridV2` удерживается как separate topology-line, которая может рассматриваться later только через отдельное явное решение.

## Explicit exclusions

Этот документ намеренно не делает следующего:

- не задаёт migration sequencing;
- не даёт implementation steps или roadmap переноса;
- не выполняет exhaustive audit legacy-проекта;
- не переоткрывает решение о full Grid transfer;
- не трактует lab/dev scaffolding как готовую gameplay base;
- не описывает `GridV2` как тихую замену `legacy global Grid`;
- не превращает transfer boundary в re-architecture plan.

## Unresolved but allowed unknowns

Следующие неизвестные допускаются и не блокируют текущий boundary:

- точная later-форма внутреннего рефакторинга `legacy global Grid` после переноса foundation;
- точный момент и способ включения `Gas.Interest` и `Gas.T3.Data` beyond their current `transfer-later` status;
- будущая судьба `GridV2` beyond its current status as separate topology-line;
- точный объём сохранения non-foundation tooling и lab assets как reference surface, пока они не возвращаются в carry-now foundation.
