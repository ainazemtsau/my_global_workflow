# Workflow Governance Direction

Workflow Governance is the self-hosted Direction for maintaining the Workflow OS.

## Active Payload

Accepted state for this Direction lives in the root payload:

- `LEDGER.md`
- `OBLIGATIONS.md`
- `RECEIPTS_INDEX.md`
- `COMMIT_SCOPES.md`
- `DASHBOARD.md`
- `MIGRATION_RECEIPT.md`
- `receipts/`
- `projections/`
- `project_setup/`

Only verified Receipts committed to `LEDGER.md` create accepted state. Documents, setup instructions, projections, and loaded context do not create truth by themselves.

## Legacy Boundary

Old vNext-R Workflow Governance files are legacy evidence only. They are not accepted Direction state unless a future Legacy Import Receipt explicitly admits them through Verify and Commit.

## Operating Boundary

- Use this Direction for workflow governance and repository maintenance.
- Do not run roadmap selection, Horizon selection, Active Frontier selection, or product execution from this Direction unless a committed Obligation explicitly admits it.
- Do not modify sibling Directions or product repositories unless the current repository maintenance task explicitly lists those paths.
- Keep changes small and report Project Files refresh requirements when uploaded Project sources change.
