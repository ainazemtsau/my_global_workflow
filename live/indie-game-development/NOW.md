# NOW — indie-game-development

active_bet:
  node: g-9c41
  phase: shape -> work
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

active_tasks:
  - id: t-1
    goal: Engine-free core scaffold + networked harness handshake.
    done_when: |
      (1) sim core = pure C# lib, 0 Unity refs, builds/runs headless (R13);
      (2) composition root gives 3 modes (pure-local / local host-loop / networked),
          a test scene picks the mode, no network logic in business classes (R14);
      (3) FishNet: player-host + 2 headless clients connect, deterministic fixed-tick
          loop, per-tick state hash of a TRIVIAL field equal across all three over a
          fixed run;
      (4) FishNet viability verdict recorded (packet limits, headless x3, Steam transport).
    kind: executor (Opus 4.8 — Fable 5 unavailable; build model per next.model_routing)
    status: done    # 2026-06-13 c-exec-002 GREEN: engine-free integer-only 3-mode deterministic core + FishNet lockstep input-bus; per-tick state-hash EQUAL host + 2 clients (agent-run via Unity MCP) + dotnet 3-core convergence/golden vector; FishNet verdict GREEN (Steam transport YELLOW-deferred); ADR-0002; merged main @daab33d; owner-verified. → history/s-work-003.md
  - id: t-2
    goal: Toy gas field + custom chunked-delta stream + breach + first wire measurement.
    done_when: |
      (1) trivial room-graph diffusion on host through real fabric contracts (layer
          registry + revision feed — contracts that survive to the real sim);
      (2) host streams ONLY changed chunks as quantized deltas over our own channel,
          clients reconstruct, per-tick hash host vs clients equal across a scripted
          breach (two rooms merge);
      (3) deadband + per-client clamp + aggregate host clamp all engaged;
      (4) FIRST measured numbers recorded: honest dirty-chunk wire size (bytes) + dirty-rate.
    kind: executor (Opus 4.8 — Fable 5 unavailable)
    status: done   # 2026-06-15 c-exec-003 RETURNED GREEN/GREEN (recorded s-work-005). Multi-layer host-authoritative chunked-delta field-state stream: dual lossless⇄lossy through ONE codec (lossless per-tick bit-exact incl. breach; lossy |Δ|≤Q every tick + bit-exact at every converged settle); REAL LayerRegistry+RevisionFeed fabric (gas=L0, temp=L1, single-writer token, pinned P0→P3 phases); REAL controlled breach over the lockstep input plane; 3 flow controls proven engaged via negative tests; deterministic fault tolerance (revision barrier never applies a stale chunk). ADR-0003 v2 frozen (C1–C22). dotnet 71/71 + FishNet PlayMode 6/6 (Tugboat loopback); merged main @b9edbce+30f9e45; 2 independent 5-skeptic audits, 0 blockers. FIRST leg to dogfood the new RESULT.md -Deliver gate. clampVerdict stamped DEFERRED-T3 (t-3 pronounces it). → history/2026-06-15-c-exec-003-t-2-result.md
  - id: t-3
    goal: Breach-load consistency hold + stream lock (kill-gate).
    done_when: |
      (1) host + 2 clients run a sustained breach wave; hash consistency holds with both
          clamps engaged;
      (2) measured steady dirty-rate recorded vs the aggregate clamp (fail tripwire =
          >clamp irrecoverably -> Barotrauma-hybrid contingency or model spike);
      (3) stream wire-format + revision barrier declared LOCKED (precondition for building
          band sim on top);
      (4) reproducible build + machine-readable telemetry artifact.
    kind: executor (Opus 4.8 — Fable 5 unavailable)
    status: done   # 2026-06-15 c-exec-004 RETURNED GREEN/GREEN — Wave-1 kill-gate VERDICT=HOLD (owner-confirmed in build). p1 sustained-load consistency HOLDS over the M=3 pulse→settle wave (both clamps; lossless bit-exact every tick incl. breach, lossy |Δ|≤Q every tick, bit-exact at ≥6 non-vacuous settles). p2 steady-rate VERDICT=HOLD via a single binary recovery-mechanism predicate (under a binding 184/184 stress budget WITH the production fault model + on-quiesce resync keyframe, every steady-window settle bit-exact AND the deferred-chunk backlog drains ≤D=4 ticks; keyframe-off negative control trips BLOWN; host-accepted-revision oracle = no stale chunk applied). p3 cross-layer reaction→temperature (ReactionHeat=32, LayerKey 1, suppressed-event negative oracle) proven bit-exact UNDER load. p4 Wave-2 LOCK declared (ADR-0004 §LOCK + drift-guard test). Honesty boundary: toy scene runs ~75× under the real 275 KB/s clamp → proves the scene-size-independent RECOVERY MECHANISM + an honest throughput PROJECTION (~4.9k lossless / ~59k lossy cells @275 KB/s), not a literal 275-blow; loopback only. check.ps1 -Deliver green, dotnet 103/103, FishNet PlayMode GREEN (new SustainedBreachWave_… + R3 suite). ADR-0004 (T1–T14, 5-skeptic + 3 Codex/GPT-5.5 validator rounds); ADR-0003 v2 C1–C22 + t-2 artifacts byte-untouched. Telemetry docs/measurements/g9c41-t3-{lossless,lossy}.json + repro-constants. Merged dev→main @6619299 + pushed. → history/2026-06-15-c-exec-004-t-3-result.md

recurring: []

open_calls:
  - id: c-exec-003
    status: done   # 2026-06-15 RETURNED GREEN/GREEN (recorded s-work-005); t-2 → done. RESULT → history/2026-06-15-c-exec-003-t-2-result.md
    note: framed at s-work-004 (c-work-002); hardened via an 8-agent pass; PLAN ratified converge §WHAT-C into ADR-0003 v2 (C1–C22 frozen). → history/s-work-004.md
  - id: c-review-001
    status: ready   # 2026-06-15 framed at s-work-006 — review of bet g-9c41 after t-3 closed the LAST Wave-1 task (kill-gate VERDICT=HOLD). G5: must run in a FRESH session (never the build) and refute the kill-gate claim from the committed evidence BEFORE Wave 2 is shaped on the LOCK. Full CALL in NOW.next.
    note: |
      Wave-1 kill-gate review. Independently re-derive the HOLD verdict from the committed telemetry (don't
      trust the flag), name any honesty-boundary weakness, harvest what Wave-1 proved into the tree + knowledge,
      bring the owner a next-bet decision (Wave-2 band-sim shape vs alternative). Folds in two known follow-ups:
      the Wave-2 cleanup card (Codex round-3) and the parked map-level re-check of the clip-gated parallel
      tracks (s-shape-004 / root map_order). Builds on history/2026-06-15-c-exec-004-t-3-result.md + ADR-0004.
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

next: |
  CALL c-review-001 — review bet g-9c41 (Wave-1 kill-gate close). Owner opens a FRESH session on this OS
  direction (G5 — the review must NOT run in the session/repo that did the work).
  to: session   direction: indie-game-development   play: review   node: g-9c41
  parent: s-work-006 (recorded the c-exec-004/t-3 return)
  goal: |
    The Wave-1 kill-gate result for g-9c41 stands up to independent inspection — or its weak points are named
    in plain terms — the goal tree shows what Wave-1 actually proved versus what is still only projected, and
    the owner holds a decision on the next bet: Wave 2 (band sim + grid from DA + the temperature layer, built
    on the LOCKed stream) or another node, each option carrying its why-now.
  context: |
    - The t-3 executor exit report: history/2026-06-15-c-exec-004-t-3-result.md (VERDICT=HOLD, the honesty
      boundary, the Wave-2 cleanup card, the cuts). Its manual-acceptance step 3 shows the verdict is
      re-derivable from the committed series — don't trust the flag.
    - The bet + kill_by + wave_plan: this NOW.md active_bet (checkpoint_2026-06-30 = HOLD ⇒ next_if_true =
      roll to Wave 2 — but through this review first).
    - Frozen design in GasCoopGame: docs/adr/ADR-0004-sustained-load-verdict-lock.md (T1–T14, §LOCK, §Verdict)
      + ADR-0003 v2 (C1–C22); telemetry docs/measurements/g9c41-t3-{lossless,lossy}.json + repro-constants.
    - TREE g-9c41 done_when criteria 2/3/10 (the Wave-1-relevant ones) + CHARTER lenses.
    - Two follow-ups to weigh in the harvest/selection: the Wave-2 cleanup card (Codex round-3, owner-accepted)
      and the parked map-level re-check of the clip-gated parallel tracks (s-shape-004 / root map_order).
  boundaries: |
    No Wave-2 code or shaping beyond the next-bet recommendation; the product repo is not touched. The
    verdict's own correctness is re-established from the committed evidence, not assumed from the build's
    self-report or the in-build owner-confirm. g-9c41 is a MULTI-WAVE node — closing Wave 1 is not closing the
    node; the verdict is on the Wave-1 deliverable. TREE.md / CHARTER.md edits reach state only via the owner's
    in-session approval (G9).
  done_when: |
    g-9c41's Wave-1 done_when carries an independently-verified verdict (met / partially / not, G5 refutation),
    with the surprise vs the bet's forecast/against named; TREE.md reflects the Wave-1 learnings under owner
    approval; NOW.md is clear of the closed Wave-1 tasks; the owner has a next-bet decision with 2–3 options
    and a recommendation.
  return: |
    review RESULT — verdict + tree diff (owner-approved cards) + ≤1–3 knowledge entries with read_by +
    decisions_needed (the next-bet choice) + next = shape CALL on the recommended node.
  budget: one session.
  surface: a fresh session on this OS direction (chat or this repo via CLI); the owner is present for the
    next-bet decision and any TREE edits (G9).

END_OF_FILE: live/indie-game-development/NOW.md
