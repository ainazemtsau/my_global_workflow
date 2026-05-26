# 07 - Real Start Acceptance Tests

Status: active

These are real-start behavior checks for the manually installed ChatGPT Project. They use synthetic prompts only and must not create a live diet/menu for the user.

## Test 1 - Global Strategy First Start

Prompt:

```text
Режим: Global Strategy Chat. Первый запуск.
```

Pass if:

- collects personal strategic data;
- separates user profile from strategy;
- proposes or updates `USER_PROFILE_AND_CONSTRAINTS.yml`;
- creates detailed markdown `DEEP_RESEARCH_REQUEST.md`;
- does not finalize `GLOBAL_NUTRITION_PLAN` before research;
- does not generate menu;
- does not output a generic plan.

## Test 1B - Global Strategy After Research

Prompt:

```text
Режим: Global Strategy Chat. Продолжаем после Deep Research.
```

Pass if:

- preserves `DEEP_RESEARCH_RESULT.md`;
- creates `DEEP_RESEARCH_SYNTHESIS.md`;
- compares major diet, fasting, hydration, and behavior practices;
- creates detailed user-specific `GLOBAL_NUTRITION_PLAN.md`;
- requires user approval before save.

## Test 2 - Weekly Planning Start

Prompt:

```text
Режим: Weekly Planning Chat. Создаём план недели.
```

Pass if:

- creates a one-week plan;
- reads global plan and history if present;
- outputs `WEEKLY_PLAN`;
- gives inputs for Menu Chat and Tracking Chat;
- does not generate concrete menu.

## Test 3 - Menu Chat Start

Prompt:

```text
Режим: Menu Chat. Создаём меню на неделю по WEEKLY_PLAN.
```

Pass if:

- requires `WEEKLY_PLAN`;
- creates concrete menu;
- creates shopping list;
- creates prep plan;
- supports edits for current week.

## Test 4 - Tracking Chat Start

Prompt:

```text
Режим: Tracking Chat. Начинаем неделю по WEEKLY_PLAN и ACTIVE_WEEK_MENU.
```

Pass if:

- requires `WEEKLY_PLAN` and `ACTIVE_WEEK_MENU`;
- tracks food/photos/water/events;
- estimates calories/BJU when required;
- keeps pending questions until answered or declined;
- gives status and advice;
- creates `WEEK_TRACKING_REPORT` at end;
- durable GitHub update default is `false`.

## Test 5 - Week Close

Prompt:

```text
Режим: Weekly Planning Chat. Закрываем неделю по WEEK_TRACKING_REPORT.
```

Pass if:

- reviews `WEEK_TRACKING_REPORT`;
- reports unlogged or unresolved items;
- saves week result/history/progress by proposed save packet only;
- prepares `NEXT_WEEK_INPUTS`;
- closes the week chat.

## Refresh Reproducibility Check

After a Codex save, a fresh chat must continue from refreshed Project Files without hidden memory and without a giant pasted state packet.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/07_REAL_START_ACCEPTANCE_TESTS.md
