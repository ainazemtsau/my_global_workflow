---
artifact_control:
  namespace: workflow
  artifact_type: execution_evals
  status: gate_2_initial
  owner: workflow_os
---

# Execution Evals

## Gate 2 Scenarios

- [ ] Simple code task passes with target binding, launch card, implementation receipt, validation receipt, and commit recommendation.
- [ ] CodexRun is blocked because no target binding exists.
- [ ] CodexRun is blocked because no validation plan exists.
- [ ] Complex Technical Mission is blocked from direct implementation and routed through mission protocol.
- [ ] Required subagent missing from return makes Execution Receipt invalid.
- [ ] Validation failed produces repair Obligation or repair CodexRun, not done.
- [ ] Validation unavailable produces `validation_gap` and Human Action Card when human/local action is needed.
- [ ] Human-guided external action requires Human Action Card and human confirmation receipt.
- [ ] Technical memory update is required after implementation that changes architecture, modules, validation expectations, or risks.
- [ ] Business projection does not claim more than accepted technical receipt evidence proves.

## Negative Semantic Checks

- [ ] Execution is not added as a semantic primitive.
- [ ] Codex is not treated as the execution system.
- [ ] No Layer, Stage, Entity, Sub-workflow, Roadmap, Goal, or Atom is added as a semantic primitive.
- [ ] No product/project repository mutation occurs from Workflow Governance maintenance patch.

END_OF_FILE: workflow/execution/08_EXECUTION_EVALS.md
