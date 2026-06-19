# NOW — health

active_bet:
  status: none
  note: >
    No active bet. The workflow authority gate bet met review/refutation in
    s-health-nutrition-workflow-authority-review-004 on 2026-06-18:
    health-ai graph/current-workflow/router/writer validation passed WG1-WG14
    and WGA0-WGA15 checks with blocker_gaps=0, and no nutrition execution content
    was introduced. A repo-backed ChatGPT Project/bootstrap repair is now visible
    in health-ai commits 7a872c7 and 7303ac4, and continuation checks pass, but
    the owner's subsequent ChatGPT Project transcript revealed a deeper product
    defect: the operator can still trust chat claims as state, skip from startup
    to seed/menu artifacts, and produce nutrition choices without a current
    evidence/import/program-synthesis lifecycle. Next is a full health-ai
    nutrition evidence-workflow repair; real nutrition execution remains blocked.

tasks: []

open_calls: []

recurring: []

decisions: []

next: |
  CALL c-health-ai-nutrition-evidence-workflow-repair-001
  to: executor
  direction: health
  repo: ainazemtsau/health-ai
  kind: engineering
  node: g-health-nutrition-system
  goal: |
    Health AI nutrition startup and continuation are repaired so the owner can
    begin nutrition from a normal ChatGPT Project message while every material
    nutrition decision is repo-backed, current-evidence-backed, task-scoped, and
    explainable; no program, cycle, menu, timing, fasting, tracking, or food choice
    is produced from operator guesswork, stale seeds, or unverified chat claims.
  context: |
    Prior accepted state:
    - live/health/knowledge/health-nutrition-workflow-authority-g5-review.md:
      workflow authority review passed on 2026-06-18 with WG1-WG14 and WGA0-WGA15,
      blocker_gaps=0, and no nutrition execution content introduced.
    - health-ai commits 7a872c7 and 7303ac4 added a repo-backed ChatGPT Project
      entrypoint, synthetic owner journey proof, and bootstrap negative probes.
      `python tools/check_nutrition_continuation.py` currently reports pass with
      blocker gaps 0 and ChatGPT Project bootstrap/journey checks passing.

    New owner-proven defect:
    In a ChatGPT Project transcript starting with "Хочу начать питание", the
    operator initially followed STARTUP_ROUTER correctly and emitted a writer
    packet, but then accepted the owner's phrase "пакет применен" as if durable
    repo state had changed. The visible health-ai repo still shows
    `x_nutrition/state/current-workflow.md` at STARTUP_ROUTER. The operator then
    claimed PROGRAM/WEEK_PLAN, treated seed artifacts as active authority, and
    proposed a menu/food substitutions with insufficient evidence chain. It later
    admitted the menu was heuristic.

    Owner clarified the required repair:
    - Direction OS owns the formal repair and emits an engineering CALL; Health AI
      does not self-invent architecture from chat.
    - One chat equals one task, adapted for Health AI. A daily DAY_LOOP/tracking
      chat may continue across several updates, but setup/research/program/cycle/
      menu/review/mutation should be task-scoped and resumable from repo.
    - A non-code ChatGPT Project chat must never claim a durable state transition
      without commit SHA, diff evidence, or a fresh repo read proving the change.
      The owner's phrase "packet applied" is not evidence by itself.
    - Current/best-practice nutrition claims require current evidence. Health AI
      must generate a separate ChatGPT Deep Research request when evidence is
      missing, stale, or insufficient; the owner runs that in a separate Deep
      Research chat; the report is imported/validated into repo before program
      synthesis.
    - Research scope must be dynamic from owner goal/context and current evidence,
      not a hardcoded list. It must discover and compare relevant practices such
      as timing, fasting/TRE, meal frequency, protein, calories/day vs week,
      tracking modes, high-satiety strategy, prep/fallback, training interaction,
      safety, and any other material current practices found by research.
    - Menu/recipes/grocery/fallback are not primary decision artifacts. They are
      execution renders/projections of an accepted program and cycle. The owner
      must be able to see why a meal exists, what evidence/context it follows,
      what alternatives were rejected, and when to revisit it.
    - Program/cycle construction must be explainable end to end: owner facts used,
      evidence used with source freshness, rejected alternatives, operational
      rules, tracking/review signals, mutation triggers, and refresh routes.
    - If training starts, hunger/energy/adherence changes, weight trend stalls,
      safety context changes, or prep/tracking fails, Health AI must resume at the
      correct layer (evidence refresh, program synthesis, cycle, execution render,
      review, or mutation), not rebuild blindly and not continue silently.

    Current product surfaces likely relevant:
    - CHATGPT_PROJECT.md
    - SYSTEM.md
    - AGENTS.md
    - CLAUDE.md
    - x_nutrition/index.md
    - x_nutrition/workflow/graph.md
    - x_nutrition/state/current-workflow.md
    - x_nutrition/procedures/workflow-router.md
    - x_nutrition/procedures/provider-continuation.md
    - x_nutrition/procedures/writer-handoff.md
    - x_nutrition/procedures/research-to-program.md
    - x_nutrition/state/first-setup-pending.md
    - x_nutrition/state/normalizer-summary.md
    - x_nutrition/research/deep-research-packet.md
    - x_nutrition/research/first-owner-deep-research-report.json
    - x_nutrition/reference/method-landscape.md
    - x_nutrition/reference/evidence-reference.md
    - x_nutrition/programs/active-program.md
    - x_nutrition/cycles/first-cycle.md
    - x_nutrition/menus/current-menu-cycle.md
    - acceptance/x_nutrition/provider-continuation-matrix.json
    - acceptance/x_nutrition/project-bootstrap-negative-fixtures.json
    - tools/check_nutrition_continuation.py
    - tools/check_nutrition_research_setup.py

    Known inconsistency to handle:
    `x_nutrition/procedures/research-to-program.md` still carries
    `status: active_procedure_pending_first_report` and says first setup is
    pending until a report exists, while `x_nutrition/state/first-setup-pending.md`
    and `x_nutrition/state/normalizer-summary.md` say the first Deep Research
    report was accepted and normalized. Repair or explicitly resolve this.
  boundaries: |
    Do not start real owner nutrition execution.
    Do not create real owner menus, grocery lists, shopping instructions, daily
    plans, daily food logs, or actual nutrition prescriptions.
    Synthetic examples/fixtures are allowed only if clearly marked synthetic,
    non-authoritative acceptance evidence and not to be followed as the owner's
    real nutrition plan.
    Do not move into training/activity implementation.
    Do not rewrite g-health-core or redefine core-owned concepts.
    Do not add app UI, runtime, DB, server, cron, scheduler, or background worker.
    Do not edit Direction OS repo files from this executor.
    Do not make uploaded snapshots, provider memory, or chat transcript claims
    durable state when GitHub/repo access is available.
    Do not ask the owner to choose expert nutrition variables.
    Do not make medical diagnoses or prescriptions.
  allowed_files_or_surfaces: |
    You may edit or add only the Health AI carrier, nutrition workflow,
    research/evidence/program-synthesis, handoff, journey, and validation surfaces
    needed for this repair:
    - SYSTEM.md
    - AGENTS.md
    - CLAUDE.md
    - CHATGPT_PROJECT.md
    - README.md if present
    - x_nutrition/index.md
    - x_nutrition/workflow/graph.md
    - x_nutrition/state/current-workflow.md
    - x_nutrition/state/first-setup-pending.md
    - x_nutrition/state/normalizer-summary.md
    - x_nutrition/procedures/workflow-router.md
    - x_nutrition/procedures/provider-continuation.md
    - x_nutrition/procedures/writer-handoff.md
    - x_nutrition/procedures/research-to-program.md
    - new or updated nutrition session/research/evidence/program-synthesis
      procedures under x_nutrition/procedures/
    - x_nutrition/research/deep-research-packet.md and schema/reference surfaces
      only as needed for dynamic Deep Research handoff/import contracts
    - x_nutrition/reference/* only as needed to carry evidence-map/freshness
      contracts or synthetic acceptance evidence
    - x_nutrition/programs/* and x_nutrition/cycles/* only for contracts/seeds/
      synthetic examples, not real owner execution changes
    - x_nutrition/menus/*, grocery/*, fallbacks/*, logs/*, reviews/* only for
      contract wording or synthetic fixtures; do not produce real execution
    - acceptance/x_nutrition/provider-continuation-matrix.json
    - acceptance/x_nutrition/project-bootstrap-negative-fixtures.json
    - new focused negative fixture files if needed
    - tools/check_nutrition_continuation.py
    - tools/check_nutrition_research_setup.py
    - optionally new focused checks for session contract, Deep Research handoff,
      evidence import, or program synthesis
    - owner journey proof docs/fixtures under acceptance/x_nutrition/ or
      x_nutrition/handoffs/

    If the executor finds a contradiction outside these surfaces that prevents
    the repair from being truthful, stop and return STUCK with exact files and
    contradiction. Do not silently widen scope and do not paper over it with prose.
  mandatory_investigation: |
    Before editing, inspect the existing provider/client, workflow, writer,
    research-to-program, and acceptance surfaces. Classify defects explicitly in
    the executor RESULT:
    - repo bootstrap/journey already fixed or still insufficient;
    - operator session contract gap;
    - durable-state evidence gap;
    - seed artifact authority gap;
    - Deep Research handoff/import gap;
    - evidence freshness/current-practice claim gap;
    - program synthesis / execution-render architecture gap;
    - validation/negative-fixture gap;
    - broader contradiction that blocks truthful repair.

    If the repair cannot honestly be completed in the allowed surfaces, return
    STUCK with exact blockers and a ready next repair CALL. Do not fake a pass.
  done_when: |
    A committed health-ai repair exists such that:

    1. Health AI has a repo-owned operator/session contract aligned with Direction
       OS: one chat = one task, with DAY_LOOP/tracking explicitly allowed to
       continue only within the same resolved tracking state; setup, research,
       evidence import, program synthesis, cycle design, execution render, review,
       and mutation are task-scoped and resumable from repo.

    2. Non-code ChatGPT/Claude operator chats cannot claim durable state changes
       without evidence. A workflow transition requires either committed repo
       state, a visible diff/patch applied by a writer, or a fresh repo read
       proving the transition. Owner text such as "packet applied" is not enough.

    3. Nutrition workflow no longer lets seed program/cycle/menu/grocery/fallback/
       LOG/review artifacts act as startup authority. Startup and continuation
       must resolve one state and one artifact family from graph+cursor+router;
       seed artifacts are evidence only until graph-selected.

    4. Nutrition startup includes or routes through an explicit lifecycle
       equivalent to intake -> dynamic research planner -> separate ChatGPT Deep
       Research handoff -> evidence import/validation -> evidence map/currentness
       check -> program synthesis -> cycle design -> execution render -> DAY_LOOP/
       review/mutation. Naming may differ, but the lifecycle must be mechanically
       represented and validated.

    5. The dynamic research planner creates a Deep Research request from the
       current owner goal, known owner facts, pending facts, and current evidence
       gaps. It must not rely on a hardcoded topic checklist as the authority; it
       must discover and compare material practices from current sources and
       record why each included or excluded practice matters for the owner.

    6. The Deep Research flow is an explicit separate-chat handoff: Health AI
       prepares a prompt for ChatGPT Deep Research, the owner runs it in a fresh
       Deep Research chat, and the returned report is imported into repo by a
       writer before it can authorize program synthesis. If browsing/deep research
       is unavailable, Health AI produces a research handoff instead of deciding.

    7. Evidence artifacts carry source freshness and claim authority. Any claim
       about "current", "best practice", fasting/16:8/TRE, meal timing, meal
       count, protein, calories/day vs week, calorie tracking vs rough tracking,
       high-satiety strategy, prep/fallback, training interaction, or safety must
       cite accepted evidence with searched_at/source metadata or be marked
       pending/insufficient.

    8. Program synthesis is a first-class product surface, not hidden prose. It
       records selected strategy, owner facts used, evidence used, rejected or
       conditional alternatives, operational rules, tracking/review signals,
       mutation triggers, refresh routes, and unresolved owner facts/reduced-mode
       consequences. It asks the owner only irreducible facts and never asks the
       owner to choose expert variables.

    9. Menus, recipes, grocery/prep, fallback meals, and daily execution outputs
       are execution renders/projections of an accepted program and cycle. A menu
       cannot be treated as the place where major strategy decisions are made, and
       each material meal/template choice must be traceable to program/cycle
       rationale, owner context, evidence, substitution rules, and revisit triggers.

    10. Reviews and mutations route to the correct layer. Hunger, energy, weight
        trend, adherence, safety, training start/change, cooking friction, tracking
        burden, food fatigue, travel, or medical changes must resume at evidence
        refresh, program synthesis, cycle design, execution render, review, or
        mutation as appropriate, rather than rebuilding blindly or continuing
        silently.

    11. The `research-to-program.md` pending-first-report inconsistency is resolved
        truthfully against the accepted first report / normalizer state, without
        pretending that real current evidence has already been refreshed if it has
        not.

    12. Owner-facing journey evidence is updated with detailed synthetic examples
        covering both successful and failing paths: startup, intake, Deep Research
        handoff, evidence import, program synthesis, cycle, execution render/menu,
        day-3 check, day-8 review, weeks 2-4, new recipe, training start, hunger/
        energy failure, prep failure, stale evidence, and provider/client handoff.

    13. Validation is strengthened so the defect cannot silently return. Checks or
        negative fixtures fail if:
        - menu/recipe/grocery/daily plan appears before graph-selected execution
          render;
        - seed artifacts are treated as active authority;
        - "repo is now PROGRAM/WEEK_PLAN" is claimed without commit/diff/re-read
          evidence;
        - pending allergy/medical facts are deleted or treated as known without
          owner evidence;
        - current/best-practice claims are made without searched_at/source
          metadata or accepted evidence;
        - 16:8/TRE, meal timing, meal count, tracking mode, calories, or protein
          decisions are made from owner mention or operator preference instead of
          evidence+context;
        - program synthesis is bypassed before cycle/menu rendering;
        - one chat bundles unrelated states or artifact families outside the
          permitted DAY_LOOP continuation.

    14. Existing checks pass and any new checks pass. Required minimum commands:
        - python tools/check_acceptance_matrix.py
        - python tools/check_core_slice.py
        - python tools/check_core_evidence.py
        - python tools/check_nutrition_research_setup.py
        - python tools/check_nutrition_full_module.py
        - python tools/check_nutrition_continuation.py
        - plus any new checks added by this repair.

    15. The executor RESULT includes commit SHA, changed files, exact check output,
        blocker_gaps count, defect classification, paths to changed workflow/
        research/evidence/program-synthesis/journey artifacts, a concise owner
        summary of the new journey, and a ready fresh review/refutation CALL.
  return: |
    RESULT from executor with commit SHA, changed files, check output, blocker_gaps,
    defect classification, changed artifact paths, owner-readable summary of the
    repaired journey, and a ready review/refutation CALL.

    If the executor finds that the defect is broader than this allowed repair and
    cannot be fixed truthfully, return STUCK with exact blockers, exact files, and
    recommended next repair CALL. Do not produce a fake pass.
  budget: one focused half-day

END_OF_FILE: live/health/NOW.md
