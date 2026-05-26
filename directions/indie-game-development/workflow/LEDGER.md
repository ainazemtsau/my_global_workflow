---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: ledger_storage
  status: root_objective_accepted
  owner: proof_carrying_workflow_os
---

# Indie Game Development Proof Ledger

## Ledger State

```yaml
direction_id: indie-game-development
proof_state: root_objective_accepted
accepted_receipts:
  - R-IDG-ROOT-OBJECTIVE-DECISION-001
  - R-IDG-SUCCESS-SEMANTICS-DEFINE-001
accepted_claims:
  - Root objective accepted: create and finish an indie game within the already selected concept, with equal technical-pride and commercial-success pillars.
  - Success semantics accepted: full success requires technical-pride success, game-completion success, commercial success, and personal-pride success.
open_obligations_ref: directions/indie-game-development/workflow/OBLIGATIONS.md
commit_scopes_ref: directions/indie-game-development/workflow/COMMIT_SCOPES.md
projections_state: root_objective_accepted_no_strategy_projection
legacy_import_state: not_performed
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

## Unresolved / Not Accepted

- hard technical constraints
- hard product constraints
- team/time/budget constraints
- risk tolerance
- platform target
- release ambition
- engine choice
- networking stack
- exact genre
- monetization
- timeline
- visual style
- launch strategy
- specific algorithms/data models
- Codex execution readiness
- roadmap
- Horizon
- Active Frontier
- Strategic Path Map
- strategy
- product execution
- legacy import

## Authority Boundary

This Ledger contains no imported old Direction facts.

Old `project_files/00-08` are not accepted proof state.

Old archive files and old Direction files, including `archive/**` and `project_files/**`, remain legacy evidence only unless imported later through Legacy Import Receipt + Verify + Commit.

Direction proof files are storage and projection surfaces. They are not additional semantic primitives.

## Accepted Receipts

- R-IDG-ROOT-OBJECTIVE-DECISION-001
- R-IDG-SUCCESS-SEMANTICS-DEFINE-001

## Current Work Boundary

The next required run is `O-IDG-CONSTRAINTS-DEFINE`.

No Strategic Path Map, Horizon, Active Frontier, Roadmap, strategy, constraints, execution package, Codex work package, product execution, monetization, launch strategy, or legacy import is created or admitted by this success-semantics receipt.

END_OF_FILE: directions/indie-game-development/workflow/LEDGER.md
