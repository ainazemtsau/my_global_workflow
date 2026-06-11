# Goal Working Context — Repaired Project `Питание` nutrition loop

```yaml
artifact_control:
  artifact_name: "Goal Working Context — Repaired Project `Питание` nutrition loop"
  schema: goal_working_context.v1
  owner_layer: direction_goal
  status: active
  direction: directions/health-and-beauty
  phase_path: directions/health-and-beauty/phases/ai-nutrition-operating-layer
  goal_id: nutrition-project-operational-setup-v0
  shaped_by_stage: G1_GOAL_SHAPE
  shaped_at: "2026-05-20"
  lifecycle_state: goal_shaped_pending_E1
```

## Direction

`directions/health-and-beauty`

## Active Phase

`directions/health-and-beauty/phases/ai-nutrition-operating-layer`

Phase objective: build a convenient, evidence-based nutrition process without heavy tracking.

## Phase fit

This Goal directly repairs the active nutrition bottleneck: no stable low-friction process for planning, correction, state persistence, and weekly continuation.

## Source state

S3 selected:

`keep_and_repair_project_pitanie_repo_backed_multi_chat_loop`

Use the old Project `Питание` artifacts only as historical/current input. Do not execute the old E1/U1/R1 route.

## Selected solution shape

```yaml
source_of_truth_policy:
  canonical_state: GitHub markdown files
  chatgpt_project_files: runtime_cache_only
  chat_memory: non_authoritative

runtime_container_policy:
  project_pitanie: kept_as_user_facing_runtime_UI
  repository: durable_state
  codex: save_only_repository_maintenance_writer

chat_role_model:
  - dietitian_plan_builder
  - weekly_menu_builder
  - weekly_tracking_and_adaptation
  - dietitian_review_and_sync

weekly_cycle:
  - dietitian_plan_or_review
  - weekly_menu
  - weekly_tracking
  - dietitian_review_and_sync
```

## Likely state files for E1 to evaluate

E1 must evaluate exact file set and may cut/merge if Component Necessity Test proves a simpler structure still preserves the acceptance floor.

Candidate state files:

- `directions/health-and-beauty/projects/nutrition/state/USER_NUTRITION_BASELINE.md`
- `directions/health-and-beauty/projects/nutrition/state/CURRENT_NUTRITION_PLAN.md`
- `directions/health-and-beauty/projects/nutrition/state/MENU_PREFERENCES.md`
- `directions/health-and-beauty/projects/nutrition/state/ACTIVE_WEEK_MENU.md`
- `directions/health-and-beauty/projects/nutrition/state/WEEK_SHOPPING_LIST.md`
- `directions/health-and-beauty/projects/nutrition/state/WEEK_PREP_PLAN.md`
- `directions/health-and-beauty/projects/nutrition/state/WEEK_TRACKING_REPORT.md`
- `directions/health-and-beauty/projects/nutrition/state/REVIEW_DECISIONS.md`
- `directions/health-and-beauty/projects/nutrition/state/NEXT_WEEK_INPUTS.md`

## Likely protocol files for E1 to evaluate

- `directions/health-and-beauty/projects/nutrition/project_files/00_NUTRITION_START_HERE.md`
- `directions/health-and-beauty/projects/nutrition/project_files/01_DIETITIAN_PLAN_PROTOCOL.md`
- `directions/health-and-beauty/projects/nutrition/project_files/02_WEEKLY_MENU_PROTOCOL.md`
- `directions/health-and-beauty/projects/nutrition/project_files/03_TRACKING_AND_ADAPTATION_PROTOCOL.md`
- `directions/health-and-beauty/projects/nutrition/project_files/04_REVIEW_AND_SYNC_PROTOCOL.md`
- `directions/health-and-beauty/projects/nutrition/project_files/05_STATE_AND_SAVE_PROTOCOL.md`
- `directions/health-and-beauty/projects/nutrition/project_files/06_CHAT_LAUNCHERS.md`
- `directions/health-and-beauty/projects/nutrition/protocols/CODEX_SAVE_OPERATOR.md`
- `directions/health-and-beauty/projects/nutrition/protocols/DRY_RUN_ACCEPTANCE.md`

## Required context for E1

Default-loaded context:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md`
- `workflow/runtime/CONTEXT_ACQUISITION_POLICY.md`
- `workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md`
- `workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md`
- `workflow/stage_registry/STAGE_REGISTRY.md`
- `directions/health-and-beauty/project_files/00_DIRECTION_START_HERE.md`
- `directions/health-and-beauty/project_files/01_DIRECTION_STATE.md`
- `directions/health-and-beauty/project_files/02_CURRENT_PHASE.md`
- `directions/health-and-beauty/project_files/03_FOCUS_REGISTER.md`
- `directions/health-and-beauty/project_files/04_ACTIVE_GOAL.md`
- `directions/health-and-beauty/project_files/05_PORTFOLIO_QUEUE.md`
- `directions/health-and-beauty/project_files/06_CONTEXT_LIBRARY_INDEX.md`
- `directions/health-and-beauty/project_files/07_PHASE_MEMORY_INDEX.md`
- `directions/health-and-beauty/project_files/08_DIRECTION_MAP.md`

Exact stage prompt required in the E1 chat:

- `workflow/stage_prompts/E1_EXECUTION_BRIEF.md`

Request-only context for E1 if needed:

- this Goal Contract;
- this Goal Working Context;
- prior Project `Питание` setup files;
- existing nutrition project files under `directions/health-and-beauty/projects/nutrition/**`;
- existing setup package under `directions/health-and-beauty/project_setup/pitanie/**`;
- user nutrition baseline/preferences only when needed for dry-run test design, not for live diet generation.

## Allowed actions for E1

- Produce minimum execution brief.
- Choose execution topology.
- Define exact files to create/update.
- Define validation anchors and dry-run acceptance.
- Produce Codex repository maintenance plan/card if needed.
- Route to U1 only for ChatGPT Project UI setup if human-guided UI work is required.
- Route to D1 only if current external/platform evidence is blocking.

## Forbidden actions for E1

- Do not generate live diet/menu as the Goal outcome.
- Do not revive MacroFactor/heavy tracker as default.
- Do not require detailed calorie/macro ledger as default.
- Do not store state only in chat memory.
- Do not normalize manual giant packets as routine UX.
- Do not route to R1 until parent Goal completion evidence exists.
- Do not mutate repository without approved repository_patch and read-back.

## Acceptance tests to preserve

- `first_week_bootstrap_from_empty_state`
- `later_week_bootstrap_from_saved_state`
- `fresh_menu_chat_from_saved_plan`
- `fresh_tracking_chat_from_saved_plan_and_menu`
- `week_review_from_saved_report`
- `project_files_refresh_reproducibility`

## Stop conditions

Stop or route to B1/S3/Context Request if:

- no concrete state/protocol file target can be defined;
- Project Files refresh cannot be made reproducible;
- solution requires hidden chat memory;
- user burden becomes higher than the low-friction constraint allows;
- existing files contradict the repaired Goal Contract;
- E1 would need to decide a new strategic direction rather than plan execution.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/01_GOAL_WORKING_CONTEXT.md`
