# Memory Artifact Promotion Eval

status: active_eval

## Purpose

Validate Memory Artifact promotion quality.

## PASS checks

- Uses `workflow_v3/formation/MEMORY_ARTIFACT_PROMOTION_RUNBOOK.md`.
- Promotes only high-value reusable memory.
- Includes source refs, scope of reuse, when to load, when not to use, refresh/expiry condition, and acceptance decision ref.
- Keeps Memory Artifact from replacing canonical state.
- Rejects interesting notes that lack reuse value or source traceability.

## WARN checks

- Reuse scope is narrow but explicit.
- Refresh condition depends on future accepted state changes.

## FAIL checks

- Raw notes are promoted as memory.
- Source refs or acceptance decision ref are missing.
- Artifact overrides exact repository state.
- Loading guidance is broad or ambiguous.

END_OF_FILE: workflow_v3/evals/MEMORY_ARTIFACT_PROMOTION_EVAL.md
