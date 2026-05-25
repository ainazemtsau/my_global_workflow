---
artifact_control:
  namespace: proof_workflow
  artifact_type: transport_card
  card_type: child_result_return_card
  status: gate_4_0_initial
  owner: proof_carrying_workflow_os
---

# Child Result Return Card

## Purpose

Child Result Return Card serializes a compact child result for parent synthesis.

Child result is candidate input to parent, not Ledger state.

## Required Shape

```yaml
child_result_return_card:
  child_result_id: string
  parent_obligation_id: string
  child_obligation_id: string
  verdict: satisfied | partial | blocked | failed | needs_human_decision
  human_summary: string
  parent_relevant_findings: [string]
  evidence_or_basis: [string]
  assumptions: [string]
  blockers: [string]
  decisions_made: [string]
  decisions_not_made: [string]
  sufficient_for_parent_synthesis: true | false
  missing_inputs: [string]
  recommended_parent_action: string
  technical_receipt_ref_or_embedded_receipt: string | object | null
```

## Rules

- Child result is candidate input to parent, not Ledger state.
- Child does not mutate Ledger.
- Child does not close parent.
- Child should not return full heavy artifact unless parent asked for it.
- Child should return compact, parent-facing findings.
- Child must list decisions not made when those decisions belong to the parent or human.

END_OF_FILE: proof_workflow/transport/CHILD_RESULT_RETURN_CARD.md
