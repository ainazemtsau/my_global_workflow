# Stack profile: unity (engine-free-core Unity game)

First created 2026-06-13 (GasCoopGame setup, indie-game-development/g-9c41). Format: `profiles/README.md`.

## 1. Module conventions
- **Engine-free core is the spine.** All game logic in a pure-C# core; Unity = render/input/
  transport adapters only. Core under `Assets/<Game>/Core/` with an asmdef whose
  `"noEngineReferences": true` — Unity compiles it WITHOUT UnityEngine (mechanical R13). Set
  `autoReferenced: false` so it doesn't leak into Assembly-CSharp; adapters reference it explicitly.
- **Dual build of the same sources:** a root `core/<Game>.Core.csproj` (`netstandard2.1`,
  `EnableDefaultCompileItems=false`, `<Compile Include="..\Assets\<Game>\Core\**\*.cs"><Link>`)
  compiles the SAME files headlessly via `dotnet`. One source of truth, two compilers.
- Unity-side module boundaries = Assembly Definitions (asmdef); violations fail compilation.

## 2. Default validation.config thresholds
- Retry budget 3/gate; non-convergence = same failure class twice → stop.
- Gates: `dotnet build core/<Game>.Core.csproj` (boundary), `dotnet test <testproj>` (headless),
  hygiene script, **G2 diff-scoped mutation (Stryker.NET on the headless core) ≥ the
  `mutation_kill_floor` config key — score recorded for the deliver check** (this runs on the
  engine-free core, so it needs NO Unity license; only PlayMode/EditMode CI is deferred).
- Deliver (`pwsh tools/check.ps1 -Deliver`) also enforces the strong-check enablement gate
  (PROJECT_SETUP §Strong-check enablement): recorded mutation score ≥ floor + a non-empty
  spec-silence-audit section in the frozen change spec — `dotnet test` passing is NOT G2 on its own.
- **Unity PlayMode/EditMode CI (GameCI + license secret) DEFERRED** until engine-dependent tests
  exist — core logic is tested headless without a Unity license. **Deferring PlayMode CI does NOT
  exempt an engine-side DELIVERABLE from existence** (VALIDATION.md §Enabled ≠ written, CONTOUR §c):
  a promised scene/prefab/composer/adapter still needs a ledger row whose closure the deliver check
  trips on — the license-free form is a `Test-Path` on the committed artifact (a `*.unity` / prefab /
  asset under `Assets/<Game>/`, NOT a vendor sample) or a recorded MCP/batch-run artifact (path +
  hash) under `docs/measurements/`. The proof must be NON-TRIVIAL — a recorded run artifact carries a
  measurement (node / cell / spawned-object count > 0) and a committed scene is asserted above a stub
  floor — so an empty placeholder file cannot satisfy the existence row. This gates BUILD-exists
  without a license; only the owner LOOK (the eyeball) stays the manual A2.4 axis.
- **Render / shader / scene BEHAVIOR evidence = a real run, never a source scan** (VALIDATION.md
  §Behavior evidence by venue). The existence proof above closes BUILD-exists (the artifact is
  present); it is NOT render-behavior. Behavior for a GasVisual / shader / scene leg is a real
  **EditMode/PlayMode run via the Unity MCP** (`tests-run`) or a **live-editor MCP structural query**
  (scene / component / material state), plus **owner-eye** for the look; engine-free logic stays
  headless `dotnet test`. A **self-written source-text scanner/parser** over `.cs` / `.shader` /
  `.hlsl` is FORBIDDEN as behavior evidence — it proves text-presence, not rendering — and a negative
  control / property test never attaches to it (hardening a scanner is the arms-race engine). The
  dependency-boundary gate stays the real headless COMPILE (§4), which EXECUTES, not a scan. Unity MCP
  dropped / Editor not launched ⇒ STOP and ask the owner to launch it (contract v16), never a scan
  stand-in.

## 3. Test layout
- Headless core tests: `tests/<Game>.Core.Tests/` (`net8.0`, **NUnit** — same family as Unity's Test
  Framework, so assertions transfer). Run via `dotnet test`.
- Unity tests later: `Assets/Tests/` (EditMode/PlayMode), one registered test-scene root.

## 4. Known landmines + mechanical fixes
- **Unity `.gitignore` ignores `*.csproj`/`*.sln`** (it regenerates its own at root). Hand-authored
  headless `core`/`tests` projects + solution are real source → add `!`-exceptions
  (`!/core/**/*.csproj`, `!/tests/**/*.csproj`, `!/<Game>.Core.sln*`).
- **`/[Oo]bj/` in the Unity template is ROOT-ANCHORED** — nested `core/obj`, `tests/**/{bin,obj}`
  from `dotnet` are NOT covered. Add non-anchored `[Bb]in/` + `[Oo]bj/`.
- **`dotnet new sln` on .NET SDK 9/10 emits `.slnx`** (XML), not `.sln`. Use/track the `.slnx`
  (`dotnet sln x.slnx add` works on SDK 9+). For CI on older SDKs, target the `.csproj` paths, not
  the slnx, so the SDK version doesn't matter.
- **Hand-authored core/test files have no `.meta`** until Unity imports them — fine for headless
  `dotnet` build; Unity generates `.meta` on first import. Run a batchmode import in the dev
  worktree to finalize asmdef GUID references before wiring adapters.
- **`.meta`-tracking hygiene gate (git-aware) — a tracked `.cs` requires a tracked `.cs.meta`:**
  the hygiene script (§2) FAILS when a git-tracked `Assets/**/*.cs` has no git-tracked `.cs.meta`
  sibling (or an orphan `.cs.meta` exists). This catches the refresh→commit timing gap — a `.cs`
  committed while its Unity-generated `.meta` stays untracked — which the headless `dotnet` build
  and the batchmode-import step above do NOT cover (the seam between the Unity/git world and the
  `dotnet` world has no other guard).
- **The dependency-boundary gate is the headless core build itself** — no separate linter needed:
  no Unity reference in the core csproj → any `using UnityEngine;` in core fails `dotnet build`.

## 5. Setup notes
- **Dev-worktree pattern (Unity + agent coexistence):** owner keeps Unity open on `main`; the agent
  works in a persistent sibling git worktree (`<repo>_dev`, branch `dev`) — edits, `dotnet`, Unity
  batchmode — then merges `dev`→`main` when gates are green. ONE persistent worktree, not per-feature.
  Encode the rule in the repo's AGENTS.md.
- **Unity version:** pick the latest **LTS** (e.g. 6.3 = `6000.3.x`) for commercial builds, NOT the
  tech stream (`6000.4.x`, numerically higher but non-LTS). Install via Unity Hub — manual, agents
  cannot drive the Hub GUI; treat "install Unity + create project" as the owner's physical step.
- **TFMs:** core `netstandard2.1` (Unity loads it on the default scripting runtime); tests `net8.0`.
- .NET SDK must be installed separately for the headless build (`dotnet`) — not bundled with Unity Hub.

## 6. Contract v23 SURFACE-FREEZE timing

- A compiled SURFACE-FREEZE handoff runs both the headless repo-native build and the existing git-aware hygiene gate
  before any independent RED session. Headless compile GREEN alone is not an eligible carrier.
- Every new `Assets/**/*.cs` and its tracked `.cs.meta` are in the same freeze commit. The earlier note that a missing
  `.meta` is tolerable for an inner-loop headless build does not make it tolerable at SURFACE-FREEZE.
- A mechanically generable script sidecar may be created in the surface session. If correctness depends on Unity's
  real importer and Unity is unavailable, STOP and ask the owner to launch it; do not guess or defer the sidecar.

END_OF_FILE: os/engineering/profiles/unity.md
