# 07 Reviews / Knowledge / Canon

```
artifact_control:
  artifact_name: "07 Reviews / Knowledge / Canon"
  schema: reviews_knowledge_canon.v1
  owner_layer: persistence
  status: canonical
  storage_target: "Indie Game Development Direction / 07 Reviews / Knowledge / Canon"
  default_load: pointer_only
  freshness: fresh
  next_action: "Load specific docs only when the stage request requires them."

```

## Purpose

This area holds reviewed material, canon candidates, active-domain documentation, and durable references for the Direction. It is not bulk-loaded by default.

## Active-domain documentation

`Game Documentation` remains active-domain documentation and must stay accessible to ChatGPT by topic request. It is not archive material.

Use the Context Loading Index to request specific game documentation areas rather than loading the whole tree by default.

## Review and canon rules

- Goal close uses `R1_GOAL_REVIEW_DISTILL` when goal review/distillation is needed.

- Phase close uses `P9_PHASE_CLOSE` when phase closure is needed.

- Raw sessions, wave outputs, and execution artifacts do not become canon automatically.

- Canon candidates require explicit review/distillation before becoming accepted canon.
