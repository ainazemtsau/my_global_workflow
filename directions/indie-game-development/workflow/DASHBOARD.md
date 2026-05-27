---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: dashboard_projection
  status: strategic_map_projection_created_no_strategy_commitment
  owner: proof_carrying_workflow_os
---

# Indie Game Development Dashboard

## Projection Warning

Dashboard is projection, not truth; Ledger wins.

This dashboard reflects constraints accepted state plus a projection-only artifact and does not create strategy commitment.

## Current State

```yaml
direction: Indie Game Development
proof_state: constraints accepted
accepted_root_objective: >
  Create and finish an indie game within the already selected concept, with two equal
  top-level outcomes: a technically strong game the user can be proud of, and a
  commercially successful product that can generate meaningful revenue.
accepted_receipts:
  - R-IDG-ROOT-OBJECTIVE-DECISION-001
  - R-IDG-SUCCESS-SEMANTICS-DEFINE-001
  - R-IDG-CONSTRAINTS-DEFINE-001
  - R-IDG-STRATEGIC-MAP-PROJECTION-CREATE-001
projection_artifact:
  - IDG-STRATEGIC-PATH-MAP-PROJECTION-001
legacy_import_state: not_performed
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

## Projection Artifact Summary

- IDG-STRATEGIC-PATH-MAP-PROJECTION-001: projection-only Strategic Path Map artifact from accepted root objective, success semantics, and constraints; creates no accepted strategy, Horizon, Active Frontier, roadmap, execution, Steam launch strategy, monetization model, or legacy import.

## Satisfied Obligations

- O-IDG-STRATEGIC-MAP-PROJECTION-CREATE satisfied by `R-IDG-STRATEGIC-MAP-PROJECTION-CREATE-001`.

## Open Critical Obligations

None.

## Open Next Obligations

- O-IDG-STRATEGIC-ROUTE-DECIDE

## Optional Available Obligation

- O-IDG-LEGACY-INVENTORY-OPTIONAL

## Blocked Obligations

None.

## Forbidden Now

- Horizon selection
- Active Frontier selection
- Roadmap
- Codex/product execution
- Steam/game/product implementation
- accepted strategy claims beyond committed receipts

## Next Valid Runs

- HumanDecision over `O-IDG-STRATEGIC-ROUTE-DECIDE`
- optional LegacyImport over `O-IDG-LEGACY-INVENTORY-OPTIONAL` only if explicitly selected

## Projection Availability

Constraints run: satisfied by `R-IDG-CONSTRAINTS-DEFINE-001`.

Strategic Path Map projection: created as `IDG-STRATEGIC-PATH-MAP-PROJECTION-001`; no accepted strategy commitment is created.

Horizon projection: unavailable until committed orientation state exists.

Active Frontier view: unavailable until projection eligibility can be computed from accepted Receipts.

END_OF_FILE: directions/indie-game-development/workflow/DASHBOARD.md
