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
  critical_constraint: "R1 accepted the repaired nutrition loop Goal complete; P9_PHASE_CLOSE must decide whether the Phase closes, pauses, or carries forward optional expansion after repository read-back and Project Files refresh."
  minimum_outcome: "One complete repo-backed low-friction weekly nutrition loop can continue across fresh chats through GitHub markdown state, Project Files refresh, and Codex save boundaries."
  validation_signal: "R1 accepted the Project `Питание` repo-backed multi-chat nutrition loop as complete; P9_PHASE_CLOSE must review whether the Phase closes, pauses, or carries forward optional expansion."
  active_goal_pointer: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0"
  active_goal_title: "Собрать отдельный рабочий ChatGPT Project “Питание” как low-friction nutrition operating system"
  goal_state: r1_accepted_goal_complete
  next_route: P9_PHASE_CLOSE
  next_goal_seed: null
  phase_closeable: true
```

## Guard state

* Active Goal unresolved: `no`
* Active Goal shaped: `yes`
* Phase can close now: `yes, pending P9_PHASE_CLOSE`
* Current blocker: repository projection/read-back and manual Project Files refresh before next material stage
* Tooling policy: AI/ChatGPT/Project/app/storage may be tools, not the objective.
* Superseded prior Phase: `MacroFactor Nutrition AI Support Setup`
* Correction note: R1 accepted the repo-backed multi-chat Project `Питание` nutrition loop as complete for this Goal based on U1/setup/real-use validation.
