RESULT s-designlab-ono-dyshit-bubble-proof-repair-001
direction: indie-game-development   play: local/design-lab   node/task: g-d3a8/q-ono-dyshit-core-frame-fork

owner_summary: |
  Owner was right: the previous "Bubble-vs-mission constrained hybrid" recommendation read as spending time on two mechanics.

  Correction:
  - do not compare two playable mechanics;
  - do not build a mission-value branch in parallel;
  - first proof should be one loop only: Bubble-first;
  - mission-value-first remains only a paper sanity-check/fallback.

outcome: |
  Recommendation corrected from "Bubble-informed hybrid first" to "Bubble-first as the single first proof".

  Bubble-first proof:
  - find sleeping gas;
  - bubble a bounded gas state;
  - carry visible live custody through route danger;
  - rupture releases gas back into the world simulation;
  - decide whether to go back for another.

  This preserves the `Пузырь` hook without spending owner/team time on two objective systems.

evidence: |
  Correction note created:
  - live/indie-game-development/work/design-labs/ono-dyshit-bubble-proof-repair-001.md

  Prior context:
  - live/indie-game-development/work/design-labs/ono-dyshit-bubble-variant-001.md
  - live/indie-game-development/work/design-labs/ono-dyshit-core-frame-fork-001.md
  - live/indie-game-development/NOW.md

state_changes: |
  Applied mechanically in this repo:

  1. Created:
     live/indie-game-development/work/design-labs/ono-dyshit-bubble-proof-repair-001.md
     Content: correction note saying Bubble is one proof, not a two-mechanic comparison.

  2. Created:
     live/indie-game-development/history/2026-07-08-s-designlab-ono-dyshit-bubble-proof-repair-001.md
     Content: this RESULT block, ending with its END_OF_FILE trailer.

  3. Appended to live/indie-game-development/LOG.md before its END_OF_FILE trailer:
     2026-07-08 — design-lab correction (g-d3a8/q-ono-dyshit-core-frame-fork, s-designlab-ono-dyshit-bubble-proof-repair-001): owner rejected `Bubble-vs-mission hybrid` as wasting time on two mechanics. Route corrected: one first proof only — Bubble-first. Mission-value remains paper sanity-check/fallback, not a parallel playable branch. Pending decision narrowed to approve Bubble-first single proof or reject it and fall back. → work/design-labs/ono-dyshit-bubble-proof-repair-001.md

  4. Edited live/indie-game-development/NOW.md:
     - updated header to:
       updated: 2026-07-08 by s-designlab-ono-dyshit-bubble-proof-repair-001
     - replaced g-d3a8 state with corrected route:
       one first proof only, Bubble-first; mission-value-first is paper sanity-check/fallback, not parallel playable branch.
     - narrowed d-ono-dyshit-core-frame-fork-001 to:
       approve Bubble-first single proof, or reject Bubble-first and fall back to mission-value-first.
     - left primary NOW.next unchanged on c-exec-034.

captures:
  - Hybrid comparison was an operational error because it could become two prototypes.
  - `Пузырь` should be tested as one core loop, not compared by implementation against mission-value.
  - Mission-value remains useful only as a paper gate: if Bubble does not make gas itself valuable enough, fall back.

decisions_needed:
  - id: d-ono-dyshit-core-frame-fork-001
    q: |
      Should canon-forge inherit Bubble-first as the single first proof?
    options:
      - Approve Bubble-first single proof.
      - Reject Bubble-first and fall back to mission-value-first.
    recommendation: |
      Approve Bubble-first as one proof. Do not build a Bubble-vs-mission comparison.

title_boundary: |
  Preserved. No canon freeze; no living-city ontology, gas subjectivity, creature AI, magical sleep/wake, exact gas names, exact tools, economy, timers or progression imported.

log: |
  2026-07-08 — design-lab correction (g-d3a8/q-ono-dyshit-core-frame-fork, s-designlab-ono-dyshit-bubble-proof-repair-001): owner rejected `Bubble-vs-mission hybrid` as wasting time on two mechanics. Route corrected: one first proof only — Bubble-first. Mission-value remains paper sanity-check/fallback, not a parallel playable branch. Pending decision narrowed to approve Bubble-first single proof or reject it and fall back. → work/design-labs/ono-dyshit-bubble-proof-repair-001.md

next: |
  awaiting_decision d-ono-dyshit-core-frame-fork-001

END_OF_FILE: live/indie-game-development/history/2026-07-08-s-designlab-ono-dyshit-bubble-proof-repair-001.md
