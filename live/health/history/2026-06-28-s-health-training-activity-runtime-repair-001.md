RESULT s-health-training-activity-runtime-repair-001 (call: c-health-training-activity-runtime-repair-001)
direction: health   play: work   node/task: g-health-training-activity-system/r-health-ai-minor-fix-lane

outcome: |
  Health AI training/activity no longer presents the false launch-ready state from
  health-ai 8aa14f8. Product commit 1fe41c2 repairs the runtime to resolve no-program
  natural training/activity intents to PROGRAM / research_request / awaiting Deep Research,
  not ACTIVE/DAY_LOOP.

  Missing research now produces a ready-to-run plain Markdown Deep Research request at
  x_training_activity/research/current-request.md. Program proposal, ACTIVE authority,
  current week, today/session brief, first session, progression, and material mutation are
  blocked until a suitable returned research conclusion exists and the owner approves a named
  proposed artifact. Ordinary fatigue/tired-day reduction remains allowed only inside an
  already ACTIVE accepted program and cannot increase demand or bypass safety.

  No Deep Research conclusion, citations, owner approval, ACTIVE program, first real
  training/activity session, or raw body-execution evidence was fabricated.

evidence: |
  Product commit:
  - health-ai 1fe41c22139c10587fbfa82137611620b33f2095
  - short SHA: 1fe41c2
  - commit message: Repair training activity launch readiness

  Changed product files:
  - validation.config
  - tools/check_training_activity_thin_slice.py
  - acceptance/x_training_activity/negative-fixtures.json
  - acceptance/x_training_activity/route-equivalence-fixtures.json
  - acceptance/x_training_activity/thin-slice-evidence-summary.md
  - acceptance/x_training_activity/thin-slice-matrix.json
  - x_training_activity/index.md
  - x_training_activity/domain.md
  - x_training_activity/runtime/state-machine.md
  - x_training_activity/runtime/cursor.md
  - x_training_activity/runtime/artifact-families.md
  - x_training_activity/reference/evidence-reference.md
  - x_training_activity/research/index.md
  - x_training_activity/research/deep-research-brief.md
  - x_training_activity/research/current-request.md
  - x_training_activity/research/conclusions/README.md
  - x_training_activity/program-synthesis/proposed-program-synthesis.md
  - x_training_activity/programs/proposed-program.md
  - x_training_activity/programs/active-program.md
  - x_training_activity/weeks/current-week.md
  - x_training_activity/briefs/what-today.md
  - x_training_activity/logs/YYYY-MM-DD.md
  - x_training_activity/procedures/operator-seams.md
  - x_training_activity/procedures/day-loop.md
  - x_training_activity/procedures/review.md
  - x_training_activity/procedures/mutation.md
  - x_training_activity/reviews/first-cycle-review.md
  - x_training_activity/setup/material-questions.md

  Check commands and outputs from committed product state:
  - `python tools/check_training_activity_thin_slice.py`:
    PASS: x_training_activity research-first repair is complete; required markdown files 23;
    done_when rows 17 pass, 0 fail; negative fixtures 23 pass, 0 fail; cursor PROGRAM,
    selected family research_request, awaiting deep_research; launch authority blocked until
    research-backed proposal and owner approval; first session/day loop blocked until ACTIVE
    program plus current week; old ACTIVE/DAY_LOOP sample-launch state rejected.
  - `python tools/check_kernel_spine.py`:
    PASS: kernel spine acceptance; WA-K1/2/3/4/5/7/9/10/11/12 GREEN; WA-K6 and WA-K8
    RED-DEFERRED as expected; negative fixtures trip on rejected cases.
  - `python tools/check_structural_repair.py`:
    PASS: structural repair contracts; owner_fact_delta, shared owner facts, nutrition day-loop
    branches, no forbidden stores/infrastructure, projection freshness, pain signal, hydration
    support and cursor contracts remain green.
  - `git -C C:\my_global_workflow_worktrees\health-ai status --short --branch`:
    `## main...origin/main [ahead 1]` after commit.
  - `rg -n "x_nutrition|raw_body_execution_claimed.*true|raw_payload_saved.*true|import_raw_payload_saved.*true" x_training_activity acceptance/x_training_activity tools/check_training_activity_thin_slice.py validation.config`:
    only acceptance/checker text mentions the forbidden `x_nutrition` dependency; no true raw
    payload/body-execution flags.

  Done_when reconciliation:
  1. PASS - no false ACTIVE/DAY_LOOP without authority: cursor is PROGRAM / research_request /
     awaiting deep_research; active-program.md is NOT_ACTIVE; what-today.md is
     BLOCKED_NO_ACTIVE_PROGRAM.
  2. PASS - short natural intents route semantically: state-machine declares
     training_launch_intent, evidence_dependent_question, active_day_adjustment and
     weekly_review_intent; route-equivalence fixtures reject exact phrase matching and manual
     workflow dependence.
  3. PASS - missing Deep Research emits a ready-to-run Markdown request and blocks downstream:
     x_training_activity/research/current-request.md is plain Markdown; no JSON/YAML packet is the
     primary owner instruction.
  4. PASS - Deep Research gate is general for material evidence-dependent decisions:
     PROGRAM child_dependency blocks program_proposal, owner_ready_launch, first_session,
     progression and material_program_mutation; fatigue/tired-day same-authority reduction after
     ACTIVE approval is explicitly not blocked by default.
  5. PASS - proposal and ACTIVE are gated: proposed-program.md is BLOCKED_AWAITING_RESEARCH;
     active-program.md is NOT_ACTIVE; current-week and today/session are blocked until ACTIVE plus
     current week.
  6. PASS - sample claims cannot launch: evidence-reference.md, proposed-program.md and
     active-program.md mark sample_committed_claims_only as non-authoritative for launch,
     session, progression or material mutation.
  7. PASS - planned prescriptions vs raw logs boundary: future plan/week/session artifacts may
     contain planned work after ACTIVE; LOG remains coarse/normalized and raw payload/body flags
     stay false.
  8. PASS - weekly review/mutation trainer loop: review procedure compares planned demand with
     coarse actual completion, recovery, pain and adherence, and emits exactly one class:
     hold/progress/regress/substitute/reduced_mode/deload/rebuild/safety_escalation/
     nutrition_review_handoff.
  9. PASS - checker fails old bad state: negative fixtures include ACTIVE/DAY_LOOP sample launch,
     sample launch basis, sample artifact promotion, first session before research/approval,
     missing child dependency, exact phrase matching, internal-packet primary instruction and
     pre-ACTIVE REDUCED/today_brief bypass; checker reports old ACTIVE/DAY_LOOP sample-launch
     state rejected.
  10. PASS - owner-facing outputs are Markdown/plain language: current-request.md is a plain
      Deep Research request; proof-of-load stage is program foundation / awaiting research.
  11. PASS - data and infrastructure boundaries: no app/server/database/scheduler/background
      worker/second router/lifecycle/writer/job model; no raw Direction OS data; no direct
      training runtime dependency on x_nutrition internals.

  Before/after behavior examples:
  - No program + natural training intent: before, 8aa14f8 could resolve to ACTIVE/DAY_LOOP and a
    reduced today brief; after, Health AI shows training/activity PROGRAM / awaiting Deep
    Research and emits x_training_activity/research/current-request.md, not a workout.
  - Yoga/new modality/evidence-dependent question: before, sample claims could be treated as
    enough for advice; after, it routes to PROGRAM research unless a current suitable conclusion
    exists.
  - Fatigue/reduced day: before, reduced mode blurred no-program launch readiness; after,
    tired-day reduction is allowed only inside an already ACTIVE accepted program and only to
    hold/reduce same-authority demand.
  - Weekly review: before, review was mostly a class list; after, review/mutation compare planned
    demand against coarse actual completion/recovery/pain/adherence and choose one bounded class.

  Review evidence:
  - Ultracode read-only exploration and architecture agents identified the false ACTIVE/DAY_LOOP,
    missing child dependency and validation.config drift.
  - Independent reviewer found one blocker after implementation: pre-ACTIVE PROPOSED -> REDUCED
    could emit today_brief. It was repaired by removing PROPOSED -> REDUCED, requiring ACTIVE
    authority for REDUCED, adding NEG23 and wiring check.pre_active_reduced_blocked into DW13.
  - Focused re-review found no blocking findings after that repair.

state_changes: |
  Applied exact Direction OS state changes:

  live/health/NOW.md:
  - Preserve active_bet.status: none.
  - Replace active_bet.note with a note that health-ai 1fe41c2 supersedes the false
    8aa14f8 launch route, training/activity now resolves to PROGRAM awaiting Deep Research,
    and first real performed session remains unclaimed.
  - Preserve tasks: [].
  - Preserve open_calls: [].
  - In recurring[id=r-health-ai-minor-fix-lane]:
      change last_done from 2026-06-24 to 2026-06-28.
      update note to include health-ai 1fe41c2, os-engineering-contract.v9 validation sync,
      checker rejection of old ACTIVE/DAY_LOOP sample launch, and PROGRAM awaiting Deep Research.
  - Preserve decisions: [].
  - Replace NOW.next with CALL c-health-training-activity-deep-research-child-guide-001
    (play: guide) whose goal is that a returned Health AI training/activity Deep Research
    conclusion is available for program synthesis.

  live/health/LOG.md:
  - Append:
    2026-06-28 — health/g-health-training-activity-system repair: health-ai 1fe41c2 replaced false ACTIVE/DAY_LOOP launch readiness with PROGRAM awaiting Deep Research, v9 validation and checker guards; first session remains blocked, no research/approval/session fabricated; next Deep Research child guide. → history/2026-06-28-s-health-training-activity-runtime-repair-001.md

  live/health/history/:
  - Add this RESULT as 2026-06-28-s-health-training-activity-runtime-repair-001.md.

  TREE.md:
  - No changes.

captures:
  - Health AI now needs the real returned training/activity Deep Research conclusion before any personal program proposal or first session can proceed.
  - Checker remains static over declarative Markdown; it now covers the witnessed ACTIVE/DAY_LOOP sample-launch and pre-ACTIVE REDUCED/today_brief bypass classes, while true semantic routing still depends on the Health AI operator following committed state.
decisions_needed: []
play_check:
  - 1 Recite: done - recurring repair goal was to stop false launch readiness and route training/activity through research, proposal, approval, ACTIVE, session and weekly review state.
  - 2 Owner inputs (owner): skipped/no new question - this was a product repair, not a new owner-content program to live by; the owner correction from 2026-06-28 was used: no Direction OS PROGRAM card, no long internal prompt, no hardcoded launch phrase, Health AI owns the process internally.
  - 3 Do the work: done - ultracode fan-out mapped repo/checker gaps, one implementer repaired the product, one blocker from adversarial review was fixed, product commit 1fe41c2 created.
  - 4 Self-check: done - done_when reconciled point-by-point above; training, kernel and structural checks pass from committed state; focused re-review found no blocking findings.
  - 5 Close: done - RESULT recorded, recurring lane updated, LOG/history updated, and next CALL prepared for Deep Research child guide.
log: health/g-health-training-activity-system repair: health-ai 1fe41c2 replaced false ACTIVE/DAY_LOOP launch readiness with PROGRAM awaiting Deep Research, v9 validation and checker guards; first session remains blocked, no research/approval/session fabricated; next Deep Research child guide.
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

END_OF_FILE: live/health/history/2026-06-28-s-health-training-activity-runtime-repair-001.md
