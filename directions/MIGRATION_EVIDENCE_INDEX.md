# Legacy Direction Migration Evidence Index

Status: legacy_evidence_index

## Purpose

This is a tracking/index surface for Workflow v2 legacy Direction migration evidence.

It is not accepted Workflow v3 state. It does not import, bridge, migrate, accept, discard, or create runtime state.

No automatic import. No automatic discard.

Any carried-forward fact requires legacy evidence review plus an explicit acceptance/update path.

## Status Values

Allowed `migration_review_status` values:

- `not_reviewed`
- `evidence_reviewed`
- `bridge_candidate`
- `selective_import_candidate`
- `full_migration_candidate`
- `clean_start_candidate`
- `no_adoption_candidate`
- `imported_to_v3_after_acceptance`
- `superseded`

Required `accepted_v3_state_status` values:

- `legacy_evidence_only`
- `accepted_v3_state_after_explicit_update`
- `not_applicable`

## Evidence Index

| legacy_direction_id | legacy_path | legacy_workflow_version | evidence_available | migration_review_status | proposed_migration_mode | accepted_v3_state_status | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| health-and-beauty | directions/health-and-beauty/ | Workflow v2 legacy | Lightweight check found workflow/LEDGER.md, workflow/OBLIGATIONS.md, workflow/RECEIPTS_INDEX.md, workflow/MIGRATION_RECEIPT.md, workflow/project_setup, workflow/DASHBOARD.md. | not_reviewed | undecided | legacy_evidence_only | Placeholder index row; not import. |
| solo-max-productive | directions/solo-max-productive/ | Workflow v2 legacy | Lightweight check found workflow/LEDGER.md, workflow/OBLIGATIONS.md, workflow/RECEIPTS_INDEX.md, workflow/MIGRATION_RECEIPT.md, workflow/DASHBOARD.md. | not_reviewed | undecided | legacy_evidence_only | Placeholder index row; not import. |
| workflow-governance | directions/workflow-governance/ | Workflow v2 legacy | Lightweight check found workflow/LEDGER.md, workflow/OBLIGATIONS.md, workflow/RECEIPTS_INDEX.md, workflow/MIGRATION_RECEIPT.md, workflow/project_setup, workflow/DASHBOARD.md. | not_reviewed | undecided | legacy_evidence_only | Placeholder index row; not import. |

END_OF_FILE: directions/MIGRATION_EVIDENCE_INDEX.md
