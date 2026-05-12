# 01_DIRECTION_STATE.md

```yaml
project_file_control:
  file: 01_DIRECTION_STATE.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/01_DIRECTION_STATE.md"
  activated_at: "2026-05-12"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
direction:
  name: Indie Game Development
  id: indie_game_development
  state: active
  workflow_version: vNext-R
  current_phase_pointer: "directions/indie-game-development/phases/expedition-first-playable-proof-slice"
  active_goal_pointer: null
  last_closed_phase_pointer: "directions/indie-game-development/phases/expedition-first-proof-checkpoint"
  last_closed_phase_result: p9_closed
  last_completed_goal_pointer: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof"
  last_completed_goal_result: r1_reviewed_accepted
  accepted_goal_artifact: "directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md"
  required_proof_slice_handoff: "directions/indie-game-development/domain_docs/game_documentation/expedition-proof-handoff.md"
  next_route: G1_GOAL_SHAPE
  last_updated: "2026-05-12"
```

## Purpose / thesis

Build a commercially viable indie game direction focused on Expedition product judgment, game meaning, clean technical base, durable documentation, and selective transfer from prior work.

## Durable commitments

* Expedition is the active product hypothesis.
* The first proof should test game meaning and system synergy, not gas simulation alone.
* The accepted minimum proof core is a connected Expedition co-op judgment loop:
  risk preparation → lift descent → gas/topology/dangerous value reading → route/safety intervention → dangerous vessel recovery/stabilization → readable consequence → push/reroute/secure/retreat/abandon decision → consequence ledger → reason for next descent.
* Gas-only proof is rejected. Gas is supporting evidence only when it creates Expedition judgment.
* The current active Phase must move from accepted proof boundary to the first minimal playable proof slice.
* Do not create another abstract proof-boundary/readiness artifact unless new evidence proves the existing handoff/core insufficient.
* Game truths produced by Goals may move into permanent `Game Documentation` only through an explicit later documentation stage or approved documentation-maintenance patch.
* Codex/project execution requires verified concrete project/tool bindings.

## Current Phase

* Phase: `Expedition First Playable Proof Slice`
* Path: `directions/indie-game-development/phases/expedition-first-playable-proof-slice`
* Status: `active`
* Started by: `P0_PHASE_START`
* Started at: `2026-05-12`
* Current Critical Constraint: proof identity/boundary exists, but the smallest playable proof slice does not.
* Minimum Outcome: accepted `First Playable Proof Slice Brief`.
* Validation Signal: G1 can shape a concrete first playable proof slice without repeating proof-boundary work or starting implementation.
* Next route: `G1_GOAL_SHAPE`

## Last closed Phase

* Phase: `Expedition First Proof Checkpoint`
* Path: `directions/indie-game-development/phases/expedition-first-proof-checkpoint`
* Close stage: `P9_PHASE_CLOSE`
* Close result: `closed`
* Closed at: `2026-05-12`
* Next route after close: `P0_PHASE_START`
* P0 route completed by starting `Expedition First Playable Proof Slice`.

## Last completed Goal

* Goal: `Определить минимальное доказательное ядро первого proof Expedition`
* Path: `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof`
* Accepted artifact: `03_MINIMUM_EXPEDITION_PROOF_CORE.md`
* Review stage: `R1_GOAL_REVIEW_DISTILL`
* Review result: `completed_verified`
* Status: `r1_reviewed_accepted`

## Project Files export state

* Last refresh: `2026-05-12`
* Required refresh: `none after P0 phase-start patch is applied and read back`
* Known stale files: `none known after this patch is applied and read back`
* Current route: `G1_GOAL_SHAPE`
* Active Phase: `Expedition First Playable Proof Slice`
* Active Goal: `none`