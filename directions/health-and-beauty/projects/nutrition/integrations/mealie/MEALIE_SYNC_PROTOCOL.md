# Mealie Sync Protocol

Status: active

Purpose: define durable GitHub recipe storage and operational Mealie sync for Project `Питание`.

## Authority

```yaml
github: durable_recipe_source
mealie: operational_recipe_app
chatgpt_project: bundle_and_codex_card_author
codex: github_save_and_mealie_api_sync_executor
```

GitHub is the durable source for approved recipe bundles and catalog JSON files.

Mealie is the operational recipe app for searching, cooking, and meal planning. Mealie state is not the durable planning source.

ChatGPT Project `Питание` creates approved menu content, recipe details, `MEALIE_RECIPE_BUNDLE.json`, and one compact `PITANIE_CODEX_CARD`. It must not claim GitHub or Mealie was updated.

Codex saves approved files to GitHub and syncs recipes and meal planner entries to Mealie through the project-local API tool:

```text
integrations/mealie/mealie_api_sync.py
```

The generic Mealie MCP server is disabled for Project `Питание` writes because it does not reliably preserve native ingredient amount/unit/food fields.

## Secrets

Mealie credentials are supplied only outside GitHub:

```text
MEALIE_BASE_URL
MEALIE_API_TOKEN
MEALIE_API_KEY
```

Repository files must not contain API tokens, bearer headers, copied cookies, `.env` files, or personal Mealie credentials.

## Recipe Identity

Primary durable recipe identity:

```text
extras.pitanie_recipe_id
```

The API sync tool also writes this identity into Mealie `extras` and the recipe description marker for read-back and duplicate control.

Fallback duplicate check:

```text
exact recipe name + intended mealie_slug + chatgpt-pitanie tag + week tag
```

If duplicate identity is ambiguous, Codex must report a conflict and must not create an uncontrolled duplicate.

## Structured Ingredient Requirement

Recipe bundles intended for Mealie sync must include `structured_ingredients_ru` for every recipe.

Codex must not stop after importing ingredients as plain text, a single display string, or note-only rows. Mealie read-back must show normal ingredients populated as native fields:

```text
quantity
unit.name
food.name
note only for prep detail
```

## Failure Handling

If GitHub save succeeds but Mealie sync fails:

```text
Status: PENDING_MEALIE_SYNC
```

If required Mealie API environment is unavailable:

```text
Status: NEEDS_ENV
```

If native structured ingredient read-back fails:

```text
Status: STUCK
Reason: STRUCTURED_INGREDIENT_READBACK_FAILED
```

If a duplicate conflict is detected:

```text
Status: STUCK
Reason: DUPLICATE_CONFLICT
```

If existing meal plan entries would be duplicated and cannot be safely updated before creating new entries:

```text
Status: STUCK_MEAL_PLAN_DUPLICATE_RISK
```

The return must include the exact bundle path, the failed tool or endpoint, and the recommended next action.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/integrations/mealie/MEALIE_SYNC_PROTOCOL.md
