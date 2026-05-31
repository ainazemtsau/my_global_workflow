# Event Loop and Routing Interface

status: active_interface_layer

## Purpose

This file defines the Workflow v3 operational event loop and routing boundary.

## Owner/surface

Owner/surface: Signals, Handlers, Action Inbox/Q, Check Jobs, Event Loop Closure, Progression Router, and Next Move selection.

## Persistence target

Persistence target: `workflow_v3/interfaces/04_EVENT_LOOP_AND_ROUTING_INTERFACE.md` for shared rules; future adopted Direction operational records belong under `directions_v3/<direction-id>/runtime/operations/**` after explicit adoption and acceptance.

## Event loop contract

The operational flow is:

```text
Signal -> Handler -> Candidate Output / Check Job / Next Move -> Event Loop Closure
```

Signal is an emitted workflow event/fact record.

Signal is not a task, command, Q item, mutation, acceptance, Action Inbox item, or accepted-state update.

Handler reacts to a Signal by creating candidate output only.

Action Inbox/Q stores candidate actions, not raw signals.

Check Job is bounded verification.

Event Loop Closure is required after material work or review.

Progression Router runs during closure after candidate outputs and blockers are visible.

## Handler outputs

Handler output may be no action, inline note, Action Inbox candidate, Check Job, blocked result, repair Next Move, primary Next Move, secondary candidate, candidate Launch Packet, Transition Packet, next-chat prompt, stop condition, or human decision request.

Handler output remains candidate until accepted, converted, dropped, or explicitly launched.

## Event Loop Closure requirements

Closure must state:

- material work or review closed;
- Signals emitted;
- Handlers matched;
- candidate outputs;
- Check Jobs created or needed;
- Action Inbox candidates;
- blockers or human decisions needed;
- persistence needs;
- Progression Router result;
- exact Next Move;
- Transition Packet when transfer is needed.

## Progression Router boundary

Progression Router selects one `primary_next_move`.

Secondary candidates are optional only after the primary selection.

Progression Router may produce a candidate Launch Packet, next-chat prompt, or Transition Packet for the selected next step.

Progression Router must not execute work, accept state, launch Codex, launch child chats, mutate files, bypass acceptance, import legacy state, use Action Inbox as hidden roadmap, or continue product work after a blocking signal.

## Routing stop rules

No silent child launch.

No hidden roadmap.

No continuation after a blocking signal.

No next material chat before the current material target is accepted, persisted, verified, or explicitly stopped.

Codex handoff returns to the same current chat for verification and closure.

## Inputs

Inputs are Signals, Handler Results, candidate outputs, Check Job findings, Result Packets, Acceptance Decisions, blockers, and current closure context.

## Outputs

Outputs are candidate actions, Check Jobs, blocked results, repair Next Moves, primary Next Move, optional secondary candidates, Transition Packets, next-chat prompts, and stop conditions.

## State mutation rights

Signals, Handlers, Action Inbox/Q, Check Jobs, Event Loop Closure, and Progression Router output do not mutate accepted state.

Persistence of operational records requires explicit acceptance/update scope and future adopted Direction storage.

## Allowed producers

Allowed producers are material work chats, review chats, Check Jobs, Codex result verification, human decisions, parent chats, and explicit handler runs.

## Allowed consumers

Allowed consumers are parent closure, Runtime Console, Acceptance review, Check Jobs, Codex handoffs, child chat launches, next material chats, and Action Inbox review.

## Validation/evidence requirement

Closure validation must show that blocking handlers ran first, acceptance was not bypassed, one primary Next Move was selected, transfer packets are complete when needed, and candidate outputs remain candidate unless explicitly accepted or launched.

## Forbidden behaviors

- Treating Signals as tasks or accepted state.
- Letting Handlers execute material work.
- Storing raw Signals as Action Inbox backlog.
- Omitting Event Loop Closure after material work/review.
- Selecting multiple primary next moves.
- Silently launching child chats or Codex.
- Continuing after blocking source, validation, recovery, or legacy signals.
- Treating Action Inbox/Q as roadmap.

## Failure/recovery path

When closure is missing, rerun same-scope Event Loop Closure.

When routing is unsafe, stop and return a blocked result or human decision request.

When verification is needed, create a bounded Check Job.

When a next step needs transfer, return a complete Transition Packet instead of partial fragments.

## Dependencies

- `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md`
- `workflow_v3/RUNTIME_MODEL.md`
- `workflow_v3/QUALITY_AND_RECOVERY.md`
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md`
- `workflow_v3/templates/PROGRESSION_ROUTER_RESULT_TEMPLATE.md`
- `workflow_v3/templates/TRANSITION_PACKET_TEMPLATE.md`

END_OF_FILE: workflow_v3/interfaces/04_EVENT_LOOP_AND_ROUTING_INTERFACE.md
