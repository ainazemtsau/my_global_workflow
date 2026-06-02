# Generic Answer Procedure

status: active_procedure

## Purpose

Use `generic_answer` only for lightweight answers that do not depend on current canonical repository state, Direction runtime state, write actions, acceptance, Codex, recovery, or current Next Move.

## Allowed use

- explain stable Workflow v3 concepts already available in the admitted prompt;
- answer non-mutating, non-state-sensitive questions;
- state limitations when exact current source was not read.

## Escalation rule

Escalate to procedure lookup, status review, governance audit, acceptance review, recovery review, Codex handoff, or storage update admission when the answer is state-sensitive or action-bearing.

## Forbidden use

- infer current Direction status;
- continue material work;
- accept candidate output;
- authorize or perform repository writes;
- route a semantic next move without admission.

## Required output

```text
answer:
limitations:
escalation_if_state_sensitive:
```

END_OF_FILE: workflow_v3/procedures/GENERIC_ANSWER_PROCEDURE.md
