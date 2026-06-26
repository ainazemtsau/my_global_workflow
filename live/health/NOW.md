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
  CALL c-health-training-activity-converge-arch-001
  to: session
  direction: health
  play: converge-arch
  node: g-health-training-activity-system
  goal: |
    Training/activity has closed consumer-driven contracts and a refuted
    architecture-on-paper so a later converge-verify can attack the complete
    set before shape selects a small executable bet.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-training-activity-system.md
    - live/health/work/converge-g-health-core.md
    - live/health/work/converge-g-health-core-kernel.md
    - live/health/work/converge-g-health-core-kernel-arch.md
    - live/health/history/2026-06-20-s-health-core-kernel-wave0-derisk-001.md
    - live/health/history/2026-06-24-s-health-core-kernel-wa-k10-evidence-repair-001.md

    The signed training/activity WHAT is W1-W20 with glossary G-TA-1..G-TA-9.
    Owner signoffs:
    - Define: "ок согласен", including setup proof without a mandatory
      completed workout, split tool authority, and D-kernel-1 option A.
    - Resolve: "Да, согласен с пакетом B", amended so screenshots are transient:
      show extracted data for owner correction/confirmation, ask materially
      useful follow-ups, save only the structured normalized result.

    This is a heavy sibling-bearing node. Required architecture questions:
    - A1 guided-session durability versus save-at-job-boundary and one-chat-one-job;
    - A2 placement of session brief, guided run, normalized LOG, review, and
      mutation in the existing kernel job/state/artifact model;
    - A3 specialist screenshot/export extraction, confirmation, provenance,
      confidence, and media disposal;
    - A4 routine training-demand plus review-level training↔nutrition handoff,
      with no direct module-file dependency;
    - A5 strongest WA-K8 two-live-domain removal and one-procedure-disable proof.

    Current product facts:
    - health-ai @8246cec has current-head WA-K10 GREEN.
    - nutrition is an ACTIVE thin sibling with program/cycle/week/menu/recipe
      artifacts and cursor DAY_LOOP.
    - current registry grammar already houses D-kernel-1 as control-plane
      decide-and-inform.
  boundaries: |
    Do not implement training/activity or modify health-ai.
    Do not activate a bet, create execution tasks, or emit an executor CALL.
    Do not prescribe a concrete workout program or freeze exercise/volume/
    intensity/tool-vendor magnitudes into WHAT.
    Do not weaken or silently modify signed W1-W20.
    Do not reopen the kernel by default; name an explicit contract delta only
    where the second-domain boundary forces it.
    Keep architecture picks in context-only evidence, never in done_when.
    Keep screenshots and raw workout/activity/pulse/wearable data out of
    Direction OS.
  done_when: |
    - §CONTRACTS names every TREE interaction with core, nutrition, specialist
      input/tools, and Direction OS; each states consumer, producer, behavior,
      direction, trigger, and build-order without HOW leakage.
    - Heavy decomposition records internal seams and decides whether any part
      must become a sub-node.
    - A1-A5 each has a 3-5 option refuted comparison and a signed pick only if a
      genuine owner fork remains.
    - Guided-session durability is demonstrably compatible with the kernel job
      contract or returns a named blocker before shape.
    - Training↔nutrition routine and review-level flows are frozen without
      direct module-file coupling.
    - D-kernel-1 is imported rather than re-litigated unless a contradiction is
      proven.
    - WA-K8 proof topology covers a live nutrition sibling, training removal,
      and one training-procedure disablement.
    - contract_coverage is complete, arch_open is zero, and architecture remains
      context-only.
    - Next CALL is converge-verify, not shape or executor.
  return: |
    RESULT with exact work/NOW/LOG/history state_changes, contract and
    architecture signoff evidence, and the ready converge-verify CALL.
  budget: one session

END_OF_FILE: live/health/NOW.md
