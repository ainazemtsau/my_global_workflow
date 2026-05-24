---
artifact_control:
  namespace: proof_workflow
  artifact_type: transport_card
  card_type: human_decision_card
  status: gate_1_initial
  owner: proof_carrying_workflow_os
---

# Human Decision Card

## Purpose

Human Decision Card serializes a human-owned decision request.

The workflow must not write the user's decision for them.

## Required Shape

```yaml
human_decision_card:
  decision_id: string
  related_obligation_id: string
  decision_statement: string
  options:
    - option_id: string
      label: string
      description: string
  evidence_receipts: [string]
  consequences:
    - option_id: string
      consequence: string
  recommendation_if_any:
    option_id: string | null
    rationale: string | null
  what_user_must_decide: string
  what_happens_after_decision: string
```

## Rules

Use this card when the next move depends on preference, risk acceptance, priority, irreversible action, repository mutation approval, product/project execution, launch, publication, or other human-owned choice.

The card may recommend, but the user supplies the decision.

The decision becomes accepted state only through a Receipt and Commit.

END_OF_FILE: proof_workflow/transport/HUMAN_DECISION_CARD.md
