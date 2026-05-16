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
  status_after_p0_map_alignment: active_after_p0_map_alignment_pending_g1_repair_update
  map_binding:
    active_horizon: H1_playable_technical_nucleus
    current_gate: H1_G1_core_technical_foundation_decision_brief
    required_inside_current_gate_or_next_gate:
      - H1_G2_codex_development_operating_model_and_architecture_protocols
  next_route: G1_GOAL_SHAPE
  next_route_mode: repair_update_existing_active_goal_against_initialized_direction_map_and_existing_artifact
  active_goal_id: core-technical-foundation-decision-brief
  active_goal_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief"
  active_goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
  existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  existing_goal_artifact_status: review_candidate_evidence_artifact_not_yet_accepted_by_P0
  recommended_first_goal_candidate: null
  critical_constraint: "The Direction cannot safely move toward the playable technical nucleus while foundation choices and Codex-development architecture protocols are not reconciled into an accepted, reviewable foundation decision."
  minimum_outcome: "Accepted or review-routed Core Technical Foundation Decision Brief / Decision Map that either satisfies the current Phase closure criteria or names exact A1/D1/S3/E1 gates."
  validation_signal: "Next workflow state can choose R1 review, A1 audit, D1 research, S3 decision, or E1 execution planning without guessing and without premature implementation."
```

```yaml
active_goal_projection:
  goal_id: core-technical-foundation-decision-brief
  status: artifact_exists_pending_G1_repair_update
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
  existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  existing_goal_artifact_status: review_candidate_evidence_artifact_not_yet_accepted_by_P0
  recommended_next_stage: G1_GOAL_SHAPE
  goal_shape_note: "G1 must repair/update the existing active Goal against the initialized Direction Map and existing decision brief artifact before any E1/R1 downstream route."
  additional_goal_surface: "Project Engineering & Codex Development Operating Model / H1_G2"
```

```yaml
phase_closure_contract_status_update:
  required_goal_map:
    - goal_id: core-technical-foundation-decision-brief
      name: "Сформировать Core Technical Foundation Decision Brief"
      required_for_closure: true
      status: active_goal_shaped_pending_E1
      goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
      recommended_next_stage: E1_EXECUTION_BRIEF
  after_goal_gate_policy:
    - "After R1, run phase_progress_gate before selecting any new G0/G1 work."
    - "Do not auto-continue into Unity project creation, code transfer, or Codex product/project execution."
    - "Do not treat optional expansion candidates as required for closure."
```

## Guard state

- Active Phase unresolved: `no`
- Active Phase: `Core Co-op Technical Foundation Selection`
- Active Phase route state: `active_after_p0_map_alignment_pending_g1_repair_update`
- Active Goal unresolved: `no`
- Active Goal: `core-technical-foundation-decision-brief`
- Active Goal status: `artifact_exists_pending_G1_repair_update`
- Existing Goal Artifact: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`
- Existing artifact treatment: `review_candidate_evidence_artifact_not_yet_accepted_by_P0`
- Previous Phase: `Expedition First Playable Proof Slice`
- Previous Phase status: `paused_superseded_not_closed`
- Previous Goal: `first-playable-proof-slice-brief`
- Previous Goal status: `paused_superseded_partial_progress_not_accepted`
- Last closed Phase: `Expedition First Proof Checkpoint`
- Last completed Goal status: `r1_reviewed_accepted`
- Direction Map status: `initialized`
- Map link: `H1_playable_technical_nucleus / H1_G1_core_technical_foundation_decision_brief / H1_G2_codex_development_operating_model_and_architecture_protocols`
- Next route: `G1_GOAL_SHAPE`
- Tool/runtime blocker: `Codex product/project execution still requires verified concrete project/tool bindings before any product/project work.`

## Current phase meaning

`Core Co-op Technical Foundation Selection` exists to choose the high-lock-in technical foundation for a new co-op project before implementation.

## Почему это не повтор прошлой фазы

Previous closed Phase proved the Expedition proof identity and rejected gas-only proof. This Phase does not repeat proof identity work; it resolves technical foundation selection for a new project: multiplayer stack/architecture, Grid/Topology transfer, Gas Simulation architecture, and smallest durable nucleus.

## Next route

Run `G1_GOAL_SHAPE` in repair/update mode for the existing active Goal:

`Сформировать Core Technical Foundation Decision Brief`

G1 must reconcile:

- initialized `08_DIRECTION_MAP.md`;
- active Phase map binding to `H1_playable_technical_nucleus`;
- required `H1_G2_codex_development_operating_model_and_architecture_protocols`;
- existing `04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`;
- stale E1/G1/R1 route mismatch.

Do not run G1 until this P0 repository patch is applied, read back, diff-verified, commit-verified, and refreshed in context.
