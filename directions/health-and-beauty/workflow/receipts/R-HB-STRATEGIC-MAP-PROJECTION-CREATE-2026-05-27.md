artifact_control:
namespace: direction_proof
direction_id: health-and-beauty
artifact_type: receipt
receipt_id: R-HB-STRATEGIC-MAP-PROJECTION-CREATE-2026-05-27
status: committed
owner: proof_carrying_workflow_os
Receipt: R-HB-STRATEGIC-MAP-PROJECTION-CREATE-2026-05-27
receipt_id: R-HB-STRATEGIC-MAP-PROJECTION-CREATE-2026-05-27
direction_id: health-and-beauty
target_obligation: O-HB-STRATEGIC-MAP-PROJECTION-CREATE
operator_invoked: Projection
commit_scope: hb_projection_scope
status: committed

projection_created:
  projection_id: P-HB-STRATEGIC-PATH-MAP-2026-05-27
  projection_path: directions/health-and-beauty/workflow/projections/STRATEGIC_PATH_MAP.md
  projection_type: strategic_path_map
  authority: projection_only_not_truth
  based_on_accepted_receipts:
    - R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26
    - R-HB-CONSTRAINTS-DEFINE-2026-05-26
    - R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27
    - R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27

strategic_paths_projected:
  - path_id: HB-PATH-A-HEALTH-OPERATING-PROJECT-BOOTSTRAP
    name: Health Operating Project Bootstrap
    purpose: Create the working operational project where the user will later track food, training, weight/body metrics, daily check-ins, weekly reviews, plan changes, and research requests.
  - path_id: HB-PATH-B-BASELINE-SAFETY-MEASUREMENTS
    name: Baseline + Safety Measurements
    purpose: Collect initial measurements and safety guardrails required before precise diet, training, or high-load changes.
  - path_id: HB-PATH-C-NUTRITION-OPERATING-SYSTEM
    name: Nutrition Operating System
    purpose: Build a strict, low-friction nutrition process with menu-first planning, batch-prep, preweighed portions, fallback rules, and simple tracking.
  - path_id: HB-PATH-D-TRAINING-ACTIVITY-OPERATING-SYSTEM
    name: Training + Activity Operating System
    purpose: Build the process for preserving strength, rebuilding conditioning, logging training, managing VR/cardio/bike work, and avoiding reckless joint loading.
  - path_id: HB-PATH-E-REVIEW-ADAPTATION-RESEARCH-LOOP
    name: Review + Adaptation + Research Loop
    purpose: Create the recurring mechanism for weekly review, plan adjustment, research requests, and escalation back to Workflow when a strategic decision is needed.

candidate_horizon_options_not_selected:
  - horizon_id: H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP
    label: Health Operating Project Bootstrap
    projection_reason: Strongest first candidate because the user needs a separate operational project to actually run daily food/training/tracking work, while Workflow remains the strategic proof layer.
  - horizon_id: H2_BASELINE_AND_7_DAY_START
    label: Baseline + 7-day start
    projection_reason: Candidate if the user wants immediate practical movement before building the full operating project.
  - horizon_id: H3_NUTRITION_FIRST_STRICT_MENU_SYSTEM
    label: Nutrition-first strict menu system
    projection_reason: Candidate because nutrition is likely the main weight-loss lever and user prefers strict menu/batch-prep.
  - horizon_id: H4_TRAINING_PRESERVATION_FOUNDATION
    label: Training-preservation foundation
    projection_reason: Candidate because success requires preserving strength and function.
  selection_status: not_selected_by_this_receipt

claims_accepted_by_this_receipt:
  - claim_id: C-HB-STRATEGIC-MAP-PROJECTION-2026-05-27
    type: projection_claim
    value: >
      The Health and Beauty Direction should be projected around five paths:
      Health Operating Project Bootstrap, Baseline/Safety Measurements,
      Nutrition Operating System, Training/Activity Operating System, and
      Review/Adaptation/Research Loop.
  - claim_id: C-HB-NEXT-VALID-HORIZON-SELECTION-2026-05-27
    type: routing_claim
    value: >
      After this projection is committed, the next valid critical Obligation
      should be O-HB-HORIZON-SELECT. The Horizon itself is not selected by this receipt.

context_authority_audit:
  accepted_ledger_state:
    - root objective accepted and amended to -35 kg / about 90 kg
    - constraints accepted
    - success semantics accepted
    - strategic map projection unblocked and pending before this receipt
  committed_receipts:
    - R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26
    - R-HB-CONSTRAINTS-DEFINE-2026-05-26
    - R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27
    - R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27
  current_human_input:
    - user clarified that the real need is to create a project/process where daily tracking and training work will happen later
    - user clarified that the operational project should work independently from the proof workflow for daily actions
  projection_context:
    - O-HB-STRATEGIC-MAP-PROJECTION-CREATE is open
    - Strategic Map is projection only; Ledger remains source of truth
  candidate_context:
    - candidate Health Operating Project
    - candidate Daily Ops protocols
    - candidate Horizon H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP
    - future baseline/fast-start/tracking/training/diet work
  instruction_context:
    - Atomic run and one Obligation scope
    - Projection does not create accepted truth beyond committed receipt
    - No Horizon, Active Frontier, roadmap, execution, diet plan, training plan, tracking implementation, or operating project implementation in this run
  unknown:
    - exact ChatGPT Project setup files
    - exact Daily Ops protocols
    - exact tracking storage choice
    - which Horizon the user will select next

scope_audit:
  one_obligation_scope: passed
  in_scope_used:
    - create corrected Strategic Path Map projection from accepted receipts and current clarification
    - route next decision without selecting it
  parked_residual_context:
    - Horizon selection
    - Health Operating Project implementation
    - ChatGPT Project setup
    - Daily food log protocol
    - Training log protocol
    - Baseline collection
    - diet prescription
    - training prescription
    - tracking implementation
    - roadmap
    - Codex/product execution
  residual_obligations:
    - obligation_id: O-HB-HORIZON-SELECT
      status: should_open_after_commit
      type: human_decision
      reason: Strategic Map projection should be followed by explicit human selection of the first Horizon. This does not select the Horizon now.
    - obligation_id: O-HB-HEALTH-OPERATING-PROJECT-SPEC
      status: proposed_only_not_admitted
      type: clarify_or_design
      reason: Candidate future obligation if H1 is selected; would define the actual operating project structure and protocols.
  blocked_or_forbidden_now:
    - no Horizon selected
    - no Active Frontier selected
    - no roadmap
    - no Health Operating Project implemented
    - no ChatGPT Project setup created
    - no diet plan
    - no training plan
    - no tracking implementation
    - no Codex/product execution
  hidden_acceptance_check: passed

invariant_checks:
  one_obligation_only: passed
  no_horizon_selection_in_projection_run: passed
  no_active_frontier_selection: passed
  no_roadmap_created: passed
  no_execution_without_execution_obligation: passed
  no_diet_or_training_plan_created: passed
  no_tracking_implementation_created: passed
  no_operational_project_implementation_created: passed
  receipt_committed_to_ledger: pending_until_commit_applied

END_OF_FILE: directions/health-and-beauty/workflow/receipts/R-HB-STRATEGIC-MAP-PROJECTION-CREATE-2026-05-27.md
