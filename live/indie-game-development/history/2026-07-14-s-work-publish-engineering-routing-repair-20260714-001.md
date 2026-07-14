RESULT s-work-publish-engineering-routing-repair-20260714-001 (call: owner-direct-publish-engineering-routing-repair-20260714-001)
direction: indie-game-development
play: work
node/task: g-9c41 / engineering-v21-routing publication

outcome: |
  The approved engineering-routing repair is published to the authoritative main branch.

  Repair commit 5946277 and its checksum-preservation follow-up 45af36c were merged as
  3e6e184, then remote main ancestry was reconciled as 017d6a2. Push and fetch readback
  confirmed exact origin/main@017d6a2f1767b16430b3eeca1eb57523fcb6d0aa.

  No force push was used. Concurrent Poligon-M1 commit 59cbd6b was deliberately excluded.
  The existing NearGas PLAN-AMEND/Re-sync CALL remains NOW.next; no product work, task
  status or routing was changed by this publication.

evidence: |
  Preflight and isolation:

  - clean integration worktree C:\my_global_workflow started at
    main@45649f162975551edba98741c8ef401e4e6849c6;
  - origin/main was 4e1d7461eee10f1c163c0ca26c36e83e65594983;
  - the direction branch advanced concurrently from 45af36c to 59cbd6b during preflight;
    inspection proved 59cbd6b was the separate Poligon-M1 dashboard-routing repair;
  - integration therefore targeted exact commit 45af36c, whose ancestry contains repair
    5946277, rather than the moving branch tip.

  Semantic integration:

  - merge 3e6e184 brought exactly the engineering-routing repair, its RESULT/CALL/panel
    state, and the checksum-preservation .gitattributes change into main;
  - origin-only Frame-v2 commit 4e1d746 was already represented in the newer main:
    .gitattributes, its full RESULT history, distillation handoff and research draft had
    exact matching Git blob ids, while its LOG, NOW and dashboard facts were present in
    newer live state;
  - merge 017d6a2 therefore joined 4e1d746 ancestry with the current tree and did not
    replay its stale NOW/LOG/dashboard snapshot;
  - git diff --check passed and the clean integration tree contained 45649f1, 5946277,
    45af36c and 4e1d746 in ancestry;
  - 59cbd6b was not an ancestor of the integration head.

  Transport and remote readback:

  - git push origin main:main advanced origin/main 4e1d746 → 017d6a2;
  - no force option was used;
  - a fresh git fetch resolved both local main and origin/main to exact
    017d6a2f1767b16430b3eeca1eb57523fcb6d0aa;
  - remote ancestry checks passed for 5946277, 45af36c and 4e1d746;
  - remote ancestry explicitly rejected concurrent M1 commit 59cbd6b.

  Preservation:

  - publication commands ran only in the clean main worktree;
  - the direction worktree remained on its concurrent 59cbd6b commit with only the
    pre-existing marketing/handle-reservation-inomand.md modification dirty;
  - that foreign dirty file retained SHA-256
    4BD9AE717B7DE14A040A820509CDD284656A7C9204BC25D2BFA451DF9A1A39DA;
  - no product, canon, TREE, CHARTER, knowledge or OS file was changed.

state_changes: |
  Apply against fresh current state using stable paths and preserve unrelated work.

  1. Preserve live/indie-game-development/NOW.md byte-for-byte. Do not change tasks,
     open_calls, decisions or NOW.next.

  2. Append exactly once before END_OF_FILE in live/indie-game-development/LOG.md:

     2026-07-14 — work/publish (g-9c41/engineering-v21-routing, s-work-publish-engineering-routing-repair-20260714-001): repair 5946277 and checksum fix 45af36c were merged into main and pushed/read back at origin/main@017d6a2 without force; remote Frame-v2 ancestry 4e1d746 was preserved without replaying stale state, concurrent M1 commit 59cbd6b was excluded, and the NearGas PLAN-AMEND/Re-sync CALL remains next. → history/2026-07-14-s-work-publish-engineering-routing-repair-20260714-001.md

  3. Create exactly once:

     live/indie-game-development/history/2026-07-14-s-work-publish-engineering-routing-repair-20260714-001.md

     containing this full RESULT verbatim followed by its exact END_OF_FILE trailer.

  4. Regenerate only the current-day Journal portion of the declared owner panel
     live/indie-game-development/work/board/dashboard.html: record verified publication
     at 017d6a2, Frame-v2 ancestry preservation and exclusion of 59cbd6b. Preserve its
     Board, Problems and all unrelated content.

  5. Preserve all remaining direction state and every unrelated current file. Do not
     modify any product or canon repository.

captures: []

decisions_needed: []

play_check:
  - "1 Recite: done — publish the already committed engineering-routing repair into authoritative main, preserving concurrent work and verifying remote readback."
  - "2 Owner inputs: skipped — Git publication required no owner-content choice; live authorization is the owner's actual words: «запущ и залей в main и запуш свои изменения»."
  - "3 Do the work: done — exact repair tip 45af36c was merged, origin/main ancestry reconciled, and main pushed without force to 017d6a2."
  - "4 Self-check: done — clean-tree diff check, required and excluded ancestry, exact Frame-v2 blobs, remote ref equality and foreign dirty-file preservation were verified."
  - "5 Close: done — publication receipt is logged and archived, the owner panel Journal is synchronized, and NOW.next is unchanged."

log: |
  work/publish g-9c41: engineering-routing repair 5946277 plus checksum fix
  45af36c published without force at origin/main@017d6a2; Frame-v2 ancestry
  preserved, concurrent M1 commit excluded and remote readback green.

next: |
  CALL: work/c-exec-near-gas-core-authority-001-plan-amend-resync-002-call.md

END_OF_FILE: live/indie-game-development/history/2026-07-14-s-work-publish-engineering-routing-repair-20260714-001.md
