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
  dependency-boundary gate stays the real headless COMPILE (§4), which EXECUTES, not a scan. Commit raw
  `tests-run`/query JSON with proof id/required actor and an exact manifest of product/test dependency blobs, selection and Unity/package/project identity; the gate derives that scope from frozen/repo authority and recomputes it.
  Equal manifests reuse valid JSON across merges and process changes; changed inputs or missing/invalid JSON owe a new run.
  MCP/Editor unavailable STOPs only when that run is owed; never use a scan stand-in.

- **Contract v24 mutation scope:** `-Deliver` independently derives changed `Assets/<Game>/Core/**/*.cs` files from the authoritative review diff and fails before score comparison if any is absent from the report's normalized explicit `scopeFiles`. The fresh reviewer derives that scope and runs mutation; builder-authored globs/reports/scores are not evidence. The runner derives exact file inputs from the diff and defaults concurrency to `min(24, max(4, floor(logicalProcessors / 2)))` (explicit override recorded). Scope is file-scoped, not line-scoped: a touched hot core file is mutated whole and may still take a long time.

**Contract v24 diff identity:** the run contract declares the integration-base ref and mutation-input roots (Core source, headless mutation tests/project, mutation/check tooling and config). Independent review evidence pins mutation-reviewed `H`; the report echoes `I` (current base-ref tip), `B = merge-base(I,H)`, and `H`. Deliver recomputes and exact-matches the tuple, rejects any dependency-root change after `H`, mutates rename destinations/current A/C/M/T Core files, and exact-matches deleted/rename-source Core paths in `removedFiles` before score.

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
  `dotnet` build; Unity generates `.meta` on first import. Run a batchmode import in the selected
  task slot to finalize asmdef GUID references before wiring adapters.
- **`.meta`-tracking hygiene gate (git-aware) — a tracked `.cs` requires a tracked `.cs.meta`:**
  the hygiene script (§2) FAILS when a git-tracked `Assets/**/*.cs` has no git-tracked `.cs.meta`
  sibling (or an orphan `.cs.meta` exists). This catches the refresh→commit timing gap — a `.cs`
  committed while its Unity-generated `.meta` stays untracked — which the headless `dotnet` build
  and the batchmode-import step above do NOT cover (the seam between the Unity/git world and the
  `dotnet` world has no other guard).
- **The dependency-boundary gate is the headless core build itself** — no separate linter needed:
  no Unity reference in the core csproj → any `using UnityEngine;` in core fails `dotnet build`.

## 5. Setup notes
- **Permanent-slot pattern:** setup binds each fixed task worktree to one permanent branch. A task
  selects an available slot; it never creates or switches branches/worktrees. Released clean branches
  fast-forward to published `dev`; occupied or paused bytes remain untouched. Handoff cites exact SHA;
  after integration the same branch fast-forwards and becomes available. Encode the mapping in AGENTS.md.
- **Unity version:** pick the latest **LTS** (e.g. 6.3 = `6000.3.x`) for commercial builds, NOT the
  tech stream (`6000.4.x`, numerically higher but non-LTS). Install via Unity Hub — manual, agents
  cannot drive the Hub GUI; treat "install Unity + create project" as the owner's physical step.
- **TFMs:** core `netstandard2.1` (Unity loads it on the default scripting runtime); tests `net8.0`.
- .NET SDK must be installed separately for the headless build (`dotnet`) — not bundled with Unity Hub.

## 6. Contract v29-v31 candidate/pair timing

- A compiled PAIR-CANDIDATE reruns both the headless repo-native build and existing git-aware hygiene after its last
  carrier edit, then runs the real RED command. Headless compile GREEN alone is not an eligible pair.
- Every new `Assets/**/*.cs` and its tracked `.cs.meta` are in the same carrier commit. The earlier note that a
  missing `.meta` is tolerable for an inner-loop headless build does not make it tolerable at pair freeze.
- A mechanically generable script sidecar may be created in PAIR-CANDIDATE. If correctness depends on Unity's
  real importer and Unity is unavailable, STOP and ask the owner to launch it; do not guess or defer the sidecar.
- The exact carrier and RED commits freeze together only after the real test command compiles, discovers
  the intended tests, fails on behavior, and a fresh refutation accepts the pair.

END_OF_FILE: os/engineering/profiles/unity.md
