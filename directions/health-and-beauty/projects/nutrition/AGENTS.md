# AGENTS.md - Project `Питание` Codex instructions

Status: active

## Scope

These instructions apply only to the nutrition project:

```text
directions/health-and-beauty/projects/nutrition/**
```

This is not a Direction-wide instruction file.

Do not apply these rules to:

```text
directions/health-and-beauty/project_files/**
directions/health-and-beauty/phases/**
workflow/**
directions/* except directions/health-and-beauty/projects/nutrition/**
```

unless the user explicitly asks for workflow or Direction lifecycle repository maintenance.

## Role

Codex is the save-only repository writer for ChatGPT Project `Питание`.

ChatGPT Project `Питание` may produce save packets such as:

```text
nutrition_state_update_packet
PITANIE_CODEX_CARD
global_nutrition_plan
weekly_plan
active_week_menu
week_tracking_report
week_review
next_week_inputs
```

These packets are proposed durable state updates. They do not save themselves.

Codex must apply approved packets to GitHub files, verify the result, commit, push, and report which ChatGPT Project Files must be refreshed manually.

## Preflight

Before editing:

```text
git fetch origin
git checkout codex/direction-health-and-beauty
git rebase origin/main
git status --short
```

If the worktree is dirty before edits, report STUCK unless the dirty files are clearly part of the current requested save operation.

## Allowed files for normal nutrition save operations

Normal save operations may modify only:

```text
directions/health-and-beauty/projects/nutrition/state/**
directions/health-and-beauty/projects/nutrition/research/**
directions/health-and-beauty/projects/nutrition/weeks/**
```

Do not modify:

```text
workflow/**
directions/health-and-beauty/project_files/**
directions/health-and-beauty/phases/**
directions/health-and-beauty/project_setup/**
directions/* except directions/health-and-beauty/projects/nutrition/**
```

unless explicitly requested.

## Global Strategy targets

Nutrition save operations must understand these Global Strategy targets:

- `state/USER_PROFILE_AND_CONSTRAINTS.yml`
- `research/DEEP_RESEARCH_REQUEST.md`
- `research/DEEP_RESEARCH_RESULT.md`
- `research/DEEP_RESEARCH_SYNTHESIS.md`
- `state/GLOBAL_NUTRITION_PLAN.md`

Do not apply nutrition save packets to the repository root, Direction-level project files, sibling Directions, or `workflow/**`.

Do not save generic nutrition plans.

For Global Strategy saves, validate that profile, research request, research result, research synthesis, and final plan remain separated.

## Packet routing

If a packet contains `target_files`, use those paths as the primary target list.

If the packet contains `global_nutrition_plan`, update:

```text
state/GLOBAL_NUTRITION_PLAN.md
```

If the packet contains user profile fields such as age, sex, height, weight, constraints, allergies, schedule, equipment, training context, or risk notes, update:

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
- use existing MCP server `mealie` from `rldiao/mealie-mcp-server`;
- ensure categories/tags if supported by MCP;
- upsert only recipes listed in `recipes_to_upsert`;
- do not resend full bodies for `existing_recipes_to_reuse`;
- create meal planner entries from `meal_plan_entries` after recipes exist in Mealie;
- use `create_mealplan_bulk` if available;
- if existing meal plan entries would be duplicated and MCP cannot safely update/delete, return `STUCK_MEAL_PLAN_DUPLICATE_RISK` before writing duplicates;
- if GitHub save succeeds but MCP/Mealie sync fails, return `PENDING_MEALIE_SYNC`, not full failure.

### operation: `sync_recipes_only`

Use an existing GitHub recipe bundle path from the card.

Rules:

- do not modify menu files unless explicitly requested;
- do not modify preferences unless explicitly requested;
- validate the existing bundle JSON before syncing;
- sync recipe upserts and meal planner entries if present;
- use existing MCP server `mealie`;
- report duplicate conflicts without creating uncontrolled duplicates.

## Mealie recipe sync

Project-local Codex MCP config:

```text
.codex/config.toml
```

MCP server:

```text
rldiao/mealie-mcp-server
```

External install path:

```text
C:\my_global_workflow_tools\mealie-mcp-server
```

Mealie API keys must be supplied only through:

```text
MEALIE_API_KEY
```

Do not store Mealie tokens, bearer headers, cookies, or copied credentials in GitHub.

Do not create, restore, or use a custom project-local Mealie MCP adapter.

GitHub remains the durable recipe source. Mealie is the operational recipe and meal planner app. Full recipe JSON files live under `recipes/catalog/*.json` and must not be uploaded to ChatGPT Project Files by default.

## Apply rules

Read target files before editing.
Preserve existing markdown/YAML style where possible.
Do not save the packet wrapper itself unless an existing file explicitly uses that pattern.
Do not invent missing health data.
Do not turn risk notes into diagnoses.
Do not generate live diet/menu/training content while saving state.
Do not claim external writes unless files were actually changed, read back, committed, and pushed.
If the packet conflicts with existing state or target files are unclear, report STUCK.

## Validation

After editing, return:

```text
Status: DONE, STUCK, PENDING_MEALIE_SYNC, STUCK_MEALIE_MCP_UNAVAILABLE, or STUCK_MEAL_PLAN_DUPLICATE_RISK

Worktree:
Branch:
Rebase result:
Changed files:
Diff summary:
Read-back anchors:
Forbidden-path check:
Mealie sync summary:
Commit SHA:
Push result:
Main integration:
Project Files refresh required:
  target ChatGPT Project: Питание
  files to refresh:
Blockers/warnings:
```

Required checks:

```text
git diff --stat
changed files list
read-back anchors from every changed file
confirm no workflow/** files changed
confirm no directions/health-and-beauty/project_files/** files changed
confirm no sibling Direction files changed
confirm no superseded Project Питание legacy files were reintroduced
```

For Global Strategy saves, also confirm that profile, research request, research result, research synthesis, and final plan stayed separated.

For `save_menu_recipes_and_mealie_plan` and `sync_recipes_only`, also confirm:

```text
recipe bundle JSON validated
recipes/catalog/*.json updated only from approved recipe data
recipes/RECIPE_CATALOG_INDEX.md remains metadata-only
Mealie recipe sync summary returned by MCP server mealie
Mealie meal planner sync summary returned by MCP server mealie when meal_plan_entries are present
custom project-local Mealie MCP adapter does not exist
```

## Commit messages

Use one of:

```text
save nutrition global strategy state
save nutrition weekly plan state
save nutrition active week menu
save nutrition tracking state
save nutrition project state
```

## Project Files refresh rule

A GitHub commit does not update ChatGPT Project Files.

If any file under:

```text
state/**
research/**
weeks/**
recipes/RECIPE_TAXONOMY.yml
recipes/RECIPE_CATALOG_INDEX.md
```

changed, report the exact file names that must be manually refreshed in ChatGPT Project `Питание`.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/AGENTS.md
