# 01 Nutrition Base

```yaml
nutrition_project_file:
  schema: nutrition_project_file.v1
  project: "Питание"
  file: 01_NUTRITION_BASE.md
  status: active
  purpose: baseline_boundaries_and_safety_context
```

## Baseline Snapshot

```yaml
nutrition_base:
  schema: nutrition_base.v1
  status: template_pending_user_input
  user_profile:
    age: unknown
    sex: unknown
    height: unknown
    weight: unknown
    body_objective: pending_user_confirmation
    activity_level: unknown
    routine_constraints: []
  nutrition_boundaries:
    medical_conditions: unknown
    medications: unknown
    allergies_or_intolerances: unknown
    pregnancy_or_eating_disorder_context: unknown
    clinical_guidance_allowed: false
  operating_preferences:
    language_default: ru
    tracking_burden: low
    heavy_calorie_macro_ledger_default: false
    external_tracker_required: false
    exact_grams_required: false
  confidence:
    baseline_confidence: low
    reason: "The package has no live baseline yet."
```

## Non-Clinical Boundary

Project `Питание` may help organize meals, defaults, fallback rules, shopping/prep notes, and reviews. It must not diagnose, treat, or manage medical conditions.

If safety-critical baseline data is missing, ask one focused question. If the missing detail is only optimization-related, mark it as pending and continue.

## Minimum Useful Baseline Questions

Ask only when needed:

1. Any allergy, intolerance, medical/pregnancy/eating-disorder context that affects safe meal organization?
2. What foods are strongly disliked or preferred?
3. What meal cadence is easiest to repeat?
4. What cooking/prep burden is realistic this week?

Do not ask all questions at once unless the user asks for full setup.

## Durable Update Triggers

Update this file when the user confirms:

- safety-relevant boundaries;
- stable routine constraints;
- body objective or baseline metrics;
- activity/routine pattern relevant to meal planning;
- a persistent low-friction operating preference.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/01_NUTRITION_BASE.md`
