# Play: map

Purpose: build/revise the goal tree WITH the owner; nothing enters without approval (G9).

Reads: CHARTER.md, TREE.md, NOW.md; the latest map_evidence RESULT; evidence sources the owner names.
Writes: TREE.md, NOW.md (next), LOG.md.

Trigger: after frame; «перепланируем карту»; or a review harvest demands restructuring beyond small updates.

Track-add fast path: one map-child card (not a G8 root mission); reuse evidence, skip global skeleton/search/lens sweep with reasons, get owner approval (G9), and at capacity pause/retire first.

## Steps

1. **Recite** — restate mission and success criteria in plain words, and the current tree state.
2. **Candidates & evidence (owner)** — ask the owner for his candidates in one line; nothing is shown until he answers or explicitly waives (human-first — anti-anchoring, not priority). Map then needs a fresh `map_evidence` RESULT (research play) — spawn it and checkpoint if missing — unless the owner explicitly waives. Search-first may be added on top (G7 decision; cost: 2–3 parallel chats): name the baseline path a competent default team would take and why it likely loses, then spawn 2–3 independent strategic_search children (briefs and survivor rules: research play).
3. **Skeleton (owner)** — before any full card, show the whole proposed map on one screen — 3–6 one-liners (working goal + why), tagged `owner` / `gap-fill:<lens>` / `non-obvious` / `evidence` / `search`, in proposed order — and get his reaction to coverage, order, gaps. Owner lines get no automatic priority or position — equal footing (Berg). Orientation, not approval: G9 verdicts stay per-card.
4. **Cards** — elaborate surviving skeleton lines into cards, one at a time, drawing on map_evidence, frame captures, owner-named sources:
   - goal (an outcome in the world, not an activity)
   - done_when (verifiable)
   - **why — exactly how this node leads to the root's success criteria**
   - edge — why this owner/AI setup specifically (cite a charter edge), and why an incumbent won't follow
   - risk — what would kill or invalidate it
   At least one card must offer a non-obvious path to the success criteria — how comparable ambitions were actually reached, not another slice of the textbook chain. Seed it from exactly one rare example — an outlier win or far analogy, not a moodboard of domain hits. If no viable alternative exists, say so in one line. Acceptance check: with the direction's nouns replaced by placeholders a card must stop reading useful — otherwise anchor it in an edge, state fact, or named evidence.
5. **Per-node verdict (owner)** — accept / edit / reject, one card — one verdict, no silent batch acceptance. Rejections are recorded with reason (parked or dropped).
6. **Order (owner)** — confirm the order, adjusted by verdicts: what unblocks what, riskiest assumption first.
7. **Depth check** — top level only (rolling wave, G2). Deeper splits happen later, in shape.
8. **Lens sweep on the map** — does the tree cover every charter lens? For each gap: propose a node or an explicit `not_needed: reason`.
9. **Close (owner)** — owner approves the compact tree (G9). RESULT: TREE.md + log; normal map → shape CALL on recommended node (2–3 options); track-add map → accepted `parallel` node + track + one bounded work CALL, no tasks/appetite.

## Done when

TREE.md holds an owner-approved tree, every non-root node with its one-line why; the next CALL is ready.

## Notes

- Rerunnable anytime — revise, never recreate; done/dropped nodes stay as one-line history.
- Detail beyond the one-line why lives in the session's history file (`detail: history/<file>.md`).
- If the owner's answers reveal the charter is wrong, stop and route to frame — map does not edit CHARTER.md.

END_OF_FILE: os/plays/map.md
