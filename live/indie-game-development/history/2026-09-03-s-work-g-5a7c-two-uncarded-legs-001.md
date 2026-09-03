RESULT s-work-g-5a7c-two-uncarded-legs-001 (call: — владелец-инициированная, без родительского CALL)
direction: indie-game-development   track: —   play: work   node/task: bet-g-5a7c-wave-12

outcome: |
  **ДВЕ НОГИ, ШЕДШИЕ БЕЗ КАРТОЧЕК, ЗАВЕДЕНЫ ЗАДНИМ ЧИСЛОМ ПО ЕГО СЛОВУ «заведи карточки тем двум
  ногам».** Это тот самый учётный провал, которым волна 11 потеряла восемь ног полосы стенда;
  здесь он закрыт в день появления, а не на сверке.

  И карточка первой из них оказалась не бумагой: **стенд «хозяин» не прошёл приёмку его глазом с
  первого раза, и починка отменила решение Р14 плана.**

  **1. `c-exec-g-5a7c-bench-polygon-proba-1` — WIN-U4, `running`.** Расписка запуска — аренда
  слота (`lifecycle: CLAIMED`, endpoint `http://localhost:26436/p/94b6fcef`); ветка
  `slot/win-u4` на `90fbc3ea`, два коммита вне `main`. Словами самого исполнителя в `16003cc0`:
  «The owner opened what was delivered and could not test with it: a top-down view of a whole house
  in which a stumble does not read, and a panel that filled the screen with numbers. Both were mine
  to see and I shipped them unseen.»

  **Значит долг приёмки волны 11 НЕ оплачен, и причина другая, чем направление записало утром.**
  `t-the-bench-shows-why-he-fell-1` стоит `waiting` не потому, что владелец ещё не смотрел, а
  потому, что он посмотрел и стенд не годился. `unblock_when` задачи исправлен.

  **И РЕШЕНИЕ Р14 ПЛАНА ОТМЕНЕНО ЕГО СЛОВОМ.** Р14: «Стенды — наборы внутри `MouseLab`… отдельная
  сцена — только если набор не помещается по устройству»; строка 1 `done_when` задачи повторяла это
  буквально. Стенд переехал в собственную сцену `HouseholdLab.unity` — голый пол, хозяин, больше
  ничего в кадре. Причина не «не помещается», а сильнее: **дом мешал смотреть.** Исполнитель
  фиксирует его слово: «He asked why we need a house at all; there was no good answer.»
  Заведена улика `i-the-bench-failed-his-eye-and-moved-to-its-own-scene-001` с `route: review`:
  решать, идёт ли поправка Р14 патчем в план, будет сверка 11.09, а не эта нога.

  **2. `c-exec-g-5a7c-the-morning-ends-at-the-door-002` — WIN-U3, `running`.** Живая проба
  удлинённого утра; вне `main` ничего, ветка на `198ab3fe`. Владелец добавил ей вопрос-замер, и
  повод у вопроса был спорный: исполнитель сказал ему «помеха не должна отнимать время», и это
  прозвучало так, будто помехи времени не стоят.

  **НАПРАВЛЕНИЕ ПРОВЕРИЛО ПОСТРОЕННОЕ И ПОДТВЕРДИЛО: СПОР БЫЛ О СПОСОБЕ ЗАПИСИ, А НЕ О ПОВЕДЕНИИ.**
  Запас выводится каждый тик (`S = (дедлайн − сейчас) − ETA_min`), дедлайн — авторенное число и
  «is not a countdown and is never mutated by an event»; источников вида `EventPenalty` в проекте
  ноль; тесты называют обе стороны прямо — крюк вне обязательного пути ТРАТИТ запас, скрытая помеха
  не двигает его до знания хозяина. Помеха время отнимает, просто настоящими секундами его часов,
  а не бухгалтерской записью. **Мины здесь нет.**

  **МИНА, ЕСЛИ ОНА ЕСТЬ, В ДРУГОМ МЕСТЕ, И ОНА НОВАЯ С СЕГОДНЯ.** ETA считается по прямой между
  местами, без поиска пути. Настоящая ходьба идёт в обход мебели и через проёмы, то есть всегда
  длиннее прямой — ошибка **односторонняя**: ETA занижен, запас завышен. На утре 120 секунд с
  ногами по 12 она была мелкой; после `35a17831` утро 360 секунд, а ноги по 110, и ошибка копится
  втрое дольше. Владелец отправил ноге замер: разница между суммой ETA и настоящим временем на
  одном утре без помех, в секундах и в долях буфера 90 с, и режим в последней трети утра. Границей
  запрещено строить коэффициент и трогать формулу.

evidence: |
  - Его слова в этой сессии: «отправил в U3, теперь заведи карточки тем двум ногам». Ранее в этой
    же сессии — вопрос про «две шкалы времени» и «чтобы тут какой-то мины не было зарыто».
  - Аренды слотов, `gascoop-slot-state.v1.json` на 03.09: WIN-U1 `CLAIMED`
    (`c-exec-g-5a7c-the-magnet-has-two-poles-on-a-thing-001:build`), WIN-U2 `AVAILABLE`,
    WIN-U3 `CLAIMED` (`c-exec-g-5a7c-the-morning-ends-at-the-door-002:proba`), WIN-U4 `CLAIMED`
    (`c-exec-g-5a7c-bench-polygon-proba-1:build`).
  - Ветки: `slot/win-u1` `0a23a7f4` (5 вне `main`), `slot/win-u2` = `origin/main` = `2cea9a94`,
    `slot/win-u3` `198ab3fe` (0 вне), `slot/win-u4` `90fbc3ea` (2 вне).
  - `16003cc0` «Make the householder's bench a polygon you can actually watch» — цитата про
    приёмку и про дом приведена дословно; `90fbc3ea` «Make the throw actually reach him, and give
    the bench its own camera» — `Network/BenchFlyCamera.cs` +125, `IntegrationLabWindow.cs` +45,
    `IntegrationLabRig.cs` +22, `Scenes/HouseholdLab.unity`.
  - Резерв времени, перемерено на `198ab3fe`:
    `Probe/Householder/HouseholderTimeReserve.cs` — `DeadlineSeconds` описан как «not a countdown
    and is never mutated by an event»; `SlackSeconds` документирован как `S = (deadline - now) -
    ETA_min`; `Pressure = clamp((B - S)/B, 0, 1)`.
  - Поиск `EventPenalty|SubtractSeconds|LoseSeconds|PenaltySeconds|AddPenalty` по
    `Assets/TunnelCrew` — ноль совпадений.
  - `tests/TunnelCrew.Core.Tests/HouseholderTimeReserveTests.cs` — девять тестов, из них по существу:
    `MandatoryWalkingConsumesClockAndEtaTogetherSoSlackStaysStill`,
    `OptionalDetourThatDoesNotAdvanceTheMandatoryPathSpendsSlack`,
    `HiddenMugMovedByMiceCannotChangeReserveBeforeHeKnows`,
    `LateReserveDoesNotStopTheNextMorningTick`,
    `EtaIsRemainingMandatoryPhasesPlusStraightLinePlacesAtWalkingSpeed`.

state_changes: |
  1. ADD card `c-exec-g-5a7c-bench-polygon-proba-1` (`call`, `to: executor`, `status: running`,
     `slot: WIN-U4`, `basis: 90fbc3ea`, `parent: c-exec-g-5a7c-the-bench-shows-why-he-fell-001`,
     `note`: заведена задним числом) с блоком `call`, описывающим пять изменений ноги.
  2. ADD card `c-exec-g-5a7c-the-morning-ends-at-the-door-002` (`call`, `status: running`,
     `slot: WIN-U3`, `basis: 198ab3fe`, `parent: c-exec-g-5a7c-the-morning-ends-at-the-door-001`)
     с блоком `call`, несущим замер направления по резерву времени и текст вопроса владельца.
  3. SET `t-the-bench-shows-why-he-fell-1` → `unblock_when`: «второй взгляд владельца: первый
     показал, что стенд не годился — вид сверху и панель во весь экран». Статус остаётся `waiting`.
  4. ADD issue `i-the-bench-failed-his-eye-and-moved-to-its-own-scene-001`
     (`level: objective`, `route: review`) — отмена Р14 его словом и непройденная приёмка.
  5. Журнальные строки на ставку и затронутые карточки. Блок `tracks` ставки не правится: строка 1
     `done_when` задачи про «не третья сцена» остаётся подписанной, а её отмена лежит уликой рядом,
     чтобы сверка 11.09 видела и то и другое.
  6. `NOW.md` не менялся. План не тронут: поправка Р14 — работа `review`, не этой ноги.

captures:
  - Направление утром записало причину `waiting` у стенда неверно — «владелец ещё не смотрел»,
    тогда как он смотрел и отказал. Ошибка прожила полдня и найдена только чтением коммитов слота.
    Возвраты исполнителя надо читать по байтам, а не по строке аренды.
  - Второй раз за день строка, написанная нарезкой буквально («не третья сцена»), оказалась уже
    другой в продукте по его слову. Первый раз — строка прогноза про `Network/**`. Обе поправки
    идут уликами и журналом, ни одна — правкой подписанного блока.

decisions_needed:
  - q: Поправка Р14 плана («стенды — наборы внутри MouseLab») после переезда стенда в собственную
      сцену `HouseholdLab` его словом.
    options: [патч плана разделом 14 сейчас; решение сверки 11.09]
    recommendation: сверка 11.09 — план меняет `review` из находок, а не нога по ходу.

play_check:
  - 1 recite: done — работа названа его словами: «заведи карточки тем двум ногам».
  - 2 owner inputs (owner): done — его слово на заведение карточек; его же слово про сцену
    процитировано через фиксацию исполнителя, а не приписано. Решение о поправке плана за него не
    принято и вынесено в `decisions_needed`.
  - 3 do the work: done — обе карточки заведены с расписками запуска, улика на отмену Р14 заведена,
    `unblock_when` стенда исправлен.
  - 4 self-check: done — собственная ошибка утра названа в captures, а не затёрта. Ни один
    подписанный блок ставки не переписан.
  - 5 close: done — `close: light — because` каждая строка выведена из аренды слотов, из коммитов
    `slot/win-u4` и `slot/win-u3`, из байтов `HouseholderTimeReserve.cs` и имён тестов, и из его
    собственных слов в этой сессии. G5-чат не открывается.

log: две ноги, шедшие без карточек, заведены задним числом — и одна из них оказалась не бумагой: стенд «хозяин» НЕ прошёл приёмку его глазом с первого раза («он открыл доставленное и не смог им тестировать — вид сверху и панель во весь экран»), а починка перенесла стенд в собственную сцену HouseholdLab, чем отменила решение Р14 плана его же словом «зачем нам вообще дом»; заведена улика с route review, поправку плана решает сверка 11.09; спор про «помеха не отнимает время» проверен по байтам и закрыт — запас выводится, EventPenalty в проекте ноль, крюк вне пути запас тратит, скрытая помеха не двигает; настоящий риск в другом — ETA считается по прямой, а утро стало 360 секунд, и владелец отправил ноге замер

next: |
  Полосы: WIN-U4 и WIN-U3 заняты продолжениями (теперь с карточками), WIN-U1 держит магнит,
  WIN-U2 свободен и ждёт `c-exec-g-5a7c-four-screens-see-one-fall-001`.
  Приёмка стенда — второй взгляд владельца после того, как нога вернётся.
  Поправка Р14 — вопрос сверки 11.09.

END_OF_FILE: live/indie-game-development/history/2026-09-03-s-work-g-5a7c-two-uncarded-legs-001.md
