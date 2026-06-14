# NOW — indie-game-development

active_bet:
  node: g-9c41
  phase: shape -> work
  appetite: 6 weeks, hard end 2026-07-24 (G3 — fixed, never extended)
  approach: |
    Hybrid in ARCH-1v2 edition — "network first, coarse truth = sector bands, clip from
    band state, T2 deferred". The riskiest assumption (networked chunked-delta gas
    consistency) dies first via a net spike over a primitive field; real band sim is
    built strictly AFTER stream lock; the spectacular clip (~2026-07-10) is rendered from
    band state with NO T2 dependency. C and A are degenerate configs of this design, so
    fallback migrations are cheap. Brief: work/research-g-9c41-core-architecture-2026-06-12-v2.md.
  done_when: |
    The day-one staged cut of g-9c41 (brief v2 §5): net stream locked, band state live,
    naive DA adapter, render proof slice + first clip, node criteria met. The full-node
    bar is TREE.md g-9c41 done_when 1–9; this bet delivers the day-one stage of it and
    proves the architecture that scales to the rest.
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
    - "dynamic thermics, plume entrainment -> bet-2 (day-one static temperature field)"
    - "physical destruction -> scripted breach event only (no destruction system)"
    - "matchmaking / lobby browser -> planned-for-EA, non-gating (harness = direct connect)"
    - "save/load -> none (ephemeral harness sessions; reproducibility from deterministic seeds)"
  lens_verdicts:
    - "commercial/traction: TASK — first spectacular clip ~07-10 opens the parallel tracks"
    - "core depth: not_needed as design (re-homed to g-d3a8); substrate proven incidentally (param gas + 1 reaction)"
    - "co-op-first: TASK — 2-4 clients see consistent gas across a topology change (the net spike)"
    - "technical feasibility: TASK — net consistency = riskiest assumption, the first task"
    - "scope/production: not_needed as a task — held by the cut list + G3 appetite"
    - "audience workflow: not_needed as bet work — the clip artifact feeds g-e6f2 (parked, <=10% until clip)"
  kill_by:
    metric: "per-tick state-hash consistency host + 2 clients through a scripted breach with both clamps engaged; measured dirty-chunk wire size within the aggregate host clamp at target tick"
    checkpoint_2026-06-30: "if consistency cannot be made to hold after reasonable iteration OR the steady dirty-rate irrecoverably blows the aggregate clamp -> P6 model/vendor spike (1-2wk timebox: FishNet<->NGO, last-resort rollback) or kill the bet"
    hard_2026-07-24: "day-one done_when unmet -> bet dies (G3, no extend); continuation = re-shape bet-2"
    next_if_true: "stream locked -> roll the wave (band sim after lock -> naive DA -> render slice + clip)"
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
    status: active   # 2026-06-13 dispatched as c-exec-003 (s-work-004). kill-gate "consistency" = owner-approved dual-guarantee "A": (i) LOSSLESS (deadband off) per-tick host-vs-client FIELD-cell hash bit-exact incl. breach; (ii) LOSSY (deadband + per-client clamp + aggregate host clamp) bounded divergence (<=quant step Q) every tick + bit-exact at settle/keyframe. Resolves the literal p2-vs-p3 tension (two runs, not one). Awaiting executor return (leg opens with PLAN + ADR-0003).
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
    status: blocked_on t-2

recurring: []

open_calls:
  - id: c-exec-003
    status: dispatched   # executor leg for t-2; opens with interactive PLAN + ADR-0003 in the product repo (owner present), then autonomous build legs
    note: framed at s-work-004 (c-work-002); hardened via an 8-agent ground+draft+adversarial-verify pass (wf_7dbb52a9-1c1); full CALL in next:; → history/s-work-004.md
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
      history/s-converge-001.md RESULT.next. Resolve d-converge-001 first.

decision_inbox:
  - id: d-converge-001
    status: open
    note: |
      Feed work/converge-g-9c41.md into the in-flight c-exec-003 PLAN before ADR-0003 freezes the
      stream magnitudes (C1–C22), or keep the retrofit parallel/demonstrative? Options A/B/C +
      recommendation A (feed as input evidence to the already-interactive, owner-present PLAN —
      cheapest capture of the retrofit's value, esp. the 4 params the c-exec-003 CALL left implicit
      C19/C20/C21/C22, without re-opening the bet or risking the G3 wall). See work/converge-g-9c41.md
      §ROUTE + history/s-converge-001.md decisions_needed.
      # d-arch-001 answered at s-shape-003 (see history/s-shape-003.md outcome a-e)

next: |
  CALL c-exec-003
  to: executor (coding agent)   repo: GasCoopGame   kind: engineering
  direction: indie-game-development   node: g-9c41   task: t-2
  parent: c-work-002 (s-work-004)
  leg_opens_with: |
    PLAN — interactive, plan mode, owner present, frontier model, in the product-repo dev worktree
    C:\projects\Unity\GasCoopGame_dev (branch dev; FIRST sync dev to current main HEAD @7af478a — dev
    is 5 commits behind; the tail is MCP/tooling cleanup, no core/sim change, t-1 contracts intact).
    The custom field-state stream is architectural (new transport plane + data/wire format) -> ADR-0003
    + owner approval BEFORE any code; no build before ADR-0003 is accepted and the G0 ledger is frozen.
    PLAN must DECIDE and FREEZE in ADR-0003 + the G0 ledger (builder cannot change): integer/fixed-point
    field representation + quantization step Q; the divergence threshold (recommend = Q — a provable
    consequence of deadband+quantization, not a tuned number); deadband magnitude + per-client clamp
    (~150 KB/s) + aggregate host clamp (~250-300 KB/s); the gas-plane channel reliability (unreliable-
    sequenced vs reliable — its OWN decision, NOT a default carryover from the input plane's reliable
    bus); the settle predicate N (dirty-chunks==0 for N ticks) + keyframe cadence K (or quiescence-only
    if keyframes are out of t-2 scope); the frozen toy-field scene profile (room count, chunk grid,
    total chunk count) committed as a config/seed file; the reproducibility constants (seed, run length,
    breach tick, target-tick offset); whether t-2 injects synthetic chunk loss/reorder or defers to t-3;
    late-join out of scope.
  model_routing: |
    BUILD = Claude Code + Opus 4.8 (planner frontier/high-effort owner-facing; builder default-tier
    autonomous, one feature smallest-first, reuse-first). VALIDATE = Codex + GPT-5.5 xhigh — read-only,
    fresh-context, different family, did not author; reproduces the dotnet core + dual-mode gates as a
    regression check; MUST NOT certify the transport/PlayMode axis from a dotnet run. Weaker model =
    gate-runner, never authority. Binding acceptance = green gates + evidence + owner spot-review on the
    novel netcode (s-decide-001). Fallback chain so overnight legs survive provider errors.
  goal: |
    Two co-op clients joined to a host see the host's gas field — a toy diffusing field — reconstructed
    on their own machines in step with the host, fed ONLY by the host streaming the chunks that changed;
    and when a scripted breach merges two rooms mid-run, that burst still arrives correctly and within a
    bounded bandwidth budget, with the FIRST honest numbers for how big that change-traffic is recorded
    as machine-readable artifacts. This is the net spike that retires the bet's riskiest assumption
    (networked chunked-delta gas consistency). t-2 TAKES the measurement; it does not judge it sustained-
    under-load (that is t-3).
  context: |
    Pointers (input evidence for PLAN, NOT a binding spec — PLAN owns the design):
    - Authoritative t-2 done_when (the 4 points, made machine-testable here): this NOW.md active_tasks t-2.
    - Bet rules R12-R15 + kill_by: this NOW.md active_bet. Load-bearing: R13 engine-free pure-C# core /
      Unity = adapters only; R14 net is an edge wrapper composed at the DI root, never in business logic;
      "gas rides OUR custom chunked-delta channel regardless of vendor".
    - Architecture brief v2 (fabric contracts, stream controls, honest dirty-chunk sizing, stub-but-not-
      skip list): work/research-g-9c41-core-architecture-2026-06-12-v2.md (status: informs, does not decide).
    - t-1 GREEN — the REAL contracts you build ON (do NOT redesign): engine-free integer-only 3-mode core
      + the ITickInputBus seam (InMemoryTickInputBus; SimHostFactory.CreateNetworked(seed,localPeerId,
      injectedBus) = the DI point), SimState/Fnv1a64 pinned-order hashing, and the FishNet adapter
      FishNetTickInputBus (host-relay lockstep over reliable-ordered broadcasts) + TickInputBroadcasts.
      Sources: Assets/GasCoopGame/Core/Sim/*.cs + Core/Hashing/Fnv1a64.cs; Assets/GasCoopGame/Net/FishNet/*.cs.
      → history/s-work-003.md
    - ADR-0002 (lockstep, field-never-networked-as-inputs; prediction/[Replicate]/[Reconcile]/
      NetworkTransform/SyncVars rejected). The field-STATE stream is the NEW concern -> ADR-0003.
    - Run contract / gates / review rubric / scratch rule / dev-worktree workflow: repo AGENTS.md +
      CLAUDE.md, validation.config (schema v1: core_build = the R13 dependency-boundary gate, tests,
      hygiene; one-shot `pwsh tools/check.ps1` -> "OK: all gates green"), REVIEW.md,
      openspec/specs/sim-core/spec.md (lifecycle propose->apply->verify->archive; archiving is part of done).
    - Editor/transport loop = the free IvanMurzak Unity MCP (agent runs PlayMode/EditMode + reads console).
      No CI on the transport/PlayMode axis (Unity Personal = no unattended activation) — see done_when p2.
    THE PIVOT (state it plainly to PLAN): t-1 networks INPUTS (lockstep, every peer recomputes the field,
    field never sent); t-2 networks the FIELD ITSELF as chunked quantized deltas — authoritative host =
    single writer, clients RECONSTRUCT without running the sim. This is a SECOND plane ALONGSIDE the input
    bus, not a change to it. The existing lockstep input path is reused ONLY to agree deterministically on
    WHICH tick the breach fires.
    THE KILL-GATE (owner-approved 2026-06-13, "A" — dual guarantee): "consistency holds" = (i) LOSSLESS
    (deadband disabled): per-tick host-vs-each-client FIELD hash bit-exact over the whole run incl. the
    breach — the correctness oracle; (ii) LOSSY (deadband + both clamps on): bounded divergence every tick
    + convergence to bit-exact at settle/keyframe points — where the honest wire numbers are measured.
  boundaries: |
    - TOY gas field ONLY (trivial room-graph diffusion as a throwaway chunk-traffic generator). NOT the
      band/sector solver, NOT stratification/strips, NOT the quasi-steady pressure solve, NOT the T2 grid
      — all post-stream-lock (t-3+/bet-2). Build the field thin; build the CONTRACTS it rides real.
    - Stub-but-not-skip (FORM declared now, exercised by one toy layer): the layer registry + the
      revision/change feed + the revision barrier — these survive to the band sim. Single-writer-per-
      (layer x phase), the phase-ordering form, and a resolution key in the wire are PLAN-shaped candidates
      whose exact form ADR-0003 fixes — NOT pre-decided here (NOW.md t-2 p1 gates only "layer registry +
      revision feed"). If PLAN hard-gates single-writer, prove enforcement by a NEGATIVE/seeded-violation
      test (a second writer to the same (layer x phase) is rejected -> red test), not happy-path-only.
    - The gas plane is OUR own channel ALONGSIDE FishNet; whether it is unreliable-sequenced or reliable is
      an ADR-0003 decision, NOT a default-to-reliable carryover from the input bus. Do NOT retrofit field
      state into ITickInputBus/TickInput/InMemoryTickInputBus/TickInputBroadcasts (input-only).
    - Net model LOCKED — no P6 / vendor re-open here; FishNet stays.
    - Do NOT redesign or weaken the proven t-1 core: keep the engine-free boundary (R13; core_build is the
      gate) and the determinism contract (no float/double, unchecked, no wall-clock, seeded RNG, pinned
      hash order, stable input order); the 8 core tests + the golden vector must stay green (a broken golden
      hash = blocker). No FishNet prediction/[Replicate]/[Reconcile]/NetworkTransform/SyncVars for the field.
    - Stay inside t-2's done_when. t-3 (sustained-breach-load consistency-HOLD + the clamp VERDICT +
      declaring the wire-format LOCKED) is a separate leg — t-2 RECORDS the honest numbers, does NOT
      pronounce the clamp-sustained verdict. Late-join / join-baseline is OUT of t-2 scope (all 3 peers
      present from tick 0; the revision/keyframe FORM is declared, mid-run join deferred to bet-2).
    - Builder must NOT edit validation.config / the ledger / the spec / REVIEW.md / acceptance criteria,
      nor touch the vendored Packages/com.firstgeargames.fishnet/. Nothing under _scratch/ is committed.
      Work ONLY in the dev worktree; never the main checkout (owner keeps Unity open on main).
  done_when: |
    Each of NOW.md t-2's 4 authoritative points is made verifiable by a runnable check; the concrete
    design values (Q, threshold, N, K, deadband, clamps, scene profile, reproducibility constants, loss-
    injection scope) are FROZEN in ADR-0003 + the G0 ledger BEFORE build and the builder cannot change them.
    (p1) Toy field through REAL contracts — an automated (EditMode/dotnet) test proves the host advances
      the room-graph diffusion driven through a real layer registry + a real revision/change feed (the
      contracts exercised by a test, not asserted in prose).
    (p2) Stream + reconstruct + the LOSSLESS correctness proof — host streams only changed chunks as
      quantized deltas over our own channel; clients reconstruct the field WITHOUT running the sim. The
      field hash = Fnv1a64 (pinned little-endian order, reused from t-1) over the RECONSTRUCTED FIELD CELLS
      ONLY (host's streamed cells vs each client's reconstructed cells — NOT the whole SimState.Hash(),
      which folds Delta + RNG the non-simulating client lacks; the breach-affected cells must be inside the
      hashed domain). In LOSSLESS mode (deadband disabled), per-tick host-vs-each-client field hash is
      BIT-EXACT EQUAL every tick over the whole run INCLUDING the breach. PRIMARY proof runs headless in
      pure dotnet over an in-memory analogue of the delta channel (host->2-client reconstruction),
      validator-reproducible via `dotnet test` + a committed golden vector — mirroring t-1's in-memory
      convergence proof; the FishNet/PlayMode loopback run (host + 2 real clients) is the transport-axis
      confirmation (agent-run via Unity MCP, or owner-run if MCP can't drive it — state which). "Lossless"
      is the PROPERTY "reconstruction is provably bit-exact"; HOW (full-precision wire vs exact-resend/
      keyframe) is ADR-0003. Lost/reordered chunks: include >=1 deterministic fault-injection variant
      (drop/reorder a chunk on a seeded schedule) asserting the revision barrier + keyframe/resend recovers
      to bit-exact at the next settle — OR, if PLAN defers fault-injection to t-3, downgrade this oracle's
      claim to "serialization/round-trip (clean channel)", note the unreliable-path correctness is NOT yet
      retired, and define the client's gap-recovery behavior. (Recommend: inject in t-2.)
    (p3) All three flow controls + the LOSSY bounded-divergence proof — deadband + per-client clamp +
      aggregate host clamp ALL live and exercised together. In LOSSY mode, machine-checked every tick:
      (a) bounded divergence — divergence(tick) = max over hashed field cells of |client_cell - host_cell|
      after dequantization <= the frozen threshold (recommend = the quantization step Q; any tick exceeding
      Q is a reconstruction bug, not lossy behavior); AND (b) convergence to bit-exact at settle points — a
      settle tick = host dirty-chunk count == 0 for N consecutive ticks (N frozen), where client hash ==
      host hash bit-exact; if keyframes are in scope, the tick after a keyframe (every K) is bit-exact. The
      test asserts >=1 quiescence settle AND (if keyframes in scope) >=1 post-keyframe equality actually
      occur (non-vacuous), INCLUDING the post-breach settle once merged rooms re-equilibrate. Lossless (p2)
      and lossy (p3) MUST share the SAME reconstruction code path (anti-gaming). NOTE: NOW.md p2 (per-tick
      hash equal across the breach) and p3 (deadband + clamps engaged) are satisfied in TWO DIFFERENT RUNS,
      not one — a single deadband-on run is not expected to be per-tick bit-exact.
    (p4) First honest MEASUREMENTS as machine-readable artifacts — taken in lossy mode through the breach:
      (a) honest dirty-chunk wire size in BYTES (on-wire payload after deadband+quantization; state whether
      transport framing is included) and (b) dirty-rate. Emitted as committed machine-readable artifacts
      under a named path OUTSIDE _scratch (e.g. docs/measurements/) with a fixed schema {seed, runTicks,
      breachTick, targetTick, sceneProfileHash, mode, perClientClampKBs, aggregateClampKBs, series:[{tick,
      onWirePayloadBytes, headerOverheadBytes, dirtyChunkCount}], peakTick, dirtyChunksPerSec, windowSeconds,
      perClient[], aggregate}. target tick = the tick of MAX aggregate dirty-chunk count in the breach burst
      (worst-case, not cherry-picked); the full per-tick series is included with the peak flagged; tick rate
      pinned (10 Hz day-one) so chunks/sec is derivable from chunks/tick. t-2 records the instantaneous
      peak-through-breach, explicitly NOT the steady dirty-rate t-3 judges. The brief's 0.6-6 KB is a logged
      SANITY reference only — t-2 records the measured number, it does NOT gate on landing in that range (no
      clamp verdict here — t-3). Both modes emit distinct named artifacts; "both present + non-empty +
      covering the breach tick range" is a checkable ledger line so a silently-dropped mode is a mechanical FAIL.
    Reproducibility: fixed toy-field seed, fixed run length, deterministic breach tick (broadcast over the
      lockstep input plane so all peers fire on the SAME tick), defined target-tick; the frozen scene profile
      committed as a config/seed file so t-3 reuses byte-for-byte the same topology. Peer count = exactly
      1 host + 2 clients = 3 peers (!= the brief's scene-load "профиль 32/12/2", which denotes scene size —
      decode to concrete counts). Environment honesty: t-2 measures on loopback with software clamps — the
      byte size + per-tick dirty-chunk COUNT are the honest, environment-independent numbers; the real-uplink
      sustained question is t-3.
    Process: ADR-0003 owner-approved before code; G0 ledger frozen (every entry opened failing, flipped only
      on opened evidence; builder never edits ledger/spec/criteria/config); all repo gates green on dev
      (`pwsh tools/check.ps1` -> "OK: all gates green"); the openspec change for t-2 archived; _scratch clean.
      Merge dev->main is owner-authorized at the final report.
  return: |
    A RESULT carrying: PR/commits on dev (+ owner-authorized merge to main); green gate outputs
    (tools/check.ps1) + the dotnet dual-mode artifacts (validator-reproducible) + the PlayMode/transport
    run output (MCP-run or owner-run, state which); the default-FAIL ledger in FINAL state (entries passing
    with opened evidence as a runnable command or file:line); the dual-mode hash/divergence evidence
    (lossless per-tick bit-exact incl. breach; lossy bounded-divergence-every-tick + bit-exact-at-settle);
    the TWO measured numbers as the committed artifacts (schema above); ADR-0003 (Status/Context/Decision/
    owner echo-numbered Rn/alternatives/consequences + the frozen design values); validator REVIEW.md
    (file:line, severity, nit cap 10; dotnet gates reproduced); manual owner-acceptance steps generated from
    the SAME verification scripts the validator ran; assumptions, anything cut, cost. Surface blockers early;
    stop if infeasible or 2x over budget.
  budget: |
    t-2 ONLY (toy field + custom chunked-delta stream + scripted breach + first honest wire measurement);
    band sim, sector subdivision, frequency ladder, DA occupancy, fp16 wire are OUT (bet-2/t-3+). One focused
    interactive PLAN with the owner first (architecture + ADR-0003), then a few autonomous build legs against
    the fixed 2026-07-24 G3 hard wall — one feature per leg, smallest-first, <= a focused half-day human-
    equivalent; split larger at shape. Overnight legs run the dotnet/in-memory correctness path as the PRIMARY
    autonomous evidence; the FishNet/PlayMode confirmation is a gated checkpoint that may wait for the owner
    without marking the leg failed. Retries <=2 in-context + 1 fresh-context per gate, hard cap 3; same finding
    class twice = non-convergence -> stop + escalate. Escalate (the only mid-run owner contact) on: retry
    budget exhausted, non-convergence, an out-of-plan decision (new dependency/scope/irreversible), or a
    sandbox/permission boundary. Tier-2 actions (merge/publish/delete non-versioned) + any new dependency are
    never auto-approved regardless of PLAN approval.
  surface: executor leg = a fresh session in the product-repo dev worktree C:\projects\Unity\GasCoopGame_dev;
        opens with an interactive PLAN (owner present), then autonomous build legs.

END_OF_FILE: live/indie-game-development/NOW.md
