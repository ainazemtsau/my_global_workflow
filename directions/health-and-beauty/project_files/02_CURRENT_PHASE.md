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
  critical_constraint: "Нет устойчивого, низкофрикционного процесса питания: форма цикла, минимальные входные данные, правила коррекции, хранение состояния и контейнер выполнения ещё не выбраны после Objective Architecture correction."
  minimum_outcome: "Принято решение о минимальном nutrition loop shape и tool/container policy: что ведём, где ведём, как обновляем состояние, какая роль у AI/ChatGPT/Project/app/storage, и какой следующий Goal можно безопасно сформировать или repaired."
  validation_signal: "S3_DECIDE выбирает basis-valid route: сохранить, починить, уменьшить или заменить Project `Питание` setup path; только после этого возможна новая/исправленная Goal shape и execution planning."
  active_goal_pointer: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0"
  active_goal_title: "Собрать отдельный рабочий ChatGPT Project “Питание” как low-friction nutrition operating system"
  goal_state: blocked_stale_not_basis_valid_pending_decision
  next_route: S3_DECIDE
  next_goal_seed: null
  phase_closeable: false
```

## Guard state

* Active Goal unresolved: `yes`
* Active Goal shaped: `yes`
* Phase can close now: `no`
* Current blocker: the stale Project `Питание` E1 route is not basis-valid after user correction; S3 must decide the minimal nutrition loop shape and tool/container policy first.
* Tooling policy: AI/ChatGPT/Project/app/storage may be tools, not the objective.
* Superseded prior Phase: `MacroFactor Nutrition AI Support Setup`
* Correction note: AI Nutrition Operating Layer v0 is a design/protocol artifact, not proof of operational completion.
