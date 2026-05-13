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
  state: none_pending_G1
  goal_id: null
  goal_title: null
  goal_path: null
  goal_contract: null
  phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
  current_wave: none
  next_route: G1_GOAL_SHAPE
  smallest_useful_result: null
```

```yaml
recommended_first_goal_candidate:
  goal_candidate_id: core-technical-foundation-decision-brief
  goal_title: "Сформировать Core Technical Foundation Decision Brief"
  recommended_next_stage: G1_GOAL_SHAPE
  smallest_useful_result: "Accepted Goal Contract for producing a technical foundation decision brief."
  candidate_scope:
    - "multiplayer technology and host-player architecture"
    - "Grid/Topology transfer boundary"
    - "Gas Simulation durable logic architecture"
    - "old project evidence/reuse/unsafe assumptions"
    - "smallest durable technical nucleus"
  validation_signal: "The Direction has an accepted technical foundation decision sufficient to proceed to bootstrap/implementation planning without guessing."
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

There is no active Goal after P0. The next valid step is `G1_GOAL_SHAPE` for the first Goal candidate.

## Deferred items

The next Goal must not silently decide or perform:

- Unity project creation;
- code transfer;
- final implementation;
- exact gas taxonomy/reactions;
- final 25 cm vs 50 cm implementation;
- final multiplayer stack without evidence;
- final network authority model without decision record;
- visual gas proof;
- Game Documentation promotion.
