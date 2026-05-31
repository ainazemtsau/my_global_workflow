# Direction Map Chat Runbook

status: active_repository_completion_framework

## Trigger condition

Use when a future adopted or adoption-candidate Direction needs a bounded chat for Direction Map work only.

Trigger signals include `direction_map_missing`, `direction_map_candidate_returned`, `direction_map_update_needed`, `direction_map_stale`, or `track_imbalance_detected`.

## Input sources

- accepted Direction Spine or candidate Spine explicitly supplied for review;
- exact evidence and accepted records named by the package;
- `workflow_v3/interfaces/02_DIRECTION_MAP_INTERFACE.md`;
- `workflow_v3/templates/DIRECTION_MAP_TEMPLATE.md`.

## Source authority classification

Accepted records and exact repository files are authority. Unsupported map claims must be labeled candidate, unresolved, or hypothetical. Project Files/Sources are cache/context. Old files are `legacy_evidence` only.

## Required templates

- `workflow_v3/templates/DIRECTION_MAP_TEMPLATE.md`
- `workflow_v3/templates/RESULT_PACKET_TEMPLATE.md`
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md`
- `workflow_v3/templates/ACCEPTANCE_DECISION_TEMPLATE.md`

## Operating path

1. Bound the chat to Direction Map work only.
2. Identify tracks, map areas, strategic dependencies, strategic uncertainties, candidate fronts, blocked areas, closed fronts, evidence links, and labels.
3. Keep Direction Map distinct from roadmap, backlog, Work Graph, Action Inbox, and chat plan.
4. Label every claim as accepted, candidate, unresolved, or hypothetical.
5. Return map update candidates and acceptance question.
6. Emit applicable lifecycle signals.
7. End with Event Loop Closure and one exact Next Move.

## Expected output

Candidate Direction Map or candidate map update, claim labels, evidence references, unresolved gaps, Result Packet, and exact Next Move.

## Closure signal

`direction_map_candidate_returned`, `direction_map_update_needed`, or `blocked_lifecycle_transition`.

## Return destination

Return to parent/adoption or Direction review chat for acceptance/update decision.

## Acceptance/update requirement

Direction Map changes only through explicit Acceptance Decision and update path.

## Failure/stop condition

Stop if the map is flattened into Direction Spine, roadmap, backlog, Work Graph, Action Inbox, or unsupported route choice.

END_OF_FILE: workflow_v3/runbooks/DIRECTION_MAP_CHAT_RUNBOOK.md
