# Work Graph Opening Runbook

status: active_repository_completion_framework

## Trigger condition

Use when an accepted Active Front lacks a local Work Graph or needs the first local node structure.

Trigger signals include `work_graph_missing`, `work_graph_created`, `work_graph_node_ready`, or `blocked_lifecycle_transition`.

## Input sources

- accepted Active Front;
- Front Exit Criteria;
- Direction Map areas referenced by the front;
- relevant evidence and blockers;
- `workflow_v3/interfaces/05_WORK_GRAPH_AND_NODE_INTERFACE.md`.

## Source authority classification

Accepted Active Front and exact repository files are authority. Work Graph is local candidate/workspace structure until accepted or persisted through the authorized path.

## Required templates

- `workflow_v3/templates/WORK_GRAPH_TEMPLATE.md`
- `workflow_v3/templates/WORK_GRAPH_NODE_TEMPLATE.md`
- `workflow_v3/templates/NODE_CLOSURE_SUMMARY_TEMPLATE.md`
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md`

## Operating path

1. Confirm accepted Active Front and exit criteria.
2. Derive local nodes from exit criteria and evidence requirements.
3. Name dependencies, blockers, expected evidence, and closure conditions.
4. Select one next useful node candidate.
5. Do not build a global roadmap, backlog, or Direction Map replacement.
6. Emit `work_graph_created` and/or `work_graph_node_ready`.
7. End with Event Loop Closure and exact Next Move.

## Expected output

Candidate local Work Graph, bounded node list, selected node candidate, evidence requirements, and next Work Contract candidate.

## Closure signal

`work_graph_created`, `work_graph_node_ready`, or `blocked_lifecycle_transition`.

## Return destination

Return to the current Direction/parent chat for Work Contract creation or acceptance/update review.

## Acceptance/update requirement

Persisting or treating the Work Graph as accepted requires explicit acceptance/update path. It does not update Direction Map by itself.

## Failure/stop condition

Stop if Work Graph becomes roadmap, backlog, global Direction Map, Action Inbox, or unrelated task list.

END_OF_FILE: workflow_v3/runbooks/WORK_GRAPH_OPENING_RUNBOOK.md
