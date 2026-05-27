---
artifact_control:
  namespace: direction_proof
  direction_id: health-and-beauty
  artifact_type: ledger
  status: root_objective_and_constraints_accepted_objective_delta_pending
  owner: proof_carrying_workflow_os
---

# Health and Beauty Proof Ledger

```yaml
direction_id: health-and-beauty
proof_state: root_objective_and_constraints_accepted_objective_delta_pending
accepted_receipts:
  - R-HB-ROOT-OBJECTIVE-CONFIRM-2026-05-26
  - R-HB-CONSTRAINTS-DEFINE-2026-05-26
accepted_claims:
  - C-HB-ROOT-OBJECTIVE-2026-05-26
  - C-HB-CONSTRAINT-ANTHROPOMETRIC-BASELINE-2026-05-26
  - C-HB-CONSTRAINT-SAFETY-OVERRIDE-2026-05-26
  - C-HB-CONSTRAINT-STRICT-STRUCTURE-2026-05-26
  - C-HB-CONSTRAINT-LOW-FRICTION-TRACKING-2026-05-26
  - C-HB-CONSTRAINT-TRAINING-BASELINE-2026-05-26
  - C-HB-CONSTRAINT-RESOURCE-ABUNDANCE-2026-05-26
  - C-HB-CONSTRAINT-FOOD-FLEXIBILITY-2026-05-26
root_objective: "Снижение массы тела на 25 кг при сохранении или минимальной потере физической силы, общей физической формы, гибкости/подвижности и функционального самочувствия; построение управляемой системы, где ChatGPT помогает вести питание, тренировки, трекинг, исследования и решения с минимальной нагрузкой на пользователя."
success_semantics_state: delegated_to_O-HB-SUCCESS-SEMANTICS-DEFINE
constraints_state: accepted_by_R-HB-CONSTRAINTS-DEFINE-2026-05-26
objective_delta_state: candidate_amendment_required_to_resolve_minus_35kg_target
objective_delta_obligation: O-HB-ROOT-OBJECTIVE-AMEND-TO-35KG
open_obligations: directions/health-and-beauty/workflow/OBLIGATIONS.md
commit_scopes: directions/health-and-beauty/workflow/COMMIT_SCOPES.md
projections_state: none_available_until_success_semantics_and_objective_delta_resolution
legacy_import_state: not_performed
legacy_state_authority: false
```

This Ledger contains no imported old Direction facts.

Old `project_files/00-08` are not accepted proof state.

Any future import requires Legacy Import Receipt + Verify + Commit.

Only verified Receipts committed to this Ledger create accepted state for this Direction.

END_OF_FILE: directions/health-and-beauty/workflow/LEDGER.md
