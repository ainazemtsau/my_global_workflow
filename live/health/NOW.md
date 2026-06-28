# NOW — health

active_bet:
  status: none
  note: |
    No active bet after the training/activity v0 product/process work and its 2026-06-28 repair.
    Product/process evidence before repair: health-ai c1bf61e for t-1 and health-ai 8aa14f8 for t-2;
    owner release acceptance from t-3: "Запускаем". On 2026-06-28 the owner supplied a correction
    showing that 8aa14f8 falsely resolved x_training_activity to ACTIVE/DAY_LOOP on sample-only
    evidence. Bounded product repair health-ai 1fe41c2 supersedes that false launch route:
    training/activity now resolves to PROGRAM awaiting Deep Research, blocks proposal/ACTIVE/week/
    session until a suitable returned research conclusion plus owner approval exists, and keeps
    first real performed session unclaimed.

    Owner reported on 2026-06-28 that the Health AI research/check phase appears started. No returned
    research conclusion has been received in Direction OS yet, so no program synthesis, ACTIVE program,
    current week, today brief, first session route, or body-execution claim is allowed.

tasks: []

open_calls:
  - id: c-health-training-activity-deep-research-child-001
    to: research
    direction: health
    node: g-health-training-activity-system
    recurring: r-health-ai-minor-fix-lane
    status: in_flight_owner_reported_started
    started_at: 2026-06-28
    goal: |
      Return a suitable Health AI training/activity Deep Research conclusion for first personal
      program synthesis.
    context: |
      Health AI product state:
      - health-ai 1fe41c2 Repair training activity launch readiness
      - x_training_activity/runtime/cursor.md: PROGRAM / research_request / awaiting deep_research
      - x_training_activity/research/index.md: awaiting_deep_research; no current suitable conclusion
      - x_training_activity/research/current-request.md: owner-ready Markdown request
    boundaries: |
      Do not create a Health AI program, week plan, today brief, ACTIVE authority, or first session.
      Do not fabricate citations or owner approval.
      Do not store raw workout/activity/pulse/wearable data, screenshots, native exports, routes,
      sets, reps, loads, detailed session notes, or body-execution telemetry in Direction OS.
    done_when: |
      A real returned research conclusion exists with enough citations/source references and scope
      coverage for Health AI to synthesize a proposed training/activity program, or the owner explicitly
      cancels/defers the research.
    return: |
      Research conclusion text/artifact, source/citation basis, scope limits, missing owner facts, and
      whether it is suitable for Health AI program synthesis.
    budget: one Deep Research run / owner-operated external research step

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
  CALL c-health-training-activity-research-return-intake-001
  to: session
  direction: health
  play: guide
  node: g-health-training-activity-system
  recurring: r-health-ai-minor-fix-lane
  goal: |
    Intake the returned Health AI training/activity Deep Research conclusion and route the next
    product step without fabricating a program or training session.
  context: |
    Direction OS state:
    - live/health/NOW.md
    - live/health/TREE.md
    - live/health/LOG.md
    - live/health/knowledge/health-training-activity-v0-release-boundary.md
    - live/health/history/2026-06-28-s-health-training-activity-runtime-repair-001.md
    - live/health/history/2026-06-28-s-health-training-activity-state-validation-001.md

    Product repo:
    - C:\my_global_workflow_worktrees\health-ai
    - Repair commit: 1fe41c2 Repair training activity launch readiness
    - Health AI cursor resolves training/activity to PROGRAM / research_request / awaiting deep_research.
    - Ready-to-run request: x_training_activity/research/current-request.md

    Current truth:
    - Owner reported the research/check phase has started.
    - No returned conclusion has been supplied to Direction OS yet.
    - No owner-ready proposed program exists.
    - No ACTIVE training/activity program, current week, today brief, first session route, raw body execution claim, or owner approval exists.
    - Direction OS receives only summary-level outcome/evidence/next CALL, not raw training diary/body-execution data.
  boundaries: |
    Do not fabricate Deep Research, citations, owner approval, a proposed program, an ACTIVE
    program, current week, today brief, first session, or body-execution evidence.
    Do not ask the owner to create a Direction OS PROGRAM card or paste a long internal prompt.
    If a returned conclusion is supplied, route to a bounded Health AI product executor to commit it and
    synthesize a proposed program; do not activate the program without owner approval.
  done_when: |
    Either:
    1. a real returned training/activity research conclusion is received and a next executor CALL is ready
       to commit it into Health AI and synthesize a proposed program; or
    2. the research is cancelled/deferred and Health AI remains blocked at PROGRAM awaiting research.
  return: |
    RESULT with whether a real conclusion was returned, exact artifact/status, no-fabrication/raw-data
    statement, state_changes for NOW/LOG/history/open_calls, and next CALL to commit/synthesize or await.
  budget: one guide session

END_OF_FILE: live/health/NOW.md
