# H1_G4B E1 Execution Brief — Grid / Topology Foundation

```yaml
artifact_control:
  artifact_name: "H1_G4B E1 Execution Brief — Grid / Topology Foundation"
  schema: e1_execution_brief.v1
  owner_layer: direction_goal
  status: formalized_pending_A1_audit
  direction_id: indie_game_development
  phase_id: h1-g4b-grid-topology-foundation
  goal_id: h1-g4b-grid-topology-foundation
  stage_id: E1_EXECUTION_BRIEF
  formalized_at: "2026-05-23"
  next_route: A1_AUDIT
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
```

## Route Decision

```yaml
route_decision:
  selected_route: A1_AUDIT
  selected_route_name: "Legacy Grid / Topology Architecture Sufficiency Gate"
  execution_topology: gated_sequential
  why_this_route: >
    The H1_G4B Goal requires a production-grade, legacy-informed Grid /
    Topology Core, but X1 is blocked until old Grid/GridV2/tag parser/tests/
    perf/GasV2R/Grid-Gas evidence is inspected or exact missing context is
    requested. A1 is the smallest safe registry-valid route to challenge
    architecture sufficiency before product execution.
  alternatives_rejected:
    X1_EXECUTOR_RUN: "Rejected until legacy architecture/evidence sufficiency gate passes."
    F0_FAST_DIRECT: "Rejected; work is product implementation, multi-surface, architecture-sensitive, and evidence-dependent."
    D1_DEEP_RESEARCH: "Not primary unless A1 finds current external evidence is required."
    S3_DECIDE: "Not primary; no human-owned tradeoff currently blocks the next action."
    Context_Request: "Not primary until A1 determines exact missing legacy context."
  downstream_after_A1_if_passed: "E1_EXECUTION_BRIEF -> X1_EXECUTOR_RUN with approved Execution Work Package."
```

## Execution Graph Binding

```yaml
execution_graph_binding:
  phase_node_id: h1_g4b_grid_topology_foundation
  parent_goal_id: h1-g4b-grid-topology-foundation
  topology_type: gated_sequential
  graph_node_done_when: "Accepted product evidence proves the production-grade Grid / Topology Core or exact blocker/unblock packet."
  evidence_to_return:
    - legacy architecture sufficiency verdict
    - selected topology ingestion architecture
    - selected runtime topology model
    - selected spatial change model
    - selected cross-system coordination contract
    - exact missing-context request if old evidence is unavailable
  expected_graph_delta_input: "A1 returns audit evidence for E1/X1 or blocker routing; A1 does not mutate Direction/Phase/Goal/Map state."
```

## Proposed Architecture to Audit

```yaml
topology_ingestion_architecture:
  selected_shape: replaceable_adapter_boundary
  core_rule: "Grid core consumes topology data through an interface/adapter contract, not directly from tags, Dungeon Architect, or a scene parser."
  adapter_candidates_to_audit:
    - scene_marker_or_tag_adapter_from_legacy_evidence
    - baked_topology_asset_adapter
    - future_Dungeon_Architect_output_adapter
    - future_custom_generator_output_adapter
  forbidden:
    - hard_couple_core_grid_to_tags
    - hard_couple_core_grid_to_Dungeon_Architect
    - make_Grid_responsible_for_level_generation

runtime_topology_model:
  selected_shape: stable_spatial_identity_graph
  required_entities:
    - cells_or_nodes
    - rooms_or_regions_when_useful
    - boundaries_or_edges
    - walls
    - doors
    - openings
    - holes
    - blockers
  core_ownership: "Topology identity, connectivity, boundaries, and mutation state only."
  external_ownership: "Gas, temperature, AI, destruction gameplay, and multiplayer transport own their own domain data."

dynamic_topology_mutation_strategy:
  selected_shape: command_commit_changeset
  flow:
    - mutation_request_from_external_system
    - validate_against_topology_rules
    - deterministic_commit_boundary
    - update_connectivity_or_mark_connectivity_dirty
    - emit_batched_topology_change_set
  examples:
    - wall_destroyed_or_changed
    - door_opened_or_closed
    - blocker_added_or_removed
    - opening_created_or_removed

spatial_change_model:
  selected_shape: batched_change_sets_plus_dirty_regions_and_versioning
  event_policy: "Notify by committed change set, not naive per-cell event spam."
  deterministic_policy: "Same topology state + same ordered mutation inputs => same query/update results."
  performance_guardrail: "A1 must check old perf/tests/profiling before accepting event/change model."

cross_system_coordination_contract:
  selected_shape: spatial_identity_and_query_contract
  Grid_may:
    - expose stable spatial IDs
    - answer topology/connectivity queries
    - publish committed topology change sets
    - expose dirty regions or versioned topology snapshots
  Grid_must_not:
    - own gas simulation state
    - own temperature state
    - own fan behavior
    - own AI/gameplay domain state
    - become a bucket for all systems
```

## Allowed / Forbidden Surfaces

```yaml
allowed_A1_surfaces:
  - old Grid/GridV2 architecture
  - old tag/marker/scene parser behavior
  - old room/wall/door/opening/hole/blocker model
  - old Grid tests
  - old performance tests/benchmarks/profiling notes
  - old GasV2R topology constraints
  - old Grid-Gas interaction assumptions
  - H1_G4A accepted topology interface seam
  - proposed replaceable topology ingestion boundary
  - proposed command/commit/change-set mutation model
  - proposed batched change-set / dirty-region / versioned spatial change model
  - proposed cross-system spatial coordination contract

forbidden_surfaces:
  - product_repo_mutation_by_A1
  - implementation_by_A1
  - direct_X1_launch
  - old_code_transfer
  - throwaway_grid
  - hard_coupled_tag_parser_inside_core_grid
  - hard_coupled_Dungeon_Architect_core_dependency
  - grid_as_god_object
  - gas_simulation_foundation
  - grid_gas_interaction
  - multiplayer_boundary
  - Unity_MCP_setup
  - Task_Master_graph_creation
  - Game_Documentation_promotion
  - broad_vertical_slice
```

## Acceptance to Validation Map

| Acceptance-floor item | Artifact/check | Evidence required |
|---|---|---|
| Legacy evidence sufficiency | A1 audit verdict | reusable ideas, rejected assumptions, exact gaps |
| Replaceable ingestion boundary | A1 checks parser/adapter model | accepted/rejected architecture |
| Dynamic topology mutation strategy | A1 checks old topology model/tests/perf | accepted/rejected mutation contract |
| Spatial change model | A1 checks event/change-set/dirty-region/versioning model | accepted/rejected model |
| Cross-system coordination | A1 checks Grid ownership boundary | accepted/rejected contract |
| X1 readiness | A1 returns sufficiency result | pass or blocker/unblock packet |

## Stop Triggers

```yaml
stop_triggers:
  - old Grid/GridV2/source/tests/perf evidence is required but unavailable
  - old tag/marker parser cannot be inspected enough to judge adapter value
  - architecture would hard-couple Grid core to tags or Dungeon Architect
  - design makes Grid own gas/temperature/fan/AI/gameplay state
  - selected event/change model cannot be justified for expected scale
  - validation surface cannot prove topology behavior
  - X1 package would become blind rewrite
  - X1 package would copy old code directly
```

## Next Stage

```yaml
next_stage:
  id: A1_AUDIT
  source_path: workflow/stage_prompts/A1_AUDIT.md
  launch_status: blocked_until_repository_maintenance_readback
  return_to_parent_stage: E1_EXECUTION_BRIEF
```

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/h1-g4b-grid-topology-foundation/goals/h1-g4b-grid-topology-foundation/01_E1_EXECUTION_BRIEF.md`
