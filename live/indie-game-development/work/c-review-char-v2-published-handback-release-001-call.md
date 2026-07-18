CALL c-review-char-v2-published-handback-release-001
to: session
direction: indie-game-development
track: characters
play: review
node: g-6d4e
parent: c-exec-char-v2-body-rig-ragdoll-build-001

goal: |
  Опубликованный Character V2 reaction-core repair имеет связывающий Direction-вердикт,
  а текущий Character WIP освобождён без выдачи authority на Leg 2.

context: |
  Owner handback 2026-07-18:
  - candidate: 0e5b2948172574d6966bfd7bbab298489e56559c;
  - integration: 53453081ba54ac558d73d87c4984a54ec28cb1b4;
  - published dev/main: 029279a7a03af5869f32ddbb8b93aa49f2c6183f;
  - Deliver: GREEN, 1873/1873;
  - product RESULT: docs/results/c-exec-char-v2-reaction-core-repair-admission-003.md;
  - product review: docs/reviews/review-c-exec-char-v2-reaction-core-repair-admission-003.md.

  Authenticated readback at exact published 029279a confirmed that the RESULT records final fresh binding G5
  CONFIRMED on exact candidate 0e5b2948, integration 53453081 with candidate blobs preserved, repaired Deliver
  GREEN and serialized dev/main publication. GitHub commit metadata records 029279a as a direct child of
  5d9a0a8e9413264371bfae96daa8c09fde0831ea and 53453081 as an ancestor of 029279a.

  The full invariant remains provenance, not value: a wrapper may report pose readiness only after sampling
  inner.Current while reactions were Normal or receiving explicit restPose through wrapper GetUp. Lawful Origin
  remains valid. Published evidence routes DF-13 socket readiness, DF-14 stray Normal GetUp and DF-15 throw-path
  atomicity without claiming them fixed.

  Direction sources:
  - NOW.md entries for the returning admission-003 child and the body-rig parent;
  - work/c-exec-char-v2-reaction-core-repair-admission-003-call.md;
  - work/c-plan-characters-002-plan.md;
  - knowledge/g6d4e-char-v2-leg1-reaction-core.md;
  - history/2026-07-18-s-work-char-v2-published-handback-release-route-001.md.

  Owner scope disposition is already explicit in the returning session: «Выпусти отдельный CALL, принимающий
  handback и освобождающий текущую Character Direction. Leg 2 без отдельного решения не открывать.» Operationally,
  release means the preserved body-rig root becomes owner-paused and stops occupying WIP; it is not deleted,
  made ready or dispatched. A later resume needs a new owner decision.

boundaries: |
  Product repo and published refs are read-only in this leg. Do not mutate, merge, push, repair, re-run delivery
  publication or rewrite product evidence. Do not open, refresh, dispatch or make ready Leg 2. Do not change the
  primary core bet/default, unrelated tracks/calls/decisions, CHARTER or TREE. The current Character root is
  released as paused, not silently completed or deleted; any future Character work requires a separate owner decision.

done_when: |
  1. Exact published RESULT/review and candidate→integration→published identity have evidence-backed dispositions.
  2. All six admission-003 done_when bullets are reconciled against the published product evidence, including
     immutable RED discrimination, frozen seam identity, DF-13/14/15 routing, review class+sweep and final fresh G5.
  3. A binding Direction verdict records MET, PARTIALLY MET or NOT MET without treating publication alone as close.
  4. On MET, Leg 1 is accepted only at its bounded reaction-core height; on any other verdict, the exact blocker is named.
  5. The review child is consumed; the body-rig root becomes owner-paused with no waiting child and no runnable
     successor, so Character stops occupying WIP while g-6d4e and its evidence remain recoverable.
  6. Leg 2 remains NOT RUNNABLE and can resume only from a later explicit owner decision; primary/default and all
     unrelated track state remain unchanged.

return: |
  One Direction-OS RESULT with the binding verdict, exact evidence pointers, admission-003 reconciliation,
  Character root pause/release state changes, refreshed owner panel and no Leg 2 CALL.

budget: one fresh read-only Direction review session

END_OF_FILE: live/indie-game-development/work/c-review-char-v2-published-handback-release-001-call.md
