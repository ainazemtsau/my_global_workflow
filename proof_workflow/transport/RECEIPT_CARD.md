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
  verdict: satisfied | partial_success_with_residuals | partial | blocked | invalidated | split_required | failed
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
  human_input_normalization:
    used: boolean
    raw_user_input_ref: string | null
    interpreted_decision: string | null
    selected_option_id: string | null
    selected_option_text: string | null
    defaults_applied:
      - field: string
        value: string
        reason: string
    fields_not_accepted: [string]
    ambiguity_remaining: [string]
  context_authority_audit:
    accepted_state_used: [string]
    committed_receipts_used: [string]
    candidate_context_used: [string]
    projection_context_used: [string]
    legacy_evidence_used: [string]
    assumptions_promoted_to_claims: boolean
    unaccepted_constraints_embedded: boolean
    notes: string | null
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
  handoff_required:
    codex_commit_handoff: true | false
    next_chat_prompt: true | false
    reason: string
```

## Rules

Receipt Card must not claim committed state unless a later Commit Packet records a committed result.

Residual Obligations must be explicit when the verdict is partial, blocked, or split_required.

Evidence references must be specific enough for verification.

Receipt must fail or return `needs_input` if it promotes candidate_context to accepted claim without human decision or committed Receipt.

Normalized human input must be visible in the Receipt and must not hide defaults.

Every normalized Receipt must include raw user input reference, interpreted decision, selected option when applicable, defaults applied, fields not accepted, residual Obligations, and remaining ambiguity.

If `commit_recommendation` is `commit`, the response must include either a Codex Commit Handoff Card or an explicit reason commit handoff is deferred.

END_OF_FILE: proof_workflow/transport/RECEIPT_CARD.md
