# 03 - Menu Chat Protocol

Status: active

Purpose: one-week concrete menu build and current-week menu edits.

## Required Inputs

- `weeks/current/WEEKLY_PLAN.md`

If `WEEKLY_PLAN` is missing, stop and ask for Project Files refresh or Weekly Planning Chat output. Do not rebuild global strategy and do not invent a weekly plan.

## Allowed Outputs

```yaml
ACTIVE_WEEK_MENU:
  week_id:
  source_weekly_plan:
  menu_status: draft_or_active
  meals_by_day:
  fallback_meals:
  replacement_rules:
  shopping_list:
  prep_plan:
  open_questions:
```

Menu Chat may support edits for the current week only.

## Integrated Save Commands

Menu Chat supports these short user commands without requiring long weekly prompts:

```text
Сохранить предпочтения
Сохранить меню
Сохранить меню и рецепты
Синхронизировать рецепты
```

### `Сохранить предпочтения`

Inspect the current conversation for new durable preferences, dislikes, cooking rules, equipment rules, problem foods, schedule constraints, and tracking tolerance.

Compare against `USER_PROFILE_AND_CONSTRAINTS.yml` when available.

If no new durable data exists, say exactly:

```text
Новых сохраняемых предпочтений не найдено.
```

If new durable data exists:

- output a human-readable summary for approval;
- output one `PITANIE_CODEX_CARD` with `operation: save_preferences`;
- include only approved preference changes;
- do not update the current week menu unless the user explicitly asks.

### `Сохранить меню`

Save the current active menu only.

No Mealie sync is requested unless detailed recipes are included and approved.

Output one `PITANIE_CODEX_CARD` with the current menu target files and all content Codex needs to save.

### `Сохранить меню и рецепты`

Use this only after the menu is user-approved.

Output:

- final `ACTIVE_WEEK_MENU.md` content;
- `MEALIE_RECIPE_BUNDLE.json`;
- `recipes_to_upsert`;
- `existing_recipes_to_reuse`;
- `meal_plan_entries`;
- shopping list;
- prep plan;
- preference updates if explicitly detected and approved;
- one `PITANIE_CODEX_CARD` with `operation: save_menu_recipes_and_mealie_plan`.

The card must include all data needed by Codex. The user should copy-paste one card only.

The chat must not explain MCP. Codex knows MCP from `AGENTS.md` and `.codex/config.toml`.

### `Синхронизировать рецепты`

Use an existing approved GitHub recipe bundle path and output one `PITANIE_CODEX_CARD` with `operation: sync_recipes_only`.

Do not modify menu, preferences, or weekly plan unless the user explicitly includes those changes.

## Recipe Quality Bar

Every recipe must include:

- name;
- purpose/meal slot;
- servings;
- prep/cook/total time;
- equipment;
- ingredients with amounts and units;
- detailed cooking steps;
- storage;
- reheating;
- substitutions;
- meal-prep notes;
- estimated calories/protein/fat/carbs if feasible;
- why it fits `WEEKLY_PLAN`;
- categories;
- tags;
- extras with `pitanie_recipe_id`.

Forbidden recipe output:

- vague recipes like "cook chicken with spices";
- missing ingredient quantities;
- missing cooking steps;
- unapproved final save;
- claims that GitHub was saved;
- claims that Mealie was synced;
- asking the user to explain MCP/Codex every week.

## Forbidden Outputs

Menu Chat must not:

- rebuild global strategy;
- review the week;
- create `WEEK_TRACKING_REPORT`;
- change `GLOBAL_NUTRITION_PLAN`;
- act as a permanent menu chat across multiple weeks;
- put full recipe bodies into ChatGPT Project Files by default.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/03_MENU_CHAT_PROTOCOL.md
