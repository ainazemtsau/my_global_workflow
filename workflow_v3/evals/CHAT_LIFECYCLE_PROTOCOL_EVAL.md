# Chat Lifecycle Protocol Eval

status: active_eval

## Purpose

Validate that Workflow v3 chats follow the main-procedure runtime kernel.

## Required Checks

- START selects exactly one main procedure through the registry.
- START reads the selected procedure file.
- START begins with an operator-readable plain-language block.
- When the operator writes Russian, START begins with `## Коротко`, includes `На что тебе смотреть`, and puts compact canonical fields under `## Техническая часть`.
- START states the selected main procedure, selection reason, chat goal, terminal condition, possible child call need, default/no-action or attention status, and operator review items in human-readable form.
- START includes the selected procedure `completion:` contract.
- START shows material stages and allowed boundaries before RUN.
- RUN executes only the selected main procedure.
- RUN executes the declared stage sequence without ad hoc compression.
- RUN executes visible material stages one at a time.
- RUN emits `STAGE_RESULT` after each material stage.
- STAGE_RESULT includes an operator-readable summary when material conclusions, blockers, repair needs, or child calls exist; when the operator writes Russian, it uses `## Коротко по шагу` and `## Техническая часть`.
- User `CONTINUE` / `ДАЛЬШЕ` is required before the next material stage unless the next step is `internal_check`.
- `CHILD_PROCEDURE_CALL` returns through `CHILD_PROCEDURE_RETURN` to the same selected main procedure.
- Required child/adaptor repair opens `CHILD_PROCEDURE_CALL`, enters `RUN_WAITING_FOR_CHILD_RETURN`, and pauses CONTINUE / ДАЛЬШЕ, CHECK, FINISH, and CLOSED until matching return verification.
- Child return is verified before reliance.
- `open_child_calls != empty`, missing child returns, unverified child returns, and missing required validation/evidence block CHECK, FINISH, and CLOSED.
- CHECK emits `CLOSURE_CHECK` comparing actual result to selected procedure completion.
- FINISH closes only if CHECK and finish audit pass or blocked completion is explicit.
- FINISH failure returns to RUN repair or blocked escalation.
- CLOSED material workflow includes post-closed `NEXT_CHAT_CARD` when a new independent lifecycle is needed.
- CLOSED material workflow says `no_next_chat_needed` when continuation is not needed.

## Failure Checks

- Material work starts before START.
- START does not state selected main procedure and terminal goal in human-readable form.
- Russian-operator START begins with English labels or raw technical fields instead of Russian prose.
- STAGE_RESULT has no plain-language explanation of what happened, what was found, what to review, and what happens next.
- START selects more than one main procedure.
- START omits selected procedure completion contract.
- RUN switches main procedure.
- RUN uses ad hoc simple, compact, shortcut, or one-stage compression to bypass declared stages.
- Material stages run in batch without user continuation.
- Child return is relied on without verification.
- Repair is needed, a Codex child call is required, and no return exists, but CHECK passes.
- Required child/adaptor repair is found, the parent cannot mutate directly, no child call is opened, and RUN continues to later stage/CHECK/FINISH.
- Patch is not applied or required validation is missing, but CLOSURE_CHECK passes.
- Codex, child, check, or storage package is emitted as `actual_result` and treated as completion.
- CHECK invents completion semantics not present in selected procedure.
- CHECK passes with open child calls.
- FINISH closes after failed CHECK.
- FINISH closes with open child call.
- FINISH closes with non-empty gaps unless explicitly blocked completion is allowed and the result is marked blocked.
- User is asked to assemble a child call from scattered prior text.
- `NEXT_CHAT_CARD` is used to represent unfinished child work.
- Closed material workflow lacks continuation card or no-continuation reason.

END_OF_FILE: workflow_v3/evals/CHAT_LIFECYCLE_PROTOCOL_EVAL.md
