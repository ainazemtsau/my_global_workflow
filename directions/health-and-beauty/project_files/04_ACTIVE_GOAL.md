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
  state: none
  goal_name: none
  goal_path: none
  phase_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer"
  current_wave: none

selected_goal_seed:
  title: "Собрать AI Nutrition Operating Layer v0"
  route_stage: G1_GOAL_SHAPE
  requires_shape_before_execution: true
  proposed_goal_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0"
```

## Goal Contract snapshot

* Goal Contract: `not created yet`
* DONE / acceptance: `to be shaped by G1_GOAL_SHAPE`
* Codex execution allowed: `no, not until Goal Contract and execution basis are created`

## Preserved history

The prior MacroFactor active Goal is preserved as historical evidence under:

`directions/health-and-beauty/phases/macrofactor-nutrition-ai-support-setup/goals/ai-support-nutrition-recipes-menu-macrofactor`

It must not be executed as current work unless explicitly reshaped.
