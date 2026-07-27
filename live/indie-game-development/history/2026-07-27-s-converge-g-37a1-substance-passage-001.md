# RESULT s-converge-g-37a1-substance-passage-001

direction: indie-game-development
play: converge
node: g-37a1
call: c-converge-g-37a1-substance-passage-001
date: 2026-07-27
status: checkpoint

## outcome

`triage: heavy — converge ON — because model-bearing (a wrong stub defines the
product) and cross-cutting (it decomposes into simulation, legibility, air and
network subsystems).`

The leg did NOT complete its done_when and must not be recorded as if it had.
§GLOSSARY and §WHAT were not produced. The reason is not a failure of procedure:
the CONTENT of the node changed under the leg. The card this converge was chartered
against — «двое-четверо подключённых игроков проходят собранный руками участок
насквозь через вещество» — no longer describes the game the owner wants. A converge
cannot lock a WHAT against a card that is about to be rewritten.

What the leg produced instead is the material for that rewrite, all of it
owner-present and owner-signed: a five-law foundation for the substance, a set of
player-facing laws in a form that teaches after one failure, eighteen recorded owner
requirements, measured engineering facts, and four named contradictions inside the
approved card.

**THE CONCEPT AS IT NOW STANDS.** There is no path through the section. The crew
CUTS its own path through solid ground, and the ground holds pockets of the
substance. The candidate objective is RELOCATION, not traversal: the section arrives
already flooded and the job is to move what sits on the exit. The verb is digging;
the skill is choosing where to open relative to where the crew's exit is; the counter
is air; the crew rotates because the digger is blind and burns air fastest.

## evidence

**OWNER PRESENCE.** The whole leg ran with the owner present. Every law, requirement
and fork below is either his words or a proposal he accepted, edited or killed.
Nothing here was chosen by an agent alone.

**OWNER VERDICTS.**

- B4 CONFIRMED — «преследователь» means substance motion computed from the player's
  position; timers, finite sources, heating and physical rise are legal. His words:
  «вопрос 4 подтверждаю».
- B5 ACCEPTED — the three "no free" laws (cannot remove, cannot bypass, cannot wait).
  His words: «вопрос 5, да, принимаю как основу».
- B6 ACCEPTED — connectivity and drive; the director works the tap, not the bucket.
  His words: «вопросы закона связанности и привода принимаю».
- B7 ACCEPTED — the reference class is Barotrauma, not PEAK; from PEAK only "movement
  is expensive". His words: «вопросом согласен».
- B8 ACCEPTED as a STARTING NUMBER and explicitly NOT as law: section 3000–4000 m³.
  His words: «в закон 100% не брать».
- B10 ACCEPTED — two substance kinds in the first section.
- B12 ACCEPTED — no detection instrument in the first section; legibility is carried
  by the look of the substance instead. His words: «я тоже сейчас бы, наверное, не
  делал прибор».
- B13 ACCEPTED as direction — the substance IS the space, ~75% occupancy with places
  to catch breath. His words: «с заполненным веществом уже что-то ... тут как бы
  становится понятнее».
- B11 NOT ANSWERED and left open — whether the air counter is visible.
- The digging pivot is his: «а что если у нас нужно как бы прокопать себе путь, но
  можно вскопнуть условно карман с газом».
- The rejection of authored breach panels is his: «с панелями меня не очень
  привлекает» — because a panel takes away the player's authorship of WHERE.

**OWNER REQUIREMENTS R1–R18.** R1 cell size was built for the previous concept and
may be recomputed. R2 the simulation itself may change, up to a different state of
matter; the term stays «вещество». R3 150 rooms is a number from nowhere and is not a
target. R4 the division into rooms is inherited and the geometry is undecided. R5 the
substance has a FINITE total. R6 size must follow from gameplay, not from feeling: no
empty space, no fully flooded space, situations on the way from A to B. R7 rest stops
load the next scene. R8 he leans toward procedural generation with modules and a
branch choice at rest stops. R9 the physics need not be accurate; it must be a LAW,
not a script. R10 players must understand the law after their FIRST failure. R11
occupancy nearer 75% than a third. R12 the old canon assumed the simulation would
supply gameplay by itself; that assumption is withdrawn. R13 "the substance does not
seek the player" is an old-canon law and may be rewritten. R14 route direction stays
undecided; up was only an example. R15 negative effects first, positive ones later.
R16 understanding the game beats hitting the date; try to hit it, but understanding
wins. R17 legibility through the GROUND: the soil reads differently near a pocket —
with the constraint that the stain must be a MARK and not a store, or it becomes a
sink and breaks Z1. R18 tools and upgrades are not excluded from the concept; what
stays banned is a second counter and an inventory/crafting/economy layer, and
upgrades belong between sections.

**THE FIVE SUBSTANCE LAWS**, proposed as a canon candidate for `review`. This leg
does not write `knowledge/`. Full text with admission grounds in
`work/converge-g-37a1.md` §2.

- Z1 CONSERVATION — never created or destroyed, only relocated; no sinks. Ground:
  already demonstrated in the build (hard invariant, exceptions, dedicated test file
  `ScKernelAtomicityAndConservationTests.cs`; sources exist, sinks do not).
- Z2 CONNECTIVITY — one connected volume; any passage that passes a player passes the
  substance; while open, it flows. Ground: needed, or route-around survives.
- Z3 BREATHING — air spent always at different rates; air is the ONLY counter; it can
  be handed over; no masks. Ground: needed, it closes "wait it out".
- Z4 DRIVE — differences move it, not added mass; total fixed before the build;
  sources finite; a director may change inputs but never move the substance by a
  formula containing the player's position. Ground: needed, or the closed system dies
  at equilibrium.
- Z5 ADMISSION — an effect enters only if players can create or break it. Ground:
  needed, or the section is assembled from zones and proves nothing.

**THE PLAYER-FACING LAWS**, in the Lethal Company one-clause-plus-owned-verb form
(Coil-Head cannot move while looked at → look; Bracken angers while looked at → look
briefly; Eyeless Dog hunts by sound → crouch and be quiet). This form is why one
death teaches, and it is the operational meaning of R10. Eleven laws, tabulated in
`work/converge-g-37a1.md` §3. The most load-bearing:

- Where you cut, it comes to you. COUNTER: aim the cut.
- A light kind rises into the shaft above it. COUNTER: climb out now.
- Nothing leaves; anything you clear, you clear onto someone. COUNTER: look before
  you open.
- Whoever faces the rock burns air fastest. COUNTER: swap.
- What you can see is what kills you; what you cannot see only costs air. COUNTER:
  look. NOTE: this polarity is forced by the renderer, which stores only the dominant
  type per cell; the intuitive "the invisible one is deadlier" is arithmetically
  impossible to render honestly.

**THE FINDING THAT OUTRANKS THE REST**, produced by three independent adversaries and
missed by both the owner and the session: **THERE IS NO REASON TO OPEN A POCKET.**
Every shipped dig-into-hazard game supplies one — ore behind it, space you need, the
liquid is a resource — and this direction has banned all three. With a readable ground
the optimal play is to route around every pocket forever; with an unreadable ground
every breach is luck. There is no third state. All five developed proposals patched it
with the same sentence — "the corridor MUST go through the pocket" — which is the
authored breach panel the owner already killed, relabelled.

**THE ANSWER**, reached independently by two agents: make the objective RELOCATION
rather than traversal. The section arrives already flooded and the job is to move what
sits on the exit. This simultaneously supplies the reason to touch the substance,
kills "waiting is optimal", and gives the blind digger a live clock. It is UNTESTED
and it changes the card's own goal sentence, so it is the owner's to approve in `map`,
not this leg's to adopt.

**MEASURED ENGINEERING FACTS**, read first-hand from the product repository at commit
`1a6373b8` (main and dev identical). Full detail in `work/converge-g-37a1.md` §7.

- Substance cells 50 cm, structure cells 25 cm, both hardcoded in
  `VoxelResolution.Default`; there is no setting. 1 m³ = 8 substance cells.
- Throughput ~2.2 million substance-bearing cells per second, single-threaded, on the
  owner's Ryzen 9 7950X3D, in a headless .NET harness — NOT in Unity. Three
  independent captures agree. A weak peer is 2–4× slower and, under lockstep, sets the
  ceiling for everyone.
- Empty volume is nearly free: the same 196,608 cells cost 0.3 ms with 1,562 active
  and 89 ms with all active. **CPU is paid by SUBSTANCE, not by SPACE.**
- CORRECTION 1, mine, by a factor of about 200 in the owner's favour: the measured
  1,745 bytes per cell is a per-FACE cost wearing per-cell clothing. Solid rock has no
  open faces and no mass. As a 2-bit occupancy field the pre-allocated box costs
  0.25 B/cell — 16 KB for a 64,000-cell box, not 110 MB. The box stops being a budget
  line at all.
- CORRECTION 2, mine: "difficulty grows because clean places run out" does not follow
  from a fixed total with no sinks. The owner refuted this and was right.
- CORRECTION 3, mine: I over-applied card law 2. It forbids substance motion computed
  from the player's position, not timers, finite sources, heating or physical rise.
  The owner caught this and was right.
- **THE DECISIVE ENGINEERING FACT:** the current flow term is concentration diffusion,
  which DILUTES rather than displaces and therefore cannot express the owner's first
  image — a notch that spurts under pressure and then subsides. The impulse register
  can make it look right, but an impulse register is a hand-placed script, which Z5 and
  the owner's own test reject. Fix: capacity-limited cells with flux driven by overfill
  rather than concentration. Same loop, same conservation, same integer carry,
  different numerator.
- The pre-allocated occupancy box with dig-as-flag-flip is SOUND. A storage rewrite,
  not a patch: ~600–900 lines plus dependents, 4–6 days, plus 2–3 days regenerating
  determinism goldens. It also deletes the Dictionary and CSR index from the hot loop —
  the most common desync cause in this class.
- Biggest cost lever, cubic: substance cell size. 50→75 cm is 3.4×, 50→100 cm is 8×.
  Decoupling the dig grid (25 cm) from the substance grid (75–100 cm) costs no dig
  fidelity and hands over graded conductivity for free, so a small notch is literally a
  small-area face. **Cell size must become a setting, not a constant.**
- Second lever, unmeasured and cheap to measure: the tick is memory-bandwidth bound,
  moving ~483 MB per tick at 12 co-resident types per cell; cutting to 2 is an
  estimated 3–6×.
- Cell-versus-column dominates cost. A per-region height field is 3–8× cheaper, gives
  an exact flat surface — the most legible thing obtainable at zero art — and makes
  pressure native; it loses mixtures, plumes and per-cell reactions, and the owner's
  third image is its hard case. The two paths do not compose.
- Nothing gameplay-side exists: no scene has ever contained both a player and the
  substance; nothing a player does moves the substance; there is no oxygen, breathing
  or hand-off; two substances have never been rendered simultaneously; opening a door
  re-voxelizes the whole level.
- **A working COARSE per-room band solver already exists in the repository** —
  accepted, gate-passed, with the owner's own legibility verdict recorded as PASS:
  runtime-mutable sector graph with portals that open and close, sealed sectors that
  accumulate surplus and release nothing until a portal opens, derived interface
  heights, replication proven bit-exact ACROSS a topology change, 1.06 ms worst case at
  3,136 sectors. It reproduces all three of the owner's images. One agent would retire
  it; another states it already IS the game. **Until the expensive per-cell model is
  measured against THAT control rather than against a straw-man script, the owner's own
  test does not acquit it.** The owner's position is recorded: the old code belongs to
  the old concept and may be discarded freely, and the grid should be adapted to the new
  concept straight away. The reconciliation accepted in-leg: the difference between
  cheap and expensive is mostly CELL SIZE, not two codebases — so build the new
  substrate coarse, with the size as a setting.

**THE REACTIONS ANSWER.** Transport alone does not collapse: diffusion is driven by
difference and vanishes at uniform, buoyancy is driven by mass and does not, so the
steady state is a layered profile that re-forms in roughly 20–45 s after full mixing,
provided the two kinds carry opposite signed weight. WITH reactions at wall-to-wall
fill it collapses catastrophically: the entire reagent stock burns in about eight
ticks, under half a second, at level load. The concentration THRESHOLD is the only
available separator and it is sufficient: set it above the highest quiet co-resident
level and the undisturbed section never fires, which also makes every reaction
player-caused BY CONSTRUCTION with no player position in any formula. Under digging,
geometric separation returns as well: with rock between two pockets the mixed area is
exactly zero, and the aperture is the rate valve the players hold. Add finite reagent,
an inert product (which, since only the dominant type renders, leaves a visible scar
shaped like what the players did), and self-extinguishing. One number controls it: the
gap between the firing threshold and the quiet level — above zero it never
self-ignites, above 256 a bang cannot light its neighbours and a global cascade becomes
inexpressible, below twice the fan strength a player can still reach it. **These
constants are derived from code and NOT measured**; two headless gates of about half a
day settle them.

**PRECEDENT FINDINGS THAT CHANGED DECISIONS.** Full list in
`work/converge-g-37a1.md` §12. The ones that moved a decision:

- **PEAK does NOT load between segments.** One continuous resident scene; the Scout
  Cannon glitch flies from the beach to the summit in one unbroken physics trajectory.
  The campfire is a fog gate, a 25 m regroup point, a safe room and (since March 2026)
  an autosave — never a loader. The owner's R7 decision had been made on the opposite
  belief; the decision stands as his, the justification does not.
- **PEAK does not generate maps on the player's machine.** Aggro Crab's studio head at
  GDC 2026: the daily map "started as a design constraint as we actually couldn't
  generate these maps on the player's end at runtime". Fourteen maps baked in the
  Editor, patched every two weeks, forever.
- **PEAK has no branching route choice**; the two variable biome slots rotate by day,
  identically for every player.
- **PEAK is not big.** 1200 Unity units of vertical across six biomes, installing in
  4–6 GB, playing 60–120 minutes because CLIMBING IS EXPENSIVE. Duration comes from the
  cost of movement, not the size of the space. Team of 7, under $200,000, core in about
  four weeks, 11 million copies at under $5.
- **A Game About Digging A Hole:** one person, ~14 days of design work, licensed assets,
  $4.99, 250k copies in week one and a million by August 2025. The publisher attributes
  it to THE HOOK — 140,000 wishlists against a target of 10,000. It runs on a viral
  hook, an upgrade treadmill, a mystery at the bottom, and two hours at five dollars
  solo. This project bans the treadmill and is not a two-hour impulse buy; **what
  transfers is the hook and the mystery.**
- **Every shipped "dig and drain a hazard" game cheats with a SINK** — Terraria converts
  liquid to obsidian, Minecraft deletes lava under a placed block, ONI pumps gas into a
  reservoir. Z1 forbids all three. There is no shipped precedent for the exact mechanic
  proposed.
- **Oxygen Not Included** is the nearest shipped implementation of the owner's own image
  and still produces "the game is forcing me" rather than "I made a mistake". The owner
  refuted the transfer correctly: ONI has a permanent BASE that cannot be abandoned; a
  passage has none — you survive it and leave.
- **SteamWorld Dig:** given a free dig verb, testers dug straight down and defeated the
  level design; the fix was a whole new traversal system.
- **Deep Rock Galactic** built the terrain technology FIRST and treated it as the gate on
  whether the game was possible, then pulled authorial control back from free-form
  generation because unrestricted space fought the gameplay.
- **Minecraft's "you dug into lava"** reads as the player's mistake because the hazard
  emits a free, continuous, pre-contact signal through the material — and stops reading
  as a mistake the moment a placed block silences it.

**WHAT SIX INDEPENDENT SKILL-LAYER PROPOSALS PRODUCED**, before digging: all six were
killed by their own adversaries, for two recurring reasons — a script could fake it,
because each reduced the substance to one number per room; and a hand-built section is
memorised by run three. Digging repairs both, because the players author the topology
at runtime. Mechanisms that survived and get STRONGER under digging: "nothing leaves";
a pre-sorted start with players as the only mixer; the seam as the only live surface,
so mixing area equals excavation area; breathing rate as a function of the local mix
sampled at head and foot, audio only; the substance as the only light source; the wall
stain as a record; death as the probe; and — a large engineering gain — digging removes
the deterministic player-body-affects-substance subsystem from the critical path,
replacing it with runtime cell-solidity mutation.

**THREE PROBLEMS DIGGING DOES NOT FIX BY ITSELF**, all still open: the blind digger is
a tax and not a gate unless the cut worsens while unattended; waiting stays optimal
once a pocket equalises; and the failure unit is now maximal — one way plus a closed
exit is a team wipe, while the precedent says chaotic systems teach only through modest
losses, and the conventional softener (a downed state with a bleedout timer) is barred
by Z3's single-counter rule.

## state_changes

`live/indie-game-development/work/converge-g-37a1.md`
- Create. The full assembly surface: triage header, the concept as it now stands, the
  five substance laws as a canon candidate with admission grounds, the player-facing
  laws in one-clause form, R1–R18, the owner verdicts with B11 open, the measured
  engineering facts and the three corrections, the reactions answer, the precedent
  findings, the four card contradictions handed to `map`, the parked technical
  questions, the build order, and the legibility acceptance test.

`live/indie-game-development/work/c-map-g-37a1-digging-concept-001-call.md`
- Create. The continuation CALL.

`live/indie-game-development/NOW.md`
- `updated: 2026-07-27 by s-converge-g-37a1-substance-passage-001`.
- Prepend a `direction_forecast` driver recording the digging pivot, the relocation
  objective as owner-pending, the five laws, R16, and the pointer to the artifact.
- Mark `i-substance-passage-open-questions` superseded in part and append the state
  after the checkpoint: what is answered, what is still open (split into technical and
  owner-content), and what is dropped.
- Add `i-card-contradicts-digging` naming the four contradictions, routed to `map`.
- Add decision `d-air-counter-visibility-001`, unanswered, not auto-decided.
- Replace the open call: `c-converge-g-37a1-substance-passage-001` out,
  `c-map-g-37a1-digging-concept-001` in. Exactly one continuation.
- Preserve `bet: null`, `tasks: []`, `recurring: []`, forecast `no_basis`, every other
  issue.

`live/indie-game-development/LOG.md`
- Prepend this leg's line once.

`live/indie-game-development/history/`
- Save this full RESULT as `2026-07-27-s-converge-g-37a1-substance-passage-001.md`.

## captures

- The owner's own refutation that beat mine: the Oxygen Not Included complaint is about
  a permanent BASE that cannot be abandoned; a passage has no base, so the flooded
  corridor is a place to leave, not a problem to fix.
- Duration is bought with the cost of movement, not the size of the space. PEAK turns
  1200 vertical units into ninety minutes because climbing is expensive. Metres are the
  last resort, not the first.
- A card must never become the design document. `g-12fd` died of exactly that.
- The owner's own estimate correction: his delays come from concept changes, not from
  writing code; with clear requirements and two strong models, implementation is much
  faster than a human-hours estimate. So spend effort where the concept stops moving,
  not on architecture polish.
- Worth a bounded research question later: whether the coarse per-room solver already in
  the repository is enough to carry the game, measured against the per-cell model on the
  same playable section.
- Minecraft's break-feedback contract, free at zero art: legible progress, predictable
  duration, continuous sound, discrete termination with a reward object — and
  material-distinct sound carries more than graphics.

## decisions_needed

- id: d-air-counter-visibility-001
  question: Is the air counter visible, and how?
  options: a diegetic gauge on the canister visible on yourself and a teammate; nothing
    at all, carried by breathing and gasping; a bar on screen.
  recommendation: the diegetic gauge, because "no interface" then holds literally on the
    five Steam screenshots and a teammate's state stays readable, without which handing
    air over is blind.
  status: open, surfaced twice, not auto-decided.

## play_check

- `imported: [the five card laws born-closed; the two owner corrections of 2026-07-27;
  the ~150-room figure as an explicit non-target; the done_when 2/9 clarification]`
- Step 1 Triage and import: done. `heavy — converge ON`, recorded.
- Step 2 Define: NOT completed. The miner ran and produced the term net — «вещество»,
  «участок», «проход», «обнаружить», «переместить», «воздух», «различимо на глаз» and
  twelve more, with competing readings and twelve on-disk contradictions — but
  §GLOSSARY was not signed, because the terms that matter most changed meaning during
  the session.
- Step 3 Resolve: NOT completed. No §WHAT list exists. The leg spent its budget on the
  layer beneath §WHAT: what the game is.
- Step 4 Close and route: done as a CHECKPOINT. No executor CALL emitted. No build, no
  shape, no bet, no tasks, no tracks, no product or Steam mutation, no repository
  created or changed. Level generation left to `g-5e8c`. `knowledge/` not written. The
  2026-08-07 boundary not moved by this leg — its fate is handed to `map` as an owner
  decision under R16.
- `converge_coverage`: NOT complete, and deliberately not claimed. Coverage against the
  current card is meaningless because the card is being replaced.
- `canon_proposed: [Z1–Z5, the five substance laws, as a candidate for review]`
- G7: every owner fork was surfaced; B11 remains open and was not auto-decided.
- Owner-verdict guard respected: no owner-content decision was taken by the session.
  Digging, the rejection of panels, the 75% occupancy, the two kinds, no instrument, and
  the priority of understanding over the date are all his.
- Fan-out: the play mandates a miner and `strategic_search` children. Run: one glossary
  miner, one product-evidence miner, two research children, then two workflows totalling
  twenty-six agents (six skill-layer proposals each with an independent adversary, a
  precedent strand, a reactions strand, five digging developments each with an
  adversary, a genre strand and an architecture strand), plus two compression passes.
  All in-session pre-passes; the binding G5 review is a separate fresh chat and is not
  claimed here.
- Two process notes, recorded rather than hidden. First, the session crashed twice and
  background work was lost; the workflow was resumed from its run id and the killed
  agent from its transcript, and nothing was silently dropped. Second, this leg
  contradicted its own earlier statements three times — the "fewer clean places"
  argument, the over-broad reading of card law 2, and a memory figure wrong by a factor
  of two hundred. Each was corrected in-session, twice by the owner and once by an
  adversary. That is the gate working, not the gate failing.

## log

g-37a1/converge-checkpoint: the converge could not lock a WHAT because the node's content changed under it — the owner replaced the concept a second time and the approved card no longer describes the game; the crew no longer walks through a section filled with substance, it CUTS its own path through solid ground into pockets of it, and the candidate objective becomes RELOCATION rather than traversal after three independent adversaries found the hole nobody had seen (there is no reason to open a pocket, because every shipped dig-into-hazard game supplies one — ore, space, a resource — and this direction banned all three, so a readable ground means route around forever and an unreadable ground means every breach is luck); five substance laws are signed and proposed as a canon candidate (conservation with no sinks, one connected volume where any passage for a player is a passage for the substance, breathing everywhere at different rates with air as the only counter, drive by differences and never by a formula containing the player's position, and admission only for effects players can create or break), eleven player-facing laws are written in the Lethal Company one-clause-plus-owned-verb form that the owner adopted as the operational meaning of «understand it after the first failure», and eighteen owner requirements are recorded including R16 (understanding the game now outranks the 2026-08-07 date) and R18 (tools and upgrades are no longer excluded, while a second counter and an inventory layer stay banned); measured engineering facts are attached with three of the session's own claims corrected first-hand — the box memory estimate was wrong by two hundred times in the owner's favour, «clean places run out» does not follow from conservation, and card law 2 forbids only motion computed from the player's position — the decisive one being that concentration diffusion cannot express a pocket that spurts under pressure, so the flow term must be driven by overfill instead; the reactions worry is answered by a concentration threshold that makes every reaction player-caused by construction; an already accepted coarse per-room solver in the product repo is flagged as an unresolved control that the expensive per-cell model has never been measured against; and the leg closes as a checkpoint routing to `map` to rewrite g-37a1 and g-5e8c with the owner's verdict on exact text, with the air-counter fork left open and the technical set parked.

## next

CALL `c-map-g-37a1-digging-concept-001` — full text in
`work/c-map-g-37a1-digging-concept-001-call.md`.

to: session · direction: indie-game-development · play: map · node: g-37a1 (with a
consequential edit to g-5e8c) · budget: one owner-present session · surface: a FRESH
chat with the owner present, never the converge chat.

goal: the first outcome's card describes the game the owner now wants — a crew that cuts
its own path through solid ground into pockets of the substance — with its four internal
contradictions removed and the owner's verdict on the exact text.

AFTER `map`: a fresh `converge-verify` session refutes `work/converge-g-37a1.md` against
the new card, then `shape`. The first task of the bet should be the cheapest visible
result — a man digs a hole and walks into it, with no substance and no air — because
that is the first thing that has never existed.

END_OF_FILE: live/indie-game-development/history/2026-07-27-s-converge-g-37a1-substance-passage-001.md
