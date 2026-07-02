# Play: pulse

Purpose: the recurring sweep (weekly by default) that keeps the system trustworthy. The only play that looks across all directions at once.

Reads: every direction's NOW.md + TREE.md headers + LOG.md tail; os/FRICTION.md.
Writes: NOW.md of affected directions, LOG.md, knowledge/ staleness marks.

## Checklist — every item is a boolean, report all of them

Per direction:

1. **Decisions** — is the decision inbox empty? If not: re-surface to the owner in one batch, with recommendations.
2. **Liveness** — does the active bet have a next task ready? If the direction has no active bet and no pending decision: flag as idle, propose shape or explicit pause.
3. **Kill dates** — any kill_by date passed or threshold breached? → trigger a review CALL (do not review here).
4. **NOW hygiene** — is NOW still hot state (no closed open_calls, answered decisions, prose next, or archive-scale bloat)? If drifted, propose a repair CALL; do not compact here.
5. **Blocked & in-flight** — any task blocked longer than its unblock condition suggests, or open_calls entry older than its budget? Propose: nudge, re-issue, or drop.
6. **Captures** — triage capture backlog: each becomes a parked node, merges into an existing node, or is dropped. Captures don't accumulate beyond one pulse.
7. **Parking lot** — anything parked that current learnings make urgent, or that has been parked so long it should be dropped? Propose, don't decide.
8. **Recurring** — any recurring obligation past its cadence (today vs last_done)? → put its ready work CALL into the decision batch. Pulse never executes recurring work itself.

Global:

9. **WIP across directions** — how many directions had sessions since last pulse? If owner attention is spread thinner than 2–3 directions, recommend which to pause (Little's law applies to the owner too).
10. **Knowledge staleness** — any knowledge entry past its relevance (check `read_by` and dates)? Mark stale.
11. **Friction** — any os/FRICTION.md point with ≥2 entries? Recommend one maintenance session (and nothing more).
12. **Market contact** (per direction with an active bet) — were decisions since last pulse checked against at least one external signal (market/audience numbers, live users), with the number cited?

## Close

RESULT: the boolean report, batched decisions_needed across directions, state_changes for triage, log line per affected direction, next = the single most urgent CALL across all directions.

## Done when

All twelve items have explicit answers; the owner has one consolidated decision batch.

## Notes

- Pulse never does object-level work and never reshapes bets — it routes.
- Keep the report on one screen: twelve lines plus the decision batch.

END_OF_FILE: os/plays/pulse.md
