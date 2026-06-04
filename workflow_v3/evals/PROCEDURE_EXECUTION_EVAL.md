# Procedure Execution Eval

status: active_eval

## Purpose

Check whether a Workflow v3 procedure execution in a chat or Codex run followed lifecycle, source, run-surface, gate, and closure rules.

## PASS checks

- START selected exactly one entrypoint.
- Selected procedure source was read.
- Matching run surface contract was obeyed.
- Complexity level was justified.
- Required stages were activated or skipped with reasons.
- Gates were applied visibly enough for review.
- Checkpoints occurred when required.
- Expansion, research, child, or check work was bounded.
- No procedure switch occurred during RUN.
- FINISH_REQUEST happened before FINISH.
- Result Packet includes procedure limitations and validation.
- Event Loop Closure selects exactly one primary next move.

## WARN checks

- Gate evidence is present but terse.
- Optional expansion was proposed but not clearly tied to a later admitted surface.
- Stage skip reasons are correct but hard to audit.

## FAIL checks

- Procedure switch during RUN.
- Hidden mutation.
- Hidden acceptance.
- Weak final artifact despite unmet gate.
- Checkpoint skipped when procedure requires it.
- Research, child, or check work becomes independent material work.
- Signals emitted for every minor checkpoint.
- Final closure launches next work invisibly.

END_OF_FILE: workflow_v3/evals/PROCEDURE_EXECUTION_EVAL.md
