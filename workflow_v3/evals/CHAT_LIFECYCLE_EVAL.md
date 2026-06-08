# Chat Lifecycle Eval

status: active_eval

## Required Checks

- START_CONTRACT appears before material RUN.
- START_CONTRACT names one selected entrypoint and procedure path.
- START_CONTRACT has a plain-language operator summary first, and when the operator writes Russian it uses `## Коротко` before compact technical fields.
- START_CONTRACT includes the selected procedure completion contract.
- RUN produces `STAGE_RESULT` for each declared material stage without runtime stage compression.
- STAGE_RESULT has a plain-language explanation of what happened, what was found, what to review, and what happens next; when the operator writes Russian it uses `## Коротко по шагу` and puts compact fields under `## Техническая часть`.
- Next material stage waits for user CONTINUE / ДАЛЬШЕ unless the next step is `internal_check`.
- Child/adaptor work is visible as `CHILD_PROCEDURE_CALL`, enters `RUN_WAITING_FOR_CHILD_RETURN`, returns through `CHILD_PROCEDURE_RETURN`, and passes `CHILD_RETURN_VERIFICATION`.
- Required child/adaptor repair opens `CHILD_PROCEDURE_CALL`; CHECK fails if `required_child_work_detected = true` and `child_call_opened = false`.
- `CLOSURE_CHECK` compares actual result to selected procedure completion.
- `CLOSURE_CHECK` blocks on open, missing, or unverified child returns and on missing validation/evidence.
- FINISH_PACKET appears only after CHECK passes and explicit FINISH / ФИНИШ.
- CLOSED includes post-closed `NEXT_CHAT_CARD` or `no_next_chat_needed`.

## Failure Checks

- Material work begins before START_CONTRACT.
- START_CONTRACT is missing completion contract.
- RUN switches selected procedure.
- RUN compresses declared stages into an undeclared simple/compact/shortcut/single-stage path.
- Child/adaptor output is treated as accepted state or parent completion before return verification.
- Required repair is detected, the parent cannot mutate directly, `candidate_codex_package_prepared: true` appears, `child_calls_opened` is empty, and next stage/CHECK/FINISH is allowed.
- `CANDIDATE_CODEX_CHILD_PROCEDURE_CALL_PACKET` appears as active RUN output for required repair.
- `prepared_not_opened` is used to continue material stages after required external repair is identified.
- Required child/adaptor repair is deferred to future operator action while the parent continues.
- CHECK passes when required child work was detected but no child call was opened.
- FINISH_PACKET appears while completion gaps remain, required validation/evidence is absent, or child returns are open/missing/unverified.
- A handoff, package, card, Codex package, check packet, storage packet, copy-paste packet, child-chat card, or NEXT_CHAT_CARD is treated as terminal completion.
- Closure makes the user assemble a NEXT_CHAT_CARD manually.
- NEXT_CHAT_CARD carries unfinished child work or replaces CHILD_PROCEDURE_CALL.

END_OF_FILE: workflow_v3/evals/CHAT_LIFECYCLE_EVAL.md
