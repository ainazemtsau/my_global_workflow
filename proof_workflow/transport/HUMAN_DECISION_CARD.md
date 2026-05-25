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
  option_framing_audit:
    unaccepted_candidate_constraints_present: [string]
    options_that_embed_candidate_constraints:
      - option_id: string
        embedded_constraint: string
        authority_status: accepted | candidate | unknown | legacy
    neutral_or_broader_option_included: boolean
    user_must_explicitly_accept_embedded_constraints: boolean
  what_user_must_decide: string
  what_happens_after_decision: string
```

## Rules

Use this card when the next move depends on preference, risk acceptance, priority, irreversible action, repository mutation approval, product/project execution, launch, publication, or other human-owned choice.

The card may recommend, but the user supplies the decision.

If a material decision option embeds an unaccepted candidate constraint, the card must label it.

If all major options embed the same candidate constraint, the card is invalid unless the decision statement explicitly asks the user to accept that constraint.

At least one broader, custom, or neutral option must be included unless the constraint is already accepted in Ledger.

The decision becomes accepted state only through a Receipt and Commit.

END_OF_FILE: proof_workflow/transport/HUMAN_DECISION_CARD.md
