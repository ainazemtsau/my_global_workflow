# Procedure Execution Eval

status: active_eval

## Required Checks

- Every registry `procedure_path` exists.
- Every selectable procedure has a `completion:` block or explicit stub completion behavior.
- Procedure completion uses procedure-specific result, proof, and blocked_if fields.
- Material stages are distinguished from `internal_check` steps.
- RUN emits `STAGE_RESULT` for material stages.
- User confirmation occurs before the next material stage when required.
- Utility calls use `UTILITY_CALL` / `UTILITY_RETURN`, resume the same procedure, and verify evidence before reliance.
- CHECK compares actual output to the selected procedure completion contract.
- FINISH closes only after CHECK/audit passes.
- Closure includes `NEXT_CHAT_CARD` or `no_next_chat_needed`.

## Failure Checks

- Procedure lacks completion contract.
- Procedure defines completion by global fixed done types.
- Procedure stage cards contain old routing fields.
- Utility call becomes a procedure switch.
- Procedure relies on unverified utility evidence.

END_OF_FILE: workflow_v3/evals/PROCEDURE_EXECUTION_EVAL.md