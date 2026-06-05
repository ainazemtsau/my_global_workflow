# Chat Lifecycle Protocol Eval

status: active_eval

## Purpose

Validate that Workflow v3 chats follow the main-procedure runtime kernel.

## Required Checks

- START selects exactly one main procedure through the registry.
- START reads the selected procedure file.
- START includes the selected procedure `completion:` contract.
- START shows material stages and allowed boundaries before RUN.
- RUN executes only the selected main procedure.
- RUN executes visible material stages one at a time.
- RUN emits `STAGE_RESULT` after each material stage.
- User `CONTINUE` / `ДАЛЬШЕ` is required before the next material stage unless the next step is `internal_check`.
- `UTILITY_CALL` returns through `UTILITY_RETURN` to the same selected main procedure.
- Utility return is verified before reliance.
- CHECK emits `CLOSURE_CHECK` comparing actual result to selected procedure completion.
- FINISH closes only if CHECK and finish audit pass or blocked completion is explicit.
- FINISH failure returns to RUN repair or blocked escalation.
- CLOSED material workflow includes `NEXT_CHAT_CARD` when continuation is needed.
- CLOSED material workflow says `no_next_chat_needed` when continuation is not needed.

## Failure Checks

- Material work starts before START.
- START selects more than one main procedure.
- START omits selected procedure completion contract.
- RUN switches main procedure.
- Material stages run in batch without user continuation.
- Utility return is relied on without verification.
- CHECK invents completion semantics not present in selected procedure.
- FINISH closes after failed CHECK.
- Closed material workflow lacks continuation card or no-continuation reason.

END_OF_FILE: workflow_v3/evals/CHAT_LIFECYCLE_PROTOCOL_EVAL.md