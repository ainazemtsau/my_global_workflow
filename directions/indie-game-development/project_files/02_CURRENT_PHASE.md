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
  next_route: G1_GOAL_SHAPE
  active_goal_id: null
  active_goal_path: null
  active_goal_contract: null
  recommended_first_goal_candidate: core-technical-foundation-decision-brief
  critical_constraint: "High-lock-in co-op technical foundation choices are unresolved: multiplayer stack/architecture, Grid/Topology transfer boundary, and Gas Simulation durable logic architecture."
  minimum_outcome: "Accepted Core Technical Foundation Decision Brief."
  validation_signal: "Accepted foundation decision identifies multiplayer stack/architecture, Grid/Topology transfer boundary, Gas Simulation architecture, and smallest durable technical nucleus."
```

```yaml
phase_closure_contract:
  closure_criteria:
    - "Accepted Core Technical Foundation Decision Brief exists."
    - "Multiplayer technology and host-player architecture are selected or narrowed to an explicit decision gate."
    - "Grid/Topology transfer boundary from old project is clear."
    - "Gas Simulation gameplay logic is defined as durable/extensible, not disposable or hardcoded."
    - "Smallest durable technical nucleus to build next is identified."
    - "R1 accepts the Goal result and runs phase_progress_gate before further Goal selection."
  required_goal_map:
    - goal_candidate_id: core-technical-foundation-decision-brief
      name: "Сформировать Core Technical Foundation Decision Brief"
      required_for_closure: true
      status: first_goal_candidate_pending_G1
      goal_contract: null
      recommended_next_stage: G1_GOAL_SHAPE
  optional_expansion_candidates:
    - unity-project-bootstrap
    - durable-technical-nucleus-implementation
    - visual-gas-proof
    - performance-profiling-pass
    - game-documentation-promotion
  first_phase_closing_candidate:
    stage: P9_PHASE_CLOSE
    trigger: "After required technical foundation decision Goal is accepted by R1 and phase_progress_gate selects closure."
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
