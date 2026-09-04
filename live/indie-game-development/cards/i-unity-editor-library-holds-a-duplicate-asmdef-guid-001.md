---
id: i-unity-editor-library-holds-a-duplicate-asmdef-guid-001
_kind: issue
level: execution
route: work
found: 2026-08-30
slot: WIN-U2
_pos: 156
---

## issue
**РЕДАКТОР UNITY В СЛОТЕ WIN-U2 НЕ СТРОИТ ГРАФ СБОРОК.** `assets-refresh` валит серию
`ArgumentException` о дубликате guid `6f0a2d94…` из `AssemblyGraphBuilder`.

Guid принадлежит `TunnelCrew.Thread.EditorTests.asmdef.meta`, и **в репозитории он ровно один** —
дубликат живёт в кэше `Library` самого редактора, а не в дереве. То есть чинится сносом кэша
редактора этого слота, а не правкой файлов.

Найдено исполнителем ноги `c-exec-g-5a7c-priority-1-001` 2026-08-30, **не его работой**: вся её
правка в `Core/`, который собирает headless-проект, и на ногу это не повлияло (647 тестов зелёные).

**ПОЧЕМУ ЭТО УЛИКА, А НЕ ЗАМЕТКА.** Следующая нога, которой нужен прогон Unity в WIN-U2, упрётся
в это ПЕРВОЙ — до единой строки своей работы. А «Unity — первый гейт, а не последний» уже записано
как класс ошибки: headless-тесты слепы к сборкам редактора.
END_OF_FILE: live/indie-game-development/cards/i-unity-editor-library-holds-a-duplicate-asmdef-guid-001.md
