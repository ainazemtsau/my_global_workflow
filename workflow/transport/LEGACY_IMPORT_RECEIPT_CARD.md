---
artifact_control:
  namespace: workflow
  artifact_type: transport_card
  card_type: legacy_import_receipt_card
  status: gate_1_initial
  owner: workflow_os
---

# Legacy Import Receipt Card

## Purpose

Legacy Import Receipt Card serializes a Receipt for importing old workflow or Direction facts.

Old files may be evidence, not authority.

## Required Shape

```yaml
legacy_import_receipt_card:
  receipt_id: string
  source_path: string
  imported_claim: string
  claim_role: fact | inference | assumption | preference | decision | validation | forecast | constraint | artifact_quality
  accepted_for_new_ledger: boolean
  requires_user_confirmation: boolean
  rejected_or_legacy_only_reason: string | null
  contamination_check:
    old_semantic_term_detected: boolean
    demotion_required: boolean
    notes: string
  ledger_delta_proposal: object | null
```

## Rules

Legacy import must not copy old semantic authority into the new Ledger.

Every accepted imported claim must pass verification policy and invariant checks.

If the source contains old workflow concepts, the Receipt must state whether the claim is rejected, demoted, or accepted under new kernel terms.

END_OF_FILE: workflow/transport/LEGACY_IMPORT_RECEIPT_CARD.md
