# c-exec-013 — S0 FOUNDATION SLICE — build-facing PLAN (planner phase)

> **Status:** APPROVED — owner «да» 2026-06-23 (PLAN gate, owner present). Deltas R1–R7 folded in the block
> directly below; they OVERRIDE the body where they differ. This is the design source the dev-worktree build
> session implements.
> **Provenance:** planner session 2026-06-23 (Claude Code, OS-worktree). Grounded by workflow `wf_7fb3eb2d-a9d`
> (9 agents over the locked architecture + 5 decision docs + GasCoopGame Core keep/delete set + gate tooling +
> dev baseline). Binding CALL: `live/indie-game-development/work/c-exec-013-call.md` (read in full).
> **Build baseline (verified directly):** `C:\projects\Unity\GasCoopGame_dev` branch `dev` @ `170709b`.
> Dirty: IvanMurzak MCP-bump trio (`Packages/manifest.json`, `packages-lock.json`, `ProjectSettings.asset`) +
> untracked DA assets `Assets/GasCoopGame/Levels/GasLab/Modules/` (see §H). ChunkEncoder `(byte)c` overflow is
> ALREADY guarded on dev (`ChunkEncoder.cs:46-56` + cast L137) — CALL's "open deferral" wording is stale.
> **No ADR-0010 / G9 lock crack is required by S0** (classification §A clean).

## OWNER-APPROVED — deltas folded 2026-06-23 (owner «да»; PLAN APPROVED)

The owner reviewed the PLAN (present) and approved S0 with the deltas below (R-numbered from his words). These
OVERRIDE the body where they differ; the body remains the design source. They are the owner-ack record for the
build session's deliverable-coverage.

- **R1 — Dungeon Architect only; NO hand-placed levels; the DA-vs-hand cross-check is CUT** (owner-ack: owner «да»
  2026-06-23). Drop RED test #1 "DA-vs-hand byte-identical." Anti-substitution is preserved by: (a) the Core boundary
  gate (voxelizer in `Core/**` cannot reference DungeonArchitect — compile-enforced); (b) grep-clean
  `ActiveModel as SnapGridFlowModel = 0` (no DA-internal-model read — the hardest anti-cheat, KEPT, done_when 6);
  (c) NEW replacement RED: **re-voxelization determinism** (same DA-derived RoomSpec → byte-identical grid on re-run)
  + **fixture correctness** (the voxelizer on an in-code `RoomSpec`/`LinkSpec` fixture yields the expected grid — an
  in-code fixture is a unit-test input, NOT a "hand level"). The real DA level (Unity, owner-generated) drives the
  sandbox/owner-eye. Coverage bullet 1 carries this owner-ack.
- **R2 — doors: static + a sandbox DEBUG TOGGLE in S0; the real dynamic/networked door = S5** (owner «да» to "toggle
  is enough"). done_when (3) sandbox GAINS a debug control to flip a doorway's faces open/closed at runtime and watch
  the flow respond. It reads the LIVE per-face open/closed bit (already in the law); a closed-via-toggle face is just a
  wall → already covered by WALL-ZERO + MASS-CONSERVATION RED tests (no new conservation guarantee built). The real
  door-as-mechanic (telegraph, networked, mass-conserved-across-the-flip EVENT) STAYS in the cut list (S5).
- **R3 — per-cell 50 cm visualization, NOT a per-room bucket** (clarification, no scope change). S0 shows gas per
  50 cm cell on the near grid. The bucket/coarse `representation_tag` is reserved as DATA now; the bucket BEHAVIOR
  (room-as-one-blob + smooth un-bucket) is S4. 25 cm is not an S0 size.
- **R4 — sandbox shows a REAL owner-generated DA SnapGridFlow level, multiple connected rooms, with an orbit camera.**
  done_when (3): the owner generates the level via SGF (changing Flow for variety) following step-by-step instructions
  the BUILD SESSION provides (owner-run, confirmed — not self-marked); the new generator-blind reader reads its BUILT
  geometry. Add an orbit/free camera around the level.
- **R5 — spawn gas at a chosen cell/room in the sandbox** (any 50 cm cell, any amount). done_when (3): a spawn control
  to place gas at a picked cell/room.
- **R7 — do NOT extract a separate viz-data-contract note** (owner: "ничего не выноси, хватило ответа"). The snapshot
  schema (done_when 3) + the per-cell near read query (done_when 4) REMAIN the visualization data contract for the
  g-7e15 track — built as part of S0; just no extra standalone doc. g-7e15 reads them directly.
- **D1 (baseline) — leave the untracked `GasLab/Modules` DA assets UNTOUCHED** (owner: "не решаем сейчас, лежит"); do
  NOT `git clean`. The owner-generated fresh SGF level (R4) becomes the committed fixture. The MCP-bump trio still
  commits as a standalone chore in §0 pre-flight.

**Net effect on gate/coverage:** RED test #1 (DA-vs-hand) → replaced by determinism + fixture (still done_when 1,
still headless). Sandbox (done_when 3) GAINS door-toggle + spawn-at-cell + orbit-camera + owner-generated SGF level —
all engine-class under the existing `exists:` scene artifact (§E rows 3/7). No new lock crack; no ведро-3; appetite
unchanged.

## 0. PRE-FLIGHT (do FIRST, in order — in the dev-worktree session)

1. **Reconcile the baseline (§H):** commit the MCP-bump as a standalone chore; resolve the untracked DA assets
   per owner decision D1; reach a clean `-Deliver` tree before building.
2. **§Re-sync GasCoopGame contract v7→v8** (§E) — additive only; never weakens a green gate.
3. **READ-FIRST — the SINGLE source (consolidated 2026-06-23, owner-signed):** `knowledge/g9c41-gas-engine-SPEC.md`
   (the canon — read it, NOT the old docs). It adds 8 load-bearing invariants the build MUST honor: damage/dose
   reads COARSE not the bubble; detonation reads coarse TOTALS; integer mass clamp [0,cap] (loud assert, no wrap);
   vertical = buoyancy-BIAS not per-column sort; capacity+back-pressure is a kept law; cross-layer reads use a
   COMMITTED revision; the destructibility seam (back-pressure stores the door-break pressure).
4. **(superseded)** dev-plan-graph + the 4 decision docs are FOLDED into the canon and now in `work/archive/` — NOT read.
5. **Contour:** PLAN (this doc, owner-approved) → RED-first independent test-author (§D) → build (§B) →
   `-Deliver` gate → fresh-session G5 → owner-eye «весело».

**approach token:** voxelizer-grid-faceflow-foundation + feel-grey-box + §9-seams + integer-deterministic-by-construction.

## A. ВЕДРО CLASSIFICATION (within the LOCK) — CLEAN, no STOP

Default = room-granular Variant A. Buckets: ведро-1 = washes-out free local feel; ведро-2 = coarse-promotable
EVENT computed on every peer; ведро-3 = sub-room AND shared = expensive → STOP/escalate.

| S0 mechanic | ведро | rationale |
|---|---|---|
| voxelizer / openFaces | substrate (N/A) | produces the SOLE shared truth (grid+faces+region_id) folded into the checksum on every peer; not a detail/refinement mechanic |
| face-flow law | **ведро-1 (Variant A)** | coarse room-fill computed identically on every peer; fully in the checksum; no sub-room shared dependency |
| §9 seams-as-data | **ведро-1 / inert** | shipped STUBBED, zero behavior in S0; later ENABLEMENT classified at that slice's PLAN |
| sandbox / gizmos | **ведро-1 (for-eyes, OFF checksum)** | owner-eye view + snapshot reader over the same canonical record; non-authoritative render layer |

**No mechanic needs ведро-3 or a D1/D2 change. No ADR-0010/G9 crack.** S0 is netcode-neutral (does not touch
D1's wire), builds the coarse-authoritative grid (D2), ships collapse/expand as IDENTITY only (honors
"detail = LOCAL non-authoritative refinement"). RESULT §6 carries the "none needed" one-liner.

## B. DESIGN per done_when clause

All net-new authoritative code is engine-free, integer-only, under `Assets/GasCoopGame/Core/**` (auto-compiled
headlessly via `core/GasCoopGame.Core.csproj` glob; a `using UnityEngine`/`using DungeonArchitect` there fails
the boundary gate by construction). **Proposed placement: new subtree `Core/Field/Voxel/`** (decision D-place, mine).

**(1) VOXELIZER + openFaces.** `Voxelize(IReadOnlyList<RoomSpec>, IReadOnlyList<LinkSpec>) → CellGrid`. Integer
3-D cell grid; each cell = integer coord + region_id + 6-face open/closed bitmap + reserved per-face attr fields.
`openFaces(opening_descriptor, cell_grid) → ordered face-id set` (canonical sort by cell coord (z,y,x) then
face-axis); its COUNT = emergent open-face area.
- REUSE: `TopologyDocument`/`TopologyVolume`; `TopologyStableIds.Volume` (deterministic id law); `RoomSpec`/`LinkSpec`
  (engine-free integer DTOs in `Adapters/Topology/`, the IDENTICAL boundary data for DA and hand levels);
  `RectDecomposition`/`GridRect` (if a room is re-tiled).
- NET-NEW: the integer 3-D grid; per-face bitmap + §9 per-face primitive; `openFaces`; the integer opening descriptor
  (AABB + sill-lower-edge + span, in cells; derivable from `TopologyPortalSpec`/sill fields).
- EXTEND `TopologyConformance` (additive): admit a near-grid doc only if `openFaces` is total+deterministic over
  every opening AND `geometry_res` is an integer multiple of `gas_res` (reject 75-vs-50). Do NOT weaken existing
  checks. NOTE: the current scalar check is on `SillBandLowerEdgeHeight` (L76-78); there is no `OpeningSize` *gate*
  today — the near supersede ADDS admission logic; KEEP the scalar portal check for `TopologyPortalSpec`/far tier.
- RES sequencing: START geometry=50cm (1:1 with gas) → determinism + Conformance green → switch to 100cm by CONFIG
  (100cm face = 2×2 patch of 50cm gas faces). gas_res = 50cm GLOBAL authoritative. The face-flow operator never sees
  geometry after voxelization.

**(2) FACE-FLOW law.** Integer gather-then-apply + carry room-fill. CONSUMES open-face COUNT as DATA (the near
supersede of the area-blind t=mEq/kP; R6 HARD "площадь проёма всегда влияет на поток"). A flat per-face transfer
ignoring area FAILS. Fidelity floor (may NOT drop): area always affects flow AND a single open face seeps >0
(never seals to 0). **Single-owner-per-face + simultaneous-gather** (a sequential pass silently diverges).
NET-NEW: per-cell mass field; sparse active-front flux+carry register; the integer operator. Placement `Core/Field/Voxel/`.

**(3) SANDBOX (owner SEES).** Unity gizmos: level→grid(faces)+region_id; pause/slow/step; scenario-as-DATA
(anti-scene-sprawl). A STABLE, VERSIONED, integer-valued snapshot with a NAMED schema exposing per-cell exactly the
clause-(4) meaning fields + the per-tick meaning-checksum. Gizmos + snapshot read the SAME canonical record.
- Placement: gizmos/render = `Adapters/**` (non-authoritative, OUTSIDE the zero-float scan; float OK here). The
  canonical record + snapshot serializer = `Core/**` (integer, scanned). Reuse the `CoarseFillProjection`/`ExposureQuery`
  pure-consumer template (read-only over the frozen oracle).
- This is a class=engine deliverable (needs an `exists:` artifact — §E).

**(4) §9 SEAMS as DATA (day-one, stubbed).** Full schema §C. Key threading:
- region_id NEW: far/graph tier — add a per-sector array parallel to `_stableId[]` in `CoarseSectorGraph`, bound in
  `FromTopology`, geometry-derived; thread into `ProfileHash()` via a NEW pinned fold loop. Near tier — region_id is
  a per-cell grid field.
- per-cell NEAR query into `IGasReadModel` ADDITIVE (must not change `ConcentrationAt`): a NEW static consumer class
  alongside `CoarseFillProjection`, OR a NEW near read-model impl (today's `CoarseGasReadModel` is band-resolution,
  NOT a 3-D grid — the near read-model is NEW, not a mutation).
- meaning-checksum: there is NO single aggregator today (3 independent folds). The S0 meaning-checksum folds per-face
  open/closed, region_id, representation_tag, resolution_tag pair, the sparse active-set digest (sort
  `(tick, region_id, species-id)`; species-id = reserved comparator slot), and the GAP stubs — each via the pinned
  `Fnv1a64.StepInt32` discipline, sorted by integer cell coord (never container order). **Mirror on the follower**
  (`CoarseChunkFollower.ComputeHash`) or host≠follower. Decision D-checksum (mine): a parallel per-cell/per-face
  digest + a `schema_version` bump (rather than overloading `ProfileHash`), budgeting a golden re-baseline.

**(5) DETERMINISM-BY-CONSTRUCTION.** Integer-only authoritative path + a build-time ZERO-FLOAT scan wired as a GATE
STEP in `tools/check.ps1` (inner loop, not only `-Deliver`) over `Assets/GasCoopGame/Core/**`, failing the build on
any `float`/`System.Single`/`double`/`System.Double`/`decimal` on the authoritative path. **NET-NEW (the scan does
NOT exist yet).** Authoring risk: match C# *types* as whole tokens (`\bfloat\b`, `\bdouble\b`, `\bdecimal\b`,
`System.Single`, `System.Double`), excluding comments/identifiers — naive substring hits `FloorExtent`/`Float…`
identifiers in Core. RED control: a planted float on Core FAILS; clean PASSES. This scan on ONE machine IS the
cross-CPU guarantee. NO 2nd physical machine in any gate or RED test. An optional one-machine 2-process loopback
hash = a tripwire (NOT a gate; home is S2).

**(6) ZERO-LEGACY.** Delete both dead-path files + reconcile the scene (§F). Net-new: nothing.

## C. §9 SEAM-AS-DATA SCHEMA (integer, day-one stubs; `schema_version` int, bumped on any add/remove)

**Per-cell:** cellCoord(X,Y,Z) int×3 (actual); region_id int (geometry-derived interior label, distinct from void);
mass int[] (S0 species count=1, reserved species-id slot); representation_tag enum {fine-3D=0,mid-2.5D,coarse,bucket}
default fine-3D; resolution_tag (geometry_res,gas_res) PAIR default (50,50); tick_divisor int (GAP-4) =1.
**Per-face (6/cell, checksummed):** openClosed bit (live); conductivity int = full-open/0-closed (GAP, no partial);
directionMask = bidirectional; breachThreshold int = disabled.
**Sparse flux-register (active faces only):** flux int (implicit-zero quiet, not folded); carry int =0 (must exist).
**GAP sockets (in checksum):** GAP-1 cap {max_mass=∞-sentinel, rate_limit=0, dissipation=0}; GAP-2 void/exterior =
a reserved distinguished region_id constant (exists, distinct from every interior id, canonical drain target for
open-to-exterior faces); GAP-3 resolution_tag pair; GAP-4 tick_divisor=1.
**collapse/expand interface (IDENTITY body only in S0):** pure integer functions typed PER-REGION/PER-LAYER,
mass-exact (input column sum == output to the bit), routing transfers through the flux-register remainder
(carry-conserving), carrying an explicit remainder; **the signature MUST NOT be able to express collapsing a column
into one averaged/pre-divided scalar.** Temperature carrier RESERVED as the integer PAIR {energy_sum, capacity_sum}
(never a pre-divided mean) — a reserved data shape ONLY; NO temperature behavior/accumulator/energy field in S0 (S6).

## D. RED-TEST LIST (independent test-author, from the spec; builder cannot edit)

Headless tests under `tests/GasCoopGame.Core.Tests/**` (default-globbed; ns `GasCoopGame.Core.Tests.<mirror>`);
each file ≥ test-count `Assert.` calls, NO `[Ignore]`/`[Explicit]`.

1. **DA-vs-hand byte-identical voxelization** (1): both inputs → identical canonical tuple stream per cell
   {coord, region_id, 6-face bitmap, reserved attrs}, sorted (region_id, coord; never container order), field-by-field.
2. **openFaces total+deterministic+ordered** (1): ordered face-id set; re-run byte-identical; COUNT == what face-flow consumes.
3. **Conformance admits near-grid iff openFaces total+deterministic; rejects non-integer-multiple geometry_res** (1).
4. **Face-flow MONOTONIC** (2): sweep open-face count 1→N; per-tick transferred mass non-decreasing, strictly greater
   for ≥1 increase (a flow constant across the sweep FAILS); equilibrium guard (measure only while a gradient exists).
5. **SLIT-SEEPS** (2): flow >0 for the smallest single open face (carry never seals a slit to 0).
6. **WALL-ZERO** (2): a fully closed boundary transfers exactly 0.
7. **MASS-CONSERVATION** (2): integer gather-then-apply + carry conserves total mass across ticks (non-vacuous guard).
8. **EMERGENT-HEIGHT** (2): a low doorway drains only the low cells; no gas above the sill crosses.
9. **Snapshot schema-match + version-bump** (3): snapshot matches its declared NAMED schema + integer values; add/remove
   requires a `schema_version` bump.
10. **§9 per-face primitive present-stubbed** (4): open/closed + conductivity(full-open/0) + direction-mask(bidir) +
    breach-threshold(disabled) each EXIST with the inert default.
11. **Sparse flux-register** (4): carry present per active face; quiet faces ABSENT from the checksum.
12. **Tags present** (4): representation_tag + resolution_tag (50,50) present + folded.
13. **region_id folded** (4): present per cell + folded into the meaning-checksum (and `ProfileHash` graph tier).
14. **4 GAP sockets present-stubbed** (4): cap(∞/0/0), void-sink(exists/distinct/drain), resolution_tag, tick_divisor=1.
15. **Checksum NEG control — face flip** (4): flip a face open/closed, masses byte-equal → checksum CHANGES.
16. **Checksum NEG control — region_id change** (4): change region_id, masses byte-equal → checksum CHANGES.
17. **Checksum NEG control — tag change** (4): change a tag, masses byte-equal → checksum CHANGES.
18. **Checksum POS control — non-meaning permutation** (4): canonical-order-preserving permutation / scratch value →
    checksum UNCHANGED.
19. **collapse∘expand round-trip** (4): multi-layer column unchanged to the bit; preserves {energy_sum, capacity_sum}.
20. **collapse divided-scalar variant FAILS** (4): a variant returning a divided/averaged scalar FAILS the shape assertion.
21. **Zero-float scan planted-float RED control** (5) [BUILD-SCAN]: a planted float on Core FAILS the scan; clean PASSES.
22. **ZERO-LEGACY grep-clean + compiles + no missing-script GUID** (6) [BUILD-SCAN]: grep-clean
    (`SnapGridFlowRoomReader`/`VScale`/`ActiveModel as SnapGridFlowModel` = 0); headless build + clean scene compile;
    scene guid `f6ddb608…` = 0.

**ANTI-OVERREACH (no RED test may encode):** no 2nd physical machine / 2-hardware run. The 3 binding probes are NOT
S0 RED tests and must not be authored as S0 gates (hangar/weakest-CPU S4; 60-room cascade S6; re-flux+breach-mid-collapse
S4/S5 — its binding gate is loopback-one-machine + zero-float, never 2 hardware).

## E. §Re-sync v7→v8 + openspec change + deliverable-coverage

**v7 state:** `validation.config` `synced_contract_version: 7`, `mutation_kill_floor: 70`,
`strong_check_grandfathered: []` (S0 is NOT grandfathered → mutation ≥70 + spec-silence + coverage all apply).
`coverage-check.ps1` is v7. Zero-float scan absent.

**v8 = ADDITIVE, two pieces (never weakens a green gate):**
- (a) AGENTS.md new section "Contract v8 — anti-substitution + anti-fabricated-approval (synced_contract_version: 8)":
  1. **STOP-discipline v8 (anti-substitution):** a blocked/infeasible NAMED approach or a crutch = mandatory STOP +
     escalate, NEVER a silent substitute/descope. Forbidden: VScale-style scaling crutch; scene-tags/markers as the
     geometry/measurement SOURCE (the read is generator-BLIND); a stored area scalar in place of open-face COUNT;
     reading the DA internal model anywhere; a float fast-path on the authoritative path; shipping at REDUCED FIDELITY.
  2. **Anti-fabricated-approval:** «весело» is the ONLY non-unit-testable axis = OWNER-RUN (no self-marking); «точно»
     is DISCHARGED by the GREEN headless/build suite; an owner sign-off NEVER substitutes for a missing-or-red test;
     a leg may not close on an unconfirmed owner-run step.
  3. **Seam-presence rows each get a deliverable-coverage row** (keep the §9 seams enumerated as numbered done_when
     bullets so the existing coverage mechanism binds them).
- (b) the zero-float scan (the ONE code addition; §B(5)) wired into `tools/check.ps1`.
- (c) version bump: `validation.config` 7→8 (+ `_note`) + the AGENTS.md contract-version line.

**`coverage-check.ps1` needs NO code change:** the v7 mechanism already requires every numbered `n.` done_when bullet
to have a `| n | headless|engine | row|out-of-scope | evidence |` row — so enumerating the S0 promises (incl. seams)
as numbered bullets binds them. CALL §8 "wire deliverable-coverage over the S0 promises" is satisfied by the existing
mechanism + the S0 spec.

**openspec change** `openspec/changes/c-exec-013-s0-foundation-slice/` (module `sim-core`):
`proposal.md` + `tasks.md` (F0 = RED tests authored; F1..Fn per requirement; Fg gates; Fo owner-run) +
`specs/sim-core/spec.md` (frozen public-surface block of the integer/bool members; `## Spec-silence audit` non-empty;
`## Deliverable coverage`). Mutation evidence `docs/measurements/mutation-c-exec-013-s0-foundation-slice.json ≥ 70`
required to pass `-Deliver`.

**Deliverable-coverage table** (verbatim numbered done_when 1–7 from CALL §4):

| n | class | disposition | evidence |
|---|---|---|---|
| 1 | headless | row | DA-vs-hand voxelization + openFaces + Conformance tests (§D #1-3) |
| 2 | headless | row | face-flow tests (§D #4-8) |
| 3 | **engine** | row | `exists:Assets/GasCoopGame/Adapters/GasView/GasViewCoarseScene.unity` + `exists:docs/measurements/c-exec-013-snapshot-sample.json`; snapshot RED test (§D #9) covers the headless half |
| 4 | headless | row | §9 seam-presence + checksum controls + collapse round-trip (§D #10-20) |
| 5 | headless | row | zero-float scan + planted-float control (§D #21) [BUILD-SCAN] |
| 6 | headless | row | ZERO-LEGACY grep-clean + compile + scene-guid (§D #22) [BUILD-SCAN] |
| 7 | **engine** | row | `exists:Assets/GasCoopGame/Adapters/GasView/GasViewCoarseScene.unity` + a gizmo capture under `docs/measurements/**`; owner-run «весело» (no self-mark) |

Engine rows (3, 7) need a real `exists:` file (>64 bytes, under `Assets/` or `docs/measurements/`) — a headless test
name CANNOT discharge them (the leg-8-lie close). No out-of-scope cuts anticipated; any cut needs `owner-ack:<sig|esc-id>`.

## F. DELETE-LEDGER RECONCILIATION

**DELETE (2 files + `.meta`, under `Assets/GasCoopGame/Adapters/DungeonArchitect/`):**
- `SnapGridFlowRoomReader.cs` (124 lines): `const int VScale = 2` @L76 (NOT a separate file); DA model read L45-66;
  `.meta` guid `2fdbeef7620fb3c4b83fe12e50356c1b`.
- `SnapGridFlowTopologySource.cs` (86 lines): sole caller `new SnapGridFlowRoomReader(...).Read()` @L68 +
  `ActiveModel as SnapGridFlowModel` @L64; MonoBehaviour wired into the scene; `.meta` guid
  `f6ddb60860047eb4fb7b9dd71f65e2eb`. Deleting only the reader orphans the source → delete BOTH.

**References to reconcile:** `GasViewDirector.cs:33` `public MonoBehaviour daTopologySource;` is typed `MonoBehaviour`
(NOT the deleted class) → NO compile break; KEEP the field (generic `ITopologyProducer` seam). String literals naming
`"SnapGridFlowTopologySource"` (`GasViewDirector.cs:32/169`) compile fine → optional cleanup, not in the grep-clean set.
Tests: 0 references to the dead path.

**Scene re-point — `Assets/GasCoopGame/Adapters/GasView/GasViewCoarseScene.unity`:** the deleted source (guid
`f6ddb608…`) is a LIVE component on GameObject `SGF_TopologySource`, wired via `daTopologySource: {fileID: 785831868}`.
Pick one (both leave NO missing-script GUID): **(A) Replace** — swap in the new generator-blind reader→voxelizer
`ITopologyProducer` component on the same GameObject, re-point `daTopologySource`, re-wire fields; **(B) Clear** —
delete the `SGF_TopologySource` GameObject (+ child entry in the director transform) and set `daTopologySource:{fileID:0}`
OR flip `GasViewDirector.levelSource` Da→InCode. After the edit: grep the scene for `f6ddb608…` → 0; Editor reports no
missing scripts. Do this as a deliberate scene edit — never delete the `.cs` and leave the scene.

**KEEP (none in the dead path):** `ChunkEncoder` (S2 plumbing, already guarded); `IDaRoomReader`, `DaTopologyProducer`,
`FixedLevelRoomReader`, `SceneTopologyComposer` (shared engine-free-DTO seam); `RoomSpec`/`LinkSpec`;
`CoarsePortal`/`TopologyPortalSpec`/t=mEq/kP orifice (FAR tier S4); `TopologyDocument`/`TopologyConformance`/
`TopologyStableIds`/`CoarseSectorGraph`/`RectDecomposition`/`IGasReadModel`/`CoarseGasReadModel`.

**grep-clean acceptance (all 0 across `Assets/**`):** `SnapGridFlowRoomReader`, `VScale`,
`ActiveModel as SnapGridFlowModel`, scene guid `f6ddb608…`.

## G. CUT LIST (OUT of S0 — building OR gating on any = STOP-worthy scope violation)

S1 burst-on-spawn + displacement; S2 any lockstep wire/broadcast + the real detail tier + the loopback-hash's home;
S3 finer VERTICAL refinement (off-checksum near; far-routing layers — NOT authoritative «height-bands»; canon §5/§7); only EMERGENT drain-height is in S0; S4 authoritative rollup / real
collapse-expand / LOD-without-pop / re-flux at the moving seam / return-from-far; S5 breach / pre-declared face-flip;
S6 reactions / chemistry / cascade / energy-accumulator + ALL temperature behavior (S0 ships only the reserved
{energy_sum,capacity_sum} shape). The **3 binding probes** are NOT S0 deliverables (must not be fabricated as a
blocker, used to STOP, nor authored as S0 RED tests). NO 2nd physical machine. `ChunkEncoder (byte)c` = KEPT, already
guarded on dev — say "KEPT, already guarded, not touched by S0", NOT re-defer. Numeric tuning beyond gas=50cm (tier
radii, gas-cap magnitudes, big-room-authoritative threshold, return-from-far variant) = PLAN-decided, NOT frozen in done_when.

## H. BASELINE RECONCILIATION + OWNER DECISIONS

Build baseline = `GasCoopGame_dev` @ `170709b` (the correct baseline; dev carries the genuine new work; `a89b36b` is
main's merge view of the shared history — dev is NOT a simple linear lead). dev is unpushed past `origin/dev`.

To reach a clean `-Deliver` baseline before build:
- **MCP-bump trio** (IvanMurzak 0.81.1→0.82.1: `Packages/manifest.json`, `packages-lock.json`, `ProjectSettings.asset`):
  **commit as a standalone "bump Unity-MCP 0.81.1→0.82.1" chore** before S0 (decide-and-inform; do NOT revert — the
  owner's running Editor re-introduces it).
- **D1 (owner):** untracked DA assets `Assets/GasCoopGame/Levels/GasLab/Modules/` (`Room_A.prefab` 66 KB,
  `GasLabBounds.asset`, `SnapGridFlowModuleBounds.asset`, `GasLabRoom.mat` + `.meta`s; c-exec-012 era). **Recommend:
  commit them** as the reproducible DA-level input for the DA-vs-hand byte-identical voxelization test (done_when 1).
  Alternative: drop them if S0 uses a hand-placed DA-equivalent instead. **Do NOT `git clean`** without the owner's word.

## I. BUILD HANDOFF

After owner «да» + D1: the build runs in a FRESH Claude Code session rooted in `C:\projects\Unity\GasCoopGame_dev`
(auto-loads the v8 engineering contract; has the IvanMurzak Unity-MCP for the gizmo sandbox + owner-eye + the scene
compile/missing-script check). Contour: §0 pre-flight → §E §Re-sync v8 → RED-first independent test-author (§D) →
build (§B) → `pwsh tools/check.ps1 -Deliver` green (incl. mutation ≥70 + spec-silence + deliverable-coverage + the
new zero-float scan) → MCP PlayMode/scene green → fresh-session G5 (refute, not confirm) → owner-eye «весело» →
`RESULT.md` → merge dev→main. The builder does NOT author the next CALL — the RESULT routes home; a fresh OS writer
session marks S0 done + opens the S1 CALL (выброс-при-спауне + выдавливание).

**Build-session obligations from the owner deltas:** (a) produce step-by-step SGF level-generation instructions for
the owner (multiple connected rooms; how to vary Flow) and treat the owner's generation as an owner-run gate step
(confirmed, not self-marked — feedback: owner-run Unity steps are a real gate); (b) NO separate viz-data-contract doc
(R7) — the snapshot schema + per-cell near query are the g-7e15 contract in place; (c) honor §0 baseline pre-flight
(MCP-bump chore commit; `GasLab/Modules` left untouched per D1).

END_OF_FILE: live/indie-game-development/work/c-exec-013-PLAN-s0.md
