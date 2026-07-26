RESULT s-repair-poligon-a0-checksum-route-001 (call: owner-message-2026-07-10-checksum-before-a0)
direction: indie-game-development   play: repair   node/task: g-9c41/M1-A0

outcome: |
  c-exec-poligon-a0-001 получил терминальный Direction-OS disposition returned STOP/checkpoint,
  явно NOT DELIVERED. Старый frozen PLAN/base/CALL остаётся неизменной историей и не возобновляется.
  M1-A0 остаётся незавершённым и blocked на Phase 0 MERGED, checksum foundation и новый
  owner-approved successor A0 PLAN; M1-A1 blocked на те же зависимости плюс successor A0 delivery.
  NOW.md возвращён к 98-строчной схеме с одним next; фиксированный appetite 11 легов сохранён
  через выбранное владельцем объединение будущих M1-9 + M1-10.

evidence: |
  Owner sequencing verdict: «Я согласен с твоими рекомендациями. Сейчас давай, я так понимаю,
  что мы сначала должны реализовать вот этот новый сервис по чек-сумме и потом продолжить работу
  над нашей задачей текущей.»
  Repair step-4 brief presented one batched corrected-state diff with variants А/Б and explicitly
  asked for approval of the whole variant. Owner actual reply: «А».

  Product evidence read first-hand from C:/projects/Unity/GasCoopGame_core:
  - branch core clean at 0d2a8ae7084434f46a795efbd913d4c784ed17f3, four commits ahead of
    origin/main@a644e5db538d1102f726630d6a4ac2f3f1bdcf5a;
  - a2513505 added only the zero-overlap report, c4bb0073 added/updated only checkpoint evidence,
    and 0d2a8ae updated only docs/results/c-exec-poligon-a0-001.md;
  - docs/results/c-exec-poligon-a0-001.md says NEEDS INPUT / mandatory STOP before RED and
    production / NOT DELIVERED;
  - docs/measurements/overlap-c-exec-poligon-a0-001.md proves zero preflight overlap but the
    frozen contradiction: capture-time exact uncached MeaningChecksum requires a full-domain scan,
    while CaptureActiveCells forbids one and may touch only the new-file surface;
  - baseline tools/check.ps1 was green 1525/1525. No RED commit/transcript, production/test edit,
    -Deliver, review, post-Phase-0 rebase, binding delivery G5 or merge exists.

  Old A0 done_when reconciliation:
  1. Frozen venue/base/cleanliness/approval/baseline preflight: met and evidenced.
  2. Independent RED-first battery: not started; author interrupted before any file/commit.
  3. Pre-BUILD overlap: zero; post-BUILD overlap not reached because BUILD did not start.
  4. Snapshot/API/counters: not built.
  5. Observer parity/mutation/ordering controls: not built.
  6. Request cost/OFF cost: not measured for a built API.
  7. Full guards/-Deliver/review: baseline-only ordinary gate green; delivery gates not run.
  8. Phase-0 MERGED/rebase/final rerun/binding G5/merge: not reached.
  This closes only the returned in-flight CALL as STOP/NOT DELIVERED; it does not mark M1-A0 done.
  review-evidence: n/a - terminal STOP/NOT DELIVERED; no adopted implementation or done claim.
  G5: not claimed or waived; binding fresh G5 remains mandatory for future delivery.

  Phase 0 read first-hand from C:/projects/Unity/GasCoopGame_dev: clean dev@f30e3a38ac57102de4ff823a03550082e0d9c8ce,
  origin/main@a644e5db538d1102f726630d6a4ac2f3f1bdcf5a, HEAD is not an ancestor of origin/main;
  docs/results/c-exec-lv-ingest-phase0-001.md says NOT DELIVERED / RETRACTED. Therefore checksum
  BUILD cannot start yet; only the PLAN-only route may be prepared.

  Runtime/cost context verified first-hand: legacy MeaningChecksum is an uncached sequential FNV
  full-domain fold; RealGasViewSource polls it on each enabled Unity frame; PlayerSense computes it
  per observation; Net/FishNet contains no checksum reference. Historical
  docs/measurements/c-exec-023-kernel-scaling-matrix.json records 196,608 cells, Step 0.4045 ms and
  MeaningChecksum 28.2085 ms on strong CoreCLR; it predates the telegraph pass and is not a guarantee.

  State evidence: NOW.md was 255 lines, contained out-of-schema parallel_tracks, and its next held
  both old A0 and PGG. Every removed narrative remains recoverable at workflow commit
  89932216a7599d3e8bf15c1124a43fbb3e3b361c and in linked history/work artifacts. Pending unrelated
  calls and both pending decisions remain; c-spike-pgg-001 moved from the illegal second next into
  open_calls because its checkpoint explicitly leaves it pending.

state_changes: |
  1. REPLACE live/indie-game-development/NOW.md with the exact content between markers below;
     remove the two-space packet indentation from each content line. Marker lines are not part
     of the file.
  --- BEGIN EXACT NOW.md ---
  # NOW: indie-game-development
  updated: 2026-07-10 by s-repair-poligon-a0-checksum-route-001

  bet:
    node: g-9c41
    goal: |
      Полигон М1 доказывает representative networked co-op scene: регулируемый DA-уровень,
      gas gameplay, S4, controlled breach, full flood, две реальные машины и слабое железо.
    appetite: |
      Максимум 11 product legs, started 2026-07-10; продления нет. Checksum foundation занимает
      один слот, а будущие M1-9 + M1-10 объединены в один final evidence leg по owner «А».
    kill_by: |
      2026-07-24 либо 11 легов, что раньше; immediate review при провале bounded M1-A1 exact/no-pop.
      Финальный профиль: ≤50 ms green; 50–100 ms owner decision; >100 ms/desync/meaning-loss = not done.
    forecast: |
      После подтверждённого Phase 0 MERGED checksum foundation убирает legacy full-scan polling;
      successor A0 даёт дешёвую observability, затем M1-A1 проверяет S4 handoff.
    against: |
      Hot mutation paths, S4 handoff, DA-authoring и weak-peer flood могут съесть appetite;
      legacy exact checksum остаётся медленным oracle, а не runtime dirty/sync primitive.
    cut_list:
      - Sc-damage остаётся HELD; нет damage/consequence.
      - Нет врагов, миссии, production UI/audio/VFX и новой газовой энциклопедии.
      - Только один контролируемый стеновой пролом; нет полной разрушаемости.
      - Нет save/load, late join, matchmaking и host migration.
      - Один Полигон и минимальный DA module set; не контент-производство.
    lens_verdicts:
      commercial_traction: final evidence leg даёт capture-пакет существующим visual/marketing линиям.
      core_gameplay_depth: M1-5..7 — tracking, reactions, breach.
      coop_first: объединённый M1-9+10 — две реальные машины, sync и owner verdict.
      technical_feasibility: Phase 0 + checksum foundation + successor A0/A1, затем M1-2..4.
      scope_production: not_needed — cut_list и один уровень держат solo-scope.
      audience_workflow: final evidence leg; отдельная соцсеть-задача не нужна.

  tasks:
    - id: Lv-ingest
      goal: Phase 0 завершает deterministic authoritative gas-source seam для hand-tagged уровня.
      done_when: c-exec-lv-ingest-phase0-001 проходит собственные gates, binding fresh G5 и подтверждён MERGED.
      status: active
    - id: M1-A0
      goal: Ядро отдаёт canonical read-only ActiveCell snapshot и step counters без изменения authority.
      done_when: |
        Fresh successor change id (не c-exec-poligon-a0-001) доставляет snapshot без implicit legacy
        global checksum, проходит owner-approved PLAN, BUILD gates, review, binding fresh G5 и merge.
      status: blocked
      unblock_when: Phase 0 MERGED + checksum foundation DELIVERED/MERGED + fresh owner-approved successor A0 PLAN.
    - id: M1-A1
      goal: Одна labelled region проходит fine→collapsed→fine exact/no-pop и использует cheap synchronization digest.
      done_when: c-exec-poligon-s4-opening-001 закрыт по work/c-exec-poligon-s4-opening-001-call.md.
      status: blocked
      unblock_when: Phase 0 + checksum foundation + fresh successor A0 подтверждены DELIVERED/MERGED.

  open_calls:
    - id: c-exec-poligon-s4-opening-001
      to: executor
      for: M1-A1
      issued: 2026-07-10
      note: "BLOCKED на Phase 0 + checksum foundation + successor A0; work/c-exec-poligon-s4-opening-001-call.md."
    - id: c-exec-lv-ingest-phase0-001
      to: executor
      for: Lv-ingest
      issued: 2026-07-09
      note: "NOT MERGED/NOT DELIVERED: dev@f30e3a3, origin/main@a644e5d; work/c-exec-lv-ingest-phase0-call.md."
    - id: c-shape-sc-damage-001
      to: session
      for: Sc-damage
      issued: 2026-07-09
      note: "Pending owner-present shape CALL; current M1 cut keeps Sc-damage HELD; work/c-shape-sc-damage-call.md."
    - id: c-visual-009
      to: executor
      for: g-7e15 / Stage 3.5 movement-data PLAN
      issued: 2026-07-10
      note: "PLAN pending in a fresh product session; history/2026-07-10-s-work-067-c-visual-009-binding-checkpoint.md."
    - id: c-repair-minimum-game-frame-001
      to: session
      for: g-d3a8 / Minimum Game Frame
      issued: 2026-07-10
      note: "Pending owner-present text-only repair; work/c-repair-minimum-game-frame-001-call.md."
    - id: c-spike-pgg-001
      to: executor
      for: g-9c41 / PGG editor-time spike
      issued: 2026-07-10
      note: "CHECKPOINT/no verdict; awaits owner Authorize; history/2026-07-10-s-spike-pgg-001-cp1.md."

  recurring: []

  decisions:
    - q: "d-marketing-wake-001 — wake g-2f8c by ~2026-07-20 or explicitly re-date the 2026-08-31 Steam-page prerequisite?"
      options: ["Wake by ~07-20", "Re-date 08-31 explicitly"]
      recommendation: "Choose consciously; silently missing 08-31 is the worst branch. Source: work/marketing/questions/q-foundation.md."
    - q: "d-coop-interdependence-repin-001 — where should the dropped 'gas world forces co-op' obligation live?"
      options: ["Fold into Sc-reactions/Sc-damage PLANs", "Create a separate map node", "Defer to first Steam/playtest slice"]
      recommendation: "Fold into Sc-reactions/Sc-damage PLANs; source: work/gas-engine-plan-audit-2026-06-29.md."

  next:
    CALL: work/c-work-poligon-checksum-foundation-plan-001-call.md

  END_OF_FILE: live/indie-game-development/NOW.md
  --- END EXACT NOW.md ---

  2. ADD live/indie-game-development/work/c-work-poligon-checksum-foundation-plan-001-call.md
     with the exact content between markers below; remove the two-space packet indentation from
     each content line. Marker lines are not part of the file.
  --- BEGIN EXACT CALL ARTIFACT ---
  # CALL c-work-poligon-checksum-foundation-plan-001 — checksum foundation PLAN route

  to: session
  direction: indie-game-development
  play: work
  node: g-9c41
  task: M1-A0
  goal: |
    Для checksum foundation существует один authoritative self-contained PLAN-only executor CALL,
    готовый к owner-present product planning и к будущему fresh BUILD после Phase 0.
  context: |
    Read live/indie-game-development/NOW.md and
    history/2026-07-10-s-repair-poligon-a0-checksum-route-001.md.
    Returned frozen A0 evidence: work/c-exec-poligon-a0-001-build-call.md;
    C:\projects\Unity\GasCoopGame_core\docs\results\c-exec-poligon-a0-001.md;
    C:\projects\Unity\GasCoopGame_core\docs\measurements\overlap-c-exec-poligon-a0-001.md;
    checkpoint 0d2a8ae7084434f46a795efbd913d4c784ed17f3. Old A0 is STOP/NOT DELIVERED.

    Owner sequencing verdict: «Я согласен с твоими рекомендациями. Сейчас давай, я так понимаю,
    что мы сначала должны реализовать вот этот новый сервис по чек-сумме и потом продолжить работу
    над нашей задачей текущей.» This approves ordering, not a frozen product spec.

    Accepted planning contour:
    1. Legacy MeaningChecksum remains the exact slow audit/golden/debug oracle.
    2. Separate StateRevision serves render/snapshot dirty detection and is not called a checksum.
    3. Legacy full checksum leaves automatic per-frame/per-sense polling.
    4. Before live gas networking/S4, plan a versioned incremental synchronization digest:
       session-static digest + transactionally maintained dynamic root; ordinary root read O(1);
       no full-domain scan on a sparse ordinary step.
    5. Fast A0 activity snapshot does not call the legacy global checksum; exact legacy hash, if exposed,
       is a separate explicitly slow API.
    6. Do not turn sequential FNV into a supposedly identical incremental hash; the new digest lives beside
       it and old golden hashes remain unchanged.

    Performance evidence: docs/measurements/c-exec-023-kernel-scaling-matrix.json in GasCoopGame_core
    records 196,608 cells, Step 0.4045 ms and MeaningChecksum 28.2085 ms on strong CoreCLR; historical and
    optimistic, not a current guarantee. RealGasViewSource polls the legacy checksum each enabled Unity frame;
    PlayerSense folds it into each observation; current Net/FishNet has no checksum transport/compare path.
  boundaries: |
    This Direction session authors only the PLAN-only executor CALL. It does not design/freeze the product PLAN,
    author RED tests, create a BUILD CALL, edit product code, or claim delivery. The product Planner owns detailed
    architecture and must return an owner-readable plan for actual owner approval.
    Do not edit or reopen the old frozen PLAN/base/CALL; any future A0 continuation uses a fresh successor change id.
    PLAN-only may be routed before Phase 0 merge, but checksum BUILD may start only after Phase 0 is confirmed MERGED,
    followed by fresh origin/main rebase, full gates, review and binding fresh G5.
    Preserve the fixed 11-leg appetite: owner chose option «А», coalescing future M1-9 + M1-10 without cutting evidence.
  done_when: |
    1. work/c-exec-poligon-checksum-foundation-plan-001-call.md exists as one self-contained `to: executor`,
       `kind: engineering`, PLAN-only product CALL with a business-level goal and no play-procedure paraphrase.
    2. It carries the accepted contour above as owner direction, explicitly not as a pre-frozen implementation spec,
       and requires a detailed simple owner-readable PLAN plus actual owner approval.
    3. It permits no BUILD/RED/product implementation in the PLAN session and encodes the Phase-0 MERGED prerequisite,
       fresh origin/main rebase, full gates, review and binding fresh G5 for later BUILD.
    4. It leaves old c-exec-poligon-a0-001 immutable/closed as STOP, leaves M1-A0 blocked, and opens neither a BUILD CALL
       nor the successor A0 PLAN.
  return: |
    RESULT with the new PLAN-only executor CALL path, a short contract summary, exact evidence pointers, and explicit
    confirmation that no product file, RED test, BUILD CALL, successor A0 plan, TREE or CHARTER changed.
  budget: one session

  END_OF_FILE: live/indie-game-development/work/c-work-poligon-checksum-foundation-plan-001-call.md
  --- END EXACT CALL ARTIFACT ---

  3. APPEND exactly this one line before the LOG.md trailer:
  2026-07-10 — repair (g-9c41/M1-A0, s-repair-poligon-a0-checksum-route-001): c-exec-poligon-a0-001 recorded as returned STOP/NOT DELIVERED; NOW compacted to schema and routed through Phase-0-gated checksum foundation plus a fresh successor A0 under the fixed 11-leg appetite, with future M1-9+M1-10 coalesced by owner «А». → history/2026-07-10-s-repair-poligon-a0-checksum-route-001.md

  4. SAVE this full RESULT to
     live/indie-game-development/history/2026-07-10-s-repair-poligon-a0-checksum-route-001.md
     and maintain its END_OF_FILE trailer.
  5. TREE.md, CHARTER.md, all old A0 work artifacts, product repositories and os/**: no change.

captures:
  - CHARTER.md (211 lines) and TREE.md (342 lines) also exceed the approximate hot-file ceiling; a separate owner-present G9 hygiene repair may compact them, but this owner-scoped repair does not mix that unrelated job.
  - LOG.md is 146 lines before this repair and remains under the approximate ceiling, but its older known chronology/order drift remains the separately captured follow-up from history/2026-07-07-s-repair-log-001.md.

decisions_needed: []

play_check:
  - 1 Name the contradiction: done — old A0 FIRE-READY/next conflicted with the mandatory product STOP and owner checksum-first sequence; NOW also had a multi-call next, invented parallel_tracks field and 255-line hot-state bloat.
  - 2 Reconstruct: done — checked KERNEL/play/schema/adapter, NOW/TREE/CHARTER/LOG/history/git, old frozen CALL, product commits/docs/source/cost evidence and live Phase-0 ancestry newest-first.
  - 3 Propose corrected state: done — presented the full human diff, preserved every pending unrelated CALL/decision, supplied one exact next CALL artifact, and left TREE/CHARTER/product/old frozen A0 untouched.
  - 4 Confirm: done — the owner selected the entire presented variant with actual words «А»; appetite stays 11 by coalescing future M1-9 + M1-10 without cutting their evidence.
  - 5 Friction: done — recurrence is already named in os/FRICTION.md (2026-07-04 parallel_tracks schema drift) and history/2026-07-06-s-repair-nowmd-001.md (unrun hygiene cadence); no duplicate os/** line is added from this direction repair.

log: 2026-07-10 — repair (g-9c41/M1-A0, s-repair-poligon-a0-checksum-route-001): c-exec-poligon-a0-001 recorded as returned STOP/NOT DELIVERED; NOW compacted to schema and routed through Phase-0-gated checksum foundation plus a fresh successor A0 under the fixed 11-leg appetite, with future M1-9+M1-10 coalesced by owner «А». → history/2026-07-10-s-repair-poligon-a0-checksum-route-001.md

next: |
  CALL c-work-poligon-checksum-foundation-plan-001
  → live/indie-game-development/work/c-work-poligon-checksum-foundation-plan-001-call.md

END_OF_FILE: live/indie-game-development/history/2026-07-10-s-repair-poligon-a0-checksum-route-001.md
