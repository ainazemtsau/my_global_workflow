# 06 - Chat Launchers and Output Formats

Status: active

Use these launchers exactly enough to select the correct mode. Do not paste giant runtime packets as normal UX.

## Global Strategy First Start

```text
Режим: Global Strategy Chat. Первый запуск.
```

Expected output:

- strategic intake;
- proposed `USER_PROFILE_AND_CONSTRAINTS.yml`;
- proposed `DEEP_RESEARCH_REQUEST.md`;
- no final plan before research.

## Global Strategy After Research

```text
Режим: Global Strategy Chat. Продолжаем после Deep Research.
```

Expected output:

- proposed `DEEP_RESEARCH_RESULT.md`;
- `DEEP_RESEARCH_SYNTHESIS.md`;
- proposed `GLOBAL_NUTRITION_PLAN.md`;
- user approval request before save.

## Weekly Planning Start

```text
Режим: Weekly Planning Chat. Создаём план недели.
```

Expected output: one `WEEKLY_PLAN` and inputs for Menu Chat and Tracking Chat, not concrete menu.

## Menu Chat Start

```text
Режим: Menu Chat. Создаём меню на неделю по WEEKLY_PLAN.
```

Expected output: `ACTIVE_WEEK_MENU`, shopping list, prep plan, and current-week edit policy.

## Tracking Chat Start

```text
Режим: Tracking Chat. Начинаем неделю по WEEKLY_PLAN и ACTIVE_WEEK_MENU.
```

Expected output: food/photo/water/event tracking, status, advice, pending questions, and later `WEEK_TRACKING_REPORT`.

## Week Close

```text
Режим: Weekly Planning Chat. Закрываем неделю по WEEK_TRACKING_REPORT.
```

Expected output: `WEEK_REVIEW`, unresolved item report, history/progress save packet, `NEXT_WEEK_INPUTS`, and close instruction.

## Save Handoff Format

Use the save packet in `05_STATE_SAVE_AND_REFRESH_PROTOCOL.md`. Never claim external save without Codex read-back/diff evidence.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/06_CHAT_LAUNCHERS_AND_OUTPUT_FORMATS.md
