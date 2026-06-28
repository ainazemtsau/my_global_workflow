# NOW — health

active_bet:
  status: none
  note: >
    No active bet after review closed b-health-training-activity-domain-v0-001 as met on
    2026-06-27. Product/process evidence before repair: health-ai c1bf61e for t-1 and
    health-ai 8aa14f8 for t-2; owner release acceptance from t-3: "Запускаем". On
    2026-06-28 the owner supplied a correction showing that 8aa14f8 falsely resolved
    x_training_activity to ACTIVE/DAY_LOOP on sample-only evidence. Bounded product repair
    health-ai 1fe41c2 supersedes that false launch route: training/activity now resolves to
    PROGRAM awaiting Deep Research, blocks proposal/ACTIVE/week/session until a suitable
    research conclusion plus owner approval exists, and keeps first real performed session
    unclaimed.

tasks: []

open_calls: []

recurring:
  - id: r-health-ai-minor-fix-lane
    goal: >
      Keep a lightweight intake lane for minor Health AI UX/contract/prompt
      papercuts that do not justify a full direction bet.
    done_when: >
      Due minor Health AI issues are batched into a bounded repair/executor CALL
      or explicitly deferred/dropped; no raw health diary enters Direction OS.
    cadence: on_demand
    lens: ai-system-data-architecture
    last_done: 2026-06-28
    note: >
      Post-1338a35 bounded work was reconciled into this lane: menu workflow
      structure repair and owner_fact_delta/assumption hardening
      (7cd962a, 83dba88, 77a0ed), followed by fixed-menu/recipe support through
      health-ai 8246cec. On 2026-06-28 the lane handled the training/activity false
      launch-readiness repair in health-ai 1fe41c2: validation.config was re-synced to
      os-engineering-contract.v9, the training checker rejects the old ACTIVE/DAY_LOOP
      sample-launch state, and Health AI now blocks at PROGRAM awaiting Deep Research.
      The lane remains recurring/on-demand, not a second active bet. Authority, safety,
      provider-portability or owner-gate defects escalate to a bounded repair/executor
      CALL; cosmetic papercuts are batched, deferred or dropped.

decisions: []

next: |
  CALL c-health-training-activity-deep-research-child-guide-001
  to: session
  direction: health
  play: guide
  node: g-health-training-activity-system
  recurring: r-health-ai-minor-fix-lane
  goal: |
    A returned Health AI training/activity Deep Research conclusion is available for
    program synthesis.
  context: |
    Direction OS state:
    - live/health/NOW.md
    - live/health/knowledge/health-training-activity-v0-release-boundary.md
    - live/health/history/2026-06-28-s-health-training-activity-runtime-repair-001.md

    Product repo:
    - C:\my_global_workflow_worktrees\health-ai
    - Repair commit: 1fe41c2 Repair training activity launch readiness
    - Health AI cursor now resolves training/activity to PROGRAM / research_request /
      awaiting deep_research.
    - Ready-to-run request:
      x_training_activity/research/current-request.md

    Current product truth:
    - No suitable returned training/activity research conclusion exists.
    - No owner-ready proposed program exists.
    - No ACTIVE training/activity program, current week, today brief, first session route,
      raw body execution claim, or owner approval exists.
    - Direction OS should receive only summary-level outcome/evidence/next CALL, not raw
      training diary or body-execution data.
  boundaries: |
    Do not fabricate Deep Research, citations, owner approval, a proposed program, an ACTIVE
    program, or a first real training/activity session.
    Do not ask the owner to create a Direction OS PROGRAM card or paste a long internal prompt.
    Use the Health AI ready-to-run Markdown request as the owner-facing research request.
    Do not store raw workout/activity/pulse/wearable data, screenshots, native exports, routes,
    sets, reps, loads, detailed session notes, or body-execution telemetry in Direction OS.
  done_when: |
    The owner has the ready-to-run Health AI training/activity Deep Research request and either:
    1. returns a real Deep Research conclusion suitable to commit into Health AI; or
    2. explicitly declines/defers the research, leaving Health AI blocked at PROGRAM awaiting
       research without inventing a program/session.
  return: |
    RESULT with owner outcome, whether a real research conclusion was returned, where it is
    stored or how it should be committed, explicit no-fabrication/raw-data statement, and next
    CALL: Health AI commit/synthesis executor if a conclusion returned, awaiting_decision if
    deferred, or bounded repair if the request is unusable.
  budget: one guide session

END_OF_FILE: live/health/NOW.md
