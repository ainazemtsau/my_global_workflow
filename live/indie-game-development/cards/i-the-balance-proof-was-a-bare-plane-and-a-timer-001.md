---
id: i-the-balance-proof-was-a-bare-plane-and-a-timer-001
_kind: issue
level: objective
route: review
status: open
evidence: history/2026-09-03-s-work-g-5a7c-the-fall-itself-is-broken-001.md
_pos: 236
---

## issue
**«РАВНОВЕСИЕ ОПУБЛИКОВАНО И ДОКАЗАНО ФИЗИКОЙ» — ЭТА ЗАПИСЬ ЛОЖНА В ТОМ ВИДЕ, В КОТОРОМ ЕЁ ЧИТАЛИ.
И ПОПРАВКА, КОТОРУЮ ВЫДВИНУЛА НОГА СТЕНДА, ТОЖЕ ЛОЖНА — В ДРУГУЮ СТОРОНУ.**

Перемерено направлением 2026-09-03 первой рукой на `slot/win-u4` = `8182c984`, после разбора
92 агентами, где семь из семи механизмов провала были опровергнуты, а это — выжило.

**ЧТО ГОВОРИЛА ЗАПИСЬ.** Наряд 02.09, улика `i-the-balance-acceptance-is-unpaid-and-its-order-is-written-001`,
раздел 2 плана и карточка ставки волны 12 несут одну формулировку: «механика равновесия опубликована
и **доказана физикой**: production-путь `CargoBody → PhysX → PuppetMaster → NetworkHouseholder`,
настоящий `Alarm Clock` 48 кг на 12 м/с, accepted impact `0,52` при `8,3°`, stock fall при `10,7°`,
deadline не продлевается, recovery завершается, прежнее дело возобновляется».

**ЧТО ГОВОРИЛА ПОПРАВКА НОГИ СТЕНДА (03.09):** «доказана она была В ДОМЕ: хозяин усажен, пол —
толстые коробки дома; на голом полигоне разваливается; режим доказательства был у́же, чем все
считали».

**ЧТО ЕСТЬ НА САМОМ ДЕЛЕ — ЧЕТЫРЕ ФАКТА, ПРОЧИТАННЫЕ НАПРАВЛЕНИЕМ ГЛАЗАМИ В ФАЙЛЕ.**
Все числа формулировки взяты из одного теста
`Assets/Tests/TunnelCrew/Networking/HouseholderBalancePhysicsTests.cs`, метод
`ARealProductionCargoImpactNamesItsCauseAndClosesOnTheOriginalDeadline`.

1. **СЦЕНЫ НЕ БЫЛО ВООБЩЕ.** Докблок теста, дословно: «**No scene is saved.** The future owner-eye
   lab is a separate task; this fixture creates only the minimum runtime world needed to ask the
   engine the mechanical question.»
2. **ПОЛ БЫЛ ПРИМИТИВОМ `Plane`, А НЕ КОРОБКАМИ ДОМА.** Строки 60-62:
   `floor = GameObject.CreatePrimitive(PrimitiveType.Plane); floor.name = "balance physics floor";
   floor.layer = 0;`
3. **ХОЗЯИН БЫЛ ГОЛЫМ `GameObject`.** Строка 64: `carrier = new GameObject("balance physics
   householder")` плюс один компонент `HouseholderBodyPresenter`, поле `_settings` через рефлексию.
4. **`NetworkHouseholder` НЕ ЖИЛ НИ СЕКУНДЫ.** Строки 112-114:
   `logOwner = new GameObject("balance production log owner"); logOwner.SetActive(false);
   var householder = logOwner.AddComponent<NetworkHouseholder>();` — и **`SetActive(true)` для
   `logOwner` в файле нет вовсе** (все четыре `SetActive` в файле: 65, 70, 113, 373; вторая пара —
   про `carrier`). Значит `Awake`/`Start` не выполнялись.

**ВЫВОД, КОТОРЫЙ МЕНЯЕТ ОБЕ ЗАПИСИ.** Режим доказательства был **не домом и не у́же полигона — он
и БЫЛ полигоном**: голая плоскость, голый объект, выключенный сетевой слой. Полигон 03.09 ничего не
сузил; он показал, что доказательство **никогда не покрывало то, за что его читали**.

**И «УСАЖЕННОСТЬ» К РАВНОВЕСИЮ ОТНОШЕНИЯ НЕ ИМЕЕТ — ЭТО НАПИСАНО В КОДЕ СЛОВАМИ.**
`Assets/TunnelCrew/Network/NetworkHouseholder.cs:215-218`: «He is never seated, so the judge never
moves him and he stands exactly where the scene put him. What he KEEPS is his body: **AdvanceBalance
runs whether or not he is seated**.»

**ЧТО ИМЕННО УТВЕРЖДАЕТ ТОТ ТЕСТ.** Строки лога и фазы. Проверки положения тела в файле нет ни
одной: единственные `position` — постановка груза перед броском (строка 302). **Теста, который
спрашивает, ГДЕ оказалось тело по высоте, в проекте нет ни одного** — ни в
`tests/TunnelCrew.Core.Tests/**`, ни в `Assets/Tests/**`.

**ТРИ СЛЕДСТВИЯ, КАЖДОЕ ПРОВЕРЕНО ОТДЕЛЬНО.**

**(1) ПОДЪЁМА НЕТ НИ В КАКОМ ВИДЕ, И ЭТО РЕШЕНИЕ, А НЕ НЕДОСМОТР.**
`Assets/TunnelCrew/Presentation/HouseholderBalanceBody.cs:104-106`, дословно: «The authored
controller has no get-up states. Recovery is therefore the bounded host phase below, not the
vendor's autonomous animation branch.» — и следом `_behaviour.canGetUp = false;`.
**Это закрывает вопрос Р3 возврата: значение выставлено намеренно и объяснено в коде.**

**(2) «ОН ВСТАЛ» — УТВЕРЖДЕНИЕ ТАЙМЕРА, А НЕ ТЕЛА.**
`Assets/TunnelCrew/Core/Householder/HouseholderBalance.cs:109-128`: когда `Recovering` истекает,
**обе ветки возвращают `Stable`** — `default` при `tilt < AttemptTiltDegrees` и
`new HouseholderBalanceState(Stable, 0f, true)` иначе. Единственное последствие всё ещё наклонённого
тела — флаг `NeedsRearm`. Тело в решении не участвует.

**(3) ПОРОГ ПАДЕНИЯ 35° ФИЗИКОЙ НЕ ПРОВЕРЯЛСЯ НИ РАЗУ.**
`_householderBalanceFallTiltDegrees: 35` лежит в `GameRulesSettings.asset:20-22`, но падение в
доказательстве пришло от вендорского `Unpinned` на `10,7°`, и текст лога эту разницу не показывает.
Теста, где `Fallen` наступает по авторскому порогу `35°` в настоящей физике, не найдено.

**ЧЕГО ЭТА УЛИКА НЕ ГОВОРИТ.** Она не говорит, что нога равновесия соврала: её отчёт сам пишет в
вырезах «не строился и не сохранялся `.unity`-стенд равновесия» и ставит ручную приёмку
`INCONCLUSIVE`. Соврала не нога — **соврал пересказ**: слова «доказано физикой» уехали в наряд,
в улику, в план и в ставку без режима, в котором они были истинны.

**ЧТО С ЭТИМ ДЕЛАТЬ — РЕШАЕТ `review` 11.09.** Формулировку несут четыре места: наряд
`work/2026-09-02-order-the-homeowner-balance-bench.md`, улика
`i-the-balance-acceptance-is-unpaid-and-its-order-is-written-001`, раздел 2 плана и блок `goal`
ставки `bet-g-5a7c-wave-12`. Ни одно из них эта нога не переписывает: подписанное остаётся
подписанным, поправка лежит здесь.
## журнал
2026-09-03 · стенд показал, что сломана сама механика падения, и разбор 92 агентами перевернул запись направления — «равновесие доказано физикой» ложно, но и поправка ноги («доказывалось в доме, усаженный, пол из коробок») тоже ложна: доказательство снималось вне какой-либо сцены, пол был примитивом Plane, хозяин голым GameObject, а NetworkHouseholder создан на выключенном объекте и никогда не включён — режим доказательства и БЫЛ полигоном; подъёма нет вовсе по объяснённому в коде решению, «встал» объявляет таймер, а не тело, и порог 35° физикой не проверялся ни разу; причину просадки направление назвать не может — семь гипотез выдвинуты и все семь опровергнуты, нужен живой замер, и постановка поправлена числом: тело просело на 30 см В пол, а не пробило его; слияние U4 разрешено с AllowBlockedReport · history/2026-09-03-s-work-g-5a7c-the-fall-itself-is-broken-001.md
END_OF_FILE: live/indie-game-development/cards/i-the-balance-proof-was-a-bare-plane-and-a-timer-001.md
