# Runtime Console Runbook

status: active_repository_completion_framework

## Trigger condition

Use when a future adopted Direction needs read-only status, source orientation, uncertainty display, candidate packet drafting, or recovery orientation.

Trigger signals include `console_status_closed`, `source_signal`, `recovery_signal`, `inbox_signal`, or `blocked_lifecycle_transition`.

## Input sources

- accepted Direction runtime state after adoption;
- indexes, records, Action Inbox candidates, Check Jobs, and Event Loop Closures;
- `workflow_v3/RUNTIME_MODEL.md`;
- `workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md`.

## Source authority classification

Runtime Console may read verified state/indexes/records. It is not authority to mutate state. Project Files/Sources and console summaries are cache/context unless backed by exact records.

## Required templates

- `workflow_v3/templates/CURRENT_STATUS_TEMPLATE.md`
- `workflow_v3/templates/CURRENT_NEXT_MOVE_TEMPLATE.md`
- `workflow_v3/templates/TRANSITION_PACKET_TEMPLATE.md`
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md`

## Operating path

1. Read verified current state and indexes.
2. Summarize status, uncertainty, blockers, candidate actions, and stale context warnings.
3. Draft candidate Launch Packets or Next Moves when requested.
4. Do not execute material work.
5. Do not mutate state, accept evidence, promote Memory, launch Codex directly, or close Action Inbox items silently.
6. Emit Signals for source/recovery/inbox facts when material review occurs.
7. End with Event Loop Closure if review/routing occurred.

## Expected output

Read-only status, candidate packet or Next Move, source limitations, and exact return path.

## Closure signal

`console_status_closed`, `source_signal`, `recovery_signal`, `inbox_signal`, or `blocked_lifecycle_transition`.

## Return destination

Return to the user, parent chat, or acceptance/update path named by the console request.

## Acceptance/update requirement

Console output is candidate orientation only. Any state change requires explicit acceptance/update path.

## Failure/stop condition

Stop if Runtime Console starts executing work, deciding acceptance, routing product meaning, mutating state, or acting as hidden controller.

END_OF_FILE: workflow_v3/runbooks/RUNTIME_CONSOLE_RUNBOOK.md
