RESULT s-health-hq-scope-repair-001 (call: owner-message-2026-07-01-ok)
direction: health   play: repair   node/task: g-health-hq-goal-coordinator/t-2

outcome: |
  Direction OS is reconciled with the Health AI Health HQ proof without accepting the wrong product framing.

  What is now true:
  - Health AI main @6ca3f18 / commit 9ad9330 is recorded as a narrow technical Health HQ proof only.
  - The old acceptance path t-2..t-5 for a summary-only coordinator is superseded.
  - The active bet now routes to retrofit/converge Health HQ as a goal-achievement orchestrator.
  - TREE.md is unchanged because the tree node already names goal-management/orchestration; the drift was in NOW.md's active route.

evidence: |
  Contradiction:
  - live/health/NOW.md routed next to c-health-hq-goal-coordinator-t1-executor-001 and then old t-2/t-4 acceptance of a summary-only coordinator/front-door proof.
  - Owner transcript rejected that framing: Health HQ's main job is achievement of the health goal through milestones, metrics, strategy, and domain-level demands, not only "status, missing data, route a request."

  Product evidence:
  - C:\my_global_workflow_worktrees\health-ai main @6ca3f18.
  - Key commit: 9ad9330 Add Health HQ summary coordinator proof.
  - Added x_health_hq namespace, registry entry, domain contract, state machine, cursor, artifact families, review procedure, domain integration contract, nutrition/training summary fixtures, dry-run review, acceptance matrix, negative fixtures, and checker.
  - x_health_hq/evidence-summary.md explicitly says the proof is summary-only, fixture-backed, and still limited by pending core position/current metrics.
  - x_health_hq/reviews/2026-07-01-dry-run-progress-review.md returns verdict blocked_missing_metrics and non-mutating routed requests.

  Checks observed in this repair:
  - python tools/check_kernel_spine.py: PASS, with WA-K6/WA-K8 RED-DEFERRED as existing breadth deferrals.
  - python tools/check_structural_repair.py: PASS.
  - python tools/check_health_hq_thin_slice.py: PASS.
  - python tools/check_training_activity_thin_slice.py: FAIL on DW02/DW06/DW13; treated as pre-existing/non-HQ because git show 9ad9330 did not modify x_training_activity files.

  Owner confirmation:
  - After the repair recommendation, owner said: "ок".

state_changes: |
  live/health/NOW.md:
  - Replace the old summary-only active_bet route with the repaired active bet state:
      - keep id b-health-hq-goal-coordinator-v0-001 and node g-health-hq-goal-coordinator;
      - record repair_note that health-ai @6ca3f18 / 9ad9330 is a narrow technical proof only;
      - restate the active goal as Health HQ goal-achievement orchestration;
      - replace done_when with interim repaired criteria for milestones/phases, metrics, strategy/review loop,
        domain demand contracts, positive product essence, research needs, and preserved raw-data/domain boundaries;
      - record proof_kept with product_repo, current_main, hq_proof_commit, and meaning.
  - Replace tasks:
      - t-1 -> done, evidence = health-ai @6ca3f18 / 9ad9330, caveat = not accepted as full HQ product.
      - t-2 -> active, session task for owner-signed WHAT/route for goal-achievement orchestration.
      - remove stale pending t-3/t-4/t-5 from the old acceptance path.
  - Replace open_calls with c-health-hq-orchestrator-converge-001.
  - Preserve recurring r-health-ai-minor-fix-lane unchanged.
  - Preserve decisions as [].
  - Replace next with c-health-hq-orchestrator-converge-001.
  - Maintain END_OF_FILE trailer.

  live/health/LOG.md:
  - Append:
      - 2026-07-01 — health/g-health-hq-goal-coordinator repair: Health AI @6ca3f18 / 9ad9330 recorded as narrow summary-only HQ technical proof, not accepted as product; owner rejected status-dispatcher framing, old t-2..t-5 acceptance route superseded, next is converge retrofit for Health HQ as goal-achievement orchestrator. → history/2026-07-01-s-health-hq-scope-repair-001.md
  - Maintain END_OF_FILE trailer.

  live/health/history/2026-07-01-s-health-hq-scope-repair-001.md:
  - Add this full RESULT.

  os/FRICTION.md:
  - Append one watching line:
      2026-07-01 health Health HQ scope repair: active shape/executor route let a boundary proof ("summary-only coordinator") become the apparent product essence; owner rejected it as status-dispatcher framing and clarified HQ must orchestrate achievement of the health goal through milestones, metrics, strategy, and domain demands. Watching/candidate maintenance: shape/executor CALLs for owner-facing orchestration should preserve positive product essence separately from non-goals/boundaries; proof slices should be labeled as technical boundary proofs, not acceptance of the product.
  - Maintain END_OF_FILE trailer.

captures:
  - Health HQ needs a deep goal-achievement model: milestones, phase metrics, strategic review loop, and domain demand contracts.
  - Current x_health_hq summary-only slice can remain as a lower-level review/status component if the corrected HQ model survives converge.
  - Sleep/recovery likely belongs in the HQ demand map even if it remains out of the current implementation slice.

decisions_needed: []

play_check:
  - 1 Name the contradiction: done — NOW routed toward accepting a summary-only Health HQ proof, while owner rejected that as not the real HQ: the real HQ must orchestrate achievement of the health goal.
  - 2 Reconstruct: done — newest evidence is health-ai @6ca3f18 / 9ad9330 plus owner transcript; product commit proves a narrow technical slice, not product acceptance.
  - 3 Propose corrected state: done — NOW keeps the technical proof, removes stale acceptance tasks, and routes to converge retrofit for goal-achievement orchestration.
  - 4 Confirm: done — owner approved the repair route with "ок" after the recommendation to synchronize proof, reject acceptance, and reframe HQ.
  - 5 Friction: done — added a watching line for boundary-proof-vs-product-essence drift.

log: |
  2026-07-01 — health/g-health-hq-goal-coordinator repair: Health AI @6ca3f18 / 9ad9330 recorded as narrow summary-only HQ technical proof, not accepted as product; owner rejected status-dispatcher framing, old t-2..t-5 acceptance route superseded, next is converge retrofit for Health HQ as goal-achievement orchestrator. → history/2026-07-01-s-health-hq-scope-repair-001.md

next: |
  CALL c-health-hq-orchestrator-converge-001
  to: session
  direction: health
  play: converge
  node: g-health-hq-goal-coordinator
  task: t-2
  goal: |
    Health HQ has an owner-signed WHAT for goal-achievement orchestration, or the current bet is explicitly killed/narrowed with a clear next route.
  context: |
    Direction OS state:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/history/2026-06-29-c-health-map-evidence-001.md
    - live/health/history/2026-06-30-s-health-owner-wants-planning-001-continue.md
    - live/health/history/2026-06-30-s-health-shape-hq-goal-coordinator-001.md
    - live/health/history/2026-07-01-s-health-shape-hq-goal-coordinator-approval-001.md
    - live/health/history/2026-07-01-s-health-hq-scope-repair-001.md

    Product evidence kept as a narrow technical slice:
    - C:\my_global_workflow_worktrees\health-ai main @6ca3f18
    - key commit 9ad9330 Add Health HQ summary coordinator proof
    - x_health_hq/evidence-summary.md
    - x_health_hq/reviews/2026-07-01-dry-run-progress-review.md
    - tools/check_health_hq_thin_slice.py

    Owner correction captured in the repair:
    - Health HQ's main job is achievement of the health goal, not just status review.
    - It should hold milestones, metrics, strategy, goal progress, and domain-level demands.
    - Nutrition/training/sleep/future domains are execution mechanisms; HQ can tell them what
      outcome or support is needed without directly mutating their artifacts.
    - A proper model likely needs deep research and durable structure, not a prompt-only patch.
  boundaries: |
    Do not accept the summary-only proof as the full Health HQ product.
    Do not edit Health AI in this session.
    Do not write raw body/nutrition/training data into Direction OS.
    Do not turn HQ into medical diagnosis, dashboard/API/polling infrastructure, or a silent editor
    of nutrition/training/activity artifacts.
    Keep the positive product essence separate from safety/non-goal boundaries.
  done_when: |
    The resulting WHAT or route explicitly covers:
    - Health HQ as orchestrator of reaching the root health goal;
    - milestones/phases and target/current metrics;
    - strategic review loop and owner conversation surface;
    - domain demand contracts for nutrition, training/activity, sleep/recovery, and future domains;
    - what HQ may decide/recommend/request vs what domains must execute and owner/governance must approve;
    - what research is needed before implementation;
    - whether the active bet can be repaired inside appetite or must be killed/re-shaped.
  return: |
    RESULT with corrected WHAT/route, evidence, owner decisions if needed, state_changes, and next CALL.
  budget: one session

END_OF_FILE: live/health/history/2026-07-01-s-health-hq-scope-repair-001.md
