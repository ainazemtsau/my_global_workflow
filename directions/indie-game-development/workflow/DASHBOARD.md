---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: dashboard_projection
  status: initialized_skeleton
  owner: proof_carrying_workflow_os
---

# Indie Game Development Dashboard

## Projection Warning

Dashboard is projection, not truth; Ledger wins.

This dashboard reflects initialized skeleton state and does not create new accepted claims.

## Current State

```yaml
direction: Indie Game Development
proof_state: initialized skeleton / no accepted root objective
accepted_root_objective: null
accepted_receipts: []
legacy_import_state: not_performed
```

## Accepted Root Objective

None.

## Accepted Root-Level Constraints

None.

## Open Critical Obligations

- O-IDG-ROOT-OBJECTIVE-CONFIRM

## Optional Available Obligation

- O-IDG-LEGACY-INVENTORY-OPTIONAL

## Blocked Obligations

- O-IDG-SUCCESS-SEMANTICS-DEFINE
- O-IDG-CONSTRAINTS-DEFINE
- O-IDG-STRATEGIC-MAP-PROJECTION-CREATE

## Forbidden Now

- Strategic Path Map
- Horizon selection
- Active Frontier selection
- Roadmap
- success semantics run
- constraints run
- Codex/product execution
- Steam/game/product implementation

## Next Valid Runs

- ClarifyObjective over `O-IDG-ROOT-OBJECTIVE-CONFIRM` only

## Unavailable Projections

Success semantics and constraints runs: blocked until root objective is accepted.

Strategic Path Map projection: blocked until root objective, success semantics, and constraints are defined by accepted Receipts.

Horizon projection: unavailable until committed orientation state exists.

Active Frontier view: unavailable until constraints and open Obligation eligibility can be computed from accepted Receipts.

END_OF_FILE: directions/indie-game-development/workflow/DASHBOARD.md
