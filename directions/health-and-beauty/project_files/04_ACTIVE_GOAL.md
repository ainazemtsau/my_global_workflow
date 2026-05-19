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
  state: shaped
  goal_id: nutrition-project-operational-setup-v0
  goal_name: "Собрать отдельный рабочий ChatGPT Project “Питание” как low-friction nutrition operating system"
  goal_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0"
  phase_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer"
  current_wave: none
  current_stage: G1_GOAL_SHAPE_formalized
  status: goal_shaped_pending_E1
  next_route: E1_EXECUTION_BRIEF
  use_policy: "Fresh shaped Goal Contract; do not execute Project setup until E1 defines execution envelope, validators, and route."
```

## Goal Contract snapshot

* WHAT: Create a repo-backed standalone Project `Питание` v0 package with Project Instructions, Project Files, durable nutrition state, low-friction loop protocols, Codex Save Operator protocol, and dry-run acceptance file.
* WHY: S3 selected Project `Питание` as the repaired standalone container/tool for the nutrition loop; G1 formalized the minimum complete usable loop.
* DONE: Fresh Project `Питание` chat can plan cycle/defaults, process meal/photo/voice events with missing-answer defaults, correct exceptions, review, and emit sync/update packets; Codex Save Operator can save/read back approved state packets.
* Acceptance floor: Manual-install setup package plus three synthetic dry-runs.
* Validation: Cycle planning/restart, meal-event + exception correction, and review/sync dry-runs.

This snapshot reflects the fresh G1 Goal shape and remains pending E1 execution planning.

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
