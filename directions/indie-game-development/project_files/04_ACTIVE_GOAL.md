# 04_ACTIVE_GOAL.md

```yaml
project_file_control:
  file: 04_ACTIVE_GOAL.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/04_ACTIVE_GOAL.md"
  activated_at: "2026-05-13"
  source_freshness: active_git_file_after_p0_repository_apply_readback
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
active_goal:
  state: artifact_exists_pending_G1_repair_update
  goal_id: core-technical-foundation-decision-brief
  goal_title: "Сформировать Core Technical Foundation Decision Brief"
  goal_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief"
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
  existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  existing_goal_artifact_status: review_candidate_evidence_artifact_not_yet_accepted_by_P0
  phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
  current_wave: none
  next_route: G1_GOAL_SHAPE
  next_route_mode: repair_update_existing_active_goal_against_initialized_direction_map_and_existing_artifact
  smallest_useful_result: "Repaired/updated active Goal route/state that determines whether the existing Core Technical Foundation Decision Brief is review-ready, needs repair, or needs D1/A1/S3/E1 gates."
```

```yaml
shaped_goal:
  goal_id: core-technical-foundation-decision-brief
  goal_title: "Сформировать Core Technical Foundation Decision Brief"
  shaped_by_stage: G1_GOAL_SHAPE
  previous_status_before_p0_map_alignment: active_goal_shaped_pending_E1
  previous_recommended_next_stage_before_p0_map_alignment: E1_EXECUTION_BRIEF
  current_runtime_status: artifact_exists_pending_G1_repair_update
  current_recommended_next_stage: G1_GOAL_SHAPE
  current_recommended_next_mode: repair_update_existing_active_goal_against_initialized_direction_map_and_existing_artifact
  repair_reason: "Existing decision brief artifact now requires G1 repair/update against initialized Direction Map before any E1/R1 downstream routing."
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
  existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  existing_goal_artifact_status: review_candidate_evidence_artifact_not_yet_accepted_by_P0
  decision_status_model:
    - decided
    - decision_gate
    - research_needed_D1
    - audit_needed_A1
    - human_decision_needed_S3
    - deferred_not_blocking_for_bootstrap
  required_decision_surfaces:
    - "multiplayer technology and host-player architecture"
    - "Grid/Topology transfer boundary"
    - "Gas Simulation durable logic architecture"
    - "smallest durable technical nucleus"
    - "Project Engineering & Codex Development Operating Model / H1_G2"
  validation_signal: "G1 can determine whether the existing decision brief is review-ready, incomplete, stale/partial, or blocked by A1/D1/S3/E1 without relying on stale E1 route state."
```

```yaml
previous_active_goal:
  state: paused_superseded_partial_progress_not_accepted
  goal_id: first-playable-proof-slice-brief
  goal_title: "Сформировать минимальный playable proof slice для Expedition"
  goal_path: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief"
  goal_contract: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief/00_GOAL_CONTRACT.md"
  f0_artifact_path: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief/02_FIRST_PLAYABLE_PROOF_SLICE_BRIEF.md"
  result_status: "partial_progress_not_accepted"
  preservation_rule: "Useful scaffold/evidence only; do not treat as Goal completion."
```

## Active Goal snapshot

Active Goal remains `core-technical-foundation-decision-brief`.

The existing artifact is:

`directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`

Current treatment:

- `review_candidate_evidence_artifact_not_yet_accepted_by_P0`
- not stale by default;
- not duplicated blindly;
- not accepted as final by P0;
- must be reconciled by `G1_GOAL_SHAPE` repair/update before any E1/R1 downstream route.

The next valid route is `G1_GOAL_SHAPE`, not direct E1 from P0.

## Deferred items

The active Goal must not silently decide or perform:

- Unity project creation;
- code transfer;
- final implementation;
- Task Master graph creation;
- Codex product/project execution;
- final multiplayer stack without evidence;
- final network authority model without decision record;
- exact gas taxonomy/reactions;
- final 25 cm vs 50 cm implementation;
- exact DI package / Unity folder layout / CI setup unless evidence is sufficient and the decision brief requires it;
- full engineering handbook;
- visual gas proof;
- Game Documentation promotion.

The active Goal may leave a surface unresolved only when the unresolved item is explicitly routed to `D1_DEEP_RESEARCH`, `A1_AUDIT`, `S3_DECIDE`, Context Request, or marked `deferred_not_blocking_for_bootstrap`.
