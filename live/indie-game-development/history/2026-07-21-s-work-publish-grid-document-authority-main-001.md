# s-work-publish-grid-document-authority-main-001 — Grid documentation-authority gate published to main

Согласованная владельцем граница Grid по старой документации опубликована без force в `origin/main`.
Это не разрешает разработку: перед ней по-прежнему нужна отдельная поправка плана, которая гарантирует
одну актуальную документационную правду и либо надёжно обезвреживает старые документы, либо удаляет их
из текущего рабочего дерева с сохранением Git history.

```RESULT
RESULT s-work-publish-grid-document-authority-main-001 (call: owner-direct-publish-grid-document-authority-main-20260721)
direction: indie-game-development
track: grid
play: work
node/task: g-4b92/repository-main

outcome: |
  По прямому указанию владельца committed Grid launch-control handoff `022bf58d` опубликован обычным
  fast-forward без force в authoritative `origin/main`. Exact remote readback подтвердил сам commit,
  формальный disposition `CORRECTION FIRST`, текущую planning-only поправку документационной authority
  и сохранённую границу Grid 0/11 без продуктового запуска.

  Во время сериализованного закрытия отдельный Gas writer самостоятельно опубликовал совместимый commit
  `ca19da0b` поверх Grid commit. Он сохранён как свежая база receipt; эта Grid-сессия не изменяла его
  содержание и не присваивает себе его публикацию. Product repo, engineering CALL и BUILD authority не
  изменены.

evidence: |
  - Owner instruction: `запуш и залей в main`.
  - Fresh preflight after successful `git fetch origin`: target
    `022bf58d1f4492af1776e318e4125a9f162abe0e`; then-`origin/main`
    `676a54a829bc6727287a40734e479d9d989c5694`; ancestry check passed;
    `origin/main..target = 1`; `git diff --check origin/main..target` had zero findings.
  - Exact target manifest was the accepted Grid launch-control RESULT, its owner-readable handoff,
    the planning-only documentation-authority correction CALL, and their NOW/LOG/owner-panel render;
    no Gas file or product-repository path was part of commit `022bf58d`.
  - Non-force push output: `676a54a8..022bf58d  022bf58d... -> main`.
  - Independent `git ls-remote origin refs/heads/main` returned exact
    `022bf58d1f4492af1776e318e4125a9f162abe0e` immediately after that push.
  - Remote-identity artifact readback passed: saved history contains `CORRECTION FIRST`; the correction
    CALL contains the `current working tree` deletion fallback; current NOW contains
    `c-work-grid-v1-document-authority-correction-001` as READY/default.
  - Serialized concurrent apply then advanced both local HEAD and remote main to
    `ca19da0be66525ba5cb032693e878223fe89a795`; its parent is exact `022bf58d`, so the published Grid
    boundary remains in main without rewrite.
  - Not run: force push, reset, rebase, product mutation, Unity, tests, build, benchmark, Deliver, G01,
    product root, slot, PAIR-CANDIDATE, BUILD or any engineering CALL.

state_changes: |
  - `history/2026-07-21-s-work-publish-grid-document-authority-main-001.md` — save this complete RESULT
    once with its exact END_OF_FILE trailer.
  - `LOG.md` — append the declared Grid publication line once before END_OF_FILE, preserving the
    independently applied Gas line.
  - `work/board/dashboard.html` — update only the receipt header and add one owner-readable publication
    journal item at the top of 21 July; preserve current Grid/Gas cards, counts, problems and roadmap.
  - `NOW.md`, `TREE.md`, `CHARTER.md`, knowledge/, Grid/Gas artifacts and CALLs, current default,
    product/canon repositories and engineering authority — no change.
  - Repository publication receipt — commit only this history receipt, LOG append and owner-panel
    publication render on top of fresh `ca19da0b`; push that receipt without force only to
    `refs/heads/main`; verify exact remote SHA and the three receipt paths by fresh readback.

captures: []

decisions_needed: []

play_check:
  - "1 Recite: done — publish the committed Grid documentation-authority launch boundary to authoritative main without force, unrelated mutation or product launch."
  - "2 Owner inputs (owner): skipped — repository transport is not owner-authored content; exact scope authority is the owner's instruction `запуш и залей в main`."
  - "3 Do the work: done — fresh ancestry proved one ordinary Grid fast-forward, exact commit `022bf58d` was pushed to main, remote identity/artifact readback passed, and the later compatible Gas publication was preserved as the serialized base."
  - "4 Self-check: done — commit manifest, ancestry, range, diff-check, non-force push output, exact ls-remote equality and Grid artifact readback passed; no product action or unrelated file was performed by this session."
  - "5 Close: done — publication receipt only; NOW stays on the planning-only documentation-authority correction, Grid stays parallel at 0/11, and product work remains closed."

log: "2026-07-21 · s-work-publish-grid-document-authority-main-001 · work/publish · grid · g-4b92/repository-main: owner-requested Grid documentation-authority gate through 022bf58d was fast-forwarded without force to origin/main with exact SHA/artifact readback; CORRECTION FIRST and the READY/default planning correction remain, Grid stays 0/11 and product execution closed, while the independently published compatible Gas commit ca19da0b is preserved. → history/2026-07-21-s-work-publish-grid-document-authority-main-001.md"

next: |
  Existing Grid continuation, unchanged:
  call: c-work-grid-v1-document-authority-correction-001
  track: grid
  status: ready
  goal: |
    До любой разработки Grid существует одна актуальная документационная правда: каждый старый документ,
    способный направить executor, либо механически доказан как неавторитетный, либо удалён из текущего
    рабочего дерева с сохранением Git history.
```

END_OF_FILE: live/indie-game-development/history/2026-07-21-s-work-publish-grid-document-authority-main-001.md
