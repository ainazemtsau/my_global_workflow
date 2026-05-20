# User Nutrition Baseline

```yaml
nutrition_state_file:
  schema: nutrition_state_file.v1
  project: "Питание"
  file: USER_NUTRITION_BASELINE.md
  status: active_template
  purpose: baseline_preferences_boundaries_and_low_friction_defaults
  canonical_state: true
```

## Purpose

This file holds the durable user baseline for Project `Питание`. It is not a medical record, not a clinical nutrition prescription, and not a live menu.

Fresh chats use this file to avoid re-asking the full baseline when saved state already exists.

## Baseline State

```yaml
user_nutrition_baseline:
  schema: user_nutrition_baseline.v1
  state_status: not_collected
  last_confirmed_at: null
  source_notes: []
  profile:
    age: unknown
    sex: unknown
    height: unknown
    weight: unknown
    body_objective: pending_user_confirmation
    activity_or_routine_context: unknown
  safety_boundaries:
    allergies_or_intolerances: unknown
    medical_conditions_relevant_to_food: unknown
    medications_relevant_to_food: unknown
    pregnancy_or_eating_disorder_context: unknown
    clinical_guidance_allowed: false
  stable_preferences:
    language_default: ru
    tracking_burden: low
    cycle_length_default_days: 7
    exact_grams_required: false
    calorie_macro_ledger_required_by_default: false
    external_tracker_required: false
    liked_foods: []
    disliked_foods: []
    repeatable_meals: []
    fallback_meals: []
  practical_constraints:
    budget: unknown
    prep_time: unknown
    shopping_cadence: unknown
    cooking_equipment: unknown
    storage_capacity: unknown
    household_portions_ok: true
  pending_questions:
    blocking_safety: []
    useful_later: []
```

## First-Week Bootstrap Rule

If `state_status` is `not_collected`, ask at most one immediate question. Ask safety-relevant information first when needed. For non-safety gaps, proceed with explicit defaults and mark confidence lower.

Do not block a usable first-week loop on optimization details.

## Later-Week Continuation Rule

If this file has saved baseline data, do not ask the full baseline again. Ask only for missing, stale, or materially changed details.

## Durable Update Triggers

Update this file only when the user confirms a durable baseline, boundary, preference, or practical constraint that should affect future weeks.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/state/USER_NUTRITION_BASELINE.md`
