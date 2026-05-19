# 02 Menu Preferences

```yaml
nutrition_project_file:
  schema: nutrition_project_file.v1
  project: "Питание"
  file: 02_MENU_PREFERENCES.md
  status: active
  purpose: menu_defaults_preferences_and_constraints
```

## Preference Snapshot

```yaml
menu_preferences:
  schema: menu_preferences.v1
  status: template_pending_user_input
  default_cycle_length_days: 7
  meal_structure:
    breakfast: defaulted
    lunch: defaulted
    dinner: defaulted
    snacks: optional
  food_preferences:
    liked_foods: []
    disliked_foods: []
    repeatable_meals: []
    fallback_meals: []
  constraints:
    budget: unknown
    prep_time: unknown
    shopping_cadence: unknown
    cooking_equipment: unknown
    storage_capacity: unknown
  planning_style:
    household_portions_ok: true
    exact_grams_required: false
    calorie_macro_ledger_required: false
    variety_level: medium_defaulted
    batch_prep: pending_user_input
```

## Planning Defaults

When data is missing, use simple repeatable templates:

- stable breakfast default;
- interchangeable lunch templates;
- low-burden dinners;
- one or two fallback meals;
- replacement rules instead of perfect recipes.

Do not assume special equipment or external storage. If equipment is unknown, use generic low-equipment meals and mark equipment-specific upgrades as pending.

## Replacement Rules

Prefer replacement rules over fragile plans:

- protein component can be swapped for a similar practical option;
- fiber/vegetable component can be swapped by availability;
- carbohydrate/fat portions can be adjusted by hunger and routine;
- fallback meal beats skipping or chaotic snacking;
- off-menu eating leads to next-meal correction, not punishment.

## Durable Update Triggers

Update this file when the user confirms:

- stable likes/dislikes;
- repeatable meal defaults;
- cooking equipment;
- shopping/prep cadence;
- fallback meals that actually work;
- variety or prep-burden preference.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/02_MENU_PREFERENCES.md`
