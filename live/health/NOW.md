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
  CALL c-health-training-activity-shape-002
  to: session
  direction: health
  play: shape
  node: g-health-training-activity-system
  goal: |
    The next training/activity bet is small enough to execute, preserves the signed
    training/activity WHAT, and is likely to improve real body outcomes without
    guessing across unresolved architecture or contract seams.
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

    Converge-verify passed on 2026-06-26:
    - W1-W20 remain signed and unchanged.
    - §CONTRACTS TA-CA1..TA-CA12 coverage is complete.
    - A1-A5 are closed, arch_open=0, owner_gate_batch=[].
    - Architecture picks are input evidence only; do not copy A1-A5 picks into done_when.
    - D-kernel-1 is imported as registry-line control-plane decide-and-inform.
    - Guided-session durability is compatible with the kernel job contract under the
      checkpoint-as-job-boundary / same-LOG-family reading.
    - WA-K8 topology is closed on paper and must remain a later product acceptance
      proof with live nutrition sibling + attached training removal + one training
      procedure disablement.

    Binding rows for any later executor done_when:
    - Copy the acceptance intent of W1-W20 from
      live/health/work/converge-g-health-training-activity-system.md.
    - Copy §CONTRACTS TA-CA1..TA-CA12 requirements.
    - Preserve especially:
      W1 thin training domain;
      W2 canonical Health AI training authority;
      W3 setup asks only irreducible material facts while programming is system-decided;
      W4 session brief;
      W7 mechanical safety brake;
      W9 review mutates/preserves artifacts;
      W10 equivalent capture routes;
      W11 transient screenshot/external-result confirmation;
      W12 guided training chat bounds;
      W13 normalized session LOG minimum;
      W14 guided interruption durability;
      W15 specialist-tool authority/fallback;
      W16 training<->nutrition contract;
      W17 Direction OS boundary;
      W18 D-kernel-1;
      W19 WA-K8 second-domain proof;
      W20 setup-proven versus body-proven evidence split.
    - Preserve PLAN agenda P1-P12 as HOW-only input:
      namespace/artifact names; concrete program design; session-brief schema;
      LOG schema; screenshot parsing mechanics; adapters/vendor mapping;
      guided checkpoint granularity; review thresholds; safety wording;
      training-demand labels; WA-K8 fixture mechanics; setup/body evidence script.

    Current product facts:
    - health-ai @8246cec has current-head WA-K10 GREEN.
    - nutrition is an ACTIVE thin sibling with program/cycle/week/menu/recipe
      artifacts and cursor DAY_LOOP.
    - Raw workout/activity/pulse/wearable data and screenshots must not enter
      Direction OS state.
  boundaries: |
    Do not implement training/activity or modify health-ai.
    Do not activate a bet until shape reaches owner approval.
    Do not create an executor CALL in this shape session unless shape itself
    validly closes with an owner-approved next execution route.
    Do not prescribe a concrete workout program or freeze exercise/volume/intensity/
    vendor magnitudes during shape.
    Do not weaken or silently modify signed W1-W20.
    Do not reopen the kernel unless a direct contradiction is proven.
    Do not copy A1-A5 architecture picks into executor done_when; they are
    context-only input evidence.
    Keep screenshots and raw workout/activity/pulse/wearable data out of Direction OS.
  done_when: |
    An owner-approved training/activity bet has appetite, kill_by, real cut list,
    verdict for every CHARTER lens, a task testing the riskiest assumption first,
    no more than three active tasks, and a ready first CALL. The shaped route
    preserves W1-W20 acceptance, TA-CA1..TA-CA12 contracts, P1-P12 as PLAN agenda,
    setup/body evidence split, D-kernel-1 import, and WA-K8 second-domain proof
    as a later acceptance requirement.
  return: |
    RESULT with owner-approved TREE/NOW state_changes and the next CALL.
  budget: one session

END_OF_FILE: live/health/NOW.md
