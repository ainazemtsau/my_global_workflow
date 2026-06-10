# Source Lock Template

status: template

## SOURCE_LOCK

`repository`:

`ref_or_commit`:

`resolved_commit_sha`:

`path`:

`read_method`:

`full_read_status`:

`eof_marker_status`:

`full_blob_sha_if_available`:

`display_sha_if_any`:

`limitations`:

## Boundary

Search result is navigation only. Snippet is not source authority. Partial read is insufficient when omitted lines may affect the action. File locks should store exact path plus full blob SHA where available; abbreviated SHAs are display summaries only.

## Quality Checks

Source Lock is valid only when exact repository/path/ref and resolved commit SHA are present for material decisions, EOF status is recorded when applicable, cache/context sources are downgraded, and limitations are explicit.

Incomplete, stale, conflicting, or truncated source locks require source-integrity repair before material work continues.

END_OF_FILE: workflow_v3/templates/SOURCE_LOCK_TEMPLATE.md
