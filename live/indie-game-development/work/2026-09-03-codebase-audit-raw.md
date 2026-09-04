# АУДИТ КОДА И ТЕСТОВ — сырьё, шесть областей

дата: 2026-09-03 · продукт `origin/main` = `332488de` · шесть агентов, только чтение
заказан его словом **«стоп волне 12 и запускай аудит»**

**ЭТО СЫРЬЁ, А НЕ ПЛАН.** План режется отдельной ногой. Ни одна находка здесь не перепроверена
направлением первой рукой — они возвращены агентами и подлежат проверке перед правкой.
Порядок внутри области — по размеру работы, от минут к дням.


---

## ОБЛАСТЬ 1: МОЗГ ХОЗЯИНА — Assets/TunnelCrew/Probe/Householder/** (33 файла) и Assets/TunnelCrew/Probe/House/** (7 файлов). Всего 15 786 строк: 10 632 строки кода, 3 483 строки комментариев, 1 671 пустая. Читал целиком: Householder.cs, AuthoritativeHouseholder.cs, HouseholderStepInput.cs, HouseholderDecision.cs, HouseholderDecisionPipeline.cs, HouseholderStanding.cs, HouseholderEventMemory.cs, HouseholderReaction.cs, HouseWalk.cs, HouseWays.cs, все шесть handler-ов; остальные — по срезам и скриптовым замерам (длины методов, число конструкторов, мёртвые члены, мёртвые типы).

Находок: **14**

**Лучшая правка области:** Ввести одну структуру состояния тика (условно `HouseholderTickState`) с теми 12 значениями, которые сейчас размотаны в локальные переменные на Householder.cs:307–317, и передавать её ОДНИМ параметром вместо 21/17/17/12 позиционных аргументов в StepRoutine (:584), StepActiveResponse (:928), StepTrackedVisibleResponse (:1214) и StandStill (:877), а четыре ручные пересборки `new HouseholderLocalMemory(...12 аргументов...)` на строках 837, 904, 1116, 1363 заменить одним вызовом вроде `tick.ToMemory()`. Почему это лучшее отношение: правка чисто механическая, поле в поле, поведение не меняется ни на байт, проверяется существующими headless-тестами за 1 секунду — и при этом она сразу убивает единственный в области класс дефекта, который компилируется молча (перепутанные соседние int-параметры), про который сосед по файлу на строке 877–890 уже написал, что один раз обжёгся. И только ПОСЛЕ неё методы на 371 и 279 строк вообще становится можно резать: сейчас любой вынос куска требует протащить ещё десяток параметров, поэтому никто и не режет. Порядок работ: сначала это, потом удаление мёртвого кода (находка №8, минуты), потом единый Furthest (находка №3, минуты) — три первых шага не трогают поведение и дают чистое дерево под всё остальное.

### 1. [MOVE · минуты] Две разные функции Furthest с одним именем и одной подписью дают РАЗНЫЙ порядок отказов

**Где:**
- `Assets/TunnelCrew/Probe/Householder/HouseholderDecision.cs:845`
- `Assets/TunnelCrew/Probe/Householder/HouseholderLocalIncidentDecisionHandler.cs:286`
- `Assets/TunnelCrew/Probe/Householder/HouseholderLocalIncidentDecisionHandler.cs:294 (RefusalProgress)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderDecisionCandidate.cs:25`

**Во что обходится:** Обе отвечают на один вопрос — «как далеко строка дошла, прежде чем её отказали», и обе кладут ответ в один и тот же ростер, который владелец читает в панели `why`. HouseholderDecision.cs:845 сравнивает СЫРЫЕ номера enum-а (`reached > current`). HouseholderLocalIncidentDecisionHandler.cs:294 сравнивает по явной таблице, где ForbiddenFactPresent=2. В enum-е (HouseholderDecisionCandidate.cs:25) ForbiddenFactPresent=12, то есть по первой функции он «дальше», чем Won=8. Сейчас это не срабатывает, потому что ForbiddenFactPresent в каталожную ветку не попадает — это мина, а не живой баг. Но: номера enum-а 0..8 несут смысл порядка, а 9..12 дописаны сверху и смысла не несут, и одна из двух функций на этот порядок опирается. Любая следующая строка в enum молча меняет, какой отказ владелец увидит в `why` — то есть портит ровно ту поверхность, ради которой ростер и делался.

### 2. [DELETE · минуты] Мёртвый код: целый класс-политика, целая структура и три публичных свойства, которых никто не читает

**Где:**
- `Assets/TunnelCrew/Probe/Householder/HouseholderDecision.cs:908 (SuspiciousNoiseDecisionPolicy, 48 строк, ноль пользователей)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderActiveResponse.cs:117 (HouseholderFeeling)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStepInput.cs:390 (CurrentFeeling)`
- `Assets/TunnelCrew/Probe/House/HouseWalk.cs:118 (Waypoints)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderChoreDecisionHandler.cs:199 (ClosedByCount)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderDecisionPipeline.cs:250 (HandlerCount)`

**Во что обходится:** Проверял поиском по всему Assets/**/*.cs плюс tests/TunnelCrew.Core.Tests/*.cs. SuspiciousNoiseDecisionPolicy — 48 строк, реализует IHouseholderDecisionPolicy, упоминается только внутри собственного файла: ноль вызовов, ноль тестов. Это старая политика, вытесненная HouseholderReactionDecisionPolicy, но оставленная как альтернативный ответ на «кто решает» — читатель обязан выяснить, какая из двух живая. HouseholderFeeling: структура пишется в HouseholderStepInput.CurrentFeeling и не читается НИГДЕ; она тянет за собой параметр в приватном конструкторе на 20 аргументов, публичный конструктор HouseholderStepInput.cs:5 и `default(HouseholderFeeling)` в двух тестах. Waypoints, ClosedByCount, HandlerCount — по одному упоминанию каждое, то есть только объявление.

### 3. [DELETE · минуты] Тернарник, у которого обе ветки дают одно и то же значение — читается как развилка, развилкой не является

**Где:**
- `Assets/TunnelCrew/Probe/Householder/HouseholderDecisionPipeline.cs:331`
- `Assets/TunnelCrew/Probe/Householder/HouseholderDecision.cs:665`

**Во что обходится:** `return fallback.IsPresent ? default(HouseholderDecisionProposal).WithCandidates(wholeRoster) : fallback.WithCandidates(wholeRoster);` — для всех политик в дереве непредставленный fallback это либо `default`, либо `default.WithCandidates(...)`, а WithCandidates (HouseholderDecision.cs:665) поверх этого перезаписывает ростер. То есть обе ветки возвращают идентичный объект. Читатель на этом месте обязан доказать себе, что различие несущественно — на ветке, которая решает, какой будет тик, когда никто не победил.

### 4. [MOVE · часы] Один и тот же поиск строки daily-route скопирован дважды и копии РАЗОШЛИСЬ: скорость для оценки времени и скорость ходьбы берутся из разных мест

**Где:**
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:181`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:218`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:228`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:196`
- `Assets/TunnelCrew/Probe/Householder/HouseholderRoutineState.cs:205`

**Во что обходится:** Строки 181–190 (внутри MeasureTheReserve) и 218–227 (внутри StepThroughTheDay) — побайтово один и тот же блок: взять каталог, спросить строку по причине DailyRoute, при промахе спросить дефолтный каталог. Но сразу после второй копии стоит строка 228–229: `if (routineEntry.Reaction.IsDefined) dailyRoute = routineEntry.Reaction;` — переопределение реакции записью дня. В первой копии этого нет. Значит запас времени (Householder.cs:196 → Paces.MetersPerSecond(dailyRoute.MovementPaceName)) считается по скорости КАТАЛОГА, а идёт хозяин со скоростью ЗАПИСИ ДНЯ. Он оценивает, сколько у него осталось утра, по одной скорости, а шагает с другой. Проверил охват: JSON-загрузчик (HouseholderProfileLoader.cs:3171) RoutineReaction никогда не заполняет, так что сегодня расхождение достижимо только из тестов. Это мина, взведённая под ту самую фичу давления времени, которую вы делали на прошлой неделе.

### 5. [MOVE · часы] Три рукописные копии цикла «пометить съеденные факты обработанными» — ровно в том месте, про которое соседний комментарий уже предупреждает

**Где:**
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:466`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:1099`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:1334`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:1150`

**Во что обходится:** Три места обходят activeResponse.ConsumedFactOccurrences и зовут eventMemory.MarkHandled. Комментарий к DeedOfEnding (Householder.cs:1150) прямым текстом говорит: «each of those already keeps its OWN copy of "now mark the facts handled". A deed written out the same way would eventually be written at one ending and not the other, and the symptom of the missing one is the worst kind: it compiles, it walks him to the right spot, and nothing moves». То есть автор вынес в общую функцию deed, увидел дублирование цикла, описал последствия — и цикл оставил дублированным в трёх экземплярах. Цена: следующая правка правила «что считать обработанным» будет внесена в два места из трёх, и симптом будет ровно такой, как в комментарии.

### 6. [SPLIT · часы] Remember и RememberLatest: 31 строка дословно одинакового кода в двух методах памяти фактов

**Где:**
- `Assets/TunnelCrew/Probe/Householder/HouseholderEventMemory.cs:337`
- `Assets/TunnelCrew/Probe/Householder/HouseholderEventMemory.cs:406`
- `Assets/TunnelCrew/Probe/Householder/HouseholderEventMemory.cs:348`
- `Assets/TunnelCrew/Probe/Householder/HouseholderEventMemory.cs:417`
- `Assets/TunnelCrew/Probe/Householder/HouseholderEventMemory.cs:385`
- `Assets/TunnelCrew/Probe/Householder/HouseholderEventMemory.cs:460`

**Во что обходится:** Замерил построчным сравнением: строки 348–362 идентичны строкам 417–431 (разрешение позиции и комнаты, 15 строк), строки 385–400 идентичны строкам 460–475 (создание нового факта и дозапись в массив, 16 строк). Подписи у обоих методов одинаковые — девять параметров. Различаются только правилом поиска существующего факта в середине. Любая правка того, ИЗ ЧЕГО собирается запомненный факт (новое поле, новое правило комнаты), должна быть внесена дважды, и ничто не проверяет, что внесена. Файл HouseholderEventMemory.cs — единственный в области с 2,6 % комментариев при среднем 25 %, то есть он же и самый «немой» при чтении.

### 7. [MOVE · часы] От двух до одиннадцати публичных типов в одном файле — 24 файла из 40

**Где:**
- `Assets/TunnelCrew/Probe/Householder/HouseholderVocabulary.cs:1 (11 enum-ов)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderRoutineProfile.cs:1 (9 типов)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderDecision.cs:1 (8 типов)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderDecisionPipeline.cs:1 (8 типов)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStanding.cs:1 (6 типов)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderReaction.cs:1 (6 типов)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderThingBeliefs.cs:1 (6 типов)`
- `Assets/TunnelCrew/Probe/Householder/AuthoritativeHouseholder.cs:1 (4 типа)`
- `Assets/TunnelCrew/Probe/House/HouseWalk.cs:1 (3 типа)`

**Во что обходится:** Имя типа не говорит, в каком файле он лежит: HouseholderFeeling живёт в HouseholderActiveResponse.cs, HouseholderPoint — в HouseholderEvent.cs, IHouseholderWorldPort — в AuthoritativeHouseholder.cs, все одиннадцать словарных enum-ов — в HouseholderVocabulary.cs. Цена платится и вами, и агентами: каждый поиск «где определён X» превращается в grep по всей папке вместо открытия файла с этим именем, а каждая правка одного типа делает git-диф на файле, где лежат ещё семь. Правка чисто механическая и без изменения поведения — namespace один на всю сборку.

### 8. [MOVE · часы] Три четверти комментариев объясняют мотив, четверть пересказывает соседнюю строку — и объём начинает мешать читать

**Где:**
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:39`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:157`
- `Assets/TunnelCrew/Probe/Householder/AuthoritativeHouseholder.cs:1 (37,9 % строк — комментарии)`
- `Assets/TunnelCrew/Probe/House/HouseWalk.cs:474 (34,2 %)`
- `Assets/TunnelCrew/Probe/House/HouseFurnishing.cs:1 (53,3 %)`

**Во что обходится:** Замер по всей области: 3 483 строки комментариев на 10 632 строки кода (25 %). Худшие места конкретны: Householder.cs:39–70 — 32 строки прозы перед ДВУМЯ операторами; HouseWalk.cs:474–508 — 34 строки перед подписью метода. Это не «плохие комментарии» — они несут настоящие причины и один раз спасли (см. находку №6). Но там, где преамбула в пятнадцать раз длиннее кода, вы больше не видите тик целиком на экране, и это часть той же цены, что в находке №1. Правка не «сократить комментарии», а: перенести длинные обоснования в XML-док метода или в отдельный файл рядом, оставив в теле короткую ссылку. Отдельно: HouseholderEventMemory.cs — обратный перекос, 2,6 % при среднем 25 %, и это как раз самый запутанный из читанных файлов.

### 9. [SPLIT · день] Тик хозяина размазан по четырём методам-простыням, а его состояние — по 12 позиционным аргументам, которые пересобираются в четырёх местах вручную

**Где:**
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:202 (StepThroughTheDay, 371 строка)`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:584 (StepRoutine, 279 строк, 21 параметр)`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:928 (StepActiveResponse, 218 строк, 17 параметров)`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:1214 (StepTrackedVisibleResponse, 179 строк, 17 параметров)`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:877 (StandStill, 50 строк, 12 параметров)`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:837`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:904`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:1116`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:1363`
- `Assets/TunnelCrew/Probe/Householder/HouseholderLocalMemory.cs:98`

**Во что обходится:** Файл 1518 строк, из них 1310 — семь методов. Пять методов раскладывают HouseholderLocalMemory (15 членов) в локальные переменные на строках 307–317, тащат их как параметры через четыре подписи, и собирают обратно `new HouseholderLocalMemory(...)` двенадцатью ПОЗИЦИОННЫМИ аргументами в четырёх местах: 837, 904, 1116, 1363. Три из двенадцати — int (currentRoutePointIndex, routeDirection, pathIndex), ещё float и double. Перепутанная пара соседних int-ов компилируется молча и во всех четырёх местах даёт разное поведение. Это тот самый класс дефекта, который вы описали примером №1: он определяется НЕ там, где его ищут. Комментарий на строке 877–890 уже признаёт проблему («Twelve parameters and only TWO of them actually differ… They used to be three near-identical blocks differing only in local variable names, which is how the third one went unnoticed for so long») — то есть один такой промах уже был и его починили руками, а механизм оставили. Плюс каждая правка поведения хозяина требует прочитать метод на 371 строку целиком.

### 10. [SPLIT · день] HouseholderStepInput: 13 конструкторов от 5 до 20 параметров, из них в игре используется РОВНО ОДИН

**Где:**
- `Assets/TunnelCrew/Probe/Householder/HouseholderStepInput.cs:5`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStepInput.cs:25`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStepInput.cs:43`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStepInput.cs:64`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStepInput.cs:91`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStepInput.cs:113`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStepInput.cs:138`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStepInput.cs:164`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStepInput.cs:194`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStepInput.cs:231`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStepInput.cs:263`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStepInput.cs:299`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStepInput.cs:338 (приватный, 20 параметров)`
- `Assets/TunnelCrew/Probe/Householder/AuthoritativeHouseholder.cs:651 (единственный продуктовый вызов)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderRoutineEntry.cs:52`

**Во что обходится:** Замер: `new HouseholderStepInput(` встречается 1 раз во всём Assets (AuthoritativeHouseholder.cs:651, конструктор со строки 299) и 48 раз в tests/TunnelCrew.Core.Tests. То есть публичная форма входа рулей описывает не игру, а 48 тестовых площадок. Хуже: семь из двадцати параметров (CurrentFeeling, RoutineAbility, RoutineReaction, RoutinePlace, RoutineOccupationPhase, RoutineOccupationPhaseIndex, RoutineOccupationName) достижимы ТОЛЬКО через ветку `input.Profile == null` в HouseholderRoutineEntry.For:52 — а продуктовый путь всегда передаёт профиль. Комментарий на HouseholderRoutineEntry.cs:11 это прямо признаёт: «which is what every test that drives Householder.Step by hand does». Итог: существуют два параллельных способа сказать, какая запись дня сейчас идёт, и второй нужен только тестам. Цена: каждое новое поле входа = ещё один overload, старые overload-ы молча подставляют дефолт, и 48 тестов пришпилены к форме, которой в игре нет. Это и есть механизм, из-за которого «тесты не тестируют то, что надо».

### 11. [MOVE · день] Семь боевых реакций хозяина зашиты C#-литералами вместо данных — при том, что формат данных уже есть

**Где:**
- `Assets/TunnelCrew/Probe/Householder/HouseholderReaction.cs:551 (CreateCurrent, 131 строка)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderReaction.cs:693 (NobodyInSight)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderReaction.cs:801 (SeenRat)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderReaction.cs:138 (HouseholderReactionDefinition)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderVocabulary.cs:1`

**Во что обходится:** CreateCurrent — 131 строка object-initializer-ов, по 13 полей на строку каталога, плюс ещё ~70 строк в NobodyInSight и SeenRat. Рядом уже лежит HouseholderReactionDefinition (HouseholderReaction.cs:138) — это ровно запись данных, и профиль умеет добавлять реакции из JSON (AuthoritativeHouseholder.cs:568, WithProfileReactions). То есть механизм чтения реакций из файла построен, а семь шиповых строк остались в коде. Цена конкретная и вы её уже измерили: подкрутить шиповую реакцию = правка C# = пересборка = домен-релоад Unity, то есть это падает в те самые 316 секунд, а не в 1 секунду headless. Вторая половина той же цены — HouseholderVocabulary.cs: чтобы добавить один новый шум, надо дописать члены в 4–6 enum-ов (EventName, NoticedFactName, CauseName, Occupation, PhysicalActionName, ActionTargetName) в третьем файле. Новая реакция — это правка кода в трёх местах, хотя объявлена как «данные».

### 12. [SPLIT · день] Телескопические конструкторы по всей области: 10 у предложения решения, 7 у профиля, 6 у снимка, 5 у окружения

**Где:**
- `Assets/TunnelCrew/Probe/Householder/HouseholderDecision.cs:309 (HouseholderDecisionProposal, 10 конструкторов до строки 519)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderRoutineProfile.cs:369 (7 конструкторов)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderDecision.cs:8 (HouseholderDecisionSnapshot, 6)`
- `Assets/TunnelCrew/Probe/Householder/AuthoritativeHouseholder.cs:11 (HouseholderSurroundings, 5)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderLocalMemory.cs:8 (5)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStanding.cs:14 (4)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderEventMemory.cs:9 (4)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderRoutineProfile.cs:217 (4)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderAccumulatedFactDecisionHandler.cs:18 (4)`

**Во что обходится:** Девять типов в области держат от четырёх до десяти цепочечных конструкторов. Это одна и та же болезнь, что в находке №2, только рассеянная. Каждое новое поле на любом из этих типов = ещё один overload наверху цепочки, а все нижние продолжают подставлять дефолт молча. Комментарий на HouseholderDecision.cs:640 уже описывает, как это один раз выстрелило: «every field added to a proposal afterwards was silently dropped here until somebody remembered to add a line — his day's entry would have been the second one to go». Починка одна на все девять: один приватный конструктор со всеми полями плюс копирующий, наружу — только With*-методы.

### 13. [REWRITE · день] HouseholderCondition и HouseholderEffect — структуры-объединения на 12 и 6 полей, где смысл имеют 2–4 в зависимости от Kind

**Где:**
- `Assets/TunnelCrew/Probe/Householder/HouseholderStanding.cs:324 (HouseholderCondition, приватный конструктор на 12 параметров)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStanding.cs:546 (Holds — switch на 48 строк, 11 веток)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStanding.cs:291 (HouseholderConditionKind, 11 членов)`
- `Assets/TunnelCrew/Probe/Householder/HouseholderStanding.cs:755 (HouseholderEffect)`

**Во что обходится:** Добавить один вид условия — это правка в четырёх местах одного файла: член enum-а (:291), параметр или дефолт в приватном конструкторе (:326), новая статическая фабрика с собственной валидацией (по образцу :446, :480, :490), и новая ветка switch-а в Holds (:546). Ничто не связывает эти четыре правки: пропущенная ветка switch-а падает в `default: return true` на строке 592 — то есть новое условие молча ВСЕГДА выполняется. Это дефект, который компилируется, проходит тесты соседних условий и включает авторскую строку, которую никто не просил включать.

### 14. [REWRITE · день] Каждый тик слежки за крысой строит с нуля граф видимости дома и выбрасывает его

**Где:**
- `Assets/TunnelCrew/Probe/House/HouseWalk.cs:497`
- `Assets/TunnelCrew/Probe/House/HouseWalk.cs:580`
- `Assets/TunnelCrew/Probe/House/HouseWalk.cs:266`
- `Assets/TunnelCrew/Probe/House/HouseWays.cs:278`
- `Assets/TunnelCrew/Probe/House/HouseWalk.cs:309`
- `Assets/TunnelCrew/Probe/Householder/Householder.cs:1252`

**Во что обходится:** Householder.cs:1252 зовёт HouseWalk.Toward каждый тик, пока крыса видна. Toward строит `new HouseWays` на строке 497, RetargetedWithin — ещё один на 580, а промах отправляет в To, который строит третий на 266 и рядом шесть массивов размера |places| (строки 309–315) плюс два List-а. HouseWays на каждую затронутую комнату лениво считает матрицу видимости `new double[count*count]` (HouseWays.cs:278) по углам выращенной мебели. Комментарий HouseWays.cs:30 объявляет это сознательным решением («Nothing here is stored between walks»), и мотив разумный — не заводить второй источник правды о мебели. Но мебель и тело за тик не меняются. Честно: сегодня это НЕ измеренная проблема — в first-house.house.json 7 комнат и 8 дверных проёмов, граф крошечный. Это станет проблемой при доме побольше или нескольких хозяевах, и чинится кэшем, привязанным к (дом, тело, высота ног), без второго источника правды.

**Что в этой области сделано хорошо и трогать не надо:**
- Слой полностью engine-free и без условной компиляции. Проверял: во всех 40 файлах области ноль вхождений `#if`, `UNITY_EDITOR`, `UnityEngine`, `Debug.Log`. Дефект из вашего примера №1 (сборка плеера не компилируется, потому что редакторный член читают снаружи #if) здесь НЕВОЗМОЖЕН по устройству. Это редкая и дорогая вещь — не трогать.
- Настройки — данные, а не числа в коде. Поиск магических констант по всей области дал ровно два результата: HousePlan.cs:42 `SameNumberTolerance = 0.0005f` (именованная, с обоснованием) и `* 0.5f` в HouseFurnishing.cs:162/164/261/262 (геометрические половины). Скорости, длительности, времена жизни фактов, паузы — всё приходит через HouseholderWalkTuning и профиль. Тюнинг поведения не требует пересборки; это ровно то, чего не хватает каталогу реакций (находка №4).
- Почти всё неизменяемое: readonly struct + With*-методы, ноль изменяемых статических полей во всей области. Тик не может испортить состояние на полпути — отказ на строке 70 Householder.cs оставляет хозяина ровно таким, каким он был. Это то, что делает возможными быстрые headless-тесты, и это надо сохранить при любом рефакторинге.
- Отказ хождения — настоящий отказ, а не тихая заглушка. Householder.cs:1441 отличает «путь не нарисовался, потому что кровать на дороге» от «идти некуда»: первое НЕ считается прибытием. HouseWalk.cs:378 отказывается рисовать прямую линию сквозь мебель, вместо того чтобы соврать. Это ровно противоположность вашему примеру №2 — механика отвечает правду вместо удобной строки.
- Механизм арбитража решений реальный, а не логовый. HouseholderDecisionPipeline.cs:252 и HouseholderDecision.cs:709 строят ростер кандидатов с причиной отказа для КАЖДОЙ строки, включая тики, где никто не победил (HouseholderDecision.cs:657 объясняет, почему именно так). Поверхность `why` держится на структуре данных, а не на разборе текста. Испорчена только сортировка отказов (находка №3) — сам механизм менять не надо.
- HouseholderDecisionPipeline.cs:224 — при регистрации обработчиков проверяются пустое имя и дубликат имени, с внятной ошибкой. AuthoritativeHouseholder.cs:585 проверяет ВСЕ слова про скорость один раз до первого шага, а не в момент, когда реакция впервые сработает. Обе проверки стоят там, где должны, и обе окупаются.


---

## ОБЛАСТЬ 2: МЫШЬ, ГРУЗ, НИТЬ — Assets/TunnelCrew/Probe/{Cargo,Multiplayer,Solids,Movement,Bench} (репозиторий C:\projects\Unity\GasCoopGame_win-u2 @332488de, только чтение)

Находок: **15**

**Лучшая правка области:** Цикл вместо индекса 0 в CarryWorld.cs:249-250 — `Deliveries.Observe(...)` по всем грузам, а не только по первому. Правка на несколько минут, ноль риска для физики, и она чинит основную петлю игры: сейчас из восьми типов лута в каталоге донести до точки выдачи можно ровно один — тот, что заспавнился первым. Ни один тест этого не ловит (DeliveryObjectiveTests.cs — 64 строки, единственный мировой тест с одним грузом), а на плейтесте это выглядит как «я донёс, и ничего не случилось». Вторая по отношению польза/цена — переписать CargoNoiseMeasurementTests.cs так, чтобы он читал GameRulesSettings.asset, а не свои константы: пороги слуха хозяина сейчас выставлены по замеру в мире с гравитацией 3 вместо 9.81 и жёсткостью руки 2000 вместо 6540.

### 1. [REWRITE · минуты] Цель «вынести лут» проверяется только у ПЕРВОГО груза — остальные 7 типов лута донести невозможно

**Где:**
- `Assets/TunnelCrew/Probe/Multiplayer/CarryWorld.cs:249`
- `Assets/TunnelCrew/Probe/Multiplayer/CarryWorld.cs:250`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:1529`
- `Assets/TunnelCrew/Settings/GameRulesSettings.asset:35`
- `tests/TunnelCrew.Core.Tests/DeliveryObjectiveTests.cs:31`

**Во что обходится:** `if (Deliveries.Count > 0 && Cargo.Count > 0) Deliveries.Observe(Cargo.GetState(0));` — наблюдается ровно индекс 0. Курьер при этом спавнит цикл `for (cargoId = 0; cargoId < _startConditions.CargoSpawnCount; cargoId++)`, а каталог в GameRulesSettings.asset содержит 8 строк лута (Alarm Clock, Bedside Radio, Kitchen Timer, Hall Key Box, Remote Control, Tool Box, Food Crate, Record Case). Значит основная петля игры — донести добычу до выхода — засчитывается ТОЛЬКО для куска, заспавненного первым. Мышь может протащить будильник через весь дом, положить его в точку выдачи, и ничего не произойдёт. Тестов на несколько грузов нет: DeliveryObjectiveTests.cs — 64 строки, мировой тест ровно один и с одним грузом. Дефект не виден ни одному тесту и виден каждому игроку.

### 2. [DELETE · минуты] Две ручки в ассете настроек, которые владелец может крутить, а игра их не читает

**Где:**
- `Assets/TunnelCrew/Probe/Cargo/CargoRules.cs:345`
- `Assets/TunnelCrew/Probe/Cargo/CargoRules.cs:472`
- `Assets/TunnelCrew/Probe/Cargo/CargoHaul.cs:400`
- `Assets/TunnelCrew/Settings/GameRulesSettings.cs:623`
- `Assets/TunnelCrew/Settings/GameRulesSettings.asset:326`

**Во что обходится:** `CargoRules.CargoRestHeight` записывается из ассета (GameRulesSettings.cs:623 подаёт FirstAuthoredDefinition.HalfHeight) и не читается НИГДЕ — ни в одном файле продукта, ни в одном тесте. `CargoRules.HandForceReachFalloff` (в ассете _cargoHandForceReachFalloff: 1) читается ровно в одном месте, CargoHaul.cs:400 внутри EffectiveHandLimit, а тот вызывается только из двух мёртвых веток (см. находку про три поколения). Владелец может провести вечер, крутя силу затухания руки, и не увидеть ни одного изменения в игре — это худший сорт потери времени, потому что он не выглядит как поломка.

### 3. [SETTING · минуты] Магические 0.12 / 0.88 в поиске точки прогиба нити — единственные числа в файле без имени

**Где:**
- `Assets/TunnelCrew/Probe/Solids/ThreadSight.cs:320`
- `Assets/TunnelCrew/Probe/Solids/ThreadSight.cs:323`

**Во что обходится:** PivotOn зажимает точку прогиба в [0.12, 0.88] голыми литералами, тогда как остальные числа этого файла оформлены именованными константами (Grazing, BowSteps). Практический смысл: препятствие ближе 12% длины нити от лапы или от якоря не может быть обойдено вообще — нить рвётся, хотя обойти его видимо можно. Это дверной косяк прямо у лапы, самый частый случай в доме. Число не в настройках, не в имени, и не покрыто ни одним тестом.

### 4. [DELETE · минуты] UnboundedCarryStrength мёртв в продукте по признанию собственного файла

**Где:**
- `Assets/TunnelCrew/Probe/Cargo/UnboundedCarryStrength.cs:1`

**Во что обходится:** Файл сам пишет «Nothing registers it in the running game», и проверка это подтверждает: ссылок в продукте нет ни одной, кроме собственного определения; один тест. Держится как доказательство расширяемости шва. Это защитимое решение, но за него платят чтением: третья реализация ICarryStrengthRule рядом с FlatCarryStrength и LeverCarryStrength, и при разборе «какой закон едет» её приходится исключать вручную. Либо перенести в тестовую сборку, либо удалить.

### 5. [SPLIT · часы] Одна ручка _cargoGripLength означает три разные физические величины и читается двумя разными способами

**Где:**
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:1976`
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:1832`
- `Assets/TunnelCrew/Probe/Multiplayer/CarryWorld.cs:347`
- `Assets/TunnelCrew/Settings/GameRulesSettings.cs:292`
- `Assets/TunnelCrew/Settings/GameRulesSettings.cs:607`

**Во что обходится:** Одно число (_cargoGripLength = 3.2) служит: длиной связи хвата до срыва (CargoHold.MaxLength), дальностью, на которую мышь может привязать нить (`threads.TryTieToAim(playerId, walkers, rules.GripLength)`), и ThreadLaunchTuning.Reach — предельной длиной уже натянутой нити. Подкрутил, чтобы груз не срывался при ходьбе назад — молча изменил, куда мышь вообще может кинуть нить. Вдобавок оно читается двумя способами: GameRulesSettings.cs:292 отдаёт рисовалке `Mathf.Max(0f, _cargoGripLength)`, а CreateCargoRules() на строке 607 подаёт судье СЫРОЕ поле. Отрицательное авторское значение даёт картинку с нулём и правило с минусом. Ни одного валидатора инварианта, который сам CargoRules.cs описывает прозой («GripLength has to clear CarryOffset + HandReach + spring stretch»), в коде нет.

### 6. [REWRITE · часы] ResolveWalk множит полный проход по дому на 4, а March может звать его до 32 раз за тик

**Где:**
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:16`
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:17`
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:612`
- `Assets/TunnelCrew/Probe/Multiplayer/AuthoritativeWalkerRoster.cs:448`
- `Assets/TunnelCrew/Network/WalkSpaceProbe.cs:14`

**Во что обходится:** Три жёстко вшитых множителя перемножаются и ни один не в настройках: CompositionPasses=4, ObstaclePasses=4, MostSlices=32, плюс Passes=4 внутри дома. Композиционный цикл ResolveWalk оборачивает ЦЕЛЫЙ ответ дома, а не только выталкивание из груза. Считая по настройкам (StepLimit = WalkerRadius = 0.036 м, _threadLaunchSpeed = 6 м/с, тик 1/30): брошенная нитью мышь пролетает 0.2 м за тик = 6 срезов. 6 срезов × 4 композиции × 4 прохода дома × N стен. При ~100 SolidBox дома это ~9600 проверок коробок на одну летящую мышь за тик против ~1600 на идущую — шестикратная разница, и никто её не мерил. Четыре мыши, одновременно летящие на нитях, — худший случай демо, и это ровно то, что владелец собирается показывать.

### 7. [MOVE · часы] 15 частных копий IsFinite и четыре взаимно несовместимых Positive: бесконечный момент отключает весь закон переноски

**Где:**
- `Assets/TunnelCrew/Probe/Cargo/CargoHold.cs:565`
- `Assets/TunnelCrew/Probe/Cargo/LeverCarryStrength.cs:129`
- `Assets/TunnelCrew/Probe/Cargo/LeverCarryStrength.cs:96`
- `Assets/TunnelCrew/Probe/Solids/ThreadLaunch.cs:39`
- `Assets/TunnelCrew/Probe/Multiplayer/AuthoritativeWalkerRoster.cs:134`
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:812`
- `Assets/TunnelCrew/Probe/Cargo/CargoGeometry.cs:390`

**Во что обходится:** «Обеззаразить авторское положительное число» написано четыре раза с тремя разными ответами на бесконечность: CargoPowerMath.Positive отдаёт float.MaxValue, LeverCarryStrength.Positive отдаёт 0, ThreadLaunch.Positive отдаёт 0, WalkerBodyTuning.Positive отдаёт 0. Практическое следствие: если в _cargoCarryMoment/_cargoLiftMoment попадёт бесконечность, LeverCarryStrength.Positive обнулит оба, и строка 96 `_enabled = _pivot > 0f && (_carryMoment > 0f || _liftMoment > 0f)` выключит правило целиком — то есть «бесконечно сильная рука» превращается в игру, где НИЧЕГО нельзя поднять. Рядом 15 копий IsFinite и 2 копии Clamp в одной области (22 IsFinite по всему TunnelCrew).

### 8. [SPLIT · часы] 6 отдельных заходов в Play Mode на 6 тестов в одном файле — основной вклад в 316 секунд

**Где:**
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoNoiseMeasurementTests.cs:75`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoNoiseMeasurementTests.cs:185`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoNoiseMeasurementTests.cs:244`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoNoiseMeasurementTests.cs:297`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoNoiseMeasurementTests.cs:395`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoNoiseMeasurementTests.cs:460`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoPhysicsMeasurementTests.cs:110`
- `Assets/Tests/TunnelCrew/WalkSpace/WalkSpaceClearanceEditModeTests.cs:1`

**Во что обходится:** 25 пар `new EnterPlayMode()` / `new ExitPlayMode()` по всему Assets/Tests, из них 18 в этой области: CargoNoiseMeasurementTests 6, HouseholderSightEditModeTests 5, WalkSpaceClearanceEditModeTests 4, CargoPhysicsMeasurementTests 2, CargoSleepEditModeTests 1. Каждая пара — полный цикл перезагрузки домена, что и есть измеренные 37 ForceDomainReload за прогон. В CargoNoiseMeasurementTests сцена вообще не открывается (нет OpenScene) — все шесть тестов строят объекты кодом и заходят в Play Mode только чтобы получить живой PhysicsScene. Шесть перезагрузок домена ради шести проверок. CargoPhysicsMeasurementTests — 1844 строки ради пяти тестов.

### 9. [REWRITE · часы] CargoRules: четыре позиционных конструктора с 25 необязательными float-параметрами подряд

**Где:**
- `Assets/TunnelCrew/Probe/Cargo/CargoRules.cs:63`
- `Assets/TunnelCrew/Probe/Cargo/CargoRules.cs:124`
- `Assets/TunnelCrew/Probe/Cargo/CargoRules.cs:190`
- `Assets/TunnelCrew/Probe/Cargo/CargoRules.cs:245`
- `Assets/TunnelCrew/Probe/Cargo/CargoRules.cs:274`

**Во что обходится:** Подряд идут двадцать с лишним float с умолчанием 0f: pickupEyeHeight, cargoRestHeight, cargoCarryHeight, halfHeight, walkerRadius, cargoMass, bodyLinearDamping, verticalDampingRatio, handForceReachFalloff… Сдвиг на одну позицию даёт молча неверную физическую константу и компилируется. Комментарий ThreadRules.cs:12 прямо признаёт, что этот приём уже стоил дефекта: «a row of loose floats is the shape that once sent one lifetime into another's slot and survived review» — но в CargoRules он остался. Плюс ни одно поле CargoRules не обеззараживается при построении (в отличие от ThreadRules, WalkerBodyTuning и WalkerVerticalTuning, которые все зажимают в конструкторе).

### 10. [DELETE · часы] ThreadEndCause объявлен и не производится ни разу; нить рвётся в трёх местах молча

**Где:**
- `Assets/TunnelCrew/Probe/Solids/AuthoritativeThreadRoster.cs:7`
- `Assets/TunnelCrew/Probe/Solids/AuthoritativeThreadRoster.cs:366`
- `Assets/TunnelCrew/Probe/Solids/AuthoritativeThreadRoster.cs:383`
- `Assets/TunnelCrew/Probe/Solids/AuthoritativeThreadRoster.cs:407`

**Во что обходится:** Перечисление ThreadEndCause (Unknown/LetGo/Stretched/Jammed/HolderGone) не упоминается больше НИГДЕ во всём дереве — ни в продукте, ни в тестах. При этом Advance() рвёт нить тремя разными `_ties.RemoveAt(index)` без единого сигнала наружу: хозяин ушёл, стало длиннее Reach, не видно дальше TrembleSeconds. У груза ровно та же ситуация решена правильно — есть CargoHoldEnding и он доезжает до клиента. У нити игрок видит только исчезнувшую линию и не может выучить, за что её потерял. Либо доделать до пары CargoHoldEnding, либо удалить перечисление, чтобы оно не читалось как существующая фича.

### 11. [REWRITE · день] Замер шума груза снимался в мире, который в 3,27 раза легче и мягче настоящего, и рукой переписанным законом хвата

**Где:**
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoNoiseMeasurementTests.cs:44`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoNoiseMeasurementTests.cs:50`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoNoiseMeasurementTests.cs:51`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoNoiseMeasurementTests.cs:661`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoNoiseMeasurementTests.cs:692`
- `Assets/TunnelCrew/Settings/GameRulesSettings.asset:31`
- `Assets/TunnelCrew/Settings/GameRulesSettings.asset:304`
- `Assets/TunnelCrew/Settings/GameRulesSettings.asset:324`

**Во что обходится:** Шапка файла заявляет: «runs … on the real cargo numbers out of the settings asset». Это неправда — числа переписаны в const и с тех пор разошлись с ассетом: CargoGravity 3f против _cargoGravity 9.81; HandStiffness 2000f против _cargoHandStiffness 6540; HandCarryPower 200f против _cargoCarryPower 654. Ровно множитель 3,27 по всем трём. Строка 692 давит `AddForce(Vector3.down * CargoGravity, Acceleration)` — то есть настоящий PhysX считает удары о стену в мире с гравитацией 3. Строка 661 — `Vector3.ClampMagnitude(stretch * HandStiffness, HandCarryPower)` — это ВТОРАЯ, рукописная копия закона хвата вместо вызова CargoHaul.Reduce, и она втрое слабее шипнутой. Именно по этим показаниям выставлены пороги слышимости хозяина (_cargoRustleForce 3 / _cargoKnockForce 15 / _cargoHeavyNoiseForce 35). Весь слух хозяина откалиброван по замеру не той сцены — это буквально пример №2 из задания, но про звук.

### 12. [DELETE · день] Закон силы хвата написан в трёх поколениях в одном методе; два мертвы в игре, но именно их гоняет большинство тестов

**Где:**
- `Assets/TunnelCrew/Probe/Cargo/CargoHaul.cs:350`
- `Assets/TunnelCrew/Probe/Cargo/CargoHaul.cs:379`
- `Assets/TunnelCrew/Probe/Cargo/CargoHaul.cs:388`
- `Assets/TunnelCrew/Probe/Cargo/CargoHaul.cs:391`
- `Assets/TunnelCrew/Probe/Cargo/CargoHaul.cs:606`
- `Assets/TunnelCrew/Probe/Cargo/CargoHaul.cs:793`
- `Assets/TunnelCrew/Probe/Cargo/CargoHold.cs:10`
- `Assets/TunnelCrew/Probe/Cargo/CargoHold.cs:143`
- `Assets/TunnelCrew/Probe/Multiplayer/AuthoritativeWalkerRoster.cs:600`

**Во что обходится:** CargoHold имеет 8 публичных конструкторов, задающих три несовместимых физических режима через два скрытых флага (UsesSeparateStrengths, UsesActualGripReach). Продакшен строит хват ровно в двух местах (AuthoritativeCargoRoster.cs:1977 и :1997), оба с UsesSeparateStrengths=true, и живой путь идёт только через ActualGripBudget/LeverCarryStrength. Значит связанный 3D-бюджет (`Cap(ref handX, ref handY, ref handZ, limit)`, EffectiveVerticalStiffness) и закон затухания EffectiveHandLimit в игре НЕДОСТИЖИМЫ — их держат живыми только тесты. Хуже: сентинел, который разводит режимы, — это `float.NaN` в `independentLiftLimit`, и разветвление написано ДВАЖДЫ (HandForce:350-390 и CompleteBudget:793-813, чей собственный комментарий признаёт «selected by the same hold-kind branches as HandForce»). Их надо руками держать в согласии. Цена: читая CargoHaul, невозможно понять, какая арифметика едет в билд; половина «доказательств физики» доказывает мёртвую ветку. `AuthoritativeWalkerRoster.SetCargoHandling` (вход в мёртвый режим) не вызывается из продукта ни разу — только из 4 тестов.

### 13. [DELETE · день] Тесты судьи гоняют 6-аргументную CarryWorld.Advance, которая молча обнуляет гравитацию, массу мыши, ограничитель шага, отбрасывание и рост мыши

**Где:**
- `Assets/TunnelCrew/Probe/Multiplayer/CarryWorld.cs:142`
- `Assets/TunnelCrew/Probe/Multiplayer/CarryWorld.cs:161`
- `Assets/TunnelCrew/Probe/Multiplayer/CarryWorld.cs:181`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoPhysicsMeasurementTests.cs:1420`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoPhysicsMeasurementTests.cs:1427`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:1864`

**Во что обходится:** Продукт зовёт полную 12-аргументную перегрузку с CreateWalkerVerticalTuning(), CreateWalkerBodyTuning(), CreateCargoKnockbackTuning() и WalkerHeight. Тесты — 110 из ~158 вызовов world.Advance в headless-наборе плюс весь CargoPhysicsMeasurementTests — зовут короткую. Последствия по коду: WalkerVerticalTuning default ⇒ гравитация 0 и прыжок 0; WalkerBodyTuning default ⇒ Mass=0 (импульс нити не двигает мышь вообще), StepLimit=0 (March никогда не режет шаг, туннелирование не воспроизводится), трение 0; walkerHeight=0 ⇒ груз перекрывает проход на ЛЮБОЙ высоте, то есть ровно тот дефект, который AuthoritativeCargoRoster.cs:626-641 объявляет исправленным. Плюс пол в CargoPhysicsMeasurementTests — класс FlatFloor (строка 1427), синтетическая плоскость вместо дома. Итог: «физика доказана» доказана в мире, где у мыши нет массы, нет гравитации, она не может провалиться сквозь стену, а ящик — стена до неба. Только 9 тестов во всём дереве вообще строят WalkerBodyTuning, и лишь 1 упоминает walkerHeight.

### 14. [MOVE · день] Закон «круг против коробки» написан дважды и две копии расходятся на границе и на площадке приземления

**Где:**
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:729`
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:626`
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:805`
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:812`
- `Assets/TunnelCrew/Network/WalkSpaceProbe.cs:151`
- `Assets/TunnelCrew/Network/WalkSpaceProbe.cs:156`
- `Assets/TunnelCrew/Network/WalkSpaceProbe.cs:79`

**Во что обходится:** Один и тот же физический закон (вытолкнуть круг радиуса r из повёрнутой коробки, решить, стоит ли мышь на её крышке, пропустить ли то, что над головой) реализован в двух файлах, и копии НЕ совпадают. (а) Порог: cargo-копия `if (radius > 0f && distanceSquared >= radiusSquared) return false;` — касание ровно на радиусе НЕ толкает; wall-копия `if (distanceSquared > radius * radius) return false;` — толкает. (б) radius<=0: cargo-копия имеет отдельную ветку, wall-копия при radius=0 и точке ровно на грани падает в ветку «внутри стены» и телепортирует. (в) Площадка приземления: WalkSpaceProbe.cs:79-83 ужимает крышку на радиус мыши (`wall.HalfX - radius`), cargo-копия принципиально нет (комментарий на :626-634). То есть чтобы встать на тумбочку, нужно поместиться на неё целиком, а чтобы встать на ящик — достаточно попасть центром. Игрок учит одно правило дважды. Плюс дословно продублированы ResolveFloor и Clamp в обоих файлах.

### 15. [SPLIT · день] AuthoritativeCargoRoster.cs — 2370 строк, семь несвязанных обязанностей в одном классе

**Где:**
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:588`
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:872`
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:1049`
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:1243`
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:1621`
- `Assets/TunnelCrew/Probe/Cargo/AuthoritativeCargoRoster.cs:1862`

**Во что обходится:** В одном файле лежат: столкновение ходока с грузом как с препятствием (588-833), чтение поз у движка и возврат выпавшего куска (872-1048), «положить на поверхность» (1049-1180), жизненный цикл хвата и реестр отказов (1243-1578), отложенные импульсы (1579-1620), магнит (1621-1796), луч подбора (1862-2034), колесо дальности (2123-2300). Швы чистые и уже видны по методам — это не «плохая архитектура», а конкретный список из шести кусков, которые режутся без изменения поведения. Цена: три из находок выше (мёртвые ветки закона силы, дубль выталкивания, множитель проходов) прятались именно здесь, потому что файл невозможно прочитать целиком.

**Что в этой области сделано хорошо и трогать не надо:**
- Вся область ДЕЙСТВИТЕЛЬНО engine-free — grep по TODO/HACK/FIXME/catch/#if UNITY_EDITOR/UnityEngine во всех пяти папках (Cargo, Multiplayer, Solids, Movement, Bench) не даёт ни одного попадания. Дефект из примера №1 задания (редакторные члены, читаемые вне #if) здесь отсутствует полностью, и билд плеера эта область не ломает. Это трогать не надо.
- LootHeft.ReachThatHolds (LootHeft.cs:135-171) — образец того, как надо. Он НЕ обращает закон силы, а шагает наружу мелким шагом и спрашивает ICarryStrengthRule напрямую; его собственный комментарий объясняет, что предыдущая версия переписала формулу затухания второй раз и совпадала с игрой случайно. Этот приём — «спроси правило, не переписывай его» — надо взять шаблоном для остальных находок.
- ThreadArc и ThreadLaunch делят один порядок интегрирования и один SolidRay.TryCast (ThreadArc.cs:70-76 и 120-129) — нарисованная траектория и настоящий полёт физически не могут разойтись. Единственное место в области, где «показать» и «сделать» гарантированно одна арифметика.
- CentreAbove (AuthoritativeCargoRoster.cs:978-984) отказывается писать Height*0.5f и делегирует CargoBoxProjection.CenterYOnFloor, явно перечислив три других места, которые задают тот же вопрос. Правильная борьба с четвёртой копией.
- EndHold (AuthoritativeCargoRoster.cs:1182-1192) всегда парно зовёт ForgetFailure, и это единственный путь снятия хвата — реестр отказов _holdFailures не течёт и не переживает перехват предмета. Проверено по всем четырём путям завершения (LetGo, PieceLost, HolderGone, Stretched/Jammed/Overloaded).
- SettleAt (AuthoritativeCargoRoster.cs:999-1046) — настоящая единственная дверь для «положить предмет куда-то»: обе половины (состояние ростера и тело движка) делаются вместе, и комментарий разбирает обе зеркальные ошибки. Все вызывающие идут через неё.
- ThreadRules, WalkerBodyTuning и WalkerVerticalTuning зажимают каждое поле прямо в конструкторе. Это ровно та дисциплина, которой не хватает CargoRules — менять их не надо, надо распространить.


---

## СЕТЬ — Assets/TunnelCrew/Network/** (41 файл, 15 042 строки)

Находок: **15**

**Лучшая правка области:** Удалить строку 839 в Assets/TunnelCrew/Network/NetworkWalkerCourier.cs (`_labBalanceAnnounced = 0;` внутри AnnounceNewLabShoves). Одна строка, минуты работы. Она обнуляет водомерку ЧУЖОГО метода, который вызывается в том же тике (1903 и 1918), из-за чего вся история равновесия переотправляется по надёжному каналу каждый тик и без дедупликации накапливается на клиенте (916). Цена бездействия: прибор, по которому судили механику падения, показывает десять копий одного момента вместо десяти разных — то есть замер, на который опирались, недостоверен. Самая большая ЦЕНА при этом не здесь, а у находки №1 (сборка плеера не компилируется, 18 строк), но она стоит часов, а эта — минуты.

### 1. [DELETE · минуты] Одна лишняя строка обнуляет счётчик соседа: вся история равновесия переотправляется каждый тик и дублируется на экране

**Где:**
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:839`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:916`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:1903`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:1918`

**Во что обходится:** Прибор, по которому судили механику падения, врёт. AnnounceNewLabShoves() на 839 делает `_labBalanceAnnounced = 0;` — обнуляет водомерку ЧУЖОГО метода. Оба вызываются в одном серверном тике (1903 и 1918), поэтому AnnounceNewLabBalanceMoments каждый тик переотправляет ВСЕ накопленные моменты заново. На клиенте LabBalanceObserversRpc просто добавляет в список без проверки (916), дедупликации нет — список растёт квадратично, а панель показывает последние 10 записей, то есть десять копий одного момента. Собственный комментарий метода на 897–899 утверждает обратное: «Sent only when something changed, never every tick». Плюс шторм надёжных RPC с тремя строками в каждом (why, impactSource, chore) 30 раз в секунду.

### 2. [SETTING · минуты] Отладочная IMGUI-панель стенда навешивается на КАЖДОГО клиента в ЛЮБОЙ сборке — при том что правильный механизм в этой же папке уже есть

**Где:**
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:1596`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:1597`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:53`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:73`
- `Assets/TunnelCrew/Network/ThreadDebugOverlay.cs:58`

**Во что обходится:** В отгруженной игре у каждого игрока висит объект «Integration lab readout» с OnGUI каждый кадр — инструмент разработчика в продукте, и он же тянет за собой дефект №1. В OnStartClient (1596–1597) Attach вызывается без единого условия. При этом ThreadDebugOverlay.cs:58 уже содержит ровно нужный компилируемый затвор `TuningGaugesMayDraw` (#if UNITY_EDITOR || DEVELOPMENT_BUILD) и его комментарий прямо описывает, как прибор однажды уже уехал в билд включённым. Новый стенд этот механизм не переиспользовал.

### 3. [SETTING · минуты] Галочка DrawSightGizmos удваивает лучи хоста и живёт в отгружаемом ассете настроек, а не в компилируемом затворе

**Где:**
- `Assets/TunnelCrew/Network/HouseholderSightSource.cs:614`
- `Assets/TunnelCrew/Network/HouseholderSightSource.cs:623`
- `Assets/TunnelCrew/Network/HouseholderSightSource.cs:639`

**Во что обходится:** Тот же класс дефекта, который ThreadDebugOverlay уже закрыл компилируемым затвором: значение решает СЕРИАЛИЗОВАННОЕ в ассете, и его можно забыть включённым. CompletePicture (614–644) при включённой галочке до-пускает ВСЕ пропущенные ранним выходом лучи — чисто ради картинки, на каждую вещь, каждый тик. Ранний выход из цикла выборки (HouseholderSightSource.cs:245–252) специально экономил эти лучи, и галочка эту экономию отменяет.

### 4. [MOVE · часы] Сборка плеера не компилируется: 18 строк читают редакторные члены вне #if. Разбор до конца

**Где:**
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:1918`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:78`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:79`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:110`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:115`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:129`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:151`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:181`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:190`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:199`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:205`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:217`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:261`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:262`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:282`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:295`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:338`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:344`

**Во что обходится:** Релиза не существует вообще: игру нельзя собрать. ПОЛНЫЙ СПИСОК (18 строк, 19 чтений — на 344 строке LocalTick читается дважды). ИСТОЧНИК: 15 членов NetworkWalkerCourier объявлены внутри #if UNITY_EDITOR (блок 626–1400): LabTitleHeard(767), LabExpectHeard(769), LabRefusalHeard(772), LocalTick(775), DrawnWalkerCount(779), TryReadDrawnWalker(781), TryReadWalkerSpeed(821), TryReadAuthoritativeWalker(797), LabShovesHeard(764), LabBalanceHeard(931), HasHouseholder(959), TryReadBalanceThresholds(941), TryReadHostBalance(966), TryReadHeardBalance(1008), ReadLabPieces(738). ДВА МЕСТА ЧТЕНИЯ: (а) IntegrationLabReadout.cs — файл целиком БЕЗ единого #if, лежит в рантайм-сборке TunnelCrew.Networking, 17 строк; (б) NetworkWalkerCourier.cs:1918 — вызов AnnounceNewLabBalanceMoments(), объявленного на 862 ВНУТРИ #if. Соседний AnnounceNewLabShoves() на 1903 УЖЕ обёрнут в #if (1895–1904) — то есть «класс пройден целиком» был объявлен, когда близнец через 15 строк остался голым. Ровно тот случай: дефект определяется ЧТЕНИЯМИ, а искали по ОБЪЯВЛЕНИЯМ.

### 5. [SETTING · часы] Полный снапшот мира едет по НАДЁЖНОМУ каналу 30 раз в секунду

**Где:**
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:2243`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:2036`

**Во что обходится:** У любого игрока с потерей пакетов мир замирает и потом прыгает, вместо того чтобы плавно пропустить один кадр состояния. [ObserversRpc(BufferLast = true, ExcludeServer = true)] на 2243 не указывает Channel — FishNet берёт Reliable по умолчанию. По этому каналу каждый тик едет ВСЁ: позиции всех ходоков, всех предметов, всех хватов, всех нитей, домохозяин и список доставок. Головная блокировка очереди на полном состоянии — потерянный пакет держит следующие. Плюс BufferLast=true заставляет держать копию последнего пакета на каждое подключение.

### 6. [DELETE · часы] Семь полей снапшота едут по проводу, но на клиенте их не читает никто

**Где:**
- `Assets/TunnelCrew/Network/CargoSnapshot.cs:25`
- `Assets/TunnelCrew/Network/CargoSnapshot.cs:27`
- `Assets/TunnelCrew/Network/CargoSnapshot.cs:28`
- `Assets/TunnelCrew/Network/CargoSnapshot.cs:31`
- `Assets/TunnelCrew/Network/WalkerSnapshot.cs:21`
- `Assets/TunnelCrew/Network/CargoHoldSnapshot.cs:99`
- `Assets/TunnelCrew/Network/CargoHoldSnapshot.cs:110`

**Во что обходится:** Трафик каждый тик навсегда и ложная карта того, что клиент якобы знает. Ни одного читателя во всём Assets/: CargoSnapshot.Integrity (float), ThingStateId (int), ThingRemainingSeconds (float), Moved (bool); WalkerSnapshot.Moved (bool); CargoHoldSnapshot.Load (float), Strain (float). Единственное, что их «читает» — мёртвый теневой измеритель (см. отдельную находку), и его же комментарий CargoSnapshotRegistry.cs:346 честно признаёт: «Moved … is a previous-tick hint with no client consumer». Load и Strain хуже прочих: ради них хост зовёт CargoHaul.TryDescribeHold на КАЖДЫЙ хват КАЖДЫЙ тик (NetworkWalkerCourier.cs:2081). Плюс CargoSnapshot.Yaw дублирует кватернион и используется только как запасной вариант при вырожденной длине (NetworkCargoPresentation.cs:264–270).

### 7. [DELETE · часы] 473 строки теневого измерителя дельт крутятся на хосте каждый тик, а читателя у них ноль

**Где:**
- `Assets/TunnelCrew/Network/CargoSnapshotRegistry.cs:376`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:2219`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:138`

**Во что обходится:** Целый файл и работа хоста на каждый тик за ноль пользы. CargoSnapshotDeltaShadow.ObserveFullSnapshot вызывается на 2219 каждый тик и прогоняет весь список предметов через словарь с проверкой семи грязных полей. Единственная дверь наружу — TryReadCargoSnapshotDeltaMetrics (NetworkWalkerCourier.cs:138), у неё НОЛЬ вызовов во всём репозитории, включая тесты (проверено grep по Assets/). Механизм измеряет, сколько бы сэкономила дельта-отправка, но саму дельта-отправку никто не сделал, а результат измерения никто не смотрит.

### 8. [REWRITE · часы] Список названий доставок пересобирается как string[] и едет по проводу каждый тик, хотя названия не меняются никогда

**Где:**
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:2208`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:2215`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:2237`

**Во что обходится:** Сериализация строк 30 раз в секунду за то, что задано в сцене и константно. deliveryNames = new string[...] + цикл на 2208–2215, дальше уезжает в ReceiveSnapshotsObserversRpc. Меняется только парный bool[] deliveryComplete. То же по мелочи в HouseholderSnapshot.ReachThingName — строка в каждом тиковом снапшоте (там она хотя бы меняется).

### 9. [REWRITE · часы] Семь новых массивов на каждый серверный тик в PublishSnapshots

**Где:**
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:2039`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:2058`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:2110`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:2155`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:2159`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:2208`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:2209`

**Во что обходится:** ~210 выделений в секунду на хосте, вечно: WalkerSnapshot[], CargoSnapshot[], List<CargoHoldSnapshot>+ToArray, List<ThreadAnchorSnapshot>+ToArray, CargoHoldEndingSnapshot[], string[], bool[]. Регулярные подборки мусора у ХОЗЯИНА комнаты, то есть заикания видят все четверо. Буферы переиспользуемы: размеры меняются редко.

### 10. [REWRITE · часы] Зрение домохозяина зовёт GetComponentInParent дважды на каждое попадание луча, до проверки, нужно ли это вообще

**Где:**
- `Assets/TunnelCrew/Network/HouseholderSightSource.cs:342`
- `Assets/TunnelCrew/Network/HouseholderSightSource.cs:358`
- `Assets/TunnelCrew/Network/HouseholderSightSource.cs:322`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:1855`

**Во что обходится:** Самый дорогой цикл серверного тика. SeeWhatIsLyingAbout (курьер:1855) идёт по всем вещам дома, на каждую пускает BodyPointCount лучей, буфер попаданий на 64 (строка 38), и на КАЖДОЕ попадание делает collider.GetComponentInParent<CargoBodyContact>() (342) и collider.GetComponentInParent<LootSupport>() (358) — оба поднимаются по цепочке родителей через мост в нативный код. Причём terminalCargo проверяет subject == Thing уже ПОСЛЕ поиска, то есть для лучей на ходоков и на место поиск делается впустую. 30 раз в секунду.

### 11. [SPLIT · день] Даже после починки компиляции плеерный билд не сможет играть с редакторным хостом: номера RPC разъезжаются

**Где:**
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:902`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:1041`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:1074`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:1936`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:2243`
- `Packages/com.firstgeargames.fishnet/CodeGenerating/Processing/Rpc/RpcProcessor.cs:101`

**Во что обходится:** Собранный клиент подключится к редакторному хосту, пройдёт проверку версии и НЕ БУДЕТ ИГРАТЬ: мышь не двигается, мир заморожен, ошибок игроку не видно. Механика: ткач FishNet присваивает RPC номер сквозным счётчиком по методам типа (RpcProcessor.cs:101, cr.MethodHash = rpcCount). В курьере пять RPC, и ТРИ ПЕРВЫХ (LabBalanceObserversRpc:902, LabShoveObserversRpc:1041, LabArrangementObserversRpc:1074) объявлены внутри #if UNITY_EDITOR. В редакторе SubmitInputServerRpc = 3, ReceiveSnapshotsObserversRpc = 4; в плеере они же = 0 и 1. BuildVersionAuthenticator этого не ловит: он сравнивает Application.version (BuildVersionAuthenticator.cs:57), а она у редактора и билда одного проекта ОДНА И ТА ЖЕ. Починка: три стендовых RPC и весь блок 626–1400 вынести в отдельный NetworkBehaviour, чтобы у боевого курьера набор RPC был одинаков в обеих конфигурациях.

### 12. [SPLIT · день] ThreadPresentation.Draw — 486 строк в одном методе

**Где:**
- `Assets/TunnelCrew/Network/ThreadPresentation.cs:724`
- `Assets/TunnelCrew/Network/ThreadPresentation.cs:1210`
- `Assets/TunnelCrew/Network/ThreadPresentation.cs:490`

**Во что обходится:** Метод длиннее любого файла в половине проекта; его нельзя прочитать целиком и нельзя проверить по частям. Draw: 724–1209 (486 строк). Widen: 1210–1393 (184). Apply(перегрузка): 490–662 (173). Файл целиком 2 207 строк с 32 идентификаторами свойств шейдера (220–251).

### 13. [MOVE · больше дня] Сборка «Networking» на 79% не про сеть: 36 файлов из 41 не упоминают FishNet

**Где:**
- `Assets/TunnelCrew/Network/TunnelCrew.Networking.asmdef:1`
- `Assets/TunnelCrew/Network/ThreadPresentation.cs:34`
- `Assets/TunnelCrew/Network/NetworkHouseholder.cs:56`
- `Assets/TunnelCrew/Network/CargoBody.cs:26`
- `Assets/TunnelCrew/Network/HouseholderSightSource.cs:1`

**Во что обходится:** Часть тех самых 316 секунд и невозможность трогать графику без сети. 11 939 строк из 15 042 (79%) в этой сборке ни разу не упоминают FishNet/NetworkBehaviour/NetworkManager. FishNet ткёт IL по ВСЕЙ сборке, ссылающейся на FishNet.Runtime, и делает это на каждой перезагрузке домена — то есть 37 раз за batch прогоняется ткач по 15 тысячам строк, из которых 12 тысяч ткать не за что. Крупнейший чужак — ThreadPresentation.cs (2 207 строк), чистое рисование верёвки: using только TunnelCrew.Core, Settings, UnityEngine. Реально сетевых файлов пять: NetworkWalkerCourier, NetworkSessionService, BuildVersionAuthenticator, NoRoomBroadcast, NetworkWalkerInput.

### 14. [SPLIT · больше дня] NetworkWalkerCourier — 2 312 строк, десять ссылок из сцены, семь несвязанных обязанностей; треть файла — редакторный стенд

**Где:**
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:22`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:626`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:1400`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:1774`
- `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs:2036`

**Во что обходится:** Любая правка в любой из семи тем — правка в файле, от которого зависят и вход, и симуляция, и картинка. Обязанности: сбор ввода клиента (1618–1712, 1774), серверный тик и симуляция (1774–1935), публикация снапшота (2036–2240), приём и применение снапшота (2265–2310), стенд IntegrationLab (626–1400), наблюдательный API домохозяина (там же), пять RPC. Блок #if UNITY_EDITOR 626–1400 — это 775 строк, 33% файла, редакторный инструмент внутри боевого NetworkBehaviour; именно он порождает находки №1 и №2. Десять [SerializeField] (строки 22–47) — десять мест, где сцену можно развести неправильно.

### 15. [SPLIT · больше дня] NetworkHouseholder — 1 320 строк: перенос груза, ИК-рука, равновесие, чтение JSON с диска и рисование гизмо в одном компоненте

**Где:**
- `Assets/TunnelCrew/Network/NetworkHouseholder.cs:531`
- `Assets/TunnelCrew/Network/NetworkHouseholder.cs:572`
- `Assets/TunnelCrew/Network/NetworkHouseholder.cs:735`
- `Assets/TunnelCrew/Network/NetworkHouseholder.cs:806`
- `Assets/TunnelCrew/Network/NetworkHouseholder.cs:935`
- `Assets/TunnelCrew/Network/NetworkHouseholder.cs:1315`

**Во что обходится:** Класс, в котором одновременно живут правила и картинка, — тот самый, где «доказательство» механики снимается не там, где механика. Внутри: LoadProfileForHost (531) читает файл с диска через System.IO в рантайме; AdvanceBalance (572) — правила равновесия; ShowHisHand (806) — ИК-презентация; TakeItUp/GoOnCarrying/PutItDown (935/991/1080) — логика переноски; Draw (1315) — гизмо. Плюс 24 незакрытых Debug.Log, из них LogBalanceTransition (735–787) печатает пять разных фраз про падение — и тест HouseholderBalancePhysicsTests.cs:273 утверждает именно ЭТИ СТРОКИ («Householder balance:»), то есть механика подтверждается текстом лога, а не состоянием.

**Что в этой области сделано хорошо и трогать не надо:**
- CargoBody.TakeOverSimulation/GiveBackSimulation (CargoBody.cs:377–435) — захват и возврат Physics.simulationMode атомарны, обе половины в try/catch восстанавливают исходное значение при любом исключении, и проектная гравитация не трогается вовсе. Не трогать.
- Защёлка неисправности CargoBody (ThrowIfSimulationFaulted, CargoBody.cs:438–458) закрывает не только писателей, но и ЧИТАТЕЛЕЙ — комментарий там объясняет, почему прикрытие одних писателей было хуже, чем ничего. Это редкий случай, когда лечили корень.
- ThreadDebugOverlay.TuningGaugesMayDraw (ThreadDebugOverlay.cs:52–63) — правильный образец: компилируемый затвор вместо рантайм-флага, потому что ассет помнит включённую галочку. Этот механизм надо переиспользовать, а не переписывать.
- BuildVersionAuthenticator — настоящий FishNet Authenticator, версия берётся из Application.version, поля-обхода намеренно нет, и клиенту отдельным broadcast сообщается ПРИЧИНА отказа (BuildVersionAuthenticator.cs:110–135). Единственное, чего он не ловит — расхождение номеров RPC редактор/плеер, потому что версия там одна и та же.
- Хост применяет собственный снапшот тем же ApplySnapshots, что и клиенты (NetworkWalkerCourier.cs:2220–2228, ExcludeServer=true на 2243), — одна кодовая дорожка рисования для всех экранов, без второй правды у хоста.
- ThreadAnchorSnapshot: место дальнего конца нити разрешается на хосте заново каждый тик из живого реестра (NetworkWalkerCourier.cs:2127–2137), а не запоминается — и вещь, пропавшая между тиком и картинкой, честно пропускается вместо линии в начало координат.
- NetworkSessionService (513) и LobbyController (246) — мелкие, разложенные на короткие методы, без god-object-признаков. В рефакторинг их брать не надо.
- Снапшот-структуры плоские, без вложенности и без своих сериализаторов (WalkerSnapshot, CargoSnapshot, ThreadAnchorSnapshot) — форма правильная, лечить нужно только состав полей.


---

## ОБЛАСТЬ 4: МИР, ДОМ, ПРОФИЛИ — Assets/TunnelCrew/World/**, World/HouseBuilding/**, Profiles/** (21 файл, 8 676 строк; замерено на 332488de)

Находок: **10**

**Лучшая правка области:** Свести HouseBuilding в headless-проект. Заменить единственный метод HouseDescription.InsideExtent() (HouseDescription.cs:1605, возвращает UnityEngine.Vector2 — это ВСЯ зависимость файла на 1 638 строк от движка; вызывается из трёх мест: HouseBuildingWindow.cs:304 и двух тестов) на обычную пару float, а в HouseShellLayout.cs заменить Vector3-как-контейнер и один Mathf.Max (строка 585) на простую структуру и Math.Max. После этого добавить четыре файла в tests/TunnelCrew.Core.Tests/*.csproj — тем же способом, каким туда уже заведён HouseholderProfileLoader.cs (строка 23 csproj), — и перенести туда HouseDescriptionEditModeTests.cs (393 строки) и HouseFurnishingsDescriptionEditModeTests.cs (257 строк), в которых НОЛЬ обращений к Unity API. Цена: день. Отдача тройная — 650 строк тестов уезжают из 316-секундного прогона в односекундный; 762 строки геометрии стен (HouseShellLayout) впервые становятся доступны для прямых модульных тестов на SplitLine/Cut/GroupByLine, которых сейчас нет вообще; 2 823 строки чисто редакторного кода перестают уезжать в билд плеера. Это одна правка, которая одновременно бьёт по «тесты долго гоняются» и по «тесты тестируют не то».

### 1. [SETTING · минуты] Файл дома, который владелец правит руками, МОЛЧА глотает опечатку в имени ключа

**Где:**
- `Assets/TunnelCrew/World/HouseBuilding/HouseDescription.cs:335`
- `Assets/TunnelCrew/Profiles/HouseholderProfileLoader.cs:243`

**Во что обходится:** HouseDescription.cs:335 зовёт JsonConvert.DeserializeObject<HouseFile>(text) БЕЗ настроек. По умолчанию MissingMemberHandling = Ignore. Напиши в first-house.house.json «cielingHeight» вместо «ceilingHeight» — ключ выбрасывается, HouseFile.SettingsEntry.CeilingHeight остаётся null, HouseDescription.Positive() (строка 1478) тихо подставляет fallback, дом строится с ДРУГИМ потолком, и ни одна жалоба не выводится: TryRead возвращает true. Соседний загрузчик того же репозитория делает ровно наоборот — HouseholderProfileLoader.cs:243 ставит MissingMemberHandling.Error именно ради этого. Файл при этом задуман под ручную правку: в нём есть поле «howToReadThis» — проза для того, кто его откроет. Ни одного теста на неизвестный ключ нет. Починка — одна строка JsonSerializerSettings.

### 2. [REWRITE · минуты] ShapeBody ругается в лог и продолжает — хозяин объявляется готовым с непроставленным телом

**Где:**
- `Assets/TunnelCrew/World/HouseholderRouteController.cs:336`
- `Assets/TunnelCrew/World/HouseholderRouteController.cs:343`
- `Assets/TunnelCrew/World/HouseholderRouteController.cs:317`

**Во что обходится:** TryInitialize — образцовая цепочка отказов: девять проверок, каждая возвращает false и гасит компонент. Последний шаг, ShapeBody() (строка 336), из этой цепочки выпадает: нет CapsuleCollider — Debug.LogError на 343 и просто return, после чего строка 316 присваивает _routePlaces, строка 317 возвращает true, IsReady становится true и судья берёт хозяина в работу. Тело при этом остаётся с размерами префаба, а не с числами из settings (радиус/высота/шаг). То есть один тихий рассинхрон роста хозяина против того, что заявлено в ассете, — ровно в той механике, где уже ловили «капсула не того размера» (комментарий 320-334). Починка: ShapeBody возвращает bool, TryInitialize его читает.

### 3. [DELETE · минуты] LocalWalkerController.cs и сцена SingleWalker.unity — мёртвые, и это единственный потребитель перегрузки PlayerState(x, z), которая молча означает y = 0

**Где:**
- `Assets/TunnelCrew/World/LocalWalkerController.cs:24`
- `Assets/TunnelCrew/Scenes/SingleWalker.unity:153`

**Во что обходится:** 31 строка, двигает transform напрямую с клавиатуры, сети не знает. Единственная ссылка во всём дереве — SingleWalker.unity:153, сцена из очень старой ноги c-exec-rules-layer-and-single-walker-001; её не открывает ни один тест и её нет в EditorBuildSettings. Там же m_EditorClassIdentifier указывает на «Assembly-CSharp::TunnelCrew.World.LocalWalkerController», хотя класс давно живёт в asmdef TunnelCrew.World. Отдельная цена: строка 24, new PlayerState(position.x, position.z) — ЕДИНСТВЕННОЕ использование двухаргументной перегрузки PlayerState во всём репозитории (все остальные 19 мест передают три числа). Пока она жива, в ядре стоит конструктор, который тихо ставит высоту в ноль — тот самый класс дефекта, с которым в этом же коде уже воевали (AuthoritativeWalkerRoster.cs:898, комментарий StartConditions.cs:61-67). Удаление контроллера и сцены освобождает возможность убрать и её.

### 4. [REWRITE · минуты] Positive() пропускает NaN и Infinity в размеры дома

**Где:**
- `Assets/TunnelCrew/World/HouseBuilding/HouseDescription.cs:1478`

**Во что обходится:** Проверка одна: if (value.Value <= 0f). Сравнение с NaN всегда false, а Infinity больше нуля — оба проходят как «нормальное положительное число». Newtonsoft по умолчанию читает литералы NaN и Infinity из JSON. То есть «ceilingHeight»: Infinity в файле дома даёт потолок Infinity, дальше HouseShellLayout строит ShellBox с Size.y = Infinity, и дом собирается без единой жалобы. Соседний загрузчик профилей эту же проблему уже решил явно — ReadFiniteNumber (HouseholderProfileLoader.cs:554) и ReadPositiveDuration (3387) проверяют float.IsNaN/IsInfinity. Здесь этой проверки нет. Одна строка.

### 5. [REWRITE · часы] Сцена уже разведена на ЧЕТЫРЕ старта игроков, а StartConditions умеет считать только до двух

**Где:**
- `Assets/TunnelCrew/World/StartConditions.cs:9`
- `Assets/TunnelCrew/World/StartConditions.cs:95`
- `Assets/TunnelCrew/World/StartConditions.cs:163`
- `Assets/TunnelCrew/Scenes/IntegratedHouse.unity:1080`

**Во что обходится:** enum StartPlayerCount = {One = 1, Two = 2} — третьего значения нет. В IntegratedHouse.unity строки 1080-1085 в _playerSpawns подвязаны ЧЕТЫРЕ трансформа, а _players: 2. Последствия конкретные: (а) TrySayWhatIsWrongWithThePlayerStarts (строка 95) крутит цикл до wanted = 2 — пустой 3-й или 4-й старт не проверяется ПЕРЕД запуском вообще, и вылезает только когда третий человек уже подключился, через InvalidOperationException «Player 3 is not wired» на StartConditions.cs:73; (б) OnDrawGizmos (строка 163) рисует ровно два маркера — позиции 3-го и 4-го стартов владелец расставляет вслепую, их не видно в Scene view. Последний коммит ветки называется «four-screens-see-one-fall», то есть демо целится в четыре экрана, а предпусковая проверка и рисовалка знают про два.

### 6. [SPLIT · часы] ReadDecisionHandlers — один метод на 681 строку с пятирукавным switch внутри

**Где:**
- `Assets/TunnelCrew/Profiles/HouseholderProfileLoader.cs:2272`
- `Assets/TunnelCrew/Profiles/HouseholderProfileLoader.cs:2404`
- `Assets/TunnelCrew/Profiles/HouseholderProfileLoader.cs:3789`

**Во что обходится:** Строки 2272-2952. Внутри switch на строке 2404 с рукавами: fact-combination (2406), accumulated-fact (2465), local-incident (2563), thing-belief (2632), chore (2759) — от 60 до 170 строк каждый. Все пять читают ОДИН общий DTO HouseholderDecisionHandlerDocument (строка 3789) с 15 необязательными полями, поэтому легальность поля для типа держится вручную написанной матрицей вызовов RejectHandlerField — 38 вызовов, фактически таблица 5×15, размазанная по 550 строкам. Я её проверил по клеткам: сейчас она ПОЛНАЯ, дырок нет. Но каждое новое поле в DTO требует не забыть дописать 4 запрета в четырёх разных рукавах на расстоянии 350 строк друг от друга, и цена забывчивости названа в комментарии самого файла (2331-2337): поле загрузится молча, обработчик сработает не по тому, что написал автор, и нигде ничего не скажет. Пять рукавов вынимаются в пять именованных методов механически.

### 7. [SPLIT · часы] HouseDescription.cs — 13 типов в одном файле на 1 638 строк, из них 1 200 в одном статическом классе

**Где:**
- `Assets/TunnelCrew/World/HouseBuilding/HouseDescription.cs:11`
- `Assets/TunnelCrew/World/HouseBuilding/HouseDescription.cs:293`
- `Assets/TunnelCrew/World/HouseBuilding/HouseDescription.cs:919`
- `Assets/TunnelCrew/World/HouseBuilding/HouseDescription.cs:1301`
- `Assets/TunnelCrew/World/HouseBuilding/HouseDescription.cs:1515`

**Во что обходится:** Строки 11-292 — три enum'а, Footprint и семь классов-описаний (DescribedPlace, DescribedFurnishing, DescribedLoot, DescribedRoom, DescribedBlock, DescribedDoorway, DescribedWindow). Строки 293-1638 — класс HouseDescription, в котором смешаны три разные работы: чтение файла (ReadRooms 469, ReadPlaces 538, ReadFurnishings 609, ReadLoot 748, ReadDoorways 950, ReadWindows 1128), проверки геометрии (CheckNothingOverlaps 919, CheckDoorwaysHaveSomewhereToStand 1094, CheckRoomIsDeepEnough 1110, IsOutsideWall 1257, SitsBehind 1283, SeamOf 1301, TrySharedSeam 1331) и рисование текстового отчёта для панели (Describe 1515, N 1509). Режется на 4 файла без изменения поведения: типы-описания, читалка, проверки, отчёт. Цена сейчас — та же, что у загрузчика: любая правка про комнаты и любая правка про окна трогают один файл.

### 8. [MOVE · день] Вся сборка HouseBuilding (2 823 строки) не нужна в рантайме и заперта в Unity-прогоне 316 с из-за трёх строк с Vector2

**Где:**
- `Assets/TunnelCrew/World/HouseBuilding/HouseDescription.cs:1605`
- `Assets/TunnelCrew/World/HouseBuilding/HouseDescription.cs:1609`
- `Assets/TunnelCrew/World/HouseBuilding/HouseDescription.cs:1635`
- `Assets/TunnelCrew/World/HouseBuilding/HouseShellLayout.cs:5`
- `Assets/TunnelCrew/World/HouseBuilding/HouseShell.cs:3`
- `tests/TunnelCrew.Core.Tests/TunnelCrew.Core.Tests.csproj:23`

**Во что обходится:** HouseDescription.cs (1638) + HouseShellLayout.cs (762) + HouseFile.cs (248) + HouseShell.cs (175) = 2 823 строки. Ни одной ссылки из рантайма: единственные не-тестовые потребители — Assets/TunnelCrew/Editor/HouseBuilding/HouseBuilder.cs и HouseBuildingWindow.cs; упоминание в Probe/House/HousePlan.cs:33 — это комментарий. Весь этот код при этом лежит в РАНТАЙМНОЙ asmdef и уезжает в билд плеера. Вся единственная зависимость от движка — Vector2 в одном методе InsideExtent() (строки 1605/1609/1635) и Vector3-как-контейнер + один Mathf.Max в HouseShellLayout. Из-за них тесты HouseDescriptionEditModeTests.cs (393 строки) и HouseFurnishingsDescriptionEditModeTests.cs (257 строк) — 650 строк, в которых НОЛЬ обращений к Unity API — крутятся в 316-секундном Unity-прогоне. Шапка первого файла прямо пишет: «None of this needs a running house.» Соседний HouseholderProfileLoader.cs уже подключён в headless-проект по имени (csproj:23) — механизм есть, эти файлы просто в него не заведены.

### 9. [SPLIT · больше дня] HouseholderProfileLoader.cs — 3 878 строк, +118 строк в день, 37 коммитов за 60 дней; сам разбор JSON занимает 1 строку

**Где:**
- `Assets/TunnelCrew/Profiles/HouseholderProfileLoader.cs:288`
- `Assets/TunnelCrew/Profiles/HouseholderProfileLoader.cs:236`
- `Assets/TunnelCrew/Profiles/HouseholderProfileLoader.cs:3878`

**Во что обходится:** Разбор JSON — это ОДИН вызов JsonConvert.DeserializeObject на строке 288. Остальные 3 877 строк — это: 383 строки объявления схемы (15 вложенных DTO-классов, 94 атрибута [JsonProperty], строки 3495-3877); 202 строки чтения скаляров и форматирования ошибок (3292-3493); 367 строк словарей «слово → enum», 15 однотипных методов с 81 case-меткой (1397-1763); ~2 300 строк смысловых проверок и сборки объектов (139 мест throw); 385 пустых и 302 строки комментариев. Файл вырос с 448 строк (2026-08-06) до 3 878 (2026-09-03) — 29 дней, монотонно, ни разу не резался; это самый правимый файл области (37 из 60 дней). Цена: каждая нога по хозяину правит ОДИН файл — параллельные сессии конфликтуют, ревью 3 900 строк никто не делает целиком, а «класс определяется чтениями из другого места» здесь особенно вероятен, потому что 15 DTO с 94 полями и матрица запретов на 5 типов обработчиков лежат в 600 строках друг от друга. Естественно режется на 8 файлов по уже существующим швам: (1) 16-233 сеам резолверов + исключение, 218 стр; (2) 3495-3877 DTO-схема, 383; (3) 3292-3493 + 554-580 + 1751-1763 скаляры и ошибки, ~240; (4) 1397-1763 словари слов, 367; (5) 582-1098 семейство условий, 517; (6) 1100-1395 + 1897-1957 эффекты/реакции/темпы, ~357; (7) 1765-1895 + 2272-2978 обработчики решений, ~840; (8) остаток — вход, занятия, ветки, шаги распорядка, ~700.

### 10. [MOVE · больше дня] HouseShellLayout.cs — 762 строки геометрии дома, один вызывающий и НОЛЬ прямых тестов

**Где:**
- `Assets/TunnelCrew/World/HouseBuilding/HouseShellLayout.cs:27`
- `Assets/TunnelCrew/World/HouseBuilding/HouseShellLayout.cs:295`
- `Assets/TunnelCrew/World/HouseBuilding/HouseShellLayout.cs:414`
- `Assets/TunnelCrew/Editor/HouseBuilding/HouseBuilder.cs:138`

**Во что обходится:** Grep по всему дереву: HouseShellLayout упоминается ровно в одном месте вне себя — HouseBuilder.cs:138. Ни одного теста, который зовёт Compute() напрямую. Значит вся математика — FindWallRuns (151), SplitLine (295), Cut (414), GroupByLine (251), StretchOutsideWallsToTheCorners (195), AnyRunReaches (218), StandingPlace (713) — проверяется ТОЛЬКО косвенно, через HouseBuiltEditModeTests.cs, который собирает префаб через AssetDatabase и смотрит на получившиеся GameObject'ы. Это ровно тот калибр, что в примере 2: доказательство снимается не там, где живёт дефект. Именно эта математика исторически давала «он ходил сквозь перегородки, а не через проёмы» (комментарий HouseholderRouteController.cs:18-23). Резать разрезы стен по проёмам без прямых тестов на SplitLine/Cut — играть вслепую.

**Что в этой области сделано хорошо и трогать не надо:**
- Маркеры сцены — HouseRoomMarker.cs (95), HousePlaceMarker.cs (95), HousePassageMarker.cs (121), HouseFurnishingMarker.cs (86), HouseholderObservationMarker.cs (47), CargoSpawnPoint.cs (59) — чистые: один факт на объект, редакторская отрисовка честно закрыта в #if UNITY_EDITOR, дублирующих полей имени нет. Трогать не надо.
- Границы #if UNITY_EDITOR в этой области ЦЕЛЫЕ. Проверил все 7 пар (DeliveryPoint 177/187, HouseholderObservationMarker 1/47, HousePassageMarker 60/119, HousePlaceMarker 53/93, HouseRoomMarker 49/93, LootSupport 104/117, StartConditions 144/225): ни одного чтения редакторного члена снаружи блока. Дефекта из примера 1 здесь нет.
- HouseWall.cs (97) и LootSupport.cs (119) — образцовые: читают КАЖДЫЙ коллайдер отдельно, а не одну коробку вокруг всего, фильтруют выключенные и триггеры, и отказываются вместо угадывания. Причина каждого решения записана в комментарии рядом.
- Ни одной аллокации в кадре: во всей области нет ни одного GetComponentsInChildren/GetComponent, вызываемого из Update. SceneHousePlan.Read() и HouseWall.WorldBounds аллоцируют, но зовутся только из редакторских панелей и один раз на старте мира. Производительность здесь чинить нечего.
- Контракт HouseDescription.TryRead (строка 326) — «или дом без жалоб, или жалобы без дома, никогда оба» — реально выполняется: все шесть читалок копят жалобы в один список, и дом собирается только при said.Count == 0. Это правильная конструкция, её надо сохранить при разрезании файла.
- HouseholderRouteController.TryInitialize (130-318) — девять отдельных отказов, каждый называет КОНКРЕТНОЕ сломанное число или слово, а не «настройки неверны». Кроме выпавшего ShapeBody, это лучший образец отказов в области.
- Матрица запретов полей в ReadDecisionHandlers на сегодня ПОЛНАЯ — я проверил все пять рукавов поклеточно, ни одно поле не проваливается молча. Проблема в способе её ведения, а не в её текущем состоянии.
- HouseholderProfileLoader уже заведён в headless-проект по имени (tests/TunnelCrew.Core.Tests/*.csproj:23) и покрыт 21 файлом тестов из tests/TunnelCrew.Core.Tests — это правильный образец, по которому надо тащить HouseBuilding, а не изобретать заново.


---

## ОБЛАСТЬ 5: Presentation, Settings, Core, Architecture, Bench/ReachLab, Photography, Feel, Words (+ ответ по Core↔Probe)

Находок: **11**

**Лучшая правка области:** Поставить \"defineConstraints\": [\"TUNNELCREW_ARCHITECTURE\"] в три asmdef ветки Architecture (Assets/TunnelCrew/Architecture/TunnelCrew.Architecture.asmdef, Assets/TunnelCrew/Editor/Architecture/TunnelCrew.Architecture.Editor.asmdef, Assets/Tests/TunnelCrew/Architecture/TunnelCrew.Architecture.EditorTests.asmdef). Это три строки JSON и ноль изменений в C#. Убирает из каждой компиляции и из каждого Unity-прогона 9 519 строк и 39 из 244 тестовых атрибутов (~16% медленного прогона), причём тестов, которые прибивают гвоздями геометрию авторенного префаба (3.7f, 2.1f), а не механику. Ветка не удаляется и не ломается: возвращается добавлением одного дефайна в Player Settings, когда ArchitecturalRoomShell реально подключат через World.ISolidPieces к живому дому. Это единственная правка в области, где отношение снятой цены к затраченным минутам исчисляется тысячами строк.

### 1. [SETTING · минуты] Ветка Architecture — замкнутый остров на 9 519 строк и 39 тестов, к которому игра не притрагивается, но платит за него каждой компиляцией и каждым прогоном

**Где:**
- `Assets/TunnelCrew/Architecture/TunnelCrew.Architecture.asmdef:1`
- `Assets/TunnelCrew/Editor/Architecture/TunnelCrew.Architecture.Editor.asmdef:1`
- `Assets/Tests/TunnelCrew/Architecture/TunnelCrew.Architecture.EditorTests.asmdef:1`
- `Assets/Tests/TunnelCrew/Architecture/TrailerHouseArchitectureEditModeTests.cs:159`

**Во что обходится:** Ни один .cs и ни один .asmdef вне трёх папок Architecture не называет TunnelCrew.Architecture; ни один из семи типов (RoomShellSolids, ArchitecturalRoomShell, TrailerHouse*) не упомянут снаружи. Его префабы лежат ровно в четырёх лаб-сценах (TrailerHouse_ArchitectureLab / _ApprovalLab / _EveningLab / RoomShell_LivingRoomLab), ни одной нет в EditorBuildSettings. Последний коммит — 2026-08-26. Это 1 052 строки рантайма (уезжают в плеер), 6 565 строк редакторных строителей и 1 902 строки тестов — 39 из 244 тестовых атрибутов в Assets/Tests, то есть ~16% медленного Unity-прогона, который целиком меряет ассет, а не механику: тесты прибивают гвоздями 3.7f, 2.1f и Is.EqualTo(3) авторенного префаба. Ветка НЕ мусор — ArchitecturalRoomShell реализует World.ISolidPieces, который живой CarryStand.cs:120 ищет, — значит она спроектирована подключаться. Но пока она не подключена, она берёт полную цену. defineConstraints в трёх asmdef снимает её целиком и возвращает одной строкой.

### 2. [MOVE · минуты] Фаза равновесия едет через два слоя сырым int, а порядок enum продублирован комментарием — компилятор молчит при перестановке

**Где:**
- `Assets/TunnelCrew/Presentation/HouseholderBalanceBody.cs:215`
- `Assets/TunnelCrew/Presentation/HouseholderBalanceBody.cs:227`
- `Assets/TunnelCrew/Presentation/HouseholderBodyPresenter.cs:174`
- `Assets/TunnelCrew/Presentation/TunnelCrew.Presentation.asmdef:4`
- `Assets/TunnelCrew/Network/NetworkHouseholder.cs:609`
- `Assets/TunnelCrew/Core/Householder/HouseholderBalance.cs:35`

**Во что обходится:** NetworkHouseholder.cs:609 кастует HouseholderBalancePhase в int, тот проходит два int-типизированных прыжка и расшифровывается литералами phase == 2 / == 3 / == 0 / == 1 внутри HouseholderBalanceBody. Комментарий на строке 215 честно пишет: «Applies a host phase without importing Core into this assembly. Values are the stable wire order». То есть порядок enum живёт вторым экземпляром в комментарии. Переставит кто-нибудь Fallen и Recovering — хозяин молча уляжется рэгдоллом там, где должен стоять, и ни один компилятор не возразит. Причина устранима одной строкой: TunnelCrew.Core движконезависим и не ссылается ни на что, добавление его в references у TunnelCrew.Presentation цикла не создаёт. Заодно семь loose float'ов в ShowReceivedPhase — это Vector3+Quaternion, у которых прямо в том же файле (строка 10) уже есть тип HouseholderBalanceDisplayPose.

### 3. [SETTING · минуты] Единственный Photoshoot в проекте стоит с _settings: {fileID: 0}, а PhotoshootSettings.asset не назван ни одной сценой и ни одним префабом

**Где:**
- `Assets/TunnelCrew/Scenes/TrailerHouse_EveningLab.unity:2130`
- `Assets/TunnelCrew/Settings/PhotoshootSettings.asset:1`
- `Assets/TunnelCrew/Photography/Photoshoot.cs:24`
- `Assets/TunnelCrew/Editor/Photography/PhotoshootCapture.cs:163`
- `Assets/Tests/TunnelCrew/Photography/PhotoshootRefusalEditModeTests.cs:39`

**Во что обходится:** Инструмент съёмки капсул для Steam: 350 строк рантайма + 715 строк редакторных команд + 11 тестов. Ассет настроек существует, но не привязан, а компонент в единственной сцене, где он стоит, держит нулевую ссылку — PhotoshootCapture.cs:163 на это и отвечает отказом «has no Photoshoot Settings asset». Все 11 тестов при этом — про ОТКАЗЫ и версионирование имён файлов на подставном объекте; ни один не проходит путь «снять набор». То есть тесты зелёные, а инструмент в проекте не запускается. Сцена, в которой он стоит, — из мёртвого острова Architecture, так что при парковке острова он потеряет и её.

### 4. [DELETE · минуты] Три ручки позы приседания на теле хозяина заполнены ИЗМЕРЕННЫМИ числами, и ни одну из них никто не читает — механику приседания заменил Final IK, а замер и ручки остались

**Где:**
- `Assets/TunnelCrew/Settings/BodyVisualDefinition.cs:78`
- `Assets/TunnelCrew/Settings/BodyVisualDefinition.cs:85`
- `Assets/TunnelCrew/Settings/BodyVisualDefinition.cs:88`
- `Assets/TunnelCrew/Settings/PresentationSettings.asset:57`
- `Assets/TunnelCrew/Editor/PeekPoseMeasure.cs:24`
- `Assets/TunnelCrew/Presentation/BodyReach.cs:11`

**Во что обходится:** В ассете у хозяина проставлено _standsAtInCrouchClip: 0.02 и _stoopsAtInCrouchClip: 0.4 — это не дефолты, это результат работы PeekPoseMeasure.cs (183 строки редакторного кода, написанного чтобы найти эти кадры). Правила при этом реально порождают CrouchAndPeekAtTarget (Probe/Householder/HouseholderReaction.cs:711). А в Presentation аксессоры ReachFollowSeconds, StandsAtInCrouchClip, StoopsAtInCrouchClip не вызываются НИ ОДИН РАЗ во всём Assets: BodyReach.cs:11 объясняет, что рукописное приседание из слоёв аниматора выбросили в пользу вендорского pullBodyVertical. Цена не в трёх мёртвых полях, а в том, что цепочка «правило решает пригнуться → замер кадров → ручки в ассете» построена целиком и оборвана на последнем звене, и это выглядит как рабочая настройка.

### 5. [DELETE · минуты] SideBySide.cs — 119 строк компонента, не поставленного ни в одну сцену и ни в один префаб

**Где:**
- `Assets/TunnelCrew/Bench/ReachLab/SideBySide.cs:1`

**Во что обходится:** Единственный MonoBehaviour во всей области, чей GUID не встречается ни в одном .unity, .prefab или .asset. Четыре его соседа по ReachLab стоят в ReachLab.unity, этот — нигде. Компилируется в плеер, читается при каждом обходе папки, и всякий, кто будет чинить стенд, потратит время на выяснение, куда он подключается.

### 6. [DELETE · минуты] Три мёртвые сцены, две из них не открывались со времён разделения на сборки

**Где:**
- `Assets/TunnelCrew/Scenes/HostWalksHisDay.unity:1`
- `Assets/TunnelCrew/Scenes/SingleWalker.unity:1`
- `Assets/Scenes/SampleScene.unity:1`

**Во что обходится:** HostWalksHisDay и SingleWalker: ноль упоминаний в .cs, нет в EditorBuildSettings, последний коммит 2026-08-14, и внутри у них m_EditorClassIdentifier: Assembly-CSharp::TunnelCrew.World.HouseholderRouteController — то есть их сохраняли, когда эти классы ещё лежали в дефолтной сборке, до появления asmdef. Их живой преемник — IntegratedHouse. SampleScene — шаблон Unity от 2026-06-13. Цена: при любом «пройди по всем сценам» (поиск, миграция, рефакторинг компонента) три сцены дают ложную работу и ложные ошибки.

### 7. [REWRITE · часы] Кукла хозяина при рождении масштабируется на 0.895, а единственный тест равновесия инстанцирует префаб без масштаба — это ровно случай №2 из брифа, но внутри Presentation

**Где:**
- `Assets/TunnelCrew/Presentation/BodyVisualInstance.cs:117`
- `Assets/TunnelCrew/Settings/BodyVisualDefinition.cs:124`
- `Assets/TunnelCrew/Settings/PresentationSettings.asset:46`
- `Assets/TunnelCrew/Settings/BodySizeSettings.asset:17`
- `Assets/TunnelCrew/Presentation/HouseholderBodyPresenter.cs:33`
- `Assets/Tests/TunnelCrew/Bodies/HouseholderPuppetEditModeTests.cs:27`

**Во что обходится:** В ассете _sourceHeight хозяина = 1.955, а _householderHeight = 1.75. FitTo даёт 0.8951, и BodyVisualInstance.Create строкой 117 умножает localScale ВСЕГО корня — а корень хозяина это _puppetPrefab, то есть рэгдолл PuppetMaster: 15 Rigidbody, 15 ConfigurableJoint, 30 записей массы, авторенных при масштабе 1. Якоря суставов и коллайдеры съезжают вместе с трансформом, а массы, тензоры инерции и пороги импульса BehaviourPuppet — НЕТ. Мышь при этом не масштабируется вовсе (0.2/0.2 = 1.0), так что единственное тело, которому физику молча пересчитали, — это то самое тело, чьё равновесие вчера объявили доказанным и сегодня признали сломанным. И охраняет его тест, который на строке 27 делает Object.Instantiate(puppetPrefab) напрямую: он меряет тело на 10.5% крупнее того, что стоит в сцене, и вдобавок проверяет не механику, а количества (Has.Length.EqualTo(15) трижды) и enum-значения сериализованных полей. Пока это не починено, любой замер равновесия — замер другого тела.

### 8. [MOVE · часы] Граница Core↔Probe декоративна: одно пространство имён на обе стороны, 22% «фундамента» моложе двух суток, и стрелка уже протекла в обе стороны

**Где:**
- `Assets/TunnelCrew/Probe/TunnelCrew.Probe.asmdef:3`
- `Assets/TunnelCrew/Core/TunnelCrew.Core.asmdef:1`
- `Assets/TunnelCrew/Core/Householder/HouseholderBalance.cs:1`
- `Assets/TunnelCrew/Probe/Solids/SolidBox.cs:21`
- `Assets/TunnelCrew/Probe/Solids/ThreadArc.cs:19`
- `Assets/TunnelCrew/Probe/Solids/ThreadLaunch.cs:66`

**Во что обходится:** Probe объявляет rootNamespace TunnelCrew.Core, и все 85 его файлов лежат в namespace TunnelCrew.Core — том же, что 7 файлов Core. В исходнике граница не видна ВООБЩЕ: ни одного using не меняется при переносе файла. Держит её только отсутствие ProjectReference в core/TunnelCrew.Core.csproj, и она уже не держится: HouseholderBalance.cs (195 строк) и HouseholderPhysicalInterruption.cs (26) попали в Core 2026-09-02, то есть 221 из 988 строк «осевшего фундамента» — двухдневный дизайн, и именно тот, который вчера сломался. В обратную сторону три файла Probe в собственных комментариях утверждают, что живут в Core (SolidBox.cs:21 «IT LIVES IN CORE», ThreadArc.cs:19, ThreadLaunch.cs:66) — читающий верит документу, а компилятор собирает иначе. Цена: правило, которое нельзя нарушить незаметно, стало правилом, которое нельзя проверить взглядом.

### 9. [REWRITE · часы] _cargoClearance никто не читает, хотя его парная ручка _cargoDetourMost читается — симптом, ради которого его написали, живёт, и крутить его бесполезно

**Где:**
- `Assets/TunnelCrew/Settings/ThreadLookSettings.cs:432`
- `Assets/TunnelCrew/Settings/ThreadLookSettings.cs:608`
- `Assets/TunnelCrew/Network/ThreadPresentation.cs:1103`

**Во что обходится:** Тултип описывает конкретный видимый дефект: «когда грань поворачивается от лапы, прямой прогон входит в одну стенку коробки и выходит из другой». Соседняя ручка того же блока (_cargoDetourMost, строка 610) прочитана в ThreadPresentation.cs:1103, а CargoClearance не прочитан НИГДЕ во всём Assets. Половина авторенной пары подключена, половина — нет. Владелец видит нитку сквозь коробку, лезет в инспектор, крутит зазор, ничего не меняется — и делает вывод о механике, а не о проводке.

### 10. [SETTING · часы] 3 340 строк лабораторного инструментария компилируются в плеер: четыре рантайм-сборки без ограничения платформы

**Где:**
- `Assets/TunnelCrew/Bench/ReachLab/TunnelCrew.ReachLab.asmdef:9`
- `Assets/TunnelCrew/Photography/TunnelCrew.Photography.asmdef:8`
- `Assets/TunnelCrew/Presentation/Feel/TunnelCrew.Feel.asmdef:9`
- `Assets/TunnelCrew/Presentation/Feel/ThreadFeelAuditionRig.cs:13`
- `Assets/TunnelCrew/Architecture/ArchitectureInspectionFlyCamera.cs:1`

**Во что обходится:** ReachLab 1 572 + Photography 350 + Feel-аудишен 366 (ThreadFeelAuditionRig + ThreadFeelAuditionSet) + Architecture 1 052 = 3 340 строк, у всех includePlatforms: [] — значит они в сборке игрока и в каждом domain reload. MovementBench.cs:29 при этом сам про себя пишет «IT IS A LAB TOOL... it lives under Probe, and nothing in the game references anything here» — и файл лежит в Bench/ReachLab, не в Probe. Продакшн-часть Feel (ThreadFeelBridge, стоит в IntegratedHouse) отделима от аудишен-части одним переносом. Цена сейчас скромная (размер сборки, время компиляции), но она растёт с каждым новым стендом, и уже есть лабораторный публичный метод в рантайме, способный подменить единственный авторитет настроек: ThreadPresentation.SetEditorVisualSettings.

### 11. [SPLIT · день] GameRulesSettings — ScriptableObject-бог на 767 строк и ~90 ручек от восьми несвязанных подсистем в одном ассете

**Где:**
- `Assets/TunnelCrew/Settings/GameRulesSettings.cs:49`
- `Assets/TunnelCrew/Settings/GameRulesSettings.cs:204`
- `Assets/TunnelCrew/Settings/GameRulesSettings.cs:127`
- `Assets/TunnelCrew/Settings/GameRulesSettings.cs:260`
- `Assets/TunnelCrew/Settings/GameRulesSettings.cs:268`

**Во что обходится:** В одном файле: ходьба ходока (скорость, радиус, масса, трение), равновесие хозяина, отдача от груза, весь трос (зазор, дрожь, подъём/спад усилия, перегруз, восстановление, прогиб), физика груза (солвер, демпфирование, сон, contact offset, шаги за тик), удержание/подъём (мощность, момент, кривая силы, дальность, число рук), шум контакта с радиусами слышимости, будильник и авторинг типов лута. Соседний PlaySettings.cs — образцовый композиционный корень из семи листьев, который «не владеет ни одним значением»; GameRulesSettings проглотил всё остальное. Цена: любое изменение настройки троса трогает файл, от которого зависят все сборки; любой тест, которому нужна одна цифра, поднимает весь объект; и «настроить руками» (полоса владельца) означает скроллить 18 разделов в одном инспекторе.

**Что в этой области сделано хорошо и трогать не надо:**
- Words — лучший слой в области, трогать нельзя. Семь файлов, из них движок нужен ровно двум (Phrases.cs, LocalizedText.cs), и headless-проект (tests/TunnelCrew.Core.Tests/TunnelCrew.Core.Tests.csproj) забирает папку ПАТТЕРНОМ с явным исключением этих двух — значит новый движконезависимый файл попадает под тесты сам, а забытое исключение падает громко на сборке. Единственное статическое состояние (Phrases._book) имеет и Forget(), и [RuntimeInitializeOnLoadMethod(SubsystemRegistration)] — между прогонами не протекает.
- PlaySettings.cs — образцовый композиционный корень: 36 строк, семь листьев, ни одного собственного значения, и в комментарии прямо сказано почему. Именно на этот образец надо резать GameRulesSettings, а не изобретать новый.
- Дублирования между Presentation и Network нет. Детектор одинаковых блоков по 8 значащих строк по Presentation/Network/World/Settings/Bench/Architecture/Photography дал ровно одно попадание внутри области — и это проброс из находки про int-фазу. Пары, которые выглядят дублями, на деле чистое разделение «кто» и «как»: MouseFaceKeys (Network, спрашивает судью) против MouseFacePresenter (Presentation, надевает лицо); WalkerHandPresentation (Network, решает чья лапа) против MouseHandPresenter (Presentation, ставит цель и гасит вес).
- Дефекта класса №1 из брифа (чтение редакторных членов вне #if) в области НЕТ. Единственное упоминание UnityEditor вне папок Editor — Photoshoot.cs:154 — стоит внутри своего #if UNITY_EDITOR, и вызывающий Update тоже. Проверены все восемь блоков условной компиляции: ни один не прячет член, читаемый снаружи.
- Ни одно [SerializeField] в области не остаётся полностью непрочитанным кодом — мёртвы только четыре ПУБЛИЧНЫХ аксессора при живых полях. Это значит, что инспектор не врёт про сами поля, и чинить надо адресно, а не сплошняком.
- HostPortForThisCheckout.cs — 238 строк на один номер порта выглядит перебором, но обоснованы: разбор текста вынесен из чтения файла и компилируется во всех конфигурациях (чтобы отказы можно было проверить тестом), а само чтение отрезано препроцессором, так что в сборке игрока ветки просто не существует. Трогать не надо.
- GameRulesSettings.OnValidate (строки 692–765) — правильный образец: аксессоры нормализуют значения, а OnValidate говорит вслух, что введённое число вышло за домен и каким игра воспользуется вместо него. Молчаливый clamp — это как раз то, из-за чего инспектор показывает одно, а игра идёт на другом; здесь это уже решено.


---

## ОБЛАСТЬ 6: все тесты (tests/TunnelCrew.Core.Tests/** + Assets/Tests/**) — 140 файлов, 54 253 строки, 882 headless-теста + 244 Unity-теста

Находок: **15**

**Лучшая правка области:** Одна строка: ProjectSettings/EditorSettings.asset:30 — заменить m_EnterPlayModeOptions: 0 на 3 (отключить перезагрузку домена и сцены при входе в Play Mode). Это снимает 41 полный цикл перезагрузки, то есть практически все 316 секунд: 316/41 = 7,7 секунды на цикл, и они уходят целиком в reload, а не в саму физику. Проверять при этом надо всего 13 мест изменяемого статического состояния, которые перестанут обнуляться сами: в тестах 7 полей в одном файле (CargoPhysicsMeasurementTests.cs:68-74, у которого уже есть свой Reset()), в продукте 6 — DevConsoleCommands.cs:23 (_registered), DevConsoleHost.cs:43 (_active), LabDragTarget.cs:50 (_hasTheKeys), HostPortForThisCheckout.cs:135 (_announced), Phrases.cs:28 (_book, у него уже есть Forget()), DeliveryPoint.cs:15 (ActivePoints). Тринадцать мест против 316 секунд каждый прогон. Вторым шагом — вынести EnterPlayMode из [UnitySetUp] в CargoSleepEditModeTests.cs:223: даже без правки настройки это одно место даёт 17 циклов из 41.

### 1. [SETTING · минуты] m_EnterPlayModeOptions=0 заставляет Unity перезагружать домен на каждый вход в Play Mode — 41 вход = все 316 секунд

**Где:**
- `ProjectSettings/EditorSettings.asset:30`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoSleepEditModeTests.cs:223`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoNoiseMeasurementTests.cs:75`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/HouseholderSightEditModeTests.cs:32`
- `Assets/Tests/TunnelCrew/WalkSpace/WalkSpaceClearanceEditModeTests.cs:51`
- `Assets/Tests/TunnelCrew/Scale/ScaleMeasurementEditModeTests.cs:63`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoPhysicsMeasurementTests.cs:110`
- `Assets/Tests/TunnelCrew/Networking/HouseholderBalancePhysicsTests.cs:40`
- `Assets/Tests/TunnelCrew/Networking/FourScreensSeeOneBalanceEventTests.cs:70`
- `Assets/Tests/TunnelCrew/Furnishings/FurnishingViewSeamEditModeTests.cs:65`
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/ThreeRoomHouseEditModeTests.cs:25`

**Во что обходится:** Причина 316 секунд найдена целиком и сходится числом. m_EnterPlayModeOptionsEnabled=1 при m_EnterPlayModeOptions=0 означает: перезагружать И домен, И сцену на каждом входе. Я насчитал 41 фактический вход в Play Mode из EditMode-сборок: CargoSleep 17 (EnterPlayMode стоит в [UnitySetUp] на строке 223, значит выполняется на каждый из 17 [UnityTest]), CargoNoise 6, HouseholderSight 5, WalkSpace 4, Scale 3, CargoPhysics 2, по 1 в Furnishing/ThreeRoomHouse/FourScreens/BalancePhysics. 316 / 41 = 7,7 секунды на цикл. Один CargoSleepEditModeTests.cs съедает 17 циклов ≈ 130 секунд — 41% всего времени. Пока это так, Unity-прогон нельзя гонять в цикле разработки, и его гоняют раз в день, то есть 244 теста фактически не работают как тесты.

### 2. [REWRITE · минуты] floorTop захардкожен нулём в тесте, который по названию сверяется с полами дома

**Где:**
- `Assets/Tests/TunnelCrew/HouseBuilding/FirstHouseInSceneEditModeTests.cs:217`
- `Assets/Tests/TunnelCrew/HouseBuilding/FirstHouseInSceneEditModeTests.cs:233`

**Во что обходится:** Тест называется NothingWideAndFlatSharesAHeightWithTheHousesOwnFloors. На строке 217 стоит var floorTop = 0f; и больше нигде не присваивается — на 233 сравнение идёт с литеральным нулём, а не с реальной высотой полов этого дома. Комментарий над тестом сам рассказывает, что дом ПЕРЕЕХАЛ со своего старого начала координат и что прошлая версия этой проверки уже пропустила закопанного по пояс хозяина. Дом сдвинут — проверка мимо, и мерцание двух поверхностей на одной высоте вернётся тем же путём.

### 3. [DELETE · минуты] CargoSnapshotRegistryTestsMetricsBehavioralControl — 28 строк, утверждающих свойства default(struct)

**Где:**
- `tests/TunnelCrew.Core.Tests/CargoSnapshotRegistryTestsMetricsBehavioralControl.cs:9`

**Во что обходится:** Единственный тест файла берёт default(CargoSnapshotDeltaMetrics) и живой Metrics и утверждает, что у первого IsEnabled=false, а у второго true. Первая половина — свойство ключевого слова default, а не кода: она не упадёт ни при какой поломке логики. Отдельный файл ради этого. Рядом, в CargoSnapshotRegistryTestsNegativeControls.cs, лежит настоящая работа — самодельная мутационная обвязка на 250 строк с PublicationCountMutant и UnisolatedFaultSubject.

### 4. [REWRITE · минуты] BodyReceiverEditModeTests.EveryConfiguredRole_NamesABodyAndAController — только проверки на not null

**Где:**
- `Assets/Tests/TunnelCrew/Bodies/BodyReceiverEditModeTests.cs:42`

**Во что обходится:** Оба утверждения — Is.Not.Null внутри цикла по Roles. Заменить префаб тела на чужой, подставить не тот контроллер — тест зелёный. Соседний тест в том же файле (строка 53) сделан правильно: он проверяет, что у контроллера есть три конкретных float-параметра, и объясняет в сообщении, почему Animator.SetFloat по отсутствующему имени молчит. Первый тест надо дотянуть до второго.

### 5. [MOVE · часы] CargoPhysicsMeasurementTests.MeasureCargoPhysics — 206 строк без единого утверждения: это генератор отчёта, записанный как тест

**Где:**
- `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoPhysicsMeasurementTests.cs:99`

**Во что обходится:** Тело с 99 по 305 строку не содержит ни Assert, ни StringAssert, ни вызова хелпера с утверждением — оно собирает StringBuilder, делает Debug.Log и WriteScratch('cargo-physics-measurement.txt'). Упасть может только на исключении. При этом он числится одним из 959 зелёных тестов и стоит один полный цикл EnterPlayMode/ExitPlayMode ≈ 7,7 секунды каждый прогон. Во всём файле 1845 строк и 5 тестов при 15 вызовах Assert — 123 строки на одно утверждение.

### 6. [REWRITE · часы] Мутационный гейт установлен и мёртв: Stryker.NET 4.6.0 закреплён, но весь его инвентарь указывает на удалённые пути

**Где:**
- `.config/dotnet-tools.json:1`
- `tools/mutation.ps1:17`
- `tools/mutation.ps1:18`
- `tools/mutation-scope.ps1:143`
- `tools/mutation-scope.ps1:213`
- `validation.config:1`

**Во что обходится:** dotnet-stryker 4.6.0 закреплён как локальный инструмент. tools/mutation.ps1 строки 17-18 по умолчанию берут core/GasCoopGame.Core.csproj и tests/GasCoopGame.Core.Tests/ — обоих нет на диске. tools/mutation-scope.ps1 (1126 строк) плюс его селф-тест (688 строк) описывают три модуля под Assets/GasCoopGame/** — каталог существует и содержит 0 файлов. В validation.config: mutation_input_roots=[], mutation_engine_free_modules=[], mutation стоит в списке not_wired_to_ordinary_or_deliver, а mutation_kill_floor=70 откалиброван по коду, которого больше нет. Итог: 1985 строк инфраструктуры измеряют пустоту, а число 70 в конфиге выглядит как действующий порог. Ответ на вопрос «можно ли прогнать мутационное тестирование» — да, и почти всё уже стоит: цель core/TunnelCrew.Probe.csproj (27 627 строк) и core/TunnelCrew.Core.csproj (988), драйвер tests/TunnelCrew.Core.Tests (882 теста, ~1 секунда). Нужно три правки строк с путями.

### 7. [MOVE · часы] 4 695 строк продукта втянуты <Compile Include> прямо в тестовый проект — Stryker их принципиально не мутирует

**Где:**
- `tests/TunnelCrew.Core.Tests/TunnelCrew.Core.Tests.csproj:22`
- `tests/TunnelCrew.Core.Tests/TunnelCrew.Core.Tests.csproj:29`
- `Assets/TunnelCrew/Profiles/HouseholderProfileLoader.cs:1`

**Во что обходится:** Stryker мутирует ПРОЕКТ-ПОД-ТЕСТОМ, а не тестовый проект. HouseholderProfileLoader.cs (3878 строк — тот самый файл-монстр) и Assets/TunnelCrew/Words/*.cs (817 строк) компилируются внутрь самого тестового проекта, значит останутся с нулевым мутационным покрытием даже после починки путей. Плюс CargoSnapshot.cs, CargoSnapshotRegistry.cs, четыре файла HouseholderObservation* и IntegrationLabArrangement.cs. Чинится тем же способом, что уже применён к Probe/Core: отдельный csproj-мостик, на который ссылается тестовый проект.

### 8. [MOVE · часы] Пять файлов про реакции хозяина — 5 583 строки — почти не дублируют УТВЕРЖДЕНИЙ; дублируют они обвязку

**Где:**
- `tests/TunnelCrew.Core.Tests/HouseholderReactionPriorityTests.cs:1`
- `tests/TunnelCrew.Core.Tests/HouseholderReactionsFromProfileTests.cs:1`
- `tests/TunnelCrew.Core.Tests/HouseholderChoreTests.cs:1`
- `tests/TunnelCrew.Core.Tests/HouseholderAdditionalReactionTests.cs:1`
- `tests/TunnelCrew.Core.Tests/HouseholderLocalIncidentTests.cs:1`
- `tests/TunnelCrew.Core.Tests/HouseholderActiveResponseRuleTests.cs:1`

**Во что обходится:** Прямой ответ, и он не тот, которого ждали. Я сверил попарно множества ожидаемых значений всех 308 тестов, где утверждений три и больше: НИ ОДНОЙ пары «одно и то же разными словами» между этими пятью файлами не нашлось. 1352 строки при 21 тесте, 1234 при 17, 1084 при 20, 966 при 9, 947 при 15 — это 82 теста, каждый со своим вопросом (кто выиграл тик, чем именно проиграли остальные, что рефузится по имени поля и пути JSON). Комментарии — 10,8% всего тестового кода (5 833 строки из 54 253), сообщения на ассертах — ещё столько же, и они несут диагноз, а не украшение. Вырезать здесь нечего; выносится только обвязка из предыдущей находки. Единственная настоящая пара близнецов во ВСЁМ дереве — CargoCarriedInAHandTests.cs:311/363 против CargoPutOnSurfaceTests.cs:148/230: один и тот же контракт отказа (Held / NoSuchPiece / NotAPlace, тело не сдвинулось), проверенный дважды для TryCarryTo и TryPutOnSurface. Это оправданно, но просится в один параметризованный контракт.

### 9. [REWRITE · часы] Три цикла в FurnishingViewSeam проходят вхолостую, если коллекция окажется пустой — а она набирается по суффиксу имени

**Где:**
- `Assets/Tests/TunnelCrew/Furnishings/FurnishingViewSeamEditModeTests.cs:103`
- `Assets/Tests/TunnelCrew/Furnishings/FurnishingViewSeamEditModeTests.cs:134`
- `Assets/Tests/TunnelCrew/Furnishings/FurnishingViewSeamEditModeTests.cs:156`
- `Assets/Tests/TunnelCrew/Architecture/TrailerHouseArchitectureEditModeTests.cs:76`

**Во что обходится:** На строке 103 views набирается фильтром transform.name.EndsWith(' View'). Если кто-то переименует детей, views пуст, и все три утверждения внутри цикла (нет коллайдера, нет rigidbody, нет HouseWall) проходят молча — тест зелёный, а шов разошёлся. Количество печатается через Report($"viewchildren={views.Length}"), но НЕ утверждается. То же на 134 (walls из GetComponentsInChildren<HouseWall>) и 156 (supports из LootSupport), и то же в TrailerHouseArchitectureEditModeTests.cs:76 (цикл по ArchitecturalRoomShell без проверки количества). Соседний файл ScaleMeasurementEditModeTests.cs:117 делает это правильно — Assert.That(measured, Is.GreaterThan(0)) — образец рядом есть.

### 10. [REWRITE · часы] LogAssert.ignoreFailingMessages = true в шести местах глушит встроенную проверку «в консоли нет ошибок» на весь тест

**Где:**
- `Assets/Tests/TunnelCrew/Networking/HouseholderBalancePhysicsTests.cs:45`
- `Assets/Tests/TunnelCrew/Networking/FourScreensSeeOneBalanceEventTests.cs:75`
- `Assets/Tests/TunnelCrew/NetworkingPlay/HeCarriesAThingAcrossTheHouseTests.cs:93`
- `Assets/Tests/TunnelCrew/NetworkingPlay/HouseholderSnapshotOnTheWireTests.cs:61`
- `Assets/Tests/TunnelCrew/NetworkingPlay/RealAddressConnectionTests.cs:39`
- `Assets/Tests/TunnelCrew/NetworkingPlay/TheLabStandsAnArrangementUpTests.cs:41`

**Во что обходится:** Флаг ставится ради одного постороннего предупреждения о неизменяемом пакете, но выключает реакцию на ЛЮБУЮ ошибку в логе на всё время теста. Все шесть — это самые дорогие тесты в наборе (сеть, физика, четыре экрана). Правильное лекарство — LogAssert.Expect на конкретное сообщение; сейчас же настоящий Debug.LogError из продукта посреди прогона не уронит ничего.

### 11. [REWRITE · часы] HouseholderBalancePhysicsTests доказывает механику попадания СТРОКАМИ ЛОГА, а не значениями

**Где:**
- `Assets/Tests/TunnelCrew/Networking/HouseholderBalancePhysicsTests.cs:234`
- `Assets/Tests/TunnelCrew/Networking/HouseholderBalancePhysicsTests.cs:235`
- `Assets/Tests/TunnelCrew/Networking/HouseholderBalancePhysicsTests.cs:236`
- `Assets/Tests/TunnelCrew/Networking/HouseholderBalancePhysicsTests.cs:237`
- `Assets/Tests/TunnelCrew/Networking/HouseholderBalancePhysicsTests.cs:275`

**Во что обходится:** Тест собирает _balanceLog через Application.logMessageReceived, фильтруя строки, начинающиеся с 'Householder balance:', и дальше вся механика доказывается через StringAssert.Contains на четыре куска текста плюс подсчёт совпадений IsAcceptedImpactLine/IsResumeLine. Часть теста сильная — там есть настоящие числа: сроки acceptedAt/repeatedAt/resumedAt и проверка, что второй удар не двигает дедлайн. Но словами «попадание принято», «окно открылось», «работа возобновилась» служат ПРЕДЛОЖЕНИЯ ДЛЯ ВЛАДЕЛЬЦА. Переписать формулировку лога — тест красный без единого изменения механики; убрать лог, оставив механику — тест красный тоже. Это ровно та ошибка, что уже стоила круга на равновесии.

### 12. [MOVE · день] 99 тестов гоняются под Unity, не вызывая ни одного API движка — их продукт тоже свободен от движка

**Где:**
- `Assets/Tests/TunnelCrew/Networking/HostPortPinTests.cs:1`
- `Assets/Tests/TunnelCrew/Networking/JoiningRulesTests.cs:1`
- `Assets/Tests/TunnelCrew/HouseBuilding/HouseDescriptionEditModeTests.cs:1`
- `Assets/Tests/TunnelCrew/HouseBuilding/HouseFurnishingsDescriptionEditModeTests.cs:1`
- `Assets/Tests/TunnelCrew/Networking/LocalAddressesTests.cs:1`
- `Assets/Tests/TunnelCrew/Networking/LabArrangementFilesTests.cs:1`
- `Assets/TunnelCrew/Network/TypedAddress.cs:1`
- `Assets/TunnelCrew/Network/JoinRefusal.cs:1`
- `Assets/TunnelCrew/Network/LocalAddresses.cs:1`
- `Assets/TunnelCrew/World/HouseBuilding/HouseFile.cs:1`
- `Assets/TunnelCrew/World/HouseBuilding/HouseDescription.cs:1605`
- `Assets/TunnelCrew/Settings/HostPortForThisCheckout.cs:5`

**Во что обходится:** Я посчитал в каждом Unity-тестовом файле число обращений к API движка (GameObject, Vector3, AssetDatabase, Physics, Mathf и т.д.). Ноль обращений: HostPortPinTests (33 теста), JoiningRulesTests (21), HouseDescriptionEditModeTests (19), LocalAddressesTests (10), LabArrangementFilesTests (3). Одно обращение: HouseFurnishingsDescriptionEditModeTests (12), HouseholderBalanceTuningWiringTests (1). Итого 99 тестов. Их продукт тоже почти чист: TypedAddress.cs, JoinRefusal.cs, LocalAddresses.cs, HouseFile.cs — ноль символов UnityEngine; HostPortForThisCheckout.cs уже прячет весь Unity за #if UNITY_EDITOR; HouseDescription.cs (1638 строк) трогает Vector2 ровно в одном методе InsideExtent() на строках 1605-1635. Способ переноса в проекте уже отработан — tests/TunnelCrew.Core.Tests.csproj именно так втягивает CargoSnapshot.cs, IntegrationLabArrangement.cs и Words/*.cs. Цена: 99 проверок недоступны в секундном цикле и (см. ниже) навсегда вне мутационного тестирования.

### 13. [MOVE · день] Скопированные один в один тела вспомогательных методов: 1 281 строка байт-в-байт, 1 402 с нормализацией чисел

**Где:**
- `tests/TunnelCrew.Core.Tests/HouseholderLocalIncidentTests.cs:803`
- `tests/TunnelCrew.Core.Tests/HouseholderReactionsFromProfileTests.cs:1149`
- `tests/TunnelCrew.Core.Tests/HandlersRecipeTests.cs:878`
- `tests/TunnelCrew.Core.Tests/HouseholderAuthoredIncidentWindowTests.cs:298`
- `tests/TunnelCrew.Core.Tests/HouseholderObservationToolTests.cs:810`
- `tests/TunnelCrew.Core.Tests/HouseholderChoreTests.cs:1001`
- `tests/TunnelCrew.Core.Tests/HouseholderThingBeliefTests.cs:532`
- `tests/TunnelCrew.Core.Tests/HouseholderWorldMarksTests.cs:382`
- `tests/TunnelCrew.Core.Tests/TestHouse.cs:1`
- `tests/TunnelCrew.Core.Tests/FurnishedHouse.cs:1`

**Во что обходится:** Это и есть настоящий ответ на «что дублируется». Метод CargoRules Rules(WorldSituationNoiseTuning) — 16 строк, байт в байт одинаковых, в пяти файлах (первые пять адресов выше). HouseholderWalkTuning Tuning() — 14 копий по 16 строк (208 строк впустую) плюс ещё 4 копии по 19. TakeHeardEvent — 24 копии. Load(json) — 9 копий. ReadContact/Read/ApplyPull/Step — по 10-11 копий каждый. Всего имя Rules( объявлено в 41 разном тестовом файле, Tuning( — в 26. При этом общие хелперы в проекте УЖЕ есть — TestHouse.cs (188 строк) и FurnishedHouse.cs (201), просто ими не пользуются. Цена: правка одного поля CargoRules требует 41 одинаковой правки, и любая пропущенная копия расходится молча.

### 14. [REWRITE · день] HouseholderBalanceBody — 344 строки, которые физически двигают тело при падении, — упомянуты в тестах ровно один раз и ни разу не проверены по результату

**Где:**
- `Assets/TunnelCrew/Presentation/HouseholderBalanceBody.cs:219`
- `Assets/TunnelCrew/Presentation/HouseholderBalanceBody.cs:266`
- `Assets/TunnelCrew/Presentation/HouseholderBalanceBody.cs:285`
- `Assets/TunnelCrew/Presentation/HouseholderBalanceBody.cs:308`
- `Assets/Tests/TunnelCrew/Bodies/HouseholderPuppetEditModeTests.cs:65`

**Во что обходится:** Подтверждаю известный пример владельца и называю файл. Конечный автомат HouseholderBalance.Advance проверен headless честно (tests/TunnelCrew.Core.Tests/HouseholderBalanceTests.cs, 114 строк, 7 тестов с настоящими значениями фаз и секунд) — это здоровая часть. А вот класс, который по этим фазам ДВИГАЕТ тело, встречается во всём тестовом дереве единственной строкой HouseholderBalanceBody.On(puppet). ShowHostPhase (219) и восстановление _targetRoot.localPosition = _targetRootRestLocalPosition (285, 308) не проверены ничем: ни одного утверждения о позе или высоте тела после цикла Fallen -> Recovering -> Stable. FourScreensSeeOneBalanceEventTests меряет РАЗБРОС между экранами, а не саму позу — четыре экрана могут согласованно показывать неправильную высоту, и он останется зелёным.

### 15. [REWRITE · больше дня] Ещё шесть механик без единого теста на результат: три из них свободны от движка и проверяемы headless за секунду

**Где:**
- `Assets/TunnelCrew/Probe/House/HouseWays.cs:74`
- `Assets/TunnelCrew/Probe/Householder/HouseholderEventMemory.cs:209`
- `Assets/TunnelCrew/Probe/Cargo/CargoBodyPort.cs:1`
- `Assets/TunnelCrew/World/HouseBuilding/HouseShellLayout.cs:27`
- `Assets/TunnelCrew/Editor/HouseBuilding/HouseBuilder.cs:1`
- `Assets/TunnelCrew/Network/IntegrationLabReadout.cs:1`
- `Assets/TunnelCrew/Network/LobbyController.cs:1`
- `Assets/TunnelCrew/Words/Phrases.cs:103`

**Во что обходится:** Ни одно из этих имён не встречается ни в одном тестовом файле. HouseWays.cs — 616 строк геометрии проходов, свободных мест и «можно ли туда встать» внутри headless-сборки Probe; методы TryStandingAt, TryWithin, TryWay, Swallows, Blocks не вызваны из тестов ни разу. HouseholderEventMemory.cs — 661 строка памяти о происшествиях, тоже headless. CargoBodyPort.cs — 656 строк, тоже. HouseShellLayout.Compute — 762 строки, которые ВЫЧИСЛЯЮТ все стены дома из комнат (стен в файле дома нет по замыслу); ошибка здесь двигает каждую стену, и её ловить некому — движка там только Vector3 и один Mathf.Max. HouseBuilder.cs — 1001 строка сборщика. IntegrationLabReadout.cs — 453 строки, ровно тот файл, что ломает сборку плеера, и он ни одним тестом не удерживается. LobbyController.cs — 246 строк. Phrases.cs — выбор языка (ChosenLanguage, LanguageOfThisMachine, PinPath, TextFolder) не вызван ниоткуда, и файл ЯВНО исключён из headless-сборки строкой Exclude в csproj: у выбора языка нулевое покрытие в обеих половинах. В цифрах по всей headless-части: 28 из 228 публичных типов и 73 из 262 публичных методов не названы ни в одном тесте.

**Что в этой области сделано хорошо и трогать не надо:**
- Ни одного теста БЕЗ утверждений во всём дереве, кроме одного названного: я прогнал все 1042 тела [Test]/[UnityTest] и нашёл ровно один случай (CargoPhysicsMeasurementTests.cs:99). Остальные, попавшие в черновой список, делегируют в хелперы вроде AssertRefused/Complains — это нормальная практика, а не дыра.
- Сообщения на ассертах несут диагноз, а не украшение. 'the two rules never got to argue, so this proves nothing', 'a carry broke an authoritative mouse hold', 'Animator.SetFloat on a missing parameter is ignored without an error, so this body would stand in its default pose forever'. Это дороже самих проверок и трогать это нельзя.
- Отрицательные контроли внутри тестов: FourScreensSeeOneBalanceEventTests.cs:167 отдельно утверждает, что слово вообще СДВИНУЛО тело ('four bodies that were never told anything'), а HouseholderBalancePhysicsTests.cs:167 держит негативный контроль до удара (Assert.That(_balanceLog, Is.Empty)). Люди, писавшие это, понимали, что зелёное на пустоте — тоже зелёное.
- Headless-конечный автомат равновесия сделан правильно: tests/TunnelCrew.Core.Tests/HouseholderBalanceTests.cs, 114 строк, 7 тестов, все утверждают конкретные фазы и секунды. Это образец того, как должно выглядеть остальное.
- CargoSnapshotRegistryTestsNegativeControls.cs — самодельная мутационная обвязка на 250 строк: контракт из 9 нарушений, живой субъект и три подложных мутанта. Это ровно то, что делает Stryker, только руками и для одного класса. Механизм годится как образец для следующих.
- Граница headless/Unity описана в самих csproj-ах прозой и держится компилятором: core/TunnelCrew.Core.csproj не имеет ProjectReference намеренно, и комментарий объясняет почему. Assets-файлы втягиваются по шаблону, а не списком, с пояснением 'список был бы вторым местом, где надо помнить'.
- Assets/Tests разбит на 11 отдельных asmdef по темам с узкими списками references — Architecture, Bodies, Photography не тянут ни Core, ни FishNet. Структура сборок здоровая, менять её не надо.
- Комментарии-заголовки объясняют, ПОЧЕМУ вопрос нельзя проверить игрой ('watching him walk to a noise does not say whether the sighting lost by weight, was never noticed, or was silently unreachable'). Это и есть обоснование существования теста, и оно записано.


---

ВСЕГО НАХОДОК: **80**

END_OF_FILE: live/indie-game-development/work/2026-09-03-codebase-audit-raw.md
