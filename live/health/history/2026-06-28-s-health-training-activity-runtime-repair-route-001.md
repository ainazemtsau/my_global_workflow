RESULT s-health-training-activity-runtime-repair-route-001 (call: owner-message-2026-06-28-training-activity-repair)
direction: health   play: repair   node/task: g-health-training-activity-system/recurring:r-health-ai-minor-fix-lane

outcome: |
  NOW no longer routes the owner to the first real training/activity session.

  The 2026-06-28 owner correction shows that the previous product launch route is unsafe:
  health-ai 8aa14f8 resolves x_training_activity to ACTIVE/DAY_LOOP while evidence is
  sample_committed_claims_only and no real research-backed, owner-approved training program
  authority exists. The corrected state routes next to a bounded Health AI product repair through
  r-health-ai-minor-fix-lane.

  Direction OS remains strategic only. No raw training/body execution data was stored, and no first
  real training/activity session is claimed.

evidence: |
  Contradiction named:
  - NOW.next before repair was CALL c-health-training-activity-first-real-session-001, a guide route
    to perform the first real training/activity session through Health AI.
  - The owner-supplied repair request says this is a false launch state: x_training_activity must not
    issue a session until Deep Research / program proposal / owner approval / ACTIVE authority exist.

  Reconstruction:
  - live/health/LOG.md and history show that on 2026-06-27 the closed review relied on health-ai
    c1bf61e and 8aa14f8 plus owner launch acceptance "Запускаем".
  - health-ai is clean at 8aa14f8 Add training activity operational contour.
  - health-ai x_training_activity/runtime/cursor.md currently declares:
    x_training_activity_state=ACTIVE, selected route DAY_LOOP, reduced_mode=true, and
    raw_body_execution_claimed=false.
  - health-ai x_training_activity/programs/active-program.md currently treats
    sample_committed_claims_only as part of active reduced launch authority.
  - health-ai tools/check_training_activity_thin_slice.py currently reports that this bad state
    passes: cursor ACTIVE, reduced_mode true, raw body execution false, DAY_LOOP route.
  - Nutrition's x_nutrition/runtime/state-machine.md contains the working Deep Research child
    dependency pattern that training/activity should adapt without depending on nutrition internals.

  Owner confirmation:
  - Proposed state repair options were shown.
  - Owner chose the recommended option with: "вариант A".

  Applied evidence:
  - live/health/NOW.md now supersedes the first-session route and points to
    CALL c-health-training-activity-runtime-repair-001.
  - live/health/LOG.md has this repair line.
  - This history file records the full RESULT.

state_changes: |
  Apply the following exact Direction OS state changes.

  1) live/health/NOW.md

  - Preserve active_bet.status: none.
  - Replace active_bet.note with:

      No active bet after review closed b-health-training-activity-domain-v0-001 as met on
      2026-06-27. Product/process evidence: health-ai c1bf61e for t-1 and health-ai 8aa14f8 for
      t-2; owner release acceptance from t-3: "Запускаем". First real performed training/activity
      session is not claimed done. On 2026-06-28 the owner supplied a product repair request showing
      that the first-session route is unsafe because health-ai 8aa14f8 falsely resolves
      x_training_activity to ACTIVE/DAY_LOOP without real research-backed, owner-approved training
      program authority. The first-session route is superseded by a bounded Health AI repair through
      r-health-ai-minor-fix-lane; no first real session should be routed until the product repair
      restores the research -> proposal -> owner approval -> ACTIVE path.

  - Preserve tasks: [].
  - Preserve open_calls: [].
  - Preserve recurring r-health-ai-minor-fix-lane unchanged.
  - Preserve decisions: [].
  - Replace NOW.next with CALL c-health-training-activity-runtime-repair-001 as shown in next.

  2) live/health/LOG.md

  Append:

      - 2026-06-28 — health/g-health-training-activity-system repair: owner correction superseded the first real session route because health-ai 8aa14f8 falsely resolves x_training_activity to ACTIVE/DAY_LOOP on sample-only evidence; NOW.next rerouted to bounded product repair c-health-training-activity-runtime-repair-001 via r-health-ai-minor-fix-lane. → history/2026-06-28-s-health-training-activity-runtime-repair-route-001.md

  3) live/health/history/

  Add this full RESULT as:
  - live/health/history/2026-06-28-s-health-training-activity-runtime-repair-route-001.md

  4) TREE.md

  No TREE.md edit in this repair. The closed-node history is not rewritten here; a later review can
  reconcile the node if product repair evidence shows the prior closure should be reclassified.

captures:
  - After product repair returns, run a fresh review/refutation if the result changes the meaning of the 2026-06-27 training/activity closure rather than only repairing the runtime surface.
  - health-ai owes engineering contract re-sync to current os/engineering CONTRACT_VERSION 9; the executor CALL carries this warning so stale checker blind spots do not protect the repair.

decisions_needed: []

play_check:
  - 1 Name the contradiction: done — NOW.next routed to first real session, while the owner correction says the product is in a false ACTIVE/DAY_LOOP launch state without research/program/approval authority.
  - 2 Reconstruct: done — checked NOW, TREE, LOG/history, health-ai status/log, cursor.md, active-program.md, checker behavior, and nutrition Deep Research pattern.
  - 3 Propose corrected state: done — proposed replacing the first-session guide route with bounded executor repair via r-health-ai-minor-fix-lane, leaving active_bet none and TREE unchanged.
  - 4 Confirm: done — owner confirmed the recommended option with "вариант A".
  - 5 Friction: skipped — this is a product-runtime/checker defect routed through the existing minor-fix lane; no repeated OS-rule hole is proven in this repair session.

log: >
  2026-06-28 — health/g-health-training-activity-system repair: owner correction
  superseded the first real session route because health-ai 8aa14f8 falsely
  resolves x_training_activity to ACTIVE/DAY_LOOP on sample-only evidence;
  NOW.next rerouted to bounded product repair
  c-health-training-activity-runtime-repair-001 via r-health-ai-minor-fix-lane.

next: |
  CALL c-health-training-activity-runtime-repair-001
  to: executor
  direction: health
  node: g-health-training-activity-system
  recurring: r-health-ai-minor-fix-lane
  repo: C:\my_global_workflow_worktrees\health-ai
  kind: engineering
  goal: |
    Health AI training/activity no longer presents false launch readiness: short natural
    training/activity intents route through committed research, proposal, approval, active program,
    session, and weekly review state without manual owner workflow instructions.
  context: |
    Direction OS state:
    - live/health/NOW.md
    - live/health/TREE.md
    - live/health/history/2026-06-27-s-health-training-activity-domain-v0-review-001.md
    - live/health/knowledge/health-training-activity-v0-release-boundary.md

    Target product repo:
    - Working copy: C:\my_global_workflow_worktrees\health-ai
    - Remote identity: ainazemtsau/health-ai
    - Current bad baseline: 8aa14f8 Add training activity operational contour
    - Repo is clean at the start of this repair.
    - Contract warning: health-ai validation.config does not show current os/engineering
      CONTRACT_VERSION 9. Before or during repair, account for the owed re-sync / validation
      drift so old checker blind spots do not silently protect the fix.

    Owner correction, 2026-06-28:
    - Do not make the owner run a separate Direction OS "PROGRAM card".
    - Do not ask the owner to paste a long internal prompt into Health AI.
    - Do not hardcode a launch phrase.
    - The full training/activity process must be owned by Health AI internally.
    - Direction OS only routes this product repair and later receives summary-level outcomes.

    Current defects to repair:
    - False ACTIVE/DAY_LOOP cursor: x_training_activity/runtime/cursor.md currently says ACTIVE
      and selected route DAY_LOOP while reduced_mode=true, core phase/week/day are pending,
      evidence currentness is sample_committed_claims_only, and body execution is not claimed.
      This must not route to daily/session handling when no real research-backed,
      owner-accepted training program exists.
    - Deep Research gate missing: training/activity must declare a child dependency or equivalent
      evidence gate for first personal program creation. While the child conclusion is missing,
      Health AI must output a ready-to-run Deep Research request in plain Markdown and stop.
    - Deep Research is general, not program-only: any material training/activity decision that
      depends on current external evidence must check the research registry and block to Deep
      Research when no suitable current conclusion exists. Ordinary reduced-day adjustments inside
      an already active accepted program do not need research unless they depend on a new external
      evidence claim.
    - Checker accepts the bad state: tools/check_training_activity_thin_slice.py currently passes
      cursor ACTIVE, route DAY_LOOP, reduced_mode true, and sample-only evidence. That must become
      impossible.
    - Plan vs raw logs are confused: planned prescriptions inside Health AI plan/week/session
      artifacts are allowed and should be concrete enough to use; raw actual session telemetry and
      detailed diaries must not enter Direction OS and should stay coarse/normalized in Health AI.
    - Weekly trainer loop is underdeveloped: review/mutation must compare planned demand vs coarse
      actual completion/recovery/pain/adherence, emit one bounded decision class, and update
      next-week targets or preserve/rebuild safely without silently rewriting ACTIVE authority.

    Product files and patterns to inspect:
    - x_training_activity/programs/active-program.md
    - x_training_activity/programs/proposed-program.md
    - x_training_activity/program-synthesis/proposed-program-synthesis.md
    - x_training_activity/runtime/state-machine.md
    - x_training_activity/runtime/cursor.md
    - x_training_activity/runtime/artifact-families.md
    - x_training_activity/reference/evidence-reference.md
    - x_training_activity/setup/material-questions.md
    - x_training_activity/weeks/current-week.md
    - x_training_activity/briefs/what-today.md
    - x_training_activity/logs/YYYY-MM-DD.md
    - x_training_activity/procedures/operator-seams.md
    - x_training_activity/procedures/day-loop.md
    - x_training_activity/procedures/review.md
    - x_training_activity/procedures/mutation.md
    - x_training_activity/reviews/first-cycle-review.md
    - x_training_activity/handoffs/training-to-nutrition-demand-context.md
    - acceptance/x_training_activity/thin-slice-evidence-summary.md
    - acceptance/x_training_activity/thin-slice-matrix.json
    - tools/check_training_activity_thin_slice.py

    Working pattern to adapt without depending on nutrition internals:
    - x_nutrition/runtime/state-machine.md
    - x_nutrition/runtime/cursor.md
    - x_nutrition/runtime/artifact-families.md
    - Nutrition's PROGRAM child dependency pattern: Deep Research conclusion must return before
      downstream program/cycle/week/day outputs are allowed.

    Core delegated-job mechanism is generic; do not rewrite it unless a real core defect is found:
    - core/runtime/router.md
    - core/runtime/delegated-jobs.md
    - core/runtime/graph-contract.md
    - core/runtime/render-before-decision.md
    - core/governance/gate.md
    - core/governance/lifecycle.md

    Required owner-facing scenarios after repair:
    - No program + natural training intent: Health AI proof-of-load header shows
      domain training/activity, stage program foundation, awaiting Deep Research; output explains
      no training program exists, refuses to invent a workout, and emits the full ready-to-run
      Deep Research request in Markdown.
    - Yoga / new modality / evidence-dependent question: if no current in-scope research
      conclusion exists, route to Deep Research; if a current in-scope conclusion exists, use it
      to propose the bounded mutation/review change.
    - Tired today: with an active accepted program, route to reduced session adjustment without
      Deep Research unless the adjustment depends on a new external evidence claim.
    - Weekly review: consume only coarse feedback, choose one bounded decision class, update or
      preserve next-week targets/values appropriately, and avoid raw telemetry.

    Research artifact support may use:
    - x_training_activity/research/index.md
    - x_training_activity/research/deep-research-brief.md
    - x_training_activity/research/request-template-or-current-request.md
    - x_training_activity/research/conclusions/<date>-<topic>.md
    Do not fabricate a returned research conclusion or citations. If no real returned result exists,
    create the request/brief and set state to waiting.
  boundaries: |
    Do not perform the actual Deep Research unless a real returned research conclusion is supplied.
    Do not fabricate citations, external evidence conclusions, owner approval, or a first real
    training/activity session.
    Do not create an app UI, server, database, scheduler, background worker, second router, or
    second lifecycle/gate/writer/job model.
    Do not make Direction OS a training diary; Direction OS must receive only strategic summary,
    problem, decision, product evidence and next CALL.
    Do not store raw workout/activity/pulse/wearable data, screenshots, native exports, routes,
    sets, reps, loads, detailed session notes, or body-execution telemetry in Direction OS.
    Do not prohibit planned training prescriptions merely because raw actual logs are prohibited.
    Do not solve nutrition again or introduce direct training runtime dependency on x_nutrition
    internals.
    Do not hardcode exact launch phrases; use semantic owner-intent routing based on committed
    state and cursor/graph resolution.
  done_when: |
    Product commit exists and all of the following are true:

    1. Health AI training/activity no longer resolves to false ACTIVE/DAY_LOOP when real
       research-backed, owner-approved program authority is absent.
    2. Short natural training/activity intents route semantically through committed state without
       long owner instructions or exact phrase matching.
    3. Missing Deep Research produces a ready-to-run Markdown Deep Research request and blocks
       material program/session/mutation decisions until a bounded conclusion returns.
    4. The Deep Research gate applies to any material evidence-dependent training/activity
       decision, not only first program creation; ordinary fatigue/reduced adjustment inside an
       active accepted program does not require research by default.
    5. Proposed personal program output is generated only after suitable research conclusion
       exists; ACTIVE program/week/session route is generated only after owner approval of the
       named proposed artifact.
    6. Sample committed claims and sample proposed/active artifacts cannot become real launch
       authority.
    7. Program/week/session plan artifacts may contain usable planned prescription values, while
       raw actual logs/telemetry remain out of Direction OS and Health AI actual logs stay
       normalized/coarse unless a future scoped data-model change says otherwise.
    8. Weekly review/mutation behaves like a trainer: compares planned demand vs coarse actual
       completion/recovery/pain/adherence, emits exactly one bounded decision class such as hold,
       progress, regress, substitute, reduced_mode, deload, rebuild, safety_escalation, or
       nutrition_review_handoff, and updates/preserves/rebuilds next-week targets appropriately.
    9. Checks fail the old bad state represented by health-ai 8aa14f8 and pass the repaired state.
       At minimum they fail if live_researched=false plus cursor/session route ACTIVE/DAY_LOOP for
       launch, sample_committed_claims_only is launch basis, sample artifacts are promoted as
       owner-ready launch authority, first-session route exists before Deep Research conclusion
       plus owner-approved program, the graph lacks the Deep Research child dependency for
       evidence-dependent decisions, owner-facing launch requires a long manual instruction, or
       exact phrase matching is used.
    10. Owner-facing outputs are Markdown/plain language with the Health AI proof-of-load header
        and no YAML/JSON/internal packets as the primary owner instruction.
    11. Data and infrastructure boundaries remain intact: no raw Direction OS data, no duplicate
        infrastructure, no training-to-nutrition raw coupling, and no direct nutrition namespace
        dependency from training runtime docs.
  return: |
    RESULT with:
    - product commit SHA;
    - changed files;
    - check commands and output;
    - before/after behavior examples for no program + training intent, yoga/evidence-dependent
      question, fatigue/reduced day, and weekly review;
    - statement that actual Deep Research was not fabricated;
    - pointer to the ready-to-run Deep Research request if research is still outstanding;
    - raw-data boundary statement;
    - next recommended CALL: Deep Research child guide if research is outstanding, owner
      acceptance guide if proposed program is ready, bounded repair if checks fail, or strategic
      review if product repair is complete.
  budget: one focused repair/executor session

END_OF_FILE: live/health/history/2026-06-28-s-health-training-activity-runtime-repair-route-001.md
