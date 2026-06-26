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
  CALL c-health-training-activity-domain-v0-t1-executor-001
  to: executor
  direction: health
  node: g-health-training-activity-system
  task: t-1
  repo: ainazemtsau/health-ai
  kind: engineering
  goal: |
    Health AI has the first thin training/activity domain v0 slice: thin-domain authority,
    dynamic evidence-backed program creation, current-week slicing, and today's session
    brief path over the existing kernel, without hardcoded research/question/program
    templates and without duplicating any kernel engine.
  context: |
    Read Direction OS input evidence:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-training-activity-system.md
    - live/health/work/converge-g-health-training-activity-system-arch.md
    - live/health/work/converge-g-health-core.md
    - live/health/work/converge-g-health-core-kernel.md
    - live/health/work/converge-g-health-core-kernel-arch.md
    - live/health/history/2026-06-20-s-health-core-kernel-wave0-derisk-001.md
    - live/health/history/2026-06-24-s-health-core-kernel-wa-k10-evidence-repair-001.md
    - live/health/history/2026-06-25-s-health-training-activity-converge-001.md
    - live/health/history/2026-06-26-s-health-training-activity-shape-002.md

    Product facts imported by shape:
    - health-ai @8246cec had current-head WA-K10 GREEN.
    - nutrition is an ACTIVE thin sibling with program/cycle/week/menu/recipe artifacts
      and cursor DAY_LOOP.
    - D-kernel-1 is imported as registry-line control-plane decide-and-inform.
    - Raw workout/activity/pulse/wearable data, native exports, screenshots and daily
      session LOGs must not enter Direction OS state.

    Binding acceptance intent to preserve:
    - Copy/implement the acceptance intent of W1-W20 from
      live/health/work/converge-g-health-training-activity-system.md.
    - Copy/implement §CONTRACTS TA-CA1..TA-CA12 requirements.
    - Preserve especially:
      W1 thin training domain;
      W2 canonical Health AI training authority;
      W3 setup asks only irreducible material facts while programming is system-decided;
      W4 session brief;
      W7 mechanical safety brake;
      W8 reduced/bad-week return;
      W9 review mutates/preserves artifacts;
      W10 equivalent capture routes;
      W11 transient screenshot/external-result confirmation;
      W12 guided training chat bounds;
      W13 normalized session LOG minimum;
      W14 guided interruption durability;
      W15 specialist-tool authority/fallback;
      W16 training<->nutrition contract;
      W17 Direction OS boundary;
      W18 D-kernel-1;
      W19 WA-K8 second-domain proof;
      W20 setup-proven versus body-proven evidence split.

    PLAN agenda P1-P12 remains HOW-only input:
    namespace/artifact names; concrete program design; session-brief schema; LOG schema;
    screenshot parsing mechanics; adapters/vendor mapping; guided checkpoint granularity;
    review thresholds; safety wording; training-demand labels; WA-K8 fixture mechanics;
    setup/body evidence script.

    Owner amendment from shape:
    - Do not hardcode a research template, question script, program template, fixed schedule,
      split, volume, intensity, vendor, or intake form in Direction OS or the implementation
      contract.
    - For any training artifact that depends on current external evidence, especially the
      training program, Health AI must determine what evidence/deep-research pass is needed,
      use current data, and record source-backed rationale, owner facts used, defaults/
      assumptions and safety/adherence constraints.
    - Questions are dynamic: ask only materially missing irreducible owner facts. Do not ask
      the owner to design expert variables.
    - The program must be extensible to arbitrary schedules, constraints, equipment, preferences,
      conditions and other nuances that materially affect safety, adherence or effectiveness.

    This task is t-1 only. It should establish the authority/program/week/session-brief path.
    t-2 will handle logging/import/guided/review/handoff contour. t-3 will do owner-operated
    acceptance.
  boundaries: |
    Do not modify Direction OS state.
    Do not store raw workout/activity/pulse/wearable data, native exports, screenshots or daily
    session details in Direction OS.
    Do not build or require direct API integrations for Hevy, Strava, Apple Health, Apple Fitness,
    VR or wearable tools.
    Do not build shared body-measurements protocol, dashboard/trend UI, or full WA-K8 proof in
    this task.
    Do not prescribe concrete workout programming in the executor CALL itself; implementation must
    create the program from evidence, owner/core facts and current Health AI state.
    Do not duplicate kernel engine behavior: no second router, lifecycle, gate, writer barrier,
    job model, scheduler, server, database, background worker or module-specific engine.
    Do not weaken W1-W20, TA-CA1..TA-CA12, setup/body evidence split, D-kernel-1, or the WA-K8
    later-proof route.
    Architecture picks A1-A5 are context-only input evidence; do not copy them into product
    done_when as binding design unless required by the signed WHAT/contract rows.
  done_when: |
    Product evidence shows:
    1. Training/activity attaches as a thin domain over the existing kernel: namespaced data,
       one registry-line control-plane attach, one state-machine instance, one cursor instance,
       one bounded procedure per term/stage as needed, zero duplicated router/lifecycle/gate/
       writer/job model/scheduler/server/database/background worker.
    2. Health AI can create a training/activity program proposal from current owner/core facts
       and current external evidence. It does not use a hardcoded research template, fixed
       question script, fixed program template, fixed schedule, split, volume, intensity, vendor,
       or intake form. The system determines what evidence/deep-research pass is required for
       the artifact being created; for the training program this must include current evidence
       sufficient to justify the plan for the owner's profile, goals, constraints, safety,
       adherence, equipment and phase.
    3. Setup asks dynamically only for materially missing irreducible owner facts; it may ask
       freely when useful but does not block on nonessential answers, records defaults/assumptions
       as revisable where allowed, and never asks the owner to design expert variables. Exercise
       selection, split, volume, intensity, conditioning mix, progression, regression and deload
       logic are system-decided from evidence + owner profile + current phase + constraints +
       feedback.
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
    10. Return includes commit/PR evidence and check output, plus a short note naming any blocker
        found before breadth work.
  return: |
    RESULT with:
    - outcome: what Health AI training/activity t-1 can now do;
    - evidence: commits/PR, changed files, check output, and a concise acceptance matrix against
      done_when items 1-10;
    - explicit statement whether t-2 can proceed or which blocker must be repaired first.
  budget: one executor task, bounded to t-1 only

END_OF_FILE: live/health/NOW.md
