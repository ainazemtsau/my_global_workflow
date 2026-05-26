# 00_DIRECTION_START_HERE.md

```yaml
project_file_control:
  file: 00_DIRECTION_START_HERE.md
  schema: project_file_projection.v1
  direction: directions/health-and-beauty
  source_files:
    - "directions/health-and-beauty/project_files/00_DIRECTION_START_HERE.md"
  activated_at: "2026-05-12"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

## Current pointers

* Current Phase: `Первый рабочий Health/Body Operator: тренировочный процесс v0` -> `directions/health-and-beauty/phases/first-working-health-body-operator-training-v0`
* Current Phase status: `active`
* Active Goal pointer: `none`
* Active Goal status: `none`
* Latest closed Phase: `ai-nutrition-operating-layer`, status `closed_complete`
* Current focus: shape the first Goal for the new Phase.
* Next route: `G1_GOAL_SHAPE`
* Direction Map link: `n2_first_weekly_body_transformation_correction_loop`
* Direction Map update status: `08_DIRECTION_MAP.md` Active Front remains valid and is intentionally unchanged by P0. Its old route-binding text is stale-but-nonblocking only for the named next stage `G1_GOAL_SHAPE`.

## Operational Boundary Invariant

Workflow builds, repairs, audits, and evolves the operational health/body process. It does not run daily nutrition, training, metric logging, or week-to-week plan management.

Daily operation happens inside the separate Health/Body Operator ChatGPT Project. That operational Project may contain specialist chats for nutrition, training, daily decisions, weekly review/metrics, and local process customization.

The operational Project should not know workflow stages, phase IDs, goal IDs, Direction Map mechanics, or workflow routing. It should behave like a practical operator for the user.

Workflow may know the operational Project structure, source files, protocols, and customization boundaries. Strategic redesign, new tools, major process changes, evidence-heavy decisions, or global dissatisfaction return to the Health and Beauty workflow.

## Active Phase summary

The active Phase creates the first working autonomous training/activity process v0 inside the unified Health/Body Operator Project.

The Phase is not a daily logging workflow. Its validation is capability validation: the operational Project must demonstrate state -> plan -> log-inside-Project -> adjustment.

## Phase Memory Bridge

Latest closed Phase summary remains:
* `directions/health-and-beauty/phases/ai-nutrition-operating-layer/phase_close_summary.md`
* `directions/health-and-beauty/project_files/07_PHASE_MEMORY_INDEX.md`

Do not reopen Project `Питание` setup repair by default. The nutrition loop works enough to continue. Nutrition polish is deferred until concrete friction appears.

## Default Project Files to load

Load these Direction Project Files by default:

1. `00_DIRECTION_START_HERE.md`
2. `01_DIRECTION_STATE.md`
3. `02_CURRENT_PHASE.md`
4. `03_FOCUS_REGISTER.md`
5. `04_ACTIVE_GOAL.md`
6. `05_PORTFOLIO_QUEUE.md`
7. `06_CONTEXT_LIBRARY_INDEX.md`
8. `07_PHASE_MEMORY_INDEX.md`
9. `08_DIRECTION_MAP.md`

Also load shared runtime cache files defined in:

```text
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
```

## Superseded active work

Old Project `Питание` setup routes are historical evidence only. MacroFactor-heavy tracking remains superseded/paused. Standalone metrics/readiness work is not the current Phase.
