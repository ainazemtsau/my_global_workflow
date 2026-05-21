# Nutrition Project Map for Codex

Status: active
Scope: `directions/health-and-beauty/projects/nutrition/**`

## Project role

This directory contains the repo-backed operating system for ChatGPT Project `Питание`.

GitHub markdown/YAML/JSON files are durable source of truth.
ChatGPT Project Files are manually refreshed runtime cache.
Codex is the repository writer/repair operator.

## Top-level files

### `CHATGPT_PROJECT_INSTRUCTIONS.md`

Main ChatGPT Project Instructions. Update when the overall project behavior, mode routing, authority boundaries, or file model changes.

### `AGENTS.md`

Local Codex instructions. Do not upload to ChatGPT Project unless explicitly requested.

## Protocol files

### `project_files/00_NUTRITION_START_HERE.md`

Project overview, state map, missing-state rules, mode map. Update when file architecture or mode routing changes.

### `project_files/01_GLOBAL_STRATEGY_CHAT_PROTOCOL.md`

Global Strategy Chat. Owns profile capture, Deep Research request/result/synthesis, and final global plan approval.

### `project_files/02_WEEKLY_PLANNING_CHAT_PROTOCOL.md`

Weekly Planning Chat. Owns week planning from global plan, history, metrics, and next-week inputs. Must not create detailed menu unless explicitly routed.

### `project_files/03_MENU_CHAT_PROTOCOL.md`

Menu Chat. Owns concrete weekly menu, shopping list, prep plan, current-week menu edits, recipe handoff, and menu preference handling.

### `project_files/04_TRACKING_CHAT_PROTOCOL.md`

Tracking Chat. Owns daily/weekly tracking, food events, water, exceptions, photos, status, and week tracking report.

### `project_files/05_STATE_SAVE_AND_REFRESH_PROTOCOL.md`

Save packet and refresh rules. Update whenever new durable artifacts, save packet targets, Codex handoff, recipe/Mealie handoff, or Project Files refresh behavior changes.

### `project_files/06_CHAT_LAUNCHERS_AND_OUTPUT_FORMATS.md`

Short launch prompts and expected outputs. Update whenever the user-facing chat start/continuation UX changes.

### `project_files/07_REAL_START_ACCEPTANCE_TESTS.md`

Acceptance checks. Update whenever behavior changes should be testable.

## State files

### `state/USER_PROFILE_AND_CONSTRAINTS.yml`

Canonical structured user profile:

- body metrics;
- goals;
- training/activity;
- schedule/lifestyle;
- appetite/snacking;
- preferences/dislikes;
- exclusions/allergies;
- cooking tolerance;
- equipment;
- tracking tolerance;
- medical/safety unknowns;
- known unknowns.

Use this for durable preferences and facts.

### `state/GLOBAL_NUTRITION_PLAN.md`

Approved global strategy and operating plan. Do not change unless the user approved a strategy change.

### `state/NUTRITION_HISTORY.md`

Durable history of completed weeks, lessons, major decisions, and relevant outcomes.

### `state/PROGRESS_METRICS.md`

Durable metrics and trend summaries.

## Research files

### `research/DEEP_RESEARCH_REQUEST.md`

Approved research request.

### `research/DEEP_RESEARCH_RESULT.md`

Supplied Deep Research result.

### `research/DEEP_RESEARCH_SYNTHESIS.md`

Project synthesis of research result into user-specific conclusions and strategy implications.

## Week files

### `weeks/ACTIVE_WEEK_POINTER.md`

Pointer to active week.

### `weeks/current/WEEKLY_PLAN.md`

Current week plan. Strategic weekly structure, not detailed menu.

### `weeks/current/ACTIVE_WEEK_MENU.md`

Concrete current-week menu, shopping list, prep, substitutions, current-week edits.

### `weeks/current/MEALIE_RECIPE_BUNDLE.json`

Current week approved recipe bundle for GitHub durability and Mealie sync.

### `weeks/current/WEEK_TRACKING_REPORT.md`

Tracking report for current week.

### `weeks/current/WEEK_REVIEW.md`

End-of-week review.

### `weeks/current/NEXT_WEEK_INPUTS.md`

Inputs for next week, including lessons, temporary constraints, menu feedback, unresolved issues.

## Recipe files

### `recipes/RECIPE_TAXONOMY.yml`

Compact recipe taxonomy metadata. May be uploaded to Project Files when needed.

### `recipes/RECIPE_CATALOG_INDEX.md`

Metadata-only recipe catalog index. May be uploaded to Project Files when needed.

### `recipes/catalog/*.json`

Full durable recipe bodies. Do not upload to ChatGPT Project Files by default.

### `recipes/bundles/*/MEALIE_RECIPE_BUNDLE.json`

Week-specific approved recipe bundles. Do not upload to ChatGPT Project Files by default unless explicitly requested.

## Where to make common changes

User says: "I dislike X / don't want X again"

Durable preference:

```text
state/USER_PROFILE_AND_CONSTRAINTS.yml
```

Only this week:

```text
weeks/current/ACTIVE_WEEK_MENU.md
```

Should affect next week but not global profile yet:

```text
weeks/current/NEXT_WEEK_INPUTS.md
```

If Menu Chat failed to ask this distinction:

```text
project_files/03_MENU_CHAT_PROTOCOL.md
project_files/05_STATE_SAVE_AND_REFRESH_PROTOCOL.md
project_files/06_CHAT_LAUNCHERS_AND_OUTPUT_FORMATS.md
project_files/07_REAL_START_ACCEPTANCE_TESTS.md
```

User says: "Global Strategy is generic"

Usually update:

```text
project_files/01_GLOBAL_STRATEGY_CHAT_PROTOCOL.md
CHATGPT_PROJECT_INSTRUCTIONS.md
project_files/05_STATE_SAVE_AND_REFRESH_PROTOCOL.md
project_files/06_CHAT_LAUNCHERS_AND_OUTPUT_FORMATS.md
project_files/07_REAL_START_ACCEPTANCE_TESTS.md
```

User says: "Weekly planner creates wrong week plan"

Usually update:

```text
project_files/02_WEEKLY_PLANNING_CHAT_PROTOCOL.md
project_files/06_CHAT_LAUNCHERS_AND_OUTPUT_FORMATS.md
project_files/07_REAL_START_ACCEPTANCE_TESTS.md
```

User says: "Menu Chat output is wrong"

Usually update:

```text
project_files/03_MENU_CHAT_PROTOCOL.md
weeks/current/ACTIVE_WEEK_MENU.md
state/USER_PROFILE_AND_CONSTRAINTS.yml
weeks/current/NEXT_WEEK_INPUTS.md
```

User says: "Recipe save or Mealie sync is wrong"

Usually update:

```text
project_files/03_MENU_CHAT_PROTOCOL.md
project_files/05_STATE_SAVE_AND_REFRESH_PROTOCOL.md
recipes/RECIPE_CATALOG_INDEX.md
weeks/current/MEALIE_RECIPE_BUNDLE.json
recipes/bundles/*/MEALIE_RECIPE_BUNDLE.json
```

User says: "Tracking Chat is annoying / saves too often / loses questions"

Usually update:

```text
project_files/04_TRACKING_CHAT_PROTOCOL.md
project_files/05_STATE_SAVE_AND_REFRESH_PROTOCOL.md
project_files/07_REAL_START_ACCEPTANCE_TESTS.md
```

User says: "I want easier future changes in Codex"

Update:

```text
AGENTS.md
codex/PROJECT_MAP.md
codex/CHANGE_REQUEST_PROCESS.md
codex/VALIDATION_AND_RETURN_CONTRACT.md
```

## ChatGPT Project refresh rule

If any of these change, report manual refresh required:

```text
CHATGPT_PROJECT_INSTRUCTIONS.md
project_files/*.md
state/*.md
state/*.yml
research/*.md
weeks/ACTIVE_WEEK_POINTER.md
weeks/current/*.md
recipes/RECIPE_TAXONOMY.yml
recipes/RECIPE_CATALOG_INDEX.md
```

Do not tell the user to upload:

```text
AGENTS.md
codex/*.md
recipes/catalog/*.json
recipes/bundles/*/MEALIE_RECIPE_BUNDLE.json
weeks/current/MEALIE_RECIPE_BUNDLE.json
```

unless explicitly requested.
