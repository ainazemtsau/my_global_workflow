# Nutrition Project Change Request Process

Status: active
Scope: Codex local operation inside `directions/health-and-beauty/projects/nutrition/**`

## Goal

When the user opens this project in Codex and writes a normal request, Codex should perform the smallest safe repository change that makes ChatGPT Project `Питание` behave correctly.

The user should not need to paste long wrapper prompts.

## Step 1 - Classify request

Classify the user request into one or more categories:

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

## Step 2 - Decide whether to mutate repository

Repository mutation is appropriate when the user wants:

- changed behavior;
- changed protocol;
- durable saved preferences;
- durable state update;
- fixed menu/week/tracking output;
- updated recipe/Mealie handoff;
- updated launchers;
- updated acceptance checks;
- local Codex operation improvement.

Do not mutate repository when:

- the user only asks a conceptual question;
- the user asks for a temporary chat prompt;
- the target is unclear enough that a wrong edit is likely;
- the request would require forbidden paths;
- medical/safety facts are missing and the change would create unsafe advice.

When in doubt, make a minimal safe change or report STUCK with exact missing input. Do not overbuild.

## Step 3 - Read required files

Always read:

```text
AGENTS.md
codex/PROJECT_MAP.md
relevant protocol/state files for the request
```

For behavior changes, read:

```text
CHATGPT_PROJECT_INSTRUCTIONS.md
project_files/00_NUTRITION_START_HERE.md
the affected mode protocol
project_files/05_STATE_SAVE_AND_REFRESH_PROTOCOL.md
project_files/06_CHAT_LAUNCHERS_AND_OUTPUT_FORMATS.md
project_files/07_REAL_START_ACCEPTANCE_TESTS.md
```

For preference/profile changes, read:

```text
state/USER_PROFILE_AND_CONSTRAINTS.yml
project_files/05_STATE_SAVE_AND_REFRESH_PROTOCOL.md
current week files if the request also affects current or next week
```

For current week changes, read:

```text
weeks/current/WEEKLY_PLAN.md
weeks/current/ACTIVE_WEEK_MENU.md
weeks/current/NEXT_WEEK_INPUTS.md
state/USER_PROFILE_AND_CONSTRAINTS.yml
```

For recipe or Mealie sync changes, read:

```text
project_files/03_MENU_CHAT_PROTOCOL.md
project_files/05_STATE_SAVE_AND_REFRESH_PROTOCOL.md
recipes/RECIPE_CATALOG_INDEX.md
recipes/RECIPE_TAXONOMY.yml
relevant recipe bundle or catalog JSON files
```

## Step 4 - Apply smallest sufficient edit

Prefer targeted edits over broad rewrites.

### Project behavior changes

Update the relevant protocol so future ChatGPT Project chats behave differently.

Also update launchers and tests if the user-facing start prompt or pass/fail behavior changes.

Do not only add another workaround prompt unless the user requested a prompt-only workaround.

### Preference/profile changes

Write durable preferences to:

```text
state/USER_PROFILE_AND_CONSTRAINTS.yml
```

Examples:

- dislikes;
- liked foods;
- dietary exclusions;
- meal timing preferences;
- cooking time limits;
- preferred equipment;
- problem foods;
- tracking tolerance;
- budget/availability;
- recurring schedule constraints.

Do not write durable preferences only into `ACTIVE_WEEK_MENU.md`.

### Current week menu changes

Write current-week concrete changes to:

```text
weeks/current/ACTIVE_WEEK_MENU.md
```

If the change teaches something durable, also update:

```text
state/USER_PROFILE_AND_CONSTRAINTS.yml
```

If the change should influence next week but is not yet durable, update:

```text
weeks/current/NEXT_WEEK_INPUTS.md
```

### Recipe and Mealie sync changes

Use `PITANIE_CODEX_CARD` data as the source for approved recipe writes and syncs.

Allowed durable targets include:

```text
weeks/current/MEALIE_RECIPE_BUNDLE.json
recipes/bundles/*/MEALIE_RECIPE_BUNDLE.json
recipes/catalog/*.json
recipes/RECIPE_CATALOG_INDEX.md
recipes/RECIPE_TAXONOMY.yml
```

Do not upload full recipe bodies to ChatGPT Project Files by default.

Do not store Mealie credentials in GitHub.

### Global strategy/research changes

Keep artifacts separate:

```text
profile facts -> state/USER_PROFILE_AND_CONSTRAINTS.yml
research request -> research/DEEP_RESEARCH_REQUEST.md
research result -> research/DEEP_RESEARCH_RESULT.md
research synthesis -> research/DEEP_RESEARCH_SYNTHESIS.md
final approved global plan -> state/GLOBAL_NUTRITION_PLAN.md
```

Do not collapse them into one generic YAML blob.

## Step 5 - Keep ChatGPT Project refresh practical

After changing files, tell the user exactly which files to refresh in ChatGPT Project `Питание`.

Use two lists:

Must refresh now:

- changed Project Instructions / Project Files / state files required for the next intended use.

Do not upload:

- `AGENTS.md`
- `codex/*.md`
- full recipe JSON bodies unless explicitly requested

## Step 6 - Avoid common failures

Do not:

- touch `workflow/**`;
- touch `directions/health-and-beauty/project_files/**`;
- touch sibling Directions;
- use old `project_setup/pitanie/**`;
- reintroduce legacy standalone nutrition files;
- claim ChatGPT Project Files are refreshed after a GitHub commit;
- generate a live diet/menu when the task is protocol repair;
- write generic best-practice advice into durable plan files;
- save medical diagnoses from risk notes;
- invent missing personal/medical facts;
- store Mealie credentials in GitHub.

## Step 7 - Commit and return

After validation:

- commit;
- push;
- report changed files;
- report refresh list;
- report how the user should test the change with a short Project `Питание` chat start if needed.
