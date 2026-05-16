# 08 Direction Map - Indie Game Development

```yaml
artifact_control:
  artifact_name: "08 Direction Map - Indie Game Development"
  schema: direction_map.v1
  owner_layer: persistence
  status: active
  repo_path: "directions/indie-game-development/project_files/08_DIRECTION_MAP.md"
  default_load: yes
  freshness: fresh_after_m0_review
  last_updated: "2026-05-15"
```

## Purpose

Compact strategic routing context for the Direction's current initiative, active front, horizon slice, and map-linked Phase/Goal selection.

This file does not replace:

- `01_DIRECTION_STATE.md`
- `02_CURRENT_PHASE.md`
- `04_ACTIVE_GOAL.md`
- `05_PORTFOLIO_QUEUE.md`
- `06_CONTEXT_LIBRARY_INDEX.md`
- `07_PHASE_MEMORY_INDEX.md`

## Direction map status

```yaml
direction_map_status:
  map_state: initialized
  current_initiative_id: innovative-commercial-expedition-gas-sim-game
  map_confidence: medium
  last_reviewed_stage: M0_DIRECTION_MAP
  migration_status: completed_by_m0_review
  migration_basis:
    - project_files/00_DIRECTION_START_HERE.md
    - project_files/01_DIRECTION_STATE.md
    - project_files/02_CURRENT_PHASE.md
    - project_files/03_FOCUS_REGISTER.md
    - project_files/04_ACTIVE_GOAL.md
    - project_files/05_PORTFOLIO_QUEUE.md
    - project_files/06_CONTEXT_LIBRARY_INDEX.md
    - project_files/07_PHASE_MEMORY_INDEX.md
    - user_provided_current_initiative_or_strategic_objective
  update_policy: "M0 owns shared map review/update; branch chats emit delta proposals only."
```

## Current Initiative

```yaml
current_initiative:
  id: innovative-commercial-expedition-gas-sim-game
  title: "Create an innovative, commercially viable co-op game centered on deep gas / 3D-space simulation"
  status: active
  intent: "Create a first indie game to be proud of: not a technical demo, but a real game where gas/3D-space simulation is a deep gameplay core."
  why_now: "The Direction needs a strategic map above the current Phase so workflow does not get stuck in endless planning/research loops and can move toward practical game-making."
  success_signal: "A playable technical nucleus and later playable proof exist where gas, grid/topology, and co-op create a distinctive game situation."
  commercial_intent: "The game must have a commercial path. Commercial packaging activates when a credible playable identity or showable proof exists, not as a replacement for building the foundation."
  guardrails:
    - "Do not globally change the game concept without explicit human decision."
    - "Gas/3D-space simulation remains central."
    - "Co-op remains the current working product constraint unless explicitly reopened."
    - "Avoid research-only loops."
    - "Every active node should remove a constraint or move toward a practical game artifact."
    - "Audience testing is not an early mandatory gate."
    - "Codex is expected to be the primary code implementer; architecture and process must be designed for Codex-driven development."
    - "No production-code slice may be accepted without an explicit validation surface: test, harness, validation scene, debug evidence, or manual checklist."
    - "Gameplay/domain logic should be separated from multiplayer transport and Unity presentation to the degree needed for testability, replaceability, and safe foundation decisions."
    - "Modules should be autonomous enough for Codex to work through bounded context instead of loading the whole project for small changes."
    - "Dependency/composition boundaries must be defined before durable nucleus implementation; exact DI package selection requires sufficient evidence or explicit decision."
```

## Initiative Registry

```yaml
initiative_registry:
  - id: innovative-commercial-expedition-gas-sim-game
    title: "Innovative commercial gas-simulation game"
    status: active
    source: "User-provided M0 strategic objective plus current Direction state."
    active_horizon_node: H1_playable_technical_nucleus

  - id: commercialization_visibility_path
    title: "Commercialization / visibility / business path"
    status: parked_future
    activation_trigger: "A credible playable identity, durable nucleus, or showable proof exists."
    reason_parked: "Commercialization matters, but premature marketing planning would expand planning burden before product signal exists."
```

## Strategy Basis

```yaml
strategy_basis:
  map_generation_mode: m0_migration_from_current_00_07_plus_user_objective
  strategic_question: "What is the shortest credible path from current state to a real innovative game without returning to endless research/planning?"
  optimization_criteria:
    - shortest_credible_path
    - constraint_removal
    - evidence_value
    - scope_minimization
    - reversibility
    - human_burden_minimization
    - practical_game_progress
  selected_strategy: "Build toward a playable technical nucleus. The current foundation decision is a gate inside that horizon, not the whole map."
  candidate_paths_considered:
    - id: continue_current_foundation_decision_as_gate
      verdict: selected
      rationale: "The current foundation decision is needed, but only as a gate before real nucleus construction."
    - id: jump_to_unity_bootstrap_or_code_transfer
      verdict: rejected_now
      rationale: "High rework risk: foundation decision, route, project/tool bindings, validation, and scope are not yet accepted."
    - id: broad_research_or_market_planning
      verdict: rejected_now
      rationale: "This would repeat the planning loop."
    - id: throwaway_gas_grid_prototype
      verdict: rejected
      rationale: "Gas-only proof is rejected; the nucleus must be durable and gameplay-directed."
    - id: full_calendar_roadmap
      verdict: rejected
      rationale: "The Direction Map must not become a calendar roadmap or backlog."
  major_assumptions:
    - "The user-provided objective is the top strategic initiative, not a replacement for existing Phase/Goal files."
    - "Gas/3D-space simulation remains the central gameplay pillar."
    - "Co-op remains the current product constraint."
    - "Commercialization is important but should not displace near-term technical/product blocker removal."
  scope_cuts:
    - "No calendar roadmap."
    - "No large backlog."
    - "No Unity implementation."
    - "No automatic old-code transfer."
    - "No Codex product/project execution."
    - "No throwaway gas prototype."
    - "No full marketing plan now."
    - "No audience testing as mandatory early gate."
    - "No full engineering handbook now."
  open_issues:
    - id: active_goal_route_mismatch
      status: open_for_downstream_launch
      summary: "Project Files/bundle point to E1_EXECUTION_BRIEF, while an existing goal artifact may point to R1_GOAL_REVIEW_DISTILL. M0 does not silently resolve this."
    - id: codex_product_execution_blocked
      status: blocking_for_product_execution
      summary: "Codex product/project execution waits for verified project/tool bindings, route, scope, validation, and permissions."
    - id: external_multiplayer_tooling_evidence
      status: potentially_blocking_for_final_stack_selection
      summary: "Final multiplayer stack/architecture selection may require current external evidence through D1/A1/S3."
```

## Compact Initiative Graph

```yaml
compact_initiative_graph:
  nodes:
    - id: N0_innovative_commercial_expedition_gas_sim_game
      type: current_initiative
      status: active
      role: "Main objective: an innovative commercially directed game with deep gas/3D-space simulation as gameplay core."

    - id: H1_playable_technical_nucleus
      type: active_strategic_horizon
      status: active
      role: "First major horizon: reach a playable technical nucleus, meaning a minimal real game foundation rather than another document or throwaway demo."

    - id: H1_G1_core_technical_foundation_decision_brief
      type: current_gate_inside_active_horizon
      status: active_goal
      phase: core-coop-technical-foundation-selection
      goal: core-technical-foundation-decision-brief
      role: "Accept the foundation decision for co-op, grid/topology, gas architecture, smallest nucleus, and engineering/Codex operating model."

    - id: H1_G2_codex_development_operating_model_and_architecture_protocols
      type: development_process_gate
      status: partially_inside_H1_G1_then_explicit_next_gate_if_needed
      role: "Define minimum rules for Codex-driven development: modularity, dependency boundaries, validation gates, test/harness/scene strategy, and separation of gameplay/domain logic from multiplayer transport."

    - id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
      type: bootstrap_gate
      status: parked_until_H1_G1_or_H1_G2
      role: "Verify Unity/project/Codex/tool bindings and prepare validation scenes/harnesses for observable result checking."

    - id: H1_G4_durable_technical_nucleus
      type: implementation_nucleus
      status: parked_until_H1_G3
      role: "Build the minimal durable technical nucleus: gas/grid/network/gameplay foundation that should not be thrown away after proof."

    - id: H2_unique_gas_coop_gameplay_proof
      type: next_strategic_horizon
      status: future
      role: "Prove that gas/3D-space simulation creates a unique co-op gameplay situation."

    - id: H3_vertical_slice_demo_identity
      type: future_product_horizon
      status: future
      role: "Build a showable vertical slice / demo identity."

    - id: H4_commercialization_visibility_path
      type: future_business_horizon
      status: future
      role: "Steam/wishlist/trailer/devlog/positioning after credible playable identity exists."

  edges:
    - from: N0_innovative_commercial_expedition_gas_sim_game
      to: H1_playable_technical_nucleus
      relation: "To create the game, the Direction needs a minimal real playable technical foundation."

    - from: H1_G1_core_technical_foundation_decision_brief
      to: H1_G2_codex_development_operating_model_and_architecture_protocols
      relation: "The foundation decision must explicitly include or open a gate for Codex-driven development rules."

    - from: H1_G2_codex_development_operating_model_and_architecture_protocols
      to: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
      relation: "Project bootstrap should be built around accepted module/dependency/validation protocols."

    - from: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
      to: H1_G4_durable_technical_nucleus
      relation: "After verified bindings and validation harnesses, real nucleus implementation may be planned."

    - from: H1_G4_durable_technical_nucleus
      to: H2_unique_gas_coop_gameplay_proof
      relation: "After the nucleus exists, test unique gameplay/system synergy."

    - from: H2_unique_gas_coop_gameplay_proof
      to: H3_vertical_slice_demo_identity
      relation: "After gameplay proof, build a showable product slice."

    - from: H3_vertical_slice_demo_identity
      to: H4_commercialization_visibility_path
      relation: "After showable identity, activate commercial visibility path."
```

## Active Front

```yaml
active_front:
  active_horizon: H1_playable_technical_nucleus
  current_gate: H1_G1_core_technical_foundation_decision_brief
  required_inside_current_gate_or_next_gate:
    - H1_G2_codex_development_operating_model_and_architecture_protocols
  primary_reason: "The current Goal matters because it is the first foundation gate before a real playable technical nucleus, not because the Direction Map should be reduced to the current Phase."
  active_front_rule: "Close/accept the foundation decision minimally enough; do not expand it into endless research or a full engineering handbook."
  codex_architecture_rule: "The foundation decision is sufficient only if it either accepts minimum Codex-driven development rules or explicitly route-gates them before implementation."
  immediate_next_after_gate:
    - H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
    - H1_G4_durable_technical_nucleus
  route_integrity_issue:
    status: open_for_downstream_launch
    summary: "Before the next executable stage, check the E1 vs R1 mismatch and registry-allowed transition."
  parked_nodes:
    - H2_unique_gas_coop_gameplay_proof
    - H3_vertical_slice_demo_identity
    - H4_commercialization_visibility_path
```

## Horizon Slice

```yaml
horizon_slice:
  id: H1_playable_technical_nucleus
  title: "First playable technical nucleus"
  statement: "The current horizon is not the current Phase. The current horizon is to bring the Direction to the first real game technical foundation where gas, grid/topology, co-op, and player-facing interaction can exist together in the project."
  current_progress_fit:
    - "The current Phase/Goal closes H1_G1: foundation decision."
    - "Codex development operating model must be handled inside H1_G1 or as mandatory H1_G2 before implementation."
    - "If H1_G1 is nearly done, the next move is not more broad research; it is H1_G2/H1_G3/H1_G4."
  node_ids:
    - H1_G1_core_technical_foundation_decision_brief
    - H1_G2_codex_development_operating_model_and_architecture_protocols
    - H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
    - H1_G4_durable_technical_nucleus
  exit_signal:
    - "Foundation decision is accepted or explicitly route-gated."
    - "Minimum Codex Development Operating Model is accepted or made a mandatory next gate before implementation."
    - "Module boundary rules are defined for the first nucleus."
    - "Dependency/composition boundaries are defined at principle level."
    - "Gameplay/domain logic separation from multiplayer transport is defined at principle level."
    - "No-code-without-validation rule is accepted."
    - "Validation scene / harness strategy is defined."
    - "Project/tool bindings are verified."
    - "A minimal runnable technical foundation for gas/grid/co-op exists or is ready for implementation planning."
  stop_before:
    - "calendar roadmap"
    - "full backlog"
    - "full vertical slice"
    - "full marketing campaign"
    - "throwaway gas prototype"
    - "automatic old-code transfer"
    - "Codex product/project execution without E1/C1/C2 readiness"
```

## Parked/Future Nodes

```yaml
parked_future_nodes:
  - id: H2_unique_gas_coop_gameplay_proof
    activation_trigger: "Playable technical nucleus exists."
    reason_parked: "Technical foundation comes first; gameplay synergy proof comes after a nucleus exists."

  - id: H3_vertical_slice_demo_identity
    activation_trigger: "There is proof that gas/co-op gameplay works as a game."
    reason_parked: "Vertical slice should show a game situation, not raw technology."

  - id: H4_commercialization_visibility_path
    activation_trigger: "There is showable identity or credible demo/proof."
    reason_parked: "Commercial path matters, but should not replace building the foundation."

  - id: game_documentation_promotion
    activation_trigger: "Accepted durable truths exist."
    reason_parked: "Documentation is not promoted automatically."

  - id: old_project_transfer_audit
    activation_trigger: "A concrete transfer target is selected."
    reason_parked: "Old project material is evidence/source material, not automatic production base."
```

## Development Protocol Seeds

```yaml
development_protocol_seeds:
  status: seeds_only_not_full_handbook
  purpose: "Preserve the required engineering direction without turning M0 into a full engineering handbook."
  required_before_durable_nucleus_implementation:
    - id: module_boundary_protocol
      rule: "Every module must have clear responsibility, inputs, outputs, dependencies, tests or validation surface, and bounded Codex context."
    - id: multiplayer_domain_separation
      rule: "Multiplayer transport must not be embedded directly into core gameplay/domain logic unless an accepted decision explicitly allows it."
    - id: dependency_composition_protocol
      rule: "Composition root / dependency boundary rules must be defined before implementation; exact DI package is a later evidence-based decision."
    - id: codex_slice_contract
      rule: "Codex implementation should use bounded slices with target module, allowed files, forbidden files, expected output, validation, observable result, and rollback plan."
    - id: no_code_without_validation
      rule: "No production-code slice is accepted without validation surface."
    - id: validation_scene_strategy
      rule: "Bootstrap must define validation scenes/harnesses so the user can observe or verify practical results whenever reasonable."
  candidate_validation_surfaces:
    - "Unit tests for pure/domain logic."
    - "Integration tests for linked systems."
    - "Validation scene for Unity-visible behavior."
    - "Debug view / inspector / overlay for system state."
    - "Manual playtest checklist where automation is not yet sensible."
    - "Network harness for multiplayer behavior."
  candidate_validation_scenes:
    - id: GasSimLab
      role: "Gas propagation, pressure, reactions, and debug visualization."
    - id: GridTopologyLab
      role: "Cells, topology, obstacles, connectivity, and transfer boundary checks."
    - id: NetworkHarness
      role: "Host/client, authority, replication, and desync behavior."
    - id: GameplayInteractionLab
      role: "Player actions interacting with gas/space as gameplay."
    - id: FirstNucleusScene
      role: "First scene where gas + grid + co-op + player actions meet."
```

## Map Update Policy

```yaml
map_update_policy:
  branch_chats_may_mutate_map: false
  allowed_mutation_points:
    - M0_DIRECTION_MAP
    - R1_GOAL_REVIEW_DISTILL
    - P9_PHASE_CLOSE
    - parent_synthesis_after_parallel_branches
  forbidden_behavior:
    - branch_chat_direct_map_mutation
    - backlog_expansion_without_active_front_reason
    - calendar_roadmap_creation
    - replacing_phase_or_goal_state
    - production_code_without_explicit_validation_surface
    - Codex_changes_without_bounded_slice_contract
    - multiplayer_transport_directly_embedded_into_core_gameplay_domain_logic_without_accepted_decision
    - global_architecture_rewrite_without_stage_route
    - DI_package_selection_without_evidence_or_decision
    - module_coupling_that_forces_Codex_to_load_whole_project_for_small_changes
```

## 2026-05-16 R1 map delta

```yaml
map_delta:
  source_stage: R1_GOAL_REVIEW_DISTILL
  delta_type:
    - node_progressed
    - active_front_unchanged
    - new_dependency_discovered
  node: H1_G1_core_technical_foundation_decision_brief
  result: r1_accepted_route_gated_decision_map
  summary: >
    Core Technical Foundation Decision Brief accepted as route-gated decision map.
    Multiplayer is decided. Grid/Gas/GridV2/GasV2R transfer remains required A1 audit.
  active_front:
    active_horizon: H1_playable_technical_nucleus
    current_gate: grid-gas-transfer-boundary-audit
    implementation_allowed_now: false
  next_required_gate:
    id: grid-gas-transfer-boundary-audit
    stage_route: G1_GOAL_SHAPE -> A1_AUDIT
    target:
      - legacy Grid
      - GridV2
      - GasV2R
      - Gas↔Grid interaction
  forbidden_until_gate_resolved:
    - Unity project bootstrap
    - code transfer
    - Codex product/project execution
    - durable technical nucleus implementation
```

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/project_files/08_DIRECTION_MAP.md`
