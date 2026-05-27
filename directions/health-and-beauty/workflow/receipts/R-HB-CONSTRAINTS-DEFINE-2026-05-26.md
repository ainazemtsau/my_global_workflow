---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: receipt
  receipt_id: R-HB-CONSTRAINTS-DEFINE-2026-05-26
  status: committed
  owner: proof_carrying_workflow_os
---

# Receipt: R-HB-CONSTRAINTS-DEFINE-2026-05-26

```yaml
receipt_id: R-HB-CONSTRAINTS-DEFINE-2026-05-26
direction_id: health-and-beauty
target_obligation: O-HB-CONSTRAINTS-DEFINE
operator_invoked: ClarifyConstraints
commit_scope: hb_root_scope
status: committed

human_decision:
  normalized_from_unstructured_input: true
  constraints_summary: >
    Пользователь 35 лет, мужчина, рост 182 см, текущий вес 125 кг.
    Желаемая практическая цель по текущему вводу: около 90 кг, то есть
    примерно -35 кг. Это является candidate objective delta, а не
    автоматическим изменением accepted root objective. Пользователь хочет
    максимальную жёсткость, строгие правила, понятное меню, понятные
    тренировки, ChatGPT-first tracking через фото/голос/текст, минимум
    ручного логирования, batch-prep/preweighed portions, и готов высоко
    нагружаться при наличии структуры.

anthropometrics:
  age: 35
  sex: male
  height_cm: 182
  current_weight_kg: 125
  bmi_current_estimate: 37.7
  accepted_root_objective_delta_kg: -25
  candidate_corrected_goal_delta_kg: -35
  candidate_target_weight_kg: 90
  bmi_at_candidate_target_estimate: 27.2
  objective_delta_status: candidate_only_not_accepted_root_objective

health_constraints:
  chronic_conditions_reported: none
  hypertension_reported: false
  cardiovascular_conditions_reported: false
  diabetes_reported: false
  medical_check_or_recent_labs: unknown
  medications: unknown
  injuries_or_specific_joint_limits: none_reported
  safety_override: >
    High strictness is allowed only inside health and recovery boundaries:
    no starvation framing, no reckless crash-diet target, no ignoring chest
    pain, fainting, palpitations, severe shortness of breath, escalating binge
    behavior, serious joint pain, severe insomnia, or persistent exhaustion.
    Medical baseline review is recommended before aggressive multi-training
    or extreme calorie restriction.

behavioral_constraints:
  possible_disordered_eating_pattern: >
    User reports that after breakfast he may start repeatedly going to the
    kitchen. No formal eating disorder diagnosis is claimed. Pattern improves
    when there is a clear goal, clear menu, clear training, and structure.
  deviation_risk: high_when_plan_breaks
  required_structure: very_high
  preferred_rules: strict
  preferred_strictness_1_to_5: 5
  fatigue_tolerance: high
  fallback_requirement: >
    Future plans must include fallback behavior for deviations because
    unplanned changes create high relapse/snvack risk.

activity_constraints:
  current_steps: low
  recent_training: very_low_last_week
  prior_training: >
    Previously roughly four strength sessions per week plus VR, boxing,
    Beat Saber, cardio; prior experience with P90X, judo, and other martial arts.
  current_pushups_estimate: about_10
  pullups_now: not_preferred_due_current_bodyweight
  cardio_options:
    - VR
    - boxing_or_Beat_Saber
    - bicycle_planned
  mobility: historically_good_but_current_abdominal_mass_limits
  training_safety: >
    Future training plan must account for deconditioning, current 125 kg bodyweight,
    joint loading, limited current bodyweight strength, and available dumbbells.

resource_constraints:
  time_availability: high_for_about_6_months
  budget: flexible_if_needed
  equipment:
    - dumbbells_22_to_24_kg
    - Apple_Watch
    - body_weight_scale
    - kitchen_scale
    - air_fryer
    - multicooker
    - oven
    - pots_pans
  no_microwave: true
  apps_owned:
    - Heavy_annual_subscription

nutrition_constraints:
  allergies: none
  dietary_restrictions: none
  disliked_foods: none_reported
  restaurant_delivery_frequency: rare_about_once_per_two_weeks_or_less
  alcohol: near_none_about_once_per_half_year
  cooking_capacity: high
  preferred_food_system:
    - menu_first
    - batch_prep
    - preweighed_portions
    - repeated_meals_allowed
  detailed_daily_weighing_preference: low
  detailed_weighing_possible_if_needed: true
  hunger_tolerance_when_structured: high

tracking_constraints:
  preferred_surface: ChatGPT_first
  accepted_tracking_modes:
    - photo
    - voice
    - short_text
  manual_tracking_burden: minimize
  cloud_privacy_restrictions: none_reported
  candidate_tools:
    - ChatGPT_Project
    - Google_Sheets_or_simple_tables
    - Heavy_for_strength
    - Apple_Watch
    - Notion_candidate_only
    - GitHub_candidate_only
  note: >
    Tool mentions are candidate context only. No tracking implementation is
    authorized by this receipt.

objective_delta_detected:
  accepted_root_objective_current: "-25 kg weight loss"
  current_human_input_candidate_delta: "-35 kg weight loss from 125 kg to about 90 kg"
  required_followup_obligation: O-HB-ROOT-OBJECTIVE-AMEND-TO-35KG
  rule: >
    Do not silently mutate accepted root objective. Resolve objective delta
    through explicit amendment receipt before final success semantics.

constraints_accepted_by_this_receipt:
  - constraint_id: C-HB-CONSTRAINT-ANTHROPOMETRIC-BASELINE-2026-05-26
    type: baseline
    value: "35M, 182 cm, 125 kg, BMI estimate 37.7; candidate target 90 kg / -35 kg pending root objective amendment."
  - constraint_id: C-HB-CONSTRAINT-SAFETY-OVERRIDE-2026-05-26
    type: safety
    value: "High strictness allowed only with medical/recovery stop boundaries and no reckless crash-diet or overtraining framing."
  - constraint_id: C-HB-CONSTRAINT-STRICT-STRUCTURE-2026-05-26
    type: behavior
    value: "Strict rules, clear menu, clear schedule, fallback protocol, and batch-prep are required due high deviation/snvack risk when plan breaks."
  - constraint_id: C-HB-CONSTRAINT-LOW-FRICTION-TRACKING-2026-05-26
    type: tracking
    value: "ChatGPT-first tracking via photo/voice/text with low manual burden; detailed weighing only when systemically simplified."
  - constraint_id: C-HB-CONSTRAINT-TRAINING-BASELINE-2026-05-26
    type: training_boundary
    value: "Future training must account for low current steps, recent detraining, current bodyweight, available dumbbells, VR/cardio options, and planned bicycle."
  - constraint_id: C-HB-CONSTRAINT-RESOURCE-ABUNDANCE-2026-05-26
    type: resource
    value: "High time availability for about six months, flexible budget, home equipment and cooking tools sufficient for a structured plan."
  - constraint_id: C-HB-CONSTRAINT-FOOD-FLEXIBILITY-2026-05-26
    type: nutrition_boundary
    value: "No allergies, dietary restrictions, disliked foods, frequent delivery dependency, or meaningful alcohol pattern reported."

unresolved_items:
  - waist_circumference
  - resting_blood_pressure_recent_measurement
  - resting_heart_rate_from_Apple_Watch
  - recent_labs_or_medical_check
  - medication_status_confirmed
  - exact weekly schedule preference
  - exact maximum daily tracking minutes
  - whether medical professional review is available
  - baseline photos_or_body_measurements_policy
  - preferred meal repetition tolerance

context_authority_audit:
  accepted_ledger_state:
    - root objective accepted at -25 kg via R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26
    - O-HB-CONSTRAINTS-DEFINE open and unblocked before this receipt
  committed_receipt:
    - R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26
  current_human_input:
    - user provided constraints intake in natural language
    - user corrected practical target from -25 kg to about -35 kg
    - user prefers maximum strictness and strict rules
    - user prefers ChatGPT-first tracking and low manual burden
  external_reference_context:
    - CDC/NIDDK/WHO general safety reference only, not accepted personal plan
  projection_context:
    - Dashboard forbids diet/training prescription as accepted plan and forbids product/project implementation
  candidate_context:
    - Notion/GitHub/ChatGPT Project integration
    - future bike purchase
    - future fast-start protocol
    - future menu/training design
  instruction_context:
    - Atomic run and one Obligation scope
    - candidate state until Verify + Commit
  unknown:
    - medical baseline data
    - waist
    - labs
    - exact maximum tracking time
    - blood pressure reading

scope_audit:
  one_obligation_scope: passed
  in_scope_used:
    - hard constraints
    - capacity/time/budget/resources
    - health and risk boundaries
    - tracking/privacy boundaries
    - human input normalization
  parked_residual_context:
    - diet prescription
    - training plan
    - fast-start protocol
    - ChatGPT/Notion/GitHub tracking implementation
    - research on optimal diet/training
    - roadmap
  residual_obligations:
    - obligation_id: O-HB-ROOT-OBJECTIVE-AMEND-TO-35KG
      status: should_open
      reason: current human input changes target delta from accepted -25 kg to candidate -35 kg
    - obligation_id: O-HB-SUCCESS-SEMANTICS-DEFINE
      status: already_open
      reason: measurable targets, pace, stop conditions, adherence metrics, strength/mobility metrics still needed
    - obligation_id: O-HB-BASELINE-MEASUREMENTS-COLLECT
      status: proposed_only_not_admitted
      reason: waist, BP, resting HR, labs/checkup status would improve safety and measurement quality
    - obligation_id: O-HB-TRACKING-LAYER-DESIGN
      status: proposed_only_not_admitted
      reason: future ChatGPT-first tracking architecture
    - obligation_id: O-HB-FAST-START-PROTOCOL-CANDIDATE
      status: proposed_only_not_admitted
      reason: future immediate practical start
  blocked_or_forbidden_now:
    - no accepted diet prescription
    - no accepted training prescription
    - no Strategic Path Map
    - no Horizon selection
    - no Active Frontier
    - no roadmap
    - no Codex/product execution
    - no Notion/GitHub/project implementation
  hidden_acceptance_check: passed

invariant_checks:
  one_obligation_only: passed
  no_execution_without_execution_obligation: passed
  no_legacy_import_without_legacy_import_obligation: passed
  no_strategy_projection_before_required_receipts: passed
  no_diet_or_training_plan_created: passed
  objective_delta_not_silently_accepted: passed
  receipt_committed_to_ledger: pending_until_commit_applied
```

END_OF_FILE: directions/health-and-beauty/workflow/receipts/R-HB-CONSTRAINTS-DEFINE-2026-05-26.md
