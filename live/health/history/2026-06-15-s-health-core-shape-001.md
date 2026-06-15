RESULT s-health-core-shape-001 (call: c-health-core-shape-001)
direction: health   play: shape   node/task: g-health-core

outcome: |
  Owner approved option A. g-health-core is now the active bet with appetite
  3 focused half-days, kill_by 2026-06-19, three tasks, real cuts, a full lens
  sweep, and t-1 as the riskiest-assumption test. The next CALL is an executor
  CALL for health-ai t-1.

evidence: |
  Owner approval in-session:
  - Appetite approval: "A утверждаю"
  - Bet approval: "A."

  Source evidence:
  - live/health/TREE.md g-health-core outcome and parent g-health-root.
  - live/health/CHARTER.md lenses, constraints, risk_posture, product repo.
  - live/health/work/converge-g-health-core.md: converge set COMPLETE + refuted-clean;
    §WHAT-A WA1-WA12, pass-2 acceptance W69/W70/W72/W73/W74, §CONTRACTS CA1-CA9,
    §ARCH Q1-Q6/AA1-AA3, §PLAN-AGENDA P1-P27, §SIGNOFFs PASS.

state_changes: |
  TREE.md:
  - owner_approved: true
  - approval_evidence: >
      Owner approved the shaped bet option A: "A."
  - For node g-health-core:
      status: active
      appetite: 3 focused half-days
      kill_by: >
        2026-06-19: if there is not a committed health-ai core-only slice with zero
        blocker gaps against WA1-WA12 + W69/W70/W72/W73/W74 + CA1-CA9, plus passing
        YAML/formula/dry-run evidence, stop and review instead of extending.

  NOW.md:
  - Replace active_bet with:
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

  - Replace tasks with:
      - id: t-1
        node: g-health-core
        status: open
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
        status: open
        kind: executor
        goal: Build the minimal provider-independent core file-system slice in health-ai.
        done_when:
          - Core files cover schema_version/migration notes, profile owner_facts/derived_anchors,
            program-as-plan, PLAN/LOG separation, formulas/rounding, shared metrics/phase/review,
            parse/library surface, procedure/extension registry, and convention carriers.
          - AGENTS.md, CLAUDE.md, and portable system-prompt carry the determinism-load-bearing checklist.
          - YAML/frontmatter parsing and documented formula checks pass on the core-only fixture.
          - No app UI, runtime, DB, cron, nutrition module, or training module is built.
      - id: t-3
        node: g-health-core
        status: open
        kind: executor
        goal: Validate the core-only slice and package evidence for G5 review.
        done_when:
          - Dry-runs with synthetic/minimal seed data cover deterministic derived numbers, anchor cascade,
            PLAN-vs-LOG separation, parse/library lookup, red-flag halt, graceful default/reduced mode,
            slug immutability, dummy module attach, and zero Direction OS dependency.
          - Evidence summary maps every copied acceptance/contract row to pass/fail output.
          - Remaining gaps are classified; zero blocker gaps are required to close the bet.
          - Next review CALL is ready.
  - Set recurring: []
  - Set open_calls to:
      - id: c-health-core-t-1-executor-001
        to: executor
        for: t-1
        issued: 2026-06-15
        note: >
          health-ai core-only acceptance harness + fixture map. Must ask explicit owner confirmation
          before clearing the dirty product repo.
  - Set decisions: []
  - Set next to CALL c-health-core-t-1-executor-001 as below.

  LOG.md:
  - Append:
      2026-06-15 — health/g-health-core shape: owner approved option A; g-health-core activated with
      3 focused half-days, kill_by 2026-06-19, tasks t-1..t-3; next c-health-core-t-1-executor-001.

  history/:
  - Add this file: live/health/history/2026-06-15-s-health-core-shape-001.md.

captures:
  - Losing approach parked: PLAN/ADR-only before build; rejected because converge already closed WHAT/ARCH.
  - Losing approach parked: split g-health-core into child nodes; rejected because converge-arch found internal seams sufficient and no sub-nodes needed.

decisions_needed: []

play_check:
  - "1 Recite: done — g-health-core is an outcome node; parent is g-health-root; no outcome rewrite needed."
  - "2 Appetite first: done — owner approved option A, \"A утверждаю\" = 3 focused half-days to 2026-06-19."
  - "3 Approaches, then minimal solution: done — compared core-only slice, PLAN/ADR-only, and split; chose core-only slice."
  - "4 Scope hammer: done — real cuts recorded: modules, app/runtime/DB/cron, full libraries, objective recovery metrics, auto-sync, raw Direction OS data, and shape-time wipe authorization."
  - "5 Lens sweep: done — all six CHARTER lenses have verdicts in NOW.md."
  - "6 Riskiest assumption: done — top assumption is core-only buildability inside appetite; t-1 tests it first."
  - "7 Tasks: done — three executor tasks, each bounded to a focused half-day; t-1/t-2/t-3 recorded."
  - "8 Kill criteria: done — kill_by metric+threshold+date set; next_if_true is G5 review then module shaping; next_if_false is review kill/reshape/split depending on evidence."
  - "9 Close: done — owner approved option A: \"A.\""

log: "shape: owner approved option A; g-health-core activated with 3 focused half-days, kill_by 2026-06-19, tasks t-1..t-3; next c-health-core-t-1-executor-001."

next: |
  CALL c-health-core-t-1-executor-001
  to: executor
  direction: health
  node: g-health-core
  task: t-1
  repo: ainazemtsau/health-ai
  kind: engineering
  goal: |
    A committed health-ai acceptance harness and core-only fixture map show whether the converged
    g-health-core spec is buildable without nutrition/training modules.
  context: |
    Direction OS state: live/health/CHARTER.md, live/health/TREE.md, live/health/NOW.md.
    Converged spec: live/health/work/converge-g-health-core.md. The converge set is COMPLETE
    and refuted-clean: §WHAT-A WA1-WA12, pass-2 acceptance W69/W70/W72/W73/W74, §CONTRACTS
    CA1-CA9, §ARCH Q1-Q6 + AA1-AA3, §PLAN-AGENDA P1-P27, signoffs Define/Resolve/
    converge-arch/converge-verify=PASS.

    The product repo health-ai is dirty input, not authority. It will be cleared and rebuilt in
    place at build time only after explicit owner confirmation. Record current branch/status before
    any clearing. If the owner does not confirm the wipe, return blocked without clearing.

    PLAN agenda to carry as input evidence, not Direction OS done_when:
    P1 file/dir layout + YAML frontmatter schema; P2 resolve-on-read file layout; P3 chat-to-GitHub
    write-back path per provider; P4 formula/constant set + min-data window; P5 instruction-file
    budgets; P6 constrained-vocab literal tokens; P7 owner_facts/derived_anchors field table +
    rationale/evidence schema; P9 safety floor + protein magnitudes; P10 phase counts/weeks;
    P11 phase enum labels; P12 PLAN/LOG naming + frontmatter; P13 biofeedback scale items;
    P14 cadence magnitudes; P15 parse materiality cutoff + wording; P16 question-order weights;
    P17 confidence/source schema tokens; P18 food-record schema + source-id + slug grammar;
    P19 procedure-definition contract template; P20 extension registry path + line grammar +
    folder structure; P21 module attach-point + x_key syntax; P22 carb-by-day_type tiers;
    P23 schema_version + migration-note + back-compat reader rule; P24 rounding/precision
    magnitudes; P25 thin always-loaded index + lazy-load policy; P26 program-resume/re-anchor
    algorithm; P27 autonomy-dial labels.

    Architecture-on-paper input evidence: Q1 pure resolve-on-read; Q2 read-only git/connector
    Direction OS read; Q3 one entity per small file; Q4 additive namespaced extension over frozen
    core value grammar; Q5 two declarative extension classes; Q6 one-entity commit + lint barrier +
    append-only LOG + single-writer residual risk; AA1 work-actually-done progression; AA2 thin index
    + lazy-load context strategy; AA3 cache-vs-derive remains a PLAN fork only.
  boundaries: |
    Do not clear, delete, reset, or wipe health-ai until the owner explicitly confirms that action.
    Do not store raw daily health data in Direction OS.
    Do not build nutrition or training/activity modules.
    Do not build app UI, runtime, DB, server, cron, or automatic scheduler.
    Do not make medical prescriptions.
    The executor owns implementation details; keep Direction OS changes out of the product repo.
  done_when: |
    A commit or patch in health-ai produces the t-1 acceptance harness and fixture map:
    - Owner wipe confirmation is recorded before any clearing, or the task returns blocked without clearing.
    - Every copied acceptance row is present in the harness with a planned file/check/evidence target:
      WA1 Two providers reading the same files reach the same computed answer for any derived number.
      WA2 The system asks only for irreducible un-researchable personal facts + sustainable logging cadence.
      WA3 A daily prescription is verifiable as derived from anchors+formula, not stored as a literal.
      WA4 PLAN files and LOG files are non-overlapping.
      WA5 The three shared metrics are defined once in the core.
      WA6 Two providers parsing the same input against the same library files produce the same numeric record.
      WA7 Every parse/clarify question is non-blocking with graceful default and no re-ask.
      WA8 Adding a new domain requires exactly 1 folder + 1 registry line and no core rewrite.
      WA9 A module attaches as a thin additive layer and never edits any core file.
      WA10 Modules consume core-owned concepts and do not redefine or duplicate them.
      WA11 The Health AI repo contains zero reference to or dependency on Direction OS.
      WA12 Two providers operating the same core + attached module reach the same shared state.
      W69 The core declares the smallest tracked-signal set and biases adherence over completeness.
      W70 Red-flag/symptom halts progression, surfaces to owner, and recommends medical check non-diagnostically.
      W72 Minted slugs never change; relabels are display-only.
      W73 A minimal core-only program/day is exhibited from core-owned leaves alone.
      W74 Graceful-default-on-decline never fabricates irreducible owner_facts; reduced mode works.
    - Every copied contract is present in the harness with a planned file/check/evidence target:
      CA1 one-way Direction OS read visibility, zero Health AI dependency on Direction OS.
      CA2 daily prescription resolve-on-read from program + anchors.
      CA3 core publishes {phase, week, day} back-reference to LOG and modules.
      CA4 module attach reads phase + metric trio and writes only namespaced fields.
      CA5 coarse day_type provenance: logged overrides planned fallback for nutrition carb target.
      CA6 reusable template is core-owned, not nutrition-owned.
      CA7 core parse/library/value-grammar/procedure surface is reusable by modules.
      CA8 schema_version + forward migration is core-owned and inherited by modules.
      CA9 convention-carrier checklist is the determinism seam across providers.
    - A minimal core-only fixture exists or is precisely specified for WA73.
    - The task reports blocker gaps explicitly; zero blocker gaps are required to proceed cleanly to t-2.
  return: |
    RESULT with commit/patch evidence, check output if available, wipe-confirmation evidence or blocked status,
    blocker-gap list, and next CALL for t-2 if unblocked.
  budget: one focused half-day
  surface: Codex or Claude Code in product repo

END_OF_FILE: live/health/history/2026-06-15-s-health-core-shape-001.md
