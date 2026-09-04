# RESULT — s-work-g-5a7c-balance-published-bench-ordered-001

direction: indie-game-development
track: хозяин спотыкается
play: work
node/task: g-5a7c / t-he-loses-his-balance-and-tries-to-stay-up-1
date: 2026-09-02

outcome: |
  Равновесие хозяина опубликовано в продукте и закрыто физикой, но НЕ принято
  глазом — и это записано долгом, а не победой. Задача переведена в waiting,
  её наряд закрыт.

  Возврат ноги, сверх механики, написал наряд будущему стенду равновесия. Наряд
  сохранён готовым к выдаче и не выдан: владелец назвал место и время платежа —
  другой слот, не WIN-U2, и следующая волна, не эта.

  Попутно выправлены три карточки нарядов, стоявшие ready при закрытых ногах.

evidence: |
  Продукт: main = dev = origin/main = origin/dev = 2d2c27ff7e15430590fe75565c57d4a4b697b2f6,
  проверено `git rev-parse` в C:\projects\Unity\GasCoopGame_win-u4. Реестр слотов
  gascoop-slot-state.v1.json: все четыре слота AVAILABLE, аренда none.

  Прогоны ноги: EditMode 233/233 на merged bytes, headless 819/819, независимое
  ревью GREEN без открытых Critical/Important. Физика: настоящий Alarm Clock 48 кг
  на 12 м/с по production-пути CargoBody -> PhysX -> PuppetMaster ->
  NetworkHouseholder; accepted impact 0,52 при 8,3 град; stock fall при 10,7 град;
  исходный deadline повторным ударом не продлён; recovery завершён; прежняя работа
  возобновлена.

  ДВА САМЫХ РИСКОВАННЫХ ПОРОГА ПЕРЕПРОВЕРЕНЫ НАПРАВЛЕНИЕМ ПО БАЙТАМ, а не приняты
  с отчёта, потому что оба были сужены мной же:
  - Assets/TunnelCrew/Probe/TunnelCrew.Probe.asmdef ссылается только на
    TunnelCrew.Core, noEngineReferences true; `git grep -iE "puppet|rootmotion|
    UnityEngine" -- Assets/TunnelCrew/Probe/**` пуст.
  - Факт прерывания вошёл в Probe узко: HouseholderPhysicalInterruption несёт один
    float секунд и потребляется в Assets/TunnelCrew/Probe/Multiplayer/CarryWorld.cs.
    Механизм остался в Core/Presentation.
  - Числа лежат в Assets/TunnelCrew/Settings/GameRulesSettings.asset:
    _householderBalanceAttemptTiltDegrees 8, _householderBalanceAttemptSeconds 1.5,
    _householderBalanceFallTiltDegrees 35 — не в коде.

  НЕ ДОКАЗАНО: понимает ли игрок, какой предмет вызвал потерю равновесия; различает
  ли попытку устоять и падение; видит ли согласованную реакцию host и client.

  Слово владельца о месте и времени стенда, дословно: «пока не стоит так как он
  занимался стендом и лучше в другом слоте это сделать и возможно даже отложить в
  другую волну что бы сначало был стенд где мы сможем проверять».

state_changes: |
  cards/t-he-loses-his-balance-and-tries-to-stay-up-1.md
    status: active -> waiting; три записи журнала (публикация и цена приёмки;
    байтовая перепроверка двух порогов; наряд стенду из её возврата).
  cards/c-exec-g-5a7c-he-loses-his-balance-1-001.md
    status: ready -> done; запись журнала о закрытии и освобождении WIN-U4.
  cards/c-exec-g-5a7c-a-flying-thing-knocks-the-mouse-down-1-001.md
    status: ready -> done; починка писарской заминки, приёмка задачи не тронута.
  cards/c-exec-g-5a7c-one-lab-he-can-set-up-himself-1-001.md
    status: ready -> done; наряд исчерпан, продолжение — отдельным нарядом.
  cards/c-exec-g-5a7c-the-same-prank-costs-differently-1-001.md
    status: ready -> done; закрытие было записано 2026-09-01, статус отставал.
  cards/bet-g-5a7c-wave-11.md
    в разделе закрытия: строка таблицы про равновесие уточнена, добавлены два
    абзаца — требование о спецификации выполнено, и его слово о слоте и волне;
    одна запись журнала.
  work/2026-09-02-order-the-homeowner-balance-bench.md
    новый файл: наряд стенда равновесия, готов, НЕ выдан.

captures:
  - Наряд стенда пишет нога, которая упёрлась в его отсутствие, а не та, что будет строить. Сработало дважды подряд: стенд мыши и этот.
  - Source, strength, сырой tilt и countdown по snapshot не передаются — стенд обязан честно пометить их HOST ONLY, второй конвейер решений на клиенте запрещён.

decisions_needed: []

play_check:
  - 1 recite — done: done_when задачи перечитан, пороги 7 (Probe) и 6 (числа в настройках) проверены отдельно, потому что оба сужались направлением.
  - 2 owner inputs — done: владелец уже дал два слова, оба использованы дословно — «берём Б» и отказ вести стенд в WIN-U2 внутри этой волны.
  - 3 do the work — done: работа выполнена исполнителем в WIN-U4 и опубликована; направление применило её возврат к состоянию.
  - 4 self-check — done: три факта перепроверены по байтам в продуктовом чекауте, приёмка глазом честно оставлена неоплаченной.
  - 5 close — done: задача waiting, наряд done, следующий шаг волны — review; стенд стоит в очереди после него.

log: Равновесие хозяина опубликовано 2d2c27ff, приёмка глазом остаётся долгом; наряд стенда написан её возвратом и отложен в другой слот и другую волну его словом

next: |
  return-to-owner: волна 11 достроена по механикам — четыре опубликованы, ни одной
  открытой ноги, все слоты свободны. Остаётся его проба стенда мыши, снимающая
  первый долг приёмки; затем review волны, обязанный назвать оба долга поимённо.

END_OF_FILE: live/indie-game-development/history/2026-09-02-s-work-g-5a7c-balance-published-bench-ordered-001.md
