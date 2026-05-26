---
artifact_control:
  namespace: workflow
  artifact_type: transport_card
  card_type: context_request_card
  status: gate_1_initial
  owner: workflow_os
---

# Context Request Card

## Purpose

Context Request Card serializes missing blocking context.

It is used when an Operator cannot safely proceed, verify, or commit with the available information.

## Required Shape

```yaml
context_request_card:
  request_id: string
  blocking_obligation_id: string
  missing_context:
    - item: string
      expected_form: string
  why_required: string
  smallest_sufficient_context: string
  acceptable_sources: [string]
  unsafe_to_continue_reason: string
  return_target: string
```

## Rules

The card must ask for the smallest sufficient context, not broad background.

The card must explain why proceeding would risk unsupported claims, invariant failure, or invalid commit.

The card does not close the blocking Obligation.

END_OF_FILE: workflow/transport/CONTEXT_REQUEST_CARD.md
