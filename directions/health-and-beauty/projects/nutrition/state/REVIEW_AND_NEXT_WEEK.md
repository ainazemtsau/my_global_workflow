# Review And Next Week

```yaml
nutrition_state_file:
  schema: nutrition_state_file.v1
  project: "Питание"
  file: REVIEW_AND_NEXT_WEEK.md
  status: active_template
  purpose: weekly_review_decisions_next_week_inputs_and_refresh_status
  canonical_state: true
```

## Purpose

This file stores the latest review, next-week inputs, and refresh status for Project `Питание`.

It lets a fresh review or planning chat continue from saved report state without hidden memory.

## Review And Next Week State

```yaml
review_and_next_week:
  schema: review_and_next_week.v1
  review_status: none
  review_period:
    week_id: null
    start: null
    end: null
  basis_files:
    current_plan: CURRENT_NUTRITION_PLAN.md
    active_week_menu: ACTIVE_WEEK_MENU.md
    tracking_report: WEEK_TRACKING_REPORT.md
  latest_review:
    keep: []
    change: []
    remove_or_reduce: []
    what_worked: []
    friction_points: []
    discovered_preferences: []
  next_week_inputs:
    plan_delta: []
    menu_delta: []
    prep_storage_delta: []
    fallback_delta: []
    pending_questions:
      blocking: []
      useful_later: []
  save_and_refresh:
    latest_update_packet_status: none
    latest_codex_save_evidence: none
    project_files_refresh_required: false
    project_files_refresh_last_done_at: null
```

## Week Review Rule

Use `WEEK_TRACKING_REPORT.md` as the durable report input. Produce a readable review first, then keep/change/remove, next-week inputs, and a proposed state update packet when durable state should change.

Do not claim that repository files or Project Files were refreshed unless the user provides save and read-back evidence.

## Durable Update Triggers

Update this file when a weekly review is completed, next-week inputs are approved, save evidence is returned, or Project Files refresh status changes.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/state/REVIEW_AND_NEXT_WEEK.md`
