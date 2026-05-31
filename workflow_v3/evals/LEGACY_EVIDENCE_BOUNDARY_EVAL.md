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
- statement of what is not imported;
- acceptance/import authority if any bridge/import package exists;
- changed file check.

## PASS criteria

- Old `directions/**` and old Workflow OS files are evidence only.
- No old state is imported, migrated, or accepted by implication.
- No forbidden `workflow/**` or `directions/**` edits occur.
- Rollback/coexistence boundary remains intact.

## WARN criteria

- Legacy evidence is useful but needs a later explicit bridge/import decision.
- Source read is partial but the limitation is visible and no material claim depends on it.

## FAIL criteria

- Old Direction state imported implicitly.
- Legacy evidence treated as accepted v3 state.
- Old Workflow OS decommission/delete/move/rename occurs.
- Direction proof state invented from old files.
- Legacy path changed without explicit authorization.

## Common failure modes

- Treating old Ledger/Receipts/Dashboard as current v3 state.
- Treating old Project Files as current Project setup authority.
- Calling clean-start adoption a migration.

## Required recovery/repair action

Stop, reject or revert unauthorized legacy mutation, reclassify legacy content as evidence only, request explicit bridge/import authority if needed, and rerun the adoption/bootstrap eval.

END_OF_FILE: workflow_v3/evals/LEGACY_EVIDENCE_BOUNDARY_EVAL.md
