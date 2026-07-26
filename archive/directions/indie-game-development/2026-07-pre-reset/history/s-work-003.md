# s-work-003 — work (g-9c41 / t-1): apply executor return c-exec-002

- **date:** 2026-06-13
- **play:** work (one task of the active bet)
- **task:** t-1 — engine-free core scaffold + networked harness handshake
- **CALL applied:** c-exec-002 (executor, engineering) — built in product repo
  github.com/ainazemtsau/GasCoopGame (dev worktree), per repo AGENTS.md run contract.

## Recite

t-1: engine-free C# core gains a real deterministic sim-core with a 3-mode composition root
(pure-local / local host-loop / networked; no net types in core), and a networked harness where a
FishNet host + clients agree on a per-tick state hash of a TRIVIAL field — the network-first spike
(riskiest assumption #1), NOT gas sim. Serves bet g-9c41 (kill-gate = chunked-delta consistency).

## RESULT — DONE (verdict GREEN)

Self-check vs the 4 done_when points (evidence = artifacts/commits, not claims):

1. **Core = pure C#, 0 Unity refs, builds/runs headless** ✅ — `dotnet build core/GasCoopGame.Core.csproj`
   0 warnings/errors; the headless boundary gate compiles only `Assets/GasCoopGame/Core/**`. Integer-only
   sim (`SimState` trivial grid + `SimCore.Step` reducer + `DeterministicRng` SplitMix64), all `unchecked`,
   pinned-order FNV-1a per-tick hash (reused from `CoreBuildMarker`).
2. **3-mode composition root, test selects mode, no net types in core** ✅ — `SimMode` +
   `SimHostFactory` (PureLocal / LocalHostLoop / Networked) over the engine-free `ITickInputBus` seam;
   the in-memory bus lives in core, the FishNet bus in a separate `GasCoopGame.Net.FishNet` asmdef.
3. **Per-tick state-hash EQUAL, host + 2 headless clients, seeded run** ✅ — proven two ways:
   (a) dotnet 3-instance convergence test (600 ticks) + committed golden vector, CI-able /
   validator-reproducible (8/8 `dotnet test`); (b) **FishNet host + 2 real loopback clients**
   (`HostAndTwoClients_…`, peerCount=3, cross-peer-only inputs so the socket is load-bearing) PASSED,
   agent-run via the Unity MCP (`tests-run`) on Unity 6000.3.17f1, ~7s. Lockstep model: FishNet =
   reliable-ordered INPUT bus, prediction bypassed; each peer's identical deterministic core computes
   the field; the field is never networked.
4. **FishNet verdict recorded** ✅ — ADR-0002. **GREEN**: core determinism GREEN+CI; reliable-ordered
   transport convergence GREEN; packet/channel limits fine. **YELLOW-deferred:** Steam transport
   (FishySteamworks uncertified vs FishNet 4.7.2/Unity 6) + literal 3-headless-processes-in-CI
   (Unity Personal license has no unattended activation — accepted re-scope R1). Red → P6 not triggered.

## Evidence pointers

- Repo: github.com/ainazemtsau/GasCoopGame — t-1 merged dev→main @daab33d, pushed; ADR-0002 +
  archived OpenSpec change `t-1-net-determinism` + living spec `openspec/specs/sim-core`.
- FishNet pinned 4.7.2, vendored as an embedded package under `Packages/` (UPM-git-URL install hit an
  EPERM on Windows; embedded-package is the working install — logged to the repo FRICTION).
- Validation per s-decide-001 dual-model contract: binding acceptance = green gates + evidence + owner
  spot-review on novel netcode — all satisfied; owner ran/checked the tests and confirmed ("проверил, done").

## Decisions / captures (no scope expansion — bet cut list is law)

- **Editor bridge switched** off the paywalled official Unity MCP (`com.unity.ai.assistant` — ~$10/mo
  Unity AI seat AND no dedicated test-runner tool) to the FREE **IvanMurzak/Unity-MCP** (Apache-2.0;
  dedicated `tests-run`; self-contained .NET binary; CI-pinned on the Unity 6.3 line). Decided via a
  5-agent functional comparison (workflow wf_bf807a93-95e). Now live: the agent runs PlayMode/EditMode
  tests + reads the console directly — collapses the iterate-to-green loop for t-2+. See memory
  `unity-mcp-official-configured`. (Tooling decision; no tree/bet change.)
- Three FishNet integration facts encoded + documented (SpawnablePrefabs required even when nothing
  spawns; default `PersistenceType.DestroyNewest` → set AllowMultiple for in-process host+clients;
  embed under `Packages/`, not `Assets/` or a UPM git URL).

## State changes (applied by this session as writer)

- NOW.md active_tasks **t-1 → done** (evidence note + this pointer).
- NOW.md active_tasks **t-2 → ready** (unblocked).
- NOW.md `next:` reframed **c-exec-002 → c-work-002** (plan t-2, owner present for the stream PLAN,
  then frame executor CALL c-exec-003).
- LOG.md entry appended.

## Next

**c-work-002** — work session for t-2 (toy gas field + our custom chunked-delta stream + breach +
first wire measurement), owner present for the architecture/PLAN step, which frames the t-2 executor
CALL c-exec-003. The kill-gate (t-3) is still the consistency-under-breach hold; t-1 turned risk #1
(net consistency for a trivial field) into a measured GREEN fact, on schedule for the 2026-07-24 G3 wall.

END_OF_FILE: live/indie-game-development/history/s-work-003.md
