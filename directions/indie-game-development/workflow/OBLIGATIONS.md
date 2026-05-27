---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: obligations_storage
  status: strategic_route_decision_accepted
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

### O-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY

```yaml
obligation_id: O-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY
type: legacy_import
statement: >
  Inspect old Indie Game Development concept/archive material as legacy evidence only,
  extracting bounded concept facts needed for future strategy: concept premise,
  gameplay core, gas simulation role, player fantasy, genre/frame, commercial hooks,
  technical gameplay pillars, and explicit unknowns.
status: open_next
priority: critical
required_operator:
  - LegacyImport
boundaries:
  - evidence inventory only
  - no old Direction Map as truth
  - no old Active Goal as current obligation
  - no old Current Phase as current state
  - no old Portfolio Queue as backlog
  - no old roadmap import
  - no product execution
  - no CodexExecution
  - no Horizon selection
  - no Active Frontier selection
  - no Steam launch strategy
  - no engine commitment
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

### O-IDG-STRATEGIC-ROUTE-DECIDE

```yaml
obligation_id: O-IDG-STRATEGIC-ROUTE-DECIDE
type: human_decision
statement: Decide which strategic route to admit next from the projection map, without selecting Horizon, Active Frontier, roadmap, or execution.
status: satisfied
priority: critical
satisfied_by: R-IDG-STRATEGIC-ROUTE-DECIDE-001
accepted_result:
  selected_route: A_LEGACY_CONCEPT_EVIDENCE_FIRST
  next_obligation: O-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY
  no_legacy_facts_imported: true
  no_strategy: true
  no_horizon: true
  no_active_frontier: true
  no_roadmap: true
  no_execution: true
required_operator:
  - HumanDecision
```

### O-IDG-STRATEGIC-MAP-PROJECTION-CREATE

```yaml
obligation_id: O-IDG-STRATEGIC-MAP-PROJECTION-CREATE
type: projection
statement: Run the projection-only strategic path map step from accepted proof state; do not create Horizon, Active Frontier, roadmap, or product execution.
status: satisfied
priority: critical
satisfied_by: R-IDG-STRATEGIC-MAP-PROJECTION-CREATE-001
accepted_result:
  projection_id: IDG-STRATEGIC-PATH-MAP-PROJECTION-001
  projection_only: true
  no_horizon: true
  no_active_frontier: true
  no_roadmap: true
  no_execution: true
  no_legacy_import: true
required_operator:
  - Projection
```

### O-IDG-CONSTRAINTS-DEFINE

```yaml
obligation_id: O-IDG-CONSTRAINTS-DEFINE
type: clarify
statement: Define hard constraints for the direction such as solo capacity, time, budget, acceptable risk, preferred product domain, and execution boundaries.
status: satisfied
priority: critical
satisfied_by: R-IDG-CONSTRAINTS-DEFINE-001
accepted_result:
  constraints:
    - solo developer by default, with AI/Codex/workflow assistance allowed and no human team assumed by default
    - 50-80 hours/week available for the game direction
    - low-spend default with about $200 current liquidity, about $100/month ChatGPT spend, $1000 normal budget envelope, and up to $3000 justified ceiling
    - income/revenue flow should exist within 9 months of accepting the constraints receipt, while exact amount, pricing, launch date, and monetization model remain unresolved
    - high risk tolerance accepted, bounded by no technology for technology's sake
    - gameplay depth is more important than technical complexity or physical accuracy for its own sake
    - Steam-only / PC-via-Steam accepted as platform/distribution boundary
    - marketing/business execution is allowed, but requires a workflow-provided playbook for actions, publishing, timing, and evaluation
required_operator:
  - ClarifyObjective
```

### O-IDG-SUCCESS-SEMANTICS-DEFINE

```yaml
obligation_id: O-IDG-SUCCESS-SEMANTICS-DEFINE
type: clarify
statement: Define what success means for this direction before strategy or execution.
status: satisfied
priority: critical
satisfied_by: R-IDG-SUCCESS-SEMANTICS-DEFINE-001
accepted_result:
  success_requires_all:
    - technical_pride_success
    - game_completion_success
    - commercial_success
    - personal_pride_success
required_operator:
  - ClarifyObjective
```

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

None.

## Execution Boundary

No CodexExecution/product execution Obligations are admitted.

No CodexExecution operator may run.

No roadmap item exists without admitted Obligation.

Execution remains unavailable until required constraints, strategy, and execution-ready precondition Receipts are accepted and committed.

END_OF_FILE: directions/indie-game-development/workflow/OBLIGATIONS.md
