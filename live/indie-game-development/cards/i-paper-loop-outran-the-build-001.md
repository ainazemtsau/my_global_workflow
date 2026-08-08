---
id: i-paper-loop-outran-the-build-001
_kind: issue
_pos: 9
level: direction
route: maintenance
---

## issue
Рабочий процесс дал петлю без выхода — шесть ног, 89 строк, ноль строк игрового кода за две недели, и владелец остановил её сам. Петля остановлена маршрутом, но вопрос к самому OS остался: у heavy-триажа нет ни потолка кругов починки, ни правила «два круга подряд — узел режется, а не чинится».
## review_when
Отдельной сессией по `os/MAINTENANCE.md`, как только владелец её запустит; `live/**` она не трогает. Раньше — если любой следующий узел уйдёт на второй круг починки.
## evidence
history/2026-08-01-s-converge-verify-g-8f31-001.md и -002.md; work/converge-g-8f31.md §SIGNOFF; work/now-compaction-2026-08-05.md §3 (его слова 2026-08-01 дословно).
END_OF_FILE: live/indie-game-development/cards/i-paper-loop-outran-the-build-001.md
