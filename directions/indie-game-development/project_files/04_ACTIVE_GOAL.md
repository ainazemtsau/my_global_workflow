# 04_ACTIVE_GOAL.md

```yaml
project_file_control:
  file: 04_ACTIVE_GOAL.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/04_ACTIVE_GOAL.md"
  activated_at: "2026-05-13"
  source_freshness: active_git_file_after_g1_H1_G3_goal_shaped_pending_e1_execution_brief
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
active_goal:
  state: goal_shaped_pending_E1_execution_brief
  goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  goal_title: "Сформировать readiness-пакет для project bootstrap, tool-binding и validation scenes первого technical nucleus"
  goal_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness"
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/00_GOAL_CONTRACT.md"
  execution_log: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/execution_log.md"
  status: goal_shaped_pending_E1_execution_brief
  previous_active_goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
  previous_active_goal_title: "Проверить и адаптировать существующую workflow-процедуру Codex/project setup под первый technical nucleus"
  previous_active_goal_result: r1_accepted_goal_complete
  previous_active_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/01_GAS_COOP_GAME_PROJECT_EXECUTION_PROFILE.md"
  previous_active_goal_execution_log: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/execution_log.md"
  last_completed_goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
  last_completed_goal_result: r1_accepted_goal_complete
  previous_goal_superseded: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit"
  existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  existing_goal_artifact_status: accepted_route_gated_decision_map
  phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
  current_wave: none
  next_route: E1_EXECUTION_BRIEF
  next_route_mode: prepare_H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  review_scope: g1_goal_shape_formalized_H1_G3
  completion_scope: goal_shaped_pending_E1_execution_brief
  parent_goal_completion_state: not_complete_readiness_packet_pending
  smallest_useful_result: "Accepted readiness packet for project bootstrap, tool-binding, and validation-scene readiness."
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  unity_bootstrap_allowed_now: false
  task_master_graph_allowed_now: false
  next_goal_seed: none_active_goal_already_shaped
```

```yaml
shaped_goal:
  goal_id: core-technical-foundation-decision-brief
  goal_title: "Сформировать Core Technical Foundation Decision Brief"
  shaped_by_stage: G1_GOAL_SHAPE
  previous_status_before_p0_map_alignment: active_goal_shaped_pending_E1
  previous_recommended_next_stage_before_p0_map_alignment: E1_EXECUTION_BRIEF
  current_runtime_status: r1_accepted_route_gated_decision_map
  current_recommended_next_stage: G1_GOAL_SHAPE
  current_recommended_next_mode: shape_required_grid_gas_transfer_boundary_audit_goal
  repair_reason: "R1 accepted the existing decision brief as a route-gated decision map; Grid/Gas transfer remains a required A1 audit surface."
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
  existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  existing_goal_artifact_status: accepted_route_gated_decision_map
  decision_status_model:
    - decided
    - decision_gate
    - research_needed_D1
    - audit_needed_A1
    - human_decision_needed_S3
    - deferred_not_blocking_for_bootstrap
  required_decision_surfaces:
    - "multiplayer technology and host-player architecture"
    - "Grid/Topology transfer boundary"
    - "Gas Simulation durable logic architecture"
    - "smallest durable technical nucleus"
    - "Project Engineering & Codex Development Operating Model / H1_G2"
  validation_signal: "G1 can shape the required Grid/Gas transfer-boundary audit Goal for A1 without treating the accepted decision map as implementation approval."
```

```yaml
previous_active_goal:
  state: paused_superseded_partial_progress_not_accepted
  goal_id: first-playable-proof-slice-brief
  goal_title: "Сформировать минимальный playable proof slice для Expedition"
  goal_path: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief"
  goal_contract: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief/00_GOAL_CONTRACT.md"
  f0_artifact_path: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief/02_FIRST_PLAYABLE_PROOF_SLICE_BRIEF.md"
  result_status: "partial_progress_not_accepted"
  preservation_rule: "Useful scaffold/evidence only; do not treat as Goal completion."
```

## Active Goal snapshot

Active Goal:

`H1_G3_project_bootstrap_tool_binding_validation_scene_readiness`

Status:

`goal_shaped_pending_E1_execution_brief`

Goal contract:

`directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/00_GOAL_CONTRACT.md`

Execution log:

`directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/execution_log.md`

Next route:

`E1_EXECUTION_BRIEF`

Implementation, Unity bootstrap, Codex product/project execution, and Task Master graph creation are not authorized now.

Last completed Goal:

`H1_G2_codex_development_operating_model_and_architecture_protocols`

Accepted result: Gas Coop Game Project Execution Profile accepted as minimal project execution profile/addendum.

## R1-accepted active-front review

```yaml
active_goal_snapshot:
  goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  status: goal_shaped_pending_E1_execution_brief
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/00_GOAL_CONTRACT.md"
  execution_log: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/execution_log.md"
  last_completed_goal: H1_G2_codex_development_operating_model_and_architecture_protocols
  last_completed_goal_result: r1_accepted_goal_complete
  next_route: E1_EXECUTION_BRIEF
  next_route_mode: prepare_H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  purpose: >
    H1_G3 is shaped as the readiness Goal for project bootstrap, tool-binding,
    and validation-scene readiness. E1 must prepare the concrete readiness
    execution brief without running setup or product execution directly.
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  unity_bootstrap_allowed_now: false
  task_master_graph_allowed_now: false
```

## Superseded previous active Goal

Previous active Goal:

`grid-gas-transfer-boundary-audit`

Status:

`superseded_after_human_clarification`

Treatment:

- preserve as reset context;
- do not continue as A1 transfer-boundary audit;
- old project material is reference/evidence only;
- direct old-code transfer is out of scope;
- targeted old-project reference may occur later only after requirements are clear.

## R1 acceptance / next Goal candidate

R1 accepted `core-technical-foundation-decision-brief` as an accepted route-gated decision map.

Accepted:
- Multiplayer technology and host-player architecture are decided.
- Project Engineering & Codex Development Operating Model is decided at decision-brief level.
- The decision map is sufficient to route the remaining foundation risks.

Still unresolved:
- legacy Grid transfer boundary;
- GridV2 transfer / replacement boundary;
- GasV2R transfer / rewrite boundary;
- Gas↔Grid interaction authority/order/snapshot boundary.

Required next Goal candidate at that time, now superseded by the 2026-05-16 G1 reset:

```yaml
next_goal_candidate:
  id: grid-gas-transfer-boundary-audit
  title: "Провести аудит transfer boundary для legacy Grid, GridV2, GasV2R и Gas↔Grid interaction"
  recommended_next_stage: G1_GOAL_SHAPE
  expected_route_after_G1: A1_AUDIT
  implementation_allowed_now: false
```

## Previous accepted Goal

Previous accepted Goal: `core-technical-foundation-decision-brief` remains `r1_accepted_route_gated_decision_map`.

## Deferred items

The accepted specification did not silently decide or perform:

- Unity project creation;
- code transfer;
- final implementation;
- Task Master graph creation;
- Codex product/project execution;
- final multiplayer stack without evidence;
- final network authority model without decision record;
- exact gas taxonomy/reactions;
- final 25 cm vs 50 cm implementation;
- exact DI package / Unity folder layout / CI setup unless evidence is sufficient and the decision brief requires it;
- full engineering handbook;
- visual gas proof;
- Game Documentation promotion.

Any later Goal may leave a surface unresolved only when the unresolved item is explicitly routed to `D1_DEEP_RESEARCH`, `A1_AUDIT`, `S3_DECIDE`, Context Request, or marked `deferred_not_blocking_for_bootstrap`.

## R1 acceptance — H1_G2

R1 accepted `H1_G2_codex_development_operating_model_and_architecture_protocols`
as `completed_verified`.

Accepted artifact:

`directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/01_GAS_COOP_GAME_PROJECT_EXECUTION_PROFILE.md`

The active frontier was reviewed by `M0_DIRECTION_MAP`; H1_G3 is selected for `G1_GOAL_SHAPE` before selecting
P9, G0, E1, bootstrap, or implementation.

## 2026-05-20 M0 active-front review result

H1_G2 remains the last completed Goal:

`H1_G2_codex_development_operating_model_and_architecture_protocols`

Status:

`r1_accepted_goal_complete`

M0 selected the next frontier seed:

`H1_G3_project_bootstrap_tool_binding_validation_scene_readiness`

Recommended next stage:

`G1_GOAL_SHAPE`

H1_G3 is not yet an active shaped Goal. It is the selected next Goal seed pending G1.

Still forbidden until a later basis-valid route:

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

`H1_G3_project_bootstrap_tool_binding_validation_scene_readiness` is now the active shaped Goal.

```yaml
active_goal:
  goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  status: goal_shaped_pending_E1_execution_brief
  goal_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness"
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/00_GOAL_CONTRACT.md"
  execution_log: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/execution_log.md"
  last_completed_goal:
    goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
    result: r1_accepted_goal_complete
  next_route: E1_EXECUTION_BRIEF
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  unity_bootstrap_allowed_now: false
  product_repository_creation_allowed_now: false
  product_code_allowed_now: false
  task_master_graph_allowed_now: false
  real_internal_tool_setup_allowed_now: false
  unity_mcp_setup_allowed_now: false
  old_code_transfer_allowed_now: false
  game_documentation_promotion_allowed_now: false
```

E1 is the next route. It must not directly run Unity bootstrap, create a product repository, write product code, run Codex product/project execution, create a Task Master graph, perform real internal tool setup, configure Unity MCP, transfer old code, or promote Game Documentation.
