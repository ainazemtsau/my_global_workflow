# Core Technical Foundation Decision Brief / Decision Map

## 1. Decision summary

This brief records the current accepted foundation direction for the new co-op project.

The accepted multiplayer default is FishNet + Steamworks / Steam Networking / Steam Datagram Relay for a player-hosted architecture with no dedicated authoritative server. Photon Fusion 2 remains a fallback / paid acceleration path, not the default.

The old Grid, GridV2, GasV2R, and Grid-Gas interaction evidence are treated as source-grounded technical evidence, not as direct reuse approval. Grid/Topology and Gas Simulation transfer safety remain A1 audit surfaces.

The next safe work is not implementation. The next safe work is review/distill of this decision brief, then precise A1/E1/C1/C2 routing only where required.

## 2. Foundation surface status map

| Surface | Status | Decision / gate |
| --- | --- | --- |
| Multiplayer technology and host-player architecture | decided | FishNet + Steamworks / Steam Networking / Steam Datagram Relay is the default. Photon Fusion 2 is fallback / paid acceleration path. Architecture is player-hosted, with no dedicated authoritative server. |
| Host migration policy | deferred_not_blocking_for_bootstrap | Seamless host migration is not MVP acceptance. MVP may end session, return to lobby, or support manual/guided rehost. Architecture must preserve migration-addability seams. |
| Grid / Topology transfer boundary | audit_needed_A1 | Old Grid and GridV2 / Chamberline-style topology must not be collapsed. No direct reuse or rewrite verdict is made in F0. |
| Gas Simulation durable logic architecture | audit_needed_A1 | GasV2R tiered evidence is preserved as candidate architecture input. Direct reuse, production readiness, multiplayer suitability, and performance are unresolved. |
| Grid-Gas interaction | decision_gate | Old interaction evidence shows Grid as topology/door/anchor authority and Gas as event-consuming tiered simulation. Network authority/order/prediction remains gated. |
| Smallest durable technical nucleus | decision_gate | Minimal validation nucleus is identified, but not implemented. |
| Project Engineering & Codex Development Operating Model | decided | Domain-first, testable core; Unity mainly render/presentation shell; adapter boundaries; Codex execution only after route, bindings, validators, and scope are explicit. |

## 3. Accepted multiplayer foundation policy

Default path:

- FishNet + Steamworks / Steam Networking / Steam Datagram Relay.
- Player-hosted / listen-host co-op.
- No dedicated authoritative server for MVP baseline.

Fallback path:

- Photon Fusion 2 remains fallback / paid acceleration path if FishNet + Steamworks validation fails or becomes disproportionately expensive.

Rejected baseline:

- Full per-tick full-state Grid/Gas replication.
- Dedicated-server-first design by default.
- Reopening FishNet vs Fusion without a blocking contradiction or Human Decision.

Replication direction:

- Hierarchical event / delta / snapshot / interest-based synchronization.
- Stable domain identifiers for rooms, chambers, doors, portals, entities, and interest groups.
- Domain simulation must not depend directly on transport endpoint details.

## 4. Host migration and host-loss policy

Status: deferred_not_blocking_for_bootstrap.

MVP host-loss behavior may be:

- session ends;
- return to lobby;
- manual or guided rehost.

Required migration-addability seams:

- stable Room / Chamber / Door / Portal / Entity / InterestGroup IDs;
- compact authoritative snapshots;
- late-join / rejoin bootstrap path;
- transport abstraction;
- domain-level snapshot capture/apply hooks;
- interest/relevance groups for room/chamber/proximity/hotness.

Seamless host migration is not an MVP blocker.

## 5. Grid / Topology transfer boundary

Status: audit_needed_A1.

Preserved C2 facts:

- Old Grid is a broad runtime authority with IGridCore, room/door/topology surfaces, event bus, provider adapters, and known Gas integration surfaces.
- GridV2 is a newer isolated topology redesign with source snapshots, chamber graph compilation, runtime graph storage, and tests.
- Grid and GridV2 are separate fact sets and must not be collapsed into one reuse verdict.

F0 non-verdict:

- no direct transfer approval;
- no rewrite mandate;
- no Unity/code transfer;
- no claim that GridV2 is feature-complete for new project Grid/Gas parity.

Next route:

- A1 audit for Grid/GridV2 transfer boundary, serialization, test coverage, multiplayer suitability, and new-project topology authority.

## 6. Gas Simulation durable architecture boundary

Status: audit_needed_A1.

Preserved C2 facts:

- GasV2R evidence shows a tiered model: Config / Foundation / Topology / T1 / T2 / T3.Data / Interest.
- T1 is room-level authority evidence.
- T2 is room-local distribution / reconciliation evidence.
- T3.Data and Interest are local detail, visual/query, LOD, and network/streaming relevance evidence.
- Fail-fast validation and fixed-tick host-control surfaces are important architecture signals.

F0 non-verdict:

- GasV2R is not declared production-ready.
- GasV2R is not declared directly reusable.
- Multiplayer replication, prediction, bandwidth, player-hosted authority, target scale, and performance remain unaudited.

Next route:

- A1 audit for GasV2R transfer / rewrite boundary.
- E1/C1 only after audit produces exact implementation scope and validators.

## 7. Grid-Gas interaction boundary

Status: decision_gate.

Preserved C2 facts:

- Old interaction path uses Grid as topology / door / anchor authority.
- Gas consumes Grid events through IGasGridEventHandler and GasGridIntegrationService.
- T1 reacts to topology and door state.
- T2 depends on Grid room anchors.
- Old tests cover selected local runtime behavior but not full multiplayer correctness.

Decision gate:

- choose whether new topology authority is old Grid, GridV2-derived, or new design;
- define event ordering and authority boundaries for player-hosted networking;
- define snapshot/delta surfaces before implementation.

## 8. Smallest durable technical nucleus / validation gates

Status: decision_gate.

Minimal nucleus to validate next:

- FishNet + Steamworks / SDR binding path;
- player-host session flow;
- Steam lobby / transport bootstrap;
- stable Room / Chamber / Door / Portal IDs;
- compact T1 room-level snapshot boundary;
- limited T2 local distribution slice;
- interest/relevance grouping;
- late-join / rejoin bootstrap shape;
- procedural animation sync boundary as separate from Gas/Grid truth.

Validation gates before implementation:

- concrete Unity project/tool bindings;
- exact transport adapter boundary;
- domain snapshot schema;
- deterministic or testable simulation core surfaces;
- validators for acceptance;
- explicit route to C1/C2 only after E1.

## 9. Project Engineering & Codex Development Operating Model

Status: decided.

Operating model:

- Domain-first code.
- Unity is primarily render/presentation shell.
- Core gameplay/simulation logic must be testable outside scene-specific MonoBehaviour surfaces.
- Multiplayer transport is adapter/boundary layer, not domain truth.
- Composition root / dependency assembly belongs at project boundary.
- Codex output is blocked until route, scope, project/tool bindings, validators, and acceptance checks are explicit.

Not included:

- full engineering handbook;
- final DI package;
- final Unity folder layout;
- CI setup;
- implementation code.

## 10. Explicit non-goals

This artifact does not:

- create a Unity project;
- transfer code;
- perform A1 audit;
- run Codex product/project execution;
- create Task Master graph;
- promote content to Game Documentation;
- reopen S3 accepted multiplayer policy;
- declare Grid, GridV2, or GasV2R directly reusable;
- require seamless host migration for MVP;
- define full gas taxonomy or final performance model.

## 11. Next routes

Primary next route:

- R1_GOAL_REVIEW_DISTILL reviews this F0 artifact against the Goal Contract and Phase minimum outcome.

Likely downstream gates:

- A1_AUDIT for Grid/GridV2 transfer boundary.
- A1_AUDIT for GasV2R transfer / durable architecture boundary.
- E1_EXECUTION_BRIEF before any implementation route.
- C1_CODEX_GRAPH_PLAN / C2_CODEX_EXECUTE only after concrete project/tool bindings and validators exist.
- S3_DECIDE only if accepted FishNet default, Photon fallback, host migration policy, or Game Documentation promotion is reopened.

## 12. Acceptance checklist

- [ ] Artifact exists at the active Goal path.
- [ ] Title anchor exists: `# Core Technical Foundation Decision Brief / Decision Map`.
- [ ] Multiplayer surface is `decided`.
- [ ] FishNet + Steamworks / SDR is default.
- [ ] Photon Fusion 2 remains fallback / paid acceleration path.
- [ ] Architecture is player-hosted / no dedicated authoritative server.
- [ ] Host migration is `deferred_not_blocking_for_bootstrap`.
- [ ] Migration-addability seams are listed.
- [ ] Grid/Topology boundary is `audit_needed_A1`.
- [ ] Grid and GridV2 are not collapsed.
- [ ] Gas Simulation boundary is `audit_needed_A1`.
- [ ] T1/T2/T3/Interest model is preserved as evidence, not reuse verdict.
- [ ] Grid-Gas interaction is `decision_gate`.
- [ ] Smallest durable technical nucleus is listed without implementation.
- [ ] Project Engineering & Codex model is `decided`.
- [ ] No code, Unity project, Codex product execution, Task Master graph, or Game Documentation promotion is included.