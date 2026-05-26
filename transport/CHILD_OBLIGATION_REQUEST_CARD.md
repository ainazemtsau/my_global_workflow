---
artifact_control:
  namespace: workflow
  artifact_type: transport_card
  card_type: child_obligation_request_card
  status: gate_4_0_initial
  owner: workflow_os
---

# Child Obligation Request Card

## Purpose

Child Obligation Request Card serializes one focused child request from a parent Operator invocation.

The card is a transport adapter, not a semantic primitive.

It must be copy-paste runnable.

## Required Shape

```yaml
child_obligation_request_card:
  child_request_id: string
  parent_obligation_id: string
  child_obligation_id: string
  child_title_plain: string
  why_needed_plain: string
  launch_order: run_now | run_after | optional | blocked_until
  depends_on: [string]
  operator_id: string
  copy_paste_prompt: string
  forbidden_actions: [string]
  expected_result: string
  return_to_parent_instruction: string
  recovery_reference: string
```

## Rules

- It must not ask user to fill schema manually.
- It must include what the child must not decide.
- It must state whether the child is required or optional through launch order and expected result.
- It must include clear return instructions for the parent chat.
- It must not authorize Ledger mutation.
- It must not authorize closing the parent Obligation.
- It must not authorize parent-level final decisions.

END_OF_FILE: transport/CHILD_OBLIGATION_REQUEST_CARD.md
