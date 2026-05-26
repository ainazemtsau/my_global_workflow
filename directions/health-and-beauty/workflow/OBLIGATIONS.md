---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: obligations
  status: root_objective_accepted
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
    status: open
    unblocked_by:
      - R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26

  - obligation_id: O-HB-CONSTRAINTS-DEFINE
    type: clarify
    statement: Define hard constraints for this Direction such as capacity, time, budget, acceptable risk, domain boundaries, and execution boundaries.
    status: open
    unblocked_by:
      - R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26

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
    statement: Create Strategic Path Map projection only after accepted strategic Receipts exist.
    status: blocked
    blocked_by:
      - O-HB-SUCCESS-SEMANTICS-DEFINE
      - O-HB-CONSTRAINTS-DEFINE
```

No execution Obligations are currently admitted.

No CodexExecution operator may run.

No roadmap item exists without admitted Obligation.

END_OF_FILE: directions/health-and-beauty/workflow/OBLIGATIONS.md
