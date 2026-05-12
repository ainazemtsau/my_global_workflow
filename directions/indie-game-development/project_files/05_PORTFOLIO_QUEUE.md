# 05_PORTFOLIO_QUEUE.md

```yaml
project_file_projection: 1
schema: direction_project_file_projection.v1
source_file: "directions/indie-game-development/project_files/05_PORTFOLIO_QUEUE.md"
canonical_source: GitHub repository file
projection_status: fresh
activated_at: "2026-05-12"
```

## Canon rule

This file is an active GitHub Direction runtime file. If it conflicts with another current GitHub Direction file, return Context Request; do not invent state.

## Current queue state

Active Phase: `directions/indie-game-development/phases/expedition-first-playable-proof-slice`

Active Phase name: `Expedition First Playable Proof Slice`

Last closed Phase: `directions/indie-game-development/phases/expedition-first-proof-checkpoint`

Active Goal: `none`

Recommended first Goal candidate: `first-playable-proof-slice-brief`

Last completed Goal: `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof`

Accepted Goal artifact: `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md`

Required proof-slice handoff: `directions/indie-game-development/domain_docs/game_documentation/expedition-proof-handoff.md`

Next route: `G1_GOAL_SHAPE`

Phase start result: `P0_PHASE_START created Expedition First Playable Proof Slice`

## Selected current Phase direction

* `Expedition First Playable Proof Slice` — selected by `P0_PHASE_START`.
  * Purpose: move from accepted proof handoff/core to the smallest concrete playable proof slice.
  * Required first Goal candidate: `Сформировать минимальный playable proof slice для Expedition`.
  * Not a prototype implementation phase.
  * Not a Game Documentation promotion phase.
  * Not Codex product/project execution.

## Completed / accepted

* `Определить минимальное доказательное ядро первого proof Expedition` — accepted by `R1_GOAL_REVIEW_DISTILL`.
  * Artifact: `03_MINIMUM_EXPEDITION_PROOF_CORE.md`
  * Verdict: `completed_verified`
  * Status: `r1_reviewed_accepted`

## Queue items

* Expedition First Proof Readiness Package
* Expedition Truthful Build / Proof Boundary
* Expedition Proof-Blocking Decision Map
* Expedition System Synergy Research Pack
* Expedition Controlled Visual Probe Set
* Expedition Durable Skeleton Documentation Promotion
* Expedition Project Bootstrap / Tool Binding Readiness

Queue items are request-only until selected by a vNext-R stage result.

## Queue discipline

The accepted proof core and proof handoff should guide future Phase or Goal selection, but they must not be expanded into implementation work without a proper Phase, Goal, and execution route.

Do not delete queue items during this Phase.

Do not run `G0_GOAL_SELECT` now unless G1/R1 later determines multiple next Goal candidates genuinely compete. The current first Goal candidate is clear enough for `G1_GOAL_SHAPE`.