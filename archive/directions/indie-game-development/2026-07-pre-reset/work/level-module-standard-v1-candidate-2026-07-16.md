# Level / Module Standard v1 — owner-accepted architectural basis

status: OWNER-ACCEPTED ARCHITECTURAL BASIS / D1=A / D2=A / LV0 PLAN ROUTED PARALLEL / NOT BUILD AUTHORITY
date: 2026-07-16
session: s-research-level-module-standard-v1-001
accepted: 2026-07-16 by owner; recorded by s-repair-level-module-standard-v1-owner-acceptance-001
lv0_plan_routed: 2026-07-16 by owner; c-exec-level-module-standard-v1-lv0-plan-001
owner_verdict: |
  «Кандидат Level/Module Standard v1 принимаю как архитектурную основу. D1=A, D2=A. Canonical encoding,
  shared-surface ownership, socket terminal states, transform rules, deterministic build input,
  registries/versioning, sampler authority и size/time ceiling должны быть явно заморожены в owner-approved
  LV0 PLAN. Это не разрешение на BUILD»
scope: project-owned level/module contracts, normalization and validation; LV0 product PLAN routed in parallel; no Unity/source/test/asset mutation and no BUILD authority
lv0_freeze_required: canonical encoding; shared-surface ownership; socket terminal states; transform rules; deterministic build input; registries/versioning; sampler authority; size/time ceiling

## 0. Короткий вывод

У проекта уже есть нижняя generator-neutral граница — integer topology, voxel admission, aperture vocabulary и typed
feature pattern — и доказан узкий PGG static prefab → SnapGridFlow → built-scene reader мост. Не существует верхней
project-owned платформы, которая определяет, что такое допустимый reusable module и что такое допустимый собранный
level. Поэтому Standard v1 должен добавить ровно две нормализованные authority, не переписывая нижние seams:

1. **Project Module Contract** — reusable, technology-neutral правда одного module type до композиции.
2. **Built Level Manifest** — project-owned нормализованная правда конкретной собранной level instance после любой
   композиции и до существующих topology/voxel/feature consumers.

Владелец принял этот целостный shape как **архитектурную основу** и выбрал D1=A / D2=A. Это не превращает
предложенные имена полей, byte encoding, registry/version rules или implementation split в уже замороженный product
spec: точные code-facing решения перечислены в `lv0_freeze_required` и обязаны получить отдельное owner approval в
LV0 PLAN. Позднейшая явная инструкция владельца выпустила ровно один параллельный LV0 PLAN CALL; она по-прежнему
не разрешает BUILD.

## 1. Current-truth inventory

| Класс | Current truth | Основание |
|---|---|---|
| established | Владелец выбрал clean route A: technology-neutral full-3D contract + validators → DA/PGG adapters → production content. | `work/level-platform-phasing-2026-07-11.md` (`status: owner-ratified`, Ratified verdict); `work/poligon-m1-integration-route.md` §5 LV0–LV5. |
| established | Нижняя engine boundary уже generator-neutral: `TopologyDocument`/`ITopologyProducer`, integer X/Y/Z, `Voxelizer`, `TopologyConformance`, 50 cm gas lattice, 25 cm structure truth и `ApertureSpec`. | `work/level-platform-phasing-2026-07-11.md` §§What is already genuinely generic, Vertical levels; `knowledge/g9c41-da-level-ingestion-plan.md` §§3 lanes, Lockstep determinism. |
| established, bounded | `GasSourceSpec` — полезный typed-feature pattern вне `TopologyDocument`; marker discovery/canonical sorting — generator-blind pattern. Это не заявляет доставленной Phase 0 или полного source pipeline. | `work/level-platform-phasing-2026-07-11.md` §§What Phase 0 actually does, What is already genuinely generic, Extensible items. |
| established, bounded | PGG может editor-time испечь dependency-free static prefab, DA SnapGridFlow может собрать его, а reader — прочитать. Production module pipeline остался `FAIL_STAGE` из-за отсутствия project contract. | `history/2026-07-11-s-spike-pgg-001-close-001.md` outcome/evidence; `work/pgg-analysis-2026-07-10.md` verdict/pipeline. |
| established | Module — placement/bake container; logical room/region — topology/gas unit. Один module обязан допускать 1:N rooms, в том числе на разных Z; connections/apertures выражаются на ±X/±Y/±Z. | `work/level-platform-phasing-2026-07-11.md` §§Vertical levels and compound modules; CALL standing owner inputs. |
| established | DA владеет runtime composition; PGG владеет только editor-time population/bake; hand-authored modules — control; vendor/library input обязан нормализоваться до consumption. | `work/level-platform-phasing-2026-07-11.md` §DA and PGG are not symmetric adapters; `work/poligon-m1-integration-route.md` track 2. |
| historical evidence | `DaLevel`, `IDaRoomReader`, `DaTopologyProducer`, renderer-AABB rooms, empty anchors и current aperture validation показывают полезные seams и конкретные потери, но не являются Standard v1. | `work/level-platform-phasing-2026-07-11.md` §§What is already genuinely generic, What the old Phase 1 intended. |
| obsolete authority | Старый `Lv-ingest`/Phase 0 не доставлен и никогда не возобновляется. Его source/quantization ideas — evidence only. | `work/c-exec-lv-ingest-phase0-call.md` banner; `history/2026-07-12-s-repair-near-gas-program-routing-001.md` outcome/state_changes. |
| obsolete authority | `c-exec-level-platform-phase1-plan-001` нельзя выпускать: он ждёт невозможный `Phase 0 MERGED`, несёт v19/13-leg/lane-D assumptions. Его detailed requirements остаются evidence. | `work/c-exec-level-platform-phase1-plan-001-call.md` banner; `work/poligon-m1-integration-route.md` §§7–8. |
| current dispatch truth | Фраза текущего research CALL про fresh v21 + verified lane-D описывает прежний gate. Current committed product protocol — v26/product-owned venue admission; Direction больше не назначает physical path/branch/SHA. | `work/gascoopgame-worktree-protocol-v2.md` §§Разделение authority, Product delivery; current `NOW.md`. |
| missing | Нет authoritative Project Module Contract, Built Level Manifest, typed WHERE/WHAT catalog, module/adapter/built-level validators, independent exact-geometry proof и accepted fixture suite. | `history/2026-07-14-s-research-level-module-contract-recovery-001.md` outcome/evidence; `work/level-platform-phasing-2026-07-11.md` §§Two contracts, Validation platform. |

## 2. Standard v1 invariants — candidate

1. Authority всегда project-owned; `sourceKind`/vendor ids — только provenance.
2. Любой producer нормализуется до Project Module Contract, а любая композиция — до Built Level Manifest до engine
   consumption.
3. Все authoritative coordinates integer full-3D; float/Unity transforms остаются по producer-side границе.
4. Module никогда не равен room; root/prefab count никогда не определяет room count.
5. Coarse envelope не заменяет exact structure; portal declaration не заменяет independently observed aperture.
6. Structural truth отделена от gameplay payload; WHERE отделено от WHAT.
7. Unknown authoritative kind — loud rejection. Ignore разрешён только в отдельной cosmetic-only области.
8. Same normalized input даёт byte-identical canonical ordering, ids и hashes независимо от producer.

## 3. Общие размеры и нормализация — candidate

| Правило | Standard v1 candidate |
|---|---|
| Structure/placement unit | `1 structure unit = 250 mm`; pivot, envelope, floors, sockets, clearance, occupancy, apertures, anchors и instance translation лежат на этой lattice. |
| Gas lattice | `1 gas cell = 2×2×2 structure units = 500 mm`; conversion использует математический floor division, включая отрицательные координаты. |
| Contract axes | Right-handed `X/Y/Z`, где `Z = up`; Unity adapter recommendation: contract X ← world X, contract Y ← world Z, contract Z ← world Y. Mapping живёт в adapter profile, не в Core/vendor metadata. |
| Bounds | Все integer AABB — `[minInclusive, maxExclusive)`; zero/negative extent запрещены. Coarse bounds не участвуют как exact occupancy. |
| Local frame / pivot | Один declared module-local frame; `pivot: Int3` обязан быть grid-aligned и лежать в/на declared envelope. Placement содержит integer world translation pivot и legal rotation. |
| Floor datums | Stable `floorDatumId + zPlane` в structure units; room ссылается на 0..N datums. Datum — semantic level, не mesh bounds. |
| Legal rotations | V1 default: ровно yaw quarter-turns `{0°,90°,180°,270°}` вокруг +Z; no reflection, no scale, no arbitrary float rotation. ±Z sockets не требуют переворачивать module. Расширение orientation set требует schema/profile revision. |
| Local→world | `world = placementTranslation + R_yaw(local - pivot)`, только integer matrix. Planes/normals/orientations преобразуются той же матрицей; потом arrays canonical-sort. |
| Canonical ordering | Sort by stable project ids, затем integer placement/plane/coordinates; hashes считаются по versioned canonical bytes, не по Unity object order, asset path или vendor ids. |

## 4. Authority A — Project Module Contract

### 4.1 Field matrix — candidate

| Поле | Смысл и ownership | Author/derive/validate |
|---|---|---|
| `schemaVersion`, `profileId` | Project standard и normalization profile versions. | authored by project; exact supported version required. |
| `moduleId`, `moduleRevision` | Stable project identity одного reusable module type; не prefab GUID/path/vendor id. Revision immutable для canonical content. | authored; uniqueness/version transition validated. |
| `authorityOwner` | Fixed project namespace/team owner; producer не может заменить. | authored; allow-list. |
| `sourceProvenance` | `hand | pgg-bake | library-import | future`, tool/version/receipt refs. Не authority и не semantic fallback. | derived; excluded from semantic decisions. |
| `frame` | Unit/profile, axes, pivot, envelope, floor datums, allowed rotations. | authored; grid/orientation/containment validated. |
| `connectivityRole` | Typed project role such as endpoint/pass-through/junction/hub; не выводится из vendor socket count. | authored; role/socket rule validated. |
| `rooms[]` | `localRoomId`, coarse envelope, floor-datum refs, exact-structure refs; 1..N. | semantic data authored; ids/containment/overlap relationships validated. |
| `expectedStructure` | Canonical sparse occupied 25 cm cells + occupied boundary sub-faces by room; irregular geometry сохраняется без AABB fill. | project-authored/frozen normalized expectation; independently re-observed. |
| `internalConnections[]` | Stable id, room A/B, six-face plane+normal, portal profile/version, exact expected aperture, two-sided clearance. | authored; shared-boundary/room ownership/geometry validated. |
| `externalSockets[]` | Stable id, **owningRoomId**, module-boundary plane+normal, typed role/capacity, portal profile/version, exact expected aperture, inside/outside clearance. | authored; boundary, owner room, count/profile/clearance validated. |
| `anchors[]` | WHERE: stable local id, owningRoomId, integer pose/orientation, footprint/clearance, anchor schema. | authored; containing room/cell/orientation validated. |
| `featureSpecs[]` | WHAT: typed/versioned project feature record referencing one anchor; e.g. GasSource later Item/PlayerSpawn/Machine/Valve/Loot. | authored; one feature validator per type; unknown authority fails. |
| `authorityTags[]` | Stable ids from project tag registry; classification only, no arbitrary key/value payload. | authored; closed registry validation. |
| `populationZones[]` | PGG/editor population allow-zones tied to a room, plus category policy; never overlaps structural/socket/portal clearance. | authored; geometry and clearance validated. |
| `breachSurfaces[]` | Stable refs to exact occupied faces plus typed breach spec ref; declares eligibility/meaning, not arbitrary destruction. | authored meaning; observed face support validated. |
| `cosmeticAnnotations[]` | Explicit non-authoritative namespace; ignored by Core and excluded from semantic hash. | optional; any reference from authority is an error. |
| `canonicalModuleHash` | Hash of versioned authoritative fields only. | derived after validation; recomputed independently. |
| `bakeReceipt` | Producer/tool/seed/input/output/cleanup/dependency-scan evidence. | derived provenance; never substitutes contract fields. |

### 4.2 1:N rooms and six-face connections

Hierarchy is load-bearing:

```text
ModuleType/moduleId
  Room/localRoomId [1..N]
  InternalConnection/localConnectionId: room↔room
  ExternalSocket/localSocketId: module boundary → owningRoomId
  Anchor/localAnchorId: owningRoomId + exact local pose
```

Connection plane = `{axis: X|Y|Z, sign: -|+, coordinate, tangentBasis, exactAperture}`. Internal vertical connection
between stacked rooms uses ±Z, exactly like an external vertical socket; it is not coerced into a wall portal. Portal
profile is project-owned typed compatibility (`profileId + version + role/capacity`) while `exactAperture` carries
the real 25 cm opening rectangle/mask. Profile compatibility never proves the physical hole by itself.

Stable hierarchy:

- `roomKey = moduleId/moduleRevision/localRoomId`;
- `connectionKey = moduleId/moduleRevision/localConnectionId`;
- `socketKey = moduleId/moduleRevision/localSocketId`;
- later global ids prefix these local ids with one deterministic module instance id.

### 4.3 Coarse versus exact physical truth

| Fact | Authored truth | Derived observation | Independent validation |
|---|---|---|---|
| Module/room envelope | Coarse project AABB, used for containment, broad topology and diagnostics. | Bounds may be measured only as a check. | Exact occupancy must fit; AABB is never expanded into filled structure. |
| Exact occupancy | Frozen canonical sparse 25 cm cell/sub-face expectation per room. | Separate sampler derives observed cells/faces from designated project structural geometry/colliders after bake. | Expected = observed; planted missing/extra cell must fail. Irregular voids remain voids. |
| Exact aperture | Portal/socket declares plane, profile and exact opening mask/rect. | Independent sampler observes open faces in built structural truth. | Position, size, plane and owning rooms match; whole Door-kit bounds are inadmissible evidence. |
| Clearance | Socket/portal/population zones declare empty volume. | Built geometry, props and anchors are sampled. | Any structural/cosmetic/PGG object in forbidden clearance fails with subject path. |
| Breach-ready surface | Typed project declaration references exact faces. | Structural sampler confirms faces are occupied/exposed. | Missing support, overlap with portal or room ambiguity fails; runtime destruction remains cut. |
| Anchor ownership | Author names owning room and integer pose. | Resolver computes containing exact room/cell. | Declared owner must equal resolved owner; boundary ambiguity fails loudly. |

The exporter that freezes `expectedStructure` and the registration validator that derives `observedStructure` must be
separate proof paths with planted negative fixtures; reusing one cached result twice is not independent validation.

## 5. Authority B — Built Level Manifest

### 5.1 Field matrix — candidate

| Поле | Нормализованная правда |
|---|---|
| `schemaVersion`, `profileId`, `levelId` | Project-owned manifest/profile identity. |
| `buildKey` | Explicit deterministic build input (seed/scenario key); not an implicit Unity/PGG RNG state. |
| `producerProvenance` | Hand/DA/future producer and receipts, non-authoritative. |
| `canonicalInputs[]` | Exact module ids/revisions/hashes and normalized placements, canonical-sorted. |
| `moduleInstances[]` | `instanceId`, module identity/hash, integer translation, legal yaw, provenance. Same normalized tuple twice is overlap/error. |
| `regions[]` | Flattened logical rooms with `globalRoomId = instanceId/localRoomId`, coarse world envelope and exact structure refs; module provenance retained. |
| `connections[]` | Internal connections retained; paired external sockets become resolved links. Every link keeps two room ids, plane/profile and exact aperture. |
| `exactStructure` | Canonical world-space occupied cells/sub-faces, apertures and breach-ready face refs; overlaps and gaps already rejected. |
| `anchors[]` | Global ids `instanceId/localAnchorId`, resolved global room/cell and integer world pose. |
| `featureSets[]` | Typed/versioned WHAT records referencing global anchors; no vendor object or universal payload bag. |
| `authorityTags[]` | Project registry ids after normalization. |
| `manifestHash` | Versioned canonical semantic bytes; same input twice must match. |

`instanceId` candidate formula is a project hash/key over `(levelId, moduleId, moduleRevision, translation, yaw)`;
two instances cannot occupy the same normalized tuple, so no producer ordinal or runtime GUID is required. Diagnostics
are a separate `ValidationReport` with source paths/provenance and are not smuggled into semantic hash.

### 5.2 Conversion into proven lower seams

| Manifest view | Existing/lower consumer | Boundary rule |
|---|---|---|
| Regions + adjacency + coarse volumes | `TopologyDocument` / `ITopologyProducer` | Project projection only; no DA/PGG/Unity types. Module provenance may be diagnostic, never topology authority. |
| Exact supported connection openings | `ApertureSpec[]` | Preserve exact 25 cm position/size. No full-boundary or Door-kit-bounds substitution. |
| Exact structure cells/faces | `Voxelizer` / `StructureGrid` seam | Fresh product PLAN verifies the current API. If an adapter is needed for sparse masks, it lives at this project boundary and does not weaken the manifest. |
| Typed gas features | `GasSourceSpec[]` pattern | Feature-specific projection; gas mass stays outside topology identity. Other feature types get separate consumers. |
| Projected engine document | `TopologyConformance` then voxel admission | Existing engine gate remains final lower rejection; it does not replace module/built-level validators. |
| ±Z aperture while lower engine still lacks support | explicit engine diagnostic | Manifest/module validation may be GREEN, but engine admission returns `ENGINE_UNSUPPORTED_Z_APERTURE`; silent drop or wall coercion is forbidden. |

## 6. WHERE versus WHAT

| Layer | Contains | Does not contain |
|---|---|---|
| `Anchor` (WHERE) | stable id, module+room owner, integer local/global pose, orientation, cell/footprint/clearance, schema version | item kind, gas mass, machine rules, arbitrary vendor dictionary |
| Typed `FeatureSpec` (WHAT) | stable feature id, typed kind+schema, anchor ref, kind-specific validated payload | geometry truth, implicit position, unversioned `object` payload |
| `AuthorityTagId[]` | closed project registry ids used for validated classification | arbitrary values or vendor strings interpreted by Core |
| `CosmeticAnnotations[]` | explicitly non-authoritative hints; ignored and excluded from semantic hash | anything referenced by topology, simulation, spawn, breach or gameplay authority |

Unknown authoritative anchor/feature/tag kind fails at module registration and again at manifest validation. Unknown
cosmetic data may be ignored only when it resides in the explicit cosmetic collection and no authoritative record
references it.

## 7. Producer responsibility map

| Actor | Owns | Must not own | Normalized output |
|---|---|---|---|
| Project standard | schema/profile, lattices/axes, ids, room graph, portal profiles, structural representation, typed feature registry, validators | vendor workflow or runtime layout choice | both authorities and validation reports |
| Hand-authored path | project geometry + project metadata; reference/control fixtures | exceptions unavailable to other sources | Project Module Contract directly |
| Dungeon Architect SnapGridFlow | runtime selection, placement and external composition by seed/build key | internal room graph, exact occupancy, feature meaning, project ids | normalized instance placements → Built Level Manifest |
| PGG | editor-time population inside `populationZones` | runtime generation, sockets/room graph, authority tags/features, connection clearance | dependency-free static project prefab → Project Module Contract |
| Future/library importer | one-way import and provenance | raw vendor metadata reaching Core or special-case engine path | contract or loud rejection/wrapper outside authority |
| Existing engine | normalized topology/structure/features admission and simulation | prefab/module validity or vendor interpretation | accepted engine documents/grids |

### PGG bake policy

1. PGG receives project-owned zones, kits and exclusions; it cannot redefine rooms, sockets, portals, anchors or
   breach semantics.
2. Bake output is a static prefab with project components/geometry only. PGG/GridPainter/runtime scripts, hidden data,
   editor callbacks and vendor asset references are removed or flattened; no PGG package is required to load it.
3. Post-bake cleanup runs before contract export. Dependency scan, forbidden-component scan and zone/clearance geometry
   comparison are mandatory; a `bakeReceipt` records tool version, recipe/seed, input and output hashes.
4. The cleaned result passes the same ModuleValidator as the hand-authored control. A PGG-specific PASS cannot bypass
   project validation.
5. DA later registers/composes only the accepted project module; it never sees live PGG state.

## 8. Four-boundary validation matrix

Every diagnostic has stable `code`, `boundary`, `subjectPath`, human sentence, `expected`, `actual`, producer
provenance and one actionable hint. Stack traces or vendor object names alone are not owner-readable diagnostics.

| Boundary | Required checks | Planted refutations / example codes | Passing evidence |
|---|---|---|---|
| 1. Module registration | versions/ids; 25 cm alignment; pivot/envelope/floors/rotations; 1:N rooms; role/socket counts; owning room; six-face planes; internal shared boundary; exact expected=observed structure/apertures; clearance; anchors/features/tags; breach support | off-grid pivot `MOD_GRID_OFF`; duplicate room id; missing socket owner `MOD_SOCKET_ROOM_MISSING`; AABB-fill irregular void; shifted aperture `MOD_APERTURE_MISMATCH`; prop in clearance; unknown authority kind | canonical contract + hash; readable zero-error report; each negative trips its intended code |
| 2. Adapter/bake conformance | hand control equivalence; no field loss; producer transforms normalize exactly; PGG zones honored; dependency-free/static cleanup; no vendor runtime state; repeated bake/import canonical output | dropped internal room; changed orientation; vendor id used as project id; PGG component/dependency leak `BAKE_VENDOR_LEAK`; populated socket clearance; unknown field silently discarded | source→contract comparison receipt; dependency/forbidden-component scan; same semantic module from hand/control and adapter yields same authoritative bytes |
| 3. Built-level validation | instance/global ids; compatible paired sockets; exact gaps/overlaps/profile/apertures; internal rooms remain distinct; vertical planes remain ±Z; anchor/feature resolution; canonical ordering/hash repeat | gap `LEVEL_GAP`; overlap; compatible profile but wrong hole `LEVEL_APERTURE_MISMATCH`; external socket attached to wrong room; module=room collapse; same input hash drift `LEVEL_NONDETERMINISTIC` | accepted Built Level Manifest; same input twice byte/hash identical; negative fixture reports exact instance/room/socket paths |
| 4. Existing engine admission | projection to generator-neutral topology/apertures/features; `TopologyConformance`; voxelization/admission; loud unsupported capability | malformed topology; out-of-grid feature; projection loses exact aperture; ±Z silently skipped (must instead emit `ENGINE_UNSUPPORTED_Z_APERTURE`) | current engine gates GREEN for supported horizontal fixtures; deliberate named NOT-ADMITTED result for represented-but-not-yet-supported vertical runtime path |

## 9. Fixture matrix

| Fixture | Source / modules | Proves | Planted negative |
|---|---|---|---|
| `F1-HAND-1H` | hand-authored, 1 module / 1 room | basic frame/pivot/envelope, one non-centred horizontal aperture, one typed anchor, canonical repeat | fill irregular notch by AABB; shift aperture one 25 cm cell |
| `F1-COMPOUND-1V` | hand-authored, 1 module / 2 stacked rooms | module≠room, stable room ids, internal ±Z connection, floor datums, exact vertical aperture without traversal/art | collapse to one room; rewrite ±Z as wall portal |
| `F2-PAIR-2H` | 2 modules, horizontal external sockets | socket owner rooms, portal profile + exact hole, clearance and no gap/overlap | compatible profile with mismatched aperture; wrong owning room |
| `F2-STACK-2V` | 2 modules, external floor/ceiling sockets | stacked module normalization and vertical pairing; contract/manifest GREEN | engine admission must loudly return unsupported until Z path exists; silent skip is planted failure |
| `F3-LINE-3H` | 3 modules endpoint–pass-through–endpoint; middle later repeated as PGG bake | role/socket count, PGG-cleaned result equals hand control authority, canonical ids/order | PGG prop in clearance; dropped anchor; vendor component leak |
| `F4-JUNCTION-4H` | 4 modules, one junction + three leaves | 1/2/3/4 coverage, junction role, multiple links, global id stability and repeat hash | duplicate instance id; one overlap; producer enumeration shuffle |

Fixtures are contract/validator assets only. They prove no navigation, stairs/elevators, art quality, runtime DA build,
gameplay, networking, destruction or common-scene delivery.

## 10. Old task/CALL disposition ledger

| Old/current item | Disposition | Current meaning / dependency |
|---|---|---|
| NOW task `Lv-ingest` | **obsolete**, not done | Removed without completion in `s-repair-near-gas-program-routing-001`; do not resurrect the task. Preserve only cited lower-seam evidence. |
| `c-exec-lv-ingest-phase0-001` | **obsolete / NEVER RESUME** | Phase 0 NOT DELIVERED. Its source/quantization design is historical evidence, never a prerequisite or launch pin. |
| `c-spike-pgg-001` | **keep-evidence** | Closed `FAIL_STAGE` for production pipeline; keep narrow editor static-prefab→DA→reader proof and failure classes. No spike branch merge as PASS. |
| `c-exec-level-platform-phase1-plan-001` | **replace** | `SUPERSEDED / NEVER ISSUE`; dead Phase0, v19, fixed lane-D and 13-leg assumptions cannot be repaired in place. Detailed requirements feed the successor. |
| `c-work-poligon-m1-integration-route-001` / accepted route | **keep-evidence / consumed** | Owner-accepted LV0→LV5 sequence and cuts remain direction truth; it authorizes no product work. |
| Legacy gate `fresh v21 + verified lane D worktree` | **replace current dispatch meaning** | Record as historical safety intent. As of 2026-07-16 current contract is v26 and product protocol owns venue/pre-write admission; Direction must request current-contract/fresh-admission evidence, not prescribe `GasCoopGame_levels`. |
| `c-research-level-module-standard-v1-001` | **complete / owner-disposed** | Research returned the candidate; owner later accepted it as architectural basis with D1=A / D2=A. No product leg follows automatically. |
| LV0 — fresh owner-approved PLAN | **READY PARALLEL / CALL ISSUED** | `c-exec-level-module-standard-v1-lv0-plan-001` is the first parallel Level leg. It requires fresh current product-contract/code readback and product-owned pre-write admission, then freezes canonical encoding, shared-surface ownership, socket terminal states, transform rules, deterministic build input, registries/versioning, sampler authority and size/time ceiling. Owner-present PLAN only; no Unity and BUILD remains separate. |
| LV1 — Project Level/Module Contract | **held behind LV0** | First product outcome. No DA/PGG dependency required; includes hand controls and canonical serialization. |
| LV2 — validators | **held behind LV1 contract shape + LV0 split** | Module, adapter, built-level and engine-admission matrices; may share PLAN with LV1 but must have separate executable evidence/stop. |
| LV3 — DA runtime composition | **held behind LV1+LV2** | Uses accepted modules/external sockets; outputs Built Level Manifest; fresh product admission required. |
| LV4 — PGG editor baker/importer | **held behind LV1+LV2** | Editor-time only, dependency-free cleanup; may be prepared alongside LV3 but one Unity Editor/overlapping Level surfaces serialize unless product registry proves disjointness. |
| LV5 — minimal M1 modules | **held behind LV3+LV4 gates** | Project-owned content including ≥1 PGG-derived static module; no large library or vertical production content. |

## 11. Parallelism and dependency route

```text
NOW: priority route continues independently; Level LV0 PLAN runnable in parallel = 1; Level BUILD runnable = 0
  ↓ c-exec-level-module-standard-v1-lv0-plan-001 + fresh current product preflight/admission
LV0 PLAN (READY PARALLEL; owner-present; current contract; product chooses venue; no Unity)
  ↓
LV1 Project Module Contract + hand controls
  ↓
LV2 validators + fixtures + Built Level Manifest validation
  ↓
LV3 DA adapter ─┬─ LV4 PGG baker/importer
                └─ parallel preparation only; mutations require separately admitted disjoint surfaces,
                   one Unity Editor and serial integration
  ↓
LV5 minimal M1 modules
  ↓
common M1 scene / network / evidence under the accepted route
```

Current NearGas/extraction/character/design tracks keep their own priority and state while LV0 runs in parallel. Shared
product registry, single Unity Editor, `LevelIngestion`/scene/module conflicts and integration remain serialized;
the docs-only LV0 leg launches no Editor.

## 12. Smallest owner decision package

### D1 — exact structural representation — OWNER SELECTED A

- **A — canonical sparse 25 cm cell/sub-face mask (recommended).** Preserves irregular voids, aligns with near-grid
  truth and makes expected↔observed comparison/hash direct. Bad side: artifact size and tooling need measurement.
- **B — canonical rectangular decomposition.** Smaller on boxy rooms. Bad because irregular geometry fragments,
  decomposition identity can drift and room identity may be bent to fit boxes.
- **C — mesh/collider only, sampled at runtime.** Little stored data. Bad because Unity/runtime/vendor state becomes
  authority and deterministic cross-producer validation becomes harder.

Owner verdict: **A for v1**, with size/time ceiling frozen in owner-approved LV0 PLAN; compression is storage, never
semantic identity.

### D2 — Z-normal engine scope — OWNER SELECTED A

- **A — represent + validate now, loudly refuse engine admission until a later support leg (recommended).** Protects
  the full-3D contract without hiding missing runtime capability.
- **B — implement Z-normal voxel/runtime support inside LV1/LV2.** Earlier end-to-end vertical proof. Bad because it
  expands a contract/validator leg into engine behavior before fresh product planning.
- **C — omit vertical apertures from v1.** Smaller. Bad because it contradicts ratified 1:N vertical requirements and
  recreates a wall-only model.

Owner verdict: **A**. Represent and validate ±Z now; engine admission must loudly reject unsupported runtime use.
Any later move to B is a separate explicitly budgeted owner decision, not an implicit LV1/LV2 expansion.

## 13. Explicit cuts

- Direction launch changes only Direction files; LV0 may commit product planning docs after current product-owned
  admission, but makes no Unity, source, test, package, prefab, scene, canon, TREE or CHARTER change.
- No Phase 0 revival and no old CALL dispatch.
- One LV0 PLAN executor CALL is issued in parallel. No SURFACE-FREEZE/RED/BUILD CALL or Direction-owned physical
  worktree assignment is issued; product protocol chooses the planning venue and Unity stays closed.
- No DA/PGG adapter implementation, runtime PGG, production module library or library compatibility promise.
- No production art, navigation, stairs/ladders/elevators, streaming/occlusion, giant compound module or traversal.
- No arbitrary destruction; only a typed breach-surface reference is reserved.
- No common M1 scene, seed/ProfileHash network handshake, real-network, min-spec or two-machine proof.
- No universal metadata bag and no speculative catalog of every future gameplay feature.

## 14. Confidence and limits

**High / established:** phasing A; two missing upper authorities; existing lower seams; PGG narrow proof and
`FAIL_STAGE`; DA/PGG role split; 50/25 cm dual lattice; module≠room; vertical 1:N and six-face expressibility;
old Phase0/PLAN non-runnable status.

**Owner-accepted architectural basis:** project-owned two-authority shape; D1 sparse 25 cm cell/sub-face truth; D2
represent/validate ±Z with loud unsupported engine admission; four validator boundaries and the bounded fixture route.

**Still requires LV0 freeze / product verification:** exact field/type names; canonical byte encoding; shared-surface
ownership; socket terminal states; transform rules and yaw/handedness examples; deterministic pre-build input;
registries/versioning; structural sampler authority; sparse size/time ceiling; instance-id formula; diagnostic codes;
fixture implementation and whether LV1/LV2 are separate commits or sessions. These require a fresh product-v26
code/contract read and owner-approved LV0 PLAN.

The answer changes if fresh product readback proves a lower API materially different from Direction evidence, an
independent sampler cannot reproduce canonical masks within the chosen ceiling, a later explicit owner verdict revises
D1/D2, or current engine already supports verified Z-normal admission. No product claim here was re-verified outside
committed Direction artifacts.

## 15. Recommended first implementation probe (not launched)

After an owner-approved LV0 PLAN and product-owned admission, run one bounded **contract/validator probe** with no
DA/PGG dependency:

1. Freeze `F1-HAND-1H` and `F1-COMPOUND-1V` as project-authored inputs.
2. Export Project Module Contract, independently re-sample expected structure/apertures, normalize one-instance Built
   Level Manifest twice and compare canonical bytes/hash.
3. Plant four controls: AABB-fill an irregular void; collapse two rooms into one; attach external socket to wrong room;
   silently drop ±Z aperture. Each must trip its named boundary/error.
4. Project the supported horizontal fixture through existing topology/voxel admission; vertical fixture must validate
   structurally and then return the explicit current capability verdict, never disappear.
5. Stop if sparse artifact size or independent sampling exceeds the PLAN ceiling; return measurements to D1 rather
   than widening scope.

This is the smallest probe that attacks the main assumption: the new project-owned layer can preserve exact 1:N 3D
truth and deterministic identity while reusing, not replacing, the proven lower seams.

END_OF_FILE: live/indie-game-development/work/level-module-standard-v1-candidate-2026-07-16.md
