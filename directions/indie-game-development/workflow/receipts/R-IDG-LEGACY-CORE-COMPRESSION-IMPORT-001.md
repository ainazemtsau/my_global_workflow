---
receipt_id: R-IDG-LEGACY-CORE-COMPRESSION-IMPORT-001
receipt_kind: legacy_import_compression_receipt
direction_id: indie-game-development
operator: LegacyEvidenceReview / ClarifyObjective / HumanDecision
target_obligation: O-IDG-LEGACY-CORE-COMPRESSION-IMPORT
status: accepted_after_verify_commit
candidate_status_before_merge_to_main: candidate_on_review_branch
creates_accepted_state: true_after_verify_commit_merge_to_main
creates_accepted_state_before_merge_to_main: false
legacy_documents_authority: evidence_only
legacy_documents_accepted_wholesale: false
old_workflow_state_imported: false
old_code_transfer_authorized: false
old_code_transfer_admitted: false
product_execution_admitted: false
codex_execution_admitted: false
strategy_admitted: false
roadmap_admitted: false
horizon_selected: false
active_frontier_selected: false
engine_commitment_admitted: false
networking_stack_commitment_admitted: false
steam_launch_strategy_admitted: false
---

# Receipt: IDG Legacy Core Compression Import 001

## Accepted State If Committed

```yaml
accepted_state_if_committed:
  proof_state_after_commit: legacy_core_compression_imported
  accepted_state_kind: bounded_legacy_core_compression_import
  accepted_game_concept_baseline: true
  accepted_foundation_core_boundary: true
  accepted_domain_documentation_claims: true
  accepted_technical_invariants: true
  accepted_first_nucleus_or_mvp_candidate: true_or_split_with_reason
  first_nucleus_or_mvp_candidate_resolution: split_with_reason
  split_reason: >
    Minimum Expedition Proof Core and first technical nucleus are accepted only
    as candidate boundary/evidence for a later execution-readiness obligation;
    playable proof design, implementation, Task Master graph, engine/networking
    choices, and old-code reuse remain deferred.
  candidate_follow_up_obligations_only: true
  next_execution_admitted: false
```

## Scope Audit

```yaml
scope_audit:
  target_obligation: O-IDG-LEGACY-CORE-COMPRESSION-IMPORT
  one_obligation_scope: pass
  in_scope_used:
    - live GitHub main proof state
    - restored legacy domain/game documentation
    - restored legacy technical foundation documentation
    - restored legacy phase/goal artifacts only as supporting evidence
    - current human instruction to compress/import core progress quickly
  blocked_or_forbidden:
    - product execution
    - CodexExecution product work
    - implementation
    - engine commitment
    - networking stack commitment
    - old-code transfer
    - roadmap
    - Horizon selection
    - Active Frontier selection
    - Steam launch strategy
```

## Context Authority Audit

```yaml
context_authority_audit:
  accepted_ledger_state: used_from_github_main
  committed_receipts_used: true
  dashboard_used_as_projection_only: true
  archive_used_as_legacy_evidence_only: true
  domain_docs_used_as_strong_legacy_evidence_only: true
  old_workflow_state_used_as_authority: false
  current_human_input_used: true
```

## Evidence Compression Result

```yaml
evidence_compression_result:
  import_packet: directions/indie-game-development/workflow/import_packets/IDG_LEGACY_CORE_COMPRESSION_IMPORT_PACKET_001.md
  archive_source: directions/indie-game-development/archive/legacy-vnext-r
  archive_file_count_total: 120
  domain_game_documentation_files_found: 30
  domain_markdown_docs_found: 25
  phase_goal_supporting_markdown_files_found: 72
  missing_expected_domain_docs: []
  missing_archive_navigation_files:
    - directions/indie-game-development/archive/legacy-vnext-r/README.md
    - directions/indie-game-development/archive/legacy-vnext-r/RESULTS_INDEX.md
```

## Verdicts

```yaml
verdicts:
  legacy_game_concept: adopt_with_amendments
  foundation_core: adopt_with_amendments
  domain_game_documentation: adopt_with_amendments
  technical_invariants: adopt_with_amendments
  first_nucleus_or_mvp_route: split
```

## Accepted Claim Summary If Committed

- Legacy game concept baseline is compressed into the current proof workflow as an Expedition / session-structured living reactive gas sandbox, with 2-4 player co-op framing, gas/topology/cargo/extraction decision pressure, and explicit non-goals.
- Foundation core boundary is compressed as Gas/Grid peer foundation: Gas is gameplay simulation truth and Grid/topology is shared spatial substrate.
- Domain/game documentation claims are accepted only through this bounded import; documents are not accepted wholesale.
- Technical invariants are accepted at architecture-boundary level only: stable IDs, explicit ownership, fail-fast validation, no-player debug surfaces, deterministic/update-order boundaries, and multiplayer-ready snapshot/delta/change-set surfaces.
- Minimum Expedition Proof Core and first technical nucleus are split into candidate execution-readiness inputs, not execution authorization.

## Explicit Non-Admitted State

```yaml
not_admitted:
  old_workflow_state: true
  old_horizon: true
  old_active_frontier: true
  old_roadmap: true
  old_stage_route: true
  old_phase_goal_status: true
  old_implementation_readiness: true
  product_execution: true
  codex_execution: true
  engine_commitment: true
  networking_stack_commitment: true
  old_code_transfer: true
  final_gas_taxonomy: true
  final_reaction_graph: true
  steam_launch_strategy: true
```

## Candidate Follow-Up Obligations

Candidate/proposed only:

1. `O-IDG-FOUNDATION-CORE-ACCEPTANCE-AND-EXECUTION-READINESS`
2. `O-IDG-TECHNICAL-EVIDENCE-AUDIT-FOR-FOUNDATION-BLOCKERS`
3. `O-IDG-FIRST-EXPEDITION-PROOF-EXECUTION-READINESS-PACKAGE`

## Validation Read-Back

This receipt is valid only with:

- `R-IDG-LEGACY-CORE-COMPRESSION-IMPORT-001` appended to Ledger and Receipts Index.
- `O-IDG-LEGACY-CORE-COMPRESSION-IMPORT` recorded as satisfied.
- `proof_state_after_commit: legacy_core_compression_imported`.
- `open_next_obligations: []`.
- no product execution, CodexExecution, strategy, roadmap, Horizon, Active Frontier, engine/networking commitment, Steam launch strategy, or old-code transfer admitted.

END_OF_FILE: directions/indie-game-development/workflow/receipts/R-IDG-LEGACY-CORE-COMPRESSION-IMPORT-001.md
