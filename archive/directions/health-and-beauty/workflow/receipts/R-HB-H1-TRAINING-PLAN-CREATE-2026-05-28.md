---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: receipt
  receipt_id: R-HB-H1-TRAINING-PLAN-CREATE-2026-05-28
  status: committed
  owner: proof_carrying_workflow_os
---

# Receipt: R-HB-H1-TRAINING-PLAN-CREATE-2026-05-28

```yaml
receipt_id: R-HB-H1-TRAINING-PLAN-CREATE-2026-05-28
direction_id: health-and-beauty
target_obligation: O-HB-H1-TRAINING-PLAN-CREATE
operator_invoked: ClarifyDesign / AskHumanDecision
commit_scope: hb_strategy_scope
status: committed
codex_handoff_id: CH-HB-H1-TRAINING-PLAN-CREATE-COMMIT-REVISED-2026-05-28

human_input_normalization:
  normalized_from_current_human_input: true
  record: >
    User clarifies that he should not be treated as a complete beginner.
    User reports lifelong sport background including childhood judo,
    wrestling/grappling, gym training, muay thai/striking, and broad
    sport exposure. User reports prior home strength training around
    4 times per week plus cardio exposure, with fatigue but not
    week-destroying collapse. User reports readiness for meaningfully
    hard training and refers to hardness preference 5. This receipt
    therefore frames the training authority as experienced-returner,
    assertive-but-gated progression rather than conservative
    beginner ramp, while preserving safety, joint-load, recovery,
    nutrition, and gym/bike gates.

training_plan_authority_artifact:
  artifact_id: HB-H1-TRAINING-PLAN-AUTHORITY-CANDIDATE-2026-05-28
  authority_status: accepted_after_this_commit
  scope: training_only_future_daily_ops_authority
  downstream_implementation_state: not_started
  excludes:
    - Daily_Ops_implementation
    - ChatGPT_Project_setup
    - tracking_implementation
    - Hevy_setup_or_tool_authority
    - gym_schedule
    - cycling_prescription
    - exact_exercises
    - sets
    - reps
    - weekly_calendar
    - accepted_12_week_plan
    - annual_plan
    - roadmap
    - Active_Frontier
    - Codex_product_execution
    - legacy_import

  training_readiness_profile:
    status: experienced_returner_not_zero_start
    current_state: temporarily_detrained_high_bodyweight_low_recent_training
    user_reported_background:
      - lifelong_sport_exposure
      - childhood_judo
      - wrestling_or_grappling_background
      - gym_training
      - muay_thai_or_striking_experience
      - prior_home_strength_training_about_4_times_per_week
      - cardio_exposure
    user_reported_hardness_preference:
      value: 5
      interpretation: ready_for_meaningfully_hard_training_with_gates
    authority_implication:
      - do_not_treat_user_as_complete_beginner
      - allow_challenging_training_dose_if_recovery_and_safety_gates_pass
      - preserve_high_bodyweight_joint_load_and_BP_HR_labs_medications_unknowns_as_gates

  objective:
    - preserve_or_minimize_loss_of_strength_function_and_mobility_during_weight_loss
    - rebuild_conditioning_after_low_recent_training_without_zero_start_framing
    - support_recovery_under_accepted_nutrition_deficit_authority
    - create_training_authority_boundaries_for_future_daily_ops_without_implementation

  baseline_inputs_used:
    age: 35
    sex: male
    height_cm: 182
    current_weight_kg: 125
    bmi_current_estimate: 37.7
    target_weight_context_kg: about_90
    reported_chronic_conditions: none_reported
    hypertension_reported: false
    cardiovascular_conditions_reported: false
    diabetes_reported: false
    injuries_or_specific_joint_limits: none_reported
    recent_training: very_low_last_week
    current_steps: low
    prior_training_experience:
      - strength_training
      - VR_boxing
      - Beat_Saber
      - cardio
      - P90X
      - judo
      - martial_arts
      - gym_training
      - muay_thai_or_striking
      - wrestling_or_grappling
    current_pushups_estimate: about_10
    pullups_now: not_preferred_due_current_bodyweight
    time_availability: high_for_about_6_months
    preferred_tracking_surface: ChatGPT_first_low_manual_burden

  preserved_unknowns_not_waived:
    - waist_circumference
    - baseline_photos_or_body_measurements_policy
    - resting_blood_pressure
    - resting_heart_rate
    - recent_labs_or_medical_check_status
    - medication_status
    - formal_strength_battery
    - formal_cardio_test
    - formal_mobility_checks
    - exact_weekly_schedule_preference
    - exact_maximum_daily_tracking_minutes
    - exact_gym_distance
    - exact_bike_commute_duration_each_way
    - route_safety
    - bike_parking_lock_storage
    - weather_constraints
    - gym_membership_or_access_terms
    - gym_equipment_inventory
    - shower_or_change_facilities

  training_load_mode:
    default_mode: assertive_returner_mode
    fallback_mode: conservative_rebuild_mode
    assertive_returner_mode_conditions:
      - no_red_flag_symptoms
      - joint_pain_not_worsening
      - sleep_and_energy_stable_enough
      - soreness_resolves_normally
      - nutrition_adherence_not_collapsing_from_training_fatigue
      - bike_or_VR_conditioning_not_interfering_with_strength_recovery
    assertive_returner_mode_allows:
      - three_to_four_strength_exposures_per_week_future_envelope
      - two_to_four_conditioning_exposures_per_week_future_envelope
      - RPE_6_to_8_normal_training
      - occasional_hard_conditioning_or_VR_work_if_recovery_stable
      - gym_hybrid_plan_if_gym_bike_gate_resolved
    conservative_rebuild_mode_triggers:
      - persistent_joint_pain
      - unusual_shortness_of_breath
      - poor_recovery_across_multiple_sessions
      - excessive_fatigue_under_nutrition_deficit
      - sleep_deterioration
      - repeated_training_related_food_deviations
      - bike_commute_creates_unexpected_recovery_cost

  training_structure_contract_not_schedule:
    strength_resistance:
      authority_band: 3_to_4_exposures_per_week_future_plan_envelope
      starting_default_if_recovery_unknown: 3_exposures_per_week
      upper_bound_if_recovery_stable: 4_exposures_per_week
      prescription_status: no_calendar_no_exercises_no_sets_no_reps_no_split
      intensity_boundary:
        normal_work: RPE_6_to_8
        occasional_top_sets: RPE_8_allowed_if_technique_clean_and_no_warning_flags
        failure_training: not_default_gated
      volume_boundary:
        - enough_to_be_challenging
        - not_bodybuilding_style_exhaustion_by_default
        - no_large_volume_jumps_week_to_week
      movement_families_allowed_for_future_generation:
        - squat_or_lower_pattern_scaled
        - hinge_pattern_scaled
        - push_pattern_scaled
        - pull_pattern_scaled
        - carry_core_or_bracing_pattern_scaled

    conditioning:
      authority_band: 2_to_4_exposures_per_week_future_plan_envelope
      prescription_status: no_cardio_schedule_no_cycling_prescription
      includes:
        - low_impact_zone_2_or_moderate_cardio
        - VR_boxing_or_Beat_Saber_as_conditioning_surface
        - bicycle_as_transport_or_cardio_surface
        - optional_gym_machine_conditioning_if_gym_or_hybrid_selected
      intensity_boundary:
        moderate_work: default
        vigorous_intervals: allowed_later_if_joint_recovery_and_breathing_tolerance_pass
        hard_striking_or_VR_sessions: count_as_real_training_load

    mobility_function:
      authority_band: 3_to_6_short_exposures_per_week_future_plan_envelope
      prescription_status: no_specific_mobility_routine_created
      role: keep_body_functional_under_strength_cardio_and_weight_loss_load
      focus_areas:
        - hips
        - ankles
        - thoracic_spine
        - shoulders
        - trunk_control

    recovery:
      rule: progression_subordinate_to_recovery_safety_and_nutrition_tolerance
      rest_or_low_load_exposures: required_in_future_plan_but_not_scheduled_here

  progression_boundaries:
    - progress_only_one_major_variable_at_a_time
    - allow_assertive_progression_but_not_unbounded_escalation
    - no_max_testing_until_gates_resolved_or_explicitly_accepted
    - failure_training_not_default_and_requires_later_review
    - no_high_impact_running_jumping_or_aggressive_intervals_initially_without_joint_tolerance
    - hard_VR_or_striking_work_counts_as_training_load
    - hold_or_regress_if_joint_pain_fatigue_sleep_or_recovery_worsens
    - do_not_use_training_as_punishment_for_nutrition_deviation
    - do_not_cut_calories_harder_instead_of_repairing_training_recovery_structure

  gym_bike_boundary:
    gym_access_via_bicycle_commute: optional_future_training_surface
    gym_required: false
    bicycle_commute: possible_cardio_load_and_recovery_cost
    forced_schedule_created: false
    cycling_prescription_created: false
    future_gym_or_hybrid_plan_requires:
      - exact_commute_duration_or_explicit_waiver
      - route_safety_or_explicit_waiver
      - gym_equipment_inventory_or_explicit_waiver
      - recovery_cost_accounted_for
      - no_double_counting_bike_as_free_extra_load

  nutrition_authority_interlock:
    accepted_nutrition_authority_used_as_boundary: true
    training_progression_must_respect:
      - calorie_band_and_recovery_tolerance
      - protein_support_boundary
      - weekly_review_and_escalation_gates
      - no_compensatory_fasting
      - no_punishment_cardio
      - symptoms_or_excessive_weight_loss_pause_intensification

  review_gates:
    - gate_id: G0_AUTHORITY_GATE
      rule: Training authority artifact becomes accepted only after Verify + Commit.
    - gate_id: G1_MEDICAL_SAFETY_GATE
      rule: BP/HR/labs/medications unknowns are preserved and trigger review if abnormal or relevant.
    - gate_id: G2_BASELINE_MOVEMENT_GATE
      rule: Strength/cardio/mobility baselines remain deferred/gated and must inform future exact prescription.
    - gate_id: G3_WEEKLY_TRAINING_REVIEW_GATE
      rule: Review adherence, RPE, soreness, joint pain, energy, sleep, recovery, weight trend, and deviation pressure.
    - gate_id: G4_GYM_BIKE_GATE
      rule: Gym or hybrid plan must resolve gym/bike practicals or explicitly record acceptable unknowns.
    - gate_id: G5_NUTRITION_RECOVERY_INTERLOCK
      rule: Training load cannot be intensified to compensate for nutrition deviations or excessive deficit effects.
    - gate_id: G6_IMPLEMENTATION_GATE
      rule: Daily Ops files, trackers, templates, integrations, Hevy setup, or ChatGPT Project setup require separate admitted implementation/readiness obligation.

  escalation_triggers:
    hard_pause_or_medical_review:
      - chest_pain
      - fainting
      - palpitations
      - severe_or_unusual_shortness_of_breath
      - neurological_symptoms
      - sharp_worsening_or_persistent_joint_pain
      - acute_injury
      - discovered_abnormal_blood_pressure_heart_rate_labs_or_medication_issue
      - persistent_exhaustion
      - severe_insomnia
      - recovery_collapse
    training_review_or_regression:
      - soreness_repeatedly_impairs_normal_movement
      - rising_joint_pain_across_sessions
      - inability_to_recover_between_exposures
      - unusual_fatigue_on_accepted_nutrition_targets
      - repeated_deviations_driven_by_hunger_or_fatigue
      - weight_loss_faster_than_nutrition_review_boundary
      - bike_commute_interferes_with_strength_or_recovery

  future_daily_ops_training_event_contract_not_implementation:
    status: contract_only
    implementation_created: false
    future_minimal_fields:
      - training_surface
      - exposure_type_strength_cardio_mobility_recovery
      - duration_band_or_completed_flag
      - RPE_or_talk_test_flag
      - pain_or_joint_flag
      - energy_recovery_flag
      - notes_only_if_abnormal

claims_created_by_this_receipt:
  - claim_id: C-HB-H1-TRAINING-PLAN-AUTHORITY-CREATED-2026-05-28
    type: training_authority
    value: First bounded H1 training plan authority artifact is created for future Daily Ops use.
  - claim_id: C-HB-H1-TRAINING-READINESS-PROFILE-EXPERIENCED-RETURNER-2026-05-28
    type: training_readiness_profile
    value: User is treated as experienced returner with temporarily reduced current conditioning, not complete beginner; training authority allows assertive hard-but-gated progression.
  - claim_id: C-HB-H1-TRAINING-STRUCTURE-CONTRACT-DEFINED-2026-05-28
    type: training_structure_contract
    value: Strength, conditioning, mobility, and recovery authority structure is defined without exact exercises, schedule, sets, reps, split, or implementation.
  - claim_id: C-HB-H1-TRAINING-ASSERTIVE-GATED-PROGRESSION-DEFINED-2026-05-28
    type: progression_boundary
    value: Training authority allows assertive progression for an experienced returner, bounded by safety, joint-load, recovery, nutrition interlock, and gym/bike gates.
  - claim_id: C-HB-H1-TRAINING-GYM-BIKE-OPTIONAL-LOAD-BOUNDARY-DEFINED-2026-05-28
    type: optional_training_surface_boundary
    value: Gym access via bicycle commute is handled as optional training surface and possible load/recovery factor, not forced schedule or cycling prescription.
  - claim_id: C-HB-H1-TRAINING-REVIEW-AND-ESCALATION-GATES-DEFINED-2026-05-28
    type: review_and_safety_gate
    value: Training review gates and escalation triggers are defined.
  - claim_id: C-HB-H1-TRAINING-SAFETY-UNKNOWNS-PRESERVED-2026-05-28
    type: baseline_gate
    value: BP, HR, labs, medications, formal movement checks, and gym/bike practical unknowns remain not waived.
  - claim_id: C-HB-H1-DOWNSTREAM-IMPLEMENTATION-STILL-NOT-STARTED-AFTER-TRAINING-PLAN-2026-05-28
    type: implementation_boundary
    value: Daily Ops implementation, ChatGPT Project setup, tracking implementation, roadmap, Active Frontier, Codex/product execution, and legacy import remain not_started/not_performed.

explicit_non_acceptance:
  - no Daily Ops implementation created
  - no ChatGPT Project setup created
  - no tracking implementation created
  - no Hevy setup created
  - no Hevy or tool authority created
  - no gym schedule created
  - no cycling prescription created
  - no exact exercises created
  - no sets created
  - no reps created
  - no weekly calendar created
  - no accepted 12-week plan created
  - no annual plan created
  - no roadmap created
  - no Active Frontier selected
  - no Codex/product execution performed
  - no legacy import performed

context_authority_audit:
  accepted_ledger_state:
    - GitHub main proof_state before this run is h1_training_plan_create_admitted_downstream_not_started.
    - O-HB-H1-TRAINING-PLAN-CREATE is next_admitted_obligation and open/admitted_not_started.
    - downstream_implementation_state is not_started.
    - nutrition_plan_authority is accepted.
    - no execution Obligations are admitted.
    - no CodexExecution operator may run.
  committed_receipts:
    - R-HB-H1-FIRST-PROGRAM-BLUEPRINT-CREATE-2026-05-27
    - R-HB-H1-FIRST-PROGRAM-BLUEPRINT-ACTIVATE-FOR-DAILY-OPS-2026-05-27
    - R-HB-BASELINE-MEASUREMENTS-COLLECT-2026-05-28
    - R-HB-H1-NUTRITION-PLAN-CREATE-2026-05-28
    - R-HB-H1-AFTER-NUTRITION-NEXT-BOUNDED-RUN-SELECT-2026-05-28
  current_human_input:
    - User targets Health and Beauty O-HB-H1-TRAINING-PLAN-CREATE only.
    - User requires GitHub main as source of truth and treats uploaded files as possibly stale.
    - User clarifies experienced returner / not zero-start profile and readiness for harder training.
    - User requires gym access via bicycle commute to be optional surface/load factor, not forced schedule or cycling prescription.
    - User forbids Daily Ops implementation, ChatGPT Project setup, tracking implementation, roadmap, Active Frontier, Codex/product execution, and legacy import.
  rejected_as_authority:
    - Project Files or uploads if stale against GitHub main.
    - unknown BP/HR/labs/medications as waived.
    - high motivation as permission for unbounded training load.
    - gym access as required gym schedule.
    - bicycle commute as cycling prescription.
    - Hevy or any tool as program authority.
    - training authority artifact as Daily Ops implementation.

scope_audit:
  one_obligation_scope: passed
  in_scope_used:
    - create first bounded H1 training plan authority artifact
    - preserve baseline safety gates and unknowns
    - use accepted nutrition authority only as boundary/interlock
    - define experienced-returner assertive-but-gated training readiness profile
    - define training principles, structure, progression boundaries, review gates, and escalation triggers
    - keep gym/bike optional and non-prescriptive
  parked_residual_context:
    - Daily Ops implementation readiness
    - ChatGPT Project setup
    - tracking implementation
    - exact training session generation
    - exact exercise selection
    - Hevy setup
  blocked_or_forbidden_now:
    - Daily Ops implementation
    - ChatGPT Project setup
    - tracking implementation
    - roadmap
    - Active Frontier
    - Codex/product execution
    - legacy import
  hidden_acceptance_check: passed

invariant_checks:
  target_obligation_only: passed
  operator_recorded: passed
  training_authority_created: passed
  experienced_returner_profile_recorded: passed
  assertive_gated_progression_defined: passed
  safety_gates_preserved: passed
  gym_bike_optional_not_prescription: passed
  nutrition_boundary_preserved: passed
  downstream_implementation_not_started: passed
  no_daily_ops_implementation: passed
  no_chatgpt_project_setup: passed
  no_tracking_implementation: passed
  no_roadmap: passed
  no_active_frontier: passed
  no_codex_product_execution: passed
  no_legacy_import: passed
```

END_OF_FILE: directions/health-and-beauty/workflow/receipts/R-HB-H1-TRAINING-PLAN-CREATE-2026-05-28.md
