# Play: guide

Purpose: side-by-side execution — the OWNER operates a tool the agents cannot reach (Blender, a game-engine editor, a DAW, hardware, the physical world); the session instructs step by step, verifies by screenshots, adapts.

Reads: NOW.md (always); the CALL; the owner's screenshots and answers in-session.
Writes: NOW.md (task status), LOG.md via state_changes.

## Steps

1. **Recite** — restate the goal, done_when, and ask once: the owner's skill level with this tool. Calibrate instruction granularity to it.
2. **Path** — lay out 3–7 checkpoints from the current state to done_when. Show the path before starting.
3. **Per checkpoint, loop:** ONE action at a time → the owner does it → the owner confirms with a screenshot or a short answer → verify against the expected state. On mismatch: diagnose from the screenshot and adjust. Two failed adjustments on the same step → propose an alternative route, or close the checkpoint as blocked (two-strikes, KERNEL §2).
4. **Evidence** — the owner's confirmation per checkpoint plus a final screenshot or artifact. done_when decides, not the session's impression.
5. **Close** — RESULT: outcome, evidence, task status only, captures (ideas and problems seen along the way), log line, next. If this marks the last open/active task done or kill_by is breached, next = review CALL for the same node; guide never edits TREE.md, closes the bet, or activates another node. Future-system ideas go to captures/decisions, not immediate execution.

## Done when

The CALL's done_when is met and the owner confirmed it, or a checkpoint is blocked with the reason recorded.

## Notes

- Never batch several actions into one instruction: the owner's hands are both the bottleneck and the error surface.
- A guide CALL is a normal task inside the active bet (G2 applies); shape marks such tasks as guide work.
- Engineering reports (VALIDATION G6) may emit a guide CALL for non-trivial manual acceptance or setup steps instead of a flat instruction list.

END_OF_FILE: os/plays/guide.md
