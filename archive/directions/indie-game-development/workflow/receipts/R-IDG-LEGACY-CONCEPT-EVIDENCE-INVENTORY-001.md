---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: legacy_import_receipt
  status: accepted_after_verify_commit
  owner: proof_carrying_workflow_os
---

# R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001

## Receipt State

```yaml
receipt_id: R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001
direction_id: indie-game-development
operator: LegacyImport
target_obligation: O-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY
status: accepted_after_verify_commit
run_type: bounded_concept_evidence_inventory
source_context:
  - parent_chat_bounded_inventory_result
  - legacy_ref: vnext-r-main-before-proof-os-2026-05-25
  - current_direction_payload: directions/indie-game-development/workflow/
creates_accepted_state: true
accepted_state_kind: bounded_legacy_evidence_inventory_only
legacy_state_authority: false
```

## Purpose

Record the bounded legacy concept evidence inventory required before future concept-specific strategy decisions.

This Receipt does not make old Direction files accepted current state. It records only the evidence inventory extracted through the admitted LegacyImport obligation.

## Source Obligation

```yaml
obligation_id: O-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY
type: legacy_import
required_operator:
  - LegacyImport
required_inventory_fields:
  - concept premise
  - gameplay core
  - gas simulation role
  - player fantasy
  - genre/frame
  - commercial hooks
  - technical gameplay pillars
  - explicit unknowns
```

## Evidence Inventory

### Concept Premise

```yaml
candidate_claim: >
  The legacy concept points to an innovative, commercially viable co-op game centered
  on deep gas / 3D-space simulation; it should become a real game, not a technical demo.
confidence: medium_high
authority: legacy_evidence_candidate
accepted_as_strategy: false
```

### Gameplay Core

```yaml
candidate_claim: >
  The gameplay core is systemic co-op gameplay where gas behavior, grid/topology,
  spatial interaction, validation/debug visibility, and later co-op constraints combine
  into player-visible gameplay.
confidence: medium_high
authority: legacy_evidence_candidate
accepted_as_strategy: false
```

### Gas Simulation Role

```yaml
candidate_claim: >
  Gas is intended as a central gameplay system with propagation, accumulation/clearing,
  vertical density behavior, source/sink behavior, topology sensitivity, and observable hazards.
confidence: high
authority: legacy_evidence_candidate
physical_accuracy_first: false
```

### Player Fantasy

```yaml
candidate_claim: >
  Likely candidate player fantasy is cooperative players navigating and manipulating
  hazardous spatial gas systems in an expedition-like environment.
confidence: low_medium
authority: inference_from_legacy_evidence
import_as_fact: false
needs_future_confirmation: true
```

### Genre / Frame

```yaml
candidate_claim: >
  Legacy evidence frames the project as co-op and systemic/simulation-driven.
  Exact genre remains unresolved.
confidence: medium
authority: mixed_current_unresolved_plus_legacy_candidate
exact_genre_accepted: false
networking_stack_accepted: false
engine_accepted: false
```

### Commercial Hooks

```yaml
candidate_claim: >
  Candidate commercial hooks are distinctive player-visible technical identity,
  systemic co-op gas/topology situations, and showable proof once a playable identity exists.
confidence: medium
authority: legacy_evidence_candidate
steam_launch_strategy_created: false
monetization_model_created: false
pricing_created: false
```

### Technical Gameplay Pillars

```yaml
candidate_claim:
  - gas_simulation
  - grid_topology_substrate
  - grid_gas_interaction
  - stable_spatial_ids
  - validation_debug_surface
  - domain_first_testable_core
  - multiplayer_ready_authoritative_boundaries
confidence: high
authority: legacy_evidence_candidate
code_reuse_verdict_created: false
old_code_transfer_authorized: false
architecture_finalized: false
```

### Explicit Unknowns

```yaml
unknowns:
  - exact player fantasy wording
  - exact genre
  - visual style
  - engine choice
  - networking stack acceptance under current Ledger
  - monetization/pricing/revenue target
  - Steam launch strategy
  - final gas algorithms/data model
  - old code/test transfer value
  - direct reuse/rewrite/discard verdict for old Grid/GridV2/GasV2R
```

## Evidence References

```yaml
inspected_legacy_evidence:
  - ref: vnext-r-main-before-proof-os-2026-05-25
    path: directions/indie-game-development/project_files/08_DIRECTION_MAP.md
    use: concept premise, initiative, guardrails, commercial timing, technical pillars
  - ref: vnext-r-main-before-proof-os-2026-05-25
    path: directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md
    use: gas role, spatial/topology requirements, validation/debug requirements
  - ref: vnext-r-main-before-proof-os-2026-05-25
    path: directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md
    use: old Grid/GridV2/GasV2R/Grid-Gas evidence boundaries and non-reuse verdicts
  - ref: vnext-r-main-before-proof-os-2026-05-25
    path: directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md
    use: old source/code/test availability gaps and old evidence docs index
```

## Non-Import / Non-Authority Statement

This Receipt does not import any old Direction Map, Active Goal, Current Phase, Portfolio Queue, roadmap, old execution log, old phase state, old project_files/00-08 state, or old code as current accepted state.

Old legacy files remain evidence sources only.

## Forbidden Claims Preserved

```yaml
no_strategy: true
no_roadmap: true
no_horizon_selection: true
no_active_frontier_selection: true
no_product_execution: true
no_codex_execution: true
no_steam_launch_strategy: true
no_engine_commitment: true
no_networking_stack_commitment: true
no_old_code_transfer: true
no_game_documentation_promotion: true
```

## Scope Audit

```yaml
scope_audit:
  target_obligation: O-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY
  in_scope_used:
    - concept premise
    - gameplay core
    - gas simulation role
    - player fantasy candidate
    - genre/frame candidate
    - commercial hooks candidate
    - technical gameplay pillars
    - explicit unknowns
  necessary_dependencies:
    - current Ledger authority boundary
    - current Obligations boundary
    - legacy evidence branch/tag
    - old concept/technical evidence docs
  parked_residual_context:
    - old runtime phase/goal route state
    - old H1/H2/H3/H4 map structure
    - old Codex execution setup
    - Unity MCP discussion
    - networking stack finalization
    - old code transfer/reuse
  blocked_or_forbidden:
    - strategy
    - roadmap
    - Horizon selection
    - Active Frontier selection
    - product execution
    - CodexExecution
    - Steam launch strategy
    - engine commitment
    - old-code transfer
  hidden_acceptance_check: pass
  one_obligation_scope: pass
```

## Verification Result

```yaml
verification:
  receipt_created: true
  ledger_update_required: true
  receipts_index_update_required: true
  obligations_update_required: true
  dashboard_projection_update_required: true
  commit_required_for_accepted_state: true
```

END_OF_FILE: directions/indie-game-development/workflow/receipts/R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001.md
