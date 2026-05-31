# Direction Spine Chat Runbook

status: active_repository_completion_framework

## Trigger condition

Use when a future adopted or adoption-candidate Direction needs a bounded chat for Direction Spine work only.

Trigger signals include `direction_spine_missing`, `direction_spine_candidate_returned`, or `blocked_lifecycle_transition`.

## Input sources

- accepted adoption package or explicit bootstrap decision;
- exact current Direction sources named by the package;
- `workflow_v3/interfaces/01_DIRECTION_STRUCTURE_INTERFACE.md`;
- `workflow_v3/templates/DIRECTION_SPINE_TEMPLATE.md`.

## Source authority classification

Accepted Direction state and exact repository files are authority. Old Direction files are `legacy_evidence` only when explicitly allowed. Project Files/Sources and chat memory are cache/context.

## Required templates

- `workflow_v3/templates/DIRECTION_SPINE_TEMPLATE.md`
- `workflow_v3/templates/RESULT_PACKET_TEMPLATE.md`
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md`
- `workflow_v3/templates/ACCEPTANCE_DECISION_TEMPLATE.md`

## Operating path

1. Bound the chat to Direction Spine work only.
2. Define root result, success conditions, spine points, tracks, constraints, explicit non-scope, sources, and open uncertainties.
3. Do not create Direction Map, Active Front, Work Graph, backlog, roadmap, or product implementation in this chat.
4. Mark every unsupported claim as candidate or unresolved.
5. Return a Direction Spine candidate and acceptance question.
6. Emit `direction_spine_candidate_returned` or `blocked_lifecycle_transition`.
7. End with Event Loop Closure and one exact Next Move.

## Expected output

Candidate Direction Spine, source limitations, unresolved decisions, acceptance question, Result Packet, and exact Next Move.

## Closure signal

`direction_spine_candidate_returned` or `blocked_lifecycle_transition`.

## Return destination

Return to the parent/adoption chat for acceptance/update review.

## Acceptance/update requirement

Direction Spine changes only through explicit Acceptance Decision and update path. This chat cannot accept its own result.

## Failure/stop condition

Stop if the chat starts creating Direction Map, Active Front, Work Graph, route decisions, or imported legacy state by implication.

END_OF_FILE: workflow_v3/runbooks/DIRECTION_SPINE_CHAT_RUNBOOK.md
