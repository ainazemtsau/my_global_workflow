---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: receipt
  receipt_id: R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27
  status: committed
  owner: proof_carrying_workflow_os
---

# Receipt: R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27

```yaml
receipt_id: R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27
direction_id: health-and-beauty
target_obligation: O-HB-ROOT-OBJECTIVE-AMEND-TO-35KG
operator_invoked: ClarifyObjective / AskHumanDecision
commit_scope: hb_root_scope
status: committed

human_decision:
  normalized_from_unstructured_input: true
  prior_accepted_root_objective_delta: -25 kg
  amended_root_objective_delta: -35 kg
  current_weight_kg: 125
  target_weight_kg: about_90
  amended_root_objective: >
    Снижение массы тела на 35 кг: с текущих 125 кг примерно до 90 кг,
    при сохранении или минимальной потере физической силы, общей физической
    формы, гибкости/подвижности и функционального самочувствия; построение
    управляемой системы, где ChatGPT помогает вести питание, тренировки,
    трекинг, исследования и решения с минимальной нагрузкой на пользователя.

claims_accepted_by_this_receipt:
  - claim_id: C-HB-ROOT-OBJECTIVE-AMENDED-35KG-2026-05-27
    type: root_objective_amendment
    replaces_target_delta_from: -25 kg
    replaces_target_delta_to: -35 kg
    target_weight: about_90_kg
    value: >
      Снижение массы тела на 35 кг: с текущих 125 кг примерно до 90 кг,
      при сохранении или минимальной потере физической силы, общей физической
      формы, гибкости/подвижности и функционального самочувствия; построение
      управляемой системы, где ChatGPT помогает вести питание, тренировки,
      трекинг, исследования и решения с минимальной нагрузкой на пользователя.

context_authority_audit:
  accepted_ledger_state:
    - root objective currently accepted at -25 kg before this receipt
    - constraints accepted by R-HB-CONSTRAINTS-DEFINE-2026-05-26
    - objective_delta_state pending before this receipt
  committed_receipts:
    - R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26
    - R-HB-CONSTRAINTS-DEFINE-2026-05-26
  current_human_input:
    - user previously stated that target effectively becomes minus 35 kg
    - user reported constraints commit merged to main
  projection_context:
    - Dashboard next valid run is root objective amendment, then success semantics
  instruction_context:
    - one Obligation scope
    - Receipt is candidate until Verify + Commit
  candidate_context:
    - future success semantics
    - future diet/training/tracking design
  unknown:
    - exact success pace and milestone metrics remain unresolved

scope_audit:
  one_obligation_scope: passed
  in_scope_used:
    - root objective target delta amendment
    - human input normalization
  parked_residual_context:
    - success semantics
    - diet prescription
    - training prescription
    - fast-start protocol
    - tracking architecture
    - roadmap
    - Codex/product execution
  blocked_or_forbidden_now:
    - no accepted diet prescription
    - no accepted training prescription
    - no Strategic Path Map
    - no Horizon selection
    - no Active Frontier
    - no roadmap
    - no Codex/product execution
    - no tracking implementation
  hidden_acceptance_check: passed

invariant_checks:
  one_obligation_only: passed
  no_execution_without_execution_obligation: passed
  no_legacy_import_without_legacy_import_obligation: passed
  no_strategy_projection_before_required_receipts: passed
  no_diet_or_training_plan_created: passed
  objective_delta_explicitly_resolved: passed
  receipt_committed_to_ledger: pending_until_commit_applied

END_OF_FILE: directions/health-and-beauty/workflow/receipts/R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27.md
