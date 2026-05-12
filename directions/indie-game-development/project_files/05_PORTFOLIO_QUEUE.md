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

Active Phase: `none`

Last closed Phase: `directions/indie-game-development/phases/expedition-first-proof-checkpoint`

Active Goal: `none`

Last completed Goal: `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof`

Accepted Goal artifact: `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md`

Next route: `P0_PHASE_START`

Phase close result: `P9_PHASE_CLOSE closed Expedition First Proof Checkpoint`

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

The accepted proof core should guide future Phase or Goal selection, but it must not be expanded into implementation work without a proper Phase, Goal, and execution route.

Do not delete queue items during P0. Queue items remain candidates only; they are not selected until a stage result or Human Decision selects them.

Do not run `G0_GOAL_SELECT` until P0 creates a new active Phase or another valid stage route creates one.
