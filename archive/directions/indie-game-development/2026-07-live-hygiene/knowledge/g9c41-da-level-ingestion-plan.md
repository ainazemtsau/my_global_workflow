# Knowledge — DA level-ingestion + object-placement plan (g-9c41)

read_by: the Lv-ingest executor (Phase 0 build + Phase 1 real-DA), and any level/world slice. Source: research
workflow wf_745d3a1f (2026-07-09), grounded in installed DA v1.22.0 source + DA docs + first-hand reads. Fuller
toolchain gotchas also in the owner's memory `gascoopgame-dungeon-architect-integration`.

## The confirmed architecture — 3 lanes that must not cross
1. **Unity / DA (generation, art):** SnapGridFlow (SGF) stitches hand-authored room-MODULE prefabs on a 3D grid via
   a flow graph, seeded by `DungeonConfig.Seed` (`new System.Random((int)Seed)`). Runtime trigger: `SetSeed(seed)` →
   `Dungeon.Build()` — SYNCHRONOUS (asyncBuild=false default), so the whole level exists when Build() returns.
2. **The bridge (our generator-blind reader, engine-free output):** after build, `BuiltSceneRoomReader` walks the
   spawned GameObjects, matches DA's `SnapGridFlowModule`/`SnapConnection` by TYPE NAME (no DA assembly ref), measures
   renderer bounds, quantizes to 50cm integer cells, canonical order → a plain integer `TopologyDocument`. No Unity/DA
   type passes this line.
3. **Engine-free Core (sim):** `Voxelizer.Voxelize(doc, apertures, res)` → authoritative 50cm gas `CellGrid` +
   25cm `StructureGrid`; sim runs.

## Generator choice = SnapGridFlow (owner-confirmed 2026-07-09)
SGF is DA's most advanced ROOM/MODULE-based 3D system (discrete room prefabs, multi-floor) — it manipulates ROOMS,
not tiles. It is the ONLY builder our reader reads out of the box (already lists SnapGridFlowModule/SnapConnection).
Rejected: the classic **Grid Builder** (the owner's remembered "~Simple Grid") and **GridFlow** — both TILE-based
(per-tile markers, no room objects) → would need new engine-side room-reconstruction. GridFlow noted as the fallback
only if organic/cave layouts are ever wanted (but it stays tile-based).

## Game-start flow (Phase 1 target)
A thin Unity `LevelBootstrap : DungeonEventListener` on the Dungeon GameObject: session handshake gives a shared seed →
`SetSeed(seed)` → `Build()` → `OnPostDungeonBuild` (the last, all-present hook) → run the proven
`DaTopologyProducer(BuiltSceneRoomReader)` → `Voxelizer` → read gas sources → seed → playable. NEVER `RandomizeSeed()`
(it uses UnityEngine.Random, uncoordinated).

## Object / gas-source placement (owner's «метко» instinct, confirmed native)
A `GasSourceMarker` MonoBehaviour (tag + design payload typeId/mass/continuous) on a source prefab. DA places it
seed-deterministically via its Theme/Marker system (SGF: a named `PlaceableMarker` + a "Spawn Items" node). A
generator-blind `BuiltSceneGasSourceReader` reads it by type name → engine-free `GasSourceSpec{X,Y,Z,TypeId,Mass}` →
`GasSourceSeeder` → `VoxelField.SeedMass`. Sources stay OUT of the TopologyDocument (mass ≠ geometry → topology
ProfileHash/grid identity stay source-independent).

## Lockstep determinism
The level is a SESSION-START input (Fact 5 base→raid boundary), NOT per-tick: every peer builds from the SHARED seed
locally → same level (same Unity build → same System.Random). Do NOT trust DA GameObjects byte-identical; trust the
QUANTIZED integer TopologyDocument + exchange its **ProfileHash** at handshake → abort-on-mismatch (clean, not silent
desync). 50cm quantization absorbs sub-cell float wobble. Point sources need a floor-based `ContainingCell` + a
cell-centre pivot to avoid boundary-flip.

## TWO load-bearing gotchas
1. **DA ships ZERO content** (no module DB / flow graph / room prefabs; 28 prefabs are config skeletons). A real SGF
   build needs owner-manual DA authoring (mostly editor, not code). → **Phase 0** proves the whole seam on HAND-TAGGED
   geometry (100% code/MCP) BEFORE paying that cost; **Phase 1** swaps the real DA build behind the UNCHANGED reader.
2. **Current continuous-source injection is in `VoxelSandboxDirector`** (a NON-authoritative render adapter, OUTSIDE
   the checksum) → would DESYNC in the real game. Per-tick source injection MUST move INTO the authoritative engine-free
   sim step, keyed by the ingested specs, inside the MeaningChecksum. This is the meatiest correctness piece of Phase 0.

## Two-phase plan
- **Phase 0** (c-exec-lv-ingest-phase0-001, 100% code/MCP): GasSourceMarker + engine-free GasSourceSpec/reader/seeder +
  move injection into the authoritative sim step + `LatticeQuantize.ContainingCell`; test scene (2 rooms + door + source)
  → gas flows from a placed source through the door. Proves the entire last mile + the new source seam, no DA authoring.
- **Phase 1** (framed on Phase 0 green): minimal SGF module set + flow graph + `LevelBootstrap` + seed/ProfileHash
  handshake; the SAME reader/seeder unchanged.

## MCP-vs-owner split (owner's hard rule: no crutches)
Code / prefab / component / test-scene = assistant via Unity-MCP. DA Theme/Flow **graph authoring = owner-manual,
step-by-step**. Setting an asset→component Object-reference via MCP is UNVERIFIED (may need owner drag). Where MCP can't
do a step → STOP + hand the owner instructions, NEVER a workaround. Unity/MCP unavailable → STOP + ask owner. See
[[feedback-no-crutch-checks-venue-unavailable-stops]].

## Deferred (named, not lost)
DA one-way/locked doors → our ValveSpec mapping; SGF item-spawner seed-varied placement (Phase 0 hand-places); the
seed/ProfileHash multiplayer handshake wiring (Phase 1+); pin the DA version + a same-seed-twice determinism test
(DA had a historical "SGF non-deterministic first build" bug, reportedly fixed).

## Code anchors (GasCoopGame @defade72)
`Assets/GasCoopGame/Adapters/Topology/`: BuiltSceneRoomReader.cs (generator-blind, type-name match, 50cm quantize),
DaTopologyProducer.cs (IDaRoomReader seam; the "DA reader does not exist yet" comment is STALE — BuiltSceneRoomReader
fills that role), GasRoomMarker.cs/GasDoorMarker.cs (tag pattern to mirror). `Core/Field/Voxel/Voxelizer.cs`,
`VoxelField.cs` SeedMass (apply-or-throw), `CellGrid.cs` TryGetCellAt. `Core/Field/Topology/Ingestion/LatticeQuantize.cs`
(add ContainingCell). `Adapters/GasView/VoxelSandboxDirector.cs` ComputeSourceCells/InjectSource (the injection to
MOVE into the sim). DA: `Assets/CodeRespawn/DungeonArchitect/Scripts/` — Core/Dungeon/Dungeon.cs (Build/SetSeed),
Core/Dungeon/DungeonEventListener.cs (OnPostDungeonBuild), Builders/SnapGridFlow/, Core/Frameworks/Snap/SnapConnection.cs.

END_OF_FILE: live/indie-game-development/knowledge/g9c41-da-level-ingestion-plan.md
