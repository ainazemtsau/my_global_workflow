RESULT s-work-065-c-visual-008-frame (call: owner plain message "давай идти по этому пути")
direction: indie-game-development   play: work   node/task: g-7e15/c-visual-008
outcome: |
  Stage 3.5 for the visual track is now framed and fire-ready as c-visual-008, before Stage 4. The executor handoff targets the owner's observed gaps: stationary gas needs subtle honest internal life, motion onset must stop reading as missing frames, and scene/gas muddiness must be A/B checked on the half-res path.
evidence: |
  Added live/indie-game-development/work/c-visual-008-stage3-5-motion-clarity-call.md.
  NOW.md now carries open_call c-visual-008 and the g-7e15 track state says Stage 3.5 is framed before Stage 4.
  LOG.md has the s-work-065 line.
  Base evidence from previous state: GasCoopGame origin/main@9d6f8ded contains c-visual-007 dev2@1c99a907; Stage 4 was not opened.
state_changes: |
  live/indie-game-development/work/: add c-visual-008-stage3-5-motion-clarity-call.md with a self-contained executor CALL.
  live/indie-game-development/NOW.md:
    - updated -> 2026-07-09 by s-work-065-c-visual-008-frame.
    - add open_calls entry c-visual-008 pointing to work/c-visual-008-stage3-5-motion-clarity-call.md.
    - update parallel_tracks g-7e15 state to "Stage 3.5 FRAMED + FIRE-READY" while keeping Stage 3 pushed evidence and Stage 4 unopened.
    - keep c-exec-035, c-cartography-core-concept-rebuild-001, and NOW.next unchanged.
  live/indie-game-development/LOG.md: append the s-work-065 one-line record.
  live/indie-game-development/history/: add 2026-07-09-s-work-065-c-visual-008-frame.md.
captures:
  - Future visual/design split: if c-visual-008 finds honest smooth directed flow needs sim velocity/face-flow/new view data, frame that as a separate movement-data slice rather than masking it render-side.
decisions_needed: []
play_check:
  - 1 Recite: done — task serves g-7e15 VISUAL; owner chose the path after noting dead-static idle gas, jerky motion onset, and muddy environment read.
  - 2 Owner inputs (owner): done/skipped — this artifact is an executor handoff, not owner-owned content; owner input used was "давай идти по этому пути", with no extra personal-preference question required.
  - 3 Do the work: done — produced the executor CALL c-visual-008 and registered it in NOW.open_calls.
  - 4 Self-check: done — CALL covers idle life, motion onset, clarity/muddiness, render-only honesty, baseline A/B, Core/sim diff proof, and product check expectations.
  - 5 Close: done — state updates, LOG, history, and next routing are recorded.
log: 2026-07-09 — work/frame (g-7e15/c-visual-008, s-work-065): Stage 3.5 visual-only CALL framed before Stage 4 for idle internal life, motion-onset smoothness, and environment-clarity/muddiness audit on GasCoopGame origin/main@9d6f8ded; no Core/sim edits, no fake jet, no particles/VFX acceptance crutch. → history/2026-07-09-s-work-065-c-visual-008-frame.md
next: |
  c-visual-008 is ready to fire as an executor CALL. NOW.next remains CALL c-cartography-core-concept-rebuild-001 → work/c-cartography-core-concept-rebuild-001-call.md.

END_OF_FILE: live/indie-game-development/history/2026-07-09-s-work-065-c-visual-008-frame.md
