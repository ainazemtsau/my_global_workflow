# Old Project Gas Simulation Technical Facts

Status: C2 source extraction artifact
Created: 2026-05-14
Old project source: `C:\Users\Anton\TheLastExit`
Goal: `core-technical-foundation-decision-brief`

## Boundary

This document extracts source-grounded facts about the old Gas Simulation implementation. It is not a transfer audit, not a production-readiness verdict, and not a multiplayer networking decision.

## Source Anchors

- `Assets/_Project/Modules/GasV2R/README.md`
- `Assets/_Project/Modules/GasV2R/Gas.Config`
- `Assets/_Project/Modules/GasV2R/Gas.Foundation`
- `Assets/_Project/Modules/GasV2R/Gas.Foundation/Runtime/GasRuntimeInstaller.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Foundation/Runtime/GasRuntimeLoopService.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Foundation/Runtime/GasT1RuntimeService.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Foundation/Runtime/GasT2RuntimeService.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Foundation/Runtime/GasGridIntegrationService.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Foundation/Runtime/IGasGridEventHandler.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Foundation.Tests/EditMode/GasRuntimeGridIntegrationTests.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Topology`
- `Assets/_Project/Modules/GasV2R/Gas.Topology/Data/TopologyRuntimeState.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Topology/Validation/GasTopologyStartupValidator.cs`
- `Assets/_Project/Modules/GasV2R/Gas.Topology.Tests`
- `Assets/_Project/Modules/GasV2R/Gas.T1`
- `Assets/_Project/Modules/GasV2R/Gas.T1/Runtime/GasT1RuntimeState.cs`
- `Assets/_Project/Modules/GasV2R/Gas.T1/Runtime/GasT1RoomConnectionGraph.cs`
- `Assets/_Project/Modules/GasV2R/Gas.T1/Runtime/GasT1RoomTransportKernel.cs`
- `Assets/_Project/Modules/GasV2R/Gas.T1.Tests`
- `Assets/_Project/Modules/GasV2R/Gas.T2`
- `Assets/_Project/Modules/GasV2R/Gas.T2/Runtime/GasT2RuntimeState.cs`
- `Assets/_Project/Modules/GasV2R/Gas.T2/Runtime/GasT2RoomDistributionState.cs`
- `Assets/_Project/Modules/GasV2R/Gas.T2.Tests`
- `Assets/_Project/Modules/GasV2R/Gas.T3.Data`
- `Assets/_Project/Modules/GasV2R/Gas.T3.Data/Runtime/GasT3RoomActivationBuilder.cs`
- `Assets/_Project/Modules/GasV2R/Gas.T3.Data/Runtime/GasT3RoomSeedingBuilder.cs`
- `Assets/_Project/Modules/GasV2R/Gas.T3.Data/Runtime/GasVisualFieldBridge*`
- `Assets/_Project/Modules/GasV2R/Gas.T3.Data.Tests`
- `Assets/_Project/Modules/GasV2R/Gas.Interest`
- `Assets/_Project/Modules/GasV2R/Gas.Interest/Runtime/GasRoomInterestBuilder.cs`
- `docs/gas-simulation-v2/modules/Gas.Foundation/README.md`
- `docs/gas-simulation-v2/modules/Gas.Topology/README.md`
- `docs/gas-simulation-v2/modules/Gas.T1/README.md`
- `docs/gas-simulation-v2/modules/Gas.T2/README.md`
- `docs/gas-simulation-v2/modules/Gas.T3/playtest.md`
- `docs/gas-simulation-v2/gas-game-and-simulation-transfer-brief.md`
- `docs/gas-system/decisions-map/gas-grid-integration.md`
- `docs/GasTestLab_Documentation_v1`

## Root And Module Boundary Facts

- `GasV2R` is identified by its README as the allowed runtime implementation root for the gas restart. Older Gas roots are reference material.
- The inspected GasV2R implementation is split into modules/tier surfaces: `Gas.Config`, `Gas.Foundation`, `Gas.Topology`, `Gas.T1`, `Gas.T2`, `Gas.T3.Data`, and `Gas.Interest`.
- The module docs describe a deterministic, fail-fast approach: invalid config, missing runtime dependencies, duplicate topology data, and impossible simulation inputs are expected to fail early rather than degrade silently.
- The docs and runtime services use fixed-tick concepts and host control. The inspected runtime is not a free-running visual-only effect.

## Gas.Config Facts

- `Gas.Config` supplies runtime configuration assets used by the installer and runtime services.
- `GasRuntimeInstaller` expects serialized config assets such as simulation, T1 runtime, and T2 runtime config assets.
- Missing config assets are treated as validation failures rather than optional defaults.

## Gas.Foundation Facts

- `Gas.Foundation` owns runtime orchestration surfaces: fixed tick scheduling, command buffering, telemetry/control, runtime loop service, Grid integration, and public runtime command/read models.
- `GasRuntimeLoopService` implements the runtime tick loop and host control. It requires at least one gas tick consumer.
- Runtime tick ordering is explicit. The inspected installer/loop path resolves `GasT1RuntimeService` before `GasT2RuntimeService`.
- `GasRuntimeInstaller` binds the production runtime services, including T1, T2, `GasGridIntegrationService`, and the runtime loop.
- Foundation exposes Grid event bridge contracts through `IGasGridEventHandler` and the integration service.

## Gas.Topology Facts

- `Gas.Topology` owns deterministic topology state for gas. `TopologyRuntimeState` tracks rooms, cell-to-room lookup, room connections, portal mapping, door state versions, active/pending topology versions, and deterministic room/neighbor queries.
- `GasTopologyStartupValidator` builds validated topology state and checks non-empty sources, positive unique room ids, non-empty room cells, no duplicate cell ownership, and neighbor integrity/symmetry.
- Connection ids are deterministic. The validator builds connection ids from sorted room pairs and creates default door states.
- The module docs describe topology as the contract surface consumed by T1, loading/runtime modules, and T3-style local detail.

## Gas.T1 Facts

- `Gas.T1` is the room-level simulation tier. It handles deterministic tick progression, positioned injection, room capacity/pressure, source events, portal flux events, and mass transfer across room connections.
- `GasT1RuntimeService` implements `IGasTickConsumer`, `IGasRuntimeCommands`, `IGasT1ReadModel`, and `IGasGridEventHandler`.
- T1 can queue injection by room and by world position. The world-position path requires Grid access for room resolution.
- T1 rebuilds from Grid initialization and topology change events, and it updates its room connection state on door portal state changes.
- The inspected T1 runtime uses a room connection graph, transport kernel, capacity/pressure model, and runtime state objects.

## Gas.T2 Facts

- `Gas.T2` is a room-local distribution memory tier. Its docs describe ambient room mass plus bounded primitives, with reconciliation against T1 room mass.
- `GasT2RuntimeService` implements `IGasTickConsumer`, `IGasGridEventHandler`, `IGasT2RuntimeCommands`, `IGasT2ReadModel`, `IGasT1T2ParityReadModel`, and `IGasT2AnchorProjectionReadModel`.
- T2 rebuilds from Grid data and requires `IRoomAnchorReadModel` for room anchor projection. Missing anchor data is a validation failure.
- T2 runtime state and room distribution state enforce constraints such as bounded primitive count, non-negative mass, and reconciliation between T1 mass and T2 ambient-plus-primitive mass.
- The inspected T2 module also contains airflow, primitive lifecycle, anchor affinity, reactions, replication/sync snapshots, and traffic counter surfaces.

## Gas.T3.Data Facts

- `Gas.T3.Data` contains local field/detail data structures and builders. Inspected anchors include room activation, room seeding, brick keys/configuration, local dynamics data, and visual field bridge code.
- Transfer brief text cautions that T3 should not be assumed to be a fully proven always-on per-tick simulation pass in the active runtime.
- A verified visual bridge path exists through seeded cells / T2-derived data, but this C2 pass did not prove a complete T3 gameplay simulation loop.

## Gas.Interest Facts

- `Gas.Interest` contains room interest, LOD, hotness, hotspot priority, and overlay snapshot logic.
- The transfer brief frames Interest as a way to limit local detail, streaming, and network traffic by prioritizing rooms or regions.
- Inspected anchors include `GasRoomInterestBuilder`, interest set/entry/LOD data, streaming hotness helpers, hotspot priority helpers, and overlay snapshot builders.

## Durable Facts

- The old gas design is tiered: topology and Grid integration feed room-level T1 simulation; T2 reconciles room-local distribution to T1 authority; T3.Data and Interest provide local detail/query/visual/LOD surfaces where active.
- T1 is treated as the authoritative room mass tier in the docs inspected for transfer context.
- T2 is bounded by configuration and reconciles to T1 mass rather than replacing T1.
- Grid integration is event-driven through Foundation contracts, not based on direct polling of Grid storage internals.
- The implementation repeatedly uses fail-fast validation for missing config, missing Grid/anchor dependencies, invalid room data, duplicate topology data, negative mass, unknown rooms, and invalid substance/mass inputs.

## Test And Evidence Anchors

- `Gas.Foundation.Tests/EditMode/GasRuntimeGridIntegrationTests.cs` covers Grid integration behaviors including door-state changes, overflow flow blocking, open-door transfer, mass preservation policy, and event bus door update behavior.
- `Gas.Topology.Tests` covers topology validation, deterministic state, room lookup, connection state, pending topology flush semantics, and runtime lab evidence.
- `Gas.T1.Tests` covers room injection, transport, runtime state, connection graph behavior, pressure/overflow behavior, and runtime lab paths.
- `Gas.T2.Tests` covers primitive lifecycle, T1/T2 reconciliation, portal flux/inflow handling, reaction budget/apply behavior, replication contracts, sync snapshots, and runtime lab evidence.
- `Gas.T3.Data.Tests` and `docs/gas-simulation-v2/modules/Gas.T3/playtest.md` provide T3 data/playtest evidence anchors.
- `docs/gas-simulation-v2/gas-game-and-simulation-transfer-brief.md` provides cross-module transfer context, including cautions around unproven runtime assumptions.

## Unknowns And Non-Conclusions

- This C2 pass does not conclude that GasV2R is directly reusable in the new project.
- Multiplayer replication authority, prediction, bandwidth, and player-hosted network behavior were not audited.
- T3.Data has evidence anchors, but this pass does not prove a complete always-on T3 simulation pipeline.
- Some module docs describe active or in-progress slices; this pass records those facts but does not resolve completion status.
- Performance at target player count, map scale, gas substance count, and Unity runtime target was not validated.
- Visual fidelity, UX readability, and gameplay tuning were not evaluated.
