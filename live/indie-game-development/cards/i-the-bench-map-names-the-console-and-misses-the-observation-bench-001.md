---
id: i-the-bench-map-names-the-console-and-misses-the-observation-bench-001
_kind: issue
level: execution
route: work
status: open
evidence: history/2026-08-31-s-work-g-5a7c-owner-walked-the-bench-001.md
_pos: 176
---

## issue
**КАРТА ПОЛИГОНА НАЗЫВАЕТ КОНСОЛЬ И НЕ НАЗЫВАЕТ СТЕНД НАБЛЮДЕНИЯ — А ВЛАДЕЛЕЦ ПОЛЬЗУЕТСЯ СТЕНДОМ.**

Замерено 2026-08-31 после того, как владелец прошёл полигон сам. Его слова:

> «Не через консоль, через… у нас есть **окно**, да, которое там открывается, Householder. Там
> можно в коридоре шум, я сделал, **он побежал на него**… **Почему** там побежал? Поэтому в
> принципе работает.»

**ЧТО ЕСТЬ В ПРОДУКТЕ.** Целое меню `Tunnel Crew / Householder Observation` с восемью пунктами:
`Open the bench`, `Queue configured situation`, `Watch the house from above`,
`Frame householder from above`, `Step one tick`, `Take clock control`, `Copy the bench log`,
`Show Game view mirror`, `Save live chain PNG`. Плюс готовые ситуации файлами
(`HouseholderObservation.bedroom-rustle-then-drop.json`).

`HouseholderBenchView.cs:11` описывает смысл дословно: «**SOMETHING TO WATCH HIM WITH, because
until now there was nothing**» — стенд ставит ВТОРУЮ камеру поверх мышиной, потому что игровая
камера каждый кадр переписывается глазом мыши и наблюдателю достаётся изнанка стены.

**ЧЕГО НЕТ В КАРТЕ.** Поиск по `docs/householder-walking-bench-map.md` на `observation`, `bench`,
`Queue`, `situation`, «окно», «стенд» — **ни одного совпадения**. Карта описывает консольные
команды (`who`, `why`, `noise 5/20`) и молчит про стенд целиком.

**ПОЧЕМУ ЭТО ДЕФЕКТ КАРТЫ, А НЕ МЕЛОЧЬ.** Карта писалась ровно затем, чтобы владелец знал, чем
смотреть. Он нашёл лучший инструмент **сам и вопреки ей**: стенд даёт вид сверху, пошаговый такт,
контроль часов, готовые ситуации и журнал — всё то, ради чего он и просил «инструменты, чтобы не
бегать мышью». Консоль рядом с этим — узкая щель.

**ЧЕГО ЭТА УЛИКА НЕ РЕШАЕТ.** Полноту самого стенда: что в нём работает, а что нет, не проверялось
ни ногой, ни направлением. Снимается первой же ногой, трогающей карту.
## журнал
2026-08-31 · владелец прошёл полигон сам: сделал шум в коридоре, хозяин побежал на него, и было видно ПОЧЕМУ — восприятие, решение и объяснение сошлись в одном наблюдении; задача закрыта его словом, а он вдобавок нашёл стенд наблюдения, которого карта не называет вовсе · history/2026-08-31-s-work-g-5a7c-owner-walked-the-bench-001.md
END_OF_FILE: live/indie-game-development/cards/i-the-bench-map-names-the-console-and-misses-the-observation-bench-001.md
