# Direction Map Formation Eval

status: active_eval

## Purpose

Validate Direction Map formation quality.

## PASS checks

- Uses `workflow_v3/formation/DIRECTION_MAP_FORMATION_RUNBOOK.md`.
- Forms tracks, map areas, strategic dependencies, strategic uncertainties, risk zones, candidate fronts, and source/status labels.
- Labels claims as accepted, candidate, unresolved, or hypothetical.
- Generates alternative map structures unless blocked.
- Does not become roadmap, backlog, Work Graph, or unreviewed task list.
- Includes evidence, risks, cuts, acceptance question, Result Packet, and Next Move Packet.

## WARN checks

- Some map claims are unresolved but clearly labeled.
- Candidate fronts are provisional pending acceptance.

## FAIL checks

- Map is a task list or roadmap.
- Labels and source discipline are missing.
- Work Graph nodes are mixed into Direction Map.
- Map is accepted without explicit acceptance/update path.

END_OF_FILE: workflow_v3/evals/DIRECTION_MAP_FORMATION_EVAL.md
