# Grid / Layers / World Change — аудит текущей authority

status: DRAFT / AWAITING OWNER VERDICT
date: 2026-07-20
track: grid
node: g-4b92
source_call: c-work-grid-current-authority-audit-001

Этот документ — проверенная подготовительная карта, но ещё не принятая владельцем архитектура или
PLAN. Он ничего не разрешает реализовывать. После чтения владелец должен принять выводы, исправить их
или принять только фактическую часть и отложить выбор маршрута.

## Короткий вывод простыми словами

В продукте уже есть хорошие отдельные детали: целочисленная топология, согласованные Gas/Structure
координаты, статическая проекция отверстий, детерминированные старые слои, сильное изолированное ядро
NearGas и input-lockstep primitives. Но общей современной системы Grid, которая связывает два
независимых слоя через одну подтверждённую ревизию, пока нет.

Главные причины:

1. Старый event feed разрушается при чтении: первый consumer забирает события, второй их уже не видит.
2. NearGas публикует живое generation-bound состояние, но не отдельный committed snapshot/revision на
   каждый тик и не immutable change batch для нескольких consumers.
3. У Actor нет подтверждённого целочисленного occupancy в Grid; Unity Transform/float BodyPose — view,
   не общая sim-authority.
4. Универсального Object ↔ Layer пути нет: движение объекта и приход изменившегося слоя к неподвижному
   объекту сейчас не сведены в один детерминированный контракт.
5. Текущий wind — доказанный внутренний механизм Gas, а не самостоятельный слой.
6. Multiplayer имеет FishNet input transport, но Grid revisions, NearGas, Actor identity/occupancy и
   единый commit stamp ещё не соединены.

Поэтому рекомендованный маршрут — **гибридный legacy-first**: сразу запретить новым работам зависеть от
устаревших путей, затем заморозить маленький новый контракт, после чего заменять старые участки по одному
и удалять каждый сразу после доказанной замены. Большое удаление всего legacy в начале опасно: вместе с
мусором оно снесёт работающие coordinate/topology primitives и полезные regression proofs. Оставлять
legacy без ограждения тоже нельзя: новые зависимости продолжат загрязнять систему.

## Что именно было проверено

### Product refs

- Read-only checkout `C:/projects/Unity/GasCoopGame` чистый: `HEAD = main = origin/main =
  45b15623120f395b4295e43ac6cc5ed0c3aa108c`.
- Локальный `dev = baf8513caa691a3fcbdebddde6b4feb6aa278108`; локальный `dev2 =
  a48883b5833a0d9306177ca232848cf4d6c6f486`; локальный remote-tracking `origin/dev2 =
  1c99a907435f8a5e2cce1b692ab4a273c46484e5`.
- Более свежая cleanup-линия Program существует только локально: cleanup candidate `72c7c8c6`,
  локальная интеграция `c5c21c13`, blocker evidence `baf8513c`. Deliver остановлен внешним Character
  review-evidence defect; push/merge/release не было. Поэтому эта линия — свежее evidence, но не новая
  опубликованная product authority.
- Network fetch не выполнялся. `origin/*` выше — локально наблюдаемые remote-tracking refs, а не
  утверждение о новом сетевом readback.

### Direction authority

- `TREE.md`, `CHARTER.md`, `NOW.md`;
- `work/program-v2-integration-lab-plan.md`, особенно M3 и M5;
- `knowledge/g9c41-gas-engine-SPEC.md`;
- `work/grid-object-layer-interaction-resolver-brief.md`;
- `history/2026-07-20-s-map-grid-track-resume-001.md`;
- `history/2026-07-19-s-work-near-gas-l1b-v29-terminal-home-close-001.md`;
- сохранённая aperture-линия в product OpenSpec/result/review/preservation metadata.

### Ограничение доказательств

Product code, tests, fixtures, SPEC/ADR/PLAN и сохранённые RESULT/review были прочитаны. Тесты в этой
сессии не перезапускались. Поэтому `работает и доказано` ниже означает: поведение имеет конкретную
реализацию и committed proof в текущей линии; это не заявление о свежем test run 20 июля.

## Инвентарь возможностей

| Область | Класс | Что реально есть | Evidence | Чего не хватает |
|---|---|---|---|---|
| Integer topology и stable ids | `работает и доказано` | `TopologyDocument`, `TopologyStableIds`, conformance и coarse ingestion дают стабильную целочисленную основу. | `Assets/GasCoopGame/Core/Field/Topology/TopologyStableIds.cs`; `Assets/GasCoopGame/Core/Field/Topology/Coarse/{TopologyDocument,TopologyConformance}.cs`; `tests/GasCoopGame.Core.Tests/Field/Coarse/Topology/{TopologyStableIdsDerivationTests,CoarseTopologyIngestionTests}.cs` | Это ещё не layer-neutral ownership/address service для runtime consumers. |
| Gas/Structure coordinates | `работает и доказано` | `CellGrid`, `CellLattice`, `VoxelResolution`, `VoxelGrids` согласуют 50 см Gas и 25 см Structure. | `Assets/GasCoopGame/Core/Field/Voxel/{CellGrid,CellLattice,VoxelResolution,VoxelGrids}.cs`; `RL4ProjectionCountTests.cs`; `VoxelizerTests.cs` | Нужен публичный минимальный общий address/projection contract без переноса данных слоёв в Grid. |
| Static Structure → Gas projection | `работает и доказано` | `StructureGrid`, `SubFaceOccupancy`, `StructureGasProjection`, `StructureVoxelizer` публикуют статическую occupancy/conductivity проекцию. | `Assets/GasCoopGame/Core/Field/Structure/{StructureGrid,SubFaceOccupancy,StructureGasProjection,StructureVoxelizer}.cs`; `tests/GasCoopGame.Core.Tests/Field/Structure/{RL2StructureLayerTests,RL3ApertureValidationTests,RL5NegativeControlTests}.cs` | Нет текущего runtime commit/change contract для перестройки структуры и миграции NearGas. |
| Старый layer registry/scheduler | `устарело/конфликтует` | `ILayer`, `LayerRegistry`, phases и writer tokens доказывают deterministic order и single-writer в старом Field пути. | `Assets/GasCoopGame/Core/Field/Layers/{ILayer,LayerRegistry}.cs`; `tests/GasCoopGame.Core.Tests/Field/Layers/{LayerRegistryTests,LayerRegistryAddAtomicityTests,LayerRegistryAddAtomicityNegativeControlTests}.cs` | NearGas через него не работает; принимать его универсальным current scheduler нельзя без нового решения. |
| Старый Grid event feed | `сломано` | `RevisionFeed` сортирует события, но `DrainAscending()` очищает общую очередь. `TemperatureLayer` сам вызывает drain. | `Assets/GasCoopGame/Core/Field/Events/{IGridEventBus,RevisionFeed}.cs`; `Assets/GasCoopGame/Core/Field/Layers/TemperatureLayer.cs`; `tests/GasCoopGame.Core.Tests/Field/Events/RevisionFeedTests.cs` прямо доказывает, что drain очищает queue | При двух consumers первый забирает batch, второй видит пусто. Нужен immutable committed batch или per-consumer cursor, а не patch старого destructive API. |
| NearGas atomic owner и generation lifecycle | `работает и доказано` | `NearGasSimulation` даёт engine-free atomic owner, retry/fault/lifecycle и loud stale-generation rejection. Терминальный L1B close — `693e671bcd24bc84663f5e69127adb21aac94b7d`, binding review и normal `1813/1813` в Direction receipt. | `Assets/GasCoopGame/Core/Field/NearGas/{NearGasSimulation,NearGasInput}.cs`; `tests/GasCoopGame.Core.Tests/Field/NearGas/{NearGasGenerationLifecycleTests,NearGasStepTests}.cs`; `history/2026-07-19-s-work-near-gas-l1b-v29-terminal-home-close-001.md` | Это сильное внутреннее основание Gas, но не готовый общий Grid seam. |
| NearGas committed per-tick read/revision/change batch | `отсутствует` | `INearGasReadState` читает состояние текущей generation; `NearGasGenerationId` — opaque lifetime token. | `NearGasSimulation.cs`; `NearGasInput.cs`; `NearGasLegacyAuditTests.cs` специально запрещает digest/revision в `NearGasStepResult` | Нужен отдельный committed read snapshot/stamp и immutable changed-address batch. Текущие live reads между Steps не равны общей commit revision. |
| Player gas sensing | `есть, но не доказано` | `PlayerSense.cs` имеет actor-shaped input, exposure/dose state и богатые unit/property/negative tests. | `Assets/GasCoopGame/Core/Field/Sense/PlayerSense.cs`; `tests/GasCoopGame.Core.Tests/Field/Sense/PlayerSense*Tests.cs` | Он читает raw `VoxelField`, не подключён к единственной live NearGas authority и не доказывает универсальный Object ↔ Layer seam. |
| Actor committed occupancy | `отсутствует` | `TickInput` уже несёт actor-related input; `IAuthoritativeBodyState` — view socket; `BodyPose` — float presentation value. | `Assets/GasCoopGame/Core/Sim/TickInput.cs`; `Assets/GasCoopGame/Characters/{IAuthoritativeBodyState,BodyPose}.cs` | Нет стабильного `EntityId` + integer committed cells/bounds + spawn/despawn/teleport lifecycle, пригодного для Grid и lockstep. |
| Object ↔ Layer resolver/index/subscriptions | `отсутствует` | Есть problem brief и gas-specific sense foundation. | Direction `work/grid-object-layer-interaction-resolver-brief.md` | Нет generic spatial index, subscriptions, dirty-layer trigger, previous contact cache и canonical entered/changed/exited output. |
| Static aperture validation | `работает и доказано` | Declared aperture проверяется против geometry-derived shared boundary и проецируется в sub-face occupancy. | `StructureVoxelizer.cs`; `RL3ApertureValidationTests.cs`; `StructureApertureCoordinateOverflowTests.cs` | Это не доказывает точную семантику, когда тот же boundary уже открыт portal band. |
| Exact aperture authority | `сломано` | Portal band сначала открывает всю ширину face, затем aperture только OR-ит mask. Matching portal может расширить непустой aperture. | `StructureVoxelizer.cs`, шаги 2–3; preserved RED head `5af1d8db...` | Отдельный V31-compatible disposition. Preservation metadata: `PRESERVED-PAUSED`, `not-applied`, `no_successor`; surface freeze `NOT DELIVERED`. Не смешивать с Object ↔ Layer. |
| Historical topology-change commit/replay | `работает и доказано` | `TopologyChangeSet`, `CoarseTopologyRevision`, `CoarseBreachLayer` и `CoarseSectorGraph.Apply` имеют atomic/replay proof. | `Assets/GasCoopGame/Core/Field/Topology/Coarse/{TopologyChangeSet,CoarseBreachLayer}.cs`; `Assets/GasCoopGame/Core/Field/Coarse/CoarseSectorGraph.cs`; `tests/GasCoopGame.Core.Tests/Field/Topology/Coarse/{TopologyCommitAtomicityTests,TopologyCommitAtomicityNegativeControlTests}.cs`; `tests/GasCoopGame.Core.Tests/Field/Voxel/RL7BreachFlipProofTests.cs` | Доказательство относится к interim coarse path, а не к current NearGas migration. Инварианты можно сохранить, dependencies — нельзя. |
| Coarse far-tier/read-model как current authority | `устарело/конфликтует` | `CoarseGasReadModel`/`IGasReadModel` существуют и тестировались. | Файлы имеют явный header `scheduled for DELETION at S4 / DO NOT add new dependencies`; `docs/INTERIM-COARSE-FAR-TIER.md` | Текущий Program заменяет area-blind coarse tier. Нельзя строить новый Grid вокруг этого API. |
| Current NearGas world change/migration | `отсутствует` | Static structure можно построить; historical coarse change proof существует. | Сопоставление current NearGas surface с topology-change code и Program M5 | Нет принятого atomic swap/migration policy, commit stamp и proof реакции NearGas + второго consumer на одно изменение. |
| Gas-local forced flow («wind») | `работает и доказано` | `VoxelImpulse`/face bias доказывают corridor, fork, conservation, decay и deterministic order внутри Gas. | `Assets/GasCoopGame/Core/Field/Voxel/VoxelImpulse.cs`; `docs/adr/ADR-0012-s1-forced-flow-bias.md`; `tests/GasCoopGame.Core.Tests/Field/ForcedFlow/RW*.cs` | Нет независимого Wind state/read model/revision. `LayerKey` знает Gas/Temperature, но не current Wind authority. |
| FishNet input-lockstep edge | `работает и доказано` | `ITickInputBus`, in-memory bus, `TickInput`, `FishNetTickInputBus` дают host relay, peer roster и reliable ordered input batches. | `Assets/GasCoopGame/Core/Sim/{ITickInputBus,InMemoryTickInputBus,TickInput}.cs`; `Assets/GasCoopGame/Net/FishNet/**`; `docs/adr/ADR-0002-net-determinism-lockstep-fishnet.md`; `Assets/Tests/EditMode/Net/FishNetConvergenceTests.cs` | Это transport/input foundation, не доказанная совместная Grid+NearGas+Actor multiplayer simulation. |
| NearGas/Grid/Actor multiplayer integration | `отсутствует` | Gas loopback и FishNet primitives существуют раздельно. | `ADR-0002`; `ADR-0016-s2a-zero-legacy-reconstruction-retirement.md`; Program future edge-codec route | Нет единого tick/commit stamp, PeerId↔EntityId binding, actor occupancy authority, topology commands и two-peer end-to-end proof. |
| Постоянная Integration Lab | `отсутствует` | Direction приняла одну будущую permanent playable Lab; product main не имеет принятой `IntegrationLab`/`NearGasSimulationLab`. | `work/program-v2-integration-lab-plan.md`; Program cleanup audit/blocked result | Product PROGRAM ещё называет будущую `NearGasSimulationLab`; это надо согласовать до scene PLAN. Старые validators не становятся второй постоянной Lab. |

## Матрица дефектов и долгов

| ID | Отдельная линия | Симптом | Какой контракт затронут | Сила evidence | Законный следующий disposition |
|---|---|---|---|---|---|
| G-D1 | Event transport | Второй consumer теряет события после `DrainAscending()` первого. | Один committed revision/event должен одинаково дойти минимум до двух consumers. | Прямая реализация + тест destructive drain; refutation по коду. | В новом contract PLAN выбрать immutable batch или per-consumer cursor; старое API сразу пометить no-new-dependencies. |
| G-D2 | Object ↔ Layer | Движущийся объект можно обработать ad hoc, но изменение слоя вокруг неподвижного объекта теряется или требует полного scan. | Committed occupancy + changed spatial ranges + typed sampling + canonical contacts. | Требование Direction + отсутствие product mechanism. | Отдельное architecture comparison: central god object, per-layer observers, coordinator/resolver; затем synthetic two-layer proof PLAN. |
| G-D3 | Exact aperture | Portal может открыть больше, чем разрешён непустой exact aperture. | Structure authority и точный sub-face conductivity. | Прямая code path + сохранённый tests-only RED `5af1d8db` (5 файлов, 823 additions); surface freeze не доставлен. | Отдельно re-check V31 preservation и решить resume/re-plan/retire. Не включать в Object resolver BUILD. |
| G-D4 | NearGas commit boundary | Generation-bound live read ошибочно можно принять за committed per-tick snapshot. | Cross-layer reads только из одной явно названной committed revision; live mid-tick fail-closed. | Public surface + explicit legacy audit tests. | Спроектировать минимальный adapter/envelope без переписывания NearGas internals заранее. |
| G-D5 | Actor authority | Float `BodyPose`/Transform не даёт одинаковую integer occupancy на peers. | Stable EntityId, committed footprint и deterministic lifecycle. | Отсутствие sim contract; view sockets явно не объявляют такую authority. | Character track формирует actor spatial-authority input; Grid фиксирует только потребляемый boundary. |
| G-D6 | World change | Хороший coarse proof существует на пути, который запрещает новые dependencies; NearGas migration отсутствует. | Atomic topology command → new revision → layer migration/reaction. | Historical tests + явные interim headers + current Program conflict. | Harvest invariants, затем новый Structure/Grid/NearGas planning slice; coarse API не переносить как authority. |
| G-D7 | Wind ownership | Gas-local bias могут случайно выдать за второй независимый layer. | M3 требует двух разных consumers одного universal seam. | Код/tests доказывают только Gas-owned flow. | Owner verdict: оставить gas-local или отдельно спроектировать Wind только с реальными producers/consumers. Synthetic layer допустим для generic proof. |
| G-D8 | Multiplayer seam | Lockstep transport есть, но sim modules не разделяют commit/tick/entity contract. | Deterministic re-run from same inputs and same committed world/actor identity. | ADR + transport code + отсутствие end-to-end integration. | Передать Program/Integration точный planning input; не создавать новый track автоматически. |
| G-D9 | Lab authority | Product wording про `NearGasSimulationLab` конфликтует с Direction-решением об одной permanent Integration Lab. | Один permanent entry point; module fixtures временные. | Текущие Direction и product Program тексты. | Согласовать в master plan до создания scene; ничего не переименовывать/строить из аудита. |

## Кто за что отвечает

| Владелец | Публикует | Потребляет | Что Grid от него не забирает | Текущий разрыв |
|---|---|---|---|---|
| Grid | Stable spatial addresses/regions, ownership, commit envelope, immutable change transport/cursors, ordering и stale rejection | Structure topology commands и согласованные layer/actor envelopes | Gas values, wind physics, destruction policy, actor gameplay, network session | Общего current contract ещё нет; старый feed destructive. |
| Structure / Destruction | Structure state, exact apertures, topology-change command/result и migration intent | Grid address/commit rules | Gas simulation и object contacts | Exact aperture defect и нет current NearGas migration path. |
| Gas | Gas state, sources/reactions, gas-local forced-flow; typed committed Gas read adapter | Committed Structure/Grid и, если решено, committed Wind | Universal event bus, actor authority, network | NearGas committed adapter/change batch и live wiring отсутствуют. |
| Wind, если выбран отдельно | Собственный committed flow state и changed ranges | Committed Structure; named producers/commands | Gas state и generic Grid machinery | Такого owner/read model сейчас нет. |
| Actor / Character | Stable EntityId и committed integer occupancy/footprint; gameplay reaction consumes typed contacts | Grid addresses и typed layer contact/read results | Layer storage, gas physics, Character View | Есть view/input pieces, нет authoritative occupancy. |
| Multiplayer | Session/peer identity, PeerId↔EntityId binding, input collection/order, FishNet edge/codecs | Deterministic Grid/Layer/Actor commit envelope | Simulation meaning и Grid storage | Input transport есть; end-to-end binding нет. |
| Integration Lab | Ничего из module authority; только acceptance composition, smoke и playable proof | Принятые drops всех tracks | Алгоритмы и public contracts модулей | Permanent scene ещё нет; naming/authority надо согласовать. |

Минимальная мыслительная модель будущего seam такая:

```text
inputs/topology commands
        ↓
Grid фиксирует tick + revision + spatial change batch
        ↓
Structure / Gas / Wind / Actor читают только committed snapshots
        ↓
каждый consumer имеет собственный cursor и не уничтожает batch для остальных
        ↓
Integration/Multiplayer доказывают одинаковый результат, но не владеют физикой
```

Это описание ролей, не утверждённые имена C# типов.

## Wind: три честных варианта

| Вариант | Плюсы | Цена/риск | Вердикт аудита |
|---|---|---|---|
| A. Оставить wind внутри Gas | Совпадает с текущей доказанной реализацией; нет нового lifecycle, revision и зависимости. | Другие потребители не смогут читать общий flow, пока такой реальный use case не сформирован. | Самый безопасный current default. Не мешает позже вынести слой через adapter/migration. |
| B. Самостоятельный Wind Layer | Имеет смысл, если один и тот же committed flow реально нужен минимум Gas и Actor/оборудованию; может стать настоящим вторым consumer Grid. | Нужны названные producers, собственное state/read model/revision, порядок относительно Structure/Gas/Actor и отсутствие same-tick cycle. Раннее выделение создаст пустой framework. | Серьёзный кандидат для отдельного owner decision, но сейчас не доказан и не готов служить вторым consumer. |
| C. Общий flow/field producer | Может когда-нибудь покрыть wind, pressure, conveyors и другие vector fields. | Самый высокий риск преждевременной абстракции и безымянных generic values. Нет двух текущих use cases с одинаковой семантикой. | Сейчас отклонить как преждевременный; вернуться только после двух реальных совместимых producers/consumers. |

**Ответ на прямой вопрос:** текущий wind нельзя уже считать независимым consumer layer. Если владелец
хочет проверить вариант B, сначала нужен маленький paper decision: кто публикует ветер, кто кроме Gas
читает его в первой версии, какая задержка допустима и не образуется ли live cycle. Track/CALL/BUILD из
этого аудита не создаются.

## Multiplayer: что передавать и куда

Текущая принятая модель — player-hosted input-lockstep поверх FishNet. Через сеть идут inputs, каждый
peer повторяет deterministic reducer. Старый host-broadcast/chunked gas-state stream удалён/retired;
возвращать его ради Grid не надо.

Уже есть:

- `ITickInputBus`, `InMemoryTickInputBus`, `TickInput`;
- `FishNetTickInputBus`, host relay, peer roster и ordered reliable batches;
- actor-related поля в tick input;
- deterministic loopback/convergence foundations.

Не доказано:

- один общий stamp `{tick, grid revision, topology revision}`;
- стабильное PeerId ↔ EntityId ↔ committed occupancy соответствие;
- NearGas как реальный consumer общей input bus;
- одинаковое применение topology commands и layer changes на двух peers;
- end-to-end co-op acceptance в будущей Lab.

Правильный handoff сейчас — **Program/Integration planning input**, а не автоматическая активация
нового Multiplayer track: перед co-op claim определить edge contract identity/input/order, затем доказать
два peer-а на одном committed Grid/Gas/Actor state. Grid отдаёт deterministic envelope; Multiplayer
владеет session/transport. В текущем `TREE.md` отдельного live Multiplayer track нет.

## Legacy-first маршрут

### Шаг 1. Сразу поставить ограждение

В первом planning continuation составить короткую таблицу:

- `KEEP`: stable ids, integer topology/voxel math, Structure projection, NearGas atomic owner и полезные
  tests/invariants;
- `QUARANTINE / NO NEW DEPENDENCIES`: старый `ILayer/LayerRegistry` как universal route, destructive
  `RevisionFeed`, interim coarse read model/far tier и временные scene validators;
- `FIX SEPARATELY`: exact aperture и новый non-destructive multi-consumer transport;
- `DELETE AFTER REPLACEMENT PROOF`: behavior-bearing legacy path сразу после того, как конкретная новая
  vertical slice зелёная и единственные consumers мигрировали.

Это не удаляет продукт. Оно не даёт legacy проникать в новый design.

### Шаг 2. Заморозить маленький contract

До параллельной работы определить только общее:

- address/region projection;
- commit/tick/revision envelope;
- committed read boundary;
- immutable change batch или per-consumer cursor;
- stale/live mid-tick rejection;
- кто является честным вторым consumer в proof.

Object resolver, Gas adapter, Wind decision, Actor occupancy и topology migration не должны каждый
изобретать свою версию этих пяти вещей.

### Шаг 3. Заменять вертикальными кусками

После freeze можно независимо планировать bounded slices, если они не меняют общий contract: event
transport proof; synthetic two-layer/Object proof; NearGas adapter; Actor spatial input; Structure
topology-change adapter. После каждого доказанного replacement старый behavior path удаляется сразу,
а не остаётся «на потом».

### Шаг 4. Permanent Integration Lab — последней

Lab принимает уже доказанные drops. Она не должна становиться местом, где одновременно изобретаются
Grid, Gas, Actor, Wind и multiplayer. Сначала contracts и track-owned headless/temporary validators,
затем одна permanent playable scene.

## Quality-first planning front

Рекомендуются три bounded продолжения, все пока только кандидаты:

1. **Grid legacy fence + contract freeze.** Подтвердить KEEP/QUARANTINE/FIX/DELETE-AFTER, сравнить 2–3
   архитектуры и вынести владельцу минимальный Grid/Layer/Actor contract плюс выбор второго consumer.
   Это обязательно идёт первым и последовательно.
2. **Grid migration + retirement plan.** На уже frozen contract расписать replacement → proof → immediate
   deletion для старого event/layer/coarse surface и отдельные handoffs Gas, Character, Level/Structure,
   Program/Multiplayer. Никакого кода.
3. **Grid → Integration Lab master-plan slice.** После принятых contracts собрать dependency DAG, exact
   acceptance drops M3/M5, временные validators, removal triggers и один permanent Lab intake. Никакой
   сцены до отдельного BUILD authority.

После первого frozen contract можно параллельно готовить **планы** независимых slices. Integration,
world-change end-to-end, deletion и Lab acceptance остаются последовательными, потому что зависят от
точных предыдущих доказательств.

## Межтрековые передачи

Полная временная запись находится в
`work/cross-track-recovery-notes-2026-07-20.md`. Коротко:

- Gas: NearGas committed adapter/change batch и решение, остаётся ли wind gas-local.
- Character: stable EntityId + integer committed occupancy; PlayerSense не выдавать за live integration.
- Level/Structure: exact aperture — отдельная preserved-paused линия; current topology-change/migration
  contract нужен совместно с Grid/Gas.
- Program/Integration: одна permanent Lab, lab naming conflict и будущий multiplayer edge proof.
- Multiplayer (пока без track): lockstep primitives есть; identity/commit/topology integration отсутствует.
- Presentation: читать только принятый committed model; не делать view/Transform authority.

## Что не запускалось

- BUILD, PLAN execution, product branch/worktree creation;
- product code/tests/assets/scenes changes;
- Unity, test runner, build, Deliver или network fetch;
- Wind/Water implementation, stubs или новый track;
- Multiplayer track/CALL;
- aperture repair/resume;
- permanent Integration Lab или старые validators;
- Program cleanup release/repair.

## Какой ответ нужен от владельца

Этот audit остаётся draft до фактических слов владельца.

- **A — принять аудит и рекомендуемый hybrid legacy-first маршрут.** Тогда следующий шаг — только
  bounded `legacy fence + contract freeze` planning session.
- **B — исправить конкретные выводы/приоритеты.** Документ обновляется, downstream не открывается.
- **C — принять фактическую карту, но пока не выбирать маршрут.** Audit можно зафиксировать как accepted
  evidence, а planning route оставить отдельным вопросом.

Текущее сообщение `ok` относилось к созданию простого временного межтрекового файла. Оно не считается
вердиктом по этому аудиту или архитектурному маршруту.

END_OF_FILE: live/indie-game-development/work/grid-current-authority-audit-2026-07-20.md
