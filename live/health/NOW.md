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
  CALL c-health-training-activity-converge-001
  to: session
  direction: health
  play: converge
  node: g-health-training-activity-system
  goal: |
    Training/activity has a closed owner-signed WHAT specification so a
    subsequent shape session can select a small executable bet without guessing
    and without losing the path to real body outcomes.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/history/2026-06-20-s-health-core-kernel-wave0-derisk-001.md
    - live/health/work/converge-g-health-core-kernel.md
    - live/health/work/converge-g-health-core-kernel-arch.md
    - live/health/history/2026-06-24-s-health-core-kernel-wa-k10-evidence-repair-001.md

    g-health-core is closed done. Current health-ai nutrition state has an
    ACTIVE program, cycle, week plan, fixed menu and recipe book, with cursor
    DAY_LOOP. No active Direction OS bet exists.

    g-health-training-activity-system currently combines:
    - strength/body-composition progression;
    - conditioning, walking, cycling and VR activity;
    - conservative medical/safety boundaries;
    - adherence and bad-week recovery;
    - Hevy-like, Strava-like, VR and wearable interfaces;
    - cross-module exchange with nutrition;
    - a thin domain attachment to the existing kernel.

    Explicit inputs, not automatic scope:
    - D-kernel-1: governance of the registry-line write before the first cold
      second-domain attach; prior recommendation was infrastructure control-file,
      decide-and-inform.
    - Strongest WA-K8 second-domain test: removing one domain must leave kernel
      and all remaining domains green; disabling one procedure must leave its
      siblings green.

    The preceding shape session stopped because no training/activity converge
    assembly, signoff or refutation existed.
  boundaries: |
    Do not implement training or activity.
    Do not author or modify health-ai product artifacts.
    Do not activate a bet or create execution tasks.
    Do not reopen kernel breadth by default; touch core contracts only where the
    second-domain boundary forces an explicit WHAT property.
    Do not prescribe a concrete workout program during converge.
    Keep raw workout, activity, pulse and wearable logs out of Direction OS.
    Minor Health AI papercuts remain in r-health-ai-minor-fix-lane.
  done_when: |
    A citation-backed, forward-clean, owner-signed WHAT set covers the node's
    done_when, every CHARTER lens, training↔nutrition boundary, safety properties,
    specialized-tool boundary, real-body-execution requirement, D-kernel-1 and
    the WA-K8 second-domain acceptance question; it is routed through
    converge-arch and converge-verify as required before shape.
  return: |
    RESULT with exact work/NOW/LOG/history state_changes, owner signoff evidence
    for genuine owner forks, and the ready next converge-arch or converge-verify
    CALL.
  budget: one session

END_OF_FILE: live/health/NOW.md
