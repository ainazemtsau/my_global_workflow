# RESULT s-repair-g-37a1-character-v34-replacement-route-001

call: owner-directed Character frontier repair
direction: indie-game-development · track: t-body · play: repair · node/task: g-37a1/t-2
date: 2026-07-30

## outcome

Устаревший Character publication-unblock больше не dispatchable: его работа уже выполнена, а повторный запуск не
устранял текущий frozen-authority конфликт. Файл сохранён с видимым `RETIRED`-баннером как историческое evidence.

Единственным root в t-body стал ready control-plane CALL
`c-control-g-37a1-body-first-person-replace-close-001`. Он не запускает Character feature work: в WIN-U2 он должен
процессно закрыть старый non-released pin-31 root `c-exec-g-37a1-body-first-person-001` как v34 `REPLACED`, сохранить
старые refs/commits/receipts/manifests, получить точный `carry` / `stale` и вернуть чистый committed basis. Только после
терминального `HOME: REPLACED` отдельный Direction repair сможет выпустить новый contract-34 root
`c-exec-g-37a1-body-first-person-minimal-002` с `resume_from: PLAN`.

t-2 остаётся active; bet, tasks, tracks, WIP и остальные calls не меняются.

## evidence

- Владелец подтвердил конкретную поверхность и действие точными словами:
  `давай  починим что нуно что бы запустить character`.
- Fresh Direction state держал `c-exec-g-37a1-body-plan-publication-unblock-001` как `ready`, но его собственная note
  уже говорила `ЗАЯВЛЕННАЯ РАБОТА БОЛЬШЕ НЕ НУЖНА` и называла v34 replacement-close единственным законным путём.
- Read-only WIN-U2: clean permanent branch `slot/win-u2`, HEAD
  `8c84f90fcfd2b2a9d898451bea43560e29018d46`, tree `832d3cb0f06937f05dee205bb8954194d38208dc`;
  `validation.config` says contract 34, Git blob `6e157593bb27c5bb1b971f34c1699c5573a8032e`.
- Real selector reports `CLAIMED` with lease `c-exec-g-37a1-body-first-person-001:PAIR-CANDIDATE`; Character root is
  not released and a new slot/root cannot be treated as already available.
- Old root receipts freeze PLAN blob `346f9b41a62bb2eb43deac927c0b995b82b78da2`. The owner-approved minimal PLAN at
  commit `420d6f8d05984fbc9f15bc44591e8f9b2b928b69` and current HEAD is blob
  `bdf46175de22dfd78273305026d2a1a7a5ae6c69`; the exact minimal receipt exists at
  `docs/measurements/root-receipts/c-exec-g-37a1-body-first-person-001/minimal-mvp/00-plan.json` with Git blob
  `4d365611a4e03e6a05374c611ea7bed2695dfe18` and SHA-256
  `914f98cdc5d427d4f7d6d2c6ec45b59f49f30ca657a800d78e8d5aec90edfd62`.
- Immutable failed r2 evidence still resolves: carrier `00012b6877c4512dd6d58303805660b8cffdc731`, RED
  `3cfecc766471bf2913b63784fbd2bcb64ef0988a`, process tip
  `8106170d7bfdd5cad705eeab248285fcd0621339`, disposition
  `PAIR-FREEZE FAIL / NOT BUILD ELIGIBLE`.
- Current Direction contract is 34. `os/schema/packets.md` and `os/adapters/coding-agent.md` require a committed
  product `REPLACED` receipt before Direction atomically swaps to the new current-pinned feature root; replacement is
  not delivery and does not mark t-2 done.
- Complete replacement CALL:
  `live/indie-game-development/work/c-control-g-37a1-body-first-person-replace-close-001-call.md`.

No product repo write, Character implementation, Unity/MCP action, test, build, launch, branch/worktree operation or
old-evidence rewrite was performed in this Direction leg.

## state_changes

1. `NOW.md` — set `updated` to 2026-07-30 by this session.
2. `NOW.md.open_calls` — remove `c-exec-g-37a1-body-plan-publication-unblock-001`; register
   `c-control-g-37a1-body-first-person-replace-close-001` as the sole root in t-body with status `ready`, serving t-2.
   Preserve every unrelated call/lane/task/issue/decision/forecast.
3. Add the complete v34 control-plane CALL
   `work/c-control-g-37a1-body-first-person-replace-close-001-call.md`.
4. Add a visible non-routing `RETIRED` banner to the preserved publication-unblock CALL; delete no historical bytes.
5. Prepend the declared LOG line and save this full RESULT once in history.

No CHARTER, TREE, bet, task, track or WIP-limit change.

## captures

None.

## decisions_needed

None. The next action is the registered replacement-close CALL; the fresh Character feature root is forbidden until
its terminal `HOME: REPLACED` is consumed by Direction.

## play_check

1. **Name the contradiction** — done: a `ready` CALL ordered publication work that its own current note said was
   already complete; current evidence instead requires v34 replacement-close.
2. **Reconstruct** — done: newest Direction LOG/NOW, contract rules, WIN-U2 HEAD/stamp/selector, both frozen PLAN
   identities and failed r2 evidence were read first-hand; commits/artifacts outrank the stale routing row.
3. **Propose corrected state** — done: one ready process-close root replaces the false publication route; t-2 and all
   unrelated state remain unchanged; the future feature root is named but not created.
4. **Confirm (owner)** — done on the named open-call surface with the owner's exact words:
   `давай  починим что нуно что бы запустить character`.
5. **Friction** — skipped as duplicate: the 2026-07-30 `os/FRICTION.md` Character entry already records this exact
   frozen-PLAN/RED missing-capability class and its v34 fix. This leg applies the existing fix; it does not add another
   rule or duplicate FRICTION line.

G1: t-body still has exactly one root. G3/G4 unchanged. G5: nothing marked done/PASS. G9: CHARTER/TREE untouched.
G10: exact owner words and every repair step recorded.

## log

По прямому указанию владельца починить Character-фронтир устаревший ready publication-unblock снят и сохранён с
RETIRED-баннером — его работа уже выполнена; свежая сверка WIN-U2 подтвердила contract 34, clean HEAD, старую lease
PAIR-CANDIDATE и две несовместимые frozen-authority линии под одним change id, поэтому выпущен один ready v34
replacement-close, который только закрывает старый pin-31 root как REPLACED и возвращает чистый basis; новый Character
PLAN появится лишь отдельным Direction repair после HOME.

## next

Dispatch the sole t-body root:
`live/indie-game-development/work/c-control-g-37a1-body-first-person-replace-close-001-call.md` in the existing
`C:\projects\Unity\GasCoopGame_win-u2` checkout. Stop after `HOME: REPLACED` or genuine `HOME: ESCALATE`; only a later
Direction repair may issue the fresh contract-34 Character PLAN.

END_OF_FILE: live/indie-game-development/history/2026-07-30-s-repair-g-37a1-character-v34-replacement-route-001.md
