# CALL c-exec-near-gas-dashboard-001 — простое владельческое зеркало gas-engineering программы

to: executor
direction: indie-game-development
kind: engineering
repo: C:\projects\Unity\GasCoopGame_dev
node: g-9c41
task: NearGas-dashboard
goal: |
  Владелец открывает одну красивую страницу и сразу понимает текущую цель gas-engineering программы,
  пройденный путь, состояние каждой леги, блокировки, открытые вопросы, проблемы и недавнюю работу.
context: |
  Обязательные источники: AGENTS.md; docs/gas-simulation/PROGRAM.md; архивная DECOMPOSITION и ADR-E-0010,
  перечисленные в PROGRAM; Direction owner-panel как визуальный референс:
  C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\board\dashboard.html.
  Owner verdict и точные требования: history/2026-07-12-s-repair-near-gas-program-routing-001.md.
  PROGRAM задаёт маршрут/locks; child PLAN/tasks/RESULT/review/gate evidence задаёт статус; DirectionS задаёт приоритет.
  Owner choice A: ручной self-contained static HTML, обновляемый вместе с gas/visual RESULT; это только render mirror.
  Минимальный первый релиз: current goal/where-now/next; сегментированная карта легов и зависимостей; простая карточка
  каждой леги (что это, зачем, статус, что дальше, blocker); вопросы владельцу; проблемы; дневной журнал с понятными
  what/why/problem/outcome записями; checksum/Unity/scenes/visual-lock контекст только в нужной для картины глубине.
  IDs допустимы лишь мелко рядом с полной человеческой расшифровкой. Progress — только из дискретных статусов легов,
  без субъективных процентов. Архитектурная схема сейчас не нужна.
  launch:
    lane: D (doc-only, no product-code overlap)
    venue: GasCoopGame_dev; editor not needed
    machine: ПК
    base: dev @f5c1d650 (§Re-sync обязателен)
    conflict_surface: AGENTS.md; docs/gas-simulation/dashboard.html; docs/results/c-exec-near-gas-dashboard-001.md
    depends_on: accepted PROGRAM @f5c1d650; owner dashboard verdict in Direction history
    merge_queue: none in this leg; return HOME before any integration decision
    gates: render/readback at desktop+narrow width; review n/a — light doc-only; separate Direction close verifies handback
boundaries: |
  Не менять product code, tests, scenes, packages, Unity settings или существующие PLAN/spec/tasks/ADR/PROGRAM semantics.
  Не запускать Unity, game build, L1 PLAN/BUILD или visual PLAN/BUILD. Не читать содержимое dirty c-visual-009 BUILD.
  Не создавать generator/script/server/database/status JSON и не превращать HTML во второй источник правды.
  Не показывать владельцу SHA, commit history, filesystem paths, gate transcripts или другую служебную механику.
  Не менять Direction OS dashboard и canon dashboard. Сохранить все unrelated dirty/untracked product files,
  особенно две незавершённые NearGas test-author заготовки и dirty VoxelSandboxSourcePolicyPlayModeTests.cs.
done_when: |
  1. `docs/gas-simulation/dashboard.html` — self-contained, responsive, визуально аккуратный HTML, открывающийся с диска;
     он использует понятный язык и визуальные приёмы существующей Direction-панели без копирования её старого содержания.
  2. Первый экран сразу показывает текущую цель, где мы, что сейчас, следующий шаг и главные блокеры; карта покрывает
     L1/L2/C1/M0/L3/I1/L4/L5/L6/I2, post-I2 performance/far-tier, runtime/topology и visual lanes.
  3. Каждая лега расшифрована простыми полными предложениями; видны status, dependency/blocker и next. Checksum,
     Unity migration, scene retirement и exact visual locks объяснены без архитектурной стены текста.
  4. Есть owner questions/problems и подробный простой журнал по дням, начинающийся с принятия PROGRAM/dashboard route;
     последующие gas/visual RESULT обновляют HTML вручную в том же product change/handback.
  5. Прогресс показан сегментами фактических leg-status, не экспертным процентом. Нет ID без расшифровки и нет видимых
     SHA/commit/path/gate details. Страница явно называет себя зеркалом: при расхождении PROGRAM/evidence/DirectionS выше.
  6. Root `AGENTS.md` получает always-read правило: любой gas/GasView/visual/scene/checksum/topology PLAN, BUILD или review
     сначала читает PROGRAM; любое изменение owner-visible gas/visual статуса обновляет dashboard вручную вместе с RESULT.
  7. Visual card показывает LOCKED до M0+C1+L3+I1; motion дополнительно ждёт sufficient committed-per-Step data либо
     отдельный visual-motion-data-seam; moving-source ждёт E1, door/destruction — D1/X1; old c-visual-009 не возобновляется.
  8. Diff ограничен AGENTS.md, dashboard.html и обязательным per-leg closing report; render/readback green. Все заранее
     грязные/неотслеживаемые файлы побайтно не затронуты, Unity/L1/visual не запускались.
return: |
  Product RESULT HOME: owner-readable outcome; exact changed files; render/readback evidence; preservation proof;
  dashboard screenshot/path; AGENTS read/update rule; explicit statement that no L1 CALL was authored or started.
budget: one focused half-day
surface: any

END_OF_FILE: live/indie-game-development/work/c-exec-near-gas-dashboard-001-call.md
