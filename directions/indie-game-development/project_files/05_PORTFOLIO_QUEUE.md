# 05_PORTFOLIO_QUEUE.md

```yaml
project_file_projection: 1
schema: direction_project_file_projection.v1
source_file: "directions/indie-game-development/project_files/05_PORTFOLIO_QUEUE.md"
canonical_source: GitHub repository file
projection_status: fresh_after_p0_repository_apply_readback
activated_at: "2026-05-13"
```

## Canon rule

This file is an active GitHub Direction runtime file. If it conflicts with another current GitHub Direction file, return Context Request; do not invent state.

## Current queue state

- Active Phase: `directions/indie-game-development/phases/core-coop-technical-foundation-selection`
- Active Phase name: `Core Co-op Technical Foundation Selection`
- Active Phase status: `active_after_g1_repair_update_pending_b1_route_repair`
- Map binding: `H1_playable_technical_nucleus / H1_G1_core_technical_foundation_decision_brief`
- Required H1_G2 surface/gate: `H1_G2_codex_development_operating_model_and_architecture_protocols`
- Active Goal: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief`
- Active Goal name: `Сформировать Core Technical Foundation Decision Brief`
- Active Goal status: `review_ready_candidate_pending_B1_route_repair_not_R1_accepted`
- Active Goal Contract: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md`
- Existing Goal Artifact: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`
- Existing artifact treatment: `review_ready_candidate_pending_B1_route_repair_not_R1_accepted`
- Next route: `B1_PROBLEM`
- Previous Phase: `directions/indie-game-development/phases/expedition-first-playable-proof-slice`
- Previous Phase status: `paused_superseded_not_closed`
- Previous Goal: `directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief`
- Previous Goal status: `paused_superseded_partial_progress_not_accepted`
- Last closed Phase: `directions/indie-game-development/phases/expedition-first-proof-checkpoint`
- Last completed Goal: `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof`

## Selected current Phase direction

`Core Co-op Technical Foundation Selection` is selected by `P0_PHASE_START`.

Purpose: resolve high-lock-in technical foundation choices for a new co-op project before playable proof or implementation work.

Required foundation surface:

- multiplayer technology and host-player architecture;
- Grid/Topology transfer boundary;
- Gas Simulation durable logic architecture;
- smallest durable technical nucleus.

## Completed / accepted

- `Определить минимальное доказательное ядро первого proof Expedition`
  - Artifact: `03_MINIMUM_EXPEDITION_PROOF_CORE.md`
  - Verdict: `completed_verified`
  - Status: `r1_reviewed_accepted`

## Preserved / paused

- `Expedition First Playable Proof Slice`
  - Status: `paused_superseded_not_closed`
  - Reason: technical foundation selection is now the current bottleneck.
- `first-playable-proof-slice-brief`
  - Status: `paused_superseded_partial_progress_not_accepted`
  - Reason: F0 artifact is useful scaffold/evidence but not accepted completion.

## Queue items

- Core Technical Foundation Decision Brief — `review_ready_candidate_pending_B1_route_repair_not_R1_accepted`
- Expedition Project Bootstrap / Tool Binding Readiness — request-only until selected by a vNext-R stage result
- Durable Technical Nucleus Implementation — request-only until selected by a vNext-R stage result
- Expedition System Synergy Research Pack — request-only until selected by a vNext-R stage result
- Expedition Durable Skeleton Documentation Promotion — request-only until selected by a vNext-R stage result
- Expedition Controlled Visual Probe Set — request-only until selected by a vNext-R stage result

## Queue discipline

Do not run implementation, Unity bootstrap, code transfer, or Codex product/project execution until the foundation decision and execution route are accepted.

Do not default to FishNet solely because it was used in the old project.

Do not create throwaway gas/grid prototype logic.

Do not treat the active Goal as one-shot closure of every technical detail. It produces a staged decision brief / decision map with explicit statuses and route gates.

Do not create a full engineering handbook as part of the active Goal. The active Goal only requires a decision-brief-level `Project Engineering & Codex Development Operating Model`.
