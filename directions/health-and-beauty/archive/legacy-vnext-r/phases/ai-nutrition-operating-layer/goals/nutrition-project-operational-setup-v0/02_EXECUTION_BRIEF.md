# 02_EXECUTION_BRIEF — Project `Питание` clean rebuild after U1 failure

```yaml
artifact_control:
  artifact_name: "02_EXECUTION_BRIEF — Project `Питание` clean rebuild after U1 failure"
  schema: execution_brief.v2
  owner_layer: direction_goal
  status: formalized
  direction: directions/health-and-beauty
  phase_path: directions/health-and-beauty/phases/ai-nutrition-operating-layer
  goal_id: nutrition-project-operational-setup-v0
  goal_path: directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0
  formalized_by_stage: E1_EXECUTION_BRIEF
  formalized_at: "2026-05-20"
  correction_trigger: U1_REAL_UI_TEST_FAILED
  supersedes_prior_e1: true
  prior_c1_launch_invalidated: true
  selected_next_stage: C1_CODEX_GRAPH_PLAN
```

## Failure basis

The real U1/UI test failed.

```yaml
failure_basis:
  status: U1_REAL_UI_TEST_FAILED
  user_error: false
  project_setup_error: true
  observed_failure:
    - one_chat_collapse
    - premature_menu_generation
    - missing_chat_mode_routing
    - protocol_shifted_to_user_prompt
    - old_files_contaminated_architecture
  conclusion: "The old Project `Питание` setup is not repairable by cosmetic prompt patches."
```

## Supersession rule

```yaml
supersession:
  prior_e1_execution_brief: superseded
  prior_c1_launch_card: invalid_do_not_run
  old_nutrition_project_files: do_not_repair
  implementation_policy: clean_rebuild_from_scratch
  c1_must_plan_old_file_removal_or_supersession: true
```

## Accepted architecture

Project `Питание` is a repo-backed multi-chat operating loop.

```yaml
accepted_chat_topology:
  global_strategy_chat:
    lifecycle: first_setup_or_rare_repair_only
    closes_after: GLOBAL_NUTRITION_PLAN_saved
    purpose:
      - collect strategically necessary data
      - determine what evidence question must be researched
      - create DEEP_RESEARCH_REQUEST
      - synthesize Deep Research result into GLOBAL_NUTRITION_PLAN
    not_for:
      - weekly logistics
      - equipment/budget/menu details unless strategically relevant
      - concrete weekly menu
      - shopping list
      - prep plan

  weekly_planning_chat:
    lifecycle: one_week_only
    created_each_week: true
    closes_after: week_review_saved
    purpose:
      - read GLOBAL_NUTRITION_PLAN and history
      - create WEEKLY_PLAN for one week
      - create inputs for Menu Chat and Tracking Chat
      - later review WEEK_TRACKING_REPORT
      - save week result/history
    not_for:
      - concrete menu generation
      - shopping list
      - acting as a permanent weekly chat across weeks

  menu_chat:
    lifecycle: one_week_only
    created_each_week: true
    closes_after: week_menu_no_longer_active
    purpose:
      - read WEEKLY_PLAN
      - create concrete weekly menu
      - create shopping list
      - create prep plan
      - support menu edits during that week
    not_for:
      - global strategy
      - week review
      - tracking report

  tracking_chat:
    lifecycle: one_week_only
    created_each_week: true
    closes_after: WEEK_TRACKING_REPORT_created
    purpose:
      - read WEEKLY_PLAN and ACTIVE_WEEK_MENU
      - track food/photos/water/events during the week
      - estimate calories/BJU when required by the plan
      - ask missing questions until answered or explicitly declined
      - show current status and advice
      - create WEEK_TRACKING_REPORT at end of week
    not_for:
      - concrete menu generation
      - global strategy changes
      - durable GitHub write after every message by default
```

## Global Strategy Deep Research Gate

Global Strategy Chat must not directly finalize the optimal nutrition strategy before evidence pass.

```yaml
global_strategy_research_gate:
  required: true
  sequence:
    - strategic_intake
    - preliminary_strategy_hypothesis_if_useful
    - create_DEEP_RESEARCH_REQUEST
    - run_Deep_Research
    - synthesize_research_result
    - create_GLOBAL_NUTRITION_PLAN
    - save_to_GitHub
    - close_chat

  deep_research_request_must_include:
    - user_profile_summary
    - goal_and_constraints
    - acceptable_strictness
    - whether calories_or_BJU_or_named_diet_may_be_needed
    - foods_to_include_or_exclude_if_known
    - low_friction_requirement
    - research_objective
    - specific_research_questions
    - expected_output_format_for_strategy_synthesis

  global_strategy_chat_must_not:
    - finalize_diet_before_deep_research_when_first_setup_or_strategy_rebuild
    - generate_weekly_menu
    - generate_shopping_list
    - collect_week_specific_logistics_as_main_task
```

## Storage model

```yaml
storage_model:
  github:
    role: durable_source_of_truth_for_data_history_metrics_and_saved_results
    stores:
      - GLOBAL_NUTRITION_PLAN
      - user profile if needed
      - weekly plans
      - active menus
      - tracking reports
      - week reviews
      - metrics/progress/history
  project_files:
    role: runtime_cache_for_instructions_processes_prompts_and_formats
    stores:
      - Project Instructions
      - chat mode definitions
      - prepared prompts
      - output formats
      - save protocol
      - acceptance tests
  chat_memory:
    role: non_authoritative
```

## Tracking state rule

```yaml
tracking_state_rule:
  default_after_each_tracking_message:
    output:
      - food_or_event_estimate
      - current_day_status
      - pending_questions
      - advice_for_rest_of_day
    durable_github_update: false

  missing_data_policy:
    ask_until:
      - user_answers
      - user_explicitly_declines
    report_unlogged_or_unresolved_items: true

  full_export_required_when:
    - end_of_week
    - user_explicitly_requests_state_update
```

## Week lifecycle

```yaml
week_lifecycle:
  start:
    - create_new_weekly_planning_chat
    - read_global_plan_and_history
    - create_WEEKLY_PLAN
  menu:
    - create_new_menu_chat_for_same_week
    - create_ACTIVE_WEEK_MENU
    - edit_menu_during_week_if_needed
  tracking:
    - create_new_tracking_chat_for_same_week
    - track_week
    - create_WEEK_TRACKING_REPORT
  close:
    - return_to_weekly_planning_chat_for_that_week
    - review_tracking_report
    - save_week_result_and_history_to_GitHub
    - close_weekly_planning_chat
  next_week:
    - create_new_weekly_planning_chat
    - continue_from_GitHub_history_not_from_old_chat_memory
```

## C1 mission

C1 must plan a clean rebuild. It must not execute mutations.

```yaml
c1_mission:
  selected_next_stage: C1_CODEX_GRAPH_PLAN
  must_plan:
    - clean rebuild from scratch
    - old nutrition files removal_or_supersession
    - Project Instructions rewrite
    - Project Files process/prompt rewrite
    - GitHub durable state/history layout
    - Deep Research gate for Global Strategy Chat
    - one-week lifecycle for Weekly/Menu/Tracking chats
    - real short-start validation tests
    - C2 execution envelope
  must_not:
    - patch old protocol cosmetically
    - reuse old one-chat architecture
    - require user giant bootstrap prompts as normal UX
    - generate live diet/menu
    - route to R1 before evidence
```

## Required real-start acceptance tests

```yaml
acceptance_tests:
  global_strategy_first_start:
    prompt: "Режим: Global Strategy Chat. Первый запуск."
    pass_if:
      - collects_strategic_data
      - prepares_DEEP_RESEARCH_REQUEST
      - does_not_finalize_global_plan_before_research
      - does_not_generate_menu
    fail_if:
      - asks_weekly_logistics_as_main_task
      - generates_week_menu
      - skips_research_gate

  weekly_planning_start:
    prompt: "Режим: Weekly Planning Chat. Создаём план недели."
    pass_if:
      - creates_plan_for_one_week
      - reads_global_plan_and_history
      - outputs_WEEKLY_PLAN
      - gives_inputs_for_Menu_and_Tracking
      - does_not_generate_concrete_menu
    fail_if:
      - behaves_as_permanent_weekly_chat
      - starts_from_zero_when_history_exists
      - generates_shopping_list_or_concrete_meals

  menu_chat_start:
    prompt: "Режим: Menu Chat. Создаём меню на неделю по WEEKLY_PLAN."
    pass_if:
      - requires_WEEKLY_PLAN
      - creates_concrete_menu
      - creates_shopping_list
      - creates_prep_plan
      - supports_edits_for_current_week
    fail_if:
      - rebuilds_global_strategy
      - performs_week_review
      - ignores_weekly_plan

  tracking_chat_start:
    prompt: "Режим: Tracking Chat. Начинаем неделю по WEEKLY_PLAN и ACTIVE_WEEK_MENU."
    pass_if:
      - tracks_food_photos_water_events
      - estimates_calories_BJU_when_required
      - keeps_pending_questions_until_answered_or_declined
      - gives_status_and_advice
      - creates_WEEK_TRACKING_REPORT_at_end
    fail_if:
      - generates_menu
      - forgets_missing_questions
      - requires_heavy_manual_tracker
      - writes_large_state_update_after_every_message_by_default

  week_close:
    prompt: "Режим: Weekly Planning Chat. Закрываем неделю по WEEK_TRACKING_REPORT."
    pass_if:
      - reviews_tracking_report
      - reports_unlogged_or_unresolved_items
      - saves_week_result_history_and_progress
      - prepares_next_week_inputs
      - closes_week_chat
    fail_if:
      - starts_next_week_in_same_chat
      - generates_menu
      - does_not_save_result
```

## Scope cuts

```yaml
scope_cuts:
  - no_macrofactor_revival
  - no_training_cardio_recovery_supplements_expansion
  - no_clinical_medical_nutrition_protocol
  - no_full_food_database
  - no_hidden_memory_as_state
  - no_one_chat_does_everything_default
  - no_old_file_salvage
```

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/02_EXECUTION_BRIEF.md`
