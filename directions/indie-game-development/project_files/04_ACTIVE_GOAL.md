# 04_ACTIVE_GOAL.md

```yaml
project_file_control:
  file: 04_ACTIVE_GOAL.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/04_ACTIVE_GOAL.md"
    - "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief/00_GOAL_CONTRACT.md"
  activated_at: "2026-05-12"
  source_freshness: active_git_file_after_g1_repository_apply_readback
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
active_goal:
  state: active
  goal_id: first-playable-proof-slice-brief
  goal_title: "Сформировать минимальный playable proof slice для Expedition"
  goal_path: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief"
  goal_contract: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief/00_GOAL_CONTRACT.md"
  phase_path: "directions/indie-game-development/phases/expedition-first-playable-proof-slice"
  current_wave: none
  created_by_stage: G1_GOAL_SHAPE
  next_route: E1_EXECUTION_BRIEF
  smallest_useful_result: "Accepted First Playable Proof Slice Brief"

goal_contract_summary:
  what: "Create a First Playable Proof Slice Brief for Expedition."
  why_now: "The proof boundary is accepted; the Direction now needs the smallest concrete playable proof slice."
  done: "A reviewable First Playable Proof Slice Brief exists and preserves unresolved mechanics."
  acceptance_floor:
    - minimal player situation
    - what players do by hand
    - lift/descent boundary
    - minimal route/gas/topology pressure
    - minimal dangerous vessel/value situation
    - co-op shared-state consequence
    - real push / reroute / secure / retreat / abandon judgment point
    - run ending
    - consequence ledger result
    - reason for next descent
    - unresolved mechanics deliberately kept undecided
  validation_signal: "The smallest playable slice is known and can test Expedition as connected co-op judgment, not gas simulation alone."
  validation_method: "Review against accepted minimum Expedition loop, six observable proof signals, gas-only rejection, and explicit deferred mechanics."

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

## Active Goal snapshot

* Goal: `Сформировать минимальный playable proof slice для Expedition`
* Goal ID: `first-playable-proof-slice-brief`
* Status: `active`
* Goal Contract: `directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief/00_GOAL_CONTRACT.md`
* Result expected: accepted `First Playable Proof Slice Brief`
* Current next route: `E1_EXECUTION_BRIEF`
* Codex product/project execution allowed: `no, not until project/tool binding is verified`
* Phase auto-close: `not automatic; after R1 use phase_progress_gate`

## Goal meaning

`first-playable-proof-slice-brief` should use the accepted proof handoff/core to define the smallest playable proof slice.

It should not re-create the proof boundary and should not start implementation.

## Preserved proof inputs

* Accepted proof handoff: `directions/indie-game-development/domain_docs/game_documentation/expedition-proof-handoff.md`
* Accepted proof core: `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md`

## Deferred items

The active Goal must not silently decide:

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
