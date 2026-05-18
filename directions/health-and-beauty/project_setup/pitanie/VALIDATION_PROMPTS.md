# Project Питание Validation Prompts

These dry-runs validate behavior. They are not final menus, prescriptions, or clinical nutrition plans.

## Test 1 — Cycle Planning

Prompt:

```text
Create a first simple 7-day cycle. I have not filled baseline/preferences yet. Keep it low-friction and do not ask many questions.
```

Expected readable output:
- A 7-day menu package is created in readable form.
- The plan includes shopping list, recipes, prep plan, storage plan, fallback meals, and replacement rules.
- Missing data is shown as unknown/defaulted.
- The Project asks at most one immediate question.
- No calorie/macro ledger is required.

Expected technical planning basis:

```yaml
planning_basis:
  known:
    - low_friction_required
    - no_heavy_tracking
    - default_cycle_length_7_days
  unknown:
    - exact body metrics
    - food likes/dislikes
    - cooking schedule
    - equipment
    - allergies/intolerances
  defaulted:
    - cycle_length: "7 days"
      confidence_impact: "medium confidence; easy to revise"
    - meal_structure: "repeatable templates"
      confidence_impact: "medium confidence"
```

Pass condition:
- Menu, shopping list, recipes, prep plan, storage plan, fallback rules, and replacements are present.
- Missing fields are explicit.
- The response does not require calorie/macro logging.
- User-facing output is readable before any technical block.

## Test 2 — Meal Event / Off-Menu Lunch

Prompt:

```text
Photo + voice: I ate a bigger off-menu lunch than planned. It looked like a bowl plus a sweet snack. I do not know exact amounts.
```

Expected readable output:
- Interprets it as larger off-menu lunch.
- Confidence is low because exact amounts and photo details are incomplete.
- Recommends returning to planned next meal.
- No punishment or restart.
- One optional question maximum.

Expected technical event:

```yaml
meal_event:
  input_mode: mixed
  event_type: off_menu_meal
  user_reported:
    raw_summary: "bigger off-menu lunch; bowl plus sweet snack"
    exact_values_supplied: []
    ambiguous_items:
      - bowl contents
      - snack size
      - portion size
  ai_estimate:
    meal_category: "larger mixed meal plus sweet snack"
    rough_portion: "unknown; likely above planned lunch"
    likely_deviation_from_cycle: "moderate"
    confidence: low
    confidence_reason: "No exact amount and photo details not confirmed."
  correction:
    next_action: "Return to planned next meal; make it simple and not compensatory."
    remaining_day_adjustment: "Prefer normal structured dinner; avoid extra snacks unless hungry."
    tomorrow_adjustment_if_needed: "No full reset unless pattern repeats."
    no_punishment_rule: true
  questions:
    optional_single_question: "Was the sweet snack small, normal, or large?"
    pending_if_unanswered: true
    continue_if_unanswered:
      assumption: "Treat as normal-to-large snack."
      confidence_impact: "confidence remains low."
  state_update_needed:
    update_active_cycle: false
    update_preferences: false
    update_base_snapshot: false
    add_to_weekly_review: true
```

Pass condition:
- Handles photo/voice/text-style ambiguity.
- Gives rough estimate and confidence.
- Asks at most one optional question.
- Continues if unanswered.

## Test 3 — Missing-Answer Flow

Prompt:

```text
Can you make recipes for the cycle?
```

The Project asks:

```text
Do you have any confirmed equipment I should use, or should I assume no special equipment?
```

User gives no answer.

Expected continuation:

```yaml
missing_answer_handling:
  unanswered_question: "equipment availability"
  status: defaulted
  default_used: "no-special-equipment recipe format"
  confidence: medium_low
  confidence_reason: "Recipes can be drafted, but equipment optimization is unknown."
  action: "Proceed with generic low-equipment recipes and mark equipment-specific upgrades as pending."
```

Expected readable output:
- Recipes are drafted in generic low-equipment format.
- Equipment-specific upgrades are listed as pending.
- The Project does not block or repeatedly ask the same question.

Pass condition:
- Does not block.
- Explicitly marks default and confidence.
- Does not assume tools or storage.

## Test 4 — Review/Sync Behavior

Prompt:

```text
Weekly review: breakfasts were easy, lunches were boring, dinner prep was too much, fallback meal saved me twice. I want to continue in a new chat next week.
```

Expected readable output:
- Keeps breakfast template.
- Keeps fallback meal.
- Changes lunches by adding variation.
- Simplifies dinner prep.
- Produces next cycle delta.
- Produces save/update block.
- Produces New Chat Carryover Block.

Expected review result:

```yaml
review_result:
  period: weekly
  keep:
    - item: "breakfast template"
      reason: "easy"
    - item: "fallback meal rule"
      reason: "used twice successfully"
  change:
    - item: "lunch templates"
      reason: "boring"
      proposed_update: "add interchangeable flavor variations"
    - item: "dinner prep"
      reason: "too much effort"
      proposed_update: "reduce prep steps or shift to batchable/simple dinners"
  remove: []
  discovered_preferences:
    - preference: "low-effort breakfast works"
      evidence: "user weekly review"
      confidence: high
    - preference: "lunch needs more variety"
      evidence: "user weekly review"
      confidence: medium
  next_cycle_delta:
    menu_changes:
      - "Keep breakfast."
      - "Add lunch variation rule."
      - "Simplify dinners."
    prep_storage_changes:
      - "Preserve fallback meal."
```

Expected sync packet:

```yaml
nutrition_sync_packet:
  schema: nutrition_sync_packet.v1
  source_project: "Питание"
  external_write_claimed: false
  reason_for_sync:
    - review_completed
    - cycle_updated
    - preference_changed
    - carryover_needed
  updates:
    menu_preferences:
      changed: true
      changes:
        - "breakfast easy: keep"
        - "lunch variety needed"
        - "dinner prep too heavy"
    active_cycle:
      changed: true
      changes:
        - "add lunch flavor variation rule"
        - "simplify dinner prep"
        - "keep fallback meal"
  pending_questions:
    blocking: []
    useful_later:
      - "Which lunch flavors do you prefer?"
  next_recommended_action: "Draft next cycle delta in a fresh chat from carryover."
```

Expected carryover block:
- Includes current state summary.
- Includes latest review summary.
- Includes pending questions.
- Includes next recommended action.
- Does not claim external persistence.

Pass condition:
- Shows keep/change/remove.
- Emits durable update packet.
- Emits carryover block.
- Does not claim external persistence.
- User-facing summary comes before technical blocks.

END_OF_FILE: directions/health-and-beauty/project_setup/pitanie/VALIDATION_PROMPTS.md
