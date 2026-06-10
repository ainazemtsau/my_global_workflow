# Play: review

Purpose: close the active bet, update the tree from what was learned, and select what's next. The only play that revises TREE.md after framing — feedback lives here.

Reads: CHARTER.md, TREE.md, NOW.md, history/ of the bet's sessions.
Writes: TREE.md, NOW.md, LOG.md, knowledge/.

Trigger: all bet tasks closed, OR appetite expired, OR kill_by breached. Must run in a fresh session — never the session that did the work (gate G5).

## Steps

1. **Verify by refutation** — take the bet's done_when and actively try to refute that it is met: check the evidence, not the claims. Verdict: met / partially met / not met. For kill_by breach or expired appetite: the bet is dead by default (gate G3) — no extension exists; what remains becomes a parked node that future shape may pick up as a NEW bet.
2. **Harvest per lens** — for each lens in CHARTER.md: what did this bet teach us that changes other parts of the tree? Each lens answers, even if "nothing". This is where cross-lens consequences surface (a product result triggering audience work, market data triggering a business node).
3. **Update the tree** — apply the harvest: node statuses, new child outcomes, dropped nodes (prune anything the learnings invalidated), promoted parked items. Outcomes only — no tasks (gate G2).
4. **Add-back check** — look at the bet's cut list: did any cut item turn out to be genuinely missed? If nothing was ever missed across recent bets, cuts are too timid — say so. Record the ratio observation in the log line.
5. **Knowledge** — promote at most 1–3 durable learnings into knowledge/, each with `read_by:` (which play/lens reads it, when). A learning nobody will read is not knowledge — drop it.
6. **Select next** — propose 2–3 candidate nodes for the next bet, across different lenses where sensible, each with one line of why-now (what it unblocks or which assumption it tests). Recommend one (gate G7). Include "pause this direction" as an honest option when the tree shows no urgent node.
7. **Close** — RESULT: bet closed with verdict, tree updates, decisions_needed = next-bet choice, log line, next = CALL for shape on the recommended node (activates on owner approval).

## Done when

Bet has a verified verdict; TREE.md reflects the learnings; owner has a next-bet decision with options; NOW.md is clean of the old bet.

## Notes

- Review is judgment day, not a ceremony: the value is in steps 1–3. If the bet was trivially verified, spend the session on the harvest and the selection.
- A "not met" verdict is information, not failure — the tree update and the next selection are how the system learns.

END_OF_FILE: os/plays/review.md
