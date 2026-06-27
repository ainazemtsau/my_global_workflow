# NOW — health

active_bet:
  status: none
  note: >
    No active bet after review closed b-health-training-activity-domain-v0-001 as met on
    2026-06-27. Product/process evidence: health-ai c1bf61e for t-1 and health-ai 8aa14f8 for
    t-2; owner release acceptance from t-3: "Запускаем". First real performed training/activity
    session is not claimed done and is routed next through Health AI.

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
    last_done: 2026-06-24
    note: >
      Post-1338a35 bounded work was reconciled into this lane: menu workflow
      structure repair and owner_fact_delta/assumption hardening
      (7cd962a, 83dba88, 77a0ed), followed by fixed-menu/recipe support through
      health-ai 8246cec. The lane remains recurring/on-demand, not a second
      active bet. Authority, safety, provider-portability or owner-gate defects
      escalate to a bounded repair/executor CALL; cosmetic papercuts are
      batched, deferred or dropped.

decisions: []

next: |
  CALL c-health-training-activity-first-real-session-001
  to: session
  direction: health
  play: guide
  node: g-health-training-activity-system
  goal: |
    Owner performs the first real training/activity session through Health AI, and Health AI
    records only normalized coarse training LOG/review state while Direction OS receives only
    strategic summary/problem/decision/next CALL.
  context: |
    Direction OS state:
    - live/health/NOW.md
    - live/health/TREE.md
    - live/health/history/2026-06-27-s-health-training-activity-domain-v0-review-001.md
    - live/health/knowledge/health-training-activity-v0-release-boundary.md

    Closed bet:
    - b-health-training-activity-domain-v0-001 reviewed as met on 2026-06-27.
    - g-health-training-activity-system is done at product/process level.
    - Owner accepted launch in t-3 with: "Запускаем".
    - Acceptance means personal Health AI use, not an artificial acceptance-test ritual and
      not proof that a real session already happened.

    Product repo:
    - ainazemtsau/health-ai
    - t-1 accepted for continuation at c1bf61e.
    - t-2 operational contour committed at 8aa14f8.
      Add training activity operational contour.

    Health AI evidence/operation pointers:
    - x_training_activity/programs/active-program.md
    - x_training_activity/weeks/current-week.md
    - x_training_activity/briefs/what-today.md
    - x_training_activity/logs/YYYY-MM-DD.md
    - x_training_activity/procedures/day-loop.md
    - x_training_activity/procedures/review.md
    - x_training_activity/procedures/mutation.md
    - x_training_activity/handoffs/training-to-nutrition-demand-context.md
    - acceptance/x_training_activity/thin-slice-evidence-summary.md

    Required operating meaning:
    - Open Health AI.
    - Use the ACTIVE training/activity authority to derive current-week and what-today.
    - Owner performs the first real training/activity session personally if the safety route
      remains clear.
    - Health AI captures only normalized coarse result signals:
      completion category, whether the brief was followed, coarse effort/recovery, pain/safety
      change, substitution/deviation if material, and review-needed flag.
    - Direction OS receives only strategic summary/problem/decision/next CALL if a later OS
      session is needed.
  boundaries: |
    Do not store raw training logs, screenshots, media, native exports, telemetry, wearable data,
    detailed session notes, sets, reps, loads, route maps, pulse streams, or body-execution
    records in Direction OS.

    Do not claim the first real performed training/activity session is done before the owner
    actually performs it.

    Do not represent setup/sample/import evidence as body-proven evidence.

    Do not ask the owner to manually maintain Direction OS as a training diary.

    Do not edit Health AI product internals unless the guide discovers a bounded product defect
    and returns a separate repair/executor CALL.

    If pain, red flags, unsafe symptoms, medical uncertainty or safety-brake conditions appear,
    stop/shorten according to Health AI safety rules and report only a strategic safety/problem
    summary to Direction OS.
  done_when: |
    One of the following is true:

    A. First real training/activity session was performed through Health AI:
       - Health AI produced/updated the normalized coarse training LOG/review state.
       - Direction OS receives only strategic summary, evidence pointer, safety/recovery
         disposition, and next CALL if needed.
       - No raw session details or telemetry enter Direction OS.

    B. Session was not performed because the safety/recovery/medical/friction route blocked it:
       - Health AI records the appropriate coarse blocked/reduced/BRAKE/review state.
       - Direction OS receives only strategic problem summary and a bounded repair/decision CALL
         if needed.
       - No raw session details or telemetry enter Direction OS.
  return: |
    RESULT with:
    - first real session verdict: performed | reduced/blocked | repair_needed;
    - Health AI evidence pointer only, not raw data;
    - coarse strategic summary of completion/safety/recovery/review-needed status;
    - explicit raw-data boundary statement;
    - state_changes for NOW/LOG/history only;
    - next CALL: continue personal Health AI use, bounded repair, or strategic review.
  budget: one guide session

END_OF_FILE: live/health/NOW.md
