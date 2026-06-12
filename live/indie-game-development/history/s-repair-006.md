# RESULT — s-repair-006 (repair, 2026-06-11)

```yaml
RESULT s-repair-006
direction: indie-game-development
play: repair
node: g-a7f2
outcome: |
  NOW.md matches reality and current rules again: stale CALL c-map-001 retired from
  open_calls and next; next = c-ev-001, a map_evidence research session per the
  evidence-first map rules (aba9e36). TREE.md and CHARTER.md untouched.
evidence: |
  Contradiction: c-map-001 violated CALL hygiene (goal recited method — documented
  cause of the map №1 failure, FRICTION "os/live дрейф" entry) and contradicted
  map step 2 / frame step 6 as of aba9e36 (map needs a fresh map_evidence RESULT).
  Reconstruction (artifacts > log > chat memory): frame applied (history/s-frame-005.md,
  LOG line 1, charter+root in state); TREE root g-a7f2 with children: [] — map never
  started in state; map chats №1–2 emitted no RESULT, so their content (owner candidate
  list, Card 1 accept) does not exist in state and may arrive later as checkpoint captures.
state_changes: |
  live/indie-game-development/NOW.md: open_calls [] (c-map-001 retired); next = c-ev-001
  (full CALL text in NOW.md); rest unchanged.
  live/indie-game-development/LOG.md: repair line appended.
captures:
  - owner may still close map chat №2 with a checkpoint RESULT; its captures (candidate
    list, Card 1 accept) integrate without conflict — they carry raw material for the
    future map session, not state.
decisions_needed: []
play_check: |
  1 name-the-contradiction: done (NOW vs CALL hygiene + evidence-first rules).
  2 reconstruct: done (history/s-frame-005.md, LOG, TREE, git — newest first).
  3 propose-corrected-state: done (diff table shown to owner).
  4 confirm (owner): done — owner selected «Применить (рекомендую)».
  5 friction: done — desync already logged today (os/FRICTION.md "os/live дрейф" entry,
    same cause); no duplicate line added.
log: |
  repair: stale c-map-001 retired (pre-hygiene CALL, superseded by evidence-first map
  rules); next = c-ev-001 map_evidence research session.
next: |
  c-ev-001 — see live/indie-game-development/NOW.md next block.
```

END_OF_FILE: live/indie-game-development/history/s-repair-006.md
