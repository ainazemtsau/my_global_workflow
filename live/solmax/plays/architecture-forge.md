# Play: local/architecture-forge

Purpose: forge ONE operating-substrate architecture/spec question from a
mapped question into one owner-approved architecture card. The AI may propose
options, compare tradeoffs and draft the card, but the owner freezes the
answer. This play does not design the whole substrate.

Reads: CHARTER.md, TREE.md, NOW.md, the relevant cartography artifact,
parent architecture cards if any, relevant knowledge/history/source
artifacts, and any research notes named in the CALL.

Writes: one work/operating-substrate/cards/<card-id>.md architecture card
when owner-approved, rejected alternatives, child questions or gap events,
LOG line, history RESULT, and proposed NOW changes. CHARTER/TREE edits still
require explicit owner approval per G9. No implementation code is written.

Precondition: the question comes from a local/architecture-cartography
forge_handoff, or the owner explicitly overrides the graph in-session.

## Steps

1. **Frame** — restate the exact question, the parent locks, what must be
   decided, what must not be decided, and why this question is ready now.
2. **Diverge (owner)** — present 2-3 viable answer directions with one-line
   "bad, because" for each and a recommendation. The owner picks, mixes or
   steers. `(owner)`
3. **Draft** — draft one architecture card: invariant/answer first, scope
   boundaries, rejected alternatives, downstream questions and proof anchors.
   Keep it atomic; do not answer downstream graph nodes.
4. **Gate** — refute the draft against parent locks, source/evidence policy,
   consumer-specific boundary, no-HOW/no-repo/no-implementation leakage, and
   the relevant research/proof needs. A fail returns to step 3.
5. **Freeze & grow (owner)** — owner signs the final card or refuses it.
   On sign, mark the card accepted, record owner words, rejected alternatives
   and child questions. On refusal or hidden prerequisite, emit gap_event.
   `(owner)`
6. **Close & route** — route to the next graph node, research call, or
   cartography gap pass. Do not activate implementation from this play.

## Done when

One architecture card is owner-approved with the owner's words, rejected
alternatives are recorded, child/downstream questions are preserved, gap_event
is emitted if the question was not ready, and no downstream substrate answer,
implementation, repo, test harness or Direction OS kernel change is frozen.

## Notes

- Co-frame is not co-freeze: related questions may be discussed for context,
  but the card freezes only the named question.
- If a hidden prerequisite, unclear plain question, wrong answer shape,
  missing research/proof need, or owner correction appears, close a
  checkpoint RESULT with gap_event and return to local/architecture-cartography.
- Current Zaratusta and Direction OS artifacts are evidence/source material,
  not substrate authority.

END_OF_FILE: live/solmax/plays/architecture-forge.md
