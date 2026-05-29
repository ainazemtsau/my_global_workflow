---
artifact_control:
  namespace: workflow_v3
  artifact_type: core_spec
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Event Review Patch System

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Event Types

```text
node_created, node_started, node_delegated, node_completed, node_blocked, node_failed, document_promoted, decision_made, assumption_invalidated, review_requested, review_completed, patch_proposed, patch_accepted, patch_rejected, route_challenged, route_changed, active_front_changed
```

## Event Record Shape

```yaml
event:
  id:
  type:
  source:
  target:
  summary:
  evidence_refs:
  parent_node:
  created_at:
```

## Subscriptions

Subscriptions tell the parent what events should trigger review.

```yaml
subscription:
  id:
  watcher:
  event_types:
  target_scope:
  review_job_template_ref:
  priority:
```

## Review Queue

The Review Queue holds bounded questions for parent or reviewer action.

- Each review job has a trigger, input state references, allowed memory, forbidden actions, required output, and max scope.
- A review job may inspect evidence and propose changes.
- A review job may produce `no_change`, `patch_proposal`, `blocker_report`, `discovery_request`, or `parent_decision_request`.

## Patch Proposal

Patch proposals describe possible control-state changes. They do not apply themselves.

```yaml
patch_proposal:
  id:
  target_surface:
  change_kind:
  reason:
  evidence:
  affected_nodes:
  risk:
  confidence:
  rollback_or_reopen_condition:
```

## Parent Integration Review

A review job may propose a patch, but it may not mutate control state directly.

The parent integration review decides:

- Accept patch.
- Reject patch.
- Request more discovery.
- Convert patch to a parent decision request.
- Park or block the affected node.

## No Background Magic

- No event mutates control state by implication.
- No review silently promotes memory.
- No child chat changes Direction Control directly.
- No current or legacy artifact becomes v3 authority without explicit import/review.

END_OF_FILE: workflow-v3/core/05_EVENT_REVIEW_PATCH_SYSTEM.md
