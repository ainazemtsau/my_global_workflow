---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: receipts_index
  status: legacy_concept_evidence_inventory_committed
  owner: proof_carrying_workflow_os
---

# Indie Game Development Receipts Index

## Receipt State

```yaml
root_state: legacy_concept_evidence_inventory_committed
accepted_receipts:
  - receipt_id: R-IDG-ROOT-OBJECTIVE-DECISION-001
    path: receipts/R-IDG-ROOT-OBJECTIVE-DECISION-001.md
    summary: Accepted root objective for technically strong and commercially successful indie game within the already selected concept.
  - receipt_id: R-IDG-SUCCESS-SEMANTICS-DEFINE-001
    path: receipts/R-IDG-SUCCESS-SEMANTICS-DEFINE-001.md
    summary: Accepted success semantics for technical-pride, game-completion, commercial, and personal-pride success.
  - receipt_id: R-IDG-CONSTRAINTS-DEFINE-001
    path: receipts/R-IDG-CONSTRAINTS-DEFINE-001.md
    summary: Accepted hard constraints for solo capacity, 50-80 hours/week, lean budget, 9-month income pressure, high risk bounded by gameplay depth, Steam-only distribution, and workflow-driven marketing execution.
  - receipt_id: R-IDG-STRATEGIC-MAP-PROJECTION-CREATE-001
    path: receipts/R-IDG-STRATEGIC-MAP-PROJECTION-CREATE-001.md
    summary: Created Strategic Path Map Projection v0 as a projection-only artifact from accepted root objective, success semantics, and constraints.
  - receipt_id: R-IDG-STRATEGIC-ROUTE-DECIDE-001
    path: receipts/R-IDG-STRATEGIC-ROUTE-DECIDE-001.md
    summary: Accepted route decision to perform bounded legacy concept evidence inventory next.
  - receipt_id: R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001
    path: receipts/R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001.md
    summary: Accepted bounded legacy concept evidence inventory without importing old Direction state, strategy, roadmap, Horizon, Active Frontier, product execution, Steam launch strategy, engine commitment, networking stack decision, or old-code transfer.
candidate_receipts: []
rejected_receipts: []
receipt_storage_path: receipts/
```

## Accepted Receipts

- receipt_id: R-IDG-ROOT-OBJECTIVE-DECISION-001
  path: receipts/R-IDG-ROOT-OBJECTIVE-DECISION-001.md
  summary: Accepted root objective for technically strong and commercially successful indie game within the already selected concept.

- receipt_id: R-IDG-SUCCESS-SEMANTICS-DEFINE-001
  path: receipts/R-IDG-SUCCESS-SEMANTICS-DEFINE-001.md
  summary: Accepted success semantics for technical-pride, game-completion, commercial, and personal-pride success.

- receipt_id: R-IDG-CONSTRAINTS-DEFINE-001
  path: receipts/R-IDG-CONSTRAINTS-DEFINE-001.md
  summary: Accepted hard constraints for solo capacity, 50-80 hours/week, lean budget, 9-month income pressure, high risk bounded by gameplay depth, Steam-only distribution, and workflow-driven marketing execution.

- receipt_id: R-IDG-STRATEGIC-MAP-PROJECTION-CREATE-001
  path: receipts/R-IDG-STRATEGIC-MAP-PROJECTION-CREATE-001.md
  summary: Created Strategic Path Map Projection v0 as a projection-only artifact from accepted root objective, success semantics, and constraints.

- receipt_id: R-IDG-STRATEGIC-ROUTE-DECIDE-001
  path: receipts/R-IDG-STRATEGIC-ROUTE-DECIDE-001.md
  summary: Accepted route decision to perform bounded legacy concept evidence inventory next.

- receipt_id: R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001
  path: receipts/R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001.md
  summary: Accepted bounded legacy concept evidence inventory without importing old Direction state, strategy, roadmap, Horizon, Active Frontier, product execution, Steam launch strategy, engine commitment, networking stack decision, or old-code transfer.

## Rules

No receipt -> no progress.

Receipt is candidate until Verify + Commit.

Accepted Receipts are Ledger authority only after Commit.

No full legacy state import Receipt exists.

The only accepted legacy import Receipt is bounded concept evidence inventory.

Accepted strategic decision receipt exists for route selection only. Projection receipt exists but creates no strategy commitment.

END_OF_FILE: directions/indie-game-development/workflow/RECEIPTS_INDEX.md
