# CALL c-exec-020 — Sc-weight: PER-TYPE VERTICAL BUOYANCY (heavy sinks / light rises, ENGINE-ONLY)

Direction: indie-game-development / g-9c41 / Sc-weight — the SECOND slice of the CHARACTER ROAD (d-character-road-001,
owner «можем оформлять» 2026-06-29). Builds on the post-Sc-types base (GasCoopGame `main` at-or-after @7d08882 — the
c-exec-019 Sc-types merge; §Re-sync confirms HEAD first — small repo-hygiene-only commits atop it are expected).
Executor: a FRESH GasCoopGame_dev session (branch `dev` → `main` when green, owner-gated). Opens with a PLAN (owner
present). State source = NOW.md (active_tasks Sc-weight). Canon = knowledge/g9c41-gas-engine-SPEC.md (§3 «Вертикаль
вблизи = buoyancy-BIAS, НЕ сортировка»; §7-buried height-bands/2-band; §8 far-tier code-map; Факт-4; §1 ADR poprawка:
lock = ADR-0002). Shape basis = work/character-road-shape-2026-06-29.md. Subsumes d-buoyancy-near-weight-priority-001.
HARDENED 2026-06-29 (wf_8f324a28-81e: 24 raised → 20 survived adversarial refute-verify → 3 must-fix + 9 should-fix/nit
folded; 4 refuted, incl. a goal-hygiene and a temperature-reserve challenge — the goal's «bias-not-sort/creeping» is the
canon-§3 OUTCOME anchor, not a method paraphrase, and reserving the temperature term does not gut the visible deliverable).

## Why this slice (and the lock id)

Sc-types laid the multi-gas substrate + the per-type param structure, and RESERVED `GasParentParams.RatioToAir` (its own
member-comment names it «weight class / ratio-to-air»; GasParentParams.cs:30-31) as an INERT data slot tagged «Sc-weight»,
driving NO near behaviour yet. (A sibling inert slot `DensityPacking` (GasParentParams.cs:27-28) is ALSO reserved «Sc-weight»;
it stays inert/untouched this slice — reserved for a later slice, already folded at default 0.) This slice WIRES the
weight-class slot into the FIRST vertical-FEEL mechanic: heavy gas SINKS, light gas RISES, tunable per meta-type. The owner
flagged this gap first-hand (no buoyancy/weight anywhere in Core/Field/Voxel — d-buoyancy-near-weight-priority-001). Lock =
**ADR-0002** (input-lockstep; §1 drift-guard: any stray «ADR-0010-as-lock» is a citation error — ADR-0010 = the unrelated
test-sandbox). Determinism preserved, not reopened.

## goal (outcome, not method)

Near-tier gas acquires per-type VERTICAL BUOYANCY: a heavy-class type's mass SINKS (its vertical centre-of-mass drifts DOWN
over ticks), a light-class type's mass RISES, with strength tunable per meta-type — realized as an integer BIAS on flow
through Z-faces that produces a CREEPING front (canon §3 «buoyancy-BIAS, НЕ сортировка»). The owner SEES, in the engine
debug view, a heavy test gas pool/settle low and a light test gas collect high — CREEPING, never snapping. **ENGINE-ONLY —
no visual-track hookup** (the look connects later; the g-7e15 visual track runs independently on dev2).

**approach token = `per-type-buoyancy-bias-creeping-front`** — the ONE substrate this leg exists to prove (an integer
per-type Z-face bias / creeping front). A delivered artifact whose recorded `approach:` differs (esp. a per-column
sort / capacity-fill) is a self-authored substitution needing owner-ack — otherwise STOP-escalate.

## the PORT crux — port the LAW, NEVER the far-tier SORT (read this twice)

The proven integer weight law to PORT lives in the FROZEN far-tier `CoarseSpecies.EffectiveDensity`
(Core/Field/Coarse/CoarseSpecies.cs:46): `eff(s,T) = max(1, MolecularWeight(s) − (T >> BuoyancyTempShift))` — higher eff
sinks; hotter ⇒ lighter ⇒ rises (`Weights = {64,32,16,8}`, `BuoyancyTempShift = 2`, ADR-0005). **This is the LAW: a type's
weight class sets a buoyancy direction + strength; heat lowers effective weight.** PORT this LAW SHAPE, re-expressed as a
per-type DATA param (the reserved `RatioToAir`), NOT as a new hardcoded `Weights[]` C# array.

⚠ **The far-tier law is RELATIVE / UNSIGNED — Sc-weight needs a SIGNED bias about an absolute neutral.** `eff` is always
≥ 1 (everything «sinks»); it only RANKS co-resident species against each other (densest-first), with NO air/neutral datum.
But this slice's outcome is a SIGNED Z-bias (heavy ⇒ downward, light ⇒ UPWARD, weight-neutral ⇒ no drift). So the PLAN MUST
define the ABSOLUTE NEUTRAL weight value about which the sign is taken (above-neutral rises, below sinks, ==neutral 0-drift)
and where it lives in the weight param — a literal relative densest-first port that cannot express «rises» or «neutral does
not drift» is WRONG. (The exact neutral VALUE is the PLAN's call — record it; do not let the CALL prescribe the integer.)

**DO NOT port the far-tier REALIZATION.** `CoarseBandStep.Settle` (CoarseBandStep.cs:186-251) realizes buoyancy as a
densest-first CAPACITY-FILL across 2 bands (the lower band fills heaviest-first to a temperature-throttled capacity, the
rest overflows up; it computes a sorted `targetLower` then rate-limits `move = Reduce(targetLower − lower, τ)` — a creeping
SORT). That is a per-column ALLOCATION/SORT across height bands — EXACTLY what canon §3 forbids near («текущий CoarseBandStep
сортирует — НЕ копировать его в near») and what §7 BURIES (height-bands / 2-band-as-authority / `CoarseBandStep`-as-authority
— retires at S4). Copying that capacity-fill/sort into the near grid = a per-column instant sort = vertical teleport = the
no-pop violation = **STOP-escalate**. The near realization is a CREEPING integer Z-face bias (below), not a column
allocation. (The far-tier source is FROZEN: PORT the numbers/law by re-expressing as DATA; do NOT touch, refactor,
re-data-drive, move, or scan `CoarseSpecies`/`CoarseBandStep` — they retire at S4. «Port before S4 deletes it» means lift
the proven LAW into the near DATA path now, while the reference still exists.)

**Temperature coupling is OPTIONAL this slice.** The far-tier law's `−(T >> shift)` term couples buoyancy to temperature;
temperature-as-a-mechanic is Sc-damage (a thin sink-layer, d-tempfeedback-001), NOT this slice. Weight-class buoyancy ships
fine WITHOUT a live temperature term (constant per-type weight class, uniform-T scene). The PLAN DECIDES: ship buoyancy on
the weight-class param alone with the temperature term RESERVED/zero-stubbed (recommended), keeping the far-tier law's SHAPE
so Sc-damage can later wire the T-term without a schema change. Building a live temperature mechanic here = Sc-damage
creeping in = STOP.

## the mechanism (frame the OUTCOME; the PLAN owns the realization)

Precedent: S1 forced-flow (c-exec-015) added a per-FACE decaying directional bias `_bias[faceIdx]` that `VoxelFaceFlow.Step`
scales by `faceConductivity / kpEff`, floors to ±1 (RW10), and COMBINES into `desiredMove[i]` BEFORE the per-cell
back-pressure clamp — so it inherits conservation + non-negativity + back-pressure + atomicity for free
(VoxelFaceFlow.cs:65-135). Buoyancy is structurally analogous but with these differences the PLAN must honour:
1. **per-TYPE** (keys off the resolved weight-class param), where the S1 `_bias` is per-FACE-not-per-species — so buoyancy
   CANNOT reuse `_bias`; it is computed inside the per-species loop. **Repurposing the S1 `_bias` register for per-type
   buoyancy = STOP** (it is per-face; it folds as `MeaningMembers.Bias`; conflating the two corrupts S1).
2. **Z-faces only** (vertical up/down faces; horizontal faces unaffected) and **SIGNED by weight class** (heavy ⇒ a downward
   bias on its Z-face moves; light ⇒ upward), magnitude ∝ the resolved weight class about the absolute neutral (tunable,
   per-type), consuming open-Z-face conductivity (R6: a slit biases less, a wall biases 0).
3. **PERSISTENT, not decaying.** The S1 bias decays to 0, so the settle holds «because the bias goes away»; buoyancy does NOT
   decay — so it must reach a fixed point BY CONSTRUCTION. The fixed point comes from the per-tick MAGNITUDE BOUND vs kpEff
   (the anti-overshoot guarantee — see «the settle floor»), NOT from back-pressure alone: back-pressure (VoxelFaceFlow.cs:137-150,
   `allowed = min(mag, remaining[src])`) only floors outflow to available mass (non-negativity); it does NOT by itself damp a
   balanced bias-down-vs-gradient-up oscillation around the settled state.
4. **MUST NOT bank into carry.** Like the S1 bias, the buoyancy directional term MUST NOT be banked into the per-face carry
   remainder — `_carry` is the gradient-only slit-seep accumulator AND a Mass-folded checksum member (VoxelField.cs ~312-328;
   VoxelFaceFlow.cs:103-124 documents exactly why S1 keeps the bias out of carry: a retained whole unit re-fires at ZERO
   gradient and breaks «довести фронт до покоя»). A clamped-away buoyancy unit STAYS in its source cell and is re-derived next
   tick. This trap is STRICTLY MORE dangerous than S1 (S1's bias decays so a banking bug self-heals; persistent buoyancy
   re-fires indefinitely and never settles).
A CREEPING front: a BOUNDED per-tick nudge — gas sinks/rises a few cells per tick — NEVER a teleport-to-floor. The buoyancy
term is a deterministic integer function of (resolved per-type weight param, current per-cell mass, Z-geometry), combined
into `desiredMove` before the clamp, recomputed each tick like the gradient. Do NOT prescribe the exact integer form — that
is the PLAN's call — but it MUST be: integer-only, conservative (mass-exact), creeping (bounded/tick), fixed-point-reaching,
carry-clean, and conductivity-scaled.

## the registry ContentHash fold (the lockstep-handshake determinism gate — DO NOT skip)

This slice ADDS a symmetric per-meta / per-type weight-class OVERRIDE (today `GasMetaType`/`GasType` carry only
`SpreadKpOverride` — GasMetaType.cs:20, GasType.cs:30 — and the Sc-types comment says the inert override slots are «added
when Sc-weight needs them»). That override is determinism-LOAD-BEARING and is NOT auto-folded: `ComputeContentHash`
(GasTypeRegistry.cs:146-160) today folds the PARENT params (incl. `parent.RatioToAir`, line 151) ONCE + per index ONLY
`(TypeId, MetaTypeId, EffectiveKp)` (lines 153-158) — there is NO per-type/meta weight. So two registries identical in
`(TypeId, MetaTypeId, EffectiveKp)` but differing in a per-type weight override yield an IDENTICAL ContentHash, hence an
IDENTICAL `MeaningMembers.TypeId` fold (VoxelField.cs ~379-389 folds ContentHash + the `(index,TypeId)` table) AND a matching
lockstep session-start handshake — while buoyancy physics diverges → a silent cross-peer / cross-mod desync under a GREEN
checksum (canon Факт-1 / §9.5 «чексумм ЗЕЛЁНЫЙ, физика мусор»; Факт-5 no-late-join early-rejection defeated). **OBLIGATION:**
the RESOLVED per-index weight (type ?? meta ?? parent) MUST be folded into `ComputeContentHash` EXACTLY as `effectiveKp[i]`
is (line 157 precedent) — `parent.RatioToAir` alone (the default) does NOT distinguish an override. RED control: two
registries differing ONLY in a per-type weight override MUST diverge the ContentHash (a silently-unfolded override that keeps
the hash green = FAIL). (Whether the resolved weight is precomputed into a `_weightByIndex` array or resolved on-the-fly is
the PLAN's call — only the FOLD is mandated.)

## the per-tick MeaningChecksum decision (trip-wire — the PLAN decides, but states which)

This is ORTHOGONAL to the ContentHash gate above (that is the registry-identity handshake; this is the per-tick field-state
digest). Buoyancy redistributes MASS, which is ALREADY a member (`MeaningMembers.Mass`). Two cases:
- **DERIVED (recommended):** if buoyancy is a pure per-tick function (resolved weight param + mass + Z-geometry), recomputed
  each tick and NEVER stored as field state, it adds NO new per-tick member — the mass redistribution it causes is already
  folded. The PLAN RECORDS this explicitly. (Determinism still requires the ContentHash fold above — DERIVED does not exempt
  it; even a purely-derived buoyancy reads a registry weight two peers can diverge on.)
- **STORED:** if the realization stores any per-type directional buoyancy STATE in the field, that state MUST become a NEW
  `MeaningMembers` member (next free bit `1 << 6`; current max is `TypeId = 1 << 5`, MeaningMembers.cs:36), folded ADDITIVELY
  via the **BIAS-style SKIP-ZERO precedent** (a zero-buoyancy face/plane folds NOTHING, so a weight-neutral type stays
  BYTE-IDENTICAL even inside a MULTI-type registry — VoxelField.cs ~334-339). Do NOT use the `!IsDefault` REP-conditional
  here — that is for the registry-IDENTITY (TypeId) member, NOT per-cell/per-face state; applying it would fold the all-zero
  buoyancy and BREAK byte-identity vs mass-only. Canonical order; a RED control isolates the member via `All & ~<member>` (a
  silently-absent member that stays green = FAIL). Regenerating/rebaselining the S0/S1/Sc-types goldens to absorb a buoyancy
  change = STOP-escalate.
Either way the existing S1 `_bias` (`MeaningMembers.Bias`, 1<<3) is NOT repurposed or extended for buoyancy.

## the settle floor — derive against the TRUE per-tick term, NOT raw Kp (G5 planner-note a)

`VoxelFaceFlow` runs each plane at `kpEff = registry.EffectiveSpreadKp(s) * spfClamped` (VoxelFaceFlow.cs:85), and the
per-face move is `mag * faceConductivity / kpEff` (lines 119-120); the monotone-settle floor is `Kp ≥ 2·degree` (degree ≤ 6
⇒ `MinSpreadKp = 12`), but the registry ENFORCES that floor on the RAW resolved Kp. The TRUE per-tick damping is
CONDUCTIVITY-DEPENDENT: at a FULLY-OPEN Z-face `cond == spf`, so `spf` CANCELS exactly to `mag/Kp` (raw Kp IS the correct
scale there — over-protection 1×, VoxelFaceFlow.cs:41-44); at a partial face `cond < spf` the damping is STRONGER (kpEff
over-damps — strictly safer), up to spf× at a 1-sub-face slit. So «raw Kp» is NOT uniformly conservative by a single factor —
it is exact for a full face and conservative only for partial faces. Sc-weight ADDS a PERSISTENT Z-bias to `desiredMove`,
which the gradient-only settle analysis never accounted for. OBLIGATION:
1. Derive the no-slosh / convergence-to-rest bound for the buoyancy term against the TRUE per-tick term
   `mag·cond / (Kp·spf)` — NOT a magic over-protection constant and NOT raw-Kp-assuming-spf=1 — and verify it across the
   conductivity range (full-face cond==spf is the spf-cancels case the column oracle runs on). Record the spf / floor
   (`MinSpreadKp`) dependency, so the bound is re-derived if either changes.
2. Bound the per-tick buoyancy MAGNITUDE so monotone convergence to rest STILL holds with the persistent bias present (it
   cannot lean on «the bias decays» like S1; it must reach a fixed point by construction; this magnitude bound — not
   back-pressure — is the anti-overshoot/anti-period-2 guarantee).
3. RED SETTLE oracle: a buoyancy-biased multi-Z column reaches Z-bias-flux QUIESCENCE (no net per-tick Z-flux; heavy-class
   centre-of-mass below light-class — NOT a fully-stratified «sorted column», which is the buried §7 band notion and not even
   guaranteed under sparse-dominant Факт-4) within bounded ticks; a planted over-strength buoyancy that SLOSHES FOREVER but
   keeps the loopback hash GREEN (byte-identical on both endpoints) MUST be RED here — the relational loopback hash (A==B)
   does NOT catch a both-endpoints-identical perpetual slosh.

## the no-hardcode-dispatch obligation (G5 planner-note b — Sc-weight is the FIRST per-type-DISPATCH slice)

`tools/type-hardcode-scan.ps1` catches only `enum`/`switch` TOKENS, and ONLY in `Core/Field/Types` (root, line 31). Its
header claims «the strongest possible mechanical guarantee that no hardcoded near-tier type path exists» — FALSE for
Sc-weight's threat model: (i) the buoyancy dispatch code lands in `Core/Field/Voxel` (the flow law), OUTSIDE the scanned
subtree; (ii) a `dict-of-delegates` keyed by TypeId, an `if (typeId == N)` chain, OR a **const array indexed by TypeId**
(`int[] _weightByType; bias = _weightByType[typeId]` — the EXACT `CoarseSpecies.Weights[]` shape this PORT risks
reproducing; note array indexing is NOT control flow, so it escapes even a «zero type-identity control flow» rule) all evade
the enum/switch token. Sc-weight is the FIRST slice that makes behaviour DIVERGE by type beyond a uniform per-plane Kp. The
PLAN picks ONE (a silent reliance on the old scan's false guarantee = STOP):
- **(a) PREFERRED — pure data-arithmetic, no dispatch:** realize buoyancy as ARITHMETIC on the resolved per-type weight
  param (read the weight resolved type??meta??parent as a NUMBER, compute the bias arithmetically — exactly as
  `EffectiveSpreadKp` is consumed), with ZERO type-identity control flow AND no per-type array/table keyed by TypeId (the
  weight resolves ONLY via `type ?? meta ?? parent` from the registry, never a parallel id-keyed array). THEN correct the
  scan's scope + «strongest guarantee» header to honestly state coverage, including the new Core/Field/Voxel buoyancy path.
- **(b) broaden the scan:** extend it to catch dispatch-by-comparison — `if (typeId == N)` chains, a dict-of-delegates keyed
  by TypeId, AND a const array indexed by TypeId — with a planted-violation self-test for each new pattern. ⚠ A naive
  DIRECTORY-append of `Core/Field/Voxel` (or `Core/Field/Determinism`) to the scan root is FORBIDDEN: the blunt
  `\benum\b`/`\bswitch\b` token rule would FALSE-POSITIVE on legitimate NON-TypeId code — the frozen geometry `switch (face)`
  in VoxelFaces.cs:23,40 and the `[Flags] public enum MeaningMembers` (MeaningMembers.cs:18) / `enum CoarseReductionMode`.
  Scope the new patterns by SYMBOL (TypeId-keyed dispatch), whitelist those legitimate enums/switches, and add them to the
  self-test's mustPass cases.
Either way: add the symmetric meta-type / type weight OVERRIDE (resolution `type ?? meta ?? parent`) AND fold its resolved
value into ContentHash (see «the registry ContentHash fold»). The FROZEN far-tier `CoarseSpecies` stays UNSCANNED + untouched.

## boundaries (out of scope / STOP-escalate if tempted)

- **Per-column instant sort near = STOP** (§3 forbidden vertical teleport / pop; do NOT copy `CoarseBandStep.Settle`'s
  capacity-fill/densest-first allocation into near). Near buoyancy is a CREEPING bias on Z-face flow.
- **NO visual-track hookup** (engine-only). The g-7e15 visual track's reserved `RiseSinkBias` cosmetic field (already on
  `main`, reserved by c-visual-001; c-visual-002 S2 will later DRIVE it) is a SEPARATE read-only field — do NOT touch the
  visual track and do NOT conflate the engine-authoritative buoyancy with the visual's reserved field.
- **Do NOT touch / refactor / re-data-drive / move / scan the FROZEN far-tier** `CoarseSpecies` / `CoarseBandStep`
  (Core/Field/Coarse) — PORT the LAW by re-expressing the numbers as DATA, leave the source frozen (retires at S4); the
  type-hardcode scan must still NOT scan it.
- **NO reactions, NO damage.** Temperature appears ONLY as the OPTIONAL buoyancy T-coupling term (reserved / zero-stubbed,
  keeping the far-tier law shape) — NOT the Sc-damage sink-layer mechanic. A live temperature mechanic = Sc-damage = STOP.
- **NO stored velocity / advection / true inertia / coasting** — buoyancy is a BIAS on flow, NEVER a velocity field
  (TIER-3 / ADR-0010-class is RESERVED, owner-gated, cracks the lock — d-gas-richness-tiers-001). A need for one = STOP.
- **Repurposing the S1 per-face `_bias` register for per-type buoyancy = STOP** (per-face-not-per-species).
- **The buoyancy term MUST NOT be banked into the per-face carry remainder** (carry is the Mass-folded gradient-only
  slit-seep; banking re-fires at zero gradient and never settles).
- **NO float on the authoritative path / re-flux-as-gate**; integer-only; laws in headless Core/**. Lock = ADR-0002, NOT
  reopened.

## ведро classification (PLAN reconfirms — already decided)

- **Ведро-2** (coarse-promotable, IN-checksum, shared by all peers): per-type buoyancy is an authoritative law on the shared
  50cm grid — it rides the mass every peer agrees on. The substrate all later character mechanics ride.
- **Ведро-1** (off-checksum local detail): ABSENT this slice. **Ведро-3** (sub-room AND shared): ABSENT.
The PLAN reconfirms this disposition; it does not re-derive it.

## done_when (verifiable)

1. **PLAN (owner present):** §Re-sync FIRST; ingest canon §3 (buoyancy-BIAS-not-sort) + §7-buried (no bands) + §8 far-tier
   code-map + d-character-road-001 + R15; DECIDE and RECORD: (i) the buoyancy realization (per-type Z-face creeping bias) +
   whether the temperature-coupling term is included / zero-stubbed / reserved (recommend reserved); (ii) the ABSOLUTE NEUTRAL
   weight reference (the value yielding zero Z-bias) — so done_when #2's «a weight-neutral type does not drift» is a
   well-defined falsifier (and disambiguate #2's two «weight-neutral» senses: a MIDDLE type in a mixed run vs an
   all-same/single-default run); (iii) the per-tick MeaningChecksum decision (DERIVED→no member + recorded rationale, or
   STORED→new additive SKIP-ZERO member, per the trip-wire) AND the registry ContentHash fold of the new weight override;
   (iv) the no-hardcode-dispatch fix (option a pure-arithmetic + scan-honesty, or option b broaden-the-scan-by-symbol);
   reconfirm ведро (ведро-2 only); name the per-type weight-class param VALUES for the 2-3 Sc-types test types (heavy/
   light-spanning, relative to the recorded neutral).
2. **≥2 test types of DIFFERENT weight class DIVERGE vertically** — independent-author RED: over a seeded multi-Z run, a
   heavy-class type's vertical centre-of-mass SINKS and a light-class type's RISES (and a middle weight-neutral type does NOT
   drift, against the recorded neutral reference). **NO REGRESSION:** an all-same-weight / single-default run reproduces the
   committed pre-slice gas golden BYTE-IDENTICALLY — verify FIRST-HAND at the tip WHICH committed golden covers the gas path
   (do NOT assume a literally named test); the loopback two-endpoint `VoxelField.MeaningChecksum` harness is the
   determinism-by-construction tripwire, NOT the golden, and being relational (A==B) it will NOT catch a uniform fold (see #6).
3. **CREEPING FRONT / NO-POP RED oracle:** buoyancy moves a BOUNDED amount of mass per tick (no per-column instant sort / no
   vertical teleport-to-floor); a planted instant-sort / unbounded realization MUST FAIL the no-pop oracle.
   **CONSERVATION:** total AND per-species mass exact across the buoyancy step (RED non-monotone-conservation control: a
   planted leak/duplication MUST FAIL). **CARRY-CLEAN:** a carry-banked buoyancy realization that moves at ZERO gradient MUST
   FAIL the fixed-point/settle oracle.
4. **SETTLE oracle against the TRUE per-tick term:** a buoyancy-biased multi-Z column reaches Z-bias-flux QUIESCENCE
   (heavy-class COM below light-class — NOT a fully-stratified sorted column) within bounded ticks; the no-slosh bound is
   DERIVED against `mag·cond/(Kp·spf)` (NOT raw-Kp-assuming-spf=1, NOT a magic factor), the spf/floor dependency recorded;
   a planted over-strength buoyancy that sloshes forever but keeps the loopback hash GREEN MUST be RED here.
5. **DATA-DRIVEN, no per-type hardcode (the dispatch obligation):** buoyancy strength resolves from the per-type
   weight-class param via `type ?? meta ?? parent` (add the symmetric meta/type override); NO enum/switch/`if(typeId==N)`/
   dict-dispatch / const-array-indexed-by-TypeId on the buoyancy path; the no-hardcode falsifier covers the buoyancy code's
   ACTUAL location with a planted-violation self-test for each evasion pattern (option b, scoped by symbol — NOT a blind
   directory-append that false-positives on VoxelFaces' geometry `switch(face)` or the `MeaningMembers` enum), OR buoyancy is
   pure data-arithmetic with ZERO type-identity control flow AND no id-keyed array, with the scan's scope + «strongest
   guarantee» header corrected to honest coverage (option a). The FROZEN far-tier `CoarseSpecies` stays unscanned + untouched.
6. **CHECKSUM sockets (conditional on #1):** (a) the new per-type/meta weight OVERRIDE is FOLDED into the registry
   `ComputeContentHash` (symmetric to `effectiveKp[i]`) with a RED control — two registries differing only in a weight
   override DIVERGE the ContentHash (lockstep-handshake gate); (b) per-tick field state: DERIVED → the PLAN RECORDS that
   buoyancy adds no per-tick member (mass already covers it); STORED → a NEW `MeaningMembers` member, ADDITIVELY (SKIP-ZERO,
   NOT `!IsDefault`) folded (canonical order; `All & ~<member>` RED isolates it; weight-neutral byte-identical). The S1
   `_bias` register is NOT repurposed.
7. **DETERMINISM + scan coverage:** integer-only authoritative path; the new buoyancy code covered by BOTH the zero-float +
   int-overflow scans. NOTE: both scans ALREADY carry IDENTICAL `$DefaultRoots` (incl. `Core/Field/Voxel` and
   `Core/Field/Types`) — no current root mismatch; the obligation is forward-discipline. The buoyancy code lands under
   already-scanned roots (the Voxel flow-law + the Types override slots), so the REACHABLE case is: VERIFY both scans cover
   the new files (DEMONSTRATED, not asserted). ONLY IF a NEW authoritative directory appears, add it to BOTH root lists (keep
   them identical) + a planted-violation RED self-test there. (The TYPE-HARDCODE scan is a SEPARATE obligation under #5 —
   float/overflow coverage of `Core/Field/Voxel` does NOT close the no-dispatch hole, since type-hardcode-scan.ps1 roots only
   at `Core/Field/Types`.) Loopback determinism hash green over a multi-type buoyancy seeded run (planted-float /
   order-dependence RED controls).
8. **check.ps1 -Deliver GREEN** (build + headless + zero-float + int-overflow + mutation ≥70 on new Core + spec-silence +
   deliverable-coverage). G0-frozen (openspec + frozen spec + ledger + mutation-<id>.json ≥70; RESULT.md = DELIVERED).
9. **ZERO-LEGACY**; tests rewritten not dragged.
10. **OWNER-EYE (confidence, NOT a gate):** owner sees a heavy test gas pool/settle low and a light test gas collect high in
    the debug view, CREEPING (not snapping); owner-run, no self-marking.

## discipline / gates (carried)

RED-first by an INDEPENDENT test-author (builder cannot edit the red tests) · Core/** placement · -Deliver GREEN · mutation
≥ floor (70%) · a FRESH-SESSION G5 (different model family) refuting the buoyancy-creeps-not-sorts /
settles-against-the-true-kpEff-term / no-vertical-pop / conserves-mass / carry-clean / data-driven-no-dispatch /
weight-override-folded-into-ContentHash / per-tick-checksum-decision-sound / ports-the-law-not-CoarseBandStep's-sort /
single-type-no-regression seams — COULD-NOT-REFUTE is the bar · STOP-discipline (a per-column sort near, copying
`CoarseBandStep`'s capacity-fill, touching the frozen far-tier source, repurposing `_bias`, banking buoyancy into carry,
relying on the old scan's false «strongest guarantee», a velocity/inertia/coasting term, a live temperature mechanic, float
on the authoritative path, reopening ADR-0002 = mandatory STOP + escalate) · build in small steps.

## return

A RESULT routed HOME (the OS owns the next CALL): outcome + evidence (commits, -Deliver transcript, mutation json, G5
verdict, the multi-type buoyancy loopback hash + RED-control trips, the realization + per-tick-checksum + ContentHash-fold +
scan-fix decisions, the recorded absolute-neutral reference, the kpEff-derived settle bound) + findings for the planner.
dev→main merge + push is OWNER-GATED. On GREEN → the road rolls to Sc-reactions (integer chemistry between types).

## budget

One slice. If the PLAN finds per-type buoyancy + the settle/no-pop oracle + the ContentHash fold + the scan-completeness fix
is too big for one leg, STOP and return "split needed" (e.g. the per-type Z-bias creeping front + no-pop/conservation/settle
oracle + ContentHash fold land first; the temperature-coupling term + any stored per-tick checksum member second) — do not
silently build a blob. Keep the TEST-types scope tight (the 2-3 Sc-types test types, weight-class-spanning).

END_OF_FILE: live/indie-game-development/work/c-exec-020-call.md
