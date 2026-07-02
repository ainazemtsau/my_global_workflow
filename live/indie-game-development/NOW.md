# NOW — indie-game-development
updated: 2026-07-02 by s-shape-prep-screactions-001

bet:
  node: g-9c41
  status: active
  goal: |
    Networked co-op gas core, currently on the CHARACTER ROAD: Sc-types →
    Sc-weight → Sc-rep → Sc-kernel → Sc-reactions → Sc-typing → Sc-damage. The far-tier
    S3/S4/S5 scale plumbing is parked until levels get big.
  current_truth: |
    Sc-types + Sc-weight + Sc-rep delivered and MERGED to GasCoopGame main (origin/main @5442be0,
    2026-07-02, s-work-037). Sc-kernel (active-front tick iteration) is FRAMED + HARDENED next,
    before Sc-reactions (d-sparse-tick-kernel-001, owner-signed 2026-07-02) — awaits a fresh
    GasCoopGame_dev executor session with an owner-present PLAN. Sc-reactions (c-exec-021) is
    PREPPED and waiting on Sc-kernel GREEN. VISUAL track ON HOLD per owner directive 2026-07-02
    («сначала разобраться с симуляцией»). Sim-plan audit (2026-07-02) confirmed architecture/locks/
    road correct for the owner's requirement ladder; richness-tier package adopted (see decisions
    below). Full pre-repair narrative (81 lines): work/now-current-truth-snapshot-2026-07-02.md.
    Session-by-session detail: history_pointers below, latest = history/2026-07-02-s-work-038-sc-kernel-framed.md.
  appetite: |
    Wave/core appetite remains governed by the g-9c41 de-risk wall; do not extend
    a bet silently. If the current slice overruns or reveals a core blind spot,
    stop and re-shape/review instead of stretching the appetite.
  kill_by: |
    De-risk-wall checkpoint 2026-07-05: ANSWERED 2026-07-02 by the real hangar measurement (linear roster scaling) —
    outcome = re-shape d-sparse-tick-kernel-001, SIGNED «да» by the owner 2026-07-02 — the wall is CLOSED honestly. 2026-07-24 remains the visible-gas milestone (telegraph+bang and/or two-type visual on the
    real sim; the old «Waves A→B» wording is retired), tail movable.
  sources:
    - live/indie-game-development/TREE.md#g-9c41
    - live/indie-game-development/knowledge/g9c41-gas-engine-SPEC.md
    - live/indie-game-development/work/character-road-shape-2026-06-29.md
    - live/indie-game-development/history/s-work-031.md
    - live/indie-game-development/history/s-work-033.md
    - live/indie-game-development/history/2026-06-30-c-exec-020-sc-weight-result.md
    - live/indie-game-development/work/now-snapshot-2026-06-29.md

tasks:
  - id: Sc-kernel
    status: framed-awaiting-executor
    goal: |
      Re-point the authoritative tick at the sparse store / active cells: per-tick cost scales with ACTIVE
      cells (+ their open faces + bounded co-resident types), NOT registered roster × domain cells. Behavior
      byte-identical to the post-Sc-rep goldens; determinism preserved (ADR-0002); ENGINE-ONLY.
    done_when: |
      The FRAMED + HARDENED battery = work/c-exec-023-call.md (roster-independence @1 vs 64 + roster-128 row;
      active-scaling; adversarial «hangar flooded» measure-and-BIND → auto-opens d-hangar-flood-fallback-001;
      checksum timed; wake-trigger registry seam + per-active-trigger wake round-trip RED; before/after matrix +
      mine/shaft + TwoStackedRooms Z-fixture + all-cores divisor + bytes/cell + Unity-runtime capture;
      byte-identical no-regression; scans + GC-zero + Coarse/ scan-root closure; field-level storage guard
      (Sc-rep G5 P2); ZERO-LEGACY dense per-tick path removed; -Deliver + mutation ≥70 + independent REDs +
      fresh G5 + owner-eye). The RESULT fills the SPEC §6 п.2 LEVEL-DESIGN CONTRACT ceiling number.
    kill_by: |
      Owner-set 2026-07-02 («все подтверждаю»): appetite = one slice (split-trip by machinery; leg1 = kill-test).
      KILL (approach refuted, not extended) = if gate 2(a) roster-independence can't reach ≤ ~20% roster-1-vs-64
      hangar delta, OR gate 4 byte-identity can't hold with a sparse kernel → KILL + re-shape, no silent
      rebaseline, no appetite extension. Date = 2026-07-16 (leg1 checkpoint). Flooded-over-budget is NOT a kill
      (auto-opens d-hangar-flood-fallback-001; the slice still succeeds).
    status_note: |
      FRAMED + HARDENED 2026-07-02 as work/c-exec-023-call.md (s-work-038, owner present «все подтверждаю»):
      audit §Package item-4 additions (a–k) folded + a standard adversarial pass (wf_ff1612b9-ec5: 11 raised →
      2 P2 confirmed folded [wake round-trip RED; frozen-visual honesty], 9 refuted) + the batched G9 SPEC touch
      (item 8, S1–S10) signed in the SAME session. Base = GasCoopGame main @5442be0 (Sc-rep merged). Next = a
      FRESH GasCoopGame_dev executor session opens c-exec-023 with an owner-present PLAN (the c-exec-022 PLAN
      deviation must not repeat). Do NOT re-fire c-exec-022. dev→main merge owner-gated.
  - id: Sc-rep
    status: delivered-merged
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
      forks: overflow = LOUD THROW (mass-conserving); roster size = config. c-exec-022 framed and
      issued 2026-07-01 as work/c-exec-022-call.md; next = fresh GasCoopGame_dev PLAN owner-present.
      2026-07-02: EXECUTED without the owner-present PLAN (deviation recorded); checkpoint dev @adc3b9d;
      real hangar measurement dev @8db3ee1; honest scope = representation + checksum schema (see
      bet.current_truth). Remaining: fresh-session G5 (with the scope relabel + an audit of the
      review-repair diffs against the S1/c-exec-015 oracles) → owner-eye → owner-gated merge.
      Do NOT re-fire c-exec-022.
      2026-07-02 (later, s-work-036): binding fresh-session G5 RUN = COULD-NOT-REFUTE. Held: conversion
      exact+atomic; stamp cell-keyed (isolation/distinctness/cross-peer); golden = the real post-Sc-weight
      baseline (not rebaselined); scans cover new files (+ planted self-tests); S1 repairs conform to
      d-roomfull-001 and the ForcedFlow battery 66/66; 1130/1130 tests; mutation 74.17 (artifact, read-only).
      ONE finding, P2 (test-gap, not a defect): the hashmap-substitution guard inspects the cell RECORD,
      not the FIELD authority storage — a private Dictionary<int,SparseDominantCellRecord> could pass;
      RESOLUTION = field-level storage guard folded into Sc-kernel done_when #9 (c-exec-023 draft).
      Remaining: owner-eye (confidence) → owner-gated dev→main merge + push. dev2 untouched.
      2026-07-02 (s-work-037): MERGED to main @efaa6eb and PUSHED (origin/main @5442be0); full gate battery
      green on merged main. Sc-rep is CLOSED; the road rolls to Sc-kernel.

next_slices:
  - Sc-kernel (SIGNED «да» by the owner 2026-07-02, d-sparse-tick-kernel-001) BEFORE Sc-reactions: re-point the tick kernel at the
    sparse store / active cells (kill the per-species dense expand+rebuild; cost becomes ∝ active cells, not
    roster × domain cells). done_when re-runs the 2026-07-02 measurement matrix before/after + an adversarial
    «hangar flooded» all-cells-active scenario + a Unity-runtime capture; also closes the Coarse/ scan-root hole.
    FRAMED + HARDENED CALL: work/c-exec-023-call.md (s-work-038; audit item-4 additions folded, G9 SPEC batch signed).
  - Sc-reactions after Sc-kernel: c-exec-021 PREPPED 2026-07-02 (s-shape-prep-screactions-001, owner present —
    forks (a)–(f) closed; body FULLY REWRITTEN at work/c-exec-021-call.md, banner generations retired): integer
    chemistry on the sparse-dominant overlap front; rule schema = explicit-SET > AXIS (default) > optional
    env-conditioned DEFAULT rows > identity, all data in the handshake hash; telegraph+bang = coarse event, blast
    wave GAMEPLAY-load-bearing; layered mass-conserving overflow (any-N ZONE mixing = the requirement, per-cell
    K = internal config; chemistry-first → admission clamp → config-K); condition-waves forked with pinned
    exactly-once (cell,wave-id) semantics; outcome registry on near VoxelField; old ReactionLayer demo tier =
    DELETE via owner-pre-signed live-spec amendment. AWAITS Sc-kernel GREEN; §Re-sync + full re-hardening at fire.
  - Sc-typing after Sc-reactions (homing decided 2026-07-02 at the shape-prep: placement owner-delegated,
    mechanism owner-agreed; audit local-depth-03 fix): the typing MECHANISM — env-derived spawn typing + runtime
    ACCUMULATE-WITH-HYSTERESIS flip (over instant flip); one new replicated cell-keyed SKIP-ZERO checksum member
    (schema decision at its shape); owns regime-vs-identity + single-reactant env-row firing semantics (routed
    from the Sc-reactions shape); temperature rows dormant until d-tempfeedback-001 (named re-entry = Sc-damage
    shape); consumes the Sc-kernel env-delta wake stub. The July demo-road shape (07-10..15) is the named
    checkpoint where Sc-typing↔Sc-damage order may be consciously swapped — never silently.
  - Sc-damage after Sc-typing: dose-from-coarse, type-specific damage, temperature sink-layer.

open_calls:
  - id: c-exec-023
    to: executor
    for: g-9c41 / Sc-kernel
    issued: 2026-07-02
    call: work/c-exec-023-call.md
    note: |
      FRAMED + HARDENED 2026-07-02 (s-work-038, owner «все подтверждаю»). Base = GasCoopGame main @5442be0.
      Opens with an owner-present PLAN in a FRESH GasCoopGame_dev session (the c-exec-022 PLAN deviation must
      not repeat). Audit §Package item-4 additions folded (wake-trigger seam + wake round-trip RED,
      checksum-scaling schema decision, flooded measure-and-BIND → d-hangar-flood-fallback-001, roster-128,
      mine/shaft probe, TwoStackedRooms Z-fixture, all-cores divisor, bytes/cell, weak-CPU proxy, JEWEL GUARD,
      07-24 milestone re-affirm w/ frozen-visual honesty). approach token = active-front-tick-kernel-over-sparse-store.
      kill_by = 2026-07-16 (roster-independence / byte-identity refuted → kill+re-shape). The RESULT fills the
      SPEC §6 п.2 ceiling number. On GREEN → re-harden + fire c-exec-021 (Sc-reactions). dev→main merge owner-gated.
  - id: c-visual-003
    to: executor
    for: g-7e15 / visual wave 1
    issued: 2026-06-29
    call: work/c-visual-003-call.md
    note: |
      W1a CLOSED 2026-07-02: owner-eye SIGNED WITH RESERVATIONS in-chat (dev2 @40b94cc — checklist +
      F-OWNER + RESULT flipped to DELIVERED). Honest state: render FOUNDATION accepted (de-block +
      light-through + never-worse + one inspector); clean LP1–LP5 NOT claimed — LP1 candidate-pass
      (lamp-direction read weak), LP2/LP3 confirmed live, LP4/LP5 blocked by the missing DESIGNED demo
      level (owner-eye finding: «demo level needs design»; existing levels = boxy 6×4×6 box /
      horizontal tube). NEXT visual leg per the RESULT = a deliberately-DESIGNED gas demo scene
      (roomy vertical space + finite plume + matched room/camera/colour; to be framed as
      c-visual-004; ties to the canon visual-style track) — focused design work, NOT live knob-tuning
      (the S2 anti-pattern). W1b (two-type read) RE-SCOPED 2026-07-02 (banner in the CALL): after the
      Sc-rep dev→main merge; needs a small owner-acked engine read-API for the per-cell dominant
      STAMP; no argmax/dense workaround. dev2→main MERGED 2026-07-02 (@b5675ea) and PUSHED.
      ⚠ TRACK ON HOLD (owner 2026-07-02: «сначала разобраться с симуляцией») — W1b and the
      designed-demo-scene leg (c-visual-004) WAIT; do not frame them until the owner returns to visual.
  - id: c-exec-021
    to: executor
    for: g-9c41 / Sc-reactions
    issued: 2026-06-30
    call: work/c-exec-021-call.md
    note: |
      PREPPED 2026-07-02 (s-shape-prep-screactions-001, owner present): the body at work/c-exec-021-call.md is
      FULLY REWRITTEN onto the current base (sparse-dominant, base = post-Sc-kernel main) — both banner
      generations (items 1–10, 11–17) RETIRED into it; the 2026-06-30 hardening (wf_86b1f6d0-bda) preserved as
      principle; audit §Package item 5 pins (a)–(f) folded with finding-id traceability. Shape forks CLOSED
      in-session (owner; full record = history/2026-07-02-s-shape-prep-screactions-001.md):
      (a) overflow = layered mass-conserving (chemistry-first via the NORMAL telegraph law → admission-clamp
      floor → config-K) + owner REFRAME: any-N ZONE mixing is the requirement, per-cell K = internal config
      constant, never a design cap («если можно сделать любое количество … это не требование, это устаревшее»);
      junction RED parametrized in N (≥5 + one higher), worded «survives MASS-EXACTLY»; LOUD THROW demoted to
      non-flow invariant assert; R1 owner-eye junction scene added.
      (b) schema = FOUR data tiers: explicit reactant-SET > AXIS (default) > optional env-conditioned DEFAULT
      rows (owner addition; blanket defaults rejected) > identity/no-chemistry; precedence deterministic; all
      tiers + outcome-registry + axis-coordinate table in the handshake hash. Firing scope THIS slice =
      multi-reactant rules only; single-reactant env-response rows = schema-admitted data whose firing semantics
      land at Sc-typing (no instant-flip side door).
      (c) condition-waves stay a FORK; semantics PINNED (owner delegated → decided): each gas parcel converts
      EXACTLY ONCE per wave ((cell,wave-id) idempotence) + wave×wind RED oracle.
      (d) blast wave = GAMEPLAY-load-bearing (pre-decision 16 confirmed); bang-read owner-eye axis incl. one
      open-field no-walls detonation, failed read = signed TIER-ladder evidence; owner extension ROUTED not
      promised: bodies/loot → Sc-damage (after шов-7 player-kinematics), walls → S5; reserved DORMANT outcome
      kinds (body-impulse, wall-breach, ignite/freeze).
      (e) typing homing = NAMED slice Sc-typing immediately after Sc-reactions (placement owner-delegated →
      decided; mechanism accumulate-with-hysteresis owner-agreed) — see next_slices; consume-vs-residue = per-rule
      DATA at the PLAN; regime-vs-identity routed to the Sc-typing shape.
      (f) outcome registry on the near VoxelField; old ReactionLayer demo tier = ZERO-LEGACY DELETE via
      owner-pre-signed live-spec amendment («если нам какой-то класс не нужен, мы legacy не храним, удаляем …
      Просто так не держать») — scoped to demo files + their ReactionLayer SHALL lines ONLY; GridEvent bus/enum
      stays locked (Reaction=3 STAYS); verify-uncomposed first, STOP on live composition or wider SHALL.
      PENDING (await the Sc-kernel RESULT; CALL §PENDING): weak-hardware budget fork (flooded number + CPU
      proxy), wake-source exact binding (binds «reaction front» stub; env-delta reserved for Sc-typing), base
      sha + golden identity, MeaningMembers bits, scan roots, contract version, ADR-E number.
      Rewrite adversarially checked vs STATE (wf_8ab4a0cb-401: 36 raised → 10 machine-verified + 26
      first-hand-adjudicated → ~22 distinct defects folded, 0 construction-breaking; subagent quota cut the
      verify fleet mid-run — adjudication finished first-hand in-session, recorded). The code-grounded FULL
      re-hardening + §Re-sync sweep still run at fire time. Does NOT fire until Sc-kernel GREEN (owner-gated
      dev→main merge). dev→main merge + push owner-gated.
  # c-exec-022 (Sc-rep) CLOSED 2026-07-02: G5 COULD-NOT-REFUTE → owner-eye → merged @efaa6eb, pushed
  # (origin/main @5442be0). Record: history/2026-07-02-s-work-036-screp-g5-kernel-signed.md + s-work-037.

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
  - id: d-gas-richness-tiers-001
    status: answered — TIER-1 shipped (2:1 open-space lean); TIER-2 (lattice-gas vortices) / TIER-3 (fixed-point
      stored velocity) reserved behind a named owner-eye re-trigger (bang-read / open-space jet). Full record:
      work/audit-gas-sim-plan-2026-07-02.md (local-depth-01, multiplayer-06); SPEC §6 п.9 + §3.
  - id: d-hangar-flood-fallback-001
    status: armed-dormant — created 2026-07-02 (s-work-038). AUTO-OPENS iff the Sc-kernel flooded-hangar capture
      (c-exec-023 gate 2c) projects OVER the weak-peer budget; otherwise the Sc-kernel RESULT closes it
      «not needed (fit budget)».
    q: |
      If a flooded player-occupied open hangar (all ~196k cells active) exceeds the weak-peer budget even after the
      active-front kernel, which lock-safe fallback do we activate? (Measured, not assumed — the number comes from
      the Sc-kernel flooded capture.)
    options:
      - Segment-authored halls FIRST (author the hall as segment-rooms with full-wall doors — «второстепенное»,
        owner priority) [recommended first lever].
      - sub-partition / mid-2.5D far-only / GAP-4 tick_divisor / all-peers-all-bubbles / volume cap / multicore (Sc-par).
      - «Smaller fully-fine levels» = LAST resort, spends R3 variety + R5 size, only with signature.
    recommendation: |
      Do not pre-pick — the measured flooded number picks the cheapest sufficient lever. Segment-first honors
      «ангар второстепенное»; «smaller levels» is the last resort, never the silent default. All levers lock-safe;
      activation owner-signed.
    source: work/audit-gas-sim-plan-2026-07-02.md (item 4b, global-scale-2); SPEC §6 п.3 fallback ladder (S9).
  - id: d-simaudit-package-001
    status: answered «да» по всем 4 пунктам батча (owner, 2026-07-02) — additive package accepted WHOLE
      (richness ladder re-pin, layered mass-conserving overflow, blast wave gameplay-load-bearing, July
      demo-road shape 07-10..15). Full record: work/audit-gas-sim-plan-2026-07-02.md.
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
  - id: d-sparse-tick-kernel-001
    status: answered «да» (owner, 2026-07-02) — insert Sc-kernel BEFORE Sc-reactions (tick iterates the
      sparse store / active cells; the Sc-rep G5 P2 field-storage-guard finding folded into its done_when
      #9). Full record: work/review-gas-sim-visual-2026-07-02.md (findings 8/9); history/2026-07-02-s-work-038-sc-kernel-framed.md.
  - id: d-finer-grid-fork-001
    q: |
      The visual wave-plan's biggest SHAPE lever («finer sim grid near player») exists on NO engine
      slice; render-side levers buy sub-cell RICHNESS but not sub-cell SILHOUETTE. Accept render-side
      as the medium, or schedule an engine item?
    options:
      - Accept render-side richness as the medium; strike the «finer grid» line from the wave plan.
        (Audit honesty line 2026-07-02: this ALSO leaves the detail-bubble mechanism unbuilt — the SPEC §6
        п.3 «all-peers-all-bubbles» hangar fallback and the ведро-1 near-feel host must then be re-recorded
        as render-side or dropped WITH a signature, never silently.)
      - Schedule a costed READ-ONLY view-refinement item (off-checksum, detail-bubble seam, no Fact-2/ADR-0002 reopen) after Sc-damage.
        (Audit broadening 2026-07-02: this slice = view refinement PLUS the ведро-1 host, with its Fact-3
        ADR — radius + cell size, owner-signed — the bubble is cheap insurance twice over: feel host AND a
        named hangar fallback.)
    recommendation: |
      Decide BEFORE visual WAVE 2 raises expectations. (2) is the honest keep-the-jewel path; (1) is
      the honest scope cut. Never leave the «(g-9c41 roadmap)» wording implying it is scheduled.
    source: work/gas-visual-wave-plan-2026-06-29.md ⚠ note; work/review-gas-sim-visual-2026-07-02.md (finding 23);
      work/audit-gas-sim-plan-2026-07-02.md (local-depth-04).
  - id: d-demo-road-001
    status: answered «да» (owner, 2026-07-02) — July shape session, CALENDAR-dated 2026-07-10..15, with
      mandatory rows (session-resilience, network ladder / Sc-net candidate slice, host-migration TREE #11
      carrier); mid-raid rejoin stays CUT. Full record: work/audit-gas-sim-plan-2026-07-02.md §Package item 7;
      work/review-gas-sim-visual-2026-07-02.md (finding 3).
  - id: d-marketing-wake-001
    q: |
      Every 2026-08-31 Steam-page prerequisite sits on PARKED nodes with no wake date; a ready restart
      CALL exists (history/2026-06-29-s-marketing-restart-001.md) but is undated and unsurfaced.
      Wake g-2f8c by ~2026-07-20, or re-date 08-31 explicitly?
    options:
      - Wake by ~07-20 (first marketing-forge sessions - positioning + artifact card + capsule-pipeline decision; capsule = hard external lead time, contract by early August).
      - Re-date 08-31 explicitly now (accept Q1-Q2 2027 EA as the planning default; Oct fest = wishlist seeding).
    recommendation: Pick one consciously; silently missing 08-31 is the worst branch.
    source: work/review-gas-sim-visual-2026-07-02.md (findings 2/6); TREE g-5b07/g-2f8c; work/marketing/questions/q-foundation.md.
  - id: d-biglevels-tree9-001
    status: answered «да» option 3 revised (owner, 2026-07-02) — TREE #9 huge-levels AMBITION KEPT, no
      pre-emptive re-sign-down; S4 gets a dated trigger set (first over-ceiling designed level of ANY
      archetype / 08-31 Steam copy freeze if page markets scale / post-Sc-damage checkpoint backstop);
      squeeze only on measured impossibility, by signature. Full record: work/review-gas-sim-visual-2026-07-02.md
      (finding 11); work/audit-gas-sim-plan-2026-07-02.md (global-scale-1, words-vs-docs-001, verticality-far-reentry).

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
  - Road RE-SHAPED to sparse-dominant + Sc-rep slice + SPEC edit + c-021 re-scope (2026-06-30): history/2026-06-30-s-reshape-sparse-dominant-001.md; work/character-road-shape-2026-06-29.md (§SLICE Sc-rep); vet workflow wf_967a4625-2a4
  - Sc-rep CALL framed + hardened (2026-07-01): history/2026-07-01-s-work-035.md; work/c-exec-022-call.md
  - Review sim+visual, 24 verified findings (2026-07-02): work/review-gas-sim-visual-2026-07-02.md
  - Reconcile/repair after the review (2026-07-02): history/2026-07-02-s-repair-review-reconcile-001.md
  - Sim-plan audit + decision batch (2026-07-02): work/audit-gas-sim-plan-2026-07-02.md (wf_a299ecef-44e, 34 findings)
  - Sc-kernel FRAMED + G9 SPEC batch (2026-07-02): history/2026-07-02-s-work-038-sc-kernel-framed.md; work/c-exec-023-call.md; hardening wf_ff1612b9-ec5
  - Sc-reactions PREPPED — forks (a)–(f) closed, body rewritten (2026-07-02): history/2026-07-02-s-shape-prep-screactions-001.md; work/c-exec-021-call.md; check wf_8ab4a0cb-401

next:
  Sc-kernel FRAMED + HARDENED 2026-07-02 (s-work-038, owner «все подтверждаю») as work/c-exec-023-call.md: audit
  §Package item-4 additions (a–k) folded, a standard adversarial pass run (wf_ff1612b9-ec5: 11 raised → 2 P2 folded
  [wake round-trip RED; frozen-visual honesty], 9 refuted), the batched G9 SPEC touch (item 8, S1–S10) SIGNED in the
  same session, d-gas-richness-tiers-001 RE-PINNED (P1 fix), d-hangar-flood-fallback-001 armed-dormant, kill_by =
  2026-07-16.
  NEXT WORK = a FRESH GasCoopGame_dev executor session opens c-exec-023 with an owner-present PLAN (base = GasCoopGame
  main @5442be0; the c-exec-022 PLAN deviation must not repeat). The Sc-kernel RESULT fills the SPEC §6 п.2 ceiling
  number. Do NOT re-fire c-exec-022; do NOT re-run W1a.
  PARALLEL: the c-exec-021 (Sc-reactions) re-shape PREP is DONE 2026-07-02 (s-shape-prep-screactions-001): forks
  (a)–(f) closed owner-present, body FULLY REWRITTEN (banners retired), Sc-typing homed after Sc-reactions. After
  Sc-kernel GREEN: run the CALL's §Re-sync sweep + the FULL fire-time re-hardening, fill §PENDING from the
  Sc-kernel RESULT, then fire c-exec-021 in a fresh GasCoopGame_dev session (owner-present PLAN). It does NOT
  fire before that.
  CALENDAR: July demo-road shape session 2026-07-10..15 (d-demo-road-001 «да», mandatory rows in its decision).
  VISUAL: ON HOLD by owner 2026-07-02 («сначала разобраться с симуляцией») — W1b and c-visual-004 wait. HONESTY:
  while visual is held the ONLY live player-facing terminus = Sc-reactions telegraph+bang; the 07-24 milestone is
  re-affirmed against THAT (frozen visual not cited as counterweight; audit words-vs-docs-006).
  Still pending owner: d-finer-grid-fork-001 (anchor: before visual WAVE 2 — dormant while visual on hold),
  d-marketing-wake-001, d-coop-interdependence-repin-001.

END_OF_FILE: live/indie-game-development/NOW.md
