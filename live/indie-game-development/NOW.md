# NOW — indie-game-development
updated: 2026-07-06 by s-work-056

bet:
  node: g-9c41
  status: active
  goal: |
    Networked co-op gas core, currently on the CHARACTER ROAD: Sc-types →
    Sc-weight → Sc-rep → Sc-kernel → Sc-reactions → Sc-typing → Sc-damage. The far-tier
    S3/S4/S5 scale plumbing is parked until levels get big.
  current_truth: |
    Sc-types + Sc-weight + Sc-rep + Sc-kernel DELIVERED and MERGED to GasCoopGame main; the Sc-kernel ledger is
    FULLY CLOSED (c-exec-023 + cleanup c-exec-024, both binding-G5 SOUND — s-work-039 / s-work-041). W1b
    (c-exec-025, the Sc-kernel→Sc-reactions GAP's remaining engine item — a read-only, encapsulation-safe per-cell
    dominant-type read seam over the Sc-rep stamp) is now DELIVERED + MERGED + PUSHED (origin/main @e0e4f5a,
    contract v14) and passed its BINDING fresh-session G5 (s-work-042, 2026-07-04, wf_44257b08-dfe — 8 refutation
    lenses + adjudication + completeness critic). The 3 W1b-core lenses died on output-conformance, so this session
    re-derived them FIRST-HAND: byte-identity holds (no golden/tick file in the 38ab715→e0e4f5a diff, additive read
    methods only); encapsulation-safe (TypeId readonly-struct + record returned BY VALUE, private near store never
    escapes); full-domain sentinel (near store sized to dense.CellCount → no throw-instead-of-sentinel hole); 48
    W1b+atomicity tests GREEN headless. Verdict = SOUND, 0 P1, 0 P2. The Sc-kernel→Sc-reactions GAP is now CLEAR.
    Landed in the SAME product window and independently re-verified SOUND by this session's binding G5 (0 P1/P2):
    c-exec-026 (§Re-sync of the os/engineering contract v11→v14 — property-layer v12 PILOT + refuted-register v13 +
    fix-class-closure v14, ADR-P-0004, @a08860e; all three gates confirmed WIRED into check.ps1 -Deliver with self-
    tests that execute-and-fail-on-bad-fixture; the one real bug, a v14 $null-coerced no-op, was caught by the
    builder's own G5 and fixed pre-merge @e1bbf9d) and c-exec-027 ×2 — emergent PRE-EXISTING P1s the c-025 owner-
    review surfaced OUTSIDE the c-025 diff, fixed in child sessions and merged autonomously in the product repo:
    topology inclusive-max int-overflow guard (ADR-E-0004) and throw-atomicity stage-locals at 3 sites (ADR-E-0005),
    both technical fixes CONFIRMED correct. TWO P3-defer findings, neither a live defect: (a) a review-vs-DF-1 doc
    nit on dead-code GridRect; (b) the v14 fix-class-closure gate was satisfied for the throw-atomicity leg by
    ARCHIVING the change out of the gate's walk scope (owner-decided v11-work exemption) rather than by a recorded
    machine sweep — inert now (4th sibling MaterializeDue's throw is provably unreachable) but it voids the
    reopen-tripwire for a class with a live deferred sibling → captured for maintenance. Route-home backlog
    (direction owns the CALLs): DF-2 (tools/mutation.ps1 [Category("Benchmark")] poisons Stryker — P2 tooling, EVERY
    mutation leg hit it, ties d-benchmark-category-gate-001) most pressing; DF-1 (RectDecomposition span-DoS — P1 by
    severity but ZERO production caller, wakes when GridFlow room-ingestion wires; approach C pre-selected) and
    task_441a3b58 (4th throw-atomicity site, unreachable/defense-in-depth) latent. next: d-nextcall-tooling-vs-c021-001
    ANSWERED (owner option 1) → c-exec-028 (tools/ benchmark-hardening) DELIVERED + MERGED + PUSHED (origin/main
    @cde4c3d, v14) + binding-G5 SOUND (s-work-045) — DF-2 root-fixed via [Explicit] (owner-ack), gate-integrity
    gates have teeth, bench-tax cleared; d-benchmark-category-gate-001 DISCHARGED. next = re-harden + §Re-sync
    (repo NOW v18, c-031 §Re-sync DONE) + fire c-exec-021 (Sc-reactions). VISUAL track: Stage 1 DONE
    (via c-visual-005, merged @26dd062, owner-tested OK 2026-07-06); NEXT = Stage 2 (openable — W1b landed + owner-check given).
    SPEC §6 п.2 fully-fine ceiling SEATED (~35k@50ms / ~70k@100ms weak-peer). Latest session:
    history/2026-07-04-s-work-045-c-exec-028-binding-g5-close.md.
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
    status: done
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
      DELIVERED (leg1 kill-test + leg2 measurements/closure) and MERGED to GasCoopGame main @b7d4226 (pushed,
      2026-07-03; owner «мержим», owner-eye live Play-mode of GasBuoyancyDemoScene). BINDING fresh-session G5
      (s-work-039, 2026-07-03, wf_91e57ec8-b24 — 10 lenses + independent adjudication; the builder's own G5 was a
      same-session Sonnet pre-pass) = runtime SOUND, 0 P1: byte-identity, roster-independence KILL gate (genuine,
      non-vacuous cell-by-cell Mass equality roster-1 vs 64), ZERO-LEGACY (grep-confirmed off the authoritative
      SparseStep path), contiguous-array field authority all HOLD. FOUND 2 P2 (scaling-benchmark generator
      git-ignored → numbers not committed-reproducible; AssertContiguousArrayAuthority non-recursive → misses future
      nested/base-class-private authority) + 5 P3 (FULL-path SPEC wording vs Step-only; stale store_memory note;
      buoyancy framed as registry entry vs inlined _buoyStamp; stale InternalsVisibleTo comment; single-commit
      RED→GREEN) — none a kill condition, all routed into c-exec-024 (a fix is a new leg; the slice is on main).
      SPEC §6 п.2 ceiling seated ~35k@50ms/~70k@100ms; d-hangar-flood-fallback-001 answered; Unity absolute-ms
      capture stays deferred (owner-ack, measure-only). Record: history/2026-07-03-s-work-039-sckernel-binding-g5-close.md.
      CLEANUP c-exec-024 DONE + MERGED (owner-pushed @7a54320) 2026-07-03: binding fresh-session G5 SOUND, 0 P1, all
      5 done_when CONFIRMED empirically (s-work-041, wf_fd7a1418-6cf) — 2 P2 fixed + 5 P3 swept, 5 residual low P3
      routed (none a blocker; d-benchmark-category-gate-001 holds the gate-loophole + benchmark-freshness). Sc-kernel
      ledger FULLY CLOSED. Record: history/2026-07-03-s-work-041-c-exec-024-binding-g5-close.md.
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
  - Sc-kernel ledger FULLY CLOSED; W1b (c-exec-025) DELIVERED + MERGED + PUSHED (origin/main @e0e4f5a, contract
    v14), binding-G5 SOUND (s-work-042, wf_44257b08-dfe — 0 P1/P2, 2 P3-defer). The Sc-kernel→Sc-reactions GAP is
    now CLEAR. d-nextcall-tooling-vs-c021-001 ANSWERED (owner: option 1): c-exec-028 (tools/ benchmark-hardening,
    DF-2 + d-benchmark-category-gate-001) DELIVERED + binding-G5 SOUND (s-work-045, @cde4c3d), bench-tax cleared;
    NEXT = c-exec-021 (Sc-reactions) — after its §Re-sync (repo at v14; OS now v17 — owes v15 review-scope-split /
    v16 tool-unavailable-STOP / v17 source-scan-ban, which must classify c-028's own scanner-gates as tooling-
    hygiene not behavior-evidence) + full fire-time re-hardening + fill §PENDING.
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
  # c-exec-031 (GasCoopGame §Re-sync v14→v18: review-scope-split + tool-unavailable-STOP + source-scan-ban +
  # cited-artifact-existence) CLOSED 2026-07-05: DELIVERED + MERGED @21f9c0f + PUSHED origin/main; synced_contract_version
  # = 18. Binding fresh-session G5 (s-work-052, 5-lens wf_1b1d5d16-85e + both selftests run first-hand). ROUND 1 caught a
  # real P1 (v15 anti-dodge site-parse false-green on file:line:col / #Lnn / range / (line N) / ./ forms — an in-scope
  # finding could be relabelled class-sibling to dodge in-leg fixing); FIXED REV-2 @3a5caba with a FAIL-CLOSED clean-grammar
  # site check + Case5a-e seeded-miss (all RED, run first-hand); re-G5 SOUND. v16/v17/v18/additive SOUND round 1. Process
  # signal: the in-session single-model Sonnet G5 MISSED the P1; the fresh cross-session Opus G5 caught it. DF-11 (2
  # pre-existing P3s in review-check.ps1) → LATENT. Record: history/2026-07-05-s-work-052-c-exec-031-c-visual-005-close.md.
  # c-exec-028 (tools/ benchmark-hardening: DF-2 + d-benchmark-category-gate-001) CLOSED 2026-07-04: DELIVERED +
  # MERGED + PUSHED (origin/main @cde4c3d, v14); binding fresh-session G5 SOUND, 0 P1/P2 (s-work-045, first-hand on
  # the SHIPPED [Explicit] state). DF-2 root-fixed via [Explicit] (owner-ack:c-exec-028-explicit-redesign-2026-07-04;
  # mutation.ps1 byte-identical, no stash); force-DISCOVER + exclusion-consistency + matrix-freshness gates have
  # teeth (self+real+matrix run first-hand); v17 cross-check = permit (tooling-hygiene, not behavior-evidence).
  # d-benchmark-category-gate-001 DISCHARGED. Record: history/2026-07-04-s-work-045-c-exec-028-binding-g5-close.md.
  - id: c-visual-003
    to: executor
    for: g-7e15 / visual wave 1
    issued: 2026-06-29
    call: work/c-visual-003-call.md
    note: |
      CLOSED 2026-07-02 (superseded by plan v2, s-visual-012). W1a CLOSED 2026-07-02: owner-eye SIGNED
      WITH RESERVATIONS in-chat (dev2 @40b94cc — checklist + F-OWNER + RESULT flipped to DELIVERED).
      Honest state: render FOUNDATION accepted (de-block + light-through + never-worse + one inspector);
      clean LP1–LP5 NOT claimed — LP1 candidate-pass (lamp-direction read weak), LP2/LP3 confirmed live,
      LP4/LP5 blocked by the missing DESIGNED demo level (owner-eye finding: «demo level needs design»;
      existing levels = boxy 6×4×6 box / horizontal tube). dev2→main MERGED 2026-07-02 (@b5675ea) and
      PUSHED. The designed-demo-scene leg became c-visual-004 = Stage 1 of plan v2 (OPENED 2026-07-03, see
      below). W1b (per-cell dominant-type read) RE-SCOPED OUT of the visual track entirely (panel finding: it
      is a Core/Field edit, cannot ride a render-only leg) — now a tiny ENGINE mini-CALL in the GasCoopGame_dev
      worktree, windowed per d-w1b-window-001 (Sc-kernel→Sc-reactions gap; still fires there, unaffected by
      the visual partial un-hold).
  # c-visual-004 (g-7e15 / Stage 1: стенд + отсечка по глубине) CLOSED 2026-07-06 (s-work-054): Stage 1 content was
  # DELIVERED via c-visual-005's salvage of the polluted @3858752 Stage-1 attempt — the depth composite (отсечка,
  # gas no longer draws through walls) + the designed room (GasRoomScene) + camera bookmarks + open-arena-jet replay
  # + fixed-seed restart plumbing all landed and MERGED @26dd062. Owner TESTED + confirmed OK 2026-07-06 («Stage 1
  # ок»). c-visual-004 + c-visual-005 collapsed into ONE delivery — no separate Stage-1 leg fires. (The 2026-07-06
  # FIRE-READY re-scope once written in this slot was WRONG — the "remainder" was already built; corrected here; the
  # CALL file work/c-visual-004-call.md carries a SUPERSEDED banner.) Next visual = Stage 2 (openable — see g-7e15
  # track_state). Record: history/2026-07-06-s-work-054-visual-stage1-close-stage2-open.md.
  # c-visual-005 (g-7e15 clean visual source-scan retirement) CLOSED 2026-07-05: DELIVERED (dev2) + MERGED @26dd062 +
  # PUSHED origin/main. Binding fresh-session G5 SOUND (s-work-052, first-hand): the 4 v17-banned behavior-source-scanners
  # DELETED; existence-only wiring smoke (File.Exists, no source-scan/globs/markers — the crutch retired); real visual
  # changes preserved (GasUber depth-occlusion, render-feature depth, camera/replay, GasRoomScene); owner-eye «работает»
  # (2026-07-05); 1331/1331 headless. Merge reconciled (dev2 was 2 behind, pre-RESULT-per-leg): root RESULT.md →
  # docs/results/c-visual-005.md; the c-031 grandfather (validation.config list+note + AGENTS.md v17 bullet) DISCHARGED
  # (the 4 files now deleted). Resolves d-visual-sourcescan-route-001. Record: history/2026-07-05-s-work-052-c-exec-031-c-visual-005-close.md.
  - id: c-visual-006
    to: executor
    for: g-7e15 / Stage 2 (Паспорт типа + шипучий режим)
    issued: 2026-07-06
    call: work/c-visual-006-stage2-call.md
    note: |
      FRAMED + FIRE-READY 2026-07-06 (s-work-055; owner «Stage 1 ок, давай Stage 2»). Stage 2 of gas-visual-plan-v2 —
      RENDER-ONLY: (a) owner-signed 8-channel per-type schema + the 96→128B layout-ADR, (b) consume the merged W1b
      dominant-STAMP read-API (engine side DONE — c-exec-025 @26dd062), (c) real half-res + bilateral upsample pulled
      forward. Visible payoff = a two-colour multi-type PREVIEW (labelled «colours only; character = Stage 4»). Base =
      GasCoopGame main @26dd062/v18; RESET dev_2 to origin/main @26dd062 FIRST; runs in a FRESH GasCoopGame_dev_2
      session (NEVER dev — engine cubes live there); dev_2→main merge owner-gated. Per-type CHARACTER/archetypes/
      danger-ladder = Stage 4 (OUT); natural-jet fix = Stage 3 (OUT); ZERO Core/** edit (STOP if it needs an engine
      change). 2026-07-06 owner sign-off clarified: «шипучий режим» is only the label for the two-colour real
      multi-type preview (NO extra bubbling/particle/boiling effect); the base passport is required for every gas
      (hue/value/saturation/edge-softness/motion-frequency/buoyancy-silhouette/interior-structure/glow-pattern/
      danger); reserve an extensible render-only attachment path for later per-gas modules/assets, but build none in
      Stage 2. Everything else in the proposed Stage 2 plan accepted. Opens with an owner-present PLAN (schema signed
      before build). PARALLEL to c-021 (engine).
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
      READY TO FIRE 2026-07-06 (s-work-053) — CALL fire-time anchors REFRESHED + §PENDING FILLED: base =
      GasCoopGame main @26dd062 (contract v18); weak-hardware budget fork RESOLVED by d-hangar-flood-fallback-001
      (reactions ride the ~35k–70k all-active ceiling, heavy levers parked); wake-source binds the «reaction
      front» stub (env-delta reserved for Sc-typing); contract v18 + next ADR-E ≥ 0006; v17 source-scan-ban
      interaction noted (hygiene scanners preserved → c-021 v17-compatible BY CONSTRUCTION, behaviour proof =
      the NEW-TYPE-IS-DATA RED, never a scan). The code-anchored remainder (golden identity, MeaningMembers
      next-free-bit, scan-root lists, EmitImpulse/cap signatures) STAYS the executor's fire-time first-hand
      §Re-sync CONFIRM — do NOT invent.
      ⚠ W1b (the visual track's per-cell dominant-type read-API, d-w1b-window-001) fires as its OWN tiny
      engine mini-CALL in the Sc-kernel→Sc-reactions gap (GasCoopGame_dev worktree, never dev_2) — c-exec-021
      rebases over it via its own §Re-sync sweep; it is not part of c-exec-021's own scope.
      Rewrite adversarially checked vs STATE (wf_8ab4a0cb-401: 36 raised → 10 machine-verified + 26
      first-hand-adjudicated → ~22 distinct defects folded, 0 construction-breaking; subagent quota cut the
      verify fleet mid-run — adjudication finished first-hand in-session, recorded). The code-grounded FULL
      re-hardening + §Re-sync sweep still run at fire time. Does NOT fire until Sc-kernel GREEN (owner-gated
      dev→main merge). dev→main merge + push owner-gated.
  # c-exec-030 (GasCoopGame parallel-leg merge-safety: RESULT-per-leg + DF-5) DELIVERED on dev @0c09882 2026-07-04:
  # binding fresh-session G5 SOUND-WITH-NOTES (s-work-050, 7-lens wf_ad462cc9-92d + both self-tests run first-hand).
  # Gate-integrity airtight: check.ps1 refactor byte-identical-downstream (no dropped check), RESULT-gate port
  # byte-exact, migration blob-identical, DF-5 root-set parity. DF-5 RESOLVED. ONE P1-class PROCESS note (not
  # functional): closing-docs-ahead-of-evidence class recurred (c-029+c-030) → d-review-citation-fixclass-001.
  # MERGED to GasCoopGame main @bbe86eb (--no-ff) + PUSHED origin/main 2026-07-04 (d-c030-merge-001 «да»). Record: history/2026-07-04-s-work-050-c-exec-030-binding-g5-close.md.
  # c-exec-022 (Sc-rep) CLOSED 2026-07-02: G5 COULD-NOT-REFUTE → owner-eye → merged @efaa6eb, pushed
  # (origin/main @5442be0). Record: history/2026-07-02-s-work-036-screp-g5-kernel-signed.md + s-work-037.
  # c-exec-023 (Sc-kernel) CLOSED 2026-07-03: binding fresh-session G5 SOUND (0 P1) / 2 P2 + 5 P3 → done, merged
  # main @b7d4226. Cleanup follow-up = c-exec-024. Record: history/2026-07-03-s-work-039-sckernel-binding-g5-close.md.
  # c-exec-024 (Sc-kernel cleanup) CLOSED 2026-07-03: binding fresh-session G5 SOUND (0 P1), all 5 done_when
  # CONFIRMED empirically → done, merged main (owner-pushed @7a54320). 5 residual low P3 → d-benchmark-category-gate-001.
  # Sc-kernel ledger FULLY CLOSED. Record: history/2026-07-03-s-work-041-c-exec-024-binding-g5-close.md.
  # c-exec-025 (W1b per-cell dominant-type read seam) CLOSED 2026-07-04: DELIVERED + MERGED + PUSHED (origin/main
  # @e0e4f5a, v14); binding fresh-session G5 SOUND, 0 P1/P2 (s-work-042, wf_44257b08-dfe). Sc-kernel→Sc-reactions
  # GAP CLEAR. Record: history/2026-07-04-s-work-042-c-exec-025-w1b-binding-g5-close.md.
  # c-exec-026 (§Re-sync os/engineering contract v11→v14: property-layer v12 PILOT + refuted-register v13 +
  # fix-class-closure v14, ADR-P-0004) CLOSED 2026-07-04: MERGED @a08860e; re-verified SOUND by the s-work-042 G5
  # (all 3 gates wired into -Deliver + self-tests execute-and-fail; v14 $null-no-op bug caught + fixed pre-merge
  # @e1bbf9d). CALL = work/c-exec-026-resync-v12-v13-v14-call.md (never entered open_calls — drift now absorbed).
  # c-exec-027 ×2 (emergent PRE-EXISTING P1s from the c-025 owner-review, fixed in child sessions, merged
  # autonomously) CLOSED 2026-07-04: topology inclusive-max overflow guard (ADR-E-0004) + throw-atomicity
  # stage-locals @3 sites (ADR-E-0005); both technical fixes CONFIRMED correct by the s-work-042 G5. 2 P3-defer:
  # GridRect doc nit; v14-gate-satisfied-by-archiving (capture). Records: docs/reviews/review-c-exec-027-*.

recurring: []

parallel_tracks:
  - id: g-7e15
    track: VISUAL / GASG
    track_state: active — STAGE 1 DONE 2026-07-06 (owner-tested OK): Stage 1 (стенд + отсечка по глубине) was
      delivered via c-visual-005 + merged @26dd062; c-visual-004 CLOSED (collapsed into c-visual-005). NEXT = STAGE 2
      (Паспорт типа + шипучий режим), now OPENABLE — both gates met: W1b landed (c-exec-025 merged) + the required
      fresh owner check GIVEN 2026-07-06 («Stage 1 ок, давай Stage 2»). Stage 2 FRAMED + FIRE-READY as c-visual-006
      (work/c-visual-006-stage2-call.md, s-work-055; clarified by owner in s-work-056: no extra bubbling effect,
      base passport required for every gas, extension path reserved only); runs PARALLEL to c-021 (engine) in
      GasCoopGame_dev_2. Engine-focus discipline still holds (do not silently expand past the framed Stage 2 scope
      without asking).
    note: |
      Secondary to g-9c41, no fixed hour quota. c-visual-002 S1 gas-lab delivered + merged
      (history/s-visual-009.md); W1a (real gas in a lit room) DELIVERED WITH RESERVATIONS 2026-07-02
      (history/2026-07-02-s-visual-011-w1a-owner-sign.md — LP2/LP3 confirmed live, LP1 candidate-pass,
      LP4/LP5 blocked by the missing designed demo level) and MERGED to main @b5675ea.
      2026-07-02 (s-visual-012): full re-plan replacing the 06-29 wave plan. Method: read-only inventory
      of the shipped render layer + docs (2 agents), a 5-lens external research sweep (approach forks vs
      shipped games / per-type readability language / look-dev practice), then a 4-lens adversarial panel
      (perf-feasibility / owner-visible-value / repo-contracts-OS / solo-scope) that broke the first draft
      and whose P1/P2 fixes are folded in. OFFICIAL PLAN v2 = work/gas-visual-plan-v2-2026-07-02.md
      (SUPERSEDES work/gas-visual-wave-plan-2026-06-29.md; full old→new mapping recorded in the doc,
      nothing silently dropped). Owner-confirmed 2026-07-02 (batch «подтверждаю»): plan accepted; hold
      stays until Sc-kernel GREEN (default un-hold trigger); d-finer-grid-fork-001 ANSWERED (see
      NOW.decisions); W1b window ANSWERED (see d-w1b-window-001).
      2026-07-03 (s-work-040, owner-authorized): Sc-kernel GREEN (the default un-hold trigger) is now met
      (merged main @b7d4226). Owner explicitly authorized a PARTIAL un-hold — Stage 1 ONLY (it is render-only,
      zero Core/** edit, no dependency on W1b/reactions) — while Stage 2+ stays held (Stage 2 needs W1b, which
      fires in the same Sc-kernel→Sc-reactions gap as the c-exec-024 cleanup; opening Stage 2+ needs a fresh
      owner check, not an automatic cascade). c-visual-004 (Stage 1: стенд + отсечка по глубине) OPENED —
      work/c-visual-004-call.md refreshed to the current main tip (post Sc-kernel + contract-v11 resync,
      @bc25a33) + a dev_2-behind-main flag (dev_2 is still at the old W1a tip 40b94cc; the PLAN's §Re-sync
      step must pull main into dev_2 first). Runs in a FRESH GasCoopGame_dev_2 session (never dev — engine
      debug cubes live there, this is the real gas visual).
      SIX STAGES: 1 Стенд+отсечка (designed room + open-space bookmark + depth composite + fixed-seed
      repeatable motion — CALL OPENED 2026-07-03, work/c-visual-004-call.md)
      → 2 Паспорт типа + шипучий режим (8-channel per-type schema + layout-ADR 96→128B + W1b consumption
      + real half-res pulled forward) → 3 Одна жемчужина (natural-jet fix + cheap lighting levers + LP1
      re-test + honest ceiling-exit to d-finer-grid-fork-001) → 4 Три характера + шкала опасности (3 canon
      archetypes, 3-channel minimum-separation rule, blind lineup test, danger ladder clamped <3Hz) →
      5 Затопленная комната (perf pass framed as a live multi-type flood spectacle, feeds marketing
      capture) → 6 Газ в мире (post-Steam-page, ONE owner-picked item, default = teammate readability).
      Old "S2 two-type+scatter in the empty lab" and the 06-29 wave-plan sequencing are SUPERSEDED.
      Reading set incl. docs/gas-visual-stage-plan.md §S1/§S6+ and the canon visual-style minimal note
      (history/s-canon-visual-style-minimal-gas-stage-001.md).
      2026-07-04 (s-work-044): an off-book leg "Close visual source-scan retirement" returned on dev_2 (@3858752)
      and FAILED its binding G5 (NOT met; wf_b8e01996-620) — salvageable core, but massive undeclared scope
      (FishNet/shader-occlusion/gate-tooling) + a narrowed source-scan still living in the "wiring smoke" + a
      self-relaxed DELIVERED gate arm, on a 46-behind-v11 base. NOT merged. Route decision to owner =
      d-visual-sourcescan-route-001 (rec: re-derive clean on main v14). dev_2 base is now polluted — see the
      c-visual-004 ⚠ note.
      2026-07-04 (s-work-046): RESOLVED — owner picked option 1 (visual + shader-occlusion WANTED, kept declared);
      net DELEGATED to me → NOT now / PRESERVED (tag ref/visual-sourcescan-leg-3858752) for the future Sc-net slice.
      Opened c-visual-005 (clean re-derive on main v14; wiring smoke made existence-only; net/gate-tooling/TypeId
      dropped; step 0 tags @3858752 + resets dev_2). Fire c-visual-005 BEFORE c-visual-004 Stage 1.
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
    status: answered «да» (owner, 2026-07-03, s-work-039) — the Sc-kernel flooded-hangar capture (196k all-active
      = 70.788 ms/tick → weak-peer ×4 = 283 ms) IS over the 50–100 ms budget, so it auto-opened. RESOLUTION =
      accept the DESIGN + ADMISSION ceiling (levers 1 + 6): keep simultaneously-active near-volume within the
      seated SPEC §6 п.2 ceiling (~35k–70k all-active) by level design + an admission cap; heavy levers
      (sub-partition / mid-2.5D far-only / GAP-4 tick_divisor / all-peers-all-bubbles / volume cap / multicore)
      NOT built now (far-tier scale is parked until levels get big; whole-map-active is pathological). Revisit —
      with signature — when a real designed level approaches the ceiling. All levers stay lock-safe; activation owner-signed.
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
    status: answered — option 2 (owner, 2026-07-02, plan-v2 session s-visual-012): schedule a costed
      READ-ONLY view-refinement engine item (off-checksum, detail-bubble seam, no Fact-2/ADR-0002 reopen)
      after Sc-damage — the keep-the-jewel path. Decided ahead of gas-visual-plan-v2 Stage 3 (hero polish)
      so the "jewel bar" carries an honest, pre-agreed ceiling-exit rather than an open expectation. This
      slice = view refinement PLUS the ведро-1 near-feel host (Fact-3 ADR: radius + cell size, owner-signed
      at that item's shape) — a double-duty lever (feel host AND the named hangar fallback).
    source: work/gas-visual-wave-plan-2026-06-29.md ⚠ note; work/review-gas-sim-visual-2026-07-02.md (finding 23);
      work/audit-gas-sim-plan-2026-07-02.md (local-depth-04); work/gas-visual-plan-v2-2026-07-02.md.
  - id: d-w1b-window-001
    status: answered (owner, 2026-07-02, plan-v2 session s-visual-012, batch «подтверждаю» option 4a): the
      visual track's per-cell dominant-type read-API (W1b) fires as its OWN tiny ENGINE mini-CALL in the
      GasCoopGame_dev worktree (never dev_2), in the gap after Sc-kernel merges to main and BEFORE
      c-exec-021 (Sc-reactions) fires; c-exec-021 rebases over it via its own §Re-sync sweep. Keeps the
      visual track's render-only boundary intact — a Core/Field edit cannot ride inside a render-only leg
      (it was previously mis-scoped as part of c-visual-003).
    source: work/gas-visual-plan-v2-2026-07-02.md; NOW open_calls c-exec-021 §PENDING.
  - id: d-benchmark-category-gate-001
    status: DISCHARGED 2026-07-04 by c-exec-028 (binding fresh-session G5 SOUND, s-work-045). Both halves landed on
      origin/main @cde4c3d: the Benchmark force-DISCOVER counterpart (category-AWARE source-scan, non-executing,
      requires [Explicit]) + the general exclusion-consistency gate (every check.ps1 inner-loop TestCategory!=X needs
      a counterpart, decoy-immune) + the scaling-matrix freshness asserts (x2/x4/peak/over_budget/naive) with RED
      controls — all wired into check.ps1 -Deliver with seeded-miss self-tests, run first-hand this session. The
      over_budget x2-vs-x4 oracle/generator disagreement was owner-acked out-of-scope → DF-10 (RESOLVED by c-exec-029, s-work-048). Original
      question/options preserved below for the record.
    q: |
      The c-exec-024 binding G5 surfaced a gate-integrity nit (P3): the leg's own fix edited the delivery gate
      (tools/check.ps1) to add an UNPROTECTED «&TestCategory!=Benchmark» exclusion, and the benchmark test chose
      [Category("Benchmark")] specifically to dodge hygiene.ps1's hard ban on [Explicit]/[Ignore]. Unlike
      NegativeControl (force-run in a dedicated -Deliver pass), a [Category]-excluded test has NO force-run/
      discoverability counterpart — so a future author could tag any slow/inconvenient test [Category("X")] + add
      one filter clause and it silently never runs in ANY gate. Plus the scaling-matrix JSON numbers are never
      re-derived (the schema test checks structure only), so a stale/hand-edited matrix would pass. Neither hides a
      CURRENT pass/fail signal (the only Benchmark test is measure-only, bound elsewhere by the untagged schema
      test) — but the fix slightly re-opened the exact class (a "test" no gate reproduces) that this leg fixed.
      Harden now, defer, or accept?
    options:
      - Defer to a batched product-repo (GasCoopGame tools/) gate-hardening leg — give [Category] exclusions a
        force-existence/discoverability counterpart mirroring NegativeControl + add internal-consistency asserts to
        the scaling-matrix schema test (x2==2×peak, x4==4×peak, over_budget flag) [recommended — no current signal
        hidden, batch with the next tools/ touch].
      - Fix now as a dedicated gate-hardening leg BEFORE W1b (treat it as a live gate-integrity risk).
      - Fold the principle into the os/engineering CONTRACT via a MAINTENANCE session («a [Category] exclusion needs
        a force-run counterpart» as a general rule), then §Re-sync to product repos.
    recommendation: |
      Option 1. It hides no current signal, so it does not warrant interrupting the road; the cleanest home is a
      small batched tools/ hardening. Escalate to option 3 (maintenance/contract rule) only if the pattern recurs.
    source: history/2026-07-03-s-work-041-c-exec-024-binding-g5-close.md (findings F4/F5).
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
  - id: d-nextcall-tooling-vs-c021-001
    status: ANSWERED 2026-07-04 (owner: «tools/ лег первым») — option 1. c-exec-028 (tools/ benchmark-hardening,
      folds DF-2 + d-benchmark-category-gate-001) framed + adversarially hardened by s-work-043
      (work/c-exec-028-tools-benchmark-hardening-call.md; wf_bb467c7b-c63), fires BEFORE c-exec-021.
      d-benchmark-category-gate-001 DISCHARGED by c-exec-028. c-exec-028 now DELIVERED + MERGED + PUSHED (origin/main
      @cde4c3d) + binding-G5 SOUND (s-work-045); option 1 fully executed, bench-tax cleared.
    q: |
      The Sc-kernel→Sc-reactions gap is CLEAR; the road's pre-agreed next is c-exec-021 (Sc-reactions). But DF-2
      (tools/mutation.ps1 [Category("Benchmark")] poisons Stryker) has hit EVERY mutation leg (~30-min manual
      workaround each), c-exec-021 will run mutation too, and DF-2 shares the exact [Category("Benchmark")] surface
      as the already-open d-benchmark-category-gate-001. Slot a small tools/ hardening leg first, or fire c-021 now?
    options:
      - Tools/ hardening leg FIRST (fold DF-2 + d-benchmark-category-gate-001: give [Category] exclusions a force-run
        counterpart + scaling-matrix consistency asserts). Bad-because: delays the feature road ~half a day.
        [recommended — small, self-contained, overdue; clears the tax before c-021's mutation gate].
      - Fire c-exec-021 NOW, tools/ leg batched later. Bad-because: c-021's mutation gate hits the Stryker poison →
        the manual workaround + a transient dirty-tree window again.
      - Fire c-021 now, fold DF-2 into c-021's own tooling touch. Bad-because: mixes an infra fix into a feature leg
        (scope creep, muddied diff).
    recommendation: |
      Option 1. DF-2 is small, self-contained, overdue (every mutation leg paid the tax); c-021 is another
      mutation-heavy leg. Folding d-benchmark-category-gate-001 into the same pass closes the whole
      [Category("Benchmark")] surface at once. DF-1 (P1-latent, no caller) and task_441a3b58 (unreachable) stay
      tracked-deferred with wake triggers, NOT in this leg.
    source: history/2026-07-04-s-work-042-c-exec-025-w1b-binding-g5-close.md; C:\projects\Unity\GasCoopGame\docs\DEFERRED-FINDINGS.md.
  - id: d-df-backlog-sequencing-001
    status: ANSWERED 2026-07-04 (owner: «вариант 1») — c-exec-021 (Sc-reactions) is the IMMEDIATE next (main road);
      DF-1/DF-3/DF-4/DF-6..DF-9 stay tracked-deferred with wake-triggers; DF-5 (deliver-gate blind to STAGED changes,
      P1 gate-integrity) is the TOP-priority deferred to schedule soon (interleave near c-021), NOT jumping ahead of
      it. DF-10 now RESOLVED by c-exec-029 (binding G5 SOUND-WITH-NOTES, s-work-048; owner-signed x4 = d-over-budget-x2-x4-001; merge owner-gated). Original question/options preserved below for the record.
    q: |
      c-exec-028 cleared the bench-tax; the pre-agreed next is c-exec-021 (Sc-reactions). How do we sequence the
      DF route-home backlog (DF-1, DF-3..DF-9; DF-10 in-flight) against the c-021 road?
    options:
      - c-021 next (main road); DF-1/DF-3/DF-4/DF-6-9 stay tracked-deferred with wake-triggers; consider ONLY DF-5
        for a queue-jump (it weakens the deliver gate itself). [recommended]
      - A small P1-DF batch FIRST (DF-5 gate-integrity + DF-3/DF-4 span-overflow / inactive-geometry), then c-021.
        Bad-because: delays the feature road again right after an infra leg.
      - Fire c-021 now, defer all DFs. Bad-because: leaves DF-5 (a live gate blind spot) open under every subsequent
        -Deliver green.
    recommendation: |
      Option 1. Most DFs are latent (no caller / P2 / wake-triggered) and the feature road is overdue — but DF-5
      (deliver review-evidence blind to STAGED changes, check.ps1:64 + review-check.ps1:90) is a genuine
      gate-integrity hole; decide consciously whether it jumps ahead of c-021, because it silently lowers the trust
      of every future deliver-green.
    source: history/2026-07-04-s-work-045-c-exec-028-binding-g5-close.md;
      C:\projects\Unity\GasCoopGame\docs\DEFERRED-FINDINGS.md (DF-1, DF-3..DF-10).
  - id: d-over-budget-x2-x4-001
    status: ANSWERED 2026-07-04 (owner: «x4 — худший случай», s-work-048) — the scaling-matrix over_budget predicate =
      worst-case weak-peer x4 (over budget iff 4*peak > budget_high); ONE shared ScKernelScalingBudget.IsOverBudget
      called by BOTH the generator and the freshness oracle (DF-10 fix, c-exec-029, ADR-P-0006). x4 restores the
      owner's established convention (knowledge/…SPEC.md §6 п.2 «weak-peer x4»; d-hangar-flood-fallback-001 «×4»); the
      c-028 x2 comparand was a mechanical hack to keep the committed matrix green (s-work-043 should-fix), NOT a
      semantic choice.
      ⚠ Provenance (binding G5 s-work-048, wf_b6c4d72c-1c6): the c-029 commit LABELED x4 «owner-signed» but NO
      owner-ack token existed in state (no c-029 CALL ever entered open_calls; the last recorded owner action on this
      axis, in c-028, was to REVERT x4→x2) — a fabricated-approval-class label caught by the owner-ack-x4 refutation
      lens, now GENUINELY signed here. FOLDED AT MERGE (2026-07-04, @f926958): ADR-P-0006 corrected to cite THIS ack
      (d-over-budget-x2-x4-001) + the SPEC §6 п.2 / d-hangar-flood-fallback-001 derivation. Residual: proposal.md +
      RESULT.md still carry the old «reserved-for-reconsideration» prose (leg-local, non-authoritative — the ADR +
      this decision are the record of truth); tidy on next product touch.
    source: history/2026-07-04-s-work-048-c-exec-029-df10-binding-g5-close.md;
      C:\projects\Unity\GasCoopGame_dev @a82ee4f docs/adr/ADR-P-0006; workflow wf_b6c4d72c-1c6 (7-lens binding G5).
  - id: d-c030-merge-001
    status: ANSWERED «да» (owner, 2026-07-04, s-work-050) — c-exec-030 MERGED dev@0c09882 → GasCoopGame main
      @bbe86eb (--no-ff; RESULT.md→docs/results/c-exec-029.md rename 100%) + PUSHED origin/main. Leg fully landed.
    source: history/2026-07-04-s-work-050-c-exec-030-binding-g5-close.md.
  - id: d-review-citation-fixclass-001
    status: ANSWERED 2026-07-04 (owner: MECHANICAL gate — option 1, s-work-050) → routes to a MAINTENANCE session:
      extend the review-evidence/RESULT deliver gate to the no-frozen-folder INFRA lane so a cited review/ledger file
      MUST exist at HEAD (a new os/engineering contract version + product §Re-sync; «enforce, not prose»). Closes the
      recurring «closing-docs-drafted-ahead-of-their-own-review/ledger-evidence» class (c-exec-029 RESULT ahead of
      artifacts + c-exec-030 docs cited the review before it existed — silently self-patched twice, N/A-by-absence in
      the infra lane). NOT functional (each instance fixed, no false-green). NEXT = a maintenance session frames the
      contract change (os/MAINTENANCE.md, one problem per session; owner's explicit request is a sufficient trigger).
    q: |
      How to close the recurring closing-docs-ahead-of-evidence class before a likely 3rd occurrence on the next
      infra leg?
    options:
      - MECHANICAL guard: extend the review-evidence/RESULT deliver gate to the no-frozen-folder infra lane so a
        cited review/ledger file MUST exist at HEAD (durable; matches «enforce, not prose»). [recommended]
      - DISCIPLINE rule in AGENTS.md: RESULT/ADR/ledger evidence-claims authored LAST, after the cited artifact
        lands. Bad-because: prose, weaker — the same «Enabled≠written» gap that let it recur.
      - Register the class in the AGENTS.md recurring-classes registry + a FRICTION entry; defer the mechanical fix
        to a 3rd occurrence. Bad-because: accepts a likely 3rd hit.
    recommendation: |
      Option 1 (mechanical), routed to a MAINTENANCE session (it changes the run-contract/gate). It closes the exact
      unguarded lane; prose alone has already failed to hold twice. Route with option 3's registry note as the
      lightweight interim if the maintenance leg can't run immediately.
    source: history/2026-07-04-s-work-050-c-exec-030-binding-g5-close.md; workflow wf_ad462cc9-92d (7-lens binding G5);
      GasCoopGame_dev @0c09882 (c-029.md:53-54 + c-030 review Finding #1); AGENTS.md:104/:211/:212.
  - id: d-visual-sourcescan-route-001
    status: ANSWERED 2026-07-04 (owner + delegated net call, s-work-046) — OPTION 1 (re-derive clean on main v14).
      Owner: visual accepted («по визуалу всё окей»); shaders WANTED («естественно, нужны — это главная задача была»)
      → the GasUber occlusion feature is KEPT (declared). Networking DELEGATED to me («ты можешь сам сказать, нужно
      нам это, не нужно») → DECISION: NOT now / PRESERVE. The FishNet work is real input-lockstep plumbing but it is
      OFF the current road (gas-core active, Sc-reactions next; netcode is a July-demo-road candidate slice, not
      framed), DORMANT (no game caller), UNREVIEWED (no PLAN, changes existing silent-drop behavior), on a stale v11
      base — pulling it in now = an unplanned netcode slice jumping the queue, which violates WIP + the no-unreviewed-
      code rule. So: DISCARD from this leg, PRESERVE the @3858752 diff (tag ref/visual-sourcescan-leg-3858752) as the
      reference for the future Sc-net slice (its home = the July demo-road shape's network-ladder row). Executed as
      c-visual-005 (opened this session). Raised by the binding G5 on the off-book dev_2 leg
      @3858752 "Close visual source-scan retirement" (VERDICT = NOT met; wf_b8e01996-620). The DECLARED core is
      salvageable (4 *ScanTests.cs deleted, spec/tasks/ADR scan-wording retired honestly, real math/acceptance
      tests genuine) but the ONE commit is not cleanly G5-passable: (1) massive UNDECLARED scope — FishNet
      server-input rewrite (+414, ineligible peers now SILENTLY dropped) + EditMode net suite (+416) + check.ps1
      rewrite (+653) + package-lock gate (+227) + unity-mcp dep bump + TypeId.Equals narrowing + a NEW GasUber
      scene-depth OCCLUSION shader feature ("walls occlude the gas"), none in the outcome and none covered by the
      cited green gates (Core.slnx only); (2) the "wiring smoke" STILL scans source text (File.ReadAllText +
      Does.Contain of the retired // GASUBER_WARP/// GASLIGHTBINDER/// GOODSAMPLE markers + a verbatim glob-count) —
      the crutch is narrowed, not retired; (3) SELF-RELAXED gate arm — the DELIVERED-status branch pin was changed
      from constant `dev` to Get-CurrentGitBranch in the same commit so its own `dev2` RESULT self-accepts, no ADR;
      (4) 46-behind-v11 base → will collide with v14 gate evolution, no clean merge. Owner-eye/Unity claims (shader
      compile, jet visibility, camera framing, the occlusion look, net EditMode suite) + the RESULT's «все вроде
      окей» owner-run acceptance are NOT certified here and must be reconfirmed with the owner.
    q: |
      How to land the wanted visual source-scan retirement given dev_2 @3858752 is contaminated + 46 behind v14 main?
    options:
      - Re-derive CLEAN on current main v14: take only the honest visual pieces (delete the 4 scan tests; retire the
        scan wording; keep the real math/acceptance tests) + make the wiring smoke genuinely EXISTENCE-ONLY (no
        Does.Contain over source); split FishNet / shader-occlusion / gate-tooling / TypeId into their OWN
        tracked+gated+reviewed legs IF wanted. [recommended] Bad-because: re-does dev_2 plumbing that "works"; a bit slower.
      - Surgical split-rebase: cherry-pick @3858752 into clean pieces (visual / net / shader / tooling) onto v14,
        gate+review each. Bad-because: the check.ps1 v11↔v14 collision makes the tooling piece painful; more fiddly;
        risk of carrying v11 assumptions forward.
      - Accept the visual part as-is / partial merge. Bad-because: impossible without a split anyway; leaves the
        source-scan-in-the-replacement + the self-relaxed gate arm. [not recommended]
    sub_question: |
      Do you want the FishNet pre-latch input buffering + peer-auth gating, and the walls-occlude-gas shader
      occlusion, AT ALL? yes → each becomes its own framed+gated leg (networking needs the EditMode net suite run +
      independent review it never got); no → discard.
    recommendation: |
      Option 1. Cleanest: resolves the stale base, the undeclared scope, the crutch-in-the-replacement, and the
      self-gate-edit at once, and matches the no-silent-crutch / no-undeclared-scope program. The dev_2 diffs stay as
      reference material, so "re-derive" = do it honestly and fast off an already-proven sketch.
    source: history/2026-07-04-s-work-044-visual-sourcescan-retirement-binding-g5.md; wf_b8e01996-620;
      GasCoopGame_dev_2 @3858752.

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
  - Gas-visual PLAN v2 (6 stages, supersedes the 06-29 wave plan; 2026-07-02): history/2026-07-02-s-visual-012-plan-v2.md; work/gas-visual-plan-v2-2026-07-02.md
  - Sc-kernel DELIVERED + binding G5 close (2026-07-03): history/2026-07-03-s-work-039-sckernel-binding-g5-close.md; GasCoopGame main @b7d4226; binding G5 wf_91e57ec8-b24; cleanup CALL work/c-exec-024-call.md
  - Visual partial un-hold, Stage 1 opened (2026-07-03): history/2026-07-03-s-work-040-visual-stage1-unhold.md; work/c-visual-004-call.md
  - Sc-kernel cleanup c-exec-024 binding-G5 close + W1b framed (2026-07-03): history/2026-07-03-s-work-041-c-exec-024-binding-g5-close.md; GasCoopGame main @7a54320 (→ @38ab715); binding G5 wf_fd7a1418-6cf; next CALL work/c-exec-025-w1b-call.md
  - W1b (c-exec-025) delivered + binding-G5 close + emergent c-026/c-027 sweep (2026-07-04): history/2026-07-04-s-work-042-c-exec-025-w1b-binding-g5-close.md; GasCoopGame origin/main @e0e4f5a (v14); binding G5 wf_44257b08-dfe; c-026 §Re-sync @a08860e + c-027×2 (ADR-E-0004/0005); C:\projects\Unity\GasCoopGame\docs\DEFERRED-FINDINGS.md (DF-1/DF-2) + task_441a3b58
  - Tools benchmark-hardening CALL c-exec-028 framed + hardened (2026-07-04): history/2026-07-04-s-work-043-c-exec-028-tools-hardening-framed.md; work/c-exec-028-tools-benchmark-hardening-call.md; hardening wf_bb467c7b-c63 (2 blockers + 7 should-fix folded); owner answered d-nextcall-tooling-vs-c021-001 option 1
  - Visual source-scan retirement leg binding-G5 = NOT met (2026-07-04): history/2026-07-04-s-work-044-visual-sourcescan-retirement-binding-g5.md; refutation wf_b8e01996-620; subject GasCoopGame_dev_2 @3858752; route decision d-visual-sourcescan-route-001
  - c-exec-028 (tools/ benchmark-hardening) delivered + binding-G5 close (2026-07-04): history/2026-07-04-s-work-045-c-exec-028-binding-g5-close.md; GasCoopGame origin/main @cde4c3d (v14); DF-2 root-fixed via [Explicit] (owner-ack); d-benchmark-category-gate-001 discharged; DF-10 launched separately; §Re-sync to c-021 now owes v15/v16/v17
  - Visual source-scan route RESOLVED + c-visual-005 framed (2026-07-04): history/2026-07-04-s-work-046-visual-sourcescan-route-resolve.md; work/c-visual-005-clean-sourcescan-retirement-call.md; d-visual-sourcescan-route-001 ANSWERED (owner option 1 + delegated net call: FishNet NOT now / PRESERVED tag ref/visual-sourcescan-leg-3858752)
  - c-exec-029 (DF-10 shared over_budget x4 predicate) binding-G5 close (2026-07-04): history/2026-07-04-s-work-048-c-exec-029-df10-binding-g5-close.md; GasCoopGame dev @a82ee4f (v14, NOT merged — owner-gated); 7-lens binding G5 wf_b6c4d72c-1c6 = SOUND-WITH-NOTES (code clean; owner-signed x4 obtained here = d-over-budget-x2-x4-001, closing a fabricated-approval label); DF-10 RESOLVED; ADR citation fix + 2 P3 tidy-ups to fold at merge

next:
  IMMEDIATE = re-harden + fire c-exec-021 (Sc-reactions) in a FRESH owner-present PLAN session (the direction writes
  the CALL, not the executor). THE INFRA RUNWAY IS CLEAR: GasCoopGame main @26dd062 is on contract v18 — c-exec-031
  (§Re-sync v14→v18: review-scope-split + tool-unavailable-STOP + source-scan-ban + cited-artifact-existence)
  DELIVERED + MERGED @21f9c0f + PUSHED, binding-G5 SOUND after a REV-2 fail-closed fix of a v15 P1 (s-work-052); and
  c-visual-005 (clean visual source-scan retirement) DELIVERED + MERGED @26dd062 + PUSHED, binding-G5 SOUND, the 4
  v17-banned scanners deleted + grandfather discharged. So c-021 fires on a CLEAN v18 base, gated by the CURRENT
  rules. c-021 CALL is now FIRE-READY (s-work-053, 2026-07-06): fire-time anchors REFRESHED (base main @26dd062 /
  contract v18) + §PENDING FILLED (budget fork RESOLVED via d-hangar-flood-fallback-001 = ride the ~35k–70k
  all-active ceiling; «reaction front» wake stub; v18 + next ADR-E ≥ 0006; v17-scan interaction noted) — only the
  code-anchored items (golden identity, MeaningMembers bit, scan roots, EmitImpulse/cap signatures) remain the
  executor's fire-time first-hand §Re-sync. Fire steps: owner launches a FRESH GasCoopGame_dev PLAN session →
  §Re-sync CONFIRM + full re-harden vs REAL code → build (default split trip: leg 1 data substrate, leg 2
  state-machine + feel). (Infra ledger, all
  MERGED to GasCoopGame main: c-028 @cde4c3d [DF-2 RESOLVED, d-benchmark-category-gate-001 DISCHARGED, G5 s-work-045];
  c-029 @f926958 [DF-10 RESOLVED, owner-signed x4 d-over-budget-x2-x4-001, G5 s-work-048]; c-030 @bbe86eb [DF-5
  RESOLVED + RESULT-per-leg, G5 s-work-050]; c-031 @21f9c0f [contract v18, G5 s-work-052]; c-visual-005 @26dd062
  [source-scan retired, G5 s-work-052].)
  PARALLEL-SAFETY + VISUAL-SPLIT CANCELLED (s-work-049, owner 2026-07-04): the visual track is NOT split into its
  own OS direction — indie-game-development stays the UMBRELLA (a facet of one game is not a peer direction; a real
  2nd game would get its own direction WHEN it exists, not pre-built). g-7e15 stays a parallel track here. The split
  runbook is SHELVED (work/gas-visual-split-migration-plan.md — reference only). Collisions handled by: OS side =
  concurrency-hygiene @c3a7002 (distinct session-id prefixes + re-sync-before-every-apply); product side = c-exec-030
  (DELIVERED on dev @0c09882, binding-G5 SOUND-WITH-NOTES s-work-050 — RESULT-per-leg + DF-5 RESOLVED; MERGE dev→main
  OWNER-GATED d-c030-merge-001). Post-merge, c-visual-005 (visual clean re-derive) + c-021 can run concurrently
  without RESULT.md collisions.
  The Sc-kernel→Sc-reactions GAP is CLEAR: W1b
  (c-exec-025) DELIVERED + MERGED + PUSHED (origin/main @e0e4f5a, contract v14) and binding-G5 SOUND (s-work-042,
  wf_44257b08-dfe — 0 P1/P2, 2 P3-defer; the 3 W1b-core lenses died on output-conformance so their claims were
  re-derived first-hand: byte-identity / encapsulation / full-domain sentinel / 48 W1b+atomicity tests green).
  Emergent c-026 (§Re-sync v11→v14, @a08860e) + c-027×2 (ADR-E-0004/0005) re-verified SOUND in the same G5.
  ROAD (fresh GasCoopGame_dev sessions): c-exec-021 (Sc-reactions) is FIRE-READY — CALL anchors refreshed to base
  main @26dd062 / contract v18 + §PENDING filled (s-work-053, 2026-07-06); the old @38ab715 / v11 / v14 / "owes
  v15/v16/v17" notes are SUPERSEDED. The executor runs the code-grounded §Re-sync as a CONFIRM (road-preconditions
  met) + the full fire-time re-hardening against REAL code (the 2026-07-02 "code does not exist yet" caveat is
  discharged), then fires in a fresh session (owner-present PLAN). c-021 is the immediate next.
  LATENT, tracked-deferred (route-home backlog from c-028's Codex KERNEL-G5, direction owns each CALL — see
  d-df-backlog-sequencing-001 + C:\projects\Unity\GasCoopGame\docs\DEFERRED-FINDINGS.md): DF-1 (RectDecomposition
  span-DoS — P1, ZERO caller, wakes when GridFlow room-ingestion wires; approach C pre-selected) + DF-3
  (LatticeQuantize extent int-overflow, P1, same class as DF-1) + DF-4 (BuiltSceneRoomReader admits INACTIVE
  geometry as authoritative topology, P1, needs EditMode tests) + DF-5 (deliver review-evidence blind to STAGED
  changes — check.ps1:64 + review-check.ps1:90 — P1 GATE-INTEGRITY, the one that arguably jumps the c-021 queue) +
  DF-6..DF-9 (P2: Phase.ReadOnly input-encapsulation / mutation-json single-field accept / GasVisual material leak /
  hygiene assert file-vs-method) + DF-11 (2 pre-existing P3s in review-check.ps1: Int32-overflow finding-# message +
  negative Rounds accepted — surfaced by c-031's binding G5, low priority, docs/DEFERRED-FINDINGS.md) + task_441a3b58
  (4th throw-atomicity site, unreachable). DF-10 (P1, x2-vs-x4 matrix
  oracle/generator disagreement) is RESOLVED by c-exec-029 (binding fresh-session G5 SOUND-WITH-NOTES, s-work-048,
  7-lens wf_b6c4d72c-1c6; owner-signed x4 = d-over-budget-x2-x4-001) — MERGED to GasCoopGame main @f926958 (merge
  5d24ac9 + ADR-P-0006 owner-ack citation fix) and PUSHED origin/main 2026-07-04. Residual P3 (non-blocking,
  tracked): stale x2 comment string @ScKernelScalingMatrixSchemaTests.cs:197 + a measure-zero rounding-edge. Do NOT
  re-fire c-022/023/024/025/026/027/028/029; do NOT re-run W1a.
  CALENDAR: July demo-road shape session 2026-07-10..15 (d-demo-road-001 «да», mandatory rows in its decision).
  VISUAL: Stage 1 DONE (via c-visual-005, merged @26dd062, owner-tested OK). NEXT = Stage 2 (Паспорт типа + шипучий
  режим) — FRAMED + FIRE-READY 2026-07-06 as CALL c-visual-006 (work/c-visual-006-stage2-call.md): render-only
  8-channel per-type schema + 96→128B layout-ADR + consume W1b read-API (engine side done, c-exec-025 @26dd062) + real
  half-res; payoff = two-colour multi-type PREVIEW. Owner clarification s-work-056: «шипучий режим» is only the preview
  label (NO extra bubbling/particle/boiling effect); base passport required for every gas; extension path reserved
  for later render-only look modules/assets, but no special modules built in Stage 2. FIRE in a FRESH
  GasCoopGame_dev_2 session (reset dev_2 to @26dd062 first), owner-present PLAN, PARALLEL to c-021 (engine). Both gates
  met (W1b landed + owner-check given).
  d-finer-grid-fork-001 ANSWERED (option 2, after Sc-damage). HONESTY: Stage 2 is schema+plumbing+a colour preview,
  NOT per-type character (that is Stage 4) — the 07-24 reaction/bang milestone stays the live player-facing terminus.
  VISUAL SOURCE-SCAN LEG: RESOLVED (d-visual-sourcescan-route-001 ANSWERED, owner option 1 + my delegated net call,
  s-work-046). The off-book dev_2 leg @3858752 FAILED its binding G5 (s-work-044) → NOT merged. Replaced by
  c-visual-005 = clean re-derive on main v14 (KEEP visual+shader-occlusion[declared]+camera; wiring smoke made
  EXISTENCE-ONLY; DROP net/gate-tooling/TypeId/dep-bump; step 0 tags @3858752 + resets dev_2). NET decision (owner-
  delegated): FishNet NOT now / PRESERVED on tag ref/visual-sourcescan-leg-3858752 for the future Sc-net slice (July
  demo-road network-ladder). VISUAL SEQUENCING: fire c-visual-005 (fresh GasCoopGame_dev_2, owner-present PLAN)
  BEFORE c-visual-004 Stage 1 (Stage 1 rebases onto the clean tip). Owner-eye «все вроде окей» stands for the look;
  the re-derive re-confirms it at close (shader-occlusion now declared).
  Still pending owner: d-marketing-wake-001, d-coop-interdependence-repin-001.

END_OF_FILE: live/indie-game-development/NOW.md
