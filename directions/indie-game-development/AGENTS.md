# Indie Game Development Direction Instructions

Status: active

Direction scope is `directions/indie-game-development/**`.

## Live State

Live accepted state comes only from the root proof files:

- `LEDGER.md`
- `OBLIGATIONS.md`
- `RECEIPTS_INDEX.md`
- `COMMIT_SCOPES.md`
- `DASHBOARD.md`
- `MIGRATION_RECEIPT.md`

Receipts live in `receipts/`.

Project files and caches do not create accepted state.

Archive files are `legacy_evidence` only. Old workflow folders are not accepted state.

## Boundaries

- No Legacy Import unless a future admitted Obligation explicitly asks for it.
- No roadmap, Horizon, Active Frontier, or product execution unless accepted Receipts and admitted Obligations authorize them.
- Do not treat archived Direction files, old setup text, old workflow folders, execution logs, or product documents as accepted proof state.
- Repository maintenance is allowed only under handoff `CODEX-IDG-PROOF-ROOT-CLEANUP-2026-05-26`.

## Change Rules

- Use small diffs.
- Keep edits inside `directions/indie-game-development/**`.
- Do not modify other Direction folders.
- Do not modify external product repositories.
