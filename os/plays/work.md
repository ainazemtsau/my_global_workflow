# Play: work

Purpose: execute one active-bet task, recurring obligation, or bounded parallel-track CALL.

Reads: NOW.md (always); files the CALL points to.
Writes: NOW.md (task/call status), LOG.md, work/ artifacts via state_changes.

## Steps

1. **Recite** — restate the CALL's goal/done_when and the bet, recurring obligation, or approved parallel scope it serves. If obsolete or blocked, close with that finding — it is valid.
2. **Owner inputs (owner)** — is the artifact owner-content: something the owner will personally live by, operate, or send as his own (his food, training, schedule, money, his voice)? No → one line why, move on. Yes → before any drafting, ask the questions only the owner can answer for this artifact (preferences, constraints, tastes, current reality), reuse what state already answers (CHARTER owner_edges, knowledge/), build the draft from those answers, and return it to him in-session for fix-or-accept. The artifact names its basis: owner inputs, state pointers, external sources. Substance the owner could google without the OS is filler, not a product. Owner unreachable → task blocked, not guessed.
3. **Do the work** — this is an ordinary working conversation: drafting, analyzing, deciding, producing. The session is the specialist (marketer, designer, analyst — whatever the task needs).
   - Engineering or repo execution → `call:executor` with a full CALL (goal, context, boundaries, done_when, return, budget). The session frames the outcome and evidence pointers; it never designs the solution — architecture is the contour's PLAN, where the owner participates. Close awaiting HOME; only a later Direction RESULT issues a downstream CALL.
   - A bounded side question → `call:research`.
   - Ideas and discovered work → `capture`, one line each. Never expand scope in-session (the bet's cut list is law).
4. **Self-check** — compare the actual output against done_when point by point. Evidence is the artifact itself (file in work/, executor's commits/PR + checks), not a claim. Owner-content: every major element traces to an owner input or a named source — untraceable generic filler fails this check.
5. **Close** — RESULT: outcome, evidence, task/call disposition, captures, decisions, log line, next = one ready continuation; the last bet task routes to review. Preserve unrelated calls/tracks.

Here `ready` means self-contained; status may be `waiting|blocked|paused`.

## Done when

The CALL's done_when is met with evidence, or it closes blocked/obsolete with the reason recorded.

## Notes

- One CALL per session; each track has ≤1 root. If it splits, RESULT proposes one same-position continuation plus bounded same-track children parented to it; do not silently do both.
- Track add without TREE uses work; TREE-backed add routes map. A met parallel root, retirement, or primary handoff routes review; cite owner words.
- Two-strikes rule applies: after two failed correction rounds, close with a handoff note and let a fresh session continue.
- Waiting on a human-world event (playtest answers, an email reply) is normal: close with task → blocked and the unblock condition in NOW.md. The pulse play watches blocked items.
- A work CALL may target a recurring obligation (`recurring: r-N` instead of `task:`): same lifecycle, evidence per its done_when; the RESULT updates `last_done` instead of a task status. If it can't finish, close with the reason — `last_done` stays, pulse re-raises it.
- Long task, platform switch, or a degrading session: close with a checkpoint RESULT — partial outcome, task stays active with a progress note, next = continuation CALL. A fresh session anywhere resumes from it.
- Any CALL you issue (child, executor) keeps this CALL's track and goes into state_changes with track/status for NOW.md → open_calls; unrelated call ids/default survive.

END_OF_FILE: os/plays/work.md
