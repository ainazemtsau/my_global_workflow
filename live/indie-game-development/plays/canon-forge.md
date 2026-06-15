# Play: local/canon-forge

Purpose: forge ONE canon question (world / lore / story / mechanic / visual) from open to frozen — owner-chosen direction, drafted, gated by craft, optionally illustrated with consistent images — producing one official canon card in the canon repo and growing the question-graph. Lore is CO-CREATED: the AI proposes options, the owner decides; the AI never freezes invented canon.

Reads: the canon repo (the chosen question note + its frozen parent canon + `maps/StyleBible.md` design-map + the area MOC), `knowledge/` craft-gate checklists (narrative / intrigue / world / mechanic / art), TREE.md (node `g-d3a8`), CHARTER.md (lenses).
Writes: the CANON REPO — the frozen card (text + chosen images + frontmatter `status / depends_on / images[] / gate{}`), the `rejected_alternatives` tail, the new child questions, the area MOC. In OS state: `LOG.md` (one line); PROPOSES cross-cutting canon facts to `knowledge/` (with `read_by:`) for review/pulse — never writes `knowledge/` directly. Does NOT touch `NOW.md` or the active bet (canon is never a second active bet — G1).

Precondition: a question chosen from `local/canon-status` actionable set (all `depends_on` already `frozen`). Canon runs PARALLEL to the build bet, not as a second active bet. Reached via CALL `to: session, play: local/canon-forge` — one question per session (one chat = one job).

## Steps
1. **Frame** — restate the exact question + inherit the frozen parent canon it must not contradict (cite parent ids). Name the area.
2. **Diverge (owner)** — propose 3 distinct directions (different premise/tone), cross-family where useful. The owner picks one, mixes, or steers in his own words. The AI never freezes invented lore. `(owner)`
3. **Draft** — write the chosen answer as a canon entry: invariants on top, prose below; atomic (one idea, AI-payload-friendly).
4. **Gate** — run the relevant craft checklist(s) from `knowledge/`: consistency, intrigue (iceberg has a written bottom), not-contrived, hooks, co-op interdependence (for mechanics), tone (King terror>horror). Refute cross-family. A fail returns to step 3.
5. **Illustrate — where it fits (encouraged, not forced)** — images are first-class for the owner's visual sense, but not every node needs one and early talk-through nodes (North Star, base world) stay text-only. When it fits: the ASSISTANT writes the prompt (from `StyleBible.md` + plates; pick the KIND — default = gameplay screenshot, else mascot / realistic per StyleBible), the owner generates a SET in ChatGPT (GPT Image) and picks; commit chosen PNGs under `/assets` (lowercase-hyphenated, relative refs) and reference them in the card. Images are an approximation / visual target, not final. BLOCKED until `StyleBible.md` is frozen (style is defined first).
6. **Freeze & grow (owner)** — owner signs → set `status: frozen`; log the dropped directions as the card's `rejected_alternatives`; spawn the child questions this answer forces (new notes with `depends_on`); update the area MOC. `(owner)`

## Done when
One frozen canon card (text + any chosen images) committed in the canon repo; the craft gate passed (or a fail bounced and re-passed); child questions spawned; a `LOG.md` line written; any cross-cutting fact proposed to `knowledge/` with `read_by:`. The owner's sign is recorded (his words).

## Notes
- Co-creation is binding: steps 2 and 6 are `(owner)` — invented lore never freezes without his words (G9 spirit for canon content).
- Setting before style: ordering lives in the graph's `depends_on` (the Visual Style node depends on a first slab of world); this play just forges whichever question is actionable.
- The canon TEXT is the source of truth; images are presentation. Consistency comes from the design-map + plates, never from seeds.
- AI imagery is internal/concept only — never into public marketing (standing policy).

END_OF_FILE: live/indie-game-development/plays/canon-forge.md
