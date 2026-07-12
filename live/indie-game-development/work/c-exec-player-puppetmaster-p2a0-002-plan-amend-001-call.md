# CALL c-exec-player-puppetmaster-p2a0-002-plan-amend-001 — owner-present PLAN amendment (acceptance approach)

> **PLAN-amend, owner-present. Не BUILD.** Эта сессия дорабатывает и заново замораживает
> акцептанс-подход замороженного live-source proof PLAN `b90b7205`, берёт дословное owner-«да»
> на конкретную амменд-спеку, переморозит продуктовый PLAN новым коммитом и выпускает ОТДЕЛЬНЫЙ
> свежий BUILD-only CALL. Никакого rig-build, merge, PR, `-Deliver`, G5 или owner-verdict по A/B/C.

to: executor
direction: indie-game-development
node: g-9c41
task: M1-P2a0
repo: C:\projects\Unity\GasCoopGame_p2a0_002
kind: engineering
change_id: c-exec-player-puppetmaster-p2a0-002
phase: PLAN-amend
surface: any
parent_history: history/2026-07-12-s-work-player-puppetmaster-p2a0-checkpoint-route-001.md
owner_ack: owner-ack:owner-chat-2026-07-12-p2a0-002-steer-ok   # направление амендмента; дословное «да» на спеку берётся В этой сессии

goal: |
  Замороженный live-source PuppetMaster proof имеет обновлённый, owner-одобренный акцептанс-подход:
  машинное доказательство корректности сохранено без изменений, обязательный видео-захват заменён
  живой one-machine playable A/B/C песочницей как owner-eye слоем (никогда не гейт), multiplayer —
  inventory-only. Продуктовый PLAN переморожен новым коммитом с дословным owner-вердиктом, и выпущен
  отдельный свежий BUILD-only CALL под этот амменд.

context: |
  Owner steer (owner chat «ок», 2026-07-12) — направление амендмента (заморозить ЗДЕСЬ, дословным «да»):
    - KEEP машинное доказательство корректности: observer/payload/attempt-tree/collision atomicity —
      скрытую authority/collision-state одним глазом на одной сцене не проверить (owner согласился).
    - REPLACE обязательные два A/B MP4-клипа + два контактных листа → живая single-machine playable
      A/B/C песочница (Odin `[Button]`: owner жмёт Play, применяет rock/point-impulse, смотрит передачу
      контроллер↔таз, с пошаговой инструкцией). DROP видео-захват (owner-eye only, никогда не гейт;
      автоматический one-machine capture оказался хрупким).
    - Multiplayer — INVENTORY-ONLY (уже замороженная позиция): выживший A/B оставляет будущее
      двух-пировое FishNet-доказательство обязательным отдельной ногой.
    - Тяжёлая часть НЕ меняется: развести Кандидат A (владеет контроллер) и Кандидат B
      (контроллер→таз→контроллер handoff) на реальном риге PuppetMaster — многочасовая стройка.

  Читать в этом порядке (self-contained; при доступе к репо — свежие файлы):
    - product root `AGENTS.md`;
    - `openspec/changes/c-exec-player-puppetmaster-p2a0-002/PLAN.md` + `specs/.../spec.md` (замораживаемое);
    - `docs/results/c-exec-player-puppetmaster-p2a0-002.md` (cumulative RESULT + Owner steer);
    - `docs/measurements/c-exec-player-puppetmaster-p2a0-002-build-continuation-001.md`;
    - Direction history `history/2026-07-12-s-work-player-puppetmaster-p2a0-checkpoint-route-001.md`.

  Продуктовая идентичность на диспатче (проверено первыми руками 2026-07-12):
    - worktree: `C:\projects\Unity\GasCoopGame_p2a0_002`;
    - branch: `codex/c-exec-player-puppetmaster-p2a0-002-build`;
    - HEAD (continuation tip): `b9aea60c` — база амменда; base checkpoint `a2d50c2a`; коммиты
      `04fad5dd` (live import + stand/mapper/closed-world), `b9aea60c` (owner-steer doc);
    - НЕ MERGED: `b9aea60c` не предок product `origin/main@a644e5db`; vendor `Assets/Plugins/RootMotion/` untracked;
    - frozen PLAN (амендируется): `b90b7205`; immutable RED (НЕ трогать/не повторять): `c73b0195`;
    - package authority: `PuppetMaster.unitypackage` SHA-256 `03E126E93BA44BE178DD102A7A318A0F8207350C9640068B903307D1C0AFBED3`;
    - synced engineering contract: v19.

  Уже сделано на ветке (не переделывать): чистый live PuppetMaster import + vendor readback; frozen-mapper
  target подтверждён на реальном API `BehaviourPuppet.state {Puppet|Unpinned|GetUp}`; стенд = префаб
  Pilot Root / сцена «Puppet Extended»; closed-world exclusion set перечислен. Venue-блокер прошлой
  попытки: bare-stand settle smoke застыл на headless PlayMode loop (2-й кадр) → амменд ОБЯЗАН направить
  settle-smoke и наблюдение через **раннер PlayMode-тестов**, без снижения доказательности.

boundaries: |
  Это PLAN-amend. НЕ строить риг, мост, песочницу, observer или тесты; не запускать BUILD.
  Не редактировать immutable RED `c73b0195`, immutable-001 history/evidence/tests, package hashes.
  Заморозка амменд-спеки — ТОЛЬКО с дословным owner-«да» на конкретную спеку в этой сессии (G9-класс):
  без owner-слов сессия закрывается checkpoint'ом, оставляя `c-exec-player-puppetmaster-p2a0-002-plan-amend-001`
  открытым. Задача `M1-P2a0` done_when не меняется (в ней видео и не было) — амменд живёт на PLAN-уровне.
  Multiplayer остаётся inventory-only: никакого FishNet BUILD и двух-пирового теста здесь. Никакого Core,
  damage, gas consequence, production controller, merge, PR, `-Deliver`. Живая песочница — owner-eye слой,
  НИКОГДА не гейт приёмки; гейт — только машинное доказательство корректности через PlayMode test runner.
  Продукт вне заморозки PLAN-доков — read-only.

done_when: |
  1. Конкретная амменд-спека представлена owner как читаемый бриф: что именно строит песочница
     (Odin `[Button]` набор: spawn rock, apply point-impulse, switch A/B/C, reset), пошаговая
     owner-инструкция, и — отдельно и явно — какие МАШИННЫЕ утверждения (observer/payload/attempt-tree/
     collision atomicity, bounded-C kill-probe) остаются без изменений и проверяются раннером PlayMode-тестов.
  2. Owner дал ДОСЛОВНОЕ «да»/«утверждаю» на эту амменд-спеку (цитата в RESULT `play_check`/evidence).
     Без дословных слов — checkpoint, open_call остаётся.
  3. Продуктовый PLAN переморожен новым коммитом (openspec/changes/.../PLAN.md + spec обновлены):
     видео-захват удалён, живая A/B/C песочница добавлена как owner-eye (не гейт), settle-smoke + наблюдение
     переведены на PlayMode test runner, multiplayer помечен inventory-only. Immutable RED и package hashes
     byte-identical.
  4. Выпущен ОТДЕЛЬНЫЙ свежий BUILD-only CALL под переморожённый PLAN (multi-hour rig build: Кандидат A
     controller-owned + Кандидат B controller→pelvis→controller handoff на реальном риге PuppetMaster;
     test-owned observer/attempt-tree; A/B rock+point-impulse; bounded-C kill-probe; collision restoration;
     MP inventory-only), с checkpoint-only дисциплиной и отдельным будущим fresh G5.
  5. Никакой owner-verdict по A/B/C/reject и никакой G5 здесь не берётся и не заявляется; merge/PR/`-Deliver`
     не выполняются.

return: |
  RESULT: переморожённый PLAN commit hash + дословный owner-вердикт; точный diff PLAN/spec (видео→песочница,
  smoke→PlayMode runner, MP inventory-only, машинное доказательство без изменений); подтверждение
  byte-identical immutable RED/package hashes; выпущенный BUILD-only CALL (id + файл); и — если owner-слов
  нет — precise checkpoint с открытым open_call.

budget: одна owner-present сессия.

launch:
  lane: C
  venue: C:\projects\Unity\GasCoopGame_p2a0_002
    (branch codex/c-exec-player-puppetmaster-p2a0-002-build; base continuation tip b9aea60c; §Re-sync обязателен)
  machine: ПК
  base: b9aea60c (continuation tip поверх checkpoint a2d50c2a; product origin/main@a644e5db)
  conflict_surface: openspec/changes/c-exec-player-puppetmaster-p2a0-002/** (PLAN/spec), docs/results,
    docs/measurements; immutable `002` RED пути и `001` артефакты read-only
  depends_on: [immutable RED c73b0195 — complete; live import + mapper @ b9aea60c — complete]
  merge_queue: none — PLAN-amend, без PR/product merge
  gates: PLAN заморожен owner-словами (G9) → отдельный BUILD → отдельный fresh G5 → owner final verdict
  owner_eye: живая single-machine A/B/C песочница (Odin [Button]) ПОСЛЕ машинного доказательства; никогда не гейт

END_OF_FILE: live/indie-game-development/work/c-exec-player-puppetmaster-p2a0-002-plan-amend-001-call.md
