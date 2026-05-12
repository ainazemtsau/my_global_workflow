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
  reason: "P9 closed the current Phase after the previous active Goal was completed by F0 and accepted by corrected R1."
  phase_path: null
  current_wave: none
  next_route: P0_PHASE_START

last_completed_goal:
  state: r1_reviewed_accepted
  goal_name: "Определить минимальное доказательное ядро первого proof Expedition"
  goal_id: minimum-proof-core-first-expedition-proof
  goal_path: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof"
  accepted_artifact: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md"
  reviewed_by_stage: R1_GOAL_REVIEW_DISTILL
  review_verdict: completed_verified
  closure_eligibility: eligible

last_closed_phase:
  phase_id: expedition-first-proof-checkpoint
  phase_path: "directions/indie-game-development/phases/expedition-first-proof-checkpoint"
  closed_by_stage: P9_PHASE_CLOSE
  status: closed
  next_route: P0_PHASE_START
```

## Last completed Goal snapshot

* Goal: define the minimum proof core for the first Expedition proof.
* Result: accepted.
* Accepted artifact: `03_MINIMUM_EXPEDITION_PROOF_CORE.md`
* Core accepted rule: the first proof must show Expedition as an escalating co-op judgment loop, not isolated gas simulation or loose prototype.
* Gas-only proof rejection: accepted.
* Validation method: accepted at proof-boundary level with `go`, `revise`, and `kill` outcomes.
* Codex execution allowed: `no, not until project/tool binding is verified`.
* Current next route: `P0_PHASE_START`.
* G0 allowed: `only after a new Phase exists or a valid stage route creates it`.
* Phase auto-close: `completed by P9`.

## Preserved history

The pre-vNext Goal note was moved into the now-closed Phase without deletion or cloning. Its child history remains under the Goal: Sessions, Wave Cards, Decisions, Goal Brief, Execution Pack.

## Deferred items

The accepted artifact does not decide:
* playable proof design;
* prototype scene specification;
* implementation plan;
* exact cargo/carrying/death/lift/procgen/tool/economy/progression mechanics;
* Game Documentation promotion;
* Expedition versus Containment reopening.

These remain future-stage work only.
