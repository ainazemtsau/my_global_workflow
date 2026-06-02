# Source Integrity Protocol

status: active_control_plane

## Authority rules

- Search result is navigation only.
- Snippet is not source authority.
- Project Files/Sources are cache only.
- Chat memory is not source authority.
- Exact repo path/ref/sha wins.
- Partial read is not enough when omitted lines may affect the action.
- EOF marker is required where the file has an `END_OF_FILE` marker.
- Missing EOF, truncation risk, conflicting ref, stale source, or incomplete read => SOURCE_INTEGRITY_EXCEPTION.

## SOURCE_LOCK fields

```text
repository:
ref_or_commit:
path:
read_method:
full_read_status:
eof_marker_status:
sha_if_available:
limitations:
```

## Full read rule

For procedure, template, runtime state, and affected source files, the read must cover the exact file path and ref needed for the action. If the file contains an EOF marker, the marker must be visible and match the path.

END_OF_FILE: workflow_v3/control_plane/SOURCE_INTEGRITY_PROTOCOL.md
