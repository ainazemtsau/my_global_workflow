---
id: i-cargo-sinks-into-the-floor-when-the-householder-arrives-001
_kind: issue
level: product
route: work
status: open
evidence: history/2026-08-13-s-work-g-5a7c-handlers-1-close-001.md
_pos: 91
---

## issue
**Нашёл ОН, своим прогоном 2026-08-13, а не проверка.** Когда хозяин подбежал к грузу, груз
провалился в пол, и владельцу пришлось его вытаскивать. Записано исполнителем наряда
`c-exec-g-5a7c-handlers-1-001` в §Next 5 его возврата
(`docs/results/c-exec-g-5a7c-handlers-1-001.md` на `origin/main` `1307aa3e`) как наблюдение, не
воспроизведённое и не чинившееся.

К слою правил хозяина отношения не имеет: ни одна строка диффа наряда не трогает физику груза —
перемерено, `Core/Cargo/**`, `Network/Cargo*`, `Settings/GameRulesSettings.*` и все сцены с
префабами в диапазоне `27c98d14..1307aa3e` не тронуты вовсе.

Смежное и, возможно, то же самое: `i-cargo-passes-through-cargo-in-the-running-game-001` (код
берёт `GetComponent<Collider>` в единственном числе) и `i-cargo-low-fps-derived-velocity-gap-001`.

## review_when
Первая нога дорожки `house-and-things`, трогающая физику груза, — прежде всего продолжение
`t-loot-1`. Тогда воспроизвести: подбежавший хозяин рядом с лежащим грузом. Если не
воспроизводится — закрыть как не подтверждённое, а не держать открытым бесконечно.

## журнал
2026-08-13 · заведена закрывающей ногой наряда на обработчики с его прогона · history/2026-08-13-s-work-g-5a7c-handlers-1-close-001.md
END_OF_FILE: live/indie-game-development/cards/i-cargo-sinks-into-the-floor-when-the-householder-arrives-001.md
