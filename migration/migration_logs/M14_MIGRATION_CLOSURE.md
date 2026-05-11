# M14 Migration Closure

Status: PASS_WITH_NONBLOCKING_NOTES
Updated at: 2026-05-11

## Scope

M14 closed the GitHub-only migration after M0-M13 validation passed.

## Closure validation

- Legacy inventory entries classified: 418 / 418
- `migrate_to_github` items with existing GitHub targets: 77 / 77
- `needs_user_export` items: 0
- `needs_user_decision` items: 14, explicitly deferred in manifests
- Runtime files use GitHub markdown source-of-truth model
- Migration/admin files are not default Direction runtime context
- `.serena/` remains local tooling state and is not committed

## Deferred decisions

Deferred items remain in the migration manifests with `classification: needs_user_decision`.

These are not runtime blockers because they are not classified as required active runtime context. They must be handled through a future migration/admin task before promotion into runtime, knowledge, domain docs, or project metadata.

## Files updated

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `docs/NEW_DEVICE_BOOTSTRAP.md`
- `migration/MIGRATION_STATE.md`

## Final state

GitHub repository markdown is the active canonical AI workflow source.

Routine ChatGPT/Codex runtime work should use GitHub files only.
