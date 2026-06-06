# Legacy Evidence Boundary Eval

status: active_repository_completion_framework

## Source files to inspect

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow_v3/LEGACY_EVIDENCE_POLICY.md`
- `workflow_v3/adoption/LEGACY_EVIDENCE_REVIEW_TEMPLATE.md`
- exact legacy paths named by a future package, if any
- git diff for `workflow/**` and `directions/**`

## Evidence required

- explicit legacy evidence allowance;
- exact legacy paths and read completeness;
- evidence classification as `legacy_evidence`;
- evidence review output marked as review-only;
- migration/adoption mode named per Direction when any adoption/migration claim is made;
- statement of what is not imported;
- acceptance/import authority if any bridge/import package exists;
- changed file check.

## PASS criteria

- Old `directions/**` and old Workflow OS files are evidence only unless a later accepted bridge/import/adoption package names artifacts and updates their status.
- No old state is imported, migrated, or accepted by implication.
- No legacy evidence is discarded, deleted, renamed, moved, archived, compacted, or decommissioned by review alone.
- Migration/adoption mode is explicit per Direction.
- Accepted import requires explicit acceptance/update path.
- Evidence review does not create `directions_v3/<direction-id>/runtime/**`.
- No forbidden `workflow/**` or `directions/**` edits occur.
- Rollback/coexistence boundary remains intact.

## WARN criteria

- Legacy evidence is useful but needs a later explicit bridge/import decision.
- Source read is partial but the limitation is visible and no material claim depends on it.
- Migration/adoption mode is still `undecided` and no import, discard, adoption, or runtime creation is claimed.

## FAIL criteria

- Old Direction state imported implicitly.
- Legacy evidence treated as accepted v3 state.
- Legacy evidence review output treated as import, migration, bridge, persistence, or runtime-state creation.
- Legacy evidence discarded automatically or treated as worthless by default.
- Migration/adoption mode omitted when a future adoption/migration claim is made.
- Accepted import claimed without acceptance/update path.
- `directions_v3/<direction-id>/runtime/**` root created by evidence review.
- Old Workflow OS decommission/delete/move/rename occurs.
- Legacy Direction folder deleted, renamed, moved, archived, compacted, or decommissioned by review.
- Direction proof state invented from old files.
- Legacy path changed without explicit authorization.

## Common failure modes

- Treating old Ledger/Receipts/Dashboard as current v3 state.
- Treating old Project Files as current Project setup authority.
- Treating evidence review as import.
- Treating no automatic import as automatic discard.
- Calling clean-start adoption a migration.

## Required recovery/repair action

Stop, reject or revert unauthorized legacy mutation, reclassify legacy content as evidence only, restore no automatic import and no automatic discard boundaries, request explicit bridge/import/adoption authority if needed, and rerun the adoption/bootstrap eval.

END_OF_FILE: workflow_v3/evals/LEGACY_EVIDENCE_BOUNDARY_EVAL.md
