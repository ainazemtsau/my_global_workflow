# Current Next Move Formation Runbook

status: active_formation_runbook

## Trigger

Use after Event Loop Closure, status review, acceptance review, blocker handling, or continuation routing needs exactly one primary next move.

## Inputs

- Event Loop Closure;
- Progression Router candidate if any;
- accepted state and pending acceptance;
- blockers;
- current bottleneck or constraint;
- possible destinations and return destination.

## Source reads

Read `CURRENT_STATUS.md`, `CURRENT_NEXT_MOVE.md` if present, the closure record, and any accepted/pending decision records needed to choose the next move.

## Formation steps

1. Confirm the target is Current Next Move only.
2. Classify accepted state, candidate results, blockers, and pending decisions.
3. Frame what the next move must resolve.
4. Generate candidate next moves unless only one is valid.
5. Define criteria: accepted-state readiness, bottleneck relief, closure need, transfer completeness, risk, and reversibility.
6. Identify evidence and missing decisions.
7. Attack vague "continue", multiple-primary moves, hidden launch, and product work without admitted contract.
8. Cut secondary candidates from primary execution.
9. Draft exactly one primary next move.
10. Record rejected/deferred moves.
11. State read limitations.
12. Ask acceptance/launch question when stateful.
13. Close the event loop.
14. Provide complete Transition Packet or Next Chat Prompt when needed.

## Must include

- exactly one primary next move;
- reason;
- destination surface;
- same-chat or new-chat status;
- acceptance/launch requirement;
- complete Transition Packet or Next Chat Prompt when transfer is needed.

## Outputs

Return a candidate Current Next Move compatible with `workflow_v3/templates/CURRENT_NEXT_MOVE_TEMPLATE.md`.

## Acceptance boundary

Next Move is candidate until accepted, persisted, or explicitly launched.

## Stop conditions

Stop if accepted state is unreadable, closure is missing, the move would be vague, or multiple independent primary moves are needed.

## Run-surface boundary

Formation chat is non-mutating.

After acceptance-like human input, stop with Transition Packet to `acceptance_review` / `storage_update_adapter`. Do not create acceptance records, mutate repository state, update CURRENT_STATUS, update CURRENT_NEXT_MOVE, persist Event Loop Closure files, launch Codex, or continue across role boundary.

END_OF_FILE: workflow_v3/formation/CURRENT_NEXT_MOVE_FORMATION_RUNBOOK.md
