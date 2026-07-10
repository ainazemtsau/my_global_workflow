# NOW — indie-game-development
updated: 2026-07-10 by s-work-canon-process-v3-publish-002

bet:
  node: g-9c41
  goal: |
    Networked co-op gas CORE on the character road: Sc-types → Sc-weight → Sc-rep →
    Sc-kernel → Sc-reactions → Sc-sense → Sc-damage (slot after Sc-reactions RE-SCOPED 2026-07-08:
    Sc-catalog/type-authoring kit PARKED until canon gives a real roster; Sc-sense pulled forward as the
    canon-independent player↔gas exposure/dose foundation). Sc-reactions DELIVERED + MERGED to GasCoopGame
    main @484084a and PUSHED 2026-07-07 (merge 8ef6a8e of dev@f5ba86a; origin/dev also @f5ba86a). c-exec-021
    close-verified: engine 180/180 reaction+byte-identity GREEN first-hand + `check.ps1 -Deliver` GREEN
    end-to-end on dev, merged main GREEN on inner-loop check.ps1; owner-confirmed cross-family G5 / owner-eye /
    DELIVERED-authorization. Product result doc flipped DELIVERED→MERGED. Sc-sense executor CALL c-exec-035
    framed + hardened from the interrupted Claudia/Codex handoff: fresh GasCoopGame_dev PLAN, owner present, PLAN/BUILD
    split, independent RED test-author. It builds only actor-position/volume → authoritative-near-field exposure →
    integer accumulated dose + a separate player-kinematics/dose digest + Unity capsule debug readout; NO damage,
    NO detection gameplay, NO visual pipeline, NO new gas types. Sc-catalog executor CALL c-exec-034 is preserved
    PARKED for later; env-derived dynamic typing PARKED as a later slice (socket-aware). The accidental
    parallel framing c-exec-033 (s-work-sc-typing-call-001, wrong chat) is SUPERSEDED per owner.
    Far-tier S3/S4/S5 scale plumbing parked until levels get big.
    Sc-sense DELIVERED + close-verified 2026-07-09 (s-review-sc-sense-close-001): builder handback c-exec-035
    (Codex GPT-5 build + GPT-5.5 review) treated as evidence and verified by a fresh cross-family Claude binding G5 —
    9/9 refuters could-not-refute + first-hand check.ps1 GREEN 1525/1525 at GasCoopGame main/origin @defade72
    (dev FF-merged to main; both pushed) + owner «PLAN одобрял» / «капсулу сам гонял — доза росла». c-exec-035 CLOSED.
    Road now rolls to Sc-damage (consumes the dose → first gas consequence), ready as shape CALL c-shape-sc-damage-001.
    Latest session: s-review-sc-sense-close-001 (see LOG.md / history/).
    2026-07-09 (s-shape-lv-ingest-001): Sc-damage HELD (needs design; canon core re-assembling). Owner directed a
    canon-INDEPENDENT engine slice instead — Lv-ingest (level ingestion + object/gas-source placement via Dungeon
    Architect SnapGridFlow → our engine-free grid). Researched (wf_745d3a1f); SnapGridFlow confirmed; two-phase plan
    (Phase 0 = hand-tagged seam via code/MCP, Phase 1 = real DA authoring). Lv-ingest now the recommended active engine
    work; c-exec-lv-ingest-phase0-001 ready. Plan: knowledge/g9c41-da-level-ingestion-plan.md.
  appetite: |
    Governed by the g-9c41 de-risk wall; do not extend a bet silently. If a slice
    overruns or reveals a core blind spot, stop and re-shape/review, don't stretch.
  kill_by: |
    De-risk wall CLOSED 2026-07-02 (real hangar measurement = linear roster scaling;
    re-shaped d-sparse-tick-kernel-001, owner «да»). 2026-07-24 = visible-gas milestone
    (telegraph+bang and/or two-type visual on the real sim); tail movable.

tasks:
  - id: Sc-reactions
    goal: |
      Integer chemistry (explicit-SET > AXIS > env-DEFAULT > identity; telegraph+bang;
      layered mass-conserving overflow; extensible warning-kind + outcome registries). ENGINE-ONLY.
    done_when: |
      c-exec-021 close-verified 2026-07-07 (s-review-sc-reactions-close-001): reaction+byte-identity
      180/180 GREEN first-hand at dev@a23183f; no core/tools/golden change after code-tip 0259bcf
      (post-tip = ReactionSandbox render scene + docs only); owner-confirmed IN-SESSION — cross-family
      (Codex) G5 final pass could-not-refute on current code + owner-eye ReactionSandbox accepted +
      DELIVERED authorized. dev→main merge+push OWNER-GATED (outside done_when, still pending).
    status: done
  - id: Sc-catalog
    goal: |
      Data-defined DISTINCT gas types: several genuinely-different types authored AS DATA, each carrying its own
      laws via an EXTENSIBLE per-type param set (a new param = data, ZERO Core/** edit), inheriting common→meta→type,
      folded into the handshake; reactions between them on the Sc-reactions engine; + fix the handler-into-production-
      tick gap so authored reaction outcomes fire. ENGINE-ONLY. (Re-scoped 2026-07-08 from "Sc-typing"/env-derived
      typing per owner reframe; env-derived typing PARKED as a later slice, socket-aware.)
    done_when: |
      PARKED 2026-07-08 by s-shape-sc-sense-001 before firing. Ready artifact remains at
      work/c-exec-034-sc-catalog-call.md and returns when canon/design gives a real gas roster / authoring need.
      Original done_when preserved in that CALL: data-defined distinct gas types, extensible per-type laws, reactions
      between them, handler-into-production-tick fix, deliver gates, fresh-session G5, owner-eye confidence.
    status: parked
  - id: Sc-sense
    goal: |
      Player↔gas exposure/dose foundation: one or more player-actors (first owner-eye actor = ordinary Unity capsule,
      engine-side = integer position/volume) read per-type exposure from the AUTHORITATIVE NEAR gas field and integrate
      integer accumulated dose over time, deterministically under input-lockstep. The slice records the first
      player-kinematics/dose digest seam so divergent actor position or dose desyncs loudly. ENGINE-ONLY with Unity
      debug readout; NO damage/consequence, NO detection gameplay, NO visual pipeline, NO new gas types.
    done_when: |
      Executor CALL c-exec-035 returns DELIVERED from a fresh GasCoopGame_dev leg: owner-readable PLAN approved in its
      own session (contract v19), independent RED test-author first in a separate BUILD session; exposure reads
      VoxelField/authoritative-near ConcentrationAt per TypeId (not IGasReadModel/2-band); actor position enters as
      lockstep input with explicit input schema; integer clamped dose accumulates on presence and stops outside gas;
      player-kinematics/dose digest catches divergent actor position or dose while no-actor gas MeaningChecksum stays
      byte-identical; consequence-free + detection socket only; zero-float/int-overflow scans and loopback determinism
      green; `check.ps1 -Deliver` green; fresh-session G5 could-not-refute; owner sees a capsule move through gas with
      live readout: in gas → dose rises, out → dose stops, different gas → different readout. On close verification the
      road rolls to Sc-damage.
      CLOSE-VERIFIED 2026-07-09 (s-review-sc-sense-close-001): binding fresh cross-family (Claude) G5 could-not-refute
      on all six claims (9/9 refuters) + first-hand check.ps1 GREEN 1525/1525 at GasCoopGame @defade72 + Field.Sense
      31/31 + mutation 70.26% + ADR-E-0008 + owner «PLAN одобрял» (v19 PLAN approval) / «капсулу сам гонял — доза росла»
      (owner-eye). -Deliver red at tip ONLY on the pre-existing MERGED-doc fallback (c-exec-021/c-visual-005), not
      Sc-sense (c-exec-035.md passes its own gate). Engine-only foundation is UNWIRED into SimInstance — wiring is
      Sc-damage's job (feed the committed post-step field once per sim tick; see
      knowledge/g9c41-sc-sense-delivered-unwired.md).
    status: done
  - id: Lv-ingest
    goal: |
      Level ingestion + object placement: a generated (Phase 1: Dungeon Architect SnapGridFlow) or hand-tagged
      (Phase 0) level is parsed into the AUTHORITATIVE gas grid at game start, with gas SOURCES placed as objects
      (a GasSourceMarker, DA marker/theme-native) and seeded into the sim DETERMINISTICALLY in the authoritative,
      engine-free path (inside the lockstep checksum). Canon-INDEPENDENT engine infrastructure, pulled in while
      Sc-damage is design-held (owner-directed 2026-07-09). SnapGridFlow chosen (owner-confirmed: most advanced
      room/module-based 3D flow; our BuiltSceneRoomReader already reads it generator-blind). Plan + gotchas:
      knowledge/g9c41-da-level-ingestion-plan.md.
    done_when: |
      Phase 0 (c-exec-lv-ingest-phase0-001) returns DELIVERED: on a hand-tagged test scene (2 rooms + door + 1
      gas-source marker) gas flows from the placed source through the door; the engine-free source seam
      (GasSourceMarker + GasSourceSpec + BuiltSceneGasSourceReader + GasSourceSeeder + LatticeQuantize.ContainingCell)
      is deterministic + integer + in the AUTHORITATIVE sim step (continuous injection MOVED out of the render adapter,
      folded in the MeaningChecksum); RED-first independent tests; -Deliver green; fresh-session cross-family G5
      could-not-refute; owner sees source→flow. On GREEN, Phase 1 (real DA SnapGridFlow: minimal modules +
      LevelBootstrap runtime Build + seed/ProfileHash session handshake, SAME reader unchanged) frames. Two gotchas
      (recorded): DA ships ZERO content (Phase 1 = owner-manual DA authoring), and current source-injection is outside
      the checksum (Phase 0 moves it in). MCP rule: build via MCP where possible, else step-by-step owner instructions
      — no crutches.
    status: active

open_calls:
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
      LAUNCH: lane OS-чат · HELD (дизайн) · c-repair-watchmen-001 обязан дописать сюда ось «armed open-space jet»
      + шов межтиповой ёмкости ДО запуска.
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
  - id: c-repair-canon-process-v3-question-origin-gate-001
    to: session
    for: g-d3a8 / canon-process-v3 question-origin repair
    issued: 2026-07-10
    call: work/c-repair-canon-process-v3-question-origin-gate-001-call.md
    note: |
      READY owner-present repair. Evidence: history/2026-07-10-s-pilot-canon-design-process-v3-paper-001.md;
      owner verdict = REVISED / BLOCKED because the pilot invented its starting question, priority and terms.
      Reconcile the stale PILOT READY route, add the mandatory pre-generation gate “откуда вопрос и почему
      сейчас”, and prepare one new text-only pilot CALL from a real state-derived question. The discarded
      service-connector/damper/A-B-C material has no design-anchor or canon status. No process installation,
      canon freeze, core-0/core-1 answer, graph rebuild, implementation or test work.
      LAUNCH: lane OS/канон-чат · owner-present · без worktree и Unity · параллелен инженерным линиям.

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
      PAPER-ONLY PROCESS PILOT REVISED / BLOCKED 2026-07-10
      Owner verdict in s-pilot-canon-design-process-v3-paper-001: «revised — добавить обязательный
      гейт “откуда вопрос и почему сейчас”». The pilot invented its starting mechanic question,
      priority, scene and vocabulary; service-connector/damper/A-B-C output is invalidated and has
      no game-design, DESIGN ANCHOR or canon status. Mandatory revision candidate: before any local
      criteria or generation, show where the question sits in the game/core loop, the exact unresolved
      player decision, its source, why it is current/what it blocks, provenance of every introduced
      entity, and explicit non-scope; gate result READY or BLOCKED. Canon Forge v2 remains suspended;
      core-0/core-1 stay HOLD; fixed foundations and DESIGN ANCHORS are unchanged. No canon/process
      installation occurred. Next = owner-present repair CALL c-repair-canon-process-v3-question-origin-gate-001.
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
  # ПАРАЛЛЕЛЬНЫЕ ЛИНИИ установлены 2026-07-10 (owner «подтверждаю»; s-lanes-install-001):
  # карта площадок = knowledge/g9c41-lanes-venues.md (правило 1: трек стартует только с проверенным worktree);
  # борд = play local/lanes-board — владелец в любом чате: «что можем делать».
  # Полигон М1 = ближайшая цель владельца (2026-07-10); пересборка ставки — c-shape-poligon-m1-001.
  - CALL c-shape-poligon-m1-001 → work/c-shape-poligon-m1-001-call.md  # ЯДРО/A: пересборка ставки под Полигон М1 + первые S4-леги (owner-present) — РЕКОМЕНДУЕМЫЙ СТАРТ
  - CALL c-lab-p0-001 → work/c-lab-p0-001-call.md                      # СТЕНД/C: верстак v0 (НОВЫЙ worktree lab; первым шагом — решение D1 у владельца)
  - CALL c-prep-net-spike-001 → work/c-prep-net-spike-001-call.md      # СЕТЬ/E: подготовка спайка двух реальных машин (headless)
  - CALL c-repair-watchmen-001 → work/c-repair-watchmen-001-call.md    # OS: вернуть сторожей масштаба + потолок SPEC 35k→27.7k + ось в Sc-damage CALL
  # Уже в работе / прежние фронты:
  - CALL c-exec-lv-ingest-phase0-001 → work/c-exec-lv-ingest-phase0-call.md  # ЛИНИЯ D: Phase 0 В РАБОТЕ (доделывается + code review); dev занят
  - CALL c-visual-009 → work/c-visual-009-movement-data-plan-call.md  # ЛИНИЯ B: PLAN-only movement seam (dev_2, owner-present)
  - CALL c-shape-sc-damage-001 → work/c-shape-sc-damage-call.md      # GAS: HELD (дизайн) — после c-repair-watchmen-001
  - CALL c-repair-canon-process-v3-question-origin-gate-001 → work/c-repair-canon-process-v3-question-origin-gate-001-call.md
    # CANON PROCESS: owner-present repair after REVISED/BLOCKED pilot; text-only, no canon/process install

END_OF_FILE: live/indie-game-development/NOW.md
