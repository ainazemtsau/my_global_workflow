# Workflow v3 Entity Formation Layer

status: active_entity_formation_layer

## Purpose

`workflow_v3/formation/**` defines how high-impact steering entities are formed before they are written into templates or proposed for acceptance.

Formation is the reasoning and collaboration process. Templates are storage/result shapes. Interfaces define boundaries. Runbooks define operating paths. Runtime state exists only under a future accepted `directions_v3/<direction-id>/runtime/**` package.

This layer is repository source only. It does not adopt a Direction, create runtime state, update actual ChatGPT Project Instructions UI, refresh Project Files/Sources, or accept any entity.

## Steering entities requiring formation

- Direction Spine
- Direction Map
- Active Front
- Work Graph
- Work Contract
- Current Next Move
- Acceptance Decision
- Memory Artifact promotion

## Operational entities

Operational entities may remain mostly template-driven when their source, evidence, candidate status, and closure boundaries are preserved:

- Signal Record
- Handler Result
- Action Inbox Item
- Check Job
- Event Loop Closure
- Transition Packet
- Run Record
- Evidence Record
- Result Packet
- Parent Recovery Block

## Protocol index

- `ENTITY_FORMATION_CANON.md` - canonical rules for steering-entity formation.
- `DECISION_QUALITY_PROTOCOL.md` - alternatives, criteria, tradeoffs, evidence, and acceptance question.
- `FOCUS_AND_WASTE_CUT_PROTOCOL.md` - bottleneck, value, scope, proof path, and deferred-work checks.
- `EVIDENCE_AND_HYPOTHESIS_PROTOCOL.md` - assumptions, proof signals, evidence classes, tests, and labels.
- `ANTI_BIAS_AND_RED_TEAM_PROTOCOL.md` - contradiction, premortem, stale-context, over-agreement, and false-certainty checks.
- `STEERING_ENTITY_FORMATION_CHAT_PROTOCOL.md` - bounded chat lifecycle for one steering entity.

## Formation runbook index

- `DIRECTION_SPINE_FORMATION_RUNBOOK.md`
- `DIRECTION_MAP_FORMATION_RUNBOOK.md`
- `ACTIVE_FRONT_FORMATION_RUNBOOK.md`
- `WORK_GRAPH_FORMATION_RUNBOOK.md`
- `WORK_CONTRACT_FORMATION_RUNBOOK.md`
- `CURRENT_NEXT_MOVE_FORMATION_RUNBOOK.md`
- `ACCEPTANCE_DECISION_FORMATION_RUNBOOK.md`
- `MEMORY_ARTIFACT_PROMOTION_RUNBOOK.md`

## Default chat rule

One material formation chat forms one steering entity by default.

A Direction Definition parent chat may sequence multiple formation chats only when each entity target remains bounded and visible. Child research or check chats may support the current formation target, but their outputs return to the parent formation chat and cannot decide or accept the entity.

## Candidate and accepted boundary

Formation produces a candidate entity by default.

Accepted state requires an explicit Acceptance Decision or accepted update path. User phrasing, model synthesis, child results, evidence, or template completion do not bypass that boundary.

END_OF_FILE: workflow_v3/formation/README.md
