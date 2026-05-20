# Active Week Menu

```yaml
nutrition_state_file:
  schema: nutrition_state_file.v1
  project: "Питание"
  file: ACTIVE_WEEK_MENU.md
  status: active_template
  purpose: current_week_menu_shopping_prep_and_fallback_state
  canonical_state: true
```

## Purpose

This file stores the active week menu and practical support notes for Project `Питание`.

It enables a fresh menu chat or tracking chat to continue from saved plan state without requiring hidden memory.

## Active Week Menu State

```yaml
active_week_menu:
  schema: active_week_menu.v1
  menu_status: none
  week_id: null
  last_updated_at: null
  basis_files:
    baseline: USER_NUTRITION_BASELINE.md
    current_plan: CURRENT_NUTRITION_PLAN.md
    review_next_week: REVIEW_AND_NEXT_WEEK.md
  week_dates:
    start: null
    end: null
  menu_slots:
    breakfasts: []
    lunches: []
    dinners: []
    snacks_or_optional_items: []
  replacement_rules:
    protein_or_main_component: []
    vegetable_or_fiber_component: []
    starch_or_grain_component: []
    fats_sauces_or_flavor: []
  fallback_meals: []
  shopping_notes: []
  prep_storage_notes: []
  known_constraints_used: []
  assumptions_defaulted: []
  pending_questions:
    blocking: []
    useful_later: []
```

## Fresh Menu Chat Rule

Build or update the week menu from saved baseline, current plan, and review inputs. If something is unknown, use a low-friction default and mark the assumption.

Do not require a detailed calorie/macro ledger or external food database.

## Fresh Tracking Chat Rule

When handling a meal event, compare against this active week menu when available. If no active menu exists, use the current plan and mark menu comparison as unavailable.

## Durable Update Triggers

Update this file when the active week menu, fallback meal, replacement rule, shopping note, or prep/storage note materially changes.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/state/ACTIVE_WEEK_MENU.md`
