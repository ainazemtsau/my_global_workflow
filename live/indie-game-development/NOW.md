# NOW — indie-game-development
updated: 2026-07-02 by s-repair-review-reconcile-001

bet:
  node: g-9c41
  status: active
  goal: |
    Networked co-op gas core, currently on the CHARACTER ROAD: Sc-types →
    Sc-weight → Sc-rep → Sc-reactions → Sc-damage. The far-tier S3/S4/S5 scale plumbing is
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
    (3) roster size = config, ~128 a suggested start, tunable without SPEC re-sign. 2026-07-01
    (s-work-035): the Sc-rep executor CALL c-exec-022 is FRAMED + adversarially HARDENED as
    work/c-exec-022-call.md, with §Re-sync v8→v9 first, named approach token, full Sc-rep gate
    battery, v9 escape-class registry walk, and STOP discipline against dense fallback / hashmap /
    silent overflow / dev2 edits. Sc-rep stays active awaiting the GasCoopGame_dev executor return.
    2026-07-02 REVIEW + RECONCILE (s-repair-review-reconcile-001; durable review record =
    work/review-gas-sim-visual-2026-07-02.md, 24/24 findings verified, 0 refuted): Sc-rep was EXECUTED 2026-07-01 in
    GasCoopGame_dev WITHOUT the owner-present PLAN this CALL mandates (deviation, recorded) and sat UNCOMMITTED; the
    owner checkpointed it = dev @adc3b9d. A REAL hangar measurement was then taken (dev @8db3ee1,
    docs/measurements/sc-rep-hangar-real-measurement-2026-07-02.md): tick cost scales ~linearly with REGISTERED roster
    (~9 ms/type at the 196k-cell hangar; roster-64 = 587 ms/tick avg; roster-128 extrapolates ≈1.16 s vs the 50–100 ms
    tick budget; active cells CONSTANT at 1,562) — the tick kernel still expands sparse→dense per-species planes every
    tick, so Sc-rep's honest scope = REPRESENTATION + CHECKSUM SCHEMA (the sparse-awake perf rationale is NOT delivered
    by it). De-risk-wall verdict (kill_by 07-05): the wall FIRED correctly → recommendation = insert slice Sc-kernel
    (active-front tick iteration) BEFORE Sc-reactions (d-sparse-tick-kernel-001, PENDING owner «да»; draft CALL =
    work/c-exec-023-draft-call.md). Sc-rep remaining: binding fresh-session G5 (scope-relabelled) → owner-eye →
    owner-gated dev→main merge. VISUAL: c-visual-003 W1a already EXECUTED on dev2 (7 commits + owner checkpoint
    @d25b0b2; owner-eye checklist pending; RESULT not yet home); W1b re-scoped (after the Sc-rep merge + a small
    owner-acked stamp read-API — see the CALL banner). The Codex review-fix loop was STOPPED by the owner 2026-07-02
    (fixes return via the normal contour after G5).
  appetite: |
    Wave/core appetite remains governed by the g-9c41 de-risk wall; do not extend
    a bet silently. If the current slice overruns or reveals a core blind spot,
    stop and re-shape/review instead of stretching the appetite.
  kill_by: |
    De-risk-wall checkpoint 2026-07-05: ANSWERED 2026-07-02 by the real hangar measurement (linear roster scaling) —
    outcome = re-shape recommendation d-sparse-tick-kernel-001, awaiting the owner's sign; do not let the checkpoint
    pass silently green. 2026-07-24 remains the visible-gas milestone (telegraph+bang and/or two-type visual on the
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
  - id: Sc-rep
    status: built-pending-gates
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

next_slices:
  - Sc-kernel (PENDING owner «да», d-sparse-tick-kernel-001) BEFORE Sc-reactions: re-point the tick kernel at the
    sparse store / active cells (kill the per-species dense expand+rebuild; cost becomes ∝ active cells, not
    roster × domain cells). done_when re-runs the 2026-07-02 measurement matrix before/after + an adversarial
    «hangar flooded» all-cells-active scenario + a Unity-runtime capture; also closes the Coarse/ scan-root hole.
    Draft CALL: work/c-exec-023-draft-call.md (standard hardening at framing).
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
      W1a EXECUTED on dev2 2026-06-30 (7 commits 509c502..b7dab15 + owner checkpoint @d25b0b2) —
      owner-eye checklist pending, RESULT not yet routed home. Do NOT re-run W1a. W1b RE-SCOPED
      2026-07-02 (see the ⚠ banner in work/c-visual-003-call.md): runs AFTER the Sc-rep dev→main
      merge; needs a small owner-acked engine read-API for the per-cell dominant STAMP (G channel);
      no consumer-side argmax/dense workaround.
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
      Sc-rep). dev->main merge + push owner-gated.
      2026-07-02 banner corrections added (items 11-14): ADR = next-free ADR-E-* per ADR-P-0001
      (flat «≈0022» will never exist); base shifts post-Sc-kernel if d-sparse-tick-kernel-001
      approved; NEW named shape fork = co-residency/overflow under mixing (>4 co-resident types =
      deterministic all-peer LOUD-THROW halt today) + adversarial 5-type junction RED; body
      drift-sweep or full rewrite required at its shape.
  - id: c-exec-022
    to: executor
    for: g-9c41 / Sc-rep
    issued: 2026-07-01
    call: work/c-exec-022-call.md
    note: |
      EXECUTED 2026-07-01 (deviation: no owner-present PLAN; work checkpointed by the owner
      2026-07-02 = dev @adc3b9d; real hangar measurement = dev @8db3ee1). Do NOT re-fire.
      Remaining: binding fresh-session G5 → owner-eye → owner-gated dev→main merge. Honest scope
      = representation + checksum schema only (see the ⚠ STATUS banner in work/c-exec-022-call.md).

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
  - id: d-sparse-tick-kernel-001
    q: |
      The 2026-07-02 real hangar measurement: tick cost ∝ registered roster × domain cells (587 ms/tick
      at roster-64; roster-128 extrapolates ≈1.16 s vs the 50–100 ms budget; weak peer 2–4× worse —
      breaks the lockstep weakest-peer premise even at small rosters in a hangar). Insert slice
      Sc-kernel (tick iterates the sparse store / active cells) BEFORE Sc-reactions?
    options:
      - Insert Sc-kernel before Sc-reactions (draft CALL ready - work/c-exec-023-draft-call.md).
      - Build reactions first on the dense kernel, kernel after (rework - reactions ride the tick loop).
      - Cap the roster small (4-8) and defer (still 90-180 ms weak-peer hangar; silently drops the signed many-types/big-halls canon).
    recommendation: |
      Insert BEFORE reactions. The June c-exec-014 readout already named this «the #1 optimization to
      bank before big halls»; the store Sc-rep laid is exactly the substrate it needs; reactions built
      on the dense kernel would be built twice.
    source: |
      work/review-gas-sim-visual-2026-07-02.md (findings 8/9); GasCoopGame_dev
      docs/measurements/sc-rep-hangar-real-measurement-2026-07-02.md (dev @8db3ee1).
  - id: d-finer-grid-fork-001
    q: |
      The visual wave-plan's biggest SHAPE lever («finer sim grid near player») exists on NO engine
      slice; render-side levers buy sub-cell RICHNESS but not sub-cell SILHOUETTE. Accept render-side
      as the medium, or schedule an engine item?
    options:
      - Accept render-side richness as the medium; strike the «finer grid» line from the wave plan.
      - Schedule a costed READ-ONLY view-refinement item (off-checksum, detail-bubble seam, no Fact-2/ADR-0002 reopen) after Sc-damage.
    recommendation: |
      Decide BEFORE visual WAVE 2 raises expectations. (2) is the honest keep-the-jewel path; (1) is
      the honest scope cut. Never leave the «(g-9c41 roadmap)» wording implying it is scheduled.
    source: work/gas-visual-wave-plan-2026-06-29.md ⚠ note; work/review-gas-sim-visual-2026-07-02.md (finding 23).
  - id: d-demo-road-001
    q: |
      Oct-5 co-op demo (g-5b07): nothing between Sc-damage and a submittable demo is sketched anywhere
      (real-network gas parked at ~S4; no player-gas loop / level / objectives / packaging slice).
      Force a road-to-demo shape session in July?
    options:
      - July shape session - enumerate the slices Sc-damage → demo against Sep-21/Oct-5; if it does not fit, consciously re-date Oct-5 or cut engine depth.
      - Keep building the engine road and decide in September (the review's named failure mode).
    recommendation: July shape session — a conscious choice beats a September discovery.
    source: work/review-gas-sim-visual-2026-07-02.md (finding 3).
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
    q: |
      TREE g-9c41 done_when #9 (huge levels ~200×200×40m, ≥1000 volumes) has no surviving path: only
      the S4 far-tier rollup can carry it (fully-fine is ~64× over the weak-core ceiling), the S4
      deferral is undated, and the road's hangar fallback («smaller fully-fine levels») would silently
      drop the signed promise.
    options:
      - Give S4 a dated re-entry condition (e.g. before the Steam-page copy freezes - do not market scale that has no machinery).
      - Explicitly re-sign TREE #9 down to the fully-fine ceiling the measured hangar number supports.
    recommendation: |
      Decide at the next road checkpoint; never let «smaller levels» become the answer without a
      signature — that is exactly a silent drop of frozen canon.
    source: work/review-gas-sim-visual-2026-07-02.md (finding 11).

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

next:
  (1) Owner signs the pending NOW.decisions — minimum d-sparse-tick-kernel-001 («да/нет»). (2) Fresh
  GasCoopGame_dev session runs the binding G5 refutation of Sc-rep (scope-relabelled; paste block in the
  2026-07-02 review chat + history/2026-07-02-s-repair-review-reconcile-001.md §G5) → owner-eye →
  owner-gated dev→main merge + push. (3) If d-sparse-tick-kernel-001 = «да»: frame Sc-kernel from
  work/c-exec-023-draft-call.md (standard hardening at framing) and run it in a fresh GasCoopGame_dev
  session. (4) Then re-harden + fire the held c-exec-021 (Sc-reactions) at its shape (banner items 11-14
  first). VISUAL: after the Sc-rep merge — owner-eye sign W1a on dev2, then W1b per the re-scoped
  c-visual-003. Do NOT re-fire c-exec-022; do NOT re-run W1a.

END_OF_FILE: live/indie-game-development/NOW.md
