# NOW — indie-game-development

active_bet:
  node: g-9c41
  phase: Wave 1 CLOSED 2026-06-16 (review c-review-001) — verdict MET (HOLD independently re-derived); node g-9c41 stays ACTIVE (multi-wave) -> next = shape Wave 2 (c-shape-wave2)
  appetite: 6 weeks, hard end 2026-07-24 (G3 — fixed, never extended)
  approach: |
    NETWORK-FIRST, minimal-but-REAL LAYERED CORE (RE-SHAPED 2026-06-14, s-shape-004 — owner «фокус на ядро,
    клип не паримся», «да A»). The riskiest assumption (networked chunked-delta gas consistency) dies first
    via a net spike, THEN the real core is built on the locked stream in WAVES. The bet proves the core is a
    REAL extensible LAYERED architecture over the network: gas layer + a thin DYNAMIC temperature layer +
    REAL controlled destruction (wall breach -> topology -> gas flows) on ONE seam, networked-consistent.
    Sims stay TRIVIAL, seams REAL + extensible (R13). NO clip in this bet (the spectacular clip is g-7e15's
    later job — deferred; see s-converge-002 + plan stress-test wf_454d6859-4e4).
    Brief: work/research-g-9c41-core-architecture-2026-06-12-v2.md.
  done_when: |
    Delivered in WAVES on the fixed-but-soft 2026-07-24 wall (move tail waves if needed — owner). By the end:
    (1) chunked-delta stream LOCKED — 2 clients reconstruct, consistency across a REAL controlled breach
        (kill-gate "A"); (2) the seam proven MULTI-LAYER — gas + a thin temperature scalar both reconstructed
        consistently; (3) REAL controlled wall-breach -> topology change -> gas flows (no scripted, no
        collapse); (4) cross-layer interaction visible (reaction/heat -> temperature responds); (5) everything
        on EXTENSIBLE seams (a new layer/driver plugs in without core edits); (6) min-spec budget + harness +
        debug surfaces + reproducibility. NO spectacular clip in this bet. The full-node bar (TREE g-9c41
        done_when, being realigned this session) is delivered across this bet + bet-2+ (detailed near-player
        tier + big levels + real gas types = later waves; full core ~= 12-16 solo-weeks per brief).
  wave_plan: |   # rolling wave — <=3 active tasks; plan each wave knowing the last one's result
    Wave 1 (NETWORK — t-1 done, t-2/t-3): gas synchronises over the net on a thin field + the seam carries
      >=2 trivial layers (gas + temp scalar) + a REAL controlled breach. Output: networking PROVEN,
      stream/format LOCKED. (Loopback proves correctness + byte-size; real-uplink behaviour = later.)
    Wave 2 (REAL COARSE SIM + GRID + LEVELS): band solver + grid from Dungeon Architect (naive adapter) +
      the thin temperature layer, on the proven stream. Output: real coarse gas+grid on real (small) levels,
      networked. (converge-arch c-converge-002 contracts feed this wave.)
    Wave 3 (DETAIL NEAR PLAYER): the T2 detailed per-cell window + optimisations. Output: detailed gas at the
      player.
    Wave 4+: real controlled destruction fully, reaction MECHANISM, scale to big levels. Each wave = short
      PLAN (its architecture) -> build -> measure -> next.
  rules:   # owner voice, this session — duplicated here until the maintenance home exists
    - "R12: one player hosts; no dedicated server, ever (not researched — decided)."
    - "R13: sim core = pure C# library, zero Unity refs, builds/runs headless; Unity = render/input/transport adapters only (Burst/Jobs behind a seam the core never sees)."
    - "R14: networking is an edge wrapper, never woven into business logic; every scene/harness composes the core in one of 3 modes (pure-local / local host-loop / networked host+clients) chosen at the composition root (DI); test scenes pick the mode freely."
    - "vendor default = FishNet (Steam-only, free, GameObject-native, free Steam transport/relay); verified in t-1; fallback NGO/NfE via P6, no tree change. Gas rides OUR custom chunked-delta channel regardless of vendor."
    - "R5 (refined): special gases are field-transported by the same simulation, NOT agents/enemies, NOT self-directed; distinguished by params + visual + effects. AGENT_SUBSTRATE + velocity-intent removed from the concept."
    - "R15: layered gas params — shared parent params for ALL gases (density, per-cell packing, spread speed) + meta-gas group adds own params + own visual; specific gas = pure config; per-meta-gas visual defined once but procedurally generated from params (feeds g-7e15)."
  cut_list:
    - "T2 intra-room grid -> bet-2 (clip works from bands; sectorization contract stubbed day-one)"
    - "sector subdivision (chains/grids/z-slabs) -> bet-2 (day-one = 1 sector + 2 bands per volume)"
    - "frequency ladder 10/5/1 Hz -> bet-2 (day-one all 10 Hz)"
    - "DA occupancy voxelization + 1000-object gate -> bet-2 (day-one naive adapter ~100-300 objects)"
    - "PGG / second generator -> parked (adapter seam proven on DA alone)"
    - "directed/agent gases + 'hands in fog' effects -> removed from concept / g-d3a8 design"
    - "dynamic sector-to-sector heat exchange + plume entrainment -> bet-2; day-one = a THIN DYNAMIC temperature LAYER (own minimal sim on the grid event bus) — SUPERSEDED from 'static field' per owner RESOLVED-1 (s-converge-002)"
    - "structural collapse / level-wide destruction / debris physics -> OUT (never, R9); day-one = REAL CONTROLLED LOCAL destructibility (destructible wall -> breach -> topology -> gas flows) — SUPERSEDED from 'scripted breach only' per owner RESOLVED-2 (s-converge-002)"
    - "matchmaking / lobby browser -> planned-for-EA, non-gating (harness = direct connect)"
    - "save/load -> none (ephemeral harness sessions; reproducibility from deterministic seeds)"
  lens_verdicts:
    - "commercial/traction: DEFERRED — spectacular clip dropped from this bet (owner «клип не паримся»; it is g-7e15's later job); the parallel-track gating that hung on the ~07-10 clip needs a map-level re-check (follow-up)"
    - "core depth: not_needed as design (re-homed to g-d3a8); substrate proven incidentally (param gas + 1 reaction)"
    - "co-op-first: TASK — 2-4 clients see consistent gas across a topology change (the net spike)"
    - "technical feasibility: TASK — net consistency = riskiest assumption, the first task"
    - "scope/production: not_needed as a task — held by the cut list + G3 appetite"
    - "audience workflow: not_needed as bet work — the clip artifact feeds g-e6f2 (parked, <=10% until clip)"
  kill_by:
    wave1_resolution: "RESOLVED 2026-06-16 = HOLD. c-exec-004 returned HOLD; INDEPENDENTLY re-derived at review c-review-001 (telemetry re-computed from the committed series + 6-skeptic refutation — all 6 pillars un-refuted, refuted=0/affecting-verdict=0 — + a live gate run dotnet 103/103 + git: ADR-0003 C1-C22 & t-2 artifacts byte-untouched). next_if_true taken -> roll to Wave 2. One named limit (verdict-NEUTRAL): the lossy throughput PROJECTION was ~5.3x optimistic (offered-demand-based, resync-keyframe-blind); honest on-wire basis ~11k cells (lossless ~4.9k conservative) -> folded into TREE crit-9 + knowledge + the Wave-2 shape."
    metric: "per-tick state-hash consistency host + 2 clients through a REAL controlled wall-breach with both clamps engaged; measured dirty-chunk wire size within the aggregate host clamp at target tick"
    checkpoint_2026-06-30: "if consistency cannot be made to hold after reasonable iteration OR the steady dirty-rate irrecoverably blows the aggregate clamp -> P6 model/vendor spike (1-2wk timebox: FishNet<->NGO, last-resort rollback) or kill the bet"
    hard_2026-07-24: "day-one done_when unmet -> bet dies (G3, no extend); continuation = re-shape bet-2"
    next_if_true: "stream locked -> roll to Wave 2 (band sim + grid from DA + temperature layer; NO clip)"
    next_if_false: "model/vendor spike, or narrow to the Barotrauma-hybrid (client-local diffusion + threshold corrections)"
  early_finish: |
    Early finish = success. If the day-one done_when is met before 2026-07-24, close the
    bet and immediately shape bet-2 (do NOT pad scope — G3). Wave runs <=3 active tasks;
    faster agents simply move the wave faster. Pull-forward ladder (first bet-2 items if
    running ahead): (1) sector subdivision, (2) T2 windows around players, (3) frequency
    ladder + hotness.
  forecast: "net consistency holds — every working precedent (SS14/Stationeers/Noita) does chunked single-writer delta; the plan kills this risk first (the hardest net task t-1 runs first)"
  against: "novel band solver (risk #2, no direct precedent) + a custom stream + UNAUDITED agent throughput on this project could eat the window; the first week of t-1..t-3 turns that into a measured fact"

active_tasks: []
  # Wave-1 tasks ALL DONE and CLOSED by review c-review-001 (verdict MET). Records in LOG.md + history/:
  #   t-1 — engine-free 3-mode deterministic core + FishNet handshake → c-exec-002 @daab33d / s-work-003.md
  #   t-2 — multi-layer chunked-delta field-state stream, ADR-0003 v2 C1–C22 → c-exec-003 @b9edbce / s-work-005.md
  #   t-3 — sustained-load kill-gate = HOLD, stream LOCKED, ADR-0004 → c-exec-004 @6619299 / s-work-006.md
  # The next bet (Wave 2) is shaped via c-shape-wave2 (NOW.next) and will commit fresh tasks (G1/G2).

recurring: []

open_calls:
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
  - id: c-shape-wave2
    status: ready   # 2026-06-16 framed at review c-review-001 (owner «го» → Decision A). Shape g-9c41 Wave 2 on the LOCKed stream. Full CALL in NOW.next.
    note: |
      Wave 2 = real coarse band gas-sim + temperature layer on the LOCKed stream over real (small) generated
      levels. TWO owner-mandated shape inputs (G9, «го»): (1) a player-facing TERMINATION clause — Wave 2 ends
      in something a human reads WITHOUT a debug overlay (breaks pre-mortem #2 before the 08-31/10-05/12-11
      gates); (2) size the coarse grid against the ON-WIRE keyframe-inclusive budget (~11k lossy cells, NOT the
      ~5.3x-optimistic 59k). Steers: DA gives structure/topology day-one (TopologyDocument adapter), PGG =
      population/interior LATER via the same seam (population OUT of scope now); band-handoff design question —
      track sources/emitters EXACTLY even when a volume is coarse + reconstruct local detail from the source on
      player-entry (so a weak corner source is correct on arrival). Tighten TREE crit-10 in-shape (require a
      FEEDBACK cross-layer interaction + exercise the extensible seam with a real added layer). Fold the Wave-2
      cleanup card (Codex round-3). converge-arch c-converge-002 contracts feed this. Builds on ADR-0004 §LOCK +
      knowledge/g9c41-wave1-*.
  - id: c-map-003
    status: queued   # 2026-06-16 framed at review c-review-001 — re-check the parallel-track structure post-clip-drop
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
    status: queued   # converge-arch on g-9c41 cross-node contracts (parallel retrofit; gated by d-converge-001)
    note: |
      Declare the §WHAT-B cross-node contracts consumer-driven (gas-type seam, render seam, the
      shared field-sampling oracle B31, ingestion adapter/TopologyDocument, grid↔gas) so the
      open→PLAN stream magnitudes are frozen against contracts that bound them. Full CALL in
      history/s-converge-001.md RESULT.next. (d-converge-001 resolved = A; converge-arch runs in
      parallel and refines the B-row contracts — it does NOT gate the c-exec-003 PLAN under A.)
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

next: |
  CALL c-shape-wave2 — shape Wave 2 of bet g-9c41 (on the LOCKed stream). Owner present for the shape (G6/G9).
  to: session   direction: indie-game-development   play: shape   node: g-9c41 (Wave 2)
  parent: s-review-001 (Wave-1 review; verdict MET, HOLD independently re-derived)
  goal: |
    g-9c41 Wave 2 exists as a committed, shaped bet: real coarse gas behaviour on real (small) generated
    levels is networked-consistent across host + clients on the already-LOCKed stream, the temperature layer
    rides alongside it, the riskiest NEW assumption is identified with a task that tests it first, and the bet
    ends in an artifact a human can read WITHOUT a debug overlay.
  context: |
    - The LOCKed Wave-1 contract is the foundation, do NOT re-open it: GasCoopGame docs/adr/ADR-0004 §LOCK
      (wire format + revision barrier + channel semantics + cross-layer contract + cell-hash domain) +
      ADR-0003 v2 C1–C22. Wave-1 verdict = MET/HOLD (history/s-review-001.md; independently re-derived).
    - Wave-1 learnings (read these): knowledge/g9c41-wave1-hold-mechanism-lossy-projection.md,
      knowledge/g9c41-wave1-no-player-facing-premortem2-live.md,
      knowledge/g9c41-wave1-consistency-not-depth-not-coop.md.
    - converge-arch c-converge-002 (cross-node contracts: ingestion adapter/TopologyDocument, grid↔gas,
      gas-type seam) feeds this wave's contracts.
    - The re-shaped bet context still lives in this NOW.md active_bet (approach/wave_plan/rules/cut_list).
  boundaries: |
    Appetite wall stays 2026-07-24 (G3 — never extended; the node is multi-wave, move tail waves not the wall).
    Do NOT re-open the Wave-1 HOLD verdict or edit the LOCK / C1–C22 / t-2 artifacts. Shape only — the build is
    separate executor legs. TREE/CHARTER edits reach state only via owner in-session approval (G9). The
    structural parallel-track tree work (legibility node, co-op node, clip-gate) is c-map-003, NOT this shape.
  done_when: |
    A committed Wave-2 bet valid under G6: appetite + kill_by (metric + threshold + date) + a cut list (≥1 real
    cut) + a per-lens sweep verdict + a task testing the riskiest NEW assumption (the novel band solver). Two
    owner-mandated inputs are BAKED into the bet's done_when: (1) a player-facing termination artifact (legible
    without a debug overlay); (2) coarse-grid bandwidth sizing computed from the ON-WIRE keyframe-inclusive rate
    (~11k lossy cells, NOT 59k). The band-handoff rule (sources tracked exactly when coarse + reconstruct local
    detail from the source on player-entry) and the crit-10 tightening (feedback interaction + exercise the
    seam) are addressed in the shape. The DA-structure-day-one / PGG-population-later steer is locked.
  return: |
    shape RESULT — committed Wave-2 bet (G6/G9), tasks for the wave, next = executor CALL on the first task.
  budget: one session.
  surface: a session on this OS direction (chat or this repo via CLI); the owner is present for the shape (G9).

END_OF_FILE: live/indie-game-development/NOW.md
