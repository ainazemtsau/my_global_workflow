# Current Next Move Formation Eval

status: active_eval

## Purpose

Validate Current Next Move formation quality.

## PASS checks

- Uses the registered canonical `workflow_v3/procedures/CURRENT_NEXT_MOVE_FORMATION_PROCEDURE.md` source; legacy formation source may be cited only through the selected procedure's old_source_path / migration source during migration.
- Uses Result Packet, Next Move Packet, blockers, accepted state, pending acceptance, and current bottleneck.
- Selects exactly one primary next move.
- Provides reason, destination surface, acceptance/launch requirement, and complete Transfer Packet or Next Chat Prompt when needed.
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
