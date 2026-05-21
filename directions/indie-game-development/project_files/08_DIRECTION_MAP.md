# 08 Direction Map - Indie Game Development

```yaml
artifact_control:
  artifact_name: "08 Direction Map - Indie Game Development"
  schema: direction_map.v1
  owner_layer: persistence
  status: active
  repo_path: "directions/indie-game-development/project_files/08_DIRECTION_MAP.md"
  default_load: yes
  freshness: fresh_after_p9_core_coop_technical_foundation_selection_closed
  last_updated: "2026-05-21"
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
  last_reviewed_stage: P9_PHASE_CLOSE
  migration_status: completed_by_m0_review
  objective_architecture_migration_status: completed_by_m0_review_2026_05_19
  current_objective_architecture_node: P0_PHASE_START_after_core_coop_phase_close
  next_safe_route: P0_PHASE_START
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
      status: resolved_by_r1_route_to_m0
      summary: "R1 accepted the specification and routed to M0 before P9/G0/E1."
    - id: codex_product_execution_blocked
      status: blocking_for_product_execution
      summary: "Codex product/project execution waits for verified project/tool bindings, route, scope, validation, and permissions."
    - id: external_multiplayer_tooling_evidence
      status: potentially_blocking_for_final_stack_selection
      summary: "Final multiplayer stack/architecture selection may require current external evidence through D1/A1/S3."
```

## Objective Architecture Layer

```yaml
objective_architecture:
  model: objective_architecture_model.v1
  migration_stage: M0_DIRECTION_MAP
  migration_date: "2026-05-19"
  migration_status: completed
  direction_objective: >
    Build a commercially viable co-op indie game where deep gas / 3D-space simulation
    is a central gameplay system, supported by a clean technical foundation,
    Codex-suitable development process, and durable validation surfaces.
  active_initiative: innovative-commercial-expedition-gas-sim-game
  active_horizon: H1_playable_technical_nucleus
  selected_frontier_node: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  next_safe_route: P9_PHASE_CLOSE

horizon_acceptance_proof:
  candidate_horizon: H1_playable_technical_nucleus
  direction_objective: >
    Build a commercially viable co-op indie game where deep gas / 3D-space simulation
    is a central gameplay system, supported by a clean technical foundation,
    Codex-suitable development process, and durable validation surfaces.
  objective_link:
    claim: >
      A playable technical nucleus is the nearest meaningful state that turns the Direction
      from planning/specification into a real game foundation.
    evidence:
      - "Current initiative targets an innovative commercial co-op game centered on deep gas / 3D-space simulation."
      - "R1 accepted the first technical nucleus functional/technical specification."
      - "The initialized map already identifies H1 as the active strategic horizon."
  current_state_basis:
    known_done:
      - H1_G1_core_technical_foundation_decision_brief
      - H1_G1B_first_technical_nucleus_functional_spec
    known_blockers:
      - "Project/tool bindings are not verified."
      - "Bootstrap/validation-scene readiness is not accepted."
      - "Codex product/project execution is not authorized."
    unknowns:
      - "Exact Goal Contract for H1_G2."
      - "Exact bootstrap/tool-binding route after H1_G2."
  unlock_claim:
    what_this_horizon_unlocks:
      - "Project/bootstrap readiness evaluation."
      - "Durable technical nucleus implementation planning."
      - "Later unique gas/co-op gameplay proof."
    why_unlock_matters: >
      It moves the Direction toward a real playable foundation without reverting to broad research,
      throwaway gas prototypes, premature commercialization planning, or direct old-code transfer.
  exit_predicates:
    - "Minimum Codex Development Operating Model is accepted."
    - "Module boundary rules for the first nucleus are defined."
    - "Dependency/composition boundary principles are defined."
    - "Gameplay/domain logic separation from multiplayer transport is defined at principle level."
    - "No-code-without-validation rule is accepted."
    - "Validation scene / harness strategy is defined."
    - "Project/tool bindings are verified before product execution."
    - "A minimal runnable technical foundation for gas/grid/co-op exists or is ready for implementation planning."
  prerequisite_check:
    satisfied:
      - "Core Technical Foundation Decision Brief accepted as route-gated decision map."
      - "First Technical Nucleus Functional Specification accepted."
    missing:
      - "H1_G2 Goal Contract."
      - "Project/tool-binding readiness."
      - "Execution route/validation envelope for product work."
    assumed: []
  lock_check:
    horizon_is_locked: true
    locked_by:
      - "H1_G2 is not yet shaped as a Goal."
      - "H1_G3 project/bootstrap readiness is not complete."
      - "E1/X0/X1 execution readiness is not proven."
    if_locked_select_prerequisite_horizon: H1_G2_codex_development_operating_model_and_architecture_protocols
  alternatives_considered:
    - horizon: direct_durable_technical_nucleus_implementation
      why_rejected: "Premature before H1_G2/H1_G3 readiness."
    - horizon: commercialization_visibility_path
      why_rejected: "Parked until credible playable identity/showable proof exists."
    - horizon: broad_research_or_market_planning
      why_rejected: "Would repeat planning loop and does not unlock the immediate bottleneck."
  verdict:
    accepted: true
    reason: >
      H1 is linked to the Direction objective and has meaningful exit predicates, but it is locked
      for direct execution; the nearest ready prerequisite frontier node is H1_G2.
    confidence: medium

objective_graph:
  nodes:
    - id: D0_direction_objective
      type: objective
      status: active
      summary: "Commercially viable co-op indie game with deep gas/3D-space gameplay core."

    - id: N0_innovative_commercial_expedition_gas_sim_game
      type: initiative
      status: active
      requires:
        - D0_direction_objective

    - id: H1_playable_technical_nucleus
      type: horizon
      status: active
      direct_execution_status: locked
      requires:
        - N0_innovative_commercial_expedition_gas_sim_game

    - id: H1_G1_core_technical_foundation_decision_brief
      type: decision
      status: done
      requires:
        - H1_playable_technical_nucleus

    - id: H1_G1B_first_technical_nucleus_functional_spec
      type: artifact
      status: done
      requires:
        - H1_G1_core_technical_foundation_decision_brief

    - id: H1_G2_codex_development_operating_model_and_architecture_protocols
      type: execution_readiness
      status: done
      requires:
        - H1_G1_core_technical_foundation_decision_brief
        - H1_G1B_first_technical_nucleus_functional_spec
      unlocks:
        - H1_G3_project_bootstrap_tool_binding_validation_scene_readiness

    - id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
      type: execution_readiness
      status: done
      requires:
        - H1_G2_codex_development_operating_model_and_architecture_protocols

    - id: H1_G4_durable_technical_nucleus
      type: implementation_slice
      status: premature
      blocked_by:
        - P0_G0_G1_E1_route_selection_and_scope
      premature_until: "P0/G0/G1/E1 selects and scopes durable technical nucleus implementation."

    - id: H2_unique_gas_coop_gameplay_proof
      type: horizon
      status: parked
      activates_when: H1_G4_durable_technical_nucleus

    - id: H3_vertical_slice_demo_identity
      type: horizon
      status: parked
      activates_when: H2_unique_gas_coop_gameplay_proof

    - id: H4_commercialization_visibility_path
      type: horizon
      status: parked
      activates_when: H3_vertical_slice_demo_identity

active_frontier:
  ready_nodes:
    - node_id: P0_PHASE_START
      reason_ready: >
        Core Co-op Technical Foundation Selection closed complete by P9 after
        H1_G3 readiness packet acceptance.
      expected_unlock: >
        Enables P0 to establish the next Phase from Phase Memory and Direction
        Map without guessing or launching implementation directly.
  blocked_nodes:
    - node_id: codex_product_project_execution
      blocker: "Concrete project/tool bindings, validators, scope, permissions, and execution route are not verified."
      unblock_route: "Later E1/X0/X1 readiness only."
  premature_nodes:
    - node_id: H1_G4_durable_technical_nucleus
      premature_because: "Implementation target exists conceptually, but P9/P0/G0/E1 has not selected and scoped durable technical nucleus implementation."
    - node_id: direct_X0_X1_EXECUTOR_ROUTE
      premature_because: "Executor setup/run remains blocked until E1 defines the readiness envelope, setup state, and bindings are verified."
  parked_nodes:
    - node_id: H2_unique_gas_coop_gameplay_proof
      activation_trigger: "Durable technical nucleus exists."
    - node_id: H3_vertical_slice_demo_identity
      activation_trigger: "Gas/co-op gameplay proof works as a game."
    - node_id: H4_commercialization_visibility_path
      activation_trigger: "Showable identity or credible demo/proof exists."
    - node_id: game_documentation_promotion
      activation_trigger: "Accepted durable truths exist and documentation maintenance is explicitly authorized."
    - node_id: old_project_transfer_audit
      activation_trigger: "Only after requirements are clear and a later lifecycle route asks a targeted reference/audit question."
  selected_next_node: P0_PHASE_START
  selection_reason: >
    The foundation-selection Phase is closed; P0 is the smallest safe lifecycle
    route to establish the next Phase without prematurely launching bootstrap,
    implementation, or product execution.

next_action_proof:
  direction_objective: "Commercially viable co-op indie game with deep gas/3D-space gameplay core."
  current_horizon: H1_playable_technical_nucleus
  selected_frontier_node: P0_PHASE_START
  proposed_work: >
    Start or reframe the next Phase after Core Co-op Technical Foundation
    Selection closed complete by P9.
  proposed_stage: P0_PHASE_START
  desired_delta: >
    A non-duplicate next Phase proposal with Phase Memory preserved and no
    implementation or product execution launched.
  why_this_now: >
    P9 closed the foundation-selection Phase. P0 must establish the next Phase
    before any setup, implementation planning, durable technical nucleus work,
    or Codex product/project execution.
  prerequisite_check:
    satisfied:
      - "Current Direction Project Files 00-08 are available."
      - "08_DIRECTION_MAP is initialized."
      - "Core decision brief is accepted as route-gated decision map."
      - "First technical nucleus specification is accepted."
      - "H1_G2 Gas Coop Game Project Execution Profile is accepted."
      - "H1_G3 readiness packet is accepted."
    missing:
      - "Exact P0_PHASE_START prompt for the next stage run."
      - "Manual Project Files refresh after this repository maintenance patch."
    assumed: []
  active_frontier_check:
    is_on_frontier: true
    why_not_premature: >
      P0 is allowed because P9 closed the Phase and the remaining bootstrap/
      implementation surfaces belong to later lifecycle routes.
  expected_unlock: >
    Enables later selection of U1, D1, A1, S3, X0/X1, Context Request, Human Decision,
    Stop, or a setup route without inventing tool/project state.
  alternatives_considered:
    - action: direct_E1_or_bootstrap_setup
      why_rejected: "P0 must establish the next Phase before any later setup route."
    - action: direct_bootstrap_or_implementation
      why_rejected: "Execution readiness and project/tool bindings are not verified."
  evidence_basis:
    - artifact_or_state: "first-technical-nucleus-functional-spec"
      supports: "Functional/technical specification is accepted."
    - artifact_or_state: "core-technical-foundation-decision-brief"
      supports: "Foundation decisions are accepted as route-gated decision map."
    - artifact_or_state: "08_DIRECTION_MAP"
      supports: "H1/H1_G2/H1_G3/H1_G4 dependency chain."
  readiness:
    concrete_target_exists: true
    acceptance_criteria_exist: true
    context_available: true
    stage_semantics_match: true
  verdict:
    basis_valid: true
    route_valid: true
    launch_allowed: true
    launch_condition: >
      After repository maintenance apply/read-back, manual Project Files refresh, and exact
      P0_PHASE_START prompt availability.
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
  current_gate: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  current_gate_status: r1_accepted_goal_complete
  previous_gate: H1_G2_codex_development_operating_model_and_architecture_protocols
  previous_gate_status: r1_accepted_goal_complete
  selected_next_node: P0_PHASE_START
  selected_next_route: P0_PHASE_START
  primary_reason: >
    Core Co-op Technical Foundation Selection closed; P0 must establish the
    next Phase before any setup, implementation planning, durable technical
    nucleus work, or Codex product/project execution.
  active_front_rule: >
    Run P0_PHASE_START after P9 closed the foundation-selection Phase before
    any new project bootstrap, durable technical nucleus implementation, Task
    Master graph creation, or Codex product/project execution.
  codex_architecture_rule: >
    The foundation decision is sufficient only if minimum Codex-driven development rules,
    module/dependency boundaries, and validation protocol are accepted before implementation.
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  immediate_next_after_gate:
    - P0_PHASE_START_after_core_coop_phase_close
  route_integrity_issue:
    status: resolved_by_p9_phase_close
    summary: "P9 closed the foundation-selection Phase and selected P0 as the next basis-valid route."
  blocked_nodes:
    - H1_G4_durable_technical_nucleus
    - codex_product_project_execution
    - unity_project_bootstrap
    - product_repository_creation
  premature_nodes:
    - direct_X0_EXECUTOR_PROJECT_SETUP
    - direct_X1_EXECUTOR_RUN
    - unity_project_bootstrap
    - durable_technical_nucleus_implementation
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
    - "Executor/Codex product/project execution without E1/X0/X1 readiness"
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
    status: superseded_as_active_gate
    activation_trigger: "Only after requirements are clear and a later lifecycle route asks a targeted reference/audit question."
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

## 2026-05-16 G1 map delta — grid-gas-transfer-boundary-audit shaped

Superseded as the active front by the later 2026-05-16 G1 reset to `first-technical-nucleus-functional-spec`.

```yaml
map_delta:
  source_stage: G1_GOAL_SHAPE
  delta_type:
    - goal_shaped
    - active_front_unchanged
    - implementation_still_blocked
  node: grid-gas-transfer-boundary-audit
  result: goal_shaped_pending_A1
  summary: >
    G1 formalized the Grid/Gas/GridV2/GasV2R transfer-boundary audit Goal.
    A1 must audit legacy Grid, GridV2, GasV2R, and Gas↔Grid interaction
    against the new game's bounded co-op expedition concept, including Grid
    as interaction substrate, Gas T1/T2/T3 source-of-truth review, and
    future destructibility should-not-block guardrail.
  active_front:
    active_horizon: H1_playable_technical_nucleus
    current_gate: grid-gas-transfer-boundary-audit
    next_stage: A1_AUDIT
    implementation_allowed_now: false
  forbidden_until_gate_resolved:
    - Unity project bootstrap
    - code transfer
    - Codex product/project execution
    - durable technical nucleus implementation
```

## 2026-05-16 G1 map delta — first technical nucleus functional specification shaped

```yaml
map_delta:
  source_stage: G1_GOAL_SHAPE
  delta_type:
    - goal_shaped
    - active_front_repaired
    - implementation_still_blocked
  previous_gate: grid-gas-transfer-boundary-audit
  previous_gate_result: superseded_after_human_clarification
  node: first-technical-nucleus-functional-spec
  result: goal_shaped_pending_E1
  summary: >
    G1 superseded the legacy Grid/Gas transfer-boundary audit as the active gate.
    The repaired active Goal is a single broad parent specification Goal for the
    first technical nucleus. Direct old-code transfer is out of scope. Old project
    material is reference/evidence only after requirements are clear.
  active_front:
    active_horizon: H1_playable_technical_nucleus
    current_gate: first-technical-nucleus-functional-spec
    next_stage: E1_EXECUTION_BRIEF
    implementation_allowed_now: false
  required_sequence:
    - gas_simulation_capability_frame
    - user_approval_gate_after_gas_block
    - level_and_spatial_requirements
    - grid_topology_substrate_requirements
    - cross_system_interaction_requirements
    - destructibility_compatibility_boundary
    - validation_demo_requirements
    - synthesis
  forbidden_until_gate_resolved:
    - Unity project bootstrap
    - implementation
    - old-code transfer
    - old-code audit as starting point
    - Codex product/project execution
    - durable technical nucleus implementation
```

## 2026-05-18 F0 synthesis / evidence integrity repair map delta

```yaml
map_delta:
  source_stage: F0_FAST_DIRECT_repository_maintenance
  delta_type:
    - active_front_route_repaired
    - parent_goal_completion_candidate_ready_for_R1
    - implementation_still_blocked
  node: first-technical-nucleus-functional-spec
  result: synthesis_formalized_pending_R1_review
  summary: >
    F0 formalized the synthesis block for the first technical nucleus functional
    specification. Repository maintenance repaired stale E1/project-file route
    evidence so the completed parent Goal outcome can be reviewed by R1.
  active_front:
    active_horizon: H1_playable_technical_nucleus
    current_gate: first-technical-nucleus-functional-spec
    next_stage: R1_GOAL_REVIEW_DISTILL
    parent_goal_completion_state: complete_pending_R1_acceptance
    phase_progress_gate_status: not_run_pending_R1
    p9_allowed_now: false
    implementation_allowed_now: false
  not_claimed:
    r1_acceptance: false
    phase_closed: false
    game_documentation_promoted: false
  forbidden_until_R1_and_later_gate:
    - Unity project bootstrap
    - implementation
    - old-code transfer
    - old-code audit as starting point
    - Codex product/project execution
    - durable technical nucleus implementation
    - Game Documentation promotion
```

## 2026-05-18 R1 map delta — first technical nucleus functional specification accepted

```yaml
map_delta:
  source_stage: R1_GOAL_REVIEW_DISTILL
  delta_type:
    - node_done_accepted
    - active_front_review_needed
    - m0_review_needed
  node: first-technical-nucleus-functional-spec
  result: r1_accepted_first_technical_nucleus_functional_spec
  summary: >
    Parent specification Goal accepted. The first technical nucleus is now
    defined at functional/technical specification level. Implementation,
    Unity bootstrap, old-code transfer/audit-as-starting-point, Codex
    product/project execution, Task Master graph creation, and Game
    Documentation promotion remain blocked.
  active_front_effect: >
    Active front must be reviewed before selecting project bootstrap,
    Codex/tool-binding readiness, durable nucleus implementation, Phase close,
    or a new Goal.
  next_route: M0_DIRECTION_MAP
```

## 2026-05-19 M0 Objective Architecture migration delta

```yaml
map_delta:
  source_stage: M0_DIRECTION_MAP
  delta_type:
    - objective_architecture_migration_completed
    - active_frontier_selected
    - next_action_proof_added
  result: completed_formalized
  summary: >
    M0 normalized the initialized Direction Map under the Objective Architecture Model.
    Direction Objective, Horizon Acceptance Proof, Objective Graph, Active Frontier,
    Next Action Proof, blocked/premature/parked nodes, and next safe route are now explicit.
  active_horizon: H1_playable_technical_nucleus
  selected_frontier_node: H1_G2_codex_development_operating_model_and_architecture_protocols
  next_safe_route: G1_GOAL_SHAPE
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  forbidden_until_later_basis_valid_route:
    - Unity project bootstrap
    - implementation
    - old-code transfer
    - old-code audit as starting point
    - Codex product/project execution
    - durable technical nucleus implementation
    - Task Master graph creation
    - Game Documentation promotion
```

## 2026-05-19 G1 H1_G2 formalization delta

```yaml
map_delta:
  source_stage: G1_GOAL_SHAPE
  delta_type:
    - goal_shaped
    - active_frontier_progressed_to_audit
    - implementation_still_blocked
  node: H1_G2_codex_development_operating_model_and_architecture_protocols
  result: goal_shaped_pending_A1_audit
  summary: >
    G1 shaped H1_G2 as a first-use audit/fit-check of the existing workflow
    Codex/project setup and execution-readiness procedure. The Goal must not
    create a second workflow layer. It must decide whether the existing workflow
    is sufficient, needs a minimal Indie project-specific addendum/profile,
    needs Workflow Governance repair, or needs exact missing context.
  active_front:
    active_horizon: H1_playable_technical_nucleus
    current_gate: H1_G2_codex_development_operating_model_and_architecture_protocols
    current_gate_status: goal_shaped_pending_A1_audit
    next_stage: A1_AUDIT
    implementation_allowed_now: false
    codex_product_execution_allowed_now: false
  blocked_nodes:
    - H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
    - H1_G4_durable_technical_nucleus
    - codex_product_project_execution
  forbidden_until_later_basis_valid_route:
    - Unity project bootstrap
    - implementation
    - old-code transfer
    - old-code audit as starting point
    - Codex product/project execution
    - durable technical nucleus implementation
    - Task Master graph creation
    - real internal tool setup
    - Game Documentation promotion
```

## 2026-05-20 R1 map delta — H1_G2 accepted

```yaml
map_delta:
  source_stage: R1_GOAL_REVIEW_DISTILL
  delta_type:
    - node_done_accepted
    - active_front_review_needed
    - m0_review_needed
  node: H1_G2_codex_development_operating_model_and_architecture_protocols
  result: r1_accepted_goal_complete
  summary: >
    R1 accepted the Gas Coop Game Project Execution Profile as the minimal
    project-specific profile/addendum for existing workflow project/Codex setup readiness.
    The result preserves no-bootstrap/no-product-execution boundaries and defers real
    project/tool setup to later H1_G3+ routes.
  active_front_effect: >
    H1_G2 no longer blocks active-front review. H1_G3 project/bootstrap/tool-binding/
    validation-scene readiness is the likely next candidate, but it is not selected until
    M0 reviews the frontier.
  next_route: M0_DIRECTION_MAP
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  forbidden_until_later_basis_valid_route:
    - Unity project bootstrap
    - implementation
    - old-code transfer
    - old-code audit as starting point
    - Codex product/project execution
    - durable technical nucleus implementation
    - Task Master graph creation
    - real internal tool setup
    - Game Documentation promotion
```

## 2026-05-20 M0 active-front review delta — H1_G3 selected

```yaml
map_delta:
  source_stage: M0_DIRECTION_MAP
  delta_type:
    - active_front_review_completed
    - selected_frontier_node_updated
    - next_action_proof_updated
    - implementation_still_blocked
  previous_selected_node: H1_G2_codex_development_operating_model_and_architecture_protocols
  previous_selected_node_result: r1_accepted_goal_complete
  selected_next_node: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  selected_next_route: G1_GOAL_SHAPE
  result: completed_formalized
  summary: >
    M0 reviewed the active frontier after R1 accepted H1_G2. H1_G2 no longer
    blocks bootstrap-readiness review. H1_G3 project/bootstrap/tool-binding/
    validation-scene readiness is now the smallest basis-valid next node.
  horizon_acceptance_proof:
    active_horizon: H1_playable_technical_nucleus
    status: accepted_carried_forward
    direct_execution_status: locked
    locked_by:
      - H1_G3 is not yet shaped as a Goal.
      - project/tool bindings are not verified.
      - validation scene/harness readiness is not accepted.
      - Codex product/project execution is not authorized.
  active_front:
    active_horizon: H1_playable_technical_nucleus
    current_gate: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
    current_gate_status: selected_for_G1_goal_shape
    selected_next_node: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
    selected_next_route: G1_GOAL_SHAPE
    implementation_allowed_now: false
    codex_product_execution_allowed_now: false
    p9_allowed_now: false
  ready_nodes:
    - H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  blocked_nodes:
    - H1_G4_durable_technical_nucleus
    - codex_product_project_execution
    - unity_project_bootstrap
    - product_repository_creation
  premature_nodes:
    - direct_E1_EXECUTION_BRIEF
    - direct_U1_USER_GUIDED_EXECUTION
    - direct_X0_EXECUTOR_PROJECT_SETUP
    - direct_X1_EXECUTOR_RUN
    - direct_H1_G4_durable_technical_nucleus
    - direct_P9_PHASE_CLOSE
    - direct_implementation
  parked_nodes:
    - H2_unique_gas_coop_gameplay_proof
    - H3_vertical_slice_demo_identity
    - H4_commercialization_visibility_path
    - game_documentation_promotion
    - old_project_transfer_audit
  next_action_proof:
    direction_objective: "Commercially viable co-op indie game with deep gas/3D-space gameplay core."
    current_horizon: H1_playable_technical_nucleus
    selected_frontier_node: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
    proposed_work: >
      Shape the H1_G3 Goal for project bootstrap, tool-binding, and
      validation-scene readiness before any real setup or product execution.
    proposed_stage: G1_GOAL_SHAPE
    desired_delta: >
      A bounded Goal Contract defining the minimum complete readiness target,
      non-goals, validation expectations, allowed/forbidden setup surfaces,
      tool-binding verification requirements, and next route after H1_G3.
    why_this_now: >
      H1_G2 accepted the minimal zero-state execution profile/addendum. The next
      blocker is no longer workflow/profile readiness; it is the concrete bootstrap
      readiness Goal definition.
    prerequisite_check:
      satisfied:
        - Core Technical Foundation Decision Brief accepted.
        - First Technical Nucleus Functional Specification accepted.
        - H1_G2 Gas Coop Game Project Execution Profile accepted.
      missing:
        - H1_G3 Goal Contract.
        - verified product repository.
        - verified Unity project.
        - verified tool bindings.
        - validation scene/harness readiness.
      assumed: []
    active_frontier_check:
      is_on_frontier: true
      why_not_premature: >
        H1_G3 is the direct readiness gate between accepted execution profile
        and any later bootstrap, E1 planning, U1 guided setup, Executor setup/run,
        or implementation route.
    expected_unlock: >
      Enables a later route to decide whether bootstrap should proceed through
      E1, U1, X0, X1, A1, D1, S3, Context Request, or Human Decision.
    alternatives_considered:
      - action: direct_P9_PHASE_CLOSE
        why_rejected: "Premature while H1_G3 remains the next active-front readiness node."
      - action: direct_E1_EXECUTION_BRIEF
        why_rejected: "Would plan HOW before H1_G3 WHAT/WHY/DONE is shaped."
      - action: direct_bootstrap_or_implementation
        why_rejected: "Explicitly forbidden until a later basis-valid execution route."
      - action: G0_GOAL_SELECT
        why_rejected: "Unnecessary because M0 selected the concrete next node."
    readiness:
      concrete_target_exists: true
      acceptance_criteria_exist: true
      context_available: true
      stage_semantics_match: true
    verdict:
      basis_valid: true
      route_valid: true
      launch_allowed: true
      launch_condition: >
        After repository maintenance apply/read-back, manual Project Files refresh,
        and exact G1_GOAL_SHAPE prompt acquisition in the next run.
  forbidden_until_later_basis_valid_route:
    - Unity project bootstrap
    - product repository creation
    - implementation
    - product code
    - Codex product/project execution
    - durable technical nucleus implementation
    - Task Master graph creation
    - real internal tool setup
    - Unity MCP installation/configuration
    - old-code transfer
    - old-code audit as starting point
    - final DI package selection
    - Game Documentation promotion
```

## 2026-05-20 G1 map delta — H1_G3 shaped

```yaml
map_delta:
  source_stage: G1_GOAL_SHAPE
  delta_type:
    - goal_shaped
    - active_frontier_progressed_to_E1
    - implementation_still_blocked
  node: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  result: goal_shaped_pending_E1_execution_brief
  summary: >
    G1 shaped H1_G3 as the readiness Goal for project bootstrap, tool-binding,
    and validation-scene readiness before any real setup or product execution.
    The Goal defines readiness packet requirements, evidence surfaces, stop rules,
    validation-scene/harness candidates, and next route.
  active_front:
    active_horizon: H1_playable_technical_nucleus
    current_gate: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
    current_gate_status: goal_shaped_pending_E1_execution_brief
    previous_gate: H1_G2_codex_development_operating_model_and_architecture_protocols
    previous_gate_status: r1_accepted_goal_complete
    next_route: E1_EXECUTION_BRIEF
    implementation_allowed_now: false
    codex_product_execution_allowed_now: false
    p9_allowed_now: false
  blocked_nodes:
    - H1_G4_durable_technical_nucleus
    - codex_product_project_execution
    - unity_project_bootstrap
    - product_repository_creation
    - task_master_graph_creation
    - real_internal_tool_setup
    - unity_mcp_setup
  forbidden_until_later_basis_valid_route:
    - Unity project bootstrap
    - product repository creation
    - implementation
    - product code
    - Codex product/project execution
    - durable technical nucleus implementation
    - Task Master graph creation
    - real internal tool setup
    - Unity MCP installation/configuration
    - old-code transfer
    - old-code audit as starting point
    - final DI package selection
    - Game Documentation promotion
```

## 2026-05-21 R1 map delta — H1_G3 accepted

```yaml
map_delta:
  source_stage: R1_GOAL_REVIEW_DISTILL
  delta_type:
    - node_done_accepted
    - phase_close_candidate
    - implementation_still_blocked
  node: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  result: r1_accepted_goal_complete
  summary: "H1_G3 readiness packet accepted. Project/workspace/tool-binding/validation-surface readiness is evidenced enough to close or pause the foundation-selection Phase through P9. Product implementation remains blocked."
  next_route: P9_PHASE_CLOSE
  direction_map_status:
    current_objective_architecture_node: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
    next_safe_route: P9_PHASE_CLOSE
  objective_graph:
    H1_G3:
      status: done
    H1_G4:
      status: premature
```

## 2026-05-21 P9 map delta - Core Co-op Technical Foundation Selection closed

```yaml
map_delta:
  source_stage: P9_PHASE_CLOSE
  delta_type:
    - phase_closed
    - phase_memory_bridge_updated
    - active_frontier_requires_P0
    - implementation_still_blocked
  node: core-coop-technical-foundation-selection
  result: closed_complete_by_P9
  summary: "Foundation-selection Phase closed after H1_G3 readiness acceptance. Next route is P0_PHASE_START. H1_G4 remains premature until selected/scoped by later lifecycle route."
  next_route: P0_PHASE_START
  direction_map_status:
    current_objective_architecture_node: P0_PHASE_START_after_core_coop_phase_close
    next_safe_route: P0_PHASE_START
  objective_graph:
    H1_G3_project_bootstrap_tool_binding_validation_scene_readiness:
      status: done
    H1_G4_durable_technical_nucleus:
      status: premature
      premature_until: "P0/G0/G1/E1 selects and scopes it."
```

## End-of-file marker

END_OF_FILE: directions/indie-game-development/project_files/08_DIRECTION_MAP.md
