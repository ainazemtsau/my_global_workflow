# Play: shape

Purpose: turn one tree node into the active bet.

Reads: CHARTER.md, cards/, NOW.md, relevant knowledge/.
Writes: cards/ (node/bet/tasks/tracks/call), NOW.md (bet pointer).

Precondition: no active bet (G1), chosen ordinary build node (never `outcome_kind: specification`), and cleared **Definition-of-Ready** (os/plays/converge.md).

## Steps

1. **Recite** — restate the node's goal and done_when, and its parent's goal. If the node's goal is an activity rather than an outcome, fix it first.
2. **Appetite first** — ask or propose: how much time is this outcome worth (not how long it takes)? Fix appetite before any solution talk (gate G3). Outside-view check: name 1–3 comparables; on conflict trust them.
3. **Approaches, then minimal solution** — before sketching anything, name 2–3 structurally different ways to satisfy done_when within appetite (different mechanism, not different size — build / fake-or-reuse / make-most-work-unnecessary), each with the one assumption it bets on. If he brought an approach, generate alternatives first, then rank all on equal footing. Pick one with a one-line why-over-the-others; losing approaches go to captures. Then sketch the smallest version of the chosen approach. Explicitly state what this version does NOT include.
4. **Scope hammer** — challenge every element: "what breaks if we cut this?" Cut until something genuinely hurts. Incoming `open` converge rows become cuts or `→ PLAN` lines, never the cut itself; an owner-owed one needs his word first. Record the cut list (≥1 real cut — gate G6); cuts go to `parked` or captures, not into the bet.
5. **Lens sweep** — for each lens in CHARTER.md: does this bet need work from this lens? Verdict per lens: a task, or `not_needed: <reason>` (gate G6). Silent skipping is invalid.
6. **Riskiest assumption** — list the assumptions this bet rests on, starting with the chosen approach's bet from step 3, ranked by kill-power. The top one gets a task that tests it as early and cheaply as possible (gate G6). Calibrate test depth to the charter's risk_posture.
7. **Tasks** — 3–7 tasks, each ≤ half a focused day, each with verifiable done_when. Order them so the riskiest-assumption task comes first or near-first. Mark each task's kind: session, executor (engineering), or guide (os/plays/guide.md). Executor-heavy bets name the evaluator and rollback first. ≥2 independent lines of work → offer the owner lanes and their WIP limit (G7).
8. **Kill criteria** — kill_by: metric + threshold + date (gate G4). If the bet reaches the date or breaches the threshold, review triggers automatically. State next_if_true / next_if_false — which branch opens, dies, or mutates either way.
9. **Close** — show one screen: appetite, tasks, lanes, cuts, lens verdicts, kill_by, forecast and against. On approval, RESULT makes the node `active`, writes the bet, declares any lanes the owner named in exact words, registers its first-task CALL as a `call` card, and hands it off through `RESULT.next`.

## Done when

NOW.md names an approved bet whose `bet` card passes G1–G6; its first-task CALL is a `call` card and in local `RESULT.next`.

## Notes

- Shape is one session — or two when appetite exceeds a week: close with a checkpoint once approaches are on the table; choose in the next session (≥1 night). If shaping stalls on an unknown, spawn `call:research` and close awaiting its return — do not pad the bet with guesses.
- Shaping a node may reveal it needs children instead of tasks (too big for one appetite). Then: split into 2–4 child outcome `node` cards (each with its why, owner-approved in-session — G9), recommend which child to shape, close — a valid result. Recursion happens here, on demand, never in advance.

END_OF_FILE: os/plays/shape.md
