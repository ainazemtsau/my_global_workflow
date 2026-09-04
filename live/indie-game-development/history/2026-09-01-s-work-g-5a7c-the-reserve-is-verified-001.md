# RESULT — s-work-g-5a7c-the-reserve-is-verified-001

direction: indie-game-development
play: work
node/task: g-5a7c / t-the-morning-has-a-reserve-1
track: утро давит
date: 2026-09-01
outcome_kind: close — запас времени построен исполнителем и перепроверен направлением на байтах; закрытие светлое, все девять строк сняты заново

owner_approved: |
  Слова владельца на закрытие не требовалось и не запрашивалось: строки приёмки этой задачи —
  факты о коде и о живом прогоне, а не его вердикт. Его глаз стоит в приёмке следующей задачи
  (`t-the-same-prank-costs-differently-1`), где он прячет одну вещь рано и поздно.

outcome: |
  **ЗАКРЫТИЕ СВЕТЛОЕ: ни одна строка не принята на слово исполнителя.** Все девять сняты заново
  направлением у `66124951`, и три порога волны доказаны **пустыми поисками без масок по путям** —
  по правилу `a-narrowed-search-cannot-produce-a-global-negative`, заведённому часом раньше.

  | Порог волны | Поиск | Результат |
  |---|---|---|
  | штраф временем за событие | `EventPenalty\|SpendReserve\|reserve -=\|slack -=\|PenaltySeconds\|DeductSeconds` | пусто |
  | ветвление поведения по режиму | `if.*Mode.*(Late\|Tight\|Comfortable)\|== TimeReserveMode\|case TimeReserveMode` | пусто |
  | конец утра по `S ≤ 0` | `EndRound\|EndMorning\|MorningOver\|GameOver` | пусто |

  **ЧИСЛА ЖИВУТ ДАННЫМИ.** Профиль несёт новый блок `timeReserve`: `nextRequiredState`,
  `deadlineSeconds 120`, `comfortableBufferSeconds 30`. В `HouseholderTimeReserve.cs` зашитых
  `120` и `30` нет.

  **ДЕВЯТЬ ТЕСТОВ НАЗВАНЫ ПО СТРОКАМ ПРИЁМКИ**, и это лучшее в возврате. Среди них
  `HiddenMugMovedByMiceCannotChangeReserveBeforeHeKnows` — главный инвариант спеки;
  `MandatoryWalkingConsumesClockAndEtaTogetherSoSlackStaysStill` и
  `OptionalDetourThatDoesNotAdvanceTheMandatoryPathSpendsSlack` — две строки таблицы спеки;
  `DisplayModeChangesNoDecisionOrPhysicalAction` — запрет на три ветки поведения;
  `LateReserveDoesNotStopTheNextMorningTick` — запрет на конец утра по нулю.

  **ЖИВЬЁМ ЗАКОН СПЕКИ НАБЛЮДАЕТСЯ ЧИСЛОМ:** необязательное дело потратило `49,08 с` запаса, а
  обязательный подход длиной `10,03 с` стоил всего `3,06 с`. Это и есть «время идёт, но оставшийся
  ETA сокращается настолько же».

  **ОШИБКА НАПРАВЛЕНИЯ, ТРЕТЬЯ ЗА ДЕНЬ И ТОГО ЖЕ КЛАССА.** Проверяя наличие тестов, направление
  снова искало по маске — `Assets/Tests/**` — и получило пусто, хотя тесты лежат в
  `tests/TunnelCrew.Core.Tests/`. Правило, заведённое час назад, было верным; его просто не
  выполнили. Ошибка поймана следующим же замером и до записи в карточку не дошла, но записывается
  здесь: **правило не работает, пока его не исполняют, и одного дня мало, чтобы это вошло в руку.**

  **МЕЛОЧЬ ПО ФОРМЕ, НЕ ЗАСЧИТАННАЯ В ДЕФЕКТ.** Возврат не нёс первой строки с числом полученных
  строк `done_when` — расписки, которой требует `an-order-does-not-exist-until-it-is-delivered`.
  По существу правило выполнено: работа сделана ровно по девяти строкам. Отмечено в карточке наряда.

state_changes: |
  - `t-the-morning-has-a-reserve-1` → `done`, с журнальной строкой перепроверки;
  - `c-exec-g-5a7c-the-morning-has-a-reserve-1-001` → `done`;
  - `t-the-same-prank-costs-differently-1` разблокирована; `unblock_when` снят, и добавлена
    оговорка: непрерывного `P` первая задача НЕ публикует, но `SlackSeconds` и
    `ComfortableBufferSeconds` дают его без остатка;
  - заведена `i-unity-test-runs-cost-five-minutes-for-one-second-of-work-001`;
  - journal-строка в `bet-g-5a7c-wave-11`.

evidence: |
  `main` = `dev` = `origin/main` = `origin/dev` = `slot/win-u4` = `66124951`.
  Аренда WIN-U4 освобождена, слот `AVAILABLE` — проверено в общем реестре, а не по памяти.
  WIN-U1 держит `t-a-flying-thing-knocks-the-mouse-down-1:BUILD`, WIN-U2 —
  `t-a-body-that-can-ragdoll-1:BUILD`.

  Тесты по словам ноги: headless `769/769/0`, EditMode `224/224`. Направление число не
  переснимало — гейт зелёный у публикации, и это тот случай, где чужой прогон является уликой.

next: |
  Полоса `утро давит` идёт ко второй задаче — наряда пока нет. Волна: U2 тело хозяина,
  U1 провод от летящей вещи, U4 свободен.

  Отдельно заведена улика про пять минут на прогон тестов в Unity против секунды headless —
  тридцать семь циклов перезагрузки домена за batch. Чинится своей маленькой ногой, в волну не
  входит.

END_OF_FILE: live/indie-game-development/history/2026-09-01-s-work-g-5a7c-the-reserve-is-verified-001.md
