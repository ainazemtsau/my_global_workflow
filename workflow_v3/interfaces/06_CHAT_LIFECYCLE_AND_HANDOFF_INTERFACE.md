# Chat Lifecycle and Handoff Interface

status: interface_summary

## Authority Pointers

Runtime authority lives in:

```text
workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md
```

Utility-call authority lives in:

```text
workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md
```

Final audit/closure authority lives in:

```text
workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md
```

This interface summarizes those protocols. It is not alternate lifecycle authority.

## Lifecycle Summary

```text
START -> RUN -> CHECK -> FINISH -> CLOSED
RUN -> UTILITY -> RUN
CHECK -> RUN repair or blocked escalation
FINISH -> RUN repair or blocked escalation if audit fails
```

START selects exactly one main procedure, reads that procedure, shows its completion contract, and waits for START / СТАРТ.

RUN executes visible material stages one at a time, emits `STAGE_RESULT`, and waits for CONTINUE / ДАЛЬШЕ before the next material stage unless the next step is `internal_check`.

UTILITY calls support the same selected main procedure and return as evidence through verified `UTILITY_RETURN`.

CHECK emits `CLOSURE_CHECK` by comparing actual result to the selected procedure's `completion:` block.

FINISH closes only after audit passes and returns `NEXT_CHAT_CARD` when continuation is needed, otherwise `no_next_chat_needed` with reason.

## Handoff Summary

A handoff or transfer is complete only when it gives the user copy-paste-ready content for the next surface. A new material chat uses `NEXT_CHAT_CARD`.

END_OF_FILE: workflow_v3/interfaces/06_CHAT_LIFECYCLE_AND_HANDOFF_INTERFACE.md