---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: obligations
  status: root_objective_constraints_and_success_semantics_accepted_strategy_projection_pending
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
    status: open
    unblocked_by:
      - R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27
```

No execution Obligations are currently admitted.

No CodexExecution operator may run.

No roadmap item exists without admitted Obligation.

END_OF_FILE: directions/health-and-beauty/workflow/OBLIGATIONS.md
