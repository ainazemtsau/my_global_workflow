# CALL c-exec-player-puppetmaster-p2a0-lean-spike-build-001 — лёгкий спайк PuppetMaster (owner-eye + живой прибор)

> **Disposable spike, НЕ production-лег.** Гейт = глаз владельца + живой runtime-прибор в открытом
> редакторе. НЕ строить тяжёлый тест-observer/attempt-tree, НЕ воскрешать immutable RED c73b0195,
> НЕ независимый RED-автор, НЕ openspec-freeze, НЕ ревью-машинерию, НЕ headless-loop (он завесил
> прошлый заход). Если run-contract репо навязывает тяжёлые ворота, не подходящие спайку — **STOP и
> спросить владельца**, а не инфлировать. Владелец САМ жмёт Play и выносит PASS/FAIL — билдер это не
> самозаявляет.

to: executor
direction: indie-game-development
node: g-9c41
task: M1-P2a0
repo: C:\projects\Unity\GasCoopGame_p2a0_002
kind: engineering
change_lineage: c-exec-player-puppetmaster-p2a0-002 (лёгкий спайк заменяет тяжёлый live-source proof подход)
phase: BUILD (lean spike)
surface: claude-code   # нужен Unity-MCP + открытый редактор
owner_ack: owner-ack:owner-chat-2026-07-12-p2a0-lean-spike-go   # владелец: «Лёгкий спайк» → «го» на конкретную спеку (ниже)

goal: |
  На существующем стенде собран лёгкий playable спайк, который позволяет ВЛАДЕЛЬЦУ своими руками
  проверить: (1) PuppetMaster на нашей капсуле реально отрабатывает «толчок → реакция → подъём», и
  (2) владение позицией тела в момент удара чистое и восстанавливается — то, что глазами не видно и
  что решает пригодность для мультиплеера. Билдер отдаёт готовую к игре сцену + пошаговую инструкцию;
  вердикт выносит владелец.

context: |
  Зачем этот спайк (plain): PuppetMaster = «физическое тело, которое следует за анимацией, но реагирует
  на удары и встаёт обратно» (живой рэгдолл). Единственный реальный риск — КТО владелец позиции тела в
  момент удара: в мультиплеере одна машина должна быть «истиной»; если контроллер и рэгдолл дерутся за
  владение — две машины разойдутся. Владение глазами не видно → нужен живой прибор-считыватель.

  Владелец сознательно выбрал ЛЁГКУЮ версию (chat 2026-07-12: «Лёгкий спайк» → «го») вместо тяжёлого
  live-source proof: без тест-observer/attempt-tree/A-B-C-сразу, гейт = его глаз + живой прибор.

  Переиспользовать (уже готово, не переделывать), base = continuation tip:
    - worktree C:\projects\Unity\GasCoopGame_p2a0_002; branch codex/c-exec-player-puppetmaster-p2a0-002-build;
      base b9aea60c (поверх checkpoint a2d50c2a);
    - чистый импорт живого PuppetMaster (Assets/Plugins/RootMotion/, untracked — оставить как есть);
    - подтверждённый на реальном вендорном API маппер: BehaviourPuppet.state {Puppet|Unpinned|GetUp};
    - стенд/риг: префаб Pilot Root / сцена «Puppet Extended»; closed-world exclusion set перечислен в
      docs/results/c-exec-player-puppetmaster-p2a0-002.md.
    - package authority: PuppetMaster.unitypackage SHA-256
      03E126E93BA44BE178DD102A7A318A0F8207350C9640068B903307D1C0AFBED3.
  Ветку под лёгкий стенд выбирает билдер (можно свежую от b9aea60c, сохранив import/mapper); OS ветки/SHA
  не диктует. Перед мутацией — live-запрос обязан вернуть Application.dataPath =
  C:/projects/Unity/GasCoopGame_p2a0_002/Assets. Не трогать owner's GasCoopGame_dev редактор.

  Читать: product root AGENTS.md; docs/results/c-exec-player-puppetmaster-p2a0-002.md; эту CALL;
  Direction history history/2026-07-12-s-work-player-puppetmaster-p2a0-lean-spike-001.md.

done_when: |
  Собрано на существующем стенде (переиспользуя import + маппер, base b9aea60c):
  1. Кнопки (Odin [Button] или эквивалент в игре): «Кинуть камень» (физический камень летит в капсулу),
     «Импульс» (точечный толчок в тело), «Сброс» (вернуть в исходную позу).
  2. Экранный прибор — 3 строки, обновляемые в реальном времени из НАСТОЯЩЕГО runtime-состояния
     (не из builder-логов/JSON, не подделка):
       - «Управление телом: Контроллер / Рэгдолл (PuppetMaster)»;
       - «Состояние: Норма (Puppet) / Сбит (Unpinned) / Встаёт (GetUp)»;
       - «Коллизия капсулы: цела / сломана».
  3. Проводка «Кандидат A» (делаем ПЕРВЫМ): контроллер — постоянный владелец позиции капсулы; PuppetMaster
     физически реагирует поверх; при ударе уход в Unpinned/GetUp и возврат в Puppet с восстановлением
     контроллера/коллизии.
  4. Смоук через PlayMode test runner (НЕ headless-loop): доказывает, что кнопки срабатывают и прибор
     отражает реальное runtime-состояние — чтобы владельцу не отдали мёртвую сцену. Это смоук
     работоспособности стенда, НЕ вердикт про PuppetMaster.
  5. Пошаговая owner-инструкция: как открыть сцену, войти в Play, где кнопки, что читать в приборе, что
     считать «чисто» (удар → Сбит → Встаёт → Норма, управление чисто вернулось Контроллеру, коллизия
     цела, стабильно на нескольких ударах) и что «мутно» (владение мигает / не встаёт / коллизия ломается).
  6. Если билдер во время смоука сам наблюдал удары — приложить короткий начальный след прибора; но
     БИНДЯЩИЙ PASS/FAIL выносит владелец, играя сам. Билдер НЕ самозаявляет «PuppetMaster годится».
  7. Границы соблюдены (ниже). Если «Кандидат A» очевидно мутный уже на смоуке — можно подготовить
     переключатель на «Кандидат B» (контроллер→рэгдолл→контроллер handoff), но НЕ строить обе ветки как
     полное сравнение заранее.

return: |
  Committed handback: готовая к игре сцена (путь) + пошаговая owner-инструкция + смоук-evidence (кнопки/
  прибор живые через PlayMode runner) + (если есть) начальный след прибора; список изменённых путей,
  Unity run id, допущения; явная строка, что immutable RED c73b0195 НЕ тронут и НЕ является гейтом.
  Route home БЕЗ owner-verdict, G5, мержа. Далее владелец играет и сообщает clean/muddy → Direction
  записывает вердикт P2a0 + модель сетевого владельца (инвентарь).

boundaries: |
  Disposable spike. НЕ строить тяжёлый тест-owned observer/publisher/attempt-tree/collision-atomicity
  harness; НЕ независимый RED-автор; НЕ openspec-freeze; НЕ ревью-машинерия; НЕ -Deliver.
  immutable RED c73b0195 тестировал СУПЕРСЕДНУТЫЙ тяжёлый подход — оставить как есть (read-only),
  НЕ гнаться за его зеленью, НЕ редактировать, НЕ воскрешать как build-target.
  Прибор — РЕАЛЬНЫЙ runtime-считыватель (кто драйвит transform, состояние BehaviourPuppet, целостность
  коллайдера/контроллера), НЕ source-scan/pixels/builder-JSON (это запрещённый костыль-эвиденс).
  Multiplayer — INVENTORY-ONLY: двух-машинный FishNet-тест здесь НЕ делается и остаётся обязательным
  отдельной будущей ногой; по результату записать одной строкой модель владельца.
  НЕ трогать GasCoopGame_lab (import/harness/Library/settings). НЕ Core, FishNet BUILD, продакшн-контроллер,
  урон, gas consequence, custom Candidate-C локомотор, PR, product merge. Продукт вне стенда — read-only.
  MCP/автоматизация — первым делом. Required-tool blocker (Unity MCP отвалился / редактор не открыт /
  package mismatch) = STOP + сказать владельцу «запусти», НЕ обход/костыль; исключение только с дословным
  письменным owner-«да». Та же failure-class дважды = STOP/checkpoint.

budget: |
  Одна фокус-сессия (лёгкий спайк). Если стройка выглядит 2x над бюджетом или упирается в tool-blocker —
  STOP и checkpoint, а не тихая борьба.

launch:
  lane: C
  venue: C:\projects\Unity\GasCoopGame_p2a0_002 (branch codex/c-exec-player-puppetmaster-p2a0-002-build
    или свежая lean-ветка от b9aea60c, сохранив import/mapper; §Re-sync обязателен)
  machine: ПК (редактор №3)
  base: b9aea60c (import + mapper готовы; product origin/main@a644e5db)
  conflict_surface: новый lean-стенд/сандбокс + прибор + Candidate-A проводка; immutable `002` RED и `001`
    артефакты read-only; docs/results, docs/measurements
  depends_on: [live import + mapper @ b9aea60c — complete]
  merge_queue: none — disposable spike, без PR/product merge
  gates: смоук (PlayMode runner: кнопки/прибор живые) → ВЛАДЕЛЕЦ играет = binding PASS/FAIL → Direction
    записывает вердикт + модель владельца
  owner_eye: владелец сам жмёт Play, бьёт капсулу, читает прибор — это ГЕЙТ, не косметика

END_OF_FILE: live/indie-game-development/work/c-exec-player-puppetmaster-p2a0-lean-spike-build-001-call.md
