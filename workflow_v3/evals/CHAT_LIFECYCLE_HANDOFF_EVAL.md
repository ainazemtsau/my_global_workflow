# Chat Lifecycle Utility Eval

status: active_eval

## Purpose

Validate utility calls, returns, and continuation cards.

## Required Checks

- `UTILITY_CALL` states why the utility is needed.
- `UTILITY_CALL` names target utility/surface.
- `UTILITY_CALL` includes packet/call boundary and expected return.
- External user action has complete copy-paste content.
- `UTILITY_RETURN` matches the emitted call.
- Return resumes the same selected main procedure.
- Returned evidence is verified before reliance.
- Utility return is not accepted state by itself.
- Utility call does not switch main procedure.
- Closure continuation uses `NEXT_CHAT_CARD` when a new material chat is needed.

## Failure Checks

- Utility call is hidden or incomplete.
- Return cannot be matched to a call.
- Return resumes a different procedure.
- Returned evidence is relied on without verification.
- A closure card is a placeholder instead of copy-paste-ready content.

END_OF_FILE: workflow_v3/evals/CHAT_LIFECYCLE_HANDOFF_EVAL.md