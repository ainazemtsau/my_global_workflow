# Current Nutrition Plan

```yaml
nutrition_state_file:
  schema: nutrition_state_file.v1
  project: "Питание"
  file: CURRENT_NUTRITION_PLAN.md
  status: active_template
  purpose: current_non_clinical_plan_anchor_for_menu_tracking_and_review
  canonical_state: true
```

## Purpose

This file stores the current non-clinical nutrition operating plan. It anchors weekly menu generation, low-friction tracking, and review without relying on chat memory.

It is not a live diet prescription and does not require exact calories or macros by default.

## Current Plan State

```yaml
current_nutrition_plan:
  schema: current_nutrition_plan.v1
  plan_status: none
  plan_id: null
  last_updated_at: null
  basis_files:
    baseline: USER_NUTRITION_BASELINE.md
    review_next_week: REVIEW_AND_NEXT_WEEK.md
  plan_period:
    default_cycle_days: 7
    current_cycle_start: null
    current_cycle_end: null
  operating_goal:
    user_goal_summary: pending_user_confirmation
    non_clinical_scope: true
    clinical_management_scope: false
  meal_structure:
    breakfast: defaulted_or_pending
    lunch: defaulted_or_pending
    dinner: defaulted_or_pending
    snacks: optional
  plan_principles:
    low_friction: true
    repeatable_defaults: true
    fallback_meals_required: true
    replacement_rules_preferred: true
    exact_grams_required: false
    calorie_macro_ledger_required_by_default: false
  known_defaults:
    breakfast_defaults: []
    lunch_defaults: []
    dinner_defaults: []
    snack_defaults: []
    fallback_meals: []
  pending_plan_questions:
    blocking: []
    useful_later: []
```

## Use In Fresh Chats

If `plan_status` is `none`, create the smallest useful first-week plan from baseline/defaults and emit a proposed state update packet.

If `plan_status` is saved, resume from the saved plan and build menus, event corrections, or reviews from it. Do not rebuild from memory.

## Durable Update Triggers

Update this file when the user approves a new plan, material plan adjustment, stable meal default, fallback rule, or review-driven next-week delta.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/state/CURRENT_NUTRITION_PLAN.md`
