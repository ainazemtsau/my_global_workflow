# RESULT — s-work-g-1d84-scene-move-and-call-frontier-001

call: нет — прямое сообщение владельца, разрешено по KERNEL §2 OPEN в `work` по активной ставке
direction: indie-game-development
track: сцена
play: work
node/task: g-1d84 / t-scene-2 (выпуск), t-host-1 (чекпойнт), t-look-1 (перемер базы)
date: 2026-08-05

## outcome

Три вещи, о которых просил владелец, сделаны на одном перемере продуктового репозитория.

**1. Наряд на переезд хозяина в общую сцену написан и выпущен** —
`c-exec-g-1d84-host-into-one-scene-001` на задачу `t-scene-2`, полоса «сцена». Задача разблокирована
фактом: `t-scene-1` закрыта и опубликована, `IntegratedHouse.unity` живёт в продуктовом `main`.
`done_when` уложен в три пункта (потолок контракта v35/v36) и повторяет подписанный текст задачи;
граница с `t-host-1` проведена резко — здесь владелец смотрит на ОДИН экран, требования «одинаково на
двух экранах» в наряде нет.

**2. Остановившийся наряд на хозяина закрыт чекпойнтом.**
`c-exec-g-1d84-host-under-the-judge-001` был выпущен `ready` 2026-08-04 и не мог стронуться с места по
трём измеренным причинам, из которых главная — у него не было площадки: его собственная открытая
строка «где показывать на двух экранах» осталась без ответа, а его же `boundaries` запрещали и править
интегрированную сцену, и заводить новую рабочую. Корень хозяина въезжает в сцену на `t-scene-2` —
задаче другой полосы, то есть наряд был выпущен раньше своей площадки. Работы потеряно ноль:
он ни разу не запускался. Наряд переведён в `blocked` с точным условием перевыпуска; разбор внутри
файла сохранён как заготовка, база намеренно НЕ перемеряна — она устареет снова, пока наряд стоит.

**3. Устаревшая база в наряде на пробу бесплатных наборов обновлена** с `839df47e` на `02a53bbb`,
целиком и первой рукой — включая перепроверку всех отсутствий, а не только того, что казалось
изменившимся.

Попутно измерением найдены и записаны два расхождения состояния с реальностью — см. §evidence.

## evidence

Всё измерено 2026-08-05 первой рукой В САМОМ продуктовом репозитории и в реестре слотов, не в чужих
рабочих каталогах (`i-call-named-path-absent-on-declared-basis-004`).

**База.** `C:/projects/Unity/GasCoopGame`: `main` = `HEAD` =
`02a53bbb4a59ae88da6d291e5b04a52b87999a32`, `git status --porcelain` — ноль строк.

**Для наряда на `t-scene-2` перемерено поимённо:** `IntegratedHouse.unity` (GUID
`31d4e989f2353534182e51e1c86ef3e9`, 23 226 байт, 11 компонентов; корни `DirectPlayBootstrap`,
`Directional Light`, `Floor`, `Main Camera`, `NetworkWorld` и один экземпляр `NetworkRuntime.prefab`);
все одиннадцать привинченных скриптов разрешены из GUID в имена файлов; `EditorBuildSettings.asset`
(три сцены, сцены хозяина нет); `HostWalksHisDay.unity` (21 267 байт, два компонента, ноль ссылок на
сетевой префаб, корни `Householder`, `Householder Route` с `Route Point 01..04`, `Listening Point`);
`HouseholderRouteController.cs` (`Update()` крутит `Householder.Step` в обычном кадре);
`CarryWorld.cs:24-26` (порядок тика `ApplyCarryLoad` → `Walkers.Advance` → `Cargo.Advance`);
`NetworkWalkerCourier.cs` (`OnServerTick:101`, `_world.Advance:107`, `PublishSnapshots:114`,
`ReceiveSnapshotsObserversRpc:167-168`); `WalkerSnapshot`/`CargoSnapshot` — хозяина в снимке нет;
`TunnelCrew.Core.asmdef` — `noEngineReferences: true`; `core/`, `tests/` — восемь тестовых файлов.
Отдельно измерено под третью строку `done_when`: в `IntegratedHouse.unity` один блок `PrefabInstance`
с 11 записями переопределений, у всех `objectReference: {fileID: 0}`; в `Lobby.unity` — тоже 11 и тоже
все пустые. Это не доказательство невозможности — слот под ссылку в файле сцены есть; строка
W06/W06a оставлена открытой к PLAN с венью «Unity у владельца».

**Для наряда на пробу перемерено:** `ProjectVersion.txt` = `6000.5.5f1`; `Assets/Plugins/Sirenix`,
`Assets/Plugins/NuGet`, `Assets/CodeRespawn/DungeonArchitect` на месте; `packages-lock.json` —
`com.unity.probuilder 6.1.2` (depth 1, притянут `com.ivanmurzak.unity.mcp.probuilder 1.2.23`);
`Assets/TunnelCrew/Art` в `main` — ноль путей; моделей `.fbx/.obj/.blend/.glb/.gltf` во всём
`Assets/TunnelCrew/**` — ноль; папок `Quaternius/Kenney/KayKit/PolyHaven` и ассетов Synty во всём
дереве — ноль; в закрытой `Assets/GasCoopGame/**` ровно три отслеживаемых файла; указатель
`git show d8d3d67f^:…/Quaternius/SOURCE.md` перепроверен и читается целиком (CC0-1.0, SHA-256 архива
на месте). FishNet `4.7.2`, `com.unity.ai.navigation 2.0.12` стоит и не используется.

**Что наряд на хозяина ни разу не запускался:** аренды `c-exec-g-1d84-host-under-the-judge-001:BUILD`
нет ни у одного из четырёх слотов; `git log --all --grep=host-under-the-judge` — пусто;
`git ls-tree main -- docs/results` этого id не содержит; ветки с ним нет.

**Слоты (реестр `C:/projects/Unity/GasCoopGame_slot-state/gascoop-slot-state.v1.json`), перемерено и
сверено с рабочими каталогами:** `WIN-U1` `AVAILABLE`, lease none, чист, HEAD `02a53bbb`, `rev-list
--left-right --count 02a53bbb...HEAD` = `0 0`; `WIN-U3` `AVAILABLE`, lease none, чист, HEAD
`839df47e`, `rev-list` = `5 0`; `WIN-U2` `CLAIMED` под `c-exec-g-1d84-three-rooms-by-hand-001:BUILD`,
`mcp_endpoint: http://localhost:27497/p/41ebd445`, ветка `slot/win-u2`, HEAD `5f94728c`;
`WIN-U4` `CLAIMED` под `c-exec-g-1d84-first-person-carry-001:BUILD`, ветка чиста на `839df47e`.

**Два расхождения состояния с реальностью, найденные попутно.** (а) `t-house-1` и `t-player-1` стояли
`ready` при взятых арендах — то есть выдавались бы к повторному запуску; переведены в `running` с
измеренными квитанциями (KERNEL §4: `running` никогда не переоткрывается). Закрытием это не является.
(б) Работа по дому в `WIN-U2` выглядит законченной (шесть коммитов, последний `docs(result): record
owner acceptance`, дифф против `839df47e` — 11 файлов, +1383/−77), но домой не возвращалась, в `main`
её нет, а ветка стоит на старой базе (`5 6` против `02a53bbb`). Заведена запись
`i-house-work-finished-in-slot-not-returned-001`. Два её факта уехали уликой в оба наряда: она
переписала `CarryStand` в СБОРЩИКА (в `Awake()` инстанцирует префаб дома одним дочерним объектом) и
завела папку `Assets/TunnelCrew/Art/`; файл сцены `.unity` она не тронула ни одной строкой.

## state_changes

- `NOW.md`: `updated` → эта нога. `tasks[t-scene-2].status` → `ready` + поле `unblocked`;
  `tasks[t-host-1].status` → `blocked_by_t-scene-2` + поле `checkpoint`; `tasks[t-house-1].status` и
  `tasks[t-player-1].status` → `running`, каждой добавлено `launch_receipt` с измеренной квитанцией.
  Прочие задачи, полосы, ставка и прогноз — сохранить без изменений.
- `NOW.md/open_calls`: зарегистрировать ready root `c-exec-g-1d84-host-into-one-scene-001` в полосе
  «сцена» для `t-scene-2` (contract 36); `c-exec-g-1d84-host-under-the-judge-001` → `status: blocked`
  с `blocked_by` и `checkpoint`; `c-exec-g-1d84-first-person-carry-001` и
  `c-exec-g-1d84-three-rooms-by-hand-001` → `status: running` с квитанциями;
  `c-exec-g-1d84-free-kits-probe-001` — обновить `dispatch` и `goal` под новую базу, добавить
  `rebased: 2026-08-05`. Ни один id не удалён.
- `NOW.md/issues`: добавить `i-house-work-finished-in-slot-not-returned-001` первой строкой; все
  прежние записи сохранить дословно.
- Создать `live/indie-game-development/work/c-exec-g-1d84-host-into-one-scene-001-call.md`.
- Правки в `live/indie-game-development/work/c-exec-g-1d84-host-under-the-judge-001-call.md`: `status`
  → `blocked`, добавлен `blocked_by`, добавлен раздел §ЧЕКПОЙНТ, над §«база и проверенные пути»
  поставлен маркер «УСТАРЕЛО». Текст `goal`/`context`/`boundaries`/`done_when`/`return` не тронут.
- Правки в `live/indie-game-development/work/c-exec-g-1d84-free-kits-probe-001-call.md`: раздел
  «база и проверенные пути» перемерен на `02a53bbb` целиком, рекомендация слота сменена на `WIN-U3`,
  добавлена строка `rebased`, обновлены `dispatch`, открытая строка «где владелец смотрит» и
  добавлена граница о чужом материале в `Art/`. `goal` и `done_when` не тронуты.
- Препендить ровно один LOG receipt и сохранить этот полный RESULT в `history/`.
  CHARTER, TREE, knowledge и продуктовый репозиторий не менять.

## captures

- Наряд, выпущенный раньше своей площадки, выглядит `ready` и стоит мёртвым, пока кто-нибудь не
  измерит слоты. Стоит подумать, обязана ли нарезка ставить наряду поле «чем разблокируется» рядом со
  статусом, — но это вопрос к OS, а не к этой ставке, и решается он maintenance.

## decisions_needed

Нет. Ни одна развилка владельца не тронута: `d-profile-file-format-recommendation-002` и
`d-toolkit-reading-of-criterion-10-002` остаются `waiting_owner` в прежнем виде. Запуск лишней полосы
(проба бесплатных наборов) по-прежнему принадлежит только владельцу.

## play_check

- 1 recite: done — цели `t-scene-2`, `t-host-1` и `t-look-1` сверены с активной ставкой `g-1d84` и с
  подписанным текстом задач; ни одна строка `done_when` не сочинена и не расширена.
- 2 owner inputs (owner): skipped — новых слов владельца ни на что здесь не нужно. Владелец судит
  результат `t-scene-2` глазами при её возврате, а запуск лишней полосы остаётся его словом.
- 3 do the work: done — один наряд написан, один остановлен чекпойнтом, у одного перемерена база.
  Продукт не изменён ни одной строкой; всё чтение — read-only.
- 4 self-check: done — каждый названный в нарядах путь проверен на объявленной базе `02a53bbb`
  командой в самом репозитории; каждое названное отсутствие посчитано; четыре открытые строки уехали
  вопросами (W04, W05, W06/W06a, порядок слияния), ни одна не закрыта нарядом.
- 5 close: done — открыт ровно один следующий CALL по порядку волны (задача 3), остальные id
  сохранены с честными статусами. Отступление от «one CALL per leg» названо прямо: владелец одним
  сообщением попросил три вещи на одной и той же границе нарядов, и все три стоят на ОДНОМ перемере
  базы — разносить их по ногам значило бы мерить одно и то же трижды. Прецедент —
  `s-work-g-1d84-first-lane-calls-001`, выпустившая три наряда одной ногой.
- G5: не применялась и не обходилась — ни одна задача этой ногой не закрыта. `t-house-1` и
  `t-player-1` переведены в `running`, а не в `done`.

## log

g-1d84: выпущен наряд на `t-scene-2` — переезд хозяина в общую сцену отдельным корнем, база и все
названные пути перемеряны первой рукой на `02a53bbb`; наряд на `t-host-1` остановлен чекпойнтом (ни
разу не запускался, площадки для его результата не существовало, база устарела) и перевыпускается
после `t-scene-2`; база наряда на пробу бесплатных наборов перемеряна с `839df47e` на `02a53bbb`.
Попутно измерением: `t-house-1` и `t-player-1` переведены в `running` по арендам слотов, а
законченная в `WIN-U2` работа по дому, домой не вернувшаяся, заведена отдельной записью.

## next

CALL `c-exec-g-1d84-host-into-one-scene-001` — переселить хозяина отдельным корнем в уже
опубликованную интегрированную сцену, поставить его рядом с двумя носильщиками и грузом и получить
честный owner-eye verdict «вижу их вместе». Слот называет владелец; рекомендация — `WIN-U1`. Full
packet: `live/indie-game-development/work/c-exec-g-1d84-host-into-one-scene-001-call.md`.
Сразу после возврата этой задачи стоит точка пересмотра аппетита.

END_OF_FILE: live/indie-game-development/history/2026-08-05-s-work-g-1d84-scene-move-and-call-frontier-001.md
