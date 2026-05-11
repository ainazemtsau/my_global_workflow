# 04\_ACTIVE\_GOAL.md

```yaml
project_file_control:
  file: 04_ACTIVE_GOAL.md
  schema: project_file_projection.v1
  direction: directions/health-and-beauty
  source_files:
    - "directions/health-and-beauty/project_files/04_ACTIVE_GOAL.md"
  activated_at: "2026-05-11"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes

```

```yaml
active_goal:
  state: active
  goal_name: "Собрать AI-поддержку питания, рецептов и меню под MacroFactor"
  goal_path: "directions/health-and-beauty/phases/macrofactor-nutrition-ai-support-setup/goals/ai-support-nutrition-recipes-menu-macrofactor"
  phase_path: "directions/health-and-beauty/phases/macrofactor-nutrition-ai-support-setup"
  current_wave: none

```

## Goal Contract snapshot

*   Goal: create AI support for nutrition, recipes, menus, and MacroFactor-friendly output.
*   DONE / acceptance: draft; should be tightened by `G1_GOAL_SHAPE` before execution.
*   Codex execution allowed: `no, not until project/tool binding is verified`

## Preserved history

The pre-vNext Goal note was moved into the current Phase without deletion or cloning. Its child history remains under the Goal: Sessions, Wave Cards, Goal Brief, Execution Pack.
