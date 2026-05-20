# 02 - Weekly Planning Chat Protocol

Status: active

Purpose: one-week planning and one-week close. This is not a permanent weekly chat.

## Start-of-Week Inputs

Read when available:

- `state/GLOBAL_NUTRITION_PLAN.md`
- `state/NUTRITION_HISTORY.md`
- `state/PROGRESS_METRICS.md`
- `weeks/ACTIVE_WEEK_POINTER.md`
- `weeks/current/NEXT_WEEK_INPUTS.md`

If `GLOBAL_NUTRITION_PLAN` is missing or still pending profile capture, Deep Research result, research synthesis, or user approval, stop and ask for Global Strategy completion or refresh.

## Start-of-Week Output

Create one `WEEKLY_PLAN`.

```yaml
WEEKLY_PLAN:
  week_id:
  plan_status: draft_for_current_week
  source_files_read:
  week_goal:
  practical_constraints:
  nutrition_targets_if_available:
  meal_structure_guidance:
  menu_chat_inputs:
  tracking_chat_inputs:
  explicit_non_goals:
    - concrete_menu
    - shopping_list
    - prep_plan
```

Weekly Planning must not generate concrete meals, a shopping list, or a prep plan. Those belong to Menu Chat.

## Week Close Inputs

Read:

- `weeks/current/WEEK_TRACKING_REPORT.md`
- `weeks/current/ACTIVE_WEEK_MENU.md` if useful
- `weeks/current/WEEKLY_PLAN.md`

## Week Close Output

Create:

- `weeks/current/WEEK_REVIEW.md`
- `weeks/current/NEXT_WEEK_INPUTS.md`
- proposed updates for `state/NUTRITION_HISTORY.md`
- proposed updates for `state/PROGRESS_METRICS.md`

Week close must report unresolved/unlogged items from `WEEK_TRACKING_REPORT`, save week result/history/progress through a user-approved packet, prepare next week inputs, and close the weekly chat.

It must not start next week in the same chat and must not generate a menu.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/02_WEEKLY_PLANNING_CHAT_PROTOCOL.md
