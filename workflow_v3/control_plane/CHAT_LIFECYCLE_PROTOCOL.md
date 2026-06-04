# Chat Lifecycle Protocol

status: active_control_plane

## Authority

This file is the authoritative Workflow v3 chat lifecycle kernel for material and state-sensitive chats.

## Universal law

Every material or state-sensitive chat response must enter START before work, execute exactly one admitted procedure in RUN, and close through FINISH or typed STOP.

## State machine

START -> RUN -> FINISH
START -> STOP
RUN -> STOP
RUN -> FINISH_REQUEST
FINISH_REQUEST -> FINISH
FINISH -> closed

## START

START selects one procedure and proves that it can be executed.

START must:
- classify the user input;
- detect requested work items;
- select exactly one work item;
- return SPLIT_REQUIRED when more than one independent work item is requested;
- resolve selected procedure through expanded Procedure Registry;
- read exact required source files;
- identify run_surface_type;
- read the matching run surface contract;
- record selected complexity, checkpoint policy, or research policy only after selected procedure source is read;
- show START_PACKET;
- wait for explicit user token START or СТАРТ before RUN.

## RUN

RUN executes only the procedure selected in START.

RUN must:
- execute only selected_procedure_ref;
- obey selected run_surface_type;
- obey allowed_operations, forbidden_operations, required_inputs, required_outputs, and stop_conditions;
- execute the selected procedure as a stage/gate loop when the procedure uses the Procedure Definition Framework;
- treat stage checkpoints as internal RUN gates, not lifecycle phases;
- treat any request for another procedure as BOUNDARY_CROSSING_STOP;
- produce FINISH_REQUEST when the selected procedure reaches its completion condition;
- never mutate state unless the selected procedure is storage_update_adapter;
- never accept its own output.

The Procedure Definition Framework cannot authorize procedure switching.

FINISH_REQUEST remains the only transition from RUN to FINISH.

## FINISH_REQUEST

FINISH_REQUEST is the only transition from RUN to FINISH.

FINISH_REQUEST must:
- summarize selected work result;
- list unresolved items;
- list candidate state;
- state that FINISH requires explicit user token FINISH or ФИНИШ;
- not emit FINISH_PACKET before explicit FINISH.

## FINISH

FINISH closes the chat.

FINISH must:
- read CHAT_FINISH_PROTOCOL.md before emitting final closure;
- audit that START selected one procedure and RUN did not switch procedures;
- emit FINISH_PACKET;
- emit Result Packet;
- emit Next Move Packet;
- select exactly one primary next move;
- not launch the next move invisibly.

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

## Phase mapping

START contains old Phase 0, Phase 1, and Phase 2.
RUN contains old Phase 3 and selected-procedure execution.
FINISH contains old Phase 4, Phase 5, Phase 6, and Phase 7 only when those boundaries are admitted.
Skipped old phases require a reason in FINISH_PACKET.

END_OF_FILE: workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md
