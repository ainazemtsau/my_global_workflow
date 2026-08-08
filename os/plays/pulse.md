# Play: pulse

Purpose: recurring sweep (weekly by default) that keeps every direction trustworthy. The only play that looks across directions.

Reads: each direction's NOW.md and cards/, CHARTER header, recent card journals and `git log`; os/FRICTION.md.
Writes: NOW.md pointer and cards of affected directions with their journal lines, knowledge staleness marks.

## Checklist — report every item

Per direction:

1. **Decisions** — batch every pending owner choice with recommendations.
2. **Objective/liveness** — at most one active bet; if one exists, does it have a ready task/CALL? Do all non-recurring lanes serve it, fit WIP and have one root/decision with valid child graph? No bet means no non-recurring lane; an idle direction gets its planning route, not fake work.
3. **Kill dates** — passed appetite/kill_by or invalidating evidence → review CALL.
4. **Hot-state hygiene** — schema-only compact state; pending-only calls/decisions/issues; valid artifacts/statuses; forecast well-formed; no retired selector/controller residue. Drift → repair.
5. **Blocked/outstanding** — calls beyond budget/condition, paused against current intent, waiting without live receipt, or running beyond budget? Recommend check, nudge, cancel, pause or drop; never infer progress/reset/relaunch.
6. **Issues & captures** — every issue has route owner, review trigger and evidence pointer; due items are resolved, merged, promoted through the owning play, or explicitly dropped. Triage new captures into a parked node, issue, merge or drop. Neither queue accumulates without a next review event.
7. **Roadmap** — future objectives stay visible and outcome-level. Anything newly urgent or permanently irrelevant? Propose; don't decide.
8. **Recurring** — overdue obligation → ready work CALL in the decision batch; pulse never executes it.
9. **Forecast** — is the dated target/basis current after material evidence? Numeric chance without cited empirical calibration, ritual daily movement, or stale trigger → replace recommendation with `no_basis`/review; pulse does not manufacture a number.

Global:

10. **WIP across directions** — limits/occupancy and ready/running/waiting/blocked/paused by execution lane. Recommend pauses when owner attention is spread thin.
11. **Knowledge staleness** — mark entries stale when their `read_by`/evidence no longer applies.
12. **Friction** — ≥2 matching entries → recommend one maintenance session.
13. **Market contact** — for each active bet, did recent decisions touch a cited external signal? Report honestly.

## Close

RESULT carries the report, batched decisions, exact triage state_changes and one log line per affected direction; `awaiting_decision` if needed, else `return-to-owner`. Never select unrelated work.

## Done when

All thirteen items have explicit answers and the owner has one consolidated decision batch.

## Notes

- Pulse routes; it never executes or reshapes a bet.
- Keep the rendered report compact; evidence stays behind pointers.

END_OF_FILE: os/plays/pulse.md
