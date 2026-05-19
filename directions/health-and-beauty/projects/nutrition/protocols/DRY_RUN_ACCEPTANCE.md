# Dry-Run Acceptance - Project Питание v0

These dry-runs use synthetic inputs only. They are not live user diet/menu generation and not clinical nutrition advice.

## Acceptance Rule

A fresh Project `Питание` chat passes v0 acceptance when it can complete all three dry-runs from the Project Instructions and uploaded Project files, without requiring a heavy calorie/macro ledger or external app/database.

## Dry-Run 1 - Cycle Planning / Restart

Prompt:

```text
Synthetic test. Start a simple 7-day nutrition cycle from incomplete baseline and preferences. Keep it low-friction, ask at most one question, and mark unknown/defaulted fields. Do not create a live user diet.
```

Expected output:

- readable Russian answer first;
- one focused question maximum;
- 7-day cycle or meal-slot default structure;
- fallback meal rules;
- shopping/prep notes if useful;
- unknown/defaulted inputs visible;
- no required calorie/macro ledger;
- `nutrition_state_update_packet.v1` proposed if durable state would change;
- packet status remains `proposed_for_user_approval`.

Pass condition:

```yaml
dry_run_1:
  cycle_created_or_restartable: true
  missing_data_defaulted: true
  asks_at_most_one_question: true
  heavy_ledger_required: false
  live_user_diet_generated: false
  update_packet_present_if_state_changed: true
```

## Dry-Run 2 - Meal Event + Exception

Prompt:

```text
Synthetic test. Photo plus voice-style note: I ate a bigger off-menu lunch than planned. It looked like a bowl plus a sweet snack. I do not know exact amounts. Help me correct the rest of the day without restarting the cycle.
```

Expected output:

- treats the report as a larger off-menu lunch with incomplete detail;
- labels confidence as low or medium-low;
- uses rough categories, not fake precision;
- gives a practical next-meal or remaining-day correction;
- no punishment, moralizing, or compensatory restriction;
- one optional question maximum;
- continues with a default if the question is unanswered;
- adds event to review only if useful;
- no calorie/macro ledger requirement.

Pass condition:

```yaml
dry_run_2:
  ambiguous_event_handled: true
  confidence_labeled: true
  correction_practical: true
  no_punishment_rule_preserved: true
  asks_at_most_one_question: true
  continues_if_unanswered: true
  heavy_ledger_required: false
```

## Dry-Run 3 - Review + Sync

Prompt:

```text
Synthetic test. Weekly review: breakfasts were easy, lunches were boring, dinner prep was too much, and fallback meal saved me twice. I want to continue in a fresh chat next week. Produce the review and sync output.
```

Expected output:

- readable weekly review summary first;
- keep breakfast default;
- keep fallback meal rule;
- change lunches by adding variation;
- simplify dinner prep;
- keep/change/remove structure;
- discovered preferences with confidence;
- next-cycle delta;
- fresh-chat carryover;
- compact `nutrition_state_update_packet.v1`;
- `external_write_claimed: false`;
- packet status remains `proposed_for_user_approval`.

Pass condition:

```yaml
dry_run_3:
  review_summary_present: true
  keep_change_remove_present: true
  next_cycle_delta_present: true
  carryover_present: true
  update_packet_schema: nutrition_state_update_packet.v1
  external_write_claimed: false
  live_user_diet_generated: false
```

## Failure Conditions

The package fails acceptance if the Project:

- requires precise calorie/macro logging by default;
- blocks on missing non-safety details;
- asks many setup questions before producing a usable loop;
- claims external state was saved;
- makes Codex decide nutrition content;
- produces medical/clinical nutrition treatment;
- depends on external app, database, import, or automation;
- expands into training, cardio, recovery, supplements, fasting, or labs.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/protocols/DRY_RUN_ACCEPTANCE.md`
