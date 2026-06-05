# Codex Handoff Result Eval

status: active_repository_completion_framework

## Source files to inspect

- `workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md`
- `workflow_v3/procedures/CODEX_RESULT_VERIFICATION_PROCEDURE.md`
- `workflow_v3/templates/WORK_CONTRACT_TEMPLATE.md`
- `workflow_v3/templates/RESULT_PACKET_TEMPLATE.md`
- git branch, commit/diff, changed files, and validation output

## Evidence required

- self-contained handoff;
- matching handoff id or exact emitted handoff when embedded;
- branch policy and branch name;
- base ref;
- commit SHA or diff;
- changed files;
- allowed/forbidden path check;
- validation output;
- EOF marker check for Markdown;
- Project refresh fields;
- residual risks.

## PASS criteria

- Codex changes only allowed paths.
- Commit/diff and changed files are verifiable.
- Required validation passes or limitations are explicit.
- Markdown EOF markers pass when relevant.
- Codex result returns to current chat for verification and closure.
- Embedded Codex result returns through UTILITY_RETURN to the same selected main procedure when the handoff was embedded.
- Embedded codex_return_verification occurs before FINISH_REQUEST when the result affects owner output.
- Persistence handoff includes approval/update authority, exact path boundaries, validation, and verified same-owner return when Codex/storage utility writes.
- Project refresh fields are separated.

## WARN criteria

- Validation equivalent is used because a requested command is not applicable.
- Residual risk remains but does not invalidate the bounded result.

## FAIL criteria

- Codex commit treated as done or accepted state.
- Forbidden paths changed.
- Validation failed or missing with done claim.
- EOF validation failed.
- Project UI update or Project Files/Sources refresh conflated with repository commit.
- Result Packet treated as accepted state.
- Codex result cannot be matched to the emitted embedded handoff.
- Codex is asked to close the ChatGPT lifecycle.
- Codex/storage utility write is treated as accepted state without verification and acceptance/update boundary.

## Common failure modes

- Codex routes product meaning.
- Codex expands scope beyond package.
- Embedded verification treated as acceptance.
- Changed file list omitted.

## Required recovery/repair action

Block acceptance, request or perform same-scope repair, verify diff and validation again, then rerun FINISH closure and acceptance review.

END_OF_FILE: workflow_v3/evals/CODEX_HANDOFF_RESULT_EVAL.md
