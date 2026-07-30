# RESULT s-work-g-37a1-venue-v34-home-consume-001

call: c-resync-g-37a1-venue-contract-v34-001
direction: indie-game-development · track: t-venue · play: work · node/task: g-37a1/t-3

## outcome

Терминальный HOME `c-resync-g-37a1-venue-contract-v34-001` потреблён. Опубликованная product identity v34
подтверждена прямым read-back в WIN-U3; завершившийся re-sync root снят из hot frontier. Сохранённый
`c-control-g-37a1-venue-packaged-player-replace-close-001` зарегистрирован как единственный `ready` root t-venue.

Старый `c-exec-g-37a1-venue-packaged-player-001` остаётся engineering contract 31 / `ACTIVE` /
`PAIR-CANDIDATE`. Replacement-close, новый PLAN, feature stages и Deliver в этой Direction-сессии не выполнялись;
t-3 остаётся active.

## evidence

- Owner HOME: branch `origin/slot/win-u3`, commit `bdf4a7aa9a1cc22cd131586ba11c4e87726b30cf`, tree
  `faded29ea3a87e291a718c4adf45e9e8122e1bbc`, `validation.config` blob
  `f754601e1e127f33b98194eb1876bac4a4698bb9`, synced engineering contract 34, WIN-U3 clean and AVAILABLE.
- Fresh direct WIN-U3 read-back: checkout `slot/win-u3...origin/slot/win-u3` with no changed paths; local and remote
  commit/tree exactly match the HOME; `git hash-object validation.config` matches the HOME blob; file stamp is 34.
- Product proof `docs/measurements/c-resync-g-37a1-venue-contract-v34-001-proof.json` names source tags v32-v34,
  basis `2a66cd10756ae17dff709a85d2e6f499f31e3dd4`, forward-only installs, complete basis diff, v34 replacement and
  stage-local schemas, and dedicated GREEN/seeded-miss checks.
- The same proof preserves old-root receipt blob `50bab9b54b7f8c1509b8d95653500f1aafb43741`, binding-refutation blob
  `0fd1632b7b92ab1b1ef299f0243640cfd43d8c20`, feature pin 31 and lifecycle `ACTIVE / PAIR-CANDIDATE`; its execution
  exclusions set replacement, feature, Deliver, Unity/MCP and packaged-executable execution to false.
- This Direction leg only read product state. It ran no product tool, stage, build, test, Unity action, branch or
  worktree mutation.

## state_changes

1. `NOW.md.updated` -> `2026-07-30 by s-work-g-37a1-venue-v34-home-consume-001`.
2. `NOW.md.open_calls` -> remove returned `c-resync-g-37a1-venue-contract-v34-001`; register preserved
   `c-control-g-37a1-venue-packaged-player-replace-close-001` as the sole `ready` t-venue root for t-3, pointing to
   `work/c-control-g-37a1-venue-packaged-player-replace-close-001-call.md` and carrying the exact v34 read-back.
   Preserve every unrelated task, track, call, issue, decision and forecast.
3. `work/c-control-g-37a1-venue-packaged-player-replace-close-001-call.md` -> replace its returned/blocked banner and
   stale unblock section with `READY`, attach the exact published/read-back v34 product identity and proof path, and
   distinguish the current clean v34 basis from the preserved old-root rejection identity. Keep its business goal,
   target root, planned replacement, boundaries, done_when and return unchanged.
4. Prepend the declared LOG line and save this full RESULT once in history.

No CHARTER, TREE, bet, task, track, WIP, issue, decision, forecast or product-repo change.

## captures

None.

## decisions_needed

None.

## play_check

1. **Recite** — done: returning re-sync serves active g-37a1 task t-3 in t-venue; its goal was a published/read-back
   v34 control-plane install without feature or replacement execution.
2. **Owner inputs (owner)** — done: owner supplied the terminal identity and lifecycle facts and explicitly said
   “Consume the completed HOME REPORT” and “Do not execute product work in this Direction session.” No further owner
   fact was needed.
3. **Do the work** — done: the HOME is consumed, the returned call is cleared, and the preserved v34
   replacement-close is the one same-lane continuation; no product work ran.
4. **Self-check** — done: re-sync done_when 1-5 is covered by the HOME, local/remote read-back and the committed proof:
   stamp/source identity; v34 dedicated checks; control-plane-only basis diff and old-root preservation; clean
   committed publication; terminal REPORT fields and execution exclusions.
5. **Close** — done: t-venue has exactly one parentless root and it is `ready`; t-3 remains active; unrelated state is
   preserved. G1/G3/G4 unchanged, G5 marks nothing done, G9 leaves CHARTER/TREE untouched, G10 records the owner words.

## log

terminal Re-sync v34 HOME потреблён и подтверждён прямым local/remote read-back WIN-U3; re-sync root снят, сохранённый
replacement-close зарегистрирован ready, старый pin-31 root остался ACTIVE / PAIR-CANDIDATE, а feature и Deliver не
запускались

## next

# CALL c-control-g-37a1-venue-packaged-player-replace-close-001

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

END_OF_FILE: live/indie-game-development/history/2026-07-30-s-work-g-37a1-venue-v34-home-consume-001.md
