# Indie Game Development

Direction ID: `indie-game-development`

Source of truth: GitHub repository markdown.

## Proof-Root Layout

Accepted proof state lives in these root files:

- `LEDGER.md`
- `OBLIGATIONS.md`
- `RECEIPTS_INDEX.md`
- `COMMIT_SCOPES.md`
- `DASHBOARD.md`
- `MIGRATION_RECEIPT.md`

Receipts live in `receipts/`.

Project setup lives in `project_setup/`.

The archive is `legacy_evidence` only. Do not load old archive files by default, and do not treat archived workflow folders as accepted live state.

Next valid runs are read from `DASHBOARD.md` and `OBLIGATIONS.md`.
