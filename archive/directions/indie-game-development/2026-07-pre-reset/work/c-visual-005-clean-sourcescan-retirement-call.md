# CALL c-visual-005 — clean visual source-scan retirement (re-derive on v14)

to: executor (coding agent, GasCoopGame_dev_2 worktree — the REAL gas visual; never dev)
for: g-7e15 (VISUAL) / retire the visual source-scan crutch HONESTLY
issued: 2026-07-04 (s-work-045)
supersedes: the off-book leg GasCoopGame_dev_2 @3858752 "Close visual source-scan retirement"
  (binding-G5 NOT met, s-work-044 — do NOT merge or build on it)
base: current GasCoopGame main @cde4c3d (engineering contract v14+). NOT the v11 dev_2 tip.

## goal

The visual text/source-scan crutch is retired for real: the four visual `*ScanTests.cs` are gone,
the c-visual-003 SHADER/LAMP/SAMPLE scan wording in spec/tasks/ADR is retired, and the ONLY thing
that stands in for "the artifact is wired" is a GENUINELY EXISTENCE-ONLY smoke (no source-text
scanning of ANY kind) — with the real gas VISUAL behavior owned, as always, by Unity + owner-eye.
The wanted shader/camera improvements ride along, DECLARED. Nothing else.

This is a CLEAN, SINGLE-CONCERN re-derivation on current main. The dev_2 @3858752 diff is the
REFERENCE for what the visual/shader/camera pieces should look like — copy the WANTED pieces,
drop everything else, and fix the one thing @3858752 got wrong (its "wiring smoke" still scanned
source text).

## why this exists (owner-signed 2026-07-04)

Owner: visual is accepted ("по визуалу всё окей"); the shader work is wanted ("естественно, нужны —
это главная задача была"). The networking that rode into @3858752 is OUT (see boundaries). The route
(re-derive clean on v14) is owner-approved option 1 of d-visual-sourcescan-route-001.

## context / reference

- Reference diff (WANTED pieces to re-apply): GasCoopGame_dev_2 @3858752 vs its parent bc25a33.
- The binding-G5 record: live/indie-game-development/history/2026-07-04-s-work-044-visual-sourcescan-retirement-binding-g5.md
- v14 main `tools/check.ps1` L25 STILL hardcodes the `DELIVERED on \`dev\`` status assertion and its
  literal is "(engine-only)" — it is an ENGINE-worktree gate. It does NOT apply to a dev_2 visual leg.
  @3858752's mistake was self-editing that gate to accept dev2; DO NOT repeat it (see boundaries).

## step 0 — preserve + reset (before any build)

1. In GasCoopGame, tag @3858752 so it is never lost:
   `git tag ref/visual-sourcescan-leg-3858752 3858752` (this preserves the FishNet + shader + camera
   reference for the future Sc-net slice and this re-derive). Do NOT delete the commit.
2. Start the re-derive from a CLEAN state based on current main @cde4c3d (fresh dev_2 branch/worktree
   state off main). Do NOT build on top of @3858752.

## KEEP — re-apply these from @3858752, cleanly, on v14

- DELETE the four visual scan tests: GasLightBinderScanTests.cs, GasUberShaderScanTests.cs,
  GoodSampleScanTests.cs, SingleCustomEditorScanTests.cs (under Assets/Tests/EditMode/.../GasVisual/).
- RETIRE the c-visual-003 SHADER/LAMP/SAMPLE scan wording in openspec/specs/gas-visual/spec.md,
  openspec/changes/c-visual-003.../tasks.md, docs/adr/ADR-0020 → replace with "wiring-smoke (existence-only)
  + Unity/MCP/owner-eye" evidence wording (as @3858752 did — that part was honest).
- KEEP the real headless math tests: GasShaderDepthMathTests.cs + Render/Contracts/GasShaderMath.cs
  `SceneDeviceDepth` (the depth remap the occlusion uses) — these are genuine computed-behavior tests.
- KEEP the GasUber.shader improvements: the duplicate-URP-sampler compile fix AND the scene-depth
  OCCLUSION feature (DeclareDepthTexture include + GASUBER_DEPTH_CLAMP: walls occlude the gas volume)
  + GasVisualRenderFeature depth wiring (ConfigureInput(Depth) + UseTexture). But DECLARE the occlusion
  feature explicitly in the RESULT outcome and the spec/ADR (it is a real LOOK change, not cosmetic).
- KEEP the camera fixes + their plumbing: GasDemoPlumeControls (Open Arena Jet replay: force real gas
  source, apply camera bookmark, stop on the visible jet frame), GasDemoRoomCameraControls + the
  GasRoomScene.unity serialization (LP1 Proof front-facing camera), GasRoomSceneSetup, and the minimal
  ApplyNow()/RefreshNow() the replay needs (GasViewToggles, RealGasViewSource, VoxelOrbitCamera).

## the ONE fix vs @3858752 — the wiring smoke must be EXISTENCE-ONLY

@3858752's GasVisualWiringSmokeTests.cs STILL scanned source text (File.ReadAllText().Does.Contain(
"// GASUBER_WARP"/"// GASLIGHTBINDER"/"// GOODSAMPLE") + a Directory.GetFiles(*.cs)+CountOccurrences==1
glob). That is the very source-scan-as-evidence this leg exists to retire. REWRITE the smoke to assert
ONLY: the required assets/files EXIST (File.Exists), and/or a type/component/asset is PRESENT with the
expected identity (via reflection/asset-load, NOT text). ZERO File.ReadAllText/Does.Contain/glob-count
over source or shader TEXT. If a genuine "wired exactly once" property is needed, assert it via the
type system / asset graph, not by counting a token in .cs files. If a claim can only be verified by
reading source text, it is NOT a wiring smoke — it is behavior, and behavior is owner-eye/Unity.

## boundaries — OUT of scope (do NOT touch)

- ALL FishNet networking: FishNetTickInputBus.cs, FishNetConvergenceTests.cs, the Net EditorMode asmdef.
  Preserved on tag ref/visual-sourcescan-leg-3858752 for the future Sc-net slice. NOT this leg.
- ALL gate/tooling edits: do NOT edit tools/check.ps1, do NOT add tools/package-lock-check.ps1, do NOT
  bump Packages/manifest.json or the lock. A leg may NEVER self-edit the gate it is graded by. If a
  branch-aware DELIVERED gate is genuinely wanted repo-wide, that is a SEPARATE reviewed tools/ change
  with an ADR — never inside this feature leg.
- The benchmark-scan concern: do NOT touch TypeId.cs (no Equals narrowing), GasRosterConfig.cs
  (no ClampRosterSize), VoxelBenchmarkDirector.cs, or their acceptance tests. That is a different
  concern; if wanted it is its own leg. This leg is VISUAL source-scan only.
- No new source parser, Roslyn/shader parser, pixel-readback, or golden-image harness (as @3858752 also
  correctly avoided).

## close / done_when

- Only the KEEP items + the existence-only smoke are in the diff; the diff MATCHES the declared outcome
  (no undeclared scope — the RESULT outcome lists every behavior/render change, incl. the occlusion feature).
- The four *ScanTests.cs deleted; zero surviving references; NO source-text scan anywhere in the new smoke.
- Normal gates green on v14 (build + headless tests + hygiene + zero-float + int-overflow + type-hardcode +
  negative-control + review-evidence, whatever v14's non-delivery gates are) — WITHOUT editing any gate.
  The engine "DELIVERED on \`dev\`" status assertion is NOT invoked here (dev_2 visual close = owner-eye +
  normal gates), so it does not need to be satisfied or changed. Confirm at fire-time how v14 visual legs
  close and follow that; if unclear, STOP and ask the owner rather than editing check.ps1.
- Unity/MCP smoke on dev_2 (shader compiles clean, scene loads) + OWNER-EYE: owner presses Play, Restart
  Open Arena Jet, LP1 Proof, and confirms the look incl. the walls-occlude-gas occlusion (a step sent to
  the owner is not done until he confirms — no self-marking owner-run steps).
- BINDING fresh-session G5 (separate session, try-to-refute) before "done" — especially re-checking the
  smoke is truly source-scan-free and the diff has no undeclared scope.
- dev_2→main merge OWNER-GATED.

## fire

Fire in a FRESH GasCoopGame_dev_2 session (owner-present PLAN, per the visual-track discipline).
§Re-sync at fire (the base is main @cde4c3d — confirm the tip). Full fire-time re-hardening applies.
