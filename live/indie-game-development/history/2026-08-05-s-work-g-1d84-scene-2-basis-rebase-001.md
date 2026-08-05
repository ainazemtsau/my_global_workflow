# RESULT — s-work-g-1d84-scene-2-basis-rebase-001

call: c-exec-g-1d84-host-into-one-scene-001 (перемерка базы, не исполнение)
direction: indie-game-development
track: сцена
play: work
node/task: g-1d84 / t-scene-2
date: 2026-08-05
owner_launch: «Так, запусти сам» — 2026-08-05, прямое указание не ждать его слова и сделать перемерку самому.

## outcome

Наряд на переезд хозяина в интегрированную сцену переведён с устаревшей базы `02a53bbb` на актуальный
`main` = `b7ae1fa4` и готов к выдаче. Пятого бунса класса «named path отсутствует на объявленной базе»
не случилось: он был бы неизбежен, потому что мир под нарядом изменился по существу за один день.

Нога НЕ исполняет наряд и не выбирает слот — слот по контракту продукта называет владелец.

## evidence

**База.** `git ls-remote origin` — `refs/heads/main` = `refs/heads/dev` = `b7ae1fa4`. Прежняя база
`02a53bbb` отстала на две публикации: `094d8f48` (трёхкомнатный дом, `t-house-1`) и
`1967fac2` → `b7ae1fa4` (первое лицо, `t-player-1`, закрыта этой же датой).

**Пути.** Все ВОСЕМНАДЦАТЬ путей, названных нарядом, проверены поштучно командой
`git cat-file -e b7ae1fa4:<путь>` — существуют все восемнадцать, ни одного `MISS`:
`Scenes/IntegratedHouse.unity`, `ProjectSettings/EditorBuildSettings.asset`,
`Scenes/HostWalksHisDay.unity`, `World/HouseholderRouteController.cs`,
`Editor/HouseholderRouteControllerEditor.cs`, `Core/Householder/Householder.cs`,
`Core/TunnelCrew.Core.asmdef`, `Core/Multiplayer/CarryWorld.cs`, `Network/NetworkWalkerCourier.cs`,
`Network/WalkerSnapshot.cs`, `Network/CargoSnapshot.cs`, `Network/WalkSpaceProbe.cs`,
`Network/CarryStand.cs`, `Network/NetworkPlaySettings.asset`, `Core/Multiplayer/WalkSpacePort.cs`,
`World/ThreeRoomHouse.prefab`, `core/TunnelCrew.Core.csproj`,
`Settings/HouseholderWalkSettings.asset`.

**Три факта первой редакции отменены и заменены явно.**

1. `Network/CarryStand.cs` на `b7ae1fa4` — сборщик: `Instantiate(_settings.HousePrefab, transform,
   false)` в строках 53-54. Дом (`World/ThreeRoomHouse.prefab`, `World/HouseWall.cs`, папка `Art/`)
   лежит в `main`. Предписание перевёрнуто: было «опираться нельзя, работа в чужом слоте», стало
   «опираться обязан, второго сборщика не заводить».
2. `Scenes/IntegratedHouse.unity` — GUID прежний `31d4e989f2353534182e51e1c86ef3e9`, размер
   23 370 байт вместо 23 226; ровно одна камера `--- !u!20 &2060976673`, `orthographic: 0`, под
   `NetworkWalkerCamera` с пятью непустыми ссылками. `NetworkWalkers.unity` в дереве отсутствует.
3. Блок `Stand` в `NetworkPlaySettings` исчез целиком вместе с `_standWallHeight`; вместо него
   `_housePrefab`, плюс поля первого лица `_eyeHeight: 1.7`, `_lookSensitivity: 0.12`,
   `_lookPitchLimit: 80`.

**Факты, которые ПРОВЕРЕНЫ И УЦЕЛЕЛИ** (первая редакция их утверждала, и они по-прежнему верны):
`ProjectSettings/EditorBuildSettings.asset` — те же три сцены (`Lobby`, `IntegratedHouse`,
`SampleScene`); `HostWalksHisDay.unity` — те же 21 267 байт, не тронута; в `IntegratedHouse.unity`
по-прежнему все 11 переопределений префаба стоят `objectReference: {fileID: 0}`, то есть непустых
ссылок на объект сцены в проекте нет ни одной.

**Слоты — перемерено И по реестру, И по рабочим каталогам,** потому что селектор смотрит на каталог:

| слот | реестр | каталог | HEAD | против `b7ae1fa4` |
|---|---|---|---|---|
| `WIN-U1` | `AVAILABLE`, lease none | чист (0 строк) | `094d8f48` | 10 позади / 0 впереди |
| `WIN-U2` | `AVAILABLE`, lease none | ГРЯЗЕН: `ProjectSettings/EditorBuildSettings.asset` | `094d8f48` | 10 / 0 |
| `WIN-U3` | `CLAIMED`, `c-exec-g-1d84-free-kits-probe-001:BUILD` | 194 незакоммиченных файла | `094d8f48` | 10 / 0 |
| `WIN-U4` | `AVAILABLE`, lease none | чист | `066fcba4` | 19 / 0 |

`WIN-U4` дополнительно: `origin/slot/win-u4` = `7e9556a1`, шесть чужих коммитов `g-37a1`, которых нет
ни локально, ни в `main` — `i-slot-u4-remote-tip-carries-foreign-commits-001`.

**Дефект базы, выведенный из объёма его словом.** Восемь стен `ThreeRoomHouse.prefab` высотой 1.5
против глаз 1.7. Владелец 2026-08-05: «Не надо стены поднимать, похуй, потом поднимем, когда будем
делать». В наряде это названо и прямо помечено как НЕ его дело и НЕ вопрос домой.

## state_changes

- `work/c-exec-g-1d84-host-into-one-scene-001-call.md`: `rebased` в шапке; `slot` переписан на
  фактическое состояние четырёх слотов; §«база и проверенные пути» переведена на `b7ae1fa4` с
  разделом об отменённых фактах и о выведенных из объёма стенах; размер сцены 23 226 → 23 370;
  абзац о «параллельной работе в чужом слоте» заменён на «работа в `main`, опираться обязан»;
  блок слотов переписан целиком. `goal`, `done_when`, `boundaries`, `return`, `budget` НЕ ТРОНУТЫ.
- `NOW.md`: `open_calls[c-exec-g-1d84-host-into-one-scene-001]` — добавлен `rebased`, `goal`
  переписан на новую базу; `issues[i-scene-2-call-basis-stale-after-publication-001]` →
  `closed_2026-08-05` + `closed_by`; `updated` → эта сессия.
- Препендить ровно один LOG receipt и сохранить этот полный RESULT в `history/`.
- CHARTER/TREE/knowledge, продуктовый репозиторий, реестр слотов и ветки не менять.

## play_check

- Вход — прямое слово владельца «Так, запусти сам» плюс его же просьба назвать простым языком, что
  можно запускать. Это перемерка чужого наряда, а не его исполнение.
- G7: ни одного продуктового или геймплейного решения за владельца не принято. Слот по-прежнему
  называет он — контракт продукта запрещает агенту выбирать. Вопрос стен закрыт ЕГО словом и в
  наряде помечен закрытым, а не поднят заново.
- G1/G2: полос по-прежнему пять, WIP-предел 3 не поднят, новых задач и полос не заведено.
- Границы наряда не расширены ни на строку: изменены только база, пути и слоты.

## next

Наряд готов к выдаче. Владелец называет слот (рекомендация `WIN-U1`) и запускает; исполнение идёт в
продуктовом репозитории отдельной свежей сессией, эта нога его не ведёт.

END_OF_FILE: live/indie-game-development/history/2026-08-05-s-work-g-1d84-scene-2-basis-rebase-001.md
