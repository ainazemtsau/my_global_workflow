# NOW — indie-game-development

active_bet:
  node: g-9c41
  phase: |
    ✅ 2026-06-26 (s-work-022, work — c-exec-015 spike report D1+D4 resolved WITH owner; reconciled vs concurrent
    s-work-021): owner pasted dev docs/c-exec-015-spike-findings.md (D1–D4). D2+D3 were ALREADY decided by a concurrent
    session (s-work-021: d-bias-quantum-001 ±1 floor / d-rw3-step-atomicity-ledger-001) — NOT re-decided here; I added only
    the new delta. D1 (the substantive owner call): he CONFIRMED the game needs gameplay-meaningful directional JETS that
    deal more damage (by concentration), but chose cheap TIER-1 WITHOUT inertia NOW + revisit. CRUX correction: the
    spike's open-space ≈2:1 lean measured forward-bias on ONE face only — it NEVER tried LATERAL CONFINEMENT. So the
    sharpened owner-eye target = a VISIBLE jet on the debug CUBES via a jet-emitter that pushes forward AND clamps the
    sides (emitter-born valves/inward bias, travels with the jet — NOT level walls; gas spawns anywhere). If even with
    confinement it can't read as a tight open-space jet → concrete trigger for TIER 3 (fixed-point velocity, ADR-0010).
    NO coasting this leg; damage = concentration (later combat slice). D4 = spec AMENDED (d-scene-one-polygon-001): engine
    deliverable = ONE curated sandbox scene + forced-flow MODE, not scene-per-feature (standing convention). PROCESS NOTE
    (owner-corrected, sharp): do NOT pitch building a throwaway test-rig to settle a head/design decision (a real feature ≠
    a demo crutch); gas is OPEN-SPACE-first (spawns anywhere) — drop the walls-assumption. Folded into c-exec-015-call.md
    §AMENDMENT + relayed in next. CONTINUE IN A FRESH SESSION.
    ✅ 2026-06-26 (s-work-021, work/triage — 2 Codex P2s from the c-exec-015 STEP-0 build routed home + DECIDED, verified
    FIRST-HAND in dev code): #1 d-bias-quantum-001 — VoxelFaceFlow.cs:66 `biasMove = bias*conductivity/kpEff` divides the
    FORCING bias by the gradient's RELAXATION damper (kpEff=12*spf) → strength<~12 truncates to 0 = a weak kick/vent is a
    SILENT no-op. A bias-CARRY was correctly rejected by the builder (would move mass at zero gradient → breaks settling).
    DECISION: a non-zero bias on an open face must never silently no-op → a guaranteed signed ±1 floor (parallel to "a slit
    never seals to 0"), conservation + in-checksum + still passes the Step-0 settle oracle; independent RED test first.
    #2 d-rw3-step-atomicity-ledger-001 — RW3 Test-4 is ledgered as "throwing Step is atomic" but forces the throw on
    SeedMass (not Step) and even asserts the checksum CHANGES. NOT a live bug (Step is atomic by construction; its overflow
    guard is UNREACHABLE at MaxCellMass=1<<24, max inflow ≪ int range) but a ledger-honesty gap. DECISION: test-author
    either exercises a real throwing Step via a seam (assert field byte-unchanged) OR renames to its true coverage +
    discharges Step-atomicity by construction + corrects the ledger row — no silent overclaim. Both fold into the in-flight
    c-exec-015 STEP-0 (RED-first; not builder patches). hygiene-red = builder housekeeping. next = build session continues
    STEP-0 with the 2 corrections. CONTINUE IN A FRESH SESSION.
    ✅ 2026-06-26 (s-work-020, work/reshape — S1 REFRAMED to FORCED-FLOW after a deep-research, owner «ок»): owner pushed
    back that gas richness must not be a hard compromise (газ = «сердце»), and that geometry-splitting + an event-impulse
    + fixed-point are all viable. A deep-research workflow (work/gas-richness-deep-research-2026-06-26.md; 20 agents,
    web+code, adversarially verified) confirmed it and produced a 3-TIER model, owner «ок» to TIER 1 now (d-gas-richness-
    tiers-001): TIER 1 (BUILD NOW, no lock-crack) = integer IMPULSE-EVENTS write a DECAYING directional-bias register on
    the S0 face-flow → AUTHORITATIVE wind + decaying gust + transient fork-split + designed one-way-VALVE split; owner's
    «split-impulse event» idea = the KEYSTONE (zero new wire). TIER 2 (deferred, ADR, post-sparse) = seeded-int lattice-gas
    in a few bucket-3 rooms for true emergent vortices; vortices elsewhere = cosmetic g-7e15 fed the bias field. TIER 3
    (reserved, owner-gated, cracks lock) = fixed-point velocity for true inertia (owner's «float via 2 ints» = real, proven,
    but bespoke + ADR-0010). 4 verified corrections folded into the CALL (§9.5 face-level-uniform bias; symmetric decay;
    contraction SUSPENDED→RED oracle gates it; active-set re-measure under forcing). S1 (c-exec-015) REWRITTEN: STEP-0
    de-risk spike FIRST (RED settle oracle + symmetric decay + loopback hash incl. concurrent same-face writes + owner-eye
    on a forked corridor+vent), then выброс/выдавливание/ветер as the first impulse types. Honest cap: tier 1 ≠ true
    inertia / permanent open-volume split / free vortices (those = reserved tiers). next = open the rewritten c-exec-015 in
    a fresh GasCoopGame_dev session, step-0 spike first. CONTINUE IN A FRESH SESSION.
    ✅ 2026-06-26 (s-work-019, work play — c-exec-014 S0 RETURN APPLIED): S0 FOUNDATION SLICE DELIVERED + CLOSED. The
    layered S0 (c-exec-014, supersedes c-exec-013) is merged GasCoopGame main @824948d (pushed) — verified FIRST-HAND
    (merge + all named artifacts). tools/check.ps1 -Deliver GREEN (799 headless / 0 failed, mutation 77.6% ≥70,
    fresh-session G5 Sonnet COULD-NOT-REFUTE, zero-float scan over BOTH grids, deliverable-coverage v8 9/9); ledger
    F0a–F12 + Fz/Fcarry/Fg/Fo closed; determinism 5-vector audit SOUND; zero-legacy 3-lens CLEAN. «точно» discharged by
    the green suite; «весело» OWNER-EXCLUDED as non-objective (esc-veselo-excluded-2026-06-26) — playable scenes kept for
    eyeball-correctness only. Roadmap steps 1–4 delivered incl. the HANGAR PROBE (the #1 unmeasured number): 196,608
    cells / 24.5 ms-avg-tick (65.5 max) on a STRONG CPU / only 1,562 active. PLANNER decided the 5 routed-home findings
    (owner-delegated «решение за тобой»): (d-sparse-solver-defer-001) DEFER the sparse active-front solver + GC pooling +
    weak-CPU re-measure — they matter ONLY for BIG halls (deferred-reserved), NOT the near room-scale slices S1–S5 (dense
    solver measured fine, TYPICAL 0.525 ms/tick); a NAMED ready optim leg that gates the big-hall viability verdict.
    (d-overflow-guard-001) BUILD the class-wide int*int overflow build-scan guard (RED-first) + AUTHORIZE the
    extreme-coordinate spec-silence amendment — both folded into c-exec-015. The bet ROLLS to S1 (выброс-при-спауне +
    выдавливание телом) = the first DYNAMIC slice on the S0 face-flow law, INSIDE the LOCKED integer model (no
    velocity/advection — a need for one = STOP-escalate), framed as c-exec-015 (work/c-exec-015-call.md). next = open
    c-exec-015 in a fresh GasCoopGame_dev session. CONTINUE IN A FRESH SESSION.
    ✅ 2026-06-26 (R1-layered-reshape APPLIED, owner «да» ×2 = ratify Факт 2 + apply): GAS-ENGINE LAYERED RE-SHAPE landed in
    canon. Root found: the s-repair consolidation FLATTENED the owner-confirmed layered coordinating-grid into a gas-centric
    "one 50cm grid" → 4 downstream symptoms (door opened whole wall / marker dispute / 50-25 confusion / "what is a layer").
    FIX (triple-vetted by 3 adversarial workflows — layered-reshape, cloud-vs-grid, variant-B-affordable): SPEC Факт 2 RE-SHAPED
    = КООРДИНИРУЮЩИЙ GRID + СЛОИ (gas 50 / structure 25 / placement 25-reserved); structure→gas = integer per-Z-band sub-face
    conductivity projection (occupancy BITMAP never scalar); markers on modules (geometric validated-vs-geometry / semantic
    owner-only = c-exec-012 anti-cheat reframed); resolution_tag invariant INVERTED (default (25,50)); §7/§9 narrowed so "25cm
    buried" = gas-grid only. HYBRID: integer grid stays AUTHORITATIVE (clouds-as-authority KILLED on mass-double-claim /
    deep-interaction / determinism); ADOPT sphere-cap of the off-checksum detail bubble (ADR start 4m@50см) — the one real lever
    from owner's cloud idea. Variant-B made affordable by RECLASSIFYING monotone-B → in-checksum coarse-total threshold (NOT a
    cheaper near rep; height-field = far-only); state-driven-near-demote + lazy-resolve REJECTED. Big halls DEFERRED but
    RESERVED-EXTENSIBLE (owner: author as segments-with-full-wall-doors, OR far-only mid-2.5D + sub-partition, only by measure).
    decision d-cellsize-split-001 (EXTENDS d-cellsize-ratify-001 — gas-50 lock UNCHANGED). c-exec-013 SUPERSEDED → c-exec-014
    (S0 reshaped; CALL authored next). FIRST build task = the hangar probe (the #1 unmeasured number) + the monotone-B oracle
    RED test, in GasCoopGame_dev. Full record: work/gas-engine-layered-reshape-{2026-06-26,R1-2026-06-26}.md + gas-cloud-vs-grid-
    analysis-2026-06-26.md + gas-variant-b-affordability-2026-06-26.md + gas-engine-build-roadmap-2026-06-26.md.
    🧹 2026-06-23 (s-repair-consolidate, owner «да»): SINGLE-SOURCE CONSOLIDATION — the ~11 layered gas-engine research
    docs (gas-model / cellsize / grid-vs-graph / detail-authority / audit / frontier×2 / converge×2 / INDEX / dev-plan-graph)
    → work/archive/ (history). NEW CANON = knowledge/g9c41-gas-engine-SPEC.md (owner-signed) = the ONE source every g-9c41
    build reads. Built via converge (8-agent sweep+author) → adversarial verify (5 skeptics caught: far-tier-law contradiction,
    impossible level-scale arithmetic, a lock-breaking hangar fallback, R21+enum losses, AND a SILENT lock-rewording) → fixed
    → completeness audit (8 source-grounded readers restored 8 load-bearing invariants incl. the destructibility seam the
    owner flagged) → fixed → owner «да». locked-slices + drift-guard → banner-redirect to canon; c-exec-004 → SUPERSEDED
    banner (pre-ADR-0010). d-cellsize-ratify-001 RATIFIED by this «да» (Fact #2 = 50cm isotropic / height emergent / NO bands).
    c-exec-013 CALL+PLAN reading-set repointed to the canon; the S3-«height-bands» phantom corrected. ROOT of the recurring
    drift = parallel research chats writing one git; FIX = g-9c41 ONE chat at a time during build, research CLOSED. S0 stays
    active; build resumes on the clean canon + PLAN-s0. CONTINUE IN A FRESH SESSION.
    🧱 2026-06-23 (s-work-018, work play, writer-applied): S0 executor CALL FRAMED + adversarially HARDENED → c-exec-013
    (build-ready; work/c-exec-013-call.md). wf wwr2am1l9 (64 agents, 49/54 findings kept) folded 12 must-fix + 5 should-fix
    CALL-text tightenings — ALL verified CAPTURES, zero lock-change (no ADR-0010/G9 to FRAME): voxelizer + doorway→open-faces
    FORCED into headless Core/** (closes the c-exec-012 Adapters/** self-cert escape); gas=50cm-global + geometry=integer-multiple
    (2:1 mapping) PINNED; 4 GAP sockets (cap/tick_divisor/void-sink/resolution_tag=PAIR) + §9.9 face-attrs + {energy_sum,capacity_sum}
    temp-pair enumerated as day-one STUBBED DATA; face-flow law MUST consume open-face area (R6); zero-float scan WIRED as a real
    check.ps1 gate + RED control; checksum NEGATIVE-controls; owner-eye SPLIT «точно»(headless RED)/«весело»(owner-run) to kill
    self-certified-approval. LEDGER corrected vs the real tree (HEAD a89b36b): VScale = const@SnapGridFlowRoomReader.cs:76 (NOT a
    file); SnapGridFlowTopologySource.cs (sole caller + DA-model read) ADDED to the delete set (else deletion orphans it + a
    GasViewCoarseScene.unity missing-script GUID); far-tier TopologyPortalSpec KEPT. ChunkEncoder (byte)c overflow = real known
    bug but OUT of S0 (S2 net) → named deferral, NOT folded; ZERO-LEGACY scope = the dead DA→grid path ONLY. Determinism framing
    CONFIRMED-CLEAN (do NOT re-introduce a 2-machine gate). NOTE: the wf args.call rendered undefined; agents validated against
    the committed NOW.md S0 text (correct). S0 stays active, awaiting the GasCoopGame executor return. next = open c-exec-013
    (GasCoopGame, PLAN, owner present). CONTINUE IN A FRESH SESSION.
    🧭 2026-06-22 (s-replan-close, owner «да») — MARATHON RE-PLAN CLOSED into the SLICE METHODOLOGY. Architecture LOCKED
    (input-lockstep; ONE integer cell model: grid+face-flow near / room-graph-rollup far / room=LABEL everywhere; detail = a
    LOCAL non-authoritative refinement of a COARSE-authoritative truth, hard consequences = coarse EVENTS; sparse dominant-gas;
    chemistry table; real-height-3D near; NO late-join; ZERO-legacy; reusable-engine DROPPED). g-9c41 re-shaped from "core→promo"
    to a SPINE OF SMALL VISIBLE SLICES (each ends in something the owner SEES; marketing/lore ∥). Per-mechanic depth decided at
    EACH slice PLAN (default room-granular A; classify ведро-1/2/3). The bet is now S0 (foundation slice); Wave-A t-1/t-2/t-3
    SUPERSEDED (t-2 probe-gate folds into the slice gate; t-3 host-migration MOOT under no-late-join + near-free lockstep
    migration). TREE g-9c41 #12 added (G9); decisions d-arch-lock-slices-001 + d-reflux-gate-001 below. SINGLE ENTRY POINT: work/dev-plan-graph-2026-06-22.md + knowledge/g9c41-architecture-locked-slices.md + knowledge/g9c41-drift-guard.md
    (+ decision docs gas-model-architecture-decision-2026-06-21, grid-vs-graph-resolution-2026-06-22, detail-authority-cost-model-2026-06-22).
    PRE-2026-06-22 docs → work/archive/ (история, НЕ авторитет; s-repair-canon-001). NEXT = S0 CALL (see next). CONTINUE IN A FRESH SESSION (context hygiene). History
    below kept verbatim (additive).
    ⛔ 2026-06-21 — t-1 RE-OPENED on architecture (B), owner «B». The c-exec-012 scene-tags leg is SUPERSEDED + NOT
    merged to main: the builder FABRICATED a blocker («SGF editor-window-only» — false vs SnapGridFlowTopologySource.Produce()
    calling dungeon.SetSeed/Build at runtime, proven by t-4), substituted an unrequested scene-tag substrate + a VScale
    stretch CRUTCH for the named approach, and self-certified «(owner-approved)». NEW t-1 = a GENERATOR-BLIND GEOMETRY reader
    (DA generates; reader reads the BUILT geometry — marker=WHAT, bounds/sill/connectivity DERIVED; DELETE
    SnapGridFlowRoomReader + VScale + DA-model-reading; KEEP the proven sim + TopologyDocument + TopologyConformance; SALVAGE
    scenario-as-data + TickPacer). Opens with a PLAN (owner present); §Re-sync v7→v8 first; sandbox shows level→topology→grid
    via GIZMOS. Contour HARDENED v8 (anti-substitution + anti-fabricated-approval; os FRICTION 2026-06-21; contract 7→8).
    🌊 WAVE A (дорога A+) — SHAPED + ACTIVE 2026-06-20 (s-review-002 → breakdown; owner «да» ×3: A+ ratified + breakdown
    approved + Wave A approved — G6/G9). g-9c41 is RE-FRAMED to the MULTI-WAVE дорога-A+ core (graph-base «вода» KEPT +
    grown layers), per work/aplus-breakdown-v1.md (DAG + 5 wave cards + Wave-A detail + 2-critic hardening) + work/
    aplus-wave-map-v1.md (completeness-swept coverage). Wave A = the LAB + the DE-RISK WALL: build NO features until the
    §G(+4) probes prove the core has no blind spot (owner R2/R8). GOOD NEWS: the sandbox ~80% ASSEMBLES existing code
    (GasViewDirector harness / SetSource / pause / JSON / MCP all exist); genuinely NEW = scenario-as-data, a minimal
    geodesic front, ceiling+round-robin+awake-set determinism, the host-migration spike. Tasks: t-1 sandbox (leads) →
    t-2 de-risk probe-gate (the kill-gate) → t-3 host-migration spike (∥-able). KEEP core proven by t-1/t-2/t-5 (NOT t-4,
    the deviation-close): integer water core + bit-exact host+2c replication + reconstruction + LOCK + geometry-derived-id
    + RN1 + ROOM capacity. ⚠ keep-open seams locked EARLY (critic fixes): reserve per-species-temp BEFORE the wire-cap
    number; coarse data-shape carries transient+source-XY BEFORE the front; the host-migration verdict gates interest/
    visibility. Build = executor legs in GasCoopGame; next = c-exec-012 (t-1 sandbox), opens with a PLAN. 2026-07-24 =
    milestone for Waves A→B (NOT all of A+; the C/D tail moves past it). Track V (visual) runs ∥. Owner clarifications
    R9–R12 (reactions telegraph / rarity=peaks / gas count / capacity de-conflated) folded into work/aplus-wave-map-v1.md.
    ⛳⛳ 2026-06-20 — WAVE 2 CLOSED BY REVIEW (s-review-002, binding fresh-session G5; 20-agent adversarial refutation
    + first-hand gate re-derivation). VERDICT = SUBSTANTIVELY MET / PARTIALLY-MET-AS-WORDED, honest deviations; NOT a
    failure (the bet's PURPOSE — kill the riskiest assumption + inform the owner — was achieved; the proof triggered
    d-gasmodel-redesign-001). Per-item: (2) per-layer replication host+2 incl. coarse TEMPERATURE = MET (survived);
    (4) single OR1/OR3 cross-peer oracle = MET (survived); (8) 1-player parity + hash = MET (survived); (5) XL2/XL1/
    read-seam = CUT-HONEST (temp plane-6 ships, c-exec-007 cancelled, owner-acked); (1) solver = PARTIAL — §7-#2
    battery invariants asserted only at 1–8 sectors, at ~3,136 only timing (1.06ms≤8, emitter-computed not gated)
    + structure + the ANALYTICAL BS1 certificate (CR3 float-negative is non-vacuous); (3) real-DA+hundreds-of-rooms+
    breach+CR2 = PARTIAL (2nd skeptic confirmed) — NEVER united in one run: real DA(SGF)=6 sectors (t-4, no replication,
    owner-eye) vs hundreds-of-rooms+CR2-across-breach=SYNTHETIC t-2; real breach+CR2 never on the real-DA level;
    (6) internal render-proof = PARTIAL (2nd skeptic confirmed) — met only vs the owner-LOWERED bar (glaz-only, RN2
    cut d-rn2cut-001) + 2 owner-acked deviations + 1 caveated sign-off; the load-bearing SnapGridFlowRoomReader is in
    Assets/ (no csproj/slnx), 0 headless tests, mutation scope = CoarseFillProjection only → gate STRUCTURALLY can't
    cover the reader; (7) scale-arith = PARTIAL — keyframe-inclusive basis ✓ + named assumptions ✓ + ~×3 clamp
    headroom ✓, but ">=2 independent recomputes" holds only for MEMORY (two trivially-equal forms), bandwidth gets one,
    clamp rests on a more-generous keyframe cadence per-cell. GATE-HONESTY CORRECTION (applied below): NOW.md had
    rounded "dotnet test 431/431" up to "-Deliver GREEN incl coverage/spec-silence" 3× — I re-ran the gate FIRST-HAND
    (main a89b36b clean → 431/431 GREEN) and confirmed the full -Deliver strong-checks were NEVER run (deviation-close,
    RESULT cut #5); mutation 78.12% = CoarseFillProjection-only + stale; SGF reader uncovered. FORECAST-SURPRISE =
    wrong-mechanism for "satisfaction" (transport+consistency proven ≠ feels resolved) + optimistic on "terminus =
    showable artifact" (re-scoped to non-showable internal proof). GAS-MODEL дорога A+ INDEPENDENTLY ADVERSARIALLY
    CONFIRMED (3 angles, code+math, NO dealbreaker; A+ strengthened on all axes; §K 9/11 claims code-grounded; B reopens
    the solved net-determinism problem); §G load-probes INCOMPLETE → +4 mandatory (two-machine awake-set/sleep
    determinism; resident-gas-damage RED; confirmed-colocation false-reaction; real-DA-at-hundreds-of-rooms) + split
    host-migration from the benign save/load cut. Node g-9c41 STAYS ACTIVE (multi-wave); NO active bet now (between
    waves) — the next bet AWAITS the owner road A+/B/C (rec A+) + tree-diff approval (see decision_inbox +
    d-review-treediff-001). 3 knowledge promotions written. Wave-2 history below kept verbatim (additive). → next.
    Wave 2 SHAPED + ACTIVE 2026-06-16 (shape s-shape-wave2, owner «го» — G6/G9). Consumes the VERIFIED §CONTRACTS
    (converge-verify PASSED CLEAN, c-converge-verify-002). Wave 1 CLOSED (review c-review-001, verdict MET — HOLD
    independently re-derived). Node g-9c41 stays ACTIVE (multi-wave). The build is separate executor legs in
    GasCoopGame (next = c-exec-005 on t-1).
    ✅ 2026-06-17 (s-work-007, applies c-exec-005 RESULT): t-1 band-solver kill-gate REBUILT under d-fillmodel-001
    (capacity-fill+overflow + per-band temperature) → VERDICT = PASS_WITH_NITS, owner-CONFIRMED (198/198, mutation
    76.76%, fresh-session G5 PASS, owner multi-quantity legibility PASS; Codex P1 cross-band buoyancy dispositioned
    = NO code change, d-crossband-inv-001). Merged dev→main + pushed (GasCoopGame build @a868270, RESULT @9e7dab9).
    t-1 CLOSED; the bet rolled to t-2.
    ✅ 2026-06-19 (s-work-009, applies c-exec-006 RESULT): t-2 CLOSED — real DA-shaped level + ONE controlled breach +
    per-room-capacity LIVENESS (d-roomfull-001) + per-layer coarse replication host+2c across the breach (CR1/CR2/CR3)
    + single field-sampling oracle (OR1/OR3) + clean 1-player parity; leg-8 owner-visible slice built-FOR-REAL +
    owner eyeball «работает». Gate GREEN 372/372, mutation 75.29%, fresh-session G5 clean. Home-side OpenSpec
    apply+archive DONE (canonical sim-core/spec.md +18 reqs grep-clean; folder archived). GasCoopGame main @0327b9f
    (build) + @ce79e10 (openspec close), UNPUSHED. FishNet UDP wire env-deferred (owner-run). The bet rolls to t-3
    (temperature-layer extensibility) ∥ t-4 (player-legible render terminus) — both unblocked by t-2.
    ✅ 2026-06-19 (s-work-010, owner present): owner chose C — t-3 ∥ t-4 run in PARALLEL (d-wave2-seq-001 answered; G1 = 2 active). Both
    executor legs FRAMED + adversarially hardened (wf wd3a59z47: 14 must-fixes folded) + OPENED: c-exec-007 (t-3, CORE+TEST temperature-layer
    extensibility) + c-exec-008 (t-4, render terminus + REAL Dungeon Architect; owner R1 wire-real-DA / R2 guide-loop-when-no-MCP / R3
    owner-run=close-gate). Each opens with a PLAN (owner present). Parallel-safe: t-4 reads the FROZEN IGasReadModel/RN1 read-model (never
    reaches below it), t-3 EXTENDS the read seam additively (never changes ConcentrationAt); file-ownership split (t-3 = Core/** + tests, edits
    no scene/MonoBehaviour; t-4 owns *.unity + a NEW render scene, never co-edits GasDebugCoarseScene). Build = two separate legs in GasCoopGame.
    🔧 2026-06-19 (s-work-011): TWO Codex reviews (correctness + structural) triaged → review-driven CONSOLIDATION+HARDENING leg c-exec-009
    (t-5) FRAMED + red-teamed (wf_619b23cd, SOUND-WITH-FIXES, 6 gaps folded), owner «го». Surfaced previously-SHADOW dev work: dev advanced
    UNPUSHED past 7987506 to 3be28df (4 tooling commits) + an uncommitted ADR-0008 replication-seam→Core move (read-only headless gate GREEN:
    build 0/0, 372/372, hygiene OK — coherent, KEEP, no revert). Triage of ~16 findings: 3 confirm-only (P0 STALE=all leg-8 artifacts exist +
    c-exec-006 archived; MCP-strip already durable @e58a33d; ADR-0008 move=keep), 3 fix-now THROUGH the contour (FieldDelta validate-before-mutate;
    chunk apply-before-advance; StableId→Core+conformance — all no-silent-state-corruption), 5 NAMED owner-ack deferrals, rest hygiene. SEQUENCING:
    c-exec-009 LEADS; t-4 (c-exec-008, render) CONTINUES ∥ (untouched by both reviews); t-3 (c-exec-007) HELD pending the clean baseline (shares the
    Core/Field + Coarse/Replication seam the ADR-0008 move + the 3 fixes touch). The handed CALL («pick t-3/t-4 sequencing») was STALE (predated
    s-work-010, which already answered C + opened both legs) — re-verified committed state, not re-litigated. 2 owner-gated blockers stay
    (owner-run Unity PlayMode re-run via MCP; real-UDP FishNet env-blocked).
    ✅ 2026-06-19 (s-work-012, applies c-exec-009 + c-exec-010 RESULTs): t-5 consolidation+hardening CLOSED. ONE clean
    gate-green dev baseline at GasCoopGame dev tip cb73e82 — ADR-0008 seam→Core consolidated (GUIDs preserved) + 3
    no-silent-corruption fixes THROUGH the contour (FieldDelta validate-before-mutate; chunk apply-before-advance;
    StableId→Core) + a TopologyConformance derive-mismatch admission gate (Part B = c-exec-010). Re-derived FIRST-HAND
    (wf_a94b5ed9, NOT trusted): check.ps1 -Deliver GREEN on a CLEAN tree (402/402; mutation 93.06/82.5/86.67/90.07 all
    ≥70; deliverable-coverage disposed); R13/R14 + LOCKed codec/barrier/hash byte-identical proven; fresh-session G5
    COULD-NOT-REFUTE; 2 owner-gated blockers named-not-resolved. The clean baseline UNBLOCKS t-3 (c-exec-007 UNHELD) →
    the bet now runs t-3 ∥ t-4 in PARALLEL. NEW forward-constraint to t-4: the real Dungeon Architect MUST route through
    SceneTopologyComposer.Compose (geometry-derived ids) — a non-geometry StableId is now REJECTED at the Core boundary.
    ✂️ 2026-06-19 (s-work-013, owner «C», d-t3-defer-001): t-3/XL2 CUT from Wave 2 (owner-approved scope cut). The t-3
    builder PLAN surfaced a CALL-vs-ADR fork; reconciled first-hand — the ADR-0005/0007 "temperature as a SEPARATE
    registered layer = the t-3 obligation" wording is STALE (superseded by converge-verify F2 + d-tempfeedback-001:
    XL2 = a NEW demonstrative layer byte-identical = what the CALL implemented; DECOUPLING temperature so gas reads it
    back = the deferred temperature→gas FEEDBACK, which reopens the LOCK via a 1-tick read-seam lag on the band-split).
    The demo proof was contrived; owner chose to DEFER → Wave 3 proves extensibility FOR-REAL with the first genuine 2nd
    layer (the temperature decouple + feedback, g-d3a8). t-2 already ships temperature as a replicated plane-6, so nothing
    is lost. Wave 2 now runs the SINGLE leg t-4 (c-exec-008); t-3 → dropped, c-exec-007 → cancelled. Correct the stale
    ADR wording home-side.
    ✂️ 2026-06-19 (s-work-014, owner steer): t-4 RE-SCOPED to an INTERNAL coarse-sim PROOF (inspectable visualization on a
    real DA level), NOT a player-legible/Steam-showable terminus — owner: «грубую симуляцию на витрину не вешаю; для меня
    как доказательство окей; выкинь Steam-требование, вначале базовый функционал». The 08-31/Steam linkage is DROPPED (it
    was already de-coupled by the marketing q-foundation; Steam-page timing → g-2f8c, gated on real visuals/gameplay). The
    serious TEST/AUTHORING HARNESS (sandbox) is pulled OUT of t-4 (owner: t-4 context too full; cramming it in was a bad
    idea) and registered as a SEPARATE post-wave-2 deliverable (d-sandbox-001) — built via research(best-practices)→shape,
    HOW delegated to me, anti-scene-proliferation. So Wave 2 = t-1/t-2/t-5 done + t-4 (PROOF) → close → review → Wave 3
    (fine tier + real extensibility + the harness). c-exec-008 must be RE-ISSUED to the proof scope.
    ✅ 2026-06-20 (s-work-016, applies the c-exec-011 RESULT — builder→planner handoff): t-4 DELIVERED + CLOSED as an INTERNAL
    coarse-sim PROOF. Coarse gas renders READABLY on a REAL DA level via SnapGridFlow (SnapGridFlowRoomReader → DaTopologyProducer
    → SceneTopologyComposer.Compose → CoarseSectorGraph.FromTopology conformance gate → CoarseFillProjection → heavy-low/light-high
    slabs); reads the FROZEN RN1; geometry-derived StableId + 2 distinct conformant ProfileHashes (the c-exec-010 derive-id gate
    HELD). GasCoopGame headless `dotnet test` 431/431 GREEN [⚠ REVIEW s-review-002 CORRECTION: full `-Deliver` strong-checks NOT run — deviation-close per RESULT cut #5; mutation 78.12% = CoarseFillProjection-only + stale; SGF reader uncovered]; dev 27ab14e → main
    a89b36b (--no-ff), PUSHED origin/main+dev (the owner-gated push is DONE; the t-5-era "dev UNPUSHED" residual is CLEARED). Owner
    signed LOOK L1-L3 WITH A CAVEAT (basic works + observable; NOT "model final / all understood"). DRIFT RECONCILED: c-exec-008
    (NEEDS RE-ISSUE) was re-issued as c-exec-011 (proof scope) in a session never recorded in OS state → reconstructed from the
    builder RESULT, logged transparently, NOT invented (c-exec-008 → superseded; c-exec-011 → done). TWO owner-acked builder
    DEVIATIONS (acceptance criteria untouched by design — "билдер критерии приёмки не правит"): d-grid-sgf-001 (Grid→SnapGridFlow,
    owner-ack 2026-06-20, ADR-0009 home-side; "real DA" met IN FACT, R1 TEXT stale → home-side re-spec R1 + openspec apply/archive
    OWED) + d-rn2cut-001 (RN2 machine-vision floor CUT, owner-ack esc-t4-rn2-cut-2026-06-19; readability = owner-EYE, overrides the
    frozen dual-gate + R3). NEW owner-raised decision AFTER seeing the render: d-gasmodel-redesign-001 (OPEN) — a continuous-weight /
    gas-as-SPACE / free-gas-count / no-capacity-crutch gas-MODEL redesign = a CORE redesign reopening the LOCK (ADR-0004/0005) → a
    SEPARATE planning leg + ADR, NOT a t-4 change (t-4 rendered the EXISTING model HONESTLY; the proof did its job = it informed the
    owner). t-4 was the SOLE remaining Wave-2 leg → next = a FRESH REVIEW session for g-9c41 (G5).
  appetite: |
    Wave A appetite = ~2 focused weeks; KILL checkpoint 2026-07-05 (the DE-RISK WALL — if the §G+4 probes can't be made
    green / a core blind spot is real, STOP + re-shape the affected layer; G3 — never extend a bet, re-shape instead).
    HONEST re-frame (owner underestimates eng size; A+ is multi-wave): g-9c41 is now the FULL дорога-A+ core = MULTI-WAVE.
    2026-07-24 is a MILESTONE TARGET for Waves A→B (lab + de-risk + «where is the gas»), NOT all of A+ — the tail (C/D)
    extends PAST it (move the tail, not the wall). Track V (visual) runs ∥ to reach a showable state near the deadline.
    Each wave = its own shaped bet.
  approach: |
    ⛔ 2026-06-22 SUPERSEDED → SLICE METHODOLOGY + locked architecture (input-lockstep; grid+face-flow near / graph-rollup far;
    detail = local non-authoritative refinement of coarse-authoritative truth; per-mechanic depth at each slice PLAN). Entry =
    work/dev-plan-graph-2026-06-22.md. The дорога-A+ text below is HISTORY.
    дорога A+ (graph-base «вода» + grown layers) — owner-ratified at review s-review-002, independently adversarially
    confirmed (no dealbreaker; A+ strengthened on all axes; §K 9/11 code-grounded; B reopens the solved net-determinism
    problem). METHOD = KEEP the proven-expensive core, GROW additive on it, REWRITE-clean ABOVE it (owner: throw out,
    don't drag a tail). Wave A DE-RISKS BEFORE features: (1) build the test LAB (sandbox v1 — scenario-as-DATA over the
    EXISTING GasViewDirector harness: load any level via the SGF seam, spawn gas anywhere/any amount, pause/step,
    snapshot→structured-log for Claude, MCP-read or inspector-driven); (2) run the §G(+4) PROBE-GATE = the kill-gate
    (build MINIMAL geodesic front + ceiling/round-robin ONLY to PROVE their determinism; reuse the existing
    host+2-follower / mass / scale / breach harnesses); (3) SPIKE host-migration to veto bad authority assumptions early.
    Lock the keep-open seams as DATA before any feature welds them shut (per-species-temp reserved before the wire-cap
    number; coarse data-shape carries transient+source-XY before the front; migration verdict gates interest/visibility).
    Basis: work/aplus-breakdown-v1.md (DAG + wave cards + Wave-A detail + 2-critic hardening) + work/aplus-wave-map-v1.md
    (completeness-swept coverage) + gas-model doc §K/§G/§H. KEEP core proven by t-1/t-2/t-5 (NOT t-4, the deviation-close).
  done_when: |
    ⛔ 2026-06-22 SUPERSEDED → the active bet is now S0 (foundation slice); see active_tasks S0 + NOW.next + work/dev-plan-graph-2026-06-22.md.
    Each slice's done_when carries a VISIBLE owner-eye result. The Wave-A text below is HISTORY.
    Wave A is DONE when the LAB exists and the DE-RISK WALL is signed (binding = an independent fresh-session G5
    refutation of the probe scorecard):
    (1) SANDBOX v1: owner opens ONE harness scene, picks a saved scenario from DATA (a seed/config asset, NOT
        hand-edited), presses Play → the level builds (in-code OR a real SGF seed), coarse gas spawns where set,
        pause/step/tick-rate work, a data SNAPSHOT dumps a structured log Claude can read; most functions Claude-drivable
        OR owner-inspector-driven (the MCP-adapted scene is DESIRABLE-not-required); anti-scene-sprawl convention
        (config-as-data, not scene-per-test).
    (2) §G(+4) PROBE-GATE green/measured (the kill-gate), each a RED test or measured probe against the REAL kept core:
        cascade depth-identical on 2 (loopback) machines; 8-hot-bubble round-robin under a per-tick cell CEILING; integer
        incremental Dijkstra on a breach; mass-conservation RED (incl. a MOVING-GEOMETRY probe — a door closing on a gas
        column conserves mass); awake-set/sleep DETERMINISM byte-identical on 2 machines UNDER A SPIKE; resident-gas-damage
        RED (dose only from RESIDENT gas); confirmed-colocation false-reaction (coarse-alone emits NO false reaction);
        real-DA(SGF) at HUNDREDS of rooms; high-hall slab-count by eye + no-pop crossfade via the GasDebug overlay.
    (3) the active-gas CAP + wire-plane budget is a CONCRETE NUMBER (per-room ~4, per-level ~16/max~32, TUNABLE, sparse
        encoding) — decided WITH a per-species-temperature plane RESERVED (a new plane = a SURFACED LOCK-EXT, ADR-0007;
        never silent). Catalog of TYPES stays unlimited; per-room overflow → a reaction QUEUE (RISK R-GASCOUNT-PERROOM).
    (4) the coarse-layer DATA SHAPE is decided to carry the TRANSIENT + front + source-XY (TopologyAnchor populated), NOT
        settled-only / room-totals (return-fidelity keep-open) — DECIDED BEFORE the front is built on it.
    (5) HOST-MIGRATION SPIKE verdict: a documented «host dies → session survives» feasibility verdict on the LOCKed
        stream + whether migration CONSTRAINS the authority/replication model — its verdict GATES the Wave-B
        interest-grain / visibility-as-truth design.
    KILL signal: a probe reveals a core blind spot that can't be cheaply fixed (determinism breaks under spike / front
    non-deterministic / mass not conserved / migration needs a different authority model) → STOP, re-shape that layer
    before any feature wave.
    NAMED-OPEN (carried, NOT built this wave): griefing primitives (§H, co-op design); coarse economy under many small
    sources (§H, twin of the rarity invariant); the full detail tier (Wave B); reactions/damage FEATURES (Wave C — Wave A
    uses RED-control stubs only).
  wave_plan: |   # SLICE METHODOLOGY 2026-06-22 (owner «да»); slices are TASKS not tree nodes; FULL graph + deps + index → work/dev-plan-graph-2026-06-22.md
    Wave 1 (NETWORK) + Wave 2 (REAL COARSE SIM + GENERATED LEVELS + INTERNAL PROOF) — DONE (review s-review-002). The proof
      generated the gas-model redesign → дорога A+ → now LOCKED into the architecture + slice methodology below.
    SLICE SPINE (small, VISIBLE, deterministic gas-GAMEPLAY slices; order = effect × foundation-dependency; per-mechanic depth
      classified at each slice's PLAN, default room-granular A — ведро-1/2/3):
      S0 ФУНДАМЕНТ+ОЩУЩЕНИЕ (ACTIVE) — вокселизатор (генератор-слепой ридер → грид с гранями + region_id) + грань-поток
         (наполнение комнаты) + §9-швы + дебаг-гизмо + integer/zero-float scan + loopback hash; owner-eye «весело ли». LEADS.
      S1 — выброс-при-спауне + выдавливание объектом/игроком.
      S2 — МУЛЬТИПЛЕЕР (lockstep): грубое даёт одинаковый хеш на 2 ПРОЦЕССАХ (loopback, ОДНА машина; integer cross-CPU = GIVEN, не доказываем; реальные 2 ПК = опциональный разовый прогон, НЕ гейт). Determinism by construction (integer-only + zero-float scan), NOT re-flux.
      S3 — высота/расслоение (near real-height; coarse = few vertical layers for height-routing).
      S4 — коарс-rollup + LOD без рывка (collapse/expand = discard-on-leave; graph-as-label live; no-pop owner-eye).
      S5 — базовый пролом (pre-declared face-flip).
      S6+ — из бэклога по эффекту×ведру: реакции (телеграф+бах=событие), импульс/раздвоение, ветер, температура, типы газа…
    ∥ ВИЗУАЛ (g-7e15) после S0 (read-seam), на фейк-данных; ∥ ЛОР (canon); ∥ DEVLOG (g-e6f2/g-2f8c) постит по видимым слайсам
      (owner брифует маркетинг-трек отдельной сессией). Prior Wave A/B/C/D text SUPERSEDED by this spine (kept in git history);
      §4.2 RISK-register R-* + §2 keep-open invariants still apply as a PLAN check-list. Each slice = its own fresh session.
  rules:   # owner voice, this session — duplicated here until the maintenance home exists
    - "R12: one player hosts; no dedicated server, ever (not researched — decided)."
    - "R13: sim core = pure C# library, zero Unity refs, builds/runs headless; Unity = render/input/transport adapters only (Burst/Jobs behind a seam the core never sees)."
    - "R14: networking is an edge wrapper, never woven into business logic; every scene/harness composes the core in one of 3 modes (pure-local / local host-loop / networked host+clients) chosen at the composition root (DI); test scenes pick the mode freely."
    - "vendor default = FishNet (Steam-only, free, GameObject-native, free Steam transport/relay); verified in t-1; fallback NGO/NfE via P6, no tree change. Gas rides OUR custom chunked-delta channel regardless of vendor."
    - "R5 (refined): special gases are field-transported by the same simulation, NOT agents/enemies, NOT self-directed; distinguished by params + visual + effects. AGENT_SUBSTRATE + velocity-intent removed from the concept."
    - "R15: layered gas params — shared parent params for ALL gases (density, per-cell packing, spread speed) + meta-gas group adds own params + own visual; specific gas = pure config; per-meta-gas visual defined once but procedurally generated from params (feeds g-7e15)."
  cut_list:
    fresh_cut_this_wave:   # Wave A (G6 — real cuts)
      - "full MCP-drive surface / a dedicated Unity-MCP scene for Claude -> DESIRABLE-not-required (owner R3); ship
         inspector-driven + Claude-reads-snapshots if a live drive surface is costly/hangs."
      - "the REAL detail tier -> Wave B; Wave A builds only a STUB readout to probe the crossfade (§G#7)."
      - "the REAL reactions + resident-damage FEATURES -> Wave C; Wave A uses RED-control STUBS only (prove the LAW /
         determinism, not the feature — the deliberate temptation-cut)."
      - "the sparse gas-encoding STORE rewrite -> Wave B / when a level authors > the cap; the LOCK-EXT cap NUMBER is
         decided NOW (done_when 3), the store rewrite waits."
      - "Odin live-table polish -> NOT gated on a paid asset (the file-recording path works without it)."
      - "pretty/stylized rendering in the lab -> Track V (the lab uses the existing crude slabs)."
      - "a bespoke scene per probe -> anti-sprawl convention (all probes ride the ONE lab via scenarios)."
    inherited_deferrals:   # already decided; restated, NOT this wave's sacrifice
      - "griefing primitives + coarse-economy-under-many-small-sources -> named-OPEN (§H); carried so they aren't lost, not built."
      - "PGG / room-interior population -> later, behind the SAME generator-agnostic seam."
      - "matchmaking / lobby + save/load -> none (ephemeral harness; deterministic seeds)."
      - "the full A+ feature waves (B/C/D) + Track V impl -> later bets; detailed when their turn comes (owner: by the doc)."
      - "spectacular clip -> stays g-7e15."
  lens_verdicts:   # Wave A sweep (G6 — per CHARTER lens)
    - "commercial/traction: Wave A produces NO showable artifact (de-risk + lab) — honest; storefront PARKED (owner R4). The lab IS the infra that later makes showable footage cheap+repeatable (snapshot→capture feeds g-2f8c/g-e6f2). pre-mortem #2 answered by the coming Wave-B «where is gas» visible result + Track V, NOT by Wave A."
    - "technical feasibility: THIS IS THE WAVE — the §G(+4) de-risk wall is the feasibility KILL-GATE; it turns the riskiest NEW A+ assumptions (front determinism, sleep/awake determinism under a SPIKE, mass-conservation incl. moving geometry, host-migration) into measured facts BEFORE any feature spend (owner R2/R8 = no core blind spot found late)."
    - "core gameplay depth: Wave A builds NO gameplay BY DESIGN — it is the de-risk foundation that makes depth (front/consequence) buildable WITHOUT a core blind spot. Named-not-claimed; depth starts Wave C."
    - "co-op-first: ADVANCED — the host-migration spike (t-3) directly de-risks the co-op value-prop KILLER (host death = 4-8 session death, §H); the awake-set determinism probe protects co-op consistency under load. First real co-op-survival work (relates to c-map-004)."
    - "scope/production: heavy ASSEMBLY of existing code (sandbox ~80% exists — GasViewDirector/SetSource/pause/JSON/MCP) + minimal new; aggressive cut list; A+ honestly sized MULTI-WAVE (07-24 = A→B milestone, not all of A+); each wave its own bet."
    - "audience workflow: the lab's snapshot→Claude + MCP path is reproducible-capture INFRA that later feeds the audience machine (g-e6f2) — but NO public artifact this wave (consistent with R4 storefront-parked)."
  kill_by:
    metric: |
      DE-RISK WALL kill-gate (scored against a default-FAIL ledger frozen before the probes, authored RED-first by an
      INDEPENDENT test-author): ALL §G(+4) probes PASS / measured-in-budget against the REAL kept core — cascade
      depth-identical on 2 machines; 8-bubble round-robin under the cell ceiling; integer Dijkstra on a breach;
      mass-conservation RED incl. a moving-geometry probe; awake-set/sleep DETERMINISM byte-identical on 2 machines
      UNDER A SPIKE (the binding probe — the riskiest assumption); resident-gas-damage RED; confirmed-colocation
      false-reaction; real-DA(SGF) at hundreds of rooms — AND the sandbox runs them reproducibly from saved scenarios.
    checkpoint_2026-07-05: "de-risk wall not greenable after reasonable iteration -> a core blind spot is real -> STOP + re-shape the affected layer (do NOT build features on it)."
    hard_2026-07-24: "MILESTONE target for Waves A→B (lab + de-risk + «where is gas»), NOT all of A+; the C/D tail extends past it (move the tail, not the wall)."
    next_if_true: "all probes green + the host-migration spike verdict in hand -> shape Wave B (where-is-the-gas), honoring the keep-open seams locked in Wave A (per-species-temp reserved; data-shape carries transient+source-XY; migration verdict gates interest/visibility)."
    next_if_false: |
      a probe reveals an unfixable-cheap core blind spot -> re-shape THAT layer before features (e.g. migration needs a
      different authority model -> redesign the authority seam before interest-grain). The lab + the other green probes
      are kept; only the failing layer re-shapes.
    evaluator: |
      Executor-heavy DE-RISK bet. BUILD = Opus 4.8/Claude Code in GasCoopGame; the §G(+4) probes are authored RED-first
      by an INDEPENDENT test-author from the breakdown's probe list (builder can't edit). Most de-risk legs REUSE existing
      harnesses (host+2-follower / mass / scale / breach). Binding verdict = an independent fresh-session G5 refutation of
      the probe scorecard. Rollback = the next_if_false re-shape above.
  early_finish: |
    Early finish = success (G3 — don't pad). If the de-risk wall is green before 2026-07-05, close Wave A + shape Wave B.
    Do NOT pull features forward into Wave A (the cut is deliberate — A only de-risks + builds the lab). <=3 active (G1).
  forecast: |
    Wave A is LOW-risk to DELIVER (the sandbox ~80% assembles existing code; the probes reuse proven harnesses) — but its
    PURPOSE is to SURFACE any core blind spot before feature spend. The de-risk VALUE is in what the probes FIND (esp. the
    sleep/awake determinism contract under a spike + whether host-migration constrains the authority model), not in «did A
    ship». Expected: most probes pass (the kept core is already bit-exact, proven t-1/t-2/t-5); the genuine unknowns are
    the awake-set determinism contract and the migration authority verdict.
  against: |
    The new mechanisms built minimally-to-probe (geodesic front, ceiling/round-robin/awake-set) could carry a determinism
    flaw the minimal version hides but the full Wave-B version exposes — mitigated by defining the determinism CONTRACT
    once (Wave A) so the Wave-B mechanism conforms. Host-migration is genuinely unsolved (zero code today); the spike may
    return «needs a different authority model» = a real constraint on the whole plan — but finding that NOW (cheap) is the
    point. The sandbox could balloon (scope) — held by the cut list (inspector-driven, no Odin, no per-probe scenes).

active_tasks:   # Wave-A task set (дорога A+, riskiest-first); G1 ≤3 active. Wave-1/2 tasks CLOSED → history/s-review-002.md + per-leg histories.
  - id: S0
    kind: executor (engineering, GasCoopGame) — FOUNDATION SLICE (leads; every later slice runs on it). SUPERSEDES Wave-A t-1/t-2/t-3.
    goal: |
      A test sandbox where the owner SEES a generated (DA) or hand-placed level become an integer 3D CELL GRID (per-FACE
      open/closed connectivity) and watches gas FILL A ROOM by face-flow — and renders the owner-eye verdict «точно + (early)
      весело». The generator-blind geometry reader (room = LABEL/partition; geometry-derived) is the voxelizer's input.
      Netcode-NEUTRAL (no lockstep wire / no broadcast — that is S2). FOUNDATION for every later slice.
    done_when: |
      OPENS WITH A PLAN (owner present) that INGESTS-AND-APPLIES work/dev-plan-graph-2026-06-22.md + the 4 decision docs
      (mandatory, applied not just cited) and CLASSIFIES this slice's mechanics ведро-1/2/3; §Re-sync GasCoopGame contract
      v7→v8 FIRST. (1) VOXELIZER over the proven generator-blind reader: a MARKER says WHAT (room/door); MEASUREMENTS +
      connectivity DERIVED from built geometry; voxelizes rooms+openings into an integer cell grid with PER-FACE open/closed
      (wall=closed face, doorway=open faces; doorway→open-faces = a pure canonical integer function, identical for a DA and a
      hand-placed level, covered by TopologyConformance). (2) FACE-FLOW: gas fills a room via integer face-flow — AREA emergent
      (open-face count), HEIGHT emergent (low door drains low cells), walls block. (3) SANDBOX (owner SEES): gizmos show
      level→grid(faces)+region_id; pause/slow/step; structured snapshot Claude reads; scenario-as-DATA. (4) §9 SEAMS as DATA
      day-one: per-face state primitive; SPARSE active-front flux-register per face; representation/resolution tags (both LOD
      axes); region_id in the checksum; collapse/expand interface (stub, identity now); checksum-covers-MEANING extended to
      face state + region_id. (5) DETERMINISM-BY-CONSTRUCTION (NOT a proof of the established integer-cross-CPU fact, NOT 2
      physical machines — owner has one; integer cross-CPU is GIVEN): integer-only authoritative path + a build-time ZERO-FLOAT
      scan ON ONE MACHINE (the actual cross-CPU guarantee, by construction); an OPTIONAL cheap 2-PROCESS loopback hash (one
      machine) as an ordering/RNG tripwire whose real home is S2 — NO real 2 machines in S0. (6) ZERO-LEGACY: DELETE SnapGridFlowRoomReader +
      VScale + DA-internal-model reading from the TREE (kept in git). KEEP: TopologyDocument + TopologyConformance +
      geometry-derived id + RN1 + ROOM-partition (as LABEL) + RectDecomposition. OWNER-EYE gate (binding, non-unit-testable):
      owner opens the sandbox, sees level→grid + gas filling + signs «точно + весело» — owner-run, no self-marking.
      STOP-discipline v8: a blocked/infeasible named approach or a crutch = mandatory STOP + escalate, never a silent
      substitute. approach token = voxelizer-grid-faceflow-foundation + feel-grey-box + §9-seams + integer-deterministic-by-construction.
    status: done   # ✅ 2026-06-26 (s-work-019) — S0 DELIVERED as c-exec-014 (layered reshape; supersedes c-exec-013). GasCoopGame main @824948d (merge, pushed) — verified FIRST-HAND (merge + all named artifacts). tools/check.ps1 -Deliver GREEN (799 headless/0 failed, mutation 77.6% ≥70, zero-float scan over both grids, spec-silence, deliverable-coverage v8 9/9); ledger F0a–F12 + Fz/Fcarry/Fg/Fo closed; fresh-session G5 (Sonnet, different family) COULD-NOT-REFUTE on all 6 targets; determinism 5-vector audit SOUND; zero-legacy 3-lens re-audit CLEAN. «точно» = green suite («весело» owner-excluded as non-objective, esc-veselo-excluded-2026-06-26 — playable scenes kept for eyeball-correctness only). Roadmap steps 1–4 delivered incl. the HANGAR PROBE (#1 unmeasured number): 196,608 cells / 24.5 ms-avg-tick (65.5 max) strong-CPU / 1,562 active. Source-of-truth RESULT = GasCoopGame/RESULT.md → saved home history/s-work-019.md. SUPERSEDED t-1/t-2/t-3. The bet rolls to S1.
  - id: S1
    kind: executor (engineering, GasCoopGame) — FORCED-FLOW SLICE (impulse-events + directional bias: выброс + выдавливание + ветер as first cases). REFRAMED 2026-06-26 (s-work-020, owner «ок») from "выброс+выдавливание" per deep-research. Rolls on S0. Netcode-NEUTRAL (wire = S2).
    goal: |
      The first DYNAMIC, DIRECTABLE gas via ONE general primitive (deep-research "Forced-Flow Hybrid", adversarially
      verified — work/gas-richness-deep-research-2026-06-26.md): deterministic integer IMPULSE-EVENTS that write a
      DECAYING directional-bias register, applied on top of the existing S0 gradient face-flow. First cases the owner
      SEES: (a) ВЫБРОС — a source ejects gas with a directional kick, then settles; (b) ВЫДАВЛИВАНИЕ — a body zeroes its
      cells + emits a displacement impulse, gas shoved aside + flows around; (c) ВЕТЕР — a sustained directional impulse
      carries gas down a corridor and SPLITS it at a fork (directionality pure-diffusion S0 could not do) + a face-level
      one-way VALVE for designed permanent split. Stays INSIDE the LOCKED integer model — the bias is integer / in-checksum
      / decaying, NOT a stored velocity field. NO float/fixed-point velocity / advection (a RESERVED owner-gated upgrade
      tier that cracks the lock — a need for one = STOP-and-escalate). Carries d-overflow-guard-001 H1/H2.
    done_when: |
      OPENS WITH A PLAN (owner present): §Re-sync contract v8→current FIRST; ingest S0 + work/gas-richness-deep-research-
      2026-06-26.md + mechanic-lenses; classify ведро-1/2/3; set owner-expectation (cheap tier = wind + decaying gust +
      transient split + designed-valve split; TRUE inertia/free-vortices = reserved tiers). (0) STEP-0 DE-RISK SPIKE FIRST
      (a hard GATE — build nothing on a broken base; independent test-author): RED non-monotone settle oracle (wind-into-
      corner-and-back conserves mass + settles + does NOT oscillate; planted bad-bias RED control MUST fail) + SYMMETRIC
      integer decay rule + clamp×decay conservation + bounded-return-to-quiet cost assertion + 2-process loopback hash with
      bias in MeaningChecksum incl. CONCURRENT same-face writes (canonical order-independent rule) + owner-eye "alive on a
      forked corridor + vent". Not green → STOP-and-report. (1) ERUPTION + DISPLACEMENT RED suites (conservation;
      deterministic; eruption spreads-then-settles; displacement routes around body + body-leave returns to S0 equilibrium).
      (2) WIND + one-way VALVE (carries gas + splits at fork; valve = permanent no-rejoin where authored; deterministic).
      (3) LAWS in headless Core/**; bias FACE-LEVEL-UNIFORM only (§9.5 trip-wire — sub-face bitmap stays in StructureGrid;
      no structure-bitmap import). (4) H1 int*int guard + H2 spec amendment. (5) check.ps1 -Deliver GREEN (build + headless +
      zero-float scan + new int*int scan + mutation ≥70 on new Core + spec-silence incl. coord row + deliverable-coverage).
      (6) DETERMINISM by construction (integer-only; bias in checksum; zero-float scan spans new code; loopback hash green).
      (7) PLAYABLE SCENE (eyeball-correctness, NOT a gate): источник выстреливает+растекается; тело раздвигает газ+обтекание;
      вентиляция гонит+делит на развилке — «точно» = green suite; «весело» = owner's separate eyeball (esc-veselo-excluded).
      (8) ZERO-LEGACY. STOP-discipline v8 throughout (incl. any temptation to add a velocity field = STOP). Binding verify =
      a FRESH-SESSION G5 (different family) refuting determinism (bias/concurrent-write/decay seams) / conservation-under-
      forcing / contraction-returns-after-decay / no-silent-substitution / guard soundness / ledger honesty. Re-measure the
      active-set with the bias LIVE (forcing), not after a settle. approach token = impulse-event-decaying-directional-bias
      on the S0 face-flow law + step-0-spike-first + carried-overflow-hardening.
    status: done   # ✅ 2026-06-28 (s-work-023): S1 forced-flow slice CLOSED — scope S1a delivered via c-exec-015 (merged origin/main @0adae83, 970 green, -Deliver GREEN on dev, fresh-session G5 Sonnet COULD-NOT-REFUTE, Codex by-class CLEAN, owner-eye «работает»). Delivered the forced-flow PRIMITIVE: decaying directional-bias impulse-events on the S0 face-flow → jet-emitter (forward push + lateral confinement) + ВЫБРОС + ВЕТЕР/fork-split + one-way VALVE + ±1 bias-floor + ledger-honesty + one curated scene + class-wide int*int overflow scan — INSIDE the locked integer model (no stored velocity). S1b ВЫДАВЛИВАНИЕ split out + CUT to backlog (d-displacement-s1b-cut-001, owner «весь пакет»). Velocity TIER-3 reserved/trigger-ARMED (d-gas-richness-tiers-001); pressure = signal-on-demand (d-pressure-signal-on-demand-001); sparse = deferred-UNVALIDATED (d-sparse-solver-defer-001). Architecture fork (clouds vs lockstep) RESOLVED → lockstep stands (d-clouds-fork-resolved-001). The bet ROLLS to S2. Full RESULT → history/s-work-023.md.
  - id: S2
    kind: executor (engineering, GasCoopGame) — MULTIPLAYER LOCKSTEP LOOPBACK SLICE. Rolls on S0 (S1 present). The netcode determinism core the cheap whole model rides on. Netcode IS the slice (loopback, ONE machine — real 2 PCs never a gate). Per canon §5 S2.
    goal: |
      The coarse integer sim produces the SAME per-tick MeaningChecksum on 2 PROCESSES (host + 1
      follower, loopback, ONE machine — 2 PCs NOT needed; integer cross-CPU = GIVEN, not proven).
      Determinism BY CONSTRUCTION (integer-only authoritative path + build-time zero-float scan +
      single-owner-per-face + gather-then-apply + canonical traversal order + seeded RNG), NOT via
      re-flux. Load-bearing: the cheap detail/event model + S4 no-pop all ride on this. Fork resolved
      2026-06-28 — lockstep STANDS (no ADR-0010 un-lock), so S2 hardens the lockstep apparatus
      deliberately, not on a spine about to be discarded.
    done_when: |
      OPENS WITH A PLAN (owner present): §Re-sync GasCoopGame contract → current FIRST; ingest the
      canon SPEC §5/§Факт-1 + S0/S1 artifacts; classify this slice's mechanics ведро-1/2/3.
      (1) 2-process loopback hash harness: host + 1 in-process follower produce BYTE-IDENTICAL
      per-tick MeaningChecksum over a seeded run INCLUDING forced-flow (S1 bias/impulse) events +
      CONCURRENT same-face writes (canonical order rule). (2) The follower's checksum-of-MEANING
      mirrors the host (CoarseChunkFollower.ComputeHash parity — canon §8 warning, near-checksum
      reflected on the follower). (3) zero-float scan spans ALL new code; integer mass-clamp asserts
      (no silent wrap — canon Факт-1). (4) check.ps1 -Deliver GREEN + mutation ≥70 on new Core +
      spec-silence + deliverable-coverage. (5) ZERO-LEGACY. (6) STOP-discipline: any need for a stored
      velocity / float authoritative path / re-flux-as-gate = mandatory STOP-and-escalate. Binding
      verify = a FRESH-SESSION G5 (different family) refuting the determinism / canonical-order /
      hash-parity seams. Owner-eye = he sees 2 processes agree (confidence, NOT a gate; real 2 PCs =
      optional one-off run, never a gate). approach token = loopback-meaningchecksum-determinism-by-construction.
    status: done   # ✅ S2 SLICE COMPLETE 2026-06-29 (s-work-028): both halves DELIVERED + merged to GasCoopGame main — S2a @2e24a24 (ZERO-LEGACY retirement) + S2b @adb9255 (load-bearing lockstep loopback). Multiplayer-determinism FOUNDATION proven (2-process loopback, determinism by construction); networked-gas-ITickInputBus-citizen = named ~S4 seam (NOT done). Bet rolls to S3. — PLAN DONE + SPLIT 2026-06-28 (c-exec-016 PLAN, GasCoopGame_dev, owner present): done_when 1 (PLAN) met → concluded SPLIT-NEEDED per the CALL's budget clause; NO code/git changes (PLAN-only). Owner-signed «Split S2a+S2b» + 3 more decisions (d-s2-split-001 / d-s2-rng-control-na-001 / housekeeping FF+archive folded into S2a). Migration-spine port-vs-delete inventory done (7-agent wf_89e9d3c2, verified first-hand; owner-signed). Imported PLAN RESULT → history/c-exec-016-plan-split-2026-06-28.md (applied home s-work-025). S2 = S2a (legacy retirement, FIRST) + S2b (loopback load-bearing, after). Closes done only when BOTH return GREEN. next slice after S2 = S3.
  - id: S2a
    kind: executor (engineering, GasCoopGame) — ZERO-LEGACY RECONSTRUCTION-SPINE RETIREMENT (first half of the S2 split; runs FIRST → clean base for S2b). NO new behavior.
    goal: |
      The working tree is ZERO-LEGACY under input-lockstep (ADR-0010, Факт-6): the TWO pre-lockstep host-authoritative
      reconstruction families are DELETED (chunked-delta + field-state-channel, incl. the Факт-5 FieldSnapshot late-join
      path), the surviving store/reducer/far-tier/input-bus infra KEPT (with the lock-inverted «followers must not re-run»
      framing + Follower_OnlyMutatesViaApply guard pruned), and the ~25 affected suites REWRITTEN not dragged — all green,
      NO new behavior, NO new authoritative subtree.
    done_when: |
      OPENS WITH A PLAN (owner present): §Re-sync contract → current FIRST; the owner-signed c-exec-016 PLAN inventory
      INGESTED + RE-VERIFIED first-hand at the tip before any delete. (0) HOUSEKEEPING FIRST: FF dev up to main @eed321b
      (dev⊆main, clean --ff-only, before any new dev commit) + archive c-014/c-015 openspec folders. (1) DELETE both
      families (exact sets in c-exec-017-call.md; no surviving non-test consumer — grep-proven). (2) KEEP set intact+pruned
      (FieldState/ZoneRecord/FieldStep, CellHash, 2-band far-tier [retires at S4 not here], RevisionFeed/IGridEventBus,
      FishNetTickInputBus/TickInputBroadcasts). (3) TESTS rewritten not dragged (EncapsulationGuard whitelist; LayerRegistry
      oracle→FieldStep; DW9 coexistence EXTRACTED before delete; 4 surviving-invariant RED criteria green). (4) §7-burial
      re-check passes (no BandCount=2-as-authoritative-collapse coupling left). (5) check.ps1 -Deliver GREEN (no scan-root
      change — no new authoritative subtree). (6) ZERO-LEGACY 3-lens re-audit CLEAN (deleted-symbol grep = 0 non-test hits).
      (7) OWNER-EYE (confidence, not a gate): suite green on the retired tree. Binding = FRESH-SESSION G5 (different family)
      refuting the delete/keep boundary + tests-rewritten + §7-burial. STOP-discipline (a KEEP-member that breaks / a delete
      needing a behavior change / expanding into S2b loopback work / reopening ADR-0010 = STOP+escalate). FULL CALL →
      work/c-exec-017-call.md. approach token = zero-legacy-reconstruction-spine-retirement.
    status: done   # ✅ DELIVERED 2026-06-28 (c-exec-017 build session; applied s-work-026) — binding gates GREEN on GasCoopGame dev @ec54d4f (857/857 headless, -Deliver GREEN, mutation 87.96%, coverage 8/8, fresh-session G5 COULD-NOT-REFUTE on delete/keep + tests-rewritten + §7-burial). Both legacy families DELETED, verified FIRST-HAND (0 production hits). Retirement ADR = ADR-0016 (renumbered from 0015 vs c-visual-001 S5). ✅ merge dev→main + push DONE 2026-06-28 (owner) — main @2e24a24, VERIFIED first-hand (S2a commits in main, deleted families 0 prod hits on main, pushed; the real merge with visual S5 landed clean). Owner-eye (dotnet test 857, confidence not a gate) optional/pending. Record → history/c-exec-017-s2a-result-2026-06-28.md. Bet rolls to S2b.
  - id: S2b
    kind: executor (engineering, GasCoopGame) — LOCKSTEP LOOPBACK LOAD-BEARING (second half of the S2 split; runs AFTER S2a's clean base). The load-bearing determinism proof.
    goal: |
      On the clean post-S2a base, elevate the loopback determinism proof to LOAD-BEARING: a 2-endpoint (host + 1 in-process
      follower = a 2nd VoxelField re-running the SAME input stream, NOT the deleted CoarseChunkFollower) per-tick
      MeaningChecksum byte-identity over the FULL forced-flow scenario (S1 выброс/ветер/fork/valve/jet) + CONCURRENT
      same-face writes, with the RED controls + Adapters R14 3-mode owner-eye + a frozen spec. Genuine artifact to elevate =
      VoxelField.MeaningChecksum + the F11 two-endpoint re-run harness.
    done_when: |
      AUTHORED + (re-)hardened WHEN S2a returns clean (its base must exist first). Carries the load-bearing loopback content
      of c-exec-016 done_when 2/3/4 MINUS the RNG control (d-s2-rng-control-na-001 — no RNG on the gas authoritative path):
      2-endpoint loopback hash over the full forced-flow scenario; follower-parity (host VoxelField.MeaningChecksum ==
      follower's each tick); the RED controls (order-dependent write / silent wrap / awake-queue permutation /
      region-fold-order / per-meaning-field divergence); §9.5 in-checksum membership proof (3 named fields folded today;
      count-IN/bitmap-OUT negative control; not-yet-built §9.5 members spec-silenced); zero-float scan over new code; integer
      mass-clamp loud-asserts; G0-frozen openspec + frozen spec + ledger + mutation-<id>.json ≥70; -Deliver GREEN; Adapters
      R14 3-mode owner-eye (2 endpoints agree, confidence NOT a gate; real 2 PCs = optional one-off); fresh-session G5.
      STOP = stored velocity / float authoritative path / re-flux-as-gate / reopening the input-lockstep lock (ADR-0002 —
      see d-adr-lockstep-citation-001; the canon's "ADR-0010" is a citation error, ADR-0010 is the test-sandbox). approach
      token = loopback-meaningchecksum-load-bearing.
    status: done   # ✅ DELIVERED + MERGED + PUSHED 2026-06-29 (c-exec-018 build session; applied s-work-028) — GasCoopGame origin/main @adb9255 (--no-ff merge of dev). VERIFIED first-hand: the load-bearing 2-VoxelField loopback harness EXISTS (Core/Field/Determinism/ = LockstepLoopback + LockstepDivergenceException + MeaningMembers + GasScenario); ADR-0017; lock ADR-0002 intact (deleted families 0 prod hits). Gates: -Deliver GREEN, 923/923, mutation 73.51% ≥70, coverage 10/10, fresh-session G5 (Sonnet) COULD-NOT-REFUTE + 3 Codex rounds + 5-skeptic panel. SCOPE-HONESTY: proved determinism-by-construction in LOOPBACK (2 in-process VoxelFields, one machine); gas-as-networked-ITickInputBus-citizen = a larger seam deferred ~S4. Record → history/c-exec-018-s2b-result-2026-06-29.md. This CLOSES S2 (S2a+S2b).
  - id: S3
    kind: executor (engineering, GasCoopGame) — HEIGHT / LAYERING SLICE. Rolls on S0 (near real-height already emergent). The next slice after S2. Per canon §5 S3.
    goal: |
      Height/layering on the gas grid: NEAR real-height is ALREADY emergent from S0 (the 50cm Z-cells — «crouch under a
      layer» is free); this slice adds a few VERTICAL layers to the COARSE FAR-tier for height-ROUTING in player-LESS rooms.
      ⚠ These coarse vertical layers are a FAR-tier construct for distant rooms, NOT near-authoritative «crouch bands»
      (crouch is already free via S0 Z-cells; resurrecting authoritative height-bands is §7-buried). Netcode rides the S2
      loopback determinism (in-checksum).
    done_when: |
      OPENS WITH A PLAN (owner present): §Re-sync contract FIRST; ingest canon §5 S3 + §6 п.4 (far-rollup vertical-strata
      count — decided at PLAN S3/S4) + §7 (height-bands buried) + §8 (interim 2-band far-tier); classify ведро-1/2/3;
      RESOLVE the S3-vs-S4 far-tier sequencing (S3 adds far vertical layers; S4 = far-rollup + LOD — decide whether S3 lands
      on the interim 2-band far-tier or folds into S4). Then: the far-tier holds a TUNABLE in-checksum number of vertical
      strata for height-routing; near stays the S0 3D grid (unchanged); determinism preserved (loopback hash green; the new
      authoritative code inside BOTH zero-float/int-overflow scan roots — CLOSE the scan-root parity gap surfaced by S2b);
      -Deliver GREEN + mutation ≥70 + fresh-session G5; ZERO-LEGACY; owner-eye on height-routing. STOP-discipline (no
      authoritative near height-bands = §7 burial; lock = ADR-0002). approach token = far-tier-vertical-layers-for-height-routing.
    status: active   # NEW 2026-06-29 (s-work-028): S2 done → the bet rolls to S3. CALL NOT yet framed — the direction frames the S3 executor CALL next (PLAN-first, ведро; resolve S3-vs-S4 sequencing + fold the scan-root parity-gap hardening). Then a fresh GasCoopGame_dev session opens it with a PLAN (owner present). May fold into / sequence with S4 (PLAN decides).

recurring: []

parallel_tracks:   # active ALONGSIDE the g-9c41 bet at owner-set cadence (root map_order); NOT second BETS — no NOW.active_tasks, work via CALLs. G1 intact: one active bet (g-9c41) with its tasks; tracks add none.
  - id: g-7e15
    track: VISUAL (GASG — how the gas LOOKS)
    status: active   # owner-directed 2026-06-21 (s-visual-001) — parked→active PARALLEL track: «хочу чтобы оно участвовало в дереве … со своим аппетитом … не на задворках … начать сейчас». SECONDARY to g-9c41 (the primary bet). NB: the status enum has no distinct "track" value → recorded as active + reconciled here; friction captured for maintenance.
    appetite: ~40–60 min/day in the engine's build-gaps (≈3–5 h/week); revisit cadence at pulse. Checkpoint = the P1 prototype gives a min-spec perf signal on the riskiest unknown.
    approach: |
      READ-ONLY visual view over the authoritative gas grid (the sim simulates; the visual only READS RN1 + a front and
      renders — a read-only dashboard over a DB). Decoupled by the R13/R14 seam: develop on a FAKE/stub data source now,
      swap to the real Wave-B front later with ZERO visualizer change. Research-backed (work/gas-visual-research-2026-06-21.md,
      deep-research wf_e5924329, 24/25 claims verified): no single technique — LAYERED = (0) authoritative coarse grid [the
      engine] → (1) read-only GPU view: a custom URP ScriptableRendererFeature raymarch pass for the gas BODY and/or
      VFX-Graph particles fed by a GraphicsBuffer (SetGraphicsBuffer / Sample-Graphics-Buffer + Custom HLSL per gas type)
      for type-specific accents → (2) distinctiveness = gas as the dominant saturated colour + light in a desaturated world
      (the INSIDE «low-complexity, high-fidelity» lever). Off-the-shelf MOSTLY MISMATCHES (Zibra self-simulates;
      URP-Fog-Volumes is noise/shape-driven — neither ingests our authoritative grid) → custom-but-feasible, not a buy.
      Min-spec lever = half/quarter-res raymarch + depth-aware bilateral upsample. Unity 6.3 / URP 17 RenderGraph (port any
      pre-RG sample code).
    riskiest_unknown: |
      (a) min-spec perf of a grid-fed raymarch is UNPROVEN (one dev abandoned voxel raymarch for cost) → measure early (P4);
      (b) making MANY gas types readable at a glance without colour/motion collisions is a DESIGN unknown (no sourced answer);
      (c) GPU sync (compute finishes before the visual samples the buffer) + per-tick grid→GPU upload bandwidth.
    next: |
      LOOK-DEVELOPMENT phase (2026-06-28, s-visual-005 — track BROUGHT HOME from off-contour build; owner chose A +
      «добро»). The structure-first build-phase is DONE + DELIVERED (c-visual-001 foundation→S1→S3→S5, real data in
      motion, merged origin/main @9780713; S6 look-dev WIP on dev2 @dc4c225) — that phase is HISTORY (s-visual-002/003/004
      + work/c-visual-001-call.md + work/gas-visual-architecture-2026-06-26.md). The track now DEVELOPS THE LOOK (the
      «wow»), not the pipe.
      FELT TARGET (owner — the ориентир, references-for-a-feeling, NOT a spec): газ = СЕРДЦЕ/жемчужина игры → должен
      выглядеть ОСОБЕННО КРУТО / уникально; каждый ТИП имеет свой ХАРАКТЕР (шум/движение/свет, не только цвет),
      настраиваемый под своё состояние; low-poly = the WORLD, NOT a cap on the gas; commercial-clean (no NVIDIA Flow).
      WHY it FELT like «топчемся/блекло» (diagnosed): ~half = DRIFT (the build was invisible to the OS — now reconciled);
      ~half = only ~3 of ~10 look levers built + the BOX sandbox mis-leads the eye. NOT the ceiling.
      FORWARD PLAN (owner-endorsed; SOURCE OF TRUTH = GasCoopGame docs/gas-visual-stage-plan.md §S6+ — do NOT duplicate):
      (1) a dedicated GAS-LAB scene FIRST — gas as a FREE cloud in open space (no level walls) + good camera/light, so the
      box stops lying and the look develops cleanly (owner's idea; aligns with gas-is-open-space-first — gas spawns
      anywhere); (2) the P1 levers — bake a tiling 3D noise (inverted-Worley detail-volume) + smootherstep coord-warp
      (kills box-creases/lines) + detail-volume erosion + cheap STYLIZED lighting (two-tone ambient + scatter-GLOW = the
      «jelly» fix) + analytical transmittance (budget); (3) per-type CHARACTER as DATA (noise/motion/erosion/light profile
      — ⚠ frozen 96B GpuGasParams → reserved-fields or a layout-ADR) + OPTIONAL particle ACCENTS (owner owns «Feel» —
      check its VFX/feedbacks); gas-spread STAGES later still.
      PROCESS FIX (owner «добро» — the real ask; TRACK-LEVEL, not a kernel change): the visual track now runs with the
      ENGINE-track discipline — (a) every slice COMES HOME as a RESULT applied to OS state (end the drift; no off-contour
      merge invisible to governance); (b) each slice carries TWO owner-eye axes, not one — legibility AND «does it move
      toward the JEWEL target» (the missing aesthetic gate — why tech accreted while the look stalled).
      DECISIONS recorded (were off-contour): LOOK-FIRST then optimize (perf = orthogonal bolt-on, S4 deferred); raymarch =
      the SOLE body base (NO particle/VFX base — fill-rate-bound either way; accents optional/compute-gated later);
      per-cell warning granularity (ADR-0012 D5); 96B layout FROZEN; the 4 colour CONCEPTS = a start, NOT final (CHARACTER,
      not colour, is the lever). next = the GAS-LAB look-development leg c-visual-002 (open in a FRESH GasCoopGame_dev_2
      session, opens with a PLAN; spec = docs/gas-visual-stage-plan.md §S6+).
      AGREED STEP LADDER (owner-approved 2026-06-28, shown as a plain roadmap — gas-feature-first, NOT technique-first;
      each step SMALL, owner-eye-gated «ближе к жемчужине», comes HOME): 0 gas-lab (open-space cloud) → 1 cloud-at-rest
      reads as real gas (form/light) → 2 spawn/выброс → 3 jet/струя → 4 types (character, not colour) → 5 behaviour
      (reaction/telegraph/decay); LATER = particle accents (owner's «Feel» plugin) + min-spec perf. The P1 render levers
      are the TOOLBOX inside the steps, not the steps. WORKFLOW = identical to the engine legs (CALL → fresh dev2 session
      PLAN → render-only gates + owner-eye → RESULT home); the ONE legit difference is the binding gate (sim = objective
      headless tests; look = owner-eye, since «красиво» isn't unit-testable) → so a look leg is render-only-right-sized,
      no heavy adversarial hardening. STARTING 0+1 (owner «стартуем 0-1») → FRAMED as c-visual-002 (work/c-visual-002-call.md).
      VALIDATED 2026-06-29 (s-visual-007): owner challenged "did you just take their plan / verify it / improve it?" — an
      adversarial check vs the real dev2 code KEPT the spine (no re-spine; root cause = coarse grid + box-AABB clip, NOT a
      weak shader) but folded 3 owner-approved changes into the CALL — (a) lab shows gas IN MOTION not a frozen puff;
      (b) a SEPARATE UNCLIPPED test scene (owner-requested, no rectangle); (c) front-load an early TWO-TYPE-character probe
      (character is the headline, was deferred + globally-impossible today; cheap via reserved GasParams fields) + revisit
      the SKIPPED "unique" levers now toon is revoked. Perf flagged UNVERIFIED. The "0+1=small" framing was corrected (the
      leg is real work; may split at PLAN).
      R&D-CENTER TRIAGE 2026-06-29 (s-visual-008, owner-directed): triaged the read-only Gas-Visual R&D Center's Unity-6/
      URP/VFX-Graph note. LAYERING STRATEGY CONFIRMED (matches s-visual-007): BODY = GridView→GasUber raymarch (load-
      bearing; URP still has NO built-in volumetrics → custom justified, verified) | ACCENT = VFX Graph / Six-way (sparse,
      compute-gated, fallback=Particle System, reads visual data/events ONLY — NEVER gas-position authority) | CONTACT =
      URP decals on opaque | FINISH = fullscreen post. VERIFIED in repo: VFX Graph NOT installed (manifest); Particle
      System IS; the body injects BeforeRenderingPostProcessing + is transparent → decals/post/VFX do NOT auto-see it
      (need a mask/proxy). DECISIONS: (1) INSTALL VFX Graph (owner-directed) but as a SEPARATE compute-gated ACCENT leg
      AFTER the body checkpoint — NOT folded into the render-only c-visual-002 (a package install mid-build risks the
      running leg); (2) FEEL (owner owns, Pro) = the MOMENT/orchestration layer (triggers VFX bursts + post pulses +
      shake/sound on spawn/jet/reaction; FEEL=conductor, VFX=particles), NOT the body; (3) NO purchases now (body custom;
      accents/moments covered by VFX+Particle+FEEL); (4) Unity 6.3→6.5 upgrade DEFERRED (no gas-lab payoff; don't mix with
      a visual probe). The accent leg is REFRAMED (vs the R&D's generic-flair framing) as a per-type CHARACTER + spawn/jet
      MOMENT differentiator. Timing of the VFX-install/accent leg = after the c-visual-002 body checkpoint (owner to confirm).
      RENDER-VISIBILITY CORRECTION (Codex-sharpened, VERIFIED first-hand: GasUber.shader Blend One OneMinusSrcAlpha /
      ZWrite Off / ZTest Always / Queue Transparent; feature injects BeforeRenderingPostProcessing). My earlier "decals/
      post/VFX can't see the gas" was too broad. PRECISE: the gas is NOT in _CameraOpaqueTexture (snapshot before
      transparents) nor _CameraDepthTexture (ZWrite Off); URP decals can't project onto it; VFX URP Camera Buffer gets
      SCENE depth/color but NOT gas depth/mask → LOCALIZED "where-is-the-gas" effects + decals + depth-VFX adhesion need an
      explicit gas MASK/proxy/pass. BUT built-in fullscreen post AFTER our pass (Bloom / Color Grading) DOES affect the gas
      colour (already written to camera colour before post) → an emissive-rim → bloom works IMMEDIATELY, free (a real plus
      for the "finish"). ACCENT-LEG SEED (Codex, accepted): accents express (1) gas character by type, (2) state/moment
      beats, (3) player-readable events — toxic = corrosive rim/droplets/surface stains; heavy = downward soot/sparks +
      floor-hugging residue; energetic = electric tendrils + edge sparks; vent burst = pressure plume + leading nose;
      warning = rim pulse + sparse hazard particles; clearing/counter-gas = expanding clean hole + condensation edge.
      R&D QUEUE (narrow, LATER — broad landscape is DONE-enough): (1) gas-MASK/post integration (derive a mask from GasUber
      for localized fullscreen glow/distortion: alpha-reuse / extra RT / stencil / half-res mask / RenderGraph attachment);
      (2) which 6-8 character/moment accent MODULES the gas needs as a jewel.
      READ-ONLY R&D CENTER (2026-06-29, s-work-visual-rd-center-001, owner chose "Visual R&D Center"): Codex-side
      research lab exists at work/gas-visual-rd-center-2026-06-29.md. It studies technologies/references/probe briefs
      for the JEWEL target while Claude Code builds; it edits no product code and does not replace c-visual-002.
    note: |
      Engine spine (Wave A / c-exec-012) UNTOUCHED. FIŠKA «Живое Стекло» = already CUT by the owner today in the canon track
      (b274967 / s-repair-008) — NOT re-done here (concurrent-session state reconciled). The render code lives in GasCoopGame's
      render/adapter layer (R13 — never the gated Core), owner-EYE gated (you can't unit-test «looks good»).

open_calls:
  - id: c-exec-013
    status: superseded   # SUPERSEDED 2026-06-26 by c-exec-014 (R1-layered-reshape APPLIED, owner «да»). c-exec-013 was the gas-centric "one 50cm grid" S0; the layered reshape (Факт 2 re-shaped: coordinating grid + gas-50/structure-25/placement-25 layers + per-Z-band conductivity projection + marker-authoring + door-as-aperture) supersedes its READER contract. Its hardening CARRIES OVER into c-exec-014 (Core/** voxelizer, GAP sockets, owner-eye split, zero-float gate, STOP-v8). work/c-exec-013-call.md kept as history; reshaped CALL = work/c-exec-014-call.md (authored next from work/gas-engine-layered-reshape-R1-2026-06-26.md). — Prior: 2026-06-23 (s-work-018, work play) S0 FOUNDATION-SLICE CALL FRAMED + adversarially HARDENED (wf wwr2am1l9: 64 agents). Full prior CALL → work/c-exec-013-call.md.
    note: |
      Executor leg (GasCoopGame, dev→main when green) — the S0 foundation slice: a sandbox where a generated (DA) or hand-placed
      level becomes an integer 3D per-FACE cell grid + gas FILLS a room by face-flow, owner-eye «весело». §Re-sync repo contract
      v7→v8 FIRST → PLAN → RED-first independent test-author → build → -Deliver gate → fresh-session G5 → owner-eye. KEY hardening
      folded into work/c-exec-013-call.md: (1) voxelizer + doorway→open-faces MUST live in headless Core/** (closes the c-exec-012
      Adapters/** self-cert escape — the binding DA-vs-hand identical-voxelization RED test is authorable there); (2) gas=50cm-global
      + geometry=integer-multiple (2:1 mapping, REJECT 75) pinned; (3) 4 GAP sockets (cap/tick_divisor/void-sink/resolution_tag=PAIR)
      + §9.9 per-face attrs + {energy_sum,capacity_sum} temp-pair as day-one STUBBED DATA (a later field-add = a breaking
      checksum-schema migration); (4) face-flow law CONSUMES open-face area (R6: monotonic + slit-seeps + wall-zero); (5) zero-float
      scan WIRED as a real check.ps1 gate + a planted-float RED control; (6) checksum negative-controls per meaning-dimension;
      (7) owner-eye SPLIT — «точно» discharged by the green headless suite, «весело» the ONLY owner-run axis (kills self-certified
      approval). LEDGER corrected vs HEAD a89b36b: VScale = a const inside SnapGridFlowRoomReader.cs:76 (NOT a file);
      SnapGridFlowTopologySource.cs ADDED to the delete set (sole caller + DA-model read — else deletion orphans it + a scene
      missing-script GUID); shared DA→grid plumbing + far-tier TopologyPortalSpec explicitly KEPT. ChunkEncoder (byte)c overflow =
      OUT of S0 (S2 net) → named deferral. STOP-discipline v8: a blocked/infeasible named approach or a crutch (incl. reduced
      fidelity) = mandatory STOP + escalate, never a silent substitute. On GREEN → a fresh OS session applies the RESULT (S0 done +
      S1 CALL). next = c-exec-013 RETURN → S1 (выброс-при-спауне + выдавливание).
  - id: c-exec-014
    status: done   # ✅ DELIVERED + CLOSED 2026-06-26 (s-work-019): merged GasCoopGame main @824948d (pushed), -Deliver GREEN, mutation 77.6% ≥70, fresh-session G5 (Sonnet) COULD-NOT-REFUTE — verified first-hand (merge + artifacts). Source-of-truth RESULT = GasCoopGame/RESULT.md → history/s-work-019.md. Roadmap steps 1–4 incl. the HANGAR PROBE delivered. — was: NEW 2026-06-26 (R1-layered-reshape applied) — S0 FOUNDATION SLICE, LAYERED. Supersedes c-exec-013. CALL AUTHORED → work/c-exec-014-call.md (from R# §3); ready for a FRESH GasCoopGame_dev session. Contract: STRUCTURE layer reads DA geometry + module markers — geometric validated-vs-geometry / semantic owner-only; door = declared aperture validated vs mesh + per-Z-band conductivity projection; gas-50 + structure-25 grids w/ INVERTED resolution_tag; per-face/breach data-path + one-breach proof; sphere-cap of the off-checksum detail bubble; monotone-B predicate; settled_flag far-scoped). CARRIES OVER from c-exec-013: Core/** voxelizer + 4 GAP sockets + zero-float gate + owner-eye «точно/весело» split + STOP-v8 + the corrected keep/delete sets. Build runs in GasCoopGame_dev; build session reads CALL+PLAN by path; RESULT applied home by a separate OS writer.
    note: |
      The reshaped S0 (was c-exec-013). Owner-eye verdict unchanged («точно» = green headless suite, «весело» = owner-run).
      Owner-PLAYABLE per roadmap step (work/gas-engine-build-roadmap-2026-06-26.md): (1) reader→grid — SEE level + rooms + door
      apertures, no gas (closes the ORIGINAL door/«поразносить по типам» question); (2) gas fills a room by face-flow (crude
      slabs; emergent low-creep through the low door); (3) determinism + lockstep loopback; (4) a CLICKABLE Unity benchmark
      harness (active cells + frame-time) incl. the HANGAR PROBE — the #1 unmeasured number. ⚠ owner's machine (RTX 4090 + top
      AMD) is ABOVE average and gas-sim is CPU not GPU → measurements OPTIMISTIC; judge vs the weak-target budget (~200k-cell
      comfort ceiling on a weak core), NOT "smooth on my rig". FIRST build sub-task = hangar probe + the monotone-B oracle RED.
  - id: c-exec-015
    status: done   # ✅ DELIVERED + CLOSED 2026-06-28 (s-work-023): S1 scope S1a (forced-flow primitive) merged GasCoopGame origin/main @0adae83 (970 green); tools/check.ps1 -Deliver GREEN on dev; fresh-session G5 (Sonnet, different family) COULD-NOT-REFUTE; Codex by-class CLEAN; owner-eye «работает». Delivered: step-0 de-risk spike + D1 jet-emitter (forward push + lateral confinement) + ERUPTION (RW6) + WIND/fork-split (RW7) + one-way VALVE (RW8, new ValveSpec + 4-arg Voxelize) + D2 ±1 bias-floor (RW10) + D3 RW3-atomicity ledger-honesty + D4 one curated scene + H1 class-wide int*int overflow scan (closes the T6 recurring class). Latent c-014 adapter Rebuild bug (SeedMass>MaxCellMass under forcing) found+fixed this slice. Source RESULT = GasCoopGame/RESULT.md; spike docs/c-exec-015-spike-findings.md; capacity docs/research/capacity-pressure-2026-06-27.md; active-set docs/measurements/c-exec-015-active-set-under-forcing.md → saved home history/s-work-023.md. S1b ВЫДАВЛИВАНИЕ split out + CUT (d-displacement-s1b-cut-001). The 2 STEP-0 Codex P2s (d-bias-quantum-001 ±1 floor / d-rw3-step-atomicity-ledger-001) shipped as RW10/RW3. — was: IN FLIGHT (STEP-0 spike, dev), reframed 2026-06-26 (s-work-020, owner «ок») to the FORCED-FLOW primitive; CALL work/c-exec-015-call.md.
    note: |
      Executor leg (GasCoopGame, dev→main when green). GOAL: the first DYNAMIC, DIRECTABLE gas via ONE general primitive —
      deterministic integer IMPULSE-EVENTS write a DECAYING directional-bias register, applied on top of the S0 gradient
      face-flow. First cases owner SEES: ВЫБРОС (source kick), ВЫДАВЛИВАНИЕ (body shove), ВЕТЕР (sustained impulse carries
      gas + splits at a fork) + a face-level one-way VALVE (designed permanent split). Bias = integer/in-checksum/decaying,
      NOT a stored velocity field. STAYS INSIDE the lock — NO float/fixed-point velocity/advection (a RESERVED owner-gated
      tier that cracks the lock; a need for one = STOP-and-escalate). STEP-0 DE-RISK SPIKE is a HARD GATE FIRST: RED
      non-monotone settle oracle (conserve+settle+no-oscillate; planted bad-bias control MUST fail) + symmetric integer
      decay + clamp×decay conservation + bounded-return-to-quiet + 2-process loopback hash incl. CONCURRENT same-face
      writes (canonical order rule) + owner-eye on a forked corridor+vent. Not green → STOP. The 4 verified corrections are
      folded (§9.5 trip-wire = bias FACE-LEVEL-UNIFORM, no structure-bitmap import; symmetric decay; contraction SUSPENDED-
      not-preserved → the oracle gates it; active-set inflation → re-measure under FORCING). BOUNDARIES: no wire (S2); no
      reactions (S6); no big-hall/far-LOD (d-sparse-solver-defer-001); vortices → cosmetic g-7e15 layer fed the bias field
      ONLY; laws in headless Core/**. CARRIED: H1 int*int guard + H2 spec amendment (d-overflow-guard-001). DISCIPLINE:
      RED-first independent test-author; -Deliver GREEN; mutation ≥70; fresh-session G5 (different family) COULD-NOT-REFUTE;
      STOP-v8. «точно» = green suite; «весело» = owner eyeball (not a gate). May SPLIT (PLAN scopes; step-0 spike + eruption
      is a legit first return). next slice = S2. Reserved upgrade tiers = d-gas-richness-tiers-001. FULL CALL → work/c-exec-015-call.md.
  - id: c-exec-016
    status: split   # PLAN concluded SPLIT-NEEDED 2026-06-28 (s-work-025 applied the build-PLAN checkpoint; owner-signed «Split S2a+S2b») → c-exec-017 (S2a, runs first) + c-exec-018 (S2b, queued); imported PLAN RESULT → history/c-exec-016-plan-split-2026-06-28.md. — was FRAMED + adversarially HARDENED 2026-06-28 (s-work-024): S2 multiplayer-lockstep-loopback executor CALL authored → work/c-exec-016-call.md. Hardening wf_6a2fc85f-06e (32 agents, 8 adversarial lenses → per-finding refute-verify → synth; 22 raised → 12 survived → 2 must-fix + 5 should-fix folded; ZERO lock-change / ZERO re-design — the weak "approach-token"/"re-sync" parity findings refuted-out). Every symbol baked into the CALL VERIFIED first-hand in GasCoopGame (main tip eed321b): IFieldStateChannel-family + chunked-delta family (+ LoopbackCoarseChunkHub/ICoarseChunkLink) + F11LoopbackDeterminismTests + Core/Sim ADR-0002 decoy + RW5OrderIndependenceTests all exist. Ready: owner opens c-exec-016 in a FRESH GasCoopGame_dev session (opens with a PLAN, owner present, §Re-sync contract FIRST). RESULT applied home by a separate OS writer. May SPLIT (PLAN scopes).
    note: |
      Executor leg (GasCoopGame, dev→main when green) — S2 MULTIPLAYER LOCKSTEP LOOPBACK slice (canon §5 S2). GOAL: the
      coarse integer sim gives the SAME per-tick MeaningChecksum on 2 PROCESSES (host + 1 follower, loopback, ONE machine)
      over a SEEDED scenario EXERCISING the S1 forced-flow events (выброс/ветер/fork/valve/jet) + CONCURRENT same-face
      writes; determinism BY CONSTRUCTION (integer-only + zero-float scan + single-owner-per-face + gather-then-apply +
      canonical traversal order + seeded RNG + integer mass-clamp with loud asserts), NOT via re-flux, NOT 2 physical
      machines; a divergence HALTS LOUDLY. Fork RESOLVED (d-clouds-fork-resolved-001) so S2 hardens the lockstep apparatus
      deliberately. KEY framing: NOT a from-scratch build — S2 ELEVATES the loopback hash S0 seeded + S1 extended
      (F11LoopbackDeterminismTests) to load-bearing + reconciles the MIGRATION SPINE (canon §8:184/§7:162 — the Wave-1/2
      host-broadcast reconstruction = TWO legacy families: coarse chunked-delta + field-state-channel + the Факт-5-buried
      late-join/snapshot path; PLAN inventories-first, port-or-delete under ZERO-LEGACY; 2-band-as-authority resurrection
      guard). ВЕДРО: substrate → ведро-2 backbone (full §9.5 in-checksum set proven byte-identical); ведро-1 excluded
      (count-IN/bitmap-OUT trip-wire held); ведро-3 absent. BOUNDARIES: no 2 PCs (loopback only); no vendor/transport
      change (R14 edge, no UDP needed for the gate); no stored velocity/float authoritative path (d-gas-richness-tiers-001);
      no re-flux-as-gate (d-reflux-gate-001); no S3/S4/S5/S6; no big-hall/sparse (d-sparse-solver-defer-001). DISCIPLINE:
      RED-first independent test-author (planted RED controls: order-dependent write / mis-seeded RNG / silent wrap /
      awake-queue permutation / region-fold-order / per-meaning-field divergence); -Deliver GREEN; mutation ≥70;
      fresh-session G5 (different family) COULD-NOT-REFUTE; STOP-v8. «точно» = green suite; owner-eye (2 processes agree) =
      confidence NOT a gate. next slice = S3. FULL CALL → work/c-exec-016-call.md.
  - id: c-exec-017
    status: done   # ✅ DELIVERED + applied 2026-06-28 (s-work-026): binding gates GREEN on GasCoopGame dev @ec54d4f (857/857, -Deliver GREEN, mutation 87.96%, coverage 8/8, fresh-session G5 COULD-NOT-REFUTE); both legacy families DELETED, verified first-hand (0 prod hits); retirement ADR = ADR-0016; merge dev→main + push DONE 2026-06-28 (owner; main @2e24a24, verified first-hand). Record → history/c-exec-017-s2a-result-2026-06-28.md. — was AUTHORED 2026-06-28 (s-work-025): S2a ZERO-LEGACY reconstruction-spine RETIREMENT executor CALL → work/c-exec-017-call.md. Faithful transcription of the owner-signed + 7-agent-verified (wf_89e9d3c2) c-exec-016 PLAN inventory; NOT re-hardened by a fresh workflow (inventory already adversarially verified + owner-signed; the leg's own gates — re-verify first-hand before delete + ZERO-LEGACY 3-lens re-audit + fresh-session G5 — carry verification). Ready: owner opens c-exec-017 in a FRESH GasCoopGame_dev session (PLAN, owner present; §Re-sync + FF dev→main @eed321b + archive c-014/c-015 openspec FIRST). RESULT applied home by a separate OS writer.
    note: |
      Executor leg (GasCoopGame, dev→main when green) — S2a = the ZERO-LEGACY half of the S2 split, runs FIRST (clean base
      for S2b). GOAL: tree is ZERO-LEGACY under input-lockstep (Факт-6) — DELETE both pre-lockstep host-authoritative
      reconstruction families (chunked-delta: CoarseChunkFollower/ICoarseChunkLink/LoopbackCoarseChunkHub/FishNetChunkChannel/
      ChunkEncoder/ChunkDecoder/Chunk·ChunkBatch·ChunkCodecParams·ResolutionKey/RevisionBarrier; field-state-channel:
      IFieldStateChannel/InMemoryFieldStateChannel/FishNetFieldStateChannel·FieldStateBroadcasts/FieldSnapshot[Факт-5
      late-join]/FieldDelta/FieldStreamDriver·DesyncException/FieldHost/FieldHostFactory), KEEP store/reducer/far-tier/
      input-bus (FieldState/ZoneRecord/FieldStep [drop the «must-not-re-run» framing + Follower_OnlyMutatesViaApply guard
      the lock inverts], CellHash, 2-band far-tier [retires at S4], RevisionFeed/IGridEventBus, FishNetTickInputBus/
      TickInputBroadcasts), OUT-OF-SCOPE Core/Sim/* (ADR-0002 toy = separate ADR), REWRITE ~25 suites (not dragged, Факт-6).
      NO new behavior, NO new authoritative subtree. HOUSEKEEPING FIRST: FF dev→main @eed321b (dev⊆main, clean --ff-only,
      before any new dev commit) + archive c-014/c-015 openspec. DISCIPLINE: re-verify the inventory first-hand before any
      delete; -Deliver GREEN; ZERO-LEGACY 3-lens re-audit; fresh-session G5; STOP-discipline (KEEP-member breaks / delete
      needs behavior change / expanding into S2b loopback / reopening ADR-0010). FULL CALL → work/c-exec-017-call.md.
  - id: c-exec-018
    status: done   # ✅ DELIVERED + MERGED + PUSHED 2026-06-29 (s-work-028): GasCoopGame main @adb9255; load-bearing loopback harness verified first-hand (Core/Field/Determinism/); -Deliver GREEN, 923/923, mutation 73.51%, G5 COULD-NOT-REFUTE + Codex + 5-skeptic panel; lock ADR-0002 intact. Record → history/c-exec-018-s2b-result-2026-06-29.md. — was AUTHORED + adversarially HARDENED 2026-06-28 (s-work-027): S2b load-bearing lockstep-loopback executor CALL → work/c-exec-018-call.md. Hardening wf_e4074544-feb (28 agents, 6 lenses → refute-verify → synth; 16 raised → 10 survived → 1 must-fix + 6 should-fix folded, ZERO lock-change / ZERO re-design). Must-fix caught a real bug: a RED control aimed at an UNBUILT S4 region-rollup seam → re-scoped to spec-silence; + 3 stale canon line-cites (my own §1 ADR-edit shifted them +1) → name-anchored; + awake-queue/active-front contradiction, S5 boundary, bitmap trip-wire restored. Folds ADR-0002 lock (d-adr-lockstep-citation-001 — canon now corrected), RNG-control DROP (d-s2-rng-control-na-001), chunk-span S4-deferral. Ready: owner opens c-exec-018 in a FRESH GasCoopGame_dev session (PLAN, owner present, §Re-sync FIRST) on the clean post-S2a base (main @2e24a24). RESULT applied home by a separate OS writer.
    note: |
      Executor leg (GasCoopGame, dev→main when green) — S2b = the load-bearing half of the S2 split, on the clean post-S2a
      base. GOAL: elevate the loopback determinism proof to LOAD-BEARING — a 2-endpoint (host + 1 in-process follower = a
      2nd VoxelField re-running the SAME input stream, NOT the deleted CoarseChunkFollower) per-tick MeaningChecksum
      byte-identity over the FULL forced-flow scenario (выброс/ветер/fork/valve/jet) + CONCURRENT same-face writes, with the
      RED controls (order-dependent write / silent wrap / awake-queue permutation / region-fold-order / per-meaning-field
      divergence) + §9.5 in-checksum membership proof (3 fields folded today; count-IN/bitmap-OUT negative control; not-yet
      members spec-silenced) + zero-float scan + integer mass-clamp loud-asserts + G0-frozen openspec/spec/ledger/
      mutation≥70 + -Deliver GREEN + Adapters R14 3-mode owner-eye (2 endpoints agree; real 2 PCs = optional one-off) +
      fresh-session G5. Genuine artifact to elevate = VoxelField.MeaningChecksum + the F11 two-endpoint re-run harness.
      Carries the c-exec-016 done_when 2/3/4 content MINUS the RNG control. STOP = stored velocity / float authoritative
      path / re-flux-as-gate / reopening ADR-0010. Authored when c-exec-017 is GREEN.
  - id: c-visual-001
    status: delivered   # ✅ BROUGHT HOME 2026-06-28 (s-visual-005) — off-contour VISUAL-track drift reconciled first-hand. c-visual-001 was BUILT foundation→S1→S3→S5 and MERGED to GasCoopGame origin/main: S5 real-data swap @9780713 (verified ancestor of main tip 2e24a24). Evidence (GasCoopGame_dev_2/RESULT.md, read first-hand): -Deliver inner GREEN 1022/1022, mutation 76% ≥70, independent spec-only test-author (39 RED), 6-lens adversarial review, ZERO Core/** edit (977 sim tests unchanged), owner-eye SIGNED 2026-06-28 «облако читается хорошо, верится что это газ». ADRs 0012 seam / 0013 S1 / 0014 S3 / 0015 S5. S6 look-development = WIP checkpoint on dev2 @dc4c225 (pushed, NOT merged — look not locked; render-only, zero sim/layout change). The OS recorded this as "queued/not-started" for ~2 days across 3 owner-gated merges = the drift the owner flagged; now corrected. — was: queued (structure-first build-step 1, work/c-visual-001-call.md).
    note: |
      ✅ DELIVERED through S5 (real data in motion) — see the status comment + GasCoopGame docs/gas-visual-stage-plan.md.
      The track rolls to LOOK-DEVELOPMENT (gas-lab → P1 levers → per-type character; g-7e15.next). Original build-step-1
      scope kept below as history:
      Executor leg (GasCoopGame render/adapter layer — NOT the gated Core; dev→main when green). Build-step 1 of the
      structure-first gas-visual architecture (work/gas-visual-architecture-2026-06-26.md §7 step 1): a WORKING gas-visual
      on the HOME machine on FAKE data — a one-way read-only SEAM (IGasViewSource) filling TWO GPU resources (a per-cell
      GridView volume + a per-type GasParams GraphicsBuffer), a FakeGasViewSource, and ONE shared URP RenderGraph raymarch
      "body" pass styling each sample by GasParams[dominantTypeId] → a fake blob shows WHERE + HOW-MUCH + a visible edge.
      BINDING headless evidence = a STRIDE-CONFORMANCE gate (a declared expected-stride constant vs BOTH the C# blittable
      struct AND the documented HLSL layout) + a PASSING negative control + a headless data-path test; the SOLE owner-run
      axis = owner-EYE (he SEES the fake gas: color=type, denser=more opaque, a visible edge, and it changes when he
      changes a fake number). This leg FREEZES the final buffer layout (incl. the warning-granularity fork decision) so
      steps 4/6 fill it UNCHANGED. KEY BOUNDARIES (full set in the CALL): FAKE data only (RN1 unused — that's step 6);
      read-only is STRUCTURAL (no writable handle, references no engine types) + UPLOAD-ONLY (no readback into sim);
      struct defs on the render/adapter side, never Core; FIXED bounded region (scroll/clipmap DEFERRED to the perf pass);
      flat gradient edge (depth-composited full-res front DEFERRED to step 3); perf NON-gating (2 body knobs + a recorded
      home frame-cost number). Residual risks + left-to-PLAN items in work/c-visual-001-call.md. next = c-visual-002
      (build-step 2 — three gases from DATA + the forgot-to-register guard).
  - id: c-visual-002
    status: framed   # 2026-06-28 (s-visual-006) — gas-lab + cloud-at-rest look-development leg (step 0+1 of GasCoopGame docs/gas-visual-stage-plan.md §S6+), framed the SAME way as the engine legs (CALL → fresh dev2 session opens with a PLAN → render-only gates + owner-eye → RESULT home). Corrects an off-contour paste-prompt shortcut. RIGHT-SIZED: render-only look step, NO heavy adversarial hardening (nothing correctness-critical to refute); binding gate = owner-eye «ближе к жемчужине» + render-only regression invariants. FULL CALL → work/c-visual-002-call.md. VALIDATED + REVISED 2026-06-29 (s-visual-007): an adversarial check vs the REAL dev2 code (wf_de8a9945 — ground-truth + skeptical critique + refute referee) KEPT the plan spine (NO re-spine) but folded 3 changes + flagged perf UNVERIFIED. Verified root cause of «блекло» = coarse grid (5x16x5 / 3x3x4) + the HARD BOX-AABB rectangle clip (NOT a weak shader; GasUber already ~40 knobs). The 3 changes: (a) the lab shows gas IN MOTION (spawn/jet/creep), not a frozen puff; (b) a SEPARATE UNCLIPPED test scene (owner-requested — no rectangular cut); (c) front-load an early TWO-TYPE-character probe (two visibly-different gases on one screen via a RESERVED GasParams field — character is the owner's headline, was deferred to the finale + is globally-impossible today) + reconsider the SKIPPED "unique" levers (light-through-volume/emissive-cores/flow-anisotropy) now toon is revoked. NOT a "small" step (split allowed at PLAN). CALL rewritten.
    note: |
      Executor leg (GasCoopGame render/adapter layer — NOT the gated Core; dev2→main when green). REVISED scope (post-
      validation, s-visual-007 — NOT a "small" step): (0) a SEPARATE convenient gas-LAB scene in OPEN space where the gas
      is NEVER clipped into a rectangle (generous bounds + soft falloff, verify from multiple angles — the box-AABB clip
      is a code-confirmed root cause); (1) the gas shown IN CHARACTERISTIC MOTION (scripted spawn/jet/creep loop, NOT a
      frozen puff) reads as a real, especially-cool gas; (2) an EARLY TWO-TYPE-character probe — two visibly-different
      gases in the SAME volume at once, one per-type shape/motion lever driven from a RESERVED GasParams field (the buffer
      is already per-type for colour; 96B has reserved RiseSinkBias/Temperature/State…). Pick DIFFERENTIATING look levers
      (light-through-volume/emissive-cores/flow-anisotropy), not just safe polish (toon revoked). REUSE the delivered
      GasUber body + RealGasViewSource seam, don't rebuild. BOUNDARIES: render-only (zero Core/** edit, sim + 977 tests
      untouched); 96B layout frozen (reserved-field or layout-ADR decided in the PLAN); full per-type profiles + jet-shape
      system + behaviour + particle accents + the weak-HW PERF pass (perf is UNVERIFIED, not a free bolt-on) = LATER legs;
      STOP if the build reaches past the probe. GATES: -Deliver GREEN + render-only regression invariants = the «точно»
      half; OWNER-EYE «ближе к жемчужине» (gas in motion, two types differ, no rectangle) = the binding gate (owner-run,
      no self-marking, judged in motion). May SPLIT at the PLAN. Comes HOME as a RESULT. next = the next look slice.
  - id: c-exec-012
    status: superseded   # 2026-06-21 — RAN but SUPERSEDED: builder fabricated a blocker + substituted scene-tags + a VScale crutch + self-certified «(owner-approved)» (GasCoopGame_dev RESULT.md; leg 770da4a on dev — NOT merged to main). t-1 RE-OPENED on architecture (B), re-issued in NOW.next. Contour hardened v8 so this class bounces. (note below = the original/historical c-exec-012 scope.)
    note: |
      Executor leg (GasCoopGame, dev→main when green). GOAL: the test LAB (sandbox v1) — a data-driven Unity harness:
      open ONE scene, pick a saved scenario from a config/seed ASSET, Play → any level builds (in-code OR real SGF seed),
      spawn coarse gas anywhere/any amount, pause/step/tick-rate, snapshot→structured-log Claude reads; config-as-DATA +
      naming convention (anti-sprawl). Mostly ASSEMBLES existing code (GasViewDirector / SetSource / director coroutine /
      GasViewDebug JSON / runInBackground-MCP); the one NEW build = scenario-as-data + seed catalog. BOUNDARIES: sandbox
      ONLY (the §G probes + cap-number + data-shape + minimal front = t-2; features = later waves); reuse the harness (GROW,
      no rewrite); a Unity-MCP scene for Claude = DESIRABLE-not-required; honor keep-open seams (per-species-temp readable;
      data-shape can carry transient+source-XY); no LOCK reopen. OWNER-RUN gate: owner opens the lab + confirms it works
      (lab-works axis owner-run; build/existence closes headlessly; no self-marking). next = c-exec-013 (t-2 probe-gate).
      FULL CALL → NOW.next.
  - id: c-exec-009
    status: done   # 2026-06-19 (s-work-012) RETURNED GREEN + applied — -Deliver GREEN on a CLEAN tree (tip cb73e82, re-derived first-hand wf_a94b5ed9), all 3 change-ids + the spun-out Part B over floor, fresh-session G5 COULD-NOT-REFUTE. Part B (StableId conformance derive-mismatch) spun out as c-exec-010 (also closed). FRAMED + red-teamed (wf_619b23cd) 2026-06-19 (s-work-011). RESULT → GasCoopGame @8aee8a8 + history/s-work-012.md.
    note: |
      Executor leg (GasCoopGame, dev→main when green). GOAL: ONE clean, gate-green, owner-acked dev baseline that consolidates the in-flight
      ADR-0008 coarse-replication-seam→Core move + the 4 already-committed UNPUSHED tooling commits (dev @3be28df) into a coherent tip with
      nothing correct lost, fixes the 3 no-silent-state-corruption defects THROUGH the contour, batches hygiene, and carries every out-of-scope
      review finding as a NAMED owner-ack deferral. Triaged from TWO owner-pasted Codex reviews (correctness + structural). 3 CONFIRM-ONLY (P0
      stale = all leg-8 artifacts exist + c-exec-006 archived; MCP player-strip already durable @e58a33d; the ADR-0008 seam move = KEEP, confirm
      through the gate). 3 FIX-NOW (each red-test-first by an INDEPENDENT test-author, classified by the invariant, ENROLLED as a frozen change
      with its own mutation-<id>.json ≥ floor — no symptom band-aid): (1) FieldDelta.Apply validate-before-mutate; (2)
      RevisionBarrier/ChunkDecoder/CoarseChunkFollower apply-before-advance; (3) StableId derivation moved into Core/Field/Topology + a
      derive-mismatch check in TopologyConformance. HYGIENE batched: AGENTS.md Net-edge-root bless; GasDebug version-checked reflection bootstrap;
      LogAssert targeted-Expect; delete Assets/_Recovery (untracked on disk); git rm --cached GasCoopGame.slnx; swapped-assert fixes; hygiene.ps1
      flags runtime Assert.Ignore/Assume + _Recovery/_scratch_* dirs. CLOSE: check.ps1 -Deliver GREEN on a CLEAN tree (proves P0 was the dirty
      tree) + all 3 change-ids' mutation ≥ floor + deliverable-coverage v7 over ALL done_when + a FRESH-SESSION G5 refutation on the hardened tree +
      RESULT reconciled to truth. 5 NAMED owner-ack deferrals: untrusted-peer/PeerId-spoof; topology int-overflow on pathological volumes
      (TopologyDocument MaxX/Y/Z = Min+Extent-1 unchecked); broadcast-leak on reconnect; real-UDP FishNet env-blocked/owner-run (YELLOW-not-green
      reporting rider); headless CoarseReconstructionHarness.Follower 2nd-source-of-truth (Constitution-#3). 2 owner-gated blockers NOT
      self-resolved: (i) owner-run Unity compile + PlayMode CoarseVisibleSlice re-run via MCP (edge change under Net/, outside the headless csproj —
      not done until owner confirms); (ii) real-UDP FishNet deferred (WSAENOBUFS), loopback binding. Read-only headless gate on the dirty tree
      already GREEN (build 0/0, 372/372, hygiene OK). FULL CALL → history/s-work-011.md §c-exec-009.
  - id: c-exec-010
    status: done   # 2026-06-19 (s-work-012) RETURNED GREEN + applied — fix #3 Part B, spun out of c-exec-009: TopologyConformance.Check derive-mismatch admission gate (@300b812) REJECTS any TopologyDocument whose volume/portal/surface StableId ≠ derive(geometry); required an authorized test-migration (owner-ack owner-2026-06-19-option1) of synthetic-id builder-coverage tests to geometry-derived ids (suite 402/402). Independent test-author RED test (own spec-transcribed FNV oracle). Mutation 90.07% ≥70. Closing RESULT @cb73e82: fresh-session G5 COULD-NOT-REFUTE + -Deliver transcript (re-derived first-hand wf_a94b5ed9).
    note: |
      The deferred half of c-exec-009 fix #3 (StableId), run as its own leg because enabling the Core admission gate
      broke ~59 synthetic-id builder-coverage tests (needed an authorized test-migration). NEW FORWARD-CONSTRAINT for
      t-4 (c-exec-008): the real Dungeon Architect MUST emit plain logical geometry (RoomSpec/LinkSpec: absolute
      inclusive min/max AABB + archetype + link room-key pairs) and route THROUGH the unchanged SceneTopologyComposer.Compose,
      which derives every StableId from geometry — it must NOT construct TopologyVolume/Portal/Surface with DA's own
      GUIDs/names/instance-ids/emission-order as ids (a non-geometry id path is now REJECTED at the Core boundary;
      silent-pass is impossible). Add an explicit done_when sub-clause + an independent-author RED test feeding a
      DA-shaped doc with a hand-set id and asserting a 'derive-mismatch' reject. Also: ids are now globally unique-checked
      + absolute bounds non-overlap-checked, so the DA seed→geometry mapping must yield distinct, non-overlapping
      integer AABBs. RESULT → GasCoopGame @cb73e82 + history/s-work-012.md.
  - id: c-exec-007
    status: cancelled   # 2026-06-19 (s-work-013, owner «C», d-t3-defer-001) — t-3 CUT from Wave 2 → Wave 3; this leg is NOT run this wave (the XL2 demo proof was contrived; decoupling temperature is the deferred feedback, which reopens the LOCK). FRAMED + hardened (wf wd3a59z47) + OPENED 2026-06-19 (s-work-010), UNHELD s-work-012, now cancelled. The REAL extensibility leg gets re-framed in Wave 3 with the first genuine 2nd layer. FULL prior CALL → history/s-work-010.md §c-exec-007.
    note: |
      Executor leg (GasCoopGame, dev→main when green), opens with a PLAN (owner present). GOAL: a 3rd INDEPENDENT
      system-layer is networked-consistent at coarse scale alongside gas, having plugged in WITHOUT core edits — the
      extensibility seam EXERCISED, not argued. ADDITIVE on t-2 (coarse temperature plane 6 already shipped +
      replicated; it is a coupled plane of CoarseBandLayer, NOT a registered layer): t-3 ADDS (a) XL2 file-isolation
      proof — a NEW independent demonstrative layer EXISTS as new file(s) under Core/Field/Layers/ on a fresh LayerKey,
      registers via the LayerRegistry with git-diff-EMPTY on the registry + every sibling layer file (adds files, edits
      none; deliverable-coverage row = the new file PATH); gas-only run reproduces t-2 goldens byte-identical, gas+new
      run keeps gas Hash() byte-identical + RNG-conservation guard (new layer = zero gas RNG); barrier-table re-size
      SURFACED per the LOCK; (b) XL1 gas→temperature SINK via a non-vacuous suppressed-event NEGATIVE oracle; (c)
      §RESOLVED-4 grid-addressed read seam on a COMMITTED revision (+ live/wrong-revision read REJECTED); (d) regression:
      gas IGasReadModel.ConcentrationAt byte-identical to t-2 OR1/OR3 goldens + plane-6 replication stays GREEN.
      BOUNDARIES: no LOCK/C1-C22/BS1-BS15 re-open, all goldens byte-green; temperature stays a PURE SINK (feedback
      DEFERRED — read-back coupling escalates to owner); no per-species temperature; CORE+TEST only (NO *.unity / NO
      Adapters/GasDebug edits; any shared-core C# edit is t-3-OWNED, t-4 rebases); MUST NOT alter plane-6
      representation/layerKey/fold-order/read-model ctor (STOP-and-report — would couple into t-4). Discipline:
      independent test-author RED-first; check.ps1 -Deliver GREEN; mutation ≥70; binding = fresh-session G5.
      FULL CALL → history/s-work-010.md §c-exec-007.
  - id: c-exec-008
    status: superseded   # 2026-06-20 (s-work-016): RE-ISSUED as c-exec-011 (proof scope) and DELIVERED — the re-issue/PLAN session was never recorded in OS state (drift), reconstructed from the c-exec-011 builder RESULT (not invented). See c-exec-011 (done) below. Prior: 2026-06-19 (s-work-014) t-4 re-scoped to an INTERNAL coarse-sim PROOF / inspectable visualization (drop Steam/stylization/RN2-showable/footage; KEEP real DA via the derive-id gate + reads RN1 + owner-confirm). The Steam-terminus framing in the note below is SUPERSEDED — re-issue this CALL to the proof scope before building further. FRAMED + hardened (wf wd3a59z47) + OPENED 2026-06-19 (s-work-010) — was: Wave-2 t-4 render terminus + REAL Dungeon Architect, ∥ c-exec-007
    note: |
      Executor leg (GasCoopGame, dev→main when green), opens with a PLAN (owner present). GOAL: a player can SEE the
      real coarse sim — a room visibly fills bottom-up from the breach, heavier gas low, source identifiable, readable
      WITHOUT a debug overlay + as deliberate stylization not a stub — on a REAL Dungeon-Architect-generated level.
      Reads the FROZEN IGasReadModel/RN1 (SOLVER-AGNOSTIC; band OR degraded scalar) and reaches no lower; depends on
      t-2's level+breach+read-model, NOT on t-3. DONE_WHEN: crit-6 bottom-up-fill render; TWO acceptance gates —
      (a) MACHINE RN2 blind-check (PLAN freezes a ground-truth schema {gas-present / which-room-filling /
      from-breach-side / heavier-low} + a frozen N-of-M floor, scored from RN1, artifact docs/measurements/<call>-rn2-blind.json),
      (b) render-slice = ENGINE-class v7 existence row (committed Assets/** scene + docs/measurements/** capture the
      deliver check Test-Paths; never a sibling test name/stub — the leg-8 trap); BUILD precedes LOOK; no-shimmer-EVER
      across off-screen→on-screen surfacing (committed continuity test, GG4/OR4 «100%», continuity NOT monotonicity);
      solver-agnostic smoke vs BOTH band + scalar degrade. OWNER R1/R2/R3: R1 wire the REAL DA (real
      DungeonArchitectRoomReader behind the existing DaTopologyProducer/IN2 seam, tag prefabs, REMOVE FixedLevelRoomReader
      from runtime [grep=0 non-test], evidence = DA-output run-artifact, two seeds→two conforming ProfileHashes; in-code==DA
      test RETAINED but NON-SUFFICIENT for R1; GEOMETRY-MOVE RULE — a larger/different DA level = a t-3-coordinated
      barrier-table re-size with the artifact re-recorded, never a unilateral t-4 edit); R2 guide-loop (os/plays/guide.md)
      step-by-step Unity instructions for any non-MCP action + answer owner Qs (per-step owner confirmation IS the
      evidence; no batching / no self-marking; log to docs/FRICTION.md); R3 owner-confirmation close-gate (BUILD/existence
      closes headlessly; only the LOOK is owner-run; DONE-pending-owner-LOOK until owner confirms; env-deferral does NOT
      apply to the owner-eye axis). BOUNDARIES: reads RN1 only / no core edits / no ConcentrationAt change; t-4 OWNS *.unity
      + a NEW render scene (don't co-edit GasDebugCoarseScene/GasDebugDirector — fork-by-copy); EXCLUDE g-7e15 bars;
      COARSE-only (fine tier + coarse↔fine handoff + OR1 cross-tier = Wave 3); d-returnfidelity-001 mid-transient = NOT a
      t-4 bar; no LOCK re-open; >1 breach / population / late-join OUT. FULL CALL → history/s-work-010.md §c-exec-008.
  - id: c-exec-011
    status: done   # 2026-06-20 (s-work-016) RETURNED + applied (builder→planner handoff). t-4 INTERNAL coarse-sim PROOF DELIVERED on a REAL DA level via SnapGridFlow; GasCoopGame headless `dotnet test` 431/431 GREEN [⚠ REVIEW s-review-002 CORRECTION: full `-Deliver` strong-checks NOT run — deviation-close per RESULT cut #5; mutation 78.12% = CoarseFillProjection-only + stale; SGF reader uncovered]; dev 27ab14e→main a89b36b (--no-ff), PUSHED origin/main+dev (main tree == dev tree). Owner signed LOOK L1-L3 WITH a caveat (basic works + observable; NOT "model final / all understood"). RESULT → history/s-work-016.md + GasCoopGame RESULT.md/ADR-0009/openspec/changes/c-exec-011-t4-coarse-gas-render/ + docs/measurements/t-4-da-output.json + t-4-captures/t-4-sgf-render.png + t-4-owner-checklist.md.
    note: |
      The re-issue of c-exec-008 to the PROOF scope (s-work-014, d-sandbox-001). DRIFT: the re-issue/PLAN session that
      minted this id was never recorded in OS state — this entry is RECONSTRUCTED from the builder RESULT (not invented),
      logged transparently; c-exec-008 → superseded. SCOPE (proof): coarse gas renders READABLY on a real DA level + reads
      the FROZEN RN1 + owner confirms the sim is visibly correct; NOT a Steam/player-legible terminus. EVIDENCE chain:
      SnapGridFlowRoomReader → DaTopologyProducer → SceneTopologyComposer.Compose → CoarseSectorGraph.FromTopology
      (conformance gate) → CoarseFillProjection → heavy-low/light-high slabs; geometry-derived StableId + 2 distinct
      conformant ProfileHashes (the c-exec-010 derive-id gate HELD — real level, not a hand-set id).
      TWO owner-acked builder DEVIATIONS that the BUILDER deliberately did NOT reconcile (it does not edit acceptance
      criteria) — they need DIRECTION reconciliation, carried to the review:
        (1) d-grid-sgf-001 — Grid → SnapGridFlow pivot (owner-ack 2026-06-20). Spec/ADR R1 named "Grid"; owner chose SGF
            (designed modules + verticality). "real DA" met IN FACT; R1 TEXT still says "Grid" → home-side re-spec R1 +
            openspec apply/archive (of openspec/changes/c-exec-011-t4-coarse-gas-render/) OWED. ADR-0009 records D5=SGF + cuts.
        (2) d-rn2cut-001 — RN2 MACHINE-vision floor CUT (owner-ack esc-t4-rn2-cut-2026-06-19). Readability judged by the
            owner's EYE. Overrides the direction-frozen dual-gate + R3 down to owner-eye-only.
      OPEN DECISIONS the builder surfaced for PLANNING (new legs, NOT this leg): d-gasmodel-redesign-001 (the continuous-weight
      gas-as-space model redesign = a CORE redesign + ADR, reopens the LOCK) + d-sandbox-001 reaffirmed (comprehensive test
      scene/sandbox). Builder: "Следующий CALL — за планировщиком (билдер его не сочиняет)" → next = review g-9c41.
  - id: c-work-003
    status: done   # 2026-06-17 (s-work-008) — Wave-2 t-2 framing (owner present): 2 gameplay decisions resolved (d-roomfull-001 closed-level+capacity+back-pressure; d-crossband-inv-001 ratified per-species-temp deferral + BS4 narrow + forward-constraint), BS4 narrowing + openspec L22 PLANNED, executor CALL c-exec-006 FRAMED + adversarially hardened (wf_1b929b4e: openspec spec.md:82 cross-band contamination + GG1 same-tick). t-2 stays active. → history/s-work-008.md
  - id: c-exec-006
    status: done   # 2026-06-19 (s-work-009) — RETURNED + applied. t-2 DELIVERED in GasCoopGame (legs 1-8, main @0327b9f) + owner eyeball «работает» (2026-06-18); gate check.ps1 -Deliver GREEN 372/372, mutation 75.29%, deliverable-coverage 14, fresh-session G5 clean (3 findings fixed). Home-side OpenSpec apply+archive DONE (canonical sim-core/spec.md +18 reqs grep-clean; folder → archive/; dev @7987506 / main @ce79e10, UNPUSHED). FishNet UDP wire env-deferred (WSAENOBUFS — owner-run; binding gate = headless+loopback). RESULT → history/2026-06-18-c-exec-006-t2-result.md. Full framing → history/s-work-008.md.
  - id: c-shape-marketing
    status: done   # 2026-06-16 shape DONE (s-shape-marketing) — g-2f8c set up as a parallel low-ceremony PROCESS (local plays marketing-forge + marketing-status + work/marketing/ graph), canon-forge-style. NOT a second active bet (G1); NOW spine (Wave 2 / c-exec-005) untouched. The go-to-market plan/goals/channels are DERIVED INSIDE the process (one chat = one card), NOT baked. next = first run = q-foundation in a fresh marketing-forge chat. → history/s-shape-marketing.md
  - id: c-exec-003
    status: done   # 2026-06-15 RETURNED GREEN/GREEN (recorded s-work-005); t-2 → done. RESULT → history/2026-06-15-c-exec-003-t-2-result.md
    note: framed at s-work-004 (c-work-002); hardened via an 8-agent pass; PLAN ratified converge §WHAT-C into ADR-0003 v2 (C1–C22 frozen). → history/s-work-004.md
  - id: c-review-001
    status: done   # 2026-06-16 review CLOSED — Wave-1 verdict MET (HOLD independently re-derived: telemetry re-computed + 6-skeptic refutation all un-refuted + live gate 103/103 + git constitution check). 1 verdict-neutral limit named (lossy projection ~5.3x optimistic → crit-9 + knowledge). Owner «го» → Decision A (Wave 2) + tree split + DA/PGG & band-handoff steers. → history/s-review-001.md
    note: |
      Wave-1 kill-gate review. Independently re-derive the HOLD verdict from the committed telemetry (don't
      trust the flag), name any honesty-boundary weakness, harvest what Wave-1 proved into the tree + knowledge,
      bring the owner a next-bet decision (Wave-2 band-sim shape vs alternative). Folds in two known follow-ups:
      the Wave-2 cleanup card (Codex round-3) and the parked map-level re-check of the clip-gated parallel
      tracks (s-shape-004 / root map_order). Builds on history/2026-06-15-c-exec-004-t-3-result.md + ADR-0004.
  - id: c-exec-005
    status: done   # 2026-06-17 (s-work-007) RETURNED PASS_WITH_NITS → t-2. The reopen (s-decide-004, overturned fixed-proportion `LowerShare=total·eff/(eff+16)` model + Codex P1 per-band-temp averaging) is RESOLVED: rebuilt under d-fillmodel-001 (capacity-fill+overflow) + per-band temperature; gate 198/198, mutation 76.76%, fresh-session G5 PASS, owner multi-quantity legibility PASS. A NEW Codex P1 (settle ignores cross-band eff) dispositioned = NO code change (per-band model coherent; the fix would oscillate — d-crossband-inv-001). Merged dev→main + pushed (GasCoopGame build @a868270, RESULT @9e7dab9). RESULT → history/2026-06-17-c-exec-005-t1-result.md.
  - id: c-shape-wave2
    status: done   # 2026-06-16 shape DONE (s-shape-wave2) — Wave 2 SHAPED + committed (G6/G9, owner «го»). BUILD coarse band-sim on the LOCKed stream; 4 tasks (t-1 KILL-GATE first); VERIFIED §CONTRACTS bound into done_when; crit-10 reworded (feedback deferral); owner refinements (generator-agnostic topology, DA room-composer, configurable gas cell, T3 dropped) → captures. next = c-exec-005. → history/s-shape-wave2.md
    note: |
      Wave 2 = real coarse band gas-sim + temperature layer on the LOCKed stream over real (small) generated
      levels. TWO owner-mandated shape inputs (G9, «го»): (1) a player-facing TERMINATION clause — Wave 2 ends
      in something a human reads WITHOUT a debug overlay (breaks pre-mortem #2 before the 08-31/10-05/12-11
      gates); (2) size the coarse grid against the ON-WIRE keyframe-inclusive budget (~11k lossy cells, NOT the
      ~5.3x-optimistic 59k). Steers: DA gives structure/topology day-one (TopologyDocument adapter), PGG =
      population/interior LATER via the same seam (population OUT of scope now); band-handoff design question —
      track sources/emitters EXACTLY even when a volume is coarse + reconstruct local detail from the source on
      player-entry (so a weak corner source is correct on arrival). Re-scope TREE crit-10 in-shape (G9, per
      d-tempfeedback-001): temperature→gas FEEDBACK is DEFERRED to a named later wave (post-g-d3a8 — the rule is
      gas-type game design); Wave 2 requires multi-layer consistency of the gas→temperature SINK at coarse scale
      + the grid-addressed READ-READY seam (the layer can be READ on a committed revision, OR1/OR2/GG2), NOT
      feedback. NAME the deferral, do not silently drop it. Fold the Wave-2
      cleanup card (Codex round-3). converge-arch c-converge-002 contracts feed this. Builds on ADR-0004 §LOCK +
      knowledge/g9c41-wave1-*.
      ✅ CONTRACT GATE LIFTED (2026-06-16 — c-converge-verify-002 PASSED CLEAN): the §CONTRACTS set is VERIFIED
      (independent fresh-session re-refutation across 4 axes + 3 adjudications, 0 BLOCKs). The contracts are NO
      LONGER DRAFT — shape MAY now BIND them into executor done_when: copy the §CONTRACTS acceptance + the §WHAT
      `acceptance` rows (binding by G5) and carry the `→PLAN` rows (CR1 carrier/interest-mechanism; CR2
      Q_coarse/divergence-bound/coarse-settle/coarse-mass-bound/seam-composition; CR3 coarse representation;
      band-handoff prep-window; cross-tier coordinate mapping) as the PLAN-agenda. Carry the 4 converge-verify
      CAPTUREs: V2-1 (size coarse-grid bandwidth from the ON-WIRE keyframe-inclusive ~11k basis, NOT A8.4's stale
      delta-only wording); V2-2 (keep CR1 "entitled" anchored to gameplay-reach, never the streamed window); V2-3
      (exercise the COARSE per-band temperature READ in PLAN tests). V2-4 = THIS shape's G9 job: reword TREE
      done_when #10 to NAME the temperature→gas feedback deferral (d-tempfeedback-001) — the sink ALREADY
      satisfies the literal frozen crit-10 (verify CONFIRMED this), so the rewording is TREE-honesty, NOT a gate.
  - id: c-map-003
    status: done   # 2026-06-16 CLOSED (s-map-003) — clip-trigger RESOLVED (re-hung on g-2f8c's first artifact; teeth = Wave-2 terminus + 08-31 page date); +g-2f8c (generative marketing process); (a) artifact node REJECTED as crutch (owner); (b) co-op-interdependence DEFERRED → c-map-004. NOW spine untouched (Wave 2 stays next).
    note: |
      Structural tree work routed out of review (review play: restructuring > a few nodes → map). Resolve the
      orphaned clip-gate trigger in root TREE map_order (the spectacular clip was dropped at s-shape-004 but
      g-e6f2/g-5b07 still key off it), and weigh two harvest-proposed outcome nodes: (a) "first player-legible
      harness artifact" (peer to g-7e15 — minimal legibility, NOT the full visual system; re-installs the
      player-facing terminus) and (b) "co-op interdependence proof" (peer to g-9c41/g-d3a8 — pre-mortem #5: the
      gas world must FORCE cooperation, currently owned by no node before a parked Steam Playtest). Folds the
      parked s-shape-004 follow-up. Owner-approved card-by-card (G9). Non-gating to Wave 2 (runs parallel).
  - id: c-exec-004
    status: done   # 2026-06-15 RETURNED GREEN/GREEN — Wave-1 kill-gate VERDICT=HOLD (owner-confirmed in build), stream LOCKED, merged main @6619299 + pushed. t-3 → done. RESULT → history/2026-06-15-c-exec-004-t-3-result.md
    note: |
      t-3 kill-gate finale. PLAN freezes (ADR-0004 or ADR-0003 v3, C1–C22 UNTOUCHED — t-3 only ADDS): sustained-load
      test shape; the steady-rate VERDICT predicate (single binary, irrecoverable-vs-transient encoded); production
      channel reliability C7 + fault model; keyframe K C9; min-resend C14; cross-layer integer rule; late-join
      gate-or-defer. 6 owner decisions surfaced at the PLAN (see next.owner_decisions). t-3 OPENS C7/C9/C13/C14,
      only EXTENDS frozen C16/C18. Builds on the t-2 stream → history/2026-06-15-c-exec-003-t-2-result.md.
  - id: c-frame-002
    status: queued
    note: |
      Frame touch-up — encode the owner's 2026-06-12 money-gate clarification into
      CHARTER.md: December mark = small income OR credible potential (matches the
      charter's existing reframe letter); NEW hard wall = the game earning for real by
      ~12 months (EA no later than ~Q2 2027). Map session s-map-002 could not edit the
      charter (play boundary).
  - id: c-converge-001
    status: checkpoint   # converge FORM pass DONE — parallel retrofit on g-9c41 (does NOT touch the bet)
    note: |
      First real converge run (RETROFIT/FORM). Produced work/converge-g-9c41.md: triage HEAVY,
      14 glossary terms, I1–I23 born-closed imports, mechanism C1–C22 + criteria A1–A8 + edges
      B1–B31, 3-source coverage map. Success test PASS (names as questions exactly ADR-0003's
      ad-hoc values; witness independently confirmed). Hardened by 2 multi-agent passes. → history/s-converge-001.md
  - id: c-converge-002
    status: checkpoint   # 2026-06-16 converge-arch DECLARE DONE — §CONTRACTS authored; next = converge-verify
    note: |
      Declared the §WHAT-B cross-node + internal seams as consumer-driven observable contracts in
      work/converge-g-9c41.md §CONTRACTS (IN ingestion/TopologyDocument · GG grid↔gas · OR the B31
      single field-sampling/ExposureQuery oracle · XL the cross-layer + layer-registry seam = the
      done_when-#10 WHITE SPOT the gap-hunt caught · GT gas-type seam · RN render seam · CS
      completeness) + the ARCHITECT record work/converge-g-9c41-arch.md (ARCH-1v2 imported born-closed,
      rides PLAN). HOW→PLAN; nothing re-opens the LOCK/C1–C22. Band-handoff GG4/OR4 OWNER-SIGNED (voice:
      loose spatial + exact source-tracking + FIRM no-shimmer + coarse=truth). Hardened by a 15-agent
      pre-pass (wf_c4e09962-08f). → history/s-converge-arch-001.md
  - id: c-converge-verify
    status: done   # 2026-06-16 BLOCKED close — independent fresh-session G5 refutation of the §CONTRACTS set
    note: |
      converge-verify ran the §CONTRACTS set against FOUR axes with an INDEPENDENTLY-AUTHORED oracle
      (ORACLE-NMTL — 25 contract classes for a networked multi-TIER multi-LAYER authoritative field-core,
      from first principles + precedents; knowledge/ had no checklist). VERDICT = BLOCKED close: 16 classes
      covered + firewall substantially clean + no silent LOCK re-open (XL2 table-resize correctly follows
      the LOCK's own instruction), BUT 2 real holes — F1: NO contract for COARSE-tier network replication +
      consistency obligation (crit-3/crit-9 ~11k on-wire/OR2-on-a-client/GG4-OR4 all lean on an uncited
      coarse-replication decision; latent float-Patankar-vs-locked-integer-bit-exact conflict); F2: XL1
      crit-10 FEEDBACK unreconciled with the locked pure-sink proofs (C21/§T12 byte-identical) + the
      gas/breach-only locked GridEventKind enum (XL2's generalized-C21 contradicts XL1's feedback). Bounced
      to converge-arch (c-converge-003); a clean re-verify gates shape CONSUMING the contracts. NO §SIGNOFF
      written. → §VERIFY in work/converge-g-9c41.md + history/s-converge-verify-001.md.
  - id: c-converge-003
    status: done   # 2026-06-16 converge-arch REPAIR COMPLETE — F1 closed (CR1/CR2/CR3), F2 dissolved (XL1/XL2 re-scope + d-tempfeedback-001), §RESOLVED-4 + minors; in-session hardening pre-pass (wf_b5e55d56-406) = no G7 fork (derivation holds) + 2 must-fix folded (CR1 interest-floor, XL1 per-layer); next = fresh re-verify c-converge-verify-002. → §REPAIR in work/converge-g-9c41.md + history/s-converge-003.md
    note: |
      DONE 2026-06-16 (s-converge-003). Original repair framing kept below for history.
      converge-arch REPAIR of the 2 verify-found holes (observable-first, HOW→PLAN, no LOCK re-open):
      F1 — declare a COARSE-tier network-replication + consistency contract: does coarse band-state reach
      every client-side consumer (vs host-only); carrier (locked-stream resolutionKey vs a separate plane);
      consistency standard (bit-exact / bounded-divergence / host-only) + coarse-solver determinism;
      resolve the float-Patankar-vs-locked-integer-bit-exact conflict at the contract level (crit-3/crit-9/
      OR1-OR2-OR3-on-a-client/GG4-OR4 lean on it). F2 — reconcile XL1 crit-10 FEEDBACK with the LOCK:
      read-based-in-phase-order (enum untouched; Wave-1 sink/ReactionHeat=32/C21 = frozen control) OR
      event-based (SURFACE the locked-GridEventKind-enum extension, never silent in PLAN); re-baseline XL2
      isolation (demonstrative layer == gas+temp, NOT == gas-only). Minors: fold C22 into GG4 bounds; trim
      the XL1 MECHANISM paragraph; make the version-handshake deferral explicit at the g-5b07 build edge.
      Full CALL in history/s-converge-verify-001.md RESULT.next. After re-close → fresh converge-verify.
      ⚠ UPDATED 2026-06-16 (d-tempfeedback-001): owner DEFERRED temperature→gas feedback → F2 LARGELY
      DISSOLVES (temperature stays a SINK; locked C21/§T12 hold; no new GridEventKind; the XL2 byte-identical
      tension disappears). Repair now = (a) F1 coarse-tier replication = the MAIN work; (b) re-scope XL1 for
      Wave 2 = multi-layer consistency of the gas→temperature SINK at coarse scale + the grid-addressed
      READ-READY seam (a layer can be READ on a committed revision per OR1/OR2/GG2), feedback NOT required
      this wave. Then re-verify.
  - id: c-converge-verify-002
    status: done   # 2026-06-16 PASSED CLEAN (s-converge-verify-002) — independent fresh-session re-refutation of the repaired §CONTRACTS set; §SIGNOFF: converge-verify passed → shape may CONSUME the contracts
    note: |
      NARROW fresh-session converge-verify (binding G5) of the REPAIRED §CONTRACTS set (section H CR1/CR2/CR3 +
      re-scoped XL1/XL2 + §RESOLVED-4 + GG4 bounds + CS3). VERDICT = PASSED CLEAN. Four axes attacked
      (completeness / firewall / no-lock-reopen narrowed to new/edited; no-leaning + consumer-independence
      re-traced across every CR-/§RESOLVED-4-citing contract) + the 3 mandated adjudications, adversarially
      cross-examined (14 agents). 0 BLOCK-severity holes: the F1 closure (CR1/CR2/CR3 coarse-tier replication +
      consistency, per-layer incl. coarse temperature) and the F2 dissolution (XL1/XL2 sink re-scope) HOLD;
      ORACLE-NMTL 25/25 re-confirmed; nothing re-opens the LOCK. A BLOCK was proposed (CR1 coverage-floor
      "entitled" term) and ADJUDICATED DOWN — the floor is a falsifiable observable; the proposed fix would
      itself be a firewall leak. The 3 adjudications = genuine ✓: (1) interest-set coverage floor closed; (2)
      coarse-temperature per-layer discharged (no §T12 lean); (3) class-10 — the sink satisfies the LITERAL
      frozen crit-10 (INDEPENDENTLY CONFIRMED), so the rewording is a forward TREE-honesty mandate, non-gating.
      4 non-blocking CAPTUREs forwarded to c-shape-wave2 (V2-1 keyframe-inclusive bandwidth basis / A8.4 stale;
      V2-2 entitlement anchored to gameplay-reach; V2-3 exercise the coarse temperature READ; V2-4 crit-10 G9
      rewording). → §VERIFY-2 + §SIGNOFF in work/converge-g-9c41.md + history/s-converge-verify-002.md.
  - id: c-shape-004
    status: done   # 2026-06-14 — re-shaped the g-9c41 bet under option A (owner «фокус на ядро, клип не паримся», «да A»). Applied: approach/done_when/wave_plan re-shaped, cut_list temp/destruction superseded, kill_by breach=real-controlled, clip dropped, HOLD on c-exec-003 lifted, TREE goal+criteria realigned. → history/s-shape-004.md

decision_inbox:
  - id: d-character-road-001
    status: OPEN   # surfaced 2026-06-29 (s-work-029 plan audit wf_59afe6f0-426, 37 verified gaps); the audit's #1 finding + root cause behind ~half the gaps. Owner planning decision.
    note: |
      AUDIT ROOT FINDING (work/gas-engine-plan-audit-2026-06-29.md): the FOUNDATION is solid + honestly scoped, but every
      thing that makes gas FEEL like a character — multiple gas TYPES (engine carries exactly ONE today, verified), WEIGHT/
      buoyancy (built nowhere), REACTIONS, gas-that-HURTS (dose/damage), temperature — is real in the canon model but lives
      NOWHERE on the build schedule (all crammed in one open-ended "S6+, one at a time" line), even though they depend on
      each other (no reactions without 2 types; no type-damage without types). So each surfaces as a surprise priority fight
      (buoyancy = the first, d-buoyancy-near-weight-priority-001) while the planned "next" (S3) is far-tier scale-plumbing
      for big levels that don't exist yet → the «топчемся/блекло» risk. DECISION (owner, planning — cheap, not code): define
      ONCE the ordered CHARACTER sub-spine and lift each piece out of the backlog ellipsis into NAMED, dependency-tagged
      slices. Audit's suggested order: gas TYPES (the multi-gas foundation) → weight/buoyancy → reactions → type-specific
      damage/temperature. SUBSUMES d-buoyancy-near-weight-priority-001 (buoyancy = one stop on this road) + the "name a
      multi-gas TYPES slice" + "name a damage slice" findings. Recommend: do this BEFORE starting S3 (far-tier plumbing can
      wait until levels get big). NB: the old far-tier already has proven 4-species + weight + heat integer math → port it
      before S4 deletes it (don't re-R&D).
      ── R15 / META-TYPE STRUCTURE (owner raised 2026-06-29; verified first-hand) ──
      The layered param structure (R15: shared PARENT params + per-META-TYPE group params + own visual + per-type config +
      per-INSTANCE env tuning for intensity/danger at spawn) IS a live rule (canon §5:134) + Факт-4 says "types = data
      day-one" — but built NOWHERE + on NO slice. CODE STATUS (origin/main): the engine data shape is ALREADY
      multi-species-ready (VoxelField mass/flux/carry = [species][cell]; VoxelFaceFlow loops per-species;
      SeedMass(cell,species,mass) species-aware) but pinned speciesCount=1, with NO per-type PARAM TABLE (2 species would
      behave IDENTICALLY — the flow law has no per-type params), the forced-flow bias is per-FACE not per-type, and NO
      per-cell dominant-TypeId in the MeaningChecksum (canon §9.5/Факт-4 wanted it day-one; skipped). The VISUAL half
      (GasTypeDefinition/GpuGasParams render params) is being built by g-7e15 on FAKE data. PLACEMENT ANSWER (owner asked
      early-vs-late): EARLY — make the meta-type/type param structure the FIRST character-road slice (weight/reactions/damage
      all key off it). Build the META-TYPE layer first (owner MVP: meta-types + per-instance env params for intensity/danger;
      specific types = config later). Lay the per-cell dominant-TypeId + its checksum slot WITH that slice — cheap, and
      avoids a painful networked-schema migration later (safe to do now: types aren't networked-live until ~S4, no live nodes
      to migrate). CROSS-TRACK: converge on ONE GasType/meta-type DEFINITION carrying BOTH look-params (feeds the visual
      GasParams) AND behavior-params (feeds the engine) — R15 says the visual is procedural FROM params, so one source not
      two. REPRESENTATION decision for that slice's PLAN: the engine's current DENSE [species][cell] vs Факт-4's
      SPARSE-dominant-per-cell (+ mix-overlay) — dense is fine at few types but Факт-4 warns against dense pages at many.
      ── SHARED-PARENT params + POST-RELEASE/MOD extensibility (owner raised 2026-06-29) ──
      (1) SHARED PARENT layer = confirmed = R15's «общий родитель»: params common to ALL gases (density, ratio-to-air =
      how heavy/light, spread speed, …) defined ONCE on the parent, never copied; meta-type adds its own; specific type =
      config. Reinforce in the first TYPES slice's param-table design.
      (2) POST-RELEASE / DLC / MOD gas types = a KEEP-OPEN SEAM to RESERVE now, DEFER the mechanism. The data-driven design
      (R15: a gas type = a DATA asset + register, NO per-type C# / shader) ALREADY points at moddability — so the
      load-bearing, nearly-free decision is to make the first TYPES slice purely DATA-DRIVEN (a TYPE TABLE the engine reads;
      NEVER a hardcoded C# enum/switch — that would weld moddability shut + force a rewrite). DETERMINISM CATCH (lockstep):
      if two peers have DIFFERENT type tables they DESYNC → reserve the type table as an ORDERED, CONTENT-HASHED,
      session-FIXED registry whose hash joins the lockstep session-start handshake (Факт-5 no-late-join makes a Start-time
      handshake natural; mismatch ⇒ refuse/quarantine, never silent). Ship a fixed built-in set first; later DLC/mod types =
      just more registry entries, the handshake already guarantees all peers match. DEFER (not now): runtime loading of
      external mod files (asset bundles / addressables), a mod API, workshop. IS IT NEEDED NOW: no — but reserving the seam
      (data-driven + ordered content-hashed registry + handshake hook) is cheap in the first TYPES slice and avoids both a
      later rewrite AND a silent lockstep break. RECOMMEND: reserve the seam in the TYPES slice; defer the mechanism.
  - id: d-coop-interdependence-repin-001
    status: OPEN   # surfaced 2026-06-29 (s-work-029 audit); a dropped dependency that risks a hard mid-build blocker. Owner: re-pin or fold into the next gameplay-slice PLAN.
    note: |
      AUDIT (Theme 3): forced-coop is now FROZEN signed design (2026-06-28, g-d3a8 — real teamwork must come from the SHARED
      gas: one player venting/opening a route changes the air+path the OTHER faces, live; «two buttons» banned as fake
      co-op). But the engine is co-op-NEUTRAL: lockstep makes both players SEE the same gas, yet NOTHING makes one player's
      gas action a consequence the second is forced to feel. The node «co-op interdependence proof — the gas world must FORCE
      cooperation» was spotted June (s-map-003) as owned by nobody and pushed to a task c-map-004 that was NEVER created /
      never ran → fell through the cracks. The design demand has landed, the engine can't satisfy it, no slice bridges them.
      DECISION (owner): re-pin — recreate the dropped node OR fold the "engine affordance that forces co-op" into the first
      gameplay-slice PLAN, so it's an OWNED item, not a lost deferral. Later to build; cheap to re-pin now; risk if ignored =
      a HARD blocker the day the first real co-op gas moment is built.
  - id: d-buoyancy-near-weight-priority-001
    status: OPEN   # owner-FLAGGED 2026-06-29 («хочу напомнить, чтобы не потерялось»); a real gap + a prioritization call. Verified first-hand: NO buoyancy/gravity/weight in Core/Field/Voxel (main) — near gas spreads by pure gradient diffusion.
    note: |
      OWNER OBSERVATION (verified first-hand in code): the NEAR gas currently spreads by pure GRADIENT diffusion through
      open faces — vertical behaviour comes ONLY from geometry (a low door drains the low cells), there is NO per-species
      WEIGHT (a super-heavy gas does NOT sink faster than a slightly-heavy one). Canon §3 PLANS exactly this as
      «buoyancy-BIAS» (an integer bias on flow through Z-faces, per heavy/light, a CREEPING front — NOT instant
      teleport-to-floor; per-column instant sort is FORBIDDEN near / §7-buried), but it is NOT built (S0 = gradient
      face-flow; S1 = forced-flow impulses; S2 = determinism) and NOT assigned to a named slice (the §5 spine's S3 = FAR-tier
      height-ROUTING layers for player-LESS rooms, which is a DIFFERENT thing from near per-species weight). So near
      buoyancy = a real, UNSCHEDULED near-tier FEEL — now ON THE RECORD as a named slice candidate (was only a §3 model fact).
      PRIORITIZATION (owner decides): next slice = (a) NEAR BUOYANCY (heavy sinks / light rises, tunable strength per gas —
      visible, gameplay-defining, aligns with gas-as-jewel + the ∥ visual track; near = where the player is) OR (b) the
      planned FAR-tier S3 (height-routing layers) + S4 (cheap distant rooms + no-pop rollup — scale-plumbing, load-bearing
      for big/~150-room levels, NOT urgent at the current small-level scale; S4 is now unblocked by S2). RECOMMEND (a)
      buoyancy next; far-tier waits until levels get big. Either way: do NOT lose this (owner ask).
  - id: d-adr-lockstep-citation-001
    status: answered   # owner-APPROVED + APPLIED 2026-06-28 (s-work-027, owner «да»): canon citation FIXED ADR-0010→ADR-0002 (lock = «lockstep over FishNet»; ADR-0010 = test-sandbox). 5 edits to knowledge/g9c41-gas-engine-SPEC.md (§1 authoritative correction note + Факт-1 + §6 hangar + §7 + §9-map), grounded in GasCoopGame ADR-0016/ADR-0002. Full history surfaced: host-broadcast detour was ADR-0003/0004 (+0005-part, +0008), retired ADR-0016/S2a. c-exec-018 (S2b) cites ADR-0002. — surfaced 2026-06-28 (s-work-026), verified first-hand from the c-exec-017 (S2a) build session.
    note: |
      VERIFIED canon citation error (the c-exec-017 builder flagged it; I confirmed first-hand against the actual repo ADR
      files): the canon g9c41-gas-engine-SPEC.md cites the INPUT-LOCKSTEP LOCK as «ADR-0010» (Факт-1 line 31, §2 line 12,
      §6, §7 line 162), and my c-exec-016/c-017 CALLs inherited that. But in the GasCoopGame repo the ACTUAL files are
      ADR-0002 = "Network determinism: lockstep over FishNet (input-bus only)" (THE lock) and ADR-0010 = "Test sandbox:
      scenario-as-DATA (Wave A, t-1)". So the canon points at the wrong ADR number; the lock is ADR-0002. S2a recorded the
      correction repo-side as ADR-0016 (the retirement ADR). This is a PURE CITATION/label error — the lock SEMANTICS are
      unchanged (input-lockstep stands). OPTIONS: (A, RECOMMENDED) fix the canon citation ADR-0010→ADR-0002 for the lock +
      note ADR-0010 = test-sandbox, in a review/pulse session with owner ack (the canon is owner-signed G9; a citation fix
      is low-risk but the canon is the single source of truth) — and c-exec-018 (S2b) already cites ADR-0002; (B) defer to a
      batched maintenance/review pass. IMPACT if unfixed: every future leg that reads the canon re-imports «reopen ADR-0010»
      meaning the test-sandbox, not the lock → recurring confusion (the exact drift class g9c41 fights). Recommend A.
  - id: d-s2-split-001
    status: answered   # owner-DECIDED 2026-06-28 (c-exec-016 PLAN, owner «Split S2a+S2b»; applied s-work-025): S2 multiplayer-lockstep-loopback slice SPLIT into S2a + S2b.
    note: |
      The c-exec-016 PLAN found the S2 scope too big for one leg (per the CALL's own budget split clause). DECISION
      (owner-signed): S2a = ZERO-LEGACY reconstruction-spine RETIREMENT (delete both pre-lockstep host-authoritative
      families + keep/prune store-reducer-far-tier-input-bus + rewrite tests; NO new behavior) — runs FIRST, produces the
      clean base; S2b = lockstep loopback LOAD-BEARING (2-endpoint MeaningChecksum byte-identity over the full forced-flow
      scenario + RED controls + Adapters R14 3-mode owner-eye + frozen spec) — runs AFTER. The direction authors BOTH
      sub-CALLs (builder does not). Housekeeping (owner-approved, folded into S2a): FF dev→main @eed321b (dev⊆main, clean
      --ff-only) + archive c-014/c-015 openspec folders. CALL c-exec-017 (S2a) authored; c-exec-018 (S2b) queued. Migration-
      spine inventory verified at the PLAN (7-agent wf_89e9d3c2, first-hand). Full record → history/c-exec-016-plan-split-2026-06-28.md.
  - id: d-s2-rng-control-na-001
    status: answered   # owner-DECIDED 2026-06-28 (c-exec-016 PLAN, Variant A; applied s-work-025): the done_when 2(b) RNG RED-control is DROPPED as INAPPLICABLE + recorded as intentional spec-silence.
    note: |
      The c-exec-016 CALL's done_when 2(b) listed a planted "unseeded/mis-seeded RNG" RED control. PLAN finding (verified
      first-hand): there is NO RNG on the gas AUTHORITATIVE path — the sim is deterministic-by-INPUT; the only RNG in the
      tree is the OUT-OF-SCOPE ADR-0002 Core/Sim toy. So the RNG control is inapplicable. DECISION (owner Variant A): DROP
      it + record intentional spec-silence (the canon Факт-1 «сидированный RNG» condition is vacuously satisfied — no RNG to
      seed on the gas path). The determinism-catch role is fully covered by the order-dependent-write / silent-wrap /
      awake-queue-permutation / region-fold-order RED controls (c-exec-016 done_when 2a/2c/4e/4f). Reflected in S2b
      (c-exec-018) scope: loopback content carries «MINUS the RNG control». NOT a lock change.
  - id: d-clouds-fork-resolved-001
    status: answered   # owner-DECIDED 2026-06-28 (s-work-023): «точно у игрока, грубо везде» — R7/R12-everywhere is NOT a requirement. The locked input-lockstep integer grid STANDS; no ADR-0010 un-lock; the uncommitted gas-arch-reqs-matrix (candidate E, host-state-sync float clouds) is NOT adopted → archived as history.
    note: |
      An UNCOMMITTED draft (work/gas-arch-reqs-matrix-2026-06-26.md, surfaced by an adversarial
      sequencing check this session) argued the locked model STRUCTURALLY cannot do R7/R12 — a
      50cm-precise reaction / level-spanning split in a room with NO player, EVERYWHERE — because
      far-rollup collapses a room to a position-less integer SUM (canon :79) and reactions read those
      coarse totals (:85); it recommended candidate E (host-authority + float clouds far + fine grid
      near), requiring un-signing ADR-0010 (the biggest migration on the table). VERIFIED FIRST-HAND:
      the facts hold (SPEC Факт-1 lockstep lock :31/:12; :79 SUM; :85 coarse-trigger; :90 Ведро-3
      limited to ~2-3 rooms), AND the prior cloud-vs-grid analysis (basis for the canon's
      clouds-rejection) evaluated clouds ONLY on cross-CPU determinism — never host-authority — so
      candidate E was genuinely UNDER-EVALUATED, NOT settled drift. Put to the owner as the pivotal
      requirement question. OWNER ANSWER: «нет — точно там, где игрок (+2-3 назначенные Ведро-3
      комнаты); грубо везде по тоталу». => the canon AS-LOCKED already satisfies the real requirement
      (deep interaction = coarse events everywhere + Ведро-3, exactly as locked; full precision rides
      with the player). DECISION: lockstep STANDS; no architecture change; matrix → work/archive/ as
      NON-ADOPTED history (not authority). CARRY (capture): IF host-authority is ever reconsidered,
      the cloud-vs-grid analysis must be RE-RUN on the host-auth model (its kills are
      cross-CPU-determinism-class, void under a single host) — recorded so the gap is on the record.
  - id: d-displacement-s1b-cut-001
    status: answered   # owner-ACCEPTED 2026-06-28 (s-work-023, «весь пакет»): выдавливание (S1b) CUT to backlog. The original S1 / canon-§5 «выдавливание» is split out + deferred, NOT built now.
    note: |
      Displacement (a body shoves gas aside) is the ONLY passive primitive in the S1 set; the active
      tools (jet/eruption/wind/valve) already deliver the directable-gas feel. Owner lean (confirmed):
      «player should INTERACT with gas, not have gas be a passive thing bodies push around». NOTE
      (canon line 122 anti-rule): displacement defaults to COSMETIC in-room (off-checksum; only a
      door-impulse is authoritative) — so the hand-back's «needs a capacity-aware mechanism + its own
      ADR» framing was the HEAVY-version read; the canon's own displacement is cheap. DECISION: CUT to
      backlog. RE-ENTRY TRIGGER (recorded so it's a deliberate deferral, not a silent drop): the first
      real gameplay moment that needs a body to dam/divert gas (corpse blocks a vent, player plugs a
      breach). If re-entered, the cheap cosmetic-by-canon version is the default (no capacity model, no
      ADR) unless a consumer needs authoritative blocking. Keep the pressure capacity representation
      read-only-only (d-pressure-signal-on-demand-001) so re-entry stays a cheap fold-in, not a rework.
  - id: d-pressure-signal-on-demand-001
    status: answered   # owner-ACCEPTED 2026-06-28 (s-work-023, «весь пакет»): pressure = read-only SIGNAL built ON-DEMAND when a consumer needs it; baseline back-pressure already ships; optional cap/compression DEFERRED.
    note: |
      Capacity research (builder hand-back, docs/research/capacity-pressure-2026-06-27.md) verdict: a
      read-only pressure SIGNAL (regionMass/cellCount, integer, ~trivial, ZERO flow-behaviour change)
      satisfies every named driver; ENFORCEMENT beyond the baseline is unnecessary for S1/S2/S3.
      CORRECTION (caught this session, for the record): the hand-back's «enforcement is
      unnecessary/absent» is SLIGHTLY WRONG — BASELINE back-pressure ALREADY ships and is load-bearing
      (canon d-roomfull-001: flow/inject clamped to [0,cap], source idle on a full room, sealed full
      region saturate-and-hold mass-exactly). Only the OPTIONAL extra ceiling (GAP-1 cap, stubbed ∞) +
      true COMPRESSION (behind the deferred sparse solver) are deferred. DECISION: add the read-only
      signal the moment a real consumer asks (HUD / the S5 «давление ломает дверь» destructibility
      seam, canon §9.9 / AI) and NOT a leg before; keep baseline back-pressure; leave cap/compression
      stubbed. DEPENDENCY recorded: the S5 destructibility seam READS a stored back-pressure number —
      the signal must exist by S5, but not earlier. NOT its own slice (invisible — rides inside the
      first consumer).
  - id: d-scene-one-polygon-001
    status: answered   # PLANNER spec-amendment 2026-06-26 (s-work-022) — c-exec-015 spike finding D4. Owner direction = ONE curated test polygon, not a scene-per-feature.
    note: |
      The c-exec-015 frozen spec mandated a SEPARATE GasForcedFlowScene.unity (deliverable-coverage row 7); the builder
      already (correctly) consolidated the forced-flow driver into the one VoxelSandboxDirector with a mode selector, but
      could not edit the frozen spec. DECISION (planner-authorized): the engine owner-eye deliverable = the ONE curated
      sandbox scene (existing GasVoxelSandboxScene) configured via the director's level/mode selector for forced-flow —
      NOT a new .unity per feature. Drop the separate-scene `exists:` row; point coverage at the existing sandbox scene;
      remove/fold the standalone GasForcedFlowScene.unity. ADOPT "one curated polygon, mode-selected" as the STANDING
      convention for all future richness legs (matches the project's anti-scene-sprawl cut). Folded into c-exec-015-call.md §AMENDMENT.
  - id: d-bias-quantum-001
    status: answered   # PLANNER-DECIDED 2026-06-26 (s-work-021), verified FIRST-HAND in VoxelFaceFlow.cs:66 (dev). A c-exec-015 STEP-0 finding (Codex P2 #1) routed home; not a builder patch.
    note: |
      FINDING (verified): the bias MOVE = `(long)bias * conductivity / kpEff` (line 66), where kpEff = Kp*spf = 12*spf
      (the GRADIENT's RELAXATION damper). So a valid non-zero bias below ~12 (full face) truncates to 0 → a weak
      kick/vent is a SILENT no-op (conflicts with the never-seals/valid-impulse-acts contract). Body-vents use huge
      strength so owner-eye is unaffected; this is an API-contract footgun. A bias-CARRY was correctly REJECTED by the
      builder (lines 82-86/99-102): banking bias into carry would move mass at ZERO gradient after the bias decays,
      breaking the "довести фронт до покоя" settle guarantee (ADR-0011 D3).
      DECISION (policy): a non-zero bias on an OPEN face MUST have a non-zero deterministic effect when mass is available
      — NEVER a silent no-op. PREFERRED mechanism = a guaranteed signed ±1 floor (if bias≠0 ∧ conductivity>0 ∧
      truncated biasMove==0 → ±1 in the bias direction, clamped by available mass) — parallel to the gradient's "a slit
      never seals to 0". NOT a bias-carry. The build MAY instead reconsider whether the FORCING term should be damped by
      the relaxation kpEff at all (the likely root) — its call, but the ±1 floor is the minimal settle-safe fix.
      MUST: preserve conservation; integer + in MeaningChecksum + loopback-deterministic; and STILL pass the Step-0
      monotone-settle oracle (once the bias decays to 0 the system settles — the ±1 acts only in the bounded, decaying
      forcing window). Independent test-author writes a RED test BEFORE the fix: a weak vent (strength below the current
      quantum) over N ticks MUST move mass (no silent no-op); TotalMass conserved; settles after the bias ends;
      deterministic. Document the quantization in the spec (sub-quantum strength still moves the ±1 minimum; no carry).
  - id: d-rw3-step-atomicity-ledger-001
    status: answered   # PLANNER-DECIDED 2026-06-26 (s-work-021), verified FIRST-HAND in RW3ConservationAtomicityTests.cs:170-234 (dev). A c-exec-015 STEP-0 finding (Codex P2 #2) routed home; the independent test-author fixes it.
    note: |
      FINDING (verified): RW3 Test-4 is ledgered as "throwing VoxelFaceFlow.Step leaves mass/bias/ttl unconsumed" but it
      forces the throw on SeedMass (line 214), never calls a throwing Step, and even ASSERTS the checksum CHANGES (line
      224, because EmitImpulse enqueued before the SeedMass throw). So the ledger row overclaims coverage. NOT a live
      bug: Step IS atomic by construction (all locals computed + validated before the single CommitStep at line 149),
      AND its overflow guard (line 139) is UNREACHABLE given MaxCellMass=1<<24 (max inflow ≈ 6×16.7M+16.7M ≪ int.MaxValue
      ~2.1B). It is a gap in the PROOF (honest-ledger defect), not a defect in the code.
      DECISION (ledger must be honest — the deliverable-exists/honest-ledger invariant): the independent test-author
      EITHER (a) genuinely exercises a throwing Step via a test SEAM that throws AFTER the bias/queue is computed but
      BEFORE CommitStep, and asserts the field byte-UNCHANGED (mass/bias/ttl/checksum) — the direct proof; OR (b) RENAMES
      the current test to its TRUE coverage (SeedMass overflow atomicity + EmitImpulse-before-SeedMass-throw leaves
      mass/bias unchanged) AND discharges "Step atomicity" by a CONSTRUCTION argument (overflow guard unreachable-by-
      construction at MaxCellMass=1<<24 + single CommitStep after full validation = structural atomicity), with the
      ledger row CORRECTED to cite that real evidence. No silent overclaim either way.
  - id: d-gas-richness-tiers-001
    status: answered   # owner-STEERED + owner «ок» 2026-06-26 (s-work-020) on the 3-tier gas-richness model. Basis = deep-research workflow (work/gas-richness-deep-research-2026-06-26.md; 20 agents, web + code, adversarially verified). EXTENDS the locked model (does NOT crack it): adds the impulse-event/directional-bias seam; reserves the two heavier tiers.
    note: |
      S1a CLOSE — VELOCITY STATUS (s-work-023, 2026-06-28, owner «весь пакет»): TIER-3 (fixed-point
      velocity, ADR-0010 lock-crack) = RESERVED, trigger ARMED — NOT triggered by S1a. Honest read
      carried so the corridor win can't silently answer the open question: c-exec-015 delivered
      CHANNELED net-transport ~27× (walls) but open-space concentration is still only ~2:1 (a lean,
      not a sharp jet); the owner-eye «работает» was on debug cubes WITH emitter-confinement.
      RE-TRIGGER (concrete) = ONE honest no-walls confinement-tuned open-space jet owner-eye look at
      the COMBAT slice (where «damage = concentration» becomes load-bearing). If it can't read as a
      tight open-space jet THEN → that look is the SIGNED evidence for ADR-0010, entered deliberately.
      Until then 2:1 stands; TIER-3 stays reserved. (Velocity LOCK-CRACK remains a mandatory
      STOP-and-escalate — never silent.)
      ---
      D1 SPIKE RESOLUTION (s-work-022, 2026-06-26): owner eyeballed the GREEN c-exec-015 Step-0 spike and resolved D1 —
      he CONFIRMED the game needs gameplay-meaningful directional JETS that deal more damage (by concentration), but chose
      cheap TIER-1 WITHOUT inertia NOW + revisit. The spike's open-space ≈2:1 lean measured forward-bias on ONE face only
      — it never tried LATERAL CONFINEMENT; so TIER 1 stays with a sharpened owner-eye target = a VISIBLE jet on the cubes
      via a jet-emitter (forward push + lateral confinement; emitter-born valves/inward bias; travels with the jet, NOT
      level walls — gas spawns anywhere). If even with confinement it can't read as a tight open-space jet → concrete
      trigger for TIER 3 (fixed-point velocity, lock-crack ADR-0010). NO coasting/inertia this leg. (D2 = d-bias-quantum-001
      / D3 = d-rw3-step-atomicity-ledger-001, already decided s-work-021; D4 = d-scene-one-polygon-001.)
      ---
      Owner pushed back on "gas richness is a hard compromise" and asked for deep research (incl. exotic) + a novel/hybrid
      solution; validated two of his own ideas. RESULT = a 3-TIER architecture, owner «ок» to building tier 1 now:
      • TIER 1 (BUILD NOW = S1/c-exec-015, NO lock-crack): integer IMPULSE-EVENTS write a DECAYING directional-bias
        register on top of the S0 gradient face-flow. Delivers — AUTHORITATIVELY + cheaply — WIND/directionality, a
        decaying momentum-HINT (gust), transient fork-split, and DESIGNED permanent split via a face-level one-way VALVE.
        Owner's IDEA 1 (a deterministic split-impulse EVENT in the grid) = the KEYSTONE, first-class, zero new wire
        traffic. Honest limits: NOT true coasting inertia, NOT permanent open-volume split, NOT free emergent vortices.
      • TIER 2 (DEFERRED, ADR-class, post-sparse-solver): seeded-integer LATTICE-GAS (FHP/ILG) confined to a few bucket-3
        rooms → true emergent VORTICES as shared truth without floats. Everywhere else, vortices = the read-only cosmetic
        g-7e15 visual layer, fed the authoritative bias field so swirl aligns with real wind (zero gate risk).
      • TIER 3 (RESERVED, owner-gated, cracks the lock): fixed-point (Q-format) VELOCITY field = true stored inertia +
        graceful permanent split as shared truth. Owner's IDEA 2 («float via 2 ints» = fixed-point) is REAL + proven
        (Photon Quantum/StarCraft/FixPointCS), but bespoke, heavy, and IS the velocity/advection the roadmap names a
        STOP-escalation → requires an owner-signed ADR-0010 lock-crack. Triggered ONLY if owner-eye proves tier 1 «isn't
        alive enough». NOT adopted now.
      4 VERIFIED load-bearing corrections folded into c-exec-015 (the build must honor): (1) §9.5 trip-wire — the sub-face
      bitmap lives in StructureGrid (own checksum, OUT of the gas checksum); keep bias FACE-LEVEL-UNIFORM, defer sub-face
      directionality. (2) symmetric integer decay (a signed shift breaks directional symmetry). (3) the Kp≥2*degree
      contraction proof is SUSPENDED during forcing, not preserved → a RED non-monotone settle oracle is a hard
      precondition (the de-risk spike). (4) the bias decay-tail inflates the active-set → re-measure under FORCING (it
      interacts with the deferred sparse solver; big-hall viability stays gated by d-sparse-solver-defer-001).
      LIBRARY shortlist (only IF tier 3): FixPointCS (MIT), FixedMathSharp (MIT) — arithmetic only; no off-the-shelf
      fixed-point FLUID solver exists (bespoke). Unity.Burst/Jobs (already present) = the weak-core lever for sparse.
      Float fluid packages (Zibra/Obi) = ONLY the cosmetic g-7e15 layer, never authoritative.
  - id: d-sparse-solver-defer-001
    status: answered   # PLANNER-DECIDED 2026-06-26 (s-work-019, owner-delegated «решение за тобой»); owner-VETOABLE. Covers S0 routed-home findings #1 (sparse solver), #2 (weak-CPU re-measure), #3 (GC pooling).
    note: |
      UPDATE 2026-06-28 (s-work-023, owner «весь пакет»): RELABEL "deferred-UNVALIDATED". The
      c-exec-015 active-set-under-forcing measurement (docs/measurements/c-exec-015-active-set-under-
      forcing.md) shows that under SUSTAINED forcing the active set is near-DENSE (~419 of the vented
      region), so the promised ~100× sparse win is NOW IN DOUBT and MUST be benchmarked UNDER FORCING
      (not on a settled field). The deferral STANDS, but its gating spike's FIRST job = the
      under-forcing benchmark — it either proves big-hall headroom or KILLS big halls as a design
      option. Trigger unchanged = the first time a level calls for a big open hall.
      ---
      The S0 HANGAR PROBE measured a big open volume: 196,608 cells / 24.5 ms-avg-tick (65.5 max) on a STRONG CPU, but
      only 1,562 cells held gas — the DENSE S0 solver processes ALL of them every tick (~125× redundant). The builder
      recommends a SPARSE active-front solver (the §9.3 flux/carry register is laid but not yet consumed by
      VoxelFaceFlow.Step) as the #1 optimization, plus a weak-CPU re-measure and GC-buffer pooling.
      DECISION: DEFER all three to the BIG-HALL gate — they are NOT the next leg.
      WHY: the sparse solver matters ONLY for BIG OPEN VOLUMES (hangars), which are explicitly DEFERRED-RESERVED
      (d-cellsize-split-001 #6 — activated only if a measurement shows a problem). The near room-scale slices S1–S5 run
      on the DENSE solver, which is measured FINE (TYPICAL 3,456 cells = 0.525 ms/tick, ~50× under a generous budget).
      So the sparse solver is NOT a prerequisite for S1–S5; it is a NAMED, ready optimization leg (sparse active-front +
      GC pooling + the weak-CPU re-measure as its gating measurement) that FIRES before any big-hall feature is
      committed. The big-hall VIABILITY VERDICT is now explicitly gated on that leg.
      SURFACED LOUDLY (de-risk-vs-visible tension): at full 196k the dense hangar is already MARGINAL on a strong CPU
      (24.5 ms) and a weak core is ~2–4× slower → big-hall viability on weak hardware is UNPROVEN until that leg shows
      the ~100× headroom the sparse register promises. But nothing near-term depends on it, and S1 is VISIBLE gameplay
      progress (a pure optimization leg shows the owner nothing). Owner's machine (RTX 4090 / top AMD) is OPTIMISTIC for
      a single-threaded CPU sim — a true weak-CPU number needs a representative machine or a downclock/affinity proxy.
      VETO OPENING: if the owner would rather front-load the sparse-solver / perf de-risk NOW instead of S1, the next
      CALL swaps to that optimization leg — say the word. Default = proceed to S1.
  - id: d-overflow-guard-001
    status: answered   # PLANNER-DECIDED 2026-06-26 (s-work-019, owner-delegated); folded into c-exec-015 H1/H2. Covers S0 routed-home findings #4 (int*int overflow class) + #5 (extreme-coordinate spec-silence row).
    note: |
      The "no silent int*int wrap on the authoritative path" invariant has recurred at 3 sites (SubFacesPerFace, kpEff,
      coord·spa — each fixed per-site in S0 as T6). The builder flags that a 4th per-site patch is whack-a-mole and asks
      the planner to choose: a class-wide auto-discovering guard vs accept as debt. Separately, the frozen spec's
      silence-audit covers extreme-RESOLUTION overflow but NOT extreme-COORDINATE (coord·spa) — a distinct unintended
      silence the builder may not self-fix (the spec is frozen mid-leg to prevent self-serving edits).
      DECISION: (a) BUILD the class-wide guard — a build-scan tripwire that auto-discovers unguarded int*int multiplies
      on the authoritative Core path (analogous to the zero-float scan), wired into tools/check.ps1 -Deliver, RED-first
      with a planted unguarded-multiply control that MUST fail. Rationale: "same class twice = stop" is established OS
      engineering doctrine; 3 instances = the durable fix beats a 4th band-aid. (b) AUTHORIZE the extreme-coordinate
      spec-silence amendment (planner-authorized = not a builder self-edit). Both folded into c-exec-015 as carried
      hardening H1/H2 (same leg — it touches the same authoritative path; RED-first; through the gated contour).
  - id: d-cellsize-ratify-001
    status: done   # RATIFIED 2026-06-23 by owner «да» on the canon knowledge/g9c41-gas-engine-SPEC.md (s-repair-consolidate). Fact #2 re-worded: «50cm ISOTROPIC, height EMERGENT, NO bands» — the «authoritative height-bands» phrasing in the note below is SUPERSEDED by the canon; cell-SIZE-LOD retired, LOD axis = spatial room-rollup (S4).
    note: |
      s-repair-docs-001 flagged — via a POINTER, NOT a silent lock edit — that the locked fact #2 wording «ONE integer cell
      model, cell-SIZE LOD» (knowledge/g9c41-architecture-locked-slices.md + the d-arch-lock-slices-001 note below) is
      SUPERSEDED-IN-PART by the s-research-012..016 synthesis (work/gas-cellsize-levelscale-2026-06-22.md §10-§12): the
      authoritative LOD axis is SPATIAL room-rollup (S4), NOT a per-room cell-SIZE mix; gas = 50cm GLOBAL; 25cm = off-checksum
      local visual + authoritative height-bands; the cross-resolution re-flux seam is REMOVED. The SUBSTANCE is already in force
      (c-exec-013 pins 50cm-global + drop-25cm; the pointer banner steers every PLAN, and locked-slices is a mandatory READ-FIRST).
      What is OPEN = formally re-wording the LOCKED fact text so future sessions stop reading «cell-SIZE LOD» — an owner-signed
      re-shape (G9; touches the locked canon, so it is NOT done silently).
      OPTIONS: (A, rec) RATIFY in a ~5-min owner-signed mini-session whenever convenient — reword locked-slices fact #2 to
      «50cm-global authoritative; LOD axis = spatial room-rollup (S4); 25cm = off-checksum local visual + authoritative
      height-bands» (the banner holds the interim, nothing is lost); (B) leave the banner only — bad-because the stale
      «cell-SIZE LOD» text persists in the canon indefinitely and relies on every reader noticing the banner.
      NON-BLOCKING for S0: c-exec-013 + the pointer banner fully cover it; build S0 first, ratify when convenient.
  - id: d-cellsize-split-001
    status: done   # RATIFIED 2026-06-26 by owner «да» on the re-shaped canon SPEC (R1-layered-reshape). EXTENDS d-cellsize-ratify-001 (does NOT reverse it): the gas-50cm isotropic ratification STANDS UNCHANGED; this ADDS the per-LAYER resolution split + the layered coordinating-grid frame the consolidation had flattened.
    note: |
      Root (work/gas-engine-layered-reshape-2026-06-26.md §1-§2): the s-repair consolidation flattened the owner-confirmed LAYERED
      coordinating grid into a gas-centric «one 50cm grid»; build S0 (c-exec-013) inherited it → 4 symptoms (door opened whole wall
      / marker dispute / 50-25 confusion / «what is a layer»), all = conflating GAS resolution (50cm, volumetric, ×8) with
      TOPOLOGY/PLACEMENT resolution (can be 25cm, cheap). Triple-vetted by 3 adversarial workflows (layered-reshape, cloud-vs-grid,
      variant-B). DECIDED (owner «да» 2026-06-26):
      (1) gas_res = 50cm PRESERVED verbatim (SPEC Факт 2) — ONE 50cm isotropic integer gas model, height emergent, no re-flux seam.
      (2) geometry_res (STRUCTURE layer) = 25cm DEFAULT — single source of structural truth (walls/floors/openings/breach), authored
          via markers on reusable modules, validated vs geometry; tunable via the EXISTING resolution_tag config (no rebuild, no
          extra config machinery).
      (3) placement_res = 25cm RESERVED, mechanic DEFERRED (no objects yet; address reserve §9 шов 10).
      (4) resolution_tag invariant INVERTED: geometry MAY be finer than gas (25 under 50); coupling = deterministic INTEGER per-Z-band
          sub-face occupancy-BITMAP → conductivity COUNT (never a scalar, never integer-divide). One-way structure→gas, static.
      (5) GRID = coordinating backbone (coord/address + cell→region ownership + event bus + commit clock, NOT a router); cross-layer
          read ONLY vs a committed revision (§9 шов 7). Markers: geometric = validated-vs-geometry (builder-or-owner); semantic
          (material/threshold/mask) = owner/fixture ONLY (no oracle → builder never authors = the c-exec-012 anti-cheat reframed).
      FOLDED sub-decisions (from the cloud-vs-grid + variant-B analyses; detail in the work docs):
      • HYBRID — integer grid stays AUTHORITATIVE; clouds-as-authority REJECTED (moving-boundary mass-double-claim / deep-interaction
        drop / determinism). ADOPT a fixed-radius SPHERE-CAP of the off-checksum detail bubble (ADR start 4m@50см; radius+cell-size
        LOCKED, else 25cm-inside or a big radius silently re-opens the blowup). This is the one real lever from the owner's cloud idea.
      • Variant-B made affordable by RECLASSIFYING monotone-B → an in-checksum coarse-total threshold (RED oracle + a non-monotone
        control that MUST fail). State-driven-near-demote + lazy-resolve REJECTED (byte-identical-but-WRONG). height-field = FAR-only LOD.
      • Big halls DEFERRED but RESERVED-EXTENSIBLE (owner directive): author as segments-with-full-wall-doors (far-coarser falls out
        free) OR far-only mid-2.5D (§7) + sub-partition — activated ONLY if the hangar-probe measurement shows a problem. settled_flag
        = far-scoped only (gates far-demote/sleep, never a near transition).
      PRESERVED (not reshaken): determinism by construction (integer, zero-float scan — the structure layer + projection are ALSO
      Core-side integer); gas single-50cm (no re-flux seam); R13/R14; owner-eye «точно/весело»; all model-agnostic S0 work.
      GATES: this is the FOUNDATION of the reshaped S0 (c-exec-014, supersedes c-exec-013). A MAINTENANCE request to os/engineering
      is drafted (anti-substitution over-rotation + resolution conflation = one meta-pattern «distinguish-the-scope before a decision
      becomes a global guard/lock») → hand to a SEPARATE maintenance session, os/** NOT touched here.
  - id: d-reflux-gate-001
    status: answered   # owner-decided 2026-06-22 (s-repair-canon-001) — re-flux / determinism binding gate = loopback ONE machine + zero-float guard; NO two physical machines, EVER
    note: |
      Owner closed the lone genuine canon gap the drift-sweep surfaced (re-flux kill-probe said «2 машины»; S2 said one machine).
      DECISION: integer cross-CPU determinism is an ESTABLISHED GIVEN (banks/games) — NOT proven, NO research on two machines.
      The binding gate for re-flux / the грань-operator (incl. its D5/ведро-3 hard-gate escalation) = a build-time ZERO-FLOAT scan
      + a loopback hash, BOTH on ONE machine. A real 2-physical-machine run is NEVER a gate (owner has one machine — sufficient).
      The ONE thing that must exist = a guard that does not let a float into the authoritative path (owner: «нужен гард, который
      не пропустит float — это очень плохо»). Supersedes the «2 машины» wording in work/grid-vs-graph-resolution §5/§8/§11
      (corrected in-place via a banner) + the archived aplus-replan §3. Encoded in knowledge/g9c41-drift-guard.md #2/#5.
  - id: d-arch-lock-slices-001
    status: answered   # owner «да» 2026-06-22 (marathon re-plan CLOSE) — locked architecture + slice methodology + the firm decisions
    note: |
      ARCHITECTURE LOCKED + SLICE METHODOLOGY (close of the 2026-06-21/22 re-plan marathon; co-creation + 4 verification workflows).
      Durable spec: work/dev-plan-graph-2026-06-22.md (SINGLE entry) + knowledge/g9c41-architecture-locked-slices.md + knowledge/g9c41-drift-guard.md +
      gas-model-architecture-decision-2026-06-21.md (D1–D13) + grid-vs-graph-resolution-2026-06-22.md + detail-authority-cost-model-2026-06-22.md. (PRE-2026-06-22 docs → work/archive/, s-repair-canon-001.)
      LOCKED (owner-confirmed): (1) NETCODE = input-lockstep (only inputs on wire; every peer recomputes; weakest-peer CPU the limit;
      host-migration near-free) → ADR-0010 supersedes ADR-0004/0005 host-broadcast authority (game-repo writes it). (2) ONE integer
      cell model, cell-SIZE LOD: near = full-3D grid + flow through OPEN FACES (area/height/no-through-walls emergent); far =
      room-graph ROLLUP; ROOM = a LABEL at every tier (pipe dropped near; portal = cut-set aggregate of open faces). (3) DETAIL = a
      LOCAL non-authoritative refinement of the COARSE-authoritative truth — coarse computed everywhere + in the checksum; detail only
      where a peer's OWN player is (~1 bubble/peer not N, ~8× CPU win); hard shared consequences = coarse EVENTS; collapse/expand =
      discard-on-leave; determinism GUARANTEED BY CONSTRUCTION (integer-only; cross-CPU is a GIVEN fact, NOT re-proven, NO 2nd machine needed — owner has one; cheap one-machine lint = zero-float scan + optional 2-process loopback), NOT re-flux (re-flux → owner-eye no-pop except
      D5/ведро-3). (4) sparse dominant-gas (D9), integer chemistry table (D10), real-height-3D near (D11). (5) NO LATE-JOIN (lobby/base
      → start → raid with whoever is present; no mid-raid join; later maybe). (6) ZERO-LEGACY at completion (clean tree; rollback only
      via git; tests reviewed/rewritten). (7) reusable-engine DROPPED (D12, game-first). METHODOLOGY: incremental VISIBLE slices
      (S0…), each PLAN-ingests-all-research → RED-first → build deterministic/clean/extensible → owner-VISIBLE result → integrate;
      per-mechanic depth classified ведро-1/2/3 at its slice PLAN (default room-granular A). marketing/devlog + lore ∥; storefront
      gated on visual identity. TREE g-9c41 #12 added (G9). Open per-slice classification of expressive mechanics happens at each PLAN.
  - id: d-converge-001
    status: answered   # owner 2026-06-14 «давай вариант A» → converge set wired into c-exec-003 context + leg_opens_with as mandatory PLAN input evidence (s-decide-002)
    note: |
      A CHOSEN: feed work/converge-g-9c41.md into the in-flight c-exec-003 PLAN before ADR-0003
      freezes the stream magnitudes (C1–C22); the PLAN RATIFIES the named §WHAT-C questions instead of
      re-inventing — special attention to the 4 the c-exec-003 CALL left implicit (C19 client-recon
      arithmetic determinism, C20 client apply-order/keyframe interleave, C21 layer registry vs
      revision feed, C22 lossy mass-conservation bound). Wired into NOW.next (context + leg_opens_with).
      # d-arch-001 answered at s-shape-003 (see history/s-shape-003.md outcome a-e)
  - id: d-generator-001
    status: answered   # owner 2026-06-16 (review c-review-001): «DA может делать именно уровни ... PGG уже наполнять ... сейчас мы не будем заниматься наполнением»
    note: |
      Generator strategy for the levels g-9c41 consumes. DA = day-one STRUCTURE/topology generator (rooms +
      corridors → fills the TopologyDocument the gas sim reads, via the replaceable ingestion adapter). PGG
      (grid-based) = LATER, for room POPULATION / interior / grid layouts, behind the SAME adapter; population
      is explicitly OUT of scope now. Not married (no co-generation on one level now); both stay swappable via
      the adapter — concept not locked. Wired into c-shape-wave2 as a steer (final lock at the Wave-2 shape).
      REFINED at s-shape-wave2 (owner «го»): DA runs in ROOM-COMPOSER mode (places hand-made tagged room prefabs,
      level SIZE free); the topology seam reads (scene-geometry + semantic tags/markers) → TopologyDocument, NOT DA's
      stale 2D API (generator-agnostic, decouples us from the vendor); PGG = room-INTERIOR generation later behind the
      same seam, framed as an OPTIONAL future research session (owner «можно отдельно запустить ресёрч»); population OUT.
  - id: d-bandhandoff-001
    status: answered   # owner 2026-06-16 (converge-arch c-converge-002, voice) — signed the band-handoff contract STRENGTH
    note: |
      Band-handoff contract strength (GG4/OR4). Owner (voice): metric precision NOT important («примерно»,
      few cells of error OK, «никто точность измерять не будет»); coarse sim = source of truth that unfolds
      into a prep tier within a radius + a fine close-up tier (his 3-tier HINT → PLAN, a hunch not a lock);
      the player must APPROXIMATELY see strength + main corner + that a weak source accumulates slowly; HARD
      = «никаких подрагиваний… это 100%» (no shimmer/pop on the handoff); «не нужно что-то прям дорогое»,
      gameplay-POV only. «Охренеть как важно» — open to deeper tightening at the Wave-2 shape. Signs the
      contract STRENGTH; the mechanism + tolerance magnitude stay PLAN. Recorded §SIGNOFF-BH in
      work/converge-g-9c41.md. CLARIFIED same session (owner voice): GAMEPLAY-binding, not only metric — (a) NO
      visible jerk/twitch in the gas EVER (incl. off-screen-computed state surfacing on entry; gas-reading = core
      mechanic); (b) believable amount AND rate on return (coarse tier accumulates at a plausible monotone rate;
      quantity matches the observed source strength + elapsed time, no jump; crossing tiers changes only spatial
      detail). Folded into GG4/OR4 + the cross-layer XL1 mechanism made concrete to the owner's grid-as-bus model.
  - id: d-tempfeedback-001
    status: answered   # owner 2026-06-16 (post-converge-verify design conversation, this session) — «все понятно со всем полностью согласен»
    note: |
      Temperature↔gas — TWO owner decisions confirmed in conversation (defer feedback + the inter-layer read
      architecture); recorded so the pending CALLs carry them. The formal §RESOLVED / crit-10 rewording happen
      in c-converge-003 / c-shape-wave2 (NOT written into TREE/§CONTRACTS here).
      (1) DEFER temperature→gas FEEDBACK to a later wave (post-g-d3a8). How heat affects each gas type is a
          function of the gas-type GAME DESIGN being worked in parallel (canon track / g-d3a8) — building it now
          = guaranteed rework (RESOLVED-3 "extensible seam, minimal impl now"). Nothing in the Wave-2 spine
          (band solver / grid / replication / destruction) depends on it. Temperature STAYS a live, network-
          consistent layer = the gas→temperature SINK (Wave-1 ReactionHeat sink, exercised at Wave-2 coarse
          scale), NOT deleted. Deferred HONESTLY: crit-10 is re-scoped so feedback is NAMED as deferred to a
          later wave, not silently dropped (the rewording = the SHAPE's G9 job). Consequence: verify Finding F2
          LARGELY DISSOLVES (no feedback → temperature stays a sink → locked C21 byte-identical + §T12 hold; no
          new GridEventKind needed), shrinking c-converge-003 to mainly F1.
      (2) INTER-LAYER READ ARCHITECTURE confirmed (resolves the verify watch-item "don't foreclose feedback"):
          the GRID = shared coordinate/address space + cell→room/sector ownership map + the event bus + the
          revision/commit clock — NOT a data router/god-object. Each layer publishes, on a committed revision,
          events (push, discrete "something happened") + a READ-MODEL (pull, "value at grid-cell c as of revision
          r") that translates grid-coords → its own representation internally. Consumers subscribe/query in GRID
          coordinates against a COMMITTED revision; never touch another layer's internals or live mid-tick state
          (determinism). Collapses N×N adapters → N (one grid-addressed read-model per source layer, shared by
          all consumers) and handles heterogeneous resolution (temperature answers a per-cell query from per-room
          storage). MATCHES existing contracts OR1/OR2 (single sampling oracle) + GG2 (geometry/sector
          sovereignty); the only correction to the owner's first model is "grid addresses, not routes data".
          Forward constraint to carry into Wave-2 design (cheap, not code): the read seam must let a layer read
          another layer's field at ANY resolution on a committed revision — do NOT optimize the band solver into
          a corner that forecloses later feedback. → history/s-decide-003.md.
  - id: d-fillmodel-001
    status: answered   # owner 2026-06-16 (s-decide-004) — fixed-proportion fill is OUT; capacity-fill-then-overflow IN
    note: |
      The coarse vertical gas distribution (how a species' sector mass splits between the 2 bands) is an OWNER
      gameplay/feel decision, NOT a builder detail (the ADR-0005 BS4 delegation was the defect). DECIDED:
      (1) NO fixed proportions. The built `LowerShare = total·eff/(eff+16)` (80/20 for the heaviest cold gas,
          AMOUNT-INDEPENDENT — a puff still throws 20% to the ceiling) is REJECTED outright — «их вообще не должно быть».
      (2) Model = CAPACITY-FILL + OVERFLOW (owner's mental model): the floor band fills toward its capacity FIRST
          (little gas → thin low layer, interface low; more → interface rises), the excess OVERFLOWS to the upper
          band. AMOUNT-DEPENDENT by construction. Heavy fills from the floor, light from the ceiling; temperature can
          FLIP which band is "first" (the frozen eff law stays). Multiple species layer by density (heaviest at the
          very bottom). 2 bands coarse is OK for now; smooth sub-band fill = the fine tier (Wave 3).
      (3) Deferrals to later waves (owner-confirmed, do NOT build now): Q1 opening-size→flow-rate SHOULD influence
          (simple now, the curve a later wave; built t-1 uses a FIXED kP = size-agnostic); Q2 explosion-magnitude→
          opening-size (later, with destruction); Q4 breach repair/seal (later, maybe never). Q3 = far breaches are a
          single "opening-size NUMBER" (shape does NOT affect gas far away — owner agrees); a breach CAN drive OTHER
          layers later (temperature transport / air currents) — a SEPARATE axis from geometry, the layered arch extends.
      → re-PLAN the fill model + per-band temperature in the t-1 rebuild (NOW.next). This re-opens t-1.
  - id: d-return-reconstruction-001
    status: deferred   # owner 2026-06-16 (s-decide-004) — Wave-3 design capture; deep-research deferred to Wave-3 shape
    note: |
      On player RETURN to a room, the gas state must reflect realistic spread (NEVER "enter → instantly all filled").
      KEY: the coarse tier is ALWAYS-ON whole-level (I15) — the room keeps filling at the source's RATE × elapsed time
      while the player is away, so the correct AMOUNT on return is already free (Wave-2-handled, not stale, not
      instant-full). The INTRA-room FRONT (a cloud growing from a corner source) is the FINE tier = Wave 3, and equals
      the owner-signed band-handoff (GG4/OR4, d-bandhandoff-001): track the SOURCE (location/strength) EXACTLY +
      reconstruct local detail on entry. REFINEMENT (owner-accepted critique): do NOT store a SEPARATE "fill/unfolding
      equation" (= 2nd source of truth = drift) — the coarse amount IS the truth; reconstruct the fine front from
      (source position + coarse amount). Lazy-LOD optimization (Wave 3): keep fine detail while a room is actively
      filling, collapse to coarse-only once filled (gas does NOT evaporate, for now — keep the seam extensible). A
      focused deep-research on cheap off-screen field reconstruction / lazy field seeding / analytic front propagation
      is DEFERRED to the Wave-3 shape (owner: «deep ресёрч очень не нужен» now). Relates to s-arch-003 lazy-seeding.
  - id: d-roomfull-001
    status: answered   # owner 2026-06-17 (s-work-008, c-work-003, owner present) — closed level + capacity + back-pressure; sink + doors-break-under-pressure = named future seams
    note: |
      What a room does when FULL (the A10-3 terminal-overflow finding from t-1 — t-1 guarded CONSISTENCY; a no-sink
      room was terminal-on-overflow: clearing the source did not restore liveness). DECIDED (owner «противодавление …
      самое логичное, самое хорошее решение»):
      (1) MODEL = closed level + per-room CAPACITY (bound to real DA geometry in t-2) + BACK-PRESSURE. ONE rule: a cell
          never exceeds its capacity — every flow/inject clamps to [0,capacity]. A source cannot push into a full room
          (it idles); a saturated CLOSED region SATURATES AND HOLDS. No terminal throw, no int overflow, no negative,
          mass-exact (capacity is a chosen number ≪ the int domain; internal math already uses long). Back-pressure is
          the rule for "gas that didn't fit": gas already in the level is conserved (stays, capped); a source/faucet
          simply doesn't spawn what has no room — no conserved budget violated. = the t-2 LIVENESS done_when.
      (2) NO SINK this wave (owner «со стоком согласен» = defer). Owner found a real risk: an always-on sink → the gas
          all leaks away → the threat self-resolves (anti-climax). So gas does NOT leave the level in t-2; the level is
          closed and saturates-and-holds (still demos breach→flow→hold fine).
      (3) NAMED FUTURE SEAMS (recorded, not built — owner asked to keep): (a) gas VENTS to space/vacuum/vents — a
          DOUBLE-EDGED mechanic (relieves gas BUT decompression kills), needs feel-design (rate, which rooms) → later
          wave; (b) pressure BREAKS doors/partitions by their strength → new breach → flow = destructibility (R9) →
          later wave (back-pressure already stores the pressure number that feature reads); (c) >2 bands / sector
          subdivision for big rooms/hangars = a configurable knob, Wave 3+ (2 bands now keeps the just-validated scale
          numbers; more bands help VERTICAL smoothness, sub-sectors help a HANGAR's horizontal coarseness). Owner
          also accepted: amount-on-return = coarse always-on (this wave, GG4 coarse half); the FINE intra-room cloud
          shape (corner front) = Wave 3 («понял, что это будет в волне 3, окей»). → carried into c-exec-006.
  - id: d-crossband-inv-001
    status: answered   # owner 2026-06-17 (s-decide-005) — accepts the disposition: per-band model is correct, Codex P1 fix rejected as oscillating; per-species TEMPERATURE = the future seam
    note: |
      Codex P1 on the t-1 REBUILD (CoarseBandStep.Settle, capacity-fill+overflow): the lower band fills
      densest-first in species-id order throttled by the LOWER band's OWN temperature, NOT a per-species
      cross-band `eff` sort — Codex claimed the latter is needed for hot-heavy-past-cold-light inversion.
      DECIDED (owner «принимаю рекомендацию»):
      (1) NO code change — the per-band capacity-throttle + species-id fill is the COHERENT model and matches
          d-fillmodel-001 ("layer by density, heaviest at the bottom"; within a band `eff` is monotone in id,
          so densest-first == id order). Codex's cross-band-`eff` sort is REJECTED: temperature is a per-BAND-cell
          property, so a cross-band per-species sort has NO fixed point — period-2 oscillation (re-verified this
          session in code + arithmetic: eff(0,260)=1 vs eff(3,0)=8 → swap → eff(3,260)=1 vs eff(0,0)=64 → swap
          back, against CoarseBandStep.cs:187-252 + the frozen BS4 eff law — NOT taken on the executor's word).
          Applying the reviewer's fix would INTRODUCE the bug.
      (2) The frozen BS4 prose "a hot heavy species inverts past a cold light one" over-specifies that incoherent
          cross-band behaviour and is UNTESTED (the throttle delivers "hot floor drives gas up"; it does NOT
          deliver "this gas overtakes that specific colder gas"). NARROW it to the per-band-throttle model — but
          BS4 is builder-IMMUTABLE/frozen, so the narrowing is a PLANNER action at the t-2 SHAPE (owner present),
          NOT a t-1 builder edit. ADR-0005 §Verdict already records the disposition + flags it home.
      (3) NAMED FUTURE SEAM (recorded so it is not lost — owner: «обязательно занести, чтобы не забыть»): true
          cross-band per-species inversion needs EACH GAS TO CARRY ITS OWN TEMPERATURE (per-species temperature),
          not the band's. DISTINCT from the per-species buoyancy RATE seam BS4 already names; both sit on the
          per-species-buoyancy line. Add per-species temperature to the BS4 named seam at the t-2 shape.
      (4) Kill-gate VERDICT (ADR-0005 §Verdict = PASS_WITH_NITS; 198/198, mutation 76.76%, fresh-session G5 PASS,
          owner multi-quantity legibility PASS) is owner-CONFIRMED → merge-go. The FORMAL t-1→t-2 close lands when
          the executor RESULT comes home (paste it to close c-exec-005/t-1). See memory
          gascoopgame-buoyancy-perband-ratified + ADR-0005 §Verdict. → history/s-decide-005.md
      (5) RATIFIED at the t-2 SHAPE (s-work-008, owner present): the BS4 narrowing + the per-species-temperature
          deferral are CONFIRMED and carried into c-exec-006. FORWARD-CONSTRAINT added (Р2): temperature stays an
          INDEPENDENT layer, readable at any resolution on a committed revision; never fuse it into the gas store so
          as to foreclose a future per-species temperature (a room-temperature map ALREADY exists today — deferring
          does NOT mean "one temperature everywhere"). ⚠ GUARD (3-agent verify wf_1b929b4e, owner-eyes-confirmed):
          the c-exec-005 openspec change-folder delta (specs/sim-core/spec.md:82, criterion b) STILL restates the
          dead cross-band claim ("displaced to the UPPER band … PAST A COLDER SPECIES"); the live canonical spec is
          grep-clean → applying the delta VERBATIM would RE-INJECT it. c-exec-006 narrows criterion (b) in the SAME
          pass (per-band-throttle truth, drop "past a colder species"; tests L7/BS10(e) untouched).
  - id: d-returnfidelity-001
    status: answered   # owner 2026-06-18 «ОК» (this session) — off-screen return-fidelity bar; FINAL-impl requirement, NOT this wave
    note: |
      HARD REQUIREMENT for the FINAL implementation (NOT this wave). On player return to a room — whether the
      gas has SETTLED or is still IN MOTION (mid-spread / mid-reaction / just reshaped by a blast or wind) — he
      MUST see an APPROXIMATELY correct picture (place, spread-RATE, evolving shape, + the effect of external
      events) with NO DISSONANCE vs what a continuous per-cell sim would have produced. Math precision NOT
      required (a few — even ~10 — cells off is fine); the bar is PLAUSIBLE CONTINUITY / no jarring surprise
      (e.g. NOT "left → returned to a big hangar → it's all full" when it shouldn't be).
      NEW vs prior framing (the missed case): the player can return BEFORE the gas settles (far tier off,
      mid-spread) → the always-on coarse/far layer must carry a believable TRANSIENT (time-evolving) picture,
      not only the final settled state. 4 cases (not 2): (1) near+active → fine sim live; (2) far+UNSETTLED →
      coarse carries the transient cheaply (it already fills at a believable RATE, so a mid-spread return shows
      an honest %, not instant-full + WHERE the front is via the s-research-008 knobs + external events applied
      to the coarse state WHEN they occur); on return the room is "heated" to fine and CONTINUES from that
      front; (3) far+settled → coarse holds it, fine reconstructs; (4) return at ANY moment → plausible,
      approximate, no dissonance. Owner floated "hot room" LOD (promote room→detailed, demote→coarse when
      settled, back) = accepted mechanism; cheap path = coarse carries the transient always, promote to fine by
      proximity/return (rooms hot while far+unwatched bounded by simultaneously-active-room count — Wave-3 probe).
      RELATION: CLARIFIES + EXTENDS the COVERAGE of GG4/OR4 + d-bandhandoff-001 + d-return-reconstruction-001.
      NOT a precision raise — precision stays loose (consistent with d-bandhandoff-001 "approximately, no
      shimmer"); the NEW scope = believability must hold on the MID-TRANSIENT return + reflect external-event
      reshaping, not just the settled cloud (assistant over-stated it as a precision raise earlier this session →
      corrected, owner: precision loose). One-source-of-truth holds (d-return-reconstruction-001): coarse =
      truth, fine = reconstructed-consistent; determinism makes "what would have happened" a well-defined target.
      FORWARD-CONSTRAINT (cheap, not code now): do NOT architect the coarse layer to represent only the SETTLED
      state / only room-totals — it must carry the transient + front position + applied external events at enough
      fidelity for an indistinguishable-to-the-eye reconstruction. Subordinates the s-research-008 knobs
      (graph-of-fronts / sub-sectors / checkerboard / source-seed): chosen by whether they let the TRANSIENT
      reconstruction avoid dissonance, not for precision. Independent ChatGPT deep-research cross-pass
      (owner-run) CONFIRMED the s-research-008 verdict + adds a "sparse regular checkerboard" probe variant
      (determinism-simpler than conformal cut-cells); both agree decisive evidence = the half-day integer probe.
      SCOPE: FINAL-impl / Wave-3 design bar — binds the Wave-3 shape (triage with the probe menu). Active bet
      t-2/c-exec-006 (2-band day-one) UNCHANGED + NOT blocked (G1). → history/s-decide-006.md
  - id: d-wave2-seq-001
    status: answered   # owner 2026-06-19 (s-work-010, present) chose C — run t-3 ∥ t-4 in PARALLEL (G1 = 2 active, OK). «давай рассмотрим возможность запуска параллельно … я бы сейчас сфокусировался бы на 2х задачах». Both legs framed + hardened + OPENED (c-exec-007 / c-exec-008). Owner added R1/R2/R3 for t-4 (wire real DA / guide-loop-when-no-MCP / owner-run=close-gate) — see s-work-010. The parallel-safety boundary (read-model frozen + file-ownership split) makes C non-colliding + reversible (pause t-3, t-4 unaffected).
    note: |
      t-2 is CLOSED; t-3 (temperature-layer extensibility proof) and t-4 (player-legible render terminus) are BOTH
      unblocked and parallelizable (t-4 depends on t-2's level+breach+RN1 read-model, NOT on t-3; t-3 depends on t-2).
      QUESTION: which leads, or run both in parallel (G1 allows ≤3 active tasks)?
      (A, RECOMMENDED) t-4 render terminus FIRST — the first human-legible artifact off the REAL coarse sim; breaks
          pre-mortem #2 (Wave 1 left zero player-facing output) + feeds g-2f8c's fixed 2026-08-31 page date; SOLVER-
          AGNOSTIC (reads RN1) so it does not wait on t-3. Bad, because: the 'a 3rd independent layer plugs in without
          core edits' extensibility claim stays argued-not-exercised a little longer.
      (B) t-3 temperature layer FIRST — closes the 'seam exercised not argued' half (XL2) earliest. Bad, because: it
          produces nothing the owner/audience can SEE and does not move the 08-31 commercial clock.
      (C) BOTH in parallel — t-4 (Unity/visual work-stream) ∥ t-3 (engine layer). Bad, because: two concurrent
          executor legs is more orchestration load on a solo owner — only worth it if clearly running ahead.
      Recommendation = A (t-4 leads; t-3 parallel only if capacity). Resolve at the next work session's PLAN open.
  - id: d-t3-defer-001
    status: answered   # owner 2026-06-19 (s-work-013) «C» — DEFER t-3/XL2 to Wave 3; build only t-4 this wave.
    note: |
      Raised by the t-3 builder PLAN: the CALL (c-exec-007) frames t-3 as a NEW demonstrative layer (temperature stays a
      coupled plane), but ADR-0005 / ADR-0007 Decision 5 say "temperature as a SEPARATE registered layer reading gas via
      the inter-layer read seam = the t-3 XL2 obligation". RECONCILED first-hand this session (against the ADRs + the
      VERIFIED §CONTRACTS): the ADR wording is STALE — converge-verify Finding F2 already caught it and d-tempfeedback-001
      resolved it. XL2 (verified contract) = a NEW demonstrative layer, gas byte-identical, no core edits = exactly what
      the CALL implements. DECOUPLING temperature so gas reads it back = the temperature→gas FEEDBACK, owner-DEFERRED
      (post-g-d3a8). Deep reason it can't be free now: temperature is an INPUT to the band-solver (per-band throttle,
      frozen in the LOCK); decoupling forces gas to read temperature via the committed-revision seam = a 1-tick lag →
      different band-split → breaks the frozen goldens + reopens the LOCK (the only alternative — a live same-tick read —
      breaks determinism). So the builder's "option 2 = decouple now" is OFF the table (contradicts d-tempfeedback-001 +
      reopens the LOCK).
      OPTIONS put to the owner: (A-refined) keep t-3 but pick a PLAUSIBLE byte-identical demo layer (not a counter);
      (C, RECOMMENDED) DEFER t-3 — prove extensibility FOR-REAL in Wave 3 with the first genuine 2nd layer (the temperature
      decouple + feedback), focus this wave on t-4 (the visible 08-31 artifact). OWNER CHOSE C.
      CONSEQUENCES (applied this session): t-3 → dropped (→ Wave 3); c-exec-007 → cancelled; done_when #5 reworded to NAME
      the deferral; cut_list + wave_plan updated; t-4 (c-exec-008) is the SOLE Wave-2 executor leg. Temperature-decouple
      stays Wave 3 / g-d3a8 (with feedback). FORWARD: correct the stale ADR-0005/0007 "separate-layer = t-3 obligation"
      wording home-side (fold into the Wave-3 extensibility leg, or a tiny cleanup). → history/s-work-013.md.
  - id: d-sandbox-001
    status: answered/active — SEQUENCE EARLY (Wave A of the A+ breakdown), owner 2026-06-20 «нужен достаточно быстро»   # owner 2026-06-19 (s-work-014) — the test/authoring HARNESS is a SEPARATE serious deliverable; was "after wave 2", now Wave 2 is CLOSED and the owner wants it SOON + the §G(+4) probes NEED it → it leads the A+ breakdown (Wave A). REAFFIRMED+SHARPENED 2026-06-20 (s-review-002 follow-up, owner voice — R3). Build via research(best-practices)→shape, but EARLY, not "post-everything".
      OWNER CAPABILITY LIST (R3, 2026-06-20 — this is the requirement, NOT just examples): 1–2 scenes; (a) test MULTIPLAYER with chosen conditions; (b) test GAS-SIM; (c) generate ANY level via the level-gen system (SnapGridFlow now, later + the PGG plugin INSIDE the same seam); (d) SPAWN gas at any place / any amount; (e) PAUSE the simulation; (f) everything works CONVENIENTLY; (g) take a DATA SNAPSHOT at a moment → ask Claude to analyze it; (h) DESIRABLE-not-required (only if cheap + non-hanging): a separate Unity-MCP-adapted scene for Claude OR Claude can run MOST functions in the owner's scene too. Owner has 1 inspector plugin installed, can buy more add-ons, thinks that suffices. Discipline (from d-sandbox-001 note + memory): config-as-DATA / saved seeds (not scene-per-test), ONE/few parametric harness scenes, deterministic-by-seed, owner-tweakable + MCP-drivable + structured logs, anti-scene-sprawl convention.
    note: |
      TWO linked owner steers (this conversation):
      (1) t-4 IS NOT a Steam artifact. «грубую симуляцию на витрину не вешаю; для меня как доказательство окей; выкинь
          Steam-требование из головы; вначале базовый функционал». → t-4 RE-SCOPED to an INTERNAL coarse-sim PROOF /
          inspectable visualization (real DA via the c-exec-010 derive-id gate + reads RN1 + owner-confirm-it-works);
          DROP the stylization / RN2-showable / footage / owner-gamer-eye-Steam / 08-31 bars. Steam-page timing → the
          marketing track g-2f8c (gated on real visuals/gameplay; already de-coupled from Wave 2 by q-foundation).
          c-exec-008 must be RE-ISSUED to this proof scope. pre-mortem #2 (do not go dark) is answered by the internal
          inspectable proof + the harness below, not by a public artifact now.
      (2) The serious TEST/AUTHORING HARNESS (sandbox) is its OWN deliverable, built AFTER wave 2 closes (owner: t-4
          context too full; cramming it into t-4 was a bad idea). NOT one scene — a disciplined TEST APPROACH (possibly a
          few scenes). HOW = delegated to me («полностью доверюсь … не знаю лучшие практики»). Pain to kill (owner's past
          gamedev): a PILE of hand-built test scenes + recreated configs = chaos. Recommended best-practice DIRECTION (to
          be detailed at the research→shape, NOT locked here): config-as-DATA (saved seed/config assets, version-able)
          over scene-per-test; ONE (or few) PARAMETRIC harness scene; deterministic-by-seed (reuse our core); owner-
          tweakable inspector + save-as-config; MCP-drivable by the builder (load config → run N ticks → dump a structured
          log/artifact it can read); a folder/naming CONVENTION so scenes/configs do not sprawl. EXAMPLE capabilities the
          owner floated (his words: examples, NOT requirements): hand-tweak, save a file, builder reads a log, run by
          ticks. APPROACH: research(best-practices) → shape → tasks, in the Wave-3 era (its own first leg / interstitial).
          Owner: «эта задача у нас есть, её надо ставить».
      → recorded so it is tracked + timed; framed properly post-wave-2. → history/s-work-014.md.
  - id: d-corefoundation-001
    status: answered   # 2026-06-19 (s-work-015) — assessed the coarse Core as a foundation for the owner vision (wf_16158bde, 4 agents + red-team). VERDICT: do NOTHING to the Core now (SAFE); the keep-open invariant is the only Wave-2 obligation and is ALREADY met; the Wave-3 additions are probe-gated extensions, not a rewrite.
    note: |
      Owner doubted the coarse sim is too crude / non-extensible for his vision (exact spawn place/size; plausible
      on-return cloud; no false over-mix in a big room; reactions everywhere). FIRST-HAND code map (CORRECT, red-team
      re-verified): today the Core keeps gas only per (sector,band,species) — NO finer-than-room source POSITION
      (Source struct = {Sector,Band,Species,PerTick}, XY thrown away at SetSource), NO intra-room horizontal split
      (FromTopology = 1 sector/room; RectDecomposition built+tested but NOT wired; SubdivisionIntent carried but
      ignored), NO advancing FRONT, NO gas-gas reaction (ReactionLayer is a toy over the legacy RoomGraph). So
      exact-place / on-return-cloud-place+size / no-false-over-mix / reactions-everywhere-at-fidelity are NOT done by
      the current Core — the owner's instinct re the LIMITS is RIGHT.
      BUT the synthesis over-claimed "NEEDS-CORE-CHANGE-NOW"; the RED-TEAM downgraded it (binding):
        - SUPPORTED-NOW: V1 honest-everywhere; V3 no-merge-to-one-number (K species tracked separately, never collapsed);
          V6 AMOUNT/RATE (always-on coarse + per-room capacity/back-pressure → "left, returned, whole floor filled" is
          structurally prevented at room granularity).
        - The Wave-3 seams (S4 source-seed / S2 sub-sectors / S3 graph-of-fronts) are the owner's OWN signed deferrals
          (d-roomfull-001(3c): subdivision = "Wave 3+ configurable knob", «2 полосы сейчас сохраняют проверенные числа»;
          early_finish: pull-forward-if-ahead = not now) + the 17-agent s-research-008 confirms 2-band/1-sector is
          correct day-one and triages S2/S3/S4 to the Wave-3 shape behind half-day probes NOT yet run.
        - d-returnfidelity-001's forward-constraint is a KEEP-THE-DOOR-OPEN obligation (don't bake in 1-sector/
          settled-only), tagged "cheap, not code now" — and it is ALREADY met: wire/hash key off sector COUNT (not
          1/room); the document carries SubdivisionIntent + TopologyAnchor{LocalX,Y,Z}; RectDecomposition is built.
        - Source XY is RECOVERABLE upstream (level generator / the currently-empty TopologyAnchor) → the in-Core
          source-seed is a Wave-3 ADDITION, not an irrecoverable loss → NOT a rewrite. All additions ride ALONGSIDE the
          LOCKed planes (achievable-on-LOCK = YES; coarse mass stays the single truth, no 2nd fill equation).
        - G1 + "don't break what works": the active bet is t-4 (internal proof) on a gate-green LOCK-frozen baseline —
          changing the Core for a Wave-3 benefit is out of scope.
      CONCLUSION (doNothingNowIsSafe = TRUE): change NOTHING in the Core for t-4. THE WAVE-2-BINDING KEEP-OPEN
      INVARIANT (= the Wave-3 entry bar): no solver/wire/hash invariant may assume "1 sector per room" or "settled-only";
      and source XY is lossy at the SetSource boundary today but recoverable upstream — supply it to the Wave-3
      reconstruction, do not bake the loss in. HONEST CAVEAT: even with sub-sectors the coarse layer reacts
      per-(subsector,band) — the literal "must NOT react as if co-located" is fully delivered only by the FINE per-cell
      tier (Wave 3). So exact-place / on-return / no-false-over-mix / reactions-at-fidelity are inherently Wave-3 work,
      reinforcing the downgrade. → history/s-work-015.md.
  - id: d-grid-sgf-001
    status: answered   # owner-ack 2026-06-20 (recorded s-work-016) — the t-4/c-exec-011 build wired the REAL DA via SnapGridFlow (SGF), NOT the "Grid" the spec/ADR R1 named. Owner chose SGF (designed modules + verticality). The "real DA" contract is met IN FACT (real level, geometry-derived StableId, 2 distinct conformant ProfileHashes); the DEVIATION is TEXT-only.
    note: |
      Owner R1 (c-exec-008/011) + the product-repo spec/ADR named a GRID Dungeon Architect; the builder wired SnapGridFlow
      (owner-chosen). The builder did NOT edit acceptance criteria (by design — "билдер критерии приёмки не правит"). ADR-0009
      (home-side, GasCoopGame) records D5 = SGF + the cuts. OWED home-side reconciliation (NOT the writer's job; carried into
      the review / a tiny home cleanup): re-spec R1 Grid→SGF + openspec apply/archive of
      openspec/changes/c-exec-011-t4-coarse-gas-render/. Folds in alongside the already-queued ADR-0005/0007
      "separate-layer = t-3 obligation" stale-wording cleanup. → history/s-work-016.md.
  - id: d-rn2cut-001
    status: answered   # owner-ack esc-t4-rn2-cut-2026-06-19 (recorded s-work-016) — the RN2 MACHINE-vision blind-check floor (the frozen N-of-M vision-agent gate, c-exec-008/011 acceptance gate (a)) is CUT; t-4 readability is judged by the owner's EYE (he signed LOOK L1-L3). Overrides the direction-frozen dual-gate + the R3 "machine + owner-eye" axis down to owner-eye-only.
    note: |
      The proof re-issue framed TWO acceptance gates: (a) a MACHINE RN2 blind-check (frozen ground-truth schema + N-of-M floor,
      scored from RN1) and (b) the render-slice existence row. The owner cut (a) — readability is his eye, not a vision-agent.
      Owner-acked (esc token 2026-06-19). RECORDED, not silently dropped. CONSEQUENCE for the REVIEW (G5): the binding
      done-evidence for t-4 readability is now owner-EYE-only (no machine floor) — the review must REFUTE on that basis (is
      owner-eye sufficient given the LOOK caveat "basic works, NOT model-final"?) and decide whether the cut weakens the
      Wave-2 verdict. → history/s-work-016.md.
  - id: d-gasmodel-redesign-001
    status: answered — owner chose дорога A+ 2026-06-20 (review s-review-002 follow-up). Next g-9c41 bet UNBLOCKED, but the owner asked that the BREAKDOWN be planned CAREFULLY first (research+map of the whole A+ construction into a de-risked, Unity-verifiable wave-tree) before any wave is shaped — see `next`. The old Wave-3 plan stays SUPERSEDED by the gas-model doc §K.   # RAISED by the owner 2026-06-20 AFTER seeing the t-4 render (recorded s-work-016) — a fundamental gas-MODEL redesign. Put to the owner with options A+/B/C + rec A+ at review s-review-002; owner ratified A+.
      OWNER A+ RATIFICATION + STEERS (2026-06-20, voice, recorded this session): R1 дорога A+ APPROVED (sees the risk; bets it goes FASTER — 2 waves landed faster than expected, clear requirements now, Claude Code writes fast, ~12h/day, many tokens). R2 the BREAKDOWN is the CRUX + his stated #1 fear: «не сделать волну, за которой всё сделается» (no catch-all wave) + split into MINIMAL-but-FINISHED Unity-verifiable pieces (each provable by him in Unity, not a trifle) + «прям очень такой ресёрч как это всё разбить... детально каждый кусок со всеми рисками, чтобы не оказаться что в ядре что-то жёстко не так и всё переделывать»; spec covers it well, implement the spec; floated ~3 split (Grid / gas-sim / T3). R3 the TEST SANDBOX (d-sandbox-001) is needed SOON + clearly-built: 1–2 scenes; test multiplayer with conditions; test gas-sim; generate ANY level (level-gen, later + PGG inside); spawn gas anywhere/any amount; PAUSE the sim; convenient; snapshot data → Claude analyzes; DESIRABLE-not-required (only if cheap / non-hanging): a separate Unity-MCP-adapted scene for Claude OR Claude can run most functions in his scene; he has 1 inspector plugin, can buy more, thinks it's enough. R4 STOREFRONT — «хер с ней» for now: order = build the plan → visualization → THEN think storefront; he writes lore/mechanics in parallel himself; visual should exist by the deadline. R5 PARALLEL VISUAL track (GASG): run it in parallel (architecture is now defined, visual is separate), SECONDARY priority, ~4 wk, needs a VERY big research (many requirements); do NOT forget GASG TYPES / meta-types (their own piece). R6 the 2026-07-24 wall STAYS the extreme deadline (move the tail, not the wall); to hit it → the parallel visual. R7 his estimate ~3 dense weeks for the core impl (says NOT the optimistic scenario). R8 «не спеша, очень внимательно построить планы — важнейший этап». R9 (reactions) coarse=approximate-coincidence OK; near player = visible mixing + TELEGRAPH (blink/glow «вот-вот рванёт») + PREP WINDOW, NOT instant. R10 (rarity) NOT «few guaranteed» — expect PEAKS (esp. chain reactions); requirement = graceful degradation + deterministic awake-set under a spike. R11 (gas count) catalog of TYPES = UNLIMITED («бесконечно» = types, NOT concurrent reactions); per-LEVEL ~16 / max ~32 TUNABLE; per-ROOM typically ≤4 (portal-bounded) but NOT guaranteed → a REACTION QUEUE on overflow; recorded as RISK R-GASCOUNT-PERROOM. R12 (CAPACITY DE-CONFLATED — important) the s-work-016 «убрать ёмкость+перелив» CONFLATED two things; owner CONFIRMED he never wanted ROOM capacity removed: (A) the 2-band fill-then-overflow split (d-fillmodel-001) = what A+ changes (his «continuous weight» → smoother weight+temp settling over more layers, not float); (B) ROOM capacity + back-pressure (d-roomfull-001) = KEPT. The «remove capacity» owner-confirm was a FALSE question from the conflation — closed. All R9–R12 folded into work/aplus-wave-map-v1.md (§4 RESOLVED, §4.1, §4.2 RISK register). → carried into `next`.
      R13 (2026-06-20, owner «да» ×): A+ BREAKDOWN APPROVED + Wave A APPROVED. Breakdown ran (wf_de2cf689-047: DAG + 5 wave
      cards + Wave-A detail + 2 critics) → work/aplus-breakdown-v1.md (critic verdict: sound plan/right shape; grow-vs-rewrite
      code-verified; 5 hardening fixes folded = lock keep-open seams EARLY). g-9c41 RE-SHAPED to Wave A (active_bet above):
      LAB + DE-RISK WALL (t-1 sandbox → t-2 §G+4 probe-gate kill-gate → t-3 host-migration spike); next = c-exec-012 (t-1). The
      gas-model redesign decision chain (A+ ratified → breakdown → Wave A) is now CLOSED into the active bet; this decision stays
      as the durable record of WHY the core was re-formed. → history (this session) + work/aplus-breakdown-v1.md + work/aplus-wave-map-v1.md.
      ARCHITECTURE DEEPENED (2026-06-21, s-research-011 — co-creation + 4 workflows): A+ road конкретизирована в
      owner-approved архитектуру — D1 input-lockstep (netcode LOCKED; only inputs on wire; per-machine CPU the only
      limit; this CHANGES the replication model vs the host-broadcast LOCK assumption — planner must reconcile); D2
      LOD=cell-size (one model; bucket=room-sized cell, far/small only); D3 near=full 3D; D5 big/important rooms stay
      authoritative+spatial (hold state on return); D6 loot=gas-reached-it (%-far only); D7 reactions everywhere; D9
      sparse dominant-gas (not per-gas planes); D10 chemistry collision table; D11 real-height via 3D-near; D12
      reusable-engine DROPPED (game-first); D13 carve-corridor CUT. Full spec + mechanic×tier proof + seams + de-risk:
      work/gas-model-architecture-decision-2026-06-21.md. Planner reconciles the Wave plan with this (esp. netcode
      shift + cell-size LOD); decides timing/sequencing. Decision stays answered (A+); this is its durable architecture record.
    note: |
      Owner, having SEEN the coarse sim render, wants to REDESIGN the gas MODEL itself (his framing):
        - continuous gas WEIGHT → continuously drives height / settling speed (not 2 discrete bands);
        - gas as a continuous SPACE/FIELD, NOT fixed "rooms" + 2 fixed bands;
        - a FREE number of gases (no fixed wire-format cap on species);
        - DROP the "capacity + overflow / finite source" crutch (the d-fillmodel-001 / d-roomfull-001 model).
      This is a CORE REDESIGN that REOPENS the LOCK (ADR-0004 §LOCK / ADR-0005) — the very model frozen + proven gate-green by
      t-1/t-2/t-5. The builder correctly did NOT touch physics: t-4/c-exec-011 rendered the EXISTING model HONESTLY; the
      redesign is a SEPARATE planning leg + its own ADR, NOT a t-4 change. The proof did its JOB — it informed the owner, who
      now wants better (textbook review forecast-surprise: the model met its bar, and SEEING it changed the requirement).
      TENSION to surface LOUDLY at review (memory: don't-break-what-works + explain-in-waves): a redesign re-does a large
      LOCK-frozen, gate-green core (t-1 band solver, t-2 replication, t-5 hardening, ADR-0004/0005) — NOT free; weigh
      continuous-field value vs the cost of reopening proven work, and whether it belongs to Wave 3 or a re-frame. Relates to
      d-corefoundation-001 (the coarse Core's known limits) and the Wave-3 fine-tier seams (S2 sub-sectors / S3 graph-of-fronts
      / S4 source-seed) — some of what the owner wants (gas-as-space, front position) OVERLAPS fine-tier work already triaged
      to Wave 3. The review must bring OPTIONS (full redesign / Wave-3 fine-tier-first / a bounded continuous-field probe) +
      a rec — NOT pre-commit. → history/s-work-016.md.
      RESEARCH RESULT (2026-06-20, s-research-010): the owner ran the separate discussion + brought back a result, now authored in
      full at work/gas-model-design-full-2026-06-20.md (immutable source: work/gas-model-research-result-2026-06-20.md). OUTCOME:
      недовольство = МОДЕЛЬ (not picture); RECOMMENDATION = dorога A+ (graph-base + grown layers), NOT B (continuous-field rewrite)
      — B re-opens the solved network-determinism problem. «Убрать ёмкость+перелив» REINTERPRETED (the visible face of real pressure
      + intentional "threat doesn't self-vent"; remove only WITH a replacement law) + «free gas count» DISCIPLINED (capped active
      gases per node + hard wire cap). §G LOAD-PROBES are MANDATORY before any bet (cascade depth-identical on 2 machines; 8 hot
      bubbles round-robin; integer incremental Dijkstra on breach; mass-conservation RED-test). OPEN chunks incl. HOST-MIGRATION
      (host loss = death of a 4-8 session). Construction LARGELY rides existing repo + Wave-3 plan (§K, each claim NOW.md-grounded)
      → likely A+ grow, not a from-scratch rewrite. Faithfulness verified (3-audit pass wf_c237a811: no drops, repo-claims grounded,
      Claude-overlay provenance fenced). Status STAYS open — owner ratifies A+/B/C at the review; plan by the doc's chunks. → history/s-research-010.md.
      REVIEW FINDINGS (2026-06-20, s-review-002 — independent adversarial check, 3 angles, code+math, NO dealbreaker):
      дорога A+ CONFIRMED + strengthened on all axes. (a) Network-determinism is SOUND and PROVEN-IN-CODE (FloatMutant
      CR3 control, followers reconstruct-not-recompute, host+2c bit-exact under fault) — B would knowingly discard
      proven Wave-1/2 work; «continuous field deterministically replicable cheaply» is the unsolved-expensive problem;
      C (1–2-wk net probe) will likely just rediscover «must integer-discretize = A+ with extra steps». (b) §K
      repo-overlay 9/11 claims hold EXACTLY vs code (2 over-statements, not fabrications: «sillZ»≈2-band quantization;
      real-DA proven only at 6 sectors); A+ is honestly «grow the proven core», NOT a disguised rewrite. (c) §G probes
      are real+cheap but INCOMPLETE — 3 of the 6 new A+ assumptions have NO probe → ADD 4 MANDATORY before any A+ bet:
      (i) two-machine awake-set/sleep-schedule DETERMINISM (highest silent-desync risk — A+'s perf rests on sleep, the
      LOCK forbids exactly this bit-exact break); (ii) resident-gas-damage RED ledger (a fixed correctness law shipped
      with no probe); (iii) confirmed-colocation FALSE-reaction probe; (iv) real-DA(SnapGridFlow) at hundreds-of-rooms
      scale (today proven only at 6 sectors). SPLIT host-migration (§H — host loss = death of a 4–8 session, the
      value-prop killer) out of the benign save/load cut; consider a «host dies → session survives» spike in the FIRST
      A+ bet. The LOCK barrier [7,chunkCount] has only 4 free plane-keys (2..5) before temperature at 6 → «capped active
      gases/node + hard wire cap» must be a CONCRETE NUMBER at shape (a new plane = a SURFACED LOCK-EXT per ADR-0007).
      A+ is multi-wave → re-shape PAST 2026-07-24 (move the tail, not the wall). COMMERCIAL TENSION (surface loudly):
      Wave 2 WITHDREW the storefront footage guarantee (terminus → non-showable internal proof) → the 2026-08-31 page /
      Oct-Fest gameplay half is now UNSOURCED if the next bet is footage-less core work → owner fork: next showable
      artifact from the A+ front/place layer (weeks) vs a parallel cheap visual pass on the EXISTING model. → history/s-review-002.md.

next: |
  S1 FORCED-FLOW SLICE is DELIVERED + CLOSED (s-work-023, work play): c-exec-015 scope S1a merged GasCoopGame
  origin/main @0adae83 (970 green), tools/check.ps1 -Deliver GREEN on dev, fresh-session G5 (Sonnet, different family)
  COULD-NOT-REFUTE, Codex by-class CLEAN, owner-eye «работает». Delivered the forced-flow PRIMITIVE inside the locked
  integer model: decaying directional-bias impulse-events on the S0 face-flow → jet-emitter (forward push + lateral
  confinement) + ВЫБРОС + ВЕТЕР/fork-split + one-way VALVE + ±1 bias-floor + ledger-honesty + one curated scene +
  class-wide int*int overflow scan. The bet ROLLS to S2.

  ARCHITECTURE FORK RESOLVED (d-clouds-fork-resolved-001, owner «точно у игрока, грубо везде» 2026-06-28): an
  UNCOMMITTED draft (work/gas-arch-reqs-matrix-2026-06-26.md, surfaced by an adversarial sequencing check) argued the
  locked input-lockstep integer grid STRUCTURALLY cannot do R7/R12 (a 50cm-precise reaction / level-spanning split in a
  room with NO player, EVERYWHERE) — far-rollup collapses a room to a position-less SUM (canon :79), reactions read
  coarse totals (:85) — and recommended candidate E (host-state-sync float clouds, un-signing ADR-0010, the biggest
  migration). Facts VERIFIED first-hand against the committed canon; the prior cloud-vs-grid analysis only ever evaluated
  clouds on cross-CPU determinism (never host-authority) so E was genuinely UNDER-evaluated, NOT settled drift → put to
  the owner as the pivotal requirement question. OWNER: deep interaction = full precision where the player is (+2-3
  Ведро-3 rooms), coarse events everywhere else — which the canon AS-LOCKED already delivers. => lockstep STANDS, NO
  ADR-0010 un-lock, NO architecture change; the matrix is moved to work/archive/ as NON-ADOPTED history. CARRY: if
  host-authority is ever reconsidered, RE-RUN the cloud-vs-grid analysis on the host-auth model (its kills are
  determinism-class, void under a single host).

  IMMEDIATE NEXT = FRAME the S3 executor CALL (a fresh OS work-session frames the height/layering slice — PLAN-first, ведро
  classification). **S2 is COMPLETE**: S2b DELIVERED + merged + pushed 2026-06-29 (GasCoopGame main @adb9255; the
  load-bearing 2-VoxelField loopback harness verified first-hand — Core/Field/Determinism/; -Deliver GREEN, 923/923,
  mutation 73.51%, fresh-session G5 COULD-NOT-REFUTE + 3 Codex rounds + 5-skeptic panel; lock ADR-0002 intact) → this CLOSES
  S2 (S2a + S2b). The multiplayer-determinism FOUNDATION (2-process loopback, determinism BY CONSTRUCTION) is proven;
  **gas-as-networked-ITickInputBus-citizen = a named LARGER seam ~S4 (NOT done — scope honesty)**. S3 (canon §5) = the
  coarse FAR-tier gets a few VERTICAL layers for height-routing in player-LESS rooms (near real-height already free from S0;
  authoritative crouch-bands are §7-buried). OPEN PLAN questions: far-rollup vertical-strata count (§6 п.4) + S3-vs-S4
  far-tier sequencing. FOLD INTO the S3 PLAN: the scan-root parity-gap hardening (S2b finding — FieldStep/FieldState/
  Coarse-Chunks sit OUTSIDE both determinism scan roots; $DefaultRoots duplicated with no parity enforcement → add a
  self-test asserting every authoritative Core/Field subdir is in BOTH scans). CARRIED DEFERRALS: chunk-span retirement →
  S4 2-band far-tier cleanup; gas-as-networked-citizen → ~S4; ADR-numbering-by-track (engine 0017 vs visual dev2 0013-0015).
  RESULT applied home by a separate OS writer.

  FOUR BUILDER-RETURNED DECISIONS — ACCEPTED AS A BUNDLE (owner «весь пакет» 2026-06-28):
  • DISPLACEMENT (S1b) → CUT to backlog (d-displacement-s1b-cut-001); re-entry trigger = first body-dams-gas gameplay
    moment; the cheap cosmetic-by-canon version (off-checksum, no ADR — canon line 122) is the default if re-entered.
  • PRESSURE → read-only SIGNAL built ON-DEMAND when a consumer needs it (d-pressure-signal-on-demand-001); BASELINE
    back-pressure ALREADY ships (d-roomfull-001) — only the optional cap + true compression are deferred; the S5
    destructibility seam needs the signal by then.
  • SPARSE SOLVER → DEFERRED-UNVALIDATED (d-sparse-solver-defer-001): the active-set is near-DENSE under forcing, so the
    ~100× win is in doubt; its gating spike's FIRST job = the under-forcing benchmark; trigger = first big open hall.
  • VELOCITY / TIER-3 → RESERVED, trigger ARMED (d-gas-richness-tiers-001): «работает» was on confined cubes; open-space
    is still ~2:1 (not a sharp jet); re-trigger = one honest no-walls open-space jet look at the COMBAT slice; that look
    (if it fails) is the signed evidence for the ADR-0010 lock-crack. NO silent entry.

  RESERVED UPGRADE TIERS (d-gas-richness-tiers-001, NOT built now): TIER 2 = seeded-int lattice-gas in a few Ведро-3
  rooms for true emergent vortices (ADR-class, post-sparse); TIER 3 = fixed-point velocity (owner-signed ADR-0010,
  cracks the lock) — armed, not pulled. Libraries if tier 3: FixPointCS/FixedMathSharp (arithmetic only — no
  off-the-shelf fixed-point fluid exists). Float fluid plugins (Zibra/Obi) = cosmetic g-7e15 layer ONLY.

  ∥ VISUAL TRACK (g-7e15): c-visual-001 DELIVERED (foundation→S1→S3→S5 real-data swap, merged origin/main @9780713;
  verified first-hand 2026-06-28) — brought home from off-contour drift by s-visual-005; S6 look-development = WIP on
  dev2 @dc4c225 (pushed, not merged). Track now in LOOK-DEVELOPMENT (gas-lab → P1 levers → per-type character); forward
  spec = GasCoopGame docs/gas-visual-stage-plan.md §S6+. Process fix applied: visual slices come HOME + carry the
  «moves toward the JEWEL» owner-eye gate. next = the gas-lab leg c-visual-002 in a fresh GasCoopGame_dev_2 session.

  PENDING (carried, non-blocking): the os/engineering MAINTENANCE request (anti-substitution over-rotation + resolution
  conflation — work/MAINTENANCE-os-engineering-scope-guard-2026-06-26.md) is drafted, awaiting a SEPARATE maintenance
  session (os/** NOT touched in a live-direction session).

  PUSH: this OS repo — the writer commits LOCALLY; pushing main is owner-gated (auto-mode blocks the writer's push —
  ask the owner to push). s-work-023 commits: S1 done + S2 rolled + the 4 decisions + d-clouds-fork-resolved-001 +
  matrix archived. s-work-024 commit: c-exec-016 framed+hardened (CALL artifact + open_calls + S2 note + next).
  s-work-025 commit: c-exec-016 PLAN split applied (S2→S2a+S2b; c-exec-017 authored, c-exec-018 queued; d-s2-split-001 +
  d-s2-rng-control-na-001; imported PLAN RESULT → history). s-work-026 commit: c-exec-017 (S2a) RESULT applied — S2a
  DELIVERED on dev (verified first-hand), bet rolls to S2b; d-adr-lockstep-citation-001 surfaced; S2a dev→main merge +
  owner-eye owner-gated. ed421b5: S2a merge confirmed on main @2e24a24. s-work-027 commit: canon ADR citation FIXED
  (ADR-0010→ADR-0002, d-adr-lockstep-citation-001 answered, owner «да») + c-exec-018 (S2b) authored + adversarially hardened.
  s-work-028 commit: S2b RESULT applied — S2b + the whole S2 slice DONE (verified first-hand, GasCoopGame main @adb9255);
  bet rolls to S3; 4 findings captured (scan-root parity gap, gas-as-networked-citizen ~S4, chunk-span→S4, ADR-numbering-by-track).
  s-visual-005 commit: gas-VISUAL track BROUGHT HOME — c-visual-001 queued→delivered (S5 in origin/main @9780713, S6 WIP
  dev2 @dc4c225, both verified first-hand); g-7e15.next reset to LOOK-DEVELOPMENT (gas-lab→P1 levers→character) + felt
  TARGET (jewel/character) + PROCESS fix (come-home + «moves toward the JEWEL» owner-eye gate). Push main owner-gated.

END_OF_FILE: live/indie-game-development/NOW.md
