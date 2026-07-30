# RESULT s-repair-g-37a1-venue-replacement-preflight-correction-001

call: HOME ESCALATE from c-control-g-37a1-venue-packaged-player-replace-close-001
direction: indie-game-development · track: t-venue · play: repair · node/task: g-37a1/t-3
date: 2026-07-30

## outcome

Настоящий `HOME: ESCALATE` от Venue replacement-close принят как правильная остановка без продуктовых изменений.
Предыдущий CALL больше не dispatchable и сохранён с видимым `RETURNED ESCALATE`-баннером.

Единственным root t-venue стал ready successor
`c-control-g-37a1-venue-packaged-player-replace-close-002`. Он исправляет две ложные preconditions: WIN-U3 не обязан
быть `AVAILABLE`, потому что exact target root сам законно держит lease `PAIR-CANDIDATE`; опубликованный Re-sync commit
`bdf4a7aa…` является историческим доказательством установки v34, а не ещё не созданным replacement basis. Successor
работает от fresh clean local HEAD `9c9a068e…`, re-derives every ground, создаёт basis только своей terminal
replacement transaction и по-прежнему не запускает feature/BUILD/Deliver.

t-3 остаётся active; bet, tasks, tracks, WIP и остальные calls, включая Character в WIN-U2, не меняются.

## evidence

- Владелец передал terminal product handback с точными строками `HOME`, `verdict: ESCALATE`, фактической lease
  `c-exec-g-37a1-venue-packaged-player-001:PAIR-CANDIDATE`, HEAD/tree, stamp, receipt/ref и явным подтверждением, что
  новых commits и control-plane paths нет, checkout чист, feature/BUILD/Deliver не запускались.
- Fresh read-only WIN-U3: `slot/win-u3` clean, local HEAD
  `9c9a068e3b3223e2de36d50e59f6e83e682feb00`, tree `18580f6159ce0f7f5b11b3d6ac38589d4b2b7a6a`,
  22 commits ahead of `origin/slot/win-u3@bdf4a7aa9a1cc22cd131586ba11c4e87726b30cf`.
- `validation.config` still has contract 34 and Git blob `f754601e1e127f33b98194eb1876bac4a4698bb9`.
- Real selector reproduces the returned fact: state CLEAN, lifecycle CLAIMED, lease
  `c-exec-g-37a1-venue-packaged-player-001:PAIR-CANDIDATE`, `availability: STOP`. That STOP applies to fresh slot
  selection; the v34 process-close is the exact owning root's terminal control continuation.
- `refs/backup/pre-v34-cleanup/slot/win-u3` resolves to `bdf4a7aa9a1cc22cd131586ba11c4e87726b30cf`;
  rejection commit `2a66cd10756ae17dff709a85d2e6f499f31e3dd4` resolves.
- Old receipt
  `docs/measurements/root-receipts/c-exec-g-37a1-venue-packaged-player-001/01-pair-candidate-r1.json` has current Git
  blob `50bab9b54b7f8c1509b8d95653500f1aafb43741`; old PLAN/carrier/RED/tests/tools remain in checkout, as expected before
  any replacement salvage.
- The returning CALL itself required both an old `ACTIVE / PAIR-CANDIDATE` root and an `AVAILABLE` slot, and fixed
  `bdf4a7aa…` as current clean basis. Those clauses contradict the product facts and v34 replacement semantics.
- Existing issue `i-direction-to-product-call-contract-001` already routes the CALL-ground class to mandatory
  maintenance after two bounces; this third witness is added there rather than opening duplicate state.
- Complete corrected successor:
  `live/indie-game-development/work/c-control-g-37a1-venue-packaged-player-replace-close-002-call.md`.

Direction worktree had an unrelated untracked `.claude/settings.local.json`; it was preserved and excluded. No product
repo write, test, build, Unity/MCP action, launch, branch/worktree mutation or remote update was performed in this leg.

## state_changes

1. `NOW.md` — set `updated` to 2026-07-30 by this session.
2. `NOW.md.open_calls` — consume returned
   `c-control-g-37a1-venue-packaged-player-replace-close-001`; register
   `c-control-g-37a1-venue-packaged-player-replace-close-002` as the sole ready t-venue root serving t-3. Preserve all
   unrelated calls/lanes/tasks/issues/decisions/forecast.
3. Add the complete corrected successor CALL
   `work/c-control-g-37a1-venue-packaged-player-replace-close-002-call.md`.
4. Add a visible `RETURNED ESCALATE — DO NOT REDISPATCH` banner to the prior CALL without deleting its evidence.
5. Update `i-direction-to-product-call-contract-001` with the third concrete bounce, exact class and this history
   pointer; keep its existing maintenance route and trigger.
6. Prepend the declared LOG line and save this full RESULT once in history.

No CHARTER, TREE, bet, task, track or WIP-limit change.

## captures

None.

## decisions_needed

None. The corrected successor is dispatchable; a further genuine new blocker returns HOME normally.

## play_check

1. **Name the contradiction** — done: CALL required `AVAILABLE` while its own target root lawfully held
   `CLAIMED / PAIR-CANDIDATE`, and called historical Re-sync proof the current replacement basis.
2. **Reconstruct** — done newest-first from owner-forwarded HOME, Direction NOW/LOG/CALL, WIN-U3
   HEAD/tree/stamp/selector/receipt/ref and v34 rules; product artifacts match the handback.
3. **Propose corrected state** — done: consume the returned id, issue one successor under the exact owning lease,
   derive future basis only after salvage, preserve t-3 and all unrelated state.
4. **Confirm (owner)** — done by the owner forwarding the terminal handback for this exact surface beginning
   `HOME` / `verdict: ESCALATE`; this is consumption of the returned CALL, not an invented cancellation.
5. **Friction** — skipped as duplicate: `i-direction-to-product-call-contract-001` already requires a dedicated
   maintenance session and `os/FRICTION.md` already records the same unchecked-CALL-ground class. This new witness is
   appended to the existing issue; no duplicate OS line or maintenance fix is made here.

G1: t-venue still has exactly one root. G3/G4 unchanged. G5: nothing marked done/PASS. G9: CHARTER/TREE untouched.
G10: the exact returned HOME, complete repair steps and successor are recorded.

## log

Настоящий HOME: ESCALATE от Venue replacement-close принят как правильный — WIN-U3 законно CLAIMED самим target root,
поэтому требование AVAILABLE было ложным, а bdf4a7aa являлся историческим Re-sync proof, не будущим basis; продукт не
изменился, старый CALL снят с dispatch и сохранён с RETURNED-баннером, выпущен один ready successor под точной lease на
clean 9c9a068e без требования remote equality, а третий CALL-бунс добавлен к уже обязательному maintenance issue.

## next

Dispatch the sole t-venue root:
`live/indie-game-development/work/c-control-g-37a1-venue-packaged-player-replace-close-002-call.md` in the existing
`C:\projects\Unity\GasCoopGame_win-u3` checkout. The owner still needs to run the separate Character CALL in WIN-U2;
this Venue return did not touch or replace it.

END_OF_FILE: live/indie-game-development/history/2026-07-30-s-repair-g-37a1-venue-replacement-preflight-correction-001.md
