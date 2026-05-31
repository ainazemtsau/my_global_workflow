# Event Loop Closure Runbook

status: active_repository_completion_framework

## Trigger condition

Use after every material work run, review, Check Job, Codex verification, parent/child synthesis, acceptance decision, or blocked result.

Trigger signals include `material_run_closed`, `check_job_closed`, `codex_result_verified`, `acceptance_decision_recorded`, `work_contract_complete`, `active_front_complete`, or `blocked_result_returned`.

## Input sources

- current Result Packet or review result;
- Signals emitted during work;
- Handler Results;
- evidence and validation;
- parent/child status when relevant;
- `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md`.

## Source authority classification

Closure summarizes candidate and accepted evidence; it does not create accepted state. Exact repository files and accepted records remain authority.

## Required templates

- `workflow_v3/templates/SIGNAL_RECORD_TEMPLATE.md`
- `workflow_v3/templates/HANDLER_RESULT_TEMPLATE.md`
- `workflow_v3/templates/ACTION_INBOX_ITEM_TEMPLATE.md`
- `workflow_v3/templates/CHECK_JOB_TEMPLATE.md`
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md`
- `workflow_v3/templates/PROGRESSION_ROUTER_RESULT_TEMPLATE.md`
- `workflow_v3/templates/TRANSITION_PACKET_TEMPLATE.md`
- `workflow_v3/templates/CURRENT_NEXT_MOVE_TEMPLATE.md`

## Operating path

1. State what material work or review closed.
2. Emit notable Signals.
3. Match handlers in the required order.
4. List candidate outputs, blockers, human decision needs, Check Jobs, and Action Inbox candidates.
5. State persistence needs.
6. State parent/child status when relevant.
7. Run `progression_router_handler`.
8. Select one `primary_next_move`.
9. Include optional secondary candidates without launching them.
10. Provide a complete Transition Packet or Next Chat Prompt when transfer is needed.
11. State exact Next Move.

## Expected output

Event Loop Closure record, Progression Router Result, exact Next Move, and complete Transition Packet when external transfer is selected.

## Closure signal

One of the trigger signals above, plus blocker signal when applicable.

## Return destination

Return to the current chat or acceptance/update path named by the closure.

## Acceptance/update requirement

Closure and router output are candidate unless explicitly accepted or launched. State changes require Acceptance Decision/update path.

## Failure/stop condition

Stop if routing is chosen by intuition, multiple next steps are launched silently, a blocking signal is ignored, or the user is left to assemble transfer packets manually.

END_OF_FILE: workflow_v3/runbooks/EVENT_LOOP_CLOSURE_RUNBOOK.md
