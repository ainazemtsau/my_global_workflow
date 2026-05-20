# 03_FOCUS_REGISTER.md

```yaml
project_file_control:
  file: 03_FOCUS_REGISTER.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/03_FOCUS_REGISTER.md"
  activated_at: "2026-05-13"
  source_freshness: active_git_file_after_g1_H1_G3_goal_shaped_pending_e1_execution_brief
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
focus:
  current_focus: "Run E1_EXECUTION_BRIEF for H1_G3 after repository maintenance apply/read-back and manual Project Files refresh."
  route_stage: E1_EXECUTION_BRIEF
  route_mode: prepare_H1_G3_readiness_execution_brief
  same_chat_allowed: false
  boundary_trigger: g1_H1_G3_goal_contract_formalized_pending_E1
  pending_state_carried: true
  pending_patch_pointer: g1_formalize_H1_G3_project_bootstrap_tool_binding_validation_scene_readiness_2026_05_20
  last_stage_result_pointer: "G1_GOAL_SHAPE formalized H1_G3_project_bootstrap_tool_binding_validation_scene_readiness and selected E1_EXECUTION_BRIEF."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings and execution route are verified."
  active_goal:
    goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
    status: goal_shaped_pending_E1_execution_brief
    goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/00_GOAL_CONTRACT.md"
    execution_log: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/execution_log.md"
    previous_goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
    previous_goal_status: r1_accepted_goal_complete
  active_phase:
    phase_id: core-coop-technical-foundation-selection
    phase_name: Core Co-op Technical Foundation Selection
    phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
    status: active_H1_G3_goal_shaped_pending_E1_execution_brief
    map_binding: H1_playable_technical_nucleus
    next_route: E1_EXECUTION_BRIEF
```

## Blockers / required inputs

- Missing context: `manual Project Files refresh blocks the next E1 run after G1 H1_G3 repository maintenance apply/read-back`
- Human decision: `none pending for E1 launch`
- Source conflict: `Project Files stale until this repository maintenance patch is applied/read back and manually refreshed`
- Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
- Required attachments/context for next stage:
  - exact `workflow/stage_prompts/E1_EXECUTION_BRIEF.md`
  - current Project Files 00-08 after G1 H1_G3 formalization repository maintenance read-back and manual refresh
  - active Phase Brief
  - active H1_G3 Goal Contract and execution log
  - accepted H1_G2 profile artifact
  - Direction Map

## Current focus boundary

G1 formalized `H1_G3_project_bootstrap_tool_binding_validation_scene_readiness` after M0 selected it as the active-front node.

The next focus is `E1_EXECUTION_BRIEF` to prepare the concrete readiness execution envelope. E1 must not run bootstrap, product repository creation, product code, real tool setup, Unity MCP setup, Task Master graph creation, or Codex product/project execution directly.

Forbidden in this focus:

- implementation;
- Unity bootstrap;
- old-code transfer;
- old-code audit as starting point;
- Codex product/project execution;
- Task Master graph creation;
- Game Documentation promotion;
- real internal tool setup;
- broad engineering handbook creation;
- direct C1/C2 launch without E1 readiness envelope.

## 2026-05-19 G1 H1_G2 formalization

```yaml
focus_update_after_g1_H1_G2:
  active_goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
  active_goal_status: goal_shaped_pending_A1_audit
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md"
  next_route: A1_AUDIT
  next_route_mode: audit_existing_workflow_codex_project_setup_first_use_fit
  core_correction: >
    This Goal must audit/fit-check the existing workflow Codex/project setup
    procedure. It must not create a second Indie-only workflow layer.
  forbidden:
    - implementation
    - Unity bootstrap
    - Codex product/project execution
    - Task Master graph creation
    - real internal tool setup
    - old-code transfer
    - old-code audit as starting point
    - Game Documentation promotion
```

## Historical focus after G1 reset

The focus after F0 synthesis formalization and evidence repair was R1 parent Goal review for `first-technical-nucleus-functional-spec`.

G1 superseded the transfer-boundary audit as the active Goal after human clarification.

R1 must verify that gas-first sequencing and the user approval gate after `gas_simulation_capability_frame` were preserved before accepting or route-gating the parent Goal.

## 2026-05-20 R1 H1_G2 acceptance focus update

H1_G2 is accepted as complete.

Current focus is repository projection reconciliation and then M0 active-front review.
M0 must determine the next basis-valid route after H1_G2 acceptance.

## 2026-05-20 M0 active-front review focus update

M0 selected:

`H1_G3_project_bootstrap_tool_binding_validation_scene_readiness`

Next focus:

`G1_GOAL_SHAPE`

G1 must shape the H1_G3 Goal Contract for project bootstrap, tool-binding, and validation-scene readiness.

This focus does not authorize execution. It does not create product repo, Unity project, Codex config, AGENTS.md, Task Master graph, Serena, Basic Memory, Unity MCP, scenes, prefabs, assets, scripts, old-code transfer, or implementation.

## 2026-05-20 G1 H1_G3 formalization focus update

G1 shaped:

`H1_G3_project_bootstrap_tool_binding_validation_scene_readiness`

Current route:

```yaml
route_stage: E1_EXECUTION_BRIEF
route_mode: prepare_H1_G3_readiness_execution_brief
active_goal:
  goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  status: goal_shaped_pending_E1_execution_brief
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/00_GOAL_CONTRACT.md"
same_chat_allowed: false
codex_product_execution_allowed_now: false
```

E1 must plan the readiness envelope only. Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, real internal tool setup, Unity MCP setup, old-code transfer, and Game Documentation promotion remain blocked.
