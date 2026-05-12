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
  phase_name: "Собрать AI-операционный слой питания без тяжёлого трекинга"
  phase_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer"
  critical_constraint: "Нет устойчивого AI-процесса питания: меню, рецепты, отклонения, дневные коррекции, долгосрочные выводы и сохранение состояния не связаны в один рабочий слой. MacroFactor/detailed tracking создаёт лишний friction, а один длинный ChatGPT-chat со временем деградирует."
  minimum_outcome: "Есть AI Nutrition Operating Layer v0: state packet, active menu object, prompt modes, exception correction, recipe/prep builder, review/state update protocol, storage rules, restart/context refresh rules, and sample flows."
  validation_signal: "Система проходит типовые сценарии: составить/обновить меню, дать совет по текущему дню, скорректировать остаток дня после переедания, добавить рецепт/prep note, сделать day/week summary и обновить persistent state."
```

## Guard state

* Active Goal unresolved: `yes, no active Goal yet; selected seed should be shaped by G1_GOAL_SHAPE`
* Phase can close now: `no`
* Blocker: `First Goal Contract must be shaped before execution`
* Superseded prior Phase: `MacroFactor Nutrition AI Support Setup`
