# Codex Handoff Result Eval

status: active_repository_completion_framework

## Source files to inspect

- `workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md`
- `workflow_v3/procedures/CODEX_RESULT_VERIFICATION_PROCEDURE.md`
- `workflow_v3/templates/WORK_CONTRACT_TEMPLATE.md`
- `workflow_v3/templates/FINISH_PACKET_TEMPLATE.md`
- git branch, commit/diff, changed files, and validation output

## Evidence required

- self-contained Codex child-call schema;
- matching child_call_id or exact emitted `CHILD_PROCEDURE_CALL` when embedded;
- branch policy and branch name;
- base ref;
- commit SHA or diff;
- changed files;
- allowed/forbidden path check;
- validation output;
- EOF marker check for Markdown;
- Project refresh fields;
- residual risks.
- parent verification contract and resume rule.

## PASS criteria

- Codex changes only allowed paths.
- Commit/diff and changed files are verifiable.
- Required validation passes or limitations are explicit.
- Markdown EOF markers pass when relevant.
- Codex result returns to current chat for parent verification.
- Embedded Codex result returns through `CHILD_PROCEDURE_RETURN` to the same selected main procedure when the call was embedded.
- Embedded codex_return_verification occurs before CLOSURE_CHECK passes when the result affects owner output.
- Required current-goal Codex repair has an opened parent `CHILD_PROCEDURE_CALL`, parent wait state, and matching returned `CODEX_RETURN_PACKET` / `CHILD_PROCEDURE_RETURN` before parent CHECK/FINISH.
- Persistence handoff includes approval/update authority, exact path boundaries, validation, and verified same-owner return when Codex/storage utility writes.
- Project refresh fields are separated.
- Parent lifecycle does not CHECK, FINISH, or CLOSED while Codex return is open, missing, unverified, or missing required validation/evidence.

## WARN criteria

- Validation equivalent is used because a requested command is not applicable.
- Residual risk remains but does not invalidate the bounded result.

## FAIL criteria

- Codex commit treated as done or accepted state.
- Codex, child, check, storage, handoff, package, card, or copy-paste packet treated as parent lifecycle completion.
- Forbidden paths changed.
- Validation failed or missing with done claim.
- EOF validation failed.
- Project UI update or Project Files/Sources refresh conflated with repository commit.
- Codex returned evidence treated as accepted state.
- Codex result cannot be matched to the emitted embedded `CHILD_PROCEDURE_CALL`.
- Required Codex repair exists but the parent only emits a patch plan, package, handoff, or deferred launch instruction.
- Codex is asked to close the ChatGPT lifecycle.
- Codex/storage utility write is treated as accepted state without verification and acceptance/update boundary.
- Branch, commit, changed files, validation, EOF, refresh, push, or residual-risk evidence is missing but verification passes.
- FINISH closes with open Codex child call or non-empty gaps not explicitly classified as blocked completion.
- `NEXT_CHAT_CARD` carries unfinished Codex child work.

## Common failure modes

- Codex routes product meaning.
- Codex expands scope beyond package.
- Embedded verification treated as acceptance.
- Changed file list omitted.
- User is asked to assemble a Codex child call from scattered prior text.

## Required recovery/repair action

Block acceptance and parent closure, request or perform same-scope repair, verify diff and validation again, then resume parent RUN before CHECK/FINISH.

END_OF_FILE: workflow_v3/evals/CODEX_HANDOFF_RESULT_EVAL.md
