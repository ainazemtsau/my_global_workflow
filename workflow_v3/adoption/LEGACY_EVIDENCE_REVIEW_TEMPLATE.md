# Legacy Evidence Review Template

status: template

## Boundary

This template records evidence review only.

It does not import, accept, bridge, migrate, persist, or create runtime state by itself. Old `directions/**` files remain `legacy_evidence` unless a later accepted bridge/import/adoption package changes the status for named artifacts through an explicit acceptance/update path.

## Review fields

```text
legacy_direction_id:
legacy_path:
legacy_workflow_version:

evidence_inventory:
  old_ledger:
  obligations:
  receipts:
  project_files:
  dashboard:
  migration_receipt:
  run_history:
  other:

evidence_classification:
  legacy_evidence_only:
  candidate_migration_context:
  accepted_v3_state: false

proposed_migration_mode:
  clean_start | bridge_only | selective_import | full_migration | no_adoption | undecided

import_candidates:
explicitly_not_imported:
unresolved_questions:
required_acceptance_update_path:
rollback_coexistence_notes:

decision_status:
  not_reviewed | reviewed_candidate | accepted_for_adoption_package | rejected | parked
```

## Allowed use

Legacy evidence may be cited as context for a current acceptance decision only when the citation is explicit, sourced, and labeled as `legacy_evidence`.

## Forbidden use

Do not treat old Ledger, Obligations, Receipts, Dashboard, Commit Scopes, Project setup files, old Direction Map, old project files, old migration receipts, or review output from this template as accepted Workflow v3 state.

## Stop conditions

Stop if review pressure becomes implicit migration, old-state import, invented Direction proof state, runtime root creation, legacy folder deletion, or Project setup action without authorization.

END_OF_FILE: workflow_v3/adoption/LEGACY_EVIDENCE_REVIEW_TEMPLATE.md
