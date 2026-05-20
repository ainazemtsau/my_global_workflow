# Weekly Plan

Status: draft_for_current_week

Weekly Planning Chat creates this file for one week only.

```yaml
WEEKLY_PLAN:
  schema: weekly_plan.v1
  week_id: "2026-W21-calibration-2026-05-21_to_2026-05-27"
  plan_status: draft_for_current_week
  source_global_plan: state/GLOBAL_NUTRITION_PLAN.md
  source_history: state/NUTRITION_HISTORY.md
  calendar_logic:
    today_2026_05_20: "setup_evening_only_not_counted_as_day_1"
    day_1: "Thursday 2026-05-21"
    day_7: "Wednesday 2026-05-27"
  week_goal:
    - calibration_week_for_current_nutrition_routine
    - start_real_plan_and_tracking_on_2026_05_21
  constraints_this_week:
    - "Wednesday 2026-05-20 is setup evening only: menu planning, shopping, and optionally removing visible sweets/triggers."
    - "Do not count Wednesday 2026-05-20 as Day 1."
    - "No unplanned morning sweets."
  meal_structure_guidance:
    anchor_meals_per_day: 3
    anti_grazing_slots:
      morning: 1
      guidance: "one controlled morning anti-grazing slot"
  nutrition_targets_if_available:
    calories_per_day: "2400-2600 kcal"
    protein_per_day: "~180 g"
  menu_chat_inputs:
    menu_date_range: "2026-05-21_to_2026-05-27"
    build_menu_for_days:
      day_1: "Thursday 2026-05-21"
      day_7: "Wednesday 2026-05-27"
    boundaries:
      - "Menu Chat should build the menu for 2026-05-21 through 2026-05-27."
      - "Menu Chat must not build the menu from 2026-05-20."
      - "Concrete menu, shopping list, and prep plan belong to Menu Chat, not this weekly plan."
  tracking_chat_inputs:
    tracking_start: "Thursday 2026-05-21"
    day_1: "Thursday 2026-05-21"
    day_7: "Wednesday 2026-05-27"
    tracking_days: 7
    tracking_style: low_friction_inputs
  explicit_non_goals:
    - concrete_menu
    - shopping_list
    - prep_plan
```

This file must not contain the concrete menu.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/weeks/current/WEEKLY_PLAN.md
