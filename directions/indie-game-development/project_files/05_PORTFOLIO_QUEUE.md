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
- Active Phase status: `active_r1_accepted_decision_map_pending_grid_gas_transfer_audit`
- Map binding: `H1_playable_technical_nucleus / H1_G1_core_technical_foundation_decision_brief`
- Required H1_G2 surface/gate: `H1_G2_codex_development_operating_model_and_architecture_protocols`
- Active Goal: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit`
- Active Goal name: `Провести аудит transfer boundary для legacy Grid, GridV2, GasV2R и Gas↔Grid interaction`
- Active Goal status: `goal_shaped_pending_A1`
- Active Goal Contract: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit/00_GOAL_CONTRACT.md`
- Existing Goal Artifact: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`
- Existing artifact treatment: `accepted_route_gated_decision_map`
- Next route: `A1_AUDIT`
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
- Core Technical Foundation Decision Brief — `r1_accepted_route_gated_decision_map`

## Preserved / paused

- `Expedition First Playable Proof Slice`
  - Status: `paused_superseded_not_closed`
  - Reason: technical foundation selection is now the current bottleneck.
- `first-playable-proof-slice-brief`
  - Status: `paused_superseded_partial_progress_not_accepted`
  - Reason: F0 artifact is useful scaffold/evidence but not accepted completion.

## Queue items

- Grid/Gas/GridV2/GasV2R Transfer Boundary Audit — `goal_shaped_pending_A1`, expected route `A1_AUDIT`
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

## Queue update after R1

`Core Technical Foundation Decision Brief` is accepted as a route-gated decision map.

Required next queue item:

- `grid-gas-transfer-boundary-audit`
  - stage route: `G1_GOAL_SHAPE -> A1_AUDIT`
  - target: legacy Grid, GridV2, GasV2R, Gas↔Grid interaction
  - reason: transfer/rewrite boundary must be audited before implementation planning.

Implementation, Unity bootstrap, code transfer, and Codex product/project execution remain blocked.

## Queue update after G1

`grid-gas-transfer-boundary-audit` shaped; next route `A1_AUDIT`.

Queue update after G1: grid-gas-transfer-boundary-audit shaped; next route A1_AUDIT.
