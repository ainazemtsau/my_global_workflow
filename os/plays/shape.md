# Play: shape

Purpose: turn one tree node into the active bet — the planning ritual. This is where scope is cut and the next work becomes concrete.

Reads: CHARTER.md, TREE.md, NOW.md, relevant knowledge/.
Writes: TREE.md (the node), NOW.md (the bet), LOG.md.

Precondition: no active bet (gate G1), node chosen by owner or review's accepted recommendation, and its **Definition-of-Ready** is cleared (converge-readiness — os/plays/converge.md).

## Steps

1. **Recite** — restate the node's goal and done_when, and its parent's goal. If the node's goal is an activity ("do marketing") rather than an outcome ("500 wishlists"), fix it first.
2. **Appetite first** — ask or propose: how much time is this outcome worth (not how long it takes)? Fix appetite before any solution talk (gate G3). Outside-view check: name 1–3 comparables; on conflict trust them.
3. **Approaches, then minimal solution** — before sketching anything, name 2–3 structurally different ways to satisfy done_when within appetite (different mechanism, not different size — build / fake-or-reuse / make-most-work-unnecessary), each with the one assumption it bets on. If the owner brought an approach, generate the alternatives first, then rank all on equal footing — no automatic privilege for it. Pick one with a one-line why-over-the-others; losing approaches go to captures. Then sketch the smallest version of the chosen approach. Explicitly state what this version does NOT include.
4. **Scope hammer** — challenge every element: "what breaks if we cut this?" Cut until something genuinely hurts. Record the cut list (≥1 real cut — gate G6); cuts go to `parked` or captures, not into the bet.
5. **Lens sweep** — for each lens in CHARTER.md: does this bet need work from this lens? Verdict per lens: a task, or `not_needed: <reason>` (gate G6). Silent skipping is invalid.
6. **Riskiest assumption** — list the assumptions this bet rests on, starting with the chosen approach's bet from step 3, ranked by kill-power. The top one gets a task that tests it as early and cheaply as possible (gate G6). Calibrate test depth to the charter's risk_posture.
7. **Tasks** — 3–7 tasks, each ≤ half a focused day, each with verifiable done_when. Order them so the riskiest-assumption task comes first or near-first. Mark each task's kind: session, executor (engineering), or guide (owner-operated tool — os/plays/guide.md). Executor-heavy bets name the evaluator and rollback first.
8. **Kill criteria** — kill_by: metric + threshold + date (gate G4). If the bet reaches the date or breaches the threshold, review triggers automatically. State next_if_true / next_if_false — which branch opens, dies, or mutates either way.
9. **Close** — show one screen: appetite, tasks, cuts, lens verdicts, kill_by, forecast and against. On approval, RESULT makes the node `active`, writes the bet, registers its first-task CALL in `open_calls`, and hands it off through `RESULT.next`.

## Done when

NOW.md has an approved bet passing G1–G6; its first-task CALL is in `open_calls` and local `RESULT.next`.

## Notes

- Shape is one session — or two when appetite exceeds a week: close with a checkpoint once approaches are on the table; choose in the next session (≥1 night — incubation). If shaping stalls on an unknown, spawn `call:research` and close awaiting its return — do not pad the bet with guesses.
- Shaping a node may reveal it needs children instead of tasks (too big for one appetite). Then: split into 2–4 child outcome nodes in TREE.md (each shown as a card with its why and approved by the owner in-session — gate G9), recommend which child to shape, close — a valid result. Recursion happens here, on demand, never in advance.

END_OF_FILE: os/plays/shape.md
