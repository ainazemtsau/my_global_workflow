# CALL c-resync-g-37a1-venue-contract-v34-001


> **RETIRED 2026-07-31 — DO NOT DISPATCH.** The bet `g-37a1` was closed with verdict `obsolete` (the owner changed the game concept). Every CALL issued under it is dead regardless of the status written below. This file is preserved as evidence of what was decided, never as a frontier. The live frontier is `live/indie-game-development/NOW.md`, which currently has `bet: null` and no open calls. See `history/2026-07-31-s-review-g-37a1-obsolete-concept-change-001.md`.

direction: indie-game-development
track: t-venue
for: t-3
node: g-37a1
to: executor
kind: engineering
repo: C:\projects\Unity\GasCoopGame_win-u3
issued: 2026-07-30 by s-repair-g-37a1-venue-resync-route-001

engineering_contract: re-sync:34
slot: WIN-U3
target: Local
budget: one bounded Re-sync session; no feature execution

## goal

WIN-U3 имеет опубликованную и прочитанную обратно установку engineering contract v34, включая replacement/stage-local
control plane, без изменения продуктового поведения или состояния старого feature root.

## context

- WIN-U3 сейчас чистый на постоянной ветке `slot/win-u3`, HEAD
  `2a66cd10756ae17dff709a85d2e6f499f31e3dd4`, Target Local.
- `validation.config` blob `75694f11d0166c0084d1f77c698e68e47404b139` содержит
  `synced_contract_version: 31`; требуются forward-only deltas v32, v33 и terminal v34.
- Источник Direction OS опубликован: `engineering-contract-v32` =
  `b07961353db93116bf7e61ae7a4cb51367718f18`, `engineering-contract-v33` =
  `7038b3da6f2098a5e31dd08e0fa6b8017c846d2e`, `engineering-contract-v34` =
  `0f0a27167e98b62e2cdaa878f11ee736a011ec63`; workflow `origin/main` read back at
  `8773ae24687affce308bcc8c0416f8bbc9d86f75`.
- Старый product root `c-exec-g-37a1-venue-packaged-player-001` остаётся `ACTIVE / PAIR-CANDIDATE`; его receipt blob
  `50bab9b54b7f8c1509b8d95653500f1aafb43741`, binding refutation blob
  `0fd1632b7b92ab1b1ef299f0243640cfd43d8c20`, verdict
  `PAIR_FREEZE_RETRY_1_REFUTATION_BLOCKED / NOT_ELIGIBLE_FOR_BUILD`.
- Старые carrier/tests/tools физически остаются в checkout до отдельного v34 replacement-close. Они являются
  frozen feature evidence и не должны становиться гейтами этого Re-sync.
- Product authority: корневые `AGENTS.md`, `validation.config` и применимые repo-local Re-sync instructions. Source
  contract: `os/engineering/PROJECT_SETUP.md` и tags v32-v34 из Direction OS checkout.

## boundaries

- Только forward-only установка contract v32-v34 и её control-plane проверки. Никаких PLAN, PAIR-CANDIDATE,
  PAIR-FREEZE, BUILD, VALIDATE, Deliver, Unity или запуска `.exe`.
- Не чинить и не запускать старый PAIR-CANDIDATE. Не выполнять старые intentional RED или общий feature/full-suite
  gate как условие Re-sync; проверять только установку contract и её dedicated seeded misses/checks.
- Не выполнять replacement-close: не создавать `replaced_by`, `RELEASED`, replacement receipt, `carry/stale` или
  новый feature root. Это следующий отдельный CALL после успешного HOME.
- Не менять production behavior, gameplay assets, feature PLAN/carrier/RED/tests/tools или сохранённые
  ref/receipts/manifests. Existing feature pins и lifecycle остаются как есть.
- Не создавать, не удалять и не перемещать worktree; не менять постоянную ветку/слот; не использовать
  stash/reset/clean/force или переписывание истории.
- Если exact forward-only install, dedicated proof, clean commit, publish или remote readback невозможны, вернуть
  один настоящий `HOME: ESCALATE` без обхода STOP.

## done_when

1. В WIN-U3 установлен полный forward-only delta v32-v34, а committed `validation.config` содержит
   `synced_contract_version: 34` и точную source identity terminal v34.
2. Repo-local run/replacement/stage-local control plane соответствует v34; обязательные v34 seeded-miss и dedicated
   Re-sync проверки зелёные, причём старый intentional RED/full feature suite не запускался и не использовался как
   гейт этой установки.
3. Diff от исходного basis содержит только contract/control-plane файлы и не содержит product behavior, gameplay
   assets или feature artifacts. Старый root остаётся `ACTIVE / PAIR-CANDIDATE`; ref, receipts, manifests, frozen
   commits и старые tracked evidence bytes сохранены без replacement/release.
4. Результат committed на `slot/win-u3`, checkout чист, commit опубликован без force и remote readback подтверждает
   тот же commit/tree, stamp 34 и обязательные control-plane paths.
5. Terminal HOME — `REPORT` с точными source tags, basis/head/tree, validation.config blob, changed paths, командами и
   результатами dedicated checks, proof что feature/replacement stages не запускались; либо один настоящий `ESCALATE`.

## return

Вернуть HOME `REPORT` или настоящий `ESCALATE`: source identities; product basis/head/tree; published remote readback;
`validation.config` blob/stamp; changed paths; dedicated check/seeded-miss output; подтверждение чистого checkout,
неизменного old-root lifecycle и отсутствия feature/replacement execution.

END_OF_FILE: live/indie-game-development/work/c-resync-g-37a1-venue-contract-v34-001-call.md
