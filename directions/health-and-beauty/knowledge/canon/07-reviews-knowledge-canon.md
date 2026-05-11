# 07 Reviews / Knowledge / Canon

```
artifact_control:
  artifact_name: "07 Reviews / Knowledge / Canon"
  schema: reviews_knowledge_canon.v1
  owner_layer: persistence
  status: canonical
  storage_target: "Health and beauty / 07 Reviews / Knowledge / Canon"
  default_load: pointer_only
  freshness: fresh
  next_action: "Load specific health/nutrition docs only when needed."

```

## Purpose

This area is for health/beauty/nutrition domain documentation, reviews, knowledge, canon candidates, and accepted canon references. It is not bulk-loaded by default.

## Active-domain documentation

`Health Domain Documentation` and `Legacy Direction Docs - review before canonizing` are request-only unless a stage launch names them.

## Review and canon rules

- Goal review/distillation routes through `R1_GOAL_REVIEW_DISTILL` when needed.

- Phase closure routes through `P9_PHASE_CLOSE` when needed.

- Session outputs, Codex returns, Task Master state, and Project Files do not become canon automatically.

- Legacy docs must be reviewed before becoming accepted canon.
