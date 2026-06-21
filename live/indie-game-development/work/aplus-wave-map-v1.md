# A+ wave map — v1 (DRAFT input to the breakdown, completeness-swept)

> **Status:** DRAFT — input to the careful A+ BREAKDOWN (research + map). NOT the approved wave-tree (that is owner-approved
> card-by-card at the breakdown, G9). Produced by review s-review-002 follow-up + an adversarial **completeness sweep**
> (wf_7f1bfd63-262, 3 independent finders over the full design doc, the immutable source, and all OS state) run because the
> owner said «мне нельзя доверять, я могу пропустить». Verdict: **complete-with-gaps — дорога A+ NOT invalidated; the gaps are
> placement/specification fixes, folded below.** Sources: work/gas-model-design-full-2026-06-20.md (§A–§L) +
> work/gas-model-research-result-2026-06-20.md (immutable) + NOW.md decision_inbox.

## 1. Hardened wave map (fixes from the sweep folded in)

**Wave A — Lab + de-risk (sandbox + probe-gate).** Build the test sandbox (d-sandbox-001, R3 capability list) + run the
de-risk probes BEFORE any feature. Carries: §G's 7 probes + the review's +4 (sleep-set determinism on 2 machines;
resident-gas-damage RED; confirmed-colocation false-reaction; real-DA-at-hundreds-of-rooms). **FIXES:** (i) **host-migration
DESIGN PASS + «host dies → session survives» spike lands HERE, not Wave D** (it is an UNSOLVED open chunk that may constrain
the whole authority/replication model — finding it late = redo core = the R2 nightmare). (ii) §G#6 (high-hall slab-count
by-eye) and §G#7 (no-pop/shimmer on coarse↔detail crossfade) are **RENDER-dependent** — they ride the EXISTING GasDebug
overlay (debug overlay is allowed here, t-4 used one), NOT the secondary Track V. (iii) a **minimal cell-ceiling + round-robin**
is a prerequisite of its own §G#2 probe (can't probe "round-robin keeps truth fair under the ceiling" if neither exists).
(iv) **decide the active-gas-per-node cap + wire-plane budget = a CONCRETE NUMBER** (the [7,chunkCount] LOCK barrier has only
4 free plane-keys 2..5 before temperature at 6; a new plane = a SURFACED LOCK-EXT per ADR-0007) — this is the disciplined
answer to the owner's «free gas count» ask and must be decided before any wave assumes free species.

**Wave B — "Where is the gas" (topology + front + interest).** **FIXES:** (i) wire `RectDecomposition` to split big rooms
into convex sub-sectors — carry the §D.1 SEMANTIC: an intra-room cut = a PERMISSION "flows freely here", NOT a barrier (wiring
it as a flow-barrier is the classic bug); (ii) integer geodesic FRONT (§D.4) with an explicit **front-across-seam continuity**
acceptance (§G#3: front rounds the corner without a kink at the cut seams); (iii) interest-grain + hot/cold (§D.5) — **OWNER CORRECTION 2026-06-20: rarity is NOT a guaranteed
invariant — expect PEAKS (esp. chain reactions; he would NOT bet on "few").** So the requirement is GRACEFUL DEGRADATION
UNDER PEAKS, not "rare is guaranteed": a per-tick detailed-cell CEILING + a fair round-robin + degradation, and the awake-set
must be DETERMINISTIC (byte-identical who-is-awake + update order on 2 machines) **even during a spike** (ties to the Wave-A
sleep-determinism probe). Telemetry tracks the awake count; the peak-handling mechanism is the load-bearing part, not an
assumption that the count stays small;
(iv) the §D.8 **VISIBILITY-as-truth** half belongs here (host computes ONE shared detailed field, a cell is detailed if ANY
player is near) — it is a co-op/interest-grain + network-authority claim, exercised by the Wave-A 2-machine probe, NOT bundled
into Wave-C damage; (v) **return-fidelity is a BINDING Wave-B constraint here, not Track-V taste**: the front/coarse layer MUST
carry the TRANSIENT + front position + applied external events (d-returnfidelity-001's 4 cases incl. mid-transient return),
must NOT be architected as settled-only / room-totals, and source-XY must be supplied from upstream (d-corefoundation-001
keep-open). Real-DA at hundreds-of-rooms scale (today proven only at 6).

**Wave C — "Consequence" (laws + reactions).** Resident-gas DAMAGE (§D.6) **named with §E LAW #1 as a RED invariant** (dose
from RESIDENT gas, 0 if untouched; damage = a true committed past event, never redrawn) + the hook designed GENERAL (reused
for slippery-floor / interactive objects, not damage-only); one-truth player DAMAGE half (§D.8); reactions (§D.7) **named with
§E LAW #3 as a RED invariant** (irreversible reaction fires ONLY on confirmed co-location — coarse alone must NOT emit a false
reaction). **OWNER CORRECTION 2026-06-20:** at COARSE scale APPROXIMATE coincidence is enough (no fine-grain confirm needed
far from a player); NEAR the player (detailed) the mixing must be VISIBLE and the reaction **TELEGRAPHS** — gases blink/glow
"about to react" giving the player a **PREP WINDOW**, the irreversible reaction is **NOT instant**. Reaction COUNT is not
hard-limited: if more gases than the per-room budget co-locate, a **reaction QUEUE** processes them in order (see §4.2 RISK).
explosion = a mass-conserving TRANSFER (RED-test: any op changing total mass = a BUG not balance)
+ next-tick cascade (§D.9); **ventilation (§D.3) pinned to Wave C (not vague "later") with the §D.11 ⚠ invariant: forced-flow
is an integer edge-modifier on the SAME graph — NO imported/float vent solver (the doc's single most-emphasized determinism
landmine)**. Fire/ignition = later.

**Wave D — "Robustness" (destructibility + moving geometry).** Edge-based destructibility >1 breach (§D.10) — **Case A
(destruction OPENS: add/widen/toggle an edge) is distinct from Case B (a collapse SPLITS a room = a new barrier)**; Case B has
a **hidden Wave-B/generation prerequisite** (the generator must pre-nibble break-lines at generation — §D.1 topology data —
before Wave D can flick them closed); invariant: NO runtime geometry re-partition. **Moving geometry (elevators / blast-doors
closing on a gas column, §H) is an UNSOLVED open chunk** — needs a design pass + a mass-conservation-during-movement probe
BEFORE it is a task (a door closing mid-column must not create/destroy the bisected mass). Host-migration FULL impl (the
Wave-A spike informs the design).

**Track V — Visual GASG (∥, secondary, ~4 wk).** Big render research → visual language of types/meta-types (§I), reads the
FROZEN RN1 + the new front; ventilation-visual; fog without "shelves"/steps; readability (which gas / where danger / where
front). Gate visual IMPLEMENTATION on the read-seams being fixed (RN1 frozen ✓ + front), NOT on the core finishing. NOTE: the
GASG visual language is Track V, but "free number of gases" discipline (the wire cap) is a CORE Wave-A decision, not Track V.

## 2. Keep-open invariants (A+ reopens the LOCK — these must NOT be welded shut)

- **Per-SPECIES temperature** (d-crossband-inv-001 (3)/(5) Р2) — the named future seam for true cross-band inversion; temperature
  must stay an INDEPENDENT layer readable at any resolution on a committed revision, NEVER fused into the gas store. *(Was MISSING
  from the doc/§K/map — highest-risk silent drop the sweep caught.)*
- **Transient, not settled-only** (d-returnfidelity-001 + d-corefoundation-001) — the coarse/front layer carries the time-evolving
  picture + front + external events; source-XY recoverable upstream; no "1 sector per room" assumption baked in.
- **ROOM capacity + back-pressure = KEPT** (d-roomfull-001) — owner CONFIRMED 2026-06-20 he never asked to remove it (the
  s-work-016 «убрать ёмкость» note conflated it with the band-split; see §4 item 1). It is the visible face of pressure + feeds
  the door-break / vent-to-vacuum future seams; removing it = unbounded gas → perf death. The thing A+ DOES change is the
  **2-band fill-then-overflow split** (d-fillmodel-001) → weight+temp settling over more layers-as-data + fine grain (the owner's
  «continuous weight» ask; not literal float). Both finite + infinite sources stay supported.
- **Inter-layer read architecture** (d-tempfeedback-001) — grid-addressed read-model per layer on a committed revision; temp→gas
  feedback still DEFERRED (post-g-d3a8), but the seam must not be foreclosed.
- **Generator-agnostic seam** (d-generator-001) — DA(SGF) day-one, PGG later behind the SAME seam; population OUT.

## 3. §-coverage table (every doc chunk + relevant decision → wave)

| § / decision | item | wave | status |
|---|---|---|---|
| D.1 | level cut into convex sub-sectors at generation; cut = open-permission not barrier | A(seam)+B | partial-built → wire RectDecomposition |
| D.2 | "water" integer core (per-band/species, sill, mass-exact, find-level/drain/retreat) | — | BUILT (W1-2) |
| D.3 | buoyancy/temp/**ventilation** (forced-flow edge, no float solver ⚠) | C | temp BUILT; ventilation NEW |
| D.4 | integer geodesic FRONT (non-authoritative, mass=truth) | B | NEW |
| D.5 | interest-grain + sleep + hot/cold + **RARITY invariant** | B | NEW |
| D.6 | resident-gas DAMAGE law (§E.1) + general hook (slippery floor) | C | NEW |
| D.7 | reactions + cell-escalation + **false-reaction guard (§E.3)** | C | NEW |
| D.8 | player one-truth: DAMAGE (C) + **VISIBILITY/host-shared-field (B)** | B+C | NEW |
| D.9 | explosion = mass-conserving TRANSFER + next-tick cascade; fire later | C | NEW |
| D.10 | destructibility via edges: Case A opens (D) / Case B splits-room (needs B pre-cut) | B(pre-cut)+D | NEW |
| D.11 | determinism: integer Dijkstra+flow, no float authoritative (§E.2) | x-cut | BUILT/discipline |
| D.12 | MP 4-8: per-cluster bubbles; **ceiling+round-robin (prereq of §G#2)**; uplink-degradation policy | A/B | NEW |
| E.1/E.2/E.3 | 3 iron LAWS (resident-dose / no-float / confirmed-colocation) — named per-mechanism, NOT one line | A(probes)+C | E.2 built; E.1/E.3 NEW |
| G.1-7 | 7 probes (incl. **#6 slab-count + #7 no-shimmer = render-dependent → GasDebug overlay**) | A | NEW |
| +4 | review probes (sleep-determinism / resident-dose RED / false-reaction / real-DA-at-scale) | A | NEW |
| H | host-migration (**spike→A**, impl D) · moving-geometry (UNSOLVED, design+probe before D) · griefing (OPEN) · economy-many-sources (OPEN, twin of D.5 rarity) · believability-render (V) · save/load (still CUT/ephemeral) | A/D/OPEN/V | mixed |
| I | per-gas signature / slab count / fire timing / reconstruction TIGHTNESS (taste only) | V/later | deferred |
| J | A+ over B; capacity DE-CONFLATED (room-cap KEPT, band-split changes); gas-count RESOLVED (catalog ∞, ~16–32/level tunable, ~4/room + reaction queue) | A/B | RESOLVED §4 |

## 4. Owner-confirm items — RESOLVED 2026-06-20 (owner answers, s-review-002 thread)

1. **Capacity — RESOLVED: the original ask CONFLATED TWO different "capacities"; the owner never wanted room-capacity removed.**
   The s-work-016 redesign note lumped «убрать ёмкость+перелив / finite source» across BOTH d-fillmodel-001 and d-roomfull-001.
   De-conflated: **(A) the 2-BAND fill-then-overflow band-split** (d-fillmodel-001, how a sector's gas divides floor↔ceiling) =
   the thing the owner actually wants changed (= his «continuous weight → smoother height» ask → A+ replaces it with
   weight+temp-driven settling over MORE layers-as-data + the fine grain; NOT literal float — float breaks the net). **(B) the
   ROOM total capacity + back-pressure** (d-roomfull-001) = **KEPT** — the owner confirms he never asked to remove it; removing it
   = unbounded/oscillating gas → perf death, no benefit. Both finite + infinite sources stay supported. The «capacity» owner-confirm
   question was a FALSE question born of the conflation — closed.
2. **Gas count — RESOLVED (owner numbers):** catalog of TYPES = effectively UNLIMITED (data; «бесконечно» meant TYPES, not
   concurrent reactions). Per-LEVEL concurrent = a TUNABLE cap, owner estimate ~16, **max ~32**. Per-ROOM concurrent = typically
   **≤4** (bounded by the number of portals into a room) but **NOT guaranteed** — more could theoretically arrive. Encoding =
   SPARSE + TUNABLE (pay only for species actually present; the cap is a dial, NOT a hardcoded 4). Start with a working per-room
   number (~4) but see §4.2 RISK.
3. **Commercial footage edges — PARKED (owner R4 «парку, чтобы не вскрывалось»):** Wave 2 withdrew the storefront footage
   guarantee; g-5b07 #1 / g-2f8c #2 / root map_order edges are unsourced. Stay PARKED (storefront after visualization), carried as
   a noted-OPEN to the map, not silently dangling.

## 4.1 Owner clarifications folded into the waves (2026-06-20)

- **Reactions (Wave C):** coarse = approximate coincidence OK; near player = visible mixing + TELEGRAPH (blink/glow) + PREP WINDOW,
  not instant. (Folded into Wave C / §D.7 above.)
- **Rarity (Wave B):** NOT "rare guaranteed" — expect PEAKS (esp. chain reactions); requirement = graceful degradation under peaks
  + deterministic awake-set during a spike. (Folded into Wave B above.)
- **Capacity de-conflation:** room capacity KEPT; the 2-band split is what A+ changes (see §4.1 item 1 above and §2 keep-open).

## 4.2 RISK register (carry into the breakdown — owner: «как Рикс должен записывать это»)

- **R-GASCOUNT-PERROOM:** a room could receive MORE concurrent gas species than the chosen per-room budget (~4). Mitigation =
  a **reaction QUEUE / overflow strategy** (process in order), NOT a hard silent clamp. Start with ~4 but design the overflow
  path; do not assume ≤4 is guaranteed. (owner 2026-06-20)
- **R-PEAKLOAD:** the awake/detailed set can SPIKE (chain reactions); perf rests on graceful degradation (ceiling + round-robin)
  staying DETERMINISTIC under the spike, not on the set being small. (owner 2026-06-20)
- **R-AREA-ALWAYS (owner 2026-06-21, BINDING — CORRECTS the first draft):** opening AREA must ALWAYS affect flow — in BOTH the
  coarse AND detailed tiers (owner: «площадь должна ВСЕГДА влиять, вне зависимости грубая это симуляция или нет»). The current
  coarse orifice IGNORES area entirely (`CoarsePortal` has no area; `CoarseBandStep.Orifice` flow `t=mEq/kP` has NO area term) —
  WRONG in both tiers: a 25cm slit must flow far LESS than a barn door EVEN in coarse. `TopologyPortalSpec.OpeningSize` already
  carries it; it must ENTER the orifice flow law (flow area-scaled). The coarse tier may be LESS GRANULAR (by-layer, not per-cell)
  but the area-driven flow MAGNITUDE must match the detailed tier.
- **R-HEIGHT-DETAILED-REQUIRED (owner 2026-06-21, BINDING — CORRECTS my misread):** on the DETAILED tier height MUST be computed
  by REAL height, 100% — NOT by-layer (owner: «высоту надо высчитывать, на детальном это 100%»). The player must NOT see gas pass
  THROUGH a wall, and gas must exit through the ACTUAL opening at its ACTUAL height: a door HALF in the lower layer drains the
  lower layer; a small LOW hole must NOT leak gas via the UPPER layer (the by-layer rounding's failure the owner named). On the
  COARSE tier compute by height too IF it works out; **by-layer is a LAST-RESORT compromise ONLY for coarse, only if nothing better
  is found — NOT desired** — and it BREAKS on a hole spanning TWO layers (the likely-COMMON case) and on wrong-layer leakage.
  (CORRECTS the earlier R-HEIGHT-BY-LAYER-OK, which wrongly read the coarse-only fallback as the default for both tiers — my error.)
  Implication: 2 bands is INADEQUATE for detailed — the detailed tier needs real vertical resolution (the A+ continuous-weight /
  finer-grain model). A hole/door spanning two layers = an OPEN model-design question (how mass splits across the spanned heights).
- **R-NO-PROXIMITY-POP (owner 2026-06-21, FORBIDDEN 100% — the binding LOD invariant):** the gas flow through a given door/breach
  must NOT visibly change because the PLAYER moved nearer or farther (owner: «игрок отойдёт — замедляется, подходит —
  увеличивается… это запрещено 100%»). The coarse and detailed tiers must give ≈EQUAL area-driven flow for the same opening — the
  LOD transition is SEAMLESS, no pop. Coarse approximates by-layer (cheap), but the AGGREGATE flow MATCHES detailed. §G PROBE:
  drive the player across the coarse↔detailed boundary while gas flows through a door → the flow rate stays continuous (no
  speed-up on approach / slow-down on leaving).
- **R-BREACH-GRANULARITY (owner 2026-06-21):** today a breach opens a SIZE-BLIND 2-band portal → a 1-cell pinhole, 4 scattered
  holes, and a 50-cell blown wall ALL flow IDENTICALLY (binary open/closed, no area). Required (per R-AREA-ALWAYS +
  R-NO-PROXIMITY-POP + R-HEIGHT-DETAILED-REQUIRED): breach flow scales with the hole's AREA always; POSITION by REAL height on the
  DETAILED tier (a low hole drains low gas, a high hole vents high gas; by-layer is only a coarse last-resort and BREAKS on a
  two-layer hole); multiple scattered holes = multiple flow paths (sum of areas at their heights). Coarse may approximate but the
  area-driven flow MATCHES detailed (no proximity pop). The coarse↔detailed boundary for breach geometry = an A+ model-design question with the
  owner; a §G probe pins it.

## 4.3 MODEL FRAMING — there are NO fixed "bands"; real-height cells + per-gas buoyancy (owner 2026-06-21, BINDING)

The owner challenged the "layers/bands" concept and is RIGHT: fixed bands are NOT part of the model — they are ONLY the CURRENT
proven code's cheap coarsening (2 cells per room). The CORRECT model (the A+ direction, what d-fillmodel-001 / «continuous weight»
already points at):
- gas mass per species per INTEGER REAL-HEIGHT cell — a room is a STACK of height-cells, NOT 2 fixed layers;
- each gas has a BUOYANCY COEFFICIENT — a continuous tendency toward ceiling/floor (not binary heavy/light) that relaxes the gas
  toward its preferred height each tick (the coefficient sets HOW FAST/strongly it climbs or sinks);
- a door/opening connects the cells at its REAL height range → gas flows wherever it PHYSICALLY reaches the opening: a HIGH door
  passes heavy gas ONLY once it has filled up to that height («нижний газ верхушкой достаёт»); light gas that has risen to a door
  flows through; "дверь наполовину в слое" is a NON-question — the door simply spans whatever real-height cells it covers.
- "Bands" survive ONLY as a point on the LOD spectrum = the NUMBER of vertical cells (MANY near the player, FEW / 1–2 far). The
  2-band current model is the CHEAPEST coarse case, not the model itself.

WHY the coarse-LOD (fewer cells far) is NOT optional — the honest tension: cost + bit-exact 2-machine replication. Many cells ×
hundreds of rooms is unaffordable to replicate deterministically, so far rooms collapse to few cells. That collapse IS the
affordability mechanism AND the source of the R-NO-PROXIMITY-POP risk (the cell-count must change with NO visible flow change).
The water-like settle/rise PHYSICS is right; what was «грубо» is the SPACE / topology / DOOR discretization (the 2-band hack),
which A+ replaces with real-height cells + per-gas buoyancy + doors-by-real-height. So the model-design session designs THAT, with
the cell-count LOD as risk #1 (seamless net-determinism).

## 5. BOUNDARY — the one place the repo cannot verify

The original external research chat (ChatGPT) is NOT in the repo. The immutable source captures the STRUCTURE faithfully (3-audit
pass wf_c237a811), but the §5 physics thresholds (exact probe numbers) and §4 audit internals would only live in that chat. If
the owner wants those exact numbers, re-reading that chat is the one check neither the repo nor any agent can do. (For planning
the WAVES, the structure is sufficient; the numbers are config tuned later.)

## 6. Cross-wave / cross-track dependencies (the hidden ones the sweep caught)

- §G#2 (8 hot bubbles) needs the minimal **ceiling + round-robin** to exist first (Wave A/B).
- §G#6/#7 (render probes) need a **render readout** (GasDebug overlay in Wave A), not the secondary Track V.
- Wave D Case-B (room-splitting collapse) needs **Wave-B/generation pre-cut break-lines** first.
- Wave-B front-across-seam continuity (§G#3) is the join of RectDecomposition (B) + front (B).
- §D.5 rarity invariant ↔ §H "economy under many small sources" — the closed invariant (enforce in B) vs the open research (named OPEN).
- Track-V visual implementation gates on the read-seams (RN1 ✓ + front), not on core completion.

END_OF_FILE: live/indie-game-development/work/aplus-wave-map-v1.md
