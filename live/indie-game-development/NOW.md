# NOW — indie-game-development

active_bet:
  node: g-9c41
  phase: |
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
  appetite: |
    Node wall = 6 weeks, hard end 2026-07-24 (G3 — fixed, NEVER extended; multi-wave — move tail waves not the wall).
    Wave-2 internal: band-solver KILL checkpoint 2026-06-30; player-facing terminus rides the 07-11→07-24 cushion to
    ~07-21. Tail Waves 3-4 → re-shaped as bet-3 after the wall.
  approach: |
    NETWORK-PROVEN real coarse band-sim on the LOCKed stream (BUILD — ranked 8.5 over 2 alternatives on EQUAL
    footing, wf_d2c5dcb5-0ab; the alternatives are its FALLBACK LADDER, not rivals). Build the genuinely-novel
    stratified multi-species coarse band solver (brief §3.1: exponential-relaxation Patankar settling + quasi-steady
    pressure/orifice closure + remainder-bucket conservation) on the HOST, reduce it DETERMINISTICALLY to the LOCKed
    integer-exact authoritative state (CR3), and replicate host→clients over the ALREADY-LOCKED Wave-1 chunked-delta
    stream (no new plane; coarse rides a new resolutionKey + the barrier-table re-size SURFACED per the LOCK's own
    SHALL-re-size). Levels come from a GENERATOR-AGNOSTIC topology seam (owner-refined s-shape-wave2): read
    (scene-geometry + semantic tags/markers) → TopologyDocument, NOT a per-generator API adapter — decouples us from
    DA's stale 2D API. DA in ROOM-COMPOSER mode places hand-made tagged room prefabs (PGG-interiors later behind the
    same seam; population OUT — d-generator-001 refined). A thin temperature layer rides alongside as a pure
    gas→temperature SINK (feedback DEFERRED, d-tempfeedback-001), exercised at COARSE scale, and a 3rd demonstrative
    layer plugs in WITHOUT core edits (extensibility EXERCISED, not argued). ONE real controlled wall-breach (GG3)
    drives a real topology change. Smallest-but-REAL config (brief §5 day-one): 2 bands / 1 sector-per-volume / all
    10 Hz / naive DA / sink. Tiers = TWO: coarse (everywhere) + 25cm detail near player (Wave 3); T3/12.5cm dropped to
    not-planned. Brief: work/research-g-9c41-core-architecture-2026-06-12-v2.md; contracts: work/converge-g-9c41.md §CONTRACTS.
  done_when: |
    A coarse gas world runs and HOLDS on a real generated level, networked-consistent, ending in a human-legible
    artifact. By the end (binding the VERIFIED §CONTRACTS acceptance by G5):
    (1) the novel coarse band solver passes the brief §7-#2 numerical battery AND converges in-budget at the
        ~3,300-sector R1 scale post-breach (headless), AND reduces DETERMINISTICALLY to integer-exact authoritative
        state (CR3 — whatever integrator PLAN picks; a non-deterministically-reduced float path FAILS the lossless oracle);
    (2) coarse band state replicates host + 2 clients PER LAYER (coarse gas AND coarse temperature) — bit-exact
        lossless oracle + bounded-divergence-converging-at-settle lossy, one shared reconstruction path (CR1/CR2/CR3);
    (3) it runs on a REAL DA-composed generated level (meaningful size, hundreds of rooms; generator-agnostic topology
        from scene+tags; IN1 + IN2 replaceability on DA alone) with a REAL controlled breach → topology change → gas
        flows (GG3 + CR2 lossless-bit-exact ACROSS the coarse topology change);
    (4) the single field-sampling oracle holds across CONSUMERS at coarse scale: a client visual read-model (OR1) and
        a client-resident far-AI ExposureQuery (OR3) on DIFFERENT peers return the SAME concentration for the same
        (point, species, committed revision); CR1 coverage-floor (no entitled gap) holds — vacuously this wave
        (interest = whole-level), anchored to gameplay-reach (V2-2);
    (5) the temperature SINK layer rides alongside via the layer registry — a 3rd demonstrative INDEPENDENT layer
        plugs in WITHOUT core edits (XL2: gas trajectory byte-identical + RNG-conservation guard; [2,4] barrier-table
        re-size SURFACED per the LOCK), the gas→temperature SINK interaction is observable (suppressed-event negative
        oracle, XL1), the coarse per-band temperature READ is exercised on a committed revision (§RESOLVED-4, V2-3);
    (6) a PLAYER-LEGIBLE artifact (crit-6 render slice ≤2wk, quantized-volumetric stylization behind the RN1 seam,
        ms-budget on min-spec): a room visibly fills bottom-up from the breach side over time, heavier gas settles
        low, the source/breach is identifiable — readable WITHOUT a debug overlay, reads as DELIBERATE stylization not
        a stub; acceptance = RN2-style blind vision-agent check (machine-readable ground truth) + owner gamer-eye
        verdict, EXCLUDING g-7e15's menace/silhouette/material bars; no-jerk/no-shimmer-EVER holds in the render
        (incl. off-screen-computed state surfacing) — owner-signed GG4/OR4 coarse half;
    (7) crit-9 scale ARITHMETIC validated vs the R1 profile (~3,280 sectors / ~7,000 band cells), bandwidth sized from
        the ON-WIRE keyframe-inclusive ~11k basis (V2-1, NOT A8.4's stale delta-only number), ≥2 independent
        recomputes + named assumptions (A8.5), aggregate-clamp-at-scale checked;
    (8) clean 1-player parity (crit-7) on the same level + the same determinism/hash discipline.
    NOT this wave (NAMED, not dropped): the T2 detailed per-cell window + the coarse↔fine no-jerk-on-ENTRY handoff +
    OR1 cross-TIER composition → Wave 3 (the fine tier is cut, so un-exercisable now); temperature→gas FEEDBACK →
    post-g-d3a8; gas-type seam GT1-GT5 + crit-4 → later wave / g-d3a8 converge.
  wave_plan: |   # rolling wave — <=3 active tasks; plan each wave knowing the last one's result
    Wave 1 (NETWORK — DONE, review MET): stream/format LOCKED, consistency proven on a toy field.
    Wave 2 (REAL COARSE SIM + GENERATED LEVELS + TEMPERATURE + LEGIBLE TERMINUS — ACTIVE): t-1 band-solver kill-gate
      (headless, scale-validated) → t-2 real DA-composed level + breach + coarse replication + single-oracle probe →
      t-3 temperature layer plugs in + coarse per-layer consistency (∥) → t-4 player-legible render terminus (∥).
    Wave 3 (DETAIL NEAR PLAYER): the 25cm T2 detailed per-cell window (cell size CONFIGURABLE + geometry-aligned) +
      the coarse↔fine NO-JERK handoff (owner «100%») + OR1 cross-tier composition + optimisations.
    Wave 4+: full destructibility, reaction MECHANISM + real gas types (g-d3a8), scale to big levels (occupancy +
      1000-object min-spec gate), frequency ladder, plume entrainment + dynamic heat. Each tail wave = bet-3+.
  rules:   # owner voice, this session — duplicated here until the maintenance home exists
    - "R12: one player hosts; no dedicated server, ever (not researched — decided)."
    - "R13: sim core = pure C# library, zero Unity refs, builds/runs headless; Unity = render/input/transport adapters only (Burst/Jobs behind a seam the core never sees)."
    - "R14: networking is an edge wrapper, never woven into business logic; every scene/harness composes the core in one of 3 modes (pure-local / local host-loop / networked host+clients) chosen at the composition root (DI); test scenes pick the mode freely."
    - "vendor default = FishNet (Steam-only, free, GameObject-native, free Steam transport/relay); verified in t-1; fallback NGO/NfE via P6, no tree change. Gas rides OUR custom chunked-delta channel regardless of vendor."
    - "R5 (refined): special gases are field-transported by the same simulation, NOT agents/enemies, NOT self-directed; distinguished by params + visual + effects. AGENT_SUBSTRATE + velocity-intent removed from the concept."
    - "R15: layered gas params — shared parent params for ALL gases (density, per-cell packing, spread speed) + meta-gas group adds own params + own visual; specific gas = pure config; per-meta-gas visual defined once but procedurally generated from params (feeds g-7e15)."
  cut_list:
    fresh_cut_this_wave:
      - "T2 detailed per-cell window near the player -> Wave 3 — THE real cut, and it HURTS: t-4 renders coarse-only,
         and the owner-signed coarse<->fine no-jerk-on-ENTRY handoff (GG4/OR4 «100%») goes UNEXERCISED this wave
         (named-deferred to Wave 3, not dropped — the fine tier it hands off TO lives there)"
    inherited_deferrals:   # already decided; restated for completeness, NOT this wave's sacrifice
      - "full DA occupancy voxelization + 1000-object min-spec ingest gate -> later (naive room-composer now; level
         SIZE is free — sim proven at ~3,300-sector scale headless; deferred = interior fidelity + ingest perf-at-scale)"
      - "sector subdivision (chains/grids/z-slabs) -> later (day-one 1 sector + 2 bands per volume)"
      - "frequency ladder 10/5/1 Hz -> later (all coarse 10 Hz day-one)"
      - "temperature->gas FEEDBACK -> DEFERRED (d-tempfeedback-001; temperature stays a SINK; crit-10 reworded to NAME it)"
      - "PGG / room-interior population -> parked behind the SAME generator-agnostic seam (optional future research)"
      - "plume entrainment + dynamic inter-sector heat -> later"
      - "structural collapse / level-wide destruction / debris (R9) -> OUT; day-one = ONE real controlled local breach"
      - "matchmaking / lobby browser -> planned-for-EA, non-gating (harness = direct connect)"
      - "save/load -> none (ephemeral harness; reproducibility from deterministic seeds)"
      - "spectacular clip -> stays g-7e15 (this wave's terminus is player-LEGIBLE, not spectacular)"
      - "gas-type seam GT1-GT5 + crit-4 third-gas-by-data -> later wave / g-d3a8 converge (core-depth re-homed)"
      - "OR1 cross-TIER composition + coarse<->fine handoff -> Wave 3 (with the fine tier); OR2 reduces to
         coarse-is-floor everywhere this wave (single open tier)"
  lens_verdicts:
    - "commercial/traction: TASK — t-4 player-legible terminus = the first showable artifact off the REAL sim; feeds g-2f8c's 2026-08-31 page date; breaks pre-mortem #2 (Wave 1 left ZERO player-facing artifact)"
    - "technical feasibility: TASK — t-1 band solver = the riskiest NEW assumption (brief §7-#2, zero precedent)"
    - "core gameplay depth: Wave 2 CLOSES the 'seam argued-not-exercised' half (real 3rd layer via XL2; breach->flow; sink observable) but the 'inert sink is not depth' half stays OPEN by design (feedback deferred); gas-type depth re-homed to g-d3a8 — named-deferred, NOT claimed as depth"
    - "co-op-first: NOT advanced this wave — co-op-interdependence is a KNOWN owner-deferred gap (c-map-004, unowned before a parked Steam Playtest); CR1 coarse replication is consistency infra, NECESSARY-not-sufficient for co-op (knowledge/g9c41-wave1-consistency-not-depth-not-coop) — NOT claimed to 'serve' co-op"
    - "scope/production: held by the cut list + the 07-24 wall + EXPLICIT concurrency (t-4 is a parallel Unity/visual work-stream against t-2/t-3, depends on t-2's level+breach not t-3) — not 'just the cut list'"
    - "audience workflow: covered by t-4 (feeds g-e6f2 / g-2f8c real-footage cadence)"
  kill_by:
    metric: |
      Band-solver kill-gate (single binary, scored against a default-FAIL G0 ledger frozen before the spike — I22):
      ALL of { sealed-room+source: outflow within K ticks of portal-open; two-room multirate mass-drift <1e-9/hr;
      cold-rung checkerboard: 0 flow-sign-flip sustained >2 consecutive ticks AND total-variation non-increasing;
      hot-CO2 inversion detailed-to-ceiling; Steckler monotone interface descent; quasi-steady pressure-solve
      converges in-budget at the ~3,300-sector scale post-breach } PASS, AND the solve reduces to integer-exact
      (negative test: a non-deterministically-reduced float path FAILS the host==client lossless oracle), AND
      host + 2 clients reconstruct coarse band state bit-exact lossless / bounded-at-settle lossy (PER LAYER).
    checkpoint_2026-06-30: "band-solver kill-gate above unmet after reasonable iteration -> next_if_false(i)"
    hard_2026-07-24: "Wave-2 done_when unmet even after degrade -> bet dies (G3, no extend); continuation = re-shape bet-3"
    next_if_true: "coarse sim + temperature + breach + legible terminus -> roll to Wave 3 (T2 detail + no-jerk handoff)"
    next_if_false: |
      (i) checkpoint_fail 06-30 -> DEGRADE the coarse solver to scalar-per-volume (wire-compatible, brief §6) and
          re-baseline so the terminus rides the DEGRADED model (t-4 is SOLVER-AGNOSTIC — reads the RN1 read-model that
          both the band solver and scalar-per-volume publish; the terminus survives the degrade);
      (ii) hard 07-24 unmet even after degrade -> re-shape bet-3 (node wall unmoved).
    evaluator: |
      Executor-heavy KILL-GATE bet. BUILD = Opus 4.8/Claude Code in GasCoopGame; the §7-#2 numerical battery + CR3
      determinism negative test + CR1/CR2 lossless/lossy oracles are authored by an INDEPENDENT test-author from the
      contract acceptance rows (builder can't edit — I22 + the builder-stage quality fix); the binding kill-gate
      verdict at the 06-30 checkpoint = an independent fresh-session G5 refutation (Codex/GPT-5.5 pre-pass allowed,
      binding = fresh session). Rollback = the next_if_false ladder above.
  early_finish: |
    Early finish = success (G3 — don't pad). If the Wave-2 done_when is met before 2026-07-24, close + shape Wave 3.
    Pull-forward if running ahead after the kill-gate: (1) the 25cm T2 detail window, (2) the no-jerk coarse<->fine
    handoff, (3) sector subdivision of large volumes. <=3 active tasks (G1); faster agents move the wave faster, not wider.
  forecast: |
    The band solver's scheme is unconditionally stable BY CONSTRUCTION (exponential-relaxation Patankar + quasi-steady
    pressure, brief §3.1) and the locked stream already carries multi-layer state bit-exact (Wave 1) — so the residual
    risk is the float->integer reduction + coarse-scale replication + in-budget convergence at scale, all killed FIRST
    and cheapest in t-1 (headless, no net/DA), with the scalar-per-volume degrade as a guaranteed wire-compatible fallback.
  against: |
    The band-solver synthesis has NO direct donor (brief §6 'new synthesis without a direct donor'); integer-exact
    reduction of a stiff stratified solver is unproven; the K-species throughput anchor is unmeasured; DA is a stale
    vendor with vertical-from-convention. Any could eat the window — t-1 (battery + CR3 + scale + micro-bench) turns
    them into measured facts in week 1, before any net/DA work; the topology-from-scene+tags seam decouples us from DA's API.

active_tasks:   # Wave-2 task set (riskiest first); G1 ≤3 active — only t-1 active now, the rest queued/blocked
  - id: t-1
    kind: executor (engineering, GasCoopGame) — KILL-GATE, riskiest first
    goal: |
      The novel coarse band solver is PROVEN numerically stable, integer-exact-replicable, and in-budget at the
      ~3,300-sector scale — headless, ZERO network/DA/Unity dependency — so the riskiest NEW assumption dies first + cheapest.
    done_when: |
      Headless engine-free spike: (a) brief §7-#2 numerical battery PASSES on a scale-realistic procedurally-generated
      synthetic sector graph (~3,300 sectors) incl. pressure-solve in-budget post-breach; (b) CR3 — whatever integrator
      PLAN picks reduces deterministically to exact integer/fixed-point authoritative state before hashing/wiring,
      negative test: a non-deterministically-reduced float path FAILS the host==client lossless oracle (cell with
      realistic multi-species flux summands, non-vacuous); (c) §7-#3 K-species throughput micro-bench on min-spec;
      (d) crit-9 scale arithmetic vs the R1 profile from the ON-WIRE keyframe-inclusive ~11k basis (V2-1), ≥2 independent
      recomputes; PLUS a week-1 pure-local (R14, zero net) owner-acceptance legibility pre-test. Scored against a
      default-FAIL G0 ledger frozen pre-spike; binding verdict = independent fresh-session G5 refutation at 06-30.
    status: done   # 2026-06-17 (s-work-007) REBUILT under d-fillmodel-001 (capacity-fill+overflow) + per-band temperature → kill-gate PASS_WITH_NITS, owner-confirmed (198/198, mutation 76.76%, fresh-session G5 PASS, owner multi-quantity legibility PASS). Codex P1 cross-band buoyancy dispositioned = no code change (d-crossband-inv-001). Merged dev→main + pushed (GasCoopGame build @a868270, RESULT @9e7dab9). RESULT → history/2026-06-17-c-exec-005-t1-result.md.
  - id: t-2
    kind: executor (engineering, GasCoopGame)
    goal: real coarse band gas on a REAL DA-composed generated level, networked-consistent, with a real breach.
    done_when: |
      Generator-agnostic topology seam (scene-geometry + semantic tags/markers → TopologyDocument; IN1 + IN2
      replaceability demonstrated on DA room-composer alone, hand-made tagged room prefabs; meaningful size, hundreds of
      rooms) + GG2 sovereignty; the band solver runs on the real level (whole-level always-on), per-room CAPACITY bound
      to real DA geometry; LIVENESS (d-roomfull-001 — closed level + capacity + BACK-PRESSURE: a source cannot inject
      beyond capacity, cells clamp [0,capacity], a saturated CLOSED region HOLDS — no terminal throw / no int overflow /
      no negative, mass-exact; refutes the A10-3 terminal-overflow); ONE real controlled breach (GG1/GG3) → topology
      change on a SINGLE agreed tick every peer observes identically (topology-revision strictly monotonic, no
      unreconstructable gap; change-set replay-identical) → gas flows, with CR2 lossless-bit-exact ACROSS the coarse
      topology change; CR1 coarse replication host+2 clients PER LAYER (coverage-floor vacuous = whole-level interest,
      anchored to gameplay-reach V2-2); CR3 coarse authoritative state exact integer (non-vacuous float-mutant negative
      test); the single-oracle CROSS-CONSUMER probe (OR1 visual read-model + OR3 far-AI ExposureQuery on DIFFERENT peers
      agree at the same point/species/committed revision; a region entitled per OR3 but omitted from a client's stream
      FAILS); exact source-pin (GG4 coarse half: source identity survives a non-destructive topology change, accumulates
      at a believable gradual rate = correct-amount-on-return); clean 1-player parity (crit-7). Planner spec actions
      (owner-ratified s-work-008, builder applies dictated wording): narrow ADR-0005 BS4 + apply the c-exec-005 openspec
      delta WITH its spec.md:82 criterion-(b) cross-band claim narrowed in the SAME pass (canonical sim-core/spec.md
      ends with NO "past a colder species" prose; BS10(e) preserved) + archive; temperature forward-constraint recorded.
      per-gas TEMPERATURE + the FINE intra-room cloud shape (corner front) are OUT (deferred / Wave 3).
    status: done   # 2026-06-19 (s-work-009, applies c-exec-006 RESULT): t-2 RETURNED + CLOSED. Real DA-shaped level (IN1/IN2 generator-agnostic TopologyDocument seam, hundreds of rooms) + ONE controlled low-floor breach (GG1 same-tick/monotonic-revision/replay-identical + GG2 geometric sovereignty + GG3) + per-room-capacity LIVENESS (d-roomfull-001 closed-level + back-pressure: saturate-and-hold, no throw/overflow/negative, mass-exact, clearing a source leaves a live field) + per-layer coarse replication host+2 clients across the breach (CR1/CR2 lossless-bit-exact + lossy≤Q + bit-exact-at-settle / CR3 integer-exact, float-mutant negative) + single field-sampling oracle (OR1/OR3 cross-consumer+cross-peer over CR1-RECONSTRUCTED state, omitted-region negative) + clean 1-player parity. Leg-8 owner-visible slice BUILT FOR REAL (SceneTopologyComposer + DaTopologyProducer + GasDebugCoarseScene.unity + run-artifact) — the deliverable-exists v7 gate had caught it reported-done-not-built; the rebuild closed it; owner eyeball «работает» (2026-06-18). Gate check.ps1 -Deliver GREEN 372/372, mutation 75.29%, deliverable-coverage 14 promises; fresh-session G5 CLEAN (3 findings fixed: T28b CR1-reconstructed oracle, BandForHeight long, T5b GG4 source-survival). Legs 1-8 on GasCoopGame main (build @bef6fd8→04f39ee, finalized @0327b9f). Home-side OpenSpec apply+archive DONE (canonical sim-core/spec.md +18 reqs, grep-clean; folder → archive/; dev @7987506 / main @ce79e10, UNPUSHED). FishNet UDP wire env-deferred (WSAENOBUFS persists across restart — host/OS condition, NOT a build defect; binding gate = headless+loopback per spec; real-UDP = owner-run). Per-species temperature + fine intra-room cloud shape = Wave 3 (owner-acked cuts). RESULT → history/2026-06-18-c-exec-006-t2-result.md.
  - id: t-3
    kind: executor (engineering, GasCoopGame) — parallel with t-4 after t-2
    goal: the temperature layer plugs in as a real 2nd layer without core edits; both layers consistent at coarse scale.
    done_when: |
      Temperature SINK layer registers via the layer registry (XL2: a 3rd demonstrative INDEPENDENT layer plugs in
      WITHOUT editing core; gas trajectory byte-identical + RNG-conservation guard; the [2,4] barrier-table re-size
      SURFACED per the LOCK's SHALL-re-size, never silent); coarse per-layer consistency CR1/CR2/CR3 incl. the coarse
      per-band temperature state (V2-3: the coarse temperature READ exercised on a committed revision); the
      gas→temperature SINK interaction observable (suppressed-event negative oracle, XL1); the §RESOLVED-4
      grid-addressed read-ready seam exercised (read another layer's field at a committed revision).
    status: blocked_on c-exec-009   # 2026-06-19 (s-work-011) HELD pending the c-exec-009 clean baseline — t-3 edits the Core/Field + Coarse/Replication seam that the ADR-0008 consolidation + the 3 no-silent-corruption fixes touch (collision); resume via a fresh work session once the baseline is green. Originally OPENED 2026-06-19 (s-work-010) as c-exec-007 (∥ t-4); opens with a PLAN (owner present). ADDITIVE on t-2: coarse temperature is plane 6 ALREADY shipped + replicated (a coupled plane of CoarseBandLayer, NOT a registered layer) — t-3 ADDS a NEW 3rd INDEPENDENT demonstrative layer (the XL2 file-isolation proof) + the §RESOLVED-4 read seam + the gas→temperature suppressed-event sink oracle; MUST NOT re-home/alter plane 6 or change IGasReadModel.ConcentrationAt (t-4 parallel-safe). Full CALL → history/s-work-010.md.
  - id: t-4
    kind: executor (engineering, GasCoopGame) — PARALLEL Unity/visual work-stream; depends on t-2 (level+breach+read-model), NOT t-3
    goal: a PLAYER-LEGIBLE artifact off the real coarse sim — readable without a debug overlay; breaks pre-mortem #2.
    done_when: |
      crit-6 render slice (≤2wk, quantized-volumetric stylization behind the RN1 read-model seam, ms-budget on min-spec
      class): a room visibly fills bottom-up from the breach side over time, heavier gas settles low, the source/breach
      is identifiable — NO debug overlay, reads as DELIBERATE low-poly stylization not a stub. Acceptance = RN2-style
      blind vision-agent check (machine-readable ground truth: gas present / which room filling / from the breach) at a
      floor threshold + owner gamer-eye verdict, EXCLUDING g-7e15's menace/silhouette/material bars. Holds
      no-jerk/no-shimmer-EVER (incl. off-screen-computed state surfacing — owner-signed GG4/OR4 coarse half).
      SOLVER-AGNOSTIC (reads RN1 — works on band OR degraded scalar). Rides the 07-11→07-24 cushion to ~07-21;
      auto-shrinks to a ≤1wk minimal-legibility floor if t-1 slips past 06-30.
    status: active   # 2026-06-19 (s-work-010) OPENED as c-exec-008 (∥ t-3); opens with a PLAN (owner present). Carries owner R1 (wire the REAL Dungeon Architect, existence-proven: real IDaRoomReader, tag prefabs, REMOVE FixedLevelRoomReader from runtime; SCOPE-SPLIT from the render terminus + GEOMETRY-MOVE RULE), R2 (guide-loop step-by-step Unity instructions whenever an action can't go via MCP + answer owner Qs), R3 (owner-run = close-gate: BUILD/existence closes headlessly, only the LOOK is owner-run; DONE-pending-owner-LOOK until owner confirms — no self-marking). Acceptance = RN2 machine blind-check (frozen N-of-M floor) + owner gamer-eye. Full CALL → history/s-work-010.md.
  - id: t-5
    kind: executor (engineering, GasCoopGame) — CONSOLIDATION + HARDENING (review-driven, NOT a wave feature); LEADS Wave-2; gates t-3, ∥ t-4
    goal: |
      ONE clean, gate-green, owner-acked dev baseline — the in-flight ADR-0008 coarse-replication-seam→Core move + the 4 unpushed tooling
      commits consolidated coherently (nothing correct lost), the 3 real no-silent-state-corruption fixes landed THROUGH the contour, hygiene
      batched, every out-of-scope review finding a NAMED owner-ack deferral. Closes the 2-review triage + restores OS visibility of the
      previously-shadow dev hardening work.
    done_when: |
      (consolidation) ADR-0008 changeset committed as ONE coherent boundary-correction commit on top of the 4 kept tooling commits (git clean;
      moved Core types keep GUIDs; FishNetChunkChannel : ICoarseChunkLink) + R13/R14 mechanical proof (moved Core/Field/Coarse/Replication/*
      compile noEngineReferences:true, ZERO Unity/FishNet usings). (gate-honesty) check.ps1 -Deliver GREEN on a CLEAN tree, transcript attached
      to RESULT.md (proves P0 was the dirty tree). (3 fix-now, each red-test-first by an INDEPENDENT test-author, classified
      no-silent-corruption, ENROLLED as a frozen change with its own mutation-<id>.json ≥ floor): FieldDelta validate-before-mutate;
      RevisionBarrier/ChunkDecoder/CoarseChunkFollower apply-before-advance; StableId→Core + a TopologyConformance derive-mismatch check (no
      formula-duplication). (hygiene) AGENTS.md Net-edge-root line; GasDebug version-checked reflection bootstrap; LogAssert targeted-Expect;
      delete Assets/_Recovery; git rm --cached GasCoopGame.slnx; swapped-assert fixes; hygiene.ps1 flags runtime Assert.Ignore/Assume +
      _Recovery/_scratch_*. (close) -Deliver GREEN incl. all 3 change-ids' mutation ≥ floor + deliverable-coverage v7 over ALL done_when +
      spec-silence + a FRESH-SESSION G5 refutation on the HARDENED tree + RESULT reconciled. 5 NAMED owner-ack deferrals recorded. TWO
      owner-gated blockers stated, NOT self-resolved: (i) owner-run Unity compile + PlayMode CoarseVisibleSlice re-run via MCP; (ii) real-UDP
      FishNet deferred (WSAENOBUFS).
    status: active   # 2026-06-19 (s-work-011) FRAMED as c-exec-009 (red-teamed wf_619b23cd, SOUND-WITH-FIXES). Leads Wave-2; ∥ t-4 (c-exec-008); gates t-3 (c-exec-007 HELD). Full CALL → history/s-work-011.md §c-exec-009.

recurring: []

open_calls:
  - id: c-exec-009
    status: open   # 2026-06-19 (s-work-011) FRAMED + red-teamed (wf_619b23cd, SOUND-WITH-FIXES) + OPENED — review-driven consolidation+hardening leg (t-5); LEADS Wave-2, ∥ c-exec-008, gates c-exec-007
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
  - id: c-exec-007
    status: held   # 2026-06-19 (s-work-011) HELD pending the c-exec-009 clean baseline (shares the Core/Field + Coarse/Replication seam the ADR-0008 move + the 3 fixes touch). FRAMED + hardened (wf wd3a59z47) + OPENED 2026-06-19 (s-work-010) — Wave-2 t-3 engine leg, ∥ c-exec-008
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
    status: open   # 2026-06-19 (s-work-010) FRAMED + hardened (wf wd3a59z47) + OPENED — Wave-2 t-4 render terminus + REAL Dungeon Architect, ∥ c-exec-007
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

next: |
  Owner «го» (2026-06-19, s-work-011): a review-driven CONSOLIDATION+HARDENING leg LEADS Wave-2. RUN c-exec-009 (t-5)
  in GasCoopGame (branch dev): consolidate the in-flight ADR-0008 seam→Core + 4 unpushed tooling commits into ONE clean
  gate-green baseline, fix the 3 no-silent-corruption defects THROUGH the contour (each red-test-first by an INDEPENDENT
  test-author + enrolled with its own mutation-<id>.json ≥ floor: FieldDelta validate-before-mutate; chunk
  apply-before-advance; StableId→Core+conformance), batch hygiene, carry the 5 NAMED owner-ack deferrals, close on
  check.ps1 -Deliver GREEN on a CLEAN tree + a FRESH-SESSION G5 + RESULT reconciled. Full CALL = history/s-work-011.md
  §c-exec-009 (red-teamed wf_619b23cd; handed to the owner to paste). Owner-gated blockers, NOT self-resolved:
  (i) owner-run Unity compile + PlayMode CoarseVisibleSlice re-run via MCP; (ii) real-UDP FishNet deferred (WSAENOBUFS) —
  loopback binding.

  IN PARALLEL: c-exec-008 (t-4, render terminus + REAL DA) CONTINUES — untouched by both reviews (render path; reads the
  FROZEN RN1), so it runs alongside the hardening (owner R1/R2/R3 unchanged). Full CALL → open_calls / history/s-work-010.md.
  HELD: c-exec-007 (t-3) is PAUSED until c-exec-009 lands the clean baseline — t-3 edits the Core/Field + Coarse/Replication
  seam the ADR-0008 move + the 3 fixes touch (collision). Resume t-3 via a fresh work session once the baseline is green.

  WHEN c-exec-009 + c-exec-008 (and the resumed c-exec-007) RETURN → a review session for the Wave-2 node g-9c41
  (G5 done-evidence per task done_when; then roll to Wave 3 per kill_by.next_if_true). Any leg may return
  DONE-pending-owner-LOOK (t-4) or BLOCKED — re-home via a fresh work session.

  Carry-forward (NOT this wave): per-species temperature / true cross-band inversion (d-crossband-inv-001); the FINE
  intra-room cloud shape + coarse↔fine no-jerk handoff + the d-returnfidelity-001 mid-transient return bar → Wave 3.
  Owner-side, non-gating: PUSH is owner-gated — dev is UNPUSHED ahead of origin (4 tooling commits + the pending
  c-exec-009 consolidation); push after c-exec-009 closes + the owner-run Unity gate confirms. Validate the literal
  FishNet UDP wire once the host network is healthy (WSAENOBUFS — loopback already delivered the binding slice).

END_OF_FILE: live/indie-game-development/NOW.md
