# RESULT s-repair-g-37a1-venue-replacement-wait-001

call: owner-directed repair after contamination check
direction: indie-game-development · track: t-venue · play: repair · node/task: g-37a1/t-3
date: 2026-07-30

## outcome

Преждевременно зарегистрированный minimal PLAN больше не dispatchable. Его CALL-файл сохранён как draft с видимым
предупреждением; старый audit-grade CALL сохранён как historical evidence с RETIRED-баннером.

Единственным root в t-venue стал blocked control-plane CALL
`c-control-g-37a1-venue-packaged-player-replace-close-001`. Он не запускает feature work и ждёт терминального
published/read-back Re-sync v34. После отдельной evidence-backed разблокировки он должен в WIN-U3 процессно закрыть
старый ACTIVE pin-31 root как `REPLACED`, сохранить ref/commits/receipts/manifests и вернуть чистый committed basis с
точными `carry` / `stale` dispositions. Только последующий Direction repair сможет выпустить новый PLAN.

t-3 остаётся active; bet, tasks, tracks, WIP и остальные calls не меняются.

## evidence

- Owner approval после показанного исправления: “ты можешь это сделать и сделай вот это … потом ждем ресинк”. Слово
  “это” непосредственно относится к предыдущему предложению снять ошибочный `ready`, оформить blocked replacement
  CALL и ждать завершённый Re-sync.
- Fresh Direction state: `c-exec-g-37a1-venue-packaged-player-minimal-002` был sole `ready` root t-venue; t-3 active.
- Read-only WIN-U3: HEAD `2a66cd10756ae17dff709a85d2e6f499f31e3dd4`; old root receipt state `ACTIVE`, stage
  `PAIR-CANDIDATE`; refutation `PAIR_FREEZE_RETRY_1_REFUTATION_BLOCKED` / `NOT_ELIGIBLE_FOR_BUILD`; old carrier,
  test assembly and three audit-grade tool scripts remain tracked at HEAD; focused receipt records 24 leaf tests and
  5 intentional behavioral RED.
- Read-only WIN-U1 after owner's Re-sync launch message: clean HEAD
  `0d3c8ca099835f2dfffe27aed7e9bb1c815503d1`, `validation.config` still
  `synced_contract_version: 31`; no completed v34 Re-sync is yet visible.
- During this repair the owner returned a migration report with workflow `origin/main`
  `8773ae24687affce308bcc8c0416f8bbc9d86f75` plus tags `engineering-contract-v32`, `v33`, `v34`, explicitly saying
  product files were unchanged. That SHA is this Direction repository's preceding commit, so the report proves OS
  publication, not GasCoopGame installation. A fresh post-return read confirmed WIN-U1 remains at product HEAD
  `0d3c8ca099835f2dfffe27aed7e9bb1c815503d1` / stamp 31 and WIN-U3 remains at product HEAD
  `2a66cd10756ae17dff709a85d2e6f499f31e3dd4` / stamp 31. The blocked condition therefore remains true.
- Direction current contract is 34. `os/schema/packets.md` requires old non-released root to return committed
  `REPLACED` HOME before Direction atomically issues a current-pinned replacement with clean `basis` and exact
  `carry` / `stale`; superseded files must be absent from replacement checkout/gates while old evidence survives.
- New blocked CALL:
  `live/indie-game-development/work/c-control-g-37a1-venue-packaged-player-replace-close-001-call.md`.

No product repo write, Re-sync action, Unity/MCP action, test, build, launch, branch/worktree operation or old-candidate
repair was performed in this Direction leg.

## state_changes

1. `NOW.md` — set `updated` to 2026-07-30 by this session.
2. `NOW.md.open_calls` — remove the premature ready root
   `c-exec-g-37a1-venue-packaged-player-minimal-002`; register
   `c-control-g-37a1-venue-packaged-player-replace-close-001` as the sole root in t-venue with status `blocked`, its
   exact Re-sync/WIN-U3 `unblock_when`, serving t-3. Preserve every unrelated call/lane/task/issue/decision/forecast.
3. Add the complete blocked control-plane CALL
   `work/c-control-g-37a1-venue-packaged-player-replace-close-001-call.md`.
4. Add visible non-routing banners to the preserved old CALL and minimal draft CALL; delete neither file and preserve
   their prior bytes in Git history.
5. Prepend the declared LOG line and save this full RESULT once in history.

No CHARTER, TREE, bet, task, track or WIP-limit change.

## captures

None.

## decisions_needed

None now. Wait for the terminal Re-sync v34 HOME evidence; a start message alone does not unblock the control CALL.

## play_check

1. **Name the contradiction** — done: Direction said the minimal PLAN was `ready`, while WIN-U3 still contained an
   ACTIVE rejected root and its old RED/tests/tools; prose non-authority did not isolate those bytes.
2. **Reconstruct** — done: newest Direction state/history, WIN-U3 HEAD/receipts/refutation and WIN-U1 stamp were read;
   product artifacts outrank the earlier ready note.
3. **Propose corrected state** — done: one blocked process-close root replaces the premature PLAN; preserved CALL
   surfaces receive visible non-routing banners; t-3 and unrelated state remain unchanged.
4. **Confirm (owner)** — done: owner said “ты можешь это сделать и сделай вот это … потом ждем ресинк” immediately
   after the exact blocked replacement-call proposal.
5. **Friction** — skipped: v34 already contains the clean-replacement rule; this is hot-state drift, not a missing OS
   rule. The repair applies that existing rule and invents no new authority.

G1: t-venue still has exactly one root and it is non-dispatchable. G3/G4 unchanged. G5: nothing marked done/PASS.
G9: CHARTER/TREE untouched. G10: exact owner approval and every repair step recorded.

## log

Преждевременный minimal PLAN снят с ready; единственным frontier полосы стал blocked v34 process-close CALL, который
после завершённого Re-sync должен закрыть старый ACTIVE pin-31 root как REPLACED и вернуть чистый committed basis без
переноса старых carrier/tests/tools.

## next

Wait: terminal published/read-back Re-sync v34 evidence. Then fresh Direction repair verifies the stamp in WIN-U3 and
may change `c-control-g-37a1-venue-packaged-player-replace-close-001` from `blocked` to `ready`; no other t-venue CALL
is dispatchable.

END_OF_FILE: live/indie-game-development/history/2026-07-30-s-repair-g-37a1-venue-replacement-wait-001.md
