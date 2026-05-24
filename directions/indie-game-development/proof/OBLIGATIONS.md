---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: obligations_storage
  status: initialized_skeleton
  owner: proof_carrying_workflow_os
---

# Indie Game Development Obligations

## Admission Boundary

These Obligations start the Indie Game Development pilot from the beginning under the proof workflow.

No old Direction files are imported as accepted truth.

No execution Obligations are currently admitted.

No CodexExecution operator may run.

No roadmap item exists without admitted Obligation.

## Open Obligations

### O-IDG-ROOT-OBJECTIVE-CONFIRM

```yaml
obligation_id: O-IDG-ROOT-OBJECTIVE-CONFIRM
type: human_decision / clarify_objective
statement: Confirm or redefine the root objective for Indie Game Development under the proof workflow.
status: open
required_operator:
  - AskHumanDecision
  - ClarifyObjective
acceptance_conditions:
  - root objective statement accepted
  - success semantics either accepted or delegated to a child Obligation
  - constraints marked accepted/candidate/unknown
blocks:
  - strategic path map projection
  - horizon commitment
  - active frontier view
  - execution obligations
```

## Blocked Obligations

### O-IDG-SUCCESS-SEMANTICS-DEFINE

```yaml
obligation_id: O-IDG-SUCCESS-SEMANTICS-DEFINE
type: clarify
statement: Define what success means for this direction before strategy or execution.
status: blocked
blocked_by:
  - O-IDG-ROOT-OBJECTIVE-CONFIRM
```

### O-IDG-CONSTRAINTS-DEFINE

```yaml
obligation_id: O-IDG-CONSTRAINTS-DEFINE
type: clarify
statement: Define hard constraints for the direction such as solo capacity, time, budget, acceptable risk, preferred product domain, and execution boundaries.
status: blocked
blocked_by:
  - O-IDG-ROOT-OBJECTIVE-CONFIRM
```

### O-IDG-LEGACY-INVENTORY-OPTIONAL

```yaml
obligation_id: O-IDG-LEGACY-INVENTORY-OPTIONAL
type: legacy_import
statement: Optionally inspect old Indie Game Development files as legacy evidence only.
status: blocked
blocked_by:
  - O-IDG-ROOT-OBJECTIVE-CONFIRM
acceptance_conditions:
  - Legacy Import Receipt created
  - no old state imported without verification and commit
  - old Direction Map / Active Goal / Current Phase demoted if encountered
```

### O-IDG-STRATEGIC-MAP-PROJECTION-CREATE

```yaml
obligation_id: O-IDG-STRATEGIC-MAP-PROJECTION-CREATE
type: projection
statement: Create Strategic Path Map projection only after accepted strategic Receipts exist.
status: blocked
blocked_by:
  - O-IDG-ROOT-OBJECTIVE-CONFIRM
  - O-IDG-SUCCESS-SEMANTICS-DEFINE
  - O-IDG-CONSTRAINTS-DEFINE
```

## Execution Boundary

Execution is unavailable until root objective, strategy, constraints, and execution-ready precondition Receipts are accepted and committed.

END_OF_FILE: directions/indie-game-development/proof/OBLIGATIONS.md
