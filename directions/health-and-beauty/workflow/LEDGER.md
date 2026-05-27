---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: ledger
  status: horizon_selected_h1_health_operating_project_bootstrap_downstream_not_started
  owner: proof_carrying_workflow_os
---

# Health and Beauty Proof Ledger

```yaml
direction_id: health-and-beauty
proof_state: horizon_selected_h1_health_operating_project_bootstrap_downstream_not_started
accepted_receipts:
  - R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26
  - R-HB-CONSTRAINTS-DEFINE-2026-05-26
  - R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27
  - R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27
  - R-HB-STRATEGIC-MAP-PROJECTION-CREATE-2026-05-27
  - R-HB-HORIZON-SELECT-2026-05-27
accepted_claims:
  - C-HB-ROOT-OBJECTIVE-2026-05-26
  - C-HB-ROOT-OBJECTIVE-AMENDED-35KG-2026-05-27
  - C-HB-CONSTRAINT-ANTHROPOMETRIC-BASELINE-2026-05-26
  - C-HB-CONSTRAINT-SAFETY-OVERRIDE-2026-05-26
  - C-HB-CONSTRAINT-STRICT-STRUCTURE-2026-05-26
  - C-HB-CONSTRAINT-LOW-FRICTION-TRACKING-2026-05-26
  - C-HB-CONSTRAINT-TRAINING-BASELINE-2026-05-26
  - C-HB-CONSTRAINT-RESOURCE-ABUNDANCE-2026-05-26
  - C-HB-CONSTRAINT-FOOD-FLEXIBILITY-2026-05-26
  - C-HB-SUCCESS-TARGET-WEIGHT-2026-05-27
  - C-HB-SUCCESS-WEIGHT-MILESTONES-2026-05-27
  - C-HB-SUCCESS-PACE-ENVELOPE-2026-05-27
  - C-HB-SUCCESS-STRENGTH-PRESERVATION-2026-05-27
  - C-HB-SUCCESS-CARDIO-FUNCTION-2026-05-27
  - C-HB-SUCCESS-MOBILITY-2026-05-27
  - C-HB-SUCCESS-BEHAVIORAL-STABILITY-2026-05-27
  - C-HB-SUCCESS-LOW-FRICTION-TRACKING-2026-05-27
  - C-HB-SUCCESS-SAFETY-STOPS-2026-05-27
  - C-HB-STRATEGIC-MAP-PROJECTION-2026-05-27
  - C-HB-NEXT-VALID-HORIZON-SELECTION-2026-05-27
  - C-HB-HORIZON-H1-SELECTED-2026-05-27
  - C-HB-H1-SELECTION-INTENT-MINIMAL-USABLE-CORE-FIRST-2026-05-27
root_objective: "Снижение массы тела на 35 кг: с текущих 125 кг примерно до 90 кг, при сохранении или минимальной потери физической силы, общей физической формы, гибкости/подвижности и функционального самочувствия; построение управляемой системы, где ChatGPT помогает вести питание, тренировки, трекинг, исследования и решения с минимальной нагрузкой на пользователя."
success_semantics_state: accepted_by_R-HB-SUCCESS-SEMANTICS-DEFINE-2026-05-27
constraints_state: accepted_by_R-HB-CONSTRAINTS-DEFINE-2026-05-26
objective_delta_state: resolved_accepted_by_R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27
objective_delta_obligation: closed_by_R-HB-ROOT-OBJECTIVE-AMEND-TO-35KG-2026-05-27
open_obligations: directions/health-and-beauty/workflow/OBLIGATIONS.md
commit_scopes: directions/health-and-beauty/workflow/COMMIT_SCOPES.md
projections_state: strategic_map_projection_committed_by_R-HB-STRATEGIC-MAP-PROJECTION-CREATE-2026-05-27
strategic_map_projection: directions/health-and-beauty/workflow/projections/STRATEGIC_PATH_MAP.md
selected_horizon:
  horizon_id: H1_HEALTH_OPERATING_PROJECT_BOOTSTRAP
  label: Health Operating Project Bootstrap
  selected_by: R-HB-HORIZON-SELECT-2026-05-27
  selection_intent_id: MINIMAL-USABLE-CORE-FIRST
  selection_intent: "Minimal usable Daily Ops core first."
  scope_boundary: "Horizon selection only; no downstream implementation."
downstream_implementation_state: not_started
legacy_import_state: not_performed
legacy_state_authority: false
```

This Ledger contains no imported old Direction facts.

Old `project_files/00-08` are not accepted proof state.

Any future import requires Legacy Import Receipt + Verify + Commit.

Only verified Receipts committed to this Ledger create accepted state for this Direction.

END_OF_FILE: directions/health-and-beauty/workflow/LEDGER.md
