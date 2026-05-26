# Direction: Health and Beauty

Direction ID: `health-and-beauty`

Source of truth: GitHub repo `ainazemtsau/my_global_workflow` while `WORKFLOW_SOURCE_OF_TRUTH.md` says `active`.

The Direction root is an index, not the workflow state container.

Active workflow/proof state lives under:

- `directions/health-and-beauty/workflow/`

## Root Files

- `README.md`
- `AGENTS.md`
- `direction.meta.yml`

## Workflow

`workflow/` contains:

- `LEDGER.md`
- `OBLIGATIONS.md`
- `RECEIPTS_INDEX.md`
- `COMMIT_SCOPES.md`
- `DASHBOARD.md`
- `MIGRATION_RECEIPT.md`
- `project_setup/`
- `receipts/`
- `projections/`

## Archive

`archive/` contains legacy evidence and preserved result artifacts.

`archive/` is not accepted proof state.

Next run must be read from `workflow/DASHBOARD.md` and `workflow/OBLIGATIONS.md`.
