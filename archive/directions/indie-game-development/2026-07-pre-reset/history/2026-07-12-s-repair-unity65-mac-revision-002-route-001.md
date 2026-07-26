RESULT s-repair-unity65-mac-revision-002-route-001 (call: owner handback for c-exec-unity65-mac-revision-002)
direction: indie-game-development   play: repair   node/task: g-9c41/Unity-6.5 Mac revision routing
outcome: |
  Direction routing now distinguishes the one default continuation from parallel work. The default `NOW.next`
  is restored to the pre-migration priority, Phase 0 gas-source ingestion. Frozen successor
  `c-exec-unity65-mac-revision-002` at product commit 7a3e747 is registered as a ready but non-priority runner
  BUILD prerequisite. The premature revision-001 Unity/FishNet BUILD is no longer ready: it may receive a new
  resume CALL only after independent delivery of the runner. No BUILD, test, gate, merge, push, or Windows work ran.
evidence: |
  - Product commit `7a3e7470a3b6175542dc0a2f23152798f2aa8dd1` exists on
    `codex/unity-6.5-migration-plan`, directly parented by PLAN commit
    `8a344e97da10da417d76c0a3e7534bec0a0f7c96`; its five-file diff contains only
    c-exec-unity65-mac-revision-002 PLAN/proposal/spec/tasks and ADR-E-0012.
  - Frozen PLAN and spec explicitly state that revision-002 replaces only revision-001's mandatory-PowerShell
    premise, does not start revision-001, and requires Direction OS to issue a separate fresh resume CALL only
    after runner delivery. The PLAN records owner approval words
    `Одобряю PLAN c-exec-unity65-mac-revision-002`.
  - Product `git status --short` still contains only the two pre-existing unstaged owner/editor files:
    `.vscode/settings.json` and `Assets/GasCoopGame/Levels/GasLab/Flow/CoopSmallSGF.asset`.
  - `os/schema/direction-files.md` defines exactly one `NOW.next` as the default ready CALL and `open_calls` as
    the in-flight/parallel registry. History
    `2026-07-10-s-repair-poligon-a0-checksum-route-001.md` records removal of the out-of-schema
    `parallel_tracks` and multi-CALL `next`; commit 726f679 shows Phase 0 was the default before Unity migration
    replaced it.
  - Owner routing instruction in this session: `текущая миграция, она не является приоритетной. Мне главное,
    чтобы она не поломала ничего`; owner confirmed the corrected state proposal with actual words `A`.
state_changes: |
  Against fresh live/indie-game-development state:
  1. Set NOW.md `updated` to `2026-07-12 by s-repair-unity65-mac-revision-002-route-001`.
  2. Remove `open_calls` entity `c-exec-unity65-mac-revision-build-001`; it was not started and is superseded as
     a ready route by the frozen runner prerequisite, while revision-001 planning authority remains history.
  3. Add `open_calls` entity `c-exec-unity65-mac-revision-002-build-001`, to executor, for
     `g-9c41 / local .NET repository-gate runner prerequisite`, issued 2026-07-12, with a concise note pointing to
     product PLAN commit 7a3e747, its non-priority status, its revision-001/Unity/Windows/merge/push boundaries,
     the two preserved dirty files, and
     `work/c-exec-unity65-mac-revision-002-build-001-call.md`.
  4. Set NOW.md `next` exactly to `CALL: work/c-exec-lv-ingest-phase0-call.md`.
  5. Create complete self-contained CALL file
     `live/indie-game-development/work/c-exec-unity65-mac-revision-002-build-001-call.md` from this RESULT's
     declared runner outcome, frozen authority, boundaries, evidence gates, and return contract.
  6. Preserve the current bet, every task, every other open_call, recurring, decisions, TREE.md, CHARTER.md,
     knowledge, product repository, and all unnamed NOW.md fields unchanged after semantic rebase.
  7. Append the `log` line below once to LOG.md and save this full RESULT once at
     `history/2026-07-12-s-repair-unity65-mac-revision-002-route-001.md`, maintaining trailers.
  8. Regenerate the declared owner panel live Board/Journal sections from merged NOW+LOG; show Phase 0 as the
     default, revision-002 as non-priority parallel work, revision-001 as waiting for delivered runner evidence,
     and remove the stale panel claim that each track has its own `parallel_track` field in NOW.
captures: []
decisions_needed: []
play_check:
  - 1 Name the contradiction: done — NOW routed to revision-001 BUILD @8a344e97 while newer successor runner authority @7a3e747 blocked that BUILD and the owner said migration is not priority.
  - 2 Reconstruct: done — checked KERNEL, repair play, packet/state schemas, writer adapter, current NOW/LOG/history, product commit graph, frozen revision-002 PLAN/spec/ADR, dirty boundary, and pre-migration NOW.next ancestry.
  - 3 Propose corrected state: done — separated singleton default routing from the parallel open-call registry, restored Phase 0, and supplied one self-contained runner BUILD CALL without starting it.
  - 4 Confirm: done — owner actual words `A`; routing premise cited from owner words `текущая миграция, она не является приоритетной. Мне главное, чтобы она не поломала ничего`.
  - 5 Friction: done — no new os/** line; the exact multi-next/parallel_tracks schema drift is already recorded in os/FRICTION.md (2026-07-04) and repaired in history/2026-07-10-s-repair-poligon-a0-checksum-route-001.md; the stale owner-panel rendering is corrected by this apply.
log: 2026-07-12 — repair/route (g-9c41/Unity-6.5 Mac revision, s-repair-unity65-mac-revision-002-route-001): owner `A`; frozen runner PLAN @7a3e747 registered as a non-priority parallel BUILD prerequisite, premature revision-001 BUILD removed, and global NOW.next restored to Phase 0; no BUILD/test/gate ran. → history/2026-07-12-s-repair-unity65-mac-revision-002-route-001.md
next: |
  CALL: work/c-exec-lv-ingest-phase0-call.md

END_OF_FILE: live/indie-game-development/history/2026-07-12-s-repair-unity65-mac-revision-002-route-001.md
