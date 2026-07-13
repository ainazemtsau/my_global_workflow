# CALL — c-plan-characters-001

- id: c-plan-characters-001
- to: session (play: shape→plan; roadmap + freeze first build slice)
- for: g-6d4e «Игровые персонажи» (character presentation/embodiment track)
- issued: 2026-07-13 by s-map-characters-track-p2a0-close-001

## goal (outcome, not method)

Владелец получает одобренную дорожную карту трека «Игровые персонажи» И замороженный, builder-ready
spec ПЕРВОГО артефакта: переиспользуемый **drop-in префаб игрока** + **стабильный adapter-API**, который
любая сцена любого потока может кинуть к себе и получить работающего управляемого персонажа — под вердиктом
P2a0 (Кандидат A: ядро владеет авторитетной позицией тела, PuppetMaster-рэгдолл косметичен).

## context

- Канон вердикта P2a0 + дизайн грид-баллистики (single source): GasCoopGame product repo
  `origin/main@0e9eed02` → `docs/results/c-exec-player-puppetmaster-p2a0-lean-spike-build-001.md`.
- Спайк-стенд (переиспользовать импорт + маппер `BehaviourPuppet.state{Puppet|Unpinned|GetUp}`, Candidate-A
  через `canMoveTarget=false`): ветка `codex/c-exec-player-puppetmaster-p2a0-002-build@a6d9271f`, сцена
  `Assets/_PuppetSpike/P2A0_PuppetMasterSpike.unity`, `Assets/_PuppetSpike/OWNER-INSTRUCTION.md`. RootMotion
  вендор-ассет local-only/gitignored@f2f860b7, disposable (не мержится).
- Узел трека: TREE `g-6d4e` (презентация, брат g-7e15, НЕ 2-й bet).
- Прецедент развязки: g-7e15 R13/R14 seam — READ-ONLY вид над ЗАГЛУШКОЙ данных сейчас → свап на реальное
  ядро позже без изменения потребителя. Применить тот же приём к позиции персонажа.
- Проектное builder-quality правило: independent test-author пишет RED из SPEC до BUILD (см. память
  project-builder-stage-quality-fix). Роутинг: PLAN — эта OS-сессия; BUILD — отдельная GasCoopGame_dev сессия.

## boundaries (out of scope / do not touch)

- PLAN-only: НИКАКОГО продуктового кода / тестов / RED / BUILD / Unity / MCP / мержа / пуша. BUILD выдаётся
  отдельным CALL в свежую GasCoopGame_dev сессию после заморозки.
- **Грид-баллистика НЕ в build-scope этого трека** — это будущий слайс ЯДРА g-9c41 (input-lockstep,
  целочисленно, ждёт delivered grid+Step+lockstep из маршрута NearGas L1→…→I2). PLAN только определяет
  adapter-seam, куда позже воткнётся авторитетная позиция ядра (сейчас — заглушка).
- Не трогать газовый хребет: `NOW.next` = `c-exec-near-gas-core-authority-001-plan-amend-001` остаётся
  приоритетом №1. Персонажный трек — параллельная полоса в темпе владельца.
- `live/**` меняется только через RESULT.state_changes.

## done_when (verifiable)

1. Owner-approved замороженная дорожная карта трека: персонаж-first ORDER (drop-in префаб + adapter-API →
   управление / процедурные реакции / косметический рэгдолл → [ядро] граница грид-баллистики), каждая
   ступень — outcome-уровень; co-created по одному артефакту (G9), owner-слова в play_check.
2. Builder-ready spec ПЕРВОГО слайса: переиспензируемый префаб игрока + стабильный, документированный
   adapter-API (spawn; вести авторитетную позицию ИЗ источника; дёрнуть реакцию/сбитие/вставание),
   работающий против ЗАГЛУШКИ позиции с owner-eye критерием приёмки; independent-test-author RED-план назван.
3. Захвачены (не сделаны) downstream-обязательства: грид-баллистика как слайс ядра g-9c41 (Ф1 первой) и
   обязательный 2-машинный FishNet-proof «авторитетная грид-баллистика + локальный косметический рэгдолл
   согласованны на 2 машинах».

## return

RESULT с замороженным PLAN-доком под `work/`, метками owner_approved на co-created артефактах, и `next` =
BUILD CALL в GasCoopGame_dev на первый слайс (drop-in префаб + adapter-API).

## budget

Одна сфокусированная planning-сессия.

END_OF_FILE: live/indie-game-development/work/c-plan-characters-001-call.md
