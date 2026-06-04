# Codex Handoff Verification Runbook

status: active_repository_completion_framework

## Trigger condition

Use before sending bounded repository work to Codex and after Codex returns a branch, diff, commit, or blocked result.

Trigger signals include `codex_result_returned`, `codex_result_verified`, `validation_failed`, `scope_drift_observed`, or `blocked_result_returned`.

## Input sources

- Codex handoff package;
- repository, base ref, and target branch;
- changed files/diff/commit SHA;
- validation output;
- `workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md`.

## Source authority classification

Exact repository branch/commit/diff is authority for Codex results. Codex narrative is candidate evidence until verified. Project Files/Sources are cache/context.

## Required templates

- `workflow_v3/templates/WORK_CONTRACT_TEMPLATE.md`
- `workflow_v3/templates/RUN_RECORD_TEMPLATE.md`
- `workflow_v3/templates/RESULT_PACKET_TEMPLATE.md`
- `workflow_v3/templates/EVIDENCE_RECORD_TEMPLATE.md`
- `workflow_v3/templates/TRANSFER_PACKET_TEMPLATE.md`
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md`

## Required handoff fields

- self-contained target and source authority;
- branch policy and target branch;
- allowed paths and forbidden paths;
- required reads;
- required changes;
- validation commands/checks;
- stop conditions;
- commit/push instruction if authorized;
- requested return fields;
- EOF marker requirement for Markdown;
- project refresh fields;
- residual risks.

## Verification path

1. Verify branch name.
2. Verify base ref and commit SHA or diff.
3. Verify changed files.
4. Verify allowed paths only and forbidden paths untouched.
5. Verify validation results.
6. Verify Markdown EOF markers where relevant.
7. Verify Project refresh requirements are separated.
8. Verify no Codex output is treated as accepted state.
9. Emit `codex_result_verified` or validation/scope failure signal.
10. Run Event Loop Closure and Progression Router.

## Expected output

Codex verification result, validation evidence, changed file list, residual risks, Project refresh fields, and exact Next Move.

## Closure signal

`codex_result_verified`, `validation_failed`, `scope_drift_observed`, or `blocked_result_returned`.

## Return destination

Return to the current requesting chat for acceptance/update review.

## Acceptance/update requirement

Codex commit is not acceptance. Accepted state changes require explicit Acceptance Decision/update path.

## Failure/stop condition

Stop if handoff is not self-contained, branch/path policy is unclear, validation is missing/failed, forbidden paths changed, EOF validation fails, or Project refresh fields are conflated.

END_OF_FILE: workflow_v3/runbooks/CODEX_HANDOFF_VERIFICATION_RUNBOOK.md
