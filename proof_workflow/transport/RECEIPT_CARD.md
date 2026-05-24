---
artifact_control:
  namespace: proof_workflow
  artifact_type: transport_card
  card_type: receipt_card
  status: gate_1_initial
  owner: proof_carrying_workflow_os
---

# Receipt Card

## Purpose

Receipt Card serializes a Receipt produced by one Operator invocation over one Obligation.

Receipt is candidate state until committed.

## Required Shape

```yaml
receipt_card:
  receipt_id: string
  obligation_id: string
  operator_id: string
  verdict: satisfied | partial | blocked | invalidated | split_required | failed
  produced_claims:
    - claim: string
      claim_role: fact | inference | assumption | preference | decision | validation | forecast | constraint | artifact_quality
      evidence_refs: [string]
      confidence_label: high | medium | low | unknown
      uncertainty_label: none | bounded | material | unresolved
  evidence:
    - evidence_id: string
      kind: source_backed | tested_result | human_decision | expert_audit | reasoned_inference | direct_observation | tool_return | codex_validation
      source_ref: string
      summary: string
  assumptions: [string]
  confidence_uncertainty_labels:
    overall_confidence: high | medium | low | unknown
    material_uncertainties: [string]
  residual_obligations:
    - obligation_statement: string
      reason: string
  invalidated_obligations: [string]
  ledger_delta_proposal: object | null
  proof_policy_result: pass | fail | needs_input
  invariant_check_summary: string
  commit_recommendation: commit | do_not_commit | needs_human_gate
```

## Rules

Receipt Card must not claim committed state unless a later Commit Packet records a committed result.

Residual Obligations must be explicit when the verdict is partial, blocked, or split_required.

Evidence references must be specific enough for verification.

END_OF_FILE: proof_workflow/transport/RECEIPT_CARD.md
