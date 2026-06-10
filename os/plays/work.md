# Play: work

Purpose: execute exactly one task of the active bet.

Reads: NOW.md (always); files the task's CALL points to.
Writes: NOW.md (task status), LOG.md, work/ artifacts via state_changes.

## Steps

1. **Recite** — restate the task's goal and done_when, and the bet it serves. If the task is already obsolete or blocked, say so and close with that finding — that is a valid result.
2. **Do the work** — this is an ordinary working conversation: drafting, analyzing, deciding, producing. The session is the specialist (marketer, designer, analyst — whatever the task needs).
   - Engineering or repo execution → `call:executor` with a full CALL (goal, context, boundaries, done_when, return, budget). Close the session awaiting the return, or continue other steps of the same task if they don't depend on it.
   - A bounded side question → `call:research`.
   - Ideas and discovered work → `capture`, one line each. Never expand scope in-session (the bet's cut list is law).
3. **Self-check** — compare the actual output against done_when point by point. Evidence is the artifact itself (file in work/, executor's commits/PR + checks), not a claim.
4. **Close** — RESULT: outcome, evidence, task → done (or blocked with reason), captures, decisions if any, log line, next = CALL for the next task in the bet, or for review if this was the last task or kill_by is breached.

## Done when

The task's done_when is met with evidence, or the task is closed as blocked/obsolete with the reason recorded.

## Notes

- One task per session. If the task turns out to be two, close it as "split needed" and let the RESULT propose the split — the writer updates NOW.md; do not silently do both.
- Two-strikes rule applies: after two failed correction rounds, close with a handoff note and let a fresh session continue.
- Waiting on a human-world event (playtest answers, an email reply) is normal: close with task → blocked and the unblock condition in NOW.md. The pulse play watches blocked items.
- A work CALL may target a recurring obligation (`recurring: r-N` instead of `task:`): same lifecycle, evidence per its done_when; the RESULT updates `last_done` instead of a task status. If it can't finish, close with the reason — `last_done` stays, pulse re-raises it.
- Long task, platform switch, or a degrading session: close with a checkpoint RESULT — partial outcome, task stays active with a progress note, next = continuation CALL. A fresh session anywhere resumes from it.
- Any CALL you issue (child, executor) goes into state_changes for NOW.md → open_calls, so the in-flight picture survives this chat.

END_OF_FILE: os/plays/work.md
