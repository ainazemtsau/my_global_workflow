# Memory Artifact Promotion Runbook

status: active_formation_runbook

## Trigger

Use when a Memory Candidate or repeated context may be promoted to a reusable Memory Artifact.

## Inputs

- Memory Candidate or source result;
- source refs and acceptance decision ref;
- proposed scope of reuse;
- loading and exclusion rules;
- refresh or expiry condition;
- return destination.

## Source reads

Read source refs, current canonical state affected by the memory, the Memory Candidate, and the Acceptance Decision authorizing promotion.

## Formation steps

1. Confirm the target is Memory Artifact promotion only.
2. Classify source refs, accepted state, candidate memory, and reuse need.
3. Frame what future work the memory should help and what it must not replace.
4. Generate promote / do not promote / defer alternatives.
5. Define criteria: reuse value, source traceability, stability, conflict risk, loading clarity, and expiry clarity.
6. Identify evidence and limitations.
7. Attack interesting-but-not-reusable notes, stale context, overbroad loading, and canonical-state replacement.
8. Cut low-value or broad memory.
9. Draft candidate Memory Artifact fields.
10. Record rejected/deferred promotion options.
11. State read limitations.
12. Ask acceptance question.
13. Close the event loop.
14. Provide exact next move for promotion, repair, or park.

## Must include

- source refs;
- scope of reuse;
- when to load;
- when not to use;
- refresh/expiry condition;
- acceptance decision ref.

## Outputs

Return a candidate Memory Artifact compatible with `workflow_v3/templates/MEMORY_ARTIFACT_TEMPLATE.md`.

## Acceptance boundary

Promotion requires explicit review/update. Memory does not replace canonical state.

## Stop conditions

Stop if the memory is only an interesting note, source refs are missing, accepted promotion authority is absent, or the artifact would override exact repository state.

END_OF_FILE: workflow_v3/formation/MEMORY_ARTIFACT_PROMOTION_RUNBOOK.md
