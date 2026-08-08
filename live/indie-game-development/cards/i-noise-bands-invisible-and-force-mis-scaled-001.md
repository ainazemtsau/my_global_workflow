---
id: i-noise-bands-invisible-and-force-mis-scaled-001
_kind: issue
_pos: 28
level: execution
route: work
---

## issue
У шума три полосы с РАЗНЫМ поведением (тихая — стоять и слушать на месте; стук — идти к месту шагом 1.75; тяжёлая — бежать 3.25 и караулить 1.5 с), но в СОБРАННОЙ игре не видно, какая сработала: занятие доходит только до редакторского инспектора. Слова владельца «он прибегает» доказывают, что сработала какая-то, и никогда — какая; верхняя полоса (400) не наблюдалась никем. Хуже: само число силы посчитано не в тех единицах, в которых настраивались пороги — `Network/CargoBodyContact.cs:58` делит импульс на `Time.fixedDeltaTime` (0.02), а судья симулирует шагами ≈0.0167, и число поедет при смене частоты тика.
## review_when
В первой волне, где у реакции появляется видимая или слышимая обратная связь, ЛИБО когда пороги впервые крутят под настоящую обстановку: единицы чинятся одной строкой, а полосы становятся различимы даром.
## evidence
history/2026-08-07-s-review-g-1d84-integrated-house-partial-001.md §evidence; `352f96b0:Assets/TunnelCrew/Core/Cargo/CargoNoise.cs:96-108`, `Core/Householder/Householder.cs:430-479`, `Network/NetworkPlaySettings.asset:56-58`, `Network/CargoBodyContact.cs:52-65`.
END_OF_FILE: live/indie-game-development/cards/i-noise-bands-invisible-and-force-mis-scaled-001.md
