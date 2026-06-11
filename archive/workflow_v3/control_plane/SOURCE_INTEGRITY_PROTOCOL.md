# Source Integrity Protocol

status: active_control_plane

## Authority rules

- Search result is navigation only.
- Snippet is not source authority.
- Project Files/Sources are cache only.
- Chat memory is not source authority.
- Exact repo path/ref/sha wins.
- Material admission should include the resolved commit SHA when the requested source ref is a branch such as `main`.
- File source locks should include exact path and full blob SHA where available.
- Abbreviated SHAs may be shown only as display summaries when the full SHA is stored inline or linked.
- Partial read is not enough when omitted lines may affect the action.
- EOF marker is required where the file has an `END_OF_FILE` marker.
- Missing EOF, truncation risk, conflicting ref, stale source, or incomplete read => SOURCE_INTEGRITY_EXCEPTION.

## SOURCE_LOCK fields

```text
repository:
ref_or_commit:
resolved_commit_sha:
path:
read_method:
full_read_status:
eof_marker_status:
full_blob_sha_if_available:
display_sha_if_any:
limitations:
```

## Full read rule

For procedure, template, runtime state, and affected source files, the read must cover the exact file path and ref needed for the action. If the file contains an EOF marker, the marker must be visible and match the path.

## Quality Checks

- PASS when material work names exact repository/path/ref, records resolved commit SHA for branch refs, records full blob SHA where available, verifies EOF when present, and treats Project Files/Sources, chat memory, uploads, snippets, generated packs, and pasted excerpts as cache/context until verified.
- WARN when a source is intentionally partial or unavailable but the limitation is named and no material claim relies on omitted content.
- FAIL when cache, memory, snippet, search output, stale ref, or partial read is treated as authority; when a required source is unreadable; or when conflicting source evidence is ignored.
- Recovery is `SOURCE_INTEGRITY_EXCEPTION`: stop the material claim, request or read the exact source, and rerun the same bounded procedure with limitations visible.

END_OF_FILE: workflow_v3/control_plane/SOURCE_INTEGRITY_PROTOCOL.md
