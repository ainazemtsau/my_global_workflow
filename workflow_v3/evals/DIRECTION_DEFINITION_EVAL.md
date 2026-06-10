# Direction Definition Eval

status: active_eval

## Purpose

This eval checks the semantic Direction Definition process after setup-only root exists.

## PASS checks

- Direction Definition runs only after setup-only root exists.
- `CURRENT_STATUS.md` and `CURRENT_NEXT_MOVE.md` are read.
- `CURRENT_STATUS` confirms `setup_only_root_created`.
- `CURRENT_NEXT_MOVE` confirms `launch_direction_definition`.
- Candidate context is used explicitly and remains candidate-only.
- Direction Spine, Direction Map, and Active Front canonical procedure files are used.
- Candidate Spine, Map, and Front are created as candidates only.
- No Work Graph is created before Active Front acceptance.
- No product execution starts.
- Acceptance/update path is required before state mutation.

## WARN checks

- A parent Definition chat sequences multiple entity formations but keeps boundaries separate.
- Dependency research/check chats are used and return to parent without deciding.
- Some evidence gaps remain and are labeled unresolved.

## FAIL checks

- Definition starts before setup-only root.
- Current status or next move is not read.
- Candidate context is treated as accepted state.
- Templates are filled directly without canonical procedure execution.
- Spine/Map/Front are accepted silently.
- Work Graph or product work starts before Active Front acceptance.
- Acceptance/update path is missing.

## Required result fields

```text
verdict: PASS | WARN | FAIL
setup_only_root_check:
current_status_read_check:
current_next_move_read_check:
candidate_context_check:
formation_procedure_check:
candidate_only_check:
work_graph_boundary_check:
product_execution_check:
acceptance_update_path_check:
unresolved_questions:
residual_risks:
```

END_OF_FILE: workflow_v3/evals/DIRECTION_DEFINITION_EVAL.md
