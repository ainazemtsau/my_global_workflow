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
## уточнение
**УТОЧНЕНИЕ 2026-08-30 ПОСЛЕ ВОЗРАЖЕНИЯ ИСПОЛНИТЕЛЯ: РЕШЕНИЕ ОТНОСИТСЯ К ДЕРЕВУ `slot/win-u3`,
А НЕ К `main`.** Формулировка «в `Probe/`» без указания дерева была двусмысленной, и это дефект
решения, а не исполнителя.

**НА `main` (`f6fc0918`)** папки границы нет: `Assets/TunnelCrew/Probe/` там — стенды `ReachLab` и
`ScaleTableau`, сборка `TunnelCrew.ReachLab` с `noEngineReferences: false` и ссылками на
`Presentation`/`Settings`. Класть туда engine-free ядро действительно нельзя, и исполнитель прав.

**НА `slot/win-u3` (`6579d5c0`)** — то есть в дереве, куда решение и адресовано, — перемерено
направлением:

- `TunnelCrew.Probe`: `noEngineReferences: **true**`, `references: ['TunnelCrew.Core']`. **Сборка
  engine-free.** Возражение «`Probe/` не место для engine-free логики» на этой ветке ложно.
- `Assets/TunnelCrew/Probe/Householder/AuthoritativeHouseholder.cs` существует: **хозяин УЖЕ живёт
  в `Probe/`**, все 76 файлов ядра там. Возражение «пять файлов остаются в `Core/`» ложно: в `Core/`
  ровно три файла.
- `core/TunnelCrew.Core.csproj` И `core/TunnelCrew.Probe.csproj` — **проекта два**, оба в headless.
  Возражение «вынос выбрасывает шесть файлов из headless» ложно.
- `Bench/ReachLab` — 13 файлов: стенды он перенёс сам, `Probe/` больше не стенды.

**ЗАМЕР «одна правка, 24 дня» ОТНОСИЛСЯ К ТРЁМ ПЕРЕНЕСЁННЫМ ФАЙЛАМ**, а не к папкам `Core/House`,
`Core/Situations`, `Core/Householder`. Про папки такого не утверждалось.

**«ГЕЙТА В `tools/` НЕТ» — ВЕРНО И ТАК ЗАДУМАНО.** Гейт — компилятор, а не скрипт: самописные
сканеры как улика у нас запрещены. Его же отрицательный контроль (`CS0246` на тип из того же
пространства имён) это и доказал.

**АЛЬТЕРНАТИВА `Core/Probe/` ОТКЛОНЕНА.** Подпапка внутри закреплённой сборки не запрещает ничего:
компилятор её не видит, остаётся соглашение об именах. Это ровно та замена механизма документом,
против которой нога и затевалась, — и он сам уже построил настоящую вещь.

**ЧТО ДЕЛАТЬ ТОЧНО:** шесть файлов с метами кладутся в `Assets/TunnelCrew/Probe/` по тем же
подпапкам, где они лежали под `Core/`: `Probe/House/HouseArrangement.cs`,
`Probe/Householder/HouseholderThingBelief*.cs`, `Probe/Householder/HouseholderThingReport.cs`,
`Probe/Householder/HouseholderWhereabouts.cs`, `Probe/Situations/IHouseholderThingSightSource.cs`.
END_OF_FILE: live/indie-game-development/cards/d-where-thing-belief-files-land-001.md
