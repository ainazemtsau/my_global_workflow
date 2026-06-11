---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: receipt
  receipt_id: R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27
  status: committed
  owner: proof_carrying_workflow_os
---

# Receipt: R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27

```yaml
receipt_id: R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27
direction_id: health-and-beauty
target_obligation: O-HB-SUCCESS-SEMANTICS-DEFINE
operator_invoked: ClarifySuccessSemantics
commit_scope: hb_root_scope
status: committed

human_decision:
  normalized_from_accepted_state_and_current_context: true
  success_semantics_summary: >
    Direction success means reducing body weight from 125 kg to about 90 kg
    while preserving or improving physical strength, functional fitness,
    mobility/flexibility, recovery, and behavioral stability, supported by
    a low-friction ChatGPT-first tracking system. Speed should be as aggressive
    as safely sustainable, not reckless.

accepted_state_inputs:
  root_objective:
    status: accepted
    value: >
      Снижение массы тела на 35 кг: с текущих 125 кг примерно до 90 кг,
      при сохранении или минимальной потери физической силы, общей физической
      формы, гибкости/подвижности и функционального самочувствия; построение
      управляемой системы, где ChatGPT помогает вести питание, тренировки,
      трекинг, исследования и решения с минимальной нагрузкой на пользователя.
  constraints:
    status: accepted
    summary:
      - 35M, 182 cm, 125 kg
      - high strictness preferred
      - strict rules preferred
      - low-friction ChatGPT-first tracking preferred
      - batch-prep / preweighed portions preferred
      - high time availability for about 6 months
      - no reported chronic conditions
      - safety override required

claims_accepted_by_this_receipt:
  - claim_id: C-HB-SUCCESS-TARGET-WEIGHT-2026-05-27
    type: final_success_metric
    value: >
      Final weight success is reaching about 90 kg, operationalized as
      90 kg ± 2 kg maintained for 8 consecutive weeks, not a one-day scale touch.
  - claim_id: C-HB-SUCCESS-WEIGHT-MILESTONES-2026-05-27
    type: milestone_metric
    value:
      start_weight_kg: 125
      milestone_5_percent_loss_kg: 118.75
      milestone_10_percent_loss_kg: 112.5
      milestone_20_percent_loss_kg: 100
      final_target_kg: 90
  - claim_id: C-HB-SUCCESS-PACE-ENVELOPE-2026-05-27
    type: pace_semantics
    value: >
      Success pace means fastest sustainable trend that preserves health,
      recovery, adherence, strength, and function. CDC 1-2 lb/week is used as
      conservative external safety context. For 35 kg this implies a rough
      9-18 month envelope. Faster early movement is not automatically failure
      or success because early scale movement can include water/glycogen.
  - claim_id: C-HB-SUCCESS-STRENGTH-PRESERVATION-2026-05-27
    type: performance_metric
    value: >
      Weight loss is not successful if it is achieved through meaningful loss
      of functional strength. A baseline strength battery must be collected
      later; success means preserving or improving practical strength relative
      to baseline and bodyweight during the cut.
  - claim_id: C-HB-SUCCESS-CARDIO-FUNCTION-2026-05-27
    type: fitness_metric
    value: >
      Success includes improved or stable functional cardio capacity and daily
      activity tolerance, using future baseline tests and Apple Watch signals
      as supporting data, without reckless joint-loading escalation.
  - claim_id: C-HB-SUCCESS-MOBILITY-2026-05-27
    type: mobility_metric
    value: >
      Success includes preserved or improved mobility/flexibility compared to
      baseline. Current abdominal mass may limit movement, but the process
      should not create new mobility restrictions.
  - claim_id: C-HB-SUCCESS-BEHAVIORAL-STABILITY-2026-05-27
    type: adherence_and_behavior_metric
    value: >
      Success requires a strict but resilient system: deviations are logged and
      repaired quickly, not allowed to become multi-day collapse. Escalating
      binge-like behavior is a safety/strategy failure signal.
  - claim_id: C-HB-SUCCESS-LOW-FRICTION-TRACKING-2026-05-27
    type: tracking_metric
    value: >
      Success requires low-friction tracking: photo, voice, short text,
      repeated meals, batch-prep, weekly review, Heavy for strength, Apple Watch
      for activity/recovery signals, and minimal manual logging burden.
  - claim_id: C-HB-SUCCESS-SAFETY-STOPS-2026-05-27
    type: safety_metric
    value: >
      Plans are not successful if they depend on starvation framing, reckless
      crash dieting, ignored chest pain, fainting, palpitations, severe
      shortness of breath, serious joint pain, severe insomnia, persistent
      exhaustion, or escalating binge-like behavior.

success_semantics:
  final_success:
    target_weight_kg: 90
    acceptable_maintenance_band_kg: "88-92"
    maintenance_proof_period: "8 consecutive weeks"
    final_success_requires:
      - target_weight_maintenance
      - strength_preservation
      - functional_fitness_preservation_or_improvement
      - mobility_preservation_or_improvement
      - no_safety_stop_violation
      - low_friction_tracking_system_operational
  milestones:
    - milestone_id: HB-WEIGHT-M1-5PCT
      target_weight_kg: 118.75
      meaning: first health/progress milestone
    - milestone_id: HB-WEIGHT-M2-10PCT
      target_weight_kg: 112.5
      meaning: first major bodyweight reduction milestone
    - milestone_id: HB-WEIGHT-M3-20PCT
      target_weight_kg: 100
      meaning: major transition point and prior-root-objective neighborhood
    - milestone_id: HB-WEIGHT-FINAL
      target_weight_kg: 90
      meaning: amended root objective target
  pace_semantics:
    user_preference: as_fast_as_possible
    accepted_interpretation: as_fast_as_safely_sustainable
    conservative_external_reference: "CDC gradual steady loss around 1-2 lb/week"
    rough_final_window_from_reference: "about 9-18 months for 35 kg"
    not_success_if:
      - pace_requires_starvation_or_crash_dieting
      - pace_causes_persistent_exhaustion
      - pace_causes_serious_joint_pain_or_injury
      - pace_worsens_binge_like_behavior
      - pace_significantly_degrades_strength_or_function
  performance_semantics:
    baseline_required_later: true
    preserve_strength: true
    preserve_or_improve_mobility: true
    preserve_or_improve_cardio_function: true
    candidate_measurement_sources:
      - Heavy strength logs
      - Apple Watch trends
      - standardized future strength battery
      - standardized future cardio test
      - standardized future mobility checks
  adherence_semantics:
    preferred_style: strict_rules_with_repair_protocol
    success_is_not_perfection: true
    required_repair_behavior: return_to_plan_after_deviation_without_multi_day_collapse
    tracking_style: ChatGPT_first_low_friction
  safety_semantics:
    hard_stop_signals:
      - chest_pain
      - fainting
      - palpitations
      - severe_shortness_of_breath
      - serious_joint_pain
      - severe_insomnia
      - persistent_exhaustion
      - escalating_binge_like_behavior
    medical_review_recommended: true

unresolved_items:
  - baseline_waist_circumference
  - baseline_blood_pressure
  - baseline_resting_heart_rate
  - baseline_strength_battery
  - baseline_cardio_test
  - baseline_mobility_test
  - baseline_photos_policy
  - exact weekly review format
  - exact manual tracking_time_limit
  - exact maintenance_strategy_after_reaching_target

context_authority_audit:
  accepted_ledger_state:
    - root objective amended to -35 kg / about 90 kg
    - constraints accepted
    - success semantics pending before this receipt
  committed_receipts:
    - R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26
    - R-HB-CONSTRAINTS-DEFINE-2026-05-26
    - R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27
  current_human_input:
    - user reports amendment commit created, pushed, and merged to main
  external_reference_context:
    - CDC used for gradual/steady weight-loss safety context and tracking/realistic-goal framing
    - NIDDK used for safe weight-loss-program features and warning signs
    - WHO used for physical activity and muscle-strengthening safety context
  projection_context:
    - Dashboard says next valid run is O-HB-SUCCESS-SEMANTICS-DEFINE
    - Dashboard still forbids diet/training prescription and tracking implementation as accepted plan
  candidate_context:
    - future diet design
    - future training design
    - future fast-start protocol
    - future tracking architecture
  unknown:
    - exact baseline waist/BP/strength/cardio/mobility measurements
  instruction_context:
    - one Obligation scope
    - Receipt candidate until Verify + Commit
    - no execution without admitted execution Obligation

scope_audit:
  one_obligation_scope: passed
  in_scope_used:
    - define measurable success semantics
    - translate accepted root objective and constraints into success criteria
    - define safety and failure semantics
  parked_residual_context:
    - diet prescription
    - training prescription
    - fast-start protocol
    - tracking implementation
    - Strategic Path Map
    - Horizon selection
    - Active Frontier
    - roadmap
    - Codex/product execution
  residual_obligations:
    - obligation_id: O-HB-STRATEGIC-MAP-PROJECTION-CREATE
      status: should_unblock_after_commit
      reason: root objective, constraints, and success semantics will be accepted
    - obligation_id: O-HB-BASELINE-MEASUREMENTS-COLLECT
      status: proposed_only_not_admitted
      reason: baseline waist/BP/strength/cardio/mobility data required before precise plan validation
    - obligation_id: O-HB-FAST-START-PROTOCOL-CANDIDATE
      status: proposed_only_not_admitted
      reason: user wants immediate practical start, but plan requires strategy/projection first
  blocked_or_forbidden_now:
    - no diet plan
    - no training plan
    - no fast-start prescription
    - no tracking implementation
    - no Strategic Path Map in this run
    - no Horizon
    - no Active Frontier
    - no roadmap
    - no Codex/product execution
  hidden_acceptance_check: passed

invariant_checks:
  one_obligation_only: passed
  no_execution_without_execution_obligation: passed
  no_legacy_import_without_legacy_import_obligation: passed
  no_diet_or_training_plan_created: passed
  no_tracking_implementation_created: passed
  no_strategy_projection_created_in_success_run: passed
  receipt_committed_to_ledger: pending_until_commit_applied

END_OF_FILE: directions/health-and-beauty/workflow/receipts/R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27.md
