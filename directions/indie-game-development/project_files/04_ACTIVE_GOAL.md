# 04_ACTIVE_GOAL.md

```yaml
project_file_control:
  file: 04_ACTIVE_GOAL.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/04_ACTIVE_GOAL.md"
  activated_at: "2026-05-12"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
active_goal:
  state: none
  reason: "P0 started a new active Phase; first Goal must be shaped through G1_GOAL_SHAPE."
  phase_path: "directions/indie-game-development/phases/expedition-first-playable-proof-slice"
  current_wave: none
  next_route: G1_GOAL_SHAPE

recommended_first_goal_candidate:
  id: first-playable-proof-slice-brief
  name: "Сформировать минимальный playable proof slice для Expedition"
  recommended_next_stage: G1_GOAL_SHAPE
  smallest_useful_result: "Accepted First Playable Proof Slice Brief."
  status: candidate_only_not_active_goal

last_completed_goal:
  state: r1_reviewed_accepted
  goal_name: "Определить минимальное доказательное ядро первого proof Expedition"
  goal_id: minimum-proof-core-first-expedition-proof
  goal_path: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof"
  accepted_artifact: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md"
  reviewed_by_stage: R1_GOAL_REVIEW_DISTILL
  review_verdict: completed_verified
  closure_eligibility: completed_and_closed_by_P9

last_closed_phase:
  phase_id: expedition-first-proof-checkpoint
  phase_path: "directions/indie-game-development/phases/expedition-first-proof-checkpoint"
  closed_by_stage: P9_PHASE_CLOSE
  status: closed
  next_route_completed_by: P0_PHASE_START
```

## Last completed Goal snapshot

* Goal: define the minimum proof core for the first Expedition proof.
* Result: accepted.
* Accepted artifact: `03_MINIMUM_EXPEDITION_PROOF_CORE.md`
* Core accepted rule: the first proof must show Expedition as an escalating co-op judgment loop, not isolated gas simulation or loose prototype.
* Gas-only proof rejection: accepted.
* Validation method: accepted at proof-boundary level with `go`, `revise`, and `kill` outcomes.
* Codex execution allowed: `no, not until project/tool binding is verified`.
* Current next route: `G1_GOAL_SHAPE`.
* G0 allowed: `not needed now; one first Goal candidate is clear`.
* Phase auto-close: `not automatic; after R1 use phase_progress_gate`.

## Current Goal candidate meaning

Active Goal remains none until `G1_GOAL_SHAPE` creates a Goal Contract.

`first-playable-proof-slice-brief` should use the accepted proof handoff/core to define the smallest playable proof slice.

It should not re-create the proof boundary and should not start implementation.

## Preserved history

The pre-vNext Goal note was moved into the now-closed Phase without deletion or cloning. Its child history remains under the Goal: Sessions, Wave Cards, Decisions, Goal Brief, Execution Pack.

## Deferred items

The current Goal candidate must not silently decide:

* full playable prototype design;
* implementation plan;
* exact cargo mechanics;
* exact carrying model;
* exact death / downing / group failure model;
* exact lift failure or contamination model;
* exact procedural generation model;
* exact tool list or tool stats;
* exact gas recipes, gas taxonomy, or reaction tables;
* exact inventory system;
* exact economy;
* exact progression;
* exact reward curve;
* exact base / hub form;
* Expedition versus Containment reopening;
* Game Documentation promotion.
