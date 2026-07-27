# RESULT s-repair-post-concept-reset-consistency-001

direction: indie-game-development
play: repair
node: g-0c26 (hot-state consistency after the concept reset)
call: none — opened from the owner's plain message per KERNEL §2 after an
  independent audit run from another chat reported defects
date: 2026-07-27

## outcome

An independent audit, run by a separate session that had been started on the now
withdrawn CALL, reported seven defects in the state left by the two map legs.
**All seven were verified first-hand against the files and git before anything was
touched; all seven are real.** Three were contradictions, one was a dating error
across the whole record, one was a process breach by the writer, one was a stale
knowledge surface, and one was an unpushed branch that only the owner can resolve.

Nothing owner-decided was changed. No card text was edited, no date moved, no
issue silently dropped, and the single open CALL is unchanged — so the paste block
the owner already holds stays valid.

## evidence

**A1 — CONFIRMED. Both rewritten cards pointed at the superseded receipt.**
`g-37a1` and `g-5e8c` were rewritten by `s-map-substance-passage-concept-reset-001`
but their `detail:` fields still named the order-reset receipt, whose text
describes the withdrawn ball concept. Anyone opening a card's rationale would have
read a cancelled design. Verified by reading the `detail:` lines. Cause: the
rewrite edited goal, done_when and why, and the `detail:` line sat outside the
replaced block.

**A2 — CONFIRMED, and it is the highest-consequence pointer in the file.**
`i-demo-scope-cap` cited `TREE.md (g-37a1 done_when 6)` for the 2026-08-07 cut. In
the new card done_when 6 is the air counter; the cut is done_when 11. The prose of
the issue was already correct — only the citation was wrong. This is the single
line that closes the October route, so a wrong pointer here is worse than
elsewhere. Fixed to done_when 11 and the concept-reset receipt added.

**A3 — CONFIRMED. Two drivers asserted opposite first outcomes in the present
tense.** Driver 1 (new) says the ball and all cargo-transport mechanics are out.
Driver 2 (carried over unchanged) said «The FIRST outcome is now g-37a1: two
connected players carry one ball through the loop». Both sat in `NOW.md` as
current basis, and a morning brief or the next planning leg would have read both.
Driver 2 is now marked as superseded in part, naming which part died and which
part survives. Driver 5 (the cut order) still said «the g-37a1 loop does not run
end-to-end» and now says «the g-37a1 section is not passed end-to-end».

**B1 — CONFIRMED, and it is worse than the audit stated in one way and better in
another.** Commit timestamps: `1d3b9ee5` at 2026-07-27 04:00:46 and `07d9e40b` at
2026-07-27 08:09:49, with the machine clock reading 2026-07-27 08:21. Both map
legs therefore ran on 27 July and were written as 26 July throughout — `updated`,
`as_of`, `issued`, two LOG lines, two receipt filenames, the receipts' own `date:`
fields, the withdrawal banner, and the phrase «later the same day 2026-07-26»,
which in fact described two legs four hours apart on the following day. **Better
than reported:** every earlier leg is correctly dated — `d68f1a54` and everything
before it are genuinely 26 July — so the error is bounded to the two legs written
in this chat and the previous record needed no correction. **Consequence that
matters:** the standing distance to the 2026-08-07 boundary is eleven days, not
twelve. The date the writer used came from session context rather than from the
machine; the machine and the commits are the authority and were checked here.

**B2 — CONFIRMED as a process breach by the writer, recorded rather than
argued away.** Commit `07ceab79` amended
`work/c-converge-g-37a1-substance-passage-001-call.md` — a file under `live/**` —
directly, with no LOG line and no receipt, and with a commit subject
(`writer-amend ...`) outside the `<direction> <play> <node>: <line>` convention.
The rule is that `live/**` changes only through a RESULT's `state_changes`; a
never-dispatched CALL is not an exception. The amendment's CONTENT stands and is
not reverted — it adds the laws-versus-settings split, the admission rule that a
rule becomes a law only if the first section cannot be built without it or it has
already been demonstrated in a build, the routing of the law set as a canon
candidate for `review`, and a done_when requiring the law set as a named section.
It rests on the owner's own words of 2026-07-27 («определить какие-то законы
вещества … чтобы потом мы точно их кардинально не меняли, а возможно только
дополняли»). What was missing was its trace, and this receipt is that trace.

**B3 — CONFIRMED, and repaired only as far as repair is allowed to.**
`knowledge/strategy-reset-boundary.md` still names
`c-work-october-demo-basis-authoring-001` as «the sole lawful frontier» — six CALLs
stale — while its own `read_by` sends every day, frame and map session to it
before planning. Two map legs have now run past it. Per `os/plays/repair.md`, a
knowledge surface that falsely claims current routing may receive a visible
retirement banner, and removal or rewrite needs the owner's words naming that
surface. A banner was added; the entry's body is untouched; the rewrite stays with
the narrow `review` that owns it under `i-frontier-knowledge-stale`.

**B4 — CONFIRMED, owner's step, not repaired.** All direction commits live only on
`wt/indie-game-development`. Local `main` is at `89b1292b`, six commits behind, and
`origin/main` is one commit ahead of local `main` at `b9c7ad25`. Any session that
reads `main` or the remote sees the pre-reset state — Demo Basis and the ball.
Repair does not push and does not move `main` without the owner's word.

**THE AUDIT'S ONE SUBSTANTIVE CATCH, deliberately NOT patched.** `g-37a1`
done_when 2 requires the player to MOVE the substance; done_when 9 excludes
«взаимодействие вещества с предметами». Read literally, the exclusion would also
cut any container, tool or fan, and done_when 2 names no verb. The recorded intent
of the exclusion is narrower — the owner's scope cut was that the substance no
longer has to interact with LOOT or carried objects. The card carries his `да`, so
repair does not edit it. It is recorded as open question 8 in
`i-substance-passage-open-questions` for the converge, which may return it to him
as a card edit if the wording needs tightening.

**WHAT THE AUDIT CHECKED AND FOUND CLEAN, re-verified here:** `END_OF_FILE`
trailers present on every state file, both CALLs, both knowledge entries and the
receipts; exactly one new LOG line per leg with an existing receipt behind it; the
withdrawn CALL kept with an explicit banner; exactly one open CALL with `bet:
null`, empty tasks, no lanes and no pending decisions; `owner_approved` recording
the concept reset with the owner's `да`; the other five cards and every date
untouched; `i-coop-carry-netcode` removed without residue.

**ONE ENGINEERING FACT CARRIED FORWARD FROM THE WITHDRAWN LEG**, because it
survives the concept change and is the only measured number the direction owns
against the open grid question: full substance state at 96 bytes per cell gives a
12×12×4 m room of 4,608 cells a 432 KiB snapshot — zero bytes on the wire under
lockstep, about 570 kbit/s per room if state were distributed instead, and roughly
4.5 Mbit/s at eight times the volume. Against the ~150-room figure in
`i-substance-passage-open-questions` this is the only measurement available. It is
evidence for the converge, not a decision, and it was produced by a session
working from the withdrawn CALL — so it is cited as a number to re-derive, not as
a settled result.

## state_changes

`live/indie-game-development/TREE.md`
- Point `g-37a1.detail` and `g-5e8c.detail` at
  `history/2026-07-27-s-map-substance-passage-concept-reset-001.md`; the three
  cards that were not rewritten keep the order-reset receipt.
- Re-date the two 2026-07-26 entries in `owner_approved` to 2026-07-27 and update
  their receipt paths. No card text, status or semantics changed.

`live/indie-game-development/NOW.md`
- `updated: 2026-07-27 by s-repair-post-concept-reset-consistency-001`;
  `as_of: 2026-07-27`; `issued: 2026-07-27` on the open CALL.
- Driver 1: «later the same day 2026-07-26» → «on 2026-07-27».
- Driver 2: marked superseded in part, naming that its ball-carrying first outcome
  died in the concept reset and that the rest of that leg stands.
- Driver 3: Valve verification re-dated to 2026-07-27.
- Driver 5: cut trigger reworded from «the g-37a1 loop does not run end-to-end» to
  «the g-37a1 section is not passed end-to-end»; the 2026-08-07 date is unmoved.
- `i-demo-scope-cap.evidence`: `done_when 6` → `done_when 11`, concept-reset
  receipt added.
- `i-substance-passage-open-questions`: append open question 8, the done_when 2
  versus done_when 9 ambiguity, with its recorded intent and its route.
- Preserve `bet: null`, `tasks: []`, `recurring: []`, `decisions: []`, forecast
  `no_basis`, every issue and the single open CALL.

`live/indie-game-development/history/`
- `git mv` both misdated receipts to `2026-07-27-…` and correct their `date:`
  fields; every pointer in TREE, NOW, LOG and both CALL files updated.
- Save this RESULT as `2026-07-27-s-repair-post-concept-reset-consistency-001.md`.

`live/indie-game-development/knowledge/strategy-reset-boundary.md`
- Add a visible stale-frontier banner naming the current frontier and directing
  routing to `NOW.md` `open_calls`; body untouched; rewrite left to `review`.

`live/indie-game-development/work/c-converge-g-37a1-core-loop-001-call.md`
- Withdrawal banner re-dated to 2026-07-27.

`live/indie-game-development/LOG.md`
- Re-date the two map lines to 2026-07-27 and prepend this leg's line once.

## captures

- The writer took a session-supplied date over the machine clock and mis-stamped
  two legs. Cheap standing habit: on a deadline-driven direction, read the clock
  or the last commit before writing a date into state.
- The 96-bytes-per-cell snapshot arithmetic is the direction's only measured
  number against the grid question and should be re-derived, not trusted, in the
  converge.

## decisions_needed

[]

## play_check

- 1 Name the contradiction: done — seven named, each verified first-hand against
  files, `git log --date=iso` and the machine clock before any edit.
- 2 Reconstruct: done — newest-first through git, LOG and the two receipts.
  Commits outranked the session's own memory of the date, and that is what caught
  B1. Inventory unchanged: no bet, no tasks, no lanes, one open CALL.
- 3 Propose corrected state: done — one reason per change, recorded above. No
  issue removed; the one new item is an open question, not a decision.
- 4 Confirm (owner): the owner authorized the repair in his own words —
  «Если надо, то можешь ли ты их исправить? Если да, то исправь». Removal boundary
  respected: the stale knowledge entry received a banner, not a rewrite or a
  tombstone, and no owner-signed artifact was altered. CHARTER and TREE semantics
  untouched; only pointers and dates moved, which the play classes as hygiene.
- 5 Friction: none filed. Both errors were the writer's, not holes in the OS, and
  a single occurrence is not a pattern.

## log

g-0c26/post-concept-reset-consistency: an independent audit from another chat found seven defects left by the two map legs and all seven were verified first-hand before repair — three contradictions fixed (both rewritten cards pointed at the superseded receipt; i-demo-scope-cap cited done_when 6 for the 2026-08-07 cut which now lives in done_when 11; two forecast drivers asserted opposite first outcomes in the present tense), one dating error corrected across the record (both map legs ran on 2026-07-27 by commit time and were written as 2026-07-26, so two receipts were renamed, all pointers updated and the standing count to 2026-08-07 becomes eleven days rather than twelve, while the correctly-dated earlier legs were left alone), one process breach recorded rather than hidden (commit 07ceab79 amended a pending CALL directly in live/** with no LOG line or receipt), a visible stale-frontier banner added to knowledge/strategy-reset-boundary.md with its rewrite left to the review that owns it, and the audit's substantive catch — done_when 2 requires moving the substance while done_when 9 excludes substance-object interaction — recorded as open question 8 for the converge rather than patched into an owner-approved card; no owner decision reversed, no card text changed, no date moved, one open CALL unchanged.

## next

Unchanged: `c-converge-g-37a1-substance-passage-001` remains the single open CALL
and its text is untouched by this leg, so the handoff the owner already holds is
still valid. It must run in a fresh chat with the owner present, and never in the
chat that was started on the withdrawn CALL.

Owner action outside this leg: publish the branch. All direction state lives only
on `wt/indie-game-development`; local `main` is six commits behind and
`origin/main` one commit ahead of it, so any session reading `main` or the remote
still sees the pre-reset ball concept.

END_OF_FILE: live/indie-game-development/history/2026-07-27-s-repair-post-concept-reset-consistency-001.md
