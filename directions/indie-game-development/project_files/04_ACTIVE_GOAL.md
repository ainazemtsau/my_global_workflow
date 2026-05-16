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
  state: review_ready_candidate_pending_B1_route_repair_not_R1_accepted
  goal_id: core-technical-foundation-decision-brief
  goal_title: "Сформировать Core Technical Foundation Decision Brief"
  goal_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief"
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
  existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  existing_goal_artifact_status: review_ready_candidate_pending_B1_route_repair_not_R1_accepted
  phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
  current_wave: none
  next_route: B1_PROBLEM
  next_route_mode: route_integrity_recovery_for_review_ready_decision_brief
  smallest_useful_result: "B1 route-integrity recovery that validates the registry-safe handoff from G1-classified review-ready candidate to R1 review or exact blocker route."
```

```yaml
shaped_goal:
  goal_id: core-technical-foundation-decision-brief
  goal_title: "Сформировать Core Technical Foundation Decision Brief"
  shaped_by_stage: G1_GOAL_SHAPE
  previous_status_before_p0_map_alignment: active_goal_shaped_pending_E1
  previous_recommended_next_stage_before_p0_map_alignment: E1_EXECUTION_BRIEF
  current_runtime_status: review_ready_candidate_pending_B1_route_repair_not_R1_accepted
  current_recommended_next_stage: B1_PROBLEM
  current_recommended_next_mode: route_integrity_recovery_for_review_ready_decision_brief
  repair_reason: "G1 classified the existing decision brief artifact as a review-ready candidate; B1 route-integrity recovery is required before any R1 downstream routing."
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
  existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  existing_goal_artifact_status: review_ready_candidate_pending_B1_route_repair_not_R1_accepted
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

- `review_ready_candidate_pending_B1_route_repair_not_R1_accepted`
- not stale by default;
- not duplicated blindly;
- not accepted by R1;
- must pass `B1_PROBLEM` route-integrity recovery before any R1 downstream route.

The next valid route is `B1_PROBLEM`, not direct R1 from G1.

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
