# Direction Spine Formation Runbook

status: active_formation_runbook

## Trigger

Use when a Direction needs an initial or updated Direction Spine candidate.

Do not use this as a setup-only root bootstrap step. Setup may preserve `candidate_context_for_direction_definition`, but it must not accept Spine content.

## Inputs

- direction_id and runtime/setup state if available;
- accepted source authority or setup-only pending state;
- current human input and candidate context;
- constraints, non-goals, evidence, and known uncertainties;
- return destination.

## Source reads

Read exact canonical Workflow v3 source and the bound Direction state paths when they exist. If setup-only root exists, read `CURRENT_STATUS.md` and `CURRENT_NEXT_MOVE.md` and confirm Direction Definition is the admitted next move.

Stop if required source cannot be verified.

## Formation steps

1. Confirm the target is Direction Spine only.
2. Classify source/context, including current human input as candidate until accepted.
3. Frame what the Spine must control: root outcome, success conditions, tracks, constraints, and proof direction.
4. Generate 2-3 possible root outcome / spine framings unless blocked.
5. Define criteria: outcome clarity, proofability, track coherence, constraint fit, non-goal clarity, risk exposure, and update cost.
6. Identify evidence, assumptions, proof signals, failure conditions, and open uncertainties.
7. Attack each candidate for vague success, wishful phrasing, hidden roadmap, stale context, and user-impulse overfit.
8. Cut roadmap, backlog, Work Graph, and execution items.
9. Draft candidate Spine fields.
10. Record rejected/deferred alternatives.
11. State read limitations.
12. Ask whether to accept, repair, block, or park the candidate.
13. Close the event loop.
14. Provide exact next move or Transition Packet.

## Must form

- root outcome candidate;
- success conditions;
- constraints;
- non-goals;
- proof signals;
- tracks or success dimensions;
- failure modes;
- open uncertainties.

## Outputs

Return a candidate Direction Spine compatible with `workflow_v3/templates/DIRECTION_SPINE_TEMPLATE.md`, plus evidence, risks, cuts, acceptance question, Event Loop Closure, and exact next move.

## Acceptance boundary

The candidate remains candidate until an explicit Acceptance Decision or accepted update path records it.

## Stop conditions

Stop if source is missing, the user is being asked only to fill a root outcome template, the candidate would become roadmap/backlog, or acceptance is implied.

END_OF_FILE: workflow_v3/formation/DIRECTION_SPINE_FORMATION_RUNBOOK.md
