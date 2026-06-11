# Indie Game Development Direction Instructions

Status: active

Direction scope is `directions/indie-game-development/**`.

## Live State

Live workflow state is under `directions/indie-game-development/workflow/`.

Accepted state comes from `workflow/LEDGER.md` plus committed receipts.

`workflow/DASHBOARD.md` is a projection, not truth.

Project setup files and runtime caches do not create accepted state.

Archive files are `legacy_evidence` only.

## Boundaries

- No Legacy Import unless an admitted Obligation explicitly asks for it.
- No roadmap, Horizon, Active Frontier, execution obligation, CodexRun, or product execution unless accepted Receipts and admitted Obligations authorize them.
- Do not treat archived Direction files, old setup text, old workflow folders, execution logs, or product documents as accepted proof state.
- Repository maintenance must keep root clean.

## Change Rules

- Use small diffs.
- Keep edits inside `directions/indie-game-development/**`.
- Do not modify other Direction folders.
- Do not modify external product repositories.
