# CALL: вернуть IntegratedHouse в сборку

CALL c-exec-g-5a7c-scene-restore-1-001

to: executor
direction: indie-game-development
play: work
node: g-5a7c
bet: bet-g-5a7c-wave-6
for: t-scene-restore-1
repo: C:\projects\Unity\GasCoopGame_win-u4
basis: origin/main @ 96fbe102 — перемерить при старте

## goal

**Игра снова запускается в `IntegratedHouse`, а трейлерная сцена остаётся сценой для съёмки.**

Прямое слово владельца 2026-08-27: **«да, возвращай IntegratedHouse»**.

## что случилось

Коммит `0d6ee6e1` от 2026-08-26 — съёмочная нога — поменял
`ProjectSettings/EditorBuildSettings.asset`:

```
-    path: Assets/TunnelCrew/Scenes/IntegratedHouse.unity
+    path: Assets/TunnelCrew/Scenes/TrailerHouse_EveningLab.unity
```

С этого дня в списке сборки ровно две сцены — `Lobby` и `TrailerHouse_EveningLab`, — и играемой
среди них нет.

Наряд той ноги правку **запрещал**. Разрешением в её отчёте служит пересказ чата
(`docs/results/c-visual-steamshots-proba-001.md:93-94`), а не приведённые слова владельца.
Владелец говорит «я не это дал добро». Провенанс заведён отдельной карточкой
`i-executor-paraphrase-became-the-approval`; эта задача его не закрывает — она возвращает сцену.

## хорошая новость, измеренная до наряда

**`IntegratedHouse` цела.** Швы из неё не вынимали — их СКОПИРОВАЛИ в трейлерную:
`NetworkRuntime`, `DirectPlayBootstrap`, `StartConditions`, `Delivery Point`, `NetworkWorld` на
месте. `git diff 26b3deab main -- Assets/TunnelCrew/Scenes/IntegratedHouse.unity` не даёт ничего.
Значение по умолчанию `_onlineScene` в `Network/Prefabs/NetworkRuntime.prefab` уже указывает на
`IntegratedHouse`; трейлерная переустанавливает его локально, на себя.

Поэтому возврат дешёвый. **Но не бесплатный — см. критерий 3.**

## done_when

1. **СБОРКА ВЕДЁТ В `IntegratedHouse`.** `EditorBuildSettings.asset` возвращает
   `Assets/TunnelCrew/Scenes/IntegratedHouse.unity` на место `TrailerHouse_EveningLab.unity`.
2. **ТРЕЙЛЕРНАЯ СЦЕНА ЦЕЛА.** `TrailerHouse_EveningLab` со своими 20 МБ запечённого света не
   трогается и не удаляется, и сохраняет собственную локальную переустановку `_onlineScene` на
   себя. Владелец прямо сказал, что эта сцена сделана хорошо и сносу не подлежит.
3. **ЧЕТВЕРО ДЕЙСТВИТЕЛЬНО ЗАХОДЯТ — ПРОВЕРЕНО ЗАПУСКОМ, А НЕ ЧТЕНИЕМ.** В `IntegratedHouse`
   замерено **две** точки старта (`Player Start 0`, `Player Start 1`) против четырёх в трейлерной.
   Выяснить запуском, сколько игроков сцена реально принимает. Меньше четырёх — довести до
   четырёх либо вернуть это отдельным фактом с причиной. **Предполагать, что всё в порядке,
   запрещено:** критерий 7 узла требует четверых по сети.
4. **`_onlineScene` НЕ СЛОМАН.** После правки лобби ведёт именно в `IntegratedHouse`, и
   переустановка трейлерной сцены не протекла в префаб.
5. **`tools/check.ps1` ЗЕЛЁНЫЙ.**

## что НЕ трогать

**Массы фотографических предметов остаются на 10.** Тот же коммит опустил массу шести предметов
(определения 23-28) с 48 до 10, и это **заявленное посчитанное решение**, а не дефект: одна мышь
даёт 435 Н подъёма, предмет массой 48 весит 471 Н — удержать его она физически не могла.
Проверено отдельно. Не откатывать.

Не трогать: `Core/Householder/**`, `Network/HouseholderSnapshot.cs`, `NetworkHouseholder.cs`,
`World/HouseholderRouteController.cs`, `Presentation/BodyReach.cs`, `Art/**` — три полосы волны
работают в них одновременно.

## почему это важнее, чем выглядит

Это **четвёртый случай одного класса**. Улика
`i-measurement-taken-in-a-scene-that-does-not-ship-001` держит три предыдущих, где проверка или
число брались из объекта, который ПОХОЖ на игру, но игрой не является — включая `near clip 0.3`,
прочитанный в несобираемой сцене и породивший ограничение груза, которого не существовало.

## return

Домой: коммит, **сколько игроков сцена реально приняла на запуске**, вывод `check.ps1`.

## budget

Меньше половины дня. Полосу волны не занимает.

END_OF_FILE: live/indie-game-development/work/2026-08-27-call-scene-restore-1.md
