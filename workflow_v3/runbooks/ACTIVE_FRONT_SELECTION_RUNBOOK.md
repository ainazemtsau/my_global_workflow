# Active Front Selection Runbook

status: active_repository_completion_framework

## Trigger condition

Use when an adopted or adoption-candidate Direction needs a candidate Active Front selected from the Direction Map.

Trigger signals include `active_front_missing`, `active_front_candidate_returned`, `direction_map_update_needed`, or `blocked_lifecycle_transition`.

## Input sources

- accepted Direction Spine;
- accepted or candidate Direction Map;
- relevant evidence, decisions, blockers, and user priorities;
- `workflow_v3/interfaces/04_ACTIVE_FRONT_SELECTION_INTERFACE.md`;
- `workflow_v3/templates/ACTIVE_FRONT_TEMPLATE.md`.

## Source authority classification

Accepted records and exact repository files are authority. Project Files/Sources are cache/context. Legacy evidence is not current accepted state.

## Required templates

- `workflow_v3/templates/ACTIVE_FRONT_TEMPLATE.md`
- `workflow_v3/templates/FRONT_TEMPLATE.md`
- `workflow_v3/templates/RESULT_PACKET_TEMPLATE.md`
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md`
- `workflow_v3/templates/ACCEPTANCE_DECISION_TEMPLATE.md`

## Operating path

1. Name source map area or areas.
2. Name touched tracks.
3. State bottleneck or uncertainty.
4. State `why_now`.
5. Provide selection evidence.
6. List rejected/deferred alternatives.
7. Define exit criteria.
8. Define in scope and out of scope.
9. Provide first Work Graph seed derived from exit criteria.
10. Ask the acceptance question.
11. Emit `active_front_candidate_returned` or blocker signal.
12. End with Event Loop Closure and Progression Router result.

## Expected output

Candidate Active Front packet with map areas, touched tracks, why-now, evidence, rejected alternatives, exit criteria, Work Graph seed, and acceptance question.

## Closure signal

`active_front_candidate_returned` or `blocked_lifecycle_transition`.

## Return destination

Return to parent/adoption or Direction review chat for acceptance/update decision.

## Acceptance/update requirement

Active Front is candidate until explicit Acceptance Decision and accepted state update.

## Failure/stop condition

Stop if Active Front is selected by chat intuition, without map areas/evidence, or treated as all active work or Work Graph.

END_OF_FILE: workflow_v3/runbooks/ACTIVE_FRONT_SELECTION_RUNBOOK.md
