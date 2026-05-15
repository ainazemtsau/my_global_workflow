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

* Current Phase: `Собрать AI-операционный слой питания без тяжёлого трекинга` -> `directions/health-and-beauty/phases/ai-nutrition-operating-layer`
* Active Goal: `Собрать AI Nutrition Operating Layer v0` -> `directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0`
* Current focus: prepare the E1 Execution Brief for the AI Nutrition Operating Layer v0 Goal.
* Next route: `E1_EXECUTION_BRIEF`
* Direction Map: initial `08_DIRECTION_MAP.md` stub / needs M0 review before relying on it for strategic Phase/Goal selection.

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

If `08_DIRECTION_MAP.md` is uninitialized or marked `needs_m0_review`, run `M0_DIRECTION_MAP` to migrate/build the map from current `00-07` progress and user-provided initiative context before relying on it for strategic Phase/Goal selection.

## Shared runtime file

* `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`

Do not create or require a local runtime-core copy under this Direction `project_files/` folder.

## Superseded active work

The prior Phase `MacroFactor Nutrition AI Support Setup` is superseded/paused, not completed. Its Goal files remain historical evidence and must not be executed as current work without explicit reshaping.
