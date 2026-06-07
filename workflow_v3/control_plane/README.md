# Workflow v3 Control Plane

status: active_control_plane

## Purpose

`workflow_v3/control_plane/**` defines the Workflow v3 runtime kernel, procedure selection, child/adaptor boundary, final audit, source integrity, exceptions, and storage boundary.

The control plane does not execute product work, mutate Direction runtime state by itself, or replace selected procedure source.

## Authority

- `PROCEDURE_REGISTRY.md` selects exactly one main procedure.
- `CHAT_LIFECYCLE_PROTOCOL.md` governs START, RUN stages, child-return waits, CHECK, FINISH, and CLOSED.
- `UTILITY_ADAPTER_PROTOCOL.md` governs provider-neutral `CHILD_PROCEDURE_CALL` and `CHILD_PROCEDURE_RETURN`; legacy utility labels are compatibility aliases only.
- `CHAT_FINISH_PROTOCOL.md` governs final audit and closure.
- Source and storage protocols remain supporting boundaries.

## Runtime Flow

```text
Project Instructions bootloader
-> Procedure Registry
-> selected procedure source read
-> START_CONTRACT
-> RUN stage-by-stage
-> RUN_WAITING_FOR_CHILD_RETURN when child/adaptor work is opened
-> CHILD_RETURN_VERIFICATION
-> CLOSURE_CHECK
-> FINISH audit
-> CLOSED with post-closed NEXT_CHAT_CARD or no_next_chat_needed
```

## Boundary

Control-plane files do not authorize hidden accepted state, hidden launches, procedure switching, direct writes outside an admitted storage_update, package/card terminal completion, or reliance on unverified child/adaptor evidence.

END_OF_FILE: workflow_v3/control_plane/README.md
