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
- Procedure closure uses CLOSURE_CHECK, FINISH_PACKET, and NEXT_CHAT_CARD_or_no_next_chat_needed correctly.
- Procedure gate lenses remain internal checks and do not become separate runtime entities.
- Route-changing outputs are represented by typed packets/cards and continuation boundaries.
- Procedure Definition Framework procedures use canonical `workflow_v3/procedures/**` location and `*_PROCEDURE.md` naming, or state an explicit bounded exception.
- Procedure declares `kind` when using the Procedure Definition Framework.
- Dependency decision gate is present when dependency use can affect completion.
- Common dependency choices may be named without becoming an exhaustive whitelist.
- External dependency-call/resume policy exists when the procedure can emit dependency-call packets.
- Stub procedures include target role, workflow integration, future body outline, required outputs, and STOP behavior until authored.
- Stub-body authoring extracts target role, workflow integration, future scope, must-not constraints, and required outputs from the self-contained stub.
- Procedure authoring explains target identity before detailed body drafting.

## WARN checks

- Simple procedure has more stages than needed.
- Registry selection hint is carrying execution logic that belongs in the procedure file.
- Checkpoint policy is present but vague.
- Procedure-specific dependency notes are vague.
- Procedure docs imply common dependency choices are an exhaustive whitelist.
- External dependency-call policy exists but expected return packet is terse.
- A procedure is still a stub, but it is self-contained and stops with `PROCEDURE_BODY_NOT_AUTHORED`.
- Detailed body authoring is deferred to a separate bounded `author_workflow_procedure` run.

## FAIL checks

- Procedure is only a vague "do well" instruction.
- Procedure is only a final template with no stage/gate production logic.
- Source authority handling is absent.
- Stop conditions are absent.
- Procedure permits direct ChatGPT state mutation outside `storage_update`.
- Procedure rejects same-owner Codex/storage dependency persistence solely because persistence is not a separate `storage` owner run.
- Procedure permits external repository/code write without visible `DEPENDENCY_CALL`, user approval/update authority, exact paths, validation, and verified `DEPENDENCY_RETURN`.
- Procedure permits repository/code mutation without routing through `code_repository_dependency` to Codex/code assistant.
- Procedure can accept its own output.
- Procedure creates a separate route authority outside Procedure Registry, typed outputs, and FINISH/continuation closure.
- Procedure calls another procedure as a hidden RUN switch.
- Procedure blocks global dependency access solely because a dependency was not prelisted.
- Procedure lets CLOSURE_CHECK pass while required dependency return is open, missing, or unverified.
- Procedure uses `human_decision` to avoid a required transfer packet.
- Dependency surface can mutate or accept output by implication.
- Procedure defines completion as only a handoff, package, card, Codex package, check packet, storage packet, copy-paste packet, dependency packet, or NEXT_CHAT_CARD.
- Non-trivial authoring proceeds directly to detailed body without method/checkpoint stage.
- Research is mandatory for every procedure or forbidden for high-impact/non-obvious method design.
- Complex procedure forces one-shot final artifact with no checkpoint.
- Procedure uses `*_RUNBOOK.md`, uses `*_PLAYBOOK.md`, or otherwise preserves obsolete runbook/playbook naming without an explicit bounded exception.
- Stub procedure lacks target role, workflow integration, future body outline, output contract, or STOP behavior.
- Registry points outside canonical procedure files.

END_OF_FILE: workflow_v3/evals/PROCEDURE_DEFINITION_EVAL.md
