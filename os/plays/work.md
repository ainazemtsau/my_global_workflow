# Play: work

Purpose: execute one active-bet task, recurring obligation, or bounded parallel-track CALL.

Reads: NOW.md (always); files the CALL points to.
Writes: NOW.md (task/call status), LOG.md, work/ artifacts via state_changes.

## Steps

1. **Recite** — restate the CALL's goal/done_when and the bet, recurring obligation, or approved parallel scope it serves. If obsolete or blocked, close with that finding — it is valid.
2. **Owner inputs (owner)** — if the owner will live by, operate, or send the artifact, ask only owner-only facts before drafting; reuse state and return the draft for fix-or-accept. Cite inputs, state and sources. Otherwise say why. Googleable filler fails; unavailable owner → blocked.
3. **Do the work** — draft, analyze, decide or produce as the task's specialist.
   - Engineering or repo execution → `call:executor` with a full CALL (goal, context, boundaries, done_when, return, budget). The session frames the outcome and evidence pointers; it never designs the solution — architecture is the contour's PLAN, where the owner participates. Close awaiting HOME; only a later Direction RESULT issues a downstream CALL.
   - A bounded side question → `call:research`.
   - Ideas and discovered work → `capture`, one line each. Never expand scope in-session (the bet's cut list is law).
4. **Self-check** — compare the actual output against done_when point by point. Evidence is the artifact itself (file in work/, executor's commits/PR + checks), not a claim. Owner-content: every major element traces to an owner input or a named source — untraceable generic filler fails this check.
5. **Close** — RESULT: outcome, evidence, disposition, captures, decisions and log. Ordinary work names one ready continuation (last bet task → review); an outcome request issues none and uses `return-to-requester <track-id>`. Preserve unrelated calls/tracks.

Here `ready` means self-contained; status may be `running|waiting|blocked|paused`.

## Done when

The CALL's done_when is met with evidence, or it closes blocked/obsolete with the reason recorded.

## Notes

- One CALL per session; each track has ≤1 ordinary root. If it splits, RESULT proposes one same-position continuation plus bounded same-track children parented to it; do not silently do both.
- Track add without TREE uses work; TREE-backed add routes map. A met parallel root, retirement, or primary handoff routes review; cite owner words.
- Two strikes: after two failed corrections, close with a handoff to a fresh session.
- Waiting on a human-world event is normal: close blocked with its unblock condition; pulse watches it.
- A work CALL may target a recurring obligation (`recurring: r-N` instead of `task:`): same lifecycle, evidence per its done_when; the RESULT updates `last_done` instead of a task status. If it can't finish, close with the reason — `last_done` stays, pulse re-raises it.
- Long task, platform switch, or degradation: checkpoint; keep it active and issue a continuation.
- Issued CALLs stay in-track and enter state_changes. Exception: an authorized root's outcome request; target clears it, receipts both roots, changes no target plan/status, returns only `ACCEPT|COUNTER|BLOCKED`.
- An `outcome_dispatch` root controls a cycle, not a serial task. Preserve the owner-named outcome until changed; rank direct progress/unblock above receipt recency. Administrative close is background unless blocking. Owner launch/loss words may only change matching CALL status. Show one screen: `focus / running / launch now` (0..N collision-free items with surface, paste text and exit) `/ on return`. Its same-track continuation is a ready refill, never a work quota or wait on one foreign result. Read relevant surfaces only; keep strategy stable, event detail in history, and batch housekeeping.

END_OF_FILE: os/plays/work.md
