# NOW — health

active_bet:
  id: b-health-training-activity-domain-v0-001
  node: g-health-training-activity-system
  status: active
  appetite: 7 calendar days
  started: 2026-06-26
  kill_by: >
    2026-07-03. Dies/reviews if any of the following hold:
    (a) no owner-approved thin-but-functional training/activity v0 exists by the date;
    (b) implementation requires a second router/lifecycle/gate/writer/job model, server,
        database, scheduler, background worker, or kernel/nutrition rewrite;
    (c) raw workout/activity/pulse/wearable data, screenshots, native exports or daily
        session logs are persisted into Direction OS;
    (d) setup/sample evidence is represented as real body-execution evidence;
    (e) W1-W20 or TA-CA1..TA-CA12 are weakened, or P1-P12 HOW decisions leak into
        Direction OS done_when;
    (f) the first body-execution route is not preserved.
    next_if_true: >
      Open the body-execution CALL: owner performs the first real training/activity session;
      the result reaches Health AI normalized LOG with safety/recovery feedback and next
      adjustment/review state. Direction OS receives only strategic summary/evidence pointer/next CALL.
    next_if_false: >
      Review without extension: either repair the proven contract seam, shrink to a smaller product
      contour, or cut to a manual body-first route while preserving the signed WHAT.
  forecast: >
    Likely enough for a basic training domain contour because core/kernel/nutrition are already in
    place and converge-verify passed, but scope is guarded against API integrations, shared body
    measurements, dashboards, full guided-coach polish, and full WA-K8 acceptance breadth.
  against: >
    The main risk is ambiguity/breadth creep: "program" or "guided route" could expand into
    hardcoded research templates, full integrations, body-measurement redesign, or a second engine.
    t-1 tests the thin-domain/no-hardcode/evidence-backed-program seam first.

tasks:
  - id: t-1
    status: active
    kind: executor
    repo: ainazemtsau/health-ai
    goal: >
      Training/activity has thin-domain authority, evidence-backed dynamic program creation,
      current-week slicing, and today's session brief path over the existing Health AI kernel.
    done_when: >
      Product evidence shows:
      1. Training/activity attaches as a thin domain over the existing kernel: namespaced data,
         one registry-line control-plane attach, one state-machine instance, one cursor instance,
         one bounded procedure per term/stage as needed, zero duplicated router/lifecycle/gate/
         writer/job model/scheduler/server/database/background worker.
      2. Health AI can create a training/activity program proposal from current owner/core facts
         and current external evidence. It does not use a hardcoded research template, fixed question
         script, fixed program template, fixed schedule, split, volume, intensity, vendor, or intake
         form. The system determines what evidence/deep-research pass is required for the artifact
         being created; for the training program this must include current evidence sufficient to
         justify the plan for the owner's profile, goals, constraints, safety, adherence, equipment
         and phase.
      3. Setup asks dynamically only for materially missing irreducible owner facts; it may ask
         freely when useful but does not block on nonessential answers, records defaults/assumptions
         as revisable where allowed, and never asks the owner to design expert variables. Exercise
         selection, split, volume, intensity, conditioning mix, progression, regression and deload
         logic are system-decided from evidence + owner profile + current phase + constraints + feedback.
      4. The proposed training authority can ride the existing SEED/PROPOSED/ACTIVE gate and is
         readable for owner approval; it records evidence/rationale, owner facts used, defaults/
         assumptions, safety constraints and extension points for arbitrary schedules, constraints,
         equipment, preferences and other material nuances.
      5. From ACTIVE authority, Health AI can generate a current-week training/activity slice and a
         readable "what today?" session brief for contexts such as home/gym/bike/VR/low-time/fatigue,
         without requiring the owner to read internal files.
      6. Session brief includes purpose, ordered work, planned effort, warm-up/prep, permitted
         substitutions, technique/safety cues, required result signals, reduced/bad-week branch and
         mechanical safety brake behavior.
      7. W1 thin training domain, W2 canonical Health AI training authority, W3 system-decided
         programming, W4 session brief, W7 mechanical safety brake, W8 reduced/bad-week return,
         W17 Direction OS boundary, W18 D-kernel-1, W20 setup/body evidence split are preserved.
      8. TA-CA1, TA-CA2 and TA-CA3 are satisfied; TA-CA8/TA-CA9 are not contradicted.
      9. P1-P3/P8/P9/P10/P12 remain PLAN/HOW input, not Direction OS state.
    evaluator: >
      A separate review/work session or verifier must try to refute thin-domain attach, no-hardcode
      evidence-backed program creation, gate compatibility, and session-brief correctness before t-1
      is accepted as done.
    blocker: >
      t-1 product implementation evidence now exists in ainazemtsau/health-ai at
      commit c1bf61e, but t-1 is not accepted as done until a fresh verifier
      session refutes or accepts the product evidence against done_when items 1-10.
    unblock_when: >
      A separate verifier/review work session checks Health AI commit c1bf61e,
      changed files, `python tools/check_training_activity_thin_slice.py` output,
      `python tools/check_kernel_spine.py` output, and the acceptance matrix; it
      either marks t-1 done with evidence or names the first remaining blocker.

  - id: t-2
    status: pending
    kind: executor
    repo: ainazemtsau/health-ai
    goal: >
      Training/activity has a basic operational contour: normalized logging, screenshot/export/text/voice
      import, basic guided route, status/advice/substitution handling, review decision and nutrition handoff.
    done_when: >
      Product evidence shows:
      1. Brief+later-report, specialist screenshot/export/text/voice import, and basic guided route all
         converge on one normalized training LOG meaning: assigned work, performed work, completion,
         substitutions/deviations, effort, relevant recovery/pain/safety signals, source/provenance,
         confidence, safety disposition and review-needed flag.
      2. Screenshot/external-result path treats media/raw exports as transient input: Health AI extracts
         candidate facts, shows a readable extraction for owner correction/confirmation, asks only
         materially useful follow-up questions, then persists only the structured normalized result with
         source/confidence. Screenshots/media/raw exports are not stored as durable Health AI or Direction
         OS artifacts.
      3. Basic guided route can conduct a session by bounded blocks from ACTIVE authority, accept natural
         language results, shorten/stop for safety, persist recoverable checkpoints/LOG state at lawful
         job boundaries, and cannot silently rewrite ACTIVE program authority.
      4. Owner can ask training status/advice/substitution/missed-week questions and Health AI answers
         from ACTIVE authority, current state and safety rules, not free-form chat memory.
      5. Training review can emit one bounded decision class: hold, progress, regress, substitute, reduced
         mode, deload, rebuild, safety escalation or nutrition-review handoff; material patterns mutate or
         deliberately preserve a named authoritative artifact through the existing review/mutation path.
      6. Routine training->nutrition coupling uses only coarse planned/actual dated demand, where actual
         supersedes planned; review-level handoff is bounded. Training does not write nutrition artifacts,
         nutrition does not read raw training telemetry/files, and neither domain reads/writes the other's
         internals.
      7. Direct API integrations for Hevy/Strava/Apple/VR/wearables are explicitly not required; natural-language,
         screenshot/export and text/voice fallback remains valid.
      8. W9-W17 and TA-CA4..TA-CA11 are preserved; W19/TA-CA12 WA-K8 topology is preserved as a later
         acceptance proof and not claimed complete.
      9. No raw workout/activity/pulse/wearable data, screenshots, native exports or daily session records
         enter Direction OS state.
    evaluator: >
      A separate verifier/review must try to refute LOG equivalence, transient import confirmation,
      guided-boundary legality, review-to-mutation behavior, training<->nutrition no-direct-coupling,
      and raw-data boundary before t-2 is accepted as done.

  - id: t-3
    status: pending
    kind: guide
    goal: >
      Owner-operated acceptance proves the training/activity v0 contour is usable enough to start training
      and preserves a ready body-execution route.
    done_when: >
      In a guide session:
      1. Owner completes training setup or explicitly declines nonessential questions so defaults/unknowns
         are recorded as revisable according to the Health AI rules.
      2. Owner reviews and approves or rejects the proposed ACTIVE training program through the existing gate.
      3. Owner receives a concrete current-week slice and a "what today?" session brief generated from ACTIVE
         authority.
      4. Owner tests at least one result-capture path enough to verify it is understandable and correctable:
         brief+later-report OR screenshot/export/text/voice import OR basic guided route.
      5. Direction OS receives only strategic summary/problem/decision/evidence pointer/next CALL, not raw
         session details, screenshots or telemetry.
      6. A next body-execution CALL is ready: first real performed training/activity session reaches Health AI
         normalized LOG with safety/recovery feedback and next adjustment/review state.
      7. Setup/sample/import evidence is not represented as body-proven evidence; real physical execution
         remains separate per W20.
    evaluator: >
      Owner acceptance in-session plus a reviewable evidence pointer to Health AI artifacts/outputs; no raw
      training logs or screenshots copied into Direction OS.

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
  CALL c-health-training-activity-domain-v0-t1-verifier-001
  to: session
  direction: health
  play: work
  node: g-health-training-activity-system
  task: t-1
  goal: |
    A verifier verdict exists for whether Health AI commit c1bf61e satisfies
    training/activity t-1 done_when items 1-10 or needs another repair before
    any t-2 breadth work.
  context: |
    Product repo: C:\my_global_workflow_worktrees\health-ai
    Product commit: c1bf61e Activate training activity t1 authority
    Product branch: codex/health-training-activity-t1

    Changed files:
    - acceptance/x_training_activity/thin-slice-evidence-summary.md
    - acceptance/x_training_activity/thin-slice-matrix.json
    - tools/check_training_activity_thin_slice.py
    - x_training_activity/briefs/what-today.md
    - x_training_activity/programs/active-program.md
    - x_training_activity/programs/proposed-program.md
    - x_training_activity/runtime/cursor.md
    - x_training_activity/runtime/state-machine.md
    - x_training_activity/weeks/current-week.md

    Executor check output from committed state:
    - `python tools/check_training_activity_thin_slice.py`: PASS; rows 10 pass,
      active program ACTIVE, cursor ACTIVE with reduced_mode true and raw body
      execution false, current-week and what-today ACTIVE-derived reduced
      projections, forbidden infrastructure absent, raw body execution claims
      absent.
    - `python tools/check_kernel_spine.py`: PASS; WA-K1/2/3/4/5/7/9/10/11/12
      GREEN, WA-K6 and WA-K8 RED-DEFERRED as before.

    Same-session subagent reviewer pre-pass found and repair closed two blocker
    gaps before commit: file-checkable owner echo/name/version/date metadata and
    state-machine reduced-mode exception. This pre-pass is not the binding G5
    verifier; this CALL is the fresh verifier route.
  boundaries: |
    Do not start t-2.
    Do not modify Health AI except to report a verifier finding.
    Do not store raw workout/session/activity/pulse/wearable data, screenshots,
    native exports, or daily session details in Direction OS.
    Do not claim body execution.
    Do not duplicate router/lifecycle/gate/writer/job model/scheduler/server/
    database/background worker.
    Keep reduced_mode true unless the product has valid evidence and safety
    basis to change it.
  done_when: |
    A fresh verifier RESULT gives:
    1. verdict: t-1 accepted done or first blocker named;
    2. evidence against done_when items 1-10;
    3. explicit statement that t-2 is still not started by this verifier CALL;
    4. if accepted, state_changes may mark t-1 done and route the next pending
       task; if not accepted, state_changes keep t-1 active with the blocker.
  return: |
    RESULT with verifier verdict, evidence matrix, state_changes for t-1 only,
    and next CALL. State whether evidence is a binding fresh verifier or only a
    same-session pre-pass.
  budget: one verifier session

END_OF_FILE: live/health/NOW.md
