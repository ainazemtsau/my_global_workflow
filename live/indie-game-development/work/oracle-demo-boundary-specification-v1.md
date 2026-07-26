# Node-class oracle — owner-approved demo boundary specification, v1

identity: oracle-demo-boundary-specification-v1
authored: 2026-07-26 by s-converge-verify-october-demo-basis-v2-001
status: authored from first principles for this verification; PROPOSED for
promotion to `knowledge/` by review or pulse. It has no authority until promoted.
node_class: an owner-authored artifact whose own text is the deliverable and
whose job is to bound one shippable demo (`outcome_kind: specification`).

## Why it exists

`os/plays/converge-verify.md` step 2 requires an independent oracle and forbids
relying only on the sources the author used. No checklist for this node class
existed in `knowledge/`, and an empty oracle BLOCKS the leg. This one was
authored before the attack, from first principles, without reading the authoring
or revision session's reasoning or its own done_when reconciliation.

## First principle

A demo boundary specification is not judged on whether its content is good —
content is the owner's. It is judged on whether it can be **executed and
falsified by someone who was not in the room**. Every test below asks one
question: can a reader who only has this artifact build the demo, tell when the
demo is finished, and tell when the specification itself has been proven wrong?

## The checklist

Each item is PASS/FAIL against the artifact text alone.

- **O1 Audience and success filter.** The artifact names who plays and what
  counts as a good outcome for them, and that filter is usable to reject a
  technically appealing proposal.
- **O2 Single player-facing promise.** One promise, stated without internal
  mechanics, plus an explicit "not promised" list. Every quantity inside the
  promise (players, minutes, objects) is either backed by a MUST item or
  withdrawn from the promise.
- **O3 Path stages carried by MUST.** For each stage of start → danger or task →
  joint action → readable result, the mechanism that carries the stage is in the
  MUST list. No stage may rest on a deferred item or on an open question.
- **O4 Readable moment is emergent and reachable.** The moment is described so
  that its trigger, its physical precondition and its payoff each trace to a MUST
  item, and the artifact forbids the scripted substitute.
- **O5 Causal-cooperation test is observable and correctly counted.** The test
  can be run and lost. Every support the artifact claims for it is (a) in MUST
  and (b) genuinely requires two players at the same time, not merely shared
  consequences or an opportunity cost. The count of surviving supports stated in
  the text matches the count that survives inspection.
- **O6 Public-claim ceiling matches MUST.** Nothing in the "may claim" list
  exceeds what the MUST items can produce in the shippable build. The forbidden
  list contains everything the MUST items cannot show.
- **O7 Partition of scope is exhaustive and atomic.** MUST / SHOULD / deferred /
  CUT are explicit, mutually exclusive, and each MUST item is one buildable
  thing. Each MUST item traces to the owner's words.
- **O8 Every falsifier can fire.** Each falsifier is observable under the demo's
  own conditions, is not vacuously true, and refers only to content the MUST list
  actually contains. A falsifier whose subject is deferred or absent is a defect,
  not a spare part. The falsifier set covers every quantity the promise asserts.
- **O9 Invalidation set is complete for the current MUST list.** The tuple that
  binds evidence names every dimension a MUST item can vary: basis version,
  product commit and build identity, player count, substance physics, the level
  or object, and — when the level is generated — the generator, module set and
  the identity of the layout the attempt actually ran on.
- **O10 Open questions are declared and provably non-load-bearing.** For each
  open question the artifact states where it gets answered, and no done_when
  clause, MUST item, path stage, cooperation support or public claim depends on
  its answer. Load-bearing plus unanswered is a defect even when the question is
  disclosed.
- **O11 Feasibility envelope.** Each MUST item is nameable as buildable by the
  actual team inside the standing calendar, or it carries an explicit unresolved
  risk. A MUST that depends on a third-party tool, an unverified engine version,
  a tool pair with no precedent, or content that does not exist yet, names that
  dependency where the MUST item lives — not only in a footnote.
- **O12 Authority hygiene.** No claim rests on a legacy source's former accepted
  status. Every non-owner factual assertion (a tool's capability, a recorded
  verdict's content, an engineering consequence) carries a citation that a reader
  can resolve inside current authority, and the citation says what the artifact
  says it says. Conditional prior approvals keep their condition.

## Precedent basis, stated honestly

No comparable in-repo precedent exists for this node class: `g-12fd` is the
first `outcome_kind: specification` node in this direction, and the pre-reset
material is archive-quarantined and carries zero authority. The oracle therefore
derives from three sources available inside current authority: the direction's
own quality threshold (`CHARTER.md` §2, which is a list of observable checks),
its risk posture (cut scope, never the date), and the general requirement that a
specification be executable and falsifiable by a stranger. Competitor practice
was not used: no external demo-boundary document is available as evidence here,
and inventing one would be a fabricated precedent.

## What the oracle caught

O5, O8, O9, O10 and O12 each caught at least one defect the artifact's own
structure did not surface. O1, O2 (promise text), O4 (mostly), O6 (forbidden
list) and O7 passed. The named findings live in the verification RESULT
`history/2026-07-26-s-converge-verify-october-demo-basis-v2-001.md` and in the
returning CALL `work/c-work-october-demo-basis-v3-revision-001-call.md`.

END_OF_FILE: live/indie-game-development/work/oracle-demo-boundary-specification-v1.md
