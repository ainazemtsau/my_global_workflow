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
    status: blocked_on c-setup-001   # product repo being RE-CREATED from scratch (PROJECT_SETUP, NEW repo, Unity 6.3 LTS); t-1 build CALL issues after setup DONE
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
  - id: c-setup-001
    status: in_flight
    note: |
      Setup executor (engineering) CALL — repo bootstrap per os/engineering/PROJECT_SETUP.md.
      Owner decided 2026-06-13: FULL clean RE-CREATE of the product repo on a NEW repo, latest
      Unity 6.3 LTS (old repo was Unity 6.4 tech-stream + codex-native-execution-layer harness —
      both retired). ADR-0001 architecture: engine-free C# core (.csproj, netstandard2.1,
      headless dotnet build/test, 0 Unity refs) + Unity render/input/transport adapters; core-CI
      day-1, Unity PlayMode-CI deferred; byproduct os/engineering/profiles/unity.md. SUPERSEDES
      retired c-exec-001 (built on the now-to-be-deleted foundation). Full CALL in `next`. Owner
      physical step: install Unity 6.3 LTS via Hub. Clears on its RESULT (DONE/NEEDS INPUT/STUCK).

decision_inbox: []   # d-arch-001 answered at s-shape-003 (see history/s-shape-003.md outcome a-e)

next: |
  CALL c-setup-001
  to: executor
  kind: engineering (repo bootstrap — os/engineering/PROJECT_SETUP.md)
  repo: NEW github.com/ainazemtsau/GasCoopGame (fresh; old repo renamed -> GasCoopGame-archive,
        kept read-only as evidence; local C:\projects\Unity\GasCoopGame re-created clean)
  direction: indie-game-development
  node: g-9c41   task: t-1 (PRECONDITION — setup runs BEFORE the t-1 build)
  parent: c-work-001
  goal: |
    A fresh, OS-aligned product repo exists and PASSES the PROJECT_SETUP done-when checklist:
    a clean Unity 6.3 LTS project whose architecture puts ALL game logic in an engine-free C#
    core that builds & tests HEADLESS (zero Unity refs, mechanically enforced), with Unity
    reduced to render/input/transport adapters — set up entirely through OUR process, not the
    old harness. This is the precondition the t-1 net-spike then builds on.
  context: |
    - REPLACES the old GasCoopGame (codex-native-execution-layer harness, Unity 6.4 tech-stream,
      A1_SETUP_ONLY). Full clean slate, owner-decided 2026-06-13 (R1 delete+recreate, R2 strictly
      our process, R3 latest Unity, R4 new repo). Old repo archived as evidence, never a build target.
    - Owner stack interview (PROJECT_SETUP step 1) -> ADR-0001:
      * Unity 6.3 LTS (6000.3.x, latest patch in Hub; LTS to Dec 2027). NOT the 6.4 tech stream.
      * Engine-free core = standalone .NET project (.csproj/.sln), TARGET netstandard2.1 (Unity can
        always load it); test project TARGET net8.0 via `dotnet test`. (R13.)
      * Unity = render/input/transport adapters only; networking is an edge wrapper (R14).
      * Net vendor FishNet enters in t-1, NOT setup (transport seam left empty).
      * Core-gate CI from day one (dotnet build/test + dependency-boundary lint — no Unity license);
        Unity PlayMode CI (GameCI + license secret) DEFERRED until engine-dependent tests exist.
    - Run contract to INSTALL = os/engineering/CONTOUR.md distilled into root AGENTS.md
      (planner/builder/validator; plan->ledger->build->gates->report; builder cannot weaken the
      oracle; retries<=3 then escalate; done = gates green + evidence). NOT the codex layer.
    - Bet rules R12-R15 (this NOW.md) constrain the architecture.
  boundaries: |
    - Owner has NO deep Unity experience: make every Unity-specific choice yourself with a
      plain-language rationale in the report; do not ask the owner to adjudicate Unity internals.
    - Owner physical step (cannot be automated — Hub GUI): install Unity 6.3 LTS + create the Unity
      project. Everything else (core .csproj, asmdefs, gates, CI, profile, run contract) is yours.
    - GitHub destructive ops (rename/archive the old repo, create the new one) need an explicit
      owner go at execution time before running them.
    - NO gameplay / gas / networking code in setup — the empty, gated skeleton only (t-1+ fill it).
    - Do NOT import old code/foundation (R2 clean slate). Old CoreFoundation/GridTopology are
      reference-only; re-create only what t-1 needs, fresh, in the new module layout.
  done_when: |
    The PROJECT_SETUP "Done when" checklist passes WITH EVIDENCE:
    - one-command check (format+lint+type+tests) green locally AND in CI;
    - dependency-boundary check exists and FAILS on a seeded violation (e.g. UnityEngine ref in core);
    - the engine-free core builds & tests HEADLESS via `dotnet` with ZERO Unity refs;
    - root AGENTS.md <=150 lines with working commands + the run-contract section; >=1 module AGENTS.md;
    - REVIEW.md, validation.config, docs/adr/ADR-0001 (the stack decision above), docs/FRICTION.md,
      openspec/ exist;
    - `_scratch/` exists and a seeded file in it cannot be committed;
    - test-hygiene gates fail on seeded violations;
    - os/engineering/profiles/unity.md CREATED (byproduct) and returned in state_changes;
    - Unity PlayMode CI with license recorded as DEFERRED (explicitly out until adapters exist).
  return: |
    REPORT: the PROJECT_SETUP checklist with evidence per item (commands + outputs), the new repo
    URL, ADR-0001 text, the created os/engineering/profiles/unity.md (in state_changes for the
    workflow repo), assumptions, anything deferred. State DONE | NEEDS INPUT | STUCK. Surface
    blockers early (Unity license, Hub install). On DONE -> next = the t-1 build CALL on the clean
    repo (engine-free core scaffold + 3-mode composition root + FishNet host+2-client hash handshake
    + honest FishNet verdict; the retired c-exec-001 is the template for it).
  budget: a focused one-time setup pass; 2x over or a hard blocker (license/Hub) -> stop & report.
  surface: cli; owner installs Unity 6.3 LTS via Hub in parallel.

END_OF_FILE: live/indie-game-development/NOW.md
