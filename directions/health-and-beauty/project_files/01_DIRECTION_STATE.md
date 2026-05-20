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
  current_state_summary: "G1 formalized the repaired active Goal: Project `Питание` is kept as user-facing UI, GitHub markdown state is canonical, Project Files are runtime cache, Codex is save-only writer, and E1 must plan implementation/validation."
  selected_goal_seed: nutrition-project-operational-setup-v0
  selected_frontier_node: d_nutrition_loop_shape_and_tooling
  next_route: E1_EXECUTION_BRIEF
  last_updated: "2026-05-19"

next_goal_seed: null

active_goal_status:
  goal_id: nutrition-project-operational-setup-v0
  status: goal_shaped_pending_E1

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
* Known stale files: ChatGPT Project Files cache may still show older standalone/pending-decision state until manually refreshed.
