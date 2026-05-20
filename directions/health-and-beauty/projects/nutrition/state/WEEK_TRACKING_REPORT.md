# Week Tracking Report

```yaml
nutrition_state_file:
  schema: nutrition_state_file.v1
  project: "Питание"
  file: WEEK_TRACKING_REPORT.md
  status: active_template
  purpose: low_friction_week_events_exceptions_and_review_inputs
  canonical_state: true
```

## Purpose

This file stores low-friction tracking summaries for the current week. It is exception-first and review-oriented.

It is not a detailed calorie, macro, gram, or food database ledger.

## Tracking Report State

```yaml
week_tracking_report:
  schema: week_tracking_report.v1
  report_status: empty
  week_id: null
  last_updated_at: null
  basis_files:
    current_plan: CURRENT_NUTRITION_PLAN.md
    active_week_menu: ACTIVE_WEEK_MENU.md
  event_summaries:
    planned_meals_completed: []
    off_menu_events: []
    overeating_or_under_eating_events: []
    skipped_or_disrupted_meals: []
    user_notes: []
  pattern_candidates:
    worked_well: []
    friction_points: []
    preference_discoveries: []
    fallback_meal_uses: []
  correction_notes:
    next_meal_or_day_corrections: []
    no_punishment_rule_preserved: true
  confidence_notes:
    low_confidence_events: []
    unresolved_ambiguities: []
  review_ready: false
```

## Event Handling Rule

Accept rough text, photo descriptions, voice-style notes, and user summaries. Label uncertainty. Ask at most one optional question when it materially improves the next action, and continue with explicit assumptions if unanswered.

## Durable Update Triggers

Update this file when an event should be remembered for day/week review, a friction pattern appears, a fallback meal works, or a correction note should inform the next review.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/state/WEEK_TRACKING_REPORT.md`
