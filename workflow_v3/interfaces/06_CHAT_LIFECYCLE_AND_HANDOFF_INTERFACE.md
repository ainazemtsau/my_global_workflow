# Chat Lifecycle and Dependency Interface

status: interface_summary

## Authority Pointers

Runtime authority lives in:

```text
workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md
```

Routing and dependency authority lives in:

```text
workflow_v3/control_plane/ROUTING_AND_DEPENDENCY_PROTOCOL.md
```

Support dependency packet authority lives in:

```text
workflow_v3/control_plane/SUPPORT_DEPENDENCY_PROTOCOL.md
```

Final audit/closure authority lives in:

```text
workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md
```

This interface summarizes those protocols. It is not alternate lifecycle authority.

## Lifecycle Summary

```text
START -> RUN -> CHECK -> FINISH -> CLOSED
RUN -> RUN_WAITING_FOR_DEPENDENCY_RETURN -> DEPENDENCY_RETURN_VERIFICATION -> RUN
CHECK -> RUN repair or blocked escalation
FINISH -> RUN repair or blocked escalation if audit fails
```

START selects exactly one main procedure, reads that procedure, shows its completion contract, and waits for START / СТАРТ.

RUN executes visible material stages one at a time, emits `STAGE_RESULT`, and waits for CONTINUE / ДАЛЬШЕ before the next material stage unless the next step is `internal_check`.

Dependency calls support the same selected main procedure and return as evidence through verified `DEPENDENCY_RETURN`. Prior packet labels are unsupported.

CHECK emits `CLOSURE_CHECK` by comparing actual result to the selected procedure's `completion:` block.

FINISH closes only after audit passes and returns post-closed `NEXT_CHAT_CARD` when a new independent continuation is needed, otherwise `no_next_chat_needed` with reason.

## Dependency And Transfer Summary

A dependency is complete only after a matching `DEPENDENCY_RETURN` is received, verified, and integrated by the same selected main procedure. A transfer or card can carry copy-paste-ready content for a later surface, but it is not current-goal completion and cannot replace a required dependency call.

END_OF_FILE: workflow_v3/interfaces/06_CHAT_LIFECYCLE_AND_HANDOFF_INTERFACE.md
