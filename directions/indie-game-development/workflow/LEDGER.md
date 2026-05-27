---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: ledger_storage
  status: post_inventory_orientation_frame_obligation_admitted
  owner: proof_carrying_workflow_os
---

# Indie Game Development Proof Ledger

## Ledger State

```yaml
direction_id: indie-game-development
proof_state: post_inventory_orientation_frame_obligation_admitted
accepted_receipts:
  - R-IDG-ROOT-OBJECTIVE-DECISION-001
  - R-IDG-SUCCESS-SEMANTICS-DEFINE-001
  - R-IDG-CONSTRAINTS-DEFINE-001
  - R-IDG-STRATEGIC-MAP-PROJECTION-CREATE-001
  - R-IDG-STRATEGIC-ROUTE-DECIDE-001
  - R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001
  - R-IDG-POST-INVENTORY-ORIENTATION-FRAME-ADMIT-001
accepted_claims:
  - Root objective accepted: create and finish an indie game within the already selected concept, with equal technical-pride and commercial-success pillars.
  - Success semantics accepted: full success requires technical-pride success, game-completion success, commercial success, and personal-pride success.
  - Constraints accepted: solo/AI-assisted capacity, 50-80 hours/week, lean budget with $1000 normal envelope and $3000 justified ceiling, 9-month income constraint, high risk tolerance bounded by gameplay depth, Steam-only distribution boundary, and workflow-driven marketing execution requirement.
  - Strategic Path Map Projection created as projection-only artifact; it creates no accepted strategy, Horizon, Active Frontier, roadmap, execution, monetization model, Steam launch strategy, or legacy import.
  - Strategic route decision accepted: next route is bounded legacy concept evidence inventory before concept-specific strategy decisions.
  - Legacy concept evidence inventory accepted as bounded evidence only: concept premise, gameplay core, gas simulation role, player fantasy candidate, genre/frame candidate, commercial hooks candidate, technical gameplay pillars, and explicit unknowns were inventoried. This creates no accepted strategy, Horizon, Active Frontier, roadmap, execution, monetization model, Steam launch strategy, engine commitment, networking stack decision, old-code transfer, or old Direction state authority.
  - Human decision accepted to admit O-IDG-POST-INVENTORY-ORIENTATION-FRAME as the next bounded obligation after accepted legacy concept evidence inventory. This creates no accepted strategy, roadmap, Horizon, Active Frontier, product execution, CodexExecution, Steam launch strategy, engine commitment, networking stack commitment, old-code transfer, or full legacy state import.
open_obligations_ref: directions/indie-game-development/workflow/OBLIGATIONS.md
commit_scopes_ref: directions/indie-game-development/workflow/COMMIT_SCOPES.md
projections_state: strategic_map_projection_created_no_strategy_commitment
legacy_import_state: bounded_concept_evidence_inventory_committed
legacy_state_authority: false
```

## Accepted Root Objective

Create and finish an indie game within the already selected concept, with two equal top-level outcomes: a technically strong game the user can be proud of, and a commercially successful product that can generate meaningful revenue.

## Accepted Root-Level Constraints

- Work within the already selected concept; do not restart concept discovery by default.
- Technical strength / technical ambition is a root-level value pillar.
- Commercial success / meaningful revenue is a root-level value pillar.
- Old concept/archive material remains legacy evidence only until admitted through valid workflow.

## Accepted Success Semantics

Full success requires all of the following:

- technical-pride success: A player-visible, gameplay-relevant, non-trivial technical core must be central to the game's value and robust enough to build the game around.
- game-completion success: The project must become a coherent playable game/product in the already selected concept, not remain only a research sandbox or isolated prototype.
- commercial success: The game must demonstrate real market value and a credible path to meaningful revenue, while exact revenue targets, channels, pricing, launch route, and timeline remain unresolved.
- personal-pride success: The user can reasonably be proud of the product because it combines distinctive technical identity, coherent gameplay, and commercial seriousness.

## Accepted Constraints

- Solo developer by default, with AI/Codex/workflow assistance allowed; no human team is assumed by default.
- Weekly time capacity is 50-80 hours/week for the game direction.
- Budget is low-spend by default, with current liquidity around $200, about $100/month going to ChatGPT, a normal envelope around $1000, and an extended ceiling up to $3000 only for clearly worthwhile/high-leverage expenses.
- Within 9 months from acceptance of this constraints receipt, the project should already generate some money/income/revenue flow.
- High risk tolerance is accepted, but no technology for technology's sake.
- Gameplay depth is more important than technical complexity by itself; technical systems, including gas simulation, must create interesting gameplay depth rather than pursue physical accuracy as an end in itself.
- Steam-only / PC-via-Steam is accepted as the current platform/distribution boundary.
- The user is willing to execute marketing/business tasks as needed, but the workflow must provide a clear process/playbook for what to do, where to publish, when to publish, and how to evaluate results.

## Unresolved / Not Accepted

- exact production/release schedule
- exact launch date
- exact revenue target
- exact profit definition
- exact monetization model
- pricing
- Steam launch strategy
- Steam tactics
- engine choice
- networking stack
- exact genre
- visual style
- specific algorithms/data models
- Codex execution readiness
- roadmap
- Horizon
- Active Frontier
- accepted Strategic Path Map commitments
- accepted strategy
- product execution
- full legacy state import

## Authority Boundary

This Ledger contains no imported old Direction facts.

The only committed legacy import state is the bounded concept evidence inventory accepted by `R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001`.

Old `project_files/00-08` are not accepted proof state.

Old archive files and old Direction files, including `archive/**` and `project_files/**`, remain legacy evidence only unless imported later through Legacy Import Receipt + Verify + Commit.

Direction proof files are storage and projection surfaces. They are not additional semantic primitives.

## Accepted Receipts

- R-IDG-ROOT-OBJECTIVE-DECISION-001
- R-IDG-SUCCESS-SEMANTICS-DEFINE-001
- R-IDG-CONSTRAINTS-DEFINE-001
- R-IDG-STRATEGIC-MAP-PROJECTION-CREATE-001
- R-IDG-STRATEGIC-ROUTE-DECIDE-001
- R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001
- R-IDG-POST-INVENTORY-ORIENTATION-FRAME-ADMIT-001

## Accepted Projection Artifacts

```yaml
- projection_id: IDG-STRATEGIC-PATH-MAP-PROJECTION-001
  path: directions/indie-game-development/workflow/projections/IDG_STRATEGIC_PATH_MAP_PROJECTION_001.md
  source_receipt_ids:
    - R-IDG-ROOT-OBJECTIVE-DECISION-001
    - R-IDG-SUCCESS-SEMANTICS-DEFINE-001
    - R-IDG-CONSTRAINTS-DEFINE-001
  creates_truth: false
```

## Current Work Boundary

Constraints are accepted by `R-IDG-CONSTRAINTS-DEFINE-001`.

Strategic Path Map Projection `IDG-STRATEGIC-PATH-MAP-PROJECTION-001` is created as a projection-only artifact.

Strategic route decision is accepted by `R-IDG-STRATEGIC-ROUTE-DECIDE-001`.

The route decision selected `A_LEGACY_CONCEPT_EVIDENCE_FIRST`.

The required inventory run `O-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY` is satisfied by `R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001`.

Old archive/project_files remain legacy evidence only.

Only bounded concept evidence inventory is accepted; old Direction state authority remains false.

O-IDG-POST-INVENTORY-ORIENTATION-FRAME is now the single admitted next bounded obligation. It may produce an orientation frame only; it must not select strategy, Horizon, Active Frontier, roadmap, or execution.

No next strategy state, roadmap, Horizon, Active Frontier, execution package, Codex work package, product execution, monetization model, Steam launch strategy, engine commitment, networking stack decision, old-code transfer, or accepted Strategic Path Map commitment is created or admitted by this receipt.

END_OF_FILE: directions/indie-game-development/workflow/LEDGER.md
