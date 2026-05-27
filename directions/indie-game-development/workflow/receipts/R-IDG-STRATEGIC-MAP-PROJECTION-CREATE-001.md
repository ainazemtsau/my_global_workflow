---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: projection_receipt
  status: accepted
  owner: proof_carrying_workflow_os
---

# Strategic Map Projection Create Receipt

## Receipt Control

```yaml
receipt_id: R-IDG-STRATEGIC-MAP-PROJECTION-CREATE-001
target_obligation: O-IDG-STRATEGIC-MAP-PROJECTION-CREATE
operator: Projection
status: accepted
created_projection:
  projection_id: IDG-STRATEGIC-PATH-MAP-PROJECTION-001
  path: directions/indie-game-development/workflow/projections/IDG_STRATEGIC_PATH_MAP_PROJECTION_001.md
source_receipt_ids:
  - R-IDG-ROOT-OBJECTIVE-DECISION-001
  - R-IDG-SUCCESS-SEMANTICS-DEFINE-001
  - R-IDG-CONSTRAINTS-DEFINE-001
projection_claim_boundary:
  all_claims_backed_or_marked: pass
  creates_truth: false
  creates_strategy_commitment: false
  creates_horizon: false
  creates_active_frontier: false
  creates_roadmap: false
  admits_product_execution: false
  imports_legacy: false
proposed_next_obligation:
  id: O-IDG-STRATEGIC-ROUTE-DECIDE
  status: proposed_for_open_next
```

## Not Accepted

```yaml
not_accepted:
  - Horizon
  - Active Frontier
  - roadmap
  - product execution
  - CodexExecution
  - Steam launch strategy
  - monetization model
  - exact revenue target
  - exact launch date
  - engine choice
  - legacy import
  - old concept/archive details
  - strategic commitment beyond accepted receipts
```

## Invariant Checks

```yaml
invariant_checks:
  one_obligation_scope: pass
  no_strategy_accepted: pass
  no_horizon_created: pass
  no_active_frontier_created: pass
  no_roadmap_created: pass
  no_execution_admitted: pass
  no_legacy_import_performed: pass
verification_result: pass
commit_scope: idg_projection_scope
terminal_recommendation: commit
```

END_OF_FILE: directions/indie-game-development/workflow/receipts/R-IDG-STRATEGIC-MAP-PROJECTION-CREATE-001.md
