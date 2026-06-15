# NOW — health

active_bet:
  id: g-health-core
  status: active
  appetite: 3 focused half-days
  kill_by: >
    2026-06-19: if there is not a committed health-ai core-only slice with zero
    blocker gaps against WA1-WA12 + W69/W70/W72/W73/W74 + CA1-CA9, plus passing
    YAML/formula/dry-run evidence, stop and review instead of extending.
  goal: >
    Сильное ядро Health AI System создано как провайдеро-независимая файловая система
    (Markdown/YAML в git): держит здоровье-состояние, программы-как-план, ежедневный
    трекинг и общий слой метрик/фаз/ревью; принимает ввод обычным текстом/голосом/фото;
    управляется любым LLM без проприетарной памяти.
  done_when:
    - health-ai contains a committed core-only slice satisfying copied acceptance WA1-WA12
      plus W69/W70/W72/W73/W74 and contracts CA1-CA9 from work/converge-g-health-core.md.
    - PLAN-agenda P1-P27 is carried as implementation input evidence, not promoted into
      Direction OS done_when.
    - The slice is verifiable without nutrition/training modules through a minimal core-only
      program/day fixture.
    - Direction OS remains strategic-only and raw daily data is not duplicated here.
    - Product repo clearing was explicitly owner-confirmed before any destructive wipe.
  evaluator: >
    After t-3, review/refutation must try to break the done claim. A Codex validator may
    only be an intra-family pre-pass; binding G5 verification needs a separate cross-family
    pass, ideally Claude.
  rollback: >
    health-ai is dirty input, not authority. Before clearing it, the executor must record the
    current branch/status and receive explicit owner confirmation; without that confirmation
    the task blocks rather than wiping. Git history preserves the previous repo state.
  cut_list:
    - Cut nutrition module: menus, recipes, meal-prep, grocery lists, nutrition reviews.
    - Cut training/activity module: Hevy/Strava/VR/wearables, full strength progression, conditioning.
    - Cut app UI, server, DB, runtime, cron, and automatic schedulers.
    - Cut full food/exercise library; only minimal fixtures are allowed.
    - Cut objective recovery metrics such as HRV/RHR/sleep-device data.
    - Cut automatic cross-provider sync.
    - Cut raw daily data in Direction OS.
    - Cut product-repo wipe authorization from shape; executor must ask before clearing health-ai.
  lens_sweep:
    - weight-nutrition: >
        Needs work only through core-owned weight/trend and the minimum tracked-signal principle;
        nutrition outputs are cut to the parked nutrition module.
    - strength-body-composition: >
        Needs work only through phase/value grammar and future module attach contracts;
        training programming is cut to the parked training/activity module.
    - activity-conditioning: >
        Not needed beyond generic phase/LOG hooks and future attach points; activity implementation is cut.
    - adherence-relapse: >
        Needs work through anti-bloat, non-blocking questions, graceful defaults, reduced mode,
        and review cadence.
    - medical-safety: >
        Needs work through red-flag halt, conservative defaults, non-diagnostic wording, and
        no medical prescriptions.
    - ai-system-data-architecture: >
        Primary lens; covered by the provider-independent file core, convention carriers,
        schema/versioning, PLAN-vs-LOG, parse/library surface, review seam, and module contracts.
  assumptions:
    - The converged spec is buildable as a small core-only file system in 3 focused half-days.
    - A minimal core-only fixture can test WA3/WA4/WA73 before any module exists.
    - Provider-independence evidence can be produced with files, formulas, linting, and dry-runs,
      not by building an app/runtime.
    - The executor can keep the slice from expanding into nutrition/training implementation.
  forecast: >
    A hard core-only cut should produce a buildable Health AI foundation without spending the bet
    on module details or product UI.
  against: >
    The strongest case against is that the copied acceptance/contract matrix is too large for
    3 focused half-days, or that provider-independence cannot be evidenced without a heavier harness.

tasks:
  - id: t-1
    node: g-health-core
    status: done
    kind: executor
    goal: >
      In health-ai, after explicit owner confirmation before any repo clearing, produce a committed
      acceptance harness and core-only fixture map that proves the converged spec is buildable
      without nutrition/training modules.
    done_when:
      - Owner wipe confirmation is recorded before any clearing, or the task returns blocked without clearing.
      - The repo contains a committed acceptance matrix carrying WA1-WA12 + W69/W70/W72/W73/W74 + CA1-CA9.
      - The matrix maps each acceptance/contract row to a concrete file, fixture, check, or explicit gap.
      - A minimal core-only program/day fixture is present or precisely specified for WA73.
      - The task reports whether any blocker gap exists before broader implementation.

  - id: t-2
    node: g-health-core
    status: done
    kind: executor
    goal: >
      Build the minimal provider-independent core file-system slice in health-ai.
    done_when:
      - Core files cover schema_version/migration notes, profile owner_facts/derived_anchors,
        program-as-plan, PLAN/LOG separation, formulas/rounding, shared metrics/phase/review,
        parse/library surface, procedure/extension registry, and convention carriers.
      - AGENTS.md, CLAUDE.md, and portable system-prompt carry the determinism-load-bearing checklist.
      - YAML/frontmatter parsing and documented formula checks pass on the core-only fixture.
      - No app UI, runtime, DB, cron, nutrition module, or training module is built.

  - id: t-3
    node: g-health-core
    status: done
    kind: executor
    goal: >
      Validate the core-only slice and package evidence for G5 review.
    done_when:
      - Dry-runs with synthetic/minimal seed data cover deterministic derived numbers, anchor cascade,
        PLAN-vs-LOG separation, parse/library lookup, red-flag halt, graceful default/reduced mode,
        slug immutability, dummy module attach, and zero Direction OS dependency.
      - Evidence summary maps every copied acceptance/contract row to pass/fail output.
      - Remaining gaps are classified; zero blocker gaps are required to close the bet.
      - Next review CALL is ready.

recurring: []

open_calls:
  - id: c-health-core-review-001
    to: session
    for: g-health-core review
    issued: 2026-06-15
    note: >
      Fresh review/refutation of g-health-core. Binding G5 should be cross-family,
      ideally Claude; Codex can only be a same-family pre-pass.

decisions: []

next: |
  CALL c-health-core-review-001
  to: session
  direction: health
  play: review
  node: g-health-core
  goal: |
    g-health-core has a verified bet verdict and the direction has a ready next-bet decision.
  context: |
    Direction OS state: live/health/CHARTER.md, live/health/TREE.md, live/health/NOW.md.
    Converged spec: live/health/work/converge-g-health-core.md.

    health-ai evidence so far:
    - t-1 commit a67a34e core acceptance harness: map converged spec; pushed to origin/main
    - t-2 commit ee25a89 core slice: replace v1 structure; pushed to origin/main
    - t-3 commit 8bc980a core evidence: package t-3 dry-run proof; pushed to origin/main
    - key evidence paths: acceptance/core/matrix.json, acceptance/core/evidence-summary.md,
      acceptance/core/fixtures/core-only/fixture.json, tools/check_acceptance_matrix.py,
      tools/check_core_slice.py, tools/check_core_evidence.py
    - wipe evidence: acceptance/core/clearance.md records owner confirmation before t-2 destructive clear.
    - latest checks after t-3:
      python tools/check_acceptance_matrix.py => PASS; 17 acceptance rows, 9 contract rows,
      27 PLAN rows, 9 architecture inputs, blocker gaps 0.
      python tools/check_core_slice.py => PASS; 32 core files, schema/frontmatter ok,
      matrix target files ok, WA73 formula check ok, PLAN/LOG separation ok,
      forbidden module/runtime directories absent.
      python tools/check_core_evidence.py => PASS; 11 dry-run scenarios, 26 acceptance/contract
      rows pass, 0 fail, blocker gaps 0; non-blocking gaps P8 and existing-v1-input.
    - G5 note: t-3 was executed by Codex/OpenAI. A Codex validator can only do a same-family
      pre-pass; binding G5 verification should be a fresh cross-family pass, ideally Claude.
  boundaries: |
    Do not store raw daily health data in Direction OS.
    Do not build or change product repo implementation during review.
    Do not build nutrition/training/activity modules, app UI, runtime, DB, server, cron, or scheduler.
    Do not make medical prescriptions.
    Do not treat the Codex t-3 pass as the binding cross-family G5 pass.
  done_when: |
    - g-health-core has a review verdict: met, partially met, or not met.
    - The verdict explicitly handles WA1-WA12 + W69/W70/W72/W73/W74 + CA1-CA9, check output,
      gap classification, and the cross-family G5 status.
    - Direction state is updated according to the review verdict, with any TREE changes owner-approved.
    - The next-bet decision is ready or awaiting owner decision.
  return: |
    RESULT with review verdict, refutation evidence, state_changes, decisions_needed, and next CALL/awaiting_decision.
  budget: one review session
  surface: Claude preferred for binding cross-family G5; Codex only for same-family pre-pass

END_OF_FILE: live/health/NOW.md
