---
id: i-verification-guards-unwired-not-deleted-001
_kind: issue
_pos: 8
level: execution
route: work
---

## issue
Пять сторожей (negative-control, derivation-marking, closing-control, evidence-input, implementation-root) НЕ удалены, но `check.ps1` их больше не вызывает. Решено 2026-08-03 не возвращать сейчас; сегодня их место занимают две независимые read-only вычитки каждый раз.
## review_when
Первая задача в режиме ОПОРА либо первый случай, когда зелёный прогон скрыл настоящий дефект — тогда `negative-control-check` подключается ТОЛЬКО на новую папку и отдельным решением. Остальные четверо — по мере появления своих артефактов.
## evidence
Коммит `1f016999`; `tools/negative-control-check.ps1:1-6`; `tools/check.ps1`; work/now-compaction-2026-08-05.md §3 (полный разбор решения 2026-08-03).
## журнал
2026-08-02 · вырез контура перепроверен, найден долг и красный Deliver · history/2026-08-02-s-work-g-6b13-c1-gate-cut-verified-001.md
END_OF_FILE: live/indie-game-development/cards/i-verification-guards-unwired-not-deleted-001.md
