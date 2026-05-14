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
  next_route: E1_EXECUTION_BRIEF
  active_goal_id: core-technical-foundation-decision-brief
  active_goal_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief"
  active_goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
  recommended_first_goal_candidate: null
  critical_constraint: "High-lock-in co-op technical foundation choices are unresolved: multiplayer stack/architecture, Grid/Topology transfer boundary, and Gas Simulation durable logic architecture."
  minimum_outcome: "Accepted Core Technical Foundation Decision Brief."
  validation_signal: "Accepted foundation decision identifies multiplayer stack/architecture, Grid/Topology transfer boundary, Gas Simulation architecture, smallest durable technical nucleus, and explicit route gates for unresolved foundation surfaces."
```

```yaml
active_goal_projection:
  goal_id: core-technical-foundation-decision-brief
  status: active_goal_shaped_pending_E1
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
  recommended_next_stage: E1_EXECUTION_BRIEF
  goal_shape_note: "The Goal produces a staged decision brief / decision map, not one-shot closure of every technical detail."
  additional_goal_surface: "Project Engineering & Codex Development Operating Model"
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
- Active Goal unresolved: `no`
- Active Goal: `none_pending_G1`
- Recommended first Goal candidate: `core-technical-foundation-decision-brief`
- Previous Phase: `Expedition First Playable Proof Slice`
- Previous Phase status: `paused_superseded_not_closed`
- Previous Goal: `first-playable-proof-slice-brief`
- Previous Goal status: `paused_superseded_partial_progress_not_accepted`
- Last closed Phase: `Expedition First Proof Checkpoint`
- Last completed Goal status: `r1_reviewed_accepted`
- Next route: `G1_GOAL_SHAPE`
- Tool/runtime blocker: `Codex product/project execution still requires verified concrete project/tool bindings before any product/project work.`

## Current phase meaning

`Core Co-op Technical Foundation Selection` exists to choose the high-lock-in technical foundation for a new co-op project before implementation.

## Почему это не повтор прошлой фазы

Previous closed Phase proved the Expedition proof identity and rejected gas-only proof. This Phase does not repeat proof identity work; it resolves technical foundation selection for a new project: multiplayer stack/architecture, Grid/Topology transfer, Gas Simulation architecture, and smallest durable nucleus.

## Next route

Run `G1_GOAL_SHAPE` for candidate:

`Сформировать Core Technical Foundation Decision Brief`

Do not run G1 until this P0 repository patch is applied, read back, diff-verified, commit-verified, and refreshed in context.
