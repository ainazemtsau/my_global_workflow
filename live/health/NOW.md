# NOW — health

active_bet:
  status: none
  note: |
    No active bet after the training/activity v0 product/process work and its 2026-06-28 repair.
    Product/process evidence before repair: health-ai c1bf61e for t-1 and health-ai 8aa14f8 for t-2;
    owner release acceptance from t-3: "Запускаем". On 2026-06-28 the owner supplied a correction
    showing that 8aa14f8 falsely resolved x_training_activity to ACTIVE/DAY_LOOP on sample-only
    evidence. Bounded product repair health-ai 1fe41c2 supersedes that false launch route:
    training/activity now resolves to PROGRAM awaiting Deep Research, blocks proposal/ACTIVE/week/
    session until a suitable returned research conclusion plus owner approval exists, and keeps
    first real performed session unclaimed.

    Owner clarified on 2026-06-28 that Direction OS must not track Health AI projects/processes by
    default: "мы не трэкаем проекты если только я прямо не попрошу". Health AI may continue its
    nutrition/training work outside Direction OS. Direction OS will handle nutrition/training issues,
    returned conclusions, repairs or process-development decisions only when the owner explicitly
    brings them back.

tasks: []

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
  CALL c-health-shape-hq-goal-coordinator-001
  to: session
  direction: health
  play: shape
  node: g-health-hq-goal-coordinator
  goal: |
    Shape the owner-approved g-health-hq-goal-coordinator node into the next possible health bet without activating it.
    The shaped bet should test the smallest useful Health HQ v0: goal structure, owner-triggered review, domain
    integration contract, and routed correction requests.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/history/2026-06-29-c-health-map-evidence-001.md
    - this map RESULT

    Owner-approved node:
    g-health-hq-goal-coordinator = Health HQ v0 as owner-facing goal-management/orchestration layer.
    It is not just a reviewer and not a visual dashboard. It should manage goals, current phase, phase metrics,
    domain responsibilities, review/decision log, on-demand reviews, domain coordination, and domain integration
    contracts.

    Owner constraints captured during map:
    - All checks/reviews are owner-triggered; Health AI does not self-check or poll by default.
    - Health HQ may diagnose and route but must not silently edit nutrition/training/activity artifacts.
    - Current and future domains need a structure for integration with Health HQ: summaries/reports, supported goals,
      exposed signals/metrics, accepted correction request types, and boundaries.
    - Training starts only now and nutrition has only partial recent real use, so proof may use clearly marked
      sample/test fixtures where real weekly data is not yet available.
  boundaries: |
    Do not activate a bet until shape is complete and owner approves.
    Do not create tasks before bet shaping gates are satisfied.
    Do not design a full future architecture.
    Do not build a visual dashboard, API/integration layer, automatic polling, gameful engine, cooking domain,
    habit system, sleep domain, or medical domain in this shape.
    Do not store raw body/nutrition/training data in Direction OS.
    Keep Health HQ as coordinator/front door/goal manager, not a god-agent replacing domains.
  done_when: |
    Shape output is ready for owner decision and includes:
    - appetite and kill_by;
    - cut list with at least one real cut;
    - lens sweep verdict per charter lens;
    - riskiest assumption and first task proposal testing it;
    - explicit proof target for smallest useful Health HQ v0;
    - clear boundary for domain integration contracts and owner-triggered reviews.
  return: |
    RESULT with shaped bet proposal, cut list, lens sweep, recommended first task, state_changes only if owner approves,
    and next.
  budget: one shape session

END_OF_FILE: live/health/NOW.md
