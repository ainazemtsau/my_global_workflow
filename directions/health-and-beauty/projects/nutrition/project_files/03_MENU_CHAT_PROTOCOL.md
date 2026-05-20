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

## Forbidden Outputs

Menu Chat must not:

- rebuild global strategy;
- review the week;
- create `WEEK_TRACKING_REPORT`;
- change `GLOBAL_NUTRITION_PLAN`;
- act as a permanent menu chat across multiple weeks.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/03_MENU_CHAT_PROTOCOL.md
