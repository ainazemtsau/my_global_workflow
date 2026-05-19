# 03 Active Cycle

```yaml
nutrition_project_file:
  schema: nutrition_project_file.v1
  project: "Питание"
  file: 03_ACTIVE_CYCLE.md
  status: active
  purpose: current_cycle_state
```

## Current Cycle

```yaml
active_cycle:
  schema: active_cycle.v1
  status: none
  cycle_id: null
  cycle_length_days: 7
  cycle_dates:
    start: null
    end: null
  current_day: null
  planning_basis:
    known: []
    unknown:
      - baseline
      - menu_preferences
      - cooking_schedule
      - equipment
    defaulted:
      - cycle_length_days: 7
      - planning_style: repeatable_low_friction_defaults
  menu_defaults:
    breakfast: []
    lunch: []
    dinner: []
    snacks: []
  fallback_rules: []
  prep_notes: []
  shopping_notes: []
  active_exceptions: []
  pending_questions: []
```

## Cycle Creation Output

When creating a cycle, provide:

- overview;
- day or meal-slot defaults;
- shopping notes;
- prep notes;
- fallback meals;
- replacement rules;
- unknown/defaulted inputs;
- update packet if the cycle should be saved.

The first cycle may be approximate. It should be easy to revise after real use.

## Cycle Correction Rules

- Do not restart the whole cycle after one off-menu event.
- Correct the next meal or remaining day.
- If the same friction repeats, change the next cycle default.
- If dinner prep is too heavy, simplify dinner defaults before adding complexity.
- If lunches are boring, add variation rules before replacing the whole cycle.

## Durable Update Triggers

Update this file when:

- a cycle is created;
- cycle dates or current day change;
- menu defaults materially change;
- fallback or replacement rules change;
- review creates a next-cycle delta that should be applied.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/03_ACTIVE_CYCLE.md`
