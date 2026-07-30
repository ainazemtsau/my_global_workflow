# RESULT s-repair-g-37a1-venue-resync-route-001

call: HOME ESCALATE from c-control-g-37a1-venue-packaged-player-replace-close-001
direction: indie-game-development · track: t-venue · play: repair · node/task: g-37a1/t-3
date: 2026-07-30

## outcome

Подтверждённый ESCALATE потреблён как blocker, а не как replacement outcome. Недиспетчеризуемый
`c-control-g-37a1-venue-packaged-player-replace-close-001` снят из hot frontier, но его CALL и вся история сохранены.

Единственным root в t-venue стал ready `c-resync-g-37a1-venue-contract-v34-001`: одна bounded Re-sync session прямо
в WIN-U3, без feature work, старых intentional RED/full-suite gates и replacement-close. После успешного published /
read-back HOME обычная Direction-обработка возврата сразу регистрирует сохранённый replacement-close как `ready`;
отдельный промежуточный repair-ритуал не требуется.

t-3 остаётся active; bet, tasks, tracks, WIP и остальные calls не меняются.

## evidence

- Returning HOME: replacement-close не запускался, потому что WIN-U3 не имеет product Re-sync v34; затронутых путей
  нет; feature/Deliver stages не запускались; old root остаётся ACTIVE / PAIR-CANDIDATE.
- Fresh direct WIN-U3 readback: clean `slot/win-u3`, HEAD
  `2a66cd10756ae17dff709a85d2e6f499f31e3dd4`; `validation.config` blob
  `75694f11d0166c0084d1f77c698e68e47404b139`, stamp 31; receipt/refutation blobs
  `50bab9b54b7f8c1509b8d95653500f1aafb43741` / `0fd1632b7b92ab1b1ef299f0243640cfd43d8c20`.
- Fresh direct WIN-U1 readback: clean `slot/win-u1`, HEAD
  `0d3c8ca099835f2dfffe27aed7e9bb1c815503d1`; the same validation.config blob and stamp 31. The earlier migration
  report therefore published OS/tags but installed no product contract.
- Fresh WIN-U3 path inventory still resolves the old PackagedPlayer carrier, test assembly and three evidence tools;
  they remain historical/frozen bytes and are explicitly excluded from Re-sync gates and feature execution.
- Owner approval of the exact routing change: “Если вот это твои пункты не займут долго времени, то выполняй”; “да,
  ну можешь, ну, как бы выполняй”; with the boundary “нельзя мусор оставить в workflow” and instruction to surface
  procedure-for-procedure steps.

No product repo write, Re-sync execution, Unity/MCP action, test, build, launch, branch/worktree operation or old-root
repair was performed in this Direction leg.

## state_changes

1. `NOW.md` — set `updated` to 2026-07-30 by this session.
2. `NOW.md.open_calls` — remove returned
   `c-control-g-37a1-venue-packaged-player-replace-close-001`; register
   `c-resync-g-37a1-venue-contract-v34-001` as the sole t-venue root with status `ready`, serving t-3. Preserve every
   unrelated call/lane/task/issue/decision/forecast.
3. Add complete ready `work/c-resync-g-37a1-venue-contract-v34-001-call.md` pinned `re-sync:34` to WIN-U3 / Target
   Local, bounded to control-plane install and dedicated proof with no feature/replacement execution.
4. Add a compact RETURNED ESCALATE / NOT REGISTERED banner to the preserved replacement-close CALL. Delete no work
   surface or evidence.
5. Prepend the declared LOG line and save this full RESULT once in history.

No CHARTER, TREE, bet, task, track or WIP-limit change.

## captures

- Friction candidate: a blocked prerequisite CALL was created without a dispatchable CALL that could satisfy its own
  unblock condition. The immediate repair removes that no-action wait. If this pattern repeats, maintenance should
  require every new blocked engineering frontier to name an existing actionable dependency or issue it atomically.

## decisions_needed

None.

## play_check

1. **Name the contradiction** — done: HOME and direct product readback prove stamp 31, while NOW offered only a
   blocked replacement-close and no actionable Re-sync route; waiting alone could never change the state.
2. **Reconstruct** — done: fresh NOW/TREE/CHARTER/LOG, prior repair/blocked CALL, contract v34 schema, WIN-U1 and
   WIN-U3 commit/stamp/blob/path evidence were read; product artifacts outrank the earlier migration prose.
3. **Propose corrected state** — done: consume the returned control call, preserve its file/history, and put one
   bounded `re-sync:34` root directly in WIN-U3; no other state changes.
4. **Confirm (owner)** — done: owner said “Если вот это твои пункты не займут долго времени, то выполняй” and “да,
   ну можешь, ну, как бы выполняй” after the exact four-point routing diff, explicitly requiring no workflow trash.
5. **Friction** — done: the omitted actionable prerequisite was named. The extra standalone repair after a successful
   Re-sync HOME is removed; normal processing of that HOME may immediately register the preserved replacement-close.
   No OS rule is changed in this leg; recurrence is the maintenance trigger.

G1: t-venue still has exactly one root and it is ready. G3/G4 unchanged. G5: nothing marked done/PASS. G9:
CHARTER/TREE untouched. G10: exact owner approval and every repair step recorded.

## log

Подтверждённый ESCALATE снял недиспетчеризуемый replacement-close из hot frontier; выпущен один ready re-sync:34
CALL прямо в WIN-U3, без feature/RED/full-suite работы, а успешный HOME вернёт сохранённый replacement-close сразу
без отдельного repair-шага.

## next

Dispatch `c-resync-g-37a1-venue-contract-v34-001`. Its terminal published/read-back HOME returns to Direction; on
success, consume it and register preserved `c-control-g-37a1-venue-packaged-player-replace-close-001` as ready.

END_OF_FILE: live/indie-game-development/history/2026-07-30-s-repair-g-37a1-venue-resync-route-001.md
