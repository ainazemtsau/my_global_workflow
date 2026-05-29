---
artifact_control:
  namespace: workflow_v3
  artifact_type: core_spec
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Direction Control

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Purpose

Direction Control is the root control surface for one long-running direction. It is small enough to paste into a chat and stable enough to restart from.

## Required Fields

- Root Result: the intended end state.
- Success Conditions: observable conditions that make the root result true.
- Global Spine: coarse sequence or dependency outline.
- Tracks: derived from success conditions and project reality.
- Active Front summary: current primary focus plus support, watch, parked, and blocked summaries.
- Watch / Parked / Blocked states: items tracked without pretending they are active work.
- Review Queue link: review jobs waiting for parent action.
- Shared Memory Index link: promoted reusable memory.
- Latest continuation packet: current restart surface.

Tracks are derived from success conditions and are not hardcoded global categories.

## YAML Shape

```yaml
direction_control:
  direction_id:
  root_result:
  success_conditions:
  global_spine:
  tracks:
  active_front:
  watch:
  parked:
  blocked:
  event_journal_ref:
  review_queue_ref:
  shared_memory_index_ref:
  latest_continuation_packet_ref:
```

## Control Rules

- Direction Control records the current steering state, not every local detail.
- Root Result changes require an explicit decision record.
- Success Conditions must stay testable or reviewable.
- Global Spine is a guide, not a full execution graph.
- Active Front changes emit an `active_front_changed` event.
- The latest continuation packet must point to the selected next work surface.
- Legacy/current workflow data preserved in place unless later imported by explicit review.

END_OF_FILE: workflow-v3/core/01_DIRECTION_CONTROL.md
