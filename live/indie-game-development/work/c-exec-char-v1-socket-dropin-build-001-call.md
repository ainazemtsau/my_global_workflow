# CALL — c-exec-char-v1-socket-dropin-build-001

- id: c-exec-char-v1-socket-dropin-build-001
- to: executor (GasCoopGame_dev BUILD session; BUILD Opus/Claude Code, VALIDATE Codex read-only)
- for: g-6d4e «Игровые персонажи» / В1 — socket + drop-in controllable capsule
- issued: 2026-07-13 by s-plan-characters-v1-freeze-001

## goal (outcome, not method)

Любая сцена может перетащить к себе один переиспользуемый player-префаб и получить управляемого игрока,
чья авторитетная поза приходит через СТАБИЛЬНЫЙ сменный источник — так что позже настоящая позиция ядра
g-9c41 подставляется в тот же разъём без правки префаба или сцен.

## context

- Frozen PLAN + В1 spec (authority): work/c-plan-characters-001-plan.md.
- P2a0 verdict (Кандидат A — ядро владеет авторитетной позицией, PuppetMaster-рэгдолл косметичен), single
  source: GasCoopGame origin/main@0e9eed02 docs/results/c-exec-player-puppetmaster-p2a0-lean-spike-build-001.md.
- Seam-прецедент: g-7e15 R13/R14 (READ-ONLY вид над заглушкой → свап на реальное без правки потребителя).
- Проектные правила: independent test-author пишет RED из spec ДО билда (project-builder-stage-quality-fix);
  локальная валидация = headless .NET гейты + owner-run PlayMode, CI нет (gascoopgame-local-validation-no-ci);
  owner-run Unity шаг = реальный гейт, не самоотметка (feedback-owner-run-unity-steps-real-gate).

## boundaries (out of scope / do not touch)

- НЕ строить: риг/модель/рэгдолл, реакцию/вставание (только no-op хуки), физику/ядро/грид-баллистику,
  сеть, газ. Никакого merge в main до owner-eye GREEN.
- Свежая GasCoopGame_dev сессия на ЧИСТОМ worktree по выбору билдера; НЕ назначать/не чистить/не трогать
  занятые GasCoopGame_dev / GasCoopGame_core (там foreign uncommitted работа).
- OS не диктует ветку/путь/SHA — билдер владеет реализацией.
- Unity MCP/Editor недоступен → STOP + сказать владельцу «запусти», без костылей.

## done_when (verifiable)

1. Independent test-author RED (EditMode/headless, до билда, билдер не редактирует) существует и краснеет на:
   спавн ставит игрока; префаб потребляет инъектированный источник позы; смена реализации источника двигает
   игрока БЕЗ правки префаба; drop-in во 2-ю сцену композится. После билда — GREEN.
2. Стабильный adapter-seam «read-only авторитетная поза ← сменный источник» + переиспользуемый player-префаб
   + управление + follow-камера. Источник В1 = локальная заглушка от ввода. Хуки реакция/вставание объявлены,
   no-op.
3. Owner-eye PlayMode приёмка подготовлена и передана владельцу пошагово (владелец запускает): (a) дропнул
   префаб в пустую сцену → ходит, камера следит; (b) во 2-й пустой сцене работает без допнастройки;
   (c) проба развязки — скриптовый источник вместо заглушки, префаб не тронут, капсула едет по пути.
4. Локальные headless-гейты GREEN; не затронуты чужие worktree/main; disposable/foreign work сохранён.

## return

RESULT: reviewed, gate-green В1 в GasCoopGame_dev (ветка билдера), с пошаговой owner-eye инструкцией; next =
owner-eye приёмка, затем — по её результату — В2 (тело: риг + реакции + косметический рэгдолл). Binding G5 =
fresh review + owner-eye (owner-run PlayMode — реальный гейт).

## budget

Одна сфокусированная BUILD-нога (маленькая — сокет + капсула, без контента).

END_OF_FILE: live/indie-game-development/work/c-exec-char-v1-socket-dropin-build-001-call.md
