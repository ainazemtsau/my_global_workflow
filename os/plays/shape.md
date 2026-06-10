# Play: shape

Purpose: turn one tree node into the active bet — the planning ritual. This is where scope is cut and the next work becomes concrete.

Reads: CHARTER.md, TREE.md, NOW.md, relevant knowledge/.
Writes: TREE.md (the node), NOW.md (the bet), LOG.md.

Precondition: no active bet in this direction (gate G1), node chosen by owner or by review's accepted recommendation.

## Steps

1. **Recite** — restate the node's goal and done_when, and its parent's goal. If the node's goal is an activity ("do marketing") rather than an outcome ("500 wishlists"), fix it first.
2. **Appetite first** — ask or propose: how much time is this outcome worth (not how long it takes)? Fix appetite before any solution talk (gate G3). Sanity-check with the outside view: name 1–3 comparable past efforts; if inside-view sizing conflicts with comparables, trust the comparables.
3. **Minimal solution** — sketch the smallest version that satisfies done_when within appetite. Explicitly state what this version does NOT include.
4. **Scope hammer** — challenge every element: "what breaks if we cut this?" Cut until something genuinely hurts. Record the cut list (≥1 real cut — gate G6); cuts go to `parked` or captures, not into the bet.
5. **Lens sweep** — for each lens in CHARTER.md: does this bet need work from this lens? Verdict per lens: a task, or `not_needed: <reason>` (gate G6). Silent skipping is invalid.
6. **Riskiest assumption** — list the assumptions this bet rests on, ranked by kill-power. The top one gets a task that tests it as early and cheaply as possible (gate G6).
7. **Tasks** — 3–7 tasks, each ≤ half a focused day, each with verifiable done_when. Order them so the riskiest-assumption task comes first or near-first. Mark each task's kind: session work, executor work (engineering), or guide work (the owner operates a tool the agents can't reach — os/plays/guide.md).
8. **Kill criteria** — kill_by: metric + threshold + date (gate G4). If the bet reaches the date or breaches the threshold, review triggers automatically.
9. **Close** — show the bet to the owner in one screen: appetite, tasks, cut list, lens verdicts, kill_by. On approval, RESULT: node → `active`, NOW.md gets the bet, next = CALL for work on the first task.

## Done when

NOW.md contains an approved bet passing gates G1–G6; next CALL is ready.

## Notes

- Shape is one session. If shaping stalls on an unknown, spawn `call:research` and close awaiting its return — do not pad the bet with guesses.
- Shaping a node may reveal it needs children instead of tasks (too big for one appetite). Then: split into 2–4 child outcome nodes in TREE.md, recommend which child to shape, close. That is a valid shape result — recursion happens here, on demand, never in advance.

END_OF_FILE: os/plays/shape.md
