# CALL c-control-g-37a1-venue-packaged-player-replace-close-001

> **RETURNED ESCALATE — DO NOT REDISPATCH (2026-07-30).** No product byte changed. This CALL incorrectly required
> `AVAILABLE` for a slot lawfully owned by its target root and treated the historical Re-sync commit as the current
> basis. Corrected successor: `c-control-g-37a1-venue-packaged-player-replace-close-002`. Prior bytes remain below as
> evidence of the accepted STOP.

> **READY FOR DISPATCH — V34 RE-SYNC HOME CONSUMED.** WIN-U3 is clean on `slot/win-u3`; local and
> `origin/slot/win-u3` read back commit `bdf4a7aa9a1cc22cd131586ba11c4e87726b30cf`, tree
> `faded29ea3a87e291a718c4adf45e9e8122e1bbc`, `validation.config` blob
> `f754601e1e127f33b98194eb1876bac4a4698bb9` and stamp 34. The old root remains contract 31 / `ACTIVE` /
> `PAIR-CANDIDATE`; no replacement, feature or Deliver stage ran during Re-sync.

direction: indie-game-development
track: t-venue
for: t-3
node: g-37a1
to: executor
kind: engineering
repo: C:\projects\Unity\GasCoopGame_win-u3
issued: 2026-07-30 by s-repair-g-37a1-venue-replacement-wait-001

engineering_contract: 34
control_plane: v34 frozen-authority replacement close
target_root: c-exec-g-37a1-venue-packaged-player-001
target_root_feature_pin: 31
planned_replaced_by: c-exec-g-37a1-venue-packaged-player-minimal-002
slot: WIN-U3
target: Local
budget: одна отдельная control-plane session; никакой feature execution

## dispatch status

**READY.** Терминальный Re-sync v34 HOME потреблён, а его обязательные preconditions заново прочитаны непосредственно
в WIN-U3:

- `validation.config` содержит `synced_contract_version: 34`, blob
  `f754601e1e127f33b98194eb1876bac4a4698bb9`;
- v34 replacement и stage-local tooling установлены; dedicated Re-sync proof:
  `docs/measurements/c-resync-g-37a1-venue-contract-v34-001-proof.json`;
- постоянная ветка — `slot/win-u3`, local/remote commit
  `bdf4a7aa9a1cc22cd131586ba11c4e87726b30cf`, tree
  `faded29ea3a87e291a718c4adf45e9e8122e1bbc`, Target — `Local`, рабочее дерево чистое и слот `WIN-U3` доступен.

Это разрешает только отдельный replacement-close ниже. Новый PLAN и любое feature/delivery execution остаются вне
этого CALL.

## goal

Без delivery и без ремонта feature-кандидата процессно закрыть старый non-released pin-31 root
`c-exec-g-37a1-venue-packaged-player-001` как `REPLACED`, назвать
`c-exec-g-37a1-venue-packaged-player-minimal-002` его planned replacement и вернуть Direction точный чистый committed
basis для последующего нового PLAN.

## context

- Текущий чистый v34 basis WIN-U3 — `bdf4a7aa9a1cc22cd131586ba11c4e87726b30cf`; rejection identity старого root
  остаётся `2a66cd10756ae17dff709a85d2e6f499f31e3dd4` и должна быть записана в replacement receipt.
- Binding refutation:
  `docs/measurements/c-exec-g-37a1-venue-packaged-player-001-pair-freeze-r1-refutation.json` и
  `docs/reviews/pair-freeze-c-exec-g-37a1-venue-packaged-player-001-r1.md`; verdict
  `PAIR_FREEZE_RETRY_1_REFUTATION_BLOCKED`, eligibility `NOT_ELIGIBLE_FOR_BUILD`, PAIR-FREEZE receipt отсутствует.
- Последняя root receipt
  `docs/measurements/root-receipts/c-exec-g-37a1-venue-packaged-player-001/01-pair-candidate-r1.json` оставляет root
  `ACTIVE` на стадии `PAIR-CANDIDATE`.
- На rejected HEAD физически присутствуют старый carrier `Assets/GasCoopGame/Editor/PackagedPlayerBuild.cs`,
  test assembly `Assets/Tests/EditMode/PackagedPlayer/**` с 24 leaf tests / 5 intentional RED, а также
  `tools/packaged-player-evidence-check.ps1`, `tools/packaged-player-evidence-check.selftest.ps1` и
  `tools/verify-packaged-player.ps1`. Простая надпись “не authority” не изолирует эти bytes от checkout/gates.
- Владелец запретил ремонт старого PAIR-CANDIDATE и потребовал сохранить историю без удаления. История сохраняется
  через старые commits, ref, receipts и manifests; superseded live bytes не переносятся в replacement HEAD/gates.
- Опубликованные workflow tags v32-v34 являются доступным источником установки, но не доказательством, что продукт
  установлен/stamped. Product proof должен назвать commit в GasCoopGame и readback его `validation.config: 34`.
- Новый business scope и cuts сохранены в Direction draft
  `live/indie-game-development/work/c-exec-g-37a1-venue-packaged-player-minimal-002-call.md`, но этот draft не является
  launch authority и не исполняется в этой session.

## boundaries

- Только v34 process-close старого root. Не писать новый PLAN, production behavior, carrier, RED, tests или feature
  tools; не запускать BUILD, PAIR-CANDIDATE, PAIR-FREEZE, VALIDATE, Deliver или игровой `.exe`.
- Не чинить, не переиспользовать и не переименовывать старый PAIR-CANDIDATE. Не объявлять его delivered/PASS.
- Сохранить старые commits, frozen ref, receipts и manifests как evidence. Не переписывать Git history.
- Replacement-close может создать только разрешённый v34 control-plane commit: inventoried salvage, `replaced_by`,
  lifecycle/replacement receipt и чистый committed basis. Никакого uncommitted draft transfer.
- В replacement basis/gate scope не остаются superseded old PLAN/carrier/RED/tests/tools как authority нового change id.
  Exact `carry` и `stale` dispositions должны перечислять их по устойчивым путям/manifest identity; не полагаться на
  prose “игнорировать старое”.
- Не создавать, не удалять и не перемещать worktree; не создавать, не переключать, не переименовывать, не сбрасывать
  и не удалять ветки. Никаких stash/reset/clean/force операций.
- Если stamp/tooling/slot/root state не совпадают, frozen bytes не exact-match current HEAD или clean committed basis
  нельзя получить в пределах v34 replacement-close, вернуть настоящий `ESCALATE`; не обходить STOP.

## done_when

1. Preflight доказал published/read-back Re-sync v34 непосредственно в WIN-U3, точный слот/ветку/Target Local и
   допустимое чистое состояние checkout.
2. Старый root получил committed replacement receipt с `state: RELEASED`, terminal verdict `REPLACED`, точным
   `replaced_by: c-exec-g-37a1-venue-packaged-player-minimal-002`, старым feature pin 31 и rejection identity.
3. Старый ref, commits, receipts и manifests сохранены и разрешаются; Git history не переписана.
4. Receipt называет точный clean committed `basis`, полный inventoried salvage и path/manifest-level `carry` / `stale`
   dispositions. Старые PLAN/carrier/RED/tests/tools не входят как authority или bytes replacement checkout/gates.
5. Не выполнены feature/delivery stages и не заявлен delivery outcome. Control-plane proof/gates v34 зелёные только
   в объёме replacement-close.
6. Terminal HOME в Direction — `REPLACED` с receipt path, commit/blob identities, clean basis и dispositions; при
   невозможности ровно один настоящий `ESCALATE`. Новый PLAN автоматически не запускается.

## return

Вернуть HOME: verdict `REPLACED` или настоящий `ESCALATE`; точные receipt/ref/commit/blob paths; product stamp/readback;
старый root lifecycle; `replaced_by`; clean committed basis; полный `carry` / `stale`; список фактически затронутых
control-plane paths и подтверждение, что feature/Deliver stages не запускались.

END_OF_FILE: live/indie-game-development/work/c-control-g-37a1-venue-packaged-player-replace-close-001-call.md
