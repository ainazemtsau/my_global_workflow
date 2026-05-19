# 01_DIRECTION_STATE.md

```yaml
project_file_control:
  file: 01_DIRECTION_STATE.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/01_DIRECTION_STATE.md"
  activated_at: "2026-05-13"
  source_freshness: active_git_file_after_r1_first_technical_nucleus_spec_acceptance
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
  current_initiative_from_map: innovative-commercial-expedition-gas-sim-game
  active_horizon_from_map: H1_playable_technical_nucleus
  current_phase_pointer: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
  active_goal_pointer: none_pending_g1_goal_shape
  active_goal_contract: none
  existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  existing_goal_artifact_status: r1_accepted_route_gated_decision_map
  recommended_first_goal_candidate: H1_G2_codex_development_operating_model_and_architecture_protocols
  last_closed_phase_pointer: "directions/indie-game-development/phases/expedition-first-proof-checkpoint"
  last_closed_phase_result: p9_closed
  previous_active_phase_pointer: "directions/indie-game-development/phases/expedition-first-playable-proof-slice"
  previous_active_phase_status: paused_superseded_not_closed
  previous_active_goal_pointer: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief"
  previous_active_goal_status: paused_superseded_partial_progress_not_accepted
  last_completed_goal_pointer: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec"
  last_completed_goal_result: r1_completed_verified_specification_accepted
  accepted_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md"
  active_goal_status: none_pending_g1_goal_shape
  next_route: G1_GOAL_SHAPE
  next_route_mode: shape_H1_G2_codex_development_operating_model_and_architecture_protocols
  last_updated: "2026-05-19"
```

## Purpose / thesis

Build a commercially viable indie game direction focused on Expedition product judgment, game meaning, clean technical base, durable documentation, and selective transfer from prior work.

## Durable commitments

- Expedition remains the active product hypothesis.
- The first proof should test game meaning and system synergy, not gas simulation alone.
- Gas-only proof remains rejected.
- This is a new project; old project material is evidence/source material, not automatic production base.
- Multiplayer technology and architecture are foundation decisions because the game is co-op.
- FishNet was used before but is not final for the new project until selected with evidence.
- Gas Simulation gameplay logic must be durable/extensible from the first real implementation, not hardcoded/disposable.
- Grid/Topology old modules may contain reusable ideas, algorithms, invariants, and tests, but direct old-code transfer is out of scope.
- Direct old-code transfer is out of scope for the new project.
- Old Grid/Gas material is reference/evidence only until new requirements are clear.
- The first technical nucleus specification must start from gameplay gas, spatial/level, Grid/topology, cross-system, destructibility compatibility, and validation needs.
- The active technical foundation Goal must use staged decision mapping, not one-shot closure of all technical details.
- Codex-driven development requires foundation-level engineering guardrails before implementation: modularity, testability, dependency/composition boundaries, validation gates, and separation of gameplay/domain logic from multiplayer transport.
- Game truths produced by Goals may move into permanent `Game Documentation` only through an explicit later documentation stage or approved documentation-maintenance patch.
- Codex product/project execution requires verified concrete project/tool bindings.

## Current Phase

- Phase: `Core Co-op Technical Foundation Selection`
- Path: `directions/indie-game-development/phases/core-coop-technical-foundation-selection`
- Status: `active_pending_m0_after_r1_acceptance`
- Started by: `P0_PHASE_START`
- Started at: `2026-05-13`
- Map binding: `H1_playable_technical_nucleus / H1_G1_core_technical_foundation_decision_brief`
- Required H1_G2 surface/gate: `H1_G2_codex_development_operating_model_and_architecture_protocols`
- Current Critical Constraint: foundation choices and Codex-development architecture protocols must be reconciled into an accepted, reviewable foundation decision before playable technical nucleus implementation can safely proceed.
- Minimum Outcome: accepted or review-routed `Core Technical Foundation Decision Brief / Decision Map`.
- Validation Signal: the next workflow state can choose R1 review, A1 audit, D1 research, S3 decision, or E1 execution planning without guessing and without premature implementation.
- Active Goal: `none_pending_g1_goal_shape`
- Active Goal status: `none_pending_g1_goal_shape`
- Last completed Goal: `first-technical-nucleus-functional-spec`
- Last completed Goal status: `r1_completed_verified_specification_accepted`
- Accepted Goal Artifact: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md`
- Existing Goal Artifact: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`
- Existing artifact treatment: `accepted_route_gated_decision_map`; old Grid/Gas material is reference/evidence only until requirements are clear.
- Next route: `G1_GOAL_SHAPE`

## Previous active Phase / Goal

- Phase: `Expedition First Playable Proof Slice`
- Path: `directions/indie-game-development/phases/expedition-first-playable-proof-slice`
- Status: `paused_superseded_not_closed`
- Reason: user challenged the bottleneck; playable-slice brief is premature until technical foundation selection is resolved.
- Goal: `first-playable-proof-slice-brief`
- Status: `paused_superseded_partial_progress_not_accepted`
- F0 artifact: preserved as scaffold/evidence, not accepted completion.
- P9 launched: `false`

## Last closed Phase

- Phase: `Expedition First Proof Checkpoint`
- Path: `directions/indie-game-development/phases/expedition-first-proof-checkpoint`
- Close stage: `P9_PHASE_CLOSE`
- Close result: `closed`
- Closed at: `2026-05-12`
- Next route after close: `P0_PHASE_START`

## Project Files export state

- Last refresh: `requires_refresh_after_r1_first_technical_nucleus_spec_acceptance_2026-05-18`
- Required refresh: `before G1_GOAL_SHAPE for H1_G2`
- Current route: `G1_GOAL_SHAPE`
- Active Phase: `Core Co-op Technical Foundation Selection`
- Active Goal: `none_pending_g1_goal_shape`
- Active Goal status: `none_pending_g1_goal_shape`
- Last completed Goal: `first-technical-nucleus-functional-spec`
- Last completed Goal status: `r1_completed_verified_specification_accepted`
- Existing Goal Artifact: `04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`
- Direction Map status: `initialized`
- Manual Project Files cache refresh required: `true`

## R1 accepted decision map / next required audit

R1 accepted `core-technical-foundation-decision-brief` as an accepted route-gated decision map.

Decision surface results:
- Multiplayer: `decided`.
- Host-player architecture: `decided`.
- Grid / Topology transfer boundary: `audit_needed_A1`.
- Gas Simulation durable architecture / GasV2R transfer boundary: `audit_needed_A1`.
- Grid↔Gas interaction: `decision_gate` / A1 audit surface.
- Smallest durable technical nucleus: blocked until transfer audit and later E1.
- Project Engineering & Codex Development Operating Model: `decided` at decision-map level.

Phase continues with required next Goal candidate:

`grid-gas-transfer-boundary-audit`

Do not run Unity bootstrap, code transfer, Codex product/project execution, Task Master graph creation, or Game Documentation promotion.

## 2026-05-16 G1 reset formalized first technical nucleus specification Goal

`grid-gas-transfer-boundary-audit` is superseded after human clarification.

Active Goal is now:

`first-technical-nucleus-functional-spec`

The Goal is a single parent functional/specification Goal with gated sequential execution. Gas simulation capability frame comes first and requires user approval before Grid/topology work proceeds.

Historical next route at G1 reset: `E1_EXECUTION_BRIEF`.

Current next route after F0 synthesis formalization and evidence repair: `R1_GOAL_REVIEW_DISTILL`.

Implementation, Unity bootstrap, old-code transfer, old-code audit, Codex product/project execution, Task Master graph creation, and Game Documentation promotion remain blocked.

## 2026-05-18 R1 accepted first technical nucleus specification

`first-technical-nucleus-functional-spec` is accepted as `completed_verified`.

Durable accepted result: first technical nucleus functional/technical specification only. The result defines the specification surface for the first technical nucleus; it does not authorize implementation, Unity bootstrap, old-code transfer, old-code audit as starting point, Codex product/project execution, Task Master graph creation, or Game Documentation promotion.

Next route: `M0_DIRECTION_MAP`.

## 2026-05-19 M0 Objective Architecture migration

M0 completed the Objective Architecture migration/review for the initialized Direction Map.

Current active frontier:
- `H1_G2_codex_development_operating_model_and_architecture_protocols`

Next route:
- `G1_GOAL_SHAPE`

The next Goal must shape the minimum Codex development operating model and architecture protocols required before project bootstrap, validation-scene readiness, durable technical nucleus implementation, or Codex product/project execution.
