---
id: i-accepted-work-lives-only-in-a-released-slot-001
_kind: issue
_pos: 20
level: execution
route: work
---

## issue
Принятая владельцем работа существует в ОДНОМ экземпляре — локальная ветка `slot/win-u1` (`ae9ce7b1`, 5 коммитов), которой нет ни на сервере, ни в `main`, в слоте со статусом `AVAILABLE`. Обычная первая операция аренды «привести слот к базе» её сотрёт, а класс общий: любой слот, освобождённый до публикации, хоронит свою ногу.

## review_when
ЭТОТ носитель в безопасности окончательно: работа опубликована в `main` = `15ee4151` 2026-08-06; спасательная ветка `keep/householder-profile-2026-08-06` больше не несущая и может быть удалена его словом. КЛАСС ОТКРЫТ: правило «слот освобождается только после публикации либо сохранения» пока не стоит ни в одном тексте наряда. Закрывается, когда оно там появится.

## evidence
`git for-each-ref --contains ae9ce7b1` = только `refs/heads/slot/win-u1`; `origin/slot/win-u1` = `adae7d40`; `merge-base --is-ancestor ae9ce7b1 1703599b` = NO; `gascoop-slot-state.v1.json` — `WIN-U1` `AVAILABLE`, `lease: none`. Перемерено первой рукой 2026-08-06 — history/2026-08-06-s-work-g-1d84-householder-profile-return-checkpoint-001.md.

END_OF_FILE: live/indie-game-development/cards/i-accepted-work-lives-only-in-a-released-slot-001.md
