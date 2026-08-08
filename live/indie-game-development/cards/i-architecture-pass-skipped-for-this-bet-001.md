---
id: i-architecture-pass-skipped-for-this-bet-001
_kind: issue
_pos: 7
level: execution
route: converge-arch
---

## issue
Для g-6b13 архитектурный разбор был пропущен триажем; для g-1d84 он исполнен полным плеем, но с первого раза НЕ выдержал — свежая `converge-verify` вернула complete=FAIL smuggling=FAIL, и пять строк, объявленных закрытыми решением ноги, понижены до open. Запись живёт ради одного правила вперёд: полный архитектурный плей не заменяет свежую проверку, а ТРЕБУЕТ её.
## review_when
Перед первой задачей любой полосы, которая пишет код в новом слое: разбор идёт до неё, а его результат едет уликой в `context` наряда, а не в `done_when`. Закрывается, когда правило станет привычкой.
## evidence
work/converge-g-1d84-arch.md; history/2026-08-04-s-converge-verify-g-1d84-002.md; os/plays/converge-arch.md; work/now-compaction-2026-08-05.md §3 (четыре слоя прежних текстов, ни один не удалён).
END_OF_FILE: live/indie-game-development/cards/i-architecture-pass-skipped-for-this-bet-001.md
