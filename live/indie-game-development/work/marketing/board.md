# Marketing question-graph — board (index)

Render surface for `local/marketing-status`. The live graph of the marketing track (`g-2f8c`). Markdown-first. Cards live in `questions/`; a frozen card stays in place with `status: frozen`. The PLAN is NOT here — it is derived inside the process, card by card. `marketing-status` computes actionable/blocked/parallel from each card's `depends_on` + open `cross_track`.

Legend — status: open | blocked | frozen. type: DECISION | ARTIFACT. A `cross_track` entry `{track, status}` blocks only while `status: open`.

| id | type | status | depends_on | cross_track (open) | one-line |
|---|---|---|---|---|---|
| q-foundation | DECISION | open | — | — | первая карточка: вывести нашу ситуацию / цели / путь внутри процесса; порождает остальные |
| q-studio-identity | DECISION | open | — | — | имя студии + один кросс-игровой ник |
| q-positioning-hook | DECISION | blocked | — | canon:g-d3a8 | хук / позиционирование — нужен мир из канона (пример кросс-трека) |

## Notes
- ▶️ actionable now: **q-foundation (первая)**, q-studio-identity.
- ⏳ blocked: q-positioning-hook (открытый canon-запрос).
- Дальнейшие карточки (каналы, артефакты, захват, деньги, каденс) рождает `q-foundation` — не заводим заранее.
- Движок `g-9c41` — приоритет; маркетинг — параллельная ёмкость.

END_OF_FILE: live/indie-game-development/work/marketing/board.md
