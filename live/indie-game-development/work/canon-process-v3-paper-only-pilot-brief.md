
# Canon design process v3 — paper-only pilot brief

status: PILOT ACCEPTED — owner verdict "ACCEPTED" after one completed revised paper-only pilot; not installed; not a canon decision

## Hard boundary

Everything happens in text: imagined gameplay scenes, mechanic descriptions, filters and owner
discussion. There is no Unity scene, greybox, prototype, visual probe, A/B build, implementation,
setup, playtest or tuning of variants. Engine fit is judged only from known engine capabilities and
read-only project evidence. A paper-clean candidate may still be unfun; the process must say that
honestly and never claim otherwise.

## What the process is trying to protect

- This is a game first; simulation is material for player decisions, not the product by itself.
- Simple, not primitive: one clear rule, but the best action can change with a visible situation.
- Co-op must matter in the core loop, not merely make the same solo job faster.
- The base experience stays readable and unstuffy. Extra mastery/risk is voluntary: hardcore
  players choose it themselves.
- The atmosphere stays eerie and serious. Funny moments arise from players' errors, panic,
  rescues and chain reactions; the design does not insert a gag merely to get a laugh.
- Fixed foundations remain gas simulation, reactions and destructible/changeable space.
- DESIGN ANCHORS remain visible and retrievable, but are not silently promoted to canon or made
  immutable.
- A candidate must fit existing/planned engine seams. A large new subsystem is a default kill.

## Gate F — current Minimum Game Frame

A concrete design question may be selected only from a current owner-discussed
Minimum Game Frame.

Existing documents are evidence, not automatic truth. Every earlier accepted, liked,
frozen, draft, open, rejected or superseded claim that bears on the frame retains its
provenance and is checked against the owner's current view. A changed view supersedes
explicitly. This pilot specification does not amend canon.

The frame must make seven things owner-readable:

1. **Player promise.**
   What the player repeatedly does and what fantasy or tension makes that worth trying.
   This is a working design promise, not a final marketing slogan.

2. **Global loop.**
   What the crew does across one descent/expedition and across repeated attempts:
   why it enters, what it tries to gain or change, when it goes deeper, returns,
   retreats or fails, and what carries forward. Exact economy and progression are
   not required.

3. **Local repeatable loop.**
   What players repeatedly read, do and change over seconds and minutes, and what
   new decision the changed state creates.

4. **Core interaction roles.**
   The gameplay role, at frame altitude, of player↔gas, player↔space/grid,
   gas↔space/grid, gas↔gas/reactions and destruction/changeable-space↔gas.
   Exact tools, controls, parameters and implementation remain out of scope.

5. **Why co-op.**
   Where live interdependence is expected to arise, or an explicit OPEN/BLOCKING
   statement if the current frame contains only a co-op ambition and not yet a
   credible source of non-separable play.

6. **Escalation, failure, retreat and replay.**
   How the situation worsens, how a mistake creates a continuing game state rather
   than only a punishment screen, why the crew may cash out or retreat, and why
   another attempt is attractive.

7. **Explicit non-scope.**
   Which detailed gas states, Bubble-fill rules, roster, damage outcomes, tools,
   UI, economy, numbers, balance, evidence and implementation choices the frame
   does not decide.

The frame is checked on paper against:

- grows-from-foundations;
- an interesting-decision spine;
- simple-not-primitive;
- co-op/anti-solo source or explicit gap;
- pillar and tone pull;
- field legibility and attributable failure;
- CHARTER technical feasibility, solo scope and commercial legibility.

Mechanic lenses 1–5 remain paper predictions only. Lens 6 is NOT RUN in this
text-only process. A clean paper frame is still fun-unverified.

Gate F returns exactly one result:

- `FRAME READY` — the owner can explain the game globally and locally; the frame
  has no unresolved macro contradiction; applicable paper lenses have no blocker;
  and a first detailed question can be derived from a named open gap.
- `FRAME REVISED` — the frame is understandable, but one or more blocks or lens
  findings require correction before question selection.
- `FRAME BLOCKED` — a missing basis or unresolved macro fork changes the global
  or local game enough that no single trustworthy frame can yet be stated.

The owner's frame verdict is recorded verbatim.

No detailed question may be selected, and no local criteria, shared scene or
candidate may be generated, before `FRAME READY`.

## Gate Q — question origin and currentness

Only after `FRAME READY`, the session must show six owner-readable facts before
generating local criteria, a shared scene or candidates:

1. **Game/frame location.**
   Name the exact Minimum Game Frame block and part of play in which the question
   occurs, including immediate upstream and downstream player activity.

2. **Exact unresolved player decision.**
   Write one sentence:
   “In this situation, the players must decide whether/how to ___.”
   This must be the actual unresolved decision, not a catalogue mechanic or an
   agent-created theme.

3. **Source of the question.**
   Cite the authoritative direction-state artifact, owner statement, frame gap,
   dependency or current work item that created the question. A question with no
   traceable source is blocked.

4. **Why now and what it blocks.**
   Name why the question is current, the concrete decision or work item that cannot
   proceed without it, and every independent blocker that still remains. Do not
   imply that this question is the sole blocker when it is not.

5. **Entity provenance and meaning.**
   Define every introduced entity or term and name where it came from. An invented,
   undefined or silently repurposed entity blocks the gate.

6. **Explicit non-scope.**
   State what the question does not decide, including adjacent design, canon,
   implementation and evidence claims.

Gate Q returns exactly one result:

- `QUESTION READY` — all six facts are traceable and owner-readable, and the owner
  can explain where the question came from and why it must be discussed now.
- `QUESTION BLOCKED` — any source, entity, dependency, location, blocker or
  currentness claim is missing, ambiguous or disputed.

The owner's question verdict is recorded verbatim.

Candidate generation is forbidden before both `FRAME READY` and `QUESTION READY`.
A blocked gate stays on the same missing basis or question; the session does not
invent a substitute or silently advance to another queue item.

## Two levels of criteria — owner choice «А»

### Level 1: laws for the game and core loop

The game-wide principles above are checked against the whole loop or the decision bundle where they
actually matter. Fear/greed, true co-op, horror and emergent comedy do not have to be forced into
every button press or small mechanic.

### Level 2: criteria for this exact question

Only after Gate F returns `FRAME READY` and Gate Q returns `QUESTION READY`, the
session writes 3–6 local criteria that this question can genuinely affect: for
example readability, interruption, role exchange, spatial consequence or
reversibility. It also says which game-wide laws are relevant here and which are
explicitly **not this mechanic's job**.

If a new entity, dependency, macro assumption or different question appears while
criteria or candidates are being formed, the relevant gate reopens. The session
returns to FRAME REVISED/BLOCKED or QUESTION BLOCKED before continuing generation.

## How variants are determined

1. **Use the gated player decision; do not invent a new question.**
   Repeat the `QUESTION READY` player-decision sentence and construct one short
   base scene directly from its sourced Minimum Game Frame location. Do not
   substitute a more convenient mechanic, scene, vocabulary or priority.
2. **Build a private text pool.** Combine only game-relevant levers: player verb; gas/space change;
   information visible to players; cost or commitment; partner dependency; risk/reward; and a
   perceivable world consequence. A pilot target is roughly 10–15 rough ideas, not 10–15 items for
   the owner to review.
3. **Apply hard kills.** Remove an idea immediately when any of these is true:
   - its base rule cannot be explained in one sentence;
   - it is mainly a procedure, meter maintenance or simulation watching rather than play;
   - gas could be replaced by a generic coloured key/resource without changing the interaction;
   - players cannot perceive the consequence or understand what caused it;
   - one action is always correct, so there is no decision;
   - co-op means only “the same task, but faster with two” where co-op is this question's job;
   - complexity is mandatory at entry instead of voluntarily chosen mastery;
   - the funny part is a forced joke that weakens the threat;
   - it requires a major unplanned engine subsystem;
   - it loses or silently hardens a DESIGN ANCHOR.
4. **Cluster survivors by interaction structure.** Two wordings of the same action → system change →
   consequence are one candidate. The final 2–3 must embody different gameplay hypotheses, not
   cosmetic themes or parameter values.
5. **Stress each survivor on paper.** Write a base scene and one voluntary-mastery scene. Ask whether
   a visible state can change the best action. For fear/greed, show a real “leave safely now or push
   for a visible extra gain while shared risk rises” moment; greed must not be mandatory for the base
   route. For co-op, show how one player's live action changes the other's situation and why roles
   cannot collapse into one optimal solo body. Use these tests only when relevant at this level.
6. **Check engine fit without building.** Mark each candidate:
   - `EXISTING`: supported by known systems;
   - `SMALL EXTENSION`: a bounded addition to an existing/planned seam;
   - `NEW SUBSYSTEM`: default reject or explicit blocker.
7. **Present only the survivors.** The owner sees 2–3 short, equally detailed cards, or an honest
   BLOCKED result if no candidate survives. The discarded pool is summarized by kill reasons, not
   dumped into the conversation.

## Paper candidate card

Each candidate uses the same fields:

1. one-sentence gameplay promise;
2. base scene: what both players do and see;
3. simple rule and why the best action can change;
4. voluntary-mastery scene;
5. fear/greed moment, if this is relevant here;
6. real-time co-op coupling, if this is relevant here;
7. how the threat stays serious and what player-caused funny story could emerge without a forced gag;
8. engine fit: EXISTING / SMALL EXTENSION / NEW SUBSYSTEM, with one reason;
9. treatment of fixed foundations and DESIGN ANCHORS;
10. strongest downside and likely “boring/stuffy” failure mode.

The owner may choose one, keep several alive, request a revision, reject all, or declare the question
blocked. During this pilot, that response is evidence about the **process**, not permission to write
game canon.

## Pilot pass / fail

The pilot passes only if the owner can explain in plain words:

- what the current Minimum Game Frame says globally and locally;
- why the frame was FRAME READY rather than compiled from stale documents;
- where the concrete question came from and why it was current;
- which frame block and open gap the question belongs to;
- that Gate F and Gate Q completed before local criteria, scene construction or candidate generation;
- the provenance and meaning of every introduced entity;
- where the variants came from;
- why the shown candidates survived and the others did not;
- how the survivors differ mechanically;
- which laws were checked at game/core-loop level and which criteria belonged only to the question;
- what is known only on paper, including engine-fit uncertainty;
- whether the process is accepted, revised or rejected.

It fails if the output is an arbitrary idea menu, prose variants of one mechanic, a forced checklist
of every pillar on every micro-action, a disguised implementation request, or a claim that fun was
proved.

It also fails if a detailed question is selected before FRAME READY; if an old
document label is imported as current owner truth without discussion; if a genuine
macro fork is hidden inside an automatic hybrid; if candidate generation begins
before QUESTION READY; if the session invents the starting question, priority or
vocabulary; if an introduced entity has no traceable meaning; or if a blocked gate
silently switches to another question.

The pilot does not establish whether an owner-approved paper decision may enter canon; that
policy requires a separate explicit owner verdict after the pilot.

## Completed revised pilot verdict — 2026-07-11

owner_process_verdict: "ACCEPTED"
pilot_result: PASSED
scope: process only

The completed chain was:

`FRAME READY → QUESTION READY → structurally different paper-candidate
comparison → OWNER-SELECTED PAPER ANSWER`.

All explicit Pilot pass criteria passed, and none of the declared
pilot-fail conditions occurred.

The corrected process prevented recurrence of the original unsourced
question/entity-provenance failure.

This verdict does not install the process, alter canon or admit
q-investigation-readiness-paper-decision-v1 into canon.

Canon admission for that exact paper answer requires the separate
owner-present CALL:

`c-research-q-investigation-readiness-canon-admission-001`.

END_OF_FILE: live/indie-game-development/work/canon-process-v3-paper-only-pilot-brief.md
