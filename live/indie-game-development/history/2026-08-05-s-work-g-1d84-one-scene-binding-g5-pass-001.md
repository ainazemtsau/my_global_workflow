# RESULT — s-work-g-1d84-one-scene-binding-g5-pass-001

call: c-work-g-1d84-one-scene-binding-g5-001
direction: indie-game-development
track: сцена
play: work
node/task: g-1d84 / t-scene-1
date: 2026-08-05

## outcome

PASS — отдельная fresh physical binding G5 попыталась опровергнуть все пять исходных `done_when`
exact owner-tested candidate и не нашла конкретного разрыва.

Exact chain `839df47e78127fe2ebfba5eabb307bf6bdd61e9b` → runtime
`9113b24a9a9e753de702101b3dbf1eddcf1e8e0f` → report
`82a6a6c4e88a4d216e8fa1db092118acf66b5fff` → owner receipt
`923f6f7c748b61bd5e85a272b3a5e012414e992f` выдержала refutation. Это допускает candidate только
к Control publication: `t-scene-1` остаётся `active` до terminal publication HOME.

Returning G5 CALL очищен. Зарегистрирован ровно один ready same-lane WIN-CTRL Control CALL
`c-ctrl-g-1d84-one-scene-publish-001`; соседние lanes/state и product repo не менялись.

## evidence

1. **Done_when 1 — одна runnable authoritative сцена. PASS.** Runtime commit имеет parent `839df47e`
   и tree `bd51f91d123c0422203abe4e7d3b4f4c316f8144`. Его exact manifest: R100
   `NetworkWalkers.unity` → `IntegratedHouse.unity` с неизменным blob
   `4c7b224b98b0e98dff508a65eaec4fc9d721c05c`; R100 `.meta` с неизменным blob
   `8416a25b9108ea7b9742ebc6fed2002ea9eca609`; две path-reference правки. Scene содержит
   `DirectNetworkPlayBootstrap`, `NetworkRuntime`, `NetworkWalkerCourier`,
   `NetworkCargoPresentation`, `CargoBody` и `CarryStand`. Exact committed Courier создаёт один
   cargo на server start, добавляет ходока для каждого active connection, считает `CarryWorld` на
   server tick и рассылает единый walker/cargo snapshot через ObserversRpc. Попытка опровержения
   отдельной сценой, новым поведением или client-authority не прошла.
2. **Done_when 2 — direct Play и сохранённый Lobby. PASS.** Prefab blob изменён только с online path
   `NetworkWalkers.unity` на `IntegratedHouse.unity`; offline path остаётся `Lobby.unity`.
   `DirectNetworkPlayBootstrap.Start()` на следующем frame вызывает `session.Host()` только при
   `IsIdle`. `EditorBuildSettings` сохраняет Lobby и тот же scene GUID
   `31d4e989f2353534182e51e1c86ef3e9`. Опровержение удалённым Lobby или ручным Host-экраном не прошло.
3. **Done_when 3 — Courier/Core boundary. PASS.** Runtime manifest не меняет ни одного `.cs` или Core
   path. Exact Courier по-прежнему только принимает input, вызывает rules-layer `CarryWorld` у судьи
   и публикует snapshots. `TunnelCrew.Core.asmdef` имеет `references: []` и
   `noEngineReferences: true`. Нового правила в курьере и Unity/network reference в Core нет.
4. **Done_when 4 — старая папка и старые tests. PASS.** Exact candidate manifest не содержит
   `Assets/GasCoopGame/**`. Committed report называет единственный headless run:
   `dotnet test tests/TunnelCrew.Core.Tests/TunnelCrew.Core.Tests.csproj -c Release` = 43 passed,
   0 failed, 0 skipped; `tools/check.ps1` = hygiene OK / all active gates green. Exact check script
   прямо помечает retired GasCoopGame product tests как inactive route. Опровержение касанием старой
   папки или запуском её tests не поддержано committed evidence.
5. **Done_when 5 — exact owner-eye. PASS с ограниченной силой.** Committed report дословно несёт
   «вижу старую сцену по которой ношу балку» и «Принимаю базу». Это подтверждает Play/ходьбу/балку
   и принятие старой геометрии как основания; не утверждает будущий вид дома, новый Play, G5 или
   publication. Никакой более сильный owner verdict не приписан.
6. **Identity/report refutation.** `82a6a6c4` имеет parent `9113b24a`, tree
   `3e9c270d2bfee589e6f83f3a5273773c8eec8d2e` и добавляет только report blob
   `1fd95249279318ea7d14297443ac88e8642c4352`. `923f6f7c` имеет sole parent `82a6a6c4`, tree
   `824a580c1a2f402c8853ca421e3e7e960751facf` и меняет только этот report на blob
   `42b1ed4536107be47cac953a2df5b5e35fb5c05c`. Diff четырёх runtime paths между `9113b24a` и
   `923f6f7c` пуст; report честно остаётся `CANDIDATE` до publication.
7. **Custody отделена от candidate.** Последний committed receipt сохраняет семь foreign Unity/MCP
   paths и WIN-U1 `DIRTY-PRESERVED / CLAIMED`, lease
   `c-exec-g-1d84-one-scene-what-exists-001:BUILD`, endpoint `unrecorded`. Fresh ordinary status в
   G5 не получен: Git LFS clean-filter завершился `Access is denied` на общем `lfs/tmp`. G5 не
   трогала LFS/checkout и не выдала это ограничение за clean state; Control обязан lossless readback.
8. **Независимость и review.** Это binding fresh physical Direction-сессия, отдельная от product
   build/report и предыдущего writer; subagents, Unity, tests и новый owner Play не запускались.
   `review: n/a — light change` относится к primitive rename + two path references, но G5 не снята:
   она исполнена этой отдельной refutation-сессией.

## state_changes

- `NOW.md`: оставить `t-scene-1.status: active`; заменить только checkpoint на binding G5 PASS,
  exact chain, bounded owner words, LFS/custody limitation и pending Control publication; `updated`
  перевести на эту сессию.
- `NOW.md/open_calls`: удалить только returning
  `c-work-g-1d84-one-scene-binding-g5-001`; зарегистрировать один ready parentless same-lane
  `c-ctrl-g-1d84-one-scene-publish-001` для `g-1d84/t-scene-1`. Все другие ids сохранить.
- Создать полный CALL
  `live/indie-game-development/work/c-ctrl-g-1d84-one-scene-publish-001-call.md`.
- Препендить один LOG receipt и сохранить этот полный RESULT в history. CHARTER, TREE, knowledge,
  issues, decisions, forecast, соседние полосы, product repo и slot registry не менять.

## captures

Нет. Семь foreign paths остаются product custody, не новым Direction issue этой ноги.

## decisions_needed

Нет. Control либо публикует и lossless освобождает WIN-U1, либо возвращает один точный blocker.

## play_check

- 1 recite: done — goal, пять исходных done_when, exact candidate chain и pending publication
  сопоставлены с активной ставкой `g-1d84/t-scene-1`.
- 2 owner inputs (owner): skipped — новых фактов владельца не нужно; committed report содержит exact
  «вижу старую сцену по которой ношу балку» и «Принимаю базу» с ограниченной силой.
- 3 do the work: done — fresh physical binding G5 независимо пыталась опровергнуть каждый пункт по
  exact committed objects/code/report; product bytes, Unity, tests и foreign diff не менялись.
- 4 self-check: done — пять пунктов PASS; LFS status limitation отделено от committed-object verdict;
  task не закрыта до publication.
- 5 close: done — returning id очищен, task оставлена active, зарегистрирован ровно один same-lane
  Control successor и никакая соседняя работа не выбрана.

## log

g-1d84/t-scene-1: fresh physical binding G5 вернула PASS по всем пяти done_when exact owner-tested
chain 839df47e→9113b24a→82a6a6c4→923f6f7c; задача оставлена active и открыт единственный WIN-CTRL
Control CALL на публикацию и lossless release.

## next

CALL `c-ctrl-g-1d84-one-scene-publish-001` — штатный WIN-CTRL/Control публикует exact chain поверх
fresh main/dev, переводит report в `DELIVERED` только после readback и терминально освобождает WIN-U1
только после lossless preservation семи foreign paths. Full packet:
`live/indie-game-development/work/c-ctrl-g-1d84-one-scene-publish-001-call.md`.

END_OF_FILE: live/indie-game-development/history/2026-08-05-s-work-g-1d84-one-scene-binding-g5-pass-001.md
