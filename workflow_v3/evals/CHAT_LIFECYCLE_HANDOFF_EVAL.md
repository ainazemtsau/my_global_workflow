# Chat Lifecycle Child Call Eval

status: active_eval

## Purpose

Validate child procedure calls, adapter returns, and continuation cards.

## Required Checks

- `CHILD_PROCEDURE_CALL` states why the child/adaptor is needed.
- `CHILD_PROCEDURE_CALL` names target child/adaptor surface.
- `CHILD_PROCEDURE_CALL` includes packet/call boundary and expected return.
- `CHILD_PROCEDURE_CALL` includes `expected_return_contract`, `parent_verification_contract`, `resume_rule`, and `unresolved_until_returned`.
- External user action has complete copy-paste content.
- `CHILD_PROCEDURE_RETURN` matches the emitted call.
- Return resumes the same selected main procedure.
- Returned evidence is verified before reliance.
- Child return is not accepted state by itself.
- Child call does not switch main procedure.
- Codex, child, check, storage, handoff, package, card, or copy-paste packet is not terminal parent completion.
- Closure continuation uses post-closed `NEXT_CHAT_CARD` only when a new independent lifecycle is needed.

## Failure Checks

- Child call is hidden or incomplete.
- Return cannot be matched to a call.
- Return resumes a different procedure.
- Returned evidence is relied on without verification.
- CHECK, FINISH, or CLOSED proceeds while a required child call is open, missing, or unverified.
- Codex child call is required but no return exists and CHECK passes.
- Child return exists but branch, commit, changed files, validation, EOF, refresh, push, or residual-risk evidence is missing and verification passes.
- A package, handoff, card, Codex packet, check packet, storage packet, or child-chat card is used as parent completion.
- `NEXT_CHAT_CARD` represents unfinished child work or replaces `CHILD_PROCEDURE_CALL`.
- User is asked to assemble a child call from scattered prior text.
- A closure card is a placeholder instead of copy-paste-ready content.

END_OF_FILE: workflow_v3/evals/CHAT_LIFECYCLE_HANDOFF_EVAL.md
