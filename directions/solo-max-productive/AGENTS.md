# Solo Max Productive Direction Instructions

Status: active

Direction path: `directions/solo-max-productive`

Source of truth: GitHub repository markdown in `ainazemtsau/my_global_workflow`.

## Scope

Allowed by default:
- `directions/solo-max-productive/**`

Forbidden unless explicitly requested:
- `workflow/**`
- root workflow files and shared pack directories
- `directions/workflow-governance/**`
- `directions/indie-game-development/**`
- `directions/health-and-beauty/**`
- product repositories or external project files

## Authority

- Root-level proof payload files are the default Direction authority:
  `LEDGER.md`, `OBLIGATIONS.md`, `RECEIPTS_INDEX.md`, `COMMIT_SCOPES.md`,
  `DASHBOARD.md`, and `MIGRATION_RECEIPT.md`.
- Use shared root workflow files and project packs only when a task explicitly
  needs shared packs, transport, setup validation, or execution harness context.
- `archive/` is legacy evidence only. It is not accepted proof state and is not
  default-loaded.

## Runtime Rules

- Do not use external personal notes as workflow source.
- Do not routinely load migration/admin files.
- Do not invent Direction state, accepted Receipts, accepted claims, root
  objective, Horizon, Active Frontier, roadmap, project metadata, repo URLs,
  local paths, or execution state.
- If required state is missing, return `NEEDS_INPUT` with the exact GitHub path needed.
- Only verified Receipts committed to root `LEDGER.md` create accepted state for
  this Direction.
- Do not perform Legacy Import unless explicitly requested by an admitted
  Obligation.
- Reusable Direction knowledge, canon, decisions, patterns, and reviews belong in `knowledge/` and are canonical only when present as GitHub files.
- Domain documentation belongs in `domain_docs/`; do not invent domain canon when a required file is missing.
- Project metadata belongs in `projects/` and `direction.meta.yml`; unknown repos stay `not_created` / `needs_user_input`.

## Change Rules

- Use small diffs.
- Do not delete files without explicit approval or a migration manifest replacement route.
- Do not modify other Direction folders unless the task explicitly names them.
- Do not copy stage prompts into Direction files.
- Report changed files and validation evidence after edits.
