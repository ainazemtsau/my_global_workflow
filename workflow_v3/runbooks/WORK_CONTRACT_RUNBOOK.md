# Work Contract Runbook

status: active_repository_completion_framework

## Trigger condition

Use when a Work Graph Node is ready for bounded execution by ChatGPT, Codex, human action, or another adapter.

Trigger signals include `work_graph_node_ready`, `work_contract_created`, `work_contract_complete`, or `material_run_closed`.

## Input sources

- accepted Active Front and local Work Graph;
- selected Work Graph Node;
- exact repository or domain sources needed for the run;
- adapter/provider setup boundaries;
- `workflow_v3/templates/WORK_CONTRACT_TEMPLATE.md`.

## Source authority classification

Accepted records and exact sources named in the contract are authority. Adapter output, Project cache, and prior chat are candidate/context until verified.

## Required templates

- `workflow_v3/templates/WORK_CONTRACT_TEMPLATE.md`
- `workflow_v3/templates/RUN_RECORD_TEMPLATE.md`
- `workflow_v3/templates/RESULT_PACKET_TEMPLATE.md`
- `workflow_v3/templates/EVIDENCE_RECORD_TEMPLATE.md`
- `workflow_v3/templates/ACCEPTANCE_DECISION_TEMPLATE.md`
- `workflow_v3/templates/EVENT_LOOP_CLOSURE_TEMPLATE.md`

## Operating path

1. State one bounded target.
2. Name source authority and context supplied.
3. Define in scope and out of scope.
4. Define allowed and forbidden paths/surfaces.
5. Define expected result and evidence.
6. Identify adapter or human surface.
7. Set return destination and closure signal.
8. Execute only the bounded run.
9. Return Result Packet and evidence.
10. Run Event Loop Closure and Progression Router.

## Expected output

Work Contract, Run result or blocked result, Result Packet, evidence, validation, acceptance question, and exact Next Move.

## Closure signal

`work_contract_complete`, `material_run_closed`, or `blocked_lifecycle_transition`.

## Return destination

Return to the current parent/Direction chat for verification, acceptance review, and Event Loop Closure.

## Acceptance/update requirement

Run, Result Packet, Evidence, and Codex commit are candidate until explicit Acceptance Decision/update path.

## Failure/stop condition

Stop if the contract expands scope, lacks evidence requirements, touches forbidden surfaces, or lets an adapter accept its own result.

END_OF_FILE: workflow_v3/runbooks/WORK_CONTRACT_RUNBOOK.md
