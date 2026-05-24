---
artifact_control:
  namespace: proof_workflow
  artifact_type: transport_card
  card_type: operator_launch_card
  status: gate_1_initial
  owner: proof_carrying_workflow_os
---

# Operator Launch Card

## Purpose

Operator Launch Card serializes one Operator invocation over one Obligation.

It is not a stage launch, not a process template, and not authority to work outside the named Obligation.

## Required Shape

```yaml
operator_launch_card:
  card_id: string
  target_obligation_id: string
  operator_id: string
  ledger_snapshot_ref: string
  commit_scope_ref: string
  input_context:
    accepted_receipt_ids: [string]
    projection_refs: [string]
    additional_context_refs: [string]
  constraints: [string]
  forbidden_actions: [string]
  required_return_receipt_type: string
  proof_policy: string
  stop_conditions: [string]
  human_gate:
    required: boolean
    gate_ref: string | null
    unresolved_decision: string | null
  tool_gate:
    required: boolean
    allowed_tools: [string]
    forbidden_tools: [string]
    execution_allowed: boolean
  parent_or_controller_return_target: string
```

## Admission Rules

Launch is valid only when:

- target Obligation is open
- Operator is eligible
- Commit Scope is defined
- proof policy is explicit
- required context is present
- human and tool gates are satisfied or represented as blocking
- forbidden actions are clear

## Return Rule

The launched Operator must return a Receipt Card, Context Request Card, Human Decision Card, or a clear blocked result.

The launch card itself does not create proof and does not mutate the Ledger.

END_OF_FILE: proof_workflow/transport/OPERATOR_LAUNCH_CARD.md
