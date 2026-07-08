# NOW — indie-game-development
updated: 2026-07-08 by s-designlab-gas-spatial-form-001

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
    Latest session: s-shape-sc-sense-001 (Sc-sense pulled forward; c-exec-035 ready; see LOG.md / history/).
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
    status: active

open_calls:
  - id: c-exec-035
    to: executor
    for: g-9c41 / Sc-sense
    issued: 2026-07-08
    call: work/c-exec-035-sc-sense-call.md
    note: |
      READY Sc-sense executor handoff. Base = GasCoopGame main/origin @484084a after Sc-reactions merge+push; §Re-sync
      confirms synced contract ≥18 and honours v19 behaviorally. Fresh GasCoopGame_dev PLAN, owner present; v19 split:
      PLAN closes at owner approval (no product code, no RED tests); fresh BUILD starts with an independent RED
      test-author. Scope = actor position/volume lockstep input + authoritative-near per-type exposure + integer dose
      integration + separate player-kinematics/dose digest + Unity capsule debug readout. Design-AWARE only: damage,
      breathing/«Лёгкие», detection/diagnosis gameplay, multi-actor real player controller. Boundaries: no damage/effect,
      no detection gameplay, no visual/shader/look pipeline, no new gas types, no Sc-catalog/type-authoring, no 2-band
      read dependency, no float/host-only dose, no gas MeaningChecksum layer-crossing without explicit PLAN rationale.
  - id: c-visual-007
    to: executor
    for: g-7e15 / VISUAL Stage 3
    issued: 2026-07-07
    call: work/c-visual-007-stage3-call.md
    note: |
      FIRE-READY visual-only Stage 3 ("Одна жемчужина") framed from visual plan v2 after c-visual-006 close.
      Base = GasCoopGame_dev_2 dev2@6dbdddd (Stage 2 gas passport + real two-type preview + half-res path).
      Scope: hero-polish one real gas, natural-jet fix, toon-band + opacity-ceiling decisions, LP1 lamp re-test,
      LP1-LP5 individual dispositions. Boundaries: dev_2 only; render-only; ZERO Core/**/sim/c-exec-021 work;
      primary NOW.next target unchanged. Product leg owes narrow §Re-sync to contract v19 first (owner-readable PLAN,
      PLAN and BUILD as separate sessions).
  - id: c-designlab-gas-precontact-read-001
    to: session
    for: g-d3a8 / Mechanics Workbench Q2 pre-contact read
    issued: 2026-07-08
    call: work/c-designlab-gas-precontact-read-001-call.md
    note: |
      READY next one-question Workbench Design Lab after Q1 spatial-form lab. Inherited Q1 result:
      gas before Bubble is a local shared-field area with readable edge/gradient/layer behavior; not an object,
      pickup spot, container, creature, or final VFX plate. Question = q-pre-contact-read-detection: what players can
      fairly read before touching or altering this field-area. Blocks transfer-to-Bubble fairness, first 60 seconds,
      instrument/building role, route choice, tutorial/no-tutorial, and later grey-box readability. Boundaries: no
      transfer solution, no exact tool/membrane/cargo/economy/roster/title/final VFX, no creature AI/sleep-aggro
      ontology, no HUD-number-only answer.

recurring: []

parallel_tracks:
  - id: g-7e15
    track: VISUAL / GASG
    state: active — Stage 2 DONE (c-visual-006 delivered on GasCoopGame_dev_2 dev2@6dbdddd; owner-eye/play-mode passed; real two-type preview + gas passport + half-res path; not pushed/merged by this close). Stage 3 FRAMED + FIRE-READY as c-visual-007: one-pearl/hero gas polish + natural-jet fix + LP1 re-test; visual-only/dev_2; owes §Re-sync v19 first.
    plan: work/gas-visual-plan-v2-2026-07-02.md
  - id: g-d3a8
    track: canon/design
    state: |-
      active in parallel via Mechanics Workbench, not a second active bet. Mechanics Workbench question map v0.1 is
      owner-approved (s-cartography-mechanics-workbench-questions-001, owner "вариант A"). All required draft material is
      accounted for: Bubble placed as current floor-proof candidate; `ЛЁГКИЕ`, flagship examples and title parked; quiet
      floor, detection, carry/co-op, release/reactions, tools/building and old canon salvage routed. Q1 spatial-form lab
      completed on paper (work/design-labs/gas-spatial-form-001.md): first proof uses a local shared-field area with
      readable edge/gradient/layer behavior; exact read/transfer/custody/release/reactions/anti-solo remain downstream.
      Current open design CALL is c-designlab-gas-precontact-read-001. Design Lab clears unclear blockers; worked
      gameplay mechanics later go through local/mechanic-forge; local/canon-forge freezes compact canon only when
      freeze-ready. No canon freeze; TREE/CHARTER untouched.
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
  CALL c-exec-035 → executor (GasCoopGame_dev): work/c-exec-035-sc-sense-call.md. Fresh owner-present PLAN (contract
  v19 PLAN/BUILD split), independent RED test-author first. Return RESULT HOME; dev→main merge + push owner-gated.
  Sc-catalog c-exec-034 is PARKED/preserved for later when canon gives a real roster; c-exec-033 (env-derived typing)
  SUPERSEDED per owner (accidental wrong-chat) — parked as a later slice, design preserved.
  Parallel tracks: c-visual-007 Stage 3; g-d3a8 Mechanics Workbench Q2 pre-contact read ready as
  c-designlab-gas-precontact-read-001 (Q1 result: work/design-labs/gas-spatial-form-001.md).

END_OF_FILE: live/indie-game-development/NOW.md
