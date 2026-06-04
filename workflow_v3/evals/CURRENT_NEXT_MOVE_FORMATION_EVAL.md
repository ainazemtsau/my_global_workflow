# Current Next Move Formation Eval

status: active_eval

## Purpose

Validate Current Next Move formation quality.

## PASS checks

- Uses `workflow_v3/formation/CURRENT_NEXT_MOVE_FORMATION_RUNBOOK.md`.
- Uses Result Packet, Next Move Packet, blockers, accepted state, pending acceptance, and current bottleneck.
- Selects exactly one primary next move.
- Provides reason, destination surface, acceptance/launch requirement, and complete Transition Packet or Next Chat Prompt when needed.
- Rejects vague "continue" without exact packet.
- Does not silently launch multiple steps.

## WARN checks

- Next move is candidate because acceptance is pending.
- Source read limitations block launch and are reported.

## FAIL checks

- Multiple primary next moves are returned.
- Next move is vague.
- Closure or accepted state is missing.
- Product work starts without bounded admitted contract.

END_OF_FILE: workflow_v3/evals/CURRENT_NEXT_MOVE_FORMATION_EVAL.md
