# Workflow Governance Direction

Workflow Governance is the self-hosted Direction for maintaining the Workflow OS.

The Direction root is a navigation layer. Root markdown and metadata files do not create accepted state.

## Root Files

- `README.md`
- `AGENTS.md`
- `direction.meta.yml`

## Active Workflow State

Accepted proof workflow state lives under `workflow/`:

- `workflow/LEDGER.md`
- `workflow/OBLIGATIONS.md`
- `workflow/RECEIPTS_INDEX.md`
- `workflow/COMMIT_SCOPES.md`
- `workflow/DASHBOARD.md`
- `workflow/MIGRATION_RECEIPT.md`
- `workflow/receipts/`
- `workflow/projections/`
- `workflow/project_setup/`

Only verified Receipts committed to `workflow/LEDGER.md` create accepted state. Documents, setup instructions, projections, and loaded context do not create truth by themselves.

## Legacy Boundary

`archive/` is inert archive storage. Old vNext-R Workflow Governance files are legacy evidence only. They are not accepted proof state unless a future Legacy Import Receipt explicitly admits them through Verify and Commit.

## Operating Boundary

- Use this Direction for workflow governance and repository maintenance.
- Do not run roadmap selection, Horizon selection, Active Frontier selection, or product execution from this Direction unless a committed Obligation explicitly admits it.
- Do not modify sibling Directions or product repositories unless the current repository maintenance task explicitly lists those paths.
- Keep changes small and report Project Files refresh requirements when uploaded Project sources change.
