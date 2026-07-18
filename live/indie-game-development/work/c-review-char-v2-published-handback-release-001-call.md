CALL c-review-char-v2-published-handback-release-001
to: session
direction: indie-game-development
track: characters
play: review
node: g-6d4e
parent: c-exec-char-v2-body-rig-ragdoll-build-001

goal: |
  Опубликованный Character V2 reaction-core repair имеет связывающий Direction-вердикт,
  и при MET существующий Leg 2 root становится READY по отдельному решению владельца.

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

  Initial owner scope disposition was: «Выпусти отдельный CALL, принимающий handback и освобождающий текущую
  Character Direction. Leg 2 без отдельного решения не открывать.» The owner has now supplied that required
  separate decision verbatim: «A — открывай Leg 2 после review». This later instruction supersedes the earlier
  operational pause interpretation. It does not waive this review: before a MET verdict the preserved body-rig
  root stays WAITING and NOT RUNNABLE. On MET it becomes READY; READY permits a separate fresh product executor
  session, but does not automatically dispatch or mutate the product repo.

boundaries: |
  Product repo and published refs are read-only in this leg. Do not mutate, merge, push, repair, re-run delivery
  publication or rewrite product evidence. Do not dispatch or execute Leg 2 from the review session. Before a MET
  verdict Leg 2 remains WAITING and NOT RUNNABLE. Only a MET verdict may make the existing body-rig root READY;
  PARTIALLY MET or NOT MET must keep it non-runnable behind a named repair/re-review blocker. Do not change the
  primary core bet/default, unrelated tracks/calls/decisions, CHARTER or TREE. Do not delete or silently complete
  g-6d4e or the preserved body-rig root.

done_when: |
  1. Exact published RESULT/review and candidate→integration→published identity have evidence-backed dispositions.
  2. All six admission-003 done_when bullets are reconciled against the published product evidence, including
     immutable RED discrimination, frozen seam identity, DF-13/14/15 routing, review class+sweep and final fresh G5.
  3. A binding Direction verdict records MET, PARTIALLY MET or NOT MET without treating publication alone as close.
  4. On MET, Leg 1 is accepted only at its bounded reaction-core height; the review child is consumed, its receipt
     is appended to the body-rig root, the final wait clears and that existing root becomes READY under the owner's
     exact decision «A — открывай Leg 2 после review».
  5. On PARTIALLY MET or NOT MET, the exact blocker is named and the review child is replaced by a self-contained
     same-parent repair/re-review successor, so the body-rig root stays WAITING and NOT RUNNABLE.
  6. READY is only launch eligibility for a separate fresh product executor session, not execution in this review;
     primary/default and all unrelated track state remain unchanged.

return: |
  One Direction-OS RESULT with the binding verdict, exact evidence pointers, admission-003 reconciliation,
  conditional Character root readiness state changes, refreshed owner panel and no product mutation.

budget: one fresh read-only Direction review session

END_OF_FILE: live/indie-game-development/work/c-review-char-v2-published-handback-release-001-call.md
