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
  current_phase_pointer: "directions/health-and-beauty/phases/first-working-health-body-operator-training-v0"
  active_goal_pointer: null
  active_goal_title: null
  current_state_summary: "Active Phase creates the first working Health/Body Operator training process v0. Workflow builds the process; the operational Project runs daily nutrition/training/logging/adjustment. Next route is G1_GOAL_SHAPE for the first Goal."
  selected_goal_seed: "shape-operational-boundary-and-training-process-v0"
  selected_frontier_node: n2_first_weekly_body_transformation_correction_loop
  next_route: G1_GOAL_SHAPE
  last_updated: "2026-05-23"
```

```yaml
next_goal_seed:
  candidate_id: shape-operational-boundary-and-training-process-v0
  name: "Сформировать границу workflow/operator и Goal-контракт тренировочного процесса v0"
  target_phase: first-working-health-body-operator-training-v0
  target_graph_node: operational_boundary_gate
  route: G1_GOAL_SHAPE
```

```yaml
active_goal_status:
  goal_id: null
  status: no_active_goal
```

```yaml
active_phase:
  phase_id: first-working-health-body-operator-training-v0
  phase_name: "Первый рабочий Health/Body Operator: тренировочный процесс v0"
  phase_path: "directions/health-and-beauty/phases/first-working-health-body-operator-training-v0"
  status: active
  map_link: n2_first_weekly_body_transformation_correction_loop
  phase_candidate_classification: standalone_phase
```

```yaml
latest_closed_phase:
  phase_id: ai-nutrition-operating-layer
  phase_name: "Собрать удобный, научно обоснованный процесс питания без тяжёлого трекинга"
  phase_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer"
  status: closed_complete
  closed_at: "2026-05-22"
  phase_close_summary_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/phase_close_summary.md"
```

## Operational boundary

The workflow does not run the daily process. The operational Health/Body Operator Project runs nutrition, training, logs, daily decisions, adjustments, and local process customization.

Workflow is used for strategic redesign, evidence-heavy decisions, new tools, global process changes, and repository/state maintenance.

## Direction Map note

`08_DIRECTION_MAP.md` was intentionally not changed by P0. The Active Front remains `n2_first_weekly_body_transformation_correction_loop`. Any old map route-binding text saying `P0_PHASE_START` is stale-but-nonblocking for the named next stage `G1_GOAL_SHAPE`, because this file and `02_CURRENT_PHASE.md` are the fresh Phase state after approved repository patch/read-back.

## Project Files export state

Required refresh: manual refresh after this P0 repository patch read-back / diff verification / commit verification.
