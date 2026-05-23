# H1_G4B Grid / Topology Foundation — Phase Brief

```yaml
artifact_control:
  artifact_name: "H1_G4B Grid / Topology Foundation — Phase Brief"
  schema: phase_brief.v1
  owner_layer: direction_phase
  status: active_pending_G1_goal_shape
  repo_path: directions/indie-game-development/phases/h1-g4b-grid-topology-foundation/00_PHASE_BRIEF.md
  started_by_stage: P0_PHASE_START
  started_at: "2026-05-23"
```

```yaml
phase_identity:
  phase_id: h1-g4b-grid-topology-foundation
  phase_name: "H1_G4B Grid / Topology Foundation"
  direction_id: indie_game_development
  parent_horizon: H1_playable_technical_nucleus
  map_binding: "H1_playable_technical_nucleus / H1_G4B_grid_topology_foundation"
  previous_phase: h1-g4a-core-harness-composition-validation-topology-interface-foundation
  previous_phase_status: closed_complete_by_P9
```

## Why This Phase

```yaml
why_this_phase:
  critical_constraint: "The product foundation has a topology interface seam but not yet an accepted topology substrate."
  phase_result_delta: "Actual topology substrate: cells/nodes, adjacency/connectivity, obstacles/blocking/opening semantics, deterministic stepping surface, Unity debug visualization/validation evidence."
  anti_duplicate: "Does not repeat H1_G4A harness/composition/validation/topology-interface work."
minimum_outcome: "Accepted or route-gated Grid/Topology foundation in GasCoopGame."
validation_signal: "Product evidence packet, validation result/manual checklist, Unity debug visualization evidence, changed-files rationale."
```

## Phase Closure Contract

```yaml
phase_closure_contract:
  closure_criteria:
    - "Topology substrate exists or exact blocker/unblock packet is accepted."
    - "Cells/nodes model is explicit."
    - "Adjacency/connectivity semantics are explicit."
    - "Obstacle/blocking/opening semantics are explicit."
    - "Deterministic stepping/update surface exists."
    - "Unity debug visualization or validation harness/checklist exists."
    - "Product persistence evidence exists."
  required_goal_map:
    - goal_id: h1-g4b-grid-topology-foundation
      required_for_closure: true
      status: selected_for_G1_goal_shape
      expected_route: G1_GOAL_SHAPE
  optional_expansion_candidates_not_required_for_closure:
    - H1_G4C_gas_simulation_foundation
    - H1_G4D_grid_gas_interaction
    - H1_G4E_multiplayer_boundary_foundation
    - full_level_editor
    - pathfinding
    - procedural_generation
    - full_destructibility
  first_phase_closing_candidate: h1-g4b-grid-topology-foundation
  after_goal_gate_policy:
    - "After R1 reviews the first Goal, run phase_progress_gate before selecting any new Goal."
    - "Do not treat optional expansion candidates as closure requirements."
    - "Do not run P9 until the required result node is accepted or explicitly route-gated."
```

## Phase Delivery Graph

```yaml
phase_delivery_graph:
  version: phase_delivery_graph.v1
  phase_outcome:
    outcome_id: h1_g4b_topology_foundation_exists
    one_sentence_result: "GasCoopGame contains an accepted Grid/Topology foundation."
    direction_visible_result: "The product repo has the spatial substrate needed for later Gas, Grid-Gas interaction, and multiplayer boundary work."
    definition_of_done:
      - predicate: topology_cells_or_nodes_exist
        evidence_required: "code/module evidence plus operator-readable changed-files rationale"
      - predicate: adjacency_connectivity_semantics_exist
        evidence_required: "validation result or manual/debug verification"
      - predicate: obstacle_blocking_opening_semantics_exist
        evidence_required: "validation result or manual/debug verification"
      - predicate: deterministic_stepping_surface_exists
        evidence_required: "test/harness/debug evidence"
      - predicate: unity_debug_visualization_or_validation_surface_exists
        evidence_required: "Unity debug scene/view/checklist or validation harness evidence"
      - predicate: product_persistence_evidence_exists
        evidence_required: "commit/evidence packet accepted by R1"
  completion_logic:
    closure_mode: single_primary_node_done
    required_nodes:
      - h1_g4b_grid_topology_foundation
    optional_nodes_do_not_block_closure: true
  flow_policy:
    max_active_goals: 1
    branch_workstreams_are_not_active_goals: true
    optional_expansion_policy: park_by_default
    support_gate_policy: embed_unless_primary_or_blocking
    parallel_policy: sequential_by_default_parallel_by_admission
  nodes:
    - node_id: h1_g4b_grid_topology_foundation
      node_type: result_slice
      status: ready
      required_for_closure: true
      why_needed_for_phase_outcome: "This is the topology substrate foundation itself."
      done_when: "Accepted product evidence proves the topology substrate or exact blocker/unblock packet."
      evidence_required:
        - "product commit/evidence"
        - "validation result or manual Unity/debug verification"
        - "changed-files rationale"
      owner_stage: G1_GOAL_SHAPE
      next_allowed_stage: G1_GOAL_SHAPE
    - node_id: h1_g4b_validation_surface
      node_type: validation_gate
      status: candidate
      required_for_closure: false
      why_needed_for_phase_outcome: "Support only if needed to prove the result slice."
      owner_stage: E1_EXECUTION_BRIEF
      next_allowed_stage: E1_EXECUTION_BRIEF
    - node_id: h1_g4b_blocker_unblock_packet
      node_type: fallback_path
      status: candidate
      required_for_closure: false
      why_needed_for_phase_outcome: "Fallback if topology foundation cannot be safely executed."
      owner_stage: E1_EXECUTION_BRIEF
      next_allowed_stage: B1_PROBLEM
    - node_id: h1_g4c_gas_simulation_foundation
      node_type: parked
      status: parked
      required_for_closure: false
    - node_id: h1_g4d_grid_gas_interaction
      node_type: parked
      status: parked
      required_for_closure: false
    - node_id: h1_g4e_multiplayer_boundary_foundation
      node_type: parked
      status: parked
      required_for_closure: false
  edges:
    - from: h1_g4b_grid_topology_foundation
      to: h1_g4c_gas_simulation_foundation
      type: unlocks
      reason: "Gas foundation likely depends on topology substrate."
    - from: h1_g4b_grid_topology_foundation
      to: h1_g4d_grid_gas_interaction
      type: unlocks
      reason: "Grid-Gas interaction requires topology substrate."
  evidence_ledger: []
  next_node:
    node_id: h1_g4b_grid_topology_foundation
    route: G1_GOAL_SHAPE
    reason: "This is the single required result node."
```

## First Goal Candidate

```yaml
first_goal_candidate:
  goal_id: h1-g4b-grid-topology-foundation
  recommended_next_stage: G1_GOAL_SHAPE
```

## Forbidden Scope

```yaml
forbidden_scope:
  - gas_simulation_foundation
  - grid_gas_interaction
  - multiplayer_boundary
  - product_repo_mutation_before_valid_route
  - Codex_product_project_execution_before_E1_X1
  - Unity_MCP_setup
  - Task_Master_graph_creation
  - old_code_transfer
  - Game_Documentation_promotion
  - broad_vertical_slice
```

## Next Route

```yaml
next_route:
  stage: G1_GOAL_SHAPE
  mode: shape_h1_g4b_grid_topology_foundation
  executable_state: blocked_until_repository_patch_readback_and_manual_project_files_refresh
```
