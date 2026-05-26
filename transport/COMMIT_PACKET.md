---
artifact_control:
  namespace: workflow
  artifact_type: transport_card
  card_type: commit_packet
  status: gate_1_initial
  owner: workflow_os
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
  blocker_summary:
    blocking_reason: string | null
    blocking_protocol:
      - verify | invariant | proof_policy | human_gate | commit_scope | storage | projection | tool_gate
    details: string | null
  residual_obligations:
    - obligation_statement: string
      reason: string
      suggested_operator: string | null
  projection_updates_required: [string]
  storage_updates_required: [string]
```

## Rules

Only `commit_verdict: committed` creates accepted state.

Projection and storage updates are follow-up effects of committed Ledger delta. They do not replace Commit.

If verification, invariant, verification policy, or human gate result blocks commit, the packet must state the blocker in `blocker_summary` and identify `residual_obligations` when further work is needed.

Blocked commit verdicts must include `blocker_summary`.

Blocked commit verdicts should create or reference `residual_obligations` when further work is needed.

Rejected commits may include `residual_obligations` only when recovery is allowed.

Committed verdicts should normally have `blocker_summary: null` and `residual_obligations: []`.

END_OF_FILE: transport/COMMIT_PACKET.md
