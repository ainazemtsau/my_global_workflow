# Migration Control

Status: active_migration_control
Created at: 2026-05-11 10:33:28 +03:00

This directory is admin/migration-only. Runtime Direction Projects must not load migration/ files as workflow context.

## Canonical Policy

- GitHub repository inazemtsau/my_global_workflow is the active canonical AI workflow source.
- Legacy note source is migration input only.
- Runtime files must use GitHub paths and Repository Patch / epository_patch.v1.
- Legacy note IDs and paths may appear only in migration inventory, audit, manifest, or log files.

## Step Loop

1. AUDIT/PREVIEW: read GitHub and legacy source; no writes outside the approved step scope.
2. APPLY: write only approved files.
3. READ_BACK: read exact files written.
4. VALIDATE: verify anchors, forbidden changes, and completeness.
5. STOP unless validation returns PASS or PASS_WITH_NONBLOCKING_NOTES.

## Classification Enum

- migrate_to_github
- migrate_as_reference
- personal_out_of_scope
- duplicate_superseded
- needs_user_decision
- needs_user_export
- needs_summarization_before_migration

## Forbidden Runtime Outputs

The following must not be introduced into runtime files:

- 	rilium:
- legacy_path:
- legacy notes as canonical workflow state
- Trilium/note-database dependency language

## M0/M1 Result

- solo-max-productive: 166 visible entries, 0 inaccessible
- indie-game-development: 160 visible entries, 0 inaccessible
- health-and-beauty: 92 visible entries, 0 inaccessible
