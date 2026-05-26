---
artifact_control:
  namespace: workflow
  artifact_type: transport_card
  card_type: human_action_card
  status: gate_2_initial
  owner: workflow_os
---

# Human Action Card

## Purpose

Human Action Card serializes a human-guided execution request for sensitive, manual, external, or unavailable automation steps.

The workflow may guide; the human performs the action.

## Required Shape

```yaml
human_action_card:
  card_id: string
  related_obligation_id: string
  action_purpose: string
  exact_steps:
    - step: string
  expected_visible_result: string
  stop_conditions:
    - condition: string
  evidence_to_return:
    - evidence: string
  human_confirmation_receipt:
    action_performed: string
    observed_result: string
    evidence_refs: [string]
    deviations: [string]
    stop_conditions_encountered: [string]
    confirmed_by_human: true | false
```

## Rules

- Stop on irreversible action, payment/purchase, permission prompt, secret exposure, UI mismatch, unexpected warning, or validation mismatch.
- Human confirmation is required before the action can support a Receipt.
- The card must not ask the workflow to perform a human-owned sensitive action.

END_OF_FILE: transport/HUMAN_ACTION_CARD.md
