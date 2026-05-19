# 02_CURRENT_PHASE.md

```yaml
project_file_control:
  file: 02_CURRENT_PHASE.md
  schema: project_file_projection.v1
  direction: directions/health-and-beauty
  source_files:
    - "directions/health-and-beauty/project_files/02_CURRENT_PHASE.md"
  activated_at: "2026-05-12"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
current_phase:
  state: active
  phase_name: "Собрать удобный, научно обоснованный процесс питания без тяжёлого трекинга"
  phase_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer"
  critical_constraint: "The minimal nutrition loop shape and container policy have been selected and shaped; Project `Питание` v0 package execution/validation has not yet been planned or run."
  minimum_outcome: "A repo-backed standalone Project `Питание` v0 package is created and validated through synthetic dry-runs, or a later stage returns a concrete blocker/repair route."
  validation_signal: "E1 defines the execution envelope; later implementation produces package files and dry-run evidence."
  active_goal_pointer: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0"
  active_goal_title: "Собрать отдельный рабочий ChatGPT Project “Питание” как low-friction nutrition operating system"
  goal_state: goal_shaped_pending_E1
  next_route: E1_EXECUTION_BRIEF
  next_goal_seed: null
  phase_closeable: false
```

## Guard state

* Active Goal unresolved: `yes`
* Active Goal shaped: `yes`
* Phase can close now: `no`
* Current blocker: Execution package and dry-run validation are not yet produced.
* Tooling policy: AI/ChatGPT/Project/app/storage may be tools, not the objective.
* Superseded prior Phase: `MacroFactor Nutrition AI Support Setup`
* Correction note: AI Nutrition Operating Layer v0 is a design/protocol artifact, not proof of operational completion.
