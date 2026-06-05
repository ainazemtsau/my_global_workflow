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
- Procedure gate lenses remain internal checks and do not become separate runtime entities.
- Route-changing outputs are represented by typed packets/records and Next Move Packet boundaries.
- Procedure Definition Framework procedures use canonical `workflow_v3/procedures/**` location and `*_PROCEDURE.md` naming, or state an explicit bounded exception.
- Procedure declares `procedure_class` when using the Procedure Definition Framework.
- Utility Decision Gate is present when utility use can affect completion.
- Common utility choices may be named without becoming an exhaustive whitelist.
- External handoff/resume policy exists when the procedure can emit external handoff packets.
- Stub procedures include target role, workflow integration, future body outline, required outputs, and STOP behavior until authored.
- Stub-body authoring extracts target role, workflow integration, future scope, must-not constraints, and required outputs from the self-contained stub.
- Procedure authoring explains target identity before detailed body drafting.

## WARN checks

- Simple procedure has more stages than needed.
- Registry selection hint is carrying execution logic that belongs in the procedure file.
- Checkpoint policy is present but vague.
- Procedure-specific utility notes are vague.
- Procedure docs imply common utility choices are an exhaustive whitelist.
- External handoff policy exists but expected return packet is terse.
- A procedure is still a stub, but it is self-contained and stops with `PROCEDURE_BODY_NOT_AUTHORED`.
- Detailed body authoring is deferred to a separate bounded `author_workflow_procedure` run.

## FAIL checks

- Procedure is only a vague "do well" instruction.
- Procedure is only a final template with no stage/gate production logic.
- Source authority handling is absent.
- Stop conditions are absent.
- Procedure can mutate state outside `storage_update_adapter`.
- Procedure can accept its own output.
- Procedure creates a separate route authority outside Procedure Registry, typed outputs, and FINISH/Next Move closure.
- Procedure calls another procedure as a hidden RUN switch.
- Procedure blocks global utility access solely because a utility was not prelisted.
- Procedure emits FINISH_REQUEST while required external return is pending.
- Procedure uses `human_decision` to avoid a required transfer packet.
- Utility adapter can mutate or accept output by implication.
- Non-trivial authoring proceeds directly to detailed body without method/checkpoint stage.
- Research is mandatory for every procedure or forbidden for high-impact/non-obvious method design.
- Complex procedure forces one-shot final artifact with no checkpoint.
- Procedure uses `*_RUNBOOK.md`, uses `*_PLAYBOOK.md`, or otherwise preserves obsolete runbook/playbook naming without an explicit bounded exception.
- Stub procedure lacks target role, workflow integration, future body outline, output contract, or STOP behavior.
- Registry points outside canonical procedure files.

END_OF_FILE: workflow_v3/evals/PROCEDURE_DEFINITION_EVAL.md
