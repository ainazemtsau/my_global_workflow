# CALL c-exec-near-gas-core-authority-001

to: executor
direction: indie-game-development
kind: engineering
repo: C:\projects\Unity\GasCoopGame_core
node: g-9c41
task: NearGas-L1-PLAN

goal: |
  Владелец принимает замороженный L1 PLAN, по которому NearGas получает единственного engine-free Core-владельца,
  атомарную замену поколения и один полный deterministic Step без преждевременной Unity/product активации.

context: |
  Binding authorities: root AGENTS.md; docs/gas-simulation/PROGRAM.md at accepted dev@9bc577c7
  (PROGRAM content parent f5c1d650); archived carry-forward
  openspec/changes/archive/c-exec-near-gas-authority-stabilization-001/DECOMPOSITION.md.
  Direction close: live/indie-game-development/history/2026-07-13-s-work-near-gas-dashboard-close-002.md.

  L1 outcome from the accepted program: dormant engine-free NearGasSimulation owns atomic generation candidate/swap,
  a minimal generation-bound scalar read and one prepared deterministic Step/commit using the existing kernel.
  Exact NoSourceGolden and SourceChecksumIsolation remain explicit slow legacy-audit oracles; ordinary Step/read does
  not compute or publish full-domain legacy FNV. The plan must preserve the clean future seams to L2 resource admission,
  C1 committed identity and L3 Unity authority cutover without freezing their child APIs prematurely.

  Accepted dev@9bc577c7 root AGENTS records product contract v19, equal to OS engineering current v19. The Direction
  tool could not inspect the target core-worktree validation.config stamp; preflight must read it and §Re-sync before
  planning if behind, or STOP if unreadable. Root AGENTS requires a detailed, simple owner-readable PLAN session
  separate from every RED/BUILD session and requires manual dashboard update with owner-visible status.

  launch:
    lane: A
    venue: C:\projects\Unity\GasCoopGame_core (core; PLAN-only, headless; Unity Editor not needed)
    machine: ПК
    base: dev @9bc577c7 (§Re-sync обязателен)
    conflict_surface: PLAN/spec/tasks/ADR/dashboard/result documentation only; no product code or tests
    depends_on: Direction-closed NearGas-dashboard; accepted PROGRAM/DECOMPOSITION
    merge_queue: none — PLAN-only; BUILD receives a later separately issued slot
    gates: verified assigned core worktree + owner-readable PLAN verdict; no BUILD/G5 execution in this call

boundaries: |
  PLAN-only. Не писать product code, не заказывать и не писать RED tests, не запускать tests/tools/check, Unity,
  game build, L1 BUILD или visual work. Не проектировать и не строить L2/C1/L3, PlayerSense, replay, runtime sources,
  topology/destruction, render lifecycle или legacy deletion; не возобновлять Phase 0/c-visual-009.
  Не переименовывать legacy FNV в новый обычный digest и не превращать L1 в Unity authority.
  Сохранить все существующие dirty/untracked файлы в GasCoopGame_dev; не читать dirty visual implementation.
  До любого PLAN commit проверить назначенный core worktree, его validation.config/contract v19, отсутствие другого
  in-flight core leg, свежую base и отсутствие UnityLockfile. Провал preflight = STOP с точным blocker;
  GasCoopGame_dev не является молчаливой заменой.
  После owner verdict остановиться и вернуть RESULT HOME; отдельный BUILD CALL выпускает только DirectionS.

done_when: |
  1. Владелец получает подробный, но простой PLAN: каждое техническое решение, альтернатива, риск, cut и причина
     объяснены человеческим языком; его фактический verdict дословно записан.
  2. Committed frozen PLAN artifacts дают будущему builder однозначные L1 boundaries, acceptance properties,
     evidence venues и независимые RED/review/G5 handoffs, включая spec/tasks/ADR там, где требует root contract.
  3. PLAN покрывает accepted L1 outcome и carry-forward инварианты: engine-free dormant owner, atomic generation
     replacement, complete Step/commit, no raw mutable leak, whole-operation atomicity on throws, deterministic
     source-before-flow/local-id/handler ownership, explicit slow legacy-audit goldens, zero-float/int-overflow guards;
     ordinary Step/read не вычисляет и не публикует full-domain FNV.
  4. PLAN явно сохраняет exclusions и future ownership: нет Unity wiring/production activation, committed-digest
     algorithm, final resource-limit DTO, PlayerSense/render/replay policy, dynamic source/topology gameplay или legacy
     deletion; L2/C1/L3 re-derive their own APIs after delivered L1.
  5. Изменения ограничены PLAN/spec/tasks/ADR, обязательным per-leg PLAN report и ручным dashboard status update.
     Product code/tests/scenes/packages/Unity/RED/BUILD не затронуты; все pre-existing dirty/untracked файлы сохранены.

return: |
  Product PLAN RESULT HOME: owner-readable plan summary and exact owner verdict; commit and changed files; frozen
  artifacts/evidence map; cuts/risks/assumptions; preservation proof; explicit statement that no RED, code, tests,
  Unity or BUILD ran and that only DirectionS may issue the later BUILD CALL.

budget: one focused owner-present PLAN session
surface: any

END_OF_FILE: live/indie-game-development/work/c-exec-near-gas-core-authority-001-call.md
