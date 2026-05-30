# Adoption Decision Record

decision_type: Workflow v3 first Direction adoption
direction_id: indie-game-development
adoption_mode: clean_start
accepted_effect: creates initial v3 runtime root only
no_legacy_import: true
no_project_update: true
old_workflow_os_untouched: true
effective_after: human review and acceptance/merge of this package
rollback: revert this package or ignore runtime root

## Decision Boundary

This record creates a clean_start runtime root for one Direction only after the package is accepted. It does not import old Direction state.

Old Direction files are legacy_evidence only. No old Ledger, Obligations, Receipts, Dashboard, Migration receipt, project_setup, project_files, archive, or run history is accepted_v3_state.

No actual ChatGPT Project UI update is performed. No Project Files/Sources refresh is performed. Project Files/Sources are cache/context only. Runtime Console is read-only.

## Rollback

Rollback is to revert this package or ignore/remove this runtime root. The old Workflow OS remains untouched and available.

END_OF_FILE: directions/indie-game-development/runtime/records/adoption/ADOPTION_DECISION.md
