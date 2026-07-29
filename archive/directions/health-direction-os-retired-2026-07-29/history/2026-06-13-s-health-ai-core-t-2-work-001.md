RESULT s-health-ai-core-t-2-work-001 (call: c-health-ai-core-t-2-work-001)
direction: health   play: work   node/task: g-health-ai-core/t-2

outcome: |
  Health AI Core State Skeleton v0 is created at `work/health-ai-core-state-skeleton-v0.md`.

  The skeleton defines:
  - a portable `health-ai/` source-of-truth layout;
  - concrete records and required fields for profile, preferences, metrics summaries,
    active plans, food logs, recipes, training/activity state, feedback, reviews/incidents,
    pending patches, procedures, roles, research briefs, and integration registry;
  - explicit raw-data boundaries for Health AI System vs Direction OS;
  - templates for recipe-card, food-log-entry, weekly-plan, training-output, weekly review,
    incident, and pending patch;
  - guidance/governance records for strategy, current phase, next actions, and investigations,
    based on the owner-accepted correction that the system must guide the process, not only
    answer data-manipulation requests.

evidence: |
  Artifact:
  - `work/health-ai-core-state-skeleton-v0.md`

  Done_when mapping:
  - Concrete files/records and required fields: sections 2, 4, and 5.
  - Records that may contain operational raw data inside Health AI System:
    sections 3 and 4, especially food logs, session logs, feedback, and incident boundaries.
  - Direction OS receives only strategic summary/problem/decision/CALL:
    sections 3 and 8.
  - Templates included:
    section 6 includes recipe-card, food-log-entry, weekly-plan, training-output,
    weekly review, incident, and pending patch templates.
  - Integration-neutral:
    sections 2, 3, 4.26, and 10 keep repo/app/tool choices unselected.

state_changes: |
  work/:
  - Add `work/health-ai-core-state-skeleton-v0.md`.

  NOW.md:
  - In tasks, set `t-2.status` from `open` to `done`.
  - Add `t-2.evidence`:
      - `work/health-ai-core-state-skeleton-v0.md`
      - `session s-health-ai-core-t-2-work-001 incorporated owner-accepted guidance/governance contour`
  - Set `next` to CALL `c-health-ai-core-t-3-guide-001`.

  LOG.md:
  - Append log line:
      - 2026-06-13 — health/g-health-ai-core/t-2 work: Health AI Core State Skeleton v0 created with records, raw-data boundaries, templates, procedure registry, roles, guidance/governance contour, and Direction OS bridge; next t-3 validation. → history/2026-06-13-s-health-ai-core-t-2-work-001.md

captures:
  - Future Health AI Core contract revision should explicitly promote guidance/governance from an implied loop to a first-class loop.

decisions_needed: []

play_check:
  - 1 Recite: done. Active bet `g-health-ai-core` and task `t-2` matched NOW; done_when restated from the CALL and task.
  - 2 Owner inputs (owner): done. Artifact is owner-content; used prior state plus live owner acceptance that Health AI Core needs a guidance/governance contour, next-best-step behavior, bounded investigations, and one-chat-one-job child work.
  - 3 Do the work: done. Created `work/health-ai-core-state-skeleton-v0.md`; no app, integration, database, diet program, or training program was selected.
  - 4 Self-check: done. Skeleton maps to every t-2 done_when item and includes the accepted guidance/governance correction without storing raw daily data in Direction OS.
  - 5 Close: done. RESULT saved with exact state_changes, log line, capture, and next CALL for `t-3`.

log: "work t-2: Health AI Core State Skeleton v0 created; records/raw-data boundaries/templates/procedures/roles/guidance contour covered; next t-3 validation."

next: |
  CALL c-health-ai-core-t-3-guide-001
  to: session
  direction: health
  play: guide
  node: g-health-ai-core
  task: t-3
  goal: |
    Health AI Core Contract and State Skeleton are validated against the five core flows;
    a compact validation summary exists for Direction OS.
  context: |
    Read live/health/CHARTER.md, live/health/TREE.md, live/health/NOW.md,
    work/health-ai-core-contract-v0.md,
    work/health-ai-core-state-skeleton-v0.md,
    live/health/history/2026-06-13-s-health-ai-core-t-1-work-001.md,
    live/health/history/2026-06-13-s-health-ai-core-t-2-work-001.md,
    live/health/history/2026-06-13-s-health-starter-kit-t-2-guide-003.md,
    and live/health/history/2026-06-13-s-health-ai-core-shape-001-approval.md.

    t-1 produced the contract. t-2 produced the state skeleton. The owner accepted
    the correction that Health AI Core must include a guidance/governance contour:
    it should guide next best actions, run bounded investigations, adapt plans,
    and feel like a health team while keeping one chat = one job internally.

    Validate with synthetic/minimal seed data only. Direction OS must receive only
    compact validation summary/problems/decisions/CALLs, not raw daily data.
  boundaries: |
    Do not build an app or implementation.
    Do not choose Hevy/Strava-like/wearable/VR/recipe-manager integrations.
    Do not create a long-term detailed diet or full progressive training program.
    Do not store daily raw health data in Direction OS.
    Do not ask for raw logs.
    Do not make medical prescriptions.
    Do not polish or revive work/health-starter-kit-v0.md.
    Do not change the contract or skeleton except to record blockers/contradictions.
  done_when: |
    Compact validation summary is ready and:
    - Flow 1 tested: no weekly plan exists → system guides plan creation.
    - Flow 2 tested: today's menu requested → system answers from plan/preferences or marks missing plan.
    - Flow 3 tested: food log with skipped follow-ups → system saves available data with confidence and gives same-day advice.
    - Flow 4 tested: today's training requested → system answers from current plan/safety state or marks missing plan.
    - Flow 5 tested: review/incident → system compresses summary and Direction OS escalation.
    - Validation checks the accepted guidance/governance contour by testing "what should I do next?"
      or a problem-investigation path.
    - Validation identifies blockers or confirms the slice is usable enough for next nutrition/training-system shaping.
  return: |
    RESULT with compact validation summary, evidence mapped to done_when, no raw daily logs,
    and next CALL for review because this is the last open task of the active bet.
  budget: one guide session
  surface: chatgpt

END_OF_FILE: live/health/history/2026-06-13-s-health-ai-core-t-2-work-001.md
