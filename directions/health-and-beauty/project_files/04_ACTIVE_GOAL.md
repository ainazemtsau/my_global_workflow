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
  goal_name: "Починить Project `Питание` как repo-backed multi-chat nutrition loop"
  goal_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0"
  phase_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer"
  current_wave: none
  current_stage: G1_GOAL_SHAPE_formalized
  status: goal_shaped_pending_E1
  next_route: E1_EXECUTION_BRIEF
  use_policy: "Use the repaired Goal Contract and Working Context as current authority. Do not execute old E1/U1/R1 path."
```

## Goal Contract snapshot

* WHAT: Create a minimal repo-backed multi-chat Project `Питание` nutrition loop where GitHub markdown files are durable nutrition state, ChatGPT Project Files are a refreshable runtime cache, chat memory is non-authoritative, and Codex is save-only repository maintenance writer.
* WHY: The previous Project `Питание` path was stale / not basis-valid after Objective Architecture correction; S3 selected the repaired shape that keeps Project `Питание` as UI while moving authority to repository-backed state.
* DONE: One complete low-friction loop is proven: baseline/current plan -> weekly menu -> tracking/adaptation -> review -> save to GitHub -> Project Files refresh -> fresh chat continuation.
* Acceptance floor: `first_week_bootstrap_from_empty_state`, `later_week_bootstrap_from_saved_state`, `fresh_menu_chat_from_saved_plan`, `fresh_tracking_chat_from_saved_plan_and_menu`, `week_review_from_saved_report`, and `project_files_refresh_reproducibility`.
* Validation: E1 must plan implementation and validation; later execution must prove repository read-back, dry-runs, Project Files refresh reproducibility, and fresh-chat continuation without hidden memory or manual giant packets.

This snapshot reflects the repaired G1 Goal shape and remains pending E1 execution planning.

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
