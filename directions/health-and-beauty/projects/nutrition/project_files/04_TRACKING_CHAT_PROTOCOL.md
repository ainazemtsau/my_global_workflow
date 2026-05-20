# 04 - Tracking Chat Protocol

Status: active

Purpose: one-week low-friction tracking, adaptation, and end-of-week report.

## Required Inputs

- `weeks/current/WEEKLY_PLAN.md`
- `weeks/current/ACTIVE_WEEK_MENU.md`

If either is missing, stop and ask for Project Files refresh. Do not generate a menu inside Tracking Chat.

## Normal Message Output

For food/photo/water/event messages, answer with:

```yaml
tracking_message_result:
  event_understood:
  estimate_if_needed:
  current_day_status:
  pending_questions:
  advice_for_rest_of_day:
  durable_github_update: false
```

Estimate calories/BJU only when required by `WEEKLY_PLAN` or explicitly requested by the user. Keep pending questions until answered or explicitly declined.

Default durable GitHub update after each tracking message: `false`.

## Full Export Conditions

Create `WEEK_TRACKING_REPORT` only when:

- the user asks to close the week;
- the week ends;
- the user explicitly requests a state export.

## WEEK_TRACKING_REPORT Format

```yaml
WEEK_TRACKING_REPORT:
  week_id:
  source_weekly_plan:
  source_active_week_menu:
  logged_events_summary:
  estimated_intake_if_used:
  water_and_context_notes:
  deviations_and_adaptations:
  pending_questions_unresolved:
  unlogged_or_uncertain_items:
  review_inputs:
```

Tracking Chat must not generate concrete menu, rebuild global strategy, or write GitHub after every message by default.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/04_TRACKING_CHAT_PROTOCOL.md
