# Work Contract Formation Runbook

status: active_formation_runbook

## Trigger

Use when one Work Graph node or bounded node slice needs an executable Work Contract.

## Inputs

- Work Graph node or bounded slice;
- allowed and forbidden paths/surfaces;
- source reads;
- expected result;
- validation/evidence requirement;
- adapter or human surface;
- return destination.

## Source reads

Read the source Work Graph, node context, current status, and any files or records named as required source. Do not broaden reads beyond the contract target.

## Formation steps

1. Confirm the target is one Work Contract.
2. Classify source authority, candidate context, and constraints.
3. Frame the run target and the decision/evidence it must produce.
4. Generate alternatives for target scope when the first phrasing may be too broad.
5. Define criteria: boundedness, evidence yield, path safety, return clarity, validation feasibility, and split risk.
6. Identify evidence, assumptions, stop conditions, and failure conditions.
7. Attack compound scope, hidden route authority, forbidden surfaces, and acceptance leakage.
8. Cut unrelated tasks and future work.
9. Draft the Work Contract fields.
10. Record rejected/deferred scope.
11. State read limitations.
12. Ask whether to launch, repair, split, block, or park.
13. Close the event loop.
14. Provide exact Launch Packet or next move.

## Must include

- target;
- allowed/forbidden paths or surfaces;
- source reads;
- expected result;
- evidence/validation;
- return destination;
- stop conditions;
- `split_required` behavior if compound.

## Outputs

Return a candidate Work Contract compatible with `workflow_v3/templates/WORK_CONTRACT_TEMPLATE.md`, with risks, cuts, acceptance/launch question, Event Loop Closure, and exact Launch Packet.

## Acceptance boundary

The contract may launch work only when explicitly accepted or launched by the human/update path. Adapter results remain candidate.

## Stop conditions

Return `split_required` if the target combines independent jobs or cannot be validated as one bounded run.

END_OF_FILE: workflow_v3/formation/WORK_CONTRACT_FORMATION_RUNBOOK.md
