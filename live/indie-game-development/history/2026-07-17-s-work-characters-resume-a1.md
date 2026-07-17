RESULT s-work-characters-resume-a1 (call: owner-directive-characters-resume-a1)
direction: indie-game-development   track: characters   play: work   node/task: g-6d4e/resume

outcome: |
  Characters возобновлён как bounded parallel track без превышения WIP и без product mutation. По точному
  owner verdict «вариант А» marketing поставлен на паузу; по дополнительным словам владельца damage также
  поставлен на паузу. Character body-rig root теперь WAITING на repair + отдельный binding G5, а узкий
  reaction repair child READY после полного обновления CALL под current product-owned worktree protocol.

  WIP occupancy атомарно изменился 6/6 → 5/6: core, level, canon, visual и characters занимают пять слотов;
  marketing, damage и dotnet-gates paused. Current default остаётся core / NearGas L1B surface-freeze.

  Damage не удалён. Проверка показала, что это механически сохранённый при track-mode migration legacy CALL
  c-shape-sc-damage-001, а не текущая отдельная разработка: его contract v19, product base и canon-развилка
  устарели. Рекомендация — отдельным review retire/rehome stale frontier, сохранив будущую обязанность
  «газ имеет последствия» в core SPEC/knowledge для нового shape с актуального состояния.

evidence: |
  Owner resume intent: «Я хочу сейчас параллельно ... возобновить работу над Characters».
  Owner lifecycle verdict: «Маркируем и damage на паузу ... вариант А, но только на паузу ещё поставь damage».
  The presented option A explicitly meant marketing→paused, characters→resume, default core unchanged and
  repair-002 refreshed before dispatch; the owner selected that option and added damage pause.

  Fresh NOW before apply had track_wip_limit 6 and occupancy 6/6: core, level, canon, damage, visual and
  marketing occupied; both character CALLs were paused. Exact after-graph is mechanically valid:
  core/level/canon ready roots + visual blocked root + character waiting root = 5 occupied tracks;
  repair-002 is its same-track child and adds no second slot.

  Product protocol evidence: work/gascoopgame-worktree-protocol-v2.md records DELIVERED + Direction-closed
  GREEN and makes product AGENTS/registry authoritative for admitted venue, branch/path/SHA, Editor and
  integration. The pre-resume repair CALL instead hard-coded a legacy worktree/branch/SHA, forbade rebase and
  described Characters.meta as untracked; those stale launch mechanics were removed while preserving the
  accepted provenance invariant, cuts and evidence obligations.

  Character dependency evidence: knowledge/g6d4e-char-v2-leg1-reaction-core.md records repair-002 as the
  bounded option-A class repair and requires a separate binding G5 before Leg 2. The materialized body-rig CALL
  already preserves C1–C4 and now states WAITING / NOT RUNNABLE under model-neutral current review rules.

  Damage evidence: work/c-shape-sc-damage-call.md was issued 2026-07-09 against contract v19 and product base
  defade72; LOG 2026-07-11 records owner routing Sc-damage only after a ready canon specification; track-mode
  migration explicitly preserved all open CALLs without launching/closing them. Pause is therefore safe and
  reversible; retirement remains a separate review job.

  No TREE, CHARTER, knowledge, product repo, canon repo, branch, worktree, registry, Unity process or remote
  ref changed. The unrelated in-progress edit to work/c-work-sphere-universal-capture-frame-001-call.md was
  preserved outside this RESULT and commit scope.

state_changes: |
  live/indie-game-development/NOW.md:
    - SET updated to s-work-characters-resume-a1.
    - SET c-marketing-wake-001 ready→paused with paused_by this history receipt; preserve its checkpoint and
      stale-route finding in the note.
    - SET c-shape-sc-damage-001 blocked→paused with paused_by this receipt; preserve its future obligation as
      a note and record that retirement/rehome needs a separate review.
    - SET character root c-exec-char-v2-body-rig-ragdoll-build-001 paused→waiting; preserve waiting_on
      [c-exec-char-v2-reaction-core-repair-002], remove the old pause pointer and state the later binding-G5 gate.
    - SET child c-exec-char-v2-reaction-core-repair-002 paused→ready; preserve its parent/root position and
      replace the pause note with current product-owned dispatch authority.
    - PRESERVE track_wip_limit 6, all eight track ids, bet/tasks/decision, every unrelated open_call and
      NOW.next = c-exec-near-gas-l1b-surface-freeze-001.
  live/indie-game-development/work/c-exec-char-v2-reaction-core-repair-002-call.md:
    - REPLACE the stale pre-protocol packet with a self-contained current engineering CALL. Preserve the full
      provenance invariant, accepted option A, frozen seam/cuts, F3/S8/DF-13 honesty and separate binding-G5
      return; remove Direction-assigned path/branch/SHA, model-family gate and stale Characters.meta mechanics.
  live/indie-game-development/work/c-exec-char-v2-body-rig-ragdoll-build-001-call.md:
    - PATCH status PAUSED→WAITING, record the resume receipt, retain NOT RUNNABLE until repair + binding G5,
      and make G4 model-neutral per current authority.
  live/indie-game-development/work/track-mode-owner-operations-guide.md:
    - REGENERATE the current snapshot and completed swap example to WIP 5/6, core default, Characters
      ready-child/waiting-root and marketing+damage+dotnet paused.
  live/indie-game-development/work/board/dashboard.html:
    - REGENERATE current Board, route, open-work cards, safe-parallel section, matrix and 17.07 Journal from the
      fresh after-state; preserve Problems and historical closed/journal receipts as history-at-that-time.
  live/indie-game-development/LOG.md:
    - APPEND the declared log line once before the EOF trailer.
  live/indie-game-development/history/:
    - ADD 2026-07-17-s-work-characters-resume-a1.md with this full RESULT and exact EOF trailer.
  live/indie-game-development/TREE.md, CHARTER.md, knowledge/, os/**, canon and product repositories:
    - NO CHANGE.

captures:
  - "damage review: retire/rehome stale c-shape-sc-damage-001 frontier; keep the future gas-consequence obligation in current core SPEC/knowledge and reshape only from then-current canon/core authority."

decisions_needed: []

play_check:
  - "1 Recite: done — bounded parallel-track lifecycle resume; Characters must become safely dispatchable without exceeding track WIP or opening Leg 2 prematurely."
  - "2 Owner inputs (owner): done — this is protocol/dispatch state, not owner-authored personal content; lifecycle authority came from exact owner words «вариант А» and «только на паузу ещё поставь damage»."
  - "3 Do the work: done — recomputed fresh 6/6 frontier, inspected product protocol, character dependencies and damage provenance, refreshed repair-002, and applied the atomic marketing+damage pause / Characters resume graph without product mutation."
  - "4 Self-check: done — statuses = ready 4 / waiting 1 / blocked 1 / paused 3; occupied tracks = 5/6; waiting_on/parent graph is acyclic; all paused roots have owner receipts; core default and unrelated calls survive."
  - "5 Close: done — owner panel/guide, LOG/history and one ready character continuation are recorded; damage retirement is captured for a separate review, not guessed or deleted here."

log: 2026-07-17 · s-work-characters-resume-a1 · work · characters · g-6d4e/resume: owner chose A, paused marketing and damage, resumed Characters with repair-002 READY under product-owned admission and body-rig WAITING on repair + binding G5; WIP 6/6→5/6, core default and product unchanged. → history/2026-07-17-s-work-characters-resume-a1.md

next: |
  CALL: work/c-exec-char-v2-reaction-core-repair-002-call.md
  track: characters
  status: ready
  note: Run in a fresh product executor session; current product AGENTS/registry must admit the venue before any write.

END_OF_FILE: live/indie-game-development/history/2026-07-17-s-work-characters-resume-a1.md
