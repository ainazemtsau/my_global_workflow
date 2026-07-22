# Play: pulse

Purpose: the recurring sweep (weekly by default) that keeps the system trustworthy. The only play that looks across all directions at once.

Reads: every direction's NOW.md + CHARTER.md/TREE.md headers + LOG.md tail; os/FRICTION.md.
Writes: NOW.md of affected directions, LOG.md, knowledge/ staleness marks.

## Checklist — every item is a boolean, report all of them

Per direction:

1. **Decisions** — is the decision inbox empty? If not: re-surface to the owner in one batch, with recommendations.
2. **Liveness** — does the primary bet have a ready task/CALL, does track WIP fit its limit, and does every current track have one ordinary root or decision with no orphan child/outcome request or request with a paused endpoint? No active bet/tracks/decision → flag idle; an empty track or false-ready call → repair.
3. **Kill dates** — any kill_by date passed or threshold breached? → trigger a review CALL (do not review here).
4. **Hot-state hygiene** — is NOW still hot state (no closed calls, answered decisions, prose notes)? In track-mode: unique call/track ids, valid statuses/artifacts, tracked decisions, ready default when possible; legacy: valid CALL/pointer/decision next. Are all hot files within the schema ceiling and template? Drift → repair, never compact here.
5. **Blocked & outstanding** — any task/call blocked beyond its condition or older than budget, paused without current owner intent, waiting without a live receipt, or outcome request past its useful date? Propose: nudge, re-issue, expire, pause, or drop; never silently start another track's successor.
6. **Captures** — triage capture backlog: each becomes a parked node, merges into an existing node, or is dropped. Captures don't accumulate beyond one pulse.
7. **Parking lot** — anything parked that current learnings make urgent, or that has been parked so long it should be dropped? Propose, don't decide.
8. **Recurring** — any recurring obligation past its cadence (today vs last_done)? → put its ready work CALL into the decision batch. Pulse never executes recurring work itself.

Global:

9. **WIP across directions/tracks** — report each limit/occupancy and ready/waiting/blocked/paused calls grouped by track. If attention is spread too thin, recommend tracks/directions to pause; do not hide intra-direction WIP behind one direction count.
10. **Knowledge staleness** — any knowledge entry past its relevance (check `read_by` and dates)? Mark stale.
11. **Friction** — any os/FRICTION.md point with ≥2 entries? Recommend one maintenance session (and nothing more).
12. **Market contact** (per direction with an active bet) — were decisions since last pulse checked against at least one external signal (market/audience numbers, live users), with the number cited?

## Close

RESULT: the boolean report, batched decisions_needed across directions, state_changes for triage, log line per affected direction, next = the selected default CALL without deleting other calls.

## Done when

All twelve items have explicit answers; the owner has one consolidated decision batch.

## Notes

- Pulse never does object-level work and never reshapes bets — it routes.
- Keep the report on one screen: twelve lines plus the decision batch.

END_OF_FILE: os/plays/pulse.md
