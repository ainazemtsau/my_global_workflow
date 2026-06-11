---
artifact_control:
  namespace: workflow
  artifact_type: transport_card
  card_type: receipt_card
  status: single_material_run_chat_boundary_hardened
  owner: workflow_os
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
  parent_child_context:
    parent_obligation_id: string | null
    child_obligation_id: string | null
    sufficient_for_parent_synthesis: true | false | null
    child_result_return_required: true | false
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
  scope_audit:
    target_obligation: string
    in_scope_used: [string]
    necessary_dependencies: [string]
    parked_residual_context: [string]
    proposed_residual_obligations:
      - obligation_statement: string
        reason: string
    blocked_or_forbidden: [string]
    explicit_decisions: [string]
    candidate_examples: [string]
    child_handoff_needed: true | false
    child_handoff_reason: string | null
    hidden_acceptance_check: pass | fail | needs_input
    one_obligation_scope: pass | fail | needs_input
  parent_chat_continuity:
    chat_episode_target: string
    material_run_count_in_chat: integer
    same_parent_chat_continuation: true | false
    continuation_reason: string
    codex_result_verification_only: true | false
    next_material_target_requires_new_chat: true | false
    next_chat_needed: true | false
    next_chat_reason: string | null
    next_chat_prompt_required: true | false
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
    codex_commit_handoff_self_contained: true | false
    missing_handoff_fields:
      - field: string
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

Every Receipt that uses broad, messy, anxious, speculative, or phase-jumping input must include `scope_audit`.

`scope_audit.target_obligation` must name the single active target Obligation for the material work.

`scope_audit.in_scope_used` and `scope_audit.necessary_dependencies` are the only broad-input fields that may drive material output.

`scope_audit.parked_residual_context` and `scope_audit.proposed_residual_obligations` preserve useful off-scope input without acting on it prematurely.

`scope_audit.blocked_or_forbidden` must list phase jumps, roadmap, Horizon, Active Frontier, execution, legacy import, or other forbidden work raised by the input.

`scope_audit.hidden_acceptance_check` must fail when candidate context, examples, user urgency, anxiety, brainstorming, or platform/channel/tool mentions are treated as accepted state without Receipt, Verify, and Commit.

`scope_audit.one_obligation_scope` must fail when material output performs research, strategy, roadmap, execution, or structure creation not required by the target Obligation.

`parent_chat_continuity.chat_episode_target` must name the target Obligation for the current chat episode.

`parent_chat_continuity.material_run_count_in_chat` must be recorded. Ordinary Direction chats default to `1`.

`parent_chat_continuity.same_parent_chat_continuation` is not true by default after material run closure. It may be true only for current-run verification/closure, non-material explanation, failed validation repair for the same handoff, recovery / next-chat prompt production, or child-result synthesis required for the current target Obligation.

`parent_chat_continuity.codex_result_verification_only` must be true when a Codex result returns after `CODEX_COMMIT_NEEDED`.

`parent_chat_continuity.next_material_target_requires_new_chat`, `next_chat_needed`, and `next_chat_prompt_required` must be true when a new target Obligation is opened for future material work.

If `commit_recommendation` is `commit`, the response must include either:

- `codex_commit_handoff: true` with `codex_commit_handoff_self_contained: true`
- explicit reason commit handoff is deferred

Partial handoff is invalid.

The handoff must not require the user to add repository, worktree, branch, mode, allowed paths, forbidden paths, commit behavior, push behavior, or no-main-merge instructions.

END_OF_FILE: workflow/transport/RECEIPT_CARD.md
