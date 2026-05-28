# Old Project Grid / Gas Interaction Technical Facts

Status: C2 source extraction artifact
Created: 2026-05-14
Old project source: `C:\Users\Anton\TheLastExit`
Goal: `core-technical-foundation-decision-brief`

## Boundary

This document maps old-project interaction facts between Grid and Gas. It does not decide whether the interaction model should be transferred, rewritten, or discarded.

## Source Anchors

- `Assets/_Project/Modules/GasV2R/Gas.Foundation/Runtime/IGasGridEventHandler.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Foundation/Runtime/GasGridIntegrationService.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Foundation/Runtime/GasRuntimeInstaller.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Foundation/Runtime/GasT1RuntimeService.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Foundation/Runtime/GasT2RuntimeService.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Foundation.Tests/EditMode/GasRuntimeGridIntegrationTests.cs`
- `Assets/_Project/Modules/Grid/Core/Events/GridEvents.cs`
- `Assets/_Project/Modules/Grid/Core/Events/IGridEventListeners.cs`
- `Assets/_Project/Modules/Grid/Core/Events/GridSpatialEventBus.cs`
- `Assets/_Project/Modules/Grid/Core/Topology/RoomTopologyGraph.cs`
- `Assets/_Project/Modules/Grid/Core/Topology/PortalEdge.cs`
- `Assets/_Project/Modules/Grid/Core/Rooms/RoomInfo.cs`
- `Assets/_Project/Modules/Grid/Core/Rooms/IRoomAnchorReadModel.cs`
- `Assets/_Project/Modules/Grid/Core/Services/GridDoorCommandService.cs`
- `Assets/_Project/Modules/Grid/Core/Interfaces/IGridCore.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Topology/Data/TopologyRuntimeState.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Topology/Validation/GasTopologyStartupValidator.cs`
- `Assets/_Project/Modules/GasV2R/Gas.T1/Runtime/GasT1RoomConnectionGraph.cs`
- `Assets/_Project/Modules/GasV2R/Gas.T1/Runtime/GasT1RoomTransportKernel.cs`
- `Assets/_Project/Modules/GasV2R/Gas.T2/Runtime/GasT2RuntimeState.cs`
- `Assets/_Project/Modules/GasV2R/Gas.T2/Runtime/GasT2RoomDistributionState.cs`
- `docs/grid-system/architecture.md`
- `docs/grid-system/analysis/rooms-topology.md`
- `docs/gas-system/decisions-map/gas-grid-integration.md`
- `docs/gas-simulation-v2/modules/Gas.Foundation/README.md`
- `docs/gas-simulation-v2/gas-game-and-simulation-transfer-brief.md`

## Explicit Gas Event Bridge

- `IGasGridEventHandler` is the explicit Gas-side bridge contract for Grid changes.
- `IGasGridEventHandler.RebuildFromGrid(IGridCore gridCore)` rebuilds a handler from the current Grid state.
- `IGasGridEventHandler.OnGridInitialized(GridInitializedEvent gridEvent, IGridCore gridCore)` handles Grid initialization.
- `IGasGridEventHandler.OnTopologyChanged(TopologyChangedEvent gridEvent, IGridCore gridCore)` handles topology changes.
- `IGasGridEventHandler.OnDoorPortalStateChanged(DoorPortalStateChangedEvent gridEvent)` handles door/portal state changes.
- `GasGridIntegrationService` implements Grid listener interfaces and forwards Grid events to a list of `IGasGridEventHandler` implementations.
- `GasGridIntegrationService` requires `IGridCore` and at least one handler. It throws a Foundation validation exception when the handler list is empty.
- On initialization, `GasGridIntegrationService` rebuilds all handlers if `IGridCore.IsInitialized` is already true.
- The service forwards Grid initialized, topology changed, and door portal state changed events to every registered Gas handler.
- `GasRuntimeInstaller` binds `GasGridIntegrationService` alongside the runtime loop, T1 runtime service, and T2 runtime service.

## Gas Handlers

- `GasT1RuntimeService` implements `IGasGridEventHandler`. It rebuilds from Grid, reacts to Grid initialization, reacts to topology changes, and updates connection state on door portal state changes.
- `GasT1RuntimeService` also implements runtime command/read surfaces, including room injection and world-position injection. The world-position path requires Grid room resolution.
- `GasT2RuntimeService` implements `IGasGridEventHandler`. It rebuilds from Grid data and consumes Grid room anchor data through `IRoomAnchorReadModel`.
- T2 anchor projection maps Grid room anchors into Gas T2 distribution/primitive anchor concepts. Missing or invalid anchor data is treated as a validation failure.

## Grid Event And Door Data Used By Gas

- Grid provides `GridInitializedEvent`, `TopologyChangedEvent`, and `DoorPortalStateChangedEvent`.
- `DoorPortalStateChangedEvent` includes stable door id, representative cell, open state, sorted room ids, cell count, source, actor id, and timestamp.
- `IGridCore` exposes door lookup by connecting rooms or cell, door ids in a room, door info, door cells, door open state, set/toggle commands, and room lookup.
- `GridDoorCommandService` is a command facade over the Grid door APIs. It does not own separate door truth.
- `PortalEdge` and room topology graph data provide room-to-room portal/connection facts used by consumers such as Gas.

## Door / Portal / Topology Coupling

- Grid owns room and door/portal authority in the inspected legacy integration path.
- Gas receives Grid-level events through `GasGridIntegrationService`; Gas handlers then rebuild or update their runtime state.
- T1 converts room adjacency/door information into gas room connection behavior. Closed-door state can block overflow/flow; open-door state can allow transfer.
- Gas topology has its own runtime connection/door state through `TopologyRuntimeState`, including portal mapping, deterministic connection lookup, and door state versions.
- T2 depends on Grid room anchors during rebuild for local distribution placement and anchor projection, rather than deriving all local structure from gas mass alone.
- The old docs state that Gas should not directly access Grid storage internals. The inspected bridge aligns with that: it uses `IGridCore`, Grid events, and read models instead of raw Grid storage mutation.

## Test Anchors

- `GasRuntimeGridIntegrationTests.cs` contains a two-room fake Grid core with a stable door id and explicit open/closed door behavior.
- Test coverage includes a closed door blocking overflow flow until an open event arrives.
- Test coverage includes open-door transfer behavior when overflow is not blocked.
- Test coverage includes closed-door overflow staying within the source room and raising pressure.
- Test coverage includes preserving mass for matching rooms during rebuild policy.
- Test coverage includes a Grid event bus door update changing T1 connection state.
- Grid event source anchors include `GridEvents.cs`, `IGridEventListeners.cs`, and `GridSpatialEventBus.cs`.

## Interaction Facts For Future Audit

- The hard interaction boundary is `Grid` as topology/door/anchor authority and `Gas` as tiered simulation consumer.
- The primary bridge contract is `IGasGridEventHandler`.
- The runtime forwarding service is `GasGridIntegrationService`.
- The main door-sensitive simulation consumer found in this pass is T1.
- The main anchor-sensitive simulation consumer found in this pass is T2.
- The inspected interaction is local runtime architecture evidence only. It is not a player-hosted multiplayer replication design.

## Unknowns And Non-Conclusions

- This C2 pass does not decide whether old Grid, GridV2, or a new topology source should feed Gas in the new project.
- This C2 pass does not audit transfer safety, code quality, determinism under network replication, or host/client authority boundaries.
- T2 implements the Grid event handler interface and rebuilds from Grid/anchors, but this pass did not deeply audit door-event-specific downstream behavior inside T2.
- Event ordering and rollback/prediction requirements for player-hosted multiplayer are unresolved.
- The old tests prove selected integration behavior, not full gameplay correctness or production readiness.
