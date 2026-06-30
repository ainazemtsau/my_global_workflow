# NOW — indie-game-development
updated: 2026-06-30 by s-repair-now-hygiene-002

bet:
  node: g-9c41
  status: active
  goal: |
    Networked co-op gas core, currently on the CHARACTER ROAD: Sc-types →
    Sc-weight → Sc-reactions → Sc-damage. The far-tier S3/S4/S5 scale plumbing is
    parked until levels get big.
  current_truth: |
    Sc-types AND Sc-weight are both delivered + merged (GasCoopGame origin/main
    @61b7923, --no-ff; history/s-work-031.md + history/s-work-033.md). Sc-weight
    (per-type vertical buoyancy — heavy sinks / light rises, creeping integer
    Z-face bias, ENGINE-ONLY) closed against all 10 done_when with a BINDING
    fresh-session G5 = COULD-NOT-REFUTE (s-work-033). The road now rolls to
    Sc-reactions: it is the active task, its executor CALL (c-exec-021) to be
    framed + hardened in a fresh OS session (builder does NOT author it).
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
    - live/indie-game-development/history/s-work-033.md
    - live/indie-game-development/history/2026-06-30-c-exec-020-sc-weight-result.md
    - live/indie-game-development/work/now-snapshot-2026-06-29.md

tasks:
  - id: Sc-reactions
    status: active
    goal: |
      Integer chemistry between weight-class types on the near grid: reactions read
      from a small FIXED set of data axes (not N², a new type = 0 new code branches),
      telegraph + bang, surfacing co-op interdependence pressure. Builds on the
      Sc-weight buoyancy substrate.
    done_when: |
      Its executor CALL (c-exec-021) is framed + hardened, then the GasCoopGame_dev
      RESULT satisfies it: integer/data-driven reactions, determinism preserved
      (ADR-0002 lock intact), the usual gate battery (-Deliver GREEN, mutation >=70,
      independent-author REDs, fresh-session G5, ZERO-LEGACY, owner-eye).
    status_note: |
      Active since s-work-033 (the bet rolled here when Sc-weight closed). CALL
      c-exec-021 NOT yet framed — see NOW.next (a fresh OS session frames + hardens
      it, owner present at PLAN; builder does NOT author it).

next_slices:
  - Sc-damage after Sc-reactions: dose-from-coarse, type-specific damage, temperature sink-layer.

open_calls:
  - id: c-visual-003
    to: executor
    for: g-7e15 / visual wave 1
    issued: 2026-06-29
    call: work/c-visual-003-call.md
    note: |
      Ready for a fresh GasCoopGame_dev_2 session after the degraded uncommitted
      S2 work is rolled back to the clean baseline. Opens with a PLAN, owner
      present, then returns RESULT home.

recurring: []

parallel_tracks:
  - id: g-7e15
    track: VISUAL / GASG
    track_state: active
    note: |
      Secondary to g-9c41, no fixed hour quota. c-visual-002 S1 gas-lab delivered
      and merged (history/s-visual-009.md). 2026-06-29 RE-PLAN (s-visual-010,
      owner-co-created): the framed S2 (two-type + scatter-glow tuned in the EMPTY
      analytic gas-lab) degraded to jelly/blobs/visible-grid — WORSE than before;
      root cause (verified in code) = judging the look in an empty void on a
      low-ceiling cheap-noise render + blind live knob-turning. RE-PLANNED to judge
      on the REAL sim in a real lit room (RealGasViewSource reads VoxelField render-
      only; structurally cannot write the sim) with a NEVER-WORSE discipline (saved
      baseline + A/B + one-inspector control panel + one visible win at a time).
      The degraded S2 work was uncommitted on dev2 only (main @7d08882 untouched) ->
      rolled back to the clean baseline; nothing bad merged. Official WAVE plan =
      work/gas-visual-wave-plan-2026-06-29.md (4 waves toward the JEWEL + a parallel
      engine finer-grid track; ~3 of ~10 look levers used). NEXT visual work = WAVE 1
      CALL work/c-visual-003-call.md (real room + real sim + light-through + base-
      render cleanup + first two-type; opens in a fresh GasCoopGame_dev_2 session
      with a PLAN, owner present, comes HOME with an owner-eye sign). The old
      "S2 two-type+scatter as framed" is SUPERSEDED by this re-plan. Reading set incl.
      docs/gas-visual-stage-plan.md §S1/§S6+ and the canon visual-style minimal note
      (history/s-canon-visual-style-minimal-gas-stage-001.md).
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
  - id: codex-sidecar
    track: CODEX SIDECAR / LAB
    track_state: active
    note: |
      Direction-specific process stood up 2026-06-30 for using Codex alongside
      Cloud Code without stealing the main bet or overlapping active Cloud Code
      files. Modes: Scout (read-only), Pair-Lab (owner-present small Unity
      iterations), Formal Leg (normal engineering contour/OpenSpec for
      load-bearing work). Process: plays/codex-sidecar.md; design:
      work/codex-sidecar-track-2026-06-30.md; ledger:
      work/codex-sidecar/board.md. It assigns no concrete build task yet and
      preserves the main next CALL.

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
  - Sc-weight delivered + binding-G5 closed: history/s-work-033.md; history/2026-06-30-c-exec-020-sc-weight-result.md
  - Visual gas-lab S1 delivered: history/s-visual-009.md
  - Visual re-plan to real-sim waves: history/s-visual-010.md; work/gas-visual-wave-plan-2026-06-29.md; work/c-visual-003-call.md
  - Fixed-hour quota cleanup: history/s-work-hours-quota-cleanup-001.md
  - Visual style canon update: history/s-canon-visual-style-minimal-gas-stage-001.md
  - Codex Sidecar process: work/codex-sidecar-track-2026-06-30.md; plays/codex-sidecar.md; work/codex-sidecar/board.md

next:
  CALL c-frame-021
  to: session
  direction: indie-game-development
  play: work
  node: g-9c41
  task: Sc-reactions
  goal: |
    The next CHARACTER-ROAD executor CALL -- c-exec-021 (Sc-reactions: integer
    chemistry between weight-class types) -- is framed + adversarially hardened and
    ready as a self-contained artifact under work/, for a fresh GasCoopGame_dev
    session to open with a PLAN (owner present).
  context: |
    live/indie-game-development/NOW.md (Sc-reactions = the active task).
    live/indie-game-development/knowledge/g9c41-gas-engine-SPEC.md (reactions =
    data axes, not N²; Факт-4).
    live/indie-game-development/work/character-road-shape-2026-06-29.md (the road;
    Sc-reactions slice).
    live/indie-game-development/history/2026-06-30-c-exec-020-sc-weight-result.md
    (the Sc-weight substrate it builds on).
    Decision d-coop-interdependence-repin-001: fold co-op interdependence into
    this PLAN as its recommended home.
    GasCoopGame main @61b7923 (base at-or-after; §Re-sync confirms HEAD first).
  boundaries: |
    The builder does NOT author this CALL -- the direction frames it. ENGINE-ONLY
    unless the shape says otherwise; do not reopen ADR-0002; renumber the engine
    ADR off the dev2 visual-track number collision at the cross-track merge.
  done_when: |
    work/c-exec-021-call.md exists and is hardened: goal = integer reactions
    between weight-class types (telegraph + bang, co-op interdependence pressure),
    per-type DATA not code-branching, determinism preserved, the usual gate
    battery; ready for a fresh GasCoopGame_dev session opening with a PLAN.
  return: |
    A hardened c-exec-021 CALL artifact; NOW.next repointed to it.
  budget: one framing session (+ an adversarial-hardening workflow).

END_OF_FILE: live/indie-game-development/NOW.md
