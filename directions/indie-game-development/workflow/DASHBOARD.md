---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: dashboard_projection
  status: post_inventory_orientation_frame_committed
  owner: proof_carrying_workflow_os
---

# Indie Game Development Dashboard

## Projection Warning

Dashboard is projection, not truth; Ledger wins.

This dashboard reflects constraints accepted state, a projection-only artifact, an accepted route decision, a completed bounded legacy concept evidence inventory, and a completed bounded post-inventory orientation frame. It does not create strategy commitment.

## Current State

```yaml
direction: Indie Game Development
proof_state: post_inventory_orientation_frame_committed
accepted_root_objective: >
  Create and finish an indie game within the already selected concept, with two equal
  top-level outcomes: a technically strong game the user can be proud of, and a
  commercially successful product that can generate meaningful revenue.
accepted_receipts:
  - R-IDG-ROOT-OBJECTIVE-DECISION-001
  - R-IDG-SUCCESS-SEMANTICS-DEFINE-001
  - R-IDG-CONSTRAINTS-DEFINE-001
  - R-IDG-STRATEGIC-MAP-PROJECTION-CREATE-001
  - R-IDG-STRATEGIC-ROUTE-DECIDE-001
  - R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001
  - R-IDG-POST-INVENTORY-ORIENTATION-FRAME-ADMIT-001
  - R-IDG-POST-INVENTORY-ORIENTATION-FRAME-001
projection_artifact:
  - IDG-STRATEGIC-PATH-MAP-PROJECTION-001
route_decision:
  selected_route: A_LEGACY_CONCEPT_EVIDENCE_FIRST
  satisfied_obligation: O-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY
  legacy_facts_imported: bounded_concept_evidence_inventory_only
orientation_frame:
  satisfied_obligation: O-IDG-POST-INVENTORY-ORIENTATION-FRAME
  satisfied_by: R-IDG-POST-INVENTORY-ORIENTATION-FRAME-001
  result_kind: bounded_post_inventory_orientation_frame
open_next_obligations: []
next_valid_runs_admitted_by_this_receipt: []
legacy_import_state: bounded_concept_evidence_inventory_committed
legacy_state_authority: false
strategy_admitted: false
roadmap_admitted: false
horizon_selected: false
active_frontier_selected: false
product_execution_admitted: false
codex_execution_admitted: false
steam_launch_strategy_admitted: false
engine_commitment_admitted: false
networking_stack_commitment_admitted: false
old_code_transfer_admitted: false
```

## Accepted Root Objective

Create and finish an indie game within the already selected concept, with two equal top-level outcomes: a technically strong game the user can be proud of, and a commercially successful product that can generate meaningful revenue.

## Accepted Root-Level Constraints

- Work within the already selected concept; do not restart concept discovery by default.
- Technical strength / technical ambition is a root-level value pillar.
- Commercial success / meaningful revenue is a root-level value pillar.
- Old concept/archive material remains legacy evidence only until admitted through valid workflow.

## Accepted Success Semantics

Full success requires technical-pride success, game-completion success, commercial success, and personal-pride success.

## Accepted Constraints

- Solo developer by default, with AI/Codex/workflow assistance allowed; no human team assumed by default.
- Weekly time capacity is 50-80 hours/week.
- Budget is low-spend by default: current liquidity approximately $200, about $100/month ChatGPT spend, normal envelope around $1000, and extended ceiling up to $3000 only for clearly worthwhile/high-leverage expenses.
- The project should generate some money/income/revenue flow within 9 months from acceptance of `R-IDG-CONSTRAINTS-DEFINE-001`.
- High risk tolerance is accepted, but no technology for technology's sake.
- Gameplay depth outranks technical complexity by itself; systems such as gas simulation must create interesting gameplay depth rather than pursue physical accuracy for its own sake.
- Steam-only / PC-via-Steam is accepted as the platform/distribution boundary.
- Marketing/business execution is allowed, but the workflow must provide a clear process/playbook for actions, publishing locations, timing, and result evaluation.

## Boundary Notes

- Steam-only target is accepted.
- Steam launch strategy is not accepted.
- Unity plugin ownership is candidate context, not engine commitment.
- Bounded legacy concept evidence inventory is completed; old Direction state authority remains false.
- O-IDG-POST-INVENTORY-ORIENTATION-FRAME is satisfied by `R-IDG-POST-INVENTORY-ORIENTATION-FRAME-001`.
- No next obligation is admitted by the orientation frame receipt.

## Projection Artifact Summary

- IDG-STRATEGIC-PATH-MAP-PROJECTION-001: projection-only Strategic Path Map artifact from accepted root objective, success semantics, and constraints; creates no accepted strategy, Horizon, Active Frontier, roadmap, execution, Steam launch strategy, monetization model, or legacy import.

## Accepted Route Decision

- selected route: A_LEGACY_CONCEPT_EVIDENCE_FIRST
- satisfied obligation: O-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY
- bounded concept evidence inventory committed by `R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001`
- no old Direction state authority imported
- no strategy, roadmap, Horizon, Active Frontier, product execution, CodexExecution, Steam launch strategy, engine commitment, networking stack commitment, or old-code transfer admitted

## Satisfied Obligations

- O-IDG-POST-INVENTORY-ORIENTATION-FRAME satisfied by `R-IDG-POST-INVENTORY-ORIENTATION-FRAME-001`.
- O-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY satisfied by `R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001`.
- O-IDG-STRATEGIC-ROUTE-DECIDE satisfied by `R-IDG-STRATEGIC-ROUTE-DECIDE-001`.
- O-IDG-STRATEGIC-MAP-PROJECTION-CREATE satisfied by `R-IDG-STRATEGIC-MAP-PROJECTION-CREATE-001`.

## Open Critical Obligations

None.

## Open Next Obligations

None.

## Optional Available Obligation

- O-IDG-LEGACY-INVENTORY-OPTIONAL

## Blocked Obligations

None.

## Forbidden Now

- accepting old legacy facts before LegacyImport receipt
- strategy beyond committed receipts
- Horizon selection
- Active Frontier selection
- Roadmap
- CodexExecution/product execution
- Steam/game/product implementation
- Steam launch strategy
- engine commitment
- networking stack commitment
- old-code transfer

## Candidate Safe Route Classes

All route classes below are candidate/proposed only and are not admitted obligations.

- Concept Identity Clarification
- Technical Gameplay Evidence Gap Audit
- Commercial Hook Evidence Gap Audit
- Legacy Code/Test Value Audit
- Strategy Admission Decision
- Horizon Projection Eligibility Audit

## Next Valid Runs

None admitted by this receipt.

## Projection Availability

Constraints run: satisfied by `R-IDG-CONSTRAINTS-DEFINE-001`.

Strategic Path Map projection: created as `IDG-STRATEGIC-PATH-MAP-PROJECTION-001`; no accepted strategy commitment is created.

Horizon projection: candidate/eligibility-dependent only; not selected and not admitted.

Active Frontier view: candidate/eligibility-dependent only; not selected and not admitted.

END_OF_FILE: directions/indie-game-development/workflow/DASHBOARD.md
