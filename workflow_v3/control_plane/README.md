# Workflow v3 Control Plane

status: active_control_plane

## Purpose

`workflow_v3/control_plane/**` is Workflow v3's action-admission layer.

The control plane governs how chats become admitted runs. It does not execute product work, does not mutate Direction runtime state by itself, and does not replace procedure source.

## Authority

- The control plane is active repository source for Workflow v3 action admission.
- Project Instructions are bootloader only.
- GitHub/repository procedure files are dynamic canonical source after exact path/ref read and integrity verification.
- Every material chat or run must use admission before action.

## Admission flow

```text
Project Instructions bootloader
-> action admission
-> procedure registry
-> run surface contract
-> source integrity gate
-> chat lifecycle
-> signal routing by phase
-> exception protocol
-> storage update adapter boundary
```

## Boundary

Control-plane files define permission, routing, stop, and return rules. They do not authorize a chat to invent accepted state, execute a semantic next step, or write repository/runtime files without a separately admitted storage update adapter package.

END_OF_FILE: workflow_v3/control_plane/README.md
