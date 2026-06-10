# Chat Lifecycle Dependency and Continuation Eval

status: active_eval

## Purpose

Validate dependency calls, dependency returns, and continuation cards.

## Required Checks

- `DEPENDENCY_CALL` states why the dependency is needed.
- `DEPENDENCY_CALL` names dependency type and execution surface.
- `DEPENDENCY_CALL` includes packet/call boundary and expected return.
- `DEPENDENCY_CALL` includes `expected_return_contract`, `parent_verification_contract`, `resume_rule`, and `unresolved_until_returned`.
- Prior packet labels are rejected for dependency calls/returns.
- External user action has complete copy-paste content.
- `DEPENDENCY_RETURN` matches the emitted call.
- Return resumes the same selected main procedure.
- Returned evidence is verified before reliance.
- Dependency return is not accepted state by itself.
- Dependency call does not switch main procedure.
- Required current-goal dependency repair opens `DEPENDENCY_CALL`, enters `RUN_WAITING_FOR_DEPENDENCY_RETURN`, and requires matching return verification before parent continuation.
- Code/repo mutation uses `code_repository_dependency` and Codex/code-assistant return verification.
- Codex, dependency, check, storage, handoff, package, card, or copy-paste packet is not terminal parent completion.
- Closure continuation uses post-closed `NEXT_CHAT_CARD` only when a new independent lifecycle is needed.

## Failure Checks

- Dependency call is hidden or incomplete.
- Return cannot be matched to a call.
- Return resumes a different procedure.
- Returned evidence is relied on without verification.
- CHECK, FINISH, or CLOSED proceeds while a required dependency call is open, missing, or unverified.
- Code repository dependency is required but no Codex/code-assistant return exists and CHECK passes.
- Required dependency repair is found but parent output remains only a plan, packet, handoff, card, or future launch instruction while parent RUN continues.
- Dependency return exists but branch, commit, changed files, validation, EOF, refresh, push, or residual-risk evidence is missing and verification passes.
- A package, handoff, card, Codex packet, check packet, storage packet, or dependency packet is used as parent completion.
- `NEXT_CHAT_CARD` represents unfinished dependency work or replaces `DEPENDENCY_CALL`.
- User is asked to assemble a dependency call from scattered prior text.
- A closure card is a placeholder instead of copy-paste-ready content.

END_OF_FILE: workflow_v3/evals/CHAT_LIFECYCLE_HANDOFF_EVAL.md
