# converge-g-37a1 — assembly surface

triage: heavy — converge ON — because model-bearing (a wrong stub defines the
product) and cross-cutting (it decomposes into simulation, legibility, air and
network subsystems).

status: CHECKPOINT, not complete. §GLOSSARY and §WHAT were not produced, because
the CONTENT of the node changed during the leg. See §9.

CONSUMED 2026-07-27 by s-map-g-37a1-digging-concept-001, which rewrote the card and
amended this artifact in four places. Read those amendments BEFORE the body they
correct: §6-BIS (the finding of §6 is misstated — "space you need" was never banned),
§4 (R18's ban half deleted; R19–R22 withdrawn with their numbers retired; R23–R27
added), §7's four first-hand corrections (the coarse solver cannot express digging;
cell size is a setting; graded conductivity already ships; the air socket is built —
plus the one unmeasured load-bearing claim), and §9's corrected census (nine
contradictions, not four, and one of the four was a phantom).

leg: s-converge-g-37a1-substance-passage-001 (2026-07-27, owner present)
call: work/c-converge-g-37a1-substance-passage-001-call.md

imported owner-approved decisions, born-closed:
- the five card laws of `g-37a1` (TREE.md done_when 2-6), approved 2026-07-27
- the two owner corrections of 2026-07-27: light-versus-heavy is a testing basis
  and not law; route direction is undecided
- the ~150-room figure as an explicit NON-target («мы за него не идём»)
- the done_when 2 / done_when 9 clarification of 2026-07-27

---

## 1. THE CONCEPT AS IT NOW STANDS

There is no path through the section. The crew **cuts its own path** through solid
ground, and the ground holds pockets of the substance.

The candidate objective is **RELOCATION, not traversal**: the section arrives
already flooded, and the job is to move what sits on the exit. This is NOT yet
approved — it changes the card's own goal sentence and belongs to `map`.

- The verb is digging.
- The skill is choosing **where to open relative to where the crew's exit is**.
- The counter is air.
- The crew rotates, because the digger is blind — he faces rock, stands in the
  substance and burns air fastest, and the thing that matters (where the released
  substance went) is behind him.

Occupancy is nearer 75% than a third, with places to catch breath. Two substance
kinds in the first section. No detection instrument in the first section.

---

## 2. THE FIVE SUBSTANCE LAWS — canon candidate, proposed to `review`

This leg does not write `knowledge/`. These do **not** belong in the card: a card
dies with its outcome and these must outlive it. Each carries its admission
ground — needed to build the first section, or already demonstrated in a build.

**Z1 CONSERVATION.** The substance is never created or destroyed, only relocated.
There are no sinks.
*Ground: already demonstrated.* Mass conservation is a hard invariant in the
shipped engine, enforced by exceptions, with a dedicated test file
`ScKernelAtomicityAndConservationTests.cs`. Sources exist; sinks do not.

**Z2 CONNECTIVITY.** The section is ONE connected volume: everything communicates
with everything, and any passage that lets a player through lets the substance
through. While a passage is open, it flows.
*Ground: needed.* Without it nothing emerges and route-around survives.

**Z3 BREATHING.** Air is spent always and at different rates in different
substances; there is no free place. Air is the ONLY counter the player tracks —
no second meter, no charge, no durability. Air can be handed to a teammate.
No masks: anything that cancels the cost of breathing cancels the game.
*Ground: needed.* It closes "wait it out".

**Z4 DRIVE.** The system never comes to rest. Differences move it, not added mass.
The total is fixed before the build and does not grow; sources are finite. A
director may change INPUTS — when, where, how much — but the substance is never
moved by a formula containing the player's position. *The director works the tap,
not the bucket.*
*Ground: needed.* A closed conservative system with no energy input dies at
equilibrium — which is exactly the deadness the owner felt on paper.

**Z5 ADMISSION.** An effect enters the game only if players can CREATE or BREAK it
by moving the substance. An effect that merely sits on the map is a zone, and the
simulation does not pay for itself.
*Ground: needed.* Otherwise the section is assembled from zones and proves nothing.

---

## 3. THE PLAYER-FACING LAWS — one clause, one owned verb

Form taken from Lethal Company, where every monster is one clause whose counter is
a verb the player already owns (Coil-Head cannot move while looked at → look;
Bracken angers while looked at → look briefly; Eyeless Dog hunts by sound →
crouch and be quiet). This form is the operational meaning of R10.

| LAW | COUNTER | TAUGHT BY |
|---|---|---|
| Where you cut, it comes to you | aim the cut | the small notch that starts seeping and grows while you stand in front of it |
| A light kind rises into the shaft above it | climb out now | digging down, opening a light pocket, finding your exit closed above you |
| Nothing leaves; anything you clear, you clear onto someone | look before you open | cracking the floor and finding a teammate under it |
| They only go off where both are thick, and nowhere is both thick unless you made it so | do not join two pockets | the first bang, at the cut where you joined them, leaving a coloured scar shaped like your mistake |
| A warned pocket stops if you thin it before the countdown ends | cut a relief hole | the bang you watched arrive and did nothing about |
| What you can see is what kills you; what you cannot see only costs air | look | walking into the visible kind once |
| Whoever faces the rock burns air fastest | swap | the digger nobody relieved, dying at the face while three watched |
| You cannot un-dig | cut somewhere else | the corridor you dug that flooded, and now you own it |
| You cannot get rid of it — you can only give it a better room, and it always takes the better room | dig the room before you open the wall | the room you gave it last time is the one you must now dig under |
| Aperture buys time, not safety: a narrow hole releases the same amount, slower | take one scoop, not two | it was already leaking and I took one more scoop |
| The blowout ignores gravity; the aftermath obeys it | wait two seconds before deciding which way to run | you ran uphill from a light kind because it was heading downhill when you looked |

**Note on the sixth.** The polarity is forced by the renderer, which stores only
the dominant type per cell. The intuitive "the invisible one is deadlier" is
arithmetically impossible to render honestly.

---

## 4. OWNER REQUIREMENTS, R1-R18

- **R1** Cell size (50 cm) was built for the previous concept; it may be recomputed.
- **R2** The simulation itself may change, up to a different state of matter. The
  term stays «вещество».
- **R3** 150 rooms is a number from nowhere and is not a target.
- **R4** The division into rooms is inherited; the geometry is undecided.
- **R5** The substance has a FINITE total.
- **R6** Size must follow from gameplay, not from feeling: no empty space, no fully
  flooded space, situations on the way from A to B.
- **R7** Rest stops load the next scene. *(Corrected in-leg: PEAK does not do this —
  see §7. The decision stands as his, the justification does not.)*
- **R8** He leans toward procedural generation with modules and a branch choice at
  rest stops.
- **R9** The physics need not be accurate. It must be a LAW, not a script.
- **R10** Players must understand the law after their FIRST failure.
- **R11** Occupancy nearer 75% than a third, with places to catch breath.
- **R12** The old canon assumed the simulation would supply gameplay by itself.
  That assumption is withdrawn.
- **R13** "The substance does not seek the player" is an old-canon law and may be
  rewritten.
- **R14** Route direction stays undecided; up was only an example.
- **R15** Negative effects first; positive ones (floating, lift) later.
- **R16** Understanding the game beats hitting the date. Try to hit it, but
  understanding wins.
- **R17** Legibility through the GROUND: the soil reads differently near a pocket.
  Constraint: the stain must be a MARK, not a store — it holds and releases nothing,
  or it becomes a sink and breaks Z1.
- **R18** *(ban half DELETED 2026-07-27 by the owner — «R18 надо удалить, оно
  невалидно», aimed at the economy ban; the permission and the placement survive
  after he was shown the entry's three parts.)* Tools and upgrades are not excluded
  from the concept. Upgrades belong **between** sections, because earning and
  spending are only possible there. ~~Banned: a second counter, and an
  inventory/crafting/economy layer.~~ — superseded by R26.
- **R19–R22 WITHDRAWN 2026-07-27, numbers retired and never reused.** They were this
  session's transcription of the owner's in-session brainstorm (a finite oxygen hose;
  pockets large enough that detours cost time; value hidden in a pocket; a reaction
  seeping from an opened pocket). He refused them as requirements: «это не
  требование, это просто первое, что пришло в голову, я даже особо не размышлял над
  этим». They remain ideas on the table with no authority, weighed on the same
  footing as any other candidate.
- **R23** The one-way law is CUT. «возвращаемся назад, естественно возвращаемся. Это
  должно быть убрано.» Now that the crew digs, going back is natural; the rule was
  authored by him earlier the same day under the walk-through concept, where the
  route always went upward.
- **R24** Every recorded law is under skepticism and is re-examined one at a time,
  because the concept changed twice in days and the record holds leftovers: «сейчас
  какие-то есть законы, ко всем относимся тогда со скепсисом… у нас какой-то микс
  произошёл». Air was named specifically: «также, кстати, с воздухом. Это у нас
  раньше было, сейчас, возможно, стоит и пересмотреть.»
- **R25** His own vision gets NO priority: «не надо моё видение ставить каким-то
  приоритетным». The answer that is right outranks the answer that is his.
- **R26** The bar for any additional mechanic: first how hard it is to implement, then
  what profit it gives. «Она должна давать невероятный профит. Не чуть-чуть, не
  немножко, а прям чёткий, понятный профит. Только тогда её берём.» A mechanic that
  is merely somewhat better is REJECTED. This is now the sole guard where the deleted
  bans used to stand — loot and economy are not banned and enter only through it.
- **R27** The network basis is NOT deferred: co-op follows the first playable core
  immediately, and from then on the whole game is built on it. «Это 100%.» Ground:
  recorded research that developers who deferred netcode paid disproportionately to
  retrofit it. The core must start both alone and with a partner on a second machine.

---

## 5. OWNER VERDICTS TAKEN IN THIS LEG

| id | question | verdict |
|---|---|---|
| B4 | reading of «преследователь» | CONFIRMED — motion computed from the player's position is forbidden; timers, finite sources, heating and physical rise are legal |
| B5 | the three "no free" laws | ACCEPTED as the basis |
| B6 | connectivity and drive; director on the tap | ACCEPTED |
| B7 | reference class = Barotrauma, not PEAK | ACCEPTED |
| B8 | section 3000-4000 m³ | ACCEPTED as a starting number, explicitly **not** as law |
| B9 | the verb | superseded by digging |
| B10 | two substance kinds | ACCEPTED |
| B11 | **is the air counter visible** | **OPEN — surfaced twice, not auto-decided** |
| B12 | no detection instrument in the first section | ACCEPTED; legibility carried by the look of the substance |
| B13 | the substance IS the space, ~75% | ACCEPTED as direction |

The digging pivot is his: «а что если у нас нужно как бы прокопать себе путь, но
можно вскопнуть условно карман с газом». The rejection of authored breach panels is
his: «с панелями меня не очень привлекает» — because a panel removes the player's
authorship of WHERE, and with it the sense that the mistake was his.

---

## 6. THE FINDING THAT OUTRANKS THE REST — **MISSTATED. See §6-BIS.**

**There is no reason to open a pocket.** Reached independently by three adversaries;
missed by both the owner and the session.

Every shipped dig-into-hazard game supplies a reason — ore behind it, space you
need, the liquid is a resource. This direction has banned all three. So the crew
wants only distance, every cut into a pocket is pure downside, and:

- with a readable ground, the optimal play is to route around every pocket forever;
- with an unreadable ground, every breach is luck.

There is no third state. All five developed proposals patched it with the same
sentence — "the corridor MUST go through the pocket" — which is the authored breach
panel the owner already killed, relabelled.

**THE ANSWER, reached independently by two agents: make the objective RELOCATION
rather than traversal.** The section arrives already flooded and the job is to move
what sits on the exit. This simultaneously supplies the reason to touch the
substance, kills "waiting is optimal", and gives the blind digger a live clock.

It is UNTESTED, and it changes the card's goal sentence. Owner's, in `map`.

---

## 6-BIS. THE CORRECTION — added 2026-07-27 by s-map-g-37a1-digging-concept-001

**The finding above is wrong as stated, and the error is a bookkeeping one.** Verified
first-hand by two blind strands and confirmed by a third: **"space you need" was never
banned by anything in this direction.** The actual ban lists are `done_when` 9 (art
beyond the cheapest, level generation, economy, progression, monsters, combat, story,
and substance-versus-loose-object physics), `done_when` 2's cargo clause, and R18's
deleted half. Space is in none of them — and `done_when` 2 names «пройти сквозь него»
as one of three player verbs under the owner's own `да`. One of the three horns was
scored as banned by association, and that error is what produced the finding.

**THE REASON, recorded by the owner on 2026-07-27 and costing no new mechanic:** rock
costs time, time costs air, and **a pocket is open space nobody had to cut**, sold at
the price of breathing in it. Going around a pocket of diameter *d* costs roughly
*πd/2* of extra rock; crossing costs *d* of walking at a higher air rate. One number
decides it, and the same number makes the two kinds mean genuinely different things —
one is a road, the other a wall — which is what `done_when` 5 exists to make visible.
Two conditions travel with it: the ground mark must GRADE with pocket size, not merely
signal presence, or a breach still reads as luck; and the per-kind air-rate gap must be
about an order of magnitude, or the substance decays into what Z5 itself calls a zone.

**REFUSED by the owner, on merit:** RELOCATION (§6's own answer — the price three
adversaries demanded was finally supplied and it convicts rather than acquits; it also
restores the un-abandonable place he himself identified as the Oxygen Not Included
defect); the hunt for breath; and the cleanup objective, which was his own signed
wording in the now-archived concept frame. **REFUSED on arithmetic, not authorship:**
the hose family — a hard length budget on a readable ground either leaves a
pocket-free route feasible, so route-around wins, or leaves exactly one feasible
route, which is the authored breach panel computed instead of placed, and worse,
because the player cannot see it to resent it.

**ACCEPTED FOR A LATER ITERATION, not rejected** («стоит взять на вооружение, но это
как бы не в первой итерации»): rock as a slow valve; air in the ground; the substance
as the excavator; and his own extension of the second — air as a separate gas whose
pockets you open in order to breathe.

**His own doubt, recorded so a playtest settles it and not an argument:** the accepted
reason may be too static — one trade repeated. The analysis named the same weakness
independently.

---

## 7. MEASURED ENGINEERING FACTS

Read first-hand from `C:\projects\Unity\GasCoopGame` at commit `1a6373b8`
(main and dev identical).

- Substance cells **50 cm**, structure cells **25 cm**, both hardcoded in
  `VoxelResolution.Default`; there is no setting. 1 m³ = 8 substance cells.
- Throughput **~2.2 million substance-bearing cells per second**, single-threaded,
  on the owner's Ryzen 9 7950X3D, in a **headless .NET harness — not in Unity**.
  Three independent captures agree: flooded hangar 196,608 cells at 74-89 ms;
  TYPICAL 2,934 active at 0.58-1.32 ms; sparse hangar 1,562 active at 0.27-0.35 ms.
  A weak peer is 2-4x slower and, under lockstep, sets the ceiling for everyone.
- **Empty volume is nearly free.** The same 196,608 cells cost 0.3 ms with 1,562
  active and 89 ms with all active. **CPU is paid by SUBSTANCE, not by SPACE.**
- Per-species signed buoyancy exists and works, applied as a per-Z-face bias, so
  mixtures **stratify**. The steady state is a layered profile, not grey soup, and
  it re-forms in roughly 20-45 s after full mixing — provided the two kinds carry
  **opposite** signed weight.
- An impulse register exists (face footprint, direction, strength, time-to-live);
  its own comment names "an eruption burst, a vent toggle, a body shove; a
  sustained vent = a large TTL".
- A reaction engine exists with data-driven rules, a per-cell "telegraph" warning
  state, and reaction-driven pressure shoves.
- A temperature layer exists but substances have **no per-species temperature** —
  an open seam.
- 128 types supported, 12 co-resident per cell, **only the dominant type per cell
  is visible**.
- Networking is **input lockstep**: substance state never goes over the wire, every
  peer simulates identically, the substance costs zero bandwidth.

### Three corrections of this session's own claims

1. **Memory, wrong by ~200x in the owner's favour.** The measured 1,745 B/cell is a
   per-FACE cost wearing per-cell clothing (384 B per open face; 579,584 open faces
   in that capture). Solid rock has no open faces and no mass. As a 2-bit occupancy
   field the pre-allocated box costs **0.25 B/cell — 16 KB for a 64,000-cell box**,
   not 110 MB. The box stops being a budget line at all.
2. **"Difficulty grows because clean places run out" does not follow** from a fixed
   total with no sinks. The substance redistributes; it does not accumulate where
   the players are. The owner refuted this and was right.
3. **Card law 2 was over-applied.** It forbids substance motion computed from the
   player's position. It does not forbid timers, finite sources, heating or physical
   rise. The owner caught this and was right.

### The decisive engineering fact

The current flow term is **concentration diffusion**, which DILUTES rather than
displaces, and therefore **cannot express a pocket that spurts under pressure and
then subsides**. The impulse register can make it look right, but an impulse
register is a hand-placed script — which Z5 and the owner's own test reject.

**Fix: capacity-limited cells with flux driven by overfill rather than
concentration.** Same loop, same conservation, same integer carry, different
numerator. Then a pocket bursts by itself, accelerates as the notch is widened, and
subsides as it empties. "There is time to run" becomes a consequence, not a promise.

### Levers, ranked

1. **Substance cell size, cubic.** 50→75 cm is 3.4x, 50→100 cm is 8x. Decoupling
   the dig grid (25 cm) from the substance grid (75-100 cm) costs no dig fidelity
   and hands over **graded conductivity for free** — a small notch is literally a
   small-area face. **Cell size must become a setting, not a constant.**
2. **Co-residency.** The tick is memory-bandwidth bound, moving ~483 MB per tick at
   12 types per cell. Cutting to 2 is an estimated 3-6x. **Estimate, not a
   measurement — and the cheapest measurement available.**
3. Quiescence deadband: 10-100x in the common case, **0x in the worst case**, and
   the worst case sets the budget.

### The pre-allocated occupancy box

Sound. Allocate the whole section box including rock; every cell flagged SOLID or
OPEN; digging flips a flag. It is a **storage rewrite, not a patch**: ~600-900 lines
plus dependents, 4-6 days, plus 2-3 days regenerating determinism goldens. It also
deletes the Dictionary and CSR index from the hot loop — **the most common desync
cause in this class of game**.

### The unresolved contradiction that matters most

A **coarse per-room band solver already exists** in the repository: accepted,
gate-passed, with the owner's own legibility verdict recorded as PASS. Runtime-
mutable sector graph with portals that open and close; sealed sectors accumulate
surplus and release nothing until a portal opens; interface heights derived;
replication proven bit-exact **across a topology change**; **1.06 ms worst case at
3,136 sectors**. It reproduces all three of the owner's images.

One agent would retire it as dead weight; another states it already IS the game.
**Until the expensive per-cell model is measured against THAT control rather than
against a straw-man script, the owner's own test does not acquit it.**

The owner's position, recorded: the old code belongs to the old concept and may be
discarded freely; the grid should be adapted to the new concept straight away. The
reconciliation offered and accepted in-leg: the difference between "cheap" and
"expensive" is mostly **cell size**, not two codebases — so build the new substrate
at a coarse cell size, with the size as a setting.

### FOUR CORRECTIONS TO THIS SECTION — 2026-07-27, read first-hand at commit `1a6373b8`

**Recorded as EVIDENCE ONLY and deliberately not acted on.** The owner ruled in the map
leg that technical decisions belong in technical chats: «технические решения сейчас не
особо хочу обсуждать и хочу, чтобы они были четко проверены уже именно в технических
чатах. То есть мы сейчас пишем требования, что должно быть без привязки к нашей
технической реализации.» Three of the four lower the price.

1. **The unresolved contradiction above is SETTLED, and no measurement can acquit the
   coarse solver.** `CoarseBreachLayer` validates every breach at enqueue against a
   *pre-declared, not-yet-materialized* breach surface, and `CoarseSectorGraph` builds
   breachable surfaces *pre-declared as latent portals*. It can only breach where a
   level author said it may — so under a concept where the player authors WHERE, the
   coarse solver is not "already the game": it is a gate-passed, bit-exact
   implementation of **the authored breach panel the owner rejected**. The comparison
   §7 demanded ("cheap versus expensive") is the wrong axis. The owner's recorded
   instinct that the old code belongs to the old concept is right for a reason nobody
   in the converge had established.
2. **Cell size is NOT hardcoded.** `VoxelResolution` is a parameterized pair
   (geometry, gas) whose default is (25, 50) and whose own doc names (25, 100) as a
   configuration, bounded by a maximum sub-face count. So the top-ranked performance
   lever — 3.4× at 75 cm, 8× at 100 cm — is a call-site sweep plus regenerated
   goldens, not a rewrite. §7's "hardcoded, there is no setting" overstates it.
3. **Graded conductivity ALREADY SHIPS.** `SubFaceOccupancy` stores a 25 cm sub-face
   open bitmask per gas cell-face; `StructureGasProjection.Conductivity(occ) =>
   occ.OpenCount` is written into `FaceState.Conductivity` and multiplied by the flow
   kernel. "A small notch is literally a small-area face" and "aperture buys time, not
   safety" are built at author time. Only **runtime mutation** of the bitmask is
   missing — and `VoxelField.NotifyConductivityChanged` **throws** on a face that is
   not already OPEN, which is precisely the seam a dig verb must break.
4. **The air counter is a consumer on an accepted socket, not a new subsystem.**
   Per-actor, per-kind, integer exposure and committed dose ship in `PlayerSense`, with
   an actor-pose round-trip proven byte-identical over the network in a recorded gate.
   What remains is a rate table, one monotone reserve, a hand-off command and a death
   predicate.

**What STANDS unchanged, and it is the fact that matters most:** nothing a player does
moves the substance, and no scene has ever contained a *controlled* player and the
substance together. The existing capsule is an owner-eye, auto-swept debug transform.

**And one claim in this section is UNMEASURED and load-bearing — see the issue
`i-flow-model-unmeasured`.** That an overfill numerator yields a legible, seconds-scale
burst-and-subside is asserted, not measured. The in-repo proof cited for it is false:
the coarse orifice **equalises density** and its own comment makes the overfull state
unreachable. The real capacity-fill-plus-overflow code is in a different step that
nobody read, and its receiving side is **uncapped by explicit design** — the opposite of
the back-pressure required. Derivation from constants frozen in code says the *current*
model is orders of magnitude too slow, and nothing shows that changing the numerator
changes the **timescale** rather than only the endpoint. Two independent strands priced
the measurement at about **one day in the existing headless harness** and neither ran
it. It belongs before any build commitment.

---

## 8. THE REACTIONS ANSWER

**Transport alone does not collapse.** Diffusion is driven by difference and
vanishes at uniform; buoyancy is driven by mass and does not. The steady state is a
layered profile that re-forms after mixing.

**With reactions at wall-to-wall fill it collapses catastrophically**: the entire
reagent stock burns in about eight ticks — under half a second — at level load.

**The concentration THRESHOLD is the only available separator, and it is
sufficient.** Set it above the highest quiet co-resident level and the undisturbed
section never fires. This also makes **every reaction player-caused by
construction**, with no player position in any formula.

Under digging, geometric separation returns as well: with rock between two pockets
the mixed area is exactly zero, and **the aperture is the rate valve, held by the
players**.

Add, all free in existing code: **finite reagent** (a hard event ceiling), an
**inert product** (and since only the dominant type renders, it leaves a visible
scar shaped like what the players did), and **self-extinguishing**.

**One number controls it: the gap between the firing threshold and the quiet level.**
Above zero, the section never self-ignites. Above 256, a bang cannot light its
neighbours and a global cascade becomes inexpressible. Below twice the fan strength,
a player can still reach it.

These constants are **derived from code and not measured**. Two headless gates of
about half a day each settle them: a QUIET test (10,000 ticks, zero input, assert
zero fires) and a CHAIN test (force one cell, assert bounded spread).

---

## 9. WHY THIS LEG IS A CHECKPOINT

The converge was chartered against a card that no longer describes the game.

- §GLOSSARY was mined (the term net covers «вещество», «участок», «проход»,
  «обнаружить», «переместить», «воздух», «различимо на глаз» and twelve more, with
  competing readings and twelve on-disk contradictions) but **not signed**, because
  the terms that matter most changed meaning during the session.
- §WHAT was **not produced**. Coverage against the current card would be meaningless
  because the card is being replaced.

The leg spent its budget on the layer beneath §WHAT: what the game is.

### The four contradictions inside the approved card, handed to `map`

1. «проходят участок насквозь» — versus the candidate objective of relocation.
2. «всё, что делает игрок, направлено на вещество» — versus digging, which is aimed
   at the rock.
3. **done_when 7**, «доля объёма, занятого веществом ... по ходу не растут» —
   digging violates this by construction, because cutting grows the open volume.
4. The ban on tools with their own mechanics — lifted by the owner (R18).

### THE CENSUS WAS WRONG — corrected 2026-07-27 by s-map-g-37a1-digging-concept-001

**Nine contradictions were verified, not four, and one of the four was a phantom.**

Item 4 above is **largely a PHANTOM against the card as written**: no clause of the
card ever banned tool mechanics. R18 lifted a reading, not a ban.

The five the census missed:

5. `done_when` 4's one-way law — cut by the owner in the map leg (R23). It was not an
   inherited leftover: he authored it himself earlier the same day, and he removed his
   own rule.
6. `done_when` 6's air-as-the-only-counter — put under review by the owner (R24) and
   then softened: the word «единственный» leaves the card, the rule survives as one we
   hold but never use to reject a working idea.
7. `done_when` 3 carried the broad old-canon phrasing while the owner had already
   supplied the narrow operative form (B4: no motion computed from the player's
   position). Only the narrow form is a criterion.
8. `done_when` 8's latency clause aimed at a vanished subject — moved to `g-5e8c`,
   where the network venue actually lives.
9. `g-5e8c` `done_when` 5 banned «экономика» and «прогрессия» while R18 places
   upgrades between sections, which is exactly that node's territory. Both bans are
   removed and the rest-stop upgrade criterion is added.

Also removed from `g-5e8c` `done_when` 5: «второй объект», which had no referent
anywhere in live state.

**A methodological note worth more than the census.** A thirty-one-item drift sweep was
run against the whole of live state; its own independent adversary refuted **nineteen**
of its verdicts on receipts. The nine above are what survived. No future leg should take
a drift sweep at face value without the adversarial pass — and the same discipline
caught two of this leg's own claims before the owner acted on them.

---

## 10. PARKED — technical, not owner-content, not decided here

- **Cell or column.** Per-cell (as now) versus a per-region height field. The height
  field is 3-8x cheaper, gives an exact flat surface — the most legible thing
  obtainable at zero art — and makes pressure native; it loses mixtures, plumes and
  per-cell reactions, and the owner's third image (a light kind rising through a
  flooded shaft) is its hard case. **The two paths do not compose.**
- **Is air a modelled species?** The largest evidence hole found: five independent
  developments never answered it, and without an answer the word "pressure" has no
  referent. If modelled, it buys back-pressure, trapped bubbles and the diving bell —
  named as the only mechanic a script cannot reach at all.
- **Two players or four in the first section.** Every showcase loop collapsed under
  counting: three of four supply about ten seconds of input across the best thirty
  seconds, and the shared-air advantage is 1.8x, not 4x. Evidence favours designing
  for two and proving four later.
- **The price of "dig the drain first".** Converged on by all five angles as the
  expert move, and identified by three adversaries as a laundered sink: void
  generation outpaces hazard by an order of magnitude. **No agent supplied a price
  that survives.**
- **Backfilling must be dropped** — a de-facto sink, a free risk-free probe, and it
  costs fully dynamic connectivity.
- **The renderer cannot currently tell a weep from a flood.** Dominance flips
  cell-to-cell so any interface strobes, and a cell holding a trace renders as
  100% that kind. Every hero frame depends on a surface the current flow model and
  renderer cannot produce.
- **Cheapest legibility channels at zero art**, in order: extinction distance (one
  kind visible to ~12 m, the other to ~1.5 m); emission versus pure absorption (in
  the dark, one is a lamp and the other a hole); a hard straight interface (nothing
  in a cave is straight, so a level surface reads as deliberate); colour last, chosen
  for value contrast in greyscale. **Two kinds is the honest ceiling.**
- **Air as the lamp** — range shrinks as air runs down, and a hand-off makes a
  teammate visibly brighter. A diegetic meter at zero art cost.

---

## 11. THE THREE PROBLEMS DIGGING DOES NOT FIX BY ITSELF

1. **The blind digger is a tax, not a gate.** Nothing stops stepping back, looking,
   and returning. It becomes a gate only if the cut **worsens while unattended** —
   which is the owner's own image (a notch that seeps and grows) promoted from
   anecdote to law.
2. **Waiting stays optimal** once a pocket equalises. The growing seep is the only
   clean forcing function found; the relocation objective (§6) removes the problem
   at the root, because the substance is already moving at t=0.
3. **The failure unit is maximal.** One way plus a closed exit is a team wipe, while
   the precedent says chaotic systems teach only through modest losses. The
   conventional softener — a downed state with a bleedout timer — is **barred by Z3's
   single-counter rule**. Best answer offered: make the signature death "the exit
   exists and costs more air than you have", recoverable by a teammate.

---

## 12. PRECEDENT FINDINGS THAT CHANGED DECISIONS

- **PEAK does not load between segments.** The whole mountain is one continuous
  resident scene; the Scout Cannon glitch flies from the beach to the summit in one
  unbroken physics trajectory. The campfire is a fog gate, a 25 m regroup point, a
  safe room, and (since March 2026) an autosave — never a loader.
- **PEAK does not generate maps on the player's machine.** Aggro Crab's studio head,
  GDC 2026: the daily map "started as a design constraint as we actually couldn't
  generate these maps on the player's end at runtime". Fourteen maps baked in the
  Editor, patched every two weeks, forever.
- **PEAK has no branching route choice.** The biome order is fixed; the two variable
  slots rotate by day, identically for every player on Earth.
- **PEAK is not big.** 1200 Unity units of vertical across six biomes; the whole game
  installs in 4-6 GB; it plays 60-120 minutes because **climbing is expensive**.
  Duration comes from the cost of movement, not the size of the space. Team of 7,
  under $200,000, core in about four weeks, 11 million copies at under $5.
- **A Game About Digging A Hole:** one person, ~14 days of design work, licensed
  assets, $4.99, 250k copies in week one, a million by August 2025. The publisher
  attributes it to **the hook** — 140,000 wishlists against a target of 10,000, a
  TikTok trailer at 5 million views. It runs on a viral hook, an upgrade treadmill, a
  mystery at the bottom, and two hours at five dollars solo. This project bans the
  treadmill and is not a two-hour impulse buy. **What transfers is the hook and the
  mystery.**
- **Every shipped "dig and drain a hazard" game cheats with a SINK** — Terraria
  converts liquid to obsidian, Minecraft deletes lava under a placed block, Oxygen
  Not Included pumps gas into a reservoir. Z1 forbids all three. **There is no
  shipped precedent for the exact mechanic proposed.**
- **Oxygen Not Included** is the nearest shipped implementation of the owner's own
  image and still produces "the game is forcing me" rather than "I made a mistake".
  The owner refuted the transfer correctly: ONI has a permanent BASE that cannot be
  abandoned; a passage has none — you survive it and leave.
- **SteamWorld Dig**, lead designer on first playtests: given a free dig verb, testers
  dug straight down and defeated the level design; the fix was a whole new traversal
  system.
- **Deep Rock Galactic** built the terrain technology FIRST and treated it as the gate
  on whether the game was possible; then pulled authorial control back from free-form
  generation because unrestricted space fought the gameplay.
- **Minecraft's "you dug into lava"** reads as the player's mistake because the hazard
  emits a free, continuous, pre-contact signal through the material — and stops
  reading as a mistake the moment a placed block silences it.
- **Minecraft's break feedback contract**, four parts, all free at zero art: legible
  progress, predictable duration, continuous sound, discrete termination with a
  reward object. Material-distinct **sound** carries more than graphics.
- **Lethal Company:** every monster is one clause whose counter is a verb the player
  already owns. This is the operational form of R10 and it is why one death teaches.

---

## 13. BUILD ORDER — for `shape` to cut into tasks, not this leg

1. **Occupancy substrate.** The whole box pre-allocated including rock; every cell
   flagged solid or open; digging flips a flag; **cell size becomes a setting**;
   the Dictionary and CSR index leave the hot loop; the topology edit becomes a
   canonically ordered command inside the tick phase order.
2. **A man digs a hole and walks into it.** Nothing else — no substance, no air.
   **This is the first thing that has never existed** and the fastest visible result.
3. **Substance driven by overfill, not concentration.** Capacity-limited cells,
   signed buoyancy, quiescence deadband, coarse substance grid, authored
   over-pressure pockets. **This is the footage** — a man cuts a notch, it bursts,
   he does not get out.
4. **Air.** One counter, rate by local mix, hand-off, death.
5. **Legibility.** Two kinds distinguishable at a glance, in the dark; the stranger
   test on stills.
6. **Lockstep for real.** Canonical command bus, strict phase order, an O(active)
   rolling checksum, snapshot join.
7. **The section.**

A Steam page needs a capsule and twenty seconds of step 3 — **not a finished
section**. That is how the 2026-08-31 gate survives a slip of 2026-08-07.

---

## 14. THE LEGIBILITY ACCEPTANCE TEST (mechanism, not an owner fork)

Frames from the build, shuffled, shown for **five seconds** each; a person outside
development names in their own words what they see; the developer says nothing.

**FAIL** if that person gives two different substances **the same word**, or one
substance **two different words** within the sitting. Correct names are irrelevant —
"the green one" and "the sparkly one" used consistently is a PASS.

The frame set and the pass rule are committed to the repository **before** the
sitting, so they cannot be adjusted afterwards. Known weakness: stills are easier
than live play, so three-to-four-second silent clips join the same deck.

The light condition is part of the test: if the game is dark and has a flashlight,
the test runs under that light, not under studio lighting.

---

END_OF_FILE: live/indie-game-development/work/converge-g-37a1.md
