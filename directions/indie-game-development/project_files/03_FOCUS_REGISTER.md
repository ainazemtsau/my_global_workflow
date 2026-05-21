# 03_FOCUS_REGISTER.md

```yaml
project_file_control:
  file: 03_FOCUS_REGISTER.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/03_FOCUS_REGISTER.md"
  activated_at: "2026-05-13"
  source_freshness: fresh_after_p0_project_bootstrap_validation_surface_setup_started
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
focus:
  current_focus: "Run G1_GOAL_SHAPE to shape the first Goal for Project Bootstrap and Validation Surface Setup."
  route_stage: G1_GOAL_SHAPE
  route_mode: shape_bootstrap_validation_surface_setup_envelope
  same_chat_allowed: false
  boundary_trigger: p0_project_bootstrap_validation_surface_setup_started
  pending_state_carried: true
  pending_patch_pointer: p0_start_project_bootstrap_validation_surface_setup_2026_05_21
  last_stage_result_pointer: "P0_PHASE_START started Project Bootstrap and Validation Surface Setup and selected G1_GOAL_SHAPE."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings and execution route are verified."
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  active_goal:
    goal_id: none_active_pending_G1_goal_shape
    status: none_active_pending_G1_goal_shape
    selected_first_goal_candidate: bootstrap-validation-surface-setup-envelope
    selected_first_goal_candidate_status: selected_for_G1_goal_shape
    previous_goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
    previous_goal_status: r1_accepted_goal_complete
  active_phase:
    phase_id: project-bootstrap-validation-surface-setup
    phase_name: Project Bootstrap and Validation Surface Setup
    phase_path: "directions/indie-game-development/phases/project-bootstrap-validation-surface-setup"
    status: active_pending_G1_goal_shape
    map_binding: "H1_playable_technical_nucleus / H1_G3_project_bootstrap_tool_binding_validation_scene_readiness -> H1_G4_durable_technical_nucleus"
    next_route: G1_GOAL_SHAPE
```

## Blockers / required inputs

- Missing context: `manual Project Files refresh blocks the next G1 run after P0 repository maintenance apply/read-back/commit/integration`
- Human decision: `none pending for G1 launch after refresh`
- Source conflict: `Project Files stale until this P0 repository maintenance patch is applied/read back and manually refreshed`
- Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
- Required attachments/context for next stage:
  - exact `workflow/stage_prompts/G1_GOAL_SHAPE.md`
  - refreshed Project Files 00-08 after P0 phase start
  - `directions/indie-game-development/phases/core-coop-technical-foundation-selection/phase_close_summary.md`
  - `directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/00_PHASE_BRIEF.md`
  - `directions/indie-game-development/project_files/07_PHASE_MEMORY_INDEX.md`
  - `directions/indie-game-development/project_files/08_DIRECTION_MAP.md`

## Current focus boundary

P0 started `Project Bootstrap and Validation Surface Setup` after `Core Co-op Technical Foundation Selection` closed complete by P9.

The next focus is `G1_GOAL_SHAPE` to shape the first Goal candidate `bootstrap-validation-surface-setup-envelope`. G1 must not run bootstrap, product repository creation, product code, real tool setup, Unity MCP setup, Task Master graph creation, or Codex product/project execution directly.

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
- direct X0/X1 launch without E1 readiness envelope and setup-state proof.

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

## 2026-05-21 R1 H1_G3 acceptance focus update

R1 accepted:

`H1_G3_project_bootstrap_tool_binding_validation_scene_readiness`

Current route:

```yaml
route_stage: P9_PHASE_CLOSE
route_mode: close_or_pause_core_coop_technical_foundation_selection_after_H1_G3_acceptance
boundary_trigger: r1_H1_G3_readiness_packet_accepted
active_goal:
  goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  status: r1_accepted_goal_complete
active_phase:
  status: active_H1_G3_r1_accepted_pending_P9_phase_close
codex_product_execution_allowed_now: false
```

P9 may close or pause the Phase after H1_G3 readiness acceptance. Implementation, Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, real internal tool setup, Unity MCP setup, old-code transfer, and Game Documentation promotion remain blocked.

## 2026-05-21 P9 phase close focus update

P9 closed:

`Core Co-op Technical Foundation Selection`

Current route:

```yaml
route_stage: P0_PHASE_START
route_mode: start_next_phase_after_core_coop_technical_foundation_selection_close
boundary_trigger: p9_core_coop_technical_foundation_selection_closed
active_goal:
  goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  status: closed_with_phase / r1_accepted_goal_complete
active_phase:
  status: closed_complete_by_P9
implementation_allowed_now: false
codex_product_execution_allowed_now: false
required_context_for_next_stage:
  - exact workflow/stage_prompts/P0_PHASE_START.md
  - refreshed Project Files 00-08 after P9 close
  - directions/indie-game-development/phases/core-coop-technical-foundation-selection/phase_close_summary.md
  - directions/indie-game-development/project_files/07_PHASE_MEMORY_INDEX.md
  - directions/indie-game-development/project_files/08_DIRECTION_MAP.md
```

P0 must start/reframe the next Phase. Implementation, Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, real internal tool setup, Unity MCP setup, old-code transfer, and Game Documentation promotion remain blocked.

## 2026-05-21 P0 phase start focus update

P0 started:

`Project Bootstrap and Validation Surface Setup`

Current route:

```yaml
route_stage: G1_GOAL_SHAPE
route_mode: shape_bootstrap_validation_surface_setup_envelope
same_chat_allowed: false
boundary_trigger: p0_project_bootstrap_validation_surface_setup_started
active_phase_id: project-bootstrap-validation-surface-setup
active_phase_status: active_pending_G1_goal_shape
active_goal_id: none_active_pending_G1_goal_shape
selected_first_goal_candidate: bootstrap-validation-surface-setup-envelope
implementation_allowed_now: false
codex_product_execution_allowed_now: false
```

G1 must shape the setup/validation envelope Goal before any bootstrap, setup, product repository creation, product code, Codex product/project execution, Task Master graph creation, Unity MCP setup, old-code transfer, or Game Documentation promotion.
