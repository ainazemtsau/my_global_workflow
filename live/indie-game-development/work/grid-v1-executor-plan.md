# Grid V1 — принятый executor plan

status: ACCEPTED
accepted: 2026-07-21
amended: 2026-07-21
master_owner_verdict: «Принять план с обязательным Multiplayer handoff/gate»
executor_owner_verdict_raw: «Так, принимаю, гриту один executor plan»
owner_clarification_raw: «F-tri система будет винт, ну, ветер. Это не столь важно, да, для нас сейчас. Нам нужно сделать сначала основы.»
document_authority_amendment_owner_verdict_raw: «Принимаю поправку целиком»
document_authority_correction_002_owner_verdict_raw: «Окей, принимаю прощённую correction 2 по шести правилам.»
recorded_meaning: Grid V1 executor plan принят; вторым настоящим consumer layer выбран отдельный будущий Wind, но сначала строится общая Grid-основа.

## 1. Простая картина

Grid V1 — не новая игровая механика и не хозяин всего мира. Это общий координатор, который отвечает
на четыре вопроса:

1. где что находится;
2. какое состояние мира уже полностью подтверждено;
3. что именно изменилось;
4. какие объекты или слои это изменение затрагивает.

Газ, ветер, строение и персонаж по-прежнему хранят и считают собственное состояние. Grid только даёт
им общие координаты, безопасную публикацию законченного шага, независимую доставку изменений и
контакты `entered / changed / exited`. Игровые последствия остаются у consumer-треков.

Есть два отдельных пути:

- **Layer ↔ Layer:** один слой читает подтверждённое состояние другого и сам считает реакцию;
- **Object ↔ Layer:** Resolver одинаково обнаруживает контакт, когда объект пришёл к слою или слой
  изменился под неподвижным объектом.

Object Resolver не вычисляет Layer↔Layer interaction. Synthetic proof доказывает только универсальность
Grid. Реальные M3 consumers теперь названы: Gas и будущий отдельный Wind. Wind не создаётся внутри Grid
и не запускается до общей основы.

## 2. Fresh product authority и найденные конфликты

First-hand snapshot 2026-07-21:

- product repo `C:\projects\Unity\GasCoopGame`;
- clean `main == origin/main @ f6e4f725543514bd67441d4be9ca181392f48c73` по локально
  наблюдавшимся refs; это evidence, не launch pin;
- перечитаны current product `AGENTS.md`, Core contract/asmdef, living SPEC, PROGRAM, relevant ADR/PLAN,
  source, focused tests, legacy-lab policy и опубликованный purge result;
- product repo, refs и working tree не менялись; network fetch не выполнялся.

Материальные конфликты:

1. Living SPEC и historical ADR-0016 всё ещё требуют старые `LayerRegistry` и `RevisionFeed`, хотя
   принятый Grid route требует новый non-destructive contract. Поэтому G01 supersede-ит active clauses
   до source work.
2. `RevisionFeed.DrainAscending()` очищает общую очередь. Первый consumer забирает изменения, второй
   видит пусто. Старый API не становится основой нового Grid.
3. NearGas имеет доказанный atomic generation owner, но его read остаётся live generation-bound и не
   публикует общий commit/change batch. Grid сначала задаёт нейтральный envelope; Gas later owns adapter.
4. Historical topology change имеет atomic/replay proof только на interim coarse route. Инварианты
   сохраняются, dependency на старую модель не создаётся.
5. PlayerSense, TickInput и BodyPose — foundations, но не authoritative integer object occupancy.
6. Exact aperture defect реален: полный portal band открывается раньше aperture mask. Это отдельная
   Level/Structure defect-line, не Resolver work.
7. `VoxelImpulse` — Gas-local forced flow, а не будущий самостоятельный Wind state.
8. FishNet доставляет ordered inputs, но PeerId↔EntityId, Grid commits, topology result и Resolver
   contacts ещё не доказаны на двух peers.
9. Семь retained scenes — временные validators, не новые постоянные labs.
10. Второй real consumer больше не неизвестен: owner выбрал Wind. Реальный M3/M5 всё равно ждёт
    отдельные Wind state/simulation/adapter proofs после Grid foundation.

Если future current authority материально противоречит этому принятому смыслу, executor не выбирает
сам: он возвращает same-position checkpoint с точным конфликтом.

## 3. Exact source/legacy disposition

У каждого named surface ровно один разрешённый класс. `Replacement trigger` и rollback/removal condition
обязательны даже для сохраняемых частей.

### KEEP

**K1 — integer topology foundation.**

- Artifacts: `TopologyStableIds.cs`, `Topology/Coarse/{TopologyDocument,TopologyConformance}.cs`,
  `Topology/Ingestion/{RectDecomposition,LatticeQuantize,DoorSill}.cs` и focused conformance/overflow/
  ingestion tests.
- Evidence: stable ids, integer geometry и loud conformance уже доказаны.
- Replacement trigger: отсутствует в Grid V1; только отдельный принятый plan с эквивалентным proof.
- Rollback/removal: новый `Core/Grid` откатывается отдельно; K1 не переносится и не удаляется.

**K2 — current Gas/Structure coordinate substrate.**

- Artifacts: `Field/Voxel/{CellGrid,CellLattice,VoxelResolution,VoxelGrids}.cs`, resolution/projection tests.
- Evidence: current 50 cm Gas и 25 cm Structure согласованы целочисленно.
- Replacement trigger: отсутствует; G02 добавляет neutral contract и equivalence proof, не перенос state.
- Rollback/removal: при провале G02 удаляется только новый additive root.

**K3 — Structure-owned primitives.**

- Artifacts: `StructureGrid.cs`, `SubFaceOccupancy.cs`, `StructureGasProjection.cs`, `ApertureSpec.cs`,
  `ApertureValidationException.cs` и RL2/RL3/RL5/overflow tests.
- Evidence: Structure state, validation и static projection имеют focused proof.
- Replacement trigger: только отдельный Level/Structure plan.
- Rollback/removal: Grid читает будущий adapter; K3 не перемещает и не удаляет.

**K4 — NearGas atomic owner.**

- Artifacts: `NearGas/{NearGasSimulation,NearGasInput,NearGasDefinition,NearGasTicks}.cs` и lifecycle/
  step/L1B tests.
- Evidence: atomic step, retry/fault, generation ownership и loud stale rejection.
- Replacement trigger: отсутствует; Gas C1 later creates its typed committed adapter.
- Rollback/removal: красный adapter откатывается отдельно, NearGas остаётся.

**K5 — Character/Gas sensing foundations.**

- Artifacts: `Field/Sense/PlayerSense.cs`, `Characters/{IAuthoritativeBodyState,BodyPose}.cs` и tests.
- Evidence: actor-shaped input, exposure/dose foundation и view socket существуют.
- Replacement trigger: только Character/Gas-owned plans.
- Rollback/removal: raw Voxel sensing и float pose не становятся Grid authority.

**K6 — Program/Multiplayer transport foundation.**

- Artifacts: `Core/Sim/{ITickInputBus,InMemoryTickInputBus,TickInput}.cs`,
  `Net/FishNet/{FishNetTickInputBus,TickInputBroadcasts}.cs`, FishNet convergence tests.
- Evidence: host relay, peer roster и ordered reliable input batches существуют.
- Replacement trigger: отсутствует в Grid V1; Program расширяет edge отдельно.
- Rollback/removal: Grid не импортирует FishNet/network types; Program slice откатывается отдельно.

**K7 — Gas-local forced flow.**

- Artifacts: `Field/Voxel/VoxelImpulse.cs`, forced-flow ADR и `Field/ForcedFlow/RW*.cs`.
- Evidence: deterministic Gas corridor/fork/conservation/decay proof.
- Replacement trigger: отдельный Gas/Wind owner plan, если real Wind требует shared producer input.
- Rollback/removal: текущий Gas mechanism не выдаётся за Wind state, layer или M3 adapter.

### NO NEW DEPENDENCIES

**N1 — legacy layer registry/scheduler.**

- Artifacts: `Core/Field/Layers/**` и `tests/.../Field/Layers/**`.
- Evidence: old order/single-writer invariants полезны, но current NearGas идёт другим route; fixed LayerKey
  привязан к old Gas/Temperature world.
- Replacement trigger: G01 authority supersession + G05 generic boundary + реальные consumer migrations.
- Rollback/removal: новая ссылка на N1 — regression. Удаление только при zero consumers и green replacement.

**N2 — interim coarse far tier/read model.**

- Artifacts: `Core/Field/Coarse/**`, кроме отдельно рассмотренного `CoarseSectorGraph.cs`, и его tests.
- Evidence: current policy прямо запрещает новые dependencies и назначает removal на S4.
- Replacement trigger: отдельный S4 Gas/Program area-aware near-grid rollup.
- Rollback/removal: случайная новая dependency удаляется; N2 остаётся до green S4 replacement.

**N3 — mixed coarse topology mutation path.**

- Artifacts: `Core/Field/Coarse/CoarseSectorGraph.cs` и
  `Core/Field/Topology/Coarse/{CoarseSectorGraphBuilder,TopologyChangeSet,CoarseBreachLayer}.cs`.
- Evidence: partition/ProfileHash и atomic/replay полезны, но BandCount=2 и current proof historical.
- Replacement trigger: Level/Structure M5 и S4 owner decision выбирают retained neutral partition/replacement.
- Rollback/removal: новый Grid не импортирует types; разделение/удаление только после current replacement proof.

**N4 — seven temporary validators.**

- Artifacts: `SampleScene`, `GasSourcePhase0Demo`, `GasBuoyancyDemoScene`, `GasVoxelSandboxScene`,
  `GasVisualScene`, `GasLabScene`, `GasRoomScene` по exact paths из `legacy-lab-surface-policy.md`.
- Evidence: retained unchanged only as temporary proof fixtures; SampleScene remains default/build scene.
- Replacement trigger: real gameplay path или одна Integration Lab replaces that exact proof and is green.
- Rollback/removal: no new loader/build/Addressable/test/editor dependencies; red replacement keeps validator.

### FIX SEPARATELY

**F1 — complete documentation-authority cleanup.**

- Base and inventory: G01 сначала pin-ит exact product commit `B`. Полный tracked universe строится из
  `git ls-tree -r -z --full-tree B`, не из текущего index/working tree, и сохраняется в base-pinned
  `docs/grid-v1-authority-disposition.jsonl`. Каждый исходный path/mode/blob остаётся строкой ledger.
- Stable identity and references: rename сохраняет исходный `source_id`; split создаёт child ids со ссылкой
  на parent; tracked deletion оставляет tombstone. Единственная нормативная reference grammar — explicit
  `gridref:<source_id>#<clause_id>` в machine-readable полях; literal path/blob служат проверяемой identity.
  Свободный, dynamic или неоднозначный reference не угадывается: он получает `unknown` и блокирует G01.
- Ambient inputs: ignored, untracked, generated, archive-disposed и Git-history bytes не объявляются
  отсутствующими по clean status. Grid session законна только в input-isolated venue, который на уровне
  доступа показывает разрешённый current tree/corpus, deny-ит эти классы и выдаёт read/deny receipt.
  Prompt prohibition, отсутствие citation или обычный clean worktree не считаются proof. Если такой fence
  нельзя доказать, G01 остаётся blocked.
- Disposition: каждый старый normative document/section получает ровно один `archive-with-proof` или
  `tracked-delete`. Archive законен только при literal inventory, stable ledger и фактическом input denial;
  иначе item удаляется из current tree обычным tracked commit. Невозможная lawful deletion блокирует G01
  и держит G02 закрытым. Git history сохраняется без rewrite/prune, но Grid venue не получает его как input.

**F2 — exact aperture.**

- Artifacts: exact-aperture branch of `StructureVoxelizer.cs` и preserved-paused aperture records.
- Evidence: portal band opens first, aperture OR cannot narrow it.
- Replacement trigger: fresh V31 Level/Structure admission.
- Rollback/removal: own red/green proof and rollback; G05/G08 do not touch or claim repair.

### DELETE AFTER REPLACEMENT PROOF

**D1 — destructive Grid event family.**

- Artifacts: `Core/Field/Events/{IGridEventBus,RevisionFeed,GridEvent}.cs`, `RevisionFeedTests.cs` и direct
  calls including `TemperatureLayer.DrainAscending()`.
- Evidence: first reader empties the common queue.
- Replacement trigger: G01 supersession + green G04 immutable journal/cursors + fresh reference inventory +
  migration of every surviving consumer.
- Rollback/removal: until all four hold, D1 stays quarantined. Red G04 removes only new code. Later deletion
  requires zero consumers and normal gates; dual-authority shim is forbidden.

Four purge families already absent at the observed product revision are not reintroduced as candidates.

## 4. Eleven future Grid-owned roots

Future production root: `Assets/GasCoopGame/Core/Grid/**`, namespace `GasCoopGame.Core.Grid`.
Focused tests: `tests/GasCoopGame.Core.Tests/Grid/**`. Existing Core assembly remains; no speculative
framework/assembly. Every leg is one cohesive outcome and ≤ one focused half-day. If fresh execution
cannot fit, it checkpoints/splits implementation of the same outcome without expanding ownership.

### G01 — Complete documentation-authority cleanup

- Phase boundary: pre-G01 Direction planning/correction/review pin-ят exact accepted-plan blob и receipts;
  ещё не существующий corpus им не требуется. Первый G01 bootstrap pin-ит этот plan/review, product `B`,
  fixed output paths и bootstrap identity, но не future manifest/blob/bundle, которые сам должен создать.
  После принятого G01 product execution законен только с exact уже существующим corpus receipt.
- Outcome and non-self identity: G01 создаёт один `Grid V1 Current Authority Corpus` с fixed manifest
  `docs/grid-v1-current-authority.json` и fixed ledger
  `docs/grid-v1-authority-disposition.jsonl`. Manifest не включает себя или ledger в `members` и не хранит
  собственный blob/corpus id. Это ровно два mechanically checked control-file exceptions; третье исключение
  или self-entry — RED. Отдельный binding Direction review внешне pin-ит product commit, оба fixed paths/
  blobs и вычисленный из canonical manifest `corpus_id`; следующий CALL несёт этот exact receipt.
- Exact initial members после закрытия G01:
  `AGENTS.md`; `Assets/GasCoopGame/Core/AGENTS.md`; `validation.config`;
  `openspec/specs/sim-core/spec.md`;
  `docs/adr/ADR-P-0015-c-exec-grid-v1-g01-document-authority-001-current-grid-authority.md`;
  `openspec/changes/c-exec-grid-v1-g01-document-authority-001/PLAN.md`, `proposal.md`, `tasks.md` и
  `specs/sim-core/spec.md`. Во время cleanup старые материалы доступны только как fenced disposition
  evidence, не как requirements/method.
- Lifecycle: corpus-authoring CALL pin-ит существующий corpus и объявляет только будущие output paths.
  Лишь отдельный CALL после фактического создания, owner acceptance и fresh review pin-ит resulting bundle
  paths/blobs для execution. Ни один CALL не обязан назвать identity собственного будущего output.
- Inventory/disposition: ledger покрывает весь F1 base universe, candidate additions, explicit `gridref`
  edges и rename/split/delete lineage; zero missing, duplicate, ambiguous или `unknown`. Current source/tests
  могут быть cited только как `product_fact`, не как documentation authority. Каждый legacy normative item
  имеет ровно один archive/delete disposition; скрытая historical normative section запрещена.
- Mechanical proof: `tools/grid-document-authority-check.ps1`, self-test и wiring в normal check,
  PlanPublication и Deliver проверяют manifest/receipt identity, paths/blobs, ledger completeness,
  `gridref` grammar, declared citations и input-fence receipt. Они не утверждают citation relevance,
  proposition entailment или семантическое отсутствие legacy meaning.
- Semantic proof: отдельная fresh session проверяет current-only смысл и пытается протащить (a) valid, но
  нерелевантную allowlisted citation с unsupported тезисом, (b) paraphrased legacy clause без stale имени и
  (c) ignored/history input. Первые два обязаны дать semantic `refuted`, третий — mechanical denial/RED;
  до общего binding `could-not-refute` G01 не закрыт.
- Conflict: G01 может менять только documentation, OpenSpec, root/Core repo authority,
  `validation.config`, checker/input-fence proof и wiring существующих gates. Никаких `.cs`, Unity assets,
  gameplay tests, Grid production root или изменения K/N/F2/D mechanics.
- Rollback: публикация атомарна. Любой RED отменяет принятие G01 и держит G02 закрытым. Непроверяемый
  archive item получает tracked deletion, после чего inventory/proof/refutation повторяются. Если lawful
  deletion пока невозможен, G01 остаётся blocked; старая authority не становится допустимой. Git history
  сохраняется без rewrite/prune.
- Removal trigger: none; current corpus и guard остаются maintained authority, а G02 закрыт до принятой,
  опубликованной и binding-reviewed G01 cleanup.

### G02 — Common spatial map

- Outcome: integer base lattice, positive integral scale, address, half-open region and canonical projection;
  current 25 cm/50 cm paths have equivalence tests without state transfer.
- Proof: round-trip, negative coordinates, boundaries, overflow, projection, canonical enumeration, invalid-scale rejection.
- Conflict: new `Core/Grid/Addressing/**` and tests; current Voxel/Structure read-only.
- Rollback: remove additive G02.
- Removal trigger: none.

### G03 — Committed moment

- Outcome: engine-free commit stamp and immutable committed snapshot token; live/mid-tick state is unreadable.
- Proof: atomic publish, failed candidate leaves old stamp, stale/future/foreign rejection, deterministic digest.
- Conflict: new `Core/Grid/Commit/**`.
- Rollback: remove G03, keep current owners.
- Removal trigger: historical coarse types remain; only invariants move into tests.

### G04 — Multi-consumer change delivery

- Outcome: immutable ordered batches, independent cursor per subscription, explicit retention floor and loud lag failure.
- Proof: two readers at different cadence see same batches; neither steals; retry/order/gap cases deterministic.
- Conflict: new `Core/Grid/Changes/**`; old Events unmodified.
- Rollback: remove G04 and keep D1.
- Removal trigger: D1 becomes eligible only after all consumers migrate and G11 inventory is zero.

### G05 — Generic Layer↔Layer committed read boundary

- Outcome: opaque stable layer key, typed committed reader and consumer-owned subscription; Grid never runs layer behavior.
- Proof: two test-only synthetic layers with different payloads/scales; explicit commit delay; stale/live/type mismatch rejected.
- Conflict: new `Core/Grid/Layers/**` and test-only SyntheticLayerA/B; no Water/Wind production placeholder.
- Rollback: remove G05 and fixtures.
- Removal trigger: N1 only becomes a later candidate; synthetic proof is not M3.

### G06 — Object registration and spatial index

- Outcome: owner-supplied stable object key, committed integer footprint/interests and spawn/update/teleport/despawn index.
- Proof: lifecycle atomicity, dedupe, reindex, interest update, stale rejection, changed-region query without world scan.
- Conflict: new `Core/Grid/Objects/**`; PlayerSense/TickInput/BodyPose unchanged.
- Rollback: remove G06.
- Removal trigger: none; Character later supplies real adapter.

### G07 — Resolver path A: object moved

- Outcome: canonical contact cache and exactly one ordered enter/change/exit delta from object movement.
- Proof: enter-change-exit, teleport, overlap dedupe, idempotence, order invariance; no gameplay consequence.
- Conflict: new `Core/Grid/Resolver/**`.
- Rollback: remove G07, keep G06.
- Removal trigger: focused fixtures consolidate only after G09 coverage absorbs them.

### G08 — Resolver path B: layer changed under static object

- Outcome: dirty layer regions query only interested indexed objects and produce the same contact semantics.
- Proof: equivalence with G07, no world scan, no theft/duplicates, canonical merge of same-commit causes.
- Conflict: same Resolver root, strictly after G07; layer behavior unchanged.
- Rollback: revert G08 path, keep object-move path.
- Removal trigger: none.

### G09 — Universal deterministic proof

- Outcome: SyntheticLayerA/B with different scales/data prove both generic paths independent of input order.
- Proof: permutation/property/negative controls, equal commit/change/contact digests, stale/live rejection and mutation control.
- Conflict: tests only.
- Rollback: production G02–G08 stays; red proof routes correction, never consumer workaround.
- Removal trigger: duplicated focused fixtures consolidate into universal suite; synthetic layers remain test-only.

### G10 — Stress and hot-path proof

- Outcome: internal deterministic work counters and focused stress harness measure changed regions/moved objects/candidates.
- Proof: untouched world growth does not change work counters for fixed delta; counters, allocations and elapsed observation recorded.
- Conflict: Grid diagnostics/stress tests; no new benchmark framework.
- Rollback: remove diagnostics if overhead/API leaks.
- Removal trigger: temporary timing harness only after equivalent maintained performance gate; counters remain regression evidence.

### G11 — Retirement readiness + handoff pack

- Outcome: fresh exact inventory, every removal trigger/rollback, five consumer handoffs and one existing-dashboard Grid section.
- Proof: zero ambiguous dispositions; not-yet-migrated legacy remains; synthetic/real acceptance stays separate.
- Conflict: Grid docs/tests inventory and Direction render through valid RESULT only.
- Rollback: restore prior ledger/dashboard section; source authority unchanged.
- Removal trigger: this pack itself authorizes no deletion; each named owner later needs green replacement + zero consumers.

## 5. Sequence, sessions and conditional parallelism

```text
G01 → G02 → G03 → G04
                    ├─ G05
                    └─ G06 → G07
G05 + G07 + G04 → G08 → G09 → G10 → G11
```

- G01–G04 are strictly serial.
- Each G-leg is a separate fresh product root/session lineage and receives separate fresh refutation evidence;
  owner presence is required only for a real decision/change, not routine mechanics.
- Current direction knowledge still says one mutating Core leg at a time. Therefore G05 and G06→G07 may be
  planned in parallel, but concurrent BUILD is forbidden until an explicit post-G04 launch disposition proves:
  separate clean worktrees, disjoint production/tests surfaces, shared G01–G04 files read-only, no shared project/
  spec file, serialized merge, rebase + full checks after the first merge, and independent review per branch.
- Any discovered shared write stops parallelism; work continues serially. Quality gates never reduce; only possible
  rework is accepted as the cost of speculative overlap.
- A previous leg's fresh review may pipeline with preparation of the next, but no dependent result is merged or
  declared complete before its required predecessor close.
- Consumer internal work that does not freeze shared adapter signatures may continue separately. Gas/Wind adapter
  planning starts only after G05 freeze; real acceptance cannot close before G09 and their own proofs.

## 6. No-drift execution control

The global TREE keeps one outcome node `Grid / Layers / World Change`; the eleven legs are an execution ladder,
not eleven strategic goals. Durable control is:

1. this accepted plan is the complete route and is never silently overwritten;
2. NOW exposes only the currently lawful root/children;
3. every RESULT is saved verbatim in history and committed;
4. the existing dashboard renders current phase/leg/handoffs/blockers, but is not authority.

Before G01, Direction planning/review CALLs cite this accepted plan blob and the current correction/review receipts;
they do not name a corpus that does not exist. The G01 bootstrap CALL also pins product `B` and fixed output paths,
but not future blobs. After an artifact exists, owner acceptance and fresh review externally pin its exact corpus/
bundle receipt; only then may an execution CALL cite those existing identities. A later corpus-authoring CALL cites
the prior corpus and declared output paths, never the identity of its own future output. Consumed CALL ids never relaunch.

Authority order before G01 is current product hard rules/facts → accepted Direction plan/review → current bounded
CALL. After G01 it is current product hard rules/facts → externally pinned current corpus → accepted Grid meaning →
closed predecessor identities → current bounded CALL. Historical PLAN/CALL/ADR/dashboard/result/review and Git
history remain evidence only and are not exposed as requirements/method without the proved input fence.

At every start: phase-valid identity, dependency close, old-CALL non-relaunch, clean venue/conflict and input-fence
checks run. Mechanical gates own only paths/blobs/ledger/reference/citation-presence/access proof. Separate fresh
refutation owns relevance, entailment, current-only meaning and paraphrased legacy. A builder cannot amend plan,
corpus, ledger or repo authority. Any such change needs a separate owner-present artifact, exact owner words and
fresh review. If actual archive/input isolation cannot be proved, tracked deletion is mandatory; Git history remains
intact but fenced.

The earlier master-plan statement «second consumer unknown» is superseded only by the later owner choice Wind.
All other accepted master-plan ownership and gates remain unchanged.

## 7. Named handoffs and real acceptance

**Gas:** owns NearGas adapter, gas simulation/values/sources/reactions/forced flow/consequences. It may be the first M3 consumer.

**Wind:** owner-selected second real consumer after foundation. It must be a separate state/simulation/read adapter,
not a rename of Gas `VoxelImpulse`. Grid creates no Wind placeholder. Wind later returns real M3 adapter proof and,
for M5, its own meaningful reaction to committed topology change. If Wind design cannot honestly consume this seam,
the owner revisits the choice; synthetic or Gas-local evidence cannot substitute.

**Character:** owns stable entity identity, committed integer footprint/interests/lifecycle and gameplay reaction.
View/Transform is not authority. Object proof is M6, not a second M3 layer.

**Level/Structure:** owns state, topology commands/results, destruction/migration intent and separate exact-aperture repair.

**Program/Multiplayer:** Grid supplies canonical commit stamp, immutable-change digest and ordered-contact digest.
Program owns session/peer identity, PeerId↔EntityId, input/order, initial state and two-peer harness. Co-op-ready is
forbidden until two peers receive the same inputs/topology/object/layer changes and match all Grid outputs/final result.
If identity + existing input edge + one two-peer proof cannot fit one bounded Program slice, or needs multiple roots,
new session lifecycle/reconnect/late-join, transport replacement, state replication/reconciliation or authority change,
it returns to a fresh Direction map decision for a separate Multiplayer track.

**Integration:** accepts only closed M3/M5/M6 drops, invents no adapter, remains one permanent Lab and cannot claim
co-op-ready before the Multiplayer gate.

Acceptance:

- Grid internal ready = G01–G11 on synthetic layers; not M3.
- M3 = real Gas + real Wind adapters through the common boundary.
- M5 = real Level/Structure change + own reactions from Gas and Wind.
- M6 = Character authoritative footprint + contact/reaction proof.
- Multiplayer gate = two-peer equality of commit/topology/change/contact/final results.
- Integration co-op-ready = M3/M5/M6 plus Multiplayer gate.

## 8. Dashboard, cuts, risks and next handoff

Only one Grid section is maintained in the existing owner dashboard: current phase, next leg, external handoffs
and blockers. No separate render. Current product progress is **0/11 Grid legs launched**; accepted planning and review
are not implementation credit.

Cuts: no Water; no current Wind implementation; no Gas/Character/Loot behavior; no aperture repair; no network/session
code in Grid; no Integration scene; no speculative framework; no mass legacy deletion.

Main risks and controls: authority conflict → G01; destructive reads → new G04; dual authority → no shim; Resolver
scope creep → contacts only; synthetic mistaken for real → separate labels; hidden world scan → G08/G10 counters;
local determinism mistaken for co-op → mandatory Program gate; leg too large → same-outcome checkpoint/split.

Next planning handoff after this owner-approved correction: exactly one newly issued fresh independent Direction
review of the exact corrected-plan blob and the three negative-control classes above. Consumed
`c-review-grid-v1-executor-plan-001` and refuted `c-review-grid-v1-document-authority-amendment-001` never relaunch.
The review opens no product/engineering root. Only its binding `could-not-refute` may later route a separate
owner-present launch-control disposition for possible G01; another refutation stops this correction chain instead
of automatically opening correction-003.

## 9. Explicit not-run list

Not run/created: product mutation; product branch/worktree/root; Unity; tests/build/benchmark/Deliver; remote fetch/push;
Gas/Water/Wind/Character/Loot/damage/dose/balance/presentation implementation; real adapters/fixtures; exact aperture;
multiplayer runtime/two-peer run; Integration Lab; separate dashboard; BUILD, PAIR-CANDIDATE or engineering CALL.

END_OF_FILE: live/indie-game-development/work/grid-v1-executor-plan.md
