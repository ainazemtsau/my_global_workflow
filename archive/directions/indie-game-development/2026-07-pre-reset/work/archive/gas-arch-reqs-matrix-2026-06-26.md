> ⛔ **NOT ADOPTED — ARCHIVED AS HISTORY (2026-06-28, s-work-023).** This draft proposed candidate E
> (host-state-sync + float clouds far + fine grid near), which requires un-signing ADR-0010. Its
> facts were verified first-hand and held (the locked far-rollup is a position-less SUM, so R7/R12 at
> 50cm in player-absent rooms is a real representation gap), and candidate E was genuinely
> under-evaluated by the prior cloud-vs-grid analysis (which only covered cross-CPU determinism). But
> the whole case rested on R7/R12 being a hard requirement EVERYWHERE. The owner resolved that
> question (s-work-023): «точно у игрока, грубо везде» — deep interaction = full precision where the
> player is (+2-3 Ведро-3 rooms) + coarse events everywhere, which the canon AS-LOCKED already
> delivers. => **input-lockstep STANDS; no ADR-0010 un-lock; this candidate is not pursued.** Kept as
> history (NOT authority). CARRY: if host-authority is ever reconsidered, RE-RUN the cloud-vs-grid
> analysis on the host-auth model first (its kills are determinism-class, void under a single host).
> See decision d-clouds-fork-resolved-001.

# GAS ENGINE NETWORKING — FULL REQUIREMENTS-COVERAGE VERDICT

## 1. VERDICT HEADLINE

**E wins — host state-sync with float clouds far + a fine float grid in a per-player AoI near-window — because it is the ONLY candidate that satisfies the owner's hard precision requirement (R7/R12: 50cm reactions and the level-spanning split in rooms with no player) while fitting normal home internet (~210-400 KB/s host upload) and one host's CPU. The networking change flips the prior verdict: under host state-sync the prior analysis's cloud-kills are determinism-class and VOID (single host, no cross-CPU bit-identity), so clouds are legitimate again — and the position-less SUM bucket that the current grid (A/B/D) collapses far rooms into structurally CANNOT express "gas stops 1.5m short of the corner." The cost is real and must be stated plainly: E requires switching off lockstep and discarding the BUILD-hardened integer-grid determinism apparatus (owner-signed ADR-0010), which is the largest migration of any candidate.**

## 2. THE FULL MATRIX (R1-R20 × A-E)

| R# | Requirement | A (lockstep grid+rollup) | B (lockstep grid+sphere-cap) | C (clouds everywhere) | D (host grid+rollup) | E (host clouds-far+grid-near) |
|---|---|---|---|---|---|---|
| **R1** | spawn anywhere | ✅ any cell | ✅ any cell | ✅ coord-native | ✅ any cell | ✅ coord-native |
| **R2** | spreads room-to-room everywhere | ✅ coarse-far | ✅ coarse-far | ✅ blob advect | ✅ coarse-far | ✅ cloud-far |
| **R3** | finite source keeps POSITION | ❌ far smears | ⚠️ near-only | ✅ cloud at corner | ❌ far smears | ✅ cloud at corner |
| **R4** | walk THROUGH gas — dose near | ✅ fine grid | ✅ fine grid | ⚠️ blob-soft edge | ✅ fine grid | ✅ fine grid |
| **R5** | loot broken BY gas — near + close room | ⚠️ room-avg far | ⚠️ room-avg far | ✅ coord overlap | ⚠️ room-avg far | ⚠️ cloud-grain far |
| **R6** | two-gas react ~50cm — near | ✅ fine grid | ⚠️ decides coarse | ⚠️ radius-limited | ✅ fine grid | ✅ fine grid |
| **R7** | ★react 50cm in close room, NO player★ | ❌ **CANNOT** | ❌ **CANNOT** | ⚠️ if dense | ❌ **CANNOT** | ⚠️ **only one that can** |
| **R8** | reaction in SUPER-far room | ✅ built for it | ✅ built for it | ✅ 1 blob | ✅ built for it | ✅ 1 cloud |
| **R9** | explosions near + far | ✅ coarse trigger | ⚠️ far blind | ⚠️ pop risk | ⚠️ far blind | ⚠️ far cloud-grain |
| **R10** | destructibility / breach changes flow | ✅ edge flip | ✅ edge flip | ✅ float reroute | ✅ edge flip | ✅ edge + cloud |
| **R11** | energy / wind (advection) | ✅ integer bias | ✅ integer bias | ✅ native | ✅ float bias | ✅ native |
| **R12** | ★CENTER: split decides exit-door, no player★ | ⚠️ 2-3 rooms only | ❌ worse than A | ⚠️ if dense | ❌ can't replicate | ⚠️ if dense (best fit) |
| **R13** | 8-player WORST CPU (2 halls+6) | ❌ uncapped | ✅ sphere-capped | ✅ O(entities) | ⚠️ 512k on host | ✅ AoI-capped |
| **R14** | mass conservation exact | ✅ integer carry | ✅ integer carry | ⚠️ float ledger | ✅ single-host | ⚠️ seam + ledger |
| **R15** | no-desync / authority correctness | ✅ free integer | ✅ free integer | ✅ single-host | ✅ single-host | ✅ single-host |
| **R16** | ★bandwidth fits home internet★ | ✅ inputs only | ✅ inputs only | ⚠️ if sparse | ❌ BUSTS | ⚠️ AoI closes it |
| **R17** | host-CPU one machine / distributed | ⚠️ weak-peer risk | ⚠️ weak-peer risk | ✅ cheapest | ⚠️ 512k risk | ⚠️ fits via AoI |
| **R18** | latency tolerable for gas | ✅ | ✅ | ✅ | ✅ | ✅ |
| **R19** | far-field render cheap + legible | ⚠️ no silhouette | ✅ room-grain | ✅ render-native | ⚠️ no silhouette | ✅ render-native |
| **R20** | migration from hardened grid | ✅ zero (is current) | ✅ near-zero | ❌ full restart | ⚠️ netcode rewrite | ❌ biggest migration |

**Score (✅ / ⚠️ / ❌):** A = 11/5/4 · B = 11/6/3 · C = 11/7/2 · D = 9/6/5 · E = **12/7/1**

The raw count is close — but it is NOT a vote. Three rows are decisive (R7, R12, R16) and they split the field by *capability class*, not by tally.

## 3. BANDWIDTH VERDICT ROW (R16, quantified, 20 Hz, ≤500 KB/s host upload ceiling)

| Cand | Host upload (KB/s) | Verdict | Why |
|---|---|---|---|
| **A** | **< 1-5 KB/s** | **FITS** ✅ | Inputs only (canon `:22`). 100× under ceiling. Constraint is CPU, not wire. |
| **B** | **< 1-5 KB/s** | **FITS** ✅ | Inputs only; sphere bubble is off-checksum, never wire'd (`:33`). |
| **C** | **32-96 sparse → 120-400 dense** | **FITS-WITH-WORK** ⚠️ | Clouds broadcast (one shared set, not ×7). Delta mandatory. **BUSTS** per-client (64) when R7/R12 force dense clouds. |
| **D** | **768 KB/snapshot · ~15 MB/s full** | **BUSTS** ❌ | One 8m hall = 256k cells × 3B = 768 KB — a *single snapshot* exceeds the whole budget. Only "fits" by degrading to position-less buckets (then fails R3/R7/R12 like A/B). |
| **E** | **~210-400 KB/s** | **FITS-WITH-WORK** ⚠️ | Far cloud broadcast (~32-96) + 7× AoI near-window (~20-40 each). Under 500 ceiling; per-client ~50-64 sits AT the ceiling. **Locks:** near-window 4m radius + 50cm inside-cell. 8m or 25cm → ×8 → busts. |

**The decisive bandwidth fact:** clouds compress ~2 orders of magnitude better than fine cells (whole level as clouds ≈ 16-48 KB vs ONE hall as cells ≈ 768 KB), because clouds are O(occupied-blobs) not O(volume). D proves "grid + state-sync" only works with AoI — which is exactly what makes E the disciplined version of D.

## 4. THE HARD REQUIREMENT — R7 (50cm reaction in a close room the player is NOT in)

This is the requirement that decides the architecture. Owner's case: gas fills 80% of a room but stops ~1.5m (3 cells) short of the corner where the other gas/loot sits → the reaction must **NOT** fire.

**PASS (structurally capable): C and E.**
**FAIL (structurally cannot): A, B, D.**

**Why A/B/D fail — and it is NOT a tuning gap, it is a representation gap:**
- Canon `:68` — far rollup stores `coarse_mass[layer]` = a scalar integer **SUM** of the room's cells. Once collapsed, **no coordinate survives**: "80% full, stops 3 cells short" and "100% full" are byte-identical.
- Canon `:74` — the reaction trigger reads "refinement-invariant **ГРУБЫЕ тоталы**" (coarse totals), NOT fine cells. So in an unoccupied room the *only* authoritative input to the reaction decision is a number that cannot encode the 1.5m gap. The trigger has no input that could ever say "no." **It fires the reaction that must not fire.**
- B is strictly *worst*: its design premise is "cap detail to player spheres," so a player-absent room gets ZERO sub-room structure by construction.
- D's floats and single-host change arithmetic and netcode — they do **nothing** for representation. Same SUM bucket, same blindness. D *can* promote the room to a fine grid in sim, but must then replicate a churning fine room → busts bandwidth (R16). Reachable in sim, not in replication.
- The canon's own escape hatch is per-room "Ведро-3" promotion (`:79`) — "this room computes detail for ALL peers" — explicitly limited to ~2-3 pre-designated rooms. That fails the design intent that deep gas interaction is the CENTER **everywhere** (`:83`).

**Why C/E pass — and what it honestly costs:**
- Clouds carry coordinates, so "the gas centroid is ~1.5m from the corner" is *expressible in any room, occupied or not*. Two non-touching clouds → no overlap → no reaction. A/B/D cannot even say this.
- **The prior analysis's cloud-kills do NOT apply here.** Those kills ("double-claim race → checksum GREEN, physics garbage"; "split/merge byte-determinism") are cross-CPU bit-identity failures (`:46`). Under one host there is no second peer to disagree — "double-claim" becomes an ordinary host-local bug to code correctly, not a desync. Low cheat-resistance (friends) makes single-host gas authority acceptable (`:142`).
- **Two real costs remain (not determinism — these survive single-host):** (1) **Resolution cost** — true 50cm gating requires the far cloud field to carry ≤~50cm sub-room density in rooms that host a reaction pair. This is the same fine-far resolution A/B couldn't afford, just *moved* — paid as cloud density on ONE host, not grid cells on EVERY peer. It is unmeasured (hangar-class, `:134`) — so C/E are ⚠️ (achievable) not ✅ (proven). (2) **Float mass-conservation** — cloud split/merge leaks fractional mass unless a host-side ledger enforces it; integer-grid A gets this free.
- **E beats C on R7's sibling rows:** E keeps a fine grid in the near-window → R6/R4 stay crisp 50cm *near* (clouds are blob-soft there), while clouds-far deliver R7/R12. C wins R7 the same way but loses near-crispness.

**Verdict on R7:** the owner's hard requirement is deliverable by C or E only, and **E is the better fit** (crisp near + coordinate-bearing far). It is NOT free under any model — but A/B/D cannot deliver it everywhere *at all*.

## 5. RECOMMENDATION

**Primary: adopt E — host state-sync, float clouds far + fine float grid in a per-player AoI near-window. Fallback: B (sphere-capped lockstep grid) if the owner will NOT pay the migration.**

**The foundational call — yes, this requires switching from lockstep to host-state-sync.** That is the load-bearing decision, and it cuts both ways:

**What state-sync BUYS:**
- **Removes the cross-CPU determinism constraint entirely.** Floats become legal; the zero-float scan, integer-clamp ceremony, and loopback-hash apparatus (`:46`, `:93`) are no longer required for correctness. One host = sole author; clients are pure replicas. No desync class to defend (R15 ✅).
- **Unlocks clouds** — which are the *only* representation that carries position into player-absent rooms, the *only* thing that answers R7/R12, and the cheapest far-render primitive (R19).
- **Caps the canon's single unmeasured number** (the hangar wall `:134`): E's sphere-bounded near-window makes 8 players cost ~17k fine cells total instead of an uncapped 256k-512k per peer.

**What state-sync COSTS (be honest):**
- **Bandwidth stops being free.** Lockstep's inputs-only (<5 KB/s) becomes ~210-400 KB/s host upload. It FITS normal home internet, but only WITH delta + AoI + quantization all working, and per-client sits AT the 64 KB/s ceiling with no headroom. The **near-window radius (4m) and inside-cell-size (50cm) become load-bearing locks** — fixed like canon Fact-2, or E busts.
- **Migration is the biggest of any candidate (R20 ❌).** The BUILD-phase-hardened integer-lockstep grid — which this week's reshape *doubled down on* — is partly discarded: the integer determinism path goes away, a net-new Lagrangian cloud far-tier is added (the least-built layer), and lockstep netcode is replaced by state-replication + AoI plumbing the canon doesn't have. This requires an **owner-signed ADR-0010 un-lock** (`:12`). The fine-grid physics and the off-checksum bubble (`:33`) survive as E's near-window — that work is banked — but the determinism apparatus and netcode spine are rebuilt.

**Why E over the alternatives, defended:**
- **vs A/B:** A/B fit the wire for free but **structurally cannot do R7 or general R12** — the requirements the owner called the center of the design. No amount of CPU fixes a representation gap. B's near-cap makes it strictly worse than A on exactly these rows. They win only if the owner accepts "deep interaction in 2-3 pre-named rooms," which contradicts `:83`.
- **vs C:** C answers R7/R12 but loses crisp near-interaction (R6/R4) to blob-soft clouds and pays the same far-cloud-density cost without the grid's near precision. E keeps the grid exactly where precision is felt (under the player) and uses clouds exactly where position-without-crispness suffices (far).
- **vs D:** D **busts bandwidth** as a precise model (768 KB per hall snapshot) and inherits A/B's far-precision failures when degraded to fit. D's only path to viability is bounding the fine grid to an AoI window — which *is* E.

**The honest framing for the owner:** finishing the current grid (A, or A+sphere = B) is cheaper and ships sooner, but it buys a game where deep gas interaction is real only near a player or in a few hand-picked rooms. E costs a netcode paradigm switch and an ADR-0010 un-lock, but it is the only architecture that makes "deep gas interaction everywhere is the center" literally true at acceptable bandwidth. Given the owner said "this is the CENTER" and "we cannot mess this up," the precision requirement should drive the call — and it points at E.

## 6. WHAT STILL NEEDS AN OWNER DECISION OR A FOCUSED PROTOTYPE (≤3)

1. **OWNER DECISION — pay the ADR-0010 migration, or accept "precision only in 2-3 rooms"?** This is THE fork. E delivers R7/R12 everywhere at the cost of switching off lockstep and rebuilding the determinism/netcode spine (R20). B/A keep all banked work but can never do R7/R12 generically. No prototype resolves this — it is the owner weighing "deep interaction everywhere" (his stated CENTER) against migration cost. Everything else waits on this answer.

2. **PROTOTYPE — the cloud-density measurement (the single unproven number both C and E ride on).** Measure: how many clouds, at what radius, does it actually take to (a) gate an R7 reaction at true 50cm in an unoccupied room, and (b) hold an R12 exit-door split persistently? This is the cloud-tier sibling of the canon's hangar probe (`:134`). It decides whether E's bandwidth stays ~210-400 KB/s (FITS) or tips toward BUST, and whether host-CPU holds. **This is the prototype to run before committing.**

3. **OWNER DECISION + LOCK — fix E's two load-bearing constants like canon Fact-2:** near-window **radius (4m)** and **inside-cell-size (50cm)**. At 4m/50cm E fits with margin; at 8m or 25cm-inside it is ×8 and busts both bandwidth and host-CPU. Also confirm the **near/far seam discipline** (cloud↔grid conversion must conserve mass exactly via a host-side ledger — correct-if-coded, not free-by-construction like the integer grid). These must be ratified before build, not discovered during it.