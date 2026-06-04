# Procedure Definition Eval

status: active_eval

## Purpose

Validate Workflow v3 procedure definition files before they are treated as usable procedure source.

## PASS checks

- Purpose is specific and bounded.
- Trigger and non-trigger are distinguishable.
- Required inputs are explicit.
- Source requirements are explicit.
- Context classification exists when source or state matters.
- Complexity selector exists.
- Stages use Stage Card format.
- Gates have real outcomes, including `STOP`, `REWORK`, and `EXPAND` where applicable.
- Checkpoint policy exists.
- Research or expansion policy exists where relevant.
- Output contract is downstream-usable.
- Stop conditions prevent invention and boundary crossing.
- Procedure closure uses FINISH_REQUEST, Result Packet, and Event Loop Closure correctly.

## WARN checks

- Simple procedure has more stages than needed.
- Registry selection hint is carrying execution logic that belongs in the procedure file.
- Checkpoint policy is present but vague.

## FAIL checks

- Procedure is only a vague "do well" instruction.
- Procedure is only a final template with no stage/gate production logic.
- Source authority handling is absent.
- Stop conditions are absent.
- Procedure can mutate state outside `storage_update_adapter`.
- Procedure can accept its own output.
- Complex procedure forces one-shot final artifact with no checkpoint.

END_OF_FILE: workflow_v3/evals/PROCEDURE_DEFINITION_EVAL.md
