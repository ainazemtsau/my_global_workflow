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
  hygiene script.
- **Unity PlayMode/EditMode CI (GameCI + license secret) DEFERRED** until engine-dependent tests
  exist — core logic is tested headless without a Unity license.

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

END_OF_FILE: os/engineering/profiles/unity.md
