# Exception Protocol

status: active_control_plane

## Exception packet

```text
status: blocked
exception_type:
blocked_action:
missing_or_conflicting_item:
why_continuation_is_unsafe:
allowed_next_move:
return_destination:
```

## Exception types

- `SOURCE_INTEGRITY_EXCEPTION`
- `UNREGISTERED_ACTION_EXCEPTION`
- `MISSING_PROCEDURE_EXCEPTION`
- `ROLE_BOUNDARY_EXCEPTION`
- `WRITE_ADMISSION_EXCEPTION`
- `ACCEPTANCE_AMBIGUITY_EXCEPTION`
- `LEGACY_BOUNDARY_EXCEPTION`
- `CONFLICTING_STATE_EXCEPTION`
- `VALIDATION_MISSING_EXCEPTION`
- `FORBIDDEN_PATH_EXCEPTION`

## Continuation rule

When an exception applies, the chat stops the blocked action and returns the exception packet. The allowed next move may request exact source, user decision, narrowed package, or admitted recovery review.

END_OF_FILE: workflow_v3/control_plane/EXCEPTION_PROTOCOL.md
