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
- Procedure closure uses FINISH_REQUEST, FINISH_PACKET, Result Packet, and Next Move Packet correctly.
- New or migrated Procedure Definition Framework procedures use canonical `workflow_v3/procedures/**` location and `*_PROCEDURE.md` naming, or state an explicit bounded exception.
- Migrated procedures include old source path, new procedure path, registry delta, and old-file disposition.

## WARN checks

- Simple procedure has more stages than needed.
- Registry selection hint is carrying execution logic that belongs in the procedure file.
- Checkpoint policy is present but vague.
- A compatibility shim is proposed for an old runbook/playbook path, but the shim is bounded and not the controlling procedure source.
- Existing unmigrated registry entries still point to legacy paths as declared coexistence.

## FAIL checks

- Procedure is only a vague "do well" instruction.
- Procedure is only a final template with no stage/gate production logic.
- Source authority handling is absent.
- Stop conditions are absent.
- Procedure can mutate state outside `storage_update_adapter`.
- Procedure can accept its own output.
- Complex procedure forces one-shot final artifact with no checkpoint.
- New or migrated procedure remains under `workflow_v3/runbooks/**`, uses `*_RUNBOOK.md`, uses `*_PLAYBOOK.md`, or otherwise preserves obsolete runbook/playbook naming without an explicit bounded exception.
- Migrated procedure lacks registry delta when its controlling source path changes.
- Registry would still point to the old runbook/playbook as controlling procedure source after migration.

END_OF_FILE: workflow_v3/evals/PROCEDURE_DEFINITION_EVAL.md
