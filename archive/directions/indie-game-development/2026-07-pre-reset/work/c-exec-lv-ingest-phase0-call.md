# CALL c-exec-lv-ingest-phase0-001 — Level ingestion + gas-source placement, PHASE 0 (engine-free seam on hand-tagged geometry)

**STATUS: SUPERSEDED BEFORE BUILD / NOT DELIVERED / NEVER RESUME.** The accepted replacement route is
`GasCoopGame_dev@f5c1d650:docs/gas-simulation/PROGRAM.md`. This file remains historical evidence only; no section
below is executable authority. Any request to continue Phase 0 returns to current DirectionS routing in NOW.md.

## why now / lineage
Sc-damage is HELD (needs design; canon core is being re-assembled). This is the owner-chosen canon-independent engine
work: complete the level-ingestion path so a real generated level (Phase 1 = Dungeon Architect **SnapGridFlow**,
owner-confirmed) feeds the authoritative gas grid **with gas SOURCES placed as objects**. Research 2026-07-09
(workflow wf_745d3a1f) → **knowledge/g9c41-da-level-ingestion-plan.md** (read it first). Phase 0 (this CALL) proves the
ENTIRE ingestion + source seam on **HAND-TAGGED geometry — 100% code/MCP, NO Dungeon Architect authoring** — isolating
CODE risk from DA-authoring risk. Phase 1 (real DA) later swaps the real build behind the UNCHANGED reader.

## goal (outcome, not method)
On a test scene of hand-tagged geometry (2 rooms + 1 door + 1 gas-source marker in room A), at **Play** the pipeline
reads the scene → voxelizes into the authoritative 50cm gas grid → seeds the placed gas source → **gas flows from the
source through the door into room B** — with the gas SOURCE now living in the **AUTHORITATIVE, deterministic,
engine-free path (inside the lockstep MeaningChecksum)**, not the render adapter. Owner SEES gas emerge from a placed
object and creep through the door: "a placed thing is making gas here."

## the model (properties to honour + RECORD on the PLAN)
1. **GasSourceMarker (Unity adapter — tag + payload only).** A MonoBehaviour in `Adapters/Topology`, parallel to
   GasRoomMarker/GasDoorMarker: `int TypeId, int Mass (rate), bool Continuous`. Its POSITION is MEASURED from the
   transform, never stored (contract v8 anti-substitution). No Unity/DA type leaks past the reader.
2. **Engine-free spec + generator-blind reader.** `struct GasSourceSpec { int X,Y,Z,TypeId,Mass; bool Continuous }`
   (engine-free, analog of RoomSpec). A `BuiltSceneGasSourceReader` (sibling to BuiltSceneRoomReader) finds
   GasSourceMarker by TYPE NAME, quantizes world position → cell via the SAME LatticeQuantize + axis map
   (worldX→volX, worldZ→volY, worldY-up→volZ), emits a canonically-sorted `List<GasSourceSpec>`. Sources stay OUT of
   DaLevel/SceneTopologyComposer/TopologyDocument (mass ≠ geometry → topology ProfileHash / grid identity stay
   source-independent).
3. **Engine-free seeder + INJECTION MOVED INTO THE AUTHORITATIVE SIM STEP (the desync fix — meatiest piece).**
   `GasSourceSeeder` resolves (X,Y,Z)→cell via `CellGrid.TryGetCellAt` → `VoxelField.SeedMass(cell,typeId,mass)`,
   apply-or-throw (LOUD on out-of-grid miss). CRITICAL: move the per-tick CONTINUOUS source injection OUT of
   `VoxelSandboxDirector` (non-authoritative render adapter — `ComputeSourceCells`/`InjectSource`) INTO the
   authoritative engine-free sim step, keyed by the ingested specs, so every peer injects the same integer mass at the
   same integer cell each tick — INSIDE the MeaningChecksum. (Today's adapter-side injection WOULD desync in the real
   game — SPEC §3 "что БЬЁТ читает грубое авторитетное на каждом пире".)
4. **Deterministic point-source quantization.** Add engine-free `LatticeQuantize.ContainingCell` (floor, span
   [k·cell,(k+1)·cell)) for point sources; author the source pivot near a cell CENTRE. Integer-only; NO float on the
   authoritative path.
5. **Owner-eye (owner-run, no self-marking).** A test scene (MCP-buildable: GasRoomMarker/GasDoorMarker/GasSourceMarker
   on simple axis-aligned boxes) where at Play gas emerges from the placed source and creeps through the door.

## boundaries (out of scope / STOP-escalate if tempted)
- **NO Dungeon Architect authoring / NO real DA build this phase** (that is Phase 1). **NO DungeonArchitectRoomReader**
  (keep the reader generator-blind — a DA assembly ref breaks R13 engine-free Core).
- **NO multiplayer seed/ProfileHash handshake wiring** this phase (single-peer proof; handshake is Phase 1+). But the
  source injection MUST be checksum-correct so the handshake later "just works".
- NO DA one-way/locked-door → ValveSpec mapping (deferred). NO new gas types. NO visual/shader pipeline. NO
  damage/Sc-sense/Sc-damage edits. NO env-typing.
- NO float on the authoritative path; NO silent source-cell miss (loud throw); NO source injection left in the render
  adapter; NO stored velocity; integer-only in headless Core/**.

## done_when (verifiable)
1. **PLAN (owner-readable, contract v19):** §Re-sync at tip; ingest knowledge/g9c41-da-level-ingestion-plan.md + SPEC
   (§3 authoritative read, §4 seam 5/7 checksum, Факт-1 determinism) + this CALL; RECORD: change class
   (authoritative-path integration), the source seam design (i)–(iv), the injection-into-sim decision + how it folds in
   the MeaningChecksum, the quantization choice, the ADR-E number, the test gas + scenarios, and the **MCP-vs-owner-step
   split** for the Unity scene work.
2. **Independent RED test-author FIRST** (separate BUILD session): REDs for — position→cell quantization deterministic
   (containing-cell floor, boundary-biased positions), GasSourceSeeder apply-or-throw (out-of-grid = loud), continuous
   injection in the authoritative step is BYTE-IDENTICAL across two loopback peers AND folded in the gas MeaningChecksum,
   a NO-source scene reproduces the prior gas golden byte-identically, a planted float/adapter-side/silent-miss
   realization FAILS.
3. **Build:** GasSourceMarker (Unity adapter) + engine-free GasSourceSpec / BuiltSceneGasSourceReader / GasSourceSeeder
   / LatticeQuantize.ContainingCell; continuous injection MOVED into the authoritative sim step (removed from the render
   adapter). Bind the next free ADR-E-*.
4. **Determinism + scans:** integer-only authoritative path; new authoritative Core dir in BOTH zero-float + int-overflow
   scans + planted-violation self-test; loopback determinism green over a source-in-scene seeded run.
5. **`check.ps1 -Deliver` GREEN** at tip (synced ≥18, v19 behavioural); mutation ≥70 on new engine-free Core;
   negative-control per acceptance property; review-evidence + reviewed-commit ancestry; **fresh-session cross-family G5
   could-not-refute** on: source-in-authoritative-path / deterministic-position→cell / no-regression-byte-identical /
   consequence-free-source / no-float.
6. **OWNER-EYE (owner-run):** in the test scene, gas emerges from the placed source and creeps through the door; reads
   as "a placed object makes gas here." (If a scene/asset step is not MCP-able → owner does it by step-by-step
   instruction and confirms.)

On GREEN → the **Phase 1** CALL frames (real DA SnapGridFlow: minimal module set + flow graph + `LevelBootstrap`
runtime Build at game-start + seed/ProfileHash session handshake; the SAME reader/seeder unchanged).

## return
RESULT routed HOME: outcome + evidence (commits, -Deliver transcript, mutation json, negative-control, review-evidence +
G5 verdict + family, loopback source-identity hash + RED-control trips, the PLAN decisions, the injection-move diff,
the ADR-E number, the owner-eye source→flow verdict) + the **MCP-vs-owner-step log** (which steps the assistant did via
MCP, which the owner did by hand). dev→main merge + push OWNER-GATED.

## budget
One bounded integration slice — the read/voxelize path already exists and is proven; the NEW work is the gas-source seam
+ moving continuous injection into the authoritative step + the test scene. Keep it tight; do not drift into DA authoring
(Phase 1) or multiplayer handshake (Phase 1+).

END_OF_FILE: live/indie-game-development/work/c-exec-lv-ingest-phase0-call.md
