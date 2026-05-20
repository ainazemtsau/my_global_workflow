# 01 Nutrition Loop Protocol

```yaml
nutrition_project_file:
  schema: nutrition_project_file.v1
  project: "Питание"
  file: 01_NUTRITION_LOOP_PROTOCOL.md
  status: active
  purpose: multi_chat_low_friction_nutrition_loop
```

## Purpose

This protocol defines how Project `Питание` operates across fresh chats using repository-backed state.

The loop is:

```text
baseline/current plan -> weekly menu -> tracking/adaptation -> review -> save to GitHub -> Project Files refresh -> fresh chat continuation
```

## Roles

```yaml
roles:
  dietitian_plan_builder:
    purpose: create_or_update_non_clinical_current_plan
    primary_state:
      - USER_NUTRITION_BASELINE.md
      - CURRENT_NUTRITION_PLAN.md
  weekly_menu_builder:
    purpose: build_active_week_menu_from_saved_plan
    primary_state:
      - CURRENT_NUTRITION_PLAN.md
      - ACTIVE_WEEK_MENU.md
      - REVIEW_AND_NEXT_WEEK.md
  weekly_tracking_and_adaptation:
    purpose: handle_events_and_exceptions_without_heavy_ledger
    primary_state:
      - CURRENT_NUTRITION_PLAN.md
      - ACTIVE_WEEK_MENU.md
      - WEEK_TRACKING_REPORT.md
  dietitian_review_and_sync:
    purpose: turn_report_into_review_and_next_week_inputs
    primary_state:
      - WEEK_TRACKING_REPORT.md
      - REVIEW_AND_NEXT_WEEK.md
```

## First-Week Bootstrap

When baseline or current plan is empty:

1. Read `USER_NUTRITION_BASELINE.md` and `CURRENT_NUTRITION_PLAN.md`.
2. Ask at most one immediate question, prioritizing safety-relevant food boundaries.
3. Continue with explicit defaults for non-safety gaps.
4. Create a small, low-friction first plan or plan outline.
5. Emit a `nutrition_state_update_packet.v1` if durable state should be saved.

Do not ask for full setup before giving a useful first step.

## Later-Week Bootstrap

When saved baseline and plan exist:

1. Read saved state files.
2. Summarize the current saved plan in human-readable form.
3. Ask only for changed or stale details.
4. Continue with menu, tracking, or review based on the user's requested mode.

Do not re-ask the full baseline.

## Weekly Menu

Build the active week menu from:

- saved baseline and preferences;
- current plan;
- latest review and next-week inputs;
- user constraints supplied in the current chat.

Include fallback meals, replacement rules, shopping notes, and prep/storage notes when useful. Keep the output practical and low-burden.

## Tracking And Adaptation

For a meal, photo, voice-style note, off-menu event, overeating event, skipped meal, or simple daily update:

1. Identify what is known and unknown.
2. Label confidence.
3. Use rough categories when exact amounts are missing.
4. Correct the next meal, remaining day, or next week without punishment.
5. Add a durable tracking note only when useful for review.

Do not require precise calories, macros, grams, food database lookup, or external tracker import by default.

## Week Review

Use `WEEK_TRACKING_REPORT.md` to produce:

- short readable review;
- keep/change/remove list;
- what worked;
- friction points;
- preference discoveries;
- next-week inputs;
- proposed state update packet if durable state should change.

## Missing Data Rule

Ask one focused question only when the answer materially changes the next action. Otherwise continue, mark the assumption, and preserve a pending question if useful.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/01_NUTRITION_LOOP_PROTOCOL.md`
