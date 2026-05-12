# 02_CURRENT_PHASE.md

```yaml
project_file_control:
  file: 02_CURRENT_PHASE.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/02_CURRENT_PHASE.md"
  activated_at: "2026-05-12"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
current_phase:
  state: active
  phase_name: Expedition First Playable Proof Slice
  phase_id: expedition-first-playable-proof-slice
  phase_path: "directions/indie-game-development/phases/expedition-first-playable-proof-slice"
  started_by_stage: P0_PHASE_START
  started_at: "2026-05-12"
  next_route: G1_GOAL_SHAPE
  critical_constraint: "Proof identity/boundary exists, but the Direction lacks the smallest playable proof slice that turns accepted proof core into a concrete game situation."
  minimum_outcome: "Accepted First Playable Proof Slice Brief."
  validation_signal: "G1 can shape a concrete first playable proof slice without repeating proof-boundary work or starting implementation."

phase_closure_contract:
  closure_criteria:
    - "One accepted First Playable Proof Slice Brief exists."
    - "The slice preserves expedition-proof-handoff.md and 03_MINIMUM_EXPEDITION_PROOF_CORE.md."
    - "The slice is concrete enough for later proof design / execution brief / tooling decision."
    - "The slice does not become implementation plan, prototype backlog, or full game design."
    - "R1 accepts the Goal result and runs phase_progress_gate before further Goal selection."
  required_goal_map:
    - goal_candidate_id: first-playable-proof-slice-brief
      name: "Сформировать минимальный playable proof slice для Expedition"
      required_for_closure: true
      recommended_next_stage: G1_GOAL_SHAPE
  optional_expansion_candidates:
    - proof-blocking-decision-map
    - project-tool-binding-readiness
    - documentation-promotion
  first_phase_closing_candidate:
    stage: P9_PHASE_CLOSE
    trigger: "After required playable-slice Goal is accepted by R1 and phase_progress_gate selects closure."
  after_goal_gate_policy:
    - "After R1, run phase_progress_gate before selecting any new G0/G1 work."
    - "Do not auto-continue into implementation, documentation promotion, or Codex product/project execution."

last_closed_phase:
  state: closed
  phase_name: Expedition First Proof Checkpoint
  phase_id: expedition-first-proof-checkpoint
  phase_path: "directions/indie-game-development/phases/expedition-first-proof-checkpoint"
  closed_by_stage: P9_PHASE_CLOSE
  closed_at: "2026-05-12"
  closure_reason: "Accepted minimum proof core satisfies the transitional checkpoint outcome."
  accepted_goal_artifact: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md"
  next_route_after_close: P0_PHASE_START
```

## Guard state

* Active Phase unresolved: `no`
* Active Phase: `Expedition First Playable Proof Slice`
* Active Goal unresolved: `no`
* Active Goal: `none`
* Last closed Phase: `Expedition First Proof Checkpoint`
* Last completed Goal: `Определить минимальное доказательное ядро первого proof Expedition`
* Last completed Goal status: `r1_reviewed_accepted`
* Accepted artifact: `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md`
* Required proof-slice handoff: `directions/indie-game-development/domain_docs/game_documentation/expedition-proof-handoff.md`
* Next route: `G1_GOAL_SHAPE`
* Tool/runtime blocker: `Codex product/project execution still requires verified concrete project/tool bindings before any product/project work.`

## Current phase meaning

`Expedition First Playable Proof Slice` exists to move from already accepted proof boundary into the smallest concrete playable proof slice.

It must not repeat proof-boundary/readiness work already captured in the proof handoff/core.

## Next route

Run `G1_GOAL_SHAPE` to shape the first Goal candidate:

`Сформировать минимальный playable proof slice для Expedition`

Do not run `G1_GOAL_SHAPE` until P0 repository maintenance apply/read-back, diff verification, commit verification, and context refresh are complete.