# Marketing question-graph — board (index)

Render surface for `local/marketing-status`. The live graph of the marketing track (`g-2f8c`). Markdown-first. Cards live in `questions/`; a frozen card stays in place with `status: frozen`. The PLAN is NOT here — it is derived inside the process, card by card. `marketing-status` computes actionable/blocked/parallel from each card's `depends_on` + open `cross_track`.

Legend — status: open | blocked | frozen. type: DECISION | ARTIFACT. A `cross_track` entry `{track, status}` blocks only while `status: open`.

| id | type | status | depends_on | cross_track (open) | one-line |
|---|---|---|---|---|---|
| q-foundation | DECISION | frozen | — | — | ✅ ситуация/цели/путь выведены; ось «мы никто»; гибкая AI-политика; породил 6 детей |
| q-studio-identity | DECISION | frozen | — | — | ✅ **INOMAND**; единый хэндл `@inomandgames`; `inomand.com` куплен; название игры отдельно и пока не выбрано |
| q-positioning-hook | DECISION | blocked | — | canon:g-d3a8 | хук / позиционирование — нужен мир из канона |
| q-ai-pipeline | DECISION | open | q-foundation | — | AI-конвейер картинок+голоса + проверка на скептиках + решение по капсуле |
| q-capture-setup | ARTIFACT | open | q-foundation, q-studio-identity | — | домен+входящая accounts@ готовы; захватить `@inomandgames`; Steam App ждёт отдельного названия игры |
| q-channels | DECISION | open | q-foundation | — | B1 checkpoint: Incident Pulse → Creator Crew; Shorts/devlog только производные; ждёт завершения карточки/owner-freeze |
| q-money-path | DECISION | open | q-foundation | — | клирер $1k к 11.12: itch/Ko-fi или credible-potential |
| q-cadence | DECISION | blocked | q-foundation, q-channels | — | ритм «когда есть что показать» + kill-критерий; ждёт каналы |
| q-marketing-assets-repo | DECISION | blocked | q-ai-pipeline | — | отдельный репо под ассеты — когда появятся ассеты |

## Notes
- ▶️ actionable now: **q-ai-pipeline** (капсула/конвейер — гейтит капсулу→страницу), **q-capture-setup** (резервация `@inomandgames`; Steam App ждёт названия игры), q-channels, q-money-path.
- ⏳ blocked: q-cadence (q-channels), q-marketing-assets-repo (q-ai-pipeline), q-positioning-hook (canon:g-d3a8).
- 🔀 parallelizable: q-ai-pipeline ∥ q-capture-setup ∥ q-channels ∥ q-money-path.
- Рекомендация checkpoint: продолжить `c-marketing-wake-001` по handoff-файлу; публичное продвижение ждёт реального capture, а сейчас параллельно закрываются substrate, q-money-path и проектирование автономного контура/AI pipeline.
- Движок `g-9c41` — приоритет; маркетинг заполняет параллельную ёмкость неравномерно.
- ⚠ 3 правки дерева owner-approved, ждут tree-edit-сессии (R1 охват / R3 AI-политика / R5 не-гейтить-на-Wave-2).

END_OF_FILE: live/indie-game-development/work/marketing/board.md
