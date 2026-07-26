RESULT s-repair-near-gas-l1b-track-rebase-001 (call: owner-directive-repair-in-place-2026-07-17)
direction: indie-game-development   track: core   play: repair   node/task: direction/near-gas-l1b-track-rebase
owner_approved: 2026-07-17 — owner delegated the in-place repair with exact words «сделай сам repair тут, прям тут, ничего не вызывая. Я тебе даю права на это» after receiving the recommendation to preserve the old runner in a separate paused track.

outcome: |
  Подготовленный до track-mode NearGas L1B SURFACE-FREEZE dispatch из commit
  `e26367df6220e573f710e42ca08d72db343f1f23` семантически встроен в свежий Direction HEAD. Новый executor CALL
  `c-exec-near-gas-l1b-surface-freeze-001` — единственный root трека `core`, имеет статус `ready` и выбран как
  `NOW.next`; L1B-Capture и все последующие задачи остаются open, product code не менялся.

  Старый неприоритетный `c-exec-unity65-mac-revision-002-build-001` не удалён и не объявлен выполненным. Он вынесен
  в новый отдельный parallel track `dotnet-gates` и поставлен на owner-delegated pause; его прежнее условие fresh
  authority/full-packet сохранено в hot-state pointer. Track WIP остаётся 6/6: `dotnet-gates` и `characters` с
  paused roots не занимают слот. Extraction, Level, damage, visual, marketing, characters, текущая ставка, задачи и
  pending min-spec decision сохранены.

evidence: |
  Owner repair authority: точные слова текущей сессии — «Так, сделай тут repair. Я не хочу сейчас бегать по разным
  чатам. То есть у нас был изменён, да, добавлены параллельные треки, сделай сам repair тут, прям тут, ничего не
  вызывая. Я тебе даю права на это.» Это последовало после owner-readable выбора, где рекомендованный вариант A
  сохранял старый runner в отдельном paused track; отдельный чат/агент владелец прямо запретил.

  Fresh Direction evidence before writes: clean shared worktree at
  `HEAD e95974e5744a9aa1d4f023d1527470c48501765c`; prepared commit
  `e26367df6220e573f710e42ca08d72db343f1f23`, parent
  `1edf306a55f3975cb5206adb6939561f28df21cf`, changes exactly LOG/NOW/prepared history/dashboard/CALL.
  The prepared history/CALL predated track-mode and omitted `track`; fresh NOW already had parentless core root
  `c-exec-unity65-mac-revision-002-build-001`, so a literal overlay would have created two roots and failed G1/G10.

  Reconstruction: migration history `2026-07-17-s-repair-now-track-mode-migration-001.md` preserved the old runner
  only as HELD/NON-RUNNABLE, set WIP 6/6 and made `core` primary; its original route history
  `2026-07-12-s-repair-unity65-mac-revision-002-route-001.md` records it as non-priority and says the owner primarily
  cared that it break nothing. The prepared NearGas CALL serves the current active g-9c41/L1B-Capture task and has no
  dependency on Level, characters or the old runner.

  Final mechanical inventory: 8 unique tracks; exactly one primary (`core`); roots/decision resolve for every track;
  CALL tally `ready 4 / waiting 0 / blocked 2 / paused 3`; occupied tracks are core, level, canon, damage, visual and
  marketing = 6/6. `core` has one ready root plus the preserved min-spec decision; `dotnet-gates` has one paused root;
  `characters` retains its paused root/child graph. No task/TREE/CHARTER/knowledge value changed. Product/canon repos
  were not written or invoked.

state_changes: |
  live/indie-game-development/NOW.md:
    - SET `updated` to this repair RESULT; preserve the complete bet, all six task ids/statuses, WIP limit 6,
      existing tracks/calls/decision and every unrelated field.
    - ADD owner-approved parallel track `dotnet-gates`, label `Локальный запуск проверок .NET — пауза`, scoped to the
      existing cross-platform repository-gate runner prerequisite whose complete done_when lives in its CALL.
    - MOVE stable call id `c-exec-unity65-mac-revision-002-build-001` from `core/blocked` to
      `dotnet-gates/paused`; add this history path as `paused_by`; preserve its unresolved fresh-authority/full-packet
      condition and original route receipt in one hot-state note. Do not close, consume or relabel its outcome.
    - ADD root call `c-exec-near-gas-l1b-surface-freeze-001` to `core`, status `ready`, executor, artifact
      `work/c-exec-near-gas-l1b-surface-freeze-001-call.md`; compact its scope/boundaries to one pointer note.
    - SET `next.call` to `c-exec-near-gas-l1b-surface-freeze-001`; extraction remains ready in `canon`, not default.
  live/indie-game-development/work/c-exec-near-gas-l1b-surface-freeze-001-call.md:
    - CREATE the prepared CALL from e26367d with `track: core` added and the legacy session-id `parent` removed because
      this is the parentless core root; preserve goal/context/boundaries/done_when/return/budget semantics.
  live/indie-game-development/history/2026-07-17-s-work-near-gas-l1b-surface-freeze-dispatch-001.md:
    - SAVE the byte-identical prepared legacy RESULT from e26367d once as its replay receipt. This repair is the
      current-schema compatibility wrapper; a later identical replay must no-op rather than restore legacy routing.
  live/indie-game-development/LOG.md:
    - APPEND the prepared dispatch RESULT's declared log line once, then append this repair RESULT's declared log line
      once, both before the EOF trailer.
  live/indie-game-development/work/board/dashboard.html:
    - REGENERATE current Board/Journal/current-route surfaces from final NOW+LOG: 8 tracks, WIP 6/6, default NearGas,
      ready 4 / blocked 2 / paused 3; NearGas first code-preparation CALL ready, no product code yet; extraction and
      Level ready parallel; .NET runner preserved in paused `dotnet-gates`; keep the five open findings and 17/16/15
      journal window.
  live/indie-game-development/history/2026-07-17-s-repair-near-gas-l1b-track-rebase-001.md:
    - SAVE this full repair RESULT once with its EOF trailer. This sixth Direction path is the required repair receipt;
      the five prepared-commit paths remain the only semantically overlaid target paths.
  live/indie-game-development/TREE.md, CHARTER.md, knowledge/, os/**, canon and product repos:
    - NO CHANGE.

captures: []

decisions_needed: []

play_check:
  - "1 Name the contradiction: done — the pre-track-mode dispatch wanted a new core root while fresh NOW already had the unrelated blocked Unity/.NET runner as core root; literal overlay also omitted required track routing."
  - "2 Reconstruct: done — read fresh NOW/TREE/CHARTER/LOG, current migration and guide histories, old runner route/CALL, prepared e26367d RESULT/CALL/diff, current schema, writer rules and owner-panel contract; artifacts/commits outranked chat memory."
  - "3 Propose corrected state: done — preserve the old runner in a dedicated paused dotnet-gates track, make NearGas the sole ready core root/default, retain WIP 6/6 and every unrelated id/status."
  - "4 Confirm (owner): done — owner actual words were «сделай сам repair тут, прям тут, ничего не вызывая. Я тебе даю права на это», explicitly delegating the recommended in-place repair after the A/B brief."
  - "5 Friction: done — this is a one-off queued pre-migration RESULT crossing an owner-approved track migration, already covered by semantic-rebase/repair rules; no recurring OS rule hole was established, so no os/FRICTION.md edit."

log: 2026-07-17 — repair/rebase (core/direction/near-gas-l1b-track-rebase, s-repair-near-gas-l1b-track-rebase-001): prepared NearGas SURFACE-FREEZE dispatch @e26367d is the sole ready core root/default; the non-priority .NET runner is preserved in paused dotnet-gates, WIP stays 6/6 and product remains untouched. → history/2026-07-17-s-repair-near-gas-l1b-track-rebase-001.md

next: |
  call: c-exec-near-gas-l1b-surface-freeze-001
  track: core
  status: ready
  artifact: work/c-exec-near-gas-l1b-surface-freeze-001-call.md

END_OF_FILE: live/indie-game-development/history/2026-07-17-s-repair-near-gas-l1b-track-rebase-001.md
