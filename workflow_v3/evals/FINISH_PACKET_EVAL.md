# FINISH_PACKET Eval

status: active_eval

## Required Checks

- FINISH follows passed `CLOSURE_CHECK` or explicit blocked completion from the selected procedure.
- FINISH audit compares START, RUN, utility returns, and selected procedure completion.
- FINISH does not close if CHECK failed.
- FINISH failure returns to RUN repair or blocked escalation.
- FINISH_PACKET includes human-readable result, evidence, validation, refresh requirements when relevant, and residual risks.
- FINISH_PACKET includes `NEXT_CHAT_CARD` when workflow continuation is needed.
- FINISH_PACKET includes `no_next_chat_needed` with reason when continuation is not needed.

## Failure Checks

- FINISH is first reveal of work.
- FINISH closes with unverified utility evidence.
- FINISH closes despite completion gaps.
- FINISH omits continuation card or no-continuation reason.
- FINISH silently launches next work.

END_OF_FILE: workflow_v3/evals/FINISH_PACKET_EVAL.md