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
acceptance (§G#3: front rounds the corner without a kink at the cut seams); (iii) interest-grain + hot/cold (§D.5) WITH the
**RARITY INVARIANT** as an explicit acceptance/telemetry (non-sleeping node count stays under a ceiling AND the awake-set is
byte-identical on 2 machines — ties to the Wave-A sleep-determinism probe; this is the perf-economy guard, not a feature);
(iv) the §D.8 **VISIBILITY-as-truth** half belongs here (host computes ONE shared detailed field, a cell is detailed if ANY
player is near) — it is a co-op/interest-grain + network-authority claim, exercised by the Wave-A 2-machine probe, NOT bundled
into Wave-C damage; (v) **return-fidelity is a BINDING Wave-B constraint here, not Track-V taste**: the front/coarse layer MUST
carry the TRANSIENT + front position + applied external events (d-returnfidelity-001's 4 cases incl. mid-transient return),
must NOT be architected as settled-only / room-totals, and source-XY must be supplied from upstream (d-corefoundation-001
keep-open). Real-DA at hundreds-of-rooms scale (today proven only at 6).

**Wave C — "Consequence" (laws + reactions).** Resident-gas DAMAGE (§D.6) **named with §E LAW #1 as a RED invariant** (dose
from RESIDENT gas, 0 if untouched; damage = a true committed past event, never redrawn) + the hook designed GENERAL (reused
for slippery-floor / interactive objects, not damage-only); one-truth player DAMAGE half (§D.8); reactions (§D.7) **named with
§E LAW #3 as a RED invariant** (irreversible reaction fires ONLY on confirmed co-location at fine grain — coarse alone must
NOT emit a false reaction); explosion = a mass-conserving TRANSFER (RED-test: any op changing total mass = a BUG not balance)
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
- **Capacity + overflow = the visible face of real pressure** (§J) — the owner's literal «убрать ёмкость+перелив / finite source»
  is REINTERPRETED, not granted: capacity is KEPT (it feeds d-roomfull-001's named door-break / vent-to-vacuum seams + the
  "threat doesn't self-vent" intent), removed only WITH a replacement law. Both finite + infinite sources stay supported.
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
| J | A+ over B; capacity REINTERPRET; gas-count DISCIPLINE (cap+wire) | A/B + owner-confirm | see §4 |

## 4. Owner-confirm items (surface — his decision, do not silently resolve)

1. **«Убрать ёмкость + перелив / finite source»** — the analysis REINTERPRETS this (capacity = the visible face of real pressure,
   kept; removed only with a replacement law; both source types kept). This is the owner's OWN redesign trigger being resolved
   against his literal words → he must SEE it and agree (or push back).
2. **Active-gas-per-node cap + wire-plane budget = a concrete NUMBER** — the disciplined answer to «free gas count». Needs an
   owner-aware decision (how many active gases per node / on the wire) because it touches the LOCK ceiling.
3. **Commercial footage edges** — Wave 2 withdrew the storefront footage guarantee; g-5b07 #1 / g-2f8c #2 / root map_order edges
   are now unsourced. R4 = «storefront later», so these stay parked, but the broken edges must be carried (route to the map),
   not silently left dangling.

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
