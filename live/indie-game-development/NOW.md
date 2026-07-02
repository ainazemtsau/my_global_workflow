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
    (active-front tick iteration) BEFORE Sc-reactions (d-sparse-tick-kernel-001 — SIGNED «да» by the owner
    2026-07-02; draft CALL = work/c-exec-023-draft-call.md). Sc-rep remaining after the 2026-07-02 binding fresh G5
    (COULD-NOT-REFUTE; one P2 test-gap — field-level storage guard — folded into Sc-kernel done_when): owner-eye →
    owner-gated dev→main merge. VISUAL: c-visual-003 W1a CLOSED 2026-07-02 — owner-eye SIGNED WITH RESERVATIONS
    (dev2 @40b94cc): foundation accepted, clean LP1–LP5 moves to a DESIGNED gas-demo-scene leg (next visual leg,
    → c-visual-004); W1b re-scoped (after the Sc-rep merge + a small owner-acked stamp read-API — see the CALL
    banner). The Codex review-fix loop was STOPPED by the owner 2026-07-02 (fixes return via the normal contour
    after G5).
    2026-07-02 MERGED + PUSHED (s-work-037): Sc-rep + W1a merged to GasCoopGame main (origin/main @5442be0;
    merges efaa6eb + b5675ea; conflicts resolved: RESULT.md = latest-merged-leg, Packages/config = dev superset;
    one pre-pushed origin commit 2d85442 folded — content already contained). Full gate battery GREEN on merged
    main FIRST-HAND: 1227/1227 headless + hygiene + zero-float/int-overflow/type-hardcode scans. (A 20-error
    adapter-build scare = FALSE alarm: the root csproj files are Unity-generated, gitignored, and stale in the
    main worktree — they regenerate on the next Editor open.) Owner's local package-manager edits parked in a
    git stash on main. OWNER DIRECTIVE 2026-07-02: VISUAL track ON HOLD — «сначала разобраться с симуляцией»;
    c-visual-004 NOT framed. Road position: Sc-rep CLOSED → next active work = frame Sc-kernel (c-exec-023).
    2026-07-02 (later) SIM-PLAN AUDIT (s-research-gas-sim-plan-audit-001, owner-requested, his requirement
    ladder given in-chat and binding over docs): 46-agent workflow wf_a299ecef-44e — 35 findings raised →
    34 verified (1 refuted), ONE P1 (the TIER-1/2/3 richness escalation ladder — the plan's own answer to R1
    «очень правдоподобно у игрока» — dropped from live state at the 06-29 NOW compaction; plan silently
    plateaus at TIER-1 ~2:1 jets); 3 architect packages judged → richness-first ADOPTED-pending-owner.
    Durable record = work/audit-gas-sim-plan-2026-07-02.md. Core verdict: architecture + both locks + the
    signed road are CORRECT for the owner ladder (lockstep verdict rationale recorded; HELD clouds draft
    stays held) — all fixes are ADDITIVE re-pins / gate extensions / dated-owned triggers, zero new build
    slices before reactions. Decision batch d-simaudit-package-001 queued (+ d-biglevels-tree9-001 and
    d-finer-grid-fork-001 texts broadened per the audit); the c-exec-023 framing MUST consume the audit's
    §Package item 4 additions. 2026-07-02 (latest): the audit batch is DECIDED — owner «да» по всем 4
    пунктам (package whole w/ 001b corrections; layered mass-conserving overflow; blast wave =
    gameplay-load-bearing «как и остальные реакции»; July demo-road shape 07-10..15). d-biglevels-tree9-001
    DECIDED (option 3 revised: huge-levels ambition KEPT, S4 dated triggers, squeeze only on measured
    impossibility). Pre-decisions for the Sc-reactions shape recorded in the c-exec-021 note (items 15-17).
    2026-07-02 (s-work-038): Sc-kernel FRAMED + HARDENED as work/c-exec-023-call.md — audit §Package item-4
    additions (a–k) folded + a standard adversarial pass (wf_ff1612b9-ec5: 11→2 P2 folded [wake round-trip RED;
    frozen-visual honesty], 9 refuted) + the batched G9 SPEC touch (item 8, S1–S10) SIGNED «все подтверждаю» in the
    same session; d-gas-richness-tiers-001 RE-PINNED (P1), d-hangar-flood-fallback-001 armed-dormant, kill_by
    2026-07-16. Road unchanged: next work = a fresh GasCoopGame_dev executor session opens c-exec-023 (owner-present
    PLAN, base main @5442be0); the RESULT fills the SPEC §6 п.2 ceiling number.
    2026-07-02 (s-shape-prep-screactions-001, owner present): the Sc-reactions PREP ran PARALLEL to the Sc-kernel
    executor leg (per NOW.next license): shape forks (a)–(f) CLOSED with the owner in-session, and the c-exec-021
    body was FULLY REWRITTEN at work/c-exec-021-call.md onto the current base (sparse-dominant, post-Sc-kernel) —
    both banner generations retired into it, prior hardening kept as principle, rewrite adversarially checked vs
    STATE (wf_8ab4a0cb-401: 36 raised → 10 machine-verified + 26 first-hand-adjudicated → ~22 distinct defects
    folded, 0 construction-breaking). Key owner reframe: any-N ZONE mixing = the requirement, per-cell K = internal
    config constant (the «5-газов не бывает» framing retired); old ReactionLayer demo tier = DELETE via
    owner-pre-signed live-spec amendment (scoped: demo files + their SHALL lines only; bus/enum stays locked).
    Sc-typing homed as the NAMED slice after Sc-reactions (accumulate-with-hysteresis). c-exec-021 = prepped,
    awaits Sc-kernel GREEN to re-harden+fire. G1 untouched: Sc-kernel stays the active task.
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
    status: answered — RE-PINNED into live state 2026-07-02 (s-work-038; audit P1 local-depth-01). Dropped at the
      2026-06-29 NOW compaction; restored from work/now-snapshot-2026-06-29.md with the lock-name correction folded
      (audit multiplayer-06). EXTENDS the locked model, does NOT crack it.
    q: |
      3-tier gas-richness ladder for R1 believability (owner «ок» to TIER-1 now, 2026-06-26; deep-research
      wf gas-richness-2026-06-26, adversarially verified). How far does near-player richness escalate, and on
      what signed evidence?
    note: |
      TIER-1 (SHIPPED, S1, no lock-crack): integer IMPULSE-EVENTS write a decaying directional-bias register on the
      S0 gradient face-flow — wind/directionality, decaying gust, transient fork-split, designed permanent VALVE.
      Honest limit: NOT true coasting inertia; open-space contrast ~2:1 (a lean, not a sharp jet).
      TIER-2 (RESERVED, ADR-class): seeded-integer LATTICE-GAS (FHP/ILG) in a few ведро-3 rooms → true emergent
      VORTICES as shared truth without float. Precondition «после sparse-солвера» = MET at Sc-kernel GREEN (armed,
      not pulled). Elsewhere vortices = the read-only cosmetic g-7e15 layer fed the authoritative bias.
      TIER-3 (RESERVED, owner-gated): fixed-point (Q-format) VELOCITY = true stored inertia + graceful permanent
      split as shared truth. ⚠ LOCK-NAME CORRECTION (audit multiplayer-06): TIER-3 reopens the no-stored-velocity
      REPRESENTATION boundary (S1 / ADR-0012-s1), NOT the netcode lock ADR-0002 — integer fixed-point velocity is
      lockstep-compatible (Photon Quantum/StarCraft). (Old «ADR-0010 lock-crack» wording = the same citation error
      §1 corrected.) Libraries if TIER-3: FixPointCS/FixedMathSharp (arithmetic only; no off-the-shelf fixed-point
      fluid solver exists — bespoke).
      RE-TRIGGER (concrete, ARMED, NO silent entry): owner-eye axes on the road — «бах читается как БАХ вблизи,
      вкл. одну детонацию в открытом поле без стен» (Sc-reactions bang-read) + «одна честная струя в открытом поле
      без стен» (Sc-damage open-space jet). A failed read = the SIGNED evidence to pull the next TIER (paid: new
      checksum members + weak-peer re-measure). Until then TIER-1 (2:1) stands. SPEC home = §6 п.9 + §3 «Разделение локов».
    source: work/now-snapshot-2026-06-29.md (original d-gas-richness-tiers-001); work/gas-richness-deep-research-2026-06-26.md;
      work/audit-gas-sim-plan-2026-07-02.md (local-depth-01, multiplayer-06).
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
    q: |
      2026-07-02 owner-requested audit of the PLANNED gas simulation vs his verbatim requirement ladder
      (workflow wf_a299ecef-44e, 46 agents; 34 verified findings incl. 1 P1; durable record =
      work/audit-gas-sim-plan-2026-07-02.md). Verdict: architecture/locks/road correct, no course change —
      but the richness escalation ladder (TIER-1 shipped / TIER-2 lattice-gas rooms / TIER-3 fixed-point
      velocity) lives only in history files, and ~10 promises float undated/unowned (typing slice, S4
      re-entry, host-resilience TREE #11, gas-on-real-bus, player-kinematics шов 7, ×4-8 multicore, wake
      triggers, >4-type overflow R1-lens, checksum-at-scale, Z-stacked vertical tests, floor breach).
      Accept the adopted additive package?
      (2026-07-02 OWNER CORRECTIONS folded before decision: (1) mines are NOT the primary archetype —
      levels must be STRONGLY DIVERSE; the audit's mine/shaft probe stays as the VERTICAL-archetype
      measurement scenario but no trigger/wording privileges mines — triggers key to ANY designed level
      over the ceiling; (2) huge levels = KEEP the ambition, compromise only if measurement proves it
      impossible («думаю с оптимизациями это можно сделать») — see revised d-biglevels-tree9-001 option 3;
      (3) mid-raid rejoin cut CONFIRMED by owner — R6 means «у всех всё синхронизировано и отлично
      работает», not rejoin features; the Факт-5 cut stands, halt/stall UX rows remain.)
    options:
      - Accept whole (recommended) — richness ladder re-pinned (bang-read owner-eye axis on Sc-reactions;
        open-space jet look on Sc-damage = the signed TIER-2/3 escalation evidence channel); ONE batched G9
        SPEC touch (~10 one-line additive edits incl. ADR-0002-vs-no-stored-velocity lock-name separation,
        level-design ceiling contract, S3-on-S4 rule, floor-breach naming, hangar fallbacks reordered
        segment-first); c-exec-023 framing additions (full-path checksum timing, wake-trigger registry seam,
        mine/shaft probe, Z-stacked-rooms REDs, roster-128, all-cores row, weak-CPU proxy, flooded→auto-open
        d-hangar-flood-fallback-001, JEWEL GUARD = Sc-kernel is the LAST pre-reactions engine-only insertion,
        07-24 milestone re-affirmed there); c-exec-021 shape pins (layered mass-conserving >4-type overflow
        as primary branch, reactant-set override rows, wave×wind exactly-once oracle, bang-read axis,
        Sc-typing slice homing); Sc-damage rows (player-kinematics decision first, temp=SINK-only guard,
        crouch head-Z dose acceptance, armed jet look); July demo-road shape CALENDAR-dated 2026-07-10..15
        with session-resilience + network-ladder + host-resilience mandatory rows; Sc-net candidate slice
        after Sc-damage (backstop: scheduled before 08-31 if the page says co-op).
      - Accept selectively (name dropped lines) — each dropped line stays a known silent-drop channel.
      - Reject — plan stands as-is; the P1 means near-player richness silently plateaus at TIER-1.
    recommendation: |
      Accept whole. Zero new build slices before the jewel, no lock touched, no gate weakened — the package
      only converts memory into state and undated deferrals into owned, dated triggers.
    source: work/audit-gas-sim-plan-2026-07-02.md (findings + package + judges 9/8.5/7 ×2).
    decision: |
      «да» по всем 4 пунктам батча (owner, 2026-07-02, in-chat): (1) пакет ЦЕЛИКОМ, с учётом owner-заметок
      001b (diversity not mines; huge-levels ambition kept; rejoin cut confirmed); (2) >4-type overflow =
      LAYERED MASS-CONSERVING primary branch (chemistry-first → admission-clamp saturation → config-K) —
      pre-decision for the c-exec-021 shape; (3) blast wave = GAMEPLAY-load-bearing — owner: «да это не
      косметика как и остальные реакции» — pre-decision for c-exec-021 fork 3; (4) July demo-road shape
      2026-07-10..15 with the mandatory rows (see d-demo-road-001.decision).
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
    decision: |
      «да» — insert Sc-kernel BEFORE Sc-reactions (owner, 2026-07-02, in-chat; the Sc-rep G5 P2
      field-storage-guard finding folded into its done_when #9).
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
    q: |
      Oct-5 co-op demo (g-5b07): nothing between Sc-damage and a submittable demo is sketched anywhere
      (real-network gas parked at ~S4; no player-gas loop / level / objectives / packaging slice).
      Force a road-to-demo shape session in July?
    options:
      - July shape session - enumerate the slices Sc-damage → demo against Sep-21/Oct-5; if it does not fit, consciously re-date Oct-5 or cut engine depth.
      - Keep building the engine road and decide in September (the review's named failure mode).
    recommendation: July shape session — a conscious choice beats a September discovery.
    source: work/review-gas-sim-visual-2026-07-02.md (finding 3).
    decision: |
      «да» (owner, 2026-07-02, in-chat via the audit batch): July shape session, CALENDAR-dated
      2026-07-10..15 (trigger = calendar, NOT an event), with MANDATORY rows per
      work/audit-gas-sim-plan-2026-07-02.md §Package item 7: session-resilience (halt/desync player UX —
      loud stop → readable error → lobby; raid-boundary checkpoint decision; desync-report artifact on the
      ADR-0017 MeaningMembers mask; peer-drop policy fork — anchor SimInstance.cs:38 no timeout/drop path;
      host-migration spike 1-2 days = TREE #11 carrier); network ladder (Sc-net candidate slice after
      Sc-damage — gas on the real FishNet bus, backstop: scheduled before 08-31 if the page says co-op;
      owner-run real-link feel eval; Steam-transport certification by Sep-21 OR signed direct-IP demo
      decision; TREE #3 re-pinned to a carrier); mid-raid rejoin stays CUT (owner-confirmed 2026-07-02).
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
      - (added by the 2026-07-02 sim-plan audit; REVISED same day by owner words, RECOMMENDED) Keep TREE #9
        huge levels as the signed AMBITION — owner: «я бы хотел иметь огромные уровни… но я думаю что с
        оптимизациями это можно сделать»; the optimization path = S4 rollup (+ reserved Sc-par multicore,
        bubble cap, segment-fallbacks). S4 gets the DATED trigger set — earliest of (i) the FIRST designed
        level of ANY archetype exceeding the measured ceiling (owner correction: levels must be STRONGLY
        DIVERSE; mines are ONE type among many, no archetype privileged); (ii) before the 2026-08-31 Steam
        copy freeze IF the page markets scale; (iii) the post-Sc-damage road checkpoint as backstop.
        NO pre-emptive re-sign-down: the R5 squeeze license activates ONLY on measured impossibility,
        by signature.
    recommendation: |
      Take option 3 as revised — it now carries the owner's own 2026-07-02 words (ambition kept, compromise
      only if measurement proves it impossible). NB: option 2 as worded silently also re-signs the SPEC's
      own ~150-room target. Never let «smaller levels» become the answer without a signature — that is
      exactly a silent drop of frozen canon.
    source: work/review-gas-sim-visual-2026-07-02.md (finding 11); work/audit-gas-sim-plan-2026-07-02.md
      (global-scale-1, words-vs-docs-001, verticality-far-reentry).
    decision: |
      «да» — option 3 REVISED (owner, 2026-07-02, in-chat via the audit batch «да с учётом моих заметок» +
      his own words «я бы хотел иметь огромные уровни… думаю с оптимизациями это можно сделать»): TREE #9
      ambition KEPT, no pre-emptive re-sign-down; S4 dated trigger set (first designed level of ANY
      archetype over the measured ceiling / before the 08-31 Steam copy freeze if the page markets scale /
      post-Sc-damage road checkpoint backstop; owner-of-the-watch = the road checkpoint session);
      squeeze only on measured impossibility, by signature.

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
