# 03 Dry-Run Acceptance

```yaml
nutrition_project_file:
  schema: nutrition_project_file.v1
  project: "Питание"
  file: 03_DRY_RUN_ACCEPTANCE.md
  status: active
  purpose: synthetic_acceptance_tests_for_repo_backed_fresh_chat_continuation
```

## Rule

These tests use synthetic inputs only. They are not live user diet generation, not a clinical protocol, and not evidence that external files were saved unless save/read-back evidence is supplied.

Project `Питание` passes v0 only when all six checks pass without hidden chat memory, manual giant packets, MacroFactor revival, or a default detailed calorie/macro ledger.

## Test 1 - First-Week Bootstrap From Empty State

Prompt:

```text
Synthetic test. Start Project Питание from empty state. Ask only the smallest useful missing input, continue with explicit defaults, and prepare the first durable state update proposal. Do not create a live user diet.
```

Pass condition:

```yaml
first_week_bootstrap_from_empty_state:
  reads_start_file: true
  detects_empty_baseline_or_plan: true
  asks_at_most_one_question: true
  continues_with_explicit_defaults: true
  emits_update_packet_if_state_should_change: true
  packet_status: proposed_for_user_approval
  hidden_memory_required: false
  heavy_ledger_required: false
```

## Test 2 - Later-Week Bootstrap From Saved State

Prompt:

```text
Synthetic test. Continue a later week from uploaded saved baseline and current plan. Do not re-ask the full baseline. Tell me what you can continue from and ask only one changed/stale detail if needed.
```

Pass condition:

```yaml
later_week_bootstrap_from_saved_state:
  reads_saved_state_files: true
  does_not_reask_full_baseline: true
  identifies_current_plan_anchor: true
  asks_only_changed_or_stale_detail_if_needed: true
  hidden_memory_required: false
  giant_packet_required: false
```

## Test 3 - Fresh Menu Chat From Saved Plan

Prompt:

```text
Synthetic test. Build this week's menu from the saved current plan and review inputs. Keep it low-friction and include fallback/replacement rules.
```

Pass condition:

```yaml
fresh_menu_chat_from_saved_plan:
  uses_CURRENT_NUTRITION_PLAN: true
  uses_REVIEW_AND_NEXT_WEEK_when_available: true
  produces_active_week_menu_or_update: true
  includes_fallback_or_replacement_rules: true
  external_database_required: false
  heavy_ledger_required: false
```

## Test 4 - Fresh Tracking Chat From Saved Plan And Menu

Prompt:

```text
Synthetic test. I had a bigger off-menu lunch than planned and do not know exact amounts. Help me correct the rest of the day from the saved plan/menu without restarting the week.
```

Pass condition:

```yaml
fresh_tracking_chat_from_saved_plan_and_menu:
  uses_saved_plan_or_menu: true
  handles_ambiguous_event: true
  confidence_labeled: true
  correction_is_practical: true
  no_punishment_rule_preserved: true
  asks_at_most_one_optional_question: true
  continues_if_unanswered: true
  heavy_ledger_required: false
```

## Test 5 - Week Review From Saved Report

Prompt:

```text
Synthetic test. Use the saved week tracking report: breakfasts were easy, lunches were boring, dinner prep was too much, fallback meal saved me twice. Produce review and next-week inputs.
```

Pass condition:

```yaml
week_review_from_saved_report:
  reads_WEEK_TRACKING_REPORT: true
  produces_keep_change_remove: true
  identifies_next_week_inputs: true
  emits_update_packet_if_state_should_change: true
  external_write_claimed: false
  live_user_diet_generated: false
```

## Test 6 - Project Files Refresh Reproducibility

Prompt:

```text
Synthetic test. Codex has returned save evidence. Explain exactly which Project Files to refresh and how a fresh chat should verify continuation from repository-backed state.
```

Pass condition:

```yaml
project_files_refresh_reproducibility:
  lists_five_state_files: true
  lists_four_protocol_files: true
  states_project_files_are_cache_only: true
  requires_repository_save_evidence_before_claiming_saved_state: true
  fresh_chat_starts_from_00_file: true
  hidden_memory_required: false
  giant_packet_required: false
```

## Failure Conditions

The package fails if any path:

- depends on hidden chat memory;
- requires manual giant state packets as the normal workflow;
- requires detailed calorie or macro logging by default;
- revives MacroFactor or external tracker dependence;
- claims external persistence without evidence;
- makes Codex decide nutrition content;
- expands into training, cardio, recovery, supplements, fasting, labs, or clinical treatment.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/03_DRY_RUN_ACCEPTANCE.md`
