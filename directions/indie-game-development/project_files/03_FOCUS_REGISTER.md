# 03_FOCUS_REGISTER.md

```yaml
project_file_control:
  file: 03_FOCUS_REGISTER.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/03_FOCUS_REGISTER.md"
  activated_at: "2026-05-13"
  source_freshness: active_git_file_after_r1_first_technical_nucleus_spec_acceptance
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
focus:
  current_focus: "Run M0_DIRECTION_MAP after R1 accepted first-technical-nucleus-functional-spec."
  route_stage: M0_DIRECTION_MAP
  route_mode: review_active_front_after_first_technical_nucleus_spec_acceptance
  same_chat_allowed: false
  boundary_trigger: r1_accept_first_technical_nucleus_spec
  pending_state_carried: true
  pending_patch_pointer: r1_accept_first_technical_nucleus_spec_2026_05_18
  last_stage_result_pointer: "R1_GOAL_REVIEW_DISTILL accepted first-technical-nucleus-functional-spec as completed_verified."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings and execution route are verified."
  active_goal:
    goal_id: none_pending_m0_direction_map_review
    previous_goal_id: first-technical-nucleus-functional-spec
    previous_goal_status: r1_completed_verified_specification_accepted
  active_phase:
    phase_id: core-coop-technical-foundation-selection
    phase_name: Core Co-op Technical Foundation Selection
    phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
    status: active_pending_m0_after_r1_acceptance
    map_binding: H1_playable_technical_nucleus
    next_route: M0_DIRECTION_MAP
```

## Blockers / required inputs

- Missing context: `none blocking for repository maintenance apply; manual Project Files refresh blocks the next material M0 run`
- Human decision: `none pending for Phase start`
- Source conflict: `resolved by R1 acceptance maintenance; Project Files must be refreshed after commit`
- Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
- Required attachments/context for next stage:
  - exact `workflow/stage_prompts/M0_DIRECTION_MAP.md`
  - current Project Files 00-08 after R1 acceptance maintenance read-back
  - active Phase Brief: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`
  - completed specification artifact: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md`
  - R1 execution log entry: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/execution_log.md`

## Current focus boundary

M0 must review the active front after the accepted specification Goal. It must determine whether the next lifecycle route is Phase close consideration, required continuation, project/bootstrap readiness, or another map-bound correction.

Forbidden in M0:

- implementation;
- Unity bootstrap;
- old-code transfer;
- old-code audit as starting point;
- Codex product/project execution;
- Task Master graph creation;
- Game Documentation promotion;
- direct P9/G0/E1 launch without basis-valid map/frontier review.

## Current focus after G1 reset

The current focus after F0 synthesis formalization and evidence repair: R1 parent Goal review for `first-technical-nucleus-functional-spec`.

G1 superseded the transfer-boundary audit as the active Goal after human clarification.

R1 must verify that gas-first sequencing and the user approval gate after `gas_simulation_capability_frame` were preserved before accepting or route-gating the parent Goal.
