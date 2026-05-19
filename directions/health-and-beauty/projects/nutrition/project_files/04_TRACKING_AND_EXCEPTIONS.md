# 04 Tracking And Exceptions

```yaml
nutrition_project_file:
  schema: nutrition_project_file.v1
  project: "Питание"
  file: 04_TRACKING_AND_EXCEPTIONS.md
  status: active
  purpose: low_friction_event_intake_and_exception_handling
```

## Tracking Policy

Tracking is exception-first and low-friction. The default is not a calorie/macro ledger.

Accept rough inputs:

- text;
- photo description;
- voice transcript;
- rough portions;
- exact grams if voluntarily provided;
- "I overate" or "off-menu" summaries.

## Event Template

```yaml
meal_event:
  schema: meal_event.v1
  event_id: null
  date: null
  cycle_day: unknown
  input_mode: text_or_photo_or_voice_or_mixed
  event_type: planned_meal | off_menu_meal | snack | overeating | skipped_meal | review_note
  user_reported:
    raw_summary:
    exact_values_supplied: []
    ambiguous_items: []
  ai_estimate:
    rough_category:
    rough_portion:
    likely_deviation_from_cycle:
    confidence: low | medium | high
    confidence_reason:
  correction:
    next_action:
    remaining_day_adjustment:
    tomorrow_adjustment_if_needed:
    no_punishment_rule: true
  questions:
    optional_single_question:
    pending_if_unanswered: true
    continue_if_unanswered:
      assumption:
      confidence_impact:
  state_update_needed:
    update_active_cycle: false
    update_preferences: false
    update_base_snapshot: false
    add_to_review: false
```

## Missing-Answer Defaults

If the user does not answer an optional question:

- continue;
- mark the missing answer as defaulted;
- keep confidence lower;
- do not repeat the same question immediately;
- preserve the question for later only if useful.

## Exception Correction

For off-menu eating or overeating:

- do not moralize;
- do not prescribe compensatory restriction;
- return to the planned next meal when possible;
- simplify the remaining day if needed;
- add the event to review if it reveals a pattern;
- update preferences only when the pattern is stable.

## Durable Update Triggers

Update this file when:

- an event should be remembered for day/week review;
- an exception reveals a stable pattern;
- a correction rule is added;
- a pending question should be preserved.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/04_TRACKING_AND_EXCEPTIONS.md`
