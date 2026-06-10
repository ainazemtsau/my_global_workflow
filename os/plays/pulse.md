# Play: pulse

Purpose: the recurring sweep (weekly by default) that keeps the system trustworthy. The only play that looks across all directions at once.

Reads: every direction's NOW.md + TREE.md headers + LOG.md tail; os/FRICTION.md.
Writes: NOW.md of affected directions, LOG.md, knowledge/ staleness marks.

## Checklist — every item is a boolean, report all of them

Per direction:

1. **Decisions** — is the decision inbox empty? If not: re-surface to the owner in one batch, with recommendations.
2. **Liveness** — does the active bet have a next task ready? If the direction has no active bet and no pending decision: flag as idle, propose shape or explicit pause.
3. **Kill dates** — any kill_by date passed or threshold breached? → trigger a review CALL (do not review here).
4. **Blocked items** — any task blocked longer than its unblock condition suggests? Propose: nudge, drop, or re-route.
5. **Captures** — triage capture backlog: each becomes a parked node, merges into an existing node, or is dropped. Captures don't accumulate beyond one pulse.
6. **Parking lot** — anything parked that current learnings make urgent, or that has been parked so long it should be dropped? Propose, don't decide.

Global:

7. **WIP across directions** — how many directions had sessions since last pulse? If owner attention is spread thinner than 2–3 directions, recommend which to pause (Little's law applies to the owner too).
8. **Knowledge staleness** — any knowledge entry past its relevance (check `read_by` and dates)? Mark stale.
9. **Friction** — any os/FRICTION.md point with ≥2 entries? Recommend one maintenance session (and nothing more).

## Close

RESULT: the boolean report, batched decisions_needed across directions, state_changes for triage, log line per affected direction, next = the single most urgent CALL across all directions.

## Done when

All nine items have explicit answers; the owner has one consolidated decision batch.

## Notes

- Pulse never does object-level work and never reshapes bets — it routes.
- Keep the report on one screen: nine lines plus the decision batch.

END_OF_FILE: os/plays/pulse.md
