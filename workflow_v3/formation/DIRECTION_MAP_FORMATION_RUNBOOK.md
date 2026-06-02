# Direction Map Formation Runbook

status: active_formation_runbook

## Trigger

Use when a Direction needs an initial or updated Direction Map candidate.

## Inputs

- direction_id;
- accepted or candidate Direction Spine;
- accepted records, evidence, current human input, and candidate context;
- known dependencies, uncertainties, risks, and possible fronts;
- return destination.

## Source reads

Read exact source authority for the Direction Spine and any existing Direction Map. In setup-only Definition, read `CURRENT_STATUS.md`, `CURRENT_NEXT_MOVE.md`, and the candidate Spine produced by Spine formation.

## Formation steps

1. Confirm the target is Direction Map only.
2. Classify map inputs as accepted, candidate, unresolved, hypothetical, legacy_evidence, or unknown.
3. Frame what the Map must control: structural areas, dependencies, uncertainties, and candidate fronts.
4. Generate 2-3 map structures or area groupings unless blocked.
5. Define criteria: spine alignment, dependency clarity, uncertainty visibility, non-backlog shape, front usefulness, and source labeling.
6. Identify evidence and hypotheses for each map claim.
7. Attack flattening into roadmap/backlog/Work Graph, missing labels, false certainty, and stale context.
8. Cut task lists, execution sequencing, and global backlog items.
9. Draft candidate Map fields.
10. Record rejected/deferred structures.
11. State read limitations.
12. Ask the acceptance question.
13. Close the event loop.
14. Provide exact next move.

## Must form

- tracks;
- map areas;
- strategic dependencies;
- strategic uncertainties;
- risk zones;
- candidate fronts;
- accepted/candidate/unresolved/hypothetical labels.

## Must not do

Do not become roadmap, backlog, Work Graph, Action Inbox, or product execution plan.

## Outputs

Return a candidate Direction Map compatible with `workflow_v3/templates/DIRECTION_MAP_TEMPLATE.md`, with alternatives, evidence, risks, cuts, acceptance question, Event Loop Closure, and exact next move.

## Acceptance boundary

The Map remains candidate until explicit acceptance/update path.

## Stop conditions

Stop if accepted Spine is missing and the package does not admit candidate Definition sequencing, if map claims cannot be labeled, or if the result is only a task list.

## Run-surface boundary

Formation chat is non-mutating.

After acceptance-like human input, stop with Transition Packet to `acceptance_review` / `storage_update_adapter`. Do not create acceptance records, mutate repository state, update CURRENT_STATUS, update CURRENT_NEXT_MOVE, persist Event Loop Closure files, launch Codex, or continue across role boundary.

END_OF_FILE: workflow_v3/formation/DIRECTION_MAP_FORMATION_RUNBOOK.md
