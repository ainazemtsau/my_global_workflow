# 03_FOCUS_REGISTER.md

```yaml
project_file_control:
  file: 03_FOCUS_REGISTER.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/03_FOCUS_REGISTER.md"
  activated_at: "2026-05-13"
  source_freshness: active_git_file_after_g1_H1_G2_formalization
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
focus:
  current_focus: "Run A1_AUDIT for H1_G2 Codex/project setup workflow fit-check after G1 formalization apply/read-back and manual Project Files refresh."
  route_stage: A1_AUDIT
  route_mode: audit_existing_workflow_codex_project_setup_first_use_fit
  same_chat_allowed: false
  boundary_trigger: g1_H1_G2_goal_formalized
  pending_state_carried: true
  pending_patch_pointer: igd_post_g1_a1_projection_reconciliation_2026_05_19
  last_stage_result_pointer: "G1_GOAL_SHAPE formalized H1_G2 as a goal and selected A1_AUDIT as the next route."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings and execution route are verified."
  active_goal:
    goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
    status: goal_shaped_pending_A1_audit
    goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md"
    previous_goal_id: first-technical-nucleus-functional-spec
    previous_goal_status: r1_completed_verified_specification_accepted
  active_phase:
    phase_id: core-coop-technical-foundation-selection
    phase_name: Core Co-op Technical Foundation Selection
    phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
    status: active_H1_G2_goal_shaped_pending_A1_audit
    map_binding: H1_playable_technical_nucleus
    next_route: A1_AUDIT
```

## Blockers / required inputs

- Missing context: `manual Project Files refresh blocks the next material A1 run after repository maintenance apply/read-back`
- Human decision: `none pending for A1 launch`
- Source conflict: `none expected after G1 H1_G2 repository maintenance apply/read-back and manual refresh`
- Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
- Required attachments/context for next stage:
  - exact `workflow/stage_prompts/A1_AUDIT.md`
  - current Project Files 00-08 after G1 H1_G2 formalization read-back and manual refresh
  - active Phase Brief: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`
  - active Goal Contract: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md`
  - active Goal execution log: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/execution_log.md`
  - completed specification artifact: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md`
  - accepted decision brief artifact: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`

## Current focus boundary

A1 must audit/fit-check the existing workflow Codex/project setup and execution-readiness procedure for `H1_G2_codex_development_operating_model_and_architecture_protocols`.

The audit should decide whether the existing workflow is sufficient, needs a minimal Indie project-specific input/profile, needs Workflow Governance repair, or requires exact missing context.

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
- direct E1 launch without an A1 verdict.

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
