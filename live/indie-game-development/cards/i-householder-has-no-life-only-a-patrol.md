---
id: i-householder-has-no-life-only-a-patrol
_kind: issue
_pos: 125
---

## issue
**У ХОЗЯИНА НЕТ ЖИЗНИ. У НЕГО ЕСТЬ ПАТРУЛЬ И СИГНАЛИЗАЦИЯ.**

Замерено в `HouseholderVocabulary.cs` @ origin/main. Всё, что он умеет, — восемь занятий:
WalkRoute, InvestigateSuspiciousNoise, ListenForQuietRustle, GuardAgainstRepeatedHeavyNoise,
InvestigateLanding, PerformRoutineOccupation, InvestigateSeenRat, PeekForWhoIsHiding.

**Семь из восьми — реакции на мышей.** Единственное про его собственную жизнь —
PerformRoutineOccupation, и оно безымянное.

Новый концепт весь построен на наблюдении за его жизнью и на том, что в этой жизни есть
проговорка. Значит добавлять надо не реакции, а жизнь с тайной внутри.
## review_when
Перед нарезкой любой волны, которая трогает поведение хозяина. Размер и порядок работ описаны в
docs/engineering/householder-interaction-surfaces.md §6 продуктового репозитория.
END_OF_FILE: live/indie-game-development/cards/i-householder-has-no-life-only-a-patrol.md
