# Play: repair

Purpose: restore trustworthy hot state when state contradicts reality/schema. Desync is expected; repair is cheap.

Triggers: CALL contradicts NOW; work is untracked/misclassified; lane/call/issue frontier is incomplete; cards contradict NOW or the evidence; audit flags hygiene drift; RESULT was lost; owner says "this is wrong".

Reads: NOW.md, cards/, CHARTER.md, card journals, recent history/git, named knowledge/work evidence.
Writes: cards/, NOW.md; node-card/CHARTER hygiene trims only with G9 approval; card journals; compact knowledge/local-play tombstones and work-surface retirement banners only when they remove false routing authority; optional unrecoverable-state snapshot.

## Steps

1. **Name the contradiction** - what disagrees with what, in two lines.
2. **Reconstruct** - newest-first through card journals/history/git/artifacts. Artifacts/commits outrank logs; logs outrank chat memory. Inventory: active bet, its tasks, every execution lane/root/child/status, pending decisions, unresolved issues, forecast basis, recurring work. No bet permits no non-recurring lane. Old independent strategies become explicit issues or cold evidence, never lanes by inertia.
3. **Propose corrected state** - one-line reason per change. Preserve every outstanding fact, but separate authority from evidence. A call or task overtaken by another closes `superseded` naming its successor (`card close --status superseded --superseded-by <id>`), never `dropped`: overtaken and abandoned are different facts, and this play is the only one that writes the difference. Each issue gets stable id, route owner, review trigger and pointer; each removed issue gets a disposition in history. Forecast becomes `no_basis` when calibration is absent. A knowledge/work/local-play surface that falsely claims current routing may receive only a compact reset boundary, stale tombstone or visible retirement banner: no new strategy/content, and prior bytes remain in Git. For hot-file bloat, keep schema fields/pointers only; Git/history already preserve committed detail. Save a work snapshot only if content is genuinely unrecoverable elsewhere.
4. **Confirm (owner)** - show one batched diff; apply only after explicit approval. CHARTER/node-card semantic changes route to frame/map/review, not repair.
   **Removal boundary.** Removing, retiring or tombstoning one of these needs the owner's words naming THAT surface: a local play, an execution lane, an open call, a knowledge entry, or the approved status of an artifact he signed. General agreement with a cleanup is not that permission. Hygiene needs none: dangling pointers, EOF trailers, dedup, schema-shape fixes. And if a surface is illegal ONLY because a rule changed after it was created, repair stops and asks — retroactive illegality is a question for the owner, never a licence to clear.
5. **Friction** - OS hole -> one FRICTION line; do not fix OS here.

## Done when

NOW matches reality/schema; any lanes serve the active bet; calls/decisions/issues/forecast are mutually consistent; false routing surfaces are visibly stale without lost evidence; other flagged hot files are within template; cause is logged.

## Notes

- Never invent progress. Uncertain work becomes an issue/open question, not done.
- Repair may retire obsolete dispatch state while preserving its artifacts/history.
- Repeated same-point repair is a friction pattern.

END_OF_FILE: os/plays/repair.md
