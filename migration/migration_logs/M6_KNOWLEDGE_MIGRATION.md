# M6 Knowledge Migration

Status: PASS_WITH_NONBLOCKING_NOTES
Updated at: 2026-05-11 10:52:00 +03:00

## Scope

M6 migrated high-confidence manifest items categorized as reusable knowledge, canon, decisions, patterns, or reviews.

## Items migrated

- Migrated manifest-backed knowledge-like items: 19
- Items with source content unavailable: 0
- Items needing user export: 0

## Items not migrated

- `Solo Max Productive / Archive / 07 Reviews / Knowledge / Canon / Current State Summary - Workflow vNext Transition` was reclassified as `duplicate_superseded` because its body contains obsolete source-of-truth rules that conflict with the active GitHub-only runtime policy.

## Files created

- `directions/health-and-beauty/knowledge/canon/07-reviews-knowledge-canon.md`
- `directions/health-and-beauty/phases/05-phase-review.md`
- `directions/indie-game-development/knowledge/canon/07-reviews-knowledge-canon.md`
- `directions/indie-game-development/knowledge/canon/charter.md`
- `directions/indie-game-development/knowledge/canon/thesis.md`
- `directions/indie-game-development/knowledge/canon/canon.md`
- `directions/indie-game-development/knowledge/canon/gas-and-grid-are-peer-foundation.md`
- `directions/indie-game-development/knowledge/canon/game-truth-must-leave-goal-local-notes.md`
- `directions/indie-game-development/knowledge/canon/steelman-rejected-alternatives-before-product-bet-decision.md`
- `directions/indie-game-development/knowledge/canon/separate-bet-commitments-from-proof-design-material.md`
- `directions/indie-game-development/knowledge/canon/knowledge.md`
- `directions/indie-game-development/knowledge/canon/canon-candidates.md`
- `directions/indie-game-development/knowledge/canon/foundation-goals-lockable-artifacts.md`
- `directions/indie-game-development/knowledge/canon/bounded-output-contract-for-upstream-shaping.md`
- `directions/indie-game-development/phases/05-phase-review.md`
- `directions/solo-max-productive/knowledge/canon/07-reviews-knowledge-canon.md`
- `directions/solo-max-productive/knowledge/canon/canon.md`
- `directions/solo-max-productive/knowledge/canon/knowledge.md`
- `directions/solo-max-productive/knowledge/canon/canon-candidates.md`

## Files updated

- `directions/solo-max-productive/AGENTS.md`
- `directions/indie-game-development/AGENTS.md`
- `directions/health-and-beauty/AGENTS.md`
- `migration/migration_manifests/solo-max-productive_manifest.yml`
- `migration/MIGRATION_STATE.md`

## Validation

- Every remaining `migrate_to_github` knowledge-like manifest item has a target GitHub file.
- No generated Direction runtime files mention Trilium or legacy source paths.
- No canon was invented; empty source bodies became empty canonical index files.
- Existing `needs_user_decision` items remain visible in manifests/state.
- Direction `AGENTS.md` files point to `knowledge/` as canonical reusable context.

## Next step

Next allowed step after validation: M7 Domain Documentation Migration.
