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
  critical_constraint: "Repaired nutrition loop shape is now selected; execution planning must define files, save boundaries, Project Files refresh, and dry-run validation."
  minimum_outcome: "One complete repo-backed low-friction weekly nutrition loop can continue across fresh chats through GitHub markdown state, Project Files refresh, and Codex save boundaries."
  validation_signal: "E1_EXECUTION_BRIEF produces minimum HOW, validation map, and repository maintenance route for the repaired repo-backed Project `Питание` loop."
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
* Current blocker: Execution planning has not yet defined exact files, save boundaries, Project Files refresh, and dry-run validation.
* Tooling policy: AI/ChatGPT/Project/app/storage may be tools, not the objective.
* Superseded prior Phase: `MacroFactor Nutrition AI Support Setup`
* Correction note: AI Nutrition Operating Layer v0 is a design/protocol artifact, not proof of operational completion.
