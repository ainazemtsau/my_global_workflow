# NOW — health

active_bet:
  id: b-health-first-nutrition-cycle-001
  node: g-health-first-nutrition-cycle
  status: active
  appetite: 10 calendar days
  started_from_call: c-health-first-nutrition-cycle-shape-003
  owner_approved: >
    Approve as drafted
  goal: >
    The owner completes the first real 8-day nutrition cycle through Health AI
    nutrition: startup begins from a normal owner message, Health AI validates
    graph/cursor/router before execution, Health AI-only nutrition LOG summaries
    support day-3 safety/friction check and day-8 review, and Direction OS receives
    only summary, decisions, problems, and next CALL.
  kill_by: >
    2026-06-30 23:59 Europe/Minsk: if Health AI cannot prove a graph-selected
    repo-backed startup/transition before execution, if fewer than 8 Health AI
    nutrition days are completed, if day-3 safety/friction check or day-8 review
    is missing, if raw daily food diary content leaks into Direction OS, or if
    safety/friction forces conservative branch, stop and review instead of extending.
  forecast: >
    This should fit because health-ai now has repo-owned ChatGPT Project bootstrap,
    workflow graph/current cursor/router, evidence map, accepted program synthesis,
    first-cycle projection artifacts, provider journey evidence, and the evidence
    workflow check passing at commit 50f2215.
  against: >
    The bet fails if the operator bypasses STARTUP_ROUTER, treats seed menu/cycle
    files as active authority without graph selection, trusts chat claims as durable
    state, asks the owner to choose expert nutrition variables, stores raw food
    diary content in Direction OS, or turns the first cycle into new architecture,
    training/activity, or medical prescription work.
  next_if_true: >
    Review closes the first-cycle execution bet, harvests only strategic summary
    and decisions, then choose whether to run the second nutrition cycle, shape
    training/activity, or repair any surfaced Health AI friction.
  next_if_false: >
    Stop; do not extend appetite. Route to review/repair with the exact failed
    layer: provider/bootstrap, workflow cursor/router, evidence/program synthesis,
    cycle/week-plan execution render, DAY_LOOP logging, safety/friction, or review.
  cut_list:
    - raw daily food logs, photos, check-ins, menus, grocery execution, or diary content in Direction OS
    - training/activity implementation
    - nutrition architecture rebuild during this shape/execution cycle
    - app UI, runtime, DB, server, cron, scheduler, or background worker
    - exact macro/gram tracking as the default first-cycle requirement
    - owner choosing expert variables such as calories, protein, timing, fasting, meal count, tracking precision, or review cadence
    - new Deep Research unless Health AI evidence/currentness rules explicitly route to PROGRAM refresh
  lens_sweep:
    weight-nutrition: task via t-1/t-2/t-3/t-4; first cycle must test real adherence, hunger, fallback, and review loop
    strength-body-composition: not_needed_for_this_cycle; nutrition must preserve strength/muscle assumptions, but no training work starts
    activity-conditioning: not_needed; training/activity node remains parked
    adherence-relapse: task via t-3/t-4; logging friction, fallback use, hunger, energy, and prep friction are central
    medical-safety: task via t-1/t-3/t-4; pending allergy/medical facts, red flags, and conservative branch are explicit gates
    ai-system-data-architecture: task via t-1/t-2/t-5; router authority, repo-backed state proof, Health AI-only LOG, and Direction OS boundary are tested
  riskiest_assumption: >
    A normal owner startup message in Health AI can move from STARTUP_ROUTER to
    the first executable nutrition state through graph/cursor/router and repo-backed
    evidence without falling back into seed-artifact authority, unverified chat-state,
    or menu-before-router behavior.

tasks:
  - id: t-1
    kind: guide
    surface: Health AI ChatGPT Project or repo-backed equivalent
    status: active
    goal: >
      Health AI startup from a normal owner message produces a repo-grounded current
      nutrition state and exactly one bounded next action without execution content
      bypassing graph-selected authority.
    done_when: >
      Owner starts with a normal message such as "Хочу начать питание"; Health AI
      reads repo-owned bootstrap/load order, validates graph/current-workflow/router,
      reports the current state and one bounded next action, asks no expert-variable
      questionnaire, emits no menu/recipe/grocery/daily plan/raw LOG/review wall,
      and either proves durable state with commit/diff/fresh repo read or emits a
      writer-compatible packet.
    evidence_expected: >
      Owner-readable startup transcript/summary, resolved state, artifact family
      authorization status, any writer packet or commit evidence, and explicit
      no-menu-before-router/no-raw-Direction-OS-diary proof.
  - id: t-2
    kind: guide
    surface: Health AI
    status: queued
    goal: >
      Health AI reaches the first executable nutrition cycle path through authorized
      PROGRAM/CYCLE/WEEK_PLAN state without bypassing evidence map or program synthesis.
    done_when: >
      Health AI uses accepted evidence map and active program synthesis, handles
      pending irreducible owner facts through reduced/conservative mode or at most
      one material clarifier, authorizes only the graph-selected artifact family,
      and produces the bounded first-cycle start packet or writer packet without
      asking the owner to choose expert variables.
    evidence_expected: >
      Graph-selected state path, cited evidence/synthesis references, pending fact
      handling, first-cycle start packet or writer packet, and proof that menu/cycle
      content is a projection rather than decision authority.
  - id: t-3
    kind: guide
    surface: Health AI
    status: queued
    goal: >
      Days 1-3 of the first nutrition cycle are completed in Health AI and day-3
      safety/friction check produces a clear continue/conservative/review signal.
    done_when: >
      Health AI records only Health AI nutrition LOG summaries from free-form owner
      updates, accepts messy text/voice/photo-style input without forcing templates,
      checks hunger, energy, adherence, fallback use, prep friction, and red flags,
      and returns a day-3 summary/decision/problem suitable for Direction OS without
      raw diary content.
    evidence_expected: >
      Day-3 Health AI summary, safety/friction verdict, conservative branch if used,
      and Direction OS-safe summary with raw daily content omitted.
  - id: t-4
    kind: guide
    surface: Health AI
    status: queued
    goal: >
      Days 4-8 of the first nutrition cycle are completed and Health AI performs
      the day-8 first-cycle review from summaries, owner feedback, and core metrics.
    done_when: >
      Health AI completes the remaining first-cycle days, runs day-8 review, names
      exactly one review decision class or bounded mutation/repair route, keeps raw
      diary content inside Health AI only, and produces Direction OS-safe summary,
      decisions, problems, and recommended next CALL.
    evidence_expected: >
      Day-8 review summary, review decision class, mutation/repair target if any,
      no-raw-Direction-OS-diary proof, and recommended next Direction OS CALL.
  - id: t-5
    kind: session
    play: review
    status: queued
    goal: >
      First nutrition-cycle evidence is refuted or accepted as meeting the shaped
      bet, and the next health bet is chosen from strategic summary only.
    done_when: >
      A fresh review/refutation checks t-1 through t-4 evidence against done_when,
      kill_by, cut list, lens sweep, raw-data boundary, workflow-router authority,
      day-3 check, and day-8 review; if met, it closes the bet; if not, it routes
      to the exact failed repair layer.
    evidence_expected: >
      RESULT from review session with verdict, blocker gaps, state_changes, and
      next CALL.

open_calls:
  - id: c-health-first-nutrition-cycle-t1-startup-router-001
    status: ready
    note: >
      First task of b-health-first-nutrition-cycle-001: Health AI startup from
      normal owner message must prove repo-grounded current state and one bounded
      next action before any execution content.

recurring: []

decisions: []

next: |
  CALL c-health-first-nutrition-cycle-t1-startup-router-001
  to: session
  direction: health
  play: guide
  node: g-health-first-nutrition-cycle
  task: t-1
  goal: |
    Health AI startup from a normal owner message has a repo-grounded current
    nutrition state and exactly one bounded next action, with no unauthorized
    execution content.
  context: |
    Active bet:
    - live/health/NOW.md
    - live/health/TREE.md node g-health-first-nutrition-cycle

    Accepted prerequisite evidence:
    - health-ai commit 50f2215118c190ff959b7e21cda0715d368b243c
      ("Repair nutrition evidence workflow")
    - `python tools/check_nutrition_evidence_workflow.py` in health-ai reported:
      PASS; evidence map claims 10; synthesis decisions 10; negative fixtures rejected;
      blocker gaps 0.
    - live/health/knowledge/health-nutrition-workflow-authority-g5-review.md
    - live/health/knowledge/health-nutrition-system-g5-review.md

    Product surfaces to load or verify:
    - health-ai/CHATGPT_PROJECT.md
    - health-ai/AGENTS.md
    - health-ai/SYSTEM.md
    - health-ai/x_nutrition/index.md
    - health-ai/x_nutrition/workflow/graph.md
    - health-ai/x_nutrition/state/current-workflow.md
    - health-ai/x_nutrition/procedures/workflow-router.md
    - health-ai/x_nutrition/procedures/research-to-program.md
    - health-ai/x_nutrition/reference/evidence-reference.md
    - health-ai/x_nutrition/program-synthesis/active-program-synthesis.md
    - health-ai/acceptance/x_nutrition/provider-startup-owner-journey.md
    - health-ai/tools/check_nutrition_evidence_workflow.py

    Current product cursor observed during shape:
    - `x_nutrition/state/current-workflow.md` has current_state STARTUP_ROUTER,
      allowed_next_states ["PROGRAM"], selected_output_artifact_family null,
      owner_input_needed false, blocked false, and router_preflight_required true.

    Direction OS state note:
    - The CALL mentions `live/health/knowledge/health-nutrition-evidence-workflow-g5-review.md`,
      but that knowledge file was not present locally during shape. Use the product
      commit/check evidence above plus the CALL's accepted review context; if this
      absence blocks confidence, return a repair/audit recommendation rather than
      inventing state.
  boundaries: |
    Do not store raw daily food logs, photos, check-ins, menus, grocery execution,
    or daily diary content in Direction OS.
    Do not bypass Health AI workflow graph, current-workflow cursor, or workflow-router.
    Do not emit real menus, recipes, grocery lists, shopping instructions, daily
    plans, raw LOG dumps, fallback meals, or review walls before the selected graph
    state authorizes that artifact family.
    Do not ask the owner to choose expert nutrition variables.
    Do not move into training/activity implementation.
    Do not rebuild nutrition architecture.
    Do not make medical diagnoses or prescriptions.
  done_when: |
    Owner can start with a normal Health AI message; Health AI reports the current
    nutrition state and exactly one bounded next action; repo-backed state evidence
    is named if any transition is claimed; no unauthorized execution content is
    emitted; and the result is summarized for Direction OS without raw diary content.
  return: |
    RESULT with startup transcript/summary, resolved state, bounded next action,
    state evidence or writer packet, no-bypass/no-raw-diary proof, state_changes,
    and next CALL.
  budget: one tight guide session

END_OF_FILE: live/health/NOW.md
