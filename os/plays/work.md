# Play: work

Purpose: execute one active-bet task, recurring obligation, or bounded execution-lane CALL.

Reads: NOW.md; files the CALL points to.
Writes: NOW.md task/call status, LOG.md, work/ artifacts through RESULT.state_changes.

## Steps

1. **Recite** — restate the CALL goal/done_when and the active bet or recurring obligation it serves. A non-recurring CALL outside the current bet is obsolete: close with that finding or route the problem to the issue register; never execute it as a parallel strategy.
2. **Owner inputs (owner)** — if the owner will operate, send or live by the artifact, ask only facts only he can know; reuse state and sources. Otherwise say why no owner input is needed.
3. **Do the work** — produce the bounded outcome as the task's specialist.
   - Product-repo execution → `call:executor` with goal, context, boundaries, done_when, return and budget. Direction frames outcome/evidence; product PLAN owns technical HOW.
   - Bounded side question → `call:research`.
   - Discovered ideas → captures. A material unrelated problem → issue with route/review trigger. Neither expands this leg.
4. **Self-check** — compare output with done_when point by point. Evidence is the artifact, commit/check output, or named verification — not a claim.
5. **Close** — RESULT records outcome, evidence, disposition, captures/issues, decisions and log. Name one same-lane continuation when needed; last bet task → review. Preserve every unrelated lane/call.

`ready` means self-contained; a registered call may instead be `running|waiting|blocked|paused` with its required evidence/condition.

## Done when

The CALL done_when is met with evidence, or it closes blocked/obsolete with the reason preserved.

## Notes

- One CALL per leg; each lane has ≤1 ordinary root. A split produces one same-position continuation plus bounded same-lane children.
- Tracks are execution lanes under the active bet, never future goals. Creating/retiring a lane needs cited owner words; a future objective stays in TREE.
- Long work or platform degradation checkpoints into a continuation.
- A recurring CALL updates `last_done` only when evidence is complete.
- Waiting on a human-world event is normal; pulse watches it.
- Two failed correction rounds → checkpoint and fresh session.

END_OF_FILE: os/plays/work.md
