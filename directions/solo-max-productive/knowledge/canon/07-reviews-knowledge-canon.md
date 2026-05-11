# 07 Reviews / Knowledge / Canon

```
artifact_control:
  artifact_name: "07 Reviews / Knowledge / Canon"
  schema: reviews_knowledge_canon.v1
  owner_layer: persistence
  status: canonical
  storage_target: "Solo Max Productive / 07 Reviews / Knowledge / Canon"
  default_load: pointer_only
  freshness: fresh
  next_action: "Load specific review/canon material only when needed."

```

## Purpose

This area is for direction-local reviews, knowledge, canon candidates, and accepted canon references. It is not default working context.

## Review and canon rules

- Goal review/distillation routes through `R1_GOAL_REVIEW_DISTILL` when needed.

- Phase closure routes through `P9_PHASE_CLOSE` when needed.

- Session outputs, Codex returns, Task Master state, and Project Files do not become canon automatically.

- Reusable knowledge must be reviewed/distilled before becoming accepted canon.
