# NOW — health

active_bet:
  id: b-health-hq-goal-coordinator-v0-001
  node: g-health-hq-goal-coordinator
  status: active
  appetite: 5 calendar days
  started: 2026-07-01
  kill_by: >
    2026-07-06 end-of-day Europe/Amsterdam. Kill/review if by this date Health AI cannot show
    evidence that Health HQ v0: holds explicit top-level goal structure; accepts one owner-triggered
    request such as "проверь прогресс", "разбери неделю", "где bottleneck?", or "что сегодня?";
    consumes nutrition and training/activity summary/report adapters with clearly marked fixtures
    where real data is insufficient; produces a progress verdict, bottleneck/uncertainty, routed
    correction requests, owner decisions if needed, and metrics needed now/later; preserves the
    Direction OS raw-data boundary; does not silently edit nutrition/training/activity artifacts;
    and does not add dashboard/API/polling/full architecture or out-of-scope domains.
  goal: >
    Health HQ v0 is the owner-facing front door for on-demand health goal review across nutrition,
    training/activity, current phase, phase metrics, domain responsibilities, review/decision log,
    and routed correction requests.
  done_when:
    - There is explicit top-level goal structure: root health goals, current phase, phase metrics,
      domain responsibilities, and review/decision log.
    - Health HQ accepts owner requests like "что сегодня?", "разбери неделю", "проверь прогресс",
      and "где bottleneck?".
    - There is a minimal domain integration contract for current/future domains: responsibility,
      supported goals, summary/report format for HQ, metrics/signals exposed to HQ, accepted
      correction/request types, and boundaries for what HQ does not change directly.
    - Nutrition and training/activity have at least thin summary/report adapters for HQ, using
      clearly marked sample/test fixtures where real data is sparse.
    - Health HQ conducts one dry-run or partial-real goal review across nutrition, training/activity,
      and goal state.
    - Review output includes progress verdict, bottleneck/uncertainty, routed requests into domains,
      owner decisions if needed, and which metrics are needed now/later.
    - Health HQ does not silently change domain artifacts; it routes correction through domain
      procedures and owner/governance gates.
    - Direction OS receives only summary, decisions, problems, and next CALL; raw body/nutrition/
      training data stays outside Direction OS.
  proof_target: >
    One committed Health AI evidence bundle showing a thin HQ structure/namespace or equivalent
    product slice; explicit goal/current-phase/metrics/domain-responsibility/review-log structure;
    minimal domain integration contract; nutrition and training/activity thin summary/report
    adapters or fixtures; one owner-triggered dry-run or partial-real review; review output with
    verdict, bottleneck/uncertainty, routed correction request(s), owner decisions if needed, and
    needed metrics; and evidence that HQ did not silently mutate domain artifacts or put raw data
    into Direction OS.
  cut_list:
    - visual dashboard/cockpit UI
    - automatic polling/scheduled self-checking
    - Hevy/Strava/wearable/API integrations
    - raw body/nutrition/training data in Direction OS
    - full future architecture/general integration platform
    - cooking, habit, sleep, and medical domains
    - gameful engine/challenges
    - direct domain artifact edits by HQ
    - requirement for full real weekly data
    - optimizer/adaptive engine
  lens_sweep:
    - weight-nutrition: task_required via nutrition summary/report adapter and routed requests.
    - strength-body-composition: task_required via training/body-composition summary signals.
    - activity-conditioning: task_required via coarse activity/conditioning signals and bottleneck routing.
    - adherence-relapse: task_required via drift, missed checks, friction, relapse risk, and owner decisions.
    - medical-safety: task_required via pain/symptom/red-flag surfacing and conservative routing; no diagnosis.
    - ai-system-data-architecture: primary_task_required via summary-only HQ/domain contract and boundaries.
  assumptions:
    - A thin HQ can produce useful cross-domain coordination from summary/report adapters or fixtures
      without becoming a new core, dashboard, polling system, or silent domain editor.
    - Nutrition and training/activity can expose HQ-ready summaries without major refactor and without raw logs.
    - Owner-triggered review is sufficient for useful management; automatic polling is not needed for v0.
    - Routed correction requests are specific enough for domain procedures to act on later.
    - Owner accepts a text front door and decision log instead of a visual dashboard.
  forecast: >
    Moderately favorable if kept to a summary-only coordinator: approximately 65-75% chance of a useful
    v0 proof inside appetite; lower, approximately 40-50%, if the work drifts into full architecture,
    UI/dashboard, API integrations, or real-data completeness.
  against: >
    Health HQ may duplicate g-health-core or become a god-agent/cockpit; nutrition/training adapters may
    require more domain cleanup than expected; fixture proof may feel artificial unless it produces a
    concrete routed correction request.
  next_if_true: >
    Health HQ v0 becomes the owner-facing front door for on-demand health goal review. Next likely work:
    run the first partial-real HQ review and route any concrete correction request into nutrition or
    training/activity through that domain's governance path.
  next_if_false: >
    Kill or cut Health HQ v0. Return to the narrowest useful alternative: either a 3-day review-prompt-only
    proof, or resume body-execution work in nutrition/training before attempting HQ again.

tasks:
  - id: t-1
    node: g-health-hq-goal-coordinator
    status: active
    kind: executor
    repo: C:\my_global_workflow_worktrees\health-ai
    goal: >
      Health AI has the smallest Health HQ v0 proof as a thin summary-only coordinator for
      owner-triggered cross-domain review and routed correction requests.
    done_when: >
      Evidence shows: a thin HQ structure/namespace or equivalent product slice exists; goal structure,
      current phase, phase metrics, domain responsibilities and review-decision log are represented;
      minimal domain integration contract exists; nutrition and training/activity thin summary/report
      adapters or clearly marked fixtures exist; one owner-triggered dry-run or partial-real review
      produces progress verdict, bottleneck/uncertainty, routed correction request(s), owner decisions
      if needed, and needed metrics; python tools/check_kernel_spine.py passes or any failure is
      explained as pre-existing/non-HQ; no raw data is added to Direction OS; no dashboard/API/polling/
      full architecture is added; HQ does not silently mutate domain artifacts.
    evaluator: >
      Fresh Direction OS/session review in t-2 tries to refute the proof against the shaped boundaries.
    rollback_first: >
      If the proof requires core rewrite, API/UI/server/DB/cron, raw logs, or direct domain mutation,
      stop and return evidence; do not broaden. Revert/supersede only the HQ proof slice if needed.

  - id: t-2
    node: g-health-hq-goal-coordinator
    status: pending
    kind: session
    goal: >
      Refute t-1 evidence against the shaped bet.
    done_when: >
      Review verdict is one of: accept proof / rework within appetite / kill. It explicitly checks goal
      structure, review trigger, domain contracts, routed requests, raw-data boundary, and no silent edits.

  - id: t-3
    node: g-health-hq-goal-coordinator
    status: pending
    kind: executor
    repo: C:\my_global_workflow_worktrees\health-ai
    goal: >
      Health HQ v0 evidence is corrected, if t-2 found a small fix, and stable enough for one owner
      front-door request without fixed wording.
    done_when: >
      Corrected Health HQ v0 evidence exists, checks pass or are explained, and the returned closeout
      includes one plain owner-facing next prompt such as "проверь прогресс" / "что сегодня?" plus
      the expected non-raw input boundary.

  - id: t-4
    node: g-health-hq-goal-coordinator
    status: pending
    kind: guide
    goal: >
      Owner has run one Health HQ request in plain language and judged whether the response is a useful
      front door rather than just a reviewer or dashboard mock.
    done_when: >
      Owner response is captured as accept / needs change / reject. Evidence includes only summary,
      decision, problem, and next CALL; no raw health diary enters Direction OS.

  - id: t-5
    node: g-health-hq-goal-coordinator
    status: pending
    kind: session
    goal: >
      Health HQ v0 bet outcome is verified as done, killed, or narrowed into a follow-up.
    done_when: >
      Fresh review checks t-1..t-4 evidence against node done_when and kill_by. Direction OS receives
      only summary, decisions, problems, and next CALL.

open_calls:
  - id: c-health-hq-goal-coordinator-t1-executor-001
    to: executor
    direction: health
    node: g-health-hq-goal-coordinator
    task: t-1
    repo: C:\my_global_workflow_worktrees\health-ai
    kind: engineering
    goal: |
      Health AI has the smallest Health HQ v0 proof as a thin summary-only coordinator for owner-triggered cross-domain review and routed correction requests.
    context: |
      Direction OS state:
      - live/health/CHARTER.md
      - live/health/TREE.md
      - live/health/NOW.md
      - live/health/history/2026-06-29-c-health-map-evidence-001.md
      - live/health/history/2026-06-30-s-health-owner-wants-planning-001-continue.md
      - live/health/history/2026-06-30-s-health-shape-hq-goal-coordinator-001.md
      - live/health/history/2026-07-01-s-health-shape-hq-goal-coordinator-approval-001.md

      Target product repo:
      - Working copy: C:\my_global_workflow_worktrees\health-ai
      - Remote identity: ainazemtsau/health-ai
      - validation.config is synced to os-engineering-contract.v9.

      Shape-approved boundaries:
      - Health HQ v0 is a text-first coordinator/front door.
      - It owns goal structure view, current phase/phase metrics view, domain responsibility map,
        review/decision log, owner-triggered review procedure, domain integration contract shape,
        and routed correction request format.
      - It does not own nutrition menus/recipes/logs, training programs/weeks/session logs,
        medical advice/diagnosis, raw body/nutrition/training data, automatic polling, API
        integrations, dashboard UI, or direct domain artifact edits.
      - Proof may use clearly marked sample/test fixtures where real weekly data is sparse.
    boundaries: |
      Do not rewrite g-health-core.
      Do not add dashboard/API/server/DB/cron/polling/full architecture.
      Do not store raw body/nutrition/training data in Direction OS.
      Do not silently mutate nutrition/training/activity artifacts.
      Do not add cooking, habit, sleep, medical, or gameful-engine scope.
    done_when: |
      Evidence shows:
      - a thin HQ structure/namespace or equivalent product slice exists;
      - goal structure/current phase/phase metrics/domain responsibilities/review-decision log are represented;
      - minimal domain integration contract exists;
      - nutrition and training/activity thin summary/report adapters or clearly marked fixtures exist;
      - one owner-triggered dry-run or partial-real review produces progress verdict, bottleneck/uncertainty,
        routed correction request(s), owner decisions if needed, and needed metrics;
      - python tools/check_kernel_spine.py passes or any failure is explained as pre-existing/non-HQ;
      - no raw data is added to Direction OS;
      - no dashboard/API/polling/full architecture is added;
      - HQ does not silently mutate domain artifacts.
    return: |
      RESULT with product commit, changed files, check output, evidence bundle, explicit boundary check,
      captures, and next CALL.
    budget: one executor session

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
    last_done: 2026-06-28
    note: >
      Post-1338a35 bounded work was reconciled into this lane: menu workflow
      structure repair and owner_fact_delta/assumption hardening
      (7cd962a, 83dba88, 77a0ed), followed by fixed-menu/recipe support through
      health-ai 8246cec. On 2026-06-28 the lane handled the training/activity false
      launch-readiness repair in health-ai 1fe41c2: validation.config was re-synced to
      os-engineering-contract.v9, the training checker rejects the old ACTIVE/DAY_LOOP
      sample-launch state, and Health AI now blocks at PROGRAM awaiting Deep Research.
      The lane remains recurring/on-demand, not a second active bet. Authority, safety,
      provider-portability or owner-gate defects escalate to a bounded repair/executor
      CALL; cosmetic papercuts are batched, deferred or dropped.

decisions: []

next: |
  CALL c-health-hq-goal-coordinator-t1-executor-001
  to: executor
  direction: health
  node: g-health-hq-goal-coordinator
  task: t-1
  repo: C:\my_global_workflow_worktrees\health-ai
  kind: engineering
  goal: |
    Health AI has the smallest Health HQ v0 proof as a thin summary-only coordinator for owner-triggered cross-domain review and routed correction requests.
  context: |
    Direction OS state:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/history/2026-06-29-c-health-map-evidence-001.md
    - live/health/history/2026-06-30-s-health-owner-wants-planning-001-continue.md
    - live/health/history/2026-06-30-s-health-shape-hq-goal-coordinator-001.md
    - live/health/history/2026-07-01-s-health-shape-hq-goal-coordinator-approval-001.md

    Target product repo:
    - Working copy: C:\my_global_workflow_worktrees\health-ai
    - Remote identity: ainazemtsau/health-ai
    - validation.config is synced to os-engineering-contract.v9.

    Shape-approved boundaries:
    - Health HQ v0 is a text-first coordinator/front door.
    - It owns goal structure view, current phase/phase metrics view, domain responsibility map,
      review/decision log, owner-triggered review procedure, domain integration contract shape,
      and routed correction request format.
    - It does not own nutrition menus/recipes/logs, training programs/weeks/session logs,
      medical advice/diagnosis, raw body/nutrition/training data, automatic polling, API
      integrations, dashboard UI, or direct domain artifact edits.
    - Proof may use clearly marked sample/test fixtures where real weekly data is sparse.
  boundaries: |
    Do not rewrite g-health-core.
    Do not add dashboard/API/server/DB/cron/polling/full architecture.
    Do not store raw body/nutrition/training data in Direction OS.
    Do not silently mutate nutrition/training/activity artifacts.
    Do not add cooking, habit, sleep, medical, or gameful-engine scope.
  done_when: |
    Evidence shows:
    - a thin HQ structure/namespace or equivalent product slice exists;
    - goal structure/current phase/phase metrics/domain responsibilities/review-decision log are represented;
    - minimal domain integration contract exists;
    - nutrition and training/activity thin summary/report adapters or clearly marked fixtures exist;
    - one owner-triggered dry-run or partial-real review produces progress verdict, bottleneck/uncertainty,
      routed correction request(s), owner decisions if needed, and needed metrics;
    - python tools/check_kernel_spine.py passes or any failure is explained as pre-existing/non-HQ;
    - no raw data is added to Direction OS;
    - no dashboard/API/polling/full architecture is added;
    - HQ does not silently mutate domain artifacts.
  return: |
    RESULT with product commit, changed files, check output, evidence bundle, explicit boundary check,
    captures, and next CALL.
  budget: one executor session

END_OF_FILE: live/health/NOW.md
