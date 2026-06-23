# c-exec-013 — S0 FOUNDATION SLICE executor CALL (HARDENED, build-ready)

> **Provenance.** Framed by s-work-018 (work play, g-9c41) on 2026-06-23. Adversarially hardened by
> workflow wwr2am1l9 (64 agents; 49/54 findings kept after an "is-it-real + does-it-reopen-the-lock"
> verify) → 12 must-fix + 5 should-fix CALL-text tightenings folded, **all verified CAPTURES — no
> locked-decision change**, so no ADR-0010/G9 was needed to FRAME this CALL. Delete/keep ledger
> corrected against the real GasCoopGame tree at HEAD `a89b36b`. Validated against the committed
> NOW.md S0 task (`active_tasks id:S0`).
>
> **Repo:** GasCoopGame (`C:\projects\Unity\GasCoopGame`), dev→main when green.

## 0. PRE-FLIGHT (do FIRST, in order)

1. **§Re-sync GasCoopGame repo contract v7→v8 FIRST** (anti-substitution + anti-fabricated-approval;
   the c-exec-012 failure class). The amendments below ASSUME v8 wires deliverable-coverage over the
   S0 done_when promises — if it does not, the seam-presence/coverage indexing will not bite (see §8).
2. **READ-FIRST** (sync BEFORE you explain anything to the owner):
   `knowledge/g9c41-architecture-locked-slices.md` + `knowledge/g9c41-drift-guard.md` (the 5 drift traps).
3. **INGEST-AND-APPLY** (a checklist, not a citation): `work/dev-plan-graph-2026-06-22.md` (single
   entry) + `work/gas-model-architecture-decision-2026-06-21.md` + `work/grid-vs-graph-resolution-2026-06-22.md`
   + `work/detail-authority-cost-model-2026-06-22.md` + `work/gas-cellsize-levelscale-2026-06-22.md`
   §1–§12 (the s-research-012..017 synthesis). PRE-2026-06-22 docs in `work/archive/` are HISTORY — **NOT read**.
4. **OPEN WITH A PLAN (owner present)** that classifies this slice's mechanics ведро-1/2/3 WITHIN the
   LOCK (default = room-granular Variant A). Show the design BEFORE code. Standard contour:
   PLAN → RED-first independent test-author → build → -Deliver gate → fresh-session G5 → owner-eye.

**approach token:** voxelizer-grid-faceflow-foundation + feel-grey-box + §9-seams + integer-deterministic-by-construction.

## 1. GOAL (outcome)

A test sandbox where the owner SEES a generated (DA) or hand-placed level become an integer 3D cell
grid (per-FACE open/closed connectivity) and watches gas FILL A ROOM by face-flow, and renders the
owner-eye verdict «весело» (early). **Netcode-NEUTRAL** (no lockstep wire / no broadcast — that is S2).
FOUNDATION for every later slice.

## 2. CONTEXT (locked architecture, plain)

ONE integer cell model. NEAR = full-3D grid + flow through OPEN FACES (wall = closed face; doorway =
open faces; area = open-face COUNT; height emergent). FAR = room-graph rollup over the SAME partition
(S4). ROOM = a LABEL / region_id on every tier (geometry-derived; the generator-blind reader is the
voxelizer's input). Detail will later be a LOCAL, non-authoritative refinement of a coarse-authoritative
truth (S2+), discarded on room-exit, outside the checksum. Determinism is BY CONSTRUCTION (integer-only
+ a build-time zero-float scan on ONE machine = the cross-CPU guarantee; 2 physical machines are NEVER a gate).

## 3. BOUNDARIES

### 3a. ZERO-LEGACY — DELETE the dead DA→grid reader path (kept in git)

- **`SnapGridFlowRoomReader.cs`** — CONTAINS `const int VScale = 2` at line 76 (**VScale is NOT a
  separate file — do not hunt for one**) AND the DA `SnapGridFlowModel` read (lines 45–66).
- **`SnapGridFlowTopologySource.cs`** — the SOLE caller (`new SnapGridFlowRoomReader(...).Read()`,
  line 68) AND itself reads the DA internal model (`dungeon.ActiveModel as SnapGridFlowModel`, line 64).
  Deleting only the reader ORPHANS this = a compile break the CALL would otherwise create. **Delete BOTH.**
- Reconcile every reference the deletion exposes: `GasViewDirector.daTopologySource` (MonoBehaviour
  field) + the `SnapGridFlowTopologySource` component wired into `GasViewCoarseScene.unity` → re-point
  to the new generator-blind reader→voxelizer path or clear, leaving **NO missing-script GUID**.
- **ZERO-LEGACY acceptance [BUILD-SCAN]:** grep-clean (no `SnapGridFlowRoomReader` / `VScale` /
  `ActiveModel as SnapGridFlowModel` reference remains) AND the tree COMPILES (headless `dotnet build`
  + a clean Editor compile of the scene) AND no missing-script GUID in the scene. A compile break /
  broken scene ref from THIS deletion is a CALL-scoped task, **NOT a STOP-worthy blocker** — complete the delete.
- **SCOPE of ZERO-LEGACY = this dead path ONLY, NOT a tree-wide legacy purge.** `ChunkEncoder.cs`
  (S2 net-replication plumbing) is OUT of S0 scope and stays as-is; its known `(byte)c` chunk-count
  overflow (line 125, §9.8/§14) remains a NAMED deferral (already on the c-exec-009 deferral list),
  NOT folded into S0.

### 3b. KEEP (corrected, with roles)

- **Core keep set** (all verified present + load-bearing in headless Core): `TopologyDocument`;
  `TopologyConformance` (KEEP + EXTEND — see done_when 1); geometry-derived `StableId`
  (`TopologyStableIds`); **RN1** (`IGasReadModel` / `CoarseGasReadModel` — the frozen read-model the
  visual track g-7e15 reads; ADD a per-cell near query, additive); **ROOM-partition / region_id**
  (`CoarseSectorGraph` — the region_id FIELD is NEW, add + thread into the checksum); `RectDecomposition`.
- **KEEP the shared DA→grid plumbing** (NOT the dead path; do not over-delete): `IDaRoomReader`,
  `DaTopologyProducer`, `SceneTopologyComposer`, `FixedLevelRoomReader`. The DA-generated and
  hand-placed levels enter as IDENTICAL engine-free integer boundary DATA via `RoomSpec`/`LinkSpec`
  (`Adapters/Topology/RoomSpec.cs` — engine-free integer DTO, NOT a Core type) — never the DA internal model.
- **KEEP `CoarsePortal` / `TopologyPortalSpec` / the t=mEq/kP orifice for the FAR tier** (S4 rollup
  over the same partition). It is SUPERSEDED for the NEAR grid by the per-face primitive — **do NOT
  delete it** (S4 needs it).

### 3c. OUT OF S0 (building OR gating on any = a STOP-worthy scope violation, NOT progress)

- any lockstep wire or broadcast (S2); the real detail-bubble tier (S2+); authoritative coarse rollup
  / real collapse-expand / LOD-without-pop / re-flux at the moving seam (S4); authoritative checksummed
  HEIGHT-BANDS (S3 — only EMERGENT drain-height from open faces is in S0); breach / pre-declared
  face-flip (S5); burst-on-spawn + object/player displacement (S1); reactions / chemistry table /
  cascade / energy-accumulator (S6).
- **The 3 binding probes are NOT S0 deliverables** and MUST NOT be fabricated as an S0 blocker,
  invoked to STOP the slice, nor authored as S0 RED tests: hangar / weakest-CPU (S4-era); 60-room
  cascade bit-identical (S6); re-flux + breach-mid-collapse (S4/S5, whose binding gate per
  `d-reflux-gate-001` is loopback-one-machine + zero-float, NEVER 2 hardware).

### 3d. LOCK boundary

ведро-classification is WITHIN the LOCK. The LOCK (D1 input-lockstep, D2 one-integer-cell-model,
detail = LOCAL non-authoritative refinement) cracks ONLY via a written **ADR-0010 + owner G9** (the
game-repo writes ADR-0010; authorized by the 2026-06-22 G9 close), NEVER silently inside a PLAN. If a
mechanic appears to need ведро-3 (sub-room AND shared) or any change to D1/D2 → STOP + escalate to the
owner, NOT a PLAN decision.

## 4. DONE_WHEN (each clause tagged by verification surface)

PLAN-approved (owner present).

**(1) VOXELIZER `[HEADLESS-RED]`**
- **PLACEMENT (hard):** the voxelizer AND the doorway→open-faces integer function are built in
  `Assets/GasCoopGame/Core/**` (engine-free, integer-only, inside `GasCoopGame.Core.csproj` — a
  `using UnityEngine` or `using DungeonArchitect` there FAILS the dependency-boundary gate by
  construction). DA + hand levels enter as IDENTICAL engine-free integer boundary data
  (`RoomSpec`/`LinkSpec`), never the DA internal model. CONSEQUENCE: DA-vs-hand byte-identical
  voxelization is a HEADLESS RED test in `tests/GasCoopGame.Core.Tests`, authored BEFORE build. A
  voxelizer built in `Adapters/**` (outside the gated csproj, where the binding test cannot be authored
  headlessly) is a STOP-discipline-v8 SUBSTITUTION and FAILS this clause.
- **gas cell = gas_res = 50cm GLOBAL authoritative** (gas-cellsize §10/R7 — a CAPTURE of the lock,
  not a change). This pins the grid dimension for the voxelization-determinism RED test. 25cm is NOT
  an authoritative grid / cell / room size in S0 — it returns ONLY as an off-checksum local visual
  bubble in a later slice (S3+). The remaining knobs (tier radii, gas-cap magnitudes,
  big-room-authoritative threshold) stay PLAN-decided and MUST NOT be frozen by done_when.
- **resolution_tag = the integer PAIR (geometry_res, gas_res)**, default (50,50), with the
  build-enforced invariant **geometry_res = an integer multiple of gas_res** (geometry NEVER finer than
  gas; 75 against gas=50 is REJECTED). `TopologyConformance` pins the mapping (a 100cm geometry face =
  a 2×2 patch of 50cm gas faces) and rejects any non-integer-multiple geometry_res. **S0 STARTS at
  geometry=50cm (1:1 with gas)**, drives determinism + Conformance green, THEN switches to 100cm by
  CONFIG (not a rebuild). The hot-path face-flow operator never sees geometry after voxelization.
- **IDENTICAL = byte-identical on the canonical voxelization tuple per cell** — {integer cell
  coordinate, region_id label, per-face open/closed bitmap (6 faces), reserved per-face attribute
  fields} — serialized in canonical order (sort by region_id, then integer coord; NEVER container
  order). The DA-vs-hand RED test feeds both inputs and asserts equality of this exact tuple stream
  (or its meaning-checksum) field-by-field.
- **openFaces(opening_descriptor, cell_grid) → an ORDERED set of face-ids** (canonical sort by integer
  cell coord (z,y,x), then face-axis); its COUNT is the emergent open-face area and MUST equal what the
  face-flow law (clause 2) consumes. The descriptor is integer-only (AABB + sill-lower-edge + span, in
  cells), total and deterministic (re-run = byte-identical ordered set). `TopologyConformance` is
  EXTENDED (additive) to ADMIT a near-grid document only if openFaces is total + deterministic over
  every opening; the scalar `OpeningSize`/`SillBandLowerEdgeHeight` portal check is superseded ONLY for
  the NEAR grid — KEEP `TopologyPortalSpec` for the far-tier S4 rollup.

**(2) FACE-FLOW `[HEADLESS-RED]`**
- Gas fills a room by integer face-flow (gather-then-apply + carry). The law **CONSUMES open-face
  count as DATA** — it is the named near supersede of the area-blind t=mEq/kP (locked; gas-model §9.1,
  R6 HARD «площадь проёма всегда влияет на поток»). A flat per-face transfer that ignores area FAILS.
- RED tests (headless, integer, Core/**): **(a) MONOTONIC** — fixed non-equilibrium gradient, sweep
  open-face count 1→N on an otherwise identical room pair; per-tick transferred mass is non-decreasing
  in N and strictly greater for at least one increase (a flow constant across the whole sweep FAILS);
  **(b) SLIT-SEEPS** — flow strictly >0 for the smallest single open face (carry/remainder must never
  seal a slit to 0; §13.5); **(c) WALL-ZERO** — a fully closed boundary transfers exactly 0;
  **(d) MASS-CONSERVATION** — integer gather-then-apply + carry conserves total mass across ticks;
  **(e) EMERGENT HEIGHT** — a low doorway drains only the low cells (no gas above the sill crosses).
  Equilibrium guard: measure only while a gradient exists (a legitimate 0-at-equilibrium law must not
  false-fail).

**(3) SANDBOX (owner SEES) `[owner-visible gizmos + HEADLESS-RED snapshot schema]`**
- gizmos show level→grid(faces)+region_id; pause / slow / step; scenario-as-DATA (anti-scene-sprawl).
- the structured snapshot is a STABLE, VERSIONED, integer-valued record with a NAMED schema exposing —
  per cell — exactly the meaning fields clause (4) reserves (integer coordinate, region_id, per-face
  open/closed + reserved face-attribute fields, the GAP socket values: cap stub, tick_divisor=1,
  resolution_tag pair) plus the per-tick meaning-checksum. The snapshot and the owner-eye gizmos read
  the SAME canonical record (one source of truth). RED test: the snapshot of a known fixture matches
  its declared schema + integer values; a schema-version bump is required on field add/remove.

**(4) §9 SEAMS as DATA day-one `[HEADLESS-RED schema-presence each, indexed by deliverable-coverage v7]`**
A field added later is a breaking checksum-schema migration on the live 2–8 nodes → it MUST lie
day-one; ENABLING any of these is a LATER slice — S0 ships the fields STUBBED only; numeric tuning
stays PLAN-decided.
- **per-face state primitive** = a per-face record carrying, as INTEGER fields present day-one with
  inert defaults (no behavior in S0): (a) open/closed; (b) integer conductivity (stub = full when open,
  0 when closed — no partial-block logic); (c) direction-mask (stub = bidirectional); (d) breach/explosion
  threshold integer (stub = none/disabled). Part of the checksummed face record. RED: each sub-field
  EXISTS with its inert default (so S1/S5 breach=face-flip and partial-block are a data write, not a
  primitive rewrite — the "keep-open not welded shut" rule).
- **SPARSE active-front flux-register** = an integer flux + CARRY (remainder) value per ACTIVE face
  only (faces of awake cells), implicit-zero for quiet faces (loss-free fine→fine); only non-zero
  entries fold into the meaning-checksum (active-set keyed, canonical order — quiet faces NOT folded).
  RED: carry field present; quiet faces absent from the checksum.
- **representation_tag** {fine-3D | mid-2.5D | coarse | bucket} (enum values illustrative,
  PLAN-tunable) as its own §9.2 axis; **resolution_tag** = the (geometry_res, gas_res) pair (clause 1).
  Both folded into the checksum.
- **region_id** folded into the checksum (the `CoarseSectorGraph` region_id field is NEW — add + thread).
- **the 4 GAP sockets, present-but-stubbed:** GAP-1 cap = {max_mass, rate_limit, dissipation} in the
  checksum, stub DISABLED (max_mass = ∞-sentinel, rate_limit/dissipation = 0); GAP-4 per-region
  tick_divisor in the checksum, stub = 1; GAP-2 void/exterior region_id sink = a reserved distinguished
  label (a constant that EXISTS, is DISTINCT from every interior region_id the voxelizer produces, and
  is the canonical drain target for open-to-exterior faces); GAP-3 resolution_tag pair (above). RED:
  schema-presence each with its stub default.
- **collapse/expand interface** = pure integer functions typed PER-REGION/PER-LAYER and mass-exact
  (sum of an input column == output total to the bit), routing any transfer through the §9.3
  flux-register remainder (carry-conserving), carrying an explicit remainder so the real S4
  largest-remainder impl is a BODY swap not a signature change; the signature MUST NOT be able to
  express collapsing a column into one averaged/pre-divided scalar. It RESERVES the temperature carrier
  as the integer PAIR {energy_sum, capacity_sum} (never a pre-divided mean; §9.6 idempotent-collapse) —
  a reserved data shape ONLY; **NO temperature behavior / NO live accumulator / NO energy field is
  built in S0** (that is S6). S0 ships the IDENTITY body only. RED: (a) collapse∘expand round-trips a
  multi-layer column unchanged to the bit and preserves the {energy_sum, capacity_sum} pair; (b) a stub
  variant returning a divided/averaged scalar FAILS the shape assertion.
- **checksum-covers-MEANING** extended to per-face open/closed state, region_id, AND
  representation/resolution tags, plus a CANONICAL-order digest of the active-front/active-set (sort by
  (tick, region_id, species-id) — species-id is a RESERVED comparator slot day-one since S0 has no gas
  types; NEVER container order; per-cell/per-face fields sorted by cell coord). BINDING via a NEGATIVE
  control per meaning-dimension: a mutation that flips a face open/closed OR changes a cell's region_id
  OR changes a representation/resolution tag while holding every numeric mass/flux VALUE byte-equal MUST
  change the meaning-checksum; a control perturbing a non-meaning field (a preserved-canonical-order
  container permutation, or a non-checksummed scratch value) MUST NOT change it. Each control authored
  RED before build.

**(5) DETERMINISM-BY-CONSTRUCTION `[BUILD-SCAN]` (CONFIRMED-CLEAN framing — do NOT turn this into a 2-machine gate)**
- integer-only authoritative path.
- a build-time **ZERO-FLOAT scan wired as a GATE STEP in `tools/check.ps1`** (run on one machine) over
  `Assets/GasCoopGame/Core/**` — the AUTHORITATIVE integer path (voxelizer + face-flow + checksum). It
  FAILS the build (non-zero exit) if any IEEE-754 floating type (`float`/`System.Single`,
  `double`/`System.Double`) appears on the authoritative path (`decimal` is likewise disallowed by the
  integer-only rule; the float ban is the load-bearing cross-CPU guarantee). The non-authoritative
  sandbox/gizmo/render/owner-eye code is NOT scanned. **RED control:** a planted float on the
  authoritative path FAILS the scan; the clean path PASSES. A green build with NO scan step present
  does NOT satisfy this clause — prose alone does not.
- this zero-float scan ON ONE MACHINE **IS** the cross-CPU guarantee (integer cross-CPU equality is a
  GIVEN, not proven; NO 2nd physical machine).
- an OPTIONAL one-machine 2-process loopback hash = an ordering/RNG tripwire (NOT a gate); its real home is S2.
- **ANTI-OVERREACH:** NO RED test (builder OR independent test-author) may require a 2nd physical
  machine or a 2-hardware run. The re-flux / moving-seam probe is OUT of S0 (S4/S5); its binding gate is
  loopback-one-machine + zero-float, NEVER 2 hardware. The loopback tripwire stays permitted (NO re-flux
  bans the moving-seam probe, NOT the loopback lint).

**(6) ZERO-LEGACY `[BUILD-SCAN]`** — per §3a (delete set + grep-clean + compiles + no missing-script GUID).

**(7) OWNER-EYE gate `[OWNER-RUN, binding, no self-marking]`**
- ALL `[HEADLESS-RED]` + `[BUILD-SCAN]` clauses GREEN (authored by the independent test-author BEFORE
  build; the builder cannot edit) BEFORE the owner-eye gate is offered.
- **«точно» (correct) is DISCHARGED by the green headless/build suite** (clauses 1/2/4/5/6), NOT by
  owner self-marking. **«весело» (fun) is the ONLY genuinely non-unit-testable axis** — owner-run. The
  phrase "non-unit-testable" applies ONLY to «весело». An owner sign-off does NOT substitute for a
  missing or red test (the c-exec-012 self-certified-approval pattern is thereby blocked).
- the owner opens the sandbox, sees level→grid + gas filling, and signs «весело» (early).

## 5. STOP-discipline v8 (named)

A blocked/infeasible named approach or a crutch = mandatory STOP + escalate with options, never a
silent substitute. **FORBIDDEN substitutions/descopes** (each = mandatory STOP + escalate, never silent):
- (i) any vertical-stretch / VScale-style scaling crutch in place of true per-face geometry voxelization;
- (ii) scene-tags / scene-component markers as the geometry/measurement source (the read is
  generator-BLIND: a marker says WHAT, measurements are DERIVED from built geometry);
- (iii) a stored area scalar in place of area = open-face COUNT (the area-blind t=mEq/kP orifice is
  superseded near and must NOT return);
- (iv) reading the DA internal model anywhere in the tree;
- (v) a float fast-path on the authoritative path;
- (vi) shipping the named approach at REDUCED FIDELITY — face-flow that ignores opening area, flow that
  seals a single open face to 0, or a voxelizer that only handles axis-aligned trivial rooms.

**Fidelity floor that may NOT be silently dropped:** opening AREA always affects flow AND a single open
face seeps (>0, never seals to 0) — R6 / P6.

## 6. EVIDENCE (return)

A RESULT: voxelizer + face-flow + gizmo sandbox + identical DA/hand voxelization + the GREEN headless
RED suite + the zero-float scan green + grep-clean ZERO-LEGACY + owner «весело» sign. Plus: the scene;
a gizmo capture; a sample structured-snapshot log; assumptions/cuts/mechanic-classification (ведро-1/2/3);
ADR-0010 IF any lock-adjacent classification was made (else a one-line note that none was needed).
**next = S1 CALL** (выброс-при-спауне + выдавливание).

## 7. BUDGET

A focused span; PLAN first. If the voxelizer / face-flow looks infeasible or costly → STOP and escalate
with options, never substitute or crutch.

## 8. Residual risks carried into the PLAN (flag, not fix in S0)

- numeric tuning beyond gas=50cm (tier radii, gas-cap magnitudes, big-room-authoritative threshold,
  return-from-far variant) stays deliberately OPEN (gas-model §13 / dev-plan §3) — PLAN-decided, do NOT
  freeze in done_when.
- `ChunkEncoder.cs:125` `(byte)c` silent overflow (>255 chunks, hash stays green) is a REAL known bug
  but OUT of S0 build scope (S2 net plumbing) — stays a named deferral; the PLAN states explicitly that
  `ChunkEncoder` is KEPT (not in the deleted path), so ZERO-LEGACY is unambiguous.
- the §Re-sync v7→v8 must actually wire deliverable-coverage over the S0 done_when promises, else the
  seam-presence/coverage indexing won't bite.

END_OF_FILE: live/indie-game-development/work/c-exec-013-call.md
