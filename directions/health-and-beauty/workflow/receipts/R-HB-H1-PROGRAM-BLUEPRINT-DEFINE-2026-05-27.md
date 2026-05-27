---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: receipt
  receipt_id: R-HB-H1-PROGRAM-BLUEPRINT-DEFINE-2026-05-27
  status: committed
  owner: proof_carrying_workflow_os
---

# Receipt: R-HB-H1-PROGRAM-BLUEPRINT-DEFINE-2026-05-27

```yaml
receipt_id: R-HB-H1-PROGRAM-BLUEPRINT-DEFINE-2026-05-27
direction_id: health-and-beauty
target_obligation: O-HB-H1-PROGRAM-BLUEPRINT-DEFINE
operator_invoked: ClarifyDesign / AskHumanDecision
commit_scope: hb_strategy_scope
status: committed
codex_handoff_id: CH-HB-H1-PROGRAM-BLUEPRINT-DEFINE-2026-05-27

selected_blueprint_route:
  route_id: HYBRID_BASELINE_INFORMED_RESEARCHED_STARTER_BLUEPRINT
  route_status: selected
  route_summary: >
    The first Program Blueprint Authority Route is selected as a hybrid route:
    use baseline information where available, use research and accepted
    constraints to draft a starter blueprint, and require a later separate
    Workflow receipt before any Program Blueprint becomes accepted authority.
  route_options_compared:
    - route_id: TOOL_OR_APP_FIRST_PROGRAM_AUTHORITY
      decision: rejected_as_authority
      reason: Tools, apps, templates, logs, and candidate infrastructure may
        inform future work, but they cannot select or authorize the program.
    - route_id: EXTERNAL_EXPERT_REQUIRED_BEFORE_ROUTE_SELECTION
      decision: not_required
      reason: Trainer or dietitian input may be useful review or escalation,
        but it is not a hard requirement for selecting this route.
    - route_id: BASELINE_COMPLETE_BEFORE_ROUTE_SELECTION
      decision: not_required
      reason: Baseline data is useful input, but incomplete baseline collection
        is not a hard blocker for selecting the authority route.
    - route_id: HYBRID_BASELINE_INFORMED_RESEARCHED_STARTER_BLUEPRINT
      decision: selected
      reason: This route preserves Workflow authority, uses baseline data as
        evidence when available, allows researched starter blueprint creation
        later, and keeps downstream implementation unstarted.

authority_rule:
  future_program_blueprint_authority: future_workflow_receipt_only
  rule: >
    A future Program Blueprint becomes authority only when accepted by a
    separate Workflow receipt. This receipt selects the authority route only.
  tools_are_authority: false
  tools_rule: >
    Hevy, apps, templates, HomeLab, Mealie/Miali, recipes, trackers, logs, and
    other tools are input, evidence, or tool surfaces only. They are not
    authority for the Program Blueprint.
  external_expert_required: false
  external_expert_role: optional_review_or_escalation
  baseline_required_for_route_selection: false
  baseline_role: useful_input_not_hard_blocker
  downstream_implementation_state: not_started

claims_accepted_by_this_receipt:
  - claim_id: C-HB-H1-PROGRAM-BLUEPRINT-ROUTE-DEFINED-2026-05-27
    type: authority_route
    value: >
      The first Program Blueprint Authority Route is defined for H1 without
      creating a Program Blueprint, plan, prescription, or implementation.
  - claim_id: C-HB-H1-HYBRID-BASELINE-INFORMED-STARTER-BLUEPRINT-SELECTED-2026-05-27
    type: route_selection
    value: >
      HYBRID_BASELINE_INFORMED_RESEARCHED_STARTER_BLUEPRINT is selected as the
      route for a later starter Program Blueprint.
  - claim_id: C-HB-H1-PROGRAM-BLUEPRINT-AUTHORITY-WORKFLOW-RECEIPT-NOT-TOOL-2026-05-27
    type: authority_boundary
    value: >
      Program Blueprint authority can come only from a future accepted Workflow
      receipt, not from Hevy, apps, templates, logs, recipes, HomeLab,
      Mealie/Miali, or other tools.
  - claim_id: C-HB-H1-EXTERNAL-EXPERT-OPTIONAL-REVIEW-NOT-HARD-REQUIREMENT-2026-05-27
    type: review_boundary
    value: >
      Trainer or dietitian input is optional review or escalation, not a hard
      requirement for the selected authority route.
  - claim_id: C-HB-H1-DOWNSTREAM-IMPLEMENTATION-STILL-NOT-STARTED-2026-05-27
    type: implementation_boundary
    value: >
      Downstream implementation remains not_started after this receipt.

explicit_non_acceptance:
  - no actual diet plan accepted
  - no actual nutrition plan accepted
  - no meal plan accepted
  - no calorie prescription accepted
  - no macro prescription accepted
  - no training plan accepted
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
    - H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP is selected.
    - selection_intent_id is MINIMAL-USABLE-CORE-FIRST.
    - R-HB-H1-MINIMAL-DAILY-OPS-CORE-DEFINE-2026-05-27 is accepted.
    - h1_minimal_daily_ops_core includes Plan Authority Contract.
    - Hevy / H-E-V-Y is candidate tool surface, not program authority.
    - HomeLab and Mealie/Miali Recipes are optional candidate infrastructure,
      not hard requirements.
    - downstream_implementation_state is not_started.
    - legacy_import_state is not_performed.
    - legacy_state_authority is false.
    - no execution obligations are currently admitted.
  current_human_input:
    - current handoff admits O-HB-H1-PROGRAM-BLUEPRINT-DEFINE only
    - current handoff selects the Program Blueprint Authority Route only
    - current handoff forbids actual plans, implementation, setup, tracking,
      Codex/product execution, Active Frontier, roadmap, and legacy import
  instruction_context:
    - repository maintenance only
    - direct to main allowed after validation
    - commit scope is hb_strategy_scope
    - allowed paths are limited to Health and Beauty workflow proof files
  rejected_as_authority:
    - Hevy or H-E-V-Y as training-program authority
    - apps, trackers, templates, recipes, logs, or tool exports as authority
    - HomeLab or Mealie/Miali as hard requirements
    - external trainer or dietitian as required authority gate
    - complete baseline collection as hard route-selection blocker

scope_audit:
  one_obligation_scope: passed
  in_scope_used:
    - define Program Blueprint Authority Route
    - compare route options
    - select HYBRID_BASELINE_INFORMED_RESEARCHED_STARTER_BLUEPRINT
    - separate future blueprint authority from actual nutrition or training plans
    - record tools, apps, templates, HomeLab, Mealie/Miali, and logs as
      input/evidence/tool surfaces only
    - record trainer or dietitian role as optional review or escalation
    - record baseline as useful input, not hard blocker
    - keep downstream implementation not_started
  blocked_or_forbidden_now:
    - no actual nutrition plan created
    - no actual diet plan created
    - no meal plan created
    - no calorie prescription created
    - no macro prescription created
    - no training plan created
    - no accepted 12-week plan created
    - no annual plan created
    - no Active Frontier created
    - no roadmap created
    - no Daily Ops implementation created
    - no ChatGPT Project setup created
    - no tracking implementation created
    - no Codex/product execution performed
    - no legacy import performed
  hidden_acceptance_check: passed

invariant_checks:
  receipt_marks_status_committed: passed
  target_obligation_recorded: passed
  operator_invoked_recorded: passed
  commit_scope_recorded: passed
  selected_blueprint_route_recorded: passed
  route_options_compared: passed
  future_program_blueprint_authority_requires_separate_workflow_receipt: passed
  tools_apps_templates_homelab_mealie_miali_not_authority: passed
  trainer_dietitian_optional_review_not_hard_requirement: passed
  baseline_useful_input_not_hard_blocker: passed
  downstream_implementation_state_remains_not_started: passed
  context_authority_audit_recorded: passed
  scope_audit_recorded: passed
  explicit_non_acceptance_recorded: passed
  no_active_frontier_selection: passed
  no_roadmap_created: passed
  no_execution_obligation_admitted: passed
  no_actual_diet_nutrition_meal_calorie_macro_or_training_plan_created: passed
  no_12_week_or_annual_plan_created: passed
  no_daily_ops_implementation_created: passed
  no_chatgpt_project_setup_created: passed
  no_tracking_implementation_created: passed
  no_codex_product_execution: passed
  no_legacy_import: passed
  receipt_committed_to_ledger: passed_by_this_commit
```

END_OF_FILE: directions/health-and-beauty/workflow/receipts/R-HB-H1-PROGRAM-BLUEPRINT-DEFINE-2026-05-27.md
