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
- Active Phase status: `active_g1_formalized_first_technical_nucleus_spec_pending_E1`
- Map binding: `H1_playable_technical_nucleus / H1_G1_core_technical_foundation_decision_brief`
- Required H1_G2 surface/gate: `H1_G2_codex_development_operating_model_and_architecture_protocols`
- Active Goal: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec`
- Active Goal name: `Сформировать функционально-техническую спецификацию первого technical nucleus`
- Active Goal status: `goal_shaped_pending_E1`
- Active Goal Contract: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/00_GOAL_CONTRACT.md`
- Existing Goal Artifact: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`
- Existing artifact treatment: `accepted_route_gated_decision_map`
- Next route: `E1_EXECUTION_BRIEF`
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

- First Technical Nucleus Functional Specification — `goal_shaped_pending_E1`, expected route `E1_EXECUTION_BRIEF`
- Grid/Gas/GridV2/GasV2R Transfer Boundary Audit — `superseded_after_human_clarification`; reference/evidence only, not current active queue item
- Expedition Project Bootstrap / Tool Binding Readiness — request-only until selected by a vNext-R stage result
- Durable Technical Nucleus Implementation — request-only until selected by a vNext-R stage result
- Expedition System Synergy Research Pack — request-only until selected by a vNext-R stage result
- Expedition Durable Skeleton Documentation Promotion — request-only until selected by a vNext-R stage result
- Expedition Controlled Visual Probe Set — request-only until selected by a vNext-R stage result

## Queue discipline

Do not run implementation, Unity bootstrap, code transfer, old-code audit, or Codex product/project execution until the first technical nucleus functional specification is accepted and later execution stages authorize concrete work.

Do not default to FishNet solely because it was used in the old project.

Do not create throwaway gas/grid prototype logic.

Do not treat old Grid/Gas material as the source of requirements. Old material is reference/evidence only after the new requirements are clear.

The active Goal is one parent functional/specification Goal with gated sequential execution and a required user approval gate after gas simulation capability framing.

## Queue update after R1

`Core Technical Foundation Decision Brief` is accepted as a route-gated decision map.

Required next queue item at that time, now superseded by the 2026-05-16 G1 reset:

- `grid-gas-transfer-boundary-audit`
  - stage route: `G1_GOAL_SHAPE -> A1_AUDIT`
  - target: legacy Grid, GridV2, GasV2R, Gas↔Grid interaction
  - reason: transfer/rewrite boundary must be audited before implementation planning.

Implementation, Unity bootstrap, code transfer, and Codex product/project execution remain blocked.

## Queue update after G1

`grid-gas-transfer-boundary-audit` is superseded after human clarification.

`first-technical-nucleus-functional-spec` shaped; next route `E1_EXECUTION_BRIEF`.

Queue update after G1 reset: first-technical-nucleus-functional-spec shaped; next route E1_EXECUTION_BRIEF.
