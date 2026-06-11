RESULT s-2026-06-11-indie-frame-live-shell-001 (call: owner-start-2026-06-11-indie-live-shell)
direction: indie-game-development   play: frame   node/task: root/bootstrap
outcome: |
  Подготовлен минимальный live-shell для нового direction `indie-game-development`.
  Это чистый live direction: legacy archive не импортируется, Codex/product execution не запускается, Unity project не создаётся, старый код не переносится.
evidence: |
  Route resolved by OS rule: `live/indie-game-development/NOW.md` отсутствует, поэтому direction трактуется как новый live direction и запускается `play: frame`.
  Read and validated OS files:
  - `os/KERNEL.md` read; END_OF_FILE present.
  - `os/plays/frame.md` read; END_OF_FILE present.
  - `os/schema/packets.md` read; END_OF_FILE present.
  - `os/plays/shape.md` read; END_OF_FILE present.
  Repository mutation in this session: none.
  Archive access/import: none.
  Product execution/Codex/Unity/code transfer: none.
  Next CALL is `play: shape` for setup/live-loop verification, not product execution.
state_changes: |
  Create file: `live/indie-game-development/CHARTER.md`
  Content:
  ~~~markdown
  # CHARTER — indie-game-development

  direction_id: indie-game-development
  status: live_shell_created

  ## Mission

  Создать направление для разработки оригинальной indie co-op игры через Direction OS, начиная не с продукта, а с проверенной live-оболочки: CALL/RESULT/writer loop должен сначала доказать, что состояние направления можно безопасно создавать, читать и обновлять.

  Игровая/product-амбиция направления сохраняется как будущая цель: инновационная игра с сильным системным ядром, включая будущую работу с симуляцией газа, grid/topology и co-op взаимодействиями. Эта оболочка не является переносом старого направления и не является стартом разработки игры.

  ## Success criteria

  1. `live/indie-game-development/` существует как новый чистый live direction с базовыми файлами `CHARTER.md`, `TREE.md`, `NOW.md`, `LOG.md`.
  2. Следующий шаг маршрутизирован в `play: shape` для проверки setup/live-loop, а не в product execution.
  3. Любой будущий перенос знаний из `archive/directions/indie-game-development` оформляется отдельной bounded transfer/import работой с evidence, без автоматического legacy import.
  4. Product execution начинается только после явного shape/review маршрута и отдельного CALL; не в этом bootstrap frame.

  ## Hard constraints

  - Do not restore `archive/directions/indie-game-development`.
  - Do not import legacy state.
  - Do not launch Codex/product execution.
  - Do not create a Unity project.
  - Do not transfer old code.
  - Do not treat old project files as source of truth.
  - Archive may be mentioned only as a future evidence source for separate later transfer/import work.
  - Direction state lives in `live/indie-game-development/`.

  ## Lenses

  - workflow: CALL/RESULT/writer loop, state shape, OS compliance.
  - product: game direction, player-facing value, co-op/systemic novelty.
  - technical: future engine/runtime/prototype constraints, gas/grid/topology feasibility.
  - evidence: every done claim needs concrete proof; no confidence-only closure.

  ## Product repos

  - workflow_state_repo: `github.com/ainazemtsau/my_global_workflow`
  - product_repo: none selected in this frame
  - future_product_repo: to be decided by a later shaped bet

  ## Pre-mortem

  This direction failed three years from now because:

  1. Legacy archive was blindly imported and polluted the new live direction.
     - mitigation: archive is parked as future evidence only; no import in bootstrap.
  2. Product execution started before the OS loop was verified.
     - mitigation: first next CALL is setup/live-loop shape, not Codex/product work.
  3. Unity/project/code decisions were made before scope and evidence gates existed.
     - mitigation: product repo, Unity project, and code transfer are explicitly out of scope.
  4. The game direction collapsed into disconnected gas-only documents.
     - mitigation: product and technical lenses must stay connected in later shape work.
  5. Claims of completion were accepted without durable state or writer evidence.
     - mitigation: done claims must point to live files, RESULT packets, commits, or explicit check output.

  ## Outside view

  New AI-assisted game directions usually fail early when they jump from ambition directly into implementation. Simulation-heavy indie games add extra risk: prototypes can consume time before the core loop and project discipline are proven. The correct first sequence is therefore operational, not creative: create the live direction shell, verify that CALL/RESULT/writer loop works, then shape the first real product foundation bet.

  END_OF_FILE: live/indie-game-development/CHARTER.md
  ~~~

  Create file: `live/indie-game-development/TREE.md`
  Content:
  ~~~markdown
  # TREE — indie-game-development

  direction_id: indie-game-development

  ## Root

  - id: g-root
    goal: >
      A clean live Direction OS project exists for indie-game-development and can safely carry the game direction from framing through shaped bets into later product work.
    done_when: >
      The direction has durable live state, verified routing, and a shaped path toward product foundation without importing legacy state or starting product execution prematurely.
    status: shaped
    children:

      - id: g-setup-live-loop
        goal: >
          The new live-shell and CALL/RESULT/writer loop are verified for this direction.
        done_when: >
          A shaped setup-verification bet proves that the four live state files can be created, read, updated by writer flow, and continued through a next CALL without archive import or product execution.
        status: parked

      - id: g-product-foundation
        goal: >
          The first product/technical foundation bet is shaped from the clean live direction.
        done_when: >
          An approved shape result defines scope, cuts, lenses, riskiest assumption, kill_by, and first tasks for product foundation without creating Unity project or transferring old code.
        status: parked

      - id: g-legacy-evidence-transfer-later
        goal: >
          Useful evidence from `archive/directions/indie-game-development` is evaluated without importing legacy state.
        done_when: >
          A separate bounded transfer/import session produces accepted knowledge entries or explicit rejected legacy assumptions, with evidence and no automatic state restoration.
        status: parked

      - id: g-playable-technical-nucleus-later
        goal: >
          A first playable technical nucleus is eventually scoped and produced after setup and product foundation gates.
        done_when: >
          A later shaped and executed product bet produces verifiable playable evidence for a nucleus that connects core systems such as gas, grid/topology, and co-op interaction.
        status: parked

  END_OF_FILE: live/indie-game-development/TREE.md
  ~~~

  Create file: `live/indie-game-development/NOW.md`
  Content:
  ~~~markdown
  # NOW — indie-game-development

  direction_id: indie-game-development
  updated: 2026-06-11

  ## Current state

  active_bet: none
  active_tasks: []
  open_calls: []
  decision_inbox: []
  recurring: []

  ## Routing

  current_route: >
    New live direction bootstrap completed by frame RESULT. Next step is shape/setup verification before any product execution.

  next:
    call_id: c-2026-06-11-indie-shape-setup-verification-001
    to: session
    play: shape
    node: g-setup-live-loop
    task: none
    summary: >
      Shape the first verification bet for the live-shell and CALL/RESULT/writer loop.

  ## Ready next CALL

  CALL c-2026-06-11-indie-shape-setup-verification-001
  to: session
  direction: indie-game-development
  play: shape
  node: g-setup-live-loop  task: none
  goal: |
    Сформировать первый approved bet, который проверяет setup/live-loop для нового direction `indie-game-development`: live files, CALL/RESULT/writer loop, route clarity, and continuation through state.
  context: |
    Read:
    - live/indie-game-development/CHARTER.md
    - live/indie-game-development/TREE.md
    - live/indie-game-development/NOW.md
    - live/indie-game-development/LOG.md

    This is a new clean live direction. `archive/directions/indie-game-development` was not imported and must not be treated as current state.
  boundaries: |
    Do not import `archive/directions/indie-game-development`.
    Do not restore legacy state.
    Do not launch Codex/product execution.
    Do not create Unity project.
    Do not transfer old code.
    Do not start product implementation.
    Mention archive only as a future evidence source for separate later transfer/import work.
  done_when: |
    NOW.md contains one approved active bet for setup/live-loop verification, passing gates G1-G6.
    TREE.md marks `g-setup-live-loop` active or split into valid child outcomes.
    The next CALL is ready and still points to setup/writer verification, not product execution.
  return: |
    RESULT packet with exact state_changes for TREE.md, NOW.md, LOG.md. Include evidence that no archive import or product execution happened.
  budget: one session
  surface: chatgpt

  END_OF_FILE: live/indie-game-development/NOW.md
  ~~~

  Create file: `live/indie-game-development/LOG.md`
  Content:
  ~~~markdown
  # LOG — indie-game-development

  - 2026-06-11 — frame/bootstrap: minimal live-shell prepared for new direction; no archive import, no Codex/product execution, no Unity project, no old code transfer; next CALL points to shape/setup verification.

  END_OF_FILE: live/indie-game-development/LOG.md
  ~~~
captures:
  - `archive/directions/indie-game-development` may be used later only as a bounded evidence source in a separate transfer/import session; it was not imported in this frame.
decisions_needed: []
log: frame/bootstrap: minimal live-shell prepared; no archive import; next is shape/setup verification
next: |
  CALL c-2026-06-11-indie-shape-setup-verification-001
  to: session
  direction: indie-game-development
  play: shape
  node: g-setup-live-loop  task: none
  goal: |
    Сформировать первый approved bet, который проверяет setup/live-loop для нового direction `indie-game-development`: live files, CALL/RESULT/writer loop, route clarity, and continuation through state.
  context: |
    Read:
    - live/indie-game-development/CHARTER.md
    - live/indie-game-development/TREE.md
    - live/indie-game-development/NOW.md
    - live/indie-game-development/LOG.md

    This is a new clean live direction. `archive/directions/indie-game-development` was not imported and must not be treated as current state.
  boundaries: |
    Do not import `archive/directions/indie-game-development`.
    Do not restore legacy state.
    Do not launch Codex/product execution.
    Do not create Unity project.
    Do not transfer old code.
    Do not start product implementation.
    Mention archive only as a future evidence source for separate later transfer/import work.
  done_when: |
    NOW.md contains one approved active bet for setup/live-loop verification, passing gates G1-G6.
    TREE.md marks `g-setup-live-loop` active or split into valid child outcomes.
    The next CALL is ready and still points to setup/writer verification, not product execution.
  return: |
    RESULT packet with exact state_changes for TREE.md, NOW.md, LOG.md. Include evidence that no archive import or product execution happened.
  budget: one session
  surface: chatgpt
