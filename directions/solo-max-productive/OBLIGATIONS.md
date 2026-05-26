---
artifact_control:
  namespace: direction_proof
  direction_id: solo-max-productive
  artifact_type: obligations
  status: m4_initialized_skeleton
  owner: proof_carrying_workflow_os
---

# Solo Max Productive Obligations

## Initial Obligations

```yaml
obligations:
  - obligation_id: O-SMP-ROOT-OBJECTIVE-CONFIRM
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

  - obligation_id: O-SMP-SUCCESS-SEMANTICS-DEFINE
    type: clarify
    statement: Define what success means for this Direction before strategy or execution.
    status: blocked
    blocked_by:
      - O-SMP-ROOT-OBJECTIVE-CONFIRM

  - obligation_id: O-SMP-CONSTRAINTS-DEFINE
    type: clarify
    statement: Define hard constraints for this Direction such as capacity, time, budget, acceptable risk, domain boundaries, and execution boundaries.
    status: blocked
    blocked_by:
      - O-SMP-ROOT-OBJECTIVE-CONFIRM

  - obligation_id: O-SMP-LEGACY-INVENTORY-OPTIONAL
    type: legacy_import
    statement: Optionally inspect old Solo Max Productive files as legacy evidence only.
    status: blocked
    optional: true
    blocked_by:
      - O-SMP-ROOT-OBJECTIVE-CONFIRM
    rule: Old Direction files may be inspected as legacy evidence only through Legacy Import Receipt.

  - obligation_id: O-SMP-STRATEGIC-MAP-PROJECTION-CREATE
    type: projection
    statement: Create Strategic Path Map projection only after accepted strategic Receipts exist.
    status: blocked
    blocked_by:
      - O-SMP-ROOT-OBJECTIVE-CONFIRM
      - O-SMP-SUCCESS-SEMANTICS-DEFINE
      - O-SMP-CONSTRAINTS-DEFINE
```

No execution Obligations are currently admitted.

No CodexExecution operator may run.

No roadmap item exists without admitted Obligation.

END_OF_FILE: directions/solo-max-productive/OBLIGATIONS.md
