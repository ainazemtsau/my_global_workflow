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
    Health AI nutrition can own a repeatable research-to-program procedure: request broad Deep Research,
    normalize it into an actionable active program, persist it in GitHub-state, and refresh it later
    without turning research into an external one-off.
  acceptance_evaluator_surface:
    what_rows: W1-W13 copied from signed nutrition WHAT in work/converge-g-health-nutrition-system.md
    contract_rows: NCA0-NCA9 copied from corrected architecture in work/converge-g-health-nutrition-system-arch.md
    corrected_blockers: B1-B3 preserved
    provider_continuation: >
      Nutrition outputs must persist in GitHub-state and resume across ChatGPT/Claude/Claude Code/Codex
      through AGENTS/CLAUDE/SYSTEM-style conventions and writer-compatible validation.

tasks:
  - id: t-1
    kind: executor
    repo: ainazemtsau/health-ai
    status: active
    goal: >
      Implement Health AI nutrition's research-to-program procedure and use it to bootstrap the first
      personalized nutrition program flow.
    done_when: >
      Health AI nutrition has a research-backed setup/refresh procedure; the procedure can generate a broad
      Deep Research request/prompt with expected output schema; it defines how Deep Research output is normalized
      into evidence base, method landscape, active nutrition program, first-cycle assumptions, safety boundaries,
      tracking/review framework, refresh triggers, and writer-compatible Health AI nutrition file changes; it
      supports first owner setup and later targeted refreshes; if an actual Deep Research report is unavailable,
      the output is an owner/operator-ready Deep Research packet plus explicit pending state, not invented research
      conclusions.
    evidence_expected: >
      Commit/PR, file list, research-to-program procedure, broad Deep Research prompt and output schema,
      normalizer contract, first-setup/pending-state evidence, writer-compatible change examples, and checks.
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
  - id: c-health-nutrition-t1-research-program-procedure-001
    to: executor
    for: t-1
    issued: 2026-06-17
    note: >
      Implement Health AI nutrition research-to-program procedure/bootstrap in the product repo.

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
  CALL c-health-nutrition-t1-research-program-procedure-001
  to: executor
  direction: health
  node: g-health-nutrition-system  task: t-1
  repo: ainazemtsau/health-ai
  kind: engineering
  goal: |
    Health AI nutrition has a first-class research-to-program setup/refresh procedure, and the first owner
    nutrition setup is bootstrapped through that procedure or left as an explicit pending Deep Research packet.
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

    Correction:
    Deep Research must not be treated as external one-off prep before Health AI nutrition exists.
    Health AI nutrition must own the research-to-program process: decide when research is needed,
    generate a broad Deep Research request, define the expected output schema, normalize the report into
    evidence/reference/program artifacts, persist those artifacts in GitHub-state, and support later targeted
    refreshes when training, plateau, hunger, medical constraints, travel, bad weeks, or maintenance transition
    make existing evidence insufficient.

    Owner profile known from charter:
    male, 35, 182 cm, 125 kg, BMI about 37.7; goal is sustainable weight loss toward 90-95 kg,
    strength/muscle/energy protection, long-term adherence and maintenance. Owner has sport/diet experience,
    cooking infrastructure, scale, willingness to use AI tracking; no stated restrictions yet.

    Shape requirements:
    - No nutrition feature cuts.
    - Health AI nutrition has research capability as a first-class procedure, not a one-time external report.
    - Use broad Deep Research through that procedure, not a hardcoded narrow diet prompt.
    - Do not assume a preselected diet.
    - Produce the procedure, prompt/schema, normalizer contract, and first setup/bootstrap path for:
      research brief + method landscape/reference + personalized active nutrition program.
    - Program must support no structured training initially and adaptation when training starts later.
    - Expert variables are system-decided; ask only irreducible owner facts.
    - Output must be suitable for t-2 implementation as Health AI nutrition module on g-health-core.
  boundaries: |
    Do not fake Deep Research if an actual Deep Research report is not available.
    Do not make research an external one-off outside Health AI nutrition.
    Do not create a generic menu-only answer or hardcode a preselected diet.
    Do not ask owner to choose expert variables such as meals/day, deficit, protein, timing,
    tracking precision, intermittent fasting, calorie cycling, diet breaks, or refeeds.
    Do not prescribe medically or diagnose.
    Do not rewrite g-health-core.
    Do not add UI/app/vitrine/Mealie/Notion/runtime/DB/server/cron/scheduler/background-worker requirements.
    Do not store raw daily nutrition logs in Direction OS.
  done_when: |
    - Nutrition has a research-backed setup/refresh procedure in the Health AI nutrition namespace.
    - The procedure can generate a broad Deep Research prompt and expected output schema without assuming a
      preselected diet.
    - The procedure defines how Deep Research output becomes method landscape, evidence reference, active
      nutrition program, first cycle assumptions, safety boundaries, tracking/review framework, refresh triggers,
      and writer-compatible file changes.
    - It supports first owner setup and later targeted refreshes.
    - If the actual report is missing, the repo contains an owner/operator-ready Deep Research packet and explicit
      pending state, not invented research conclusions.
  return: |
    RESULT with commit/PR, file list, checks, research-to-program procedure, prompt/schema, normalizer contract,
    first setup/bootstrap or pending Deep Research packet evidence, state_changes, and next CALL.
  budget: one focused executor movement
  surface: coding agent in health-ai product repo

END_OF_FILE: live/health/NOW.md
