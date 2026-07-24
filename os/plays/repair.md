# Play: repair

Purpose: restore trustworthy hot state when state contradicts reality/schema. Desync is expected; repair is cheap.

Triggers: CALL contradicts NOW; work is untracked/misclassified; lane/call/issue frontier is incomplete; NOW contradicts TREE/evidence; audit flags hygiene drift; RESULT was lost; owner says "this is wrong".

Reads: NOW.md, TREE.md, CHARTER.md, LOG tail, recent history/git, named knowledge/work evidence.
Writes: NOW.md; TREE/CHARTER hygiene trims only with G9 approval; LOG; compact knowledge/local-play tombstones and work-surface retirement banners only when they remove false routing authority; optional unrecoverable-state snapshot; optional LOG archive.

## Steps

1. **Name the contradiction** - what disagrees with what, in two lines.
2. **Reconstruct** - newest-first through LOG/history/git/artifacts. Artifacts/commits outrank logs; logs outrank chat memory. Inventory: active bet, its tasks, every execution lane/root/child/status, pending decisions, unresolved issues, forecast basis, recurring work. No bet permits no non-recurring lane. Old independent strategies become explicit issues or cold evidence, never lanes by inertia.
3. **Propose corrected state** - one-line reason per change. Preserve every outstanding fact, but separate authority from evidence. Each issue gets stable id, route owner, review trigger and pointer; each removed issue gets a disposition in history. Forecast becomes `no_basis` when calibration is absent. A knowledge/work/local-play surface that falsely claims current routing may receive only a compact reset boundary, stale tombstone or visible retirement banner: no new strategy/content, and prior bytes remain in Git. For hot-file bloat, keep schema fields/pointers only; Git/history already preserve committed detail. Save a work snapshot only if content is genuinely unrecoverable elsewhere. Rotate over-ceiling LOG per schema: recent entries stay, older lines move verbatim to the one archive and one pointer remains.
4. **Confirm (owner)** - show one batched diff; apply only after explicit approval. CHARTER/TREE semantic changes route to frame/map/review, not repair.
5. **Friction** - OS hole -> one FRICTION line; do not fix OS here.

## Done when

NOW matches reality/schema; any lanes serve the active bet; calls/decisions/issues/forecast are mutually consistent; false routing surfaces are visibly stale without lost evidence; other flagged hot files are within template; cause is logged.

## Notes

- Never invent progress. Uncertain work becomes an issue/open question, not done.
- Repair may retire obsolete dispatch state while preserving its artifacts/history.
- Repeated same-point repair is a friction pattern.

END_OF_FILE: os/plays/repair.md
