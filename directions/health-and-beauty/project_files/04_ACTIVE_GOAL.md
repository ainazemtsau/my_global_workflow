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
  state: active
  goal_id: nutrition-project-operational-setup-v0
  goal_name: "Собрать отдельный рабочий ChatGPT Project “Питание” как low-friction nutrition operating system"
  goal_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0"
  phase_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer"
  current_wave: none
  current_stage: G1_GOAL_SHAPE_formalized
  status: goal_contract_shaped_execution_brief_required
  next_route: E1_EXECUTION_BRIEF
```

## Goal Contract snapshot

* WHAT: Prepare separate Project `Питание` setup package with Project Instructions, Nutrition Base, Menu Preferences, Active Cycle, Tracking Protocol, Review & Sync Protocol, and dry-runs.
* WHY: v0 protocol exists but operational Project setup is not confirmed.
* DONE: Fresh Project `Питание` chat can plan cycle, track photo/voice events, handle unknown/defaulted answers, correct exceptions, review, and emit sync/update packets.
* Acceptance floor: Manual-install setup package plus 2-3 operational dry-runs.
* Validation: Cycle planning, meal-event, missing-answer, review/sync dry-runs.

## Prior artifact input

```yaml
prior_artifact_input:
  goal_id: ai-nutrition-operating-layer-v0
  status: design_protocol_artifact_input_not_operational_setup
```

## Preserved history

The prior MacroFactor active Goal is preserved as historical evidence under:

`directions/health-and-beauty/phases/macrofactor-nutrition-ai-support-setup/goals/ai-support-nutrition-recipes-menu-macrofactor`

It must not be executed as current work unless explicitly reshaped.
