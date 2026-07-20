# Временные межтрековые заметки после Grid-аудита

status: TEMPORARY RECOVERY CONTEXT / NOT AUTHORITY
date: 2026-07-20
source: Grid current-authority audit, пока ожидающий owner verdict

## Как пользоваться этим файлом

Это простой временный файл для ручного восстановления контекста после периода беспорядочной и
частично устаревшей работы. Он **не является** PLAN, backlog, новым workflow, автоматическим inbox,
решением владельца или разрешением запускать BUILD.

Владелец вручную просит конкретный трек перед его новым планированием прочитать свою секцию. Трек:

1. перечитывает current Direction и product authority;
2. проверяет, не устарела ли заметка;
3. забирает только относящийся к нему вопрос в собственный bounded PLAN/decision;
4. не исполняет чужую работу и не считает эту запись launch authority.

Когда recovery закончится, файл можно оставить историческим evidence или удалить отдельным законным
state change. Никакой автоматизации вокруг него сейчас не создаётся.

## Program / Integration Lab

### Одна permanent Lab против нескольких названий

- Direction уже приняла одну постоянную playable Integration Lab. Module-specific fixtures допустимы
  только как временные validators.
- Current product PROGRAM всё ещё говорит о будущей `NearGasSimulationLab`. До scene PLAN надо явно
  согласовать: это временный Gas validator или прежнее имя будущей единственной Integration Lab.
- Product main `45b15623` не содержит принятой `IntegrationLab` или `NearGasSimulationLab` scene.
- Не строить Lab, пока Grid/Gas/Actor contracts формируются; иначе сцена станет вторым источником
  архитектуры и соберёт legacy dependencies.

Evidence: `work/program-v2-integration-lab-plan.md`; product `docs/gas-simulation/PROGRAM.md`.

### Cleanup lineage — не путать с опубликованной authority

- Чистый product checkout: `HEAD = main = origin/main = 45b15623120f395b4295e43ac6cc5ed0c3aa108c`.
- Cleanup candidate `72c7c8c6` прошёл normal gates и non-author G5, локально интегрирован через
  `c5c21c13`, затем сохранён blocker evidence `baf8513c`.
- Локальный `dev = baf8513c`; push/merge/release не было. Deliver блокирует pre-existing Character
  review-evidence defect.
- Grid или другой track не должен считать cleanup уже выпущенным и не должен чинить этот blocker.

Evidence: `history/2026-07-20-s-work-program-v2-legacy-lab-purge-deliver-blocked-001.md`.

### Multiplayer/co-op acceptance

- Program должен принять будущий co-op claim только после реального edge proof: два peers получают
  canonical inputs и приходят к одному Grid/Gas/Actor committed result.
- Gas loopback и FishNet transport по отдельности этого не доказывают.
- В master plan нужны отдельные acceptance строки для session/identity/input/order и для deterministic
  sim result. Integration не забирает ownership ни у Grid, ни у Multiplayer.

Когда поднимать: перед M3/M4/M5 intake contract и обязательно до любого co-op-complete claim.

## Multiplayer (отдельного live track сейчас нет)

### Что уже существует

- Принята player-hosted input-lockstep модель поверх FishNet; dedicated server не является текущим
  основанием.
- Product имеет `ITickInputBus`, `InMemoryTickInputBus`, `TickInput`, `FishNetTickInputBus`, host relay,
  peer roster и reliable ordered batches.
- Старый host-authoritative gas field stream/chunk reconstruction retired в ADR-0016/S2a. Не возвращать
  его как shortcut.

### Что отсутствует

- общий `{tick, Grid revision, topology revision}` stamp;
- PeerId ↔ EntityId binding;
- integer committed actor occupancy;
- NearGas как реальный participant общей input bus;
- topology commands и layer changes, одинаково применённые на двух peers;
- настоящий end-to-end Grid/Gas/Actor co-op proof.

### Кандидат будущей передачи

Program/Integration вместе с будущим Multiplayer owner должны сформировать bounded planning input:
network edge владеет session/peer/entity binding, canonical input collection и FishNet codecs; Grid
публикует deterministic commit envelope; modules локально повторяют reducer. Новый Multiplayer track
не создавать автоматически — только по явной активации владельца.

Evidence: product `docs/adr/ADR-0002-net-determinism-lockstep-fishnet.md`,
`ADR-0016-s2a-zero-legacy-reconstruction-retirement.md`, `Assets/GasCoopGame/Net/FishNet/**`.

## Gas

### NearGas хорош внутри, но не имеет общего committed Grid read

- NearGas L1B terminal foundation выпущен на `693e671b...`; atomic owner, generation lifecycle, retry/
  fault и stale-generation rejection доказаны.
- `INearGasReadState` остаётся generation-bound live read. `NearGasGenerationId` — lifetime token, а не
  per-tick revision.
- `NearGasStepResult` намеренно не несёт digest/revision; это закреплено `NearGasLegacyAuditTests`.
- Поэтому Gas должен позже дать тонкий committed adapter/snapshot + change batch поверх принятого Grid
  envelope. Не переписывать NearGas internals и не возвращать interim `IGasReadModel` как authority.

Когда поднимать: после Grid contract freeze, в свежем Gas V31 PLAN перед M4/M5 drop.

### Wind пока принадлежит Gas

- `VoxelImpulse`/face bias и RW tests доказывают gas-local forced flow: corridor/fork, conservation,
  decay, deterministic order.
- Самостоятельного Wind state/read model/revision нет. Текущий wind не является вторым независимым
  consumer layer.
- Без отдельного решения Gas продолжает владеть этим механизмом.
- Если владелец выбирает самостоятельный Wind Layer, сначала назвать реальных consumers: минимум Gas
  и Actor/оборудование, а также producers и порядок относительно Structure/Gas. Нельзя создавать слой
  только как абстракцию «на будущее».

Evidence: `Assets/GasCoopGame/Core/Field/Voxel/VoxelImpulse.cs`,
`docs/adr/ADR-0012-s1-forced-flow-bias.md`,
`tests/GasCoopGame.Core.Tests/Field/ForcedFlow/RW*.cs`.

### Object contact

- `PlayerSense.cs` и его tests — полезное Gas-owned foundation, но он читает raw `VoxelField` и не
  доказывает live integration с единственной NearGas authority.
- После общего Grid/Object contract Gas может стать первым real typed adapter: один gas, generic object,
  `inside/outside`. Dose/damage/balance остаются у Gas/gameplay, не у resolver.

## Character / Actor

### Нужна sim-authority позиции, не View

- Grid ожидает стабильный EntityId и committed integer occupancy/footprint: cells/bounds, move, spawn,
  despawn и teleport lifecycle.
- `IAuthoritativeBodyState` сейчас является view socket, а `BodyPose` содержит float presentation data.
  Unity Transform/PhysX callback order нельзя молча сделать checksummed multiplayer authority.
- `TickInput` уже имеет actor-shaped поля, но не закрывает PeerId↔EntityId и committed occupancy.
- Новый Actor Layer относится к свежей V31 работе. Его нельзя задним числом добавить в frozen Character
  Leg 2 или использовать как повод перезапустить тот CALL.

Когда поднимать: перед Character/Gameplay Contact M6 PLAN, после минимального Grid address/commit freeze.

### Что Character должен получить от Grid

- только address projection, committed stamp и typed contact/result;
- canonical enter/changed/exit или принятый эквивалент;
- stale/live mid-tick rejection.

Character остаётся владельцем gameplay reaction и View. Grid не считает damage, movement или animation.

## Level / Structure / Destruction

### Exact aperture — отдельная линия, не Object resolver

- Current static aperture validation работает, но `StructureVoxelizer` сначала открывает полный portal
  band, а затем OR-ит aperture mask. Matching portal может расширить непустой exact aperture.
- Сохранённый product RED head:
  `5af1d8db931d10cc6149a2c1f8e1023bc3b9ffb1` — 5 test/support файлов, 823 additions, production behavior
  не изменён.
- Preservation metadata:
  `docs/engineering/openspec-preservations/c-exec-structure-aperture-authority-v1-plan-001.json` =
  `PRESERVED-PAUSED`, `application: not-applied`, `no_successor: true`; surface freeze `NOT DELIVERED`.
- Перед любой работой нужен свежий V31 disposition: resume/re-plan/retire. Grid-аудит не разрешает BUILD.

### World change

- Historical `TopologyChangeSet`, `CoarseTopologyRevision`, `CoarseBreachLayer` и
  `CoarseSectorGraph.Apply` дают ценные invariants: atomic commit, ordering, replay equality и failure
  atomicity.
- Но coarse far-tier/read model имеет явный `DO NOT add new dependencies / delete or replace at S4`.
- Level/Structure должен публиковать topology command/result и migration intent; Grid присваивает
  committed revision/change batch; Gas и второй consumer реагируют из committed state.
- Current NearGas structure migration отсутствует и требует отдельного совместного plan slice.

Когда поднимать: после Grid contract freeze; exact aperture disposition — отдельно от world-change build.

## Canon / возможный Wind decision

Это пока не новая механика и не отдельный track. Нужен только decision brief, если владелец захочет
вернуться к вопросу:

1. Оставить wind gas-local — current доказанный default.
2. Выделить Wind Layer — только если названы минимум два реальных consumers, producers, state/read
   model и допустимая задержка.
3. Делать generic flow/field producer — сейчас преждевременно, пока нет двух одинаковых use cases.

Canon может уточнить gameplay meaning и реальные consumers, но не выбирает C# architecture. До решения
не создавать Wind content/implementation/stub.

## Presentation

- Presentation читает только принятый committed read model; render buffer, collider или Transform не
  становятся Grid/Layer authority.
- Current Gas visuals и старые scenes не доказывают M3/M5 или multiplayer.
- Если Wind станет отдельным слоем, Presentation не считается достаточным вторым sim consumer: view
  может отображать Wind, но universal seam должен быть доказан независимым authoritative consumer.
- Permanent Lab принимает Presentation после module drops; Presentation не строит вторую Lab.

Когда поднимать: при новом Presentation PLAN после принятия Grid/Gas read boundary.

## Что остаётся внутри Grid и не надо перекладывать

- заменить destructive `RevisionFeed` новым multi-consumer contract;
- зафиксировать address/region projection, commit envelope и stale/live rejection;
- сравнить architecture Object ↔ Layer и определить boundary resolver/index/subscriptions;
- доказать минимум два consumers без Water/Wind stubs;
- составить KEEP/QUARANTINE/FIX/DELETE-AFTER legacy matrix;
- определить последовательность replacement → proof → immediate deletion.

Эти пункты остаются Grid planning work и не должны «утечь» в Gas, Character или Integration.

END_OF_FILE: live/indie-game-development/work/cross-track-recovery-notes-2026-07-20.md
