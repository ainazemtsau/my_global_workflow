# NOW — indie-game-development
updated: 2026-06-30 by s-reshape-sparse-dominant-001

bet:
  node: g-9c41
  status: active
  goal: |
    Networked co-op gas core, currently on the CHARACTER ROAD: Sc-types →
    Sc-weight → Sc-reactions → Sc-damage. The far-tier S3/S4/S5 scale plumbing is
    parked until levels get big.
  current_truth: |
    Sc-types AND Sc-weight delivered + merged (GasCoopGame origin/main @61b7923, --no-ff;
    history/s-work-031.md + s-work-033.md). 2026-06-30 OWNER DESIGN PASS (s-design-gas-core-001)
    LOCKED gas representation = sparse-dominant + env-derived dynamic typing + condition-waves.
    The road RE-SHAPED 2026-06-30 (s-reshape-sparse-dominant-001, owner present, G9 + 3 forks
    resolved): a NEW slice **Sc-rep** (re-represent dense→sparse-dominant + per-cell dominant-type
    STAMP socket + preserve the collapse/expand seam + the FIRST hangar measurement) is shaped (G6)
    and inserted AFTER Sc-weight, BEFORE Sc-reactions — it is now the active task (full shaped card:
    work/character-road-shape-2026-06-29.md §SLICE Sc-rep). SPEC edited with owner G9: Факт-4
    representation RESOLVED = sparse-dominant; §5 records the env-derived dynamic-typing core
    requirement; §6 п.3 hangar re-homed to Sc-rep; §9.5 checksum-member list extended (stamp +
    overlay, cell-keyed). Shape drafts adversarially vetted (workflow wf_967a4625-2a4: 29 findings →
    24 survived → folded; 5 refuted). Sc-reactions / c-exec-021 is HELD + RE-SCOPED onto
    sparse-dominant (work/c-exec-021-call.md banner: mix-overlay section rewritten, outcome-registry
    kept OFF the Wave-2-LOCKED GridEvent bus, dense→sparse §Re-sync touchpoints listed, forks +
    full re-hardening deferred to its shape; ADR shifts — Sc-rep=ADR-0021, c-021=next-free≈0022,
    verify at tip). Owner forks resolved (took recommendations): (1) accept ~1-slice milestone tail
    move (honest: 4th consecutive engine-only slice — pre-mortem-#2 tunnel; g-7e15 visual is the
    parallel player-facing surface); (2) cell overflow (>K co-resident types) = LOUD THROW at the
    representation (mass conserved, no silent loss; declared-sink is a reactions-design choice later);
    (3) roster size = config, ~128 a suggested start, tunable without SPEC re-sign. next = FRAME the
    Sc-rep executor CALL c-exec-022 (PLAN-first, owner present) + adversarial-hardening workflow,
    then owner opens it in a fresh GasCoopGame_dev session.
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
  - id: Sc-rep
    status: active
    goal: |
      Re-represent the near gas field dense `int[species][cell]` → SPARSE-DOMINANT (per active
      cell: dominant type + amount + small bounded inline mix-overlay), lay a per-cell dominant-type
      STAMP (the socket env-derived typing/waves/reactions key off), roster size = config, single-type
      run BYTE-IDENTICAL to the post-Sc-weight golden, determinism preserved (ADR-0002), the big-space
      collapse/expand seam preserved, and the architecture's one unmeasured number — the hangar —
      measured first-hand. ENGINE-ONLY. The typing MECHANISM (accumulator/flip) is NOT built this
      slice (stamp socket only).
    done_when: |
      Framed as executor CALL c-exec-022 (PLAN-first, owner present) + adversarially hardened, then the
      GasCoopGame_dev RESULT satisfies the shaped slice (work/character-road-shape-2026-06-29.md §SLICE
      Sc-rep — the folded gate battery): sparse-dominant cell layout (fixed-size inline, NOT a hashmap,
      GC-zero steady-state); per-cell dominant STAMP folded into MeaningChecksum CELL-KEYED with 3 RED
      controls (ISOLATION, DISTINCTNESS same-mass-different-layout-diverges, cross-peer divergence);
      dense→sparse conversion CONSERVES cell-total mass EXACTLY (RED on a >K-co-resident cell; a silent
      drop FAILS; overflow = LOUD THROW; stamp = max-mass species, tie = lowest TypeId); roster size =
      config (RED: change = data only); single-type no-regression byte-identical to the post-Sc-weight
      golden (verified first-hand at the tip); collapse/expand seam preserved; determinism (both scan
      roots; new dir → both lists); ZERO-LEGACY dense path removed AFTER a read-path check (no live dev2
      near-read consumer breaks); FIRST hangar measurement (MEASURE-ONLY, honest partial); -Deliver
      GREEN + mutation ≥70 + independent-author REDs + fresh-session G5 + owner-eye.
    status_note: |
      Active since 2026-06-30 (the bet re-shaped here, s-reshape-sparse-dominant-001). Slice shaped G6
      (appetite = one slice; split-trip BY MACHINERY — leg1 = full layout + stamp + cell-keyed fold +
      no-regression + determinism + hangar; leg2 = K/overflow-policy + seam check; the stamp is NOT
      deferred out of leg1). Drafts adversarially vetted (wf_967a4625-2a4: 24 findings folded). Owner
      forks: overflow = LOUD THROW (mass-conserving); roster size = config. next = frame c-exec-022.

next_slices:
  - Sc-reactions after Sc-rep: the RE-SCOPED c-exec-021 (integer chemistry on the sparse-dominant
    overlap front, telegraph+bang = coarse event, axes-not-pairs, condition-waves forked; HELD until
    the road reaches it, full re-hardening then).
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
  - id: c-exec-021
    to: executor
    for: g-9c41 / Sc-reactions
    issued: 2026-06-30
    call: work/c-exec-021-call.md
    note: |
      HELD + RE-SCOPED 2026-06-30 (s-reshape-sparse-dominant-001) onto sparse-dominant (see the
      banner at the top of work/c-exec-021-call.md): base now post-Sc-rep; mix-overlay section
      rewritten (dense-canon STOP deleted; STOP = reverting to dense planes); reactions on the
      overlap front; schema toward AXES; outcome registry on the near VoxelField (NOT the
      Wave-2-LOCKED GridEvent bus); condition-waves folded as a fork (propagation channel flagged
      as possibly-unbuilt machinery); dense→sparse §Re-sync touchpoints listed; forks + full
      re-hardening deferred to its shape. Does NOT fire until the road reaches reactions (after
      Sc-rep). ADR shifts to next-free (≈0022, verify at tip). dev->main merge + push owner-gated.

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
  - Sc-reactions CALL framed + hardened (then HELD): history/s-work-034.md; work/c-exec-021-call.md
  - Reaction/typing design + sparse-dominant LOCK (2026-06-30): work/gas-reaction-typing-design-2026-06-30.md; history/s-design-gas-core-001.md
  - Road RE-SHAPED to sparse-dominant + Sc-rep slice + SPEC edit + c-021 re-scope (2026-06-30): history/s-reshape-sparse-dominant-001.md; work/character-road-shape-2026-06-29.md (§SLICE Sc-rep); vet workflow wf_967a4625-2a4

next:
  CALL c-frame-sc-rep
  to: session
  direction: indie-game-development
  play: work
  node: g-9c41
  goal: |
    The Sc-rep executor CALL c-exec-022 is FRAMED (PLAN-first, owner present; builder does NOT
    author it) and adversarially HARDENED (a 12-lens-style workflow like c-018/c-021), ready for a
    fresh GasCoopGame_dev session to open. It builds the sparse-dominant re-representation per the
    shaped Sc-rep slice + the folded vetting findings + the sparse-dominant SPEC canon.
  context: |
    work/character-road-shape-2026-06-29.md §SLICE Sc-rep (the shaped slice + folded gate battery —
    read FIRST).
    knowledge/g9c41-gas-engine-SPEC.md (Факт-4 sparse-dominant lock; §5 dynamic typing; §9.5 checksum
    stamp+overlay; §6 п.3 hangar; §4 шов 2/4/5/7 collapse/expand seam).
    work/gas-reaction-typing-design-2026-06-30.md (the owner design lock).
    work/c-exec-021-call.md (the re-scoped sibling — pattern + RE-SCOPE banner).
    Folded must/should-fixes from vet workflow wf_967a4625-2a4 (cell-keyed stamp 3 REDs; conversion
    mass-conservation + stamp=max-mass/lowest-TypeId tiebreak; fixed-inline-no-hashmap GC-zero gate;
    no-regression first-hand golden; ZERO-LEGACY read-path check + dev2 boundary; determinism scan-dir
    contingency; cache-friendliness falsifier; partial-hangar honesty).
  boundaries: |
    Owner present at the PLAN (G9). Verify c-exec-022 is free at framing (mirror the ADR tip-verify
    discipline; bump + record if taken). Sc-rep claims ADR-0021 (supersedes the ADR-0018 dense
    decision; verify sub-number at tip). Do NOT build the typing MECHANISM (stamp socket only). Do NOT
    build S4 / big-space (collapse/expand seam only). Do NOT touch the dev2 visual track. ADR-0002 not
    reopened. Cell overflow (>K) = LOUD THROW (no silent loss; a declared-sink is a reactions-design
    choice, not this slice).
  done_when: |
    c-exec-022 framed (PLAN-first, owner present) + adversarially hardened (workflow), carrying the full
    folded gate battery; NOW open_calls registers it; owner opens it in a fresh GasCoopGame_dev session.
  return: a framed + hardened c-exec-022 ready to open.
  budget: one framing session + an adversarial-hardening workflow.

END_OF_FILE: live/indie-game-development/NOW.md
