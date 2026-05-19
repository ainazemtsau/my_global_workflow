# 04_ACTIVE_GOAL.md

```yaml
project_file_control:
  file: 04_ACTIVE_GOAL.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/04_ACTIVE_GOAL.md"
  activated_at: "2026-05-13"
  source_freshness: active_git_file_after_r1_first_technical_nucleus_spec_acceptance
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
active_goal:
  state: goal_shaped_pending_A1_audit
  goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
  goal_title: "Проверить и адаптировать существующую workflow-процедуру Codex/project setup под первый technical nucleus"
  goal_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols"
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md"
  execution_log: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/execution_log.md"
  status: goal_shaped_pending_A1_audit
  previous_active_goal_id: first-technical-nucleus-functional-spec
  previous_active_goal_title: "Сформировать функционально-техническую спецификацию первого technical nucleus"
  previous_active_goal_result: r1_completed_verified_specification_accepted
  previous_active_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md"
  previous_active_goal_execution_log: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/execution_log.md"
  previous_goal_superseded: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit"
  existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  existing_goal_artifact_status: accepted_route_gated_decision_map
  phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
  current_wave: none
  next_route: A1_AUDIT
  next_route_mode: audit_existing_workflow_codex_project_setup_first_use_fit
  review_scope: audit_existing_workflow_codex_project_setup_first_use_fit
  completion_scope: functional_technical_specification_only
  parent_goal_completion_state: r1_completed_verified_specification_accepted
  smallest_useful_result: "A1 verdict on whether the existing workflow Codex/project setup procedure can be used for Gas Coop Game."
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  unity_bootstrap_allowed_now: false
  task_master_graph_allowed_now: false
  next_goal_seed:
    id: H1_G2_codex_development_operating_model_and_architecture_protocols
    title: "Проверить и адаптировать существующую workflow-процедуру Codex/project setup под первый technical nucleus"
    recommended_next_stage: A1_AUDIT
    map_binding: H1_playable_technical_nucleus / H1_G2_codex_development_operating_model_and_architecture_protocols
    implementation_allowed_now: false
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

`H1_G2_codex_development_operating_model_and_architecture_protocols`

Status:

`goal_shaped_pending_A1_audit`

Goal contract:

`directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md`

Execution log:

`directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/execution_log.md`

Next route:

`A1_AUDIT`

Implementation, Unity bootstrap, Codex product/project execution, and Task Master graph creation are not authorized now.

Last completed Goal:

`first-technical-nucleus-functional-spec`

Accepted result: first technical nucleus functional/technical specification.

## G1-shaped next audit

```yaml
active_goal_snapshot:
  goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
  status: goal_shaped_pending_A1_audit
  next_route: A1_AUDIT
  next_route_mode: audit_existing_workflow_codex_project_setup_first_use_fit
  purpose: >
    Audit/fit-check the existing workflow Codex/project setup and execution-readiness
    procedure on first real use before project bootstrap, durable nucleus implementation,
    or Codex product/project execution.
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
