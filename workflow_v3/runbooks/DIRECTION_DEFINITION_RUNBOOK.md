# Direction Definition Runbook

status: active_direction_definition_runbook

## Purpose

Direction Definition is the first semantic entity-formation process after setup-only root exists.

It forms candidate Direction Spine, Direction Map, and first Active Front. It does not execute product work and does not open Work Graph before Active Front acceptance.

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

## Candidate context handling

Use `candidate_context_for_direction_definition` as candidate context only.

It may seed alternatives, constraints, or evidence questions. It cannot bypass formation and cannot be accepted by setup.

## Formation sequence

1. Direction Spine Formation creates candidate Spine with alternatives, proof signals, non-goals, risks, cuts, acceptance question, closure, and next move.
2. Direction Map Formation creates candidate Map from the Spine candidate and evidence labels.
3. Active Front Formation creates first candidate Active Front from Direction Map areas.

Default: one steering entity per material formation chat. A parent Definition chat may sequence these if each entity's candidate, evidence, risks, cuts, acceptance question, closure, and next move remain separate.

## Acceptance boundary

Definition returns candidate entities.

Acceptance requires explicit Acceptance Decision/update path. No Direction Spine, Direction Map, or Active Front becomes accepted merely because Definition produced it.

## Closure

Return:

```text
result_packet:
candidate_spine:
candidate_map:
candidate_active_front:
evidence:
source_read_limitations:
risks:
cuts:
acceptance_questions:
event_loop_closure:
primary_next_move:
```

## Stop conditions

Stop if setup-only root is absent, `CURRENT_NEXT_MOVE` is not `launch_direction_definition`, source reads are missing, product execution starts, Work Graph is requested before Active Front acceptance, or candidate context is treated as accepted state.

END_OF_FILE: workflow_v3/runbooks/DIRECTION_DEFINITION_RUNBOOK.md
