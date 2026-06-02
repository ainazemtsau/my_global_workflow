# Signal Routing Protocol

status: active_control_plane

## Core philosophy

Signal is fact. Handler output is candidate only. Action Inbox stores candidate actions.

Signals, Handlers, Event Loop Closure, and Progression Router do not launch work by themselves. Closure/router output does not silently launch next work.

## Phase-based signal disposition

Allowed dispositions:

```text
handle_inline_now
defer_to_closure
create_action_inbox_candidate
create_signal_chat_packet
create_codex_handoff
create_check_job
stop_current_run
ignore_with_reason
```

## Phase rules

Preparation/admission phase handles only blocking source, procedure, role, write, legacy, or acceptance issues inline.

Execution phase handles only run-safety issues inline.

Persistence/verification phase handles adapter, validation, and write-scope failures inline.

Closure phase may match handler registry and route one primary next move.

Multiple matched handlers do not all launch. Progression Router selects one primary disposition and returns secondary candidates.

## Off-scope signals

Non-blocking or off-scope signals may produce a Signal Chat Packet, Action Inbox candidate, Check Job, or ignored-with-reason record. They must not hijack the admitted run.

END_OF_FILE: workflow_v3/control_plane/SIGNAL_ROUTING_PROTOCOL.md
