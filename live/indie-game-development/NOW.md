# NOW — indie-game-development
updated: 2026-07-10 by s-spike-pgg-001-cp1

bet:
  node: g-9c41
  goal: |
    Полигон М1 — одно end-to-end доказательство репрезентативной сетевой co-op сцены g-9c41:
    регулируемый DA-уровень примерно на 150 комнат, тип/сила источников, player↔gas tracking,
    реакции и тестовый взрыв, один стеновой пролом с area-aware потоком, видимые sleeping-front
    + S4 room-rollup, полное затопление, две реальные машины и замер слабого железа.
    Утверждённая лестница 0–10, cuts и риски: work/poligon-m1-shape-2026-07-10.md.
  appetite: |
    Максимум 11 продуктовых легов (ступени 0–10), started 2026-07-10; это ёмкость, не
    календарное обещание. Продления нет: исчерпание appetite → review/cut/re-shape.
  kill_by: |
    2026-07-24 либо 11 легов, что раньше → обязательный review. Immediate review, если M1-A1
    не даёт bit-exact/no-pop в одном bounded slice или требует вскрыть лок. Финальный профиль:
    ≤50 ms green; 50–100 ms owner decision; >100 ms, desync или meaning-loss = not done.
  forecast: |
    Первый ранний сигнал — M1-A0 даёт byte-neutral observability параллельно Phase 0; следующий —
    M1-A1 доказывает либо опровергает самый опасный S4 handoff до оплаты большого уровня.
    Сохранённые S4-швы и Sc-kernel делают ступени 0–4 вероятными.
  against: |
    S4 — новый far-representation, а не body swap; реальная input-bus wiring, DA-авторинг и
    all-filled слабый пир могут съесть appetite. Merge/G5 остаются полными; продления нет.
  cut_list:
    - Sc-damage остаётся HELD; нет damage/consequence.
    - Нет врагов, миссии, баланса, production UI/audio/VFX и новой газовой энциклопедии.
    - Только один контролируемый стеновой пролом; пол/потолок и полная разрушаемость вырезаны.
    - Нет save/load, late join, matchmaking и host migration.
    - Один Полигон и минимальный DA module set; не контент-производство.
  lens_verdicts:
    commercial_traction: M1-10 — capture-пакет для существующих visual/marketing линий.
    core_gameplay_depth: M1-5..7 — tracking, reactions, breach.
    coop_first: M1-9 — честный прогон на двух реальных машинах.
    technical_feasibility: Lv-ingest + M1-A0 + M1-A1, затем M1-2..4.
    scope_production: "not_needed: cut_list + один уровень держат solo-scope."
    audience_workflow: M1-10; отдельная соцсеть-задача не нужна.

tasks:
  - id: Lv-ingest
    goal: |
      Phase 0 завершает deterministic authoritative gas-source seam на hand-tagged уровне,
      чтобы Phase 1 DA и Полигон использовали тот же reader/seeder.
    done_when: |
      c-exec-lv-ingest-phase0-001 закрыт по собственному done_when: source→flow owner-eye,
      byte-identical authoritative injection, -Deliver green и binding fresh G5.
    status: active
  - id: M1-A0
    goal: |
      Ядро отдаёт canonical read-only ActiveCell snapshot и счётчики шага без изменения
      authoritative state, tick result или MeaningChecksum.
    done_when: |
      c-exec-poligon-a0-001 закрыт по work/c-exec-poligon-a0-001-build-call.md; exact
      owner-approved frozen PLAN @f80bf700, independent RED-first test-author, worktree core
      проверен, overlap с Phase 0 нулевой, observer OFF/ON byte-identical, merge slot 2.
    status: open
  - id: M1-A1
    goal: |
      Одна labelled region проходит fine→collapsed→fine exact/no-pop, а cheap digest
      чувствителен к authoritative meaning и открывает следующие S4-леги.
    done_when: |
      c-exec-poligon-s4-opening-001 закрыт по work/c-exec-poligon-s4-opening-001-call.md:
      owner-approved PLAN, RED battery, exactness, digest cost, owner-eye, -Deliver и fresh G5.
    status: blocked
    unblock_when: c-exec-lv-ingest-phase0-001 MERGED и c-exec-poligon-a0-001 MERGED.

open_calls:
  - id: c-exec-poligon-a0-001
    to: executor
    for: g-9c41 / M1-A0
    issued: 2026-07-10
    call: work/c-exec-poligon-a0-001-build-call.md
    note: |
      FIRE-READY separate BUILD-only in C:\projects\Unity\GasCoopGame_core (branch core) по exact
      frozen PLAN/base f80bf700c26376edb7965eef3481cc04607834c3; owner approval =
      owner-chat-2026-07-10-c-exec-poligon-a0-001-plan-approved. Сначала отдельный independent
      RED-first test-author, builder эти тесты не редактирует. BUILD может идти параллельно Phase 0
      только после zero-overlap preflight; любое пересечение с Phase-0 diff или hot Core → STOP.
      Merge slot 2 строго после Phase 0 MERGED: rebase на fresh origin/main, полный rerun и binding G5.
      LAUNCH: lane A · core/headless · ПК · frozen base f80bf700c26376edb7965eef3481cc04607834c3.
  - id: c-exec-poligon-s4-opening-001
    to: executor
    for: g-9c41 / M1-A1
    issued: 2026-07-10
    call: work/c-exec-poligon-s4-opening-001-call.md
    note: |
      BLOCKED до c-exec-lv-ingest-phase0-001 MERGED + c-exec-poligon-a0-001 MERGED. Bounded S4
      micro-proof: одна labelled region, exact collapse/expand, cheap digest, owner-eye no-pop;
      production room-rollup/auto-subpartition остаются следующими легами. Merge slot 3.
      LAUNCH: lane A · GasCoopGame_core/core · ПК · base = merged tip обоих deps · fresh G5.
  - id: c-exec-lv-ingest-phase0-001
    to: executor
    for: g-9c41 / Lv-ingest (Phase 0)
    issued: 2026-07-09
    call: work/c-exec-lv-ingest-phase0-call.md
    note: |
      READY fresh GasCoopGame_dev BUILD leg. Canon-independent engine infrastructure while Sc-damage is design-held.
      Base = GasCoopGame origin/main @defade72 (§Re-sync at tip). Phase 0 = the engine-free gas-source seam on
      HAND-TAGGED geometry (100% code/MCP, NO Dungeon Architect authoring): GasSourceMarker + GasSourceSpec +
      BuiltSceneGasSourceReader + GasSourceSeeder + LatticeQuantize.ContainingCell + MOVE continuous source injection
      out of the VoxelSandboxDirector render adapter INTO the authoritative sim step (inside the MeaningChecksum);
      test scene (2 rooms + door + source) → gas flows from the placed source through the door. Discipline: contract
      v19 PLAN/BUILD split, independent RED test-author, deterministic integer path + both scans, -Deliver green,
      fresh cross-family G5. Boundaries: no real DA build / no DA authoring / no DungeonArchitectRoomReader (Phase 1),
      no multiplayer seed handshake (Phase 1+), no new gas types / visual / damage. MCP rule (owner hard): build via
      Unity-MCP where possible, else STOP + step-by-step owner instructions, NO crutch; Unity/MCP unavailable → STOP.
      Reads: knowledge/g9c41-da-level-ingestion-plan.md + g9c41 SPEC. On GREEN → Phase 1 (real DA) frames.
      LAUNCH: lane D · venue GasCoopGame_dev (dev) · mq-слот 1. 2026-07-10 (owner): лег В РАБОТЕ —
      доделывается, впереди code review; dev worktree ЗАНЯТ этим легом до мержа (правило 1 карты
      knowledge/g9c41-lanes-venues.md). DA Phase 1 заблокирован до мержа + owner-гейта.
  - id: c-shape-sc-damage-001
    to: session
    for: g-9c41 / Sc-damage
    issued: 2026-07-09
    call: work/c-shape-sc-damage-call.md
    note: |
      READY shape session (play: shape) for the next gas slice Sc-damage — the FIRST gas CONSEQUENCE that consumes the
      Sc-sense accumulated dose. Owner-present; the produced executor CALL mandates contract v19 (PLAN/BUILD split +
      independent RED test-author). Base = GasCoopGame origin/main @defade72 (§Re-sync at tip). Reads: Sc-sense wiring
      contract (dose read/integration + detection socket + UNWIRED-into-SimInstance note) at
      knowledge/g9c41-sc-sense-delivered-unwired.md, the g9c41 SPEC, engineering contract. Fold the co-op-interdependence
      axis (decision d-coop-interdependence-repin-001) into the Sc-damage framing. Goal = a fire-ready Sc-damage executor
      CALL. Boundaries: SHAPE only (produces the CALL, builds nothing); no new gas types; no visual pipeline.
      LAUNCH: lane OS-чат · READY (дизайн, owner-present). Обязательные оси: owner-eye «одна честная струя
      в открытом поле без стен»; Sc-reactions «два облака → телеграф → взрыв» НЕ закрывает отсутствующее
      open-space/no-walls свидетельство; кросс-типовая общая ёмкость решается не позже Sc-damage PLAN.
  - id: c-visual-009
    to: executor
    for: g-7e15 / VISUAL Stage 3.5 movement-data PLAN
    issued: 2026-07-10
    call: work/c-visual-009-movement-data-plan-call.md
    note: |
      READY fresh owner-present PLAN-only product session after c-visual-008 reached its frozen
      stop-needs-new-data branch (NOT DELIVERED). Select the honest simulation-derived movement seam: previous/current
      density + tick interpolation versus a separate read-only resource derived from existing signed per-face flux;
      decide whether density history is complementary, and explicitly split or couple half-res blur/upsample plus
      dense-core shaping. Preserve GridView meanings and the 128-byte GpuGasParams ABI; no new physics, feedback,
      render tuning, tests, BUILD or Stage 4. Product preflight observed origin/main@a644e5db while dev2@a48883b5 was
      stale/diverged with untracked c-visual-008 closure evidence; verify latest main and reconcile that evidence first.
      LAUNCH: lane B · venue GasCoopGame_dev_2 (dev2, редактор №2) · PLAN-only, owner-present · base: сверить
      свежий origin/main (§Re-sync) · mq: PLAN не мержится · conflict: рендер-путь — будущее рендер-окно
      Полигона идёт в ЭТОЙ ЖЕ линии, последовательно.
  - id: c-repair-minimum-game-frame-001
    to: session
    for: g-d3a8 / Minimum Game Frame
    issued: 2026-07-10
    call: work/c-repair-minimum-game-frame-001-call.md
    note: |
      READY owner-present text-only repair of the missing shared design basis.
      The owner accepted a Minimum Game Frame before any detailed design question and
      explicitly rejected mere compilation of old documents: existing files are
      evidence, while every weight-bearing frame block must be discussed against the
      owner's current view.
      The frame must state the game globally and locally, expose genuine macro forks,
      preserve but not auto-promote DESIGN ANCHORS, run applicable paper mechanic and
      CHARTER checks, and return FRAME READY / FRAME REVISED / FRAME BLOCKED.
      No canon or process installation, detailed gas-state/Bubble-fill/Sc-damage answer,
      graph rebuild, Unity or product work.
      LAUNCH: lane OS/канон-чат · owner-present · text only · no worktree or Unity.

recurring: []

parallel_tracks:
  - id: g-7e15
    track: VISUAL / GASG
    state: |-
      active — Stage 3 DONE + PUSHED (c-visual-007 delivered on GasCoopGame_dev_2 dev2@1c99a907 and merged+pushed
      to GasCoopGame origin/main@9d6f8ded; one real gas on the Stage 2 half-res path; owner choices band 2 and opacity
      ceiling 0.72; LP1-LP5 pass with caveats; no fake visual-only jet; Core/sim diff empty). c-visual-008 terminated
      2026-07-10 as STUCK / stop-needs-new-data, NOT DELIVERED: render-only motion became visible/smoother but owner
      rejected the solid dense center emitting side wisps; half-res blur remained; rejected product candidate removed.
      c-visual-009 is FIRE-READY as a PLAN-only movement-data contract over current origin/main: choose density-history
      interpolation versus/read alongside a separate flux-derived read-only movement resource, and decide whether
      blur/upsample plus dense-core shaping split into a later render-only leg. Stage 4 remains unopened.
    plan: work/gas-visual-plan-v2-2026-07-02.md
  - id: g-d3a8
    track: canon/design
    state: |-
      CANON/DESIGN FRAME REPAIR READY / DETAIL PILOT DEFERRED 2026-07-10

      The failed paper pilot remains REVISED / BLOCKED under the owner's verdict:
      «revised — добавить обязательный гейт “откуда вопрос и почему сейчас”».
      Its service-connector, damper and A/B/C output remains invalidated and has no
      game-design, DESIGN ANCHOR or canon status.

      The owner accepted a prior missing gate before question origin:
      a current owner-discussed Minimum Game Frame must explain the game coherently at
      global and local levels before any detailed design question is selected.

      The frame is not a compilation of prior documents. Owner correction:
      «не то, что мы собрали рамку из существующих документов, а чтобы мы еще обсудили».
      Existing files are evidence because some earlier concept views may have changed.

      Fixed foundations remain gas simulation, reactions and destructible/changeable
      space. Bubble, three phases, sleeping-gas reconnaissance and other owner-liked
      material remain DESIGN ANCHORS: mandatory to surface, legal to revise or reject
      explicitly, illegal to lose or silently harden into canon.

      The paper pilot specification now has two ordered pre-generation gates:
      Gate F = current Minimum Game Frame, returning FRAME READY / FRAME REVISED /
      FRAME BLOCKED;
      Gate Q = question origin/currentness, returning QUESTION READY /
      QUESTION BLOCKED.

      No detailed-question selection, local criteria, shared scene or candidate
      generation is legal before both gates are READY.

      The former direct Sc-damage paper-pilot proposal is not registered.
      The existing c-shape-sc-damage-001 route remains unchanged; this repair neither
      activates it as the design pilot nor alters its current watchmen-added evidence
      requirements. It may become a later canon/design question only if the finished
      frame derives it through Gate Q.

      Canon Forge v2 remains suspended. core-0/core-1 remain HOLD source material.
      No canon or process installation occurred.

      Next canon/design session =
      c-repair-minimum-game-frame-001.
  - id: g-2f8c
    track: marketing
    state: parked — latest history/2026-06-29-s-marketing-restart-001.md; wake pending (decision d-marketing-wake-001)
  - id: codex-sidecar
    track: CODEX SIDECAR / LAB
    state: active (process only, no build task) — plays/codex-sidecar.md; ledger work/codex-sidecar/board.md

decisions:
  - id: d-marketing-wake-001
    q: |
      Every 2026-08-31 Steam-page prerequisite sits on PARKED nodes with no wake date; a
      ready restart CALL exists (history/2026-06-29-s-marketing-restart-001.md) but is
      undated. Wake g-2f8c by ~2026-07-20, or re-date 08-31 explicitly?
    options:
      - Wake by ~07-20 (positioning + artifact card + capsule-pipeline decision; capsule = hard external lead time).
      - Re-date 08-31 explicitly now (accept Q1–Q2 2027 EA default; Oct fest = wishlist seeding).
    recommendation: Pick one consciously; silently missing 08-31 is the worst branch.
    source: work/review-gas-sim-visual-2026-07-02.md; work/marketing/questions/q-foundation.md.
  - id: d-coop-interdependence-repin-001
    q: |
      Where should the dropped "gas world forces co-op" obligation live so it does not
      become a late hard blocker?
    options:
      - Fold into Sc-reactions / Sc-damage PLANs as a required owner-eye/gameplay axis.
      - Recreate as a separate map node before the first co-op gameplay slice.
      - Defer until the first Steam/playtest slice.
    recommendation: Fold into Sc-reactions / Sc-damage PLANs now (first real gas consequences = where interdependence becomes testable).
    source: work/gas-engine-plan-audit-2026-06-29.md; work/now-snapshot-2026-06-29.md.
next:
  CALL c-exec-poligon-a0-001 → work/c-exec-poligon-a0-001-build-call.md
  # Параллельно, ничего не занимает (owner «да» 2026-07-10, s-pgg-analysis-001):
  - CALL c-spike-pgg-001 → work/c-spike-pgg-001-call.md  # УРОВНИ/D-разведка: таймбокс-спайк PGG ≤3 дня (бросовый Unity-проект); вердикт = work/pgg-analysis-2026-07-10.md; PASS → PLAN шага M1-4
    # CHECKPOINT s-spike-pgg-001-cp1: PGG_Spike компилируется после двух scratch-only fixes; PASS/FAIL не вынесен.
    # resume: history/2026-07-10-s-spike-pgg-001-cp1.md; первый unblock = owner Authorize в AI Game Developer.

END_OF_FILE: live/indie-game-development/NOW.md
