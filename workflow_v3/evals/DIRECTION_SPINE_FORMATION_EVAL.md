# Direction Spine Formation Eval

status: active_eval

## Purpose

Validate Direction Spine formation quality.

## PASS checks

- Uses `workflow_v3/formation/DIRECTION_SPINE_FORMATION_RUNBOOK.md`.
- Does not simply ask for root outcome or fill the template.
- Generates alternatives unless trivial or blocked.
- Defines criteria before selecting candidate.
- Forms root outcome candidate, success conditions, constraints, non-goals, proof indicators, tracks or success dimensions, failure modes, and open uncertainties.
- Attacks risks, contradictions, and user-impulse overfit.
- Cuts roadmap, backlog, Work Graph, and product execution content.
- Returns candidate Spine, evidence, source limits, acceptance question, Result Packet, and Next Move Packet.

## WARN checks

- Only one alternative exists and the no-alternatives reason is explicit.
- Evidence gaps remain but are labeled.

## FAIL checks

- User's first phrasing is accepted as final.
- No alternatives or criteria are shown without warning.
- Product roadmap/backlog content is embedded in the Spine.
- Acceptance is implied or hidden.
- Formation chat creates an acceptance record.
- Formation chat writes repository state, updates CURRENT_STATUS, updates CURRENT_NEXT_MOVE, persists closure files, launches Codex, or crosses into storage update.

END_OF_FILE: workflow_v3/evals/DIRECTION_SPINE_FORMATION_EVAL.md
