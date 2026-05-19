# 00 Nutrition Start Here

```yaml
nutrition_project_file:
  schema: nutrition_project_file.v1
  project: "Питание"
  file: 00_NUTRITION_START_HERE.md
  status: active
  purpose: startup_and_resume_pointer
```

## Purpose

This is the first file to read in a fresh Project `Питание` chat. It explains how to start or resume the nutrition loop from durable state.

This file is not a diet prescription and does not contain a live user menu.

## Load Order

1. Read this file.
2. Read `01_NUTRITION_BASE.md` for baseline and boundaries.
3. Read `02_MENU_PREFERENCES.md` for menu preferences and defaults.
4. Read `03_ACTIVE_CYCLE.md` for the current cycle.
5. Read `04_TRACKING_AND_EXCEPTIONS.md` for event intake and exception handling.
6. Read `05_REVIEW_AND_SYNC.md` for day/week review and update packets.

## Current State

```yaml
current_state:
  baseline_status: not_collected
  menu_preferences_status: not_collected
  active_cycle_status: none
  tracking_status: empty
  latest_review_status: none
  durable_state_ready: partial_template_only
```

## Startup Behavior

If baseline and preferences are incomplete, continue with explicit defaults and ask at most one immediate question.

If no active cycle exists, offer a starter cycle plan from known/defaulted inputs and clearly mark what is unknown.

If an active cycle exists, resume it and ask what the user wants to do next only if the next action is unclear.

## Normal Commands

The user may ask for:

- start or restart a cycle;
- update preferences;
- log a meal/photo/voice-style event;
- correct an off-menu or overeating event;
- review today or this week;
- prepare a state update packet;
- prepare a fresh-chat carryover.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/00_NUTRITION_START_HERE.md`
