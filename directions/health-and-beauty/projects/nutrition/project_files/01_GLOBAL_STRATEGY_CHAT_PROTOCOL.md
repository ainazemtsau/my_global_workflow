# 01 - Global Strategy Chat Protocol

Status: active

Purpose:
Build a genuinely personalized, evidence-based global nutrition strategy through separate profile capture, research request, research result preservation, research synthesis, and user-approved final plan.

This chat is not a menu chat.
This chat is not weekly planning.
This chat is not tracking.
This chat must not produce generic advice as final strategy.

## Required source files

Read if present:

- `state/USER_PROFILE_AND_CONSTRAINTS.yml`
- `research/DEEP_RESEARCH_REQUEST.md`
- `research/DEEP_RESEARCH_RESULT.md`
- `research/DEEP_RESEARCH_SYNTHESIS.md`
- `state/GLOBAL_NUTRITION_PLAN.md`

If old `state/USER_PROFILE_AND_CONSTRAINTS.md` exists, treat it as legacy compatibility input only. Prefer `.yml` for structured user facts.

## Non-negotiable separation

The chat must keep these artifacts separate:

```text
USER_PROFILE_AND_CONSTRAINTS.yml
= facts, constraints, preferences, risks, schedule, equipment, lifestyle, uncertainty.

DEEP_RESEARCH_REQUEST.md
= detailed research task generated from the user profile.

DEEP_RESEARCH_RESULT.md
= supplied research output, source-backed where possible, not yet the plan.

DEEP_RESEARCH_SYNTHESIS.md
= analysis, tradeoffs, conclusions, suitability matrix, decision logic.

GLOBAL_NUTRITION_PLAN.md
= final approved operating strategy and cycle plan.
```

Do not collapse all of this into one YAML blob.

## First-start sequence

```yaml
sequence:
  - read_existing_profile_if_available
  - collect_personal_strategic_intake
  - identify_profile_gaps_and_unknowns
  - produce_or_update_USER_PROFILE_AND_CONSTRAINTS_yml_save_packet
  - produce_DEEP_RESEARCH_REQUEST_md
  - stop_before_research_result
```

First start must output:

- Short human-readable summary of what was learned.
- `USER_PROFILE_AND_CONSTRAINTS.yml` proposed content or update packet.
- `DEEP_RESEARCH_REQUEST.md` proposed content.
- Clear instruction: user must approve/save profile and run Deep Research before final plan.

First start must not:

- finalize `GLOBAL_NUTRITION_PLAN`;
- create weekly plan;
- create concrete menu;
- create shopping list;
- create prep plan;
- pretend research is complete;
- give generic final advice.

## Personal strategic intake requirements

Collect enough to avoid generic planning.

Required domains:

- body metrics: age, sex, height, weight, waist if available, weight history;
- body composition context: fat distribution, muscle/training background, visual goal if user wants;
- training: current strength training, cardio, steps/activity, recovery capacity;
- work/cognition: mental load, work hours, energy/concentration requirements;
- schedule: wake time, sleep window, meal timing reality, travel/work disruptions;
- appetite/snacking: hunger pattern, cravings, post-meal eating, evening eating, binge/compulsive risk indicators;
- food environment: what foods are available, what foods are dangerous, family/social context;
- preferences: liked foods, disliked foods, cuisines, budget, cooking tolerance;
- equipment: kitchen tools, meal-prep capacity, storage/freezer/vacuum sealer;
- tracking tolerance: what user will actually log and what is too much;
- medical/safety: medications, diabetes risk, blood pressure, kidney/GI issues, sleep apnea signs, labs if known;
- previous attempts: diets tried, what failed, what was sustainable;
- strictness preference: acceptable rigidity, failure handling, social meals.

If not all data is available, separate:

- blocking gaps;
- useful later gaps;
- non-blocking unknowns.

Do not invent unknowns.

## Deep Research Request requirements

`DEEP_RESEARCH_REQUEST.md` must be normal markdown, not YAML-only.

It must be detailed enough for a separate Deep Research process to answer.

It must include:

- User profile summary.
- Goal hierarchy.
- Hard constraints.
- Uncertainties.
- Research objective.
- Required evidence standard.
- Required topic coverage.
- Output format expected from research.
- Safety boundaries.
- Explicit instruction to compare options and reject unsuitable options.

Required research coverage:

- energy deficit strategies for obese but strength-trained adult male;
- body recomposition versus fat-loss priority;
- protein targets and distribution;
- resistance training interaction with diet;
- carbohydrates: moderate carb, low carb, keto, carb timing, glycemic load;
- fats: minimums, satiety, calorie density;
- fiber, food volume, ultra-processed food, satiety;
- meal timing and meal frequency;
- breakfast timing for very early wake schedule;
- intermittent fasting / time-restricted eating;
- alternate-day fasting;
- 5:2 fasting;
- extended fasting and why/when it is inappropriate;
- diet breaks;
- refeeds;
- maintenance phases;
- Mediterranean/DASH/whole-food patterns;
- low-fat diets;
- high-protein diets;
- low-carb/keto diets;
- flexible dieting / calorie counting;
- portion-control approaches without heavy tracking;
- meal replacements, if relevant;
- hydration and water targets;
- electrolytes/sodium/potassium/magnesium where relevant;
- caffeine timing and appetite/energy impact;
- alcohol policy if relevant;
- snacking/grazing control;
- sweets/problem-food policy;
- meal prep and fallback meals;
- behavior design and food environment;
- hunger/craving management;
- sleep/stress/cognitive performance interactions;
- weekly/monthly cycle design;
- metrics and adjustment rules;
- safety red flags and when to involve a clinician.

Expected Deep Research output:

- evidence summary by topic;
- evidence quality notes;
- options compared;
- suitability for this user;
- what to use by default;
- what to avoid;
- what is optional/conditional;
- what requires medical supervision;
- practical implications;
- citations/source notes if available.

## After Deep Research result is supplied

Sequence:

```yaml
sequence:
  - save_or_propose_DEEP_RESEARCH_RESULT_md
  - produce_DEEP_RESEARCH_SYNTHESIS_md
  - explicitly_compare_major_strategy_options
  - reject_unsuitable_options
  - select_default_operating_strategy
  - create_detailed_GLOBAL_NUTRITION_PLAN_md
  - require_user_approval_before_save
```

The chat must produce a detailed synthesis before final plan.

## Deep Research Synthesis requirements

`DEEP_RESEARCH_SYNTHESIS.md` must be normal markdown.

It must include:

- Executive conclusion.
- User-specific implications.
- Evidence-by-topic analysis.
- Suitability matrix for major diet/practice options.
- What to use now.
- What to avoid by default.
- What can be tested conditionally.
- Safety constraints.
- Decision rules.
- Open uncertainties.
- How the synthesis changes the global plan.

Suitability matrix must cover at minimum:

- moderate deficit high-protein structured diet;
- Mediterranean/whole-food pattern;
- low-carb but not keto;
- ketogenic diet;
- intermittent fasting/time-restricted eating;
- alternate-day fasting;
- 5:2 fasting;
- extended fasting;
- calorie counting / macro tracking;
- portion method / hand portions;
- meal replacements;
- diet breaks/maintenance phases;
- refeeds;
- high-volume/high-fiber strategy.

For each option:

- possible benefit;
- main risk;
- user fit;
- burden;
- evidence confidence;
- decision: default / conditional experiment / avoid / medical-only.

## Final GLOBAL_NUTRITION_PLAN requirements

`GLOBAL_NUTRITION_PLAN.md` must be detailed, operational, and personalized.

It must include:

- Plan status and source artifacts.
- User objective hierarchy.
- Strategic thesis.
- Non-negotiables.
- Nutrition targets with rationale.
- Meal structure rules.
- Problem-food strategy.
- Hydration strategy.
- Caffeine strategy if relevant.
- Fasting/time-restricted-eating decision.
- Named diet decisions.
- First 2-week calibration phase.
- 4-week operating cycles or other cycle structure chosen by evidence.
- Weekly review logic.
- Monthly review logic.
- Adjustment rules.
- Diet break / maintenance criteria.
- Training-day versus rest-day logic if relevant.
- Emergency/fallback rules.
- Low-friction tracking rules.
- Safety red flags.
- What Weekly Planning Chat should do next.
- What Menu Chat should not override.
- What Tracking Chat should monitor.

The plan must be stronger than:

- "eat more protein";
- "moderate deficit";
- "meal prep";
- "drink water";
- "avoid snacking".

It must include operational decision rules, for example:

- if weekly average weight drops too fast/slow;
- if hunger becomes unmanageable;
- if training performance falls;
- if cravings increase;
- if sleep worsens;
- if adherence fails;
- if binge/compulsive patterns appear;
- when to add/remove fasting windows;
- when to use diet break;
- when to simplify plan.

## User approval gate

Before any final save packet:

- show human-readable plan summary;
- show exact files to be updated;
- ask user to approve or request changes;
- do not mark packet `approved_by_user` unless the user explicitly approves.

## Save packets

Save packet must be separated by artifact.

Allowed target files:

- `state/USER_PROFILE_AND_CONSTRAINTS.yml`
- `research/DEEP_RESEARCH_REQUEST.md`
- `research/DEEP_RESEARCH_RESULT.md`
- `research/DEEP_RESEARCH_SYNTHESIS.md`
- `state/GLOBAL_NUTRITION_PLAN.md`

The chat may propose a multi-file save packet, but it must not claim external save.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/01_GLOBAL_STRATEGY_CHAT_PROTOCOL.md
