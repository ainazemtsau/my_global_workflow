# NOW — health

active_bet:
  id: b-health-hq-goal-coordinator-v0-001
  node: g-health-hq-goal-coordinator
  status: active
  appetite: 5 calendar days
  started: 2026-07-01
  kill_by: >
    2026-07-06 end-of-day Europe/Amsterdam. Kill/review if by this date Health HQ cannot
    show a corrected, owner-signed route toward goal-achievement orchestration, or if the
    work remains only a status/review dispatcher without milestone/metric/strategy/domain-demand
    structure for reaching the root health goal.
  repair_note: >
    2026-07-01 scope repair: Health AI main @6ca3f18 / commit 9ad9330 produced a narrow
    summary-only Health HQ proof. That proof is retained as technical evidence that an
    x_health_hq namespace can read summaries, preserve boundaries, and route non-mutating
    requests. It is NOT accepted as the Health HQ product. Owner rejected the framing as
    a "status dispatcher" and clarified that Health HQ's main purpose is to orchestrate
    achievement of the health goal through milestones, metrics, strategy, and domain-level
    demands across nutrition, training/activity, sleep/recovery, and future domains.
  goal: >
    Health HQ v0 becomes the owner-facing goal-achievement orchestrator for the health root
    goal: it holds the goal, milestones, current phase, metrics, strategy, review/decision log,
    bottlenecks, and domain responsibilities, and it tells each execution domain what outcome
    it needs to support without silently mutating that domain's artifacts.
  done_when:
    - Health HQ's positive essence is explicit: it is an orchestrator for achieving the health
      goal, not merely a status screen, prompt, reviewer, dashboard mock, or dispatcher.
    - There is a corrected WHAT for milestones/phases, target metrics, current progress model,
      strategic review loop, owner conversation surface, decision log, and domain demand routing.
    - Domain responsibilities cover at least nutrition, training/activity, sleep/recovery as a
      future domain, and future health domains; each domain remains the execution mechanism for
      its own artifacts.
    - Health HQ can state requirements or demand-shapes for domains, such as nutrition deficit/
      adherence/satiety requirements, training weekly load/recovery/strength-conditioning focus,
      sleep/recovery constraints, and metric needs.
    - Summary/status review remains a sub-capability, but not the whole product definition.
    - Research needs are named clearly enough that a deep-research child can be launched for the
      health goal-achievement model if the converge session cannot close responsibly from current
      state.
    - Raw body/nutrition/training data stays outside Direction OS; Health HQ still does not provide
      medical diagnosis, build dashboards/API/polling, or silently edit source-domain artifacts.
  proof_kept:
    product_repo: C:\my_global_workflow_worktrees\health-ai
    current_main: 6ca3f18
    hq_proof_commit: 9ad9330
    meaning: >
      Narrow technical proof only: registry/object namespace, summary adapters/fixtures,
      dry-run review, boundary flags, and non-mutating routed requests.
  cut_list:
    - accepting the summary-only proof as the whole Health HQ product
    - visual dashboard/cockpit UI
    - automatic polling/scheduled self-checking
    - Hevy/Strava/wearable/API integrations
    - raw body/nutrition/training data in Direction OS
    - direct domain artifact edits by HQ
    - medical diagnosis/advice
    - prompt-only solution without durable goal/milestone/metric structure
  lens_sweep:
    - weight-nutrition: required as domain demand structure for deficit, satiety, adherence, and review routing.
    - strength-body-composition: required as training/body-composition progress and load/recovery demand structure.
    - activity-conditioning: required as weekly activity/conditioning demand structure and bottleneck routing.
    - adherence-relapse: required as review loop, friction detection, relapse risk, and owner decision structure.
    - medical-safety: required as conservative red-flag/symptom routing boundary; no diagnosis.
    - ai-system-data-architecture: required as HQ/domain contract, summary-only boundary, and goal state structure.
  assumptions:
    - The current TREE node can be repaired in place because it already names goal-management and orchestration;
      the failure is the active bet's narrow proof route, not the existence of the node.
    - The Health AI x_health_hq summary-only slice can become a subcomponent of the corrected HQ instead of
      being reverted.
    - A deep goal-achievement model likely needs converge and possibly a research child before new executor work.
  forecast: >
    Favorable only if the next session retrofits the WHAT around goal achievement before more product commits.
    Unfavorable if we continue the old t-2/t-4 acceptance path and let the boundary proof stand in for HQ.
  against: >
    Health HQ can still become too broad ("god-agent") or too thin ("status dispatcher"). The repair must
    preserve safety/domain boundaries while restoring the positive job: achieving the root health goal.
  next_if_true: >
    Re-shape or continue the Health HQ bet from an owner-signed goal-achievement WHAT, then issue a corrected
    Health AI executor task.
  next_if_false: >
    Kill the current Health HQ bet and return to narrower nutrition/training/body-execution work until the HQ
    model can be responsibly shaped.

tasks:
  - id: t-1
    node: g-health-hq-goal-coordinator
    status: done
    kind: executor
    repo: C:\my_global_workflow_worktrees\health-ai
    goal: >
      Narrow Health HQ summary-only technical proof exists.
    done_when: >
      Health AI evidence shows an x_health_hq namespace, registry entry, summary adapters/fixtures,
      dry-run review, boundary flags, and non-mutating routed requests; this is not accepted as
      the full HQ product.
    evidence: >
      health-ai main @6ca3f18, key commit 9ad9330 Add Health HQ summary coordinator proof.
      Checks observed: check_kernel_spine PASS with WA-K6/WA-K8 RED-DEFERRED as existing breadth
      deferrals; check_structural_repair PASS; check_health_hq_thin_slice PASS. The training/activity
      thin-slice checker currently fails DW02/DW06/DW13, but 9ad9330 did not modify x_training_activity;
      treat that as pre-existing/non-HQ until a separate training/activity repair asks for it.
    caveat: >
      Owner-facing framing was rejected as too narrow: Health HQ must orchestrate achievement of
      the health goal, not merely report status and route missing-data requests.

  - id: t-2
    node: g-health-hq-goal-coordinator
    status: done
    kind: session
    goal: >
      Health HQ has an owner-signed WHAT for goal-achievement orchestration, or the current bet is
      explicitly killed/narrowed with a clear next route.
    done_when: >
      Corrected requirements explicitly cover root-goal achievement, milestones/phases, metrics,
      strategy/review loop, domain demand contracts, and the difference between safety boundaries
      and the product's positive purpose.
    evidence: >
      converge-verify PASS @ 2026-07-04 in s-health-hq-orchestrator-converge-verify-001.
      Owner-signed WHAT and converge-arch architecture/check route match; completeness and smuggling refutations passed;
      no failed checklist item remains. No executor implementation occurred in the verify session.
    verification_note: >
      Health HQ t-2 requirements route is now verified. The next implementation route is a separate corrected
      executor CALL that must use the signed WHAT and architecture/check artifact as input evidence, not raw research.
    route_decision: >
      Owner approved option A on 2026-07-02 with "A": Health HQ remains active only on the corrected
      WHAT/research/architecture/verify route. No new Health AI implementation is authorized from the
      summary-only proof.
    what_signoff: >
      Owner signed the research-integrated Health HQ WHAT/route on 2026-07-04 with
      "A — подписываю". Health HQ is accepted as an owner-triggered goal-achievement orchestration
      layer, not a status dispatcher/dashboard/god-agent/medical advisor/integration hub. Next route
      is converge-arch before converge-verify and any executor implementation.
    architecture_note: >
      Converge-arch closed on 2026-07-04. Architecture/check artifact:
      live/health/work/converge-g-health-hq-goal-coordinator-arch.md. It covers §CONTRACTS,
      decomposition, phase/milestone objects, metric hierarchy + summary-source contract,
      strategic review loop, bottleneck taxonomy, domain demand contract objects,
      decision classes/owner approval gate, safety/recovery boundary, old x_health_hq proof
      as subcomponent only, later implementation evidence expectations, and converge-verify checklist.
      It does not authorize Health AI implementation.
    current_route: >
      Owner-signed WHAT/route has passed converge-arch as an implementation-neutral
      architecture/check route. Next is converge-verify. No executor implementation is authorized
      until converge-verify passes and emits a separate route.
    research_note: >
      Research returned and accepted as input on 2026-07-03; artifact:
      live/health/work/health-hq-goal-achievement-model-research-2026-07-03.md.
      It has been integrated into the signed WHAT/route, but remains research input, not product
      acceptance and not implementation authorization.

  - id: t-3
    node: g-health-hq-goal-coordinator
    status: active
    kind: executor
    repo: github.com/ainazemtsau/health-ai
    goal: >
      Health HQ v0 is implemented as owner-triggered goal-achievement orchestration in Health AI, preserving
      signed WHAT, architecture/check boundaries, domain authority, summary-only Direction OS boundary, and safety/governance gates.
    done_when: >
      Health AI evidence shows Health HQ v0 can perform owner-triggered goal reviews across the main intent classes,
      produce phase-aware progress verdicts, classify bottlenecks with strategy implications, emit non-mutating domain
      demand objects, preserve owner approval gates and domain authority, maintain review/decision summaries without raw
      Direction OS data, treat x_health_hq as subcomponent only, and demonstrate safety/recovery boundary behavior without
      diagnosis or treatment.
open_calls: []

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
  CALL c-health-hq-goal-coordinator-v0-executor-001
  to: executor
  direction: health
  repo: github.com/ainazemtsau/health-ai
  kind: engineering
  node: g-health-hq-goal-coordinator
  task: t-3
  goal: |
    Deliver Health HQ v0 as an owner-triggered goal-achievement orchestration layer in Health AI.

    Health HQ must coordinate progress toward the root health goal through phases, milestones,
    decision-grade metrics, bottleneck classification, non-mutating domain demands, owner/governance
    decisions, and safety/recovery gates. It must not regress into a status dispatcher, dashboard,
    integration hub, god-agent, medical advisor, or silent domain editor.
  context: |
    Input evidence to read:
    - live/health/work/converge-g-health-hq-goal-coordinator.md
    - live/health/work/converge-g-health-hq-goal-coordinator-arch.md
    - live/health/history/2026-07-04-s-health-hq-what-signoff-001.md
    - live/health/history/2026-07-04-s-health-hq-orchestrator-converge-arch-001.md
    - live/health/history/2026-07-04-s-health-hq-orchestrator-converge-verify-001.md

    Current authority:
    - Owner signed the Health HQ WHAT/route with "A — подписываю".
    - Converge-verify passed on 2026-07-04.
    - Signed WHAT W1-W16 and W20-W21 are the business acceptance surface.
    - W17 means existing x_health_hq is technical subcomponent evidence only, not product acceptance.
    - W18/W19 mean no implementation was authorized from the old summary-only proof or raw research.
    - Architecture/check artifact is input evidence only; do not copy architecture picks as implementation done_when.
    - Raw research must not be used as direct executor instructions; it has been compressed into signed WHAT and arch.
  boundaries: |
    No dashboard/API/polling/integration design.
    No raw body/nutrition/training data in Direction OS.
    No medical diagnosis or treatment plan.
    No silent mutation of nutrition, training/activity, sleep/recovery, or future domain artifacts.
    Preserve domain authority: HQ may review, classify, recommend, request, route, and ask for owner decisions;
    domains execute and mutate their own artifacts through their own procedures and governance gates.
    Do not claim live sleep/recovery or future-domain capability unless a producer exists and has passed its own route;
    pending/fixture status must be explicit.
    Do not relabel the existing x_health_hq summary-only proof as Health HQ v0 product acceptance.
  done_when: |
    Return verifiable Health AI evidence that demonstrates:

    1. Owner-triggered review surface:
       - supports at least "что сегодня?", "разбери неделю", "проверь прогресс", "где bottleneck?", "добавить новый процесс?";
       - routes plain-language owner intent without requiring fixed wording;
       - does not rely on background polling or automatic self-checking.

    2. Explicit Health HQ goal structure:
       - root health goal;
       - current phase;
       - phase/milestone objects with entry condition, exit condition, target/current relationship, dominant bottleneck classes,
         phase-specific domain demands, safety/recovery gates, and owner decision requirements;
       - domain responsibilities;
       - review/decision log.

    3. Phase-aware review:
       - produces progress verdict: on-track / at-risk / stalled / blocked / unsafe-to-escalate;
       - compares phase target to current summary state;
       - explains the phase-relevant implication and next action.

    4. Metric hierarchy and summary-source contract:
       - distinguishes current-phase minimum, later-only, and pending/non-mandatory metrics;
       - every verdict-driving metric/signal carries source, live/fixture/pending status, freshness, confidence,
         reason if pending, and decision impact;
       - no invented numbers;
       - no raw body/nutrition/training logs copied into Direction OS.

    5. Strategic review output:
       - progress verdict;
       - main bottleneck class + reason + confidence;
       - what would change the classification;
       - strategy implication;
       - non-mutating domain demands;
       - owner decision required yes/no;
       - if owner decision is required, options plus recommendation;
       - metrics needed now;
       - metrics later;
       - next owner-facing action.

    6. Domain demand objects:
       - nutrition, training/activity, sleep/recovery pending/fixture handling, and future-domain handling use the same demand contract shape;
       - demands are non-mutating review/proposal/comparison requests;
       - domains retain execution and mutation authority;
       - material strategy, phase, boundary, domain, or canonical source changes require owner/governance approval.

    7. Decision classes:
       - advisory;
       - approval-required;
       - blocked;
       - blocked actions include diagnosis/treatment, raw-data leak, silent domain edit, unsafe escalation, and dashboard/API/polling implementation creep.

    8. Safety/recovery boundary:
       - HQ can mark unsafe-to-escalate, hold deficit/load escalation, route domain review, and raise owner-facing concern;
       - HQ does not diagnose, treat, reassure away red flags, or frame rapid unexplained loss/symptoms as automatic success.

    9. Old proof treatment:
       - existing x_health_hq summary loading / fixtures / adapters / non-mutating routed-request mechanics may be reused only under the full orchestration spine;
       - summary-only reviewer proof is not returned as sufficient product acceptance.

    10. Evidence:
       - commits/PR or equivalent repository evidence;
       - check output or equivalent validation output;
       - a short evidence map from the returned implementation proof to signed WHAT W1-W16/W20-W21 and the architecture/check artifact.
  return: |
    RESULT with product-repo evidence, commit/PR/check output, evidence map to signed WHAT and architecture/check,
    any blockers, state_changes for Direction OS, play_check/evaluator notes, log line, and next CALL/awaiting_decision.
  budget: one executor leg

END_OF_FILE: live/health/NOW.md
