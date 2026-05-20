# 00 - Nutrition Start Here

Status: active runtime router

Read this file first in every fresh Project `Питание` chat.

## Non-Negotiables

- Use one explicit chat mode at a time.
- GitHub files are durable state.
- Project Files are a refreshable runtime cache.
- Chat memory is non-authoritative.
- No hidden memory as state.
- No giant user prompt as normal UX.
- No live clinical protocol.
- No default heavy macro/calorie ledger.

## Mode Router

If the user provides:

```text
Режим: Global Strategy Chat. Первый запуск.
```

open `01_GLOBAL_STRATEGY_CHAT_PROTOCOL.md`.

If the user provides:

```text
Режим: Global Strategy Chat. Продолжаем после Deep Research.
```

open `01_GLOBAL_STRATEGY_CHAT_PROTOCOL.md`.

If the user provides:

```text
Режим: Weekly Planning Chat. Создаём план недели.
```

open `02_WEEKLY_PLANNING_CHAT_PROTOCOL.md` and create one-week `WEEKLY_PLAN`.

If the user provides:

```text
Режим: Menu Chat. Создаём меню на неделю по WEEKLY_PLAN.
```

open `03_MENU_CHAT_PROTOCOL.md`. Require `WEEKLY_PLAN`.

If the user provides:

```text
Режим: Tracking Chat. Начинаем неделю по WEEKLY_PLAN и ACTIVE_WEEK_MENU.
```

open `04_TRACKING_CHAT_PROTOCOL.md`. Require `WEEKLY_PLAN` and `ACTIVE_WEEK_MENU`.

If the user provides:

```text
Режим: Weekly Planning Chat. Закрываем неделю по WEEK_TRACKING_REPORT.
```

open `02_WEEKLY_PLANNING_CHAT_PROTOCOL.md` and run week close from `WEEK_TRACKING_REPORT`.

If no mode is clear, ask for mode selection. Do not infer one all-purpose chat.

## Required State Map

```yaml
global_strategy:
  profile: state/USER_PROFILE_AND_CONSTRAINTS.yml
  legacy_profile_md: state/USER_PROFILE_AND_CONSTRAINTS.md
  legacy_profile_md_policy: compatibility_only_if_present
  research_request: research/DEEP_RESEARCH_REQUEST.md
  research_result: research/DEEP_RESEARCH_RESULT.md
  research_synthesis: research/DEEP_RESEARCH_SYNTHESIS.md
  global_plan: state/GLOBAL_NUTRITION_PLAN.md
  first_setup_status: pending_profile_and_DEEP_RESEARCH_REQUEST
profile:
  file: state/USER_PROFILE_AND_CONSTRAINTS.yml
history:
  file: state/NUTRITION_HISTORY.md
metrics:
  file: state/PROGRESS_METRICS.md
active_week:
  pointer: weeks/ACTIVE_WEEK_POINTER.md
  plan: weeks/current/WEEKLY_PLAN.md
  menu: weeks/current/ACTIVE_WEEK_MENU.md
  tracking_report: weeks/current/WEEK_TRACKING_REPORT.md
  review: weeks/current/WEEK_REVIEW.md
  next_inputs: weeks/current/NEXT_WEEK_INPUTS.md
```

Global Strategy Chat must keep profile facts, research request, research result, research synthesis, and final approved plan as separate artifacts. Do not substitute `state/USER_PROFILE_AND_CONSTRAINTS.md` for the canonical `.yml` profile except as legacy compatibility input.

## Missing State Rule

If required state is missing:

1. Name the exact missing file.
2. If the file should already exist in GitHub, ask for Project Files refresh from GitHub and list exactly that file.
3. If the file must be created, ask for the minimum input needed to create only that file and propose a save packet for that exact path.
4. For Global Strategy missing files, use these exact targets: `state/USER_PROFILE_AND_CONSTRAINTS.yml`, `research/DEEP_RESEARCH_REQUEST.md`, `research/DEEP_RESEARCH_RESULT.md`, `research/DEEP_RESEARCH_SYNTHESIS.md`, and `state/GLOBAL_NUTRITION_PLAN.md`.
5. Do not reconstruct missing state from chat memory.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/00_NUTRITION_START_HERE.md
