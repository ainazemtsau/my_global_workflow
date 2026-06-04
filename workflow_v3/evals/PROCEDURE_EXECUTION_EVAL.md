# Procedure Execution Eval

status: active_eval

## Purpose

Check whether a Workflow v3 procedure execution in a chat or Codex run followed lifecycle, source, run-surface, gate, registry, canonical path, and closure rules.

## PASS checks

- START selected exactly one entrypoint.
- Selected procedure source was read.
- Matching run surface contract was obeyed.
- Complexity level was justified.
- Required stages were activated or skipped with reasons.
- Gates were applied visibly enough for review.
- Procedure gate lenses stayed internal to RUN.
- Route-changing effects were emitted as typed outputs, Result Packet, or Next Move Packet rather than hidden continuation.
- Checkpoints occurred when required.
- Expansion, research, child, or check work was bounded.
- No procedure switch occurred during RUN.
- For procedure authoring, canonical path/naming and stub/body status were evaluated.
- Registry delta points `procedure_ref` to the canonical procedure file unless an explicit bounded exception was recorded.
- FINISH_REQUEST happened before FINISH.
- Result Packet includes procedure limitations and validation.
- Next Move Packet selects exactly one primary next move.

## WARN checks

- Gate evidence is present but terse.
- Optional expansion was proposed but not clearly tied to a later admitted surface.
- Stage skip reasons are correct but hard to audit.
- A selected procedure is still a stub, but it stops cleanly with `PROCEDURE_BODY_NOT_AUTHORED`.

## FAIL checks

- Procedure switch during RUN.
- Hidden mutation.
- Hidden acceptance.
- Weak final artifact despite unmet gate.
- Checkpoint skipped when procedure requires it.
- Research, child, or check work becomes independent material work.
- External routing output emitted for every minor checkpoint.
- Final closure launches next work invisibly.
- Parent integration, graph delta, escalation, downstream delta, or derived gate output mutates accepted state by existence.
- Procedure authoring preserves obsolete runbook/playbook path or naming without an explicit bounded exception.
- Stub execution attempts detailed body work instead of stopping.
- Registry points outside canonical procedure files.

END_OF_FILE: workflow_v3/evals/PROCEDURE_EXECUTION_EVAL.md
