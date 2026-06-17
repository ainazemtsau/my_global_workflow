# NOW — health

active_bet:
  id: b-health-nutrition-system-full-001
  node: g-health-nutrition-system
  status: active
  review_status: binding_g5_met_pending_owner_close_decision
  review_checkpoint: 2026-06-17 s-health-nutrition-t4-review-tomorrow-start-001
  product_evidence_status: clean_binding_g5_met
  product_blocker_gaps: 0
  binding_g5_status: met
  verdict: met
  tomorrow_start_packet_status: produced
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
    status: done
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
    status: done
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
    status: done
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
    status: done
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

open_calls: []

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
  - id: d-health-nutrition-close-and-next-bet-001
    status: awaiting_owner
    question: >
      Approve closing g-health-nutrition-system as done based on binding G5 verdict=met,
      and choose the next health bet posture?
    options:
      - A: Approve nutrition system done; add/shape first real Health AI nutrition execution cycle next.
      - B: Approve nutrition system done; shape g-health-training-activity-system next.
      - C: Approve nutrition system done; pause new Direction OS bets after the tomorrow-start packet.
    recommendation: A
    activation_condition: immediate after s-health-nutrition-t4-review-tomorrow-start-001
    pending_owner_approved_tree_diff: >
      On A/B/C, set g-health-nutrition-system.status active -> done. On A, also add parked node
      g-health-first-nutrition-cycle under g-health-root before shaping it.
    pending_new_node_card_on_A:
      id: g-health-first-nutrition-cycle
      goal: >
        Первые 8 дней питания реально выполнены через Health AI nutrition: owner стартовал по
        tomorrow-start packet, вёл Health AI-only nutrition LOG, прошёл day-3 safety/friction check
        и day-8 review, а Direction OS получил только summary/decision/problem без raw food diary.
      why: >
        Реальная body-value начинается не от внедрённого модуля, а от первого выдержанного цикла;
        этот узел тестирует adherence, logging, fallback и review loop до следующей системной стройки.
      done_when:
        - Owner начал питание по Health AI nutrition first cycle.
        - Day-3 safety/friction check выполнен и не выявил blocker red flags, либо включил conservative branch.
        - Day-8 first-cycle review выполнен в Health AI по LOG summaries, owner feedback and core metrics.
        - Direction OS не содержит raw daily food logs/photos/check-ins; только summary, decisions, problems, and next CALL.
      status: parked

next: |
  awaiting_decision d-health-nutrition-close-and-next-bet-001

  recommended_next_on_A:
    CALL c-health-first-nutrition-cycle-shape-001
    to: session
    direction: health
    play: shape
    node: g-health-first-nutrition-cycle
    goal: |
      The first real Health AI nutrition execution cycle is ready as the next health bet.
    context: |
      Requires owner decision A from d-health-nutrition-close-and-next-bet-001.
      s-health-nutrition-t4-review-tomorrow-start-001 returned binding G5 verdict met for
      g-health-nutrition-system, blocker_gaps=0, and a tomorrow-start packet.

      On owner approval, writer should:
      - mark g-health-nutrition-system done in TREE/NOW;
      - add parked node g-health-first-nutrition-cycle from pending_new_node_card_on_A;
      - clear decision d-health-nutrition-close-and-next-bet-001;
      - make this CALL the next ready CALL.

      Read:
      - live/health/CHARTER.md
      - live/health/TREE.md
      - live/health/NOW.md
      - live/health/knowledge/health-nutrition-system-g5-review.md
      - health-ai x_nutrition/programs/active-program.md
      - health-ai x_nutrition/cycles/first-cycle.md
      - health-ai x_nutrition/menus/current-menu-cycle.md
      - health-ai x_nutrition/logs/YYYY-MM-DD.md
      - health-ai x_nutrition/reviews/first-cycle-review.md
    boundaries: |
      Do not store raw daily food logs, photos, or check-ins in Direction OS.
      Do not rebuild the nutrition architecture.
      Do not build product repo code unless a later executor CALL asks for it.
      Do not ask owner to choose expert nutrition variables.
      Do not make medical diagnoses or prescriptions.
    done_when: |
      A shaped bet exists for the first real Health AI nutrition execution cycle,
      with appetite, kill_by, cut list, lens sweep, tasks, and a next CALL.
    return: |
      RESULT with shaped bet, state_changes, decisions_needed, and next CALL.
    budget: one focused shape session

END_OF_FILE: live/health/NOW.md
