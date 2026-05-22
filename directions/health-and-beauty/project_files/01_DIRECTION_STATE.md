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
  current_phase_pointer: null
  active_goal_pointer: null
  active_goal_title: null
  current_state_summary: "P9 closed the AI Nutrition Operating Layer Phase as close_complete after R1 accepted the repo-backed Project `Питание` nutrition loop Goal complete. Next action is Project Files refresh and P0_PHASE_START for a non-duplicate next Phase."
  selected_goal_seed: null
  selected_frontier_node: n2_minimal_body_metrics_packet
  next_route: P0_PHASE_START
  last_updated: "2026-05-22"

next_goal_seed: null

active_goal_status:
  goal_id: nutrition-project-operational-setup-v0
  status: closed_under_closed_phase

latest_closed_phase:
  phase_id: ai-nutrition-operating-layer
  phase_name: "Собрать удобный, научно обоснованный процесс питания без тяжёлого трекинга"
  phase_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer"
  status: closed_complete
  closed_at: "2026-05-22"
  phase_close_summary_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/phase_close_summary.md"

r1_review_result:
  verdict: accepted_complete
  review_date: "2026-05-21"
  next_route: P0_PHASE_START
  repository_projection_status: p9_repository_maintenance_readback_completed

superseded_phase:
  phase_name: MacroFactor Nutrition AI Support Setup
  phase_path: "directions/health-and-beauty/phases/macrofactor-nutrition-ai-support-setup"
  status: superseded_paused
  reason: "MacroFactor-centered setup is no longer the current nutrition bottleneck."
  closure_status: not_completed
```

## Project Files export state

* Last refresh: `2026-05-17`
* Required refresh: `manual refresh after P9 repository patch read-back / diff verification`
* Known stale files: ChatGPT Project Files cache may still show older P9 or E1 route state until manually refreshed.
