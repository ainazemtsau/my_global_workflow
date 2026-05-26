# Mealie API Sync

Status: active

Purpose: project-local write path for syncing Project `Питание` recipe bundles to Mealie without losing structured ingredient fields.

## Tool

```text
integrations/mealie/mealie_api_sync.py
```

Use this tool for all Mealie writes from nutrition recipe bundles.

Do not use the generic Mealie MCP server for recipe or meal planner writes. The MCP path is disabled because it can import ingredients as one display/note string instead of native Mealie fields.

## Credentials

Supply credentials outside GitHub:

```text
MEALIE_BASE_URL
MEALIE_API_TOKEN
```

`MEALIE_API_KEY` is also accepted for compatibility.

Do not commit tokens, bearer headers, cookies, copied request headers, `.env` files, or screenshots with secrets.

## Commands

Validate the local bundle shape only:

```powershell
python integrations/mealie/mealie_api_sync.py check-bundle --bundle weeks/current/MEALIE_RECIPE_BUNDLE.json
```

Check that the target Mealie API exposes native structured ingredient fields:

```powershell
python integrations/mealie/mealie_api_sync.py inspect-schema --bundle weeks/current/MEALIE_RECIPE_BUNDLE.json
```

Preview recipe and meal planner writes without mutating Mealie:

```powershell
python integrations/mealie/mealie_api_sync.py sync --dry-run --sync-mealplans --bundle weeks/current/MEALIE_RECIPE_BUNDLE.json
```

Write recipes and meal planner entries:

```powershell
python integrations/mealie/mealie_api_sync.py sync --sync-mealplans --bundle weeks/current/MEALIE_RECIPE_BUNDLE.json
```

Read back and validate current Mealie state:

```powershell
python integrations/mealie/mealie_api_sync.py validate --bundle weeks/current/MEALIE_RECIPE_BUNDLE.json
```

## Required Bundle Contract

Each `recipes_to_upsert` item must include:

```text
recipe_id
name
mealie_slug
ingredients_structured
instructions
extras.pitanie_recipe_id
```

Each `ingredients_structured` row must include:

```text
amount
unit
food
note
```

`amount` may be null only for true free-text quantities such as `по вкусу`.

## Native Mealie Ingredient Mapping

The script writes every ingredient row to Mealie as:

```text
recipeIngredient.quantity <- amount
recipeIngredient.unit     <- Unit entity found/created from unit_ru
recipeIngredient.food     <- Food entity found/created from food_ru
recipeIngredient.note     <- prep_note_ru only
recipeIngredient.display  <- rendered Russian ingredient line
recipeIngredient.originalText <- rendered Russian ingredient line
```

The validation command fails if normal ingredients are note-only or if measurable ingredients lack amount/unit/food read-back fields.

For scheduled recipes, `food` must be a grocery product, not a prepared component. Names such as `готовая курица`, `заготовка`, `картофельные дольки`, `чесночно-йогуртовый соус`, `prepared`, or `potato wedges` are rejected before sync.

Preview grocery rows aggregated from scheduled planner recipes:

```powershell
python integrations/mealie/mealie_api_sync.py shopping-preview --bundle weeks/current/MEALIE_RECIPE_BUNDLE.json
```

## Meal Planner Mapping

When `--sync-mealplans` is used, the script reads existing entries for the bundle date range and updates existing date + meal type slots. It creates a new slot only when no matching slot exists.

If more than one entry exists for the same date + meal type, the script stops with duplicate-risk evidence instead of creating another duplicate.

## Failure States

- `NEEDS_ENV`: Mealie URL or API token is missing.
- `PENDING_MEALIE_SYNC`: GitHub save succeeded but this API sync did not finish.
- `STUCK_MEAL_PLAN_DUPLICATE_RISK`: duplicate planner slots exist and cannot be safely collapsed automatically.
- `STUCK`: Mealie API schema or read-back validation does not preserve native structured ingredients.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/integrations/mealie/MEALIE_API_SYNC.md
