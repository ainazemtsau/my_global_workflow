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
  forecast: "net consistency holds — every working precedent (SS14/Stationeers/Noita) does chunked single-writer delta; the plan kills this risk first; the Fable-5 window catches the hardest net tasks"
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
    kind: executor (Fable 5)
    status: ready   # repo setup DONE 2026-06-13 (c-setup-001; CI green, commit 5fe3b3b on main); next = c-exec-002 build CALL
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
    kind: executor (Fable 5)
    status: blocked_on t-1
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
    kind: executor (Fable 5 if before 2026-06-22, else Opus 4.8)
    status: blocked_on t-2

recurring: []

open_calls:
  - id: c-frame-002
    status: queued
    note: |
      Frame touch-up — encode the owner's 2026-06-12 money-gate clarification into
      CHARTER.md: December mark = small income OR credible potential (matches the
      charter's existing reframe letter); NEW hard wall = the game earning for real by
      ~12 months (EA no later than ~Q2 2027). Map session s-map-002 could not edit the
      charter (play boundary).

decision_inbox: []   # d-arch-001 answered at s-shape-003 (see history/s-shape-003.md outcome a-e)

next: |
  CALL c-exec-002
  to: executor
  kind: engineering
  repo: github.com/ainazemtsau/GasCoopGame — work in the dev worktree
        C:\projects\Unity\GasCoopGame_dev (branch dev); merge to main when gates green (per repo AGENTS.md)
  direction: indie-game-development
  node: g-9c41   task: t-1
  parent: c-work-001
  goal: |
    t-1 met on the clean repo: the engine-free C# core gains a real deterministic sim-core with a
    composition root selectable into 3 modes (pure-local / local host-loop / networked host+clients;
    no network logic in core/business classes), and a networked harness where a FishNet player-host +
    2 headless clients run a deterministic fixed-tick loop and AGREE on a per-tick state hash of a
    TRIVIAL field over a fixed seeded run — plus a recorded honest FishNet viability verdict. The
    network-first spike (riskiest assumption #1), NOT gas simulation.
  context: |
    - Repo is OS-aligned and CI-green (setup c-setup-001 DONE 2026-06-13, main @5fe3b3b). Build ON the
      existing scaffold: Assets/GasCoopGame/Core (asmdef noEngineReferences) + headless
      core/GasCoopGame.Core.csproj + tests/ (net8.0 NUnit) + tools/check.ps1 + core CI. Replace the
      CoreBuildMarker placeholder with the real core; reuse its FNV-1a as the per-tick state hash.
    - Conventions live in the repo — follow them, the OS does not restate them: root AGENTS.md (run
      contract + dev-worktree workflow + commands), Assets/GasCoopGame/Core/AGENTS.md (engine-free +
      determinism), REVIEW.md, validation.config, docs/adr/ADR-0001.
    - Authoritative done_when (4 points): this NOW.md active_tasks t-1.
    - Architecture brief (input evidence, not binding): work/research-g-9c41-core-architecture-
      2026-06-12-v2.md §3.4 tick phases, §5 day-one stub-but-not-skip contracts.
    - Bet rules R12-R15. FishNet = default vendor; verdict HONEST (red -> P6 fallback, never a forced pass).
  boundaries: |
    - TRIVIAL field only (one scalar per node, pure deterministic tick). NO gas sim/bands/diffusion (t-2+).
    - Net model locked (P6: one player hosts, no dedicated server). Do not redesign.
    - Adding FishNet is a NEW DEPENDENCY -> owner approval in PLAN; determinism + netcode = architectural
      -> ADR + owner conversation BEFORE building.
    - Work in the dev worktree; never edit the main checkout (owner's Unity Editor). Merge to main when green.
    - Stay inside t-1 done_when; t-2/t-3 are separate.
  done_when: |
    t-1's 4 points, each by a runnable check: (1) core builds/tests headless, 0 Unity refs (existing
    gate); (2) 3-mode composition root, a test selects a mode, no net types in core (dependency check);
    (3) FishNet host + 2 HEADLESS clients, deterministic fixed-tick, per-tick TRIVIAL-field hash EQUAL
    across all three over a fixed seeded run; (4) FishNet verdict recorded (green|yellow|red: packet/
    channel limits, headless x3, Steam transport).
  return: |
    REPORT: commits/PR on dev (merged to main when green), outputs of the headless build + the
    3-instance hash-equality run, the FishNet verdict, assumptions, anything cut. DONE | NEEDS INPUT |
    STUCK. On DONE -> a fresh session verifies (G5, refute, different model) and advances t-1; next =
    c-work-002 (t-2). Red FishNet verdict -> P6 fallback spike, not a forced pass.
  budget: one focused half-day (executor sizing); 2x over -> stop & report.
  surface: cli, Fable 5 window (closes 2026-06-22) — hardest net task; owner present for the PLAN/FishNet step.

END_OF_FILE: live/indie-game-development/NOW.md
