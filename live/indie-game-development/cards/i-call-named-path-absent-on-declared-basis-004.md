---
id: i-call-named-path-absent-on-declared-basis-004
kind: issue
pos: 6
level: execution
route: maintenance
---

## issue
Наряд объявляет базу и называет пути, которых на ней нет: сессия смотрит файлы в чужом рабочем каталоге, а «проверено первой рукой» не говорит ГДЕ. Четыре бунса; сюда же слит прежний `i-direction-to-product-call-contract-001` — тот же корень, наряд утверждает о венью факт, не сверенный с венью.

## review_when
MAINTENANCE отдельной сессией, когда владелец её запустит; `live/**` она не трогает. До неё каждый названный путь и слот/lease/HEAD сверяется командой на ОБЪЯВЛЕННОЙ базе перед выпуском наряда.

## evidence
history/2026-07-28-s-repair-g-37a1-exec-call-contract-001.md; history/2026-07-30-s-repair-g-37a1-simple-gas-call-base-fix-001.md; history/2026-07-30-s-repair-g-37a1-venue-replacement-preflight-correction-001.md; слияние двух записей — history/2026-08-05-s-day-g-1d84-issues-cleanup-001.md.

## two_more_cases_2026_08_06
ПЯТЫЙ И ШЕСТОЙ СЛУЧАИ, оба из текста `c-exec-g-1d84-named-house-routes-001`, оба по исходу безвредны и потому особенно показательны — исполнитель поймал их сам. (1) `context` назвал `West Doorway` и `East Doorway` «именованными дверными местами»; по байтам `ThreeRoomHouse.prefab` это ПРОХОДЫ (`HousePassageMarker`), а дверные МЕСТА зовутся `West Door Side` и `East Door Side`. Перемерено этой ногой. (2) `base` объявлен как `d647a58b8b64b7d516b583cfde38691109909139` — такого объекта в репозитории НЕТ (`git cat-file -t` → `fatal: could not get object info`, exit 128): короткий sha дополнен до сорока знаков вместо разрешения. Настоящий коммит — `d647a58b5f39c242e197f6b4d923a348752131fe`. Оба — ровно класс записи: наряд утверждает о венью факт, не сверенный с венью.

END_OF_FILE: live/indie-game-development/cards/i-call-named-path-absent-on-declared-basis-004.md
