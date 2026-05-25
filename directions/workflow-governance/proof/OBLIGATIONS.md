---
artifact_control:
  namespace: direction_proof
  direction_id: workflow-governance
  artifact_type: obligations
  status: m4_initialized_skeleton
  owner: proof_carrying_workflow_os
---

# Workflow Governance Obligations

## Initial Obligations

```yaml
obligations:
  - obligation_id: O-WG-ROOT-OBJECTIVE-CONFIRM
    type: human_decision / clarify_objective
    statement: Confirm or redefine the root objective for this Direction under the Proof-Carrying Workflow OS.
    status: open
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

  - obligation_id: O-WG-SUCCESS-SEMANTICS-DEFINE
    type: clarify
    statement: Define what success means for this Direction before strategy or execution.
    status: blocked
    blocked_by:
      - O-WG-ROOT-OBJECTIVE-CONFIRM

  - obligation_id: O-WG-CONSTRAINTS-DEFINE
    type: clarify
    statement: Define hard constraints for this Direction such as capacity, time, budget, acceptable risk, domain boundaries, and execution boundaries.
    status: blocked
    blocked_by:
      - O-WG-ROOT-OBJECTIVE-CONFIRM

  - obligation_id: O-WG-LEGACY-INVENTORY-OPTIONAL
    type: legacy_import
    statement: Optionally inspect old Workflow Governance files as legacy evidence only.
    status: blocked
    optional: true
    blocked_by:
      - O-WG-ROOT-OBJECTIVE-CONFIRM
    rule: Old Direction files may be inspected as legacy evidence only through Legacy Import Receipt.

  - obligation_id: O-WG-STRATEGIC-MAP-PROJECTION-CREATE
    type: projection
    statement: Create Strategic Path Map projection only after accepted strategic Receipts exist.
    status: blocked
    blocked_by:
      - O-WG-ROOT-OBJECTIVE-CONFIRM
      - O-WG-SUCCESS-SEMANTICS-DEFINE
      - O-WG-CONSTRAINTS-DEFINE
```

No execution Obligations are currently admitted.

No CodexExecution operator may run.

No roadmap item exists without admitted Obligation.

END_OF_FILE: directions/workflow-governance/proof/OBLIGATIONS.md
