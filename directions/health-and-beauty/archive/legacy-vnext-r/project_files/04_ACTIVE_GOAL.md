# 04_ACTIVE_GOAL.md

```yaml
project_file_control:
  file: 04_ACTIVE_GOAL.md
  schema: project_file_projection.v1
  direction: directions/health-and-beauty
  source_files:
    - "directions/health-and-beauty/project_files/04_ACTIVE_GOAL.md"
  activated_at: "2026-05-12"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
active_goal:
  state: no_active_goal
  goal_id: null
  goal_name: null
  goal_path: null
  phase_path: "directions/health-and-beauty/phases/first-working-health-body-operator-training-v0"
  current_wave: none
  current_stage: none
  status: none
  next_route: G1_GOAL_SHAPE
  use_policy: "No active Goal exists yet. Next material route is G1_GOAL_SHAPE to shape the first Goal for the active Phase. Do not execute training process work, daily logging, or old Project `Питание` setup routes before G1/E1."
```

## Next Goal seed

```yaml
next_goal_seed:
  candidate_id: shape-operational-boundary-and-training-process-v0
  name: "Сформировать границу workflow/operator и Goal-контракт тренировочного процесса v0"
  phase_id: first-working-health-body-operator-training-v0
  phase_path: "directions/health-and-beauty/phases/first-working-health-body-operator-training-v0"
  graph_node: operational_boundary_gate
  recommended_next_stage: G1_GOAL_SHAPE
  confidence: high
```

## Latest completed Goal snapshot

```yaml
latest_completed_goal:
  goal_id: nutrition-project-operational-setup-v0
  goal_name: "Починить Project `Питание` как repo-backed multi-chat nutrition loop"
  goal_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0"
  closed_under_phase: ai-nutrition-operating-layer
  phase_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer"
  review_verdict: accepted_complete
  goal_state: closed_under_closed_phase
```

## Boundary note

G1 must not shape a Goal that requires workflow to hold daily training logs, daily nutrition logs, or ordinary week-to-week operation. The Goal must shape how the autonomous Operational Project will perform those functions.
