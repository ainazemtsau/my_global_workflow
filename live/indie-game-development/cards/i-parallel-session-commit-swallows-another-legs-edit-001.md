---
id: i-parallel-session-commit-swallows-another-legs-edit-001
kind: issue
pos: 21
level: direction
route: maintenance
---

## issue
Параллельная сессия закоммитила `git add -A` НЕЗАКОНЧЕННУЮ правку `NOW.md` другой сессии, шедшей в тот же момент: правка уехала под чужим сообщением коммита, хотя то же сообщение отдельно утверждает, что чужие правки не тронуты. Содержимое уцелело случайно — при другом порядке правок это была бы наполовину применённая транзакция в общем горячем файле.

## review_when
MAINTENANCE отдельной сессией, когда владелец её запустит; `live/**` она не трогает. До неё каждая нога перед коммитом сверяет, что в индексе только её собственные пути.

## evidence
Коммит `5aac4232` (`s-map-g-1d84-tunnel-out-of-the-wave-001`) содержит поля `ready_because` и `preserve_done`, написанные `s-work-g-1d84-householder-profile-owner-verdict-001`; его же сообщение — «Правки параллельной сессии в work/ не тронуты и не закоммичены». Разбор — history/2026-08-06-s-work-g-1d84-householder-profile-owner-verdict-001.md.

END_OF_FILE: live/indie-game-development/cards/i-parallel-session-commit-swallows-another-legs-edit-001.md
