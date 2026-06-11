---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: strategic_path_map_projection
  status: projection_only_created
  owner: proof_carrying_workflow_os
---

# IDG Strategic Path Map Projection 001

## Projection Control

```yaml
projection_id: IDG-STRATEGIC-PATH-MAP-PROJECTION-001
projection_type: StrategicPathMapProjection
source_ledger_ref: directions/indie-game-development/workflow/LEDGER.md@main
source_receipt_ids:
  - R-IDG-ROOT-OBJECTIVE-DECISION-001
  - R-IDG-SUCCESS-SEMANTICS-DEFINE-001
  - R-IDG-CONSTRAINTS-DEFINE-001
generated_at: 2026-05-27
authority_boundary:
  creates_truth: false
  creates_strategy_commitment: false
  creates_horizon: false
  creates_active_frontier: false
  creates_roadmap: false
  admits_product_execution: false
  admits_codex_execution: false
  imports_legacy: false
accepted_anchors:
  root_objective: from R-IDG-ROOT-OBJECTIVE-DECISION-001
  success_semantics: from R-IDG-SUCCESS-SEMANTICS-DEFINE-001
  constraints: from R-IDG-CONSTRAINTS-DEFINE-001
```

## Projection Boundary

This artifact is a projection surface only. It does not accept a strategy, choose a Horizon, select an Active Frontier, create a roadmap, admit product execution, admit Codex execution, import legacy material, or convert old concept/archive details into accepted claims.

Current-state note: the candidate next obligation below is historical projection context. `O-IDG-STRATEGIC-ROUTE-DECIDE` was later satisfied by `R-IDG-STRATEGIC-ROUTE-DECIDE-001`. Read current next state from `directions/indie-game-development/workflow/LEDGER.md`, `directions/indie-game-development/workflow/OBLIGATIONS.md`, and `directions/indie-game-development/workflow/DASHBOARD.md`.

## Strategic Surfaces

```yaml
strategic_surfaces:
  - S1_LEGACY_CONCEPT_EVIDENCE
  - S2_GAMEPLAY_DEPTH_CORE
  - S3_STEAM_COMMERCIAL_PATH
  - S4_NINE_MONTH_INCOME_PRESSURE
  - S5_PRODUCTION_FEASIBILITY
  - S6_MARKETING_PROCESS_SYSTEM
```

## Strategic Tensions

```yaml
strategic_tensions:
  - T1_DEPTH_VS_TIME
  - T2_TECH_VS_GAMEPLAY
  - T3_STEAM_ONLY_VS_UNRESOLVED_LAUNCH
  - T4_SELECTED_CONCEPT_VS_NO_LEGACY_IMPORT
```

## Unsupported Or Unresolved Claims

```yaml
unsupported_or_unresolved_claims:
  - exact production/release schedule
  - exact launch date
  - exact revenue target
  - exact profit definition
  - exact monetization model
  - pricing
  - Steam launch strategy
  - Steam tactics
  - engine choice
  - networking stack
  - exact genre
  - visual style
  - specific algorithms/data models
  - Codex execution readiness
  - roadmap
  - Horizon
  - Active Frontier
  - accepted strategy
  - product execution
  - legacy import
  - old concept/archive details
```

## Candidate Next Obligation

```yaml
candidate_next_obligation:
  id: O-IDG-STRATEGIC-ROUTE-DECIDE
  status: historical_candidate_superseded_by_R-IDG-STRATEGIC-ROUTE-DECIDE-001
  purpose: Decide which strategic route to admit next.
refresh_policy: Refresh after any Ledger change affecting root objective, success semantics, constraints, strategic receipts, legacy import, Horizon, Active Frontier, roadmap, or execution readiness.
```

## Refresh Policy

Refresh after any Ledger change affecting root objective, success semantics, constraints, strategic receipts, legacy import, Horizon, Active Frontier, roadmap, or execution readiness.

END_OF_FILE: directions/indie-game-development/workflow/projections/IDG_STRATEGIC_PATH_MAP_PROJECTION_001.md
