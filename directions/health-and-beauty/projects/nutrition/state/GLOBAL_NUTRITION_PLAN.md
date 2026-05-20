# Global Nutrition Plan

Status: draft_for_user_approval  
Schema: global_nutrition_plan.v1  
Date: 2026-05-20

## Source artifacts

```yaml
global_nutrition_plan:
  schema: global_nutrition_plan.v1
  plan_status: draft_for_user_approval
  source_research:
    user_profile: state/USER_PROFILE_AND_CONSTRAINTS.yml
    deep_research_request: research/DEEP_RESEARCH_REQUEST.md
    deep_research_result: research/DEEP_RESEARCH_RESULT.md
    deep_research_synthesis: research/DEEP_RESEARCH_SYNTHESIS.md
    user_approval: pending
  external_write_claimed: false
```

## User objective hierarchy

### Primary objective

Reduce body weight and fat mass sustainably while preserving muscle mass, strength potential, cognitive performance, and the ability to return to structured strength training.

### Secondary objectives

1. Reduce load on legs/joints and improve health markers.
2. Control post-breakfast grazing and post-smoking-cessation oral craving.
3. Build a repeatable nutrition operating system that can run through Weekly Planning, Menu Chat, Tracking Chat, and Weekly Review.
4. Keep cooking and tracking low-friction enough to execute.
5. Improve body composition and appearance as a consequence of the above, not by crash dieting.

### First milestone

First major target: **5–10% body-weight reduction**, approximately **6–12.5 kg** from 125 kg.

This is not the final endpoint. It is the first clinical/behavioral milestone for validating the system.

## Strategic thesis

The best default strategy is:

> Moderate deficit, high protein, whole-food Mediterranean/DASH-like structure, three anchor meals, one planned morning anti-grazing slot, controlled sweets, modular meal prep, and light but real tracking.

This plan treats the main risk as a behavioral-energy-system problem: recent smoking cessation and household sweets increase oral craving and automatic eating, especially after breakfast. The strategy therefore controls timing, food environment, and decision points rather than relying on willpower alone.

## Non-negotiables

1. **Protein comes first.** Daily target ~180 g; acceptable range 170–200 g.
2. **No unplanned morning sweets.** The breakfast-to-lunch window is protected.
3. **No free grazing.** There may be one planned anti-grazing slot; everything else is a meal or logged deviation.
4. **Sweets are planned, portioned, and after a protein-containing meal.** Not with coffee between tasks.
5. **Weekly average beats daily scale noise.** Daily weight is allowed; decisions use 7-day averages.
6. **No crash fasting as default.** Keto, 5:2, alternate-day fasting, and extended fasting are not the starting plan.
7. **The plan adjusts from evidence.** Calories are a starting hypothesis, then calibrated by actual trend.
8. **Tracking is practical, not obsessive.** Approximate calories are enough unless a future issue requires tighter control.
9. **Medical risk is not ignored.** Snoring, possible insulin resistance, unknown BP/labs, and waist need follow-up.

## Nutrition targets

### Phase 1: first 14-day calibration

```yaml
calibration_phase:
  duration: 14_days
  calories:
    target_range_kcal_per_day: 2400-2600
    default_start_kcal_per_day: 2500
    status: hypothesis_to_validate_by_weight_trend
  protein:
    target_g_per_day: 180
    acceptable_range_g_per_day: 170-200
  fat:
    target_range_g_per_day: 60-80
  fiber:
    target_range_g_per_day: 30-40
    ramp_policy: increase_gradually_if_gi_discomfort
  carbohydrates:
    policy: remaining_calories_after_protein_and_fat
    default: moderate
  water:
    target_l_per_day: 3.0-3.5
  alcohol:
    policy: none_or_keep_zero
```

### Rationale

- Calories: 2400–2600 kcal/day is a working start, not a final truth.
- Protein: high enough to support lean-mass retention and satiety without using actual 125 kg body weight as a crude multiplier.
- Fat: sufficient but bounded to avoid invisible calorie overflow.
- Fiber/volume: supports satiety and lowers energy density.
- Moderate carbs: preserves flexibility and later supports strength training.

## Meal structure rules

### Default day structure

```yaml
meal_structure:
  anchor_meals: 3
  planned_anti_grazing_slot: 1
  free_snacking: false
  dinner: usually_present_but_lighter
```

### Timing anchors

- Wake: ~03:20.
- Breakfast: around 07:00.
- Lunch: around 12:00 or slightly later.
- Dinner: earlier evening if needed; should not be automatically skipped after a big lunch.

### Breakfast rule

Breakfast is the anti-grazing keystone.

Default breakfast requirements:

- 40–55 g protein;
- 10+ g fiber when feasible;
- no pastry/cookie/chocolate/cereal-type sweet trigger;
- not a “light sweet start” that opens grazing;
- enough volume to stabilize the next 2–3 hours.

### Morning anti-grazing slot

Use between breakfast and lunch only if needed.

Two versions:

1. **True hunger version:** 150–250 kcal protein-dominant snack.
2. **Mouth-stimulation version:** sugar-free gum, mint, tea, sparkling water/zero drink, crunchy cucumber/carrot/celery, tooth brushing.

Rule: first classify the urge as either “stomach hunger” or “mouth wants stimulation.” Do not treat both as the same.

### Lunch rule

Lunch is usually the main meal. It should contain:

- protein base;
- high-volume vegetable/fiber component;
- controlled carb portion;
- controlled fat.

### Dinner rule

Dinner may be lighter but should normally exist. Skipping dinner is allowed only if the day is genuinely complete and does not create later compensatory eating.

## Problem-food strategy

### High-risk foods

- sweets;
- pastries/buns;
- chips;
- dense savory snack foods;
- any food that becomes automatic eating when visible.

### Household rule

Sweets brought by wife are treated as environmental exposure, not personal failure.

Default storage policy:

- spouse sweets: opaque container, not visible, not near coffee/work path;
- user planned sweet: pre-portioned, logged, only after a meal with protein;
- no open packages near workstation;
- high-protein/low-calorie options should be more visible than sweets.

### Planned sweet policy

```yaml
planned_sweet_policy:
  allowed: true
  default_limit_kcal: 150-250
  timing: after_main_meal_with_protein
  forbidden_contexts:
    - post_breakfast_to_lunch_window_during_calibration
    - with_coffee_between_tasks
    - standing_in_kitchen_from_package
    - late_evening_if_it_disrupts_sleep_or_triggers_more_eating
  if_unplanned_sweet_occurs:
    - log_event
    - return_to_next_planned_meal
    - no_punishment_compensation
    - review_trigger_and_visibility
```

## Hydration strategy

Target: **3.0–3.5 L/day** unless medical constraints appear.

Tracking:

- use simple bottle count or chat note;
- do not micromanage electrolytes by default;
- if low-carb/fasting experiments ever happen, hydration/electrolyte review becomes more important.

## Caffeine strategy

Current: ~3 cups coffee/day.

Default policy:

- keep coffee if sleep/energy are stable;
- last full coffee usually before noon;
- if sleep worsens, move final caffeine earlier before changing diet calories;
- no sweet snack automatically attached to coffee.

## Fasting / time-restricted-eating decision

### Default

No intermittent fasting experiment during the first 14-day calibration.

### Conditional use

Time restriction can be tested later only if it clearly reduces decision burden and does not worsen post-breakfast grazing or rebound eating.

### Avoid / medical-only

- alternate-day fasting: avoid as default;
- 5:2 fasting: avoid as start;
- extended fasting: medical-only / avoid as lifestyle strategy.

## Named diet decisions

```yaml
named_diet_decisions:
  high_protein_structured_moderate_deficit: default
  mediterranean_whole_food_pattern: default_framework
  dash_like_pattern: conditional_if_bp_or_cardiometabolic_risk_supports
  low_carb_non_keto: conditional_experiment_after_calibration
  ketogenic_diet: avoid_as_default
  low_fat_diet: not_default_unless_preference_emerges
  flexible_dieting: default_as_light_tracking_not_heavy_ledger
  portion_method: backup_after_calibration
  meal_replacements: conditional_fallback_not_core_identity
```

## First 2-week calibration phase

### Purpose

Find whether 2400–2600 kcal/day, ~180 g protein/day, and the breakfast/anti-grazing system create the desired trend without excessive hunger, fatigue, or mental load.

### Daily minimum tracking

Tracking Chat should record:

- morning body weight;
- rough calories;
- protein hit/missed;
- water hit/missed;
- morning grazing: none / controlled slot / uncontrolled;
- sweets: none / planned / unplanned;
- hunger/energy: low / ok / high issue.

### Calibration success criteria

A successful first 14 days does not require perfect eating. It requires:

- enough logged data to estimate the trend;
- protein target hit most days;
- fewer uncontrolled post-breakfast events;
- no severe fatigue or dangerous symptoms;
- visible pattern for adjustments.

## 4-week operating cycle

After calibration, run 4-week cycles.

### Week 1

Stabilize menu, breakfast, tracking, and food environment.

### Week 2

Adjust calories/meal structure if needed based on Week 1 trend and adherence.

### Week 3

Keep stable unless trend is clearly wrong. Do not over-edit.

### Week 4

Review weight trend, waist, adherence, hunger, energy, training status, and problem foods. Decide whether to continue deficit, adjust, simplify, or take a maintenance break.

## Weekly review logic

Every week, review:

```yaml
weekly_review:
  metrics:
    - seven_day_average_weight
    - waist_if_available
    - protein_adherence
    - calorie_estimate_adherence
    - morning_grazing_frequency
    - planned_vs_unplanned_sweets
    - water_adherence
    - cognitive_energy
    - hunger
    - sleep_quality_or_snoring_notes
    - training_status_if_applicable
  decisions:
    - continue
    - reduce_150_200_kcal
    - add_100_200_kcal
    - tighten_environment
    - change_breakfast
    - add_or_remove_planned_snack
    - simplify_menu
    - consider_maintenance_break
```

## Monthly review logic

Every 4 weeks:

- compare starting and current 7-day average weight;
- compare waist if measured;
- inspect adherence trend;
- inspect whether morning grazing is improving;
- inspect training return/performance;
- decide whether the deficit is still tolerable;
- decide whether to continue another 4-week cycle or run maintenance.

## Adjustment rules

### Weight trend

- **0.4–0.8% loss/week:** continue.
- **<0.3–0.4% loss/week for 2 weeks with high adherence:** reduce 150–200 kcal/day or tighten environment.
- **>1.0% loss/week for 2 weeks or high fatigue/hunger:** add 100–200 kcal/day.
- **Flat trend with poor adherence:** fix execution before cutting calories.

### Hunger

- If stomach hunger is high: increase volume/fiber, ensure protein distribution, consider moving calories earlier.
- If mouth craving is high: use oral toolkit, not automatic calories.
- If hunger is worst after breakfast: redesign breakfast before lowering calories.

### Cravings and sweets

- If planned sweets work: keep them bounded.
- If planned sweets cause more eating: suspend for 7–14 days and replace with less-triggering options.
- If spouse sweets are visible: fix storage before blaming adherence.

### Training performance

When strength training returns:

- keep baseline calories for 1–2 weeks;
- if performance drops, add 100–250 kcal on training days from carbs around training;
- if recovery is poor, inspect sleep/protein/hydration/training load.

### Sleep and caffeine

If sleep worsens:

1. move caffeine earlier;
2. check late food/sweets;
3. check hydration timing;
4. consider sleep apnea screening if snoring/daytime sleepiness is present.

### Adherence failure

If off-plan eating happens:

- log it;
- return to next planned meal;
- do not compensate aggressively;
- identify trigger: visibility, hunger, boredom, mouth craving, stress, underbuilt meal, no fallback.

### Binge/compulsive pattern warning

If repeated loss-of-control eating appears:

- reduce rigid restriction;
- remove high-risk foods from visible access;
- use structured meals/snacks;
- consider clinician/therapist input if loss of control persists.

## Diet break / maintenance criteria

Use 7–14 days at estimated maintenance if:

- 2+ weeks of declining adherence despite simplification;
- sustained high hunger or irritability;
- significant drop in training performance after strength return;
- sleep/stress makes deficit nonfunctional;
- weight loss has been substantial and the system needs consolidation.

Maintenance is not a failure. It is a controlled phase with protein, meal structure, and tracking retained.

## Training-day vs rest-day logic

### During current 1–2 week cardio-only phase

- calories: 2400–2600;
- protein: unchanged;
- carbs: moderate;
- do not add calories just because VR/cardio happened unless hunger or performance data requires it.

### After strength training returns

- keep calories stable for 1–2 weeks;
- if performance is fine, no automatic increase;
- if performance drops, add carbs around training;
- protein remains unchanged.

## Emergency / fallback rules

### If no prepared meal

Use any fallback that satisfies:

- 40+ g protein;
- controlled calories;
- low trigger risk;
- quick assembly.

Examples are categories, not fixed menu:

- lean protein + frozen vegetables + potato/rice portion;
- cottage cheese / Greek yogurt-style protein base + fruit/oats if tolerated;
- eggs + vegetables + controlled carb;
- tuna/chicken/turkey-style protein + salad/vegetables + controlled carb;
- meal replacement only as backup, not core plan.

### If delivery urge appears

Decision rule:

1. Eat fallback protein meal first if genuinely hungry.
2. Wait 20 minutes.
3. If still ordering, choose high-protein/low-trigger option and log it.
4. Do not restart the week.

### If day goes off-plan

No punishment fasting. Resume next planned meal.

## Low-friction tracking rules

Tracking happens in weekly Tracking Chat, not Global Strategy Chat.

### Default daily tracking

```yaml
daily_tracking:
  weight_morning: required_if_possible
  food: rough_log_or_photo_or_voice
  calories: approximate
  protein: hit_or_miss_plus_estimate
  water: rough_liters_or_bottle_count
  morning_grazing: none_or_controlled_or_uncontrolled
  sweets: none_or_planned_or_unplanned
  hunger_energy: low_ok_high
  durable_github_update: false
```

### What not to track by default

- exact gram-level macro ledger forever;
- every micronutrient;
- guilt narrative;
- punishment/compensation math.

## Safety red flags

Seek medical input or stop aggressive deficit if any of these appear:

- chest pain;
- fainting;
- severe dizziness;
- unusual shortness of breath;
- severe fatigue not explained by sleep;
- signs of sleep apnea: loud frequent snoring, witnessed pauses, daytime sleepiness;
- repeated loss-of-control binge episodes;
- abnormal blood pressure or glucose markers if measured.

Recommended non-urgent checks:

- waist circumference;
- blood pressure;
- fasting glucose and/or HbA1c;
- lipid profile;
- ALT/AST if clinically appropriate;
- sleep apnea screening if snoring/daytime sleepiness is meaningful.

## What Weekly Planning Chat should do next

Weekly Planning Chat should create one `WEEKLY_PLAN` only. It should:

- define the week goal;
- choose calibration targets;
- define meal-structure constraints;
- define tracking inputs;
- define menu-chat inputs;
- avoid concrete meals, shopping lists, and prep plan.

## What Menu Chat must not override

Menu Chat must not override:

- protein target;
- calibration calorie range;
- no unplanned morning sweets;
- one controlled anti-grazing slot;
- planned sweet rules;
- low-friction tracking policy;
- safety constraints;
- global fasting decisions.

Menu Chat should build concrete meals around these constraints.

## What Tracking Chat should monitor

Tracking Chat should monitor:

- daily rough intake and protein;
- water;
- morning grazing;
- planned/unplanned sweets;
- hunger/energy;
- weight trend;
- deviations and triggers;
- training status when strength resumes;
- unresolved questions for weekly review.

Tracking Chat should not request GitHub writes after every food message. Durable update default is false until week close or explicit user request.

## Current approval status

This plan is a draft. It should not be treated as saved durable state until the user approves and Codex returns read-back/diff evidence.
