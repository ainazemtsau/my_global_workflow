# Signal, Handler, and Lifecycle Eval

status: active_repository_completion_framework

## Source files to inspect

- `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md`
- `workflow_v3/interfaces/03_DIRECTION_LIFECYCLE_SIGNAL_INTERFACE.md`
- `workflow_v3/interfaces/07_EVENT_LOOP_AND_ROUTING_INTERFACE.md`
- `workflow_v3/templates/SIGNAL_RECORD_TEMPLATE.md`
- `workflow_v3/templates/HANDLER_RESULT_TEMPLATE.md`
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md`
- `workflow_v3/runbooks/EVENT_LOOP_CLOSURE_RUNBOOK.md`

## Evidence required

- Signals emitted for notable lifecycle/material facts;
- handler matches and candidate outputs;
- Event Loop Closure;
- Progression Router Result;
- acceptance/update path for state changes.

## PASS criteria

- Signal is fact only and not task, command, Action Inbox item, acceptance, or mutation.
- Handler output is candidate only and not executor/acceptor.
- Lifecycle transition is visible through Signal, Handler, Event Loop Closure, and acceptance/update path.
- Progression Router selects one primary next move without executing it.

## WARN criteria

- Non-blocking signals are handled inline with limitations.
- Handler output is parked as candidate Action Inbox item with close condition.

## FAIL criteria

- Signal/Handler bypassed for lifecycle transition.
- Chat intuition route replaces Event Loop Closure.
- Handler executes material work or accepts state.
- Action Inbox stores raw signals as backlog.
- Check Job treated as material work.
- Event Loop Closure omitted after material work/review.

## Common failure modes

- Signal treated as task.
- Handler treated as automation engine.
- Progression Router treated as execution engine.

## Required recovery/repair action

Stop continuation, rerun Event Loop Closure, classify signals and handlers correctly, convert only valid candidate outputs, and require acceptance/update for state changes.

END_OF_FILE: workflow_v3/evals/SIGNAL_HANDLER_LIFECYCLE_EVAL.md
