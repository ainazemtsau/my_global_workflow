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
