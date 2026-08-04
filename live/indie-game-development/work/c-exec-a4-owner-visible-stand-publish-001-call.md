# CALL — c-exec-a4-owner-visible-stand-publish-001

to: executor
kind: engineering
repo: ainazemtsau/GasCoopGame
engineering_contract: 36
mode: ПРОБА — режим по умолчанию контракта 36; ОПОРА здесь не включена.
basis: `8da649430e5d9b55baadefc23a01519380863216` — подтверждённые read-only remote
       `refs/heads/main` = `refs/heads/dev` 2026-08-04
direction: indie-game-development
node: g-6b13
task: a-4
track: переноска
issued: 2026-08-04 by s-work-g-6b13-a4-owner-visible-publish-checkpoint-001
status: ready

## goal

Опубликованные `main/dev` содержат именно проверенную владельцем версию стенда, где перегородка с
проёмом видна без скрытого поиска, при сохранённых переноске, столкновениях и текущей полосе хозяина.

## context

- Исходный продуктовый наряд и отчёт:
  `live/indie-game-development/work/c-exec-two-carry-one-physical-cargo-proba-001-call.md` и
  `docs/results/c-exec-two-carry-one-physical-cargo-proba-001.md`.
- Владелец сначала сообщил дословно: «Не было же приемов в сцене, что ты меня голову дуришь? Ну,
  сцена пустая была, приемов не было.» После появления перегородки в начальном кадре он запустил
  WIN-U3 и сказал: «Так, проверил в слоте 3, да, действительно есть балка, всё работает, как
  ожидается. Можем закрывать.»
- Проверенный им tip — `4f3cbc1cfe1bfab9cb211a311415459af0f41565`, единственный parent
  `dc5d48b059c0739dfc0524d46cc766e7b3912dca`. Он меняет только
  `Assets/TunnelCrew/Network/NetworkPlaySettings.asset` и
  `Assets/TunnelCrew/Scenes/NetworkWalkers.unity`.
- Owner-tested runtime-блобы: settings `f750868c2b8d423ef678b6aedc09f31c808aa952`; scene
  `4c7b224b98b0e98dff508a65eaec4fc9d721c05c`. Дельта делает camera minimum 9, cargo spawn Z 2.5,
  stand half-extent 7, divider Z 5 и согласует размер пола; это tuning/layout, не новая механика.
- Текущий опубликованный tip `8da64943` уже содержит параллельную полосу хозяина и является потомком
  `dc5d48b0`, но двух owner-tested runtime-блобов не содержит. Read-only `git ls-remote` дал
  `refs/heads/main` = `refs/heads/dev` = `8da64943`; поэтому Direction G5 не закрыла a-4.
- WIN-U3 прочитан как clean, без `Temp/UnityLockfile`; shared slot state: `AVAILABLE / lease none`,
  `mcp_endpoint: unrecorded`.

## boundaries

- Только публикация уже проверенного runtime-изменения и приведение его продуктового отчёта к
  фактическим размерам/координатам. Нового поведения, новой механики и нового тюнинга здесь нет.
- Не менять Core/Cargo, правило движения, курьер, сетевой протокол, первое лицо/a-4b, полосу хозяина,
  `Packages/**`, `ProjectSettings/**`, `tools/**`, `validation.config` или `AGENTS.md`.
- Не терять текущий опубликованный tip `8da64943` и его параллельные изменения. Owner-eye относится
  ровно к двум названным runtime-блобам; если их байты меняются, это новый непроверенный кандидат и
  terminal HOME обязан сказать об этом вместо заявления о готовности.
- Не закреплять tuning-числа новым тестом: контракт 36 прямо оставляет tuning вне frozen surface.
  Известное ограничение низкого FPS из исходного отчёта не чинить и не скрывать.

## done_when

1. `origin/main` и `origin/dev` указывают на один опубликованный tip поверх актуального basis; в нём
   runtime-блобы settings `f750868c…` и scene `4c7b224b…` сохранены побайтово, а текущая полоса
   хозяина не потеряна.
2. `docs/results/c-exec-two-carry-one-physical-cargo-proba-001.md` честно называет фактические
   размеры/координаты принятого стенда и дословные слова владельца; старые 24×24 / `z = 8` не
   выдаются за опубликованную фактическую сцену.
3. Focused tests, обычный repo check и scoped diff зелёные; terminal HOME называет exact commits,
   remote readback и `WIN-U3 CLEAN / AVAILABLE / lease none` либо один точный blocker.

## return

Terminal HOME/RESULT в `indie-game-development`, g-6b13 / a-4 / переноска: published commit(s),
два runtime blob SHA, правка отчёта, точные outputs проверок, scoped diff, remote readback и terminal
slot evidence. Product delivery сама по себе a-4 не закрывает: после HOME направление выпускает
новую fresh physical close-verification.

budget: one light PROBA root — публикация двух уже owner-tested runtime-блобов плюс честный report

END_OF_FILE: live/indie-game-development/work/c-exec-a4-owner-visible-stand-publish-001-call.md
