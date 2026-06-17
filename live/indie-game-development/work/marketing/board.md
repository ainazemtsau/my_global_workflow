# Marketing question-graph — board (index)

Render surface for `local/marketing-status`. The live graph of the marketing track (`g-2f8c`). Markdown-first. Cards live in `questions/`; a frozen card stays in place with `status: frozen`. The PLAN is NOT here — it is derived inside the process, card by card. `marketing-status` computes actionable/blocked/parallel from each card's `depends_on` + open `cross_track`.

Legend — status: open | blocked | frozen. type: DECISION | ARTIFACT. A `cross_track` entry `{track, status}` blocks only while `status: open`.

| id | type | status | depends_on | cross_track (open) | one-line |
|---|---|---|---|---|---|
| q-foundation | DECISION | frozen | — | — | ✅ ситуация/цели/путь выведены; ось «мы никто»; гибкая AI-политика; породил 6 детей |
| q-studio-identity | DECISION | open | — | — | имя студии + один кросс-игровой ник |
| q-positioning-hook | DECISION | blocked | — | canon:g-d3a8 | хук / позиционирование — нужен мир из канона |
| q-ai-pipeline | DECISION | open | q-foundation | — | AI-конвейер картинок+голоса + проверка на скептиках + решение по капсуле |
| q-capture-setup | ARTIFACT | blocked | q-foundation, q-studio-identity | — | поднять страницу + рассылку + хэндл (сейчас); ждёт имя |
| q-channels | DECISION | open | q-foundation | — | сабреддиты + список мелких стримеров (одалживаем аудиторию) |
| q-money-path | DECISION | open | q-foundation | — | клирер $1k к 11.12: itch/Ko-fi или credible-potential |
| q-cadence | DECISION | blocked | q-foundation, q-channels | — | ритм «когда есть что показать» + kill-критерий; ждёт каналы |
| q-marketing-assets-repo | DECISION | blocked | q-ai-pipeline | — | отдельный репо под ассеты — когда появятся ассеты |

## Notes
- ▶️ actionable now: **q-studio-identity** (разблокирует capture-setup — «поднять сейчас»), **q-ai-pipeline** (капсула/конвейер), q-channels, q-money-path.
- ⏳ blocked: q-capture-setup (q-studio-identity), q-cadence (q-channels), q-marketing-assets-repo (q-ai-pipeline), q-positioning-hook (canon:g-d3a8).
- 🔀 parallelizable: q-studio-identity ∥ q-ai-pipeline ∥ q-channels ∥ q-money-path.
- Рекомендация: следующий — **q-studio-identity** (имя+ник нужны для страницы/капсулы/хэндла), параллельно q-ai-pipeline.
- Движок `g-9c41` — приоритет; маркетинг заполняет параллельную ёмкость неравномерно.
- ⚠ 3 правки дерева owner-approved, ждут tree-edit-сессии (R1 охват / R3 AI-политика / R5 не-гейтить-на-Wave-2).

END_OF_FILE: live/indie-game-development/work/marketing/board.md
