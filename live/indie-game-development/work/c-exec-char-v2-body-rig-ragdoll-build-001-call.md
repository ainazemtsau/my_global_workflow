CALL c-exec-char-v2-body-rig-ragdoll-build-001 — READY / FRESH EXECUTOR ELIGIBLE

* id: c-exec-char-v2-body-rig-ragdoll-build-001
* to: executor
* direction: indie-game-development
* track: characters
* repo: ainazemtsau/GasCoopGame
* kind: engineering
* node: g-6d4e
* for: g-6d4e «Игровые персонажи» / В2 Leg 2 — engine-side body
* issued: 2026-07-14; materialized from the frozen plan and legacy NOW by s-repair-now-track-mode-migration-001
* status: **READY — ELIGIBLE FOR A SEPARATE FRESH PRODUCT EXECUTOR SESSION**

## Dispatch gate

Binding fresh Direction review `s-review-char-v2-published-handback-release-001` вернул **MET** по exact candidate
`0e5b2948172574d6966bfd7bbab298489e56559c`, integration
`53453081ba54ac558d73d87c4984a54ec28cb1b4` и published `dev == main ==
029279a7a03af5869f32ddbb8b93aa49f2c6183f`. Review child consumed, последний wait очищен. Отдельное owner-решение
существует дословно: «A — открывай Leg 2 после review». Поэтому этот существующий root теперь READY.

READY — только launch eligibility. Он не выбирает worktree/branch/SHA, не создаёт checkout и не разрешает
автоматический dispatch. Отдельная свежая product executor-сессия до любой записи перечитывает current
GasCoopGame `AGENTS.md`, protocol/registry и проходит действующую pre-write admission-проверку. Любой authority,
tool, admission или scope conflict = STOP/checkpoint, не обход.

## Goal

Доставить reusable drop-in тело персонажа поверх неизменного В1 socket adapter: low-poly humanoid rig,
процедурную локомоцию из последовательных authoritative `BodyPose.Current`, изолированный косметический
PuppetMaster-ragdoll с flop/get-up blend и собственный character material. Базовый авторитетный prefab обязан
работать без gitignored `Assets/Plugins/RootMotion/`; vendor layer никогда не пишет в socket или authoritative
transform.

## Frozen source of truth

* План и исходные acceptance/cuts: `work/c-plan-characters-002-plan.md`, особенно §4 Leg 2.
* Текущий binding Leg 1 handoff: `knowledge/g6d4e-char-v2-leg1-published-acceptance.md`.
* Direction review receipt: `history/2026-07-18-s-review-char-v2-published-handback-release-001.md`.
* Exact product evidence at published 029279a: `docs/results/c-exec-char-v2-reaction-core-repair-admission-003.md`
  and `docs/reviews/review-c-exec-char-v2-reaction-core-repair-admission-003.md`.

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

Executor returns a product RESULT and exact evidence pointers HOME. The executor does not author the next CALL,
close this open_call or declare g-6d4e/В2 complete. Product gates, merge/push or owner-eye are evidence inputs only;
the Direction call remains open until a later valid Direction RESULT carries the required fresh binding close.

## Budget

One focused product executor leg. STOP with evidence before any approach substitution, extra service mutation,
scope expansion, unavailable required tool or work beyond the frozen Leg 2 boundary.

END_OF_FILE: live/indie-game-development/work/c-exec-char-v2-body-rig-ragdoll-build-001-call.md
