# RESULT s-repair-g-37a1-body-plan-publication-route-001

call: owner-confirmed recovery of c-exec-g-37a1-body-first-person-plan-amend-001
direction: indie-game-development · track: t-body · play: repair · node/task: g-37a1/t-2
date: 2026-07-30

## outcome

Character однозначно возвращён в WIN-U2. Устаревший ready
`c-exec-g-37a1-body-first-person-plan-amend-001` снят с dispatch: его фактический продуктовый результат уже
существует на `420d6f8d` как замороженный owner-approved минимальный PLAN, но обязательная публикация вернула genuine
ESCALATE и не создала новый receipt.

По выбранному владельцем варианту A выпущен один ready same-leg successor
`c-exec-g-37a1-body-plan-publication-unblock-001` с сохранённым pin 31 в WIN-U2 / Target Local. Он может изменить
только узкий product process/control-plane route: явно superseded immutable r2 RED остаётся byte-identical
`PAIR-FREEZE FAIL / NOT BUILD ELIGIBLE`, но больше не является ложным гейтом публикации нового PLAN. Любая иная
ошибка продолжает закрывать публикацию fail-closed.

t-2 остаётся active. PAIR-CANDIDATE, PAIR-FREEZE, BUILD, Unity и gameplay work этим Direction leg не запускались.
U3 Re-sync сохранён `ready`, а U4 gas root — `running`.

## evidence

- Owner confirmation: `да, вариант A, запускаем U2` после показанного выбора: сохранить старые RED как историческое
  evidence и исключить только их явно superseded immutable lineage из публикации нового Character PLAN.
- Fresh WIN-U2 readback: clean permanent `slot/win-u2`, HEAD
  `420d6f8d05984fbc9f15bc44591e8f9b2b928b69`, ahead of `origin/slot/win-u2` by 11.
- `openspec/changes/c-exec-g-37a1-body-first-person-001/PLAN.md` and
  `docs/body-first-person-decisions.md` record exact owner words `принимаю`, frozen/accepted status and publication
  blocker.
- `docs/engineering/worktree-legs/c-exec-g-37a1-body-first-person-001.md` records
  `ADMITTED-ACTIVE / PLAN-AMEND FROZEN OWNER-APPROVED / ESCALATE`: the real route produced
  `1830 passed / 16 failed`, issued no `minimal-mvp/00-plan.json` receipt and prohibited PAIR-CANDIDATE.
- Direct product check: the new receipt path is absent; the r2 Character test scope is unchanged since process tip
  `8106170d7bfdd5cad705eeab248285fcd0621339`.
- Current NOW before apply still mislabeled the completed PLAN-AMEND CALL `ready`; t-venue Re-sync was `ready`, not
  `running`; t-sim gas was `running` by its recorded product receipt.
- New complete CALL:
  `live/indie-game-development/work/c-exec-g-37a1-body-plan-publication-unblock-001-call.md`.

No product file, Unity/MCP state, test, process gate, branch, worktree or remote was changed in this Direction leg.

## state_changes

1. `NOW.md` — set `updated` to 2026-07-30 by this session.
2. `NOW.md.open_calls` — remove returned
   `c-exec-g-37a1-body-first-person-plan-amend-001`; register
   `c-exec-g-37a1-body-plan-publication-unblock-001` as the sole `ready` root in `t-body`, serving t-2, preserving
   pin 31, WIN-U2 and Target Local. Preserve every unrelated task, track, call, issue, forecast and decision.
3. Add the complete engineering CALL
   `work/c-exec-g-37a1-body-plan-publication-unblock-001-call.md`.
4. Prepend the declared LOG line and save this full RESULT once in history.

No CHARTER, TREE, bet, task, track, WIP-limit, issue, forecast or product-state field changes.

## captures

None.

## decisions_needed

None. The owner selected variant A explicitly.

## play_check

1. **Name the contradiction** — done: NOW called the U2 PLAN-AMEND `ready`, while product HEAD and lifecycle evidence
   prove it already froze the accepted plan and returned genuine ESCALATE without a receipt.
2. **Reconstruct** — done: fresh NOW, LOG/history, Direction Git, WIN-U2 Git, frozen PLAN/decision/lifecycle and receipt
   absence were read newest-first; artifacts and commits outranked chat memory.
3. **Propose corrected state** — done: one same-lane pin-31 successor replaces only the stale t-body root; U3 stays
   ready, U4 stays running and all unrelated state is preserved.
4. **Confirm (owner)** — done with exact words `да, вариант A, запускаем U2`; this authorizes the named U2 route that
   preserves old RED evidence and narrowly unblocks PLAN publication.
5. **Friction** — done: the lost/incomplete handback is represented as state drift and repaired; no new OS rule defect
   is asserted or changed here.

G1: t-body retains exactly one root and WIP is unchanged. G3/G4: appetite and bet stay unchanged. G5: t-2 and the
product root are not marked done/PASS. G7: no pending owner decision remains. G9: CHARTER/TREE untouched. G10: exact
owner words and all five repair steps are recorded.

## log

Сохранённый PLAN-AMEND@420d6f8d восстановлен как owner-approved ESCALATE, устаревший ready CALL снят; по выбранному
владельцем варианту A выпущен один pin-31 U2 successor, который узко разблокирует PLAN publication, сохраняя r2 RED
как immutable FAIL evidence и не открывая PAIR-CANDIDATE или BUILD.

## next

Dispatch `c-exec-g-37a1-body-plan-publication-unblock-001` in
`C:\projects\Unity\GasCoopGame_win-u2`, permanent branch `slot/win-u2`, Target Local. Its successful committed
product-stage handback opens only a separate fresh minimal PAIR-CANDIDATE; genuine failure returns HOME ESCALATE.

END_OF_FILE: live/indie-game-development/history/2026-07-30-s-repair-g-37a1-body-plan-publication-route-001.md
