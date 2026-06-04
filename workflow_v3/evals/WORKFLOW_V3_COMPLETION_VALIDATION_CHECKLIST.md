# Workflow v3 Completion Validation Checklist

status: active_repository_completion_framework

## Source files to inspect

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `README.md`
- `directions_v3/README.md`
- `workflow_v3/**`
- git diff against the package base

## Evidence required

- base SHA used;
- changed files list;
- new and updated files list;
- registry entity count;
- coverage matrix entity row count;
- completion matrix entity crosswalk;
- procedure stub field validation;
- eval field validation;
- EOF marker validation;
- Project Instructions payload counts when instruction sources changed;
- `git diff --check` output.

## PASS criteria

- Changes are limited to allowed paths.
- No `workflow/**`, `directions/**`, product repository, or real runtime root files changed.
- No `directions_v3/<direction-id>/runtime/**` exists from this package.
- Every new/edited Markdown file has `END_OF_FILE`.
- Registry entity count and coverage matrix entity row count do not decrease.
- Every registry entity has completion matrix coverage.
- Every unauthored procedure stub has target role, workflow integration, future body scope, required outputs, closure shape, and STOP behavior.
- Every eval has PASS/WARN/FAIL criteria and recovery action.
- Project setup refresh categories are separated.
- `git diff --check` passes or only line-ending warnings are reported separately.

## WARN criteria

- A Project setup source changes but payload is under 8,000 and above 7,200 characters.
- A future rollout need is identified but remains properly classified as future manual rollout only.
- A validation command is not applicable but an equivalent check is documented.

## FAIL criteria

- Forbidden paths changed.
- Runtime root created without explicit adoption package.
- Legacy state imported or accepted by implication.
- Project UI update or Project Files/Sources refresh is implied by repository commit.
- Project Instructions payload exceeds 8,000 characters.
- EOF marker validation fails.
- Entity coverage cannot be proven.
- `git diff --check` has validation failures.

## Common failure modes

- Treating repository completion as Direction adoption.
- Treating Codex commit as accepted state.
- Treating Project Files/Sources as source authority.
- Skipping payload counts after Project Instructions source changes.

## Required recovery/repair action

Repair within allowed paths if the issue is same-package and bounded. Otherwise stop with a Context Request naming exact path/ref/question. Re-run this checklist after repair.

END_OF_FILE: workflow_v3/evals/WORKFLOW_V3_COMPLETION_VALIDATION_CHECKLIST.md
