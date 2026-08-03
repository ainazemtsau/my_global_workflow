# RESULT — s-work-g-6b13-a3-close-verification-001

call: c-work-a3-close-verification-001
direction: indie-game-development
track: переноска
play: work
node/task: g-6b13 / a-3
date: 2026-08-03

## outcome

verdict: PASS

Binding fresh G5 в отдельной физической Direction-сессии попытался опровергнуть каждый пункт
исходного `done_when` и не нашёл разрыва. Задача a-3 закрыта: один самостоятельный груз принят
владельцем в двух окнах, вся обязательная форма подтверждена exact-кодом, проверки и exact-history
связаны с опубликованным tip, WIN-U3 терминально свободен.

Ни product RESULT, ни owner-eye, ни merge, ни зелёные проверки, ни свободный слот не использованы
по отдельности как закрытие: PASS стоит на их совместной связи с каждым пунктом исходного наряда.
Следующий same-lane root — только owner-present архитектурный разбор a-4; схема двух держателей и
инженерный наряд в этой ноге не создавались.

## evidence

1. **Owner-eye: взял → понёс → положил; обе копии совпали.** Владелец передал дословно:
   «работает»; «Так всё работает. Я одним поднял, вторым, который подключился, видно, что другой
   таскает, в новом месте остаётся. Как бы я никаких проблем не обнаружил.» Те же слова сохранены в
   опубликованном `docs/results/c-exec-one-carries-cargo-proba-001.md` на `8219f6c0`. Это не
   пересказ: в поле стоят его русские слова как есть.
2. **Решает судья; обе копии получают одно состояние.** На exact candidate `22d55e77`
   `NetworkWalkerCourier.OnStartServer` создаёт `AuthoritativeCargoRoster`, только server tick
   вызывает `_cargoRoster.Advance`, а client RPC несёт лишь `carryToggle`-намерение. Ходоки и груз
   собираются вместе и передаются одним `ReceiveSnapshotsObserversRpc(walkers, cargo)`; хост
   применяет тот же snapshot локально.
3. **Самостоятельный груз, не ребёнок игрока.** `CargoState` — отдельное состояние, presentation
   создаёт отдельный куб без `NetworkTransform`, `Rigidbody`, joint или collider behavior. Попытка
   опровержения нашла один `SetParent(transform, false)`: его parent — `NetworkWorld`/presentation,
   а не ходок; ни состояние, ни поза груза не выводятся из Unity-parent игрока. Поэтому точное
   требование наряда «не вешается на игрока родительством» выдержано.
4. **Поза вне Unity из списка длины один.** `CargoPose.Settle(CargoState,
   IReadOnlyList<CargoHold>)` использует только `System.Collections.Generic`; asmdef несёт
   `noEngineReferences: true`, а `core/TunnelCrew.Core.csproj` glob-ом включает весь Core в
   `netstandard2.1`. В рабочем roster второй holder не может появиться: `TryPickUp` пропускает груз,
   когда `Holds.Count > 0`, поэтому a-3 вызывает расчёт с длиной списка один.
5. **Форма есть; схема двух держателей не выбрана.** `CargoHold` хранит holder id, собственные
   `TargetX/TargetZ`, `Strength`, `CanEvict`; `CargoState` хранит `HomeX/HomeZ`. Третий тест создаёт
   две записи и проверяет только форму. Попытка опровержения рассмотрела `CargoPose` при искусственно
   переданном списке длиннее одного: функция читает только `holds[0]`, комментарий прямо помечает
   это placeholder и оставляет ответ a-4 нерешённым; вторая цель, сила и право вытолкнуть не
   читаются, а production roster такую длину не создаёт. Это не правило сведения двух держателей.
6. **Три заявленных теста, build и routine check.** Опубликованный отчёт фиксирует exact output:
   `dotnet build core/TunnelCrew.Core.csproj -c Release` — 0 warnings / 0 errors;
   `dotnet test ... -c Release` — 8/8, filtered `CargoPoseTests` — 3/3;
   `tools/check.ps1` — `hygiene OK`, `all active gates green`. На published tip существуют ровно
   три `[Test]` в `CargoPoseTests.cs`: empty list сохраняет позу, one holder даёт его target, shape
   несёт две записи и все обязательные поля. По read-only границе G5 не перезапускал команды,
   создающие `bin/obj`; он проверил committed run evidence и exact test source.
7. **Четыре movement-блоба не изменены.** И на candidate, и на published tip:
   `MovementInput.cs` = `6427b8091e84a92930402d4fc014b67c9dce0715`;
   `PlayerMovement.cs` = `2346fe651cff9e79bccdd9502a27b93028664813`;
   `PlayerMovement.Rule.cs` = `bfe9aa1dd6cb50271e37b8b27027ef3a5cedc21b`;
   `PlayerState.cs` = `df4a754f6a34940962034fd67b18c0ffcfedc31a`.
8. **Exact-history опубликована.** `22d55e775e1e606811c3dea50118d776ee2d8e6a` имеет единственного
   parent `cca530a01c49f38f676942a531c2ee837ebe2454`; затем идут report `e469eeae`, отдельный MPPM
   `a8ddb891`, handoff-fix `4ba8d0f1`. Merge `8ca106a96eccec2b8030c5a768adfdbbbd7157cd`
   имеет parents `2e9116fa` и `4ba8d0f1`; candidate остаётся exact ancestor candidate-side цепи.
   После delivered marker `2c51ab2c` и release `8219f6c0` текущие `HEAD`, `dev`, `origin/dev` и
   `origin/main` равны `8219f6c0bdc5e28d29353b2b29ed08932dc7253d`. Ни один task-source или
   test-файл не изменён между candidate и tip.
9. **Multiplayer Play Mode отделён.** `a8ddb891` следует после candidate/report и меняет только
   `Packages/manifest.json`, `Packages/packages-lock.json`,
   `ProjectSettings/VirtualProjectsConfig.json`; candidate этих файлов не касается. Коммит не
   использован как evidence a-3 и сохранён как отдельная owner-directed установка.
10. **WIN-U3 терминально свободен.** Fresh read: `slot/win-u3@8219f6c0`, Git status clean;
    shared state `gascoop.slot-state.v1` даёт `lifecycle: AVAILABLE`, `lease: none`, endpoint
    `unrecorded`; `Temp/UnityLockfile` и `Library/EditorInstance.json` отсутствуют, index flags
    допустимы. Это совпадает с терминальным selector receipt из входящего CALL.

## state_changes

- `NOW.md`: по stable task id `a-3` установить `status: done`, удалить её временный
  `return_checkpoint`, записать `closed` с owner-eye, binding G5, exact-history, code/form/tests,
  movement blobs, MPPM separation и WIN-U3 release evidence; обновить `updated` на эту сессию.
- `NOW.md/open_calls`: удалить returning id `c-work-a3-close-verification-001`; в той же полосе
  зарегистрировать один ready root `c-work-a4-architecture-decision-001`, `play: work`, `for: a-4`,
  pointing to `live/indie-game-development/work/c-work-a4-architecture-decision-001-call.md`.
- Создать полный CALL `live/indie-game-development/work/c-work-a4-architecture-decision-001-call.md`:
  отдельный owner-present архитектурный разбор a-4; никакого продуктового write или engineering
  handoff до фактических слов владельца.
- Препендить LOG receipt и сохранить этот полный RESULT в history. CHARTER, TREE, knowledge,
  issues, forecast, соседнюю полосу и продуктовый репозиторий сохранить без изменений.

## captures

Нет.

## decisions_needed

Нет. Архитектурный выбор a-4 принадлежит следующей owner-present ноге.

## play_check

- 1 recite: done — задача a-3, исходный наряд и обязательная форма перечитаны из свежего NOW/CALL.
- 2 owner inputs (owner): done — новых фактов не требовалось; входящий CALL и published report
  содержат его точные слова «работает» и «Так всё работает… я никаких проблем не обнаружил».
- 3 do the work: done — read-only сопоставлены exact-код candidate/tip, commit graph, refs, report,
  tests, blobs и terminal slot state; продуктовый репозиторий не менялся.
- 4 self-check: done — каждый пункт done_when получил отдельное evidence; отдельно атакованы
  `SetParent`, multi-holder placeholder, package separation и literal merge ancestry.
- 5 close: done — PASS закрывает только a-3; returning CALL снят, один owner-present same-lane
  CALL a-4 открыт без выбора схемы и без инженерного наряда.

## log

g-6b13/a-3: binding fresh G5 дал PASS по owner-eye, judge/list form, tests/build/check, неизменным
movement blobs, published exact-history и terminal WIN-U3; a-3 закрыта, открыт owner-present
архитектурный разбор a-4 без engineering handoff.

## next

CALL `c-work-a4-architecture-decision-001` — отдельная owner-present сессия `work` по задаче a-4;
до фактического вердикта владельца продуктовый CALL не выпускать.

END_OF_FILE: live/indie-game-development/history/2026-08-03-s-work-g-6b13-a3-close-verification-001.md
