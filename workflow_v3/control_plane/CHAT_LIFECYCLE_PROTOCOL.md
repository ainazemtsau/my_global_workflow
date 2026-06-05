# Chat Lifecycle Protocol

status: active_control_plane

## Authority

This file is the authoritative Workflow v3 chat lifecycle kernel for material and state-sensitive chats.

Embedded utility/adapter behavior is governed by:

```text
workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md
```

## Universal law

Every material or state-sensitive chat response must enter START before work, execute exactly one admitted owner procedure in RUN, and close through FINISH or typed STOP.

## State machine

START -> RUN
START -> STOP
RUN -> RUN_EXTERNAL_HANDOFF
RUN_EXTERNAL_HANDOFF -> RUN_EXTERNAL_RETURN
RUN_EXTERNAL_RETURN -> RUN
RUN -> STOP
RUN -> FINISH_REQUEST
FINISH_REQUEST -> FINISH
FINISH -> closed

`RUN_EXTERNAL_HANDOFF` and `RUN_EXTERNAL_RETURN` are internal RUN gates. They are not lifecycle phases that select another procedure.

After FINISH, the chat is closed for material work. A new material START in the same chat is forbidden.

## START

START selects one owner procedure and proves that it can be executed.

START must:
- classify the user input;
- detect requested work items;
- select exactly one work item;
- return SPLIT_REQUIRED when more than one independent work item is requested;
- resolve selected owner procedure through expanded Procedure Registry;
- read exact required source files;
- identify run_surface_type and procedure_class;
- read the matching run surface contract;
- read `UTILITY_ADAPTER_PROTOCOL.md` when utility/adapter categories or external handoff boundaries are relevant;
- record selected complexity, checkpoint policy, research policy, or utility policy only after selected procedure source is read;
- show START_PACKET;
- wait for explicit user token START or СТАРТ before RUN.

## RUN

RUN executes only the owner procedure selected in START.

RUN must:
- execute only selected_procedure_ref;
- obey selected run_surface_type;
- obey allowed_operations, forbidden_operations, required_inputs, required_outputs, utility notes, Utility Use Gate, and stop_conditions;
- execute the selected procedure as a stage/gate loop when the procedure uses the Procedure Definition Framework;
- treat stage checkpoints and embedded utility/adapter gates as internal RUN gates, not lifecycle phases;
- treat any request for another owner procedure as BOUNDARY_CROSSING_STOP unless the selected procedure emits a bounded utility packet through the Utility Use Gate;
- produce RUN_EXTERNAL_HANDOFF when an external utility result is required before completion and the Utility Use Gate passes;
- resume the same selected owner procedure after RUN_EXTERNAL_RETURN;
- produce FINISH_REQUEST only when the selected procedure reaches its completion or blocked condition and no required external return is pending;
- never mutate state unless the selected procedure is storage_update_adapter;
- never accept its own output.

The Procedure Definition Framework and Utility Adapter Protocol cannot authorize procedure switching.

FINISH_REQUEST remains the only transition from RUN to FINISH.

## RUN_EXTERNAL_HANDOFF

RUN_EXTERNAL_HANDOFF is a typed internal RUN gate used when the selected owner procedure needs an external utility result before completion.

RUN_EXTERNAL_HANDOFF must follow `UTILITY_ADAPTER_PROTOCOL.md` and include a complete `copy_paste_packet`, expected return fields, validation requirements, and same-owner resume rule.

RUN_EXTERNAL_HANDOFF must not:
- select a new owner procedure;
- emit FINISH_REQUEST;
- ask the external surface to perform ChatGPT lifecycle FINISH;
- authorize mutation, acceptance, or hidden next work beyond the packet.

## RUN_EXTERNAL_RETURN

RUN_EXTERNAL_RETURN resumes the same selected owner procedure after the user returns external evidence.

RUN_EXTERNAL_RETURN must:
- match the returned evidence to the pending handoff;
- classify the return as adapter evidence until verified;
- perform required embedded verification or stop with exact missing evidence;
- continue only the selected owner procedure.

## FINISH_REQUEST

FINISH_REQUEST is the only transition from RUN to FINISH.

FINISH_REQUEST must:
- summarize selected work result;
- list unresolved items;
- list candidate state;
- state that FINISH requires explicit user token FINISH or ФИНИШ;
- confirm that required external handoffs have returned, been verified, or been explicitly stopped/abandoned;
- not emit FINISH_PACKET before explicit FINISH.

## FINISH

FINISH closes the chat.

FINISH must:
- read CHAT_FINISH_PROTOCOL.md before emitting final closure;
- audit that START selected one owner procedure and RUN did not switch procedures;
- audit that no required external return is pending;
- emit FINISH_PACKET;
- emit Result Packet;
- emit Next Move Packet;
- select exactly one primary next move;
- not launch the next move invisibly.

After FINISH, only non-material clarification about the closed result or pointers to emitted packets are allowed in the same chat.

## STOP

STOP is terminal for the current attempted transition.

STOP types:
- SPLIT_REQUIRED
- CONTEXT_REQUEST
- UNREGISTERED_ACTION_EXCEPTION
- SOURCE_AUTHORITY_CONFLICT
- BINDING_CONFLICT
- MISSING_RUN_SURFACE_TYPE
- BOUNDARY_CROSSING_STOP
- WRITE_NOT_ADMITTED
- ACCEPTANCE_AMBIGUITY
- LEGACY_BOUNDARY_STOP
- VALIDATION_REQUIRED_STOP
- SOURCE_INTEGRITY_STOP
- EXTERNAL_RETURN_REQUIRED_STOP
- UTILITY_BOUNDARY_STOP

## Phase mapping

START contains old Phase 0, Phase 1, and Phase 2.
RUN contains old Phase 3, selected-procedure execution, and any allowed RUN_EXTERNAL_HANDOFF / RUN_EXTERNAL_RETURN gates.
FINISH contains old Phase 4, Phase 5, Phase 6, and Phase 7 only when those boundaries are admitted.
Skipped old phases or utility gates require a reason in FINISH_PACKET.

END_OF_FILE: workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md
