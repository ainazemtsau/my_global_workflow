# 01_DIRECTION_STATE.md

```yaml
project_file_control:
  file: 01_DIRECTION_STATE.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/01_DIRECTION_STATE.md"
  activated_at: "2026-05-13"
  source_freshness: fresh_after_p0_project_bootstrap_validation_surface_setup_started
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
  current_phase_pointer: "directions/indie-game-development/phases/project-bootstrap-validation-surface-setup"
  current_phase_status: active_pending_G1_goal_shape
  active_goal_pointer: none_active_pending_G1_goal_shape
  active_goal_contract: none_active_pending_G1_goal_shape
  existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  existing_goal_artifact_status: r1_accepted_route_gated_decision_map
  recommended_first_goal_candidate: bootstrap-validation-surface-setup-envelope
  last_closed_phase_pointer: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
  last_closed_phase_result: p9_closed_complete
  previous_active_phase_pointer: "directions/indie-game-development/phases/expedition-first-playable-proof-slice"
  previous_active_phase_status: paused_superseded_not_closed
  previous_active_goal_pointer: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief"
  previous_active_goal_status: paused_superseded_partial_progress_not_accepted
  last_completed_goal_pointer: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness"
  last_completed_goal_result: r1_accepted_goal_complete
  accepted_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/execution_log.md"
  accepted_product_local_artifacts:
    - "C:\\projects\\Unity\\GasCoopGame\\.workflow\\outbox\\H1_G3_READINESS_PACKET.md"
    - "C:\\projects\\Unity\\GasCoopGame\\.workflow\\evidence\\h1-g3-readiness-2026-05-21.md"
  active_goal_status: none_active_pending_G1_goal_shape
  next_route: G1_GOAL_SHAPE
  next_route_mode: shape_bootstrap_validation_surface_setup_envelope
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  last_updated: "2026-05-21"
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

- Phase: `Project Bootstrap and Validation Surface Setup`
- Path: `directions/indie-game-development/phases/project-bootstrap-validation-surface-setup`
- Status: `active_pending_G1_goal_shape`
- Started by: `P0_PHASE_START`
- Started at: `2026-05-21`
- Map binding: `H1_playable_technical_nucleus / H1_G3_project_bootstrap_tool_binding_validation_scene_readiness -> H1_G4_durable_technical_nucleus`
- Required H1_G2 surface/gate: `H1_G2_codex_development_operating_model_and_architecture_protocols`
- Current Critical Constraint: accepted H1_G3 readiness has not yet been converted into a bounded setup/validation envelope for safe H1_G4 scoping.
- Minimum Outcome: accepted or route-gated project bootstrap / validation-surface setup envelope.
- Validation Signal: later E1/U1/X0/X1 or H1_G4 scoping can proceed without inventing project/tool state.
- Active Goal: `none_active_pending_G1_goal_shape`
- Active Goal status: `none_active_pending_G1_goal_shape`
- Selected first Goal candidate: `bootstrap-validation-surface-setup-envelope`
- Last completed Goal: `H1_G3_project_bootstrap_tool_binding_validation_scene_readiness`
- Last completed Goal status: `r1_accepted_goal_complete`
- Accepted Goal Artifact: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/execution_log.md`
- Existing Goal Artifact: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`
- Existing artifact treatment: `accepted_route_gated_decision_map`; old Grid/Gas material is reference/evidence only until requirements are clear.
- Next route: `G1_GOAL_SHAPE`
- Implementation allowed now: `false`
- Codex product execution allowed now: `false`

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

- Phase: `Core Co-op Technical Foundation Selection`
- Path: `directions/indie-game-development/phases/core-coop-technical-foundation-selection`
- Close stage: `P9_PHASE_CLOSE`
- Close result: `closed_complete_by_P9`
- Closed at: `2026-05-21`
- Close summary: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/phase_close_summary.md`
- Next route after close: `P0_PHASE_START`

## Previous closed Phase

- Phase: `Expedition First Proof Checkpoint`
- Path: `directions/indie-game-development/phases/expedition-first-proof-checkpoint`
- Close stage: `P9_PHASE_CLOSE`
- Close result: `closed`
- Closed at: `2026-05-12`
- Next route after close: `P0_PHASE_START`

## Project Files export state

- Last refresh: `requires_manual_refresh_after_p0_project_bootstrap_validation_surface_setup_repository_maintenance_2026-05-21`
- Required refresh: `before G1_GOAL_SHAPE after P0 phase start repository maintenance read-back/commit/integration`
- Current route: `G1_GOAL_SHAPE`
- Active Phase: `Project Bootstrap and Validation Surface Setup`
- Active Phase status: `active_pending_G1_goal_shape`
- Active Goal: `none_active_pending_G1_goal_shape`
- Active Goal status: `none_active_pending_G1_goal_shape`
- Selected first Goal candidate: `bootstrap-validation-surface-setup-envelope`
- Last completed Goal: `H1_G3_project_bootstrap_tool_binding_validation_scene_readiness`
- Last completed Goal status: `r1_accepted_goal_complete`
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

Next route: `E1_EXECUTION_BRIEF`.

## 2026-05-19 M0 Objective Architecture migration

M0 completed the Objective Architecture migration/review for the initialized Direction Map.

Current active frontier:
- `H1_G2_codex_development_operating_model_and_architecture_protocols`

Next route:
- `G1_GOAL_SHAPE`

The next Goal must shape the minimum Codex development operating model and architecture protocols required before project bootstrap, validation-scene readiness, durable technical nucleus implementation, or Codex product/project execution.

## 2026-05-19 G1 H1_G2 formalization

```yaml
g1_H1_G2_formalization:
  active_goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
  active_goal_status: goal_shaped_pending_A1_audit
  active_goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md"
  next_route: A1_AUDIT
  next_route_mode: audit_existing_workflow_codex_project_setup_first_use_fit
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  unity_bootstrap_allowed_now: false
  task_master_graph_allowed_now: false
key_correction: >
    H1_G2 is a first-use audit/fit-check of the existing workflow Codex/project
    setup procedure, not creation of a second workflow layer.
```

## 2026-05-20 R1 accepted H1_G2 profile/addendum

`H1_G2_codex_development_operating_model_and_architecture_protocols`
is accepted as `completed_verified`.

The accepted artifact is the Gas Coop Game Project Execution Profile:

`directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/01_GAS_COOP_GAME_PROJECT_EXECUTION_PROFILE.md`

H1_G2 is complete only as an execution-readiness/profile addendum.
It does not authorize Unity bootstrap, product repository creation, implementation,
Codex product/project execution, Task Master graph creation, real internal tool setup,
old-code transfer, or Game Documentation promotion.

Next route: `G1_GOAL_SHAPE`.

## 2026-05-20 M0 active-front review — H1_G3 selected

M0 completed the active-front review after H1_G2 acceptance.

Current selected next node:

`H1_G3_project_bootstrap_tool_binding_validation_scene_readiness`

Next route:

`G1_GOAL_SHAPE`

H1_G3 is not execution. It is the next Goal-shaping target for project/bootstrap/tool-binding/validation-scene readiness.

Still not authorized:

- Unity bootstrap;
- product repository creation;
- implementation;
- product code;
- Codex product/project execution;
- Task Master graph creation;
- real internal tool setup;
- Unity MCP installation/configuration;
- old-code transfer;
- old-code audit as starting point;
- Game Documentation promotion.

## 2026-05-20 G1 H1_G3 formalization

```yaml
g1_H1_G3_formalization:
  active_goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  active_goal_pointer: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness"
  active_goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/00_GOAL_CONTRACT.md"
  active_goal_status: goal_shaped_pending_E1_execution_brief
  last_completed_goal: H1_G2_codex_development_operating_model_and_architecture_protocols
  last_completed_goal_result: r1_accepted_goal_complete
  next_route: E1_EXECUTION_BRIEF
  next_route_mode: prepare_H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  unity_bootstrap_allowed_now: false
  product_repository_creation_allowed_now: false
  task_master_graph_allowed_now: false
summary: >
  G1 shaped H1_G3 as the readiness contract for project bootstrap,
  tool-binding, and validation-scene readiness. E1 is the next route to
  prepare the concrete execution brief without running bootstrap or product execution.
```

Still not authorized:

- Unity bootstrap;
- product repository creation;
- product code;
- Codex product/project execution;
- Task Master graph creation;
- real internal tool setup;
- Unity MCP setup;
- old-code transfer;
- old-code audit as starting point;
- Game Documentation promotion.

## 2026-05-21 R1 accepted H1_G3 readiness packet

```yaml
r1_H1_G3_readiness_packet_acceptance:
  current_phase_status: active_H1_G3_r1_accepted_pending_P9_phase_close
  active_goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  active_goal_status: r1_accepted_goal_complete
  last_completed_goal_pointer: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness"
  last_completed_goal_result: r1_accepted_goal_complete
  next_route: P9_PHASE_CLOSE
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  project_files_cache_refresh_required_before_P9: true
summary: >
  R1 accepted the H1_G3 readiness packet as complete. Phase close is now the
  next lifecycle route; implementation/bootstrap remains blocked until a later
  Phase/Goal/E1/X1 route.
```

## 2026-05-21 P9 closed Core Co-op Technical Foundation Selection

```yaml
p9_core_coop_technical_foundation_selection_close:
  current_phase_status: closed_complete_by_P9
  active_goal_status: closed_with_phase
  last_completed_goal_pointer: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness"
  last_completed_goal_result: r1_accepted_goal_complete
  last_closed_phase_pointer: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
  last_closed_phase_result: p9_closed_complete
  phase_close_summary: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/phase_close_summary.md"
  next_route: P0_PHASE_START
  next_route_mode: start_next_phase_after_core_coop_technical_foundation_selection_close
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  project_files_cache_refresh_required_after_P9: true
summary: >
  P9 closed the foundation-selection Phase after H1_G3 readiness acceptance.
  P0 is the next route after repository maintenance and manual Project Files
  refresh.
```

## 2026-05-21 P0 started Project Bootstrap and Validation Surface Setup

```yaml
p0_project_bootstrap_validation_surface_setup_start:
  current_phase_pointer: "directions/indie-game-development/phases/project-bootstrap-validation-surface-setup"
  current_phase_status: active_pending_G1_goal_shape
  active_goal_pointer: none_active_pending_G1_goal_shape
  active_goal_status: none_active_pending_G1_goal_shape
  recommended_first_goal_candidate: bootstrap-validation-surface-setup-envelope
  last_completed_goal_pointer: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness"
  last_completed_goal_result: r1_accepted_goal_complete
  last_closed_phase_pointer: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
  last_closed_phase_result: p9_closed_complete
  next_route: G1_GOAL_SHAPE
  next_route_mode: shape_bootstrap_validation_surface_setup_envelope
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  last_updated: "2026-05-21"
summary: >
  P0 opened the new setup/validation Phase and selected the first Goal candidate
  for G1 shaping. Product/project execution remains blocked.
```
