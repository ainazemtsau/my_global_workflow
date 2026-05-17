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
  active_goal_pointer: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0"
  active_goal_title: "Собрать AI Nutrition Operating Layer v0"
  current_state_summary: "AI Nutrition Operating Layer v0 exists as a design/protocol artifact; operational setup remains required before claiming a working ChatGPT Project `Питание`."
  selected_goal_seed: nutrition_project_operational_setup_seed
  next_route: G1_GOAL_SHAPE
  last_updated: "2026-05-17"

next_goal_seed:
  id_candidate: nutrition-project-operational-setup-v0
  title: "Собрать рабочий ChatGPT Project “Питание” на базе AI Nutrition Operating Layer v0"
  route: G1_GOAL_SHAPE
  reason: "Shape the setup/installation Goal for Project Instructions, Snapshot, Current Loop, Active Menu starter, save/update behavior, and minimal dry-run scenarios."
  forbidden:
    - clinical_nutrition_advice
    - macrofactor_centered_workflow
    - heavy_calorie_macro_ledger
    - tracker_database_api_automation
    - full_body_transformation_plan
    - P9_PHASE_CLOSE

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
