---
artifact_control:
  namespace: direction_proof
  direction_id: workflow-governance
  artifact_type: receipt
  receipt_id: R-WG-ATOMIC-RUN-HARDEN-001
  status: accepted
  owner: proof_carrying_workflow_os
---

# Receipt: Atomic Run And Parent Chat Continuity Hardening

```yaml
receipt_id: R-WG-ATOMIC-RUN-HARDEN-001
source_obligation_id: O-WG-ATOMIC-RUN-HARDEN
commit_scope: wg_workflow_policy_scope
receipt_status: accepted
accepted_at: 2026-05-26
operator_mode: repository_maintenance
product_execution_allowed: false
legacy_import_performed: false
summary: >
  Accepts Workflow OS hardening that combines strict one-active-target-Obligation
  discipline with practical parent-chat continuity. Broad user input must be
  scope-triaged before material work; off-scope concerns are preserved as residual
  context instead of acted on prematurely; user urgency, anxiety, examples, and
  channel/tool mentions cannot cause hidden acceptance or phase drift. One bounded
  user problem stays in one parent chat until terminal outcome when safe. Codex and
  child results return to the parent chat; NEXT_CHAT_NEEDED is exceptional.
accepted_claims:
  - atomic_run_single_responsibility_hardened
  - operator_independence_hardened
  - scope_triage_before_material_work_required
  - parent_chat_problem_closure_required
  - child_handoff_gated_by_current_obligation_need
  - receipt_scope_audit_required
  - same_parent_chat_default_for_codex_results
evidence:
  - evidence_id: E-WG-ROOT-OBJECTIVE-RECEIPT-001
    kind: committed_receipt
    source_ref: directions/workflow-governance/workflow/receipts/R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001.md
    summary: Root objective admitted Atomic Run hardening as the next valid Workflow Governance work item.
  - evidence_id: E-WG-OBLIGATION-ATOMIC-RUN-001
    kind: accepted_ledger_state
    source_ref: directions/workflow-governance/workflow/OBLIGATIONS.md
    summary: O-WG-ATOMIC-RUN-HARDEN was open before this patch.
  - evidence_id: E-WG-HUMAN-HANDOFF-001
    kind: current_human_input
    source_ref: current Codex handoff card CCH-WG-ATOMIC-RUN-HARDEN-001
    summary: User requested one hardening patch for Atomic Run discipline and Parent Chat Problem Closure.
changed_policy_surfaces:
  - workflow/core/02_RUNTIME_PROTOCOLS.md
  - workflow/invariants/CORE_INVARIANTS.md
  - workflow/policies/08_CHATGPT_PROJECT_SETUP.md
  - workflow/policies/10_CONTEXT_AUTHORITY_POLICY.md
  - workflow/policies/11_HUMAN_INPUT_NORMALIZATION_POLICY.md
  - workflow/policies/12_HUMAN_FACING_RUN_CLOSURE_POLICY.md
  - workflow/policies/13_RECURSIVE_CHILD_HANDOFF_POLICY.md
  - workflow/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md
  - workflow/transport/RECEIPT_CARD.md
refreshed_runtime_caches:
  - workflow/project_packs/WORKFLOW_BASE_PACK.md
  - workflow/project_packs/UNIVERSAL_PROJECT_SHELL_PACK.md
  - workflow/project_packs/TRANSPORT_CORE_PACK.md
  - workflow/project_packs/PROJECT_PACKS_INDEX.md
  - directions/workflow-governance/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
  - directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
scope_audit:
  target_obligation: O-WG-ATOMIC-RUN-HARDEN
  in_scope_used:
    - Atomic Run / Single Responsibility enforcement
    - Operator Independence / Effectiveness Over Agreement
    - Scope Triage Before Material Work
    - Parent Chat Problem Closure and Same Parent Chat Default
    - child-handoff gating for current Obligation need
    - Receipt scope audit and parent chat continuity fields
    - project setup instruction and pack refresh
  necessary_dependencies:
    - R-WG-ROOT-OBJECTIVE-ATOMIC-RUN-001
    - existing Workflow Governance proof payload
    - active workflow policy files listed in WORKFLOW_SOURCE_OF_TRUTH.md
  parked_residual_context: []
  proposed_residual_obligations: []
  blocked_or_forbidden:
    - product execution
    - roadmap creation
    - Horizon selection
    - Active Frontier selection
    - legacy import
    - Indie Game Development proof-state mutation
    - execution harness changes
  explicit_decisions:
    - Harden workflow policy now under O-WG-ATOMIC-RUN-HARDEN.
    - Keep one bounded user problem in one parent chat until terminal outcome when safe.
    - Treat NEXT_CHAT_NEEDED as exceptional.
  candidate_examples:
    - Indie Game Development Project Instructions were refreshed as the observed failure surface without mutating Indie Game Development proof state.
  child_handoff_needed: false
  child_handoff_reason: null
  hidden_acceptance_check: pass
  one_obligation_scope: pass
parent_chat_continuity:
  same_parent_chat_continuation: true
  continuation_reason: >
    The hardening patch preserves parent-chat problem closure by returning Codex and
    child results to the parent chat when safe.
  next_chat_needed: false
  next_chat_reason: null
obligation_deltas:
  - obligation_id: O-WG-ATOMIC-RUN-HARDEN
    status: satisfied
    satisfied_by_receipt: R-WG-ATOMIC-RUN-HARDEN-001
ledger_delta:
  accepted_receipts_add:
    - R-WG-ATOMIC-RUN-HARDEN-001
  accepted_claims_add:
    - atomic_run_single_responsibility_hardened
    - operator_independence_hardened
    - scope_triage_before_material_work_required
    - parent_chat_problem_closure_required
    - child_handoff_gated_by_current_obligation_need
    - receipt_scope_audit_required
    - same_parent_chat_default_for_codex_results
forbidden_state_preserved:
  - no product execution
  - no roadmap
  - no Horizon
  - no Active Frontier
  - no legacy import
  - no Indie Game Development proof-state mutation
project_files_refresh_required:
  - Refresh Workflow Governance Project Files with LEDGER.md, OBLIGATIONS.md,
    RECEIPTS_INDEX.md, DASHBOARD.md, COMMIT_SCOPES.md, and
    project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md.
  - Refresh shared packs: UNIVERSAL_PROJECT_SHELL_PACK.md, WORKFLOW_BASE_PACK.md,
    TRANSPORT_CORE_PACK.md, and PROJECT_PACKS_INDEX.md.
  - Refresh Indie Game Development Project Instructions with
    directions/indie-game-development/workflow/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md.
  - Do not load EXECUTION_HARNESS_PACK.md by default; it remains request-only.
```

END_OF_FILE: directions/workflow-governance/workflow/receipts/R-WG-ATOMIC-RUN-HARDEN-001.md
