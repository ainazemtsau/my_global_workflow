---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: obligations_storage
  status: root_objective_accepted
  owner: proof_carrying_workflow_os
---

# Indie Game Development Obligations

## Admission Boundary

These Obligations govern the Indie Game Development pilot under the workflow.

No old Direction files are imported as accepted truth.

No product execution Obligations are currently admitted.

No CodexExecution operator may run.

No roadmap item exists without admitted Obligation.

## Open Obligations

### O-IDG-SUCCESS-SEMANTICS-DEFINE

```yaml
obligation_id: O-IDG-SUCCESS-SEMANTICS-DEFINE
type: clarify
statement: Define what success means for this direction before strategy or execution.
status: open
priority: critical
reason: Root objective is accepted, but success semantics remain unresolved.
required_operator:
  - ClarifyObjective
```

### O-IDG-CONSTRAINTS-DEFINE

```yaml
obligation_id: O-IDG-CONSTRAINTS-DEFINE
type: clarify
statement: Define hard constraints for the direction such as solo capacity, time, budget, acceptable risk, preferred product domain, and execution boundaries.
status: open
priority: critical
reason: Root objective is accepted, but hard constraints remain unresolved.
required_operator:
  - ClarifyObjective
```

### O-IDG-LEGACY-INVENTORY-OPTIONAL

```yaml
obligation_id: O-IDG-LEGACY-INVENTORY-OPTIONAL
type: legacy_import
statement: Optionally inspect old Indie Game Development files as legacy evidence only.
status: open_optional
optional: true
legacy_import_performed: false
required_operator_before_evidence_use:
  - LegacyImport
acceptance_conditions:
  - Legacy Import Receipt created
  - no old state imported without verification and commit
  - old Direction Map / Active Goal / Current Phase demoted if encountered
rule: Old files must not become evidence or accepted state without explicit LegacyImport Operator invocation.
```

## Satisfied Obligations

### O-IDG-ROOT-OBJECTIVE-CONFIRM

```yaml
obligation_id: O-IDG-ROOT-OBJECTIVE-CONFIRM
type: human_decision / clarify_objective
statement: Confirm or redefine the root objective for Indie Game Development under the workflow.
status: satisfied
satisfied_by: R-IDG-ROOT-OBJECTIVE-DECISION-001
accepted_result:
  root_objective: Create and finish an indie game within the already selected concept, with two equal top-level outcomes: a technically strong game the user can be proud of, and a commercially successful product that can generate meaningful revenue.
  root_level_constraints:
    - Work within the already selected concept; do not restart concept discovery by default.
    - Technical strength / technical ambition is a root-level value pillar.
    - Commercial success / meaningful revenue is a root-level value pillar.
    - Old concept/archive material remains legacy evidence only until admitted through valid workflow.
required_operator:
  - ClarifyObjective
```

## Blocked Obligations

### O-IDG-STRATEGIC-MAP-PROJECTION-CREATE

```yaml
obligation_id: O-IDG-STRATEGIC-MAP-PROJECTION-CREATE
type: projection
statement: Create Strategic Path Map projection only after accepted strategic Receipts exist.
status: blocked
blocked_by:
  - O-IDG-SUCCESS-SEMANTICS-DEFINE
  - O-IDG-CONSTRAINTS-DEFINE
blocked_until:
  - success semantics accepted
  - constraints accepted
```

## Execution Boundary

No CodexExecution/product execution Obligations are admitted.

No CodexExecution operator may run.

No roadmap item exists without admitted Obligation.

Execution remains unavailable until required success semantics, strategy, constraints, and execution-ready precondition Receipts are accepted and committed.

END_OF_FILE: directions/indie-game-development/workflow/OBLIGATIONS.md
