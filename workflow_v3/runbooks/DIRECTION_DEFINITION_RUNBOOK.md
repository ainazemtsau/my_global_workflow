# Direction Definition Runbook

status: active_direction_definition_runbook

## Purpose

Direction Definition is the first semantic entity-formation process after setup-only root exists.

Direction Definition is a procedure family for forming the next required steering entity candidate after setup-only root exists.

It does not execute product work and does not open Work Graph before Active Front acceptance.

It may not persist accepted Spine/Map/Front, status, next move, acceptance records, or event loop closure files.

Each acceptance signal routes to acceptance/storage procedure; it does not authorize Definition chat writes.

## Trigger

Use when setup-only root exists and:

```text
CURRENT_NEXT_MOVE = launch_direction_definition
```

## Source reads

Read:

- bound `CURRENT_STATUS.md`;
- bound `CURRENT_NEXT_MOVE.md`;
- `workflow_v3/formation/ENTITY_FORMATION_CANON.md`;
- `workflow_v3/formation/STEERING_ENTITY_FORMATION_CHAT_PROTOCOL.md`;
- `workflow_v3/formation/DIRECTION_SPINE_FORMATION_RUNBOOK.md`;
- `workflow_v3/formation/DIRECTION_MAP_FORMATION_RUNBOOK.md`;
- `workflow_v3/formation/ACTIVE_FRONT_FORMATION_RUNBOOK.md`.

Stop if exact source cannot be read or if setup-only root is not confirmed.

## Direction Definition execution policy

Direction Definition is a procedure family. A single chat RUN executes exactly one selected procedure.

Default selection order:
1. If no accepted Direction Spine exists, select form_direction_spine only.
2. If accepted Direction Spine exists and no accepted Direction Map exists, select form_direction_map only.
3. If accepted Direction Map exists and no accepted Active Front exists, select form_active_front only.

The selected procedure must be named in START_PACKET.

A chat must not form Direction Spine, Direction Map, and Active Front in one RUN.

A chat must not continue from Spine to Map or from Map to Active Front during RUN.

After the selected procedure reaches completion, emit FINISH_REQUEST.

Next entity formation requires a new START after FINISH.

## Candidate context handling

Use `candidate_context_for_direction_definition` as candidate context only.

It may seed alternatives, constraints, or evidence questions. It cannot bypass formation and cannot be accepted by setup.

## Formation sequence

The selected formation procedure creates only its selected candidate with alternatives, proof signals, non-goals, risks, cuts, acceptance question, closure inputs, and next move.

Unselected formation procedures are deferred and require a separate START after FINISH.

## Acceptance boundary

Definition returns candidate entities.

Acceptance requires explicit Acceptance Decision/update path. No Direction Spine, Direction Map, or Active Front becomes accepted merely because Definition produced it.

Definition chat is a `formation_chat` surface and is non-mutating.

## Closure

Return:

```text
result_packet:
selected_procedure_result:
evidence:
source_read_limitations:
risks:
cuts:
acceptance_question:
event_loop_closure:
primary_next_move:
```

## Stop conditions

Stop if setup-only root is absent, `CURRENT_NEXT_MOVE` is not `launch_direction_definition`, source reads are missing, product execution starts, Work Graph is requested before Active Front acceptance, or candidate context is treated as accepted state.

END_OF_FILE: workflow_v3/runbooks/DIRECTION_DEFINITION_RUNBOOK.md
