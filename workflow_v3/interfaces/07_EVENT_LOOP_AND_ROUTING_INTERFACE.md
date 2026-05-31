# Event Loop and Routing Interface

status: active_interface_layer

## Purpose

This interface defines Event Loop Closure, Signal/Handler, Action Inbox, Check Jobs, and Progression Router behavior.

It reconciles the interface layer with `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md`.

## Signal

Signal is fact only.

Signal is not:

- task;
- command;
- acceptance;
- mutation;
- Action Inbox item;
- hidden route selection.

## Handler

Handler output is candidate only.

A Handler may create candidate outputs such as inline note, Action Inbox candidate, Check Job, repair Next Move, candidate packet, blocked result, stop condition, or human decision request.

A Handler must not execute work, accept state, launch hidden children, or become a hidden roadmap.

## Action Inbox

Action Inbox stores candidate actions, not raw Signals.

Action Inbox is not roadmap, backlog, automatic execution queue, or global project manager.

## Check Job

Check Job is bounded verification. It answers a scoped source, evidence, consistency, or risk question and returns candidate findings.

Check Job is not material execution or acceptance.

## Event Loop Closure

Event Loop Closure is required after material work/review.

Closure must make visible:

- material work or review closed;
- emitted Signals;
- matched Handlers;
- candidate outputs;
- blocking or human decision needs;
- persistence needs;
- closure signal;
- parent/child status if relevant;
- Progression Router result;
- exact Next Move.

## Progression Router

Progression Router selects one `primary_next_move`.

It may include optional secondary candidates, but must not silently launch more than one next step.

Router output is candidate until accepted or explicitly launched.

## Hard rules

- No hidden launches.
- No hidden roadmap.
- No product work after a blocking signal.
- No chat-intuition routing.
- Transfer steps require a complete Transition Packet or Next Chat Prompt.
- Codex handoff returns to current chat for verification/closure.
- Next material chat waits until current material target is accepted, persisted, verified, or explicitly stopped.

END_OF_FILE: workflow_v3/interfaces/07_EVENT_LOOP_AND_ROUTING_INTERFACE.md
