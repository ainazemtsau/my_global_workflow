# Play: map

Purpose: co-create/revise the owner-approved goal tree (G9).

Reads: CHARTER.md, TREE.md, NOW.md; latest map_evidence; owner-named sources.
Writes: TREE.md, NOW.md (open_calls), LOG.md.

Trigger: after frame; «перепланируем карту»; or a review harvest demands restructuring beyond small updates.

Roadmap-node fast path: one bounded child under an approved parent; reuse evidence, skip skeleton/search/lens sweep with reasons, get G9 approval. At capacity, first owner-approve a drop/merge.

## Steps

1. **Recite** — restate mission and success criteria in plain words, and the current tree state.
2. **Candidates & evidence (owner)** — ask the owner for his candidates in one line; nothing is shown until he answers or explicitly waives (human-first — anti-anchoring, not priority). Map then needs a fresh `map_evidence` RESULT (research play) — spawn it and checkpoint if missing — unless the owner explicitly waives. Search-first may be added on top (G7 decision; cost: 2–3 parallel chats): name the baseline path a competent default team would take and why it likely loses, then spawn 2–3 independent strategic_search children (briefs and survivor rules: research play).
3. **Skeleton (owner)** — before any full card, show the whole proposed map on one screen — 3–6 one-liners (working goal + why), tagged `owner` / `gap-fill:<lens>` / `non-obvious` / `evidence` / `search`, in proposed order — and get his reaction to coverage, order, gaps. Owner lines get no automatic priority or position — equal footing (Berg). Orientation, not approval: G9 verdicts stay per-card.
4. **Cards** — elaborate survivors one at a time from evidence/captures/owner sources:
   - goal (an outcome in the world, not an activity)
   - done_when (verifiable)
   - **why — exactly how this node leads to the root's success criteria**
   - edge — why this owner/AI setup specifically (cite a charter edge), and why an incumbent won't follow
   - risk — what would kill or invalidate it
   - `outcome_kind: specification` only when the versioned owner-approved specification itself exhausts done_when; otherwise omit it (ordinary build outcome)
   At least one card must offer a non-obvious path to the success criteria — how comparable ambitions were actually reached, not another slice of the textbook chain. Seed it from exactly one rare example — an outlier win or far analogy, not a moodboard of domain hits. If no viable alternative exists, say so in one line. Acceptance check: with the direction's nouns replaced by placeholders a card must stop reading useful — otherwise anchor it in an edge, state fact, or named evidence.
5. **Per-node verdict (owner)** — accept / edit / reject, one card — one verdict, no silent batch acceptance. Rejections are recorded with reason (parked or dropped).
6. **Order (owner)** — confirm the order, adjusted by verdicts: what unblocks what, riskiest assumption first.
7. **Depth check** — top level only (rolling wave, G2). Deeper splits happen later, in shape.
8. **Lens sweep on the map** — does the tree cover every charter lens? For each gap: propose a node or an explicit `not_needed: reason`.
9. **Close (owner)** — after G9, save TREE + log; offer 2–3 first nodes. No choice → `awaiting_decision`. A chosen specification outcome opens one untracked owner-authority `work` CALL while staying parked; any other choice uses KERNEL §2 readiness. Never create execution lanes.

## Done when

TREE.md holds an owner-approved tree; every non-root node has its why; RESULT.next hands off specification-authoring or ordinary readiness.

## Notes

- Rerunnable anytime — revise, never recreate; done/dropped nodes stay as one-line history.
- Detail beyond why lives in the session history (`detail: history/<file>.md`).
- If the owner's answers reveal the charter is wrong, stop and route to frame — map does not edit CHARTER.md.

END_OF_FILE: os/plays/map.md
