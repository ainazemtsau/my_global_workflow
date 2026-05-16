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
  current_focus: "Run G1_GOAL_SHAPE to shape required Goal grid-gas-transfer-boundary-audit after R1 accepted the Core Technical Foundation Decision Brief as a route-gated decision map."
  route_stage: G1_GOAL_SHAPE
  route_mode: shape_required_grid_gas_transfer_boundary_audit_goal
  same_chat_allowed: false
  boundary_trigger: p0_phase_start_map_alignment_after_m0
  pending_state_carried: true
  pending_patch_pointer: r1_accept_route_gated_decision_map_and_select_grid_gas_audit_2026_05_16
  last_stage_result_pointer: "R1_GOAL_REVIEW_DISTILL accepted core-technical-foundation-decision-brief as route-gated decision map and Phase Progress Gate selected required Grid/Gas transfer-boundary audit."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings and execution route are verified."
  active_goal:
    goal_id: core-technical-foundation-decision-brief
    goal_title: "Сформировать Core Technical Foundation Decision Brief"
    goal_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief"
    goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
    existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
    status: r1_accepted_route_gated_decision_map
  active_phase:
    phase_id: core-coop-technical-foundation-selection
    phase_name: Core Co-op Technical Foundation Selection
    phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
    status: active_r1_accepted_decision_map_pending_grid_gas_transfer_audit
    map_binding: H1_playable_technical_nucleus
    next_route: G1_GOAL_SHAPE
```

## Blockers / required inputs

- Missing context: `none blocking for repository maintenance apply; manual Project Files refresh blocks the next material G1 run`
- Human decision: `none pending for Phase start`
- Source conflict: `resolved by approved G1 patch; Project Files must be refreshed after apply`
- Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
- Required attachments/context for next stage:
  - exact `workflow/stage_prompts/G1_GOAL_SHAPE.md`
  - current Project Files 00-08 after R1 repository maintenance read-back
  - active Phase Brief: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`
  - active Goal Contract: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md`

## Current focus boundary

G1 must shape the required transfer-boundary audit Goal narrowly for A1. G1 must not perform the audit itself.

Audit target:

- legacy Grid;
- GridV2;
- GasV2R;
- Gas↔Grid interaction.

Forbidden:

- Unity bootstrap;
- code transfer;
- Codex product/project execution;
- Task Master graph creation;
- Game Documentation promotion;
- implementation planning before audit result.

## Current focus after R1

The current focus is no longer B1 route-integrity repair.

R1 accepted the existing decision brief as an accepted route-gated decision map. The next required workflow step is to shape the audit Goal:

`grid-gas-transfer-boundary-audit`

G1 must shape this Goal narrowly for A1 audit. G1 must not perform the audit itself.

Audit target:
- legacy Grid;
- GridV2;
- GasV2R;
- Gas↔Grid interaction.

Forbidden:
- Unity bootstrap;
- code transfer;
- Codex product/project execution;
- Task Master graph creation;
- Game Documentation promotion;
- implementation planning before audit result.
