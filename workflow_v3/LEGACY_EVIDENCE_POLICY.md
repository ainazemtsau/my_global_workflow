# Workflow v3 Legacy Evidence Policy

status: active_skeleton_namespace_corrected

## Purpose

This file defines how Workflow v3 treats the old Workflow OS and old Direction files in this skeleton slice.

## Legacy/rollback boundary

The old Workflow OS remains the legacy and rollback system. This slice does not delete, rename, move, replace, or decommission it.

Old Workflow OS files may be used as legacy evidence when a later package explicitly asks for them. They are not active Workflow v3 accepted state.

## Old Direction files

Old Direction files are `legacy_evidence`, not `accepted_v3_state`.

This includes:

- old Ledger;
- old Obligations;
- old Receipts index;
- old Commit scopes;
- old Dashboard;
- old Migration receipt;
- old `project_files`;
- old `project_setup`;
- old receipts/run history.

These files may inform a later current decision, but they must not silently become Workflow v3 accepted state.

## No invented proof state

Workflow v3 must not infer accepted Direction state from old files, chat memory, stale Project Files/Sources, candidate docs, or document existence.

Any accepted_v3_state must come from explicit acceptance/update paths after adoption.

## Future adoption modes

Allowed future adoption modes:

- `clean_start` - begin v3 from an explicit current decision, without importing old state.
- `bridge_only` - reference old state through an explicit bridge without claiming import.
- `selective_import` - import specific artifacts with evidence and Acceptance Decision.
- `full_migration` - allowed only after a separate migration policy, validation evidence, and rollback design.
- `no_adoption` - keep the Direction under the old Workflow OS.

## Default for existing Directions

The default existing Direction adoption mode should be `clean_start` from an explicit current decision.

Clean start means old files can be inspected as legacy_evidence, but v3 state begins from a current accepted Direction Spine, Active Front, Current Status, and Next Move created through a later adoption package.

END_OF_FILE: workflow_v3/LEGACY_EVIDENCE_POLICY.md
