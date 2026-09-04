# RESULT — s-work-g-5a7c-loot-foundation-dispatch-001

direction: indie-game-development
play: work
node/task: g-5a7c / t-loot-1
track: house-and-things
date: 2026-08-13

owner_approved: |
  Точный архитектурный handoff передан владельцем из продуктового чата как управляющий вход. Его
  прямой приказ: «используй нижеследующее как owner-agreed архитектурный вход, оцени его и выпусти
  отдельный полноценный loot-CALL/наряд».

  Осознанный ответ на прежнюю развилку размера и состава первого BUILD дан там же: «Первый BUILD —
  входит: data types/catalog/layout/support, validation, migration 10 items, primitive IDs in host
  state/network snapshot, functional prefab-selection seam with fallback, definition-based behavior
  dispatch seam, Inspector, stale-contact correction, headless + Unity tests, full RESULT and real
  rollback/reapply if required by issued CALL».

  Старый RESULT/candidate защищён его отдельным указанием: «НЕ переоткрывай и НЕ меняй уже закрытый
  RESULT c-exec-g-5a7c-loot-1-001; старый candidate законно PRESERVED-PAUSED».

outcome: |
  **АРХИТЕКТУРА ПРИНЯТА, И ВЫПУЩЕН ОТДЕЛЬНЫЙ ПОЛНЫЙ НАРЯД
  `c-exec-g-5a7c-loot-foundation-001`.** Он идёт одним owner-approved BUILD: definitions,
  physics/visual/behavior profiles, catalog, layout, exact physical supports, validation, десять
  предметов 5/3/2, `DefinitionId` через host/network/client, prefab fallback, behavior dispatch,
  Inspector, stale-contact fix, headless/Unity/owner matrix и rollback/reapply.

  **ОЦЕНКА: ПОДХОДИТ.** Тип, физический профиль и экземпляр имеют разные identity; один каталог и
  layout заменяют silent fallback; support collider, а не покрытие, является источником высоты;
  network остаётся primitive-only; visual и behavior выбираются по definition. Два прежних
  возражения сняты без ослабления границ: Inspector спрашивает production-закон носильщиков, а
  stable `BehaviorId` registry ограничен dispatch в уже существующем `CargoThingState`-слое — без
  PaintCan, комбинаций и общего handler pipeline.

  **СТАРЫЙ КАНДИДАТ НЕ ПЕРЕОТКРЫТ.** Старый call-card остаётся `paused`, preserve-ref остаётся
  custody-only; новый CALL зарегистрирован как same-lane child для единственного законного root.
  База нового BUILD — свежий `origin/main`, а `e0a30194…` — только источник десяти строк, замера
  твёрдости и блокера.

  Дополнительного продукта-решения перед BUILD не осталось. Конкретные числовые IDs, форма registry,
  SpawnKey/CargoId rule, normal tolerance и compatibility mechanics четырёх legacy components —
  технический HOW продуктового PLAN внутри зафиксированных инвариантов.

evidence: |
  - Перед выпуском `git ls-remote` перевыведен первой рукой: `origin/main` = `origin/dev` =
    `c485b30e704b1706675dd92d15c5223b0d166b92`; preserve ref =
    `e0a301947c28ef04a8465a411104098f54d9b9f7`.
  - `c485b30e:validation.config` → `synced_contract_version: 36`; новый child наследует pin 36.
  - `origin/main:docs/results/c-exec-g-5a7c-loot-1-001.md` → статус
    `PRESERVED-PAUSED; NOT DELIVERED`, десять names 5/3/2, 66.548 ms / 10 240 steps и explicit
    stale-contact blocker; результат не менялся.
  - Fresh scene readback исправил факт предыдущего ревью: `IntegratedHouse` сейчас содержит runtime
    class order `0,0,1,2`, не один class-0 cargo. `GameRulesSettings.CreateCargoSpawnState` вызывает
    `AlarmClockCargoThing.InitialStateFor(classId)` для каждого экземпляра, поэтому coupling уже
    размножает alarm behavior; preserve-layout увеличил бы class-0 экземпляры до пяти.
  - Owner-authority сохранена полностью в
    `work/2026-08-13-loot-owner-architecture-handoff.md`; executable packet —
    `work/c-exec-g-5a7c-loot-foundation-001-call.md`.
  - Новый CALL содержит ровно три верхнеуровневые строки `done_when` и полную acceptance coverage:
    headless identity/copy/validation/dispatch, Unity exact support/body/presentation/solidity/contact,
    owner-eye profile/covering/model mapping.

state_changes: |
  1. `work/2026-08-13-loot-owner-architecture-handoff.md` добавлен как свежая owner-authority копия
     тринадцати пунктов; `work/2026-08-13-loot-structure-proposal.md` получил верхний баннер, что его
     split/registry-cut — историческое ревью, перекрытое свежим решением.
  2. Добавлен self-contained `work/c-exec-g-5a7c-loot-foundation-001-call.md` от basis `c485b30e`,
     contract 36, preserve-input `e0a30194`; он запрещает патч frozen ref/covering/manual Y и несёт
     полный включённый/исключённый scope, acceptance matrix и return contract.
  3. Зарегистрирован call-card `c-exec-g-5a7c-loot-foundation-001`: `ready`,
     `track: house-and-things`, `for: t-loot-1`, parent old paused root. Старый
     `c-exec-g-5a7c-loot-1-001` не открыт и не закрыт: добавлены только `waiting_on`, `paused_by` и
     новый точный `unblock_when`; его product RESULT/ref не менялись.
  4. `t-loot-1` получил свежий owner-decision block; note исправляет исторический дешёвый объём и
     снимает light-close, потому что support/client behavior/owner-eye требуют binding fresh review.
  5. Две прямые issue-карты переписаны в pointer form: alarm evidence исправляет class order и
     маршрутизирует stable behavior dispatch; stale-contact evidence маршрутизирует новый BUILD от
     `origin/main`, а preserve оставляет входом, не базой.
  6. Этот RESULT сохранён в history; одна journal/commit line добавлена к task, старому/новому CALL и
     обеим issue-картам. Другие tracks/calls/cards сохранены без изменений.

captures: []
decisions_needed: []

play_check:
  - 1 recite: done — служит активной ставке `g-5a7c`, task `t-loot-1` и дорожке
    `house-and-things`; цель и текущие done_when перечитаны.
  - 2 owner inputs: done — владелец дал точную структуру, полный первый-BUILD scope, запрет менять
    preserve и прямой приказ выпустить CALL; вопросов, которые знает только он, не осталось.
  - 3 do the work: done — архитектура оценена, конфликт старого review разрешён свежей властью,
    выпущен self-contained engineering CALL и сохранена owner-authority.
  - 4 self-check: done — CALL покрывает все 13 handoff sections, обе blockers/issues, три матрицы,
    exclusions, one-authority migration и return evidence; старый RESULT/ref отсутствуют в diff.
  - 5 close: done — task не закрыта; новый same-lane child зарегистрирован ready, старый root остаётся
    paused, next локален и исполним.

log: владелец выбрал один полный первый BUILD лута вместо split/cut; точный handoff сохранён, старый candidate оставлен PRESERVED-PAUSED, выпущен отдельный child CALL от свежего origin/main со stable IDs, physical supports, network/visual/behavior seams и stale-contact fix

next: |
  CALL `c-exec-g-5a7c-loot-foundation-001` — полный пакет:
  `work/c-exec-g-5a7c-loot-foundation-001-call.md`.

END_OF_FILE: live/indie-game-development/history/2026-08-13-s-work-g-5a7c-loot-foundation-dispatch-001.md
