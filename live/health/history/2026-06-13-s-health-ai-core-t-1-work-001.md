RESULT s-health-ai-core-t-1-work-001 (call: c-health-ai-core-t-1-work-001)
direction: health   play: work   node/task: g-health-ai-core/t-1

outcome: |
  Health AI Core Contract v0 is created at `work/health-ai-core-contract-v0.md`.

  The contract defines:
  - Direction OS vs Health AI System vs future integration boundaries;
  - a minimal operational state model;
  - the new-chat operating protocol;
  - planning, menu, training, food-log, recipe, and review loops;
  - explicit non-goals and cut list;
  - five dry-run scenarios for cross-chat continuation and missing-state behavior.

evidence: |
  Artifact:
  - `work/health-ai-core-contract-v0.md`

  Done_when mapping:
  - Source-of-truth boundaries: sections 2 and 6.
  - Minimal state model: section 3.
  - New-chat operating protocol: section 4.
  - Planning/menu/training/food-log/recipe/review loops: section 5.
  - Explicit non-goals and cut list: section 7.
  - Five dry-run scenarios: section 8.
  - No integration choices, implementation, raw-log request, or raw daily Direction OS storage:
    sections 2, 4, 6, 7, and 8.

state_changes: |
  work/:
  - Add `work/health-ai-core-contract-v0.md`.

  NOW.md:
  - In tasks, set `t-1.status` from `open` to `done`.
  - Add `t-1.evidence`:
      - `work/health-ai-core-contract-v0.md`
      - `session s-health-ai-core-t-1-work-001 self-check matched every t-1 done_when item`
  - Set `next` to CALL `c-health-ai-core-t-2-work-001`.

  LOG.md:
  - Append log line:
      - 2026-06-13 — health/g-health-ai-core/t-1 work: Health AI Core Contract v0 created with boundaries, state model, chat protocol, loops, non-goals, and five dry-runs; next t-2 state skeleton. → history/2026-06-13-s-health-ai-core-t-1-work-001.md

captures: []

decisions_needed: []

play_check:
  - 1 Recite: done. Active bet `g-health-ai-core` and task `t-1` matched NOW; done_when restated from the CALL and task.
  - 2 Owner inputs (owner): done. Artifact is owner-content; reused recorded owner inputs including "меню на сегодня", "тренировки на сегодня", "источник ... это GitHub", "он должен на имеющихся данных сохранить данные", and "совет на дальнейший день"; no new owner-only question was needed.
  - 3 Do the work: done. Created `work/health-ai-core-contract-v0.md` and did not revive `work/health-starter-kit-v0.md`.
  - 4 Self-check: done. Contract sections map to every t-1 done_when item; no raw daily data is stored in Direction OS.
  - 5 Close: done. RESULT saved with exact state_changes, log line, and next CALL for `t-2`.

log: "work t-1: Health AI Core Contract v0 created; boundaries/state model/chat protocol/loops/non-goals/five dry-runs covered; next t-2 state skeleton."

next: |
  CALL c-health-ai-core-t-2-work-001
  to: session
  direction: health
  play: work
  node: g-health-ai-core
  task: t-2
  goal: |
    Produce work/health-ai-core-state-skeleton-v0.md: a minimal source-of-truth skeleton
    for profile, preferences, metrics summaries, active plans, food logs, recipes,
    training/activity state, feedback, reviews/incidents, and pending patches.
  context: |
    Read live/health/CHARTER.md, live/health/TREE.md, live/health/NOW.md,
    work/health-ai-core-contract-v0.md,
    live/health/history/2026-06-13-s-health-ai-core-t-1-work-001.md,
    live/health/history/2026-06-13-s-health-starter-kit-t-2-guide-003.md,
    and live/health/history/2026-06-13-s-health-ai-core-shape-001-approval.md.

    t-1 produced the minimal Health AI Core Contract. The contract fixes the boundaries:
    Direction OS is strategic only; Health AI System is the operational source of truth;
    future integrations are optional and unchosen; AI chats propose patches instead of
    silently overwriting state.

    The skeleton should instantiate the contract's record families:
    profile, preferences, metrics summaries, active plans, food logs, recipes,
    training/activity state, feedback, reviews/incidents, and pending patches.
  boundaries: |
    Do not build an app.
    Do not choose Hevy/Strava-like/wearable/VR/recipe-manager integrations.
    Do not create a long-term detailed diet or full progressive training program.
    Do not store daily raw health data in Direction OS.
    Do not ask for raw logs.
    Do not make medical prescriptions.
    Do not polish or revive work/health-starter-kit-v0.md.
    Do not change the contract except to note a blocker or contradiction.
  done_when: |
    work/health-ai-core-state-skeleton-v0.md content is ready for writer application and:
    - lists concrete files/records and required fields;
    - states which records may contain operational raw data inside Health AI System;
    - states that Direction OS receives only strategic summary/problem/decision/CALL output;
    - includes recipe-card, food-log-entry, weekly-plan, training-output, and review/incident templates;
    - remains integration-neutral.
  return: |
    RESULT with artifact content or exact work/ file addition, evidence mapped to done_when,
    no raw daily logs, and next CALL for t-3.
  budget: one work session
  surface: chatgpt

END_OF_FILE: live/health/history/2026-06-13-s-health-ai-core-t-1-work-001.md
