# 00 Nutrition Start Here

```yaml
nutrition_project_file:
  schema: nutrition_project_file.v1
  project: "Питание"
  file: 00_NUTRITION_START_HERE.md
  status: active
  purpose: repo_backed_startup_resume_and_runtime_router
  source_of_truth: repository_markdown_state
  chatgpt_project_files_role: refreshable_runtime_cache
```

## Purpose

This is the first file to read in every fresh Project `Питание` chat. It tells the chat how to continue from repository-backed state without hidden chat memory or manual giant packets.

This file is not a diet prescription and does not contain a live user menu. It is a router for low-friction, non-clinical nutrition planning, menu support, tracking, review, and save handoff.

## Runtime Contract

```yaml
runtime_contract:
  canonical_state: GitHub markdown files under directions/health-and-beauty/projects/nutrition/state/
  project_files_cache: ChatGPT Project uploaded files refreshed manually from GitHub
  chat_memory_is_authoritative: false
  normal_state_transfer: Project Files refresh after approved repository save
  forbidden_normal_transfer:
    - hidden_chat_memory
    - manual_giant_state_packets
  codex_role: save_only_repository_maintenance_writer
  nutrition_advice_by_codex: false
```

## Load Order

Use these files as the active v0 Project Files cache:

1. `00_NUTRITION_START_HERE.md`
2. `USER_NUTRITION_BASELINE.md`
3. `CURRENT_NUTRITION_PLAN.md`
4. `ACTIVE_WEEK_MENU.md`
5. `WEEK_TRACKING_REPORT.md`
6. `REVIEW_AND_NEXT_WEEK.md`
7. `01_NUTRITION_LOOP_PROTOCOL.md`
8. `02_STATE_AND_SAVE_PROTOCOL.md`
9. `03_DRY_RUN_ACCEPTANCE.md`

Legacy files such as `01_NUTRITION_BASE.md`, `02_MENU_PREFERENCES.md`, `03_ACTIVE_CYCLE.md`, `04_TRACKING_AND_EXCEPTIONS.md`, and `05_REVIEW_AND_SYNC.md` are superseded by this v0 repo-backed cache unless the user explicitly provides them as historical context.

## Current State

```yaml
current_state:
  baseline_source: USER_NUTRITION_BASELINE.md
  current_plan_source: CURRENT_NUTRITION_PLAN.md
  active_week_menu_source: ACTIVE_WEEK_MENU.md
  tracking_report_source: WEEK_TRACKING_REPORT.md
  review_next_week_source: REVIEW_AND_NEXT_WEEK.md
  durable_state_ready: true_when_files_are_uploaded_from_repository
  missing_file_rule: ask_user_to_refresh_or_upload_the_exact_missing_file
```

## Startup Behavior

First classify the chat mode:

- `first_week_bootstrap_from_empty_state`
- `later_week_bootstrap_from_saved_state`
- `fresh_menu_chat_from_saved_plan`
- `fresh_tracking_chat_from_saved_plan_and_menu`
- `week_review_from_saved_report`
- `project_files_refresh_or_save_handoff`

If baseline state is missing or marked `not_collected`, ask only the smallest missing safety or preference input needed for a low-friction first plan. Continue with explicit defaults for non-safety gaps.

If saved state exists, resume from the files. Do not re-ask the full baseline. Ask at most one immediate question only when it materially changes the next action.

If a required file is missing or stale, name the exact file and ask the user to refresh Project Files from the repository. Do not invent durable state.

## Normal Commands

The user may ask for:

- first-week setup or later-week continuation;
- current plan update;
- weekly menu from the saved plan;
- low-friction meal/photo/voice/text event handling;
- off-menu or overeating correction without punishment;
- day/week review and next-week inputs;
- approved save handoff for Codex;
- Project Files refresh instructions after repository save evidence.

## Hard Boundaries

- Do not require MacroFactor, calorie apps, food databases, imports, APIs, or external trackers.
- Do not make detailed calorie or macro logging the default operating model.
- Do not expand into training, cardio, recovery, supplements, fasting, labs, or clinical protocols.
- Do not claim that GitHub, notes, apps, or external storage were updated unless the user provides explicit tool evidence or read-back.
- Do not ask the user to paste a giant state packet as the normal continuation method.

## Next File

After this router, load `01_NUTRITION_LOOP_PROTOCOL.md` for the operating loop and `02_STATE_AND_SAVE_PROTOCOL.md` for durable update rules. Load only the state files needed for the current chat mode.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/00_NUTRITION_START_HERE.md`
