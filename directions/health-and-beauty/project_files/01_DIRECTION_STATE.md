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
  active_goal_title: "Починить Project `Питание` как repo-backed multi-chat nutrition loop"
  current_state_summary: "R1 accepted the repaired Project `Питание` repo-backed multi-chat nutrition loop Goal as complete after user-confirmed real-use validation; Direction is ready for P9 phase close review after repository maintenance/read-back and Project Files refresh."
  selected_goal_seed: nutrition-project-operational-setup-v0
  selected_frontier_node: d_nutrition_loop_shape_and_tooling
  next_route: P9_PHASE_CLOSE
  last_updated: "2026-05-21"

next_goal_seed: null

active_goal_status:
  goal_id: nutrition-project-operational-setup-v0
  status: r1_accepted_goal_complete

r1_review_result:
  verdict: accepted_complete
  review_date: "2026-05-21"
  next_route: P9_PHASE_CLOSE
  repository_projection_status: pending_readback_until_Codex_return

superseded_phase:
  phase_name: MacroFactor Nutrition AI Support Setup
  phase_path: "directions/health-and-beauty/phases/macrofactor-nutrition-ai-support-setup"
  status: superseded_paused
  reason: "MacroFactor-centered setup is no longer the current nutrition bottleneck."
  closure_status: not_completed
```

## Project Files export state

* Last refresh: `2026-05-17`
* Required refresh: `manual refresh after this repository patch read-back / diff verification`
* Known stale files: ChatGPT Project Files cache may still show older E1 route state until manually refreshed.
