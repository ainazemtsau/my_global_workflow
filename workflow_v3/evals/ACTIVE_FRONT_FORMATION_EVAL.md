# Active Front Formation Eval

status: active_eval

## Purpose

Validate Active Front formation quality.

## PASS checks

- Uses the registered canonical `workflow_v3/procedures/ACTIVE_FRONT_FORMATION_PROCEDURE.md` source; if the procedure is still a stub, it stops with `PROCEDURE_BODY_NOT_AUTHORED`.
- Selects from Direction Map areas.
- References Active Unresolved Cut when Goal Evidence Graph context exists.
- Shows candidate fronts and rejected/deferred alternatives.
- Includes touched tracks, root criticality, bottleneck relief, uncertainty reduction, evidence value, dependency unlock, scope control, reversibility, WIP/capacity, success-dimension balance, and exit criteria.
- Ties exit criteria to graph nodes or map claims.
- Does not select by preference or convenience alone.
- Does not open Work Graph before accepted front when acceptance is required.
- Returns candidate front, evidence, risks, cuts, acceptance question, STAGE_RESULT/FINISH_PACKET evidence as applicable, and NEXT_CHAT_CARD or no_next_chat_needed when closure is reached.

## WARN checks

- Direction Map is candidate and this limitation is visible.
- Evidence is enough for candidate formation but not final acceptance.

## FAIL checks

- No source map area is named.
- Goal Evidence Graph exists but cut/node trace is missing.
- No alternatives are considered.
- Selection is preference-only.
- Front becomes global backlog or roadmap.
- Acceptance is hidden.

END_OF_FILE: workflow_v3/evals/ACTIVE_FRONT_FORMATION_EVAL.md
