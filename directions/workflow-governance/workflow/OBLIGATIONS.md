---
artifact_control:
  namespace: direction_proof
  direction_id: workflow-governance
  artifact_type: obligations
  status: project_instruction_budget_residual_sweep
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
    status: satisfied
    satisfied_by_receipt: R-WG-ATOMIC-RUN-HARDEN-001
    required_operator: GovernancePatch / RepositoryMaintenancePlan
    acceptance_conditions:
      - Explicit Atomic Run / Single Responsibility invariant is added or strengthened.
      - Operator Independence / effectiveness-over-agreement rule is added or strengthened.
      - Scope triage before material work is required.
      - Child handoff is gated: child chats only when needed for the current Obligation.
      - Receipt schema or policy records scope_audit / parked residual context / hidden acceptance check.
      - Project setup instructions and runtime packs are refreshed when source files change.
      - No product execution, roadmap, Horizon, Active Frontier, or legacy import is introduced.

  - obligation_id: O-WG-PROJECT-SURFACE-SEPARATION-HARDEN
    type: workflow_setup_policy_patch
    statement: >
      Harden setup terminology and artifacts so ChatGPT Project Instructions UI,
      Project Files/Sources, repo instruction sources, and request-only sources
      cannot be conflated.
    status: satisfied
    satisfied_by_receipt: R-WG-PROJECT-SURFACE-SEPARATION-HARDEN-001
    required_operator: GovernancePatch / RepositoryMaintenancePlan
    acceptance_conditions:
      - Project Instructions UI is defined separately from Project Files/Sources.
      - `CHATGPT_PROJECT_INSTRUCTIONS.md` files are treated as UI payload sources, not default uploads.
      - Generated Project Instructions are optimized for the Project Instructions UI.
      - Handoffs split instruction UI updates from Project Files/Sources refresh.
      - Project Files manifests exclude Project Instructions sources from default upload count.
      - No product execution or Indie Game Development proof-state mutation is introduced.

  - obligation_id: O-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN
    type: workflow_setup_policy_patch
    statement: >
      Harden Project Instructions generation so UI payloads are compact,
      paste-ready, below the ChatGPT Web UI character limit, and still preserve
      critical Workflow OS behavior.
    status: satisfied
    satisfied_by_receipt: R-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN-001
    required_operator: GovernancePatch / RepositoryMaintenancePlan
    acceptance_conditions:
      - Project Instructions UI payload hard max is 8,000 characters.
      - Project Instructions UI payload target max is 6,500 characters.
      - Payload extraction and character-count validation are required.
      - Ordinary Direction and Workflow Governance generated UI payloads fit within the target.
      - Payloads are compact behavioral instructions, not workflow documentation.
      - No product execution or Indie Game Development proof-state mutation is introduced.

  - obligation_id: O-WG-PROJECT-INSTRUCTION-BUDGET-RESIDUAL-SWEEP
    type: workflow_setup_policy_patch
    statement: >
      Sweep active workflow/Codex-facing files for residual ambiguous Project Files
      refresh wording after Project Instructions UI payload budget hardening.
    status: satisfied
    satisfied_by_receipt: R-WG-PROJECT-INSTRUCTION-BUDGET-RESIDUAL-SWEEP-001
    required_operator: GovernancePatch / RepositoryMaintenancePlan
    acceptance_conditions:
      - Active Codex-facing refresh wording uses separated project refresh fields.
      - Project Instructions UI source changes require payload character counts.
      - No product execution or forbidden Direction proof-state mutation is introduced.

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

O-WG-ATOMIC-RUN-HARDEN is satisfied by R-WG-ATOMIC-RUN-HARDEN-001.

O-WG-PROJECT-SURFACE-SEPARATION-HARDEN is satisfied by R-WG-PROJECT-SURFACE-SEPARATION-HARDEN-001.

O-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN is satisfied by R-WG-PROJECT-INSTRUCTION-BUDGET-HARDEN-001.

O-WG-PROJECT-INSTRUCTION-BUDGET-RESIDUAL-SWEEP is satisfied by R-WG-PROJECT-INSTRUCTION-BUDGET-RESIDUAL-SWEEP-001.

END_OF_FILE: directions/workflow-governance/workflow/OBLIGATIONS.md
