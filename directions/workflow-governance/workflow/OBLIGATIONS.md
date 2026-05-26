---
artifact_control:
  namespace: direction_proof
  direction_id: workflow-governance
  artifact_type: obligations
  status: root_objective_accepted
  owner: proof_carrying_workflow_os
---

# Workflow Governance Obligations

## Initial Obligations

```yaml
obligations:
  - obligation_id: O-WG-ROOT-OBJECTIVE-CONFIRM
    type: human_decision / clarify_objective
    statement: Confirm or redefine the root objective for this Direction under the Workflow OS.
    status: satisfied
    satisfied_by_receipt: R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001
    required_operator: AskHumanDecision or ClarifyObjective
    acceptance_conditions:
      - root objective statement accepted
      - success semantics either accepted or delegated to child Obligation
      - constraints marked accepted/candidate/unknown

  - obligation_id: O-WG-SUCCESS-SEMANTICS-DEFINE
    type: clarify
    statement: Define what success means for this Direction before strategy or execution.
    status: satisfied_by_root_receipt
    satisfied_by_receipt: R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001
    satisfaction_scope: minimal accepted root objective scope

  - obligation_id: O-WG-CONSTRAINTS-DEFINE
    type: clarify
    statement: Define hard constraints for this Direction such as capacity, time, budget, acceptable risk, domain boundaries, and execution boundaries.
    status: satisfied_by_root_receipt
    satisfied_by_receipt: R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001
    satisfaction_scope: minimal accepted root objective scope

  - obligation_id: O-WG-ATOMIC-RUN-HARDEN
    type: workflow_policy_patch
    statement: >
      Harden Workflow OS with explicit Atomic Run / Single Responsibility,
      Operator Independence, Scope Triage, and child-handoff gating rules.
    status: open
    required_operator: GovernancePatch / RepositoryMaintenancePlan
    acceptance_conditions:
      - Explicit Atomic Run / Single Responsibility invariant is added or strengthened.
      - Operator Independence / effectiveness-over-agreement rule is added or strengthened.
      - Scope triage before material work is required.
      - Child handoff is gated: child chats only when needed for the current Obligation.
      - Receipt schema or policy records scope_audit / parked residual context / hidden acceptance check.
      - Project setup instructions and runtime packs are refreshed when source files change.
      - No product execution, roadmap, Horizon, Active Frontier, or legacy import is introduced.

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

No product execution Obligations are currently admitted.

No CodexExecution operator may run.

No roadmap item exists without admitted Obligation.

END_OF_FILE: directions/workflow-governance/workflow/OBLIGATIONS.md
