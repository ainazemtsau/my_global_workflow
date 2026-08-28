# Play: day

Purpose: the owner's daily adviser and the sweep that keeps the direction trustworthy. Nothing is recorded until he says to save.

Reads: the `osctl context` working set (never the whole `cards/` folder), CHARTER.md, recent journals and `git log`, due issue evidence, knowledge whose `read_by` names day.
Writes after explicit save only: the `day` card, other cards with journal lines, issued CALL artifacts. Never CHARTER.md, node cards, or `owner_approved`.

## Steps

1. **Refresh reality** — fresh Git, then `osctl context` for the bet: target and hard dates, roadmap, objective, tasks/lanes, open issues/decisions, recent outcomes, forecast. Follow evidence pointers only where they change today's advice; never bulk-load history.
2. **His first** — before any brief: what waits for HIS word, and which dates are near with days left. He may defer; a deferred item stays and returns tomorrow.
3. **Derived brief** — plain Russian: what changed since the previous working day, where it stands, what is not on plan, key evidence and problems, chance of the dated target. `no_basis` is honest. No ids, enum labels or fixed questionnaire.
4. **Sweep** — report each item that has something to say, stay silent on the rest. One bet at most, and has it a ready task/CALL. Work past appetite, a breached kill_by or invalidating evidence → review; never elapsed time. Hot-state drift → repair. Calls beyond budget, paused against intent, or waiting without a live receipt → check, nudge, cancel, pause or drop; never infer progress. Every issue has route owner, trigger, evidence; due ones resolve, merge, promote or drop. New captures become `question`/`idea` cards or die named. Roadmap stays outcome-level. Overdue recurring → ready work CALL in the batch, never executed here. Forecast basis current, else `no_basis`. Knowledge whose `read_by` no longer applies → stale. ≥2 matching FRICTION entries → recommend one maintenance session. Did recent decisions touch a cited external signal. Propose; never decide, never reshape a bet.
5. **Advise** — one focus and 0..N collision-free starts. Every non-recurring start serves the active bet; without a bet, recommend the planning route, not legacy work. Name why, what is deliberately not done, and what would change the advice.
6. **Discuss** — challenge assumptions, compare alternatives, revise the plan in chat. Read-only; memory never overrides freshly read state.
7. **Save boundary (owner)** — only his exact words (`сохрани`, `запиши`, `запускай`) authorize the delta; cite them in `play_check`. A saved day writes the `day` card — focus, starts, deliberately-not, and what would change the advice — REPLACING yesterday's: past days stay in Git. Otherwise save only explicit issue/forecast/decision or launch-state changes, bounded CALLs inside the objective, or — at `bet: null` — one lawful untracked planning CALL. Mission → frame; roadmap → map; specification → owner-authority work/verify/review; activation → KERNEL §2; objective stop → review; contradiction → repair; OS defect → maintenance.
8. **Close** — a saved leg emits one RESULT, then writer apply/commit. A later owner turn may start another fresh day leg here. `закрываем день` ends it; unsaved discussion stays unsaved.

## Done when

He has a truthful operating view, what waits for him came first, the sweep answered every item that had something to say, and nothing was saved without his words.

## Notes

- The dashboard is the chat answer, derived each time; the `day` card holds only the agreed plan.
- Forecast is not completion percent; never rises by ritual.
- Absorbed `pulse` 2026-08-10 by owner decision: it ran once in 213 legs because nothing triggered it. The cross-direction view died with it — `day` sees one direction, and no play now looks across.

END_OF_FILE: os/plays/day.md
