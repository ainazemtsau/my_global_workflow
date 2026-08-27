# CALL: реакции хозяина переезжают из C# в профиль

CALL c-exec-g-5a7c-reactions-data-1-001

to: executor
direction: indie-game-development
play: work
node: g-5a7c
bet: bet-g-5a7c-wave-6
track: словарь
for: t-reactions-data-1
repo: C:\projects\Unity\GasCoopGame_win-u1
basis: origin/main @ 96fbe102 — перемерить при старте, ветка могла уехать

## goal

Двенадцатая реакция хозяина заводится **строкой в текстовом файле, без единой правки C#**.
Одиннадцать сегодняшних переезжают туда же без потерь.

## почему это первое, что делается в волне

Владелец спросил дословно: «у нас что максимум может быть 11 реакций если да то это точно нужно
исправлять». Измеренный ответ — не потолок, а два разных ценника:

- реакция из **существующих слов** словаря стоит ~25 строк C# в одном файле;
- **новое физическое действие** стоит нового члена перечисления, на котором ветвятся 7 файлов
  и 17 мест.

Второй ценник честный и снимать его не надо: кто-то обязан исполнить новое телодвижение. Первый —
чистый дефект, и он снимается насовсем.

Порядок именно такой, потому что каждая следующая работа волны добавит по слову в закрытый
словарь, и потом это придётся выносить тем же трудом плюс миграцией. Это записано в
`docs/engineering/householder-interaction-surfaces.md` §6.

## что измерено на входе — перепроверить, не принимать на веру

- `HouseholderReactionCatalog.CreateCurrent` (`Assets/TunnelCrew/Core/Householder/HouseholderReaction.cs:383-513`)
  держит все реакции списком в C#. Насчитано **11** вхождений `new HouseholderReaction`.
  Продуктовый обзор называет цифру 7 — **обзор устарел, верить замеру**.
- `HouseholderReactionDefinition` — обычный класс с **13 именованными полями**: `Name`,
  `EventName`, `NoticedFactName`, `NoticedFactLifetimeSeconds`, `Priority`, `Occupation`,
  `PhysicalActionName`, `ActionTargetName`, `Cause`, `MovementPaceName`, `ResponseKind`,
  `ReturnToLifeMode`, `RequiresSafeInterruption`, плюс делегат `Weight`.
- `HouseholderProfileLoader` (`Assets/TunnelCrew/Profiles/HouseholderProfileLoader.cs`) умеет
  только НАЗВАТЬ существующую: `references.TryResolveReaction(reactionName, out _)` → отказ по
  имени, если такой нет. Секции `reactions[]` в схеме нет вообще.
- `Assets/StreamingAssets/TunnelCrew/Householder/default.householder.json` — 2010 байт; в нём
  `occupations`, `routine`, `activeResponseRules`, `behaviorBranches`, `decisionHandlers`.
  Секций `gauges` и `reactions` нет.

## done_when

1. **ДВЕНАДЦАТАЯ ЗАВОДИТСЯ БЕЗ C#.** Секция `reactions[]` появляется в схеме профиля. Реакция,
   которой не было, собранная из уже существующих слов словаря, названа в
   `default.householder.json` и **наблюдаемо сработала в запущенной игре**. Доказательство —
   прогон, а не рассуждение.
2. **ОДИННАДЦАТЬ ПЕРЕЕХАЛИ БЕЗ ПОТЕРЬ.** Все 13 полей имеют дом в схеме, включая
   `MovementPaceName`, `ReturnToLifeMode` и `RequiresSafeInterruption`. `CreateCurrent` либо
   исчезает, либо остаётся ровно встроенным запасным набором с одним названным основанием.
3. **526 ТЕСТОВ ЗЕЛЁНЫЕ.** `dotnet test` целиком зелёный, без Unity.
4. **НЕИЗВЕСТНОЕ ИМЯ ОТКАЗЫВАЕТ ПО ИМЕНИ.** Добавлен тест: неизвестное имя реакции в профиле даёт
   отказ с именем, а не молчаливую пустую реакцию. Тот же приём уже защищает имена фактов
   (`HouseholderProfileLoader` — трёхстрочный `switch`, неизвестное имя отказывает).
5. **ВТОРОЙ ЦЕННИК НЕ ТРОГАЕТСЯ И НАЗВАН.** `HouseholderPhysicalActionName` и прочие перечисления
   в данные НЕ выносятся. В возврате одной строкой: что осталось в C# и почему.

## boundaries

**ВЛАДЕЕТ ФАЙЛАМИ:** `Core/Householder/HouseholderReaction.cs`,
`Profiles/HouseholderProfileLoader.cs`, `StreamingAssets/TunnelCrew/Householder/*.json`
и их тесты.

**НЕ ТРОГАЕТ:** `Network/**`, `World/HouseholderRouteController.cs`,
`Presentation/BodyReach.cs`, `Art/**` — они принадлежат другим полосам той же волны, идущим
одновременно. Пересечение = коллизия, а не мелочь.

**НЕ ДЕЛАЕТ:** шкалу раздражения (отдельная задача `t-irritation-1`), новое физическое действие
(отдельная задача `t-world-port-1`), ни одной новой игровой реакции сверх той единственной, что
доказывает критерий 1.

## ловушка, названная заранее

`Weight` в определении — **делегат, а не значение**. В данные он не переносится. Решить и записать
в возврате, как строка профиля выбирает уже существующий вычислитель веса: по имени из закрытого
набора, или вес остаётся свойством вида реакции. Молча уронить поле нельзя.

## return

Возврат домой, в Направление: изменённые файлы, коммиты, вывод `dotnet test`, точный текст
двенадцатой реакции из json и как она наблюдалась в игре, плюс строка про то, что осталось в C#.

## budget

Половина сфокусированного дня. Волна стоит четыре дня целиком на четыре полосы.

END_OF_FILE: live/indie-game-development/work/2026-08-27-call-reactions-data-1.md
