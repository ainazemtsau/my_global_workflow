# NOW: indie-game-development
updated: 2026-07-11 by s-repair-player-puppetmaster-p2a0-001

bet:
  node: g-9c41
  goal: |
    Полигон М1 доказывает representative networked co-op scene: регулируемый DA-уровень,
    gas gameplay, S4, controlled breach, full flood, две реальные машины и слабое железо.
  appetite: |
    Максимум 13 product legs, started 2026-07-10; разовая owner-authorized exception 2026-07-11
    для M1-GAS-PROBE + M1-GAS-CORE, дальнейшего автоматического продления нет. Checksum foundation
    занимает один слот, а будущие M1-9 + M1-10 остаются одним final evidence leg. P2a0 — risk-first
    opening уже существующего M1-5 player-tracking leg, не 14-й leg; остаток M1-5 не продлевается молча.
  kill_by: |
    2026-07-24 либо 13 легов, что раньше; immediate review, если M1-GAS-PROBE не даёт
    deterministic mass-exact bounded body/no-tail или M1-A1 не даёт bounded exact/no-pop.
    Финальный профиль: ≤50 ms green; 50–100 ms owner decision; >100 ms/desync/meaning-loss = not done.
  forecast: |
    После Phase 0 MERGED checksum foundation убирает legacy full-scan polling, successor A0 даёт
    дешёвую observability, затем M1-GAS-PROBE выбирает закон, M1-GAS-CORE меняет authority,
    c-visual-009 разблокируется, и только после этого M1-A1 проверяет S4 handoff. Параллельно P2a0
    в disposable lab проверяет player root authority и сетевую пригодность до production controller.
  against: |
    Packed-body law может не пройти determinism/no-tail или прочитаться как вода; dirty visual BUILD
    потребует fresh rebase. S4, DA-authoring и weak-peer flood всё ещё могут съесть appetite;
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
    technical_feasibility: Phase 0 + checksum foundation + successor A0 + M1-GAS-PROBE/CORE, затем A1 и M1-2..4.
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
  - id: M1-P2a0
    goal: |
      PuppetMaster получает проверенный root-authority маршрут для сетевого игрока, которого могут
      физически сбивать камни и импульсы, до заморозки production controller.
    done_when: |
      c-exec-player-puppetmaster-p2a0-001 возвращает compile/runtime proof текущего допустимого plugin,
      transition evidence Puppet→Unpinned→GetUp, A/B comparison + C kill-probe, multiplayer authority
      inventory и fresh independent refutation; без FishNet BUILD, gameplay damage и product merge.
    status: active

open_calls:
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
    for: g-7e15 / Stage 3.5 movement-data BUILD reconciliation
    issued: 2026-07-10
    note: "BLOCKED on M1-GAS-CORE: approved PLAN @a0db28a2 + dirty BUILD preserved on codex/c-visual-009-build; no continuation/close; history/2026-07-11-s-repair-visual-sim-upstream-001.md."
  - id: c-exec-player-puppetmaster-p2a0-001
    to: executor
    for: M1-P2a0 / PuppetMaster authority suitability spike
    issued: 2026-07-11
    note: "READY: lane C disposable lab, base origin/main@a644e5db, no product merge; folded into M1-5; work/c-exec-player-puppetmaster-p2a0-001-call.md."
recurring: []

decisions:
  - q: "d-marketing-wake-001 — wake g-2f8c by ~2026-07-20 or explicitly re-date the 2026-08-31 Steam-page prerequisite?"
    options: ["Wake by ~07-20", "Re-date 08-31 explicitly"]
    recommendation: "Choose consciously; silently missing 08-31 is the worst branch. Source: work/marketing/questions/q-foundation.md."
  - q: "d-coop-interdependence-repin-001 — where should the dropped 'gas world forces co-op' obligation live?"
    options: ["Fold into Sc-reactions/Sc-damage PLANs", "Create a separate map node", "Defer to first Steam/playtest slice"]
    recommendation: "Fold into Sc-reactions/Sc-damage PLANs; source: work/gas-engine-plan-audit-2026-06-29.md."
  - q: "d-level-platform-phasing-001 — how should Lv-ingest be re-phased after the PGG production-pipeline FAIL_STAGE?"
    options: ["Clean rephase: Phase 1 = generic level/module contract + validators; old DA/PGG runtime Phase 1 becomes Phase 2; production extensions/content become Phase 3", "Keep historical numbering as Phase 1A = contract/validators and Phase 1B = adapters/runtime; Phase 2 = production extensions/content", "Keep current Phase 1 unchanged and add the generic standard later"]
    recommendation: "Clean rephase: the generic contract and validators are prerequisites for DA/PGG adapters and must reserve full 3D, module!=room, compound modules with 1:N logical rooms, and six-direction connections before vendor integration; putting the standard after current Phase 1 repeats the spike's build-before-contract failure. Source: work/level-platform-phasing-2026-07-11.md."
next:
  CALL: work/c-exec-lv-ingest-phase0-call.md

END_OF_FILE: live/indie-game-development/NOW.md
