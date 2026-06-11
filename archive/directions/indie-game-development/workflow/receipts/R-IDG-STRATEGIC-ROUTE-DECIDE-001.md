---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: receipt
  status: accepted
  owner: proof_carrying_workflow_os
---

# Strategic Route Decision Receipt

```yaml
receipt_id: R-IDG-STRATEGIC-ROUTE-DECIDE-001
target_obligation: O-IDG-STRATEGIC-ROUTE-DECIDE
operator: HumanDecision
status: accepted
selected_route:
  id: A_LEGACY_CONCEPT_EVIDENCE_FIRST
  decision: >
    Open a bounded LegacyImport route to inspect old Indie Game Development
    concept material as legacy evidence only before making concept-specific
    strategy decisions.
accepted_decision_effect:
  - O-IDG-STRATEGIC-ROUTE-DECIDE is satisfied.
  - O-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY is opened as the next bounded obligation.
  - Legacy evidence may be inspected only under the new bounded LegacyImport obligation.
  - No old fact is accepted by this decision.
next_obligation_to_open:
  obligation_id: O-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY
  type: legacy_import
  operator: LegacyImport
  statement: >
    Inspect old Indie Game Development concept/archive material as legacy evidence only,
    extracting bounded concept facts needed for future strategy: concept premise,
    gameplay core, gas simulation role, player fantasy, genre/frame, commercial hooks,
    technical gameplay pillars, and explicit unknowns.
  boundaries:
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
not_accepted:
  - legacy facts themselves
  - accepted strategy
  - Horizon
  - Active Frontier
  - roadmap
  - product execution
  - CodexExecution
  - Steam launch strategy
  - monetization model
  - exact launch date
  - engine choice
  - old project execution state
invariant_checks:
  one_obligation_scope: pass
  no_legacy_facts_imported: pass
  no_strategy_accepted: pass
  no_horizon_created: pass
  no_active_frontier_created: pass
  no_roadmap_created: pass
  no_execution_admitted: pass
verification_result: pass
commit_scope: idg_strategy_scope
terminal_recommendation: commit
```

END_OF_FILE: directions/indie-game-development/workflow/receipts/R-IDG-STRATEGIC-ROUTE-DECIDE-001.md
