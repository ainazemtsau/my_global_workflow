---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: receipt
  receipt_id: R-HB-H1-NUTRITION-PLAN-CREATE-2026-05-28
  status: committed
  owner: proof_carrying_workflow_os
---

# Receipt: R-HB-H1-NUTRITION-PLAN-CREATE-2026-05-28

```yaml
receipt_id: R-HB-H1-NUTRITION-PLAN-CREATE-2026-05-28
direction_id: health-and-beauty
target_obligation: O-HB-H1-NUTRITION-PLAN-CREATE
operator_invoked: ClarifyDesign / AskHumanDecision
commit_scope: hb_strategy_scope
status: committed
codex_handoff_id: CH-HB-H1-NUTRITION-PLAN-CREATE-COMMIT-2026-05-28

nutrition_plan_authority_artifact:
  artifact_id: HB-H1-NUTRITION-PLAN-AUTHORITY-CANDIDATE-2026-05-28
  authority_status: accepted_after_this_commit
  scope: nutrition_only_future_daily_ops_authority
  downstream_implementation_state: not_started
  excludes:
    - actual_meal_plan
    - recipes
    - shopping_list
    - training_plan
    - gym_schedule
    - cycling_prescription
    - Daily_Ops_implementation
    - ChatGPT_Project_setup
    - tracking_implementation
    - roadmap
    - Active_Frontier
    - Codex_product_execution
    - legacy_import

  objective:
    - create controlled energy deficit compatible with recovery, strength/function preservation, and adherence
    - use strict structure without starvation framing or crash-diet behavior
    - support low-friction ChatGPT-first tracking once implementation is separately admitted
    - repair deviations without compensatory fasting or punishment cardio

  baseline_inputs_used:
    age: 35
    sex: male
    height_cm: 182
    current_weight_kg: 125
    bmi_current_estimate: 37.7
    target_weight_context_kg: about_90
    chronic_conditions_reported: none_reported
    hypertension_reported: false
    cardiovascular_conditions_reported: false
    diabetes_reported: false
    injuries_or_specific_joint_limits: none_reported
    time_availability: high_for_about_6_months
    preferred_tracking_surface: ChatGPT_first
    accepted_tracking_modes:
      - photo
      - voice
      - short_text
    repeated_meals_allowed: true

  preserved_unknowns_not_waived:
    - waist_circumference
    - baseline_photos_or_body_measurements_policy
    - resting_blood_pressure
    - resting_heart_rate
    - recent_labs_or_medical_check_status
    - medication_status
    - exact_weekly_schedule_preference
    - exact_maximum_daily_tracking_minutes
    - preferred_meal_repetition_tolerance

  initial_target_bands:
    weight_trend_target:
      preferred_after_initial_adaptation: about_0_45_to_0_9_kg_per_week
      early_scale_noise_note: first two weeks may include water_glycogen_noise
      excessive_loss_gate: loss above about_1_percent_bodyweight_per_week_after_initial_adaptation_requires_review
    calories:
      initial_band_kcal_per_day: 2200_to_2600
      default_operational_start_kcal_per_day: about_2400
      lower_floor_without_medical_or_dietitian_review_kcal_per_day: 2000
      adjustment_increment_kcal_per_day: 150_to_250
    protein:
      target_g_per_day: 160_to_200
      caveat: revise_if_labs_medications_kidney_or_other_medical_issue_later_contraindicates
    fat:
      ordinary_minimum_g_per_day: about_60
    fiber:
      target_g_per_day: 30_to_45_gradual_build
    meal_pattern:
      planned_feedings_per_day: 3_to_4
      grazing_loop: not_allowed_as_default

  meal_architecture_contract:
    rule: future meals or menus must be generated from modules, not improvisation
    meal_module_requirements:
      - protein_anchor
      - high_volume_fiber_or_produce_anchor
      - controlled_energy_anchor_from_carbs_or_fats
      - optional_flavor_anchor
    allowed_design_patterns:
      - batch_prep
      - preweighed_portions
      - repeated_meals
      - simple_default_foods
    forbidden_by_this_receipt:
      - no actual menu created
      - no recipe list created
      - no shopping list created

  tracking_protocol_contract_not_implementation:
    minimum_food_event_log:
      - photo_or_voice_or_short_text
      - planned_vs_unplanned_tag
      - compliance_tag_on_plan_minor_deviation_major_deviation_unknown
      - hunger_or_energy_flag_only_when_abnormal
    review_data:
      - weight_trend_at_least_weekly
      - adherence_count_weekly
      - safety_flags
      - tracking_burden_check
    implementation_state: not_started
    exact_tracking_capacity: unknown_deferred

  review_and_adjustment_protocol:
    review_cadence: weekly
    adjustment_rule:
      - if_weight_loss_inside_target_and_adherence_stable_hold
      - if_loss_too_slow_for_two_consecutive_weeks_and_adherence_at_least_80_percent_reduce_150_to_250_kcal_or_tighten_portion_modules
      - if_loss_too_fast_after_initial_adaptation_or_symptoms_worsen_increase_150_to_250_kcal_or_pause_intensification
      - if_deviations_repeat_repair_structure_before_cutting_calories_harder

  deviation_repair_protocol:
    - log_deviation_once
    - return_to_next_planned_meal
    - no_compensatory_fasting
    - no_punishment_cardio
    - if_two_or_more_major_deviations_in_7_days_review_food_environment_hunger_sleep_stress_and_strictness

  escalation_triggers:
    hard_pause_or_review:
      - chest_pain
      - fainting
      - palpitations
      - severe_shortness_of_breath
      - serious_joint_pain
      - severe_insomnia
      - persistent_exhaustion
      - escalating_binge_like_behavior
      - discovered_abnormal_blood_pressure_or_medication_or_lab_issue_relevant_to_deficit_safety

claims_created_by_this_receipt:
  - claim_id: C-HB-H1-NUTRITION-PLAN-AUTHORITY-CREATED-2026-05-28
    type: nutrition_authority
    value: First bounded H1 nutrition plan authority artifact is created for future Daily Ops use.
  - claim_id: C-HB-H1-NUTRITION-INITIAL-TARGET-BANDS-DEFINED-2026-05-28
    type: nutrition_target_bands
    value: Initial calorie, protein, fiber, meal-pattern, and weight-trend authority bands are defined with safety gates.
  - claim_id: C-HB-H1-NUTRITION-MEAL-ARCHITECTURE-CONTRACT-DEFINED-2026-05-28
    type: nutrition_architecture
    value: Meal architecture contract is defined without creating a menu, recipes, or shopping list.
  - claim_id: C-HB-H1-NUTRITION-TRACKING-PROTOCOL-CONTRACT-DEFINED-NOT-IMPLEMENTED-2026-05-28
    type: tracking_contract_boundary
    value: Low-friction nutrition tracking protocol contract is defined but tracking implementation is not created.
  - claim_id: C-HB-H1-NUTRITION-REVIEW-AND-ESCALATION-GATES-DEFINED-2026-05-28
    type: review_and_safety_gate
    value: Weekly review, adjustment, deviation repair, and escalation gates are defined.
  - claim_id: C-HB-H1-NUTRITION-SAFETY-UNKNOWNS-PRESERVED-2026-05-28
    type: baseline_gate
    value: BP, HR, labs, medications, waist/photos policy, exact tracking capacity, and meal repetition tolerance unknowns remain not waived.
  - claim_id: C-HB-H1-DOWNSTREAM-IMPLEMENTATION-STILL-NOT-STARTED-AFTER-NUTRITION-PLAN-2026-05-28
    type: implementation_boundary
    value: Downstream Daily Ops implementation, ChatGPT Project setup, and tracking implementation remain not_started.

explicit_non_acceptance:
  - no training plan created
  - no gym schedule created
  - no cycling prescription created
  - no Daily Ops implementation created
  - no ChatGPT Project setup created
  - no tracking implementation created
  - no roadmap created
  - no Active Frontier selected
  - no Codex/product execution performed
  - no legacy import performed
  - no actual menu created
  - no recipes created
  - no shopping list created

context_authority_audit:
  accepted_ledger_state:
    - proof_state before this commit is h1_nutrition_plan_create_admitted_downstream_not_started
    - O-HB-H1-NUTRITION-PLAN-CREATE is open and admitted_not_started
    - downstream_implementation_state is not_started
    - baseline collection is accepted by R-HB-BASELINE-MEASUREMENTS-COLLECT-2026-05-28
    - first Program Blueprint is activated as limited authority for boundaries, gates, escalation, and Plan Authority Contract use
  committed_receipts:
    - R-HB-CONSTRAINTS-DEFINE-2026-05-26
    - R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27
    - R-HB-H1-FIRST-PROGRAM-BLUEPRINT-CREATE-2026-05-27
    - R-HB-H1-FIRST-PROGRAM-BLUEPRINT-ACTIVATE-FOR-DAILY-OPS-2026-05-27
    - R-HB-BASELINE-MEASUREMENTS-COLLECT-2026-05-28
    - R-HB-H1-AFTER-BASELINE-NEXT-BOUNDED-RUN-SELECT-2026-05-28
  current_human_input:
    - user requests O-HB-H1-NUTRITION-PLAN-CREATE only
    - user requires nutrition plan bounded to future Daily Ops authority artifact
    - user forbids training plan, gym schedule, cycling prescription, implementation, setup, tracking implementation, roadmap, Active Frontier, Codex/product execution, and legacy import
  external_reference_context:
    - CDC and NIDDK used as safety calibration only, not personal medical authority
  rejected_as_authority:
    - Project Files or uploads if stale against GitHub main
    - unknown BP/HR/labs/medications as waived
    - nutrition authority artifact as Daily Ops implementation
    - nutrition authority artifact as training plan
    - web references as accepted personal medical prescription

scope_audit:
  one_obligation_scope: passed
  in_scope_used:
    - create nutrition plan authority artifact
    - define target bands
    - define meal architecture contract
    - define tracking protocol contract without implementation
    - define review and escalation gates
    - preserve baseline safety unknowns
    - close O-HB-H1-NUTRITION-PLAN-CREATE as accepted
  parked_residual_context:
    - O-HB-H1-TRAINING-PLAN-CREATE
    - O-HB-H1-DAILY-OPS-IMPLEMENTATION-READINESS-DEFINE
    - O-HB-H1-DAILY-OPS-CHATGPT-PROJECT-SETUP
    - menu_generation
    - recipes
    - shopping_list
  blocked_or_forbidden_now:
    - training plan
    - gym schedule
    - cycling prescription
    - Daily Ops implementation
    - ChatGPT Project setup
    - tracking implementation
    - roadmap
    - Active Frontier
    - Codex/product execution
    - legacy import
  child_handoff_needed: false
  hidden_acceptance_check: passed

invariant_checks:
  receipt_marks_status_committed: passed
  target_obligation_recorded: passed
  operator_invoked_recorded: passed
  commit_scope_recorded: passed
  nutrition_plan_authority_artifact_created: passed
  safety_unknowns_preserved_not_waived: passed
  downstream_implementation_state_remains_not_started: passed
  no_training_plan_created: passed
  no_gym_schedule_created: passed
  no_cycling_prescription_created: passed
  no_daily_ops_implementation_created: passed
  no_chatgpt_project_setup_created: passed
  no_tracking_implementation_created: passed
  no_roadmap_created: passed
  no_active_frontier_selected: passed
  no_codex_product_execution: passed
  no_legacy_import: passed
  receipt_committed_to_ledger: passed_by_this_commit
```

END_OF_FILE: directions/health-and-beauty/workflow/receipts/R-HB-H1-NUTRITION-PLAN-CREATE-2026-05-28.md
