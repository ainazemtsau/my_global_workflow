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
  current_focus: "Run A1_AUDIT for the shaped grid-gas-transfer-boundary-audit Goal."
  route_stage: A1_AUDIT
  route_mode: audit_grid_gas_transfer_boundary
  same_chat_allowed: false
  boundary_trigger: p0_phase_start_map_alignment_after_m0
  pending_state_carried: true
  pending_patch_pointer: r1_accept_route_gated_decision_map_and_select_grid_gas_audit_2026_05_16
  last_stage_result_pointer: "R1_GOAL_REVIEW_DISTILL accepted core-technical-foundation-decision-brief as route-gated decision map and Phase Progress Gate selected required Grid/Gas transfer-boundary audit."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings and execution route are verified."
  active_goal:
    goal_id: grid-gas-transfer-boundary-audit
    goal_title: "Провести аудит transfer boundary для legacy Grid, GridV2, GasV2R и Gas↔Grid interaction"
    goal_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit"
    goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit/00_GOAL_CONTRACT.md"
    existing_goal_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
    status: goal_shaped_pending_A1
  active_phase:
    phase_id: core-coop-technical-foundation-selection
    phase_name: Core Co-op Technical Foundation Selection
    phase_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection"
    status: active_g1_formalized_grid_gas_transfer_boundary_audit_pending_A1
    map_binding: H1_playable_technical_nucleus
    next_route: A1_AUDIT
```

## Blockers / required inputs

- Missing context: `none blocking for repository maintenance apply; manual Project Files refresh blocks the next material A1 run`
- Human decision: `none pending for Phase start`
- Source conflict: `resolved by approved G1 patch; Project Files must be refreshed after apply`
- Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
- Required attachments/context for next stage:
  - exact `workflow/stage_prompts/A1_AUDIT.md`
  - current Project Files 00-08 after G1 repository maintenance read-back
  - active Phase Brief: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`
  - active Goal Contract: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit/00_GOAL_CONTRACT.md`

## Current focus boundary

A1 must audit the shaped transfer-boundary Goal. A1 must not implement or transfer code.

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

## Current focus after G1

The current focus after G1: A1 audit of transfer boundary, with product-fit filters and destructibility guardrail.

G1 formalized the audit Goal:

`grid-gas-transfer-boundary-audit`

A1 must audit it without implementation, Unity bootstrap, code transfer, Codex product/project execution, Task Master graph creation, or Game Documentation promotion.

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
