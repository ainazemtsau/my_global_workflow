# H1_G4B Goal Contract — Grid / Topology Foundation

```yaml
artifact_control:
  artifact_name: "H1_G4B Goal Contract — Grid / Topology Foundation"
  schema: goal_contract.v1
  owner_layer: direction
  status: goal_shaped_pending_E1_execution_brief
  direction_id: indie_game_development
  phase_id: h1-g4b-grid-topology-foundation
  goal_id: h1-g4b-grid-topology-foundation
  shaped_by_stage: G1_GOAL_SHAPE
  formalized_at: "2026-05-23"
  next_route: E1_EXECUTION_BRIEF
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
```

## Goal

Produce or route-gate a production-grade, legacy-informed Grid / Topology Core for GasCoopGame.

The Grid is the central spatial/topology substrate of the level. It owns stable spatial identity, topology representation, dynamic topology state, deterministic topology query/update, and spatial change propagation. It must not become a god-object and must not own every game system's domain simulation.

## WHY now

H1_G4A accepted the core harness / composition / validation / topology interface foundation. That gave the product a topology seam and execution boundary, but not the topology substrate itself.

H1_G4B must now produce the actual Grid / Topology foundation before future Gas Simulation Foundation, Grid-Gas Interaction, and Multiplayer Boundary work can safely build on it.

## WHAT

Build or route-gate a durable Grid / Topology Core that supports:

- level topology ingestion through a replaceable reader/parser/adapter boundary;
- runtime Grid topology state;
- cells/nodes/rooms/regions/boundaries identity model;
- adjacency/connectivity semantics;
- walls/doors/openings/holes/blockers semantics;
- dynamic topology mutation for destruction/opening/blocking changes;
- deterministic step/query/update surface;
- spatial change propagation model;
- cross-system spatial coordination contract;
- validation/debug/inspection surface;
- legacy-informed architecture rationale;
- product evidence packet.

## DONE

The Goal is complete only when R1 later accepts product evidence proving:

- topology cells/nodes/rooms/regions/boundaries exist;
- adjacency/connectivity semantics exist;
- walls/doors/openings/holes/blockers semantics exist;
- Grid can build/load runtime topology from a level/generator/scene/source boundary;
- the ingestion source is replaceable without rewriting core Grid;
- dynamic topology mutation can reflect opening/blocking/destruction changes;
- deterministic step/query/update surface exists;
- spatial changes are exposed through events, change sets, dirty regions, versioning, or another justified model;
- other systems can map/query/publish/observe spatially indexed data without Grid becoming owner of each domain simulation;
- validation/debug/inspection evidence exists;
- old Grid/GridV2/GasV2R/Grid-Gas evidence was reviewed or exact missing context was requested;
- product persistence evidence exists.

OR when a concrete blocker/unblock packet explains why the topology foundation cannot safely be produced yet and what exact route resolves it.

## Minimum Complete Outcome

One complete topology substrate loop:

```text
level topology ingestion
-> runtime Grid topology state
-> dynamic topology mutation
-> deterministic query/update
-> spatial change propagation
-> validation/debug evidence
-> product evidence
```

Not enough:

- only an interface;
- only a document;
- only a toy/demo Grid;
- only hard-coupled tag parsing;
- only old-code transfer;
- only tests disconnected from product behavior;
- only visualization without topology semantics;
- Grid that cannot support future system coordination.

## Required Capabilities

```yaml
required_capabilities:
  topology_ingestion:
    required: true
    description: >
      Grid must build runtime topology from level data after the level exists
      or is generated. Grid does not own level generation.
    replaceable_boundary_required: true
    default_candidate_to_inspect:
      - tag_or_marker_based_scene_parser_from_old_project
    possible_sources:
      - manually_authored_scene_or_prefab_markers
      - Dungeon_Architect_generated_output
      - other_generation_plugin_output
      - baked_topology_asset
      - future_custom_adapter
    forbidden:
      - hard_couple_core_grid_to_tag_parsing_forever
      - hard_couple_core_grid_to_Dungeon_Architect
      - make_grid_responsible_for_procedural_generation

  topology_model:
    required: true
    includes:
      - cells_or_nodes
      - rooms_or_regions_when_useful
      - boundaries_or_edges
      - walls
      - doors
      - openings
      - holes
      - blockers
      - stable_spatial_identity

  connectivity:
    required: true
    includes:
      - adjacency
      - open_connections
      - closed_or_blocked_connections
      - connected_or_disconnected_regions
      - query_surface

  dynamic_topology:
    required: true
    includes:
      - opening_created_or_removed
      - blocker_added_or_removed
      - wall_destroyed_or_changed
      - door_opened_or_closed
      - connectivity_invalidated_or_recomputed
      - deterministic_mutation_surface

  cross_system_spatial_coordination:
    required: true
    description: >
      Grid provides shared spatial identity and topology. Other systems own
      their own domain state and optimized layouts.
    supports:
      - external_systems_mapping_data_to_cells_or_regions
      - external_systems_querying_topology_or_connectivity
      - external_systems_reacting_to_topology_or_spatial_changes
      - future_gas_simulation_reading_topology_without_owning_topology
      - future_temperature_like_system_registering_spatial_values_without_grid_owning_temperature_simulation
      - future_interaction_or_destruction_systems_publishing_topology_mutations

  spatial_change_model:
    required: true
    acceptable_forms_to_research:
      - events
      - batched_change_sets
      - dirty_regions
      - versioned_updates_or_snapshots
      - reactive_subscriptions
      - command_commit_notification
      - justified_hybrid_model
    performance_guardrail: >
      Avoid naive per-cell event spam for large grids. Prefer batching,
      dirty regions, change sets, or versioning if required by old evidence
      or target performance constraints.

  deterministic_surface:
    required: true
    includes:
      - deterministic_step_or_commit_boundary
      - deterministic_query_results_for_same_state_and_inputs
      - Unity_frame_order_independence_where_needed

  validation_debug_surface:
    required: true
    includes:
      - tests_or_validation_harness
      - Unity_debug_view_or_manual_debug_checklist_when_useful
      - operator_readable_changed_files_rationale
      - product_evidence_packet
```

## Legacy Research Gate

```yaml
legacy_research_gate:
  required_before_X1: true
  source_policy: >
    Old project material is evidence/source material, not automatic production base.
    Direct old-code transfer is forbidden. Old ideas, algorithms, invariants,
    tests, and performance lessons may be reused after review.
  must_inspect_or_request:
    - old Grid/GridV2 architecture
    - old tag/marker/scene parser behavior
    - old room/wall/door/opening/hole/blocker model
    - old Grid tests
    - old performance tests/benchmarks/profiling notes
    - old GasV2R constraints relevant to topology
    - old Grid-Gas interaction assumptions
  required_outputs_before_execution:
    - reusable_old_ideas_and_invariants
    - rejected_old_assumptions
    - selected_ingestion_architecture
    - selected_topology_representation
    - selected_change_propagation_model
    - selected_cross_system_spatial_coordination_contract
    - exact_missing_context_if_old_source_tests_are_unavailable
    - route_decision_for_E1_A1_D1_Context_Request_S3_or_Stop
```

## Scope In

- production-grade Grid / Topology Core;
- level topology ingestion;
- replaceable ingestion boundary;
- legacy tag/marker parser inspection;
- runtime topology state;
- cells/nodes/rooms/regions/boundaries;
- adjacency/connectivity;
- walls/doors/openings/holes/blockers;
- dynamic topology mutation;
- deterministic step/query/update;
- spatial change propagation;
- cross-system spatial coordination;
- validation/debug/inspection;
- legacy-informed architecture rationale;
- product evidence or blocker/unblock packet.

## Non-goals / Responsibility Boundary

```yaml
grid_boundary_non_goals:
  generation:
    statement: >
      Grid does not generate levels. It ingests topology from level/generator
      output through a replaceable ingestion boundary.

  domain_simulation:
    statement: >
      Grid does not simulate gas, temperature, fan behavior, AI, or gameplay
      systems. It provides topology/spatial substrate and change/query
      contracts for them.

  old_code:
    statement: >
      Grid does not directly copy old code. Old code/docs/tests/perf are
      evidence used to derive architecture, invariants, requirements, and
      validation.

  god_object:
    statement: >
      Grid must not become a storage bucket for all game state. External
      systems own their own domain data and register/query spatially through
      clear contracts.

  source_coupling:
    statement: >
      Grid core must not be permanently coupled to tags, Dungeon Architect,
      or any single ingestion source.
```

## Acceptance Floor

The smallest acceptable result is a product-facing Grid / Topology Core that can be inspected and validated as a durable foundation.

It must not be a throwaway prototype. It must be small enough to finish, but strong enough that future Gas, Grid-Gas, destruction/interaction, temperature-like systems, and multiplayer boundary can build on it without replacing the core for ordinary growth.

## Validation Signal

- product evidence packet;
- validation command/result or Unity/manual debug checklist;
- changed-files rationale;
- topology substrate inspectability;
- legacy-informed architecture rationale;
- old-evidence sufficiency result or exact missing-context request.

## Route

Next stage:

```text
E1_EXECUTION_BRIEF
```

E1 must not route to X1 until the legacy research gate and architecture sufficiency gate are resolved.

## Stop Conditions

Stop or route-gate if:

- old Grid/Gas evidence is required but unavailable;
- old source/tests/perf context is required but not accessible;
- ingestion architecture would hard-couple Grid core to one source;
- selected design turns Grid into a god-object;
- event/change model is unproven for expected scale;
- validation/debug surface cannot prove topology behavior;
- execution would become blind rewrite;
- execution would copy old code directly;
- execution expands into Gas Simulation Foundation, Grid-Gas Interaction, Multiplayer Boundary, Unity MCP setup, Task Master graph creation, Game Documentation promotion, or broad vertical slice work.

## Map / Graph Binding

```yaml
map_binding:
  initiative_id: innovative-commercial-expedition-gas-sim-game
  node_or_edge: H1_playable_technical_nucleus / H1_G4B_grid_topology_foundation
  expected_map_delta_after_R1_acceptance:
    - H1_G4B_grid_topology_foundation accepted or route-gated
    - H1_G4C_gas_simulation_foundation may become the next candidate if topology substrate is accepted
    - H1_G4D_grid_gas_interaction remains parked until Grid and Gas foundations are available or intentionally scoped together
  why_this_goal_is_minimal: >
    It produces the missing topology substrate after H1_G4A without pulling
    in Gas Simulation, Grid-Gas Interaction, Multiplayer Boundary, broad
    vertical slice work, old-code transfer, or Game Documentation promotion.
```

```yaml
goal_graph_binding:
  phase_delivery_graph_version: phase_delivery_graph.v1
  node_id: h1_g4b_grid_topology_foundation
  node_type: result_slice
  phase_outcome_supported: h1_g4b_topology_foundation_exists
  why_this_goal_advances_node: >
    This is the single required primary result node for the H1_G4B Phase.
  expected_graph_delta:
    if_goal_succeeds:
      - required node can be marked done by R1 after accepted evidence
      - H1_G4B Phase can become P9 close candidate
    if_goal_fails:
      - exact blocker/unblock packet routes to E1/B1/A1/D1/S3/Context Request/Stop
  documentation_admission_required: false
  support_artifact_handling: >
    Research notes, validation report, operator report, and evidence packet
    are support artifacts only. The primary result is the product-facing
    Grid / Topology Core or an exact blocker/unblock packet.
```

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/h1-g4b-grid-topology-foundation/goals/h1-g4b-grid-topology-foundation/00_GOAL_CONTRACT.md`
