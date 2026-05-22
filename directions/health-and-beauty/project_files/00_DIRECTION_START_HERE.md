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

* Current Phase: `Собрать удобный, научно обоснованный процесс питания без тяжёлого трекинга` -> `directions/health-and-beauty/phases/ai-nutrition-operating-layer`
* Current Phase status: `closed_complete`
* Active Goal pointer: `none`
* Active Goal status: `none`; latest completed Goal `nutrition-project-operational-setup-v0` is closed under the closed Phase.
* Current focus: post-phase-close Project Files refresh, then launch `P0_PHASE_START` in a new Health and Beauty workflow chat.
* Next route: `P0_PHASE_START`
* Direction Map: `08_DIRECTION_MAP.md` is the current routing authority after Objective Architecture migration; use verified GitHub read-back over stale Project Files cache.

## Stale-state correction

P9 2026-05-22 closed the AI Nutrition Operating Layer Phase as `closed_complete` after R1 accepted the repo-backed multi-chat Project `Питание` nutrition loop as complete for this Goal based on U1/setup/real-use validation.

Do not execute old E1/U1/R1 Project `Питание` setup routes. The next material route is `P0_PHASE_START` after this repository maintenance/read-back and manual Project Files refresh.

## Phase Memory Bridge

Use these files before proposing the next Phase:

* Phase close summary: `directions/health-and-beauty/phases/ai-nutrition-operating-layer/phase_close_summary.md`
* Phase memory index: `07_PHASE_MEMORY_INDEX.md`

The next Phase should not repeat Project `Питание` setup repair. The candidate frontier for P0 is `n2_minimal_body_metrics_packet`.

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

If `08_DIRECTION_MAP.md` conflicts with these corrected runtime files, rely on verified GitHub read-back and return Context Request rather than inferring a downstream route.

## Shared runtime file

* `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`

Do not create or require a local runtime-core copy under this Direction `project_files/` folder.

## Superseded active work

The prior Phase `MacroFactor Nutrition AI Support Setup` is superseded/paused, not completed. Its Goal files remain historical evidence and must not be executed as current work without explicit reshaping.
