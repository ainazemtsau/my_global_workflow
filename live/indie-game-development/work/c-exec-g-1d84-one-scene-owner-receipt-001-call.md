# CALL — c-exec-g-1d84-one-scene-owner-receipt-001

to: executor
kind: engineering
repo: C:/projects/Unity/GasCoopGame_win-u1
engineering_contract: legacy:c-exec-g-1d84-one-scene-what-exists-001
direction: indie-game-development
node: g-1d84
task: t-scene-1
track: сцена
issued: 2026-08-05 by s-work-g-1d84-one-scene-owner-receipt-checkpoint-001
status: ready
slot: WIN-U1
basis: 82a6a6c4e88a4d216e8fa1db092118acf66b5fff

## goal

Продуктовый отчёт честно содержит уже данную владельцем приёмку базовой интегрированной сцены,
а exact runtime-кандидат остаётся неизменным и отделённым от постороннего Unity/MCP diff.

## context

- Исходный наряд:
  `live/indie-game-development/work/c-exec-g-1d84-one-scene-what-exists-001-call.md`.
- Объявленная база — `839df47e78127fe2ebfba5eabb307bf6bdd61e9b`; runtime-candidate —
  `9113b24a9a9e753de702101b3dbf1eddcf1e8e0f`; первый report commit —
  `82a6a6c4e88a4d216e8fa1db092118acf66b5fff`.
- Candidate переименовал `Assets/TunnelCrew/Scenes/NetworkWalkers.unity` в
  `Assets/TunnelCrew/Scenes/IntegratedHouse.unity` с сохранённым GUID
  `31d4e989f2353534182e51e1c86ef3e9` и перевёл две ссылки —
  `Assets/TunnelCrew/Network/Prefabs/NetworkRuntime.prefab` и
  `ProjectSettings/EditorBuildSettings.asset`. Содержимое старого сетевого стенда намеренно стало
  основанием общей сцены, а не новым визуальным домом.
- Владелец после Play сказал дословно: «вижу старую сцену по которой ношу балку». После явного
  объяснения границы между структурной базой и отдельной новой сценой он выбрал дословно:
  «Принимаю базу». Сила второго токена ровно одна: старая геометрия принята как основание; это не
  fresh G5, не публикация и не приёмка будущего вида дома. Receipt:
  `owner-ack:s-work-g-1d84-one-scene-owner-receipt-checkpoint-001#accept-base`.
- Текущий report `docs/results/c-exec-g-1d84-one-scene-what-exists-001.md` всё ещё имеет статус
  `CANDIDATE on slot/win-u1; owner Play and fresh binding G5 pending`; после слов владельца его
  owner-часть устарела и должна стать честной до возврата в Direction.
- После Play в рабочем дереве наблюдались семь НЕ принадлежащих candidate незакоммиченных путей:
  `Assets/Plugins/NuGet/.nuget-installed.json`, `Assets/Plugins/NuGet/McpPlugin.Common.dll`,
  `Assets/Plugins/NuGet/McpPlugin.dll`, `Assets/Plugins/NuGet/ReflectorNet.dll`,
  `Packages/manifest.json`, `Packages/packages-lock.json`,
  `ProjectSettings/EditorBuildSettings.asset`. Diff указывал на MCP/NuGet 0.86.2 → 0.87.0 и
  editor-сериализацию; их происхождение и желательность этим нарядом НЕ решаются.
- Реестр держит WIN-U1 в `CLAIMED` с lease
  `c-exec-g-1d84-one-scene-what-exists-001:BUILD`; candidate ещё не в `main`.

## boundaries

- Единственная разрешённая продуктовая правка —
  `docs/results/c-exec-g-1d84-one-scene-what-exists-001.md`. Runtime, scene/meta, Core, Network,
  Packages, Plugins, ProjectSettings, tools и старую папку не менять.
- Семь наблюдавшихся working-tree путей не stage/commit/revert/clean/stash и не приписывать этой
  задаче. Если report нельзя закоммитить отдельно, вернуть один точный blocker, а не очищать дерево.
- Не менять статус на `DELIVERED`, не интегрировать и не push. Законный статус после этой ноги —
  candidate с owner Play accepted и fresh binding G5 pending.
- Не запускать старые тесты. Нового поведения нет; сверить exact ancestry/manifest и честность
  отчёта достаточно. Эта нога не является G5 и не объявляет t-scene-1 done.

## done_when

1. Report называет оба точных высказывания владельца, их ограниченную силу и честный статус:
   candidate принят глазами как база, fresh binding G5 и публикация ещё впереди.
2. Новый commit имеет parent `82a6a6c4e88a4d216e8fa1db092118acf66b5fff` и меняет только report;
   `9113b24a9a9e753de702101b3dbf1eddcf1e8e0f` остаётся exact runtime ancestor, а его scene/meta и
   две ссылки не меняются ни байтом.
3. Terminal HOME называет exact report SHA, commit manifest, текущий отдельный working-tree diff и
   точное состояние WIN-U1/lease; ни один посторонний байт не выдан за clean или за результат.

## return

Полный продуктовый RESULT домой: exact parent/report commit, однопутный manifest, новый status и
дословные owner words, runtime ancestry, текущий working-tree manifest, slot/lease, отклонения и
`review: n/a — light change`. Product return не закрывает задачу: Direction после него выпускает
отдельную свежую binding G5 по exact candidate.

budget: одна механическая report-only нога

END_OF_FILE: live/indie-game-development/work/c-exec-g-1d84-one-scene-owner-receipt-001-call.md
