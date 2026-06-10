# Procedure Execution Eval

status: active_eval

## Required Checks

- Every registry `procedure_path` exists.
- Every selectable procedure has a `completion:` block or explicit stub completion behavior.
- Procedure completion uses procedure-specific result, proof, and blocked_if fields.
- Material stages are distinguished from `internal_check` steps.
- RUN emits `STAGE_RESULT` for declared material stages without runtime stage compression.
- User confirmation occurs before the next material stage when required.
- Dependency calls use `DEPENDENCY_CALL` / `DEPENDENCY_RETURN`, enter `RUN_WAITING_FOR_DEPENDENCY_RETURN`, resume the same procedure, and verify evidence before reliance.
- Required dependency repair for the current START goal opens a dependency call; later stage progression pauses until matching return verification.
- CHECK compares actual output to the selected procedure completion contract.
- CHECK and FINISH block on open, missing, or unverified dependency returns and missing required validation/evidence.
- Repository/code mutation routes only through `code_repository_dependency` to Codex/code assistant.
- FINISH closes only after CHECK/audit passes.
- Closure includes post-closed `NEXT_CHAT_CARD` or `no_next_chat_needed`.

## Failure Checks

- Procedure lacks completion contract.
- Procedure defines completion by global fixed done types.
- Procedure stage cards contain old routing fields.
- Runtime compresses declared stages into an undeclared simple/compact/shortcut/single-stage path.
- Dependency call becomes a procedure switch or standalone terminal chat.
- Procedure relies on unverified dependency evidence.
- Procedure identifies required external repair but leaves it as a plan, package, or future launch instruction while continuing.
- Procedure completion is only a handoff, package, card, Codex package, check packet, storage packet, copy-paste packet, dependency packet, or NEXT_CHAT_CARD.

END_OF_FILE: workflow_v3/evals/PROCEDURE_EXECUTION_EVAL.md
