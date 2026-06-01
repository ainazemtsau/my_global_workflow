# Direction Spine Formation Eval

status: active_eval

## Purpose

Validate Direction Spine formation quality.

## PASS checks

- Uses `workflow_v3/formation/DIRECTION_SPINE_FORMATION_RUNBOOK.md`.
- Does not simply ask for root outcome or fill the template.
- Generates alternatives unless trivial or blocked.
- Defines criteria before selecting candidate.
- Forms root outcome candidate, success conditions, constraints, non-goals, proof signals, tracks or success dimensions, failure modes, and open uncertainties.
- Attacks risks, contradictions, and user-impulse overfit.
- Cuts roadmap, backlog, Work Graph, and product execution content.
- Returns candidate Spine, evidence, source limits, acceptance question, Event Loop Closure, and exact next move.

## WARN checks

- Only one alternative exists and the no-alternatives reason is explicit.
- Evidence gaps remain but are labeled.

## FAIL checks

- User's first phrasing is accepted as final.
- No alternatives or criteria are shown without warning.
- Product roadmap/backlog content is embedded in the Spine.
- Acceptance is implied or hidden.

END_OF_FILE: workflow_v3/evals/DIRECTION_SPINE_FORMATION_EVAL.md
