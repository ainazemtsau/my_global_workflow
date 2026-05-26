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

No execution Obligations are currently admitted.

No CodexExecution operator may run.

No roadmap item exists without admitted Obligation.

## Satisfied Obligations

### O-IDG-ROOT-OBJECTIVE-CONFIRM

```yaml
obligation_id: O-IDG-ROOT-OBJECTIVE-CONFIRM
type: human_decision / clarify_objective
statement: Confirm or redefine the root objective for Indie Game Development under the workflow.
status: satisfied
satisfied_by: R-IDG-ROOT-OBJECTIVE-DECISION-B-001
accepted_result:
  root_objective: "Create a systemic co-op indie game where the core value is built around gas simulation, level/topology interaction, and an extensible technical nucleus."
  accepted_root_level_constraints:
    - systemic co-op indie game
    - gas simulation is a core value pillar
    - level/topology interaction is a core value pillar
    - extensible technical nucleus is a core foundation concept
fields_not_accepted:
  - success semantics
  - hard technical constraints
  - hard product constraints
  - team/time/budget constraints
  - risk tolerance
  - platform target
  - release ambition
  - engine choice
  - Unity or non-Unity commitment
  - networking stack
  - exact genre
  - monetization
  - timeline
  - visual style
  - launch strategy
  - specific gas algorithms
  - specific topology data model
  - Codex execution readiness
  - roadmap
  - Horizon
  - Active Frontier
```

## Open Obligations

### O-IDG-SUCCESS-SEMANTICS-DEFINE

```yaml
obligation_id: O-IDG-SUCCESS-SEMANTICS-DEFINE
type: clarify
statement: Define what success means for this direction before strategy or execution.
status: open
opened_by: R-IDG-ROOT-OBJECTIVE-DECISION-B-001
reason: Success semantics were delegated by the accepted root objective Receipt.
required_operator:
  - ClarifyObjective
```

### O-IDG-CONSTRAINTS-DEFINE

```yaml
obligation_id: O-IDG-CONSTRAINTS-DEFINE
type: clarify
statement: Define hard constraints for the direction such as solo capacity, time, budget, acceptable risk, preferred product domain, and execution boundaries.
status: open
opened_by: R-IDG-ROOT-OBJECTIVE-DECISION-B-001
reason: Detailed constraints remain unresolved; root-level constraints are accepted only as listed in the Receipt.
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
```

## Execution Boundary

No execution Obligations are admitted.

No CodexExecution operator may run.

No roadmap item exists without admitted Obligation.

Execution is unavailable until root objective, strategy, constraints, and execution-ready precondition Receipts are accepted and committed.

END_OF_FILE: directions/indie-game-development/proof/OBLIGATIONS.md
