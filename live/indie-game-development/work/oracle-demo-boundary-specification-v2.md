# Node-class oracle — owner-approved demo boundary specification, v2

identity: oracle-demo-boundary-specification-v2
authored: 2026-07-26 by s-converge-verify-october-demo-basis-v3-001
extends: oracle-demo-boundary-specification-v1 (authored 2026-07-26 by the v2
verification; that leg's own «what the oracle caught» section is corrected below)
status: PROPOSED for promotion to `knowledge/` by review or pulse. No authority
until promoted. It supersedes v1 as the promotion candidate.
node_class: an owner-authored artifact whose own text is the deliverable and whose
job is to bound one shippable demo (`outcome_kind: specification`).

## Why a v2 and not a reuse

`os/plays/converge-verify.md` step 2 forbids relying only on the sources the
author used and requires an independent oracle; the CALL
`c-converge-verify-october-demo-basis-v3-001` additionally warns that reusing v1
unchanged would inherit the previous attacker's blind spots, and names three
surfaces of v3 that v1 contains no test for: a section that declares itself
**not law**, a **dormant** falsifier, and an **explicit null** exceptions
statement. A fourth surface is new to v3 and was not named in the CALL: a body of
text repaired by an **agent under owner delegation** rather than authored by the
owner.

WHAT WAS DONE, stated exactly. The first principle was re-derived independently
before the artifact was attacked. O1–O12 were kept as a test *set* but each was
re-applied from the artifact text rather than from v1's recorded verdicts — which
is what exposed the correction below. O13–O17 are new. No verdict of v1 was
trusted.

CORRECTION TO v1. v1 records «O1, O2 (promise text), O4 (mostly), O6 (forbidden
list) and O7 passed». Re-application shows O4 and O7 did **not** pass, and did not
pass in v2 either: the readable moment's three physical dependencies were already
outside MUST in v2 verbatim, and v2's SHOULD list already offered as optional a
second substance behaviour that its own MUST 2 already mandated. Those are the
previous attacker's blind spots the CALL warned about, and they are not new to v3.
A passed test is a claim about the artifact, not a property of the checklist.

## First principle, re-derived

A demo boundary specification is not judged on whether its content is good —
content is the owner's. It is judged on whether a **stranger holding only this
artifact** can (1) build the demo, (2) tell when the demo is finished, and (3)
tell when the specification itself has been proven wrong. Everything below is one
of those three questions asked of one part of the text.

Corollary used throughout: a specification may legitimately leave content
undecided, but it may not *depend* on what it leaves undecided, and it may not
make a false claim about its own coverage. A false self-claim is worse than a gap,
because a gap invites a question and a false claim closes it.

## The checklist

Each item is PASS/FAIL against the artifact text alone.

- **O1 Audience and success filter.** The artifact names who plays and what counts
  as a good outcome for them, and that filter is usable to reject a technically
  appealing proposal.
- **O2 Single player-facing promise.** One promise, stated without internal
  mechanics, plus an explicit "not promised" list. Every quantity inside the
  promise (players, minutes, objects) is either backed by a MUST item or withdrawn
  from the promise — withdrawn from the whole promise section, not from one
  sentence of it.
- **O3 Path stages carried by MUST.** For each stage of start → danger or task →
  joint action → readable result, the mechanism that carries the stage is in MUST.
  No stage — and no branch of a stage — may rest on a deferred item, a CUT item or
  an open question.
- **O4 Readable moment is emergent and reachable.** The moment's trigger, its
  physical precondition and its payoff each trace to a MUST item, and the artifact
  forbids the scripted substitute. A dependency satisfied only by a SHOULD item is
  a FAIL: a build that ships MUST alone must still be able to produce the moment.
- **O5 Causal-cooperation test is observable and correctly counted.** The test can
  be run and lost. Every support the artifact claims is (a) in MUST and (b)
  genuinely requires two players at the same time, not shared consequence or
  opportunity cost. The stated count matches the count that survives inspection.
- **O6 Public-claim ceiling matches MUST.** Nothing in the "may claim" list exceeds
  what MUST can produce in the shippable build. The forbidden list contains
  everything MUST cannot show. Every *prohibition* is grounded in MUST too — a
  ceiling narrowed by something that is not law is not a ceiling.
- **O7 Partition of scope is exhaustive and atomic.** MUST / SHOULD / deferred /
  CUT are explicit and **mutually exclusive**; each MUST item is one buildable
  thing; each traces to the owner's words. No SHOULD item duplicates a MUST item
  or presupposes a MUST item that does not exist. Content the MUST list newly
  requires and that does not exist yet appears somewhere in the partition.
- **O8 Every falsifier can fire.** Each falsifier is observable under the demo's own
  conditions, is not vacuously true, and refers only to content MUST contains. The
  falsifier set covers every quantity the artifact asserts anywhere, not only in
  the promise sentence.
- **O9 Invalidation set is complete for the current MUST list.** The tuple binding
  evidence names every dimension a MUST item can vary, and every dimension a
  *non-law* decision can vary while evidence stands.
- **O10 Open questions are declared and provably non-load-bearing.** For each open
  question the artifact says where it gets answered, and no done_when clause, MUST
  item, path stage, cooperation support or public claim — permission or
  prohibition — depends on its answer.
- **O11 Feasibility envelope.** Each MUST item is nameable as buildable inside the
  standing calendar or carries an explicit unresolved risk where the MUST item
  lives. Where a risk list exists in the direction's own records, the disclosure
  names the whole list or says which part it deliberately routes elsewhere.
- **O12 Authority hygiene.** No claim rests on a legacy source's former accepted
  status. Every non-owner factual assertion carries a citation resolvable inside
  current authority, the citation says what the artifact says it says, and
  conditional prior approvals keep their condition. Superlatives and universal
  claims ("the only item that…", "entirely lives in…") are assertions and need
  support like any other.

### New in v2 — tests for v3's new surface

- **O13 A "not law" section is provably inert.** Where the artifact declares a
  section not binding, nothing binding may reason *from* it. Check every MUST item,
  path stage, cooperation support, falsifier, public permission **and public
  prohibition** for dependence on it. If the not-law section can change without a
  new artifact version — as such sections normally may — then anything depending on
  it silently changes with it, and the artifact's own invalidation rule stops
  covering the evidence.
- **O14 A dormant criterion cannot mislead.** A falsifier suspended because its
  subject is deferred must state (a) why it cannot fire, (b) that it is not counted
  as fired, and (c) the exact condition that revives it. And it may not be the sole
  cover for anything: the falsifier set minus the dormant entries must still cover
  every asserted quantity and every required claim.
- **O15 An explicit null is a real answer only if it is true.** A statement of the
  form "there are no exceptions / nothing is excluded" satisfies a required atom
  only if no carve-out, suspension or conditional applicability exists anywhere
  else in the artifact. A null contradicted by the artifact's own body is a defect,
  not coverage — and a null whose scope is quietly limited to the text *above* it
  is not the atom's answer either.
- **O16 Delegated mechanical repair is bounded.** Where an agent repaired the text
  under owner delegation rather than owner authorship, each repair must be
  traceable to the finding it answers, must be subtractive or bookkeeping rather
  than a new normative commitment, must not narrow or ground an owner decision in
  something that is not law, and must be checked **against every other repair in
  the same round** — independent repairs of independent findings are the likeliest
  source of a fresh contradiction.
- **O17 Self-description matches the body.** The artifact's own statements about
  itself — a changelog, a "what changed" section, "X now lives only in Y", "Z is no
  longer cited here", "this requirement lives entirely in W" — are checked against
  the body. A self-claim that did not land is a defect of the same severity as the
  thing it claims to have fixed, because it stops the next reader from looking.

## Precedent basis, stated honestly

Unchanged from v1 and re-verified: no comparable in-repo precedent exists for this
node class — `g-12fd` is the first `outcome_kind: specification` node in this
direction, and the pre-reset material is archive-quarantined with zero authority.
The oracle derives from three sources inside current authority: the direction's own
observable quality threshold (`CHARTER.md` §2), its risk posture (cut scope, never
the date, and premortem 4's demand for an explicit list of what is not done), and
the general requirement that a specification be executable and falsifiable by a
stranger. No competitor practice was used: no external demo-boundary document is
available as evidence here, and inventing one would be a fabricated precedent.

## What this oracle caught in v3

O2, O3, O4, O6, O7, O10, O11, O13, O15 and O17 each caught at least one defect the
artifact's own structure did not surface. O1, O5, O8, O9, O12's legacy half, O14
and O16's traceability half passed. The eight findings are named in the
verification RESULT
`history/2026-07-26-s-converge-verify-october-demo-basis-v3-001.md` and in the
returning CALL `work/c-work-october-demo-basis-v4-revision-001-call.md`.

O16 is the load-bearing new test: four of the eight findings are defects of the
mechanically delegated repair round, not of the owner's content.

END_OF_FILE: live/indie-game-development/work/oracle-demo-boundary-specification-v2.md
