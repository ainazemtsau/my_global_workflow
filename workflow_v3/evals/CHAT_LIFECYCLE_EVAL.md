# Chat Lifecycle Eval

status: active_eval

## Required Checks

- START_CONTRACT appears before material RUN.
- START_CONTRACT names one selected entrypoint and procedure path.
- START_CONTRACT includes the selected procedure completion contract.
- RUN produces `STAGE_RESULT` for each visible material stage.
- Next material stage waits for user CONTINUE / ДАЛЬШЕ unless the next step is `internal_check`.
- Utility use is visible as `UTILITY_CALL` / `UTILITY_RETURN` and returns to the same main procedure.
- `CLOSURE_CHECK` compares actual result to selected procedure completion.
- FINISH_PACKET appears only after CHECK passes and explicit FINISH / ФИНИШ.
- CLOSED includes `NEXT_CHAT_CARD` or `no_next_chat_needed`.

## Failure Checks

- Material work begins before START_CONTRACT.
- START_CONTRACT is missing completion contract.
- RUN switches selected procedure.
- Utility output is treated as accepted state.
- FINISH_PACKET appears while completion gaps remain.
- Closure makes the user assemble a NEXT_CHAT_CARD manually.

END_OF_FILE: workflow_v3/evals/CHAT_LIFECYCLE_EVAL.md