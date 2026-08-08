---
id: i-house-fixture-not-bound-to-the-prefab-001
_kind: issue
_pos: 27
level: execution
route: work
---

## issue
Двадцать два самых сильных теста ходят по РУКОПИСНОЙ копии дома, а не по заготовке: `tests/TunnelCrew.Core.Tests/TestHouse.cs:93-142` держит три комнаты, семь мест и два прохода литералами, и файл сам предупреждает, что при сдвиге маркера в сцене тесты продолжат доказывать то, что доказывали всегда. Связи заготовка→фикстура нет ни в коде, ни в воротах. Отдельно: предикат пересечения проверяет только две ВНУТРЕННИЕ перегородки (`PartitionX = 2.5`), наружные стены не покрыты вовсе.

## review_when
В узле, который заново собирает дом: фикстура разойдётся с заготовкой в первый же день. Дешёвая форма — выгрузить план дома в текстовый файл уже существующей кнопкой редактора и читать его в тестах.

## evidence
history/2026-08-07-s-review-g-1d84-integrated-house-partial-001.md §evidence; `352f96b0:tests/TunnelCrew.Core.Tests/TestHouse.cs:83-91,93-142,158-181`.

END_OF_FILE: live/indie-game-development/cards/i-house-fixture-not-bound-to-the-prefab-001.md
