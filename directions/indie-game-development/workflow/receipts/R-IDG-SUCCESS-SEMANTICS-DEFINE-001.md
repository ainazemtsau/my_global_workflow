---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: receipt
  status: accepted
  owner: proof_carrying_workflow_os
---

# Success Semantics Definition Receipt

```yaml
receipt_id: R-IDG-SUCCESS-SEMANTICS-DEFINE-001
target_obligation: O-IDG-SUCCESS-SEMANTICS-DEFINE
operator: ClarifyObjective
status: accepted
accepted_success_semantics:
  success_requires_all:
    - technical_pride_success
    - game_completion_success
    - commercial_success
    - personal_pride_success
  technical_pride_success: >
    A player-visible, gameplay-relevant, non-trivial technical core must be central
    to the game's value and robust enough to build the game around.
  game_completion_success: >
    The project must become a coherent playable game/product in the already selected
    concept, not remain only a research sandbox or isolated prototype.
  commercial_success: >
    The game must demonstrate real market value and a credible path to meaningful
    revenue, while exact revenue targets, channels, pricing, launch route, and
    timeline remain unresolved.
  personal_pride_success: >
    The user can reasonably be proud of the product because it combines distinctive
    technical identity, coherent gameplay, and commercial seriousness.
not_accepted:
  - exact revenue target
  - exact timeline commitment
  - exact monetization channel
  - launch strategy
  - marketing strategy
  - roadmap
  - Horizon
  - Active Frontier
  - engine choice
  - implementation plan
  - legacy concept details
parked_residual_context:
  - user wants eventual commercial income, ideally within 3-6 or 3-9 months
  - candidate channels include Steam, Patreon, Kickstarter, Discord, YouTube, but none are commitments
  - user lacks business/marketing/audience-building expertise
  - concept-specific success criteria may require future LegacyImport
invariant_checks:
  one_obligation_scope: pass
  no_strategy_created: pass
  no_roadmap_created: pass
  no_execution_admitted: pass
  no_legacy_import_performed: pass
verification_result: pass
commit_scope: idg_root_scope
terminal_recommendation: commit
```

END_OF_FILE: directions/indie-game-development/workflow/receipts/R-IDG-SUCCESS-SEMANTICS-DEFINE-001.md
