---
artifact_control:
  namespace: workflow_v3
  artifact_type: core_spec
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Parallel Chat Runtime

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Parent-Controlled Parallelism

Parallel child work is allowed only when the parent can integrate every child result.

The parent defines:

- Child node purpose.
- Input context.
- Allowed and forbidden memory.
- Allowed and forbidden actions.
- Expected outputs.
- Required result report.
- Return target.

## Child Chat Packet

Each child chat starts from an explicit packet.

```yaml
child_chat_packet:
  parent_node:
  child_node:
  purpose:
  input_context:
  allowed_memory:
  forbidden_memory:
  allowed_actions:
  forbidden_actions:
  expected_outputs:
  result_report_required:
  events_to_emit:
  return_to:
```

No child work starts without a parent contract.

## Parent Recovery Block

The parent maintains a recovery block while child work is open.

```yaml
parent_recovery:
  open_children:
  expected_reports:
  integration_order:
  known_conflicts:
  blocked_children:
  latest_safe_continuation_packet_ref:
```

## Integration Order

- Integrate blockers first when they affect other children.
- Integrate shared dependencies before dependent reports.
- Integrate independent outputs in the order that reduces rework.
- Emit events for accepted reports, rejected reports, and active-front changes.

## Conflict Policy

- Conflicting child outputs return to parent integration review.
- The parent can accept one, reject one, request more discovery, or create a patch proposal.
- A child result cannot override a decision record without parent decision.
- A child result cannot promote memory by itself.

## Safe Multi-Tab Use

The user can launch multiple ChatGPT tabs safely when packets are explicit. Each tab gets only the parent-approved packet and returns a result report for integration.

END_OF_FILE: workflow-v3/core/06_PARALLEL_CHAT_RUNTIME.md
