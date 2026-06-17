# NOW — health

active_bet:
  id: b-health-nutrition-system-full-001
  node: g-health-nutrition-system
  status: active
  appetite: 1 focused day
  started_from_call: c-health-nutrition-shape-001
  owner_approved: >
    Ну, в принципе, согласен. Можно ожидать обновлённую эту карточку T1, T2 реально можешь
    объединить. С остальным согласен по твоим рекомендациям.
  goal: >
    Full chat-first nutrition functionality is implemented in Health AI as an additive module on top of
    g-health-core: broad evidence-backed method landscape, personalized active nutrition program,
    first executable cycle, menus/recipes/grocery/prep/fallback outputs, low-friction food tracking,
    nutrition review/mutation, bad-week/safety behavior, provider-independent continuation, writer handoff,
    and future app/vitrine integration seam.
  kill_by: >
    2026-06-18 12:00 Europe/Amsterdam: if there is not a research-backed personalized nutrition program
    encoded into Health AI nutrition, a full W1-W13/NCA0-NCA9 implementation/evidence surface,
    provider-independent continuation + writer handoff proof, and a tomorrow-start packet that lets the
    owner begin nutrition without another architecture session, stop and review/repair instead of extending.
  forecast: >
    AI executor can complete this within one focused day because the work is primarily structured text,
    conventions, evaluator evidence, and file-based module design, not a human-scale app buildout.
  against: >
    The bet fails if implementation becomes a reduced MVP/skeleton, skips the broad research landscape,
    hardcodes a narrow diet answer, requires UI/app/runtime/server/DB/cron/scheduler/background-worker,
    rewrites g-health-core, stores raw nutrition logs in Direction OS, or lacks writer/continuation path.
  cut_list:
    - current Mealie/Notion/recipe-app/shopping-app/weekly-menu UI/vitrine dependency
    - server, database, runtime, cron, scheduler, background-worker, autonomous recurring jobs
    - full polished recipe/content database
    - exact macro/gram logging as default
    - training/activity module implementation
    - Direction OS storage of raw daily food logs/photos/check-ins
  lens_sweep:
    weight-nutrition: task via t-1/t-2/t-4
    strength-body-composition: task-light via t-1/t-2; nutrition adapts when training starts, but training implementation is out
    activity-conditioning: not_needed_for_implementation; later training/activity module
    adherence-relapse: task via t-1/t-2/t-4
    medical-safety: task via t-1/t-2/t-4
    ai-system-data-architecture: task via t-2/t-3/t-4
  riskiest_assumption: >
    Broad Deep Research can be converted into an actionable personalized nutrition program without hardcoding
    a narrow diet answer or leaving a dead research report.
  acceptance_evaluator_surface:
    what_rows: W1-W13 copied from signed nutrition WHAT in work/converge-g-health-nutrition-system.md
    contract_rows: NCA0-NCA9 copied from corrected architecture in work/converge-g-health-nutrition-system-arch.md
    corrected_blockers: B1-B3 preserved
    provider_continuation: >
      Nutrition outputs must persist in GitHub-state and resume across ChatGPT/Claude/Claude Code/Codex
      through AGENTS/CLAUDE/SYSTEM-style conventions and writer-compatible validation.

tasks:
  - id: t-1
    kind: guide
    surface: ChatGPT Deep Research
    status: active
    goal: >
      Run broad Deep Research and normalize it into a personalized active nutrition program for the owner.
    done_when: >
      Deep Research maps the current evidence landscape without assuming a preselected diet; compares relevant
      method families; synthesizes evidence brief, method reference, personalized active program, no-training
      initial phase, training-start adaptation rules, system-decided expert variables, askable owner facts,
      first-cycle design rules, tracking/review framework, safety boundaries, refresh triggers, and implementation
      handoff for Health AI nutrition.
    evidence_expected: >
      Research brief with source citations, method landscape/reference, personalized program spec, decision framework,
      uncertainty notes, refresh triggers, and implementation handoff artifact suitable for t-2.
  - id: t-2
    kind: executor
    repo: ainazemtsau/health-ai
    status: queued
    goal: >
      Implement the full chat-first Health AI nutrition system as an additive module on g-health-core,
      using the t-1 research/program output.
    done_when: >
      Health AI nutrition contains the full functional surface: evidence/reference layer, method landscape,
      active personalized program, decision framework, owner facts known/pending/defaults, phase rules,
      first cycle, menu/eating plan, substitutions/swaps, executable recipes/instructions, grocery/prep/base-prep,
      fallback/lazy meals, food LOG shape, review procedure, mutation decisions, bad-week mode, safety behavior,
      operator-invoked procedure seams, future integration seam; passes W1-W13/NCA0-NCA9/B1-B3 with no core rewrite,
      no forbidden infrastructure, and no raw Direction OS nutrition diary.
    evidence_expected: >
      Commit/PR, file list, evidence summary, evaluator/check output mapping implementation to W1-W13/NCA0-NCA9/B1-B3,
      and first-cycle artifacts showing owner can begin nutrition.
  - id: t-3
    kind: executor
    repo: ainazemtsau/health-ai
    status: queued
    goal: >
      Add provider-independent continuation and writer handoff for nutrition so new ChatGPT/Claude/Codex sessions
      can resume from GitHub-state and durable changes pass writer validation.
    done_when: >
      AGENTS.md is canonical; CLAUDE.md points to AGENTS.md without conflicting fork; portable SYSTEM/project prompt
      or equivalent convention explains non-code chat operation; operator/writer/executor/reviewer roles are explicit;
      generated program/menu/cycle/log/review changes can be represented as file changes; writer-compatible packets/
      patches include exact files, rationale, active program/cycle references, and checks; writer validates schema,
      namespace, PLAN-vs-LOG, continuity, W1-W13/NCA0-NCA9/B1-B3, no core rewrite, no forbidden infrastructure,
      no Direction OS raw diary; bad write attempts are rejected with examples; fresh-chat continuation dry-run passes.
    evidence_expected: >
      Commit/PR; AGENTS/CLAUDE/SYSTEM or equivalent carrier changes; writer handoff examples; rejection examples;
      fresh-chat continuation dry-run evidence.
  - id: t-4
    kind: session
    play: review
    status: queued
    goal: >
      Refute or verify the full nutrition system against the shaped bet, then produce the tomorrow-start packet.
    done_when: >
      Separate review checks t-1 through t-3 evidence; reports pass/fail for broad Deep Research quality,
      personalized active nutrition program, full W1-W13 functionality, NCA0-NCA9, B1-B3, no functionality cuts,
      no core rewrite, no forbidden app/runtime/server/DB/cron/scheduler/background-worker, no raw Direction OS diary,
      and provider-independent continuation + writer handoff; if blocker_gaps=0, produces tomorrow-start packet with
      what to eat tomorrow, what to buy/prep, fallback, how to log, what to write AI in the evening, and when/how first
      nutrition review happens.
    evidence_expected: >
      RESULT from review session with refutation evidence, pass/fail verdict, blocker_gaps, tomorrow-start packet
      if passed, state_changes, and next CALL.

open_calls:
  - id: c-health-nutrition-t1-deep-research-program-001
    to: session
    for: t-1
    issued: 2026-06-17
    note: >
      Guide session for the broad ChatGPT Deep Research work packet and personalized active nutrition program.

recurring: []

decisions:
  - id: d-health-nutrition-define-signoff-001
    status: resolved
    owner_choice: A
    owner_words: "A — да, подписываем"
  - id: d-health-nutrition-what-signoff-001
    status: resolved
    owner_choice: A
    owner_words: "A"

next: |
  CALL c-health-nutrition-t1-deep-research-program-001
  to: session
  direction: health
  play: guide
  node: g-health-nutrition-system  task: t-1
  goal: |
    Produce and run/prepare the broad ChatGPT Deep Research work needed to create an evidence-backed,
    personalized active nutrition program for the owner.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-system.md
    - live/health/work/converge-g-health-nutrition-system-arch.md
    - live/health/knowledge/health-core-corrected-g5-review.md
    - health-ai acceptance/core/evidence-summary.md
    - health-ai core/extensions/attach-contract.md
    - health-ai core/procedures/template-contract.md
    - health-ai core/provenance/day-type.md

    Owner profile known from charter:
    male, 35, 182 cm, 125 kg, BMI about 37.7; goal is sustainable weight loss toward 90-95 kg,
    strength/muscle/energy protection, long-term adherence and maintenance. Owner has sport/diet experience,
    cooking infrastructure, scale, willingness to use AI tracking; no stated restrictions yet.

    Shape requirements:
    - No nutrition feature cuts.
    - Use broad Deep Research, not a hardcoded narrow diet prompt.
    - Do not assume a preselected diet.
    - Produce research brief + method landscape/reference + personalized active nutrition program +
      implementation handoff for Health AI nutrition.
    - Program must support no structured training initially and adaptation when training starts later.
    - Expert variables are system-decided; ask only irreducible owner facts.
    - Output must be suitable for t-2 implementation as Health AI nutrition module on g-health-core.
  boundaries: |
    Do not implement product repo code.
    Do not create a generic menu-only answer.
    Do not ask owner to choose expert variables such as meals/day, deficit, protein, timing,
    tracking precision, intermittent fasting, calorie cycling, diet breaks, or refeeds.
    Do not prescribe medically or diagnose.
    Do not add UI/app/vitrine/Mealie/Notion/runtime/DB/server/cron/scheduler/background-worker requirements.
    Do not store raw daily nutrition logs in Direction OS.
  done_when: |
    - A self-contained Deep Research prompt/work packet exists and is broad enough to discover the relevant
      method landscape rather than confirm a preselected approach.
    - Deep Research output or ready-to-run packet covers:
      evidence landscape, method comparison, applicability to owner, use_now/later_option/reject decisions,
      personalized active nutrition program, no-training initial phase, training-start adaptation rules,
      system-decided expert variables, askable owner facts, first-cycle design rules, tracking/review framework,
      safety boundaries, refresh triggers, and Health AI implementation handoff.
    - If actual Deep Research cannot be run inside this session/surface, return the exact ready-to-run Deep Research
      prompt plus expected output schema and next CALL for implementation after owner supplies the report.
  return: |
    RESULT with Deep Research prompt/report, normalized program spec, method landscape, implementation handoff,
    state_changes, and next CALL.
  budget: one tight guide/research movement
  surface: ChatGPT Deep Research

END_OF_FILE: live/health/NOW.md
