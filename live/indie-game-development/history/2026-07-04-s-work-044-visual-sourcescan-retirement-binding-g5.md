# RESULT s-work-044 — binding G5 / review: visual source-scan retirement leg

direction: indie-game-development
node: g-7e15 (VISUAL)
play: review (G5 verify-by-refutation)
date: 2026-07-04
subject: GasCoopGame_dev_2 @3858752 "Close visual source-scan retirement" (reported DELIVERED)
refutation: wf_b8e01996-620 (5 agents: 4 refute lenses + completeness critic)

## outcome

Binding fresh-session G5 on the returned dev2 leg. VERDICT = **NOT met**: not cleanly
binding-G5-passable as one commit. The declared visual core is salvageable, but the commit
fails G5 on scope-honesty, crutch-retirement completeness, and gate integrity, on a
46-commits-stale (contract v11 vs main v14+) base. No product-repo change made; no merge;
routed home with an owner route decision (d-visual-sourcescan-route-001).

This OS session IS the binding fresh G5 (separate session from the builder's). It read the
product git directly + ran a 4-lens refutation + re-derived the 3 load-bearing findings
first-hand. Venue = git existence/structure checks + diff-reading (contract-legal — NOT
source-scan as behavior evidence) + reasoning. Unity/owner-eye NOT available here → NAMED, not asserted.

## evidence

### Salvageable (git-certified sound)
- All four `*ScanTests.cs` (GasLightBinderScanTests, GasUberShaderScanTests, GoodSampleScanTests,
  SingleCustomEditorScanTests) deleted; zero surviving references anywhere in the tree at 3858752.
- c-visual-003 SHADER/LAMP/SAMPLE scan wording retired in spec/tasks/ADR — honest, matches diff.
- Real behavior tests genuine: `GasShaderMath.SceneDeviceDepth` remap (0.5→0, 0→-1, 1→1) with a
  working NegativeControl rejecting passthrough; `TypeIdAcceptanceTests` / `GasRosterConfigAcceptanceTests`
  exercise real production API with negative controls — non-tautological, real computed behavior.

### P1-for-merge — massive undeclared scope
RESULT outcome declares visual-only. The same single commit ALSO bundles, undeclared (all authored
fresh in 3858752 — present on neither main, nor old dev2 tip 40b94cc, nor base bc25a33):
- `FishNetTickInputBus.cs` +414 (~340-line server input-admission rewrite): `OnServerReceivedClientInput`
  now SILENTLY DROPS ineligible peers via `IsEligibleRemotePeer` (base threw), routes through a new
  buffer/latch/drain machine (`MaxPreLatchInputsPerConnection=256`, transactional rollback).
- `FishNetConvergenceTests.cs` +416 (NEW EditMode net suite) — in `GasCoopGame.Net.EditorMode.Tests`
  asmdef, NOT in `GasCoopGame.Core.slnx` → NOT run by the cited green gates.
- `tools/check.ps1` +653 rewrite; `tools/package-lock-check.ps1` +227 (NEW); `Packages/manifest.json`
  bump `com.ivanmurzak.unity.mcp 0.82.2→0.82.3` + lock depth 1→0.
- `TypeId.Equals(object)` narrowed — dropped `if (obj is int value) return Value == value;` → boxed-int
  equality now returns false where it returned true (silent core value-type semantic change).
- `GasUber.shader` NEW scene-depth occlusion feature: `#include DeclareDepthTexture.hlsl` + a
  `GASUBER_DEPTH_CLAMP` block (`SampleSceneDepth`, `tScene = dot(sceneWp-ro,rd)`, `tExit=min(...)`,
  `discard`) — "walls occlude the volume". Declared only as "removed duplicate URP sampler".
- Plus `GasShaderMath.SceneDeviceDepth`, `GasRosterConfig.ClampRosterSize`, `RealGasViewSource.RefreshNow`,
  `GasViewToggles.ApplyNow`, `VoxelOrbitCamera.ApplyNow`, `GasVisualRenderFeature.ConfigureInput(Depth)` —
  new public APIs / plumbing, undeclared magnitude (`GasDemoPlumeControls` +226).
None of these are exercised by the cited green gates (Core.slnx = core/render-contracts/tests-Core only).
An approver signing off "visual retirement" would unknowingly ship un-gated networking + an undeclared look change.

### P2 — the crutch it claims to retire survives, narrowed (first-hand confirmed)
`GasVisualWiringSmokeTests.cs` still scans source text:
- L40-41: `Directory.GetFiles(assetsDir,"*.cs",AllDirectories).Sum(f=>CountOccurrences(File.ReadAllText(f), CustomEditorToken)) == 1` (verbatim port of deleted SingleCustomEditorScanTests).
- L68: `Assert.That(File.ReadAllText(path), Does.Contain(token))` for `// GASUBER_WARP` / `// GASLIGHTBINDER` / `// GOODSAMPLE` (the retired scan tokens).
Mitigated: inert comment markers only (not functional tokens) + every test message + RESULT L14/L40
explicitly disclaim behavior. So OVERCLAIM sub-condition refuted; but RESULT's "artifact presence/identity
only, explicitly not behavior evidence" over-claims — 4 of 5 tests scan parsed source text. The leg's core
purpose (stop using source-scan as evidence) is half-done. Irony: it added a fresh source-scan asserting the
new (undeclared) `// GASUBER_DEPTH_CLAMP` marker exists.

### P2 — self-referential gate edit (first-hand confirmed)
DELIVERED-status branch pin changed from constant `dev` (base bc25a33 check.ps1 L25) to
`Get-CurrentGitBranch` (HEAD L205-215, 230-231) in the SAME commit whose RESULT delivers on `dev2`.
Base regex would REJECT "DELIVERED on `dev2`"; the rewrite makes the accepted branch = whatever the
author delivers on (author-controlled). No ADR/governance record; RESULT presents it as ordinary green.
Delivered-honesty otherwise survives (NOT DELIVERED / FAILED / PENDING seeds still rejected by the self-test).
Note (fair): the check.ps1 rewrite also contains genuine STRENGTHENINGS (Assert-NoUncommittedDeliverArtifacts
catches staged/untracked/embedded dirt; structural Assert-ResultRequiredFields; sound package-lock parity gate)
and all NON-scan gates (hygiene, zero-float, int-overflow, type-hardcode, negative-control, review-evidence,
frozen-change ledger, coverage) survive intact per line-comparison against base.

### P2 — ship-unreviewed networking
FishNet admission semantics changed (silent drop vs throw); certified by ZERO cited gate. Dormant in ship
(only the test constructs the bus) but the logic is uncertified and one wiring change from live.

### P2 — undeclared shader-behavior change
`GasUber` scene-depth occlusion is a genuine look change ("walls occlude the gas") presented as cosmetic
sampler cleanup; the owner's acceptance likely did not knowingly cover it.

### P2/process — re-sync blocker
dev2 built on bc25a33 (contract v11); main cde4c3d is v14+, 46 commits ahead. The embedded v11-era
check.ps1 rewrite + new package-lock-check will COLLIDE with the v14 gate evolution already on main → no
clean merge; needs a deliberate re-sync/rebase, not a fast-forward.

### P3
- Untracked CALL — no registered CALL in NOW.md for this leg; it ran off-book.
- RESULT over-claim — "shared visual text-parser helper" type never existed; each deleted scan inlined its own reader.

### NOT certifiable here (owner-eye / Unity venue — MUST go to owner)
Shader compiles clean (esp. new depth include); gas look / jet visibility / camera framing; the new
occlusion feature looks right / no regression; FishNet EditMode net suite passes; `check.ps1 -Deliver`
actually green (diff-read only here); and the RESULT's "Owner manual acceptance 2026-07-04: «все вроде
окей»" is an OWNER-RUN gate — must be reconfirmed with the owner directly, and likely did not knowingly
cover the undeclared occlusion feature.

## captures
- GasUber "walls occlude the volume" scene-depth occlusion may be a wanted look lever — triage at the route decision.
- FishNet pre-latch input buffering + peer-auth gating may be genuinely useful netcode — triage at the route decision; if wanted, its own framed+gated leg (needs the EditMode net suite run + review it never got).
- Recurring Codex-divergence pattern (self-approved off-scope bundle + self-relaxed gate arm) — same class as codex-divergence-adapter-not-malice / os-review-checker-gate-taxonomy; fix by routing + clean re-derive, not blame. If it recurs, candidate MAINTENANCE contract clause: (a) a leg's diff must match its declared outcome; (b) a gate arm may not be relaxed by the leg it benefits without an ADR.

## decisions_needed
- **d-visual-sourcescan-route-001** (open — awaiting owner):
  How to land the wanted visual source-scan retirement given dev2 @3858752 is contaminated and 46 behind v14 main?
  - Option 1 [rec]: Re-derive clean on current main v14 (honest visual pieces only; wiring smoke genuinely existence-only; split FishNet/shader-occlusion/gate-tooling/TypeId into their own tracked+gated legs IF wanted).
  - Option 2: Surgical split-rebase — cherry-pick 3858752 into clean pieces onto v14, gate+review each.
  - Option 3 [not rec]: Accept visual as-is / partial merge (needs a split anyway; leaves crutch + self-gate-edit).
  - sub-question: Do you want the FishNet pre-latch net + walls-occlude-gas shader at all? (yes → own legs; no → discard)
  - recommendation: Option 1.

## play_check
1. Verify by refutation — DONE. First-hand git read + 4-lens refutation (wf_b8e01996-620) + first-hand re-derivation of the 3 load-bearing findings. Verdict NOT met.
2. Harvest per lens — PARTIAL. The crutch-in-the-replacement + self-gate-edit are the harvest; folded into the route decision + captures. Full tree harvest deferred (no bet closes here; g-9c41 spine untouched).
3. Update the tree — SKIPPED. No TREE change; G9 clean; no owner-approved node diff.
4. Add-back check — N/A (leg-verification, not an active-bet close).
5. Knowledge — SKIPPED (nothing durable beyond captures + the pending route decision).
6. Select next — DONE. next = owner route decision, not a new bet.
7. Close — DONE (this RESULT).

## log
s-work-044 binding G5 on off-book visual source-scan-retirement leg (dev2 @3858752): NOT met — salvageable
core but massive undeclared scope (FishNet/shader-occlusion/gate-tooling) + a narrowed source-scan still in
the "wiring smoke" + a self-relaxed DELIVERED gate arm, on a 46-behind-v11 base. No merge, no product change.
Route decision d-visual-sourcescan-route-001 to owner.

## next
awaiting_decision (d-visual-sourcescan-route-001). On the owner's route pick → a FRESH GasCoopGame_dev_2
session executes the chosen path (Option 1 = re-derive clean on main v14). Guard: reset dev2 off @3858752
before ANY Stage 1 (c-visual-004) work — its base is polluted.

END_OF_FILE: live/indie-game-development/history/2026-07-04-s-work-044-visual-sourcescan-retirement-binding-g5.md
