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
    status: active
    kind: session
    goal: >
      Health HQ has an owner-signed WHAT for goal-achievement orchestration, or the current bet is
      explicitly killed/narrowed with a clear next route.
    done_when: >
      Corrected requirements explicitly cover root-goal achievement, milestones/phases, metrics,
      strategy/review loop, domain demand contracts, and the difference between safety boundaries
      and the product's positive purpose.
    route_decision: >
      Owner approved option A on 2026-07-02 with "A": Health HQ remains active only on the corrected
      WHAT/research/architecture/verify route. No new Health AI implementation is authorized from the
      summary-only proof.
    current_route: >
      Research child c-health-hq-goal-achievement-model-research-001 returned; parent converge
      c-health-hq-orchestrator-converge-001 must convert the accepted research into an
      owner-signable WHAT/route before Define/Resolve can close.
    research_note: >
      Research returned and accepted as input on 2026-07-03; artifact:
      live/health/work/health-hq-goal-achievement-model-research-2026-07-03.md.
      It is input for owner-signable WHAT/route, not product acceptance and not implementation authorization.

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
  return-to-parent c-health-hq-orchestrator-converge-001

END_OF_FILE: live/health/NOW.md
