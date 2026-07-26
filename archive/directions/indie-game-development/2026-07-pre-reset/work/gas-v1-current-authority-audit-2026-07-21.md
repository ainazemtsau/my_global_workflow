# Gas V1 — аудит текущей границы и фронт master plan

date: 2026-07-21
status: ACCEPTED PLANNING ROUTE
product_snapshot: `GasCoopGame main == origin/main @ f6e4f725543514bd67441d4be9ca181392f48c73`, clean
owner_verdict: `Полный Gas V1 master plan сейчас, реализация ступенями — рекомендую`; далее владелец уточнил: `в принципе, согласен` и потребовал отдельно подробно планировать каждый узел перед реализацией, особенно оптимизацию.

## Короткий итог

Gas V1 — это вся будущая игровая симуляция газа. `NearGas` — только уже построенное подробное ядро
этой системы, а не готовый газ полного уровня.

Текущая основа умеет детерминированно считать типы, массу, перенос, вес, реакции и направленный поток
по клеткам 50 см. Она выпущена и хорошо проверена, но пока не подключена к настоящему игровому циклу,
сгенерированному уровню, изменениям мира, игрокам и общей сетевой сессии. Она также не решает масштаб
уровня примерно из 150 комнат.

Владелец принял маршрут: сейчас составить один полный, но верхнеуровневый Gas V1 master plan. Он
покажет ступени, зависимости, владельцев и критерии готовности. Он не будет заранее проектировать
внутреннее устройство каждой ступени. Перед реализацией каждого крупного узла будет отдельный
подробный план и, где требуется выбор, отдельное решение владельца. Оптимизация полного уровня
обязательно присутствует в master plan, но её способ нельзя выбрать без отдельного обсуждения.

Gas Simulation владеет только самой симуляцией газа и её доказательствами. Сетевую сессию, доставку
действий, участников и смену хоста он себе не забирает. Однако Gas обязан вернуть детерминированный
результат, быстрый контрольный отпечаток и нагрузочное доказательство, которые сможет принять
Multiplayer/Program. Общая сцена не может называться co-op-ready, пока этот handoff не замкнут.

## Почему компонент называется NearGas

Название появилось, когда рядом существовали старый грубый расчёт дальних комнат и новый подробный
расчёт по кубам 50×50×50 см. Новый подробный путь назвали `NearGas`, то есть газ ближнего,
детализированного масштаба.

Название не означает, что текущий код уже умеет работать «около игрока». Он не знает положения игрока
и не выбирает близкие или дальние области. Ему передают одно поколение мира, и он подробно считает
весь переданный объём. Сейчас у него нет рабочего дальнего тира, свёртки комнат или перехода между
подробным и дешёвым состоянием.

Поэтому во владельческих материалах вся цель называется `Gas V1`. `NearGas` остаётся внутренним
названием существующего подробного ядра. Переименование до выбора полной масштабной архитектуры не
устраняет ни одного функционального разрыва.

## First-hand срез текущего продукта

- Product `main` и `origin/main` совпадали на `f6e4f725543514bd67441d4be9ca181392f48c73`; рабочее дерево
  было чистым. Между прежним аудитным основанием `45b15623` и `f6e4f725` в `Assets/GasCoopGame/Core`
  и `tests` изменений нет: более свежие коммиты относятся к cleanup/control-plane, поэтому прямой
  разбор Core остаётся применим к текущему product main.
- `Assets/GasCoopGame/Core/Field/NearGas/NearGasSimulation.cs` прямо описывает текущий owner как
  dormant/unwired. Один `Step` применяет постоянные источники, разовые массовые события, импульсы,
  реакции и sparse flow, затем делает один commit. Публичное чтение привязано к поколению, а не к
  подтверждённой ревизии каждого тика.
- `Assets/GasCoopGame/Core/Field/NearGas/NearGasInput.cs` принимает ожидаемый тик, массовые события и
  импульсы. В нём нет команд создать/переместить/выключить источник, изменения двери/топологии,
  scheduler или worker count. Результат шага не несёт нового digest, общей revision или change batch.
- `Assets/GasCoopGame/Core/Sim/SimInstance.cs` остаётся игрушечной оболочкой и не подключает NearGas,
  PlayerSense или Actor authority.
- Текущий sparse-dominant store считает активный фронт, но сохраняет массивы, размер которых зависит от
  всего домена. Старый полный `MeaningChecksum` проходит по домену и оставлен как медленный audit/debug
  oracle, а дешёвого обычного per-tick digest ещё нет.
- Product `docs/gas-simulation/PROGRAM.md`, текущие ADR и Direction terminal close согласны в главном:
  NearGas L1/L1B — выпущенная foundation, не готовый live scene drop. Direction terminal receipt:
  `history/2026-07-19-s-work-near-gas-l1b-v29-terminal-home-close-001.md`, product revision `693e671b`.

## Текущий инвентарь

### 1. Доставлено и выпущено

| Что | Что реально доказано | Текущее evidence |
|---|---|---|
| Подробный перенос газа | Целочисленный поток через открытые грани, сохранение массы, детерминированный порядок | `knowledge/g9c41-gas-engine-SPEC.md`; current `Core/Field/Voxel/**`; living sim-core spec |
| Типы, вес и представление | Registry/config, разные параметры переноса и веса, sparse-dominant active-front storage | current `openspec/specs/sim-core/spec.md`; Core/tests; SPEC Fact 4 |
| Реакции | Табличные реакции, telegraph/bang и handlers в текущем ядре | `knowledge/g9c41-sc-reactions-c-exec-021-delivered.md`; current Core/tests |
| Направленный поток внутри Gas | Выброс, коридор, развилка, клапан, затухающий face bias | current `VoxelImpulse`/forced-flow tests; SPEC forced-flow section |
| Атомарный NearGas owner | Замена поколения, подготовленный полный Step, один commit и fail-atomic поведение | current `NearGasSimulation.cs`; product ADR-E-0011; released L1 receipt |
| Наблюдаемость L1B | Пять operation-local observation families, retry/fault evidence и real loopback без изменения поведения | terminal Direction close at `693e671b`; product ADR-E-0013 |
| Статическая Structure→Gas проекция | Статическая 25 см структура проецируется в 50 см газовые грани | current Structure/Voxel code and tests; Grid authority audit |

### 2. Основа есть, но к игре не подключена

| Что | Чего не хватает | Текущее evidence |
|---|---|---|
| NearGas Step | Не включён в production `SimInstance`/игровой цикл и не публикует обычный committed tick snapshot | current `NearGasSimulation.cs`, `NearGasInput.cs`, `SimInstance.cs` |
| Постоянные источники | Источники задаются при создании поколения; нет runtime lifecycle-команд | current NearGas generation/input surface; product PROGRAM source route |
| PlayerSense | Расчёт exposure/dose доставлен отдельно, но читает raw field и не подключён к живому игроку | `knowledge/g9c41-sc-sense-delivered-unwired.md`; current Sense code |
| Network foundations | Input bus, FishNet relay и loopback существуют отдельно | current `Core/Sim/**`, `Net/FishNet/**`; Grid audit |
| Structure/topology | Статическую геометрию можно построить; полезные старые atomic-change инварианты существуют | current Structure code; historical coarse topology tests; Grid audit |
| Performance foundation | Active-front kernel уменьшает работу на пустом/спящем газе | current sparse-dominant code/tests; SPEC scale measurements |

### 3. Припарковано или отложено

| Что | Текущая граница | Основание |
|---|---|---|
| Независимый Wind Layer | Владелец выбрал его как отдельную будущую систему; сейчас сохраняется gas-local forced flow | `history/2026-07-21-s-map-gas-track-resume-001.md`; Grid accepted plan |
| Богатство потока выше текущего bias | Lattice-room и настоящая fixed-point inertia включаются только после отдельного owner-eye триггера | `knowledge/g9c41-scale-watchmen.md` |
| Огромные ангары | Не входят в текущий целевой профиль; fallback остаётся вооружённым до отдельного решения | SPEC scale section; актуальное слово владельца в этой сессии |
| Деталь тоньше 50 см | Только будущий read-only визуальный refinement, не новая authority газа | `knowledge/g9c41-scale-watchmen.md` |
| Production roster, сложная env-типизация и баланс последствий | Технические сокеты частично есть; конкретное игровое содержание и момент активации требуют свежих узлов/канона | SPEC; `knowledge/g9c41-sc-catalog-reframe.md`; current Program |

### 4. Устарело или заменено

| Старый путь | Текущий вердикт | Почему нельзя запускать |
|---|---|---|
| S0–S6 как живая дорога | Доставленные способности сохраняются, но сама последовательность заменена current Program/Gas planning | старые CALL/status не отражают NearGas L1/L1B и Program v2 |
| Отдельный Sc-damage track | Retired | Gas позже выдаёт consequence; Character потребляет его. Старый CALL не соответствует current ownership |
| `c-exec-034` Sc-catalog | Parked historical call, никогда не запускался | нынешний product уже получил type/reaction substrate и требует свежего определения остатка |
| Lv-ingest Phase 0 | NOT DELIVERED / SUPERSEDED BEFORE BUILD / NEVER RESUME | Direction repair и product historical-not-delivered marker |
| Host-broadcast gas-state stream | Retired | принята input-lockstep модель; state stream не возвращается |
| Старые `LayerRegistry`/destructive `RevisionFeed` как новая universal authority | NO NEW DEPENDENCIES | первый consumer может уничтожить batch для второго; Grid V1 строит новый общий контракт |
| Interim coarse far-tier как новая база | NO NEW DEPENDENCIES / должен быть заменён | product headers и Grid audit запрещают строить новые зависимости; current NearGas rollup отсутствует |
| Несколько постоянных Gas Labs | Superseded | Direction приняла одну permanent Integration Lab; старые validators временные |

### 5. Реально отсутствует

- один принятый ступенчатый Gas V1 master plan;
- live composition текущего ядра в игровом цикле;
- runtime lifecycle игровых источников;
- подтверждённый per-tick Gas snapshot/revision/change batch и быстрый digest;
- честный вход от реального сгенерированного уровня;
- выбранная и доказанная архитектура масштаба для примерно 150 комнат;
- измерения памяти, загрузки, idle/active tick и слабого CPU на реальных level profiles;
- реакция текущего NearGas на подтверждённое изменение двери/топологии;
- подключённый output воздействия газа на игрока;
- Gas-side adapters к будущим Grid read/contact contracts;
- единая Grid+Gas+Actor/topology two-peer проверка;
- нагрузочное доказательство восьми одновременно действующих игроков;
- принятый Gas drop для одной постоянной Integration Lab.

## Конфликты текущей authority

| Вопрос | Что говорят действующие/старые тексты | Что показывает current product | Решение аудита |
|---|---|---|---|
| Общая правда газа | В одном месте SPEC говорит «50 см глобально и авторитетно везде»; рядом — «единственная общая правда грубая по комнатам, подробность локальна» | NearGas считает один подробный generation; нового room-rollup нет, interim coarse запрещает новые зависимости | Это реальная архитектурная развилка следующего master plan, а не готовый ответ. Вариант выбирается отдельно владельцем до scale BUILD |
| Размер уровня | Старый target: около 150 комнат ≈223 тыс. клеток; уже там дальний rollup назван обязательным | Текущий код не доказан на полном generated profile | Новое owner-описание 8×4×8 м даёт около 307 тыс. клеток до коридоров. Старое число устарело; scale node обязателен |
| Sparse = полный scale | Старый road местами подразумевает, что active-front почти решает цену | Store всё ещё имеет domain-sized arrays; digest/parallel tick отсутствуют; восемь игроков могут разбудить много областей | Отдельно доказать память, empty/stable cost, 8 active regions, widespread gas и слабый CPU. Не банковать недоставленное ×4–8 ускорение |
| Сеть | SPEC принимает input-lockstep, но старый текст объявляет две реальные машины «никогда не гейтом» | Есть input transport и Gas loopback по отдельности, нет end-to-end Grid/Gas/Actor proof | Принятый Grid plan и требование 8 игроков supersede эту мягкость: обязательны настоящий two-peer handoff и поздний 8-player proof |
| Committed read | Accepted cross-layer rule запрещает live mid-tick reads | NearGas public read generation-bound; per-tick revision/snapshot отсутствует | Gas формулирует требования сейчас, точный adapter ждёт Grid contract freeze |
| World change | Старые coarse tests доказывают полезную atomic/replay форму | Current NearGas migration/door change отсутствует | Инварианты можно перенести, старый API — нельзя. Нужен свежий Level/Structure/Grid→Gas handoff |
| Источники | Старый Lv-ingest route объявлял Phase 0 | Phase 0 не доставлен; NearGas отдельно получил статические continuous emitters | Старый route не возобновлять. Runtime source commands — новая Gas-owned работа |
| Lab | Product PROGRAM местами говорит `NearGasSimulationLab` | permanent Lab ещё нет | Direction-решение об одной Integration Lab является текущей границей; Gas возвращает drop, а не строит вторую Lab |
| Старые статусы | Reactions/sense/S0–S6 тексты местами говорят pending/main-pending | Current `f6e4f725` уже содержит delivered foundations | Сохранять доказанное поведение, игнорировать старый routing/status как launch authority |

## Ответственность между треками

Термин `NOT OUR BLOCKER` ниже означает только «не останавливает планирование/внутреннюю работу Gas».
Он не означает, что общий product proof может игнорировать проблему.

| Вопрос | Класс | Что делает Gas | Что должно прийти извне |
|---|---|---|---|
| Поведение, типы, реакции, source semantics, deterministic harness | `GAS OWNS` | Определяет и доказывает саму симуляцию | Ничего |
| Масштабный Gas engine и proof 150-room профиля | `GAS OWNS` | Планирует и доказывает стоимость/корректность, включая 8 активных областей | Level отдаёт representative generated profiles; min-spec решение задаёт бюджет |
| Committed tick/revision/change envelope | `WAITS FOR CONTRACT` | Сейчас фиксирует требования; после freeze строит только Gas-side adapter | Grid публикует общий контракт, порядок и immutable change delivery |
| Generic Object↔Layer Resolver/contact | `WAITS FOR CONTRACT` | Возвращает typed Gas sampling/contact adapter и consequence output | Grid владеет Resolver; Character владеет identity/footprint |
| Actor occupancy | `HANDOFF` | Читает стабильный контакт и выдаёт Gas consequence | Character/Actor возвращает integer committed footprint и lifecycle |
| Topology/world change | `HANDOFF` | Сохраняет массу и реагирует на подтверждённое изменение | Level/Structure задаёт изменение; Grid коммитит revision/change batch |
| Generated 150-room profile | `HANDOFF` | Принимает geometry/topology через replaceable boundary и измеряет Gas | Level/Generation возвращает representative profiles, включая длинные коридоры и вертикаль |
| Exact aperture defect | `NOT OUR BLOCKER` | Не чинит и не подменяет; сохраняет честный внешний gate | Structure/Level закрывает точность проёма до финальной сцены |
| Multiplayer identity/input/order/session | `HANDOFF` | Даёт deterministic reducer, быстрый digest и нагрузочный input surface | Program/Multiplayer связывает peer↔entity, доставляет порядок и возвращает two-peer/8-player evidence |
| Одна permanent Integration Lab | `HANDOFF` | Возвращает scene-ready simulation drop и smoke contract | Integration принимает готовые drops; не изобретает Gas внутри сцены |
| Program cleanup Direction debt | `NOT OUR BLOCKER` | Ничего не ремонтирует и не использует как Gas launch authority | Program отдельно reconciles уже выпущенный product `f6e4f725` со своей live записью |

## Wind: что есть сейчас и к чему хотим прийти

Сейчас направленный поток является частью Gas. `VoxelImpulse` и face bias дают выброс, ветер по
коридору, развилку, клапан и затухание. Это доказанное поведение сохраняется: его нельзя удалить ради
пустой будущей абстракции.

Цель владельца — позднее иметь самостоятельный Wind Layer. Он остаётся deferred и не входит в Gas V1.
Перед будущим запуском надо отдельно ответить:

1. кто создаёт ветер в первой игре;
2. кто кроме Gas действительно читает его;
3. какое состояние Wind является общей подтверждённой правдой;
4. в каком порядке Wind, Structure, Gas и Actor обновляются без same-tick cycle;
5. как мигрировать gas-local bias и доказать, что два ветра не работают одновременно.

В этом аудите не создаются Wind node, track, state, API, adapter, fixture или stub.

## Масштаб полного уровня

Owner target в этой сессии: примерно 150 комнат; средняя комната около 8×4×8 м, отдельные комнаты
на 20–30% больше или меньше, возможны длинные коридоры; огромные ангары пока в паузе.

При клетке 50 см средняя такая комната содержит около 2 048 газовых клеток, а 150 комнат — около
307 000 до коридоров и особенностей раскладки. Поэтому мастер-план обязан иметь отдельный scale/optimization
node и не может оставлять его недатированной пометкой.

Перед реализацией этого узла владелец отдельно получает и принимает подробный план. Он должен сравнить:

- полностью подробную общую симуляцию с chunking/sleep/incremental digest/parallelism;
- общую дешёвую дальнюю правду плюс одинаковые для всех peers подробные активные области вокруг всех
  игроков/событий;
- грубую общую правду с только локальной визуальной подробностью — самый дешёвый, но самый слабый для
  общей глубокой газовой механики вариант.

Рекомендация аудита для следующего подробного разбора: серьёзно рассматривать второй вариант, а первый
держать измеряемой базой. Третий не принимать автоматически из старого SPEC.

Обязательные профили будущего доказательства: пустой уровень; один источник; распространение через
несколько комнат; восемь активных мест; заполненные, но уснувшие комнаты; дверь/пролом, заново будящий
газ; длинный коридор; вертикальная связка; широкое заполнение как stress/kill gate. Измеряются память,
время подготовки, ordinary tick, digest, allocations и слабый CPU. Binding min-spec остаётся отдельным
решением `d-m1-min-spec-hardware-001`.

## Мультиплеерная граница

Gas сохраняет input-lockstep: по сети идут действия, каждый peer сам считает газ. Gas-owned результат:

- один и тот же ordered input всегда даёт тот же Gas state;
- source/topology/player events имеют стабильную identity и порядок;
- ordinary tick выдаёт дешёвый контрольный отпечаток;
- расхождение обнаруживается громко;
- восемь одновременных источников активности не ломают корректность и заявленный budget.

Program/Multiplayer-owned результат: peer/session identity, доставка и порядок inputs, stall/leave/host
policy, two-peer network composition и поздний 8-player session proof. Минимум для реального сетевого
утверждения — две настоящие сетевые машины; loopback на одном компьютере остаётся ранней проверкой, а
не финальным доказательством. Финальный живой тест группы из восьми относится к общей product-proof
цепочке, не к внутреннему Gas BUILD.

## Фронт планирования

### Можно планировать независимо уже сейчас

- верхнеуровневую карту Gas V1 и границы будущих узлов;
- путь от выпущенного NearGas owner к live deterministic Gas capability;
- runtime source lifecycle как Gas-owned outcome;
- требования к ordinary committed publication/digest без выдумывания Grid signatures;
- отдельный scale/optimization node, его owner gate и профили 150-room proof;
- Gas-owned сторону generated-Level, world-change, player-consequence и multiplayer handoffs;
- старые маршруты, которые нельзя возобновлять;
- cuts: giant hangars, independent Wind, late join, dedicated server, rendering и balance.

### Ждёт freeze общего Grid-контракта

- точная форма tick/revision/change envelope;
- точная форма generic Layer↔Layer read и immutable multi-consumer delivery;
- точная форма Object↔Layer Resolver/contact adapter;
- окончательные public names/signatures Gas-side adapters.

### Ждёт возврата других потребителей

- world-change proof — Level/Structure + Grid;
- actor contact/consequence proof — Character/Actor + Grid;
- two-peer/8-player proof — Program/Multiplayer;
- permanent scene intake — Integration;
- generated scale profiles — Level/Generation.

## Рассмотренные маршруты и решение владельца

### A. Полный Gas V1 master plan сейчас, реализация ступенями — ACCEPTED

Master plan показывает весь путь до full-level/network/integration readiness, но остаётся картой. Каждый
крупный узел получает собственный подробный owner-present plan до реализации. Оптимизация включена как
обязательный узел с отдельным владельческим решением. Multiplayer присутствует как обязательный handoff,
не как захваченная Gas работа.

### B. Сначала только маленький live Gas, scale/network отдельными планами потом — NOT SELECTED

Быстрее даёт комнатный результат, но рискует снова закрепить основу, которую придётся переделывать под
150 комнат и восемь игроков.

### C. Ждать готовности всех соседних систем и только потом планировать Gas — NOT SELECTED

Даёт более точные сигнатуры, но без необходимости останавливает независимое Gas planning и слишком
поздно вскрывает масштабные риски.

Точные слова владельца: `Полный Gas V1 master plan сейчас, реализация ступенями — рекомендую`; затем
`в принципе, согласен`, с уточнением, что master plan должен показать путь и разбиение на nodes, а
`для каждой ноды мы уже прям отдельно детально планируем`; оптимизацию владелец хочет `отдельно
проговаривать ... перед тем, как мы будем реализовывать`.

## Следующий шаг

Ровно один следующий root — owner-present planning-only Gas V1 master plan. Он создаёт карту узлов,
зависимостей, доказательств и отдельных будущих plan gates. Он не открывает product branch/worktree,
BUILD или реализацию. Direction default остаётся у Grid.

## Что в этой сессии не запускалось

Не изменялись product code, tests, assets, scenes или product docs. Не запускались Unity, tests, build,
Deliver или benchmark. Не создавались product branch/worktree, executor CALL, BUILD authority, Wind
track/stub, Grid contract, Resolver, Character/Actor implementation, aperture repair, Multiplayer runtime
или вторая permanent Lab.

END_OF_FILE: live/indie-game-development/work/gas-v1-current-authority-audit-2026-07-21.md
