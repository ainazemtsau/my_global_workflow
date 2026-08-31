---
id: i-a-living-day-breaks-a-promise-that-rested-on-emptiness-001
_kind: issue
level: execution
route: work
status: open
evidence: history/2026-08-31-s-work-g-5a7c-morning-finding-001.md
_pos: 170
---

## issue
**ЖИВОЙ ДЕНЬ ХОЗЯИНА ЛОМАЕТ ОБЕЩАНИЕ, КОТОРОЕ ДЕРЖАЛОСЬ НА ЕГО ПУСТОТЕ.**

Найдено ногой утра `c-exec-g-5a7c-morning-content-1-001` и перевыверено направлением в её кандидате.

**ОБЕЩАНИЕ.** Тест `EitherMomentAnswersTheFirstNoiseAndTheSecondStillTakesHim`, шапка дословно:
**«THE FIRST NOISE NO LONGER HAS TO BE A PROBE»** — раньше игрок тратил первый шум на то, чтобы
выяснить, в каком моменте хозяин; теперь оба момента дают один ответ. Утверждения: «one rustle and
he listens, **whenever it reaches him**» и «and the same **at any other moment of his day** — there
is no second answer for the owner to have to tell apart».

**ЧТО СЛОМАЛОСЬ.** Пока хозяин идёт, `Householder.cs:687` ставит `isSafeToInterrupt = false`, а
тихие реакции — `quiet-rustle` и `suspicious-noise`, единственные две с
`RequiresSafeInterruption = true` — до него не доходят. Пустой день не содержал ходьбы вовсе, и
обещание было истинно даром. Живое утро даёт ходьбу, и **на ходу первый шум снова становится
пробой.**

**ОБЕЩАНИЕ ВЕРНО ПО СУЩЕСТВУ, И ЭТО ВАЖНО.** Владелец 2026-08-31 постановил, что слышимость должна
решаться **расстоянием**, а «глух на ходу» — дефект. То есть половина «whenever it **reaches** him»
совпадает с его решением дословно, а ломается именно вторая — «момент не должен иметь значения».
**Тест красен по правильной причине и его нельзя переписывать:** переписать значит записать дефект
в приёмку и снять давление с волны про звук.

**ЦЕНА СНЯТИЯ ГЛУХОТЫ ЗАМЕРЕНА, И ОНА НЕ ОДНА СТРОКА.** Нога сняла флаг, померила и вернула:
**13 красных из 730**, четыре — прямо в честь удаляемого поведения
(`Step_BoardCreakDuringUnsafeMovement_DefersUntilSafeInterruption`,
`Step_QuietRustle_WaitsForSafeThenListensInPlaceAndReturns`,
`Step_RepeatedHeavyNoise_InterruptsUnsafeAndGuardsBeforeReturning`,
`SightReachesHimWhileHeIsStillWalkingHisRoute`). Значит **«отложить шум до безопасного момента» —
механизм с собственной приёмкой, а не флаг**, и снять его одной строкой нельзя.

**ЧЕГО ЭТА УЛИКА НЕ РЕШАЕТ.** Ложится ли утро в `main` до починки — вопрос владельцу: это игровой
размен, который он почувствует руками. Снимается волной про слышимость по расстоянию, которую он
сам назначил позднейшей (`idea-owner-hearing-is-decided-by-distance-001`).
END_OF_FILE: live/indie-game-development/cards/i-a-living-day-breaks-a-promise-that-rested-on-emptiness-001.md
