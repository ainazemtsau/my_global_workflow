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
  CALL c-health-training-activity-converge-verify-001
  to: session
  direction: health
  play: converge-verify
  node: g-health-training-activity-system
  goal: |
    Refute the complete training/activity converge set before shape: signed WHAT
    W1-W20, §CONTRACTS TA-CA1..TA-CA12, and the context-only architecture paper
    A1-A5.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-training-activity-system.md
    - live/health/work/converge-g-health-training-activity-system-arch.md
    - live/health/work/converge-g-health-core.md
    - live/health/work/converge-g-health-core-kernel.md
    - live/health/work/converge-g-health-core-kernel-arch.md
    - live/health/history/2026-06-20-s-health-core-kernel-wave0-derisk-001.md
    - live/health/history/2026-06-24-s-health-core-kernel-wa-k10-evidence-repair-001.md
    - live/health/history/2026-06-25-s-health-training-activity-converge-001.md

    Training/activity WHAT is owner-signed:
    - Define: "ок согласен", including setup proof without mandatory completed
      workout, split tool authority, and D-kernel-1 option A.
    - Resolve: "Да, согласен с пакетом B", amended so screenshots are transient:
      show extracted data for owner correction/confirmation, ask materially useful
      follow-ups, save only the structured normalized result.

    Current product facts:
    - health-ai @8246cec has current-head WA-K10 GREEN.
    - health-ai @8246cec registry grammar houses D-kernel-1 as control-plane
      decide-and-inform.
    - nutrition is an ACTIVE thin sibling with program/cycle/week/menu/recipe
      artifacts and cursor DAY_LOOP.

    Converge-arch closed:
    - §CONTRACTS TA-CA1..TA-CA12 cover core/kernel, nutrition, specialist tools,
      Direction OS, setup/body evidence split, and WA-K8 proof topology.
    - Decomposition records internal seams and no required sub-node before shape.
    - A1-A5 are closed with refuted comparisons and system picks; owner_gate_batch=[].
    - Guided-session durability is claimed compatible with kernel job contract via
      checkpoint-as-job-boundary in the same LOG family.
    - Architecture picks are input evidence only; they must not be copied into
      done_when.
  boundaries: |
    Do not implement training/activity or modify health-ai.
    Do not activate a bet, create execution tasks, emit an executor CALL, or shape.
    Do not prescribe a concrete workout program or freeze exercise/volume/intensity/
    vendor magnitudes.
    Do not weaken or silently modify signed W1-W20.
    Do not reopen the kernel unless a direct contradiction is proven; D-kernel-1
    should be imported unless contradicted.
    Keep screenshots and raw workout/activity/pulse/wearable data out of Direction OS.
  done_when: |
    - Every TREE interaction is covered by a §CONTRACTS row with consumer, producer,
      behavior, direction, trigger, and build-order.
    - No contract dangles, no contract line relies on an open WHAT term, and no HOW
      detail is made binding.
    - Heavy decomposition has no missing internal seam and its sub-node decision is
      refutable.
    - A1-A5 each has a 3-5 option refuted comparison; any claimed system pick is
      forced by signed WHAT/kernel contracts or else returned as a decision_needed.
    - Guided-session durability is either compatible with the kernel job contract
      or a named blocker is returned before shape.
    - Training<->nutrition routine demand and review-level handoff remain frozen
      without direct module-file coupling.
    - D-kernel-1 is imported rather than re-litigated unless a contradiction is proven.
    - WA-K8 proof topology covers live nutrition sibling, training removal, and one
      training-procedure disablement.
    - contract_coverage is complete, arch_open is zero, and architecture remains
      context-only: no pick is copied into done_when.
    - Next route is shape only if verify passes; otherwise repair/converge-arch
      correction.
  return: |
    RESULT with refutation verdict, exact bounce/fix state_changes if any, and either
    a ready shape CALL or a repair/converge-arch correction CALL.
  budget: one session

END_OF_FILE: live/health/NOW.md
