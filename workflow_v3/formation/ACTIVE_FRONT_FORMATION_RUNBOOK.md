# Active Front Formation Runbook

status: active_formation_runbook

## Trigger

Use when a Direction needs a candidate Active Front selected from Direction Map areas.

## Inputs

- accepted or candidate Direction Map;
- source map areas and touched tracks;
- current blockers, uncertainties, dependencies, evidence, and user priorities;
- return destination.

## Source reads

Read exact Direction Map source and relevant current status. Direction Definition may form the first Active Front candidate after Spine and Map candidates, but acceptance still requires explicit decision.

## Formation steps

1. Confirm the target is Active Front only.
2. Classify source map claims and candidate context.
3. Frame why one focus is needed now and what it controls.
4. Generate candidate fronts from map areas.
5. Define criteria: bottleneck/constraint relief, uncertainty reduction, evidence speed, dependency unlock, scope control, track balance, feasibility, reversibility, and user priority.
6. Summarize evidence and failure conditions.
7. Attack convenience selection, preference-only selection, stale map, false urgency, and overbroad front.
8. Cut unrelated map areas, backlog items, and Work Graph nodes not needed for the front.
9. Draft candidate Active Front fields.
10. Record rejected/deferred fronts.
11. State read limitations.
12. Ask the acceptance question.
13. Close the event loop.
14. Provide exact next move.

## Must include

- candidate fronts;
- touched tracks;
- bottleneck / constraint check;
- uncertainty reduction;
- evidence speed;
- dependency unlock;
- scope control;
- reversibility;
- rejected alternatives;
- exit criteria.

## Outputs

Return a candidate Active Front compatible with `workflow_v3/templates/ACTIVE_FRONT_TEMPLATE.md`, with evidence, risks, cuts, acceptance question, Event Loop Closure, and exact next move.

## Acceptance boundary

The front remains candidate until explicit acceptance/update path.

## Stop conditions

Stop if no Direction Map area is available, if the front is selected by preference alone, if it includes global backlog, or if Work Graph is being opened before front acceptance.

## Run-surface boundary

Formation chat is non-mutating.

After acceptance-like human input, stop with Transition Packet to `acceptance_review` / `storage_update_adapter`. Do not create acceptance records, mutate repository state, update CURRENT_STATUS, update CURRENT_NEXT_MOVE, persist Event Loop Closure files, launch Codex, or continue across role boundary.

END_OF_FILE: workflow_v3/formation/ACTIVE_FRONT_FORMATION_RUNBOOK.md
