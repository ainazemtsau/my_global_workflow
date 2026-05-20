# 00 - Nutrition Start Here

Status: active runtime router

Read this file first in every fresh Project `Питание` chat.

## Non-Negotiables

- Use one explicit chat mode at a time.
- GitHub markdown files are durable state.
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
  file: state/GLOBAL_NUTRITION_PLAN.md
  first_setup_status: pending_DEEP_RESEARCH_REQUEST
profile:
  file: state/USER_PROFILE_AND_CONSTRAINTS.md
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

## Missing State Rule

If required state is missing:

1. Name the exact missing file.
2. Ask for Project Files refresh from GitHub or for the minimum input needed to create only that file.
3. Do not reconstruct missing state from chat memory.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/00_NUTRITION_START_HERE.md
