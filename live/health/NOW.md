# NOW — health

active_bet:
  status: none
  note: >
    No active bet after owner-approved option-A WA-K10 evidence repair and
    closure of g-health-core. health-ai main now contains current-head canonical
    WA-K10 proof at 8246cec19672bdd7eaadb2fec070a247088b6749; `python
    tools/check_kernel_spine.py` reports WA-K10 GREEN. The repaired proof
    restores the real historical SEED->PROPOSED->ACTIVE journey chain
    (f94351b -> 078d36d -> 78bad5a), preserves the original fresh refutation
    (9a0124a), and survived a fresh in-session validator pre-pass after commit.
    WA-K6 and the strongest WA-K8 form remain explicit follow-on breadth, not
    blockers to this kernel-spine closure.

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
    last_done: 2026-06-24
    note: >
      Post-1338a35 bounded work was reconciled into this lane: menu workflow
      structure repair and owner_fact_delta/assumption hardening
      (7cd962a, 83dba88, 77a0ed), followed by fixed-menu/recipe support through
      health-ai 8246cec. The lane remains recurring/on-demand, not a second
      active bet. Authority, safety, provider-portability or owner-gate defects
      escalate to a bounded repair/executor CALL; cosmetic papercuts are
      batched, deferred or dropped.

decisions: []

next: |
  CALL c-health-training-activity-shape-001
  to: session
  direction: health
  play: shape
  node: g-health-training-activity-system
  goal: |
    The next training/activity bet is small enough to execute and likely to
    improve real body outcomes.
  context: |
    g-health-core is closed done after current-head WA-K10 evidence repair.
    Product evidence:
    - health-ai commit 8246cec19672bdd7eaadb2fec070a247088b6749 restored
      acceptance/kernel/journey-proof.md.
    - `python tools/check_kernel_spine.py` reports WA-K10 GREEN.
    - Fresh in-session validator pre-pass post-commit returned
      SURVIVES-PREPASS for the WA-K10 proof package.

    Owner approval carried by the repair CALL:
    - D-health-core-kernel-review-close-003 option A: repair current-head
      WA-K10 evidence, then approve g-health-core active -> done and replace the
      stale g-health-nutrition-system dirty/blocked preamble with current
      ACTIVE-program/cycle/week-plan, DAY_LOOP partial-progress reality.
    - D-health-next-large-bet-003 prepared route: shape
      g-health-training-activity-system next.

    Current health-ai nutrition state has an ACTIVE program, cycle, week plan,
    fixed menu and recipe book with cursor DAY_LOOP. Minor Health AI papercuts
    remain in r-health-ai-minor-fix-lane rather than expanding this bet.
    Carry D-kernel-1 and the strongest WA-K8 second-domain test as explicit
    shape inputs, not automatic scope.
  boundaries: |
    Do not implement training. Do not author Health AI artifacts. Do not reopen
    kernel breadth by default. Keep raw workout/activity logs out of Direction OS.
  done_when: |
    An owner-approved training/activity bet has appetite, kill_by, real cut
    list, verdict for every CHARTER lens, a task testing the riskiest
    assumption first, no more than three active tasks, and a ready first CALL.
  return: |
    RESULT with owner-approved TREE/NOW state_changes and the next execution
    CALL.
  budget: one session

END_OF_FILE: live/health/NOW.md
