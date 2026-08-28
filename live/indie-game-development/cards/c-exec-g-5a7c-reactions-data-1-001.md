---
id: c-exec-g-5a7c-reactions-data-1-001
_kind: call
_bet: bet-g-5a7c-wave-6
track: словарь
status: delivered
to: executor
for: t-reactions-data-1
play: work
issued: 2026-08-27
call: work/2026-08-27-call-reactions-data-1.md
repo: C:\projects\Unity\GasCoopGame_win-u1
description: Реакции хозяина переезжают из C# в профиль; двенадцатая заводится строкой
  текста
_pos: 140
---

## note
Владеет `HouseholderReaction.cs`, `HouseholderProfileLoader.cs` и профильным json.
НЕ трогает `Network/**`, `BodyReach.cs`, `Art/**` — там одновременно работают другие полосы.
Ловушка: `Weight` — делегат, а не значение; решить и записать, как строка профиля выбирает
уже существующий вычислитель веса.
## журнал
2026-08-28 · исполнитель доставил и опубликовал: origin/main == origin/dev на daeb3b4d. ПЕРЕМЕРЕНО ЭТОЙ НОГОЙ ПЕРВОЙ РУКОЙ, а не принято пересказом: секция reactions[] стоит в боевом профиле на main, реакция stand-over-the-spot названа только там, в продуктовом C# её имени нет ни разу (единственные три вхождения — тестовый файл), dotnet test на этой же голове дал 551 из 551 зелёными (цифра наряда 526 устарела). НЕ ПЕРЕМЕРЕНО и потому задача НЕ закрыта: строка 1 требует наблюдаемого прогона в запущенной игре, а прогон в редакторе делал сам исполнитель — по G5 это судит свежий чат, а не пересказ. Открыт биндинговый наряд на опровержение
2026-08-27 · выпущен при нарезке шестой волны, полосы стартуют одновременно · history/2026-08-27-s-shape-g-5a7c-wave-6-001.md

END_OF_FILE: live/indie-game-development/cards/c-exec-g-5a7c-reactions-data-1-001.md
