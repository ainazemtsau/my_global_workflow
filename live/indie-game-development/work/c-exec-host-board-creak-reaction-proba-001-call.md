# CALL — c-exec-host-board-creak-reaction-proba-001

to: executor
kind: engineering
repo: ainazemtsau/GasCoopGame
engineering_contract: 36
mode: ПРОБА — режим по умолчанию контракта 36. ОПОРА здесь НЕ включается и сама не включается.
basis: `cca530a01c49f38f676942a531c2ee837ebe2454` — ровно текущий `origin/main` и `origin/dev`,
       повторно получено из origin этой Direction-сессией 2026-08-03
direction: indie-game-development
node: g-6b13
task: b-2
track: хозяин
issued: 2026-08-03 by s-work-g-6b13-b2-first-reaction-call-issued-001
status: ready

## slot

**WIN-U1**, каталог `C:\projects\Unity\GasCoopGame_win-u1`, ветка `slot/win-u1`.

Слот проверен заново непосредственно перед выпуском, не перенесён из закрытия b-1. Источник
истины настоящего селектора —
`C:\projects\Unity\GasCoopGame_slot-state\gascoop-slot-state.v1.json`; его текущая запись для U1:
`lifecycle: AVAILABLE`, `lease: none`, `mcp_endpoint: unrecorded`. Сам checkout: ветка
`slot/win-u1`, HEAD `7067a0adbb25ded1a56e339ae14bf6a99e3b1c79`, `git status --porcelain` пуст,
`Temp/UnityLockfile` и `Library/EditorInstance.json` отсутствуют; три разрешённых skip-worktree
конфига на месте, в рабочей поверхности задачи скрытых index-флагов нет. Blob текущего
`tools/select-slot.ps1` на базе — `b1d47f14915e`; его read-only ворота и state-authority прочитаны
первой рукой. `7067a0ad` является предком `cca530a0`, поэтому обновление — чистый fast-forward.

**Первым действием исполнителя** всё равно остаётся настоящий запуск
`pwsh -NoProfile -File tools/select-slot.ps1 -Slot WIN-U1`, затем fast-forward на объявленную базу и
атомарная аренда `-Claim -LeaseId c-exec-host-board-creak-reaction-proba-001:BUILD`. Если живой
селектор в момент запуска говорит не `AVAILABLE`, база изменилась или fast-forward невозможен —
СТОП домой; другой слот самовольно не выбирать. WIN-U3 сейчас занят параллельным
`c-exec-one-carries-cargo-proba-001:BUILD`, и эта нога его не касается.

## goal

В сцене хозяина действие команды заставляет доску скрипнуть. Хозяин замечает **подозрительный
шум**, при ближайшей безопасной точке прерывания покидает обычный маршрут, идёт к отдельной
сценовой **точке прослушивания**, затем возвращается к сохранённому занятию и шагу маршрута.

Скрип **не несёт координату игрока**. Точка прослушивания — отдельная настройка самого хозяина в
сцене, а не место, которое событие выдало ему как всеведущую подсказку.

Владельцу не нужна команда игроков, чтобы это проверить: в Unity Editor он двигает точку
прослушивания, нажимает Play, одной кнопкой создаёт тот же event, который позднее создаст игра, и
видит весь след решения и реакцию капсулы.

## решение владельца — обязательная граница

Перед его ответом решение было сформулировано дословно так: **«Утверждаю B2: скрип доски создаёт
факт подозрительного шума, хозяин идёт к фиксированной точке прослушивания и затем возвращается;
реализация через расширяемый engine-free контур, без BT и GOAP.»**

Он ответил своими словами: **«Так, я с тобой согласен.»** И добавил обязательное условие проверки:
**«чтобы удобно было тестировать в сцене»**, **«чтобы я мог легко там где-то что-то событие
вызвать»**, **«это прям важно тоже»**. Ранее в том же выборе он назвал архитектурный смысл:
**«факты, реакции так, чтобы они не были хардкодными, и чтобы мы могли легко добавлять новые»** и
позднее подключить GOAP, когда появятся реальные действия и факты.

Это разрешает только описанный ниже маленький разъём. Это НЕ разрешение построить GOAP, Behavior
Tree, универсальный AI framework или вторую реакцию.

## обязательный engine-free контур

На этой ПРОБЕ существуют ровно один event, один замеченный факт и одна реакция, но между ними не
должно быть скрытой прямой команды.

1. **Event — одноразовый вход:** `BoardCreaked` сообщает только «доска скрипнула». Ни позиции
   игрока, ни Transform, ни комнаты, ни списка слушателей в нём нет.
2. **Fact — память хозяина:** engine-free `Householder.Step` превращает вход в отдельный
   `SuspiciousNoise` occurrence, защёлкивает его в единственной локальной памяти с временем и
   expiry. Event не хранится как приказ. Fact не стирается по прибытии: exact occurrence
   помечается уже обработанным, поэтому не запускает ту же реакцию снова, и исчезает только по
   expiry. Новый occurrence того же вида позднее остаётся новым событием.
3. **Decision — сменяемый порт в Core:** между snapshot памяти/факта и следующим
   intention/action существует маленькая engine-free policy-граница. Единственная production
   policy этой задачи умеет предложить только реакцию на `SuspiciousNoise`. Центральный Step и
   Unity-controller не содержат ветку вида «если скрип — переставь Transform/иди сюда». Позднее
   этот порт сможет реализовать BT, GOAP либо другую политику, не меняя вход событий, локальную
   память и исполнение действий.
4. **Intent/action — существующий семиполевой seam:** решение повышает один названный приоритет над
   `Routine`, сохраняет прежние occupation + step в `ReturnToLife`, выдаёт физическое
   `WalkToward` с отдельной целью `ListeningPoint` и причиной `SuspiciousNoise`, соблюдает
   occupation phase + `IsSafeToInterrupt`. При достижении точки возвращается к сохранённой жизни.
5. **World — переходник и показ:** Unity хранит возвращённую коробочку памяти и отдаёт её в
   `Householder.Step` нетронутой, подаёт один pending event, сценовую точку и tuning, затем только
   показывает возвращённую позицию. Ни решение, ни expiry, ни acknowledgement в MonoBehaviour не
   живут.

Policy-граница должна быть доказуемо заменяемой обычным тестовым double вне Unity. Это не вторая
игровая реакция: в production остаётся одна concrete policy и одна concrete реакция. Не строить
каталог целей, preconditions/effects/costs, план, очередь планов или общий склад фактов — это
данные, которых у игры ещё нет.

## редакторный стенд — часть поставки, не обход

На базе уже есть `HouseholderRouteControllerEditor` и Gizmos маршрута. Расширить именно этот
маленький контур встроенными средствами Unity:

- в Edit Mode у хозяина есть отдельный Transform точки прослушивания; он виден цветным Gizmo с
  подписью и двигается Scene handle/координатами так же удобно, как точки маршрута;
- в Play Mode в Inspector хозяина есть одна явно названная кнопка вроде **Emit Board Creak**;
- кнопка вызывает тот же общий event-вход controller-а, которым позднее воспользуется игровое
  действие. Ей запрещено напрямую писать fact, intention, target, local memory или Transform;
- рядом идёт live read-only след: pending event; noticed fact и сколько ему осталось до expiry;
  occupation, phase, safe-to-interrupt и priority; physical action, cause и target; return
  occupation + step. Если скрип пришёл в небезопасной фазе, владелец сразу видит сохранённый fact и
  ожидание безопасного прерывания, а не думает, что кнопка сломана;
- остановил Play, передвинул точку или поменял lifetime в settings, снова Play и нажал кнопку —
  проверяется другой вариант без правки кода. Для повторения той же ПРОБЫ отдельная сцена, игрок,
  сеть или консольная команда не нужны.

**Odin Inspector куплен владельцем, но на объявленной базе не установлен:** в
`Packages/manifest.json` его нет. Не импортировать пакет ради этой задачи. Существующий
`CustomEditor + Handles + Gizmos` даёт весь нужный стенд без зависимости; если Odin появится позже,
он сможет заменить только оболочку панели, не event/fact/decision seam.

Никакого Canvas, runtime debug HUD и кнопки в Game view. Владелец прямо просил инструмент в Unity
Editor; он не становится частью игры.

## что реально есть на базе `cca530a0`

Каждый названный ниже существующий путь разрешён через `git ls-tree cca530a0 -- <path>` в
продуктовом репозитории непосредственно перед выпуском:

| Путь | blob |
|---|---|
| `Assets/TunnelCrew/Core/TunnelCrew.Core.asmdef` | `df60855e3430` |
| `Assets/TunnelCrew/Core/Householder/Householder.cs` | `b0bce4842863` |
| `Assets/TunnelCrew/World/HouseholderRouteController.cs` | `33aad6b014c4` |
| `Assets/TunnelCrew/World/HouseholderWalkSettings.cs` | `a0fa0cd1d4a0` |
| `Assets/TunnelCrew/Editor/HouseholderRouteControllerEditor.cs` | `743ba230aa5c` |
| `Assets/TunnelCrew/Scenes/HostWalksHisDay.unity` | `6ae4f20d0e42` |
| `Assets/TunnelCrew/Settings/HouseholderWalkSettings.asset` | `9788eb5f1151` |
| `tests/TunnelCrew.Core.Tests/HouseholderTests.cs` | `507596e0567e` |
| `tests/TunnelCrew.Core.Tests/TunnelCrew.Core.Tests.csproj` | `9c2ccf8dcda5` |
| `core/TunnelCrew.Core.csproj` | `3e89fa4f45ec` |
| `Packages/manifest.json` | `b33122097a8c` |
| `ProjectSettings/ProjectVersion.txt` | `07f1ecb4ef5b` |
| `validation.config` | `5a716599405a` |
| `tools/select-slot.ps1` | `b1d47f14915e` |

Их соседние `.meta`, также названные поверхностью этой задачи, существуют на той же базе:
`Householder.cs.meta` `f5f050d7c0c1`, `HouseholderRouteController.cs.meta` `f37378548091`,
`HouseholderWalkSettings.cs.meta` `3427f4acddbf`, `HouseholderRouteControllerEditor.cs.meta`
`19e02d49888e`, `HostWalksHisDay.unity.meta` `9c836742ec2c`,
`HouseholderWalkSettings.asset.meta` `6ead5774ea2f`.

Фактическое состояние прочитано, а не угадано:

- `TunnelCrew.Core.asmdef` по-прежнему несёт `noEngineReferences: true`;
- public переход остаётся одной функцией `Householder.Step`, а сцена хранит один
  `HouseholderLocalMemory` и возвращает его нетронутым;
- `HouseholderRouteController` сейчас всегда передаёт `default` feeling, затем применяет только
  возвращённую позицию; это место становится переходником event → Step, но не получает решения;
- `Householder.cs` уже содержит cause рядом с action, target, noticed fact с временем/expiry,
  return occupation+step, occupation phase/safe interrupt, tuning и priority; поля существуют, но
  реальной реакции ещё нет;
- существующий CustomEditor уже рисует и двигает точки маршрута, controller уже рисует Gizmos;
- `core/TunnelCrew.Core.csproj` рекурсивно включает `Assets/TunnelCrew/Core/**/*.cs`, поэтому новые
  host-файлы попадут в headless build без правки проекта;
- Unity — `6000.5.5f1`; contract в `validation.config` — 36, ПРОБА default.

## owner-visible check

1. Открыть `Assets/TunnelCrew/Scenes/HostWalksHisDay.unity`. В Edit Mode передвинуть цветную точку
   прослушивания в заметно другое место; маршрутные точки по-прежнему двигаются как раньше.
2. Нажать Play, выбрать капсулу хозяина, нажать **Emit Board Creak**. Inspector сразу показывает
   event/fact и полный read-only след. Хозяин без телепорта и без знания координаты игрока при
   безопасном прерывании уходит к перемещённой точке.
3. Он доходит до неё и продолжает сохранённый маршрут с сохранённого occupation+step; тот же fact
   не запускает его по кругу. Остановить Play, передвинуть точку, повторить — реакция использует
   новое сценовое значение без изменения кода.

Это один owner-visible reaction check. Всё, что владелец видит здесь глазами, автоматическим
«проверяющим сцену» не подменять.

## headless evidence — только невидимое глазами

В существующем `tests/TunnelCrew.Core.Tests` оставить/добавить сфокусированные NUnit cases:

1. `BoardCreaked` через общий Step-вход создаёт timestamped/expiring `SuspiciousNoise`; в безопасной
   фазе concrete policy выдаёт higher-priority intention + `WalkToward(ListeningPoint)` с причиной,
   а return содержит исходные occupation и step.
2. После достижения точки exact occurrence остаётся в памяти до expiry, но отмечен обработанным и
   не запускает ту же реакцию снова; expiry удаляет его. Это проверка невидимой памяти, не сцены.
3. Test-only decision-policy double подставляется вместо production policy и его предложение
   проходит через тот же Step без Unity и без изменения центрального перехода. Double не попадает
   в production и не является второй реакцией b-3.

Существующий тест engine-free движения остаётся зелёным. Запустить `dotnet test
tests/TunnelCrew.Core.Tests`, импорт/компиляцию Unity 6000.5.5f1 и обычный `tools/check.ps1`. Не
заводить тесты «Gizmo виден», «кнопка существует», «капсула дошла», «сцена содержит объект» — это
владелец проверяет за секунды собственными глазами.

## boundaries

- **Только b-2:** один `BoardCreaked`, один `SuspiciousNoise`, одна реакция «идти к ListeningPoint»
  и возвращение через уже принятый seam. Никаких b-3, второй/третьей реакции или второго вида
  события.
- **Никаких Behavior Tree, GOAP/planner, utility-системы, behavior framework, action
  preconditions/effects/costs, динамического плана, очереди планов, fact warehouse, общей таксономии
  distraction/suspicion, escalation meter, профилей разных хозяев, anti-kiting и разрешения
  конкурирующих стимулов.** Здесь только разъём, в который эти решения смогут войти позже.
- Никаких зрения/конусов/комнат/регионов, сети, груза, копания, тоннеля, Animation System,
  Animation Event, NavMeshAgent, Rigidbody/физики движения или NetworkTransform.
- Никакого Odin/import/package change. `Packages/**`, `ProjectSettings/**`, `tools/**`,
  `validation.config`, `AGENTS.md` не менять.
- Полоса переноски неприкосновенна: не менять `Assets/TunnelCrew/Core/Movement/**`,
  `Assets/TunnelCrew/Core/Multiplayer/**`, `Assets/TunnelCrew/Network/**`, cargo-файлы/сцены и её
  тесты. Параллельный U3 не открывать и не приводить к базе.
- Разрешённая продуктовая поверхность: `Assets/TunnelCrew/Core/Householder/**`,
  `Assets/TunnelCrew/World/Householder*`, `Assets/TunnelCrew/Editor/Householder*`, только
  `Assets/TunnelCrew/Scenes/HostWalksHisDay.unity`, `Assets/TunnelCrew/Settings/Householder*`,
  `tests/TunnelCrew.Core.Tests/Householder*.cs`, обязательные Unity `.meta` и собственный
  `docs/results/c-exec-host-board-creak-reaction-proba-001.md`.
- Новые маленькие типы/файлы внутри `Core/Householder/` разрешены, если это делает event/fact/policy
  границы явными. Не превращать один файл в универсальный framework. Любой новый `Assets/**/*.cs`
  получает настоящий `.meta` в том же коммите.
- Все числа — lifetime факта и иные реально появившиеся tuning values — поля
  `HouseholderWalkSettings`/asset, не константы в коде и не предмет headless-теста. Координата точки
  — Transform сцены, не число в коде.
- Unity Editor или Unity MCP не поднимаются — СТОП. Не заменять реальный import/Play суррогатным
  source scan. Работа не помещается без запрещённой системы — один точный blocker домой, а не
  расширение.

## done_when

1. Владелец в Unity Editor передвинул точку прослушивания, нажал Play и одной Inspector-кнопкой
   вызвал скрип: капсула при безопасном прерывании пошла к этой точке и затем продолжила сохранённый
   маршрут; live panel показал event → fact → intention/action/cause/target/return.
2. Тот же event проходит через общий engine-free вход, timestamp/expiry/acknowledgement памяти и
   сменяемую decision-policy границу; editor probe не пишет решение напрямую, единственная
   production reaction не зацикливается, а test double доказывает заменяемость без второй игровой
   реакции.
3. `dotnet test tests/TunnelCrew.Core.Tests`, Unity 6000.5.5f1 import/compile и обычный
   `tools/check.ps1` зелёные; изменение ограничено перечисленной host-поверхностью и не касается
   параллельной переноски, packages или tools.

## return

**Возврат ДОМОЙ в `indie-game-development`, g-6b13 / b-2 / хозяин.**

ПРОБА — один живой цикл в этой же продуктовой сессии: собрать → владелец открыл сцену и подвигал
точку → нажал event → сказал, что не так → поправить. Для его tuning-слов не нужен новый CALL.

После его принятия глазами:

1. Нога пишет собственный `docs/results/c-exec-host-board-creak-reaction-proba-001.md` с честным
   прединтеграционным статусом; `DELIVERED on dev` ставит только интеграция после merge. Красный
   `-Deliver` на slot-ветке до этого нормален.
2. Интеграция сохраняет exact candidate родителем merge, публикует один tip на `dev`,
   `origin/dev`, `origin/main`, fast-forward-ит `slot/win-u1` и снимает ровно аренду этого CALL.
3. Домой одним сообщением: candidate/merge/published commits, результаты трёх проверок, пути
   сценового стенда и отчёта, точные слова владельца после Play, terminal selector evidence
   `WIN-U1 CLEAN / AVAILABLE / lease none`, и одна строка о том, что оказалось дороже или
   невозможнее.

Product delivery не закрывает b-2 автоматически. Direction-close требует отдельной свежей
G5-рефутации done_when и owner-eye evidence. B-3 этой ногой не открывается.

## budget

Одна маленькая ПРОБА: один event/fact/response, один существующий стенд, один editor probe, один
decision port и только сфокусированные невидимые тесты. Не помещается — STOP домой, не framework.

END_OF_FILE: live/indie-game-development/work/c-exec-host-board-creak-reaction-proba-001-call.md
