# 01_DIRECTION_STATE.md

```yaml
project_file_control:
  file: 01_DIRECTION_STATE.md
  schema: project_file_projection.v1
  direction: directions/health-and-beauty
  source_files:
    - "directions/health-and-beauty/project_files/01_DIRECTION_STATE.md"
  activated_at: "2026-05-12"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
direction:
  name: directions/health-and-beauty
  id: YqlUxoXMVTUr
  state: active
  workflow_version: vNext-R
  current_phase_pointer: "directions/health-and-beauty/phases/ai-nutrition-operating-layer"
  active_goal_pointer: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0"
  active_goal_title: "Собрать отдельный рабочий ChatGPT Project “Питание” как low-friction nutrition operating system"
  current_state_summary: "Objective Architecture migration corrected the active frontier: the Direction Objective is outcome-first, tooling is optional, and the prior Project `Питание` execution path is blocked as stale pending S3 decision."
  selected_goal_seed: nutrition-project-operational-setup-v0
  selected_frontier_node: d_nutrition_loop_shape_and_tooling
  next_route: S3_DECIDE
  last_updated: "2026-05-19"

next_goal_seed: null

active_goal_status:
  goal_id: nutrition-project-operational-setup-v0
  status: blocked_stale_not_basis_valid_pending_decision

superseded_phase:
  phase_name: MacroFactor Nutrition AI Support Setup
  phase_path: "directions/health-and-beauty/phases/macrofactor-nutrition-ai-support-setup"
  status: superseded_paused
  reason: "MacroFactor-centered setup is no longer the current nutrition bottleneck."
  closure_status: not_completed
```

## Project Files export state

* Last refresh: `2026-05-17`
* Required refresh: `after repository patch read-back / diff verification`
* Known stale files: ChatGPT Project Files cache may still show `E1_EXECUTION_BRIEF` / `execution_brief_pending` until manually refreshed.
