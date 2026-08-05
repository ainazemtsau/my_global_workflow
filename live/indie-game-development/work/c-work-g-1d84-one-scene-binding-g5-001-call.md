# CALL — c-work-g-1d84-one-scene-binding-g5-001

to: session
direction: indie-game-development
node: g-1d84
task: t-scene-1
track: сцена
play: work
issued: 2026-08-05 by s-work-g-1d84-one-scene-binding-g5-001
status: ready

## goal

Для exact owner-tested candidate установлен независимый binding fresh-session verdict: он либо
удовлетворяет каждому исходному `done_when` и допускается к Control publication, либо имеет один
точный blocker без завышенного вывода.

## context

- Живое состояние: `live/indie-game-development/NOW.md`, задача `t-scene-1` полосы «сцена»;
  задача остаётся `active`.
- Исходный инженерный наряд со всеми пятью обязательствами:
  `live/indie-game-development/work/c-exec-g-1d84-one-scene-what-exists-001-call.md`.
- Report-only successor и его границы:
  `live/indie-game-development/work/c-exec-g-1d84-one-scene-owner-receipt-001-call.md`.
- Exact committed ancestry в `C:/projects/Unity/GasCoopGame_win-u1`:
  basis `839df47e78127fe2ebfba5eabb307bf6bdd61e9b` → runtime
  `9113b24a9a9e753de702101b3dbf1eddcf1e8e0f` → first report
  `82a6a6c4e88a4d216e8fa1db092118acf66b5fff` → owner receipt
  `923f6f7c748b61bd5e85a272b3a5e012414e992f`.
- Commit `923f6f7c748b61bd5e85a272b3a5e012414e992f` имеет единственный parent
  `82a6a6c4e88a4d216e8fa1db092118acf66b5fff`, message
  `c-exec-g-1d84-one-scene-owner-receipt-001: record owner acceptance` и manifest ровно
  `M docs/results/c-exec-g-1d84-one-scene-what-exists-001.md`.
- Report на `923f6f7c` имеет честный статус `CANDIDATE`: owner Play принят как база, fresh binding
  G5 и публикация pending. В нём дословно стоят слова владельца: «вижу старую сцену по которой
  ношу балку» и «Принимаю базу». Сила ровно такая: старая геометрия принята как основание
  `IntegratedHouse`, не как будущий вид дома.
- Diff между `9113b24a` и `923f6f7c` пуст для четырёх runtime-путей:
  `Assets/TunnelCrew/Scenes/IntegratedHouse.unity`,
  `Assets/TunnelCrew/Scenes/IntegratedHouse.unity.meta`,
  `Assets/TunnelCrew/Network/Prefabs/NetworkRuntime.prefab` и
  `ProjectSettings/EditorBuildSettings.asset`.
- Report-only leg не перезапускала tests/Deliver: нового поведения не было; review записан как
  `n/a — light change`.
- Terminal custody: WIN-U1 `DIRTY-PRESERVED`, lifecycle `CLAIMED`, lease
  `c-exec-g-1d84-one-scene-what-exists-001:BUILD`, endpoint `unrecorded`; release, integration и
  push не выполнялись.
- Семь чужих незакоммиченных путей сохранены отдельно от candidate:
  `Assets/Plugins/NuGet/.nuget-installed.json`,
  `Assets/Plugins/NuGet/McpPlugin.Common.dll`,
  `Assets/Plugins/NuGet/McpPlugin.dll`,
  `Assets/Plugins/NuGet/ReflectorNet.dll`,
  `Packages/manifest.json`, `Packages/packages-lock.json` и
  `ProjectSettings/EditorBuildSettings.asset`.

## boundaries

- Только read-only product verification: разрешено инспектировать committed objects, report, code
  и history точного candidate. Ничего не писать в product repo или slot registry.
- Семь перечисленных foreign working-tree paths не stage/commit/revert/clean/stash и не включать в
  доказательство candidate.
- Не интегрировать, не публиковать, не release, не push, не claim/release slot и не запускать новый
  owner play. Слова владельца уже committed; повторная проверка глазами этой ноге не принадлежит.
- Проверяется ровно pair runtime `9113b24a9a9e753de702101b3dbf1eddcf1e8e0f` + report
  `923f6f7c748b61bd5e85a272b3a5e012414e992f`. Изменённые или недоступные байты — blocker, а не
  новый candidate.
- Это binding G5 в новой физической сессии, отдельной от product work, owner-receipt и этой
  Direction-ноги. In-session/subagent pre-pass её не заменяет.
- Не решать будущий вид дома, t-scene-2, первое лицо, соседние полосы или судьбу чужого Unity/MCP
  diff. Product delivery, owner-eye и зелёные checks — evidence, но ни один по отдельности не
  является Direction-close.

## done_when

1. Exact identity выдержала попытку опровержения: вся ancestry разрешается; manifest `923f6f7c`
   содержит только report; четыре runtime-пути побайтово совпадают с `9113b24a`; foreign diff и
   terminal slot custody не выданы за часть candidate.
2. Каждый пункт исходного `done_when` сопоставлен с committed evidence и попыткой опровержения:
   одна runnable scene одновременно содержит двух сетевых ходоков на разных копиях и существующий
   физический груз под судьёй-создателем; Play этой сцены сразу поднимает судью без ручных экранов,
   а Lobby сохранён; Courier не получил правил, Core остался без Unity/сети; старая папка не
   менялась и её тесты не запускались; владелец нажал Play, походил и взял балку.
3. Owner-eye держится только на точных committed словах «вижу старую сцену по которой ношу балку»
   и «Принимаю базу» с их ограниченной силой; report, code/history и фактически выполненные checks
   не подменены утверждением о новом owner play или о будущем виде дома.
4. Полный Direction RESULT даёт один binding verdict. `PASS` оставляет `t-scene-1: active`, очищает
   этот CALL и регистрирует ровно один ready same-lane WIN-CTRL publication CALL
   `c-ctrl-g-1d84-one-scene-publish-001`, который сохраняет exact runtime `9113b24a` и report
   `923f6f7c` как неизменные входы. До terminal publication HOME задача не закрывается.
5. Любой реальный разрыв даёт `CHECKPOINT`, сохраняет `t-scene-1: active`, не выпускает publication
   CALL и называет ровно один точный blocker с одним same-task continuation; соседние lanes/state
   остаются без изменений.

## return

Полный RESULT по play `work`: binding verdict `PASS` либо `CHECKPOINT`; evidence-матрица по пяти
исходным обязательствам, exact commits/manifests/runtime paths, owner words, checks и custody.
При PASS — только exact `c-ctrl-g-1d84-one-scene-publish-001`; при gap — только один blocker и его
same-task continuation. Не закрывать `t-scene-1` этой ногой.

budget: one fresh physical session

END_OF_FILE: live/indie-game-development/work/c-work-g-1d84-one-scene-binding-g5-001-call.md
