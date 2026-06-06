# Direction Map Formation Eval

status: active_eval

## Purpose

Validate Direction Map formation quality.

## PASS checks

- Uses the registered canonical `workflow_v3/procedures/DIRECTION_MAP_FORMATION_PROCEDURE.md` source; if the procedure is still a stub, it stops with `PROCEDURE_BODY_NOT_AUTHORED`.
- Forms tracks, map areas, strategic dependencies, strategic uncertainties, risk zones, candidate fronts, and source/status labels.
- Forms or references Goal Evidence Graph candidates with required claims, alternatives, obstacles, evidence gaps, and Active Unresolved Cut candidates.
- Labels claims as accepted, candidate, unresolved, or hypothetical.
- Generates alternative map structures unless blocked.
- Does not become roadmap, backlog, Work Graph, or unreviewed task list.
- Includes evidence, risks, cuts, acceptance question, STAGE_RESULT/FINISH_PACKET evidence as applicable, and NEXT_CHAT_CARD or no_next_chat_needed when closure is reached.
- Keeps graph output candidate until accepted.

## WARN checks

- Some map claims are unresolved but clearly labeled.
- Candidate fronts are provisional pending acceptance.

## FAIL checks

- Map is a task list or roadmap.
- Labels and source discipline are missing.
- Work Graph nodes are mixed into Direction Map.
- Goal Evidence Graph is treated as accepted state by existence.
- Map is accepted without explicit acceptance/update path.

END_OF_FILE: workflow_v3/evals/DIRECTION_MAP_FORMATION_EVAL.md
