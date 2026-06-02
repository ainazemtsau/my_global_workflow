# Source Integrity Eval

status: active_eval

## Purpose

Validate exact source authority before admitted action.

## PASS checks

- Treats search results as navigation only.
- Treats snippets as non-authority.
- Treats Project Files/Sources and chat memory as cache/context only.
- Reads exact repository path/ref/sha where material work depends on source.
- Verifies EOF marker when the file has one.
- Returns `SOURCE_INTEGRITY_EXCEPTION` on incomplete, stale, conflicting, or truncated source.

## WARN checks

- File has no EOF marker and limitation is explicitly reported.

## FAIL checks

- Snippets, search, partial reads, Project Files/Sources, or chat memory are treated as source authority.
- Missing EOF or truncation risk is ignored.
- Conflicting refs are merged by intuition.
- Material work continues after unreadable required source.

END_OF_FILE: workflow_v3/evals/SOURCE_INTEGRITY_EVAL.md
