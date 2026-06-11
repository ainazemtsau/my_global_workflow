# Workflow Governance Direction Instructions

Status: active

Direction path: `directions/workflow-governance`

Use `directions/workflow-governance/workflow/` for live Workflow Governance state.

## Active Authority

- Live state comes from `workflow/LEDGER.md`, `workflow/OBLIGATIONS.md`, `workflow/RECEIPTS_INDEX.md`, `workflow/COMMIT_SCOPES.md`, `workflow/DASHBOARD.md`, `workflow/MIGRATION_RECEIPT.md`, committed `workflow/receipts/`, and `workflow/projections/`.
- Only committed Receipts in the Ledger create accepted proof state.
- Root files are navigation/setup metadata only.
- Project setup files are runtime cache/setup instructions, not accepted state.

## Legacy Boundary

- Do not use old `project_files/00-08` or old vNext-R files as accepted state.
- `archive/` is legacy or candidate evidence only.
- Do not perform Legacy Import unless an admitted Obligation explicitly authorizes it.
- Do not invent Direction proof state from legacy material.

## Execution Boundary

- Do not create a roadmap, select Horizon, select Active Frontier, admit execution obligations, or run product execution from this Direction unless a committed Obligation explicitly admits that work.
- Repository maintenance is allowed only when explicitly requested and must stay within the named allowed paths.
- Do not touch sibling Direction folders or product repositories unless the current task explicitly names them.

## Change Rules

- Use small diffs.
- Preserve Receipt -> Verify -> Commit -> Ledger update.
- Report changed files, validation evidence, and separated project refresh requirements after edits, including Project Instructions UI payload character counts when instruction sources change.
