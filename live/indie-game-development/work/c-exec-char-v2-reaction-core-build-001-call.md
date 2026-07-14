# CALL — c-exec-char-v2-reaction-core-build-001

- id: c-exec-char-v2-reaction-core-build-001
- to: executor (GasCoopGame BUILD session; BUILD Opus/Claude Code, VALIDATE Codex read-only cross-family)
- for: g-6d4e «Игровые персонажи» / В2 — Leg 1: headless-ядро реакции + knockdown-aware источник
- issued: 2026-07-14 by s-plan-characters-v2-freeze-001
- kind: engineering · project: GasCoopGame · node: g-6d4e

## goal (outcome, not method)

За В1-сокетом появляется ДЕТЕРМИНИРОВАННОЕ, headless-проверяемое ядро реакции: тело можно «сбить»
(knockdown) и «поднять» (get-up) через объявленные в В1 хуки, причём пока тело не Normal — авторитетная поза
НЕ двигается вводом, а на вставании авторитетная поза переселяется в точку покоя. Сейм-типы неизменны, так что
Leg 2 (риг + косметический рэгдолл) и позже ядро g-9c41 подключаются без правки контракта.

## context

- Frozen PLAN + В2 spec (AUTHORITY — ПРОЧТИ ЭТОТ ФАЙЛ; абсолютный путь на этой машине; НЕ строить из CALL одного):
  C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\c-plan-characters-002-plan.md
  (особенно §0 F1 knockdown-контракт, §3 гейтинг v21, §4 Leg 1, §6 riskiest assumption).
- В1 сейм, который РАСШИРЯЕМ, но НЕ меняем по типам (worktree C:\projects\Unity\GasCoopGame_p2a0_002@db69aba6,
  ветка c-exec-char-v1-socket-dropin-build-001): Assets/GasCoopGame/Characters/{IAuthoritativeBodyState, BodyPose,
  BodyReactions(IBodyReactions/NullBodyReactions/BodyReactionState/BodyImpulse), PlayerBodySocket}.cs;
  Adapters/Characters/{PlayerBodyView(SetReactions/Knockdown/GetUp хуки уже проброшены), InputBodyStateSource}.cs;
  tests/GasCoopGame.Core.Tests/Characters/*. Читай их first-hand.
- Проектные правила: independent test-author пишет RED из spec ДО билда, builder не редактирует
  (project-builder-stage-quality-fix); локальная валидация = headless .NET гейты, CI нет
  (gascoopgame-local-validation-no-ci); VALIDATE Codex cross-family read-only (не авторитет; binding = гейты +
  evidence + свежий G5 в ОТДЕЛЬНОЙ сессии). Контур: os/engineering/CONTOUR.md + VALIDATION.md (v21 Plan-to-RED).

## boundaries (out of scope / do not touch)

- НЕ строить в этой ноге: риг/модель/скин, рэгдолл/PuppetMaster, процедурную локомоцию, префаб-визуал, материалы
  (magenta — Leg 2). НЕ трогать физику/ядро/грид/сеть/газ. Никакого merge в main.
- Сейм-ТИПЫ IAuthoritativeBodyState / PlayerBodySocket / BodyPose — БАЙТ-ИДЕНТИЧНЫ (обёртка — новый источник ЗА
  сокетом, не правка сокета). Если понадобилось менять сейм-тип — STOP + ESCALATE владельцу, это не тихое решение.
- Реакция триггерится АБСТРАКТНЫМ токеном (BodyImpulse), НЕ газом и НЕ уроном (Sc-damage HELD).
- Worktree: ПЕРЕИСПОЛЬЗОВАТЬ disposable C:\projects\Unity\GasCoopGame_p2a0_002 (там В1-ветка + импортированный
  Library + PuppetMaster локально); завести ветку Leg 1 от В1 tip (или origin/main — билдер решает) прямо в нём;
  НЕ плодить новый worktree; НЕ трогать GasCoopGame_dev / GasCoopGame_core (foreign uncommitted).
- Открывающий v20→v21 re-sync — ТОЛЬКО текст контракта (root AGENTS.md + OpenSpec guidance + validation.config
  bump 20→21); НИ строки product source/tests/gate-scripts; идемпотентно (уже 21 → пропустить); никакого нового
  скрипта/парсера/conformance-инструмента.
- Unity MCP/Editor не нужен этой ноге (всё headless); если понадобится и недоступен → STOP + сказать владельцу.

## done_when (verifiable)

1. **v20→v21 re-sync** выполнен как первый шаг (или зафиксировано «уже 21, пропущено»): validation.config
   `synced_contract_version:21`, клауза Plan-to-RED отражена в root run-contract + OpenSpec guidance; product
   source/tests/gate-scripts не тронуты; никакого нового конформанс-скрипта.
2. **Independent test-author RED** (EditMode/headless, ДО билда, builder не редактирует) существует и краснеет на:
   (a) state machine Normal→Knockdown→GettingUp→Normal по BodyImpulse-токену; (b) инвариант «одно активное
   состояние»; (c) детерминизм при (event, time); (d) неизвестный/нулевой токен = no-op (negative-control);
   (e) knockdown-aware обёртка: при State≠Normal вход НЕ двигает авторитетную позу; (f) GetUp(restPose) ⇒
   авторитетная поза == restPose (reconcile = авторитет ← rest); (g) сейм байт-идентичность: обёртка реализует
   СУЩЕСТВУЮЩИЙ IAuthoritativeBodyState, старые Characters-тесты зелёные без правок. После билда — GREEN.
3. **Pre-freeze RED-ревьюер** (свежий read-only) вывел полный obligation-set из финального spec и написал по
   скелету на каждую headless-строку; вернул ПОЛНЫЙ gap-list; любое изменение spec → полный перепрогон.
4. Настоящая реализация: `IBodyReactions`-драйвер (state machine) + knockdown-aware `IAuthoritativeBodyState`
   обёртка, engine-free; ставится через PlayerBodyView.SetReactions + обёртка биндится в сокет. NullBodyReactions
   остаётся дефолтом (В2 driver — опциональная установка).
5. Локальные headless .NET гейты GREEN; один cross-family (Codex) G4 read-only ревью записан
   (docs/reviews/review-<id>.md, все находки dispositioned); ветка НЕ на main; чужие worktree/main не тронуты.
6. Сейм-типы байт-идентичны (git diff по трём сейм-файлам пуст).

## return

RESULT HOME (в направление, НЕ в product): reviewed, gate-green Leg 1 с base/branch/commit, v20→v21 diff/stamp,
obligation-инвентарь + RED-скелеты + gap-list-раунды, cross-family G4-ссылка, доказательство неизменности
сейм-типов, статус NOT MERGED. next = НАПРАВЛЕНИЕ выпускает связывающий свежий G5 (отдельная сессия, cross-family
предпочтительно на Unity-adapter/логику) — только его CONFIRMED закрывает Leg 1 и разблокирует Leg 2
(c-exec-char-v2-body-rig-ragdoll-build-001, сейчас HELD). Builder НЕ авторит следующий CALL и НЕ мёржит.

## budget

Одна сфокусированная BUILD-нога (маленькая — engine-free state machine + обёртка, ноль арта).

END_OF_FILE: live/indie-game-development/work/c-exec-char-v2-reaction-core-build-001-call.md
