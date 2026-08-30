---
id: d-where-thing-belief-files-land-001
_kind: decision
about: t-bedrock-boundary-1
decided_by: направление
decided: 2026-08-30
_pos: 157
---

## decision
**ВСЕ ШЕСТЬ НОВЫХ ФАЙЛА ОТ `c-exec-g-5a7c-thing-belief-1-001` КЛАДУТСЯ В `Probe/`.**
Включая `Core/House/HouseArrangement.cs`, который не конфликтует и уехал бы в закреплённое молча.

Файлы: `HouseArrangement.cs`, `HouseholderThingBeliefDecisionHandler.cs`, `HouseholderThingBeliefs.cs`,
`HouseholderThingReport.cs`, `HouseholderWhereabouts.cs`, `IHouseholderThingSightSource.cs` — вместе
с их `.meta`. Пять изменённых файлов в `Householder/` вопроса не создают: папка целиком в пробе.

**ПОЧЕМУ, И ЭТО НЕ ВКУСОВЩИНА.** Три файла попали в закреплённое по ИЗМЕРЕННОМУ признаку: по одной
правке за всю историю, не тронуты 24 дня. Файлу, рождённому пробной ногой, — один день. Он не
проходит гейт по возрасту, и то, что он собрался бы в закреплённой сборке безупречно, ничего не
значит: см. `knowledge/compiling-alone-is-not-being-ready.md`.

**ПРАВИЛО, ЧТОБЫ ЭТО НЕ ПОВТОРИЛОСЬ:** в закреплённую сборку файл попадает ТОЛЬКО через сознательную
ногу переноса. Никогда слиянием, никогда разрешением конфликта, никогда потому, что «git так
предложил».

Исполнитель поступил ровно правильно, остановившись: наряд предписывал СТОП, и молчаливый переезд
`HouseArrangement` — именно тот класс, ради которого стоп и написан.
END_OF_FILE: live/indie-game-development/cards/d-where-thing-belief-files-land-001.md
