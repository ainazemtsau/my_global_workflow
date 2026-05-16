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
  status_after_g1_repair_update: active_after_g1_repair_update_pending_b1_route_repair
  map_binding:
    active_horizon: H1_playable_technical_nucleus
    current_gate: H1_G1_core_technical_foundation_decision_brief
    required_inside_current_gate_or_next_gate:
      - H1_G2_codex_development_operating_model_and_architecture_protocols
  next_route: B1_PROBLEM
  next_route_mode: route_integrity_recovery_for_review_ready_decision_brief
  active_goal_id: core-technical-foundation-decision-brief
  active_goal_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief"
  active_goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
  existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  existing_goal_artifact_status: review_ready_candidate_pending_B1_route_repair_not_R1_accepted
  recommended_first_goal_candidate: null
  critical_constraint: "The Direction cannot safely move toward the playable technical nucleus while foundation choices and Codex-development architecture protocols are not reconciled into an accepted, reviewable foundation decision."
  minimum_outcome: "Accepted or review-routed Core Technical Foundation Decision Brief / Decision Map that either satisfies the current Phase closure criteria or names exact A1/D1/S3/E1 gates."
  validation_signal: "Next workflow state can choose R1 review, A1 audit, D1 research, S3 decision, or E1 execution planning without guessing and without premature implementation."
```

```yaml
active_goal_projection:
  goal_id: core-technical-foundation-decision-brief
  status: review_ready_candidate_pending_B1_route_repair_not_R1_accepted
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
  existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  existing_goal_artifact_status: review_ready_candidate_pending_B1_route_repair_not_R1_accepted
  recommended_next_stage: B1_PROBLEM
  goal_shape_note: "G1 classified the existing decision brief as a review-ready candidate; B1 must repair the registry-valid route handoff before any R1 downstream route."
  additional_goal_surface: "Project Engineering & Codex Development Operating Model / H1_G2"
```

```yaml
phase_closure_contract_status_update:
  required_goal_map:
    - goal_id: core-technical-foundation-decision-brief
      name: "Сформировать Core Technical Foundation Decision Brief"
      required_for_closure: true
      status: review_ready_candidate_pending_B1_route_repair_not_R1_accepted
      goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
      existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
      existing_goal_artifact_status: review_ready_candidate_pending_B1_route_repair_not_R1_accepted
      recommended_next_stage: B1_PROBLEM
      recommended_next_mode: route_integrity_recovery_for_review_ready_decision_brief
  after_goal_gate_policy:
    - "After R1, run phase_progress_gate before selecting any new G0/G1 work."
    - "Do not auto-continue into Unity project creation, code transfer, or Codex product/project execution."
    - "Do not treat optional expansion candidates as required for closure."
```

## Guard state

- Active Phase unresolved: `no`
- Active Phase: `Core Co-op Technical Foundation Selection`
- Active Phase route state: `active_after_g1_repair_update_pending_b1_route_repair`
- Active Goal unresolved: `no`
- Active Goal: `core-technical-foundation-decision-brief`
- Active Goal status: `review_ready_candidate_pending_B1_route_repair_not_R1_accepted`
- Existing Goal Artifact: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`
- Existing artifact treatment: `review_ready_candidate_pending_B1_route_repair_not_R1_accepted`
- Previous Phase: `Expedition First Playable Proof Slice`
- Previous Phase status: `paused_superseded_not_closed`
- Previous Goal: `first-playable-proof-slice-brief`
- Previous Goal status: `paused_superseded_partial_progress_not_accepted`
- Last closed Phase: `Expedition First Proof Checkpoint`
- Last completed Goal status: `r1_reviewed_accepted`
- Direction Map status: `initialized`
- Map link: `H1_playable_technical_nucleus / H1_G1_core_technical_foundation_decision_brief / H1_G2_codex_development_operating_model_and_architecture_protocols`
- Next route: `B1_PROBLEM`
- Tool/runtime blocker: `Codex product/project execution still requires verified concrete project/tool bindings before any product/project work.`

## Current phase meaning

`Core Co-op Technical Foundation Selection` exists to choose the high-lock-in technical foundation for a new co-op project before implementation.

## Почему это не повтор прошлой фазы

Previous closed Phase proved the Expedition proof identity and rejected gas-only proof. This Phase does not repeat proof identity work; it resolves technical foundation selection for a new project: multiplayer stack/architecture, Grid/Topology transfer, Gas Simulation architecture, and smallest durable nucleus.

## Next route

Run `B1_PROBLEM` for route-integrity recovery / review handoff repair.

B1 must reconcile:

- existing `04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md` classified by G1 as `review_ready_candidate`;
- registry rule that direct `G1_GOAL_SHAPE` -> `R1_GOAL_REVIEW_DISTILL` is not valid;
- active Goal status `review_ready_candidate_pending_B1_route_repair_not_R1_accepted`;
- downstream route expectation that R1 reviews the artifact if B1 confirms no blocker.

Do not run B1 until this G1 repository patch is applied, read back, diff-verified, commit-verified, and refreshed in context.
