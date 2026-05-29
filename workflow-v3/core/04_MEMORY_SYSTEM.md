---
artifact_control:
  namespace: workflow_v3
  artifact_type: core_spec
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Memory System

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Memory Classes

- Control Memory: Direction Control, Active Front, queues, and continuation references.
- Node Memory: local inputs, work notes, temporary findings, and node evidence.
- Shared Direction Memory: promoted reusable facts, constraints, summaries, and references.
- Decision Memory: accepted decisions, rationale, date, owner, and reopen condition.
- Event Journal: append-only event records.
- Artifact Store: produced files, evidence, reports, and review outputs.
- Shared Memory Index: navigable index of promoted shared memory and decision records.

## Node Boundary Rule

Nodes do not read arbitrary internals of other nodes. They consume parent contracts, allowed shared memory, decision records, explicit result reports, and attached evidence.

## Promotion Policy

Node output becomes reusable only after promotion to shared memory or decision memory.

Promotion requires:

- Parent acceptance.
- Clear source reference.
- Reuse purpose.
- Scope of validity.
- Reopen condition when appropriate.

## Memory Record Shape

```yaml
memory_record:
  id:
  class:
  source_node:
  summary:
  evidence_refs:
  scope:
  valid_until_or_reopen_condition:
  promoted_by:
  promoted_at:
```

## Rules

- Control Memory must stay compact enough for continuation.
- Node Memory can be detailed but remains local.
- Decision Memory overrides older non-decision notes in the same scope.
- Event Journal records what happened; it does not by itself accept changes.
- Artifact Store preserves evidence without making it shared truth.
- Shared Memory Index points to promoted reusable memory only.
- Legacy/current workflow data preserved in place and reused later only through explicit import/review.

END_OF_FILE: workflow-v3/core/04_MEMORY_SYSTEM.md
