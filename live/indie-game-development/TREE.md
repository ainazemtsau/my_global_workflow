# Goal tree: indie-game-development

owner_approved: 2026-07-20 — history/2026-07-20-s-map-program-v2-hot-migration-route-001.md; 2026-07-20 — history/2026-07-20-s-repair-build-tooling-parking-001.md («припаркую», g-c5d1 parked); 2026-07-20 — history/2026-07-20-s-map-grid-track-resume-001.md («Принимаю активацию Grid по этому маршруту», g-4b92 parallel)

- id: g-a7f2
  goal: Выпущенная в Steam коммерческая co-op игра строится вокруг gas + grid, изменения пространства и экспедиционной игры; продукт технически силён, понятен игрокам и приносит реальный доход.
  done_when: |
    Игра доступна как платный Early Access/1.0; получила реальную выручку или funding; достигла текущей цели CHARTER $100k gross lifetime; playable evidence доказывает co-op-first, gas + grid, spatial change, разные газы и expedition pressure; владелец гордится результатом, а внешний сигнал показывает, что игроки его понимают.
  status: active
  detail: history/2026-07-20-s-map-program-v2-hot-migration-route-001.md; live route — work/program-v2-integration-lab-plan.md
  children:

    - id: g-9c41
      goal: "Integration Lab & Product Proof: одна развиваемая тестовая сцена принимает проверенные capability drops и становится representative playable proof."
      done_when: Один entry point воспроизводимо сводит принятые Grid, Gas, World Change, Character, Level и Presentation drops; остаток и proof по каждому видны в глобальном плане.
      why: Один serial integration owner позволяет параллельную работу без размытой ответственности за совместимость.
      status: parallel
      detail: work/program-v2-integration-lab-plan.md; legacy NearGas L1B terminal HOME — history/2026-07-19-s-work-near-gas-l1b-v29-terminal-home-close-001.md
      children:

        - id: g-1a63
          goal: "Gas Simulation: authoritative слой газа вычисляет типы, перенос, взаимодействия и игровые последствия на committed topology/grid revisions."
          done_when: Детерминированный harness и negative controls доказывают gas behavior и scene-ready drop, включая реакцию на committed topology change.
          why: Центральная системная механика должна развиваться отдельно от сцены, grid transport и rendering.
          status: parked
          detail: work/program-v2-integration-lab-plan.md#2-gas-simulation

        - id: g-4b92
          goal: "Grid / Layers / World Change: общий address/ownership space, commit clock и event transport связывают независимые слои и публикуют topology changes."
          done_when: Минимум два разных consumer layers одинаково принимают committed revision/event; stale и live mid-tick cross-layer access fail-closed.
          why: Газ, ветер, оборудование, взрывы и будущие слои должны общаться через универсальный seam, а не gas-only уведомление или god object.
          status: parallel
          detail: work/program-v2-integration-lab-plan.md#3-grid--layers--world-change; preparation route — history/2026-07-20-s-map-grid-track-resume-001.md

        - id: g-8f20
          goal: "Level & Environment: hand-authored и procedural sources создают валидное пространство через replaceable ingestion contract."
          done_when: Structural validation, вертикальные/боковые пути и apertures доказаны в track-owned scene; reproducible generator drop принят Integration.
          why: Геометрия и генератор должны меняться без переписывания sim layers и общей сцены.
          status: parallel
          detail: work/program-v2-integration-lab-plan.md#4-level--environment; LV0 receipt remains waiting

        - id: g-6d4e
          goal: "Character & Gameplay Contact: authoritative Player Simulation / Actor Layer и отдельный Character View дают управление, контакт и честную реакцию."
          done_when: Actor следует принятому Grid/Layer seam, View не становится authority, а reusable prefab проходит contact/reaction proof и Integration smoke.
          why: Системный стенд становится игрой только через действия игрока и читаемую обратную связь.
          status: parallel
          detail: work/program-v2-integration-lab-plan.md#5-character--gameplay-contact; legacy Leg 2 remains in review/closing

        - id: g-7e15
          goal: "Presentation: gas/world/character state читаем, держит performance budget и даёт reproducible capture."
          done_when: Visual drop потребляет только принятые read models, различает ключевые состояния и проходит clarity/budget/negative proof.
          why: Невидимая или неоднозначная симуляция не создаёт gameplay clarity и showable product proof.
          status: parallel
          detail: work/program-v2-integration-lab-plan.md#6-presentation; legacy c-visual-009 remains blocked

    - id: g-d3a8
      goal: "Design & Canon: системы, мир, fantasy и ограничения образуют согласованный owner-approved канон для продуктовых направлений."
      done_when: Существенные design questions имеют принятые ответы, конфликты явны, downstream work ссылается на current canon.
      why: Технические возможности должны превращаться в решения игрока и узнаваемую игру.
      status: parallel
      detail: Существующий canon-forge сохраняется; current root c-cartography-g-d3a8-post-gas-behavior-admission-front-001.

    - id: g-c5d1
      goal: "Build & Tooling: version, build, validators и shared tooling воспроизводимо снимают конкретные cross-track blockers."
      done_when: Каждый bounded task имеет named product consumer, first-hand proof и не создаёт отдельную техническую authority.
      why: Общие инструменты нужны как сервис продукту, а не как бесконечный самостоятельный roadmap.
      status: parked
      detail: Standalone .NET Gates retired; V30 route superseded by installed V31; no live root, wake only for a concrete named product consumer → history/2026-07-20-s-repair-build-tooling-parking-001.md.

    - id: g-2f8c
      goal: "Marketing & Audience: реальные product proofs превращаются в позиционирование, storefront, публикации, аудиторию и коммерческий signal."
      done_when: Существующий marketing-forge выпускает необходимые артефакты из accepted evidence, сохраняет голос владельца и возвращает измеримый feedback.
      why: Технически сильная игра без понятного обещания и внешнего сигнала не получает рынок.
      status: parallel
      detail: Existing marketing-forge and its accepted operating split remain unchanged → history/s-map-003.md; Factorio Friday Facts is the map's single rare form reference, not an automatic strategy.
      children:

        - id: g-5b07
          goal: "Steam Storefront: страница честно переводит принятый product proof в понятное обещание игроку."
          done_when: Scope, copy и media согласованы с current product и проходят owner review.
          why: Главный conversion surface не должен опережать доказанную игру.
          status: parked
          detail: Existing accepted storefront gates/dates remain unchanged → history/s-map-002.md; nested Marketing outcome, not a separate live track.

        - id: g-e6f2
          goal: "Audience Growth: реальные материалы разработки формируют устойчивую аудиторию и пул будущих playtesters."
          done_when: Принятый cadence не превращается в filler treadmill и даёт измеримый внешний сигнал.
          why: Co-op proof и коммерческая проверка требуют внешних игроков, а не только внутреннего стенда.
          status: parked
          detail: Existing accepted cadence/channel/AI-policy remains unchanged → history/s-map-002.md; nested Marketing outcome, not a separate live track.

END_OF_FILE: live/indie-game-development/TREE.md
