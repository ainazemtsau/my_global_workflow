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

Active Phase: `directions/indie-game-development/phases/expedition-first-proof-checkpoint`

Active Goal: `none`

Last completed Goal: `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof`

Accepted Goal artifact: `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md`

Next route: `P9_PHASE_CLOSE`

Phase Progress Gate: `closure_selected_by_human`

no_phase_auto_close: true

G0 allowed only after: `P9_handoff` / `explicit_phase_continue_decision`

Phase auto-close: `no; P9 closes formally`

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

The accepted proof core should guide future Goal or Phase selection, but it must not be expanded into implementation work without a proper Goal and execution route.

Do not delete queue items during P9. Queue items remain candidates only; they are not required_for_closure unless P9 or a later Human Decision explicitly classifies them that way.

Do not run `G0_GOAL_SELECT` from the current state before P9 closes or hands off the Phase.
