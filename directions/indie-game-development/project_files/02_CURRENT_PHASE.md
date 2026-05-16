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
  source_freshness: active_git_file_after_p0_repository_apply_readback
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
  status_after_g1: active_g1_formalized_grid_gas_transfer_boundary_audit_pending_A1
  map_binding:
    active_horizon: H1_playable_technical_nucleus
    current_gate: H1_G1_core_technical_foundation_decision_brief
    required_inside_current_gate_or_next_gate:
      - H1_G2_codex_development_operating_model_and_architecture_protocols
  next_route: A1_AUDIT
  next_route_mode: audit_grid_gas_transfer_boundary
  active_goal_id: grid-gas-transfer-boundary-audit
  active_goal_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit"
  active_goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit/00_GOAL_CONTRACT.md"
  existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  existing_goal_artifact_status: accepted_route_gated_decision_map
  recommended_first_goal_candidate: grid-gas-transfer-boundary-audit
  critical_constraint: "The Direction cannot safely move toward the playable technical nucleus while foundation choices and Codex-development architecture protocols are not reconciled into an accepted, reviewable foundation decision."
  minimum_outcome: "Accepted or review-routed Core Technical Foundation Decision Brief / Decision Map that either satisfies the current Phase closure criteria or names exact A1/D1/S3/E1 gates."
  validation_signal: "Next workflow state can choose R1 review, A1 audit, D1 research, S3 decision, or E1 execution planning without guessing and without premature implementation."
```

```yaml
active_goal_projection:
  goal_id: grid-gas-transfer-boundary-audit
  status: goal_shaped_pending_A1
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit/00_GOAL_CONTRACT.md"
  execution_log: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit/execution_log.md"
  recommended_next_stage: A1_AUDIT
  next_goal_candidate: none
  goal_shape_note: "G1 shaped the required Grid/Gas/GridV2/GasV2R transfer-boundary audit Goal; A1 is next."
  additional_goal_surface: "Project Engineering & Codex Development Operating Model / H1_G2"
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
    - goal_id: grid-gas-transfer-boundary-audit
      name: "Провести аудит transfer boundary для legacy Grid, GridV2, GasV2R и Gas↔Grid interaction"
      required_for_closure: true
      status: goal_shaped_pending_A1
      recommended_next_stage: A1_AUDIT
      expected_route_after_G1: A1_AUDIT
  after_goal_gate_policy:
    - "R1 ran phase_progress_gate after accepting the decision map."
    - "Phase continues with required Grid/Gas/GridV2/GasV2R transfer-boundary audit Goal."
    - "Do not launch P9 until the required transfer audit is accepted or explicitly route-gated as no longer blocking."
    - "Do not auto-continue into Unity project creation, code transfer, or Codex product/project execution."
    - "Do not treat optional expansion candidates as required for closure."
```

## Guard state

- Active Phase unresolved: `no`
- Active Phase: `Core Co-op Technical Foundation Selection`
- Active Phase route state: `active_g1_formalized_grid_gas_transfer_boundary_audit_pending_A1`
- Active Goal unresolved: `no`
- Active Goal: `grid-gas-transfer-boundary-audit`
- Active Goal status: `goal_shaped_pending_A1`
- Active Goal Contract: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit/00_GOAL_CONTRACT.md`
- Previous accepted Goal Artifact: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`
- Previous accepted artifact treatment: `accepted_route_gated_decision_map`
- Previous Phase: `Expedition First Playable Proof Slice`
- Previous Phase status: `paused_superseded_not_closed`
- Previous Goal: `first-playable-proof-slice-brief`
- Previous Goal status: `paused_superseded_partial_progress_not_accepted`
- Last closed Phase: `Expedition First Proof Checkpoint`
- Last completed Goal status: `r1_reviewed_accepted`
- Direction Map status: `initialized`
- Map link: `H1_playable_technical_nucleus / H1_G1_core_technical_foundation_decision_brief / H1_G2_codex_development_operating_model_and_architecture_protocols`
- Next route: `A1_AUDIT` for `grid-gas-transfer-boundary-audit`
- Tool/runtime blocker: `Codex product/project execution still requires verified concrete project/tool bindings before any product/project work.`

## Current phase meaning

`Core Co-op Technical Foundation Selection` exists to choose the high-lock-in technical foundation for a new co-op project before implementation.

## Почему это не повтор прошлой фазы

Previous closed Phase proved the Expedition proof identity and rejected gas-only proof. This Phase does not repeat proof identity work; it resolves technical foundation selection for a new project: multiplayer stack/architecture, Grid/Topology transfer, Gas Simulation architecture, and smallest durable nucleus.

## Next route

Run `A1_AUDIT` for `grid-gas-transfer-boundary-audit`.

A1 must audit:

- legacy Grid;
- GridV2;
- GasV2R;
- Gas↔Grid interaction.

Do not run A1 until this G1 repository patch is applied, read back, diff-verified, commit-verified, and refreshed in context.

## 2026-05-16 R1 Phase Progress Gate

R1 accepted the current Goal as an accepted route-gated decision map.

Phase Progress Gate result: `continue_with_required_goal`.

P9 is not allowed now because Grid/Gas/GridV2/GasV2R transfer safety remains a required foundation audit surface before implementation.

Next route after R1 was `G1_GOAL_SHAPE` for `grid-gas-transfer-boundary-audit`.

## 2026-05-16 G1 formalization

G1 shaped the required Grid/Gas/GridV2/GasV2R transfer-boundary audit Goal; A1 is next.
