---
id: c-exec-g-5a7c-reactions-data-1-001
_kind: call
_bet: bet-g-5a7c-wave-6
track: словарь
status: ready
to: executor
for: t-reactions-data-1
play: work
issued: 2026-08-27
call: work/2026-08-27-call-reactions-data-1.md
repo: C:\projects\Unity\GasCoopGame_win-u1
description: Реакции хозяина переезжают из C# в профиль; двенадцатая заводится строкой текста
_pos: 140
---

## note
Владеет `HouseholderReaction.cs`, `HouseholderProfileLoader.cs` и профильным json.
НЕ трогает `Network/**`, `BodyReach.cs`, `Art/**` — там одновременно работают другие полосы.
Ловушка: `Weight` — делегат, а не значение; решить и записать, как строка профиля выбирает
уже существующий вычислитель веса.
## журнал
2026-08-27 · выпущен при нарезке шестой волны, полосы стартуют одновременно · history/2026-08-27-s-shape-g-5a7c-wave-6-001.md

END_OF_FILE: live/indie-game-development/cards/c-exec-g-5a7c-reactions-data-1-001.md
