# Play: repair

Purpose: restore a trustworthy hot-state NOW.md when state contradicts reality or schema hygiene drift makes the entrypoint unreliable. Desync is expected, not exceptional — repair is cheap by design.

Triggers: a session's CALL contradicts NOW.md; NOW.md contradicts TREE.md or visible evidence; audit/pulse flags NOW hygiene drift; a session was interrupted and its RESULT lost; the owner says "this is wrong".

Reads: NOW.md, TREE.md, LOG.md tail, recent history/ files, git log of the direction, work/ artifacts.
Writes: NOW.md, LOG.md (a repair entry naming what diverged), optional `work/` snapshot artifact.

## Steps

1. **Name the contradiction** — state exactly what disagrees with what, in two lines.
2. **Reconstruct** — newest-first through LOG.md, history/, git commits, and artifacts: what actually happened? Artifacts and commits outrank log lines; log lines outrank memory of prior chats; prior chat content is the weakest evidence (authority order of the kernel applies). For hygiene drift, separate current truth from archive text.
3. **Propose corrected state** — a corrected NOW.md (and TREE.md statuses if needed) with a one-line justification per change. For NOW compaction, first save the full pre-repair NOW as a `work/` snapshot, then keep only hot state plus one-line pointers to LOG/history/work. Anything unrecoverable becomes an explicit open question, not a guess.
4. **Confirm** — show the diff to the owner (gate G7: this is one batched decision). On approval, RESULT applies it.
5. **Friction** — if the desync came from a hole in the OS (not a one-off accident), add one line to os/FRICTION.md.

## Done when

NOW.md matches reality and the NOW hygiene rules to the owner's confirmation, and the divergence cause is logged.

## Notes

- Repair never invents progress: when in doubt, mark a task open rather than done. Optimistic repair is worse than lost work.
- If repair recurs in the same spot twice, that's a friction pattern — flag it in step 5 rather than silently fixing again.

END_OF_FILE: os/plays/repair.md
