# Old Project Grid / Topology Technical Facts

Status: C2 source extraction artifact
Created: 2026-05-14
Old project source: `C:\Users\Anton\TheLastExit`
Goal: `core-technical-foundation-decision-brief`

## Boundary

This document extracts technical facts from the old project. It is not an A1 transfer audit, not a Unity implementation plan, and not approval to reuse code. It separates old `Grid` facts from newer `GridV2` facts because the two systems have different boundaries and authority models.

## Source Anchors

- `Assets/_Project/Modules/Grid/Core/Project.Grid.Core.asmdef`
- `Assets/_Project/Modules/Grid/Core/Data/CellData.cs`
- `Assets/_Project/Modules/Grid/Core/Chunks/Chunk.cs`
- `Assets/_Project/Modules/Grid/Core/Storage/IGridStorage.cs`
- `Assets/_Project/Modules/Grid/Core/Storage/GridStorage.cs`
- `Assets/_Project/Modules/Grid/Core/Interfaces/IGridCore.cs`
- `Assets/_Project/Modules/Grid/Core/Services/GridCore.cs`
- `Assets/_Project/Modules/Grid/Core/Services/GridDoorCommandService.cs`
- `Assets/_Project/Modules/Grid/Core/Rooms/RoomInfo.cs`
- `Assets/_Project/Modules/Grid/Core/Rooms/RoomRegistry.cs`
- `Assets/_Project/Modules/Grid/Core/Rooms/RoomSourceContracts.cs`
- `Assets/_Project/Modules/Grid/Core/Rooms/RoomSourceExtractionUtility.cs`
- `Assets/_Project/Modules/Grid/Core/Rooms/IRoomAnchorReadModel.cs`
- `Assets/_Project/Modules/Grid/Core/Topology/RoomTopologyGraph.cs`
- `Assets/_Project/Modules/Grid/Core/Topology/GraphBuilder.cs`
- `Assets/_Project/Modules/Grid/Core/Topology/RoomNode.cs`
- `Assets/_Project/Modules/Grid/Core/Topology/PortalEdge.cs`
- `Assets/_Project/Modules/Grid/Core/Topology/TopologyChangeBuffer.cs`
- `Assets/_Project/Modules/Grid/Core/Events/GridEvents.cs`
- `Assets/_Project/Modules/Grid/Core/Events/IGridEventListeners.cs`
- `Assets/_Project/Modules/Grid/Core/Events/GridSpatialEventBus.cs`
- `Assets/_Project/Modules/Grid/Providers/DungeonArchitectAdapter/Runtime/DAGridBuildSink.cs`
- `Assets/_Project/Modules/GridV2/Foundation/README.md`
- `Assets/_Project/Modules/GridV2/Source/README.md`
- `Assets/_Project/Modules/GridV2/Topology/Chambers/README.md`
- `Assets/_Project/Modules/GridV2/Foundation/Storage/IGridStorage.cs`
- `Assets/_Project/Modules/GridV2/Source/Rooms/RoomSourceContracts.cs`
- `Assets/_Project/Modules/GridV2/Source/Rooms/RoomSnapshotValidator.cs`
- `Assets/_Project/Modules/GridV2/Topology/Chambers/Compilation/ChamberGraphCompiler.cs`
- `Assets/_Project/Modules/GridV2/Topology/Chambers/Runtime/ChamberGraphRuntimeStore.cs`
- `Assets/_Project/Modules/GridV2/Tests/EditMode/Foundation/GridV2FoundationAuditTests.cs`
- `Assets/_Project/Modules/GridV2/Tests/EditMode/Chambers/ChamberGraphCompilerTests.cs`
- `Assets/_Project/Modules/GridV2/Tests/EditMode/Chambers/ChamberGraphDeterminismTests.cs`
- `Assets/_Project/Modules/GridV2/Tests/EditMode/Chambers/ChamberGraphRuntimeStoreTests.cs`
- `docs/grid-system/architecture.md`
- `docs/grid-system/analysis/rooms-topology.md`
- `docs/grid-system-transfer-brief.md`
- `docs/specs/2026-03-14-gridv2-topology-graph-boundary-opening-authority-block-a-chamber-graph-core-spec.md`

## Grid Core Facts

- `Project.Grid.Core` is the older runtime grid authority. It owns cell data, chunk-backed storage, coordinate conversion, passability queries, room queries, door queries, topology, and Grid events.
- Cell storage is chunk-oriented. The inspected anchors include `CellData`, chunk coordinate helpers, `IGridStorage`, and `GridStorage`.
- `IGridCore` is the central facade. It exposes world/cell conversion, cell reads/writes, passability, neighbors, room lookup, room membership, room adjacency, door lookup, door mutation, and Burst-compatible access.
- `RoomInfo` is a blittable summary of a room. It stores room id, cell counts, floor cell count, bounds, volume, floor area, center of mass, neighbor count, door count, and flags. The helper marks large rooms and multi-floor rooms from cell count and height.
- `RoomRegistry` and the room source contracts are the room authority surface. The old docs describe flood-fill room detection and source-authored room snapshots as relevant room inputs.
- The room source path separates semantic/source data from low-level room facts. Anchors include `IRoomSemanticSourceReadModel`, `IRoomAnchorReadModel`, source room snapshots, portal snapshots, and room anchor snapshots.
- The topology graph is represented by `RoomTopologyGraph`, `RoomNode`, and `PortalEdge`. `GraphBuilder` builds room-to-room connectivity from the registry and door/portal data.
- Door state is part of Grid authority. `IGridCore` exposes stable door ids, door cells, door info, open/closed state, set/toggle commands, and room-door lookup. `GridDoorCommandService` is a thin command facade over those `IGridCore` door APIs.
- Grid events include `GridInitializedEvent`, `TopologyChangedEvent`, entity movement events, and `DoorPortalStateChangedEvent`.
- `DoorPortalStateChangedEvent` carries a stable door id, representative cell, open/closed state, sorted room ids, door cell count, source, actor id, and timestamp.
- `GridSpatialEventBus` is a deterministic phased event bus. It queues events by phase, scope, and cadence, validates cascade depth, rejects backward phase publish, and dispatches by global, room, or chunk scope.
- The Dungeon Architect adapter exists as a provider adapter. `DAGridBuildSink` and related adapter files feed Grid, but the inspected Grid Core facts do not require treating Dungeon Architect as the new project's source of truth.

## GridV2 Facts

- `GridV2` is a newer isolated grid/topology redesign under `Project.GridV2.*`, not a compatibility bridge for `Project.Grid.Core`.
- `GridV2.Foundation` is the low-level substrate. Its README says it owns cell data, chunk helpers, neutral storage, and explicit projection, while avoiding legacy room/topology authority.
- `GridV2.Source` owns immutable input contracts and validation. Its anchors include `RoomSnapshot`, `IRoomSource`, `RoomSourceImportPipeline`, `ManualRoomSourceComponent`, and `RoomSnapshotValidator`.
- `GridV2.Topology.Chambers` is the first runtime authority layer in the inspected GridV2 path. Its data flow is source rooms to chamber graph compilation, then publish into a runtime store.
- `ChamberGraphCompiler` creates one chamber per source room, validates the room snapshot, assigns deterministic chamber ids, and carries source region keys from source room instance keys.
- `ChamberGraphRuntimeStore` publishes a staged immutable graph and indexes by chamber id and cell. It fails fast on invalid graph data such as duplicate chamber ids or duplicate cell ownership.
- The GridV2 chamber docs explicitly state that legacy `Grid` remains reference-only for this path and that GridV2 must not take runtime references on `Project.Grid.Core`.

## Grid vs GridV2 Distinction

- `Grid` is the older broad runtime system with `IGridCore`, rooms, doors, event bus, topology graph, provider adapters, and known Gas integration surfaces.
- `GridV2` is the newer boundary-opening/topology redesign with isolated assemblies, source snapshots, chamber graph compilation, and runtime graph storage.
- The two systems should not be collapsed into one fact set. Old Gas integration anchors primarily target `Grid` and `IGridCore`; GridV2 anchors show a possible newer topology direction but not a proven Gas runtime integration in the inspected material.

## Test And Documentation Anchors

- `Assets/_Project/Modules/GridV2/Tests/EditMode/Foundation/GridV2FoundationAuditTests.cs`
- `Assets/_Project/Modules/GridV2/Tests/EditMode/Source/*`
- `Assets/_Project/Modules/GridV2/Tests/EditMode/Chambers/ChamberGraphCompilerTests.cs`
- `Assets/_Project/Modules/GridV2/Tests/EditMode/Chambers/ChamberGraphDeterminismTests.cs`
- `Assets/_Project/Modules/GridV2/Tests/EditMode/Chambers/ChamberGraphRuntimeStoreTests.cs`
- `Assets/_Project/Modules/GridV2/Tests/EditMode/Chambers/ChamberGraphProbeBootstrapTests.cs`
- `docs/grid-system/architecture.md` describes Grid Core as the spatial foundation and lists consumers such as Gas, Debug, and Tests.
- `docs/grid-system/analysis/rooms-topology.md` documents room registry flood fill, multi-cell door handling, room adjacency, CSR-style graph structures, and Grid-to-Gas topology mapping concepts.
- `docs/grid-system-transfer-brief.md` distinguishes main `Grid` from `GridV2` and frames old Grid as source material for future decisions.
- `docs/specs/2026-03-14-gridv2-topology-graph-boundary-opening-authority-block-a-chamber-graph-core-spec.md` records the GridV2 hard root break and no-runtime-reference rule from GridV2 to legacy Grid.

## Unknowns And Non-Conclusions

- This C2 pass did not decide whether old `Grid`, `GridV2`, or a new topology design should be transferred.
- This C2 pass did not audit code quality, multiplayer suitability, serialization behavior, or Unity version compatibility.
- The new project's room identity model, cell scale, authoring source, door authority, and topology rebuild policy are still undecided.
- GridV2 has strong isolation/test anchors, but this pass did not prove it is feature-complete for old Grid/Gas parity.
- The old Dungeon Architect adapter is a source anchor only; it is not a decision to depend on Dungeon Architect in the new project.
