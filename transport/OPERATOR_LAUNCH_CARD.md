---
artifact_control:
  namespace: workflow
  artifact_type: transport_card
  card_type: operator_launch_card
  status: gate_1_initial
  owner: workflow_os
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
  parent_obligation_id: string | null
  child_obligation_id: string | null
  ledger_snapshot_ref: string
  commit_scope_ref: string
  input_context:
    accepted_receipt_ids: [string]
    projection_refs: [string]
    additional_context_refs: [string]
  context_authority:
    accepted_state_refs: [string]
    committed_receipt_refs: [string]
    candidate_context_refs: [string]
    projection_context_refs: [string]
    legacy_evidence_refs: [string]
    instruction_context_refs: [string]
  context_use_rules:
    candidate_context_may_define_options: true
    candidate_context_may_define_accepted_state: false
    legacy_evidence_requires_import_receipt: true
  constraints: [string]
  forbidden_actions: [string]
  required_return_receipt_type: string
  proof_policy: string
  stop_conditions: [string]
  expected_closure:
    - human_decision_needed
    - codex_commit_needed
    - next_chat_needed
    - complete_no_commit
    - blocked_context_needed
    - stop
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
  return_to_parent_instruction: string | null
  recovery_reference: string | null
```

## Admission Rules

Launch is valid only when:

- target Obligation is open
- Operator is eligible
- Commit Scope is defined
- verification policy is explicit
- required context is present
- context authority is classified
- human and tool gates are satisfied or represented as blocking
- forbidden actions are clear

## Return Rule

The launched Operator must return a Receipt Card, Context Request Card, Human Decision Card, or a clear blocked result.

Launch Cards should tell the operator whether a commit handoff may be required.

The launch card itself does not create proof and does not mutate the Ledger.

END_OF_FILE: transport/OPERATOR_LAUNCH_CARD.md
