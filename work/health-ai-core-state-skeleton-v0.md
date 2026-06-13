# Health AI Core State Skeleton v0

Status: minimal source-of-truth skeleton for Health AI System.

Basis:
- `live/health/CHARTER.md`
- `live/health/TREE.md`
- `live/health/NOW.md`
- `work/health-ai-core-contract-v0.md`
- `live/health/history/2026-06-13-s-health-ai-core-t-1-work-001.md`
- `live/health/history/2026-06-13-s-health-starter-kit-t-2-guide-003.md`
- `live/health/history/2026-06-13-s-health-ai-core-shape-001-approval.md`
- Live owner clarification in this session: Health AI System must not be only a data store plus chat interface; it needs a guidance/governance contour that can choose the next best step, run investigations, adapt plans, spawn bounded child work, and feel like a health team while staying structurally simple.

## 1. Skeleton Purpose

This skeleton defines the first durable state shape for Health AI System.

It must let an AI provider or coding agent:
- understand the current health direction without relying on chat memory;
- answer ordinary-language requests by selecting the right procedure;
- guide the owner toward the global goal, not only manipulate records;
- store operational raw data inside Health AI System when useful;
- keep Direction OS strategic: summary, problem, decision, CALL only;
- remain portable to future apps and integrations.

This is not a database schema, API, app UI, recipe-manager choice, training app choice, or full nutrition/training program.

## 2. Top-Level Shape

Recommended portable layout:

```text
health-ai/
  README.md
  STATE_INDEX.md

  governance/
    strategy.md
    current_phase.md
    next_actions.md
    open_questions.md
    investigation_queue.md

  state/
    profile.md
    preferences.md
    safety.md
    metrics_summaries.md
    active_plans.md
    training_activity.md
    feedback.md

  nutrition/
    weekly_plans/
    food_logs/
    recipes/
    recipe_feedback.md

  training/
    plan_summaries/
    session_logs/
    activity_summaries/

  reviews/
    weekly/
    incidents/

  procedures/
    registry.md
    guidance.md
    weekly_planning.md
    today_menu.md
    food_log.md
    recipe.md
    today_training.md
    weekly_review.md
    investigation.md
    research.md

  roles/
    registry.md

  knowledge/
    research_briefs.md

  patches/
    pending.md
    applied_log.md

  integrations/
    registry.md
```

The exact repository or app location is intentionally unchosen. The layout is a portable skeleton that can live in GitHub-backed files first and later map into a database or specialized tools.

Integration-neutrality rule:
- records may name an integration area, owned-data boundary, candidate status, or export/import surface;
- records must not select a concrete recipe manager, training app, wearable, VR tool, database, API, or automation platform in v0.

## 3. Source-of-Truth Rules

### Direction OS

Direction OS stores strategic direction state only:
- mission and success criteria;
- bets, tasks, reviews, decisions, and CALLs;
- compact summaries and incidents when they matter strategically.

Direction OS must not store:
- raw food logs;
- raw training sets;
- raw wearable/activity streams;
- raw daily check-ins;
- raw meal photos or meal descriptions;
- app-native exports except as compressed review evidence.

### Health AI System

Health AI System stores operational state:
- current strategy/phase/next actions;
- owner profile, preferences, constraints, and safety flags;
- plans, logs, recipes, summaries, feedback, reviews, incidents;
- pending patches and applied patch log;
- procedure and role definitions;
- research briefs and freshness notes.

Health AI System may contain operational raw data when it directly helps the system work:
- food-log entries;
- owner check-in notes;
- training/session summaries or raw entries before a specialized tool exists;
- recipe drafts and feedback;
- daily plan adherence notes;
- measurement rows if later chosen as part of Health AI state.

### Future Integrations

Future tools may own raw tool-native data:
- training app for sets and exercises;
- activity tracker for bike/walk/VR/wearable streams;
- recipe manager for recipe UI and grocery flow;
- lab/medical record source if ever used.

Health AI System stores import summaries, pointers, and interpretation notes. It does not choose any integration in v0.

## 4. Core State Records

Each record has:
- `id`
- `status`
- `updated_at`
- `source`
- `confidence`
- `owner_approved` when needed
- `pending_patches` when proposed changes exist

### 4.1 `STATE_INDEX.md`

Purpose:
- make new chats quickly understand what exists, what is missing, and where to look.

Required fields:
- `state_version`
- `updated_at`
- `current_phase_ref`
- `active_plans_ref`
- `today_context_ref`
- `safety_status_ref`
- `next_actions_ref`
- `open_investigations_ref`
- `missing_required_state`
- `stale_state`
- `how_to_start`

Raw operational data allowed: no. This is an index.

Direction OS output: no, unless index says the system is blocked or needs a strategic CALL.

### 4.2 `governance/strategy.md`

Purpose:
- hold the global health operating strategy that guides choices.

Required fields:
- `goal`
- `success_metrics`
- `current_horizon`
- `phase_sequence`
- `guardrails`
- `primary_constraints`
- `decision_rules`
- `known_risks`
- `review_cadence`
- `when_to_escalate_to_direction_os`

Raw operational data allowed: no.

Direction OS output: strategic summary or decision only.

### 4.3 `governance/current_phase.md`

Purpose:
- define what the system is optimizing now.

Required fields:
- `phase_id`
- `phase_name`
- `started_at`
- `target_outcome`
- `done_when`
- `kill_or_review_triggers`
- `current_focus`
- `not_now`
- `required_baselines`
- `active_constraints`
- `next_review_due`

Raw operational data allowed: no. It may link to summaries.

Direction OS output: phase review or decision only.

### 4.4 `governance/next_actions.md`

Purpose:
- let the owner ask "what is my next step?" and receive a guided answer.

Required fields:
- `top_next_action`
- `why_this_now`
- `action_type`: `measure | plan | execute | log | review | investigate | research | buy_prepare | decide | rest`
- `owner_effort`
- `blocking_state`
- `fallback_action`
- `expires_or_review_at`
- `source_reasoning`
- `related_procedure`

Raw operational data allowed: no.

Direction OS output: only if the next action is a strategic decision or CALL.

### 4.5 `governance/investigation_queue.md`

Purpose:
- track bounded investigations when progress is off or risk appears.

Required fields:
- `investigation_id`
- `trigger`
- `hypothesis`
- `scope`
- `questions`
- `data_needed`
- `child_work_needed`
- `owner_input_needed`
- `status`: `open | waiting | done | dropped`
- `result_summary`
- `patches_proposed`
- `escalate_to_direction_os`

Raw operational data allowed: limited links and short excerpts only. Detailed logs stay in their owning records.

Direction OS output: compact incident/problem/decision/CALL only.

### 4.6 `state/profile.md`

Purpose:
- durable owner facts used across procedures.

Required fields:
- `identity_basics`
- `starting_context`
- `equipment`
- `environment`
- `experience_level`
- `available_tools`
- `medical_safety_context`
- `measurement_access`
- `source_refs`

Raw operational data allowed: no; durable facts only.

Direction OS output: only if a strategic constraint changes.

### 4.7 `state/preferences.md`

Purpose:
- prevent the owner from repeating preferences in every chat.

Required fields:
- `food_preferences`
- `cooking_preferences`
- `shopping_constraints`
- `meal_timing_preferences`
- `training_preferences`
- `activity_preferences`
- `communication_preferences`
- `friction_notes`
- `known_failure_patterns`
- `fallback_preferences`

Raw operational data allowed: no; preference facts and summaries only.

Direction OS output: no, except major repeated adherence blocker.

### 4.8 `state/safety.md`

Purpose:
- keep safety gates visible to every procedure.

Required fields:
- `risk_posture`
- `standing_cautions`
- `current_red_flags`
- `pain_or_injury_notes`
- `fatigue_recovery_flags`
- `medical_escalation_rules`
- `load_escalation_allowed`
- `last_checked_at`
- `unknowns`

Raw operational data allowed: limited symptom/check-in notes. Detailed daily logs stay in check-ins or incident records if later added.

Direction OS output: incident or decision only.

### 4.9 `state/metrics_summaries.md`

Purpose:
- provide trend context without forcing Direction OS to store metrics.

Required fields:
- `period`
- `weight_summary`
- `nutrition_adherence_summary`
- `training_summary`
- `activity_summary`
- `sleep_energy_summary`
- `hunger_recovery_summary`
- `trend_confidence`
- `data_completeness`
- `notable_changes`
- `review_flags`

Raw operational data allowed: no. This is a summary record; raw rows live in Health AI logs or future integrations.

Direction OS output: review summary only.

### 4.10 `state/active_plans.md`

Purpose:
- let new chats find current plans.

Required fields:
- `global_strategy_ref`
- `current_phase_ref`
- `weekly_food_plan_ref`
- `training_activity_plan_ref`
- `today_menu_status`
- `today_training_status`
- `plan_gaps`
- `fallbacks_available`
- `last_plan_review`
- `next_plan_review_due`

Raw operational data allowed: no; links to plan records.

Direction OS output: only plan-level problem/decision/CALL.

### 4.11 `nutrition/weekly_plans/<week-id>.md`

Purpose:
- concrete weekly food/menu plan.

Required fields:
- `week`
- `goal`
- `assumptions`
- `nutrition_targets_level`: `rough | portions | grams | macros`
- `daily_menu`
- `meal_prep_plan`
- `fallback_meals`
- `shopping_notes`
- `recipe_refs`
- `owner_constraints`
- `confidence`
- `review_due`

Raw operational data allowed: planned meals only, not raw eaten logs.

Direction OS output: no daily data; only weekly summary/problem/decision if needed.

### 4.12 `nutrition/food_logs/<date>.md`

Purpose:
- store what was eaten enough for same-day advice and review.

Required fields:
- `date`
- `entries`
- `entry_id`
- `time_or_meal_slot`
- `owner_description`
- `input_mode`: `text | voice_transcript | photo_style_description | imported`
- `followup_questions`
- `skipped_questions`
- `estimated_foods`
- `portion_confidence`
- `plan_match`
- `same_day_advice`
- `confidence`
- `source_chat`

Raw operational data allowed: yes, inside Health AI System only.

Direction OS output: no raw logs. Only repeated problem, incident, or review summary.

### 4.13 `nutrition/recipes/<recipe-id>.md`

Purpose:
- durable recipe card usable by menus and future recipe apps.

Required fields:
- `recipe_id`
- `name`
- `status`: `draft | active | archived`
- `servings`
- `ingredients`
- `steps`
- `equipment`
- `prep_time`
- `nutrition_estimate`
- `nutrition_confidence`
- `owner_fit_notes`
- `tags`
- `substitutions`
- `menu_refs`
- `feedback_history`
- `export_targets`

Raw operational data allowed: recipe content and feedback notes, yes. Not daily food logs unless linked as feedback summary.

Direction OS output: no, unless recipe process creates a strategic tooling decision.

### 4.14 `state/training_activity.md`

Purpose:
- top-level training and activity state.

Required fields:
- `current_plan_ref`
- `today_training_status`
- `available_modes`
- `equipment`
- `safety_status_ref`
- `recent_training_summary_ref`
- `activity_summary_ref`
- `constraints`
- `missing_state`

Raw operational data allowed: no; links to logs/summaries.

Direction OS output: only strategic problem/decision/CALL.

### 4.15 `training/plan_summaries/<plan-id>.md`

Purpose:
- store current training/activity plan without choosing an app.

Required fields:
- `plan_id`
- `date_range`
- `goal`
- `weekly_structure`
- `strength_work`
- `conditioning_or_activity`
- `home_gym_options`
- `progression_rule_level`: `none | simple | full`
- `safety_modifications`
- `fallback_sessions`
- `review_due`

Raw operational data allowed: planned work only.

Direction OS output: no daily data; only plan-level decision/problem.

### 4.16 `training/session_logs/<date>.md`

Purpose:
- temporary Health AI-owned session record until a specialized training app owns raw sets.

Required fields:
- `date`
- `session_type`
- `planned_session_ref`
- `completed_summary`
- `exercises_or_activity`
- `effort`
- `pain_or_symptoms`
- `modifications`
- `confidence`
- `source`

Raw operational data allowed: yes, inside Health AI System unless a future training app owns it.

Direction OS output: no raw sets; only summaries/incidents.

### 4.17 `training/activity_summaries/<period>.md`

Purpose:
- summarize walking, bike, VR, conditioning, and wearable-like activity without choosing tools.

Required fields:
- `period`
- `activity_modes`
- `duration_summary`
- `intensity_summary`
- `consistency`
- `source`
- `confidence`
- `issues`
- `next_adjustment`

Raw operational data allowed: summary only. Raw streams belong to future integrations or separate logs.

Direction OS output: review summary/problem only.

### 4.18 `state/feedback.md`

Purpose:
- capture friction and learning across nutrition, training, tracking, and motivation.

Required fields:
- `feedback_id`
- `date`
- `area`
- `owner_words`
- `severity`
- `recurrence`
- `likely_cause`
- `recommended_patch`
- `needs_investigation`
- `needs_direction_os`

Raw operational data allowed: owner feedback text, yes.

Direction OS output: repeated blocker or decision only.

### 4.19 `reviews/weekly/<week-id>.md`

Purpose:
- close the weekly loop and adapt plans.

Required fields:
- `week`
- `goal_for_week`
- `weight_trend_summary`
- `nutrition_summary`
- `training_summary`
- `activity_summary`
- `sleep_energy_recovery_summary`
- `adherence_summary`
- `what_worked`
- `what_failed`
- `investigations_opened`
- `patches_proposed`
- `next_week_focus`
- `direction_os_output`

Raw operational data allowed: no; this is compressed review.

Direction OS output: summary/problem/decision/CALL only.

### 4.20 `reviews/incidents/<incident-id>.md`

Purpose:
- handle pain, safety, repeated failures, tooling breakdown, or system overload.

Required fields:
- `incident_id`
- `trigger`
- `severity`
- `area`
- `facts`
- `unknowns`
- `immediate_action`
- `investigation_needed`
- `patches_proposed`
- `medical_or_professional_escalation`
- `direction_os_output`

Raw operational data allowed: limited facts needed for incident; raw logs remain in source records.

Direction OS output: incident summary/decision/CALL only.

### 4.21 `patches/pending.md`

Purpose:
- keep proposed changes explicit before they are applied.

Required fields:
- `patch_id`
- `target`
- `change`
- `reason`
- `source`
- `confidence`
- `owner_approval_required`
- `risk_level`
- `direction_os_escalation`
- `status`

Raw operational data allowed: no; patches may reference raw records.

Direction OS output: only if patch changes strategic direction state.

### 4.22 `patches/applied_log.md`

Purpose:
- maintain audit trail of state changes.

Required fields:
- `patch_id`
- `applied_at`
- `applied_by`
- `target`
- `summary`
- `source`
- `rollback_note`

Raw operational data allowed: no.

Direction OS output: no.

### 4.23 `procedures/registry.md`

Purpose:
- let ordinary-language requests route to repeatable procedures.

Required fields:
- `procedure_id`
- `name`
- `intent_examples`
- `reads`
- `writes`
- `owner_inputs`
- `child_work_allowed`
- `output`
- `done_when`
- `escalation_rules`

Raw operational data allowed: no.

Direction OS output: procedure-level CALL only if the work belongs in Direction OS.

### 4.24 `roles/registry.md`

Purpose:
- define the AI team roles without binding them to a provider.

Required fields:
- `role_id`
- `name`
- `responsibility`
- `allowed_procedures`
- `must_read`
- `must_not_do`
- `handoff_rules`

Initial roles:
- `health_director`: chooses next best step and keeps global route coherent.
- `nutrition_lead`: plans food, menus, recipes, and food-log advice.
- `training_coach`: plans training/activity and protects safety constraints.
- `review_analyst`: performs weekly reviews and investigations.
- `researcher`: checks current external knowledge when needed.
- `writer_operator`: applies approved patches and exports to future integrations.
- `general_health_chat`: receives ordinary-language requests and routes to procedures.

Raw operational data allowed: no.

Direction OS output: no.

### 4.25 `knowledge/research_briefs.md`

Purpose:
- keep modern external knowledge usable without mixing it with raw operational logs.

Required fields:
- `brief_id`
- `question`
- `date_checked`
- `sources`
- `applicable_to_owner`
- `confidence`
- `expires_or_review_after`
- `state_implication`
- `procedure_implication`

Raw operational data allowed: no.

Direction OS output: decision/CALL only if external knowledge changes strategy.

### 4.26 `integrations/registry.md`

Purpose:
- record possible integration surfaces without selecting tools in v0.

Required fields:
- `integration_area`
- `status`: `none | candidate | selected | deprecated`
- `candidate_tools`
- `owned_data`
- `health_ai_import_summary`
- `export_action`
- `selection_decision_ref`

Raw operational data allowed: no.

Direction OS output: integration decision only.

## 5. Procedure Registry v0

Procedures are the way the system acts. A chat can be free-form on the surface, but internally it should route to one procedure at a time. If the request is broad, `guidance` chooses the next work item.

### `guidance`

Purpose:
- answer "what should I do next?" or steer after review.

Reads:
- `STATE_INDEX.md`
- `governance/strategy.md`
- `governance/current_phase.md`
- `governance/next_actions.md`
- `state/metrics_summaries.md`
- `reviews/weekly/`
- `reviews/incidents/`

Writes:
- `governance/next_actions.md`
- optional `governance/investigation_queue.md`
- optional pending patches.

Output:
- one next best action;
- why now;
- what not to do now;
- whether child work, research, or Direction OS escalation is needed.

### `weekly_planning`

Purpose:
- create or update the next week's food/training/activity plan.

Reads:
- strategy, current phase, preferences, safety, active plans, metrics summaries, feedback, recipes, training state.

Writes:
- `nutrition/weekly_plans/<week-id>.md`
- `training/plan_summaries/<plan-id>.md`
- `state/active_plans.md`
- pending patches.

Output:
- weekly plan plus missing-state flags.

### `today_menu`

Purpose:
- answer today's menu from state.

Reads:
- active plans, weekly food plan, preferences, recipes, food-log context.

Writes:
- optional patch to active plan or today's derived menu.

Output:
- today's menu, substitutions, fallback, missing-plan route if needed.

### `food_log`

Purpose:
- save available food data and give same-day advice.

Reads:
- active food plan, preferences, recipes, current day logs.

Writes:
- `nutrition/food_logs/<date>.md`
- feedback or pending patches when a pattern appears.

Output:
- log confirmation, confidence, same-day advice.

### `recipe`

Purpose:
- create, update, or prepare export of a recipe.

Reads:
- preferences, nutrition goals, active plans, recipe library, feedback.

Writes:
- `nutrition/recipes/<recipe-id>.md`
- optional integration export action in future.

Output:
- recipe-card patch and menu linkage if relevant.

### `today_training`

Purpose:
- answer today's training/activity from plan and safety state.

Reads:
- active plans, training/activity state, safety, recent summaries.

Writes:
- optional session plan patch or incident if safety issue appears.

Output:
- today's training/activity, safety modification, missing-plan route if needed.

### `weekly_review`

Purpose:
- adapt the system after a week.

Reads:
- metrics summaries, weekly plans, food logs summaries, training/activity summaries, feedback, incidents.

Writes:
- `reviews/weekly/<week-id>.md`
- `governance/next_actions.md`
- pending patches;
- investigation queue when cause is unclear.

Output:
- compact review, patches, next week focus, Direction OS output only if needed.

### `investigation`

Purpose:
- find the cause of a problem without turning every review into a huge chat.

Reads:
- the triggering review/incident;
- scoped logs and summaries.

Writes:
- `governance/investigation_queue.md`
- incident/review update;
- pending patches.

Output:
- cause hypothesis, evidence, next action, child-work CALL if needed.

Example triggers:
- weight not moving;
- plan not followed;
- food tracking incomplete;
- training skipped;
- pain/fatigue appears;
- sleep or recovery likely blocks progress;
- system too heavy to use.

### `research`

Purpose:
- check current external knowledge when a plan or decision depends on it.

Reads:
- owner context, current phase, exact research question.

Writes:
- `knowledge/research_briefs.md`
- pending patches if findings change procedures or plans.

Output:
- short brief with sources, owner applicability, freshness, and state implication.

## 6. Templates

### Recipe Card Template

```yaml
recipe_id:
name:
status: draft
servings:
ingredients:
  - item:
    amount:
    unit:
steps:
  - 
equipment:
prep_time:
cook_time:
nutrition_estimate:
  level: rough
  calories:
  protein:
  carbs:
  fat:
nutrition_confidence:
owner_fit_notes:
tags:
substitutions:
menu_refs:
feedback_history:
  - date:
    feedback:
    change:
export_targets:
  - target:
    status: none
source:
updated_at:
END_OF_RECORD: recipe-card
```

### Food Log Entry Template

```yaml
entry_id:
date:
time_or_meal_slot:
input_mode: text
owner_description:
followup_questions:
  - question:
    answered:
    answer:
skipped_questions:
estimated_foods:
  - food:
    portion_estimate:
    confidence:
plan_match:
same_day_advice:
confidence:
source_chat:
patches_proposed:
updated_at:
END_OF_RECORD: food-log-entry
```

### Weekly Plan Template

```yaml
week:
goal:
phase_ref:
assumptions:
nutrition_targets_level: rough
daily_menu:
  monday:
  tuesday:
  wednesday:
  thursday:
  friday:
  saturday:
  sunday:
meal_prep_plan:
fallback_meals:
shopping_notes:
recipe_refs:
training_activity_plan_ref:
owner_constraints:
missing_state:
confidence:
review_due:
updated_at:
END_OF_RECORD: weekly-plan
```

### Training Output Template

```yaml
date:
request:
plan_ref:
safety_status:
location_or_mode:
today_output:
  warmup:
  main_work:
  conditioning_or_activity:
  cooldown:
modifications:
fallback_if_low_energy:
stop_conditions:
after_session_log_prompt:
state_patch:
confidence:
updated_at:
END_OF_RECORD: training-output
```

### Weekly Review Template

```yaml
week:
goal_for_week:
data_completeness:
weight_trend_summary:
nutrition_summary:
training_summary:
activity_summary:
sleep_energy_recovery_summary:
adherence_summary:
what_worked:
what_failed:
root_cause_hypotheses:
investigations_opened:
patches_proposed:
next_week_focus:
direction_os_output:
  summary:
  problem:
  decision:
  call:
updated_at:
END_OF_RECORD: weekly-review
```

### Incident Template

```yaml
incident_id:
trigger:
severity:
area:
facts:
unknowns:
immediate_action:
investigation_needed:
patches_proposed:
medical_or_professional_escalation:
direction_os_output:
  summary:
  problem:
  decision:
  call:
updated_at:
END_OF_RECORD: incident
```

### Pending Patch Template

```yaml
patch_id:
target:
change:
reason:
source:
confidence:
owner_approval_required:
risk_level:
direction_os_escalation:
status: pending
updated_at:
END_OF_RECORD: pending-patch
```

## 7. Ordinary-Language Routing

The owner does not need to use packet formats.

Routing examples:
- "What should I do next?" -> `guidance`
- "Make a plan for the week" -> `weekly_planning`
- "Menu today?" -> `today_menu`
- "I ate this..." -> `food_log`
- "Add this recipe" -> `recipe`
- "Training today?" -> `today_training`
- "Review the week" -> `weekly_review`
- "Why is weight stuck?" -> `investigation`
- "What does current evidence say about X?" -> `research`

If a request spans multiple jobs, the current chat chooses one primary procedure and opens child work for the rest. One chat should not do an unbounded multi-procedure overhaul.

## 8. Direction OS Bridge

Health AI System sends to Direction OS only:
- compact review summary;
- strategic problem;
- owner decision needed;
- incident requiring direction-level attention;
- next CALL for a bounded session;
- evidence pointer to a work artifact.

Health AI System never sends to Direction OS:
- raw food-log entries;
- raw training sets;
- raw daily check-ins;
- raw activity streams;
- raw meal photos or descriptions;
- full app exports.

Direction OS examples:
- good: "weekly review found tracking friction; decision needed: simplify food logging vs add recipe workflow."
- bad: "Monday breakfast: eggs, rice, sauce, 312 g..."

## 9. Integrity Checks

Before any new chat gives advice, it should check:
- `STATE_INDEX.md` exists and is recent enough;
- current phase exists;
- safety state is not missing for training advice;
- active plan exists for today's menu/training, or missing-plan behavior is triggered;
- preferences are loaded before recipe/menu work;
- pending patches do not conflict with the requested answer;
- research brief is fresh enough when external knowledge affects the recommendation.

Before any weekly review closes:
- data completeness is stated;
- missing data is treated as evidence, not ignored;
- problems become investigations when cause is unclear;
- changes become pending patches;
- Direction OS output is compressed and excludes raw daily data.

## 10. What This Enables

This skeleton supports three modes at once:

1. Guided operating mode:
   - owner asks "what next?";
   - system reads phase, metrics, gaps, safety, and reviews;
   - system chooses the next best bounded action.

2. Procedure mode:
   - owner asks for menu, training, recipe, logging, review, or research;
   - system runs the matching procedure against stored state.

3. Team mode:
   - health director, nutrition lead, training coach, review analyst, researcher, and writer/operator are roles over the same source of truth;
   - provider can be ChatGPT, Codex, Claude Code, or another AI surface;
   - the state and procedures stay portable.

END_OF_FILE: work/health-ai-core-state-skeleton-v0.md
