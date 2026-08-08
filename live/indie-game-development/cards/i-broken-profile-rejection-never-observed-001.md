---
id: i-broken-profile-rejection-never-observed-001
_kind: issue
_pos: 22
level: execution
route: work
---

## issue
Отказ хозяина запускаться на сломанном профиле — единственная строка `done_when` `t-host-3`, за которой не стоит НИ теста, НИ живого наблюдения: у `HouseholderProfileLoader.cs` ноль тестов, в `HouseholderProfileTests.cs` четыре теста и ни один про сломанный файл, владелец файл не ломал. Задача закрыта его явным выбором «в» после того, как ему это назвали прямо.

## review_when
При первом будущем задании, которое действительно открывает загрузчик профиля, либо при первом кривом профиле от ассистента. Закрывается тестом на неизвестное имя поля, называющим путь и позицию, либо собственным прогоном владельца.

## evidence
`15ee4151`: `git grep -l HouseholderProfileLoader` = только сам файл и `NetworkHouseholder.cs`; поиск по `tests/` на `MissingMember|cannot start|unknown ability|unknown place` пуст; `docs/results/c-exec-g-1d84-householder-profile-file-001.md` §Evidence сам называет отказ от тестового сборника осознанным. Разбор и его выбор — history/2026-08-06-s-work-g-1d84-householder-profile-close-001.md.

## журнал
2026-08-07 · доставленная пара закрыта, open_calls пуст, сирота снята · history/2026-08-07-s-work-g-1d84-delivered-pair-close-001.md
2026-08-07 · сведены две параллельные сессии 2026-08-06 по t-host-3 · 8441787d
2026-08-06 · закрыта светло на main = 15ee4151; пятая строка закрыта его решением, а не уликой · history/2026-08-06-s-work-g-1d84-householder-profile-close-001.md

END_OF_FILE: live/indie-game-development/cards/i-broken-profile-rejection-never-observed-001.md
