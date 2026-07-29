RESULT s-health-shape-hq-goal-coordinator-001 (call: c-health-shape-hq-goal-coordinator-001)
direction: health   play: shape   node/task: g-health-hq-goal-coordinator

outcome: |
  Shaped bet proposal is ready for owner decision; no bet is activated and no tasks are created.

  Proposed bet:
    node: g-health-hq-goal-coordinator
    status_if_approved: active
    appetite: 5 calendar days from activation
    kill_by: |
      If activated on 2026-06-30, kill/review on 2026-07-05 end-of-day Europe/Amsterdam.
      If approved later, keep the same 5-calendar-day appetite and set kill_by to activation_date + 5 calendar days.

      Kill/review if by kill_by Health AI cannot show evidence that Health HQ v0:
      1. Holds explicit top-level goal structure: root health goals, current phase, phase metrics,
         domain responsibilities, and review/decision log.
      2. Accepts one owner-triggered request such as "проверь прогресс", "разбери неделю",
         "где bottleneck?", or "что сегодня?".
      3. Consumes nutrition and training/activity summary/report adapters, using clearly marked
         sample/test fixtures where real weekly data is insufficient.
      4. Produces a progress verdict, bottleneck/uncertainty, routed correction requests into domains,
         owner decisions if needed, and a list of metrics needed now/later.
      5. Does not store raw body/nutrition/training data in Direction OS.
      6. Does not silently edit nutrition/training/activity artifacts.
      7. Does not add visual dashboard, API/integration layer, automatic polling, gameful engine,
         cooking domain, habit system, sleep domain, medical domain, server, DB, cron, or broad future architecture.

    next_if_true: |
      Health HQ v0 becomes the owner-facing front door for on-demand health goal review.
      Next likely work: run the first partial-real HQ review and route any concrete correction request
      into nutrition or training/activity through that domain's governance path.
    next_if_false: |
      Kill or cut Health HQ v0. Return to the narrowest useful alternative:
      either a 3-day review-prompt-only proof, or resume body-execution work in nutrition/training
      before attempting HQ again.

  One-screen bet:
    appetite: 5 calendar days.
    forecast: |
      Moderately favorable if kept to a summary-only coordinator: approximately 65–75% chance of a
      useful v0 proof inside appetite. Lower, approximately 40–50%, if the work drifts into full
      architecture, UI/dashboard, API integrations, or real-data completeness.
    against: |
      The main countercase is that Health HQ may duplicate g-health-core or become a god-agent/cockpit.
      The second countercase is that nutrition/training adapters may require more domain cleanup than
      expected. The third countercase is that fixture proof may feel too artificial unless it produces
      a concrete routed correction request.
    proof_target: |
      The smallest useful Health HQ v0 proof is one committed Health AI evidence bundle showing:
      - a thin HQ layer/namespace or equivalent product structure;
      - explicit goal structure/current phase/phase metrics/domain responsibilities/review-decision log;
      - a minimal domain integration contract;
      - nutrition and training/activity thin summary/report adapters or fixtures;
      - one owner-triggered dry-run or partial-real review across nutrition + training/activity + goal state;
      - review output containing progress verdict, bottleneck/uncertainty, routed correction request(s),
        owner decisions if needed, and metrics needed now/later;
      - checks/evidence that HQ did not silently modify domain artifacts and Direction OS did not receive raw data.

  Approaches considered:
    1. Thin Health HQ coordinator layer in Health AI:
       Create an additive HQ layer/namespace with goal state, owner-triggered review procedure,
       domain summary contracts, and routed request outputs.
       Assumption: summary-level contracts are enough to create coordination value without a new core.
       Chosen because it satisfies the node's actual done_when while preserving HQ/domain boundaries.

    2. Core-only extension:
       Add HQ concepts directly into g-health-core review/phase machinery.
       Assumption: core already owns enough shared concepts to absorb HQ.
       Rejected/captured because it risks reopening the kernel and turning HQ into a second core.

    3. Prompt-only / fake-reuse proof:
       Use a single review prompt over copied summaries and no durable HQ structure.
       Assumption: the value is mostly the review protocol.
       Rejected/captured because owner explicitly wanted goal management and orchestration, not only a reviewer.

  Minimal solution chosen:
    Health HQ v0 is a text-first coordinator/front door. It owns:
    - goal structure view;
    - current phase and phase metrics view;
    - domain responsibility map;
    - review/decision log;
    - owner-triggered review procedure;
    - domain integration contract shape;
    - routed correction request format.

    Health HQ v0 does not own:
    - nutrition menus/recipes/logs;
    - training programs/weeks/session logs;
    - medical advice or diagnosis;
    - raw body/nutrition/training data;
    - automatic polling;
    - API integrations;
    - dashboard UI;
    - direct domain artifact edits.

  Cut list:
    - Cut visual dashboard/cockpit UI; keep text front door only.
    - Cut automatic polling/scheduled self-checking; reviews are owner-triggered only.
    - Cut Hevy/Strava/wearable/API integrations; use manual summaries/fixtures.
    - Cut raw body/nutrition/training data in Direction OS.
    - Cut full future architecture and general integration platform.
    - Cut cooking, habit, sleep, and medical domains from this bet.
    - Cut gameful engine/challenges from this bet.
    - Cut direct domain artifact edits by HQ; HQ only routes correction requests through domain procedures/gates.
    - Cut requirement for full real weekly data; proof may use clearly marked sample/test fixtures where real data is sparse.
    - Cut optimizer/adaptive engine; review produces bounded decisions/requests, not an autonomous plan mutator.

  Lens sweep:
    - weight-nutrition:
        verdict: task_required
        task_link: t-1/t-3
        reason: HQ needs a nutrition summary/report adapter: adherence, hunger/satiety, menu execution,
          weight-relevant signals, issues, and accepted correction request types. It must not redesign nutrition.
    - strength-body-composition:
        verdict: task_required
        task_link: t-1/t-3
        reason: HQ needs training/body-composition summary signals: strength progression readiness,
          training completion, recovery, pain/fatigue, and demand context. It must not build the training program.
    - activity-conditioning:
        verdict: task_required
        task_link: t-1/t-3
        reason: HQ needs coarse activity/conditioning signals and bottleneck routing. It must not build a
          gameful engine, Strava clone, or activity API integration.
    - adherence-relapse:
        verdict: task_required
        task_link: t-1/t-2/t-4
        reason: HQ review must classify adherence drift, missed checks, friction, relapse risk, and owner decisions.
    - medical-safety:
        verdict: task_required
        task_link: t-1/t-2
        reason: HQ must surface pain/symptom/red-flag signals and route conservative review. It does not diagnose
          and does not create a medical domain.
    - ai-system-data-architecture:
        verdict: primary_task_required
        task_link: t-1/t-3
        reason: The bet's core is a summary-only HQ/domain contract that preserves raw-data boundaries,
          governance gates, and thin-domain separation.

  Assumptions ranked by kill-power:
    1. A thin HQ can produce useful cross-domain coordination from summary/report adapters or fixtures
       without becoming a new core, dashboard, polling system, or silent domain editor.
       Test: t-1, first and cheapest proof.
    2. Nutrition and training/activity can expose HQ-ready summaries without major refactor and without raw logs.
       Test: t-1/t-3.
    3. Owner-triggered review is sufficient for useful management; automatic polling is not needed for v0.
       Test: t-2/t-4.
    4. Routed correction requests are specific enough for domain procedures to act on later.
       Test: t-1/t-3.
    5. Owner accepts a text front door and decision log instead of a visual dashboard.
       Test: t-4.

  Proposed tasks if owner approves:
    - id: t-1
      kind: executor
      goal: |
        In ainazemtsau/health-ai, produce the smallest Health HQ v0 proof that tests whether
        a thin summary-only coordinator can run an owner-triggered cross-domain review and route
        correction requests without core rewrite, raw-data capture, dashboard/API work, polling,
        or silent domain edits.
      done_when: |
        Evidence shows:
        - a thin HQ structure/namespace or equivalent product slice exists;
        - goal structure/current phase/phase metrics/domain responsibilities/review-decision log are represented;
        - minimal domain integration contract exists;
        - nutrition and training/activity thin summary/report adapters or fixtures exist;
        - one owner-triggered dry-run or partial-real review produces progress verdict,
          bottleneck/uncertainty, routed correction request(s), owner decisions if needed,
          and needed metrics;
        - python tools/check_kernel_spine.py passes or any failure is explained as pre-existing/non-HQ;
        - no raw data is added to Direction OS; no dashboard/API/polling/full architecture is added;
        - HQ does not silently mutate domain artifacts.
      evaluator: |
        Fresh Direction OS/session review in t-2 tries to refute the proof against the shaped boundaries.
      rollback_first: |
        If the proof requires core rewrite, API/UI/server/DB/cron, raw logs, or direct domain mutation,
        stop and return evidence; do not broaden. Revert/supersede only the HQ proof slice if needed.

    - id: t-2
      kind: session
      goal: |
        Refute t-1 evidence against the shaped bet: verify whether HQ v0 really stayed thin,
        summary-only, owner-triggered, and domain-routed.
      done_when: |
        Review verdict is one of: accept proof / rework within appetite / kill. It explicitly checks
        goal structure, review trigger, domain contracts, routed requests, raw-data boundary, and no silent edits.

    - id: t-3
      kind: executor
      goal: |
        Apply the smallest correction from t-2, if any, and stabilize the HQ v0 evidence bundle
        so the owner can try one front-door request without needing fixed wording.
      done_when: |
        Corrected Health HQ v0 evidence exists, checks pass or are explained, and the returned closeout
        includes one plain owner-facing next prompt such as "проверь прогресс" / "что сегодня?"
        plus the expected non-raw input boundary.

    - id: t-4
      kind: guide
      goal: |
        Owner runs one Health HQ request in plain language and judges whether the response is a useful
        front door rather than just a reviewer or dashboard mock.
      done_when: |
        Owner response is captured as accept / needs change / reject. Evidence includes only summary,
        decision, problem, and next CALL; no raw health diary enters Direction OS.

    - id: t-5
      kind: session
      goal: |
        Verify the bet outcome and decide whether Health HQ v0 is done, killed, or should open a
        narrower follow-up.
      done_when: |
        Fresh review checks t-1..t-4 evidence against node done_when and kill_by. Direction OS receives
        only summary, decisions, problems, and next CALL.

  Recommended first task:
    t-1 executor, because it tests the riskiest assumption before spending effort on owner-facing polish:
    whether HQ can be a thin summary-only coordinator with domain contracts and routed requests, not a new core.

evidence: |
  State read and gates:
  - os/KERNEL.md confirms one active bet max, appetite before tasks, bet validity, evidence,
    and shape validity gates G1-G6.
  - os/plays/shape.md confirms required steps: recite, appetite, approaches/minimal solution,
    scope hammer, lens sweep, riskiest assumption, tasks, kill criteria, close.
  - live/health/NOW.md: active_bet status none; tasks empty; open_calls empty.
  - live/health/TREE.md: g-health-hq-goal-coordinator exists, status parked, and done_when names
    goal structure, owner requests, domain integration contract, nutrition/training adapters,
    dry-run/partial-real review, routed requests, no silent domain edits, and Direction OS raw-data boundary.
  - live/health/CHARTER.md: Direction OS must not become a raw diary; Health AI is the operational support layer;
    risk posture is guarded; pre-mortem flags product procrastination and over-heavy tracking.
  - live/health/history/2026-06-29-c-health-map-evidence-001.md: research recommended a thin referee/reconciler,
    not a cockpit, tracker, or second kernel.
  - live/health/history/2026-06-30-s-health-owner-wants-planning-001-continue.md: owner approved the HQ node and
    clarified owner-triggered checks, no silent domain edits, and domain report/integration structure.
  - ainazemtsau/health-ai AGENTS.md: Health AI is file-backed, chat surfaces do not save, domains attach through
    registry, and raw/gated governance boundaries must be preserved.
  - ainazemtsau/health-ai core/extensions/registry.md: active modules are x_nutrition and x_training_activity.
  - ainazemtsau/health-ai x_nutrition/index.md and x_training_activity/index.md show current domain indexes and
    summary/boundary surfaces suitable for a thin HQ adapter proof.

state_changes: |
  None. Owner approval is not yet given, so no TREE.md/NOW.md/LOG.md/history edits are proposed for application
  by a writer in this RESULT. No bet is activated and no tasks are created.

captures:
  - rejected_approach: core-only HQ extension risks reopening g-health-core and turning HQ into a second kernel.
  - rejected_approach: prompt-only review proof is too small because owner wanted goal management/orchestration, not reviewer-only.
  - parked: visual dashboard/cockpit UI may be revisited only after text-first HQ proves value.
  - parked: API integrations with Hevy/Strava/wearables remain deferred until manual summary contracts are stable.
  - parked: gameful activity/training challenge layer remains under training/activity, not Health HQ v0.
  - parked: cooking, habit, sleep, and medical domains remain out of this shape.
  - risk: health-ai current training/activity repo state may be fresher than Direction OS summary; HQ proof should be robust by accepting clearly marked fixtures or current summaries without requiring Direction OS to track raw projects.

decisions_needed:
  - q: |
      Approve the shaped Health HQ v0 bet with 5-calendar-day appetite and t-1 executor proof as the first task?
    options:
      - A: approve recommended bet
      - B: cut further to a 3-day review-prompt-only proof
      - C: park HQ and return to nutrition/training execution
    recommendation: |
      A, because it is the smallest version that still tests the real node: goal structure,
      owner-triggered review, domain integration contract, and routed correction requests.
      B is too likely to collapse into "reviewer only"; C leaves cross-domain goal management unmanaged.

play_check:
  - 1 Recite: done — node goal/done_when and parent root goal were read; node is an outcome, not an activity.
  - 2 Appetite first: done — proposed 5 calendar days before solution talk; outside-view compared against prior larger core/training bets and the research recommendation for a thin referee.
  - 3 Approaches, then minimal solution: done — considered thin HQ layer, core-only extension, and prompt-only proof; chose thin HQ coordinator and captured rejected approaches.
  - 4 Scope hammer: done — cut list includes dashboard, polling, APIs, raw Direction OS data, full architecture, extra domains, gameful engine, direct domain edits, real-data completeness, and optimizer engine.
  - 5 Lens sweep: done — all six CHARTER lenses have task_required or primary_task_required verdicts with task links.
  - 6 Riskiest assumption: done — top assumption is thin summary-only HQ value without core rewrite/god-agent drift; t-1 tests it first.
  - 7 Tasks: done — proposed five tasks, each sized to half a focused day or less, with kind, done_when, evaluator, and rollback-first for executor work.
  - 8 Kill criteria: done — kill_by has metric/threshold/date logic and next_if_true/next_if_false branches.
  - 9 Close: done_as_checkpoint — shaped bet shown for owner decision; no approval yet, so no state_changes and no activation.

log: |
  shape health/hq-goal-coordinator: proposed 5-day Health HQ v0 bet testing thin goal-management/orchestration layer with owner-triggered review, domain integration contracts, and routed correction requests; awaiting owner decision.

next: |
  awaiting_decision:
    Owner chooses A approve / B cut to 3-day review-prompt-only proof / C park HQ and return to nutrition-training execution.

END_OF_FILE: live/health/history/2026-06-30-s-health-shape-hq-goal-coordinator-001.md
