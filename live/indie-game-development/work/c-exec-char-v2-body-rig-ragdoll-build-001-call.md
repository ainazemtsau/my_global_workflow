CALL c-exec-char-v2-body-rig-ragdoll-build-001 — WAITING / NOT RUNNABLE UNTIL DIRECTION REVIEW

* id: c-exec-char-v2-body-rig-ragdoll-build-001
* track: characters
* to: executor
* for: g-6d4e «Игровые персонажи» / В2 Leg 2 — engine-side body
* issued: 2026-07-14; materialized from the frozen plan and legacy NOW by s-repair-now-track-mode-migration-001
* play: execute
* status: **WAITING ON FRESH DIRECTION REVIEW / NOT RUNNABLE**

## Dispatch gate

Track-wide пауза была снята владельцем в `history/2026-07-17-s-work-characters-resume-a1.md`, но этот root всё ещё
WAITING и не открыт к исполнению. Product handback уже опубликован. После первоначального требования не открывать
Leg 2 без отдельного решения owner дал это отдельное решение дословно: «A — открывай Leg 2 после review».
Не запускать product executor, пока одновременно не выполнены оба Direction-условия:

1. `c-review-char-v2-published-handback-release-001` дал binding Direction-вердикт по опубликованным candidate
   `0e5b2948`, integration `53453081` и dev/main `029279a`, включая уже записанный product fresh G5 `CONFIRMED`;
2. тот Direction-RESULT с verdict MET consumed review child, append-нул receipt, очистил последний `waiting_on` и
   перевёл этот существующий root в READY по owner decision «A — открывай Leg 2 после review».

После этого отдельная свежая product executor-сессия обязана до любой записи перечитать current protocol/registry
и пройти обязательную pre-write admission-проверку. READY в Direction state не является автоматическим dispatch.

До MET-review файл — recovery artifact. Он не разрешает checkout/worktree/build/merge/push и не заменяет свежую
pre-write admission-проверку по действующему GasCoopGame protocol/registry. Если review вернёт PARTIALLY MET или
NOT MET, root остаётся non-runnable и ждёт названный repair/re-review successor. После MET root может стать READY,
но фактическая работа начинается только отдельной fresh product executor-сессией.

## Goal

Доставить reusable drop-in тело персонажа поверх неизменного В1 socket adapter: low-poly humanoid rig,
процедурную локомоцию из последовательных authoritative `BodyPose.Current`, изолированный косметический
PuppetMaster-ragdoll с flop/get-up blend и собственный character material. Базовый авторитетный prefab обязан
работать без gitignored `Assets/Plugins/RootMotion/`; vendor layer никогда не пишет в socket или authoritative
transform.

## Frozen source of truth

* План и исходные acceptance/cuts: `work/c-plan-characters-002-plan.md`, особенно §4 Leg 2.
* Состояние Leg 1 и обязательные carry-forward: `knowledge/g6d4e-char-v2-leg1-reaction-core.md`.
* Owner pause: `history/2026-07-16-s-work-gascoopgame-worktree-protocol-v2-blocked-001.md`.

Свежая runnable-версия обязана перечитать эти файлы и текущий product repo; никакой path/branch/SHA из старых
сессий не считается authority.

## Mandatory entry obligations

1. **C1 — inner-source re-seed на get-up.** До реализации записать отдельную ledger/acceptance-строку и получить
   настоящий RED, различающий полный gated-phase drift. Без этого authoritative pose телепортируется примерно на
   4.5–5.2 м при возврате в Normal; owner-eye «без рывка» не является единственным допустимым ловцом.
2. **C2 — правильный get-up call.** Не использовать очевидный `PlayerBodyView.GetUp()`: он форвардит в
   parameterless `IBodyReactions.GetUp()` и обходит reconcile. Интеграция обязана вызывать
   `wrapper.GetUp(restPose)`.
3. **C3 — timed auto-rise.** Отдельно связать и проверить reconcile для таймерного auto-rise: текущий интерфейс не
   сообщает wrapper, что подъём начался.
4. **C4 — F2/F3.** Переписать P3/rationale по фактическому evidence; старое объяснение «self-healing» признано
   ложным. Не выдавать латентное или owner-accepted boundary за закрытый дефект.

## Work boundaries

* Reuse low-poly humanoid skin and the existing drop-in capsule through the unchanged `PlayerBodyView` socket seam.
* Procedural locomotion may derive planar speed and turn-rate from consecutive authoritative poses; допустим
  low-poly foot-slide, но запрещён новый movement/authority source.
* PuppetMaster is write-only cosmetic presentation. Missing RootMotion leaves the base prefab functional. Switching
  to the named Unity built-in ragdoll fallback requires a separate explicit owner acknowledgement.
* Create a project-owned low-poly material only for the four character assets named by the frozen plan. Do not edit,
  replace or pin the URP default GUID and do not treat gas-scene/global-settings references as character work.
* No network authority, grid ballistics, gas-specific reactions, Sc-damage, synced ragdoll, full facial/hand rig,
  economic/canon change or fine active-muscle tuning.
* Do not close, merge or publish Leg 1 from this leg. Product gates and a merge/push are evidence, never a
  Direction-OS close.

## done_when (binding only after the dispatch gate is refreshed)

1. C1–C4 each have explicit ledger/RED/evidence disposition; C1, C2 and C3 are exercised, not prose-only.
2. Base prefab demonstrably works without RootMotion; PuppetMaster remains isolated cosmetic output and cannot
   mutate authoritative pose/socket state.
3. Rig + procedural locomotion + flop/get-up blend exist in engine, use the existing socket seam, and satisfy the
   frozen Leg 2 cuts.
4. The character-owned material fixes the four character assets without modifying the URP default GUID or gas
   scenes/global settings.
5. Current product gates are green with exact commands/results, and the seam/authority boundary is shown unchanged.
6. Engine existence proof and owner-eye LOOK both exist; LOOK explicitly checks real flop and get-up without jerk.
7. One fresh G4 reviews the product result under current model-neutral rules, then a separate fresh binding G5 attempts to refute every claim.
   The CALL remains open until that binding close evidence exists in a valid Direction-OS RESULT.

## Return

Executor returns a product RESULT and evidence pointers to the direction. The executor does not author the next CALL,
close this open_call, merge, push or declare g-6d4e/В2 complete. Published Leg 1 evidence never auto-dispatches this
file. The separate owner decision now exists — «A — открывай Leg 2 после review» — so a MET Direction review may
make this root READY; dispatch and product mutation still belong only to the later fresh executor session.

END_OF_FILE: live/indie-game-development/work/c-exec-char-v2-body-rig-ragdoll-build-001-call.md
