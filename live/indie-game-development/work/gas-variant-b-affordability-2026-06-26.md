I have the complete materials: the shared frame, five strategy analyses, and three kill attempts. I will synthesize now. No new file reads are needed — the SPEC grounding is fully carried in the inputs, and I will quote `file:line` as the analyses did.

# Variant-B affordability — synthesis verdict

## 1. Headline

**The B-cost is a real wall, but only at the observed hangar — and Variant-B is made affordable broadly NOT by a cheaper representation but by collapsing the count of rooms that need true spatial precision: most "B" mechanics are secretly Variant-A (monotone, answerable by an in-checksum coarse-total threshold), the genuinely-B rooms stay full-3D, and the height-field survives only as a far-tier vertical-LOD knob — never as the near B-tier the owner hoped for.**

The owner's core insight (cost should follow gas STATE, settled is cheap) is **correct about cost and wrong about where it helps**: settled gas is already free via byte-sleep (`:52`), and the place a height-field would save most (the observed hangar) is exactly where canon forbids it (crouch dies `:27`, demote = vertical pop `:62`).

## 2. Recommended fidelity ladder

What gas STATE picks which tier, and what survived the kills:

| Tier | Gas state / condition that selects it | Status | What the kills landed |
|---|---|---|---|
| **Full 3D @50cm (near)** | Any room a player occupies OR active/turbulent OR non-monotone (wind/reaction/breach) OR multi-type interface OR overhang/pit/low-ceiling | **ADOPTED (load-bearing baseline, S5)** | Correct-by-construction; determinism-free; the only tier that answers B with zero approximation. Unbeaten on correctness. |
| **Byte-sleep + sparse fine-shadow** | Saturated, settled, unobserved; held/D5 rooms | **ADOPTED (already canon, S5)** | This *is* the safe core of S4. expand=identity (`:68`), O(1) wake. The real "settled is cheap" win lives here, not in a new tier. |
| **2-band far rollup (interim)** | Distant rooms, no observer, until S4 room-rollup | **ADOPTED (already canon)** | Kept-as-far-tier until S4 (`:168`). The existing stratified far model. |
| **Height-field / per-column-k (mid-2.5D)** | FAR/unobserved rooms only, as a vertical-LOD refinement of the far tier (BandCount=2 → per-column-k) | **ADOPTED-WITH-LIMITS — far only** | S1 survives ONLY here. As a *near* B-tier it is **KILLED** (transition-determinism-kill + heightfield-kill). See §3. |
| **Coarse-total threshold rule (monotone-B → A)** | A B-mechanic *proven* monotone/path-independent (slow flood, fill-line): `broke = coarse_cumulative_mass ≥ static_corner_threshold` | **ADOPTED-WITH-LIMITS (the real prize)** | This is the salvaged core of S4. In-checksum, byte-identical at any observation tick, needs zero fine state. Demotes "B" rooms back to A — shrinking the B-count. Gated behind a RED oracle test with a non-monotone control that MUST fail. |
| **Sub-partition (region_id split)** | Huge rooms (hangar) for far-rollup keying + localizing ведро-3 | **ADOPTED-WITH-LIMITS (enabling infra, S3)** | Necessary day-one plumbing for far-rollup; **cost-neutral-to-negative on the observed hangar**. Never sold as the cost-reducer. Adaptive/runtime re-partition + coarser cells FORBIDDEN. |
| **State-driven near promote/demote (S2)** | "auto-demote settled near rooms to columns" | **REJECTED — KILLED** | transition-determinism-kill: free the bits ⇒ lose the mid-air pocket ⇒ no-pop violation on expand (`:68`,`:94`); keep the bits ⇒ no memory freed ⇒ it's S5. Structural contradiction, not tuning. Plus settle-predicate is a derived-field-in-checksum lock-opener (`:97`). |
| **Lazy resolve arbitrary B from endpoints (S4 general)** | "skip sim, synthesize answer at observation" | **REJECTED — KILLED** | lazy-resolve-kill: dose is time-integrated (`:74`), field is non-monotone (`:134`); correct ⇒ full replay, cheap ⇒ silently wrong, and silent-wrong agrees across peers (passes checksum, fails ground truth). Zero relief for the observed hangar. |

**The ladder in one sentence:** near = 3D-or-asleep (full stop); far = rollup with an optional per-column-k vertical-LOD knob; B-precision is made broad by *reclassifying monotone-B to a coarse-total rule*, not by a cheaper near representation.

## 3. The height-field tier verdict

**Verdict: ADOPT-WITH-LIMITS as a FAR-tier vertical-LOD knob only. REJECT as an intermediate near/observed B-tier.** Both kills landed decisively on the near use; S1's own analysis already retreated to this home.

**Where it is legal (the §6 п.4 knob):** an unobserved, player-absent far room may carry per-column-k layered fill instead of BandCount=2. Mass-exact, commit-gated, largest-remainder per-layer (`:94`). The round-trip pop is invisible (no observer), crouch is irrelevant (no player, `:113`). This genuinely answers the *settled, unobserved* corner-loot case at 8–48× less state and is a clean refinement of the far tier that already ships.

**Where it gives WRONG answers → MUST fall back to full-3D (the kill findings, folded):**

1. **Any player-occupied room** — crouch-under-a-layer needs head/feet in distinct Z-cells (`:27`); a single fill-height has one height per XY. Demote-with-player-present = the forbidden vertical pop (`:62`, the buried `CoarseBandStep`).
2. **Two stacked gas types** — heavy-low + light-high + clear void: a single `(height,type)` column is a lie at one layer and loses the interface-Z the reaction trigger needs. This is the **flagship two-type-interface mechanic** (`:77`) — the heightfield-kill's strongest shot. Minimum honest form = **two heights per column** (heavy fill + light fill ⇒ interface derivable), which erodes 48× → ~24×.
3. **Mid-air / suspended blob, overhang/mezzanine, pit-vs-pan, low-ceiling-clamp** — all non-monotone in Z or multi-body per XY; the column fabricates a settled monotone fill that isn't there.
4. **Mid-motion query** — valid only once settled; B-answers are demanded *during* events.
5. **Trigger path** — the column may serve the spatial corner-mask ("which XY corners are below fill"), but the reaction fire/no-fire decision stays on refinement-invariant coarse totals, chain next tick (`:74`). The column never decides detonation.
6. **Seam #4 hard constraint** — never average a column to one scalar (`:94`); the naive single-fill form *is* that forbidden averaging and is not lock-safe.

**Lock status:** reviving the superseded `mid-2.5D` tag (`:92`, `:157`) is lock-adjacent — it does NOT touch Факт-2 (columns stay 50cm XY-isotropic, no ADR-0010), but it reverses a §7 "не воскрешать" entry, so it needs an **owner-signed decision** to legitimately re-add the tag, scoped to far-only.

## 4. Quantified worst case — with vs without the ladder

Cost law is canon: weak-peer limit = `active_cells / cores`, Burst/Jobs ×4–8 (`:134`). Every peer pays for the **union** of all awake cells (lockstep — work is NOT split 8 ways).

**Typical play (8 players, ~8–12 small/medium live rooms, no hangar):**
- Baseline (S5): ~13k–25k awake cells. **Comfortably real-time** (well under the ~200k comfort ceiling `:132`).
- With ladder: identical — B-mechanics that are monotone now cost a single integer compare instead of fine cells, so the ladder is *marginally cheaper*, never more. **Fits a weak CPU with margin, with or without the ladder.**

**Adversarial worst case (cascade through a chain of large rooms + 8 manipulators + one player in the hangar):**
- Baseline (S5): hangar ~256k–1.23M + 7 players × 3k–12k ≈ **280k – 1.3M awake cells on every peer at once.** Exceeds the comfort ceiling; lands on the **unmeasured hangar wall** (`:134`).
- **With the full ladder: essentially unchanged.** The hangar is observed → height-field illegal there → still full-3D. Lazy-resolve gives zero relief (observed). State-driven demote is dead. Sub-partition is cost-neutral-to-negative on the observed hall. **No adopted tier lowers the worst-case number**, because every adopted cheap tier is legal only where a player is *absent*, and the worst case is *defined* by a player being present.

**The honest conclusion the ladder forces:** the ladder makes the *typical* and *many-settled-B* cases cheaper and reclassifies most B to a free coarse rule — but the absolute ceiling (observed hangar) is bounded by **nothing in S1–S4**. It is bounded only by the two canon design fallbacks (`:134`): shrink the level, or accept the measured cost. **Whether the observed hangar fits at all is the one unmeasured number and remains so.**

## 5. Determinism

| Adopted element | Byte-identical lockstep-safe? | Cost / mechanism |
|---|---|---|
| Full 3D near | **YES, by inheritance** | Integer, zero-float, double-buffered pure function of last tick (`:134`). No new surface. |
| Byte-sleep + shadow | **YES** | Already in checksum; ticks_asleep canonical-order in-checksum; expand=identity (`:68`). |
| Far height-field (per-column-k) | **YES, conditional** | Must obey seam #4 (per-layer largest-remainder, never scalar-average, `:94`), conversion only against a committed revision (`:97`), region_id-keyed checksum order (`:95`). No new determinism machinery needed — but the single-scalar form is NOT safe. |
| Monotone-B coarse-total rule | **YES** | Pure integer function of in-checksum coarse mass at the observation tick; identical on every peer regardless of *when/who* observes — because it reads the shared in-checksum total, not a private replay. This is exactly why `:74` mandates triggers read coarse totals. |
| Sub-partition | **YES, conditional** | Partition must be a pure function of committed geometry/revision (never live state, `:97`); cross-cut reaction summation must be partition-invariant (`:74`) or it silently changes physics. |

**The two determinism traps the kills exposed (both avoided by the rejections):**
- **Silently-deterministic info loss** — S2's promote and S4's endpoint-resolve both produce byte-identical *wrong* answers that pass the cross-CPU checksum but diverge from ground truth (`:94`/`:95` vs the silent-wrap class at `:46`). Rejecting S2-near and S4-general removes this entirely.
- **Derived-field-in-checksum** — driving an in-checksum tier transition off the out-of-checksum front/settle predicate (`:72`,`:97`). Avoided because we do NOT adopt state-driven near transitions.

Every adopted tier is byte-identical with **no new determinism mechanism** beyond seams that already exist.

## 6. Does this change the R# or just extend it?

**Mostly EXTEND, with one small new reservation to make in S0.**

Already covered (no change): `representation_tag = {fine-3D | coarse | bucket}` exists day-one (`:92`); `region_id` per-tier exists day-one for sub-partition (`:67`); collapse/expand seam (`:94`); commit-revision cross-layer read (`:97`); triggers-read-coarse-totals (`:74`); byte-sleep + sparse-shadow (`:68`); the far vertical-strata-count as a tunable LOD param is already named open in §6 п.4 (`:136`).

**What to ADD / reserve in S0 (small, additive, non-lock-breaking):**
1. **Re-admit `mid-2.5D` to the tag enum as FAR-ONLY**, owner-signed, with a hard invariant: *illegal for any player-occupied or active region; per-column-k layered, never single-scalar.* This reverses a §7 "не воскрешать" entry → needs an owner decision, but it does not touch Факт-2.
2. **Add a monotone-B classification predicate** to the Variant-A/B test (`:81`): a B-mechanic that is provably monotone/path-independent is resolved by an in-checksum coarse-total corner threshold and demoted to A. This is a *sharpening* of the existing A/B test, not a new seam.
3. **Reserve the `settled_flag` / quiescence as an in-checksum integer** (ticks-since-net-flux from the committed flux-register) — used ONLY to gate far-demote and byte-sleep, **never** a near transition. This is the one genuinely new in-checksum quantity; keep it minimal and far-scoped.

No new state-file type. No ADR-0010 (Факт-2 intact — cells stay 50cm isotropic everywhere). The fidelity ladder is **not a new core seam**; it is the existing seam-set with one far-LOD tag re-admitted and the A/B test sharpened.

## 7. Recommendation + what to prototype/measure first

**Position (no hedge): SHIP S5 baseline as the authoritative B-mechanism. Do NOT build a near height-field, do NOT build state-driven near promote/demote, do NOT build lazy-resolve. Make B broad by reclassification (monotone-B → coarse-total rule), not by representation.** Adopt the far height-field and sub-partition only as the unobserved-room LOD/keying infrastructure they already are.

**Why this is the call:** the owner wanted "spatial precision broadly" via a cheap near representation. Both kills proved that representation cannot be both cheap and correct near a player — and the worst case is *defined* by a player. The thing that actually makes B broad is cheaper: prove most B-mechanics monotone and answer them with a single in-checksum integer compare, which is *free* and *more correct* than any column. "Spatial precision broadly, cheaply, near the player" is a fantasy; "most B-precision is secretly a coarse threshold" is real and large.

**Prototype / measure FIRST, in strict order:**
1. **The hangar probe (`:134`) — the one unmeasured number, before anything else.** One player in an open ~256k-cell @50cm hall on the weakest target core, full-3D, Burst/Jobs. Measure cache/memory, not flops. **This single number decides whether ANY of the rest matters** — if the observed hangar doesn't fit, the answer is a design concession (cut/shrink the hangar), and no tier saves it.
2. **The monotone-B oracle test (RED-first).** Full-sim vs the coarse-total corner rule on a seeded scenario, assert identical corner-loot outcome — **with a mandatory non-monotone control (wind into-then-out-of the corner) that the rule MUST get wrong.** This proves the A/B boundary is real and policed before the rule touches any executor. If this can't be made to pass+fail cleanly, the reclassification is unsafe and we stay pure-S5.
3. **Far per-column-k collapse/expand round-trip** (only if 1 and 2 pass): assert mass-bit-exact, expand=identity on a held room, on a *settled two-type* column (the case that erodes 48×→24×) — to measure the *real* far saving after honoring seam #4.

Run 1 before committing a single line of tier code. It is the gate on the entire question.

---

**Files referenced:** `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\knowledge\g9c41-gas-engine-SPEC.md` (§2 Факт-2 lock; §3 `:52`,`:62`,`:68`,`:72`,`:74`,`:77`,`:79`,`:81`; §6 `:128-145` esp. `:134`,`:136`; §7 `:148-160` esp. `:150`,`:157`; §8 `:164-180` esp. `:166`,`:168`,`:171`; tag/seam `:92`,`:93`,`:94`,`:95`,`:97`,`:113`).