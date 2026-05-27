---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: receipt
  receipt_id: R-HB-H1-FIRST-PROGRAM-BLUEPRINT-CREATE-2026-05-27
  status: committed
  owner: proof_carrying_workflow_os
---

# Receipt: R-HB-H1-FIRST-PROGRAM-BLUEPRINT-CREATE-2026-05-27

```yaml
receipt_id: R-HB-H1-FIRST-PROGRAM-BLUEPRINT-CREATE-2026-05-27
direction_id: health-and-beauty
target_obligation: O-HB-H1-FIRST-PROGRAM-BLUEPRINT-CREATE
operator_invoked: ClarifyDesign / AskHumanDecision
commit_scope: hb_strategy_scope
status: committed
codex_handoff_id: CH-HB-H1-FIRST-PROGRAM-BLUEPRINT-CREATE-REPAIRED-2026-05-27

human_input_normalization:
  normalized_from_current_human_input: true
  record: >
    User agrees with the candidate Program Blueprint and clarifies that gym
    access is available as a future training option. The user bought a bicycle
    partly so travelling to the gym would be practical. User estimates the bike
    commute may be about 30 minutes one way. User does not require immediate gym
    use and does not ask for a training plan.

candidate_program_blueprint:
  blueprint_id: HB-H1-FIRST-PROGRAM-BLUEPRINT-CANDIDATE-2026-05-27
  blueprint_status: candidate_strategy_artifact
  daily_ops_authority_status: not_authority
  future_activation_requires_separate_workflow_receipt: true
  downstream_implementation_state: not_started

  scope:
    includes:
      - authority_and_scope_boundary
      - blueprint_level_objective
      - nutrition_blueprint_principles
      - training_blueprint_principles
      - available_training_surfaces
      - baseline_input_contract
      - review_gates
      - conversion_boundaries_for_future_plan_creation
    excludes:
      - actual_diet_plan
      - actual_nutrition_plan
      - meal_plan
      - recipes
      - shopping_list
      - calorie_prescription
      - macro_prescription
      - actual_training_plan
      - exercises_sets_reps_sessions
      - accepted_12_week_plan
      - annual_plan
      - Active_Frontier
      - roadmap
      - Daily_Ops_implementation
      - ChatGPT_Project_setup
      - tracking_implementation
      - Codex_product_execution
      - legacy_import

  nutrition_blueprint_principles:
    - future_nutrition_plan_must_create_controlled_deficit_compatible_with_recovery_safety_and_adherence
    - future_nutrition_plan_must_support_strength_preservation_satiety_and_behavioral_stability
    - menu_first_batch_prep_repeated_meals_and_preweighed_portions_are_allowed_as_future_design_patterns
    - future_nutrition_plan_must_include_deviation_repair_logic
    - future_tracking_should_be_low_friction_photo_voice_or_short_text_first
    - no_calories_macros_meals_recipes_shopping_lists_or_menus_are_created_by_this_receipt

  available_training_surfaces:
    - home_dumbbells
    - bodyweight_limited_currently
    - VR_boxing_or_Beat_Saber
    - bicycle
    - gym_access_via_bicycle_commute

  training_blueprint_principles:
    - future_training_must_account_for_deconditioning_current_bodyweight_joint_loading_and_available_equipment
    - future_training_must_prioritize_strength_and_function_preservation
    - future_cardio_work_must_be_progressive_and_joint_respectful
    - future_mobility_work_must_preserve_or_improve_range_and_function
    - future_training_must_include_recovery_and_stop_signal_logic
    - future_training_plan_may_use_gym_access_as_available_training_surface
    - gym_use_is_optional_and_not_immediate_requirement
    - bicycle_commute_to_gym_must_be_treated_as_possible_training_load_cardio_exposure_and_recovery_cost_in_future_plan
    - future_training_design_may_choose_home_based_gym_based_or_hybrid_training_but_this_receipt_does_not_select_between_them
    - no_exercises_sets_reps_sessions_weekly_split_progression_12_week_or_annual_plan_is_created_by_this_receipt

  baseline_input_contract:
    required_now_for_blueprint_creation:
      - accepted_root_objective
      - accepted_success_semantics
      - accepted_anthropometrics_35M_182cm_125kg
      - accepted_safety_override
      - accepted_behavioral_constraints
      - accepted_training_boundary
      - accepted_nutrition_boundary
      - accepted_low_friction_tracking_preference
      - accepted_program_blueprint_route
      - current_human_input_gym_access_available
      - current_human_input_bike_commute_to_gym_practically_available
      - current_human_input_bike_commute_estimated_about_30_minutes_one_way

    can_remain_unknown_now_but_must_be_recorded:
      - waist_circumference
      - resting_blood_pressure
      - resting_heart_rate
      - recent_labs_or_medical_check_status
      - medication_status
      - current_pain_injury_joint_limitations
      - baseline_strength_battery
      - baseline_cardio_test
      - baseline_mobility_checks
      - baseline_photos_or_body_measurements_policy
      - exact_weekly_schedule_preference
      - exact_maximum_daily_tracking_minutes
      - preferred_meal_repetition_tolerance
      - medical_professional_review_availability
      - exact_gym_distance
      - exact_bike_commute_duration_each_way
      - route_safety
      - bike_parking_lock_storage
      - weather_constraints
      - gym_membership_or_access_terms
      - gym_equipment_inventory
      - shower_or_change_facilities
      - whether_bike_commute_should_count_as_cardio_load
      - recovery_effect_of_bike_commute_plus_strength_training

    blocks_future_actual_prescription_until_resolved_or_explicitly_waived:
      - blood_pressure_or_medical_risk_baseline
      - medication_status
      - injury_or_joint_pain_status
      - strength_cardio_mobility_baselines
      - schedule_and_tracking_capacity
      - gym_commute_and_equipment_baseline_if_gym_based_or_hybrid_plan_is_selected

  review_gates:
    - gate_id: G0_AUTHORITY_GATE
      rule: Candidate blueprint cannot govern Daily Ops without future Workflow receipt.
    - gate_id: G1_MEDICAL_SAFETY_GATE
      rule: Safety symptoms, aggressive deficit/training, unknown BP/labs/medications, or escalating binge-like behavior require pause or escalation.
    - gate_id: G2_NUTRITION_PLAN_CONVERSION_GATE
      rule: Calories, macros, meals, menus, recipes, and shopping lists require separate future obligation and receipt.
    - gate_id: G3_TRAINING_PLAN_CONVERSION_GATE
      rule: >
        Exercises, sets, reps, split, cardio schedule, progression, 12-week or
        annual plan require separate future obligation and receipt. If a future
        training plan uses the gym, it must explicitly account for bicycle
        commute load, gym equipment availability, route safety, and recovery.
    - gate_id: G4_BASELINE_SUFFICIENCY_GATE
      rule: >
        Future prescription must resolve baseline inputs or explicitly record
        acceptable unknowns. Before gym-based or hybrid prescription, collect or
        explicitly waive exact commute duration/distance, route safety, gym
        equipment inventory, and expected recovery cost.
    - gate_id: G5_REVIEW_ESCALATION_GATE
      rule: Trainer or dietitian input is optional review/escalation, not authority by itself.
    - gate_id: G6_IMPLEMENTATION_GATE
      rule: Daily Ops files, trackers, dashboards, integrations, or ChatGPT Project setup require separate implementation-readiness obligation.

claims_accepted_by_this_receipt:
  - claim_id: C-HB-H1-FIRST-PROGRAM-BLUEPRINT-CANDIDATE-CREATED-2026-05-27
    type: candidate_blueprint
    value: Candidate first Program Blueprint is created as a strategy artifact.
  - claim_id: C-HB-H1-FIRST-PROGRAM-BLUEPRINT-BLUEPRINT-LEVEL-ONLY-2026-05-27
    type: scope_boundary
    value: Blueprint is structure/principles/gates only, not actual nutrition or training prescription.
  - claim_id: C-HB-H1-NUTRITION-PRINCIPLES-SEPARATED-FROM-PRESCRIPTION-2026-05-27
    type: nutrition_boundary
    value: Nutrition principles are separated from actual meal plan, calorie prescription, and macro prescription.
  - claim_id: C-HB-H1-TRAINING-PRINCIPLES-SEPARATED-FROM-PRESCRIPTION-2026-05-27
    type: training_boundary
    value: Training principles are separated from actual training plan, sessions, exercises, sets, reps, and progression.
  - claim_id: C-HB-H1-BASELINE-INPUTS-AND-REVIEW-GATES-DEFINED-2026-05-27
    type: baseline_and_review_gate_contract
    value: Baseline inputs and review gates are defined for future prescription and activation decisions.
  - claim_id: C-HB-H1-GYM-ACCESS-VIA-BIKE-COMMUTE-AVAILABLE-2026-05-27
    type: training_surface
    value: Gym access via bicycle commute is recorded as an available future training surface.
  - claim_id: C-HB-H1-GYM-BIKE-SURFACE-NOT-TRAINING-PRESCRIPTION-2026-05-27
    type: scope_boundary
    value: Gym access and bicycle commute are recorded as future design inputs only, not a training plan, schedule, or prescription.
  - claim_id: C-HB-H1-FIRST-PROGRAM-BLUEPRINT-NOT-DAILY-OPS-AUTHORITY-2026-05-27
    type: authority_boundary
    value: Candidate blueprint is not Daily Ops authority and requires future Workflow activation receipt.
  - claim_id: C-HB-H1-FIRST-PROGRAM-BLUEPRINT-DOWNSTREAM-IMPLEMENTATION-NOT-STARTED-2026-05-27
    type: implementation_boundary
    value: Downstream implementation remains not_started.

explicit_non_acceptance:
  - no actual diet plan accepted
  - no actual nutrition plan accepted
  - no meal plan accepted
  - no recipe system accepted
  - no shopping list accepted
  - no calorie prescription accepted
  - no macro prescription accepted
  - no actual training plan accepted
  - no gym schedule accepted
  - no gym frequency accepted
  - no cycling prescription accepted
  - no exercises_sets_reps_sessions accepted
  - no accepted 12-week plan created
  - no annual plan created
  - no Active Frontier selected
  - no roadmap created
  - no Daily Ops implementation created
  - no ChatGPT Project setup created
  - no tracking implementation created
  - no Codex/product execution performed
  - no legacy import performed

context_authority_audit:
  accepted_ledger_state:
    - proof_state before this commit is h1_program_blueprint_route_defined_downstream_not_started
    - H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP is selected
    - Minimal Daily Ops Core is accepted as operating shell only
    - Program Blueprint route is accepted as HYBRID_BASELINE_INFORMED_RESEARCHED_STARTER_BLUEPRINT
    - downstream_implementation_state is not_started
    - no execution obligations are admitted
  committed_receipts:
    - R-HB-CONSTRAINTS-DEFINE-2026-05-26
    - R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27
    - R-HB-H1-MINIMAL-DAILY-OPS-CORE-DEFINE-2026-05-27
    - R-HB-H1-PROGRAM-BLUEPRINT-DEFINE-2026-05-27
  current_human_input:
    - current handoff admits O-HB-H1-FIRST-PROGRAM-BLUEPRINT-CREATE
    - user agrees with the candidate blueprint
    - user clarifies gym access is available
    - user clarifies bicycle commute makes gym access practical
    - user estimates bicycle commute may be about 30 minutes one way
    - user does not require immediate gym use
  rejected_as_authority:
    - Hevy/apps/templates/HomeLab/Mealie/Miali/logs as program authority
    - external trainer/dietitian as hard authority requirement
    - gym availability as automatic training prescription
    - bicycle commute as automatic cardio prescription

scope_audit:
  one_obligation_scope: passed
  in_scope_used:
    - create candidate first Program Blueprint structure/content at blueprint level
    - separate nutrition principles from actual nutrition prescription
    - separate training principles from actual training prescription
    - record gym access via bicycle commute as available future training surface
    - define baseline input contract
    - define review gates
    - keep downstream implementation not_started
  parked_residual_context:
    - actual nutrition plan
    - actual meal plan
    - calorie and macro prescription
    - actual training plan
    - gym schedule
    - gym frequency
    - cycling schedule
    - 12-week plan
    - annual plan
    - Daily Ops implementation
    - ChatGPT Project setup
    - tracking implementation
  blocked_or_forbidden_now:
    - Active Frontier
    - roadmap
    - actual diet plan
    - actual nutrition plan
    - meal plan
    - calorie prescription
    - macro prescription
    - actual training plan
    - gym schedule
    - gym frequency
    - cycling prescription
    - accepted 12-week plan
    - annual plan
    - Daily Ops implementation
    - ChatGPT Project setup
    - tracking implementation
    - Codex/product execution
    - legacy import
  hidden_acceptance_check: passed

invariant_checks:
  receipt_marks_status_committed: passed
  target_obligation_recorded: passed
  operator_invoked_recorded: passed
  commit_scope_recorded: passed
  blueprint_level_only: passed
  nutrition_principles_separated_from_prescription: passed
  training_principles_separated_from_prescription: passed
  gym_recorded_as_option_not_requirement: passed
  bike_commute_recorded_as_future_training_load_factor: passed
  baseline_inputs_and_review_gates_defined: passed
  candidate_blueprint_not_daily_ops_authority: passed
  downstream_implementation_state_remains_not_started: passed
  no_active_frontier_selection: passed
  no_roadmap_created: passed
  no_execution_obligation_admitted: passed
  no_actual_diet_nutrition_meal_calorie_macro_or_training_plan_created: passed
  no_gym_schedule_or_cycling_prescription_created: passed
  no_12_week_or_annual_plan_created: passed
  no_daily_ops_implementation_created: passed
  no_chatgpt_project_setup_created: passed
  no_tracking_implementation_created: passed
  no_codex_product_execution: passed
  no_legacy_import: passed
  receipt_committed_to_ledger: passed_by_this_commit
```

END_OF_FILE: directions/health-and-beauty/workflow/receipts/R-HB-H1-FIRST-PROGRAM-BLUEPRINT-CREATE-2026-05-27.md
