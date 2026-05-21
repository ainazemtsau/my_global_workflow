# AGENTS.md - Project `Питание` Codex local operator

Status: active

## Scope

These instructions apply only to:

```text
directions/health-and-beauty/projects/nutrition/**
```

This file is not a Direction-wide instruction file.

Do not apply these rules to:

```text
workflow/**
directions/health-and-beauty/project_files/**
directions/health-and-beauty/phases/**
directions/health-and-beauty/project_setup/**
directions/* except directions/health-and-beauty/projects/nutrition/**
```

unless the user explicitly asks for workflow or Direction lifecycle repository maintenance.

## Role

Codex is the local repository operator for ChatGPT Project `Питание`.

Codex may perform two normal nutrition-project roles:

- Nutrition state save operation: apply approved save packets from ChatGPT Project `Питание` to durable markdown/YAML/JSON state.
- Nutrition project change operation: repair or change the project's local instructions, protocols, state schema, research artifacts, launchers, acceptance tests, recipe metadata, or Codex-local docs so the ChatGPT Project behaves differently.

Codex must not default to giving the user another ChatGPT prompt when the user asks to change the project. If a repository change is the right fix, make the repository change.

## Required local docs

Before any non-trivial change request, read:

```text
codex/PROJECT_MAP.md
codex/CHANGE_REQUEST_PROCESS.md
codex/VALIDATION_AND_RETURN_CONTRACT.md
```

If any of these files are missing, recreate them from the intended structure in this AGENTS.md setup or report STUCK.

## Preflight

Before editing:

```text
git fetch origin
git checkout codex/direction-health-and-beauty
git rebase origin/main
git status --short
```

If the worktree is dirty before edits, classify the dirty files:

- if they are clearly part of the current requested nutrition change, continue carefully;
- if unrelated, report STUCK before overwriting anything.

## Request classification

When the user writes a normal request, classify it first:

```text
state_save
profile_or_preference_update
current_week_menu_update
weekly_planning_update
tracking_or_review_update
global_strategy_research_update
recipe_or_mealie_sync_update
project_behavior_change
project_protocol_bug
chatgpt_project_refresh_help
codex_operator_docs_update
unclear_or_unsafe
```

Then act according to `codex/CHANGE_REQUEST_PROCESS.md`.

## Core rule

If the user says something like:

```text
"это не работает"
"чат делает хуйню"
"надо поменять поведение"
"добавь механизм"
"сделай чтобы он сохранял preferences"
"Menu Chat должен..."
"Weekly Planner должен..."
"Global Strategy должен..."
```

then Codex should normally update repository files under the nutrition project, not only produce a prompt.

Prompt-only output is allowed only when:

- the user explicitly asks for a prompt;
- the requested change does not belong in repository files;
- the repository change is blocked and a temporary workaround prompt is the safest fallback.

## Allowed normal change targets

Project behavior / protocol changes:

```text
CHATGPT_PROJECT_INSTRUCTIONS.md
project_files/00_NUTRITION_START_HERE.md
project_files/01_GLOBAL_STRATEGY_CHAT_PROTOCOL.md
project_files/02_WEEKLY_PLANNING_CHAT_PROTOCOL.md
project_files/03_MENU_CHAT_PROTOCOL.md
project_files/04_TRACKING_CHAT_PROTOCOL.md
project_files/05_STATE_SAVE_AND_REFRESH_PROTOCOL.md
project_files/06_CHAT_LAUNCHERS_AND_OUTPUT_FORMATS.md
project_files/07_REAL_START_ACCEPTANCE_TESTS.md
```

Durable nutrition state:

```text
state/GLOBAL_NUTRITION_PLAN.md
state/USER_PROFILE_AND_CONSTRAINTS.yml
state/NUTRITION_HISTORY.md
state/PROGRESS_METRICS.md
```

Research artifacts:

```text
research/DEEP_RESEARCH_REQUEST.md
research/DEEP_RESEARCH_RESULT.md
research/DEEP_RESEARCH_SYNTHESIS.md
```

Week state:

```text
weeks/ACTIVE_WEEK_POINTER.md
weeks/current/WEEKLY_PLAN.md
weeks/current/ACTIVE_WEEK_MENU.md
weeks/current/WEEK_TRACKING_REPORT.md
weeks/current/WEEK_REVIEW.md
weeks/current/NEXT_WEEK_INPUTS.md
weeks/current/MEALIE_RECIPE_BUNDLE.json
```

Recipe and Mealie sync state for approved `PITANIE_CODEX_CARD` operations:

```text
recipes/RECIPE_TAXONOMY.yml
recipes/RECIPE_CATALOG_INDEX.md
recipes/catalog/*.json
recipes/bundles/*/MEALIE_RECIPE_BUNDLE.json
```

Codex-local operator docs:

```text
AGENTS.md
codex/PROJECT_MAP.md
codex/CHANGE_REQUEST_PROCESS.md
codex/VALIDATION_AND_RETURN_CONTRACT.md
```

## Forbidden normal targets

Do not modify these during normal nutrition project change requests:

```text
workflow/**
directions/health-and-beauty/project_files/**
directions/health-and-beauty/phases/**
directions/health-and-beauty/project_setup/**
directions/workflow-governance/**
directions/solo-max-productive/**
directions/indie-game-development/**
```

Do not reintroduce old legacy/superseded Project `Питание` files from:

```text
directions/health-and-beauty/project_setup/pitanie/**
```

or old standalone nutrition protocol/state files unless explicitly requested and justified.

## Behavior-change principle

When fixing behavior, update the smallest sufficient protocol surface.

Examples:

- Global Strategy behavior bug: usually update `project_files/01_GLOBAL_STRATEGY_CHAT_PROTOCOL.md`; maybe also update `CHATGPT_PROJECT_INSTRUCTIONS.md`, `00_NUTRITION_START_HERE.md`, `05_STATE_SAVE_AND_REFRESH_PROTOCOL.md`, `06_CHAT_LAUNCHERS_AND_OUTPUT_FORMATS.md`, `07_REAL_START_ACCEPTANCE_TESTS.md`.
- Weekly Planning behavior bug: usually update `project_files/02_WEEKLY_PLANNING_CHAT_PROTOCOL.md`; maybe also update launchers/tests/save protocol.
- Menu Chat behavior bug: usually update `project_files/03_MENU_CHAT_PROTOCOL.md`; if persistent preferences are involved, also update `05_STATE_SAVE_AND_REFRESH_PROTOCOL.md`, `06_CHAT_LAUNCHERS_AND_OUTPUT_FORMATS.md`, and acceptance tests.
- Tracking behavior bug: usually update `project_files/04_TRACKING_CHAT_PROTOCOL.md`; maybe also update save protocol/tests.
- Project refresh or mode-launch UX bug: usually update `06_CHAT_LAUNCHERS_AND_OUTPUT_FORMATS.md`.

## State-save principle

Do not store user preferences or profile facts in protocol files.

Use:

```text
state/USER_PROFILE_AND_CONSTRAINTS.yml
```

for durable personal facts, preferences, dislikes, equipment, schedule, tracking tolerance, constraints, and problem-food rules.

Use:

```text
weeks/current/NEXT_WEEK_INPUTS.md
```

for lessons or constraints that should affect the next week but are not yet durable global preferences.

Use:

```text
weeks/current/ACTIVE_WEEK_MENU.md
```

for current-week menu changes.

Use:

```text
state/GLOBAL_NUTRITION_PLAN.md
```

only for approved global strategy changes.

## Save approval rule

For state save operations:

- do not mark a save packet approved unless the user explicitly approved it;
- do not invent missing health data;
- do not turn risk notes into diagnoses;
- do not claim GitHub was saved until write, read-back, diff verification, commit, and push are done;
- do not claim Mealie sync until Mealie API sync and structured ingredient read-back evidence exists.

## Project-change approval rule

When the user directly asks Codex to change the nutrition project behavior, that is approval to make a scoped repository change under:

```text
directions/health-and-beauty/projects/nutrition/**
```

unless the request is ambiguous, unsafe, or would modify forbidden paths.

If scope is ambiguous, make the smallest safe change and report assumptions.

## Packet routing

If a packet contains `target_files`, use those paths as the primary target list.

If the packet contains `global_nutrition_plan`, update:

```text
state/GLOBAL_NUTRITION_PLAN.md
```

If the packet contains user profile fields such as age, sex, height, weight, constraints, allergies, schedule, equipment, training context, preferences, dislikes, tracking tolerance, or risk notes, update:

```text
state/USER_PROFILE_AND_CONSTRAINTS.yml
```

Treat `state/USER_PROFILE_AND_CONSTRAINTS.md` as legacy compatibility input only, not as the canonical Global Strategy save target.

If the packet contains Deep Research request, result, or synthesis content, update the matching target:

```text
research/DEEP_RESEARCH_REQUEST.md
research/DEEP_RESEARCH_RESULT.md
research/DEEP_RESEARCH_SYNTHESIS.md
```

If the packet contains nutrition history, update:

```text
state/NUTRITION_HISTORY.md
```

If the packet contains progress metrics, update:

```text
state/PROGRESS_METRICS.md
```

If the packet contains weekly planning state, update as appropriate:

```text
weeks/ACTIVE_WEEK_POINTER.md
weeks/current/WEEKLY_PLAN.md
weeks/current/ACTIVE_WEEK_MENU.md
weeks/current/WEEK_TRACKING_REPORT.md
weeks/current/WEEK_REVIEW.md
weeks/current/NEXT_WEEK_INPUTS.md
```

Prefer explicit packet `target_files` over inference.

## Project integration operations

Project `Питание` may hand Codex one compact `PITANIE_CODEX_CARD` for persistent preferences, menu saves, recipe bundle saves, and Mealie sync. The card must include an `operation` field and all content needed by Codex. Do not require the user to paste long prompts every week.

Supported operations:

```text
save_preferences
save_menu_recipes_and_mealie_plan
sync_recipes_only
```

### operation: `save_preferences`

Input comes from `PITANIE_CODEX_CARD`.

Target:

```text
state/USER_PROFILE_AND_CONSTRAINTS.yml
```

Rules:

- if no new durable preference data is present, do not write;
- do not invent user facts;
- write only approved preference changes;
- preserve existing YAML style where possible;
- return read-back anchors and ChatGPT Project Files refresh requirement.

### operation: `save_menu_recipes_and_mealie_plan`

Targets may include:

```text
weeks/current/WEEKLY_PLAN.md
weeks/current/ACTIVE_WEEK_MENU.md
weeks/current/MEALIE_RECIPE_BUNDLE.json
weeks/current/NEXT_WEEK_INPUTS.md
recipes/bundles/<week_id>/MEALIE_RECIPE_BUNDLE.json
recipes/catalog/*.json
recipes/RECIPE_CATALOG_INDEX.md
state/USER_PROFILE_AND_CONSTRAINTS.yml
```

Rules:

- update `state/USER_PROFILE_AND_CONSTRAINTS.yml` only when explicitly included;
- validate `PITANIE_CODEX_CARD` and recipe bundle JSON before writing/syncing;
- save `weeks/current/ACTIVE_WEEK_MENU.md`;
- save `weeks/current/MEALIE_RECIPE_BUNDLE.json`;
- save `recipes/bundles/<week_id>/MEALIE_RECIPE_BUNDLE.json`;
- save each new or changed recipe as an individual JSON file under `recipes/catalog/`;
- update metadata-only `recipes/RECIPE_CATALOG_INDEX.md`;
- use project-local API tool `integrations/mealie/mealie_api_sync.py`, not generic Mealie MCP, for Mealie writes;
- require `structured_ingredients_ru` before recipe sync;
- ensure categories/tags through the Mealie API when present in the bundle;
- upsert only recipes listed in `recipes_to_upsert`;
- do not resend full bodies for `existing_recipes_to_reuse` unless the bundle explicitly requests a resync;
- create or update meal planner entries from `meal_plan_entries` after recipes exist in Mealie;
- run `python integrations/mealie/mealie_api_sync.py validate --bundle weeks/current/MEALIE_RECIPE_BUNDLE.json` after sync;
- if existing meal plan entries would be duplicated and cannot be safely updated, report `STUCK_MEAL_PLAN_DUPLICATE_RISK` before writing duplicates;
- if GitHub save succeeds but Mealie API sync fails, report `PENDING_MEALIE_SYNC` in blockers/warnings and do not claim full sync.

### operation: `sync_recipes_only`

Use an existing GitHub recipe bundle path from the card.

Rules:

- do not modify menu files unless explicitly requested;
- do not modify preferences unless explicitly requested;
- validate the existing bundle JSON before syncing;
- sync recipe upserts and meal planner entries if present through `integrations/mealie/mealie_api_sync.py`;
- do not use generic Mealie MCP for writes;
- report duplicate conflicts without creating uncontrolled duplicates.

## Mealie recipe sync

Project-local Mealie write path:

```text
integrations/mealie/mealie_api_sync.py
```

Project-local generic MCP config:

```text
.codex/config.toml
```

The generic `mcp_servers.mealie` entry must remain disabled for Project `Питание` writes:

```text
enabled = false
```

Mealie API credentials must be supplied only through environment variables or local uncommitted Codex config values:

```text
MEALIE_BASE_URL
MEALIE_API_TOKEN
MEALIE_API_KEY
```

Do not store Mealie tokens, bearer headers, cookies, copied credentials, or `.env` files in GitHub.

The generic Mealie MCP may be used only for non-authoritative read-only inspection. It must not be used to create or update recipes or meal planner entries because it can collapse ingredients into note/display strings instead of native amount/unit/food fields.

A custom project-local Mealie MCP wrapper is allowed only if the user explicitly requests it and it delegates to the API sync contract in `integrations/mealie/mealie_api_sync.py` or preserves the same structured ingredient read-back validation.

GitHub remains the durable recipe source. Mealie is the operational recipe and meal planner app. Full recipe JSON files live under `recipes/catalog/*.json` and must not be uploaded to ChatGPT Project Files by default.

## Apply rules

Read target files before editing.
Preserve existing markdown/YAML/JSON style where possible.
Do not save the packet wrapper itself unless an existing file explicitly uses that pattern.
Do not invent missing health data.
Do not turn risk notes into diagnoses.
Do not generate live diet/menu/training content while saving state.
Do not generate generic nutrition advice when the task is protocol repair.
Do not claim external writes unless files were actually changed, read back, committed, pushed, and synced where applicable.
If the packet conflicts with existing state or target files are unclear, report STUCK.

## Validation

After every mutation, follow:

```text
codex/VALIDATION_AND_RETURN_CONTRACT.md
```

Minimum checks:

```text
git diff --stat
changed files list
forbidden-path check
read-back anchors from changed files
no workflow files changed
no Direction project_files changed
no sibling Direction files changed
no legacy Project Питание files reintroduced
Project Files refresh list for ChatGPT Project Питание
```

For Global Strategy saves, also confirm that profile, research request, research result, research synthesis, and final plan stayed separated.

For `save_menu_recipes_and_mealie_plan` and `sync_recipes_only`, also confirm:

```text
recipe bundle JSON validated
recipes/catalog/*.json updated only from approved recipe data
recipes/RECIPE_CATALOG_INDEX.md remains metadata-only
Mealie API sync summary returned by `integrations/mealie/mealie_api_sync.py`
Mealie structured ingredient read-back shows quantity/unit/food populated
Mealie meal planner API read-back confirms meal_plan_entries when present
project-local generic `mcp_servers.mealie` remains disabled for writes
```

## Commit messages

Use one of:

```text
update nutrition project codex operator
repair nutrition global strategy protocol
repair nutrition weekly planning protocol
repair nutrition menu protocol
repair nutrition tracking protocol
save nutrition global strategy state
save nutrition user profile preferences
save nutrition weekly plan state
save nutrition active week menu
save nutrition tracking state
save nutrition project state
```

If multiple behavior areas changed, use:

```text
repair nutrition project behavior
```

## Project Files refresh rule

A GitHub commit does not update ChatGPT Project Files.

If any file under:

```text
CHATGPT_PROJECT_INSTRUCTIONS.md
project_files/*.md
state/**
research/**
weeks/**
recipes/RECIPE_TAXONOMY.yml
recipes/RECIPE_CATALOG_INDEX.md
```

changed, report the exact file names that must be manually refreshed in ChatGPT Project `Питание`.

Do not tell the user to upload:

```text
AGENTS.md
codex/*.md
recipes/catalog/*.json
recipes/bundles/*/MEALIE_RECIPE_BUNDLE.json
weeks/current/MEALIE_RECIPE_BUNDLE.json
```

unless explicitly requested.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/AGENTS.md
