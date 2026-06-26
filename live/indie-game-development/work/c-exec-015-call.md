# CALL c-exec-015 — S1: ВЫБРОС-ПРИ-СПАУНЕ + ВЫДАВЛИВАНИЕ ТЕЛОМ (gas reacts to sources & moving bodies)

Direction: indie-game-development / g-9c41 / S1 (slice spine, after S0).
Executor: a FRESH GasCoopGame_dev session (Unity-MCP + branch `dev` → `main` when green). Opens with a PLAN (owner present).
Authored: 2026-06-26 (s-work-019). Builds ON c-exec-014 (S0 foundation, merged GasCoopGame `main` @824948d).
Source of truth for state = `live/indie-game-development/NOW.md`. Canon = `knowledge/g9c41-gas-engine-SPEC.md`.
Roadmap = `work/gas-engine-build-roadmap-2026-06-26.md`. Mechanic gate = `knowledge/mechanic-lenses.md`.

## goal (outcome, not method)

The FIRST DYNAMIC gas slice on the S0 foundation. Gas no longer only sits and fills — it:
- (a) **ERUPTS** when a source introduces it: gas enters under integer **pressure / over-fill** and is pushed
  outward by the EXISTING S0 face-flow law over subsequent ticks (a burst that visibly spreads, then settles to the
  S0 equilibrium), NOT a one-tick teleport-fill.
- (b) is **DISPLACED** when a body (player / object) moves into its cells: the occupied cells become temporarily
  zero-capacity, the displaced integer mass redistributes to valid open neighbours (mass conserved), and the cells
  reopen when the body leaves.

The owner SEES both on a playable scene. Netcode-NEUTRAL (no wire / no broadcast — that is S2). Everything stays
INSIDE the LOCKED integer face-flow model — NO velocity field, NO advection, NO per-cell momentum.

## context (read first — applied, not just cited)

1. **§Re-sync the GasCoopGame repo contract to its CURRENT version FIRST** (S0 closed at v8 — re-read it, do not assume).
2. **S0 deliverables you extend (do NOT reopen):** the layered coordinating grid (GAS 50 cm authoritative /
   STRUCTURE 25 cm), the per-Z-band integer conductivity COUNT projection (structure→gas, no divide), and
   `VoxelFaceFlow.Step` — the face-flow law (monotonic-in-count / slit-seeps / wall-zero / mass-conservation /
   emergent height). Eruption and displacement RIDE this law; they do not replace it.
3. **Mechanic-lens gate** (`knowledge/mechanic-lenses.md`): the PLAN classifies S1's two mechanics ведро-1/2/3 and
   runs the cheap paper lenses. Lens 6 / «весело» is the owner's SEPARATE eyeball, NOT a build gate (see done_when).
4. **Roadmap rhythm:** small owner-PLAYABLE steps, each preceded by RED-first autotests written by an INDEPENDENT
   test-author (the builder cannot edit the red tests).

## the two mechanics — the PLAN classifies depth; this CALL fixes the boundaries

1. **ВЫБРОС-ПРИ-СПАУНЕ (eruption-on-spawn).** A source cell is filled ABOVE the local equilibrium (an integer
   pressure / over-fill amount); the EXISTING `VoxelFaceFlow` law evacuates the excess through open faces over the
   following ticks → a visible burst that spreads then settles. Modelled as an integer over-fill source CONSUMED by
   the face-flow law — NOT a new velocity / advection axis.
2. **ВЫДАВЛИВАНИЕ ТЕЛОМ (displacement by player/object).** A body occupies a set of cells → those cells become
   zero-capacity (occupied) → the displaced integer mass is redistributed to valid open neighbours by the same law
   (conserved); a fully-blocking body holds zero gas in its cells; body-leave reopens the cells. NOT momentum
   transfer to the gas, NOT a force field.

## boundaries (out of scope / do not touch)

- NO networking / lockstep wire / broadcast (S2). NO reactions / chemistry / cascade (S6). NO breach BEHAVIOUR beyond
  S0's one-flip data-proof (S5). NO placement MECHANIC (resolution only reserved). NO big-hall / far-LOD optimization
  (deferred — d-sparse-solver-defer-001; the sparse active-front solver is a SEPARATE future leg).
- **DO NOT introduce a velocity field, advection, or per-cell momentum.** Eruption + displacement MUST be expressible
  on the EXISTING integer face-flow conductivity law. If either genuinely cannot be → **STOP-and-escalate** (it would
  reopen the LOCK / SPEC Факт 2) — never a silent substitute (STOP-discipline v8: a blocked/infeasible named approach
  or a crutch, incl. reduced fidelity, is a mandatory STOP + escalate).
- The eruption + displacement LAWS live in **headless `Core/**`** (unit-testable); `Adapters/**` only renders + drives
  input — the same anti-self-cert boundary as S0.
- Gas-50 law, R5 (special gases are field-transported, not agents/velocity-intent), R13/R14 — unchanged.

## carried hardening (DO in the SAME leg, RED-first — routed home from the S0 RESULT)

- **H1 — class-wide `int*int` overflow GUARD** (decision d-overflow-guard-001). The "no silent `int*int` wrap on the
  authoritative path" invariant has recurred at 3 sites (SubFacesPerFace, kpEff, coord·spa — all fixed per-site). Per
  "same class twice = stop", replace per-site patching with a **build-scan tripwire** that auto-discovers unguarded
  `int*int` multiplies on the authoritative `Core` path (analogous to the zero-float scan), wired into
  `tools/check.ps1 -Deliver`, with a **planted unguarded-multiply RED control that MUST fail the scan**. The
  independent test-author writes the RED control.
- **H2 — spec-silence amendment** (PLANNER-AUTHORIZED — so it is NOT a builder self-edit). Add the
  EXTREME-COORDINATE overflow case (`coord·spa`) to the frozen spec's silence-audit coverage (today it covers
  extreme-RESOLUTION but not extreme-COORDINATE). The planner (s-work-019) authorizes this specific amendment; record
  it as authorized in the change.

## done_when (verifiable)

1. **PLAN (owner present)** — §Re-sync v8→current FIRST; ingest S0 + the roadmap + mechanic-lenses; classify eruption
   & displacement ведро-1/2/3; fix the S1 scene plan and the owner-playable steps.
2. **ERUPTION RED suite** (independent author): mass-conservation under a burst source; the burst SPREADS over ticks
   then SETTLES to the S0 equilibrium (not a 1-tick fill); monotone-in-pressure; deterministic (integer, zero-float).
3. **DISPLACEMENT RED suite**: a body entering N cells redistributes EXACTLY the displaced mass to valid open
   neighbours (zero created / zero destroyed); occupied cells hold zero gas; body-leave reopens; deterministic.
4. **H1 guard** green (planted RED control fails the scan as designed) + **H2 amendment** in the frozen spec.
5. **`tools/check.ps1 -Deliver` GREEN** — build + headless tests + zero-float scan + the NEW `int*int` scan +
   mutation ≥ 70 % on the new `Core` code + spec-silence (incl. the coord row) + deliverable-coverage.
6. **DETERMINISM by construction** — integer-only authoritative path; the zero-float scan spans the new code;
   (optional) a loopback 2-process hash as an ordering/RNG tripwire (one machine; real 2-machine is never a gate).
7. **PLAYABLE SCENE** (owner SEES — eyeball-correctness, NOT a gate): owner spawns a source and watches gas ERUPT +
   spread; moves a body through gas and watches it get SHOVED ASIDE and flow around. «точно» = the green suite is the
   sole discharge; «весело» is the owner's separate eyeball (per `esc-veselo-excluded-2026-06-26`, not pass/fail).
8. **ZERO-LEGACY** — no dead code; transitional debt tracked with explicit delete triggers (not silent legacy).

## discipline / gates (carried from S0)

RED-first by an INDEPENDENT test-author (builder cannot edit the red tests) · `Core/**` placement · `-Deliver` GREEN ·
mutation ≥ floor (70 %) · a **FRESH-SESSION G5 refutation** (a different model family for rigor) that tries to REFUTE
(determinism / conservation / no-silent-substitution / guard soundness / ledger honesty) — COULD-NOT-REFUTE is the
bar · STOP-discipline v8 · build in small owner-PLAYABLE steps.

## return

A RESULT routed HOME (the workflow OS owns the next CALL — the builder does not author it): `outcome` + `evidence`
(commits, `-Deliver` transcript, mutation json, G5 verdict, any benchmark delta) + any findings/decisions for the
planner. `dev → main` merge + push is OWNER-GATED.

## budget

One slice. If eruption and displacement turn out to be two legs, **STOP and return "split needed"** — do not silently
build both as one blob (work-play split discipline).

END_OF_FILE: live/indie-game-development/work/c-exec-015-call.md
