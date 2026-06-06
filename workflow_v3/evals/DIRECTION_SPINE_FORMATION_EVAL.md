# Direction Spine Formation Eval

status: active_eval

## Purpose

Validate Direction Spine formation quality.

## PASS checks

- Uses the registered canonical `workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md` source; if the procedure is still a stub, it stops with `PROCEDURE_BODY_NOT_AUTHORED`.
- Does not simply ask for root outcome or fill the template.
- Generates alternatives unless trivial or blocked.
- Defines criteria before selecting candidate.
- Forms root outcome candidate, success conditions, constraints, non-goals, proof indicators, tracks or success dimensions, failure modes, and open uncertainties.
- Attacks risks, contradictions, and user-impulse overfit.
- Cuts roadmap, backlog, Work Graph, and product execution content.
- Returns candidate Spine, evidence, source limits, acceptance question, STAGE_RESULT/FINISH_PACKET evidence as applicable, and NEXT_CHAT_CARD or no_next_chat_needed when closure is reached.

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
