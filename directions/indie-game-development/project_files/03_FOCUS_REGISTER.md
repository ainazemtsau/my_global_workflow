# 03_FOCUS_REGISTER.md

```yaml
project_file_control:
  file: 03_FOCUS_REGISTER.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/03_FOCUS_REGISTER.md"
  activated_at: "2026-05-13"
  source_freshness: active_git_file_after_r1_H1_G2_acceptance_pending_m0_review
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
focus:
  current_focus: "Run repository maintenance for R1 H1_G2 acceptance projection reconciliation, then run M0_DIRECTION_MAP after manual Project Files refresh."
  route_stage: M0_DIRECTION_MAP
  route_mode: active_front_review_after_H1_G2_acceptance
  same_chat_allowed: false
  boundary_trigger: r1_H1_G2_goal_accepted
  pending_state_carried: true
  pending_patch_pointer: igd_r1_h1_g2_acceptance_projection_reconciliation_2026_05_20
  last_stage_result_pointer: "R1_GOAL_REVIEW_DISTILL accepted H1_G2 as completed_verified and selected M0_DIRECTION_MAP."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings and execution route are verified."
  active_goal:
    goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
    status: r1_accepted_goal_complete
    goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md"
    previous_goal_id: first-technical-nucleus-functional-spec
    previous_goal_status: r1_completed_verified_specification_accepted
  active_phase:
    phase_id: core-coop-technical-foundation-selection
    phase_name: Core Co-op Technical Foundation Selection
    phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
    status: active_H1_G2_r1_accepted_pending_M0_active_front_review
    map_binding: H1_playable_technical_nucleus
    next_route: M0_DIRECTION_MAP
```

## Blockers / required inputs

- Missing context: `manual Project Files refresh blocks the next material M0 run after R1 repository maintenance apply/read-back`
- Human decision: `none pending for M0 launch`
- Source conflict: `Project Files stale until this repository maintenance patch is applied/read back and manually refreshed`
- Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
- Required attachments/context for next stage:
  - exact `workflow/stage_prompts/M0_DIRECTION_MAP.md`
  - current Project Files 00-08 after R1 H1_G2 acceptance repository maintenance read-back and manual refresh
  - active Phase Brief
  - active Goal Contract and accepted profile artifact
  - Direction Map

## Current focus boundary

M0 must review the active frontier after R1 accepted `H1_G2_codex_development_operating_model_and_architecture_protocols`.

The review should decide whether `H1_G3_project_bootstrap_tool_binding_validation_scene_readiness`, P9, G0, E1, or another route is basis-valid before any material continuation.

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
- direct E1 launch without M0 active-front selection.

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
