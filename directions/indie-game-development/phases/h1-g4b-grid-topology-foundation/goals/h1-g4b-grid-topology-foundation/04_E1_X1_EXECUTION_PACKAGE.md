# H1_G4B E1 Guarded X1 Execution Package — Grid / Topology Foundation

```yaml
artifact_control:
  artifact_name: "H1_G4B E1 Guarded X1 Execution Package — Grid / Topology Foundation"
  schema: e1_x1_execution_package.v1
  owner_layer: direction_goal
  status: formalized_pending_x1_executor_run
  direction_id: indie_game_development
  phase_id: h1-g4b-grid-topology-foundation
  goal_id: h1-g4b-grid-topology-foundation
  stage_id: E1_EXECUTION_BRIEF
  formalized_at: "2026-05-23"
  next_route: X1_EXECUTOR_RUN
  implementation_allowed_now: false_in_chatgpt_e1
  codex_product_execution_allowed_now: true_only_through_this_guarded_x1_package
```

## Route Decision

```yaml
route_decision:
  selected_route: X1_EXECUTOR_RUN
  selected_route_name: "Guarded Codex Executor Run"
  execution_topology: executor_work_package
  route_status: prepared_pending_repository_maintenance_readback
  why_this_route: >
    A1 resolved the legacy Grid / Topology sufficiency blocker enough for
    E1 to prepare a guarded X1 package. The Goal requires product-facing
    Grid / Topology Core implementation and evidence, not another support
    artifact. X1 is allowed only with explicit architecture, validation,
    performance, tooling, and multiplayer-readiness guards.
  alternatives_rejected:
    F0_FAST_DIRECT: "Rejected; this is product/project implementation with architecture-sensitive multi-file validation and Codex handoff."
    X0_EXECUTOR_PROJECT_SETUP: "Rejected unless setup evidence proves stale; GasCoopGame is recorded as setup_complete_external_repo."
    D1_DEEP_RESEARCH: "Rejected for now; A1 resolved legacy evidence enough for guarded execution. Route back if current external/plugin/tooling facts block architecture."
    A1_AUDIT: "Rejected for now; A1 already returned DONE and carried gaps into X1 deliverables."
    S3_DECIDE: "Rejected unless X1 preflight finds a human-owned architecture/tooling tradeoff."
    Context_Request: "Rejected for now; exact Goal, A1 result, guardrail, and project binding were available."
```

## X1 Objective

Execute or route-gate the smallest production-grade H1_G4B Grid / Topology Core slice in GasCoopGame.

Minimum complete loop:

```text
level topology ingestion
-> runtime Grid topology state
-> dynamic topology mutation
-> deterministic query/update
-> versioned change-set / dirty-region spatial change model
-> validation/debug evidence
-> product evidence packet
```

## Mandatory Architecture Selection Gate

X1 must not begin product mutation until it completes a read-only technical discovery / architecture selection preflight.

```yaml
architecture_selection_gate:
  required_before_product_mutation: true
  codex_may_not_silent_choose: true
  inspect:
    - product AGENTS or equivalent project instructions
    - product Module Map / public interface docs / validation profile if present
    - H1_G4A accepted topology interface seam
    - current Grid/topology-related code and tests
    - generated/protected/read-only/plugin surfaces
    - old Grid/GridV2/GasV2R/Grid-Gas evidence when available as evidence only
  compare_representations:
    - dense_grid
    - sparse_or_chunked_grid
    - graph_topology
    - hybrid_grid_plus_region_graph
  comparison_criteria:
    - memory_at_expected_H1_scale
    - adjacency_query_speed
    - connectivity_region_query_speed
    - dynamic_mutation_cost
    - dirty_region_or_change_set_cost
    - doors_walls_openings_holes_blockers_support
    - future_gas_simulation_readiness
    - future_multiplayer_snapshot_delta_readiness
    - deterministic_command_commit_support
    - Unity_debug_and_validation_feasibility
    - module_boundary_and_reuse_fit
  required_pre_mutation_output:
    - selected_topology_representation
    - rejected_alternatives_with_reasons
    - performance_assumptions
    - gameplay_implications
    - future_gas_readiness_implications
    - future_multiplayer_readiness_implications
    - validation_plan
    - stop_or_continue_verdict
  continue_allowed_only_if:
    - selected_architecture_fits_goal_contract
    - no unresolved_plugin_or_DOTS_or_ingestion_source_choice_affects_core
    - no hard_coupling_to_tags_DungeonArchitect_or_Unity_scene_state
    - no material_human_owned_tradeoff_remains
  stop_if:
    - architecture_choice_requires_human_decision
    - plugin_or_DOTS_or_DungeonArchitect_choice_blocks_core_boundary
    - product_module_boundaries_are_unclear
    - old_source_context_is_required_but_unavailable
    - performance_scale_assumptions_cannot_be_set
```

## Required Deliverables

```yaml
deliverables:
  stable_spatial_identity:
    required: true
    includes:
      - stable_ids_for_cells_or_nodes
      - stable_ids_for_regions_or_rooms_when_used
      - stable_ids_for_boundaries_or_edges
      - stable_ids_for_doors_openings_holes_blockers
    forbidden:
      - NetworkObject_as_spatial_identity
      - Unity_scene_object_as_authoritative_identity

  replaceable_topology_ingestion_boundary:
    required: true
    rule: >
      Tags, markers, scene parsers, Dungeon Architect output, baked assets,
      or generator output may feed adapters. None may define or hard-couple
      the core Grid model.
    includes:
      - topology_source_or_adapter_contract
      - at_least_one_concrete_or_fixture_adapter
      - validation_that_core_grid_is_source_agnostic

  runtime_topology_state:
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
      - adjacency
      - open_closed_blocked_connectivity

  dynamic_topology_mutation:
    required: true
    shape: command_validate_deterministic_commit
    examples:
      - door_opened_or_closed
      - blocker_added_or_removed
      - wall_destroyed_or_changed
      - opening_created_or_removed
    output:
      - topology_state_update
      - connectivity_invalidation_or_recompute
      - committed_change_set

  spatial_change_model:
    required: true
    preferred_shape: versioned_batched_change_sets_with_dirty_region_semantics
    forbidden:
      - naive_per_cell_event_spam_at_large_scale
    must_support:
      - future_gas_consumption
      - future_multiplayer_snapshot_delta_or_change_set_export
      - deterministic_replay_or_consistent_ordering_where_needed

  narrow_cross_system_contract:
    required: true
    Grid_may:
      - expose_stable_spatial_ids
      - answer_topology_and_connectivity_queries
      - publish_committed_topology_change_sets
      - expose_dirty_regions_or_versioned_snapshots
    Grid_must_not:
      - own_gas_simulation_state
      - own_temperature_state
      - own_fan_behavior
      - own_AI_state
      - own_multiplayer_transport
      - own_gameplay_domain_state

  foundation_multiplayer_readiness:
    required: true
    includes:
      - stable_ids
      - command_or_intent_input_boundary
      - authoritative_tick_or_explicit_step_or_commit_boundary
      - deterministic_or_server_authoritative_consistency_model
      - snapshot_delta_or_change_set_output_boundary
      - validation_surface
      - performance_or_scale_evidence
    forbidden:
      - FishNet_dependency_inside_Grid_core
      - Steam_dependency_inside_Grid_core
      - RPC_dependency_inside_Grid_core
      - NetworkObject_as_domain_identity
      - local_single_player_only_core_assumptions
```

## Validation Requirements

```yaml
validation_requirements:
  topology_correctness:
    - build_or_load_topology_from_adapter_or_fixture
    - adjacency_and_connectivity_queries
    - blocked_vs_open_connections
    - region_connectivity_if_regions_exist
  mutation_correctness:
    - door_open_close_changes_connectivity_or_state
    - blocker_add_remove_changes_connectivity_or_state
    - wall_destroy_or_opening_create_changes_topology
    - command_validate_commit_boundary_is_deterministic
  spatial_change_model:
    - committed_change_set_contains_expected_delta
    - dirty_region_or_version_increments_as_expected
    - no_required_per_cell_event_spam_for_large_batches
  performance_scale:
    - define_H1_scale_assumptions_before_claiming_performance
    - measure_build_or_load_cost
    - measure_query_cost
    - measure_mutation_batch_cost
    - measure_change_set_or_dirty_region_cost
    - report_allocations_or_hot_path_concerns_when available
  debug_or_manual:
    - Unity_debug_view_or_manual_debug_checklist_when_useful
    - operator_readable_validation_steps
```

## Product Evidence Packet Required

X1 must return an Executor Return Packet or equivalent containing:

```yaml
product_evidence_packet:
  required:
    - product_commit_sha_or_explicit_no_commit_blocker
    - technical_discovery_card
    - selected_architecture_and_rejected_alternatives
    - changed_files_rationale
    - validation_commands_and_results
    - performance_scale_evidence
    - operator_report
    - manual_Unity_debug_checklist_if_needed
    - forbidden_scope_confirmation
    - unresolved_carryovers
```

## Stop Conditions

X1 must stop and return a blocker/unblock packet if:

- product setup evidence is missing or stale;
- product repo/worktree is inaccessible or unsafe to mutate;
- module boundaries are unclear after read-only preflight;
- architecture choice is material and unresolved;
- plugin/DOTS/Dungeon Architect/tooling choice affects Grid core boundary;
- selected design would hard-couple Grid core to tags, scene parser, Dungeon Architect, Unity presentation, or old code;
- stable spatial identity cannot be represented without NetworkObject or Unity scene object authority;
- command/commit dynamic topology mutation cannot be made deterministic enough for foundation acceptance;
- versioned change-set / dirty-region model cannot be validated at expected scale;
- validation/debug evidence cannot prove topology behavior;
- scope expands into Gas Simulation, Grid-Gas Interaction, multiplayer implementation, Unity MCP, Task Master, Game Documentation, or broad vertical slice work.

## Compact X1 Launch Summary

```yaml
next_launch:
  stage_id: X1_EXECUTOR_RUN
  source_path: workflow/stage_prompts/X1_EXECUTOR_RUN.md
  target_runtime: codex
  target_project_ref:
    direction_id: indie_game_development
    project_id: gas_coop_game
    project_name: Gas Coop Game
    expected_repo_or_workspace: ainazemtsau/GasCoopGame
    project_root_pointer: C:\projects\Unity\GasCoopGame
    executor_setup_status: setup_complete_external_repo
  launch_allowed_after:
    - this_file_committed_and_read_back
    - execution_log_append_committed_and_read_back
  prompt_acquisition_policy: >
    Next X1 run must acquire the exact X1 prompt under the runtime context
    acquisition policy before executing.
```

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/h1-g4b-grid-topology-foundation/goals/h1-g4b-grid-topology-foundation/04_E1_X1_EXECUTION_PACKAGE.md`
