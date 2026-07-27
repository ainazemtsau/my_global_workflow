# RESULT s-map-substance-passage-concept-reset-001

direction: indie-game-development
play: map (roadmap-node fast path — one card revised under an approved parent)
node: g-37a1 (with a light edit to g-5e8c)
call: none — opened from the owner's plain message per KERNEL §2 (content of an
  approved roadmap card changed → map)
date: 2026-07-27

## outcome

The FIRST outcome keeps its position and loses its content. `g-37a1` is no longer
«набрал вещество → понесли шар вдвоём → сдали или не успели». It is now a one-way
passage of one hand-built section through the substance, in which the ONLY player
interaction is with the substance itself: detect it, pass through it, move it.

The owner approved the exact eleven-point card with `да`. The seven-outcome
roadmap, all six other cards, every date and the whole calendar are untouched.

Two consequences that are worth more than the card text:

- **The hardest engineering risk of the direction is gone, not mitigated.** Two
  players carrying one physics object over the network — unsolved in FishNet,
  an open issue in Unity's own netcode — was the kill-risk of the previous first
  outcome. There is no carried object any more, so `i-coop-carry-netcode` is
  closed by removal.
- **The simulation gets a scope cut, not more work.** The substance no longer has
  to interact with objects. Substance-to-player and substance-to-substance only.

## evidence

OWNER PRESENCE. The whole leg ran with the owner present, as a long read-only
design conversation followed by one approval. No content below was chosen by an
agent; each item is either his words or a proposal he accepted, edited or killed.

HOW THE CONCEPT ARRIVED — the sequence, because the refutations are the value.

1. He asked whether the current concept could ever be commercially interesting,
   and whether to abandon it. Four research children were run at his explicit
   request (`делай ресёрч ... какие лучшие практики`). The decisive finding was
   that the experiment had already been run and published: R.E.P.O.'s co-founder
   on why they CUT cleaning when they went co-op — «Co-op cleaning in real life,
   it's not that fun»; «You never go like: "Hey friend, let's help each other
   clean here" ... It's always: "You take bathroom one, I take bathroom two"»;
   «there wasn't really anything in the gameplay loop that kept the players
   together». The structural reading, which became this leg's design thesis:
   **cleaning parallelises because your action changes only your room; a
   simulated shared medium cannot parallelise because your action changes every
   room.**
2. The agent's first concept («не сводить вместе» — two crews carrying
   incompatible substances) was REFUTED BY THE OWNER, correctly: the conflict is
   avoidable by waiting, and an avoidable conflict is not a conflict. Recorded so
   the same class of proposal is not made again.
3. The agent's second concept put some players outside in safety operating the
   air for one player inside. The owner rejected the operator/spectator split.
4. He then proposed the shape that survived: a passage — «нам нужно, чтобы игроки
   идут через газ ... они должны решать какие-то вопросы, которые они встречают с
   газом» — with a chain of sections and rest stops between them, PEAK-like in
   structure only.
5. He killed the agent's «rising substance that chases you» outright, and the
   reasoning is his: a pursuer can be scripted, so it does not need the
   simulation at all. This is now the sharpest available test for any future
   mechanic on this project — **if a script could fake it, the simulation is not
   earning its cost.**
6. He asked why come back at all. The return trip was cut; the run is one-way.
   The consequence is better, not merely simpler: a player's change to the
   atmosphere now lands on a LIVING teammate who shouts about it two seconds
   later, instead of on his own past self forty minutes on.
7. His own image became the strongest co-op structure in the concept: an
   instrument that shows shapes through the substance, one player walking ahead
   carefully, another directing — «тут налево, тут направо» — and watching who got
   through. Recorded as content for the converge; he explicitly REFUSED to fix
   one-instrument-per-crew as law.

THE FIVE LAWS, approved as the card's own done_when. Each was chosen because
reversing it later would throw away real work:

1. No cargo-transport mechanics of any kind; all interaction is with the
   substance. His words: «никаких больше механик по переносу ... всё направлено на
   взаимодействие с газом, либо его детект, либо его какой-то перенос».
2. The substance is an environment, never a scripted pursuer.
3. One-way passage, no way back; rooms have real height and the substance's
   vertical distribution is part of the problem, not decoration.
4. Substance kinds are distinguishable at a glance, without instrument or UI,
   verified on a person outside development.
5. Air is the only counter; it drains differently in different substances and can
   be handed to a teammate.

TWO OWNER CORRECTIONS APPLIED TO THE AGENT'S DRAFT, both recorded against drift:

- **«Вниз» was removed.** The agent had presented a downward route as a
  consequence of the physics. It is not: the physics requires vertical SPACE, not
  a vertical DIRECTION of travel, and the agent had conflated them. The owner's
  challenge — «почему именно вниз?» — was correct. Difficulty comes from what a
  section is made of, not from which way it runs, so the direction is left
  undecided and resolves on real geometry.
- **«Лёгкое и тяжёлое» was removed as law.** His words: «я бы не хотел делать
  акцент именно лёгкий и тяжёлый газ, как будто мы это уже выбрали ... у нас же
  могут быть вообще другие вещества даже, да, не газ там, жидкость, например».
  It stays a testing basis only. The term «вещество», chosen by him on
  2026-07-26, was already the right one and predetermines nothing.

THE SIZE QUESTION, which he named as priority one — «сначала вот самое важное —
это грид». His fact: the simulation was planned around roughly 150 fairly large
rooms as ONE level, with the optimisation for a fully filled space never written.
Under this concept the space is neither fully filled nor nearly empty. The agent's
claim that the section structure solves this was WRONG and is corrected here: the
chain of sections does not shrink a section, so the size envelope is a decision to
be taken, not a consequence to be enjoyed. 150 rooms is a candidate, not a given.
`done_when 7` therefore requires the size, the room count and the filled fraction
to be fixed BEFORE the build and to not grow afterwards.

WHAT THE RESEARCH SAYS ABOUT THE EMPTY SPACE, recorded because it is the reason
this concept is worth the risk. No shipped title combines a per-cell simulated
multi-species medium, that medium acting as the traversal volume, players
redistributing it, and co-op. Oxygen Not Included is the simulation twin and is
single-player only by Klei's decision, with gas as resource and hazard that never
carries a duplicant. PixelJunk Shooter is the co-op fluid twin, but rock remains
the terrain. Splatoon is the «the medium you create is the medium you move in»
twin, but ink is painted surface, not a volume. Gas that lifts a player exists
only as scripted volumes — Zelda updrafts, Minecraft bubble columns. Direct
competitors found: zero.

WHAT THE ADVERSARIAL PASS FOUND, kept because it is the risk register. Its two
fatal objections were (a) a gaseous medium has no silhouette and may not read in
a still frame or a short clip — Klei REMOVED the Oxygen Not Included gas overlay
because players did not notice their duplicants suffocating, and a Steam capsule
must read at 120×45 px; and (b) the determinism claim breaks where player float
state feeds the simulation. Objection (a) is answered in the card as law 4, which
turns legibility from a hope into a done_when verified on an outsider. Objection
(b) is an engineering question for the converge, not for the tree. The same pass
tried and FAILED to refute three things: that zero art and a small budget are
disqualifying (Meccha Chameleon: two people, ~2 months, no marketing, 10M+
copies), that co-op is a declining category (no decline data exists), and that
twelve weeks is impossible (PEAK's core was four).

## state_changes

`live/indie-game-development/TREE.md`
- Rewrite `g-37a1` in place, keeping its id, position and `status: parked`: new
  goal, the exact eleven-point owner-approved done_when, new why, detail pointer
  to this history file.
- Light edit to `g-5e8c`: goal names the chain of sections with rest stops;
  done_when 1 replaces the cargo phrase «сдан / не успели» with «прошли / не
  прошли»; done_when 5 adds cargo-transport mechanics to what must not return;
  why replaces «смысл "не успели"» with «устройство привалов и смысл провала».
  Everything else in that card is preserved verbatim.
- Append the concept reset and the owner's `да` to `owner_approved`.
- No other card, and no date, is touched.

`live/indie-game-development/NOW.md`
- Set `updated: 2026-07-26 by s-map-substance-passage-concept-reset-001`.
- Preserve `bet: null`, `tasks: []`, `recurring: []`, `decisions: []`; no track,
  no lane; forecast stays `no_basis`.
- Prepend a `direction_forecast` driver recording the concept reset, the five
  laws, both owner corrections, the section/chain structure and the two gains
  (co-carry risk gone, substance-to-object interaction cut).
- Remove `i-coop-carry-netcode`: closed by removal of the mechanic it described.
- Add `i-substance-passage-open-questions` carrying the seven deliberately open
  questions in the owner's priority order, with his standing rule that a question
  is discussed only once a concrete task has stopped on it.
- Re-express `i-demo-scope-cap`'s trigger against the section rather than the
  carry loop; the 2026-08-07 date is unmoved.
- Replace the open call: `c-converge-g-37a1-core-loop-001` out,
  `c-converge-g-37a1-substance-passage-001` in, exactly one continuation.

`live/indie-game-development/work/`
- Add `c-converge-g-37a1-substance-passage-001-call.md`.
- Prepend a WITHDRAWN header to `c-converge-g-37a1-core-loop-001-call.md`; the
  file is kept as a receipt and must not be dispatched.

`live/indie-game-development/LOG.md`
- Prepend the one-line log entry from `log` exactly once.

`live/indie-game-development/history/`
- Save this full RESULT once as
  `2026-07-27-s-map-substance-passage-concept-reset-001.md`.

## captures

- The owner's test for any future mechanic, from his own rejection of the
  chasing substance: if a script could fake it, the simulation is not earning
  its cost. Worth promoting to knowledge once a second leg uses it.
- The seer-and-walker image is his, and it is the strongest co-op structure
  produced in this conversation. It is content for the converge, not law.
- Reactions as a FORGE rather than only as destruction — two substances making a
  third — is his idea and is unused so far.
- Steam Playtest still unused and still free; it does not consume the one-per-
  title Next Fest slot.
- A co-op demo has an unmeasured empty-lobby risk at Next Fest; worth a bounded
  research question before 2026-09-15.

## decisions_needed

[]

## play_check

- Roadmap-node fast path taken: one bounded card under an approved parent, with a
  light consequential edit to its immediate sibling. Skeleton, search and the
  full lens sweep were skipped with reason — the tree's shape, order and lens
  coverage were approved earlier the same day and are unchanged; only the content
  of one card moved.
- 1 Recite: done — the current card, the five laws and the open questions were
  restated in plain words before the exact text was shown.
- 4 Cards: done — one card elaborated with goal, verifiable done_when, root-facing
  why, and an explicit list of what does not appear in it.
- 5 Per-node verdict (owner): done — the exact eleven-point text was shown and
  revised twice on his challenges (route direction removed; light/heavy removed),
  and the verdict was given on the final text: `да`.
- 6 Order: unchanged — g-37a1 keeps its position; no other card moved.
- 7 Depth check: done — top level only; the section/chain split is expressed as
  g-37a1 versus g-5e8c, not as new children.
- 8 Lens sweep: not re-run, with reason — the approved lens coverage of
  2026-07-26 is unaffected by a content change inside one card; lens 2 (player
  clarity) is in fact strengthened, since legibility became done_when 5.
- 9 Close (owner): done — `да` on the exact card; TREE and LOG saved; exactly one
  continuation registered; no bet, task, track or lane created.
- Process note: this is a second leg in one physical chat, which the rules
  discourage. It was taken because the change is one card and the owner was
  present for the whole derivation. The converge is explicitly required to run in
  a FRESH chat.

## log

g-0c26/substance-passage-concept-reset: the owner replaced the CONTENT of the first outcome and approved the exact eleven-point card with «да» — g-37a1 is no longer a carried ball but a one-way passage of a hand-built section through the substance, where the only player interaction is with the substance itself (detect, pass, move); five laws are now in its done_when — no cargo-transport mechanics at all, the substance is an environment and never a scripted pursuer, one-way passage with rooms of real height whose vertical distribution is part of the problem, substance kinds distinguishable at a glance verified on someone outside development, and air as the only counter that can be handed to a teammate; two owner corrections are recorded against future drift — light-versus-heavy is a testing basis and NOT law since the substances may not be gases at all, and the route direction stays undecided because difficulty comes from a section's composition rather than its direction; the structure is a chain of sections with rest stops, g-37a1 being one section and g-5e8c the chain, so g-5e8c lost its cargo language too; the two-player carried-rigidbody netcode risk is CLOSED because the mechanic is gone, substance-to-object interaction is an explicit simulation scope cut, and the grid and size envelope — his own stated priority, against a planned ~150-room level — is fixed as a done_when requirement to be decided before the build; the seven-outcome roadmap, every other card and every date are untouched; c-converge-g-37a1-core-loop-001 is WITHDRAWN and replaced by c-converge-g-37a1-substance-passage-001.

## next

CALL c-converge-g-37a1-substance-passage-001
to: session
direction: indie-game-development
play: converge
node: g-37a1
goal: |
  The WHAT of the first outcome is locked to an owner-signed spec that `shape` can
  consume: two to four connected players pass one hand-built section end to end
  through the substance, interacting with nothing but the substance.
context: |
  Full CALL text: `work/c-converge-g-37a1-substance-passage-001-call.md`. Readiness
  route per KERNEL §2 is unchanged: no passing `converge-verify` and no recorded
  converge-OFF triage, so `converge`. The five laws enter born-closed. The leg's
  first business is the owner's stated priority — the grid and the size envelope
  — then how a player reads the substance at a glance.
boundaries: |
  Converge only: no build, no shape, no bet, no tasks, no lanes, no executor CALL,
  no product or Steam mutation. Do not reopen the five laws, do not reinstate any
  cargo mechanic, do not fix light-versus-heavy as law, do not decide owner
  content. Generation belongs to g-5e8c. No archive or frozen-canon read. Do not
  move 2026-08-07.
done_when: |
  As in the CALL file: triage recorded, glossary and §WHAT signed, the grid
  decomposed into cell resolution, section extent, rooms per section, volume
  simulated at once and cost on the owner's machine, a runnable acceptance test
  for at-a-glance legibility, forward- and backward-clean, owner forks batched,
  and `next` routed to `converge-arch` if heavy else `converge-verify`.
return: |
  One `converge` RESULT with the triage line, signed glossary and §WHAT, the size
  envelope or the owner fork that decides it, `converge_coverage`, the owner's
  verbatim signoffs and the routing handoff.
budget: one owner-present session
surface: a FRESH chat with the owner present — never this chat

END_OF_FILE: live/indie-game-development/history/2026-07-27-s-map-substance-passage-concept-reset-001.md
