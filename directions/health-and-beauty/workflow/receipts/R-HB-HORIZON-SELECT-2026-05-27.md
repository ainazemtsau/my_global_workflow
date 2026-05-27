---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: receipt
  receipt_id: R-HB-HORIZON-SELECT-2026-05-27
  status: committed
  owner: proof_carrying_workflow_os
---

# Receipt: R-HB-HORIZON-SELECT-2026-05-27

```yaml
receipt_id: R-HB-HORIZON-SELECT-2026-05-27
direction_id: health-and-beauty
target_obligation: O-HB-HORIZON-SELECT
operator_invoked: AskHumanDecision / ClarifyObjective
commit_scope: hb_root_scope
status: committed
codex_handoff_id: CH-HB-HORIZON-SELECT-H1-MINIMAL-CORE-FIRST-2026-05-27
source_receipt_id: R-HB-HORIZON-SELECT-2026-05-27
source_obligation_id: O-HB-HORIZON-SELECT

human_decision:
  normalized_from_current_human_input: true
  selected_horizon: H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP
  selected_horizon_label: Health Operating Project Bootstrap
  selection_intent_id: MINIMAL-USABLE-CORE-FIRST
  selection_intent: >
    Future H1 work should prioritize a minimal usable Daily Ops core so the
    user can quickly start nutrition and training, while preserving future
    extensibility and GitHub-backed state.

selected_horizon:
  horizon_id: H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP
  label: Health Operating Project Bootstrap
  selected_by: R-HB-HORIZON-SELECT-2026-05-27
  selected_from_projection: directions/health-and-beauty/workflow/projections/STRATEGIC_PATH_MAP.md
  projection_receipt: R-HB-STRATEGIC-MAP-PROJECTION-CREATE-2026-05-27
  scope_boundary: Horizon selection only; no downstream implementation.

selection_intent:
  intent_id: MINIMAL-USABLE-CORE-FIRST
  summary: >
    The first later H1 run should define or admit only a minimal usable Daily
    Ops core before broader Health Operating Project work, so nutrition and
    training can start quickly.
  future_support_candidate_context:
    - Heavy workout logging
    - ChatGPT photo food logging
    - ChatGPT voice food logging
    - ChatGPT short text food logging
    - GitHub-backed state
    - low context pollution
    - recipes
    - training discussions
    - plan adjustments
    - research requests
    - possible HomeLab or recipe integration
  authority: accepted_preference_for_future_h1_scoping_only

claims_accepted_by_this_receipt:
  - claim_id: C-HB-HORIZON-H1-SELECTED-2026-05-27
    type: decision
    value: >
      First Horizon selected: H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP.
    evidence:
      - current human input in source chat
      - O-HB-HORIZON-SELECT open and unblocked in OBLIGATIONS.md
      - H1 candidate option and projection recommendation in STRATEGIC_PATH_MAP.md
  - claim_id: C-HB-H1-SELECTION-INTENT-MINIMAL-USABLE-CORE-FIRST-2026-05-27
    type: preference
    value: >
      Future H1 work should prioritize a minimal usable Daily Ops core that
      allows quick start for nutrition and training, while remaining extensible
      and GitHub-backed.
    evidence:
      - current human input in source chat

context_authority_audit:
  accepted_ledger_state:
    - root objective accepted and amended to -35 kg / about 90 kg
    - constraints accepted
    - success semantics accepted
    - strategic map projection committed
    - O-HB-HORIZON-SELECT open and unblocked before this receipt
  committed_receipts:
    - R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26
    - R-HB-CONSTRAINTS-DEFINE-2026-05-26
    - R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27
    - R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27
    - R-HB-STRATEGIC-MAP-PROJECTION-CREATE-2026-05-27
  current_human_input:
    - user selected H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP as the first Horizon
    - user wants to start nutrition and training quickly
    - user prefers creating the Health Operating Project / Daily Ops core first if it can become usable quickly
  projection_context:
    - STRATEGIC_PATH_MAP.md lists H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP as a candidate Horizon
    - STRATEGIC_PATH_MAP.md recommends H1 as projection only and requires separate human decision receipt
  candidate_context:
    - future minimal Daily Ops core
    - future Health Operating Project
    - future food logging by photo, voice, and short text
    - future Heavy integration
    - future GitHub-backed state
    - future recipes, training discussions, plan adjustments, and research requests
    - possible future HomeLab or recipe integration
  instruction_context:
    - repository maintenance verify and commit only
    - one Obligation scope
    - no product execution
    - no downstream implementation in this run
    - old project_files/00-08 are not accepted proof state
  unknown:
    - exact Minimal Daily Ops Core content
    - exact ChatGPT Project setup files
    - exact tracking storage schema
    - exact nutrition or training plans
    - exact Active Frontier or roadmap

scope_audit:
  one_obligation_scope: passed
  in_scope_used:
    - record explicit human Horizon selection
    - record selected Horizon H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP
    - record selection intent MINIMAL-USABLE-CORE-FIRST
    - close O-HB-HORIZON-SELECT
  parked_residual_context:
    - H1 Minimal Daily Ops Core definition
    - Active Frontier selection
    - roadmap
    - Health Operating Project implementation
    - ChatGPT Project setup
    - Daily Ops files
    - diet plan
    - meal plan
    - calorie prescription
    - training plan
    - tracking implementation
    - Codex/product execution
  residual_obligations:
    - obligation_id: O-HB-H1-MINIMAL-DAILY-OPS-CORE-DEFINE
      status: proposed_only_not_admitted
      type: clarify_or_design
      reason: Candidate future obligation after this commit if user admits a bounded H1 Minimal Daily Ops Core run.
  blocked_or_forbidden_now:
    - no Active Frontier created
    - no roadmap created
    - no execution obligation admitted
    - no Codex/product execution
    - no Health Operating Project implementation created
    - no ChatGPT Project setup created
    - no Daily Ops files created
    - no diet plan created
    - no meal plan created
    - no calorie prescription created
    - no training plan created
    - no tracking implementation created
    - no legacy state imported
  hidden_acceptance_check: passed

invariant_checks:
  receipt_marks_status_committed: passed
  target_obligation_recorded: passed
  operator_invoked_recorded: passed
  commit_scope_recorded: passed
  selected_horizon_recorded: passed
  selection_intent_recorded: passed
  context_authority_audit_recorded: passed
  scope_audit_recorded: passed
  parked_residual_context_recorded: passed
  no_active_frontier_selection: passed
  no_roadmap_created: passed
  no_execution_without_execution_obligation: passed
  no_diet_meal_calorie_or_training_plan_created: passed
  no_tracking_implementation_created: passed
  no_chatgpt_project_setup_created: passed
  no_health_operating_project_implementation_created: passed
  no_legacy_import: passed
  receipt_committed_to_ledger: passed_by_this_commit
```

END_OF_FILE: directions/health-and-beauty/workflow/receipts/R-HB-HORIZON-SELECT-2026-05-27.md
