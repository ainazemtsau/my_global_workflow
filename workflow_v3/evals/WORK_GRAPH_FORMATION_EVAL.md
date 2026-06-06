# Work Graph Formation Eval

status: active_eval

## Purpose

Validate Work Graph formation quality.

## PASS checks

- Uses the registered canonical `workflow_v3/procedures/WORK_GRAPH_FORMATION_PROCEDURE.md` source; if the procedure is still a stub, it stops with `PROCEDURE_BODY_NOT_AUTHORED`.
- Derives from Active Front exit criteria.
- Preserves parent graph/front/map claim trace.
- Includes minimum nodes needed to close the front, dependency structure, proof path, and explicit non-nodes/cut items.
- Keeps graph local to one Active Front.
- Avoids roadmap, global backlog, Direction Map, and unreviewed task-list drift.
- Returns candidate graph, evidence, risks, cuts, acceptance question, STAGE_RESULT/FINISH_PACKET evidence as applicable, and NEXT_CHAT_CARD or no_next_chat_needed when closure is reached.

## WARN checks

- Candidate Active Front is used and acceptance limitation is stated.
- Some node dependencies require check jobs.

## FAIL checks

- Work Graph spans the whole Direction.
- Node list is a disguised backlog.
- Graph includes unrelated product work.
- Node relation to parent is missing.
- No proof path or closure condition exists.

END_OF_FILE: workflow_v3/evals/WORK_GRAPH_FORMATION_EVAL.md
