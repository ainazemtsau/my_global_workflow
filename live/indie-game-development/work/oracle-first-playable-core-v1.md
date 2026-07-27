# Oracle: node class «first playable core of a simulation-bearing cooperative game»

status: CANDIDATE. Authored 2026-07-27 by `s-converge-verify-g-37a1-digging-card-001`
because `converge-verify` step 2 requires a node-class decision checklist and
`live/indie-game-development/knowledge/` holds none — an empty oracle BLOCKS the leg.
PROPOSED for promotion by `review` or `pulse`. It has no authority until promoted, and
it was authored from first principles and external precedent BEFORE the attack, never
derived from the artifact it was used against.

node class: the outcome that turns a paper concept into a build the author plays daily,
where the simulation model itself is the product risk.

---

## PART A — the fourteen decision classes

Each is a NAME, what it decides, and the test «what breaks if it is unanswered».
Every class is checkable against a spec by someone who did not write the spec.

1. **SUBSTRATE UNIT AND TICK.** What exactly is simulated, the quantum of space one
   unit occupies, what one unit may hold at once, and the quantum of TIME one update
   advances. *Breaks:* no data structure, no budget, and no claim about how fast
   anything happens can be checked — «seconds-scale» is not a number until a tick is.
   *Precedent:* Oxygen Not Included fixes one substance per tile with no partial
   pressures, and that one choice produces both its impassable-CO₂ behaviour and its
   tile-flicker cost. Noita's unit is one PIXEL in 64×64 chunks with per-chunk dirty
   rects. Barotrauma's unit is a HULL — a room volume, not a cell. Minecraft's unit is
   a 1 m block carrying an integer fluid level 0-7.
2. **CONSERVATION, SOURCES, SINKS AND DRIVE.** Whether the quantity is conserved,
   which sources and sinks are legal, and what keeps the system out of equilibrium
   without referencing the player. *Breaks:* a bug is indistinguishable from a rule;
   «drain the hazard» is either impossible or free; a closed conservative system
   settles and stops being content. *Precedent:* Minecraft is deliberately
   non-conservative — a source block never depletes.
3. **PLAYER VERB FOOTPRINT.** What the verb touches, at what granularity relative to
   the sim unit, at what rate, with what feedback contract (progress, duration,
   termination). *Breaks:* no input path exists; the world's mutability at the sim's
   own unit is untested; the verb's feel is discovered after the storage is frozen.
4. **EMBODIMENT AND TRAVERSAL OF A SELF-AUTHORED VOID.** What the body is, how it
   collides with a field the player mutates, and how it moves through a void of its
   own making — including back out of it. *Breaks:* the first runnable thing cannot
   run; the «man» has nothing to stand on and no way home, and every answer (climb,
   rope, lift) is a new mechanic arriving after the budget is spent.
5. **THE COUNTER, ITS RATE LAW AND ITS FAILURE STATE.** The single tracked quantity,
   what changes its rate, what happens at zero, whether zero is recoverable.
   *Breaks:* nothing is at risk, so no choice costs anything and the simulation is
   scenery. *Precedent:* Barotrauma's oxygen is a property of the SPACE, not of the
   avatar — per-hull volume, flowing through gaps, consumed per breather.
6. **OBSERVABILITY CHANNEL AND ITS ACCEPTANCE TEST.** How a person who did not build
   it reads the sim's state, in which channel, and by what pre-registered test
   pass/fail is judged. *Breaks:* the model cannot be judged at all; every playtest
   verdict becomes a verdict on the renderer and the author's own knowledge silently
   supplies the missing legibility.
7. **AUTHORITY AND REPLICATION OF A MUTABLE WORLD.** Who owns world state, how a
   topology edit is ordered canonically, how peers agree, how a late peer obtains the
   world. *Breaks:* co-op becomes retrofit-only and the first divergence has no
   diagnosis. *Precedent:* Teardown shipped full voxel destruction years before
   multiplayer and its author names destruction-plus-networking as the hard hurdle.
8. **FALSIFICATION EXPERIMENT AND ITS PRICE.** Which single measurement would show
   the model wrong, in which harness, at what cost, before which commitment.
   *Breaks:* model risk is found by the owner in play, weeks after the storage froze.
9. **THE CONTROL MODEL.** Which cheaper model is the explicit control, and on which
   axis the expensive one must beat it. *Breaks:* «it must be really simulated» is
   unfalsifiable and the expensive model is built on faith. *Precedent:* two of the
   three nearest shipped comparables ARE the cheap control — Barotrauma's per-hull
   volumes and ONI's one-substance tiles both shipped.
10. **THE FIRST RUNNABLE THING AND ITS VENUE.** The smallest end-to-end runnable
    artifact, HOW it is produced (packaged? in-editor?), how it is launched, by whom.
    *Breaks:* «playable» has no referent; an Editor scene is not a thing an author
    enters on an arbitrary day, and packaging cost is discovered at the end.
11. **THE EXPERIMENT INSTRUMENT.** How conditions are changed, restarted and compared
    WITHOUT the authoring tools, and where the parameters live. *Breaks:* tuning is a
    code edit, only the author can tune, and no comparison is reproducible.
12. **RUN LIFECYCLE AND IRREVERSIBILITY.** What a run is, what ends it, what resets,
    what persists across launches, what state exists after total failure — in a world
    that can only be consumed. *Breaks:* repeated play either starts in yesterday's
    wreckage or silently discards it, and «repeat launch works» cannot be tested
    because nobody said what it should produce.
13. **THE EXPLICIT NON-MODEL AND ITS SEAM.** What is deliberately NOT simulated, and
    what happens at the boundary where the excluded thing meets the modelled thing.
    *Breaks:* scope grows by discovery, and the first object that touches the
    substance forces an unbudgeted decision mid-build.
14. **EXIT CRITERION AND VERDICT AUTHORITY.** Who declares the core done, on what
    evidence, and where «not good enough» routes. *Breaks:* the node becomes a
    permanent laboratory — this direction's own named failure mode (`g-12fd`).

---

## PART B — verdict per class against `work/converge-g-37a1.md`

The artifact is a CHECKPOINT: §GLOSSARY unsigned, §WHAT never produced (its own header
lines 7-8), so no class has a §WHAT row and coverage was judged on substantive
treatment anywhere in the file.

| # | class | verdict | locator |
|---|---|---|---|
| 1 | substrate unit and tick | space ANSWERED-then-PARKED; TIME never decided | §7:276, §7:328-331, §7:383-387, §10:511-515; §8:426-427 and §7:286-287 both presuppose a tick rate nowhere named |
| 2 | conservation, sources, sinks, drive | RAISED as a canon candidate, with live defects tracked | §2 Z1, §2 Z4, §10:528-529; `i-substance-laws-canon-candidate` |
| 3 | player verb footprint | RAISED, under-decided (rate, reach, feedback open) | §13:611-614, §7:388-394, §12:601-603 |
| 4 | **embodiment and traversal** | **NEVER RAISED** | — |
| 5 | counter, rate law, failure state | RAISED and routed | §2 Z3, §13:621, §11:553-558, `d-air-counter-visibility-001` |
| 6 | observability and its acceptance test | RAISED — the artifact's strongest section | §14:633-647, §10:530-538 |
| 7 | authority and replication | RAISED in unusual detail for a pre-shape artifact | §7:296-298, §13:611-614, §13:624-625, §4 R27 |
| 8 | falsification experiment and its price | RAISED, including its own refutation | §7:405-415, §8:446-448 |
| 9 | the control model | RAISED and then SETTLED without measurement | §7:346-357 then §7:373-382; residual at §10:511-515 |
| 10 | **first runnable thing and its VENUE** | thing answered; **VENUE NEVER RAISED** | §13:615-616 only |
| 11 | **the experiment instrument** | **NEVER RAISED** | — |
| 12 | **run lifecycle and irreversibility** | **NEVER RAISED** | — |
| 13 | the explicit non-model and its seam | RAISED | card done_when 10, §10:528-529, §2 Z5, §4 R26 |
| 14 | exit criterion and verdict authority | RAISED | card done_when 11, §13:626 |

**SCORE: ten of fourteen raised (two of them parked by design), four never raised —
and all four are on the same side of the artifact: everything between the simulation
and the man who is supposed to play it daily.**

---

## PART C — sourcing ledger

SOURCED this session by external search: ONI one-substance-per-tile and its
consequences; Noita per-pixel automata, 64×64 chunks, dirty rects (GDC 2019);
Barotrauma hull-volume water and per-hull oxygen through gaps at a fixed per-breather
rate; Minecraft fluid levels 0-7 with 7-block horizontal spread and infinite downward
flow; Teardown's 1-byte voxel materials and multiplayer as a later hurdle.

UNSOURCED and therefore carrying NO weight in this oracle, though the artifact cites
several of them: Deep Rock Galactic's terrain tech as an explicit go/no-go gate;
Teardown's 10 cm voxel size; Dwarf Fortress 7/7 water levels; the SteamWorld Dig
playtest anecdote; the Terraria/ONI sink claims. No class in PART A depends on an
unsourced claim for its existence.

END_OF_FILE: live/indie-game-development/work/oracle-first-playable-core-v1.md
