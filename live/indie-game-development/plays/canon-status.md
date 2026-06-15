# Play: local/canon-status

Purpose: render the current state of the canon question-graph so the owner sees, at a glance, what to work on next — RENDER-ONLY, changes nothing (KERNEL §2 read-only exception). The "one chat shows next step" surface.

Reads: the canon repo question notes (frontmatter `id / area / status / depends_on`), the area MOCs, `maps/StyleBible.md` (is the design-map frozen yet?).
Writes: nothing. No RESULT, no state change.

Precondition: invoked by the owner (`canon-status`, optionally an area filter). A read-only command, not a state-changing CALL.

## Steps
1. **Load the graph** — read every question note + its `depends_on` from the canon repo.
2. **Compute (Kahn topo-sort)** — per open question, in-degree = count of `depends_on` not yet `frozen`. Actionable now = in-degree 0. Blocked = in-degree >0 (name the blocker). Parallelizable = the actionable set that shares no open dependency (an antichain). A dependency cycle = a contradiction → flag it.
3. **Render** (group by area):
   - ✅ frozen (done)
   - ▶️ actionable now — take any in a fresh chat under `local/canon-forge`
   - 🔀 parallelizable — safe to run in separate chats at once
   - ⏳ blocked — and by what
   - 🖼 image-ready — text frozen AND `StyleBible.md` frozen → can illustrate
   - 📦 cluster fully frozen → ready to assemble an artbook chapter
   - ⚠️ blind spots — orphan notes, dangling `depends_on`, cycles, frozen mysteries with no recorded "bottom", un-paid setups
4. **Recommend** one next step — and note that the engine bet (`g-9c41`) stays the priority; canon fills parallel capacity.

## Done when
The state is rendered to the owner; nothing is written.

## Notes
- The graph lives in the canon repo, not in `NOW.md` — so this never touches the build bet.
- Read-only by construction: it cannot break anything.

END_OF_FILE: live/indie-game-development/plays/canon-status.md
