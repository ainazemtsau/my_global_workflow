# Memory Index Eval

status: active_eval

## Purpose

Validate Memory Index entries and prevent memory from replacing source authority or accepted state.

## PASS checks

- Memory entries have source refs, tags, applies_to, load_when, do_not_load_when, and refresh/expiry.
- Memory Index points to promoted Memory Artifacts, not raw notes.
- Memory does not replace accepted state or exact source reads.

## WARN checks

- Entry has narrow load guidance and depends on later refresh after accepted state changes.
- Entry is useful only for a specific Direction context, and that scope is explicit.

## FAIL checks

- Raw notes are indexed as always-load memory.
- Source refs or exclusion rules are missing.
- Memory Index is treated as accepted Direction state.

## Required recovery/repair action

Remove or repair the candidate index entry, require Memory Artifact promotion evidence, and keep canonical state/source reads authoritative.

END_OF_FILE: workflow_v3/evals/MEMORY_INDEX_EVAL.md
