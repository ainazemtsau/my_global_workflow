# Play: local/marketing-status

Purpose: render the marketing question-graph so the owner sees, at a glance, what to work on next — RENDER-ONLY, changes nothing (KERNEL §2 read-only exception). The "one chat shows the next step" surface for the marketing track.

Reads: work/marketing/board.md + every card (frontmatter id / type / status / depends_on / cross_track), work/marketing-track-design-2026-06-16.md.
Writes: nothing. No RESULT, no state change.

Precondition: invoked by the owner (`marketing-status`). A read-only command, not a state-changing CALL.

## Steps
1. **Load the graph** — read every card + its depends_on + any open cross_track request from work/marketing/.
2. **Compute (Kahn topo-sort)** — per open card, in-degree = depends_on not yet frozen + open cross_track requests (entries with `status: open`; an entry counts only while open — when the upstream track freezes the answer the owner flips it to `satisfied` and the card recomputes). Actionable now = in-degree 0. Blocked = in-degree >0 (name the blocker: a sibling card, or an open canon/dev request). Parallelizable = the actionable antichain. A cycle = a contradiction → flag it.
3. **Render** (group by area):
   - ✅ frozen
   - ▶️ actionable now — take any in a fresh chat under `local/marketing-forge`
   - 🔀 parallelizable — safe to run at once
   - ⏳ blocked — and by what
   - 📤 cross-track requests open — waiting on canon or dev (name each + what it unblocks)
   - ⚠️ blind spots — orphan cards, dangling depends_on, cycles
4. **Recommend** one next step — and note the engine bet (`g-9c41`) stays the priority; marketing fills parallel capacity.

## Done when
The state is rendered to the owner; nothing is written.

## Notes
- The graph lives in work/marketing/, not in NOW.md — so this never touches the build bet.
- Read-only by construction: it cannot break anything.

END_OF_FILE: live/indie-game-development/plays/marketing-status.md
