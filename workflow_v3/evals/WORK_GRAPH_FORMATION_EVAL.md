# Work Graph Formation Eval

status: active_eval

## Purpose

Validate Work Graph formation quality.

## PASS checks

- Uses `workflow_v3/formation/WORK_GRAPH_FORMATION_RUNBOOK.md`.
- Derives from Active Front exit criteria.
- Includes minimum nodes needed to close the front, dependency structure, proof path, and explicit non-nodes/cut items.
- Keeps graph local to one Active Front.
- Avoids roadmap, global backlog, Direction Map, and Action Inbox drift.
- Returns candidate graph, evidence, risks, cuts, acceptance question, Event Loop Closure, and exact next move.

## WARN checks

- Candidate Active Front is used and acceptance limitation is stated.
- Some node dependencies require check jobs.

## FAIL checks

- Work Graph spans the whole Direction.
- Node list is a disguised backlog.
- Graph includes unrelated product work.
- No proof path or closure condition exists.

END_OF_FILE: workflow_v3/evals/WORK_GRAPH_FORMATION_EVAL.md
