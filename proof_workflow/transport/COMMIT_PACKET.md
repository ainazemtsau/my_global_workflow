---
artifact_control:
  namespace: proof_workflow
  artifact_type: transport_card
  card_type: commit_packet
  status: gate_1_initial
  owner: proof_carrying_workflow_os
---

# Commit Packet

## Purpose

Commit Packet serializes a commit proposal or commit result.

It records whether verified Receipts changed the Ledger under the target Commit Scope.

## Required Shape

```yaml
commit_packet:
  commit_id: string
  receipt_ids: [string]
  target_commit_scope: string
  proposed_ledger_delta: object
  verification_result: pass | fail | needs_input
  invariant_result: pass | fail
  proof_policy_result: pass | fail | needs_input
  human_gate_result: satisfied | not_required | blocked
  commit_verdict: committed | rejected | blocked_needs_context | blocked_needs_human_gate | blocked_invariant_failure | blocked_scope_violation
  projection_updates_required: [string]
  storage_updates_required: [string]
```

## Rules

Only `commit_verdict: committed` creates accepted state.

Projection and storage updates are follow-up effects of committed Ledger delta. They do not replace Commit.

If verification, invariant, proof policy, or human gate result blocks commit, the packet must state the blocker and residual Obligation.

END_OF_FILE: proof_workflow/transport/COMMIT_PACKET.md
