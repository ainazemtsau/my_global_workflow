# Project Files Manifest - Project `Питание`

Status: active clean rebuild

Use this manifest for manual ChatGPT Project setup and refresh.

## Project Instructions

Paste this file into the ChatGPT Project Instructions field:

```text
directions/health-and-beauty/projects/nutrition/CHATGPT_PROJECT_INSTRUCTIONS.md
```

## Upload as Project Files

Protocol/runtime cache:

```text
directions/health-and-beauty/projects/nutrition/project_files/00_NUTRITION_START_HERE.md
directions/health-and-beauty/projects/nutrition/project_files/01_GLOBAL_STRATEGY_CHAT_PROTOCOL.md
directions/health-and-beauty/projects/nutrition/project_files/02_WEEKLY_PLANNING_CHAT_PROTOCOL.md
directions/health-and-beauty/projects/nutrition/project_files/03_MENU_CHAT_PROTOCOL.md
directions/health-and-beauty/projects/nutrition/project_files/04_TRACKING_CHAT_PROTOCOL.md
directions/health-and-beauty/projects/nutrition/project_files/05_STATE_SAVE_AND_REFRESH_PROTOCOL.md
directions/health-and-beauty/projects/nutrition/project_files/06_CHAT_LAUNCHERS_AND_OUTPUT_FORMATS.md
directions/health-and-beauty/projects/nutrition/project_files/07_REAL_START_ACCEPTANCE_TESTS.md
```

Durable state cache copied from GitHub:

```text
directions/health-and-beauty/projects/nutrition/state/USER_PROFILE_AND_CONSTRAINTS.yml
directions/health-and-beauty/projects/nutrition/research/DEEP_RESEARCH_REQUEST.md
directions/health-and-beauty/projects/nutrition/research/DEEP_RESEARCH_RESULT.md
directions/health-and-beauty/projects/nutrition/research/DEEP_RESEARCH_SYNTHESIS.md
directions/health-and-beauty/projects/nutrition/state/GLOBAL_NUTRITION_PLAN.md
directions/health-and-beauty/projects/nutrition/state/NUTRITION_HISTORY.md
directions/health-and-beauty/projects/nutrition/state/PROGRESS_METRICS.md
directions/health-and-beauty/projects/nutrition/weeks/ACTIVE_WEEK_POINTER.md
directions/health-and-beauty/projects/nutrition/weeks/current/WEEKLY_PLAN.md
directions/health-and-beauty/projects/nutrition/weeks/current/ACTIVE_WEEK_MENU.md
directions/health-and-beauty/projects/nutrition/weeks/current/WEEK_TRACKING_REPORT.md
directions/health-and-beauty/projects/nutrition/weeks/current/WEEK_REVIEW.md
directions/health-and-beauty/projects/nutrition/weeks/current/NEXT_WEEK_INPUTS.md
directions/health-and-beauty/projects/nutrition/recipes/RECIPE_TAXONOMY.yml
directions/health-and-beauty/projects/nutrition/recipes/RECIPE_CATALOG_INDEX.md
```

Operator protocols, request-only unless doing save or validation:

```text
directions/health-and-beauty/projects/nutrition/protocols/CODEX_SAVE_OPERATOR.md
directions/health-and-beauty/projects/nutrition/protocols/DRY_RUN_ACCEPTANCE.md
```

## Explicitly Excluded

Do not upload:

```text
directions/health-and-beauty/project_setup/pitanie/**
directions/health-and-beauty/projects/nutrition/state/ACTIVE_WEEK_MENU.md
directions/health-and-beauty/projects/nutrition/state/CURRENT_NUTRITION_PLAN.md
directions/health-and-beauty/projects/nutrition/state/REVIEW_AND_NEXT_WEEK.md
directions/health-and-beauty/projects/nutrition/state/USER_NUTRITION_BASELINE.md
directions/health-and-beauty/projects/nutrition/state/USER_PROFILE_AND_CONSTRAINTS.md
directions/health-and-beauty/projects/nutrition/state/WEEK_TRACKING_REPORT.md
directions/health-and-beauty/projects/nutrition/recipes/catalog/*.json
directions/health-and-beauty/projects/nutrition/recipes/bundles/**
directions/health-and-beauty/projects/nutrition/.codex/config.toml
directions/health-and-beauty/projects/nutrition/integrations/mealie/mealie_mcp_server.py
```

Those files are superseded compatibility stubs if still present. `state/USER_PROFILE_AND_CONSTRAINTS.md` is legacy compatibility input only; the canonical structured profile is `state/USER_PROFILE_AND_CONSTRAINTS.yml`.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/PROJECT_FILES_MANIFEST.md
