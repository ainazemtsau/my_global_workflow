# NOW — indie-game-development
updated: 2026-06-29 by s-repair-now-hygiene-001

bet:
  node: g-9c41
  status: active
  goal: |
    Networked co-op gas core, currently on the CHARACTER ROAD: Sc-types →
    Sc-weight → Sc-reactions → Sc-damage. The far-tier S3/S4/S5 scale plumbing is
    parked until levels get big.
  current_truth: |
    Sc-types is delivered and merged (GasCoopGame origin/main @7d08882,
    history/s-work-031.md). Sc-weight is active and its executor CALL is framed +
    hardened (history/s-work-032.md, work/c-exec-020-call.md), awaiting the
    GasCoopGame_dev executor RESULT.
  appetite: |
    Wave/core appetite remains governed by the g-9c41 de-risk wall; do not extend
    a bet silently. If the current slice overruns or reveals a core blind spot,
    stop and re-shape/review instead of stretching the appetite.
  kill_by: |
    2026-07-05 checkpoint for the de-risk wall; 2026-07-24 remains the milestone
    target for Waves A→B / visible gas progress, with the tail movable.
  sources:
    - live/indie-game-development/TREE.md#g-9c41
    - live/indie-game-development/knowledge/g9c41-gas-engine-SPEC.md
    - live/indie-game-development/work/character-road-shape-2026-06-29.md
    - live/indie-game-development/history/s-work-031.md
    - live/indie-game-development/history/s-work-032.md
    - live/indie-game-development/work/now-snapshot-2026-06-29.md

tasks:
  - id: Sc-weight
    status: active
    goal: |
      Per-type vertical buoyancy on the near grid: heavy gas sinks and light gas
      rises via integer Z-face bias, a creeping front, never a near per-column sort.
    done_when: |
      The executor RESULT satisfies work/c-exec-020-call.md: PLAN owner-present,
      per-type Z-bias buoyancy, conservation/no-pop/settle REDs, determinism,
      ContentHash fold for the new weight override, no hardcoded type dispatch,
      -Deliver GREEN, mutation >=70, fresh-session G5, ZERO-LEGACY, owner-eye.
    status_note: |
      Active since s-work-031; c-exec-020 framed+hardened in s-work-032. Awaiting
      executor RESULT from a fresh GasCoopGame_dev session.

next_slices:
  - Sc-reactions after Sc-weight returns clean: integer chemistry, telegraph + bang, co-op interdependence pressure.
  - Sc-damage after Sc-reactions: dose-from-coarse, type-specific damage, temperature sink-layer.

open_calls:
  - id: c-exec-020
    to: executor
    for: Sc-weight
    issued: 2026-06-29
    call: work/c-exec-020-call.md
    note: |
      Ready for a fresh GasCoopGame_dev session. Opens with a PLAN, owner present,
      §Re-sync first, base at-or-after GasCoopGame main @7d08882. May split at PLAN
      if too large. Return RESULT home.

recurring: []

parallel_tracks:
  - id: g-7e15
    track: VISUAL / GASG
    track_state: active
    note: |
      Secondary to g-9c41, no fixed hour quota. c-visual-002 S1 gas-lab delivered
      and merged (history/s-visual-009.md). The next visual work is the S2 look
      sub-leg (two differently-charactered gases + scatter-glow), but no active
      CALL is open in NOW. Use GasCoopGame docs/gas-visual-stage-plan.md §S6+ and
      the canon visual-style update (history/s-canon-visual-style-minimal-gas-stage-001.md)
      when the owner chooses that follow-up.
  - id: g-d3a8
    track: canon/design
    track_state: parked
    note: |
      Canon-forge continues in separate local/canon-forge sessions. Latest visual
      style baseline recorded in history/s-canon-visual-style-minimal-gas-stage-001.md.
  - id: g-2f8c
    track: marketing
    track_state: parked
    note: |
      Latest marketing status rendered in history/2026-06-29-s-marketing-restart-001.md;
      no current CALL in NOW.

decisions:
  - id: d-coop-interdependence-repin-001
    q: |
      Where should the dropped "gas world forces co-op" obligation live so it does
      not become a late hard blocker?
    options:
      - Fold it into Sc-reactions / Sc-damage PLANs as a required owner-eye/gameplay axis.
      - Recreate it as a separate map node before the first co-op gameplay slice.
      - Defer until the first Steam/playtest slice.
    recommendation: |
      Fold into Sc-reactions / Sc-damage PLANs now, because the first real gameplay
      gas consequences are where player interdependence naturally becomes testable.
    source: |
      work/gas-engine-plan-audit-2026-06-29.md; full pre-compaction note preserved
      in work/now-snapshot-2026-06-29.md.

history_pointers:
  - Full pre-compaction NOW: work/now-snapshot-2026-06-29.md
  - Character road shape: work/character-road-shape-2026-06-29.md; history/s-work-030.md
  - Sc-types delivered: history/s-work-031.md
  - Sc-weight CALL framed: history/s-work-032.md; work/c-exec-020-call.md
  - Visual gas-lab S1 delivered: history/s-visual-009.md
  - Fixed-hour quota cleanup: history/s-work-hours-quota-cleanup-001.md
  - Visual style canon update: history/s-canon-visual-style-minimal-gas-stage-001.md

next:
  CALL: work/c-exec-020-call.md

END_OF_FILE: live/indie-game-development/NOW.md
