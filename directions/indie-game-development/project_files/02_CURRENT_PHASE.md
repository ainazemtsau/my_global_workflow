# 02_CURRENT_PHASE.md

```yaml
project_file_control:
  file: 02_CURRENT_PHASE.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/02_CURRENT_PHASE.md"
    - "directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md"
  activated_at: "2026-05-13"
  source_freshness: active_git_file_after_r1_H1_G2_acceptance_pending_m0_review
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
current_phase:
  state: active
  phase_name: Core Co-op Technical Foundation Selection
  phase_id: core-coop-technical-foundation-selection
  phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
  phase_brief: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md"
  started_by_stage: P0_PHASE_START
  started_at: "2026-05-13"
  status_after_r1: active_r1_accepted_decision_map_pending_grid_gas_transfer_audit
  status_after_g1: active_g1_formalized_first_technical_nucleus_spec_pending_E1
  status_after_f0_synthesis: active_first_technical_nucleus_spec_synthesis_formalized_pending_R1
  status_after_r1_first_technical_nucleus_spec: active_pending_m0_after_r1_acceptance
  status_after_m0_objective_architecture_migration: active_pending_g1_H1_G2_goal_shape
  status_after_g1_H1_G2_formalization: active_H1_G2_goal_shaped_pending_A1_audit
  status_after_r1_H1_G2_acceptance: active_H1_G2_r1_accepted_pending_M0_active_front_review
  map_binding:
    active_horizon: H1_playable_technical_nucleus
    current_gate: H1_G1_core_technical_foundation_decision_brief
    required_inside_current_gate_or_next_gate:
      - H1_G2_codex_development_operating_model_and_architecture_protocols
  next_route: M0_DIRECTION_MAP
  next_route_mode: active_front_review_after_H1_G2_acceptance
  active_goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
  last_completed_goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
  last_completed_goal_result: r1_accepted_goal_complete
  existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  existing_goal_artifact_status: accepted_route_gated_decision_map
  recommended_first_goal_candidate: H1_G2_codex_development_operating_model_and_architecture_protocols
  critical_constraint: "The Direction cannot safely move toward the playable technical nucleus while foundation choices and Codex-development architecture protocols are not reconciled into an accepted, reviewable foundation decision."
  minimum_outcome: "Accepted or review-routed Core Technical Foundation Decision Brief / Decision Map that either satisfies the current Phase closure criteria or names exact A1/D1/S3/E1 gates."
  validation_signal: "Next workflow state can choose R1 review, A1 audit, D1 research, S3 decision, or E1 execution planning without guessing and without premature implementation."
```

```yaml
active_goal_projection:
  goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
  status: r1_accepted_goal_complete
  last_completed_goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
  last_completed_goal_result: r1_accepted_goal_complete
  accepted_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/01_GAS_COOP_GAME_PROJECT_EXECUTION_PROFILE.md"
  execution_log: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/execution_log.md"
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md"
  recommended_next_stage: M0_DIRECTION_MAP
  review_scope: active_front_review_after_H1_G2_acceptance
  completion_scope: parent_goal_complete
  next_goal_candidate: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  goal_shape_note: "R1 accepted H1_G2 as a minimal profile/addendum; M0 must review the active frontier before selecting H1_G3 or another route."
  additional_goal_surface: "Project Engineering & Codex Development Operating Model / H1_G2"
  implementation_allowed_now: false
```

```yaml
phase_progress_gate_after_r1_H1_G2_acceptance:
  result: active_front_review_needed
  p9_allowed_now: false
  next_route: M0_DIRECTION_MAP
  reason: "H1_G2 accepted; active front must be reviewed before H1_G3, P9, G0, E1, bootstrap, or implementation."
```

```yaml
phase_closure_contract_status_update:
  required_goal_map:
    - goal_id: core-technical-foundation-decision-brief
      name: "Сформировать Core Technical Foundation Decision Brief"
      required_for_closure: true
      status: r1_accepted_route_gated_decision_map
      goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
      existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
      existing_goal_artifact_status: accepted_route_gated_decision_map
      review_stage: R1_GOAL_REVIEW_DISTILL
      accepted_scope: "Decision map accepted; multiplayer decided; Grid/Gas transfer routed to A1."
    - goal_id: first-technical-nucleus-functional-spec
      name: "Сформировать функционально-техническую спецификацию первого technical nucleus"
      required_for_closure: true
      status: r1_completed_verified_specification_accepted
      review_stage: R1_GOAL_REVIEW_DISTILL
      accepted_scope: "Functional/technical specification accepted; implementation remains blocked."
      evidence: "R1 accepted upstream synthesis formalization and read-back packet."
    - goal_id: grid-gas-transfer-boundary-audit
      status: superseded_after_human_clarification
      required_for_closure: false
      treatment: "reference/evidence only; do not run A1 audit unless later reselected by lifecycle route."
  after_goal_gate_policy:
    - "R1 accepted the first technical nucleus functional specification."
    - "M0 selected `G1_GOAL_SHAPE` for `H1_G2_codex_development_operating_model_and_architecture_protocols` before P9, E1, project bootstrap, or implementation route selection."
    - "Do not auto-continue into Unity project creation, code transfer, old-code audit, or Codex product/project execution."
    - "Do not treat optional expansion candidates as required for closure."
```

## Guard state

- Active Phase unresolved: `no`
- Active Phase: `Core Co-op Technical Foundation Selection`
- Active Phase route state: `active_H1_G2_r1_accepted_pending_M0_active_front_review`
- Active Goal unresolved: `no`
- Active Goal: `H1_G2_codex_development_operating_model_and_architecture_protocols`
- Active Goal status: `r1_accepted_goal_complete`
- Last completed Goal: `first-technical-nucleus-functional-spec`
- Last completed Goal status: `r1_completed_verified_specification_accepted`
- Previous accepted Goal Artifact: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`
- Previous accepted artifact treatment: `accepted_route_gated_decision_map`
- Previous Phase: `Expedition First Playable Proof Slice`
- Previous Phase status: `paused_superseded_not_closed`
- Previous Goal: `first-playable-proof-slice-brief`
- Previous Goal status: `paused_superseded_partial_progress_not_accepted`
- Last closed Phase: `Expedition First Proof Checkpoint`
- Last closed Phase completed Goal status: `r1_reviewed_accepted`
- Direction Map status: `initialized`
- Map link: `H1_playable_technical_nucleus / H1_G1_core_technical_foundation_decision_brief / H1_G2_codex_development_operating_model_and_architecture_protocols`
- Next route: `M0_DIRECTION_MAP`
- Tool/runtime blocker: `Codex product/project execution still requires verified concrete project/tool bindings before any product/project work.`

## Current phase meaning

`Core Co-op Technical Foundation Selection` exists to choose the high-lock-in technical foundation for a new co-op project before implementation.

## Почему это не повтор прошлой фазы

Previous closed Phase proved the Expedition proof identity and rejected gas-only proof. This Phase does not repeat proof identity work; it resolves technical foundation selection for a new project: multiplayer stack/architecture, Grid/Topology transfer, Gas Simulation architecture, and smallest durable nucleus.

## Next route

Run `M0_DIRECTION_MAP` after R1 H1_G2 acceptance repository maintenance apply/read-back and manual Project Files refresh.

M0 must review the active frontier before selecting H1_G3 project/bootstrap/tool-binding/validation-scene readiness, P9, G0, E1, bootstrap, or implementation.

Do not proceed to P9, E1, project bootstrap, durable implementation planning, Codex product/project execution, old-code audit or transfer, Task Master graph creation, real internal tool setup, or Game Documentation promotion until a later basis-valid lifecycle route authorizes that work.

## 2026-05-16 R1 Phase Progress Gate

R1 accepted the current Goal as an accepted route-gated decision map.

Phase Progress Gate result: `continue_with_required_goal`.

P9 is not allowed now because Grid/Gas/GridV2/GasV2R transfer safety remains a required foundation audit surface before implementation.

Next route after R1 was `G1_GOAL_SHAPE` for `grid-gas-transfer-boundary-audit`; that route was later superseded by the 2026-05-16 G1 reset.

## 2026-05-16 G1 formalization

G1 shaped the required Grid/Gas/GridV2/GasV2R transfer-boundary audit Goal; this was later superseded after human clarification.

## 2026-05-16 G1 reset formalization

G1 superseded `grid-gas-transfer-boundary-audit` after human clarification and formalized `first-technical-nucleus-functional-spec` as the active Goal.

Historical next route at G1 reset: `E1_EXECUTION_BRIEF`.

Current next route after F0 synthesis formalization and evidence repair: `R1_GOAL_REVIEW_DISTILL`.

Historical next route after R1 acceptance: `M0_DIRECTION_MAP`.

Historical next route after M0 Objective Architecture migration: `G1_GOAL_SHAPE`.

Historical next route after G1 H1_G2 formalization: `A1_AUDIT`.

Current next route after R1 H1_G2 acceptance: `M0_DIRECTION_MAP`.

## 2026-05-20 R1 H1_G2 acceptance

R1 accepted the H1_G2 Gas Coop Game Project Execution Profile as the
minimal project-specific profile/addendum for existing workflow setup/Codex readiness.

Phase Progress Gate result: `active_front_review_needed`.

P9 is not launched. M0 must review the active frontier before selecting
H1_G3 bootstrap/tool-binding/validation-scene readiness, P9, G0, E1,
or any material execution route.
