# Direction Console Template

status: template

## Boundary

This template is for a future read-only console/status view. It does not create accepted state, execute work, update Project Instructions UI, refresh Project Files/Sources, or mutate runtime files.

Future concrete target path, if adopted by an explicit package:

```text
directions_v3/<direction-id>/runtime/console/DIRECTION_CONSOLE.md
```

## Console fields

`direction_id`:

`runtime_root`:

`current_status_ref`:

`current_next_move_ref`:

`active_front_ref`:

`current_work_graph_ref`:

`last_event_loop_closure_ref`:

`open_blockers`:

`exact_next_move`:

`source_read_limitations`:

`last_refreshed_from_repo_ref`:

## Use rule

The console may summarize exact repository state from bound runtime sources. It cannot replace exact reads of `CURRENT_STATUS.md` and `CURRENT_NEXT_MOVE.md` when material status or continuation depends on current source.

## Boundary

Console/status view only; does not create accepted state.

END_OF_FILE: workflow_v3/templates/DIRECTION_CONSOLE_TEMPLATE.md
