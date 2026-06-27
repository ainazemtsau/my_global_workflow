# CALL c-exec-015 — S1: ИМПУЛЬС-СОБЫТИЯ + НАПРАВЛЕННЫЙ ПОТОК (forced-flow) — выброс + выдавливание + ветер как первые случаи

Direction: indie-game-development / g-9c41 / S1. **Reframed 2026-06-26 (s-work-020)** from "выброс + выдавливание"
to the GENERAL forced-flow primitive the deep-research recommended (work/gas-richness-deep-research-2026-06-26.md,
candidate "Forced-Flow Hybrid", adversarially verified). Supersedes the prior c-exec-015 framing.
Executor: a FRESH GasCoopGame_dev session (Unity-MCP + branch `dev` → `main` when green, owner-gated). Opens with a PLAN.
Builds ON c-exec-014 (S0, merged GasCoopGame `main` @824948d). State source = NOW.md. Canon = knowledge/g9c41-gas-engine-SPEC.md.

## goal (outcome, not method)

The first DYNAMIC, DIRECTABLE gas on the S0 foundation, via ONE general primitive: **deterministic integer
IMPULSE-EVENTS that write a decaying directional-bias register, applied on top of the existing gradient face-flow.**
Outcomes the owner SEES on a playable scene:
- **Выброс-при-спауне (eruption):** a source ejects gas with a directional kick that pushes outward, then settles —
  the first impulse-event type.
- **Выдавливание телом (displacement):** a moving body zeroes its cells' capacity AND emits a displacement impulse,
  so gas is shoved aside and flows around — the second impulse-event type.
- **Ветер (wind):** a sustained directional impulse (e.g. a vent) carries gas down a corridor and SPLITS it into both
  branches at a fork — directionality the pure-diffusion S0 structurally could not do.

Stays INSIDE the LOCKED integer model: the bias register is integer, in-checksum, decaying — NOT a stored velocity
field. NO float velocity / advection / fixed-point velocity (that is a RESERVED upgrade tier requiring an owner-signed
ADR-0010 lock-crack — if a mechanic seems to need it, STOP-and-escalate, never build it). Netcode-NEUTRAL on the wire
(lockstep proof = S2); determinism proven by-construction (integer + zero-float scan + loopback hash).

## context (read first — applied, not just cited)

1. **§Re-sync the GasCoopGame repo contract to its CURRENT version FIRST** (S0 closed at v8 — re-read, don't assume).
2. **Deep-research basis (mandatory read):** work/gas-richness-deep-research-2026-06-26.md — the 3-tier model (cheap
   forced-flow NOW / lattice-gas rooms DEFERRED / fixed-point velocity RESERVED owner-gated) + the 4 load-bearing
   corrections below. This CALL = the cheap tier only.
3. **S0 deliverables you extend (do NOT reopen):** VoxelFaceFlow.Step (the gradient face-flow law, monotone-settling
   Kp=2*degree), VoxelField (_mass/_flux/_carry, MeaningChecksum), the per-Z-band integer conductivity projection,
   FaceState (open bit, Conductivity COUNT, DirectionMask — folded in the checksum but INERT/zero today).
4. **The §9.5 trip-wire (correction 1):** the sub-face occupancy BITMAP lives in StructureGrid (separate layer, own
   checksum, bitmap-OUT of the gas checksum), NOT in VoxelField. So the bias must be FACE-LEVEL-UNIFORM (a function of
   the already-checksummed Conductivity COUNT + a face-level DirectionMask scalar). Activating FaceState.DirectionMask
   directionally IS the trip-wire — it is inert today. Sub-face-resolved directionality (a valve on the lower half of a
   doorway) is DEFERRED to a later slice via the §9.7 committed-revision read-model. Do not import the structure bitmap.

## STEP 0 — DE-RISK SPIKE FIRST (a hard GATE; build NOTHING on a broken base)

Before the feature, prove the primitive is safe + alive on a small grid. This is the analog of the already-solved
Kp=4→12 fix. Independent test-author writes the RED tests.
- **RED non-monotone settle oracle (correction 3):** "wind-into-a-corner-and-back MUST conserve mass AND settle, MUST
  NOT oscillate." The contraction proof (Kp≥2*degree) is SUSPENDED during a forced window (an exogenous bias is not a
  function of the gradient → a cell can transiently exceed its neighbourhood max); the oracle is the guard that the
  operator RETURNS to the contractive base after decay. The oracle MUST FAIL on a bad bias (planted non-conservative /
  non-settling bias = a RED control). Work through the clamp×decay interaction (a clamp-denied bias transfer dropped
  while the register still decays) — prove mass-conservation, do not assert it.
- **Symmetric integer decay rule (correction 2):** a signed arithmetic shift relaxes +bias and −bias asymmetrically
  (bit-identical, so no desync, but it silently breaks directional symmetry). Pin a SYMMETRIC integer decay and prove it.
- **2-process loopback bit-identity hash:** bias register folded into MeaningChecksum; include CONCURRENT impulse
  writes to the SAME face in one tick (two players' grenades) → pin a CANONICAL, order-INDEPENDENT write rule (an
  order-dependent sum is a classic lockstep desync — the one open determinism seam).
- **Bounded-return-to-quiet cost assertion (correction 4):** a kicked region MUST return to the implicit-zero/"quiet"
  active set within a bounded tick budget (the bias decay-tail keeps faces active and eats the DEFERRED sparse solver's
  saving — measure, don't assume free).
- **OWNER-EYE gate on the spike:** forked corridor + a vent — "ветер несёт газ, резко разделяет, держит сплит пока
  форсим, с ощутимым толчком, что гаснет." If this does NOT read alive, STOP and report (the cheap tier may be
  insufficient → the owner decides on the reserved tiers; do not silently substitute).

## STEP 1+ — THE FEATURE (only if Step 0 is green)

- **The primitive:** one decaying signed-INTEGER directional-bias register per OPEN FACE, beside _flux/_carry in
  VoxelField, applied as ONE extra clamped integer transfer on top of the gradient move, decaying to zero each tick.
- **Impulse-event source:** an event `{face footprint, direction, strength, ttl}` from a player INPUT (spawn-burst =
  eruption; body-shove = displacement; vent toggle = wind) WRITES the register. Rides the existing lockstep input
  channel — ZERO new wire traffic.
- **Выброс (eruption):** an over-fill source + a directional kick → bursts and spreads, then settles.
- **Выдавливание (displacement):** body cells → zero-capacity (conserved mass redistributes) AND a displacement
  impulse → gas shoved aside, flows around; body-leave reopens. The transient part-and-rejoin emerges; persistent
  no-rejoin only where a one-way valve (below) or geometry holds it.
- **Ветер + односторонний КЛАПАН:** a sustained directional bias = wind; a face-level DirectionMask one-way valve
  clamps reverse flux to 0 → DESIGNED permanent split where the level authors it (no velocity field needed).

## boundaries (out of scope / STOP-escalate if tempted)

- **NO fixed-point velocity field / advection** (the RESERVED upgrade tier — it cracks the lock; STOP-and-escalate to
  the owner, never build it here). **NO lattice-gas rooms** (the deferred vortex tier). True coasting inertia, true
  open-volume permanent-split, and free emergent vortices are NOT this leg — set that owner-expectation in the PLAN.
- **Vortices/swirl → the read-only cosmetic g-7e15 visual layer ONLY**, FED the authoritative bias field so the look
  aligns with real wind (zero gate risk). Not authoritative this leg.
- **Bias is FACE-LEVEL-UNIFORM only** (correction 1); no sub-face directional read, no structure-bitmap import.
- NO networking/wire (S2). NO reactions/chemistry (S6). NO big-hall/far-LOD optimization (d-sparse-solver-defer-001).
- Laws live in headless Core/**; Adapters/** only renders + drives input. Gas-50 law, R5, R13/R14 unchanged.

## carried hardening (same leg, RED-first — from the S0 RESULT, decision d-overflow-guard-001)

- **H1:** class-wide int*int overflow build-scan guard (auto-discovers unguarded multiplies on the authoritative path;
  wired into check.ps1 -Deliver; planted RED control MUST fail). Especially relevant — the bias adds new integer math.
- **H2:** planner-AUTHORIZED extreme-coordinate spec-silence amendment.

## done_when (verifiable)

1. PLAN (owner present): §Re-sync v8→current FIRST; ingest S0 + the deep-research doc + mechanic-lenses; classify the
   impulse mechanics ведро-1/2/3; scope the owner-playable steps (Step 0 spike → eruption → displacement → wind/valve);
   set the explicit owner-expectation (cheap tier = wind + decaying gust + transient split + designed-valve split;
   true inertia/free-vortices are reserved tiers).
2. **STEP 0 spike GREEN:** the RED non-monotone settle oracle (+ planted bad-bias RED control fails) + symmetric decay
   + clamp×decay conservation + bounded-return-to-quiet + loopback bit-identity hash (incl. concurrent same-face writes
   with a canonical order rule) + owner-eye "alive on a forked corridor + vent". If not green → STOP-and-report.
3. ERUPTION + DISPLACEMENT RED suites (independent author): mass-conservation; deterministic (integer, zero-float);
   eruption spreads-then-settles; displacement routes around the body + body-leave returns to S0 equilibrium.
4. WIND + one-way VALVE: directional bias carries gas down a corridor + splits at a fork; the valve gives permanent
   no-rejoin where authored. Deterministic.
5. H1 guard green + H2 amendment; check.ps1 -Deliver GREEN (build + headless + zero-float scan + the new int*int scan +
   mutation ≥70 on new Core + spec-silence incl. coord row + deliverable-coverage).
6. DETERMINISM by construction: integer-only authoritative path; bias in MeaningChecksum; zero-float scan spans new
   code; loopback hash green.
7. PLAYABLE SCENE (owner SEES — eyeball-correctness, NOT a gate): источник выстреливает + растекается; тело раздвигает
   газ + обтекание; вентиляция гонит газ и делит на развилке. «точно» = green suite; «весело» = owner's separate
   eyeball (esc-veselo-excluded, not pass/fail).
8. ZERO-LEGACY; transitional debt tracked with delete triggers.

## discipline / gates (carried from S0)

RED-first by an INDEPENDENT test-author (builder cannot edit the red tests) · Core/** placement · -Deliver GREEN ·
mutation ≥ floor (70%) · a FRESH-SESSION G5 refutation (different model family) that tries to REFUTE (determinism incl.
the bias/concurrent-write/decay seams · conservation under forcing · contraction-returns-after-decay · no-silent-
substitution · guard soundness · ledger honesty) — COULD-NOT-REFUTE is the bar · STOP-discipline v8 (a blocked/
infeasible named approach, a crutch, OR a temptation to add a velocity field = mandatory STOP + escalate) · build in
small owner-PLAYABLE steps.

## return

A RESULT routed HOME (the OS owns the next CALL): outcome + evidence (commits, -Deliver transcript, mutation json, G5
verdict, the Step-0 spike result, any benchmark/active-set delta under FORCING — re-measure the active-set with the
bias LIVE, not after a settle) + findings/decisions for the planner. dev→main merge + push is OWNER-GATED.

## budget

One slice — but it is bigger than the original "выброс + выдавливание". If the PLAN finds it splits (e.g. Step-0
spike + eruption land first, displacement/wind/valve spill to S1.5), STOP and return "split needed" — do not silently
build a blob. The Step-0 spike is the highest-value de-risk; if everything else slips, the spike + eruption is a
legitimate first return.

END_OF_FILE: live/indie-game-development/work/c-exec-015-call.md
