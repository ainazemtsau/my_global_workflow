---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: obligations
  status: h1_blueprint_activation_obligation_admitted_downstream_not_started
  owner: proof_carrying_workflow_os
---

# Health and Beauty Obligations

## Initial Obligations

```yaml
obligations:
  - obligation_id: O-HB-ROOT-OBJECTIVE-CONFIRM
    type: human_decision / clarify_objective
    statement: Confirm or redefine the root objective for this Direction under the Workflow OS.
    status: closed
    resolution: accepted
    satisfied_by: R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26
    required_operator: AskHumanDecision or ClarifyObjective
    acceptance_conditions:
      - root objective statement accepted
      - success semantics either accepted or delegated to child Obligation
      - constraints marked accepted/candidate/unknown
    blocks:
      - success semantics
      - constraints
      - strategic path map projection
      - horizon commitment
      - active frontier view
      - execution obligations

  - obligation_id: O-HB-SUCCESS-SEMANTICS-DEFINE
    type: clarify
    statement: Define what success means for this Direction before strategy or execution.
    status: closed
    resolution: accepted
    satisfied_by: R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27
    unblocked_by:
      - R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26

  - obligation_id: O-HB-CONSTRAINTS-DEFINE
    type: clarify
    statement: Define hard constraints for this Direction such as capacity, time, budget, acceptable risk, domain boundaries, and execution boundaries.
    status: closed
    resolution: accepted
    satisfied_by: R-HB-CONSTRAINTS-DEFINE-2026-05-26
    unblocked_by:
      - R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26

  - obligation_id: O-HB-ROOT-OBJECTIVE-AMEND-TO-35KG
    type: clarify_objective_amendment
    statement: Confirm whether accepted root objective should change from -25 kg to -35 kg / target about 90 kg based on current user input.
    status: closed
    resolution: accepted
    satisfied_by: R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27
    unblocked_by:
      - R-HB-CONSTRAINTS-DEFINE-2026-05-26
    required_operator: ClarifyObjective / AskHumanDecision
    acceptance_conditions:
      - explicit confirmation or rejection of -35 kg target
      - if accepted, root objective amendment receipt created
      - if rejected, target delta handled as candidate context only

  - obligation_id: O-HB-LEGACY-INVENTORY-OPTIONAL
    type: legacy_import
    statement: Optionally inspect old Health and Beauty files as legacy evidence only.
    status: blocked
    optional: true
    blocked_by:
      - O-HB-ROOT-OBJECTIVE-CONFIRM
    rule: Old Direction files may be inspected as legacy evidence only through Legacy Import Receipt.

  - obligation_id: O-HB-STRATEGIC-MAP-PROJECTION-CREATE
    type: projection
    statement: Create Strategic Path Map projection from accepted root objective, constraints, and success semantics. Projection only; no Horizon, Active Frontier, roadmap, execution, diet plan, training plan, or tracking implementation may be accepted in this obligation unless separately admitted.
    status: closed
    resolution: projection_committed
    satisfied_by: R-HB-STRATEGIC-MAP-PROJECTION-CREATE-2026-05-27
    unblocked_by:
      - R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27

  - obligation_id: O-HB-HORIZON-SELECT
    type: human_decision
    statement: Select the first Horizon from the committed Strategic Path Map projection. Selection only; do not create Active Frontier, roadmap, execution, diet plan, training plan, tracking implementation, ChatGPT Project setup, or Health Operating Project implementation in this obligation.
    status: closed
    resolution: accepted
    satisfied_by: R-HB-HORIZON-SELECT-2026-05-27
    unblocked_by:
      - R-HB-STRATEGIC-MAP-PROJECTION-CREATE-2026-05-27
    required_operator: AskHumanDecision / ClarifyObjective
    candidate_options:
      - H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP
      - H2_BASELINE_AND_7_DAY_START
      - H3_NUTRITION_FIRST_STRICT_MENU_SYSTEM
      - H4_TRAINING_PRESERVATION_FOUNDATION
    acceptance_conditions:
      - one Horizon selected by explicit human decision
      - selected Horizon is recorded by Receipt
      - non-selected Horizon options remain candidate/projection context
      - no Active Frontier, roadmap, execution, diet plan, training plan, tracking implementation, ChatGPT Project setup, or Health Operating Project implementation accepted
    selection_result:
      selected_horizon: H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP
      selected_by: R-HB-HORIZON-SELECT-2026-05-27
      selection_intent_id: MINIMAL-USABLE-CORE-FIRST
      selection_intent: Minimal usable Daily Ops core first.
      downstream_implementation_state: not_started

  - obligation_id: O-HB-H1-MINIMAL-DAILY-OPS-CORE-DEFINE
    type: clarify_or_design
    statement: Define the minimal usable Health Operating Project / Daily Ops core after accepted H1, including corrected tool/program authority boundaries, without creating Active Frontier, roadmap, diet plan, meal plan, calorie prescription, training plan, 12-week plan, annual plan, tracking implementation, ChatGPT Project setup, Health Operating Project implementation, or Codex/product execution.
    status: closed
    resolution: accepted
    satisfied_by: R-HB-H1-MINIMAL-DAILY-OPS-CORE-DEFINE-2026-05-27
    admitted_by: current human input after H1 selection
    required_operator: ClarifyDesign / AskHumanDecision
    unblocked_by:
      - R-HB-HORIZON-SELECT-2026-05-27
    acceptance_conditions:
      - minimal Daily Ops core modules defined
      - Hevy/tool authority boundary recorded
      - Plan Authority Contract recorded
      - immediate usable core separated from future extensions
      - forbidden/out-of-scope list recorded
      - downstream implementation remains not_started
      - no Active Frontier, roadmap, diet plan, meal plan, calorie prescription, macro prescription, training plan, 12-week plan, annual plan, tracking implementation, ChatGPT Project setup, Health Operating Project implementation, Codex/product execution, or legacy import created

  - obligation_id: O-HB-H1-PROGRAM-BLUEPRINT-DEFINE
    type: clarify_or_design
    statement: Define the first Program Blueprint Authority Route after accepted Minimal Daily Ops Core, without creating actual diet plan, nutrition plan, meal plan, calorie prescription, macro prescription, training plan, accepted 12-week plan, annual plan, Active Frontier, roadmap, Daily Ops implementation, ChatGPT Project setup, tracking implementation, Codex/product execution, or legacy import.
    status: closed
    resolution: accepted
    satisfied_by: R-HB-H1-PROGRAM-BLUEPRINT-DEFINE-2026-05-27
    admitted_by: current human input after Minimal Daily Ops Core acceptance
    required_operator: ClarifyDesign / AskHumanDecision
    unblocked_by:
      - R-HB-H1-MINIMAL-DAILY-OPS-CORE-DEFINE-2026-05-27
    acceptance_conditions:
      - Program Blueprint authority route selected
      - route options compared
      - selected route separates blueprint authority from actual nutrition/training plans
      - tools/apps/templates are not authority
      - downstream implementation remains not_started
      - no forbidden plan or implementation surfaces created

  - obligation_id: O-HB-H1-FIRST-PROGRAM-BLUEPRINT-CREATE
    type: clarify_or_design
    statement: Create candidate first nutrition/training Program Blueprint structure/content at blueprint level only, separating nutrition principles from actual meal/calorie/macro prescription and training principles from actual training/session prescription, defining baseline inputs and review gates, and recording gym access via bicycle commute as optional future training surface, without creating Daily Ops implementation or any forbidden plan surfaces.
    status: closed
    resolution: candidate_blueprint_created
    satisfied_by: R-HB-H1-FIRST-PROGRAM-BLUEPRINT-CREATE-2026-05-27
    admitted_by: current human input after Program Blueprint Authority Route acceptance
    required_operator: ClarifyDesign / AskHumanDecision
    unblocked_by:
      - R-HB-H1-PROGRAM-BLUEPRINT-DEFINE-2026-05-27
    acceptance_conditions:
      - candidate first Program Blueprint structure/content defined at blueprint level only
      - nutrition blueprint principles separated from actual meal plan/calorie/macro prescription
      - training blueprint principles separated from actual training plan/session prescription
      - gym access via bicycle commute recorded as optional future training surface
      - baseline inputs needed now vs unknown allowed recorded
      - review gates recorded
      - candidate blueprint is not Daily Ops authority
      - downstream implementation remains not_started
      - no Active Frontier, roadmap, actual diet plan, meal plan, calorie prescription, macro prescription, actual training plan, gym schedule, cycling prescription, accepted 12-week plan, annual plan, Daily Ops implementation, ChatGPT Project setup, tracking implementation, Codex/product execution, or legacy import created

  - obligation_id: O-HB-H1-NEXT-BOUNDED-RUN-SELECT
    type: human_decision / workflow_triage
    statement: Select and admit the next single bounded Health and Beauty Obligation after candidate first Program Blueprint creation.
    status: closed
    resolution: accepted
    satisfied_by: R-HB-H1-NEXT-BOUNDED-RUN-SELECT-2026-05-27
    admitted_by: current human input after R-HB-H1-FIRST-PROGRAM-BLUEPRINT-CREATE-2026-05-27
    required_operator: ClarifyDesign / AskHumanDecision
    acceptance_conditions:
      - GitHub main state verified
      - six Dashboard proposed next runs compared
      - one next bounded Obligation selected
      - no downstream implementation or prescription created
    selection_result:
      selected_next_obligation: O-HB-H1-FIRST-PROGRAM-BLUEPRINT-ACTIVATE-FOR-DAILY-OPS
      downstream_implementation_state: not_started

  - obligation_id: O-HB-H1-FIRST-PROGRAM-BLUEPRINT-ACTIVATE-FOR-DAILY-OPS
    type: authority_activation / clarify_or_design
    statement: >
      Activate the candidate first Program Blueprint as limited Daily Ops
      authority for blueprint-level boundaries, gate logic, escalation
      rules, and Plan Authority Contract use only, without creating
      actual nutrition or training prescriptions, Daily Ops
      implementation, ChatGPT Project setup, tracking implementation,
      roadmap, Active Frontier, Codex/product execution, or legacy import.
    status: open
    resolution: not_started
    admitted_by: R-HB-H1-NEXT-BOUNDED-RUN-SELECT-2026-05-27
    required_operator: ClarifyDesign / AskHumanDecision
    unblocked_by:
      - R-HB-H1-FIRST-PROGRAM-BLUEPRINT-CREATE-2026-05-27
      - R-HB-H1-NEXT-BOUNDED-RUN-SELECT-2026-05-27
    acceptance_conditions:
      - candidate first Program Blueprint activation boundary recorded
      - Daily Ops authority scope limited to blueprint-level gates, boundaries, escalation rules, and Plan Authority Contract
      - nutrition principles remain separated from actual meal plan, calorie prescription, macro prescription, recipes, menus, and shopping list
      - training principles remain separated from actual exercises, sets, reps, sessions, split, progression, gym schedule, cycling prescription, accepted 12-week plan, or annual plan
      - baseline unknowns preserved as blockers/gates for future prescriptions, not silently waived
      - gym access via bicycle commute remains optional future training surface
      - bike commute remains possible future load/recovery factor, not cardio prescription
      - downstream implementation remains not_started
      - no ChatGPT Project setup, tracking implementation, Codex/product execution, or legacy import created

proposed_residual_obligations:
  - obligation_id: O-HB-H1-FIRST-PROGRAM-BLUEPRINT-ACTIVATE-FOR-DAILY-OPS
    status: admitted_not_started
  - obligation_id: O-HB-BASELINE-MEASUREMENTS-COLLECT
    status: proposed_only_not_admitted
  - obligation_id: O-HB-H1-NUTRITION-PLAN-CREATE
    status: proposed_only_not_admitted
  - obligation_id: O-HB-H1-TRAINING-PLAN-CREATE
    status: proposed_only_not_admitted
  - obligation_id: O-HB-H1-DAILY-OPS-IMPLEMENTATION-READINESS-DEFINE
    status: proposed_only_not_admitted
  - obligation_id: O-HB-H1-DAILY-OPS-CHATGPT-PROJECT-SETUP
    status: proposed_only_not_admitted
```

No execution Obligations are currently admitted.

No CodexExecution operator may run.

No roadmap item exists without admitted Obligation.

END_OF_FILE: directions/health-and-beauty/workflow/OBLIGATIONS.md
