# s-visual-009 — writer (g-7e15 VISUAL / c-visual-002 S1): apply the gas-lab S1 build RESULT + roll to S2

Date: 2026-06-29
Play: work / writer (apply an executor RESULT handed back by the owner)
Direction / node: indie-game-development / g-7e15 (VISUAL track, parallel to the g-9c41 bet)
Job: writer (validate-before-apply, deliverable reconciliation, first-hand verification) + roll the leg forward

## outcome

The c-visual-002 **S1** (unclipped gas-lab + characteristic-motion vertical-column jet) builder RESULT was applied home
after FIRST-HAND verification. S1 is DELIVERED + merged + pushed on GasCoopGame `origin/main` @ `f7efbea`. c-visual-002
moves `framed → delivered` (S1 done; the leg rolls to its next sub-leg **S2** — two differently-charactered gases +
the first differentiating «light-through-volume» lever; the planner owns the S2 CALL). The VISUAL track's `next` and the
NOW.md running-summary footer were updated so no place still says "c-visual-002 = framed / not started" (drift-guard).

I did NOT rubber-stamp. I reconciled every CALL `done_when` bullet against the RESULT, verified the merge + named
deliverables exist on `main`, and confirmed the ADR-0016 number collision is real.

## evidence (first-hand verification)

- Merge: `origin/main` = `main` = `f7efbea` (`--no-ff`; parents `2117341` engine main tip + `04a93ea` dev2 leg tip);
  `origin/dev2` = `04a93ea`. EXACT match to the RESULT.
- Deliverables EXIST on `main`: `Render/GasVisual/GasLabScene.unity`, `Render/Contracts/LabGasField.cs`,
  `Render/GasVisual/LabGasViewSource.cs`, `tests/.../Render/LabGasFieldEdgeTests.cs` (the independent test-author's LAB
  tests), `docs/measurements/c-visual-002-s1-owner-eye-checklist.md` (owner-eye sign), `openspec/changes/
  c-visual-002-s1-gas-lab/` (frozen change). The unclipped-lab `done_when` bullet is discharged by a real scene path, not
  a test name (deliverable-exists invariant).
- ADR collision: `docs/adr/ADR-0016-gas-visual-s1-gas-lab.md` AND `docs/adr/ADR-0016-s2a-zero-legacy-reconstruction-
  retirement.md` BOTH present on `main` → the visual ADR series collides by number with the engine ADR-0016. Recorded as
  the leg's forward flag.
- Headless «точно» (per RESULT, on the merged main): `tools/check.ps1 -Deliver` GREEN, 1003 tests (923 engine baseline +
  80 S1 Lab Render), 5 frozen strong-check folders OK, coverage 8/8; render-only invariants — `git diff Core/**` empty,
  no `AsyncGPUReadback`/`.GetData` under Render/Adapters, C#↔HLSL stride gate green, dev2 didn't touch Core from merge-base.

## validate-before-apply (deliverable reconciliation vs work/c-visual-002-call.md done_when)

| CALL `done_when` | disposition in the RESULT |
|---|---|
| PLAN owner-signed; §Re-sync first | ✅ Owner-signed Variant A; 3 owner-run Codex review rounds + fresh-context validator COULD-NOT-REFUTE |
| Unclipped lab scene, no rectangle from multiple angles | ✅ existence `GasLabScene.unity` + `NO-RECTANGLE` headless + owner «нет прямоугольника с любого угла» |
| Characteristic-motion loop (spawn+jet+creep) | ✅ `MOTION` headless + owner ran spawn→jet→creep |
| Two-type probe via reserved field | **DEFERRED → S2** — owner-ack "owner-signed split"; the CALL pre-authorized "lab+motion first → then the two-type probe" |
| Headless «точно» (-Deliver GREEN, Core/** empty, stride gate) | ✅ 1003 tests, Core/** diff empty, stride green, no readback |
| Owner-eye «ближе к жемчужине» (binding) | ✅ owner-eye #1 signed (Variant A); column accepted as the expected S1 placeholder shape; natural-jet deferred (owner-ack:esc-c-visual-002-s1-natural-jet-deferred-2026-06-29) |
| Comes HOME, no off-contour merge | ✅ owner-gated dev2→main merge; applied to OS state now |

No bounce: the soft-falloff data-side no-rectangle GUARANTEE matches the CALL's named approach; `LabGasViewSource` (an
analytical motion source) is the PLAN-decided "scripted fake motion source" option the CALL explicitly offered, not a
silent substitution; the 977→923 engine-baseline shift is from the ENGINE legs (S2a/S2b deletions), not this render-only
leg (Core untouched, verified).

## state changes applied

- NOW.md → open_calls `c-visual-002`: `framed → delivered`; status comment records S1 DELIVERED+MERGED+PUSHED 2026-06-29,
  SHAs, gates, owner-eye Variant A, the cuts/owner-acks, the ADR-renumber flag, the S5 TexelIndex follow-up.
- NOW.md → `g-7e15.next`: appended the S1-DELIVERED dated entry + reset the forward pointer to S2 (planner authors the CALL).
- NOW.md → `∥ VISUAL TRACK` footer: updated status + `next =` to S2; appended the `s-visual-009 commit:` summary line.
- LOG.md: appended one line. history/: + this file + the full builder RESULT (c-visual-002-s1-result-2026-06-29.md).
- TREE.md / active_bet (g-9c41): UNTOUCHED. g-7e15 is a parallel track (G1 intact: one active bet, the track adds no tasks).

## flags carried forward (the leg's next-owner)

1. **S2** = the next sub-leg of c-visual-002: heavy-sinks (dark&dense) vs light-rises (wispy&pale) via the reserved
   `RiseSinkBias` per-type buoyancy field (reserved-field path, no layout edit) + the first DIFFERENTIATING look lever
   «light-through-volume» (scatter-glow). Owner-signed FEEL + lever already fixed on the plan. Planner owns the S2 CALL.
2. **DEFERRED natural/turbulent jet** (owner-ack:esc-c-visual-002-s1-natural-jet-deferred-2026-06-29): the column grows as
   a hard "capsule/plasticine", does not flow — a true curl-noise-advected / billow-formed jet is an S2/S6 look-dev candidate.
3. **⚠ ADR renumber** (now CONCRETE on main): renumber the visual ADR series so ADR-0016-gas-visual-s1-gas-lab stops
   colliding with the engine ADR-0016 (c-exec-017). Not a builder action — a product-repo cleanup leg (peer to the
   duplicate-ADR-0012 cleanup already queued for the engine side).
4. **S5 follow-up** (pre-existing, not S1): `GasGridBounds.TexelIndex` int-overflow (guarded `MaxGridDim` 256³) — hardening
   against raw bounds edits frozen S5 code → a separate leg.
5. Possible lab look-dev polish pass (dither/noise) — now evaluable in motion.

## next

Route HOME — the planner owns the next CALL. next = frame the **S2** look slice (two-type buoyancy via reserved
`RiseSinkBias` + scatter-glow «light-through-volume»), opened in a fresh GasCoopGame_dev_2 session with a PLAN, owner
present; comes HOME with an owner-eye sign. The OS-repo commit is LOCAL; pushing main is owner-gated (ask the owner).

END_OF_FILE: live/indie-game-development/history/s-visual-009.md
