# Status Review Procedure

status: active_procedure

## Purpose

Use `status_review` to answer current status questions without executing material work or mutating state.

## Required reads

Where Direction-specific state is relevant:

- resolve binding before status;
- read exact `CURRENT_STATUS.md` through resolved binding;
- read exact `CURRENT_NEXT_MOVE.md` through resolved binding;
- verify source integrity and EOF status where markers exist.

## Allowed operations

- summarize accepted current status from exact sources;
- identify pending next move;
- report source limitations and binding conflicts;
- recommend admission needed for any next action.

## Forbidden operations

- execute material work;
- mutate repository/runtime state;
- accept evidence or candidate output;
- launch next work.

## Required output

```text
status_review:
binding_source:
current_status_ref:
current_next_move_ref:
source_read_limitations:
admission_needed_for_next_action:
```

END_OF_FILE: workflow_v3/procedures/STATUS_REVIEW_PROCEDURE.md
