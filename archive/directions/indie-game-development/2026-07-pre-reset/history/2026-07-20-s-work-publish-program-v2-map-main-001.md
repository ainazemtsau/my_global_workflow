RESULT s-work-publish-program-v2-map-main-001 (call: owner-direct-publish-program-v2-map-main-20260720)

direction: indie-game-development
track: program
play: work
node/task: g-a7f2/repository-main

outcome: |
  По прямому указанию владельца exact Program v2 map commit
  79e37e73a9d54e84ca24b2a15d728083ad1793a1 опубликован без force в
  origin/wt/indie-game-development.

  Свежий origin/main разошёлся с рабочей веткой. Обычный merge потянул бы
  посторонние a69b830 и 8fe7e28, поэтому exact diff только нашего 79e37e7
  воспроизведён поверх свежего origin/main@5cd6616 в чистом integration commit
  abdf057d04ceec340832a79b7b993b13ee1fc8cd.

  Один atomic non-force push обновил:
  - origin/wt/indie-game-development: 8fe7e28 → 79e37e7;
  - origin/main: 5cd6616 → abdf057.

  Параллельный local commit 6feec02 и незакоммиченные canon-файлы исключены.

evidence: |
  - Owner instruction: «запушить и замёрзить их в main», с явной границей
    «ну только свои».
  - Fresh preflight:
      local current HEAD = 6feec02b99f90715e4765a2e8d2fa018c46d0324;
      exact owned commit = 79e37e73a9d54e84ca24b2a15d728083ad1793a1;
      origin/wt/indie-game-development = 8fe7e2844680e81e85299f0c30ee1c9c8865f420;
      origin/main = 5cd6616ccc19c0884bbaec87f84209dee957e3c6.
  - 79e37e7 is the single commit above origin/wt, while current local 6feec02 is
    its later child and was not selected as a push source.
  - Preserved uncommitted files:
      live/indie-game-development/LOG.md;
      live/indie-game-development/NOW.md;
      live/indie-game-development/history/2026-07-20-s-cartography-g-d3a8-post-gas-behavior-admission-front-001.md;
      live/indie-game-development/work/c-forge-g-d3a8-visual-contract-001-call.md;
      live/indie-game-development/work/canon-maps/g-d3a8-current-question-front-v3.md.
  - Clean temporary integration:
      parent = origin/main@5cd6616;
      commit = abdf057;
      rev-list count origin/main..abdf057 = 1;
      all eight Program v2 paths are content-identical to 79e37e7;
      git diff --check returned zero findings.
  - Atomic non-force push:
      5cd6616..abdf057 → main;
      8fe7e28..79e37e7 → wt/indie-game-development.
  - Independent git ls-remote and fetched-ref readback returned exact
    abdf057 for main and 79e37e7 for wt/indie-game-development.
  - Each remote advanced by exactly one commit from its preflight ref.

state_changes: |
  live/indie-game-development/history/2026-07-20-s-work-publish-program-v2-map-main-001.md:
    - ADD this complete RESULT once with its exact END_OF_FILE trailer.

  live/indie-game-development/LOG.md:
    - APPEND the declared publication line once before END_OF_FILE.

  live/indie-game-development/NOW.md, TREE.md, CHARTER.md, knowledge/,
  dashboard, CALL artifacts, product repositories and all concurrent local
  files:
    - NO CHANGE.

  After the receipt commit:
    - publish only the receipt delta without force to both remote refs;
    - base the main receipt on abdf057 and the worktree receipt on 79e37e7;
    - verify both remote refs by ls-remote/fetch readback;
    - do not include local 6feec02 or uncommitted canon work.

captures: []

decisions_needed: []

play_check:
  - "1 Recite: done — publish only the committed Program v2 map to the worktree remote and current main, excluding every later/local change."
  - "2 Owner inputs (owner): skipped as non-owner-content transport; authority and scope are the owner’s exact words «ну только свои»."
  - "3 Do the work: done — exact 79e37e7 was isolated, replayed once over fresh main and atomically pushed to both refs without force."
  - "4 Self-check: done — content identity, one-commit ranges, clean diff-check and independent remote readback all passed; 6feec02 and dirty canon files stayed excluded."
  - "5 Close: done — publication receipt only; no NOW route, task, decision, dashboard or product authority changes."

log: 2026-07-20 · s-work-publish-program-v2-map-main-001 · work/publish · program · g-a7f2/repository-main: exact Program v2 map 79e37e7 pushed alone to origin/wt/indie-game-development and replayed alone as abdf057 on fresh origin/main; atomic non-force readback matched, while later 6feec02 and dirty canon work stayed local. → history/2026-07-20-s-work-publish-program-v2-map-main-001.md

next: |
  Preserve the existing published-snapshot default:
  CALL c-shape-program-v2-v30-entry-001 — ready and unchanged.
  No new CALL is issued by publication.

END_OF_FILE: live/indie-game-development/history/2026-07-20-s-work-publish-program-v2-map-main-001.md
