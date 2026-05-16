# 03_FOCUS_REGISTER.md

```yaml
project_file_control:
  file: 03_FOCUS_REGISTER.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/03_FOCUS_REGISTER.md"
  activated_at: "2026-05-13"
  source_freshness: active_git_file_after_p0_repository_apply_readback
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
focus:
  current_focus: "Run E1_EXECUTION_BRIEF for the first-technical-nucleus-functional-spec Goal."
  route_stage: E1_EXECUTION_BRIEF
  route_mode: plan_gated_sequential_first_technical_nucleus_spec
  same_chat_allowed: false
  boundary_trigger: p0_phase_start_map_alignment_after_m0
  pending_state_carried: true
  pending_patch_pointer: g1_formalize_first_technical_nucleus_functional_spec_2026_05_16
  last_stage_result_pointer: "G1_GOAL_SHAPE superseded grid-gas-transfer-boundary-audit and formalized first-technical-nucleus-functional-spec."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings and execution route are verified."
  active_goal:
    goal_id: first-technical-nucleus-functional-spec
    goal_title: "Сформировать функционально-техническую спецификацию первого technical nucleus"
    goal_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec"
    goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/00_GOAL_CONTRACT.md"
    existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
    status: goal_shaped_pending_E1
  active_phase:
    phase_id: core-coop-technical-foundation-selection
    phase_name: Core Co-op Technical Foundation Selection
    phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
    status: active_g1_formalized_first_technical_nucleus_spec_pending_E1
    map_binding: H1_playable_technical_nucleus
    next_route: E1_EXECUTION_BRIEF
```

## Blockers / required inputs

- Missing context: `none blocking for repository maintenance apply; manual Project Files refresh blocks the next material E1 run`
- Human decision: `none pending for Phase start`
- Source conflict: `resolved by approved G1 patch; Project Files must be refreshed after apply`
- Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
- Required attachments/context for next stage:
  - exact `workflow/stage_prompts/E1_EXECUTION_BRIEF.md`
  - current Project Files 00-08 after G1 repository maintenance read-back
  - active Phase Brief: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`
  - active Goal Contract: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/00_GOAL_CONTRACT.md`

## Current focus boundary

E1 must prepare gated sequential execution planning for the first technical nucleus functional specification.

Required sequence:

1. gas simulation capability frame;
2. user approval gate after gas block;
3. level/spatial requirements;
4. Grid/topology substrate requirements;
5. cross-system interaction requirements;
6. destructibility compatibility boundary;
7. validation/demo requirements;
8. synthesis.

Forbidden:

- implementation;
- Unity bootstrap;
- old-code transfer;
- old-code audit as starting point;
- Codex product/project execution;
- Task Master graph creation;
- Game Documentation promotion;
- Grid/topology work before user-accepted gas frame.

## Current focus after G1 reset

The current focus after G1 reset: E1 execution brief for `first-technical-nucleus-functional-spec`.

G1 superseded the transfer-boundary audit as the active Goal after human clarification.

E1 must preserve gas-first sequencing and the user approval gate after `gas_simulation_capability_frame`.
