# NOW — indie-game-development
updated: 2026-07-09 by s-cartography-core-concept-rebuild-001

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
  - id: c-visual-008
    to: executor
    for: g-7e15 / VISUAL Stage 3.5
    issued: 2026-07-09
    call: work/c-visual-008-stage3-5-motion-clarity-call.md
    note: |
      READY visual-only Stage 3.5 inserted before Stage 4 after owner observed dead-static idle gas, jerky/low-frame
      motion onset, and possible scene muddiness around the gas. Base = GasCoopGame origin/main@9d6f8ded with
      c-visual-007 dev2@1c99a907 already merged; visual checkout must verify/sync to that base first. Scope: audit
      current body shader/path, add honest render-only internal idle life, smooth motion onset where current data allows,
      and A/B gas-off/gas-on clarity. Boundaries: no Core/sim/network/reactions/Sc-sense edits, no fake directional jet,
      no particles/VFX as acceptance crutch, no Stage 4 character/danger work.
  - id: c-forge-q-ruki-001
    to: session
    for: g-d3a8 / canon node q-ruki (player verbs)
    issued: 2026-07-09
    call: work/c-forge-q-ruki-001-call.md
    note: |
      READY Кузница v2 session (play: local/canon-forge) on the owner-signed core-concept-rebuild map. Cluster = map
      node 1 q-ruki (МЕХАНИКА mode); node 2 q-prostranstvo admissible as co-frame if the session has room. Base = canon
      repo @b77571b: CONSTITUTION ratified (verdict «Б», edits П1–П3), QUEUE.md = the signed map, INDEX still empty (no v2
      card yet). Session reads CONSTITUTION+INDEX+QUEUE+SESSION itself (START.md). Goal = which 1–3 verbs are the player's
      hands on the gas world, delivered as a seconds-level loop with players separated, gated by
      knowledge/mechanic-lenses.md. Verdict = owner's verbatim words or an honest «обсуждается». Boundaries: no tools
      list, no bubble mechanic, no roster, no economy, no title; no engine beyond the planned road (П3). Gap → gap_event
      back to work/canon-maps/core-concept-rebuild-question-map-v0.1.md; do not invent canon.

recurring: []

parallel_tracks:
  - id: g-7e15
    track: VISUAL / GASG
    state: active — Stage 3 DONE + PUSHED (c-visual-007 delivered on GasCoopGame_dev_2 dev2@1c99a907 and merged+pushed to GasCoopGame origin/main@9d6f8ded; Stage 3 single-gas visual on the Stage 2 half-res path; owner choices recorded: toonBandCount 2, opacityCeiling 0.72; LP1-LP5 pass with caveats; no fake visual-only jet; Core/sim diff empty; c-visual-007 result-check green; main inner-loop `tools/check.ps1` green; full `-Deliver` on merged main is blocked by pre-existing c-exec-021/c-visual-005 MERGED-status docs, not by c-visual-007). Stage 3.5 FRAMED + FIRE-READY as c-visual-008: idle internal life for stationary gas, motion-onset smoothness, and environment clarity/muddiness audit; render-only; base origin/main@9d6f8ded; no fake jet; Stage 4 not opened.
    plan: work/gas-visual-plan-v2-2026-07-02.md
  - id: g-d3a8
    track: canon/design
    state: |-
      active in parallel, not a second active bet. CARTOGRAPHY DONE 2026-07-09 (s-cartography-core-concept-rebuild-001,
      CALL c-cartography-core-concept-rebuild-001). Two owner verdicts recorded verbatim:
      (a) CONSTITUTION.md RATIFIED — verdict «Б» = ratify with edits П1/П2/П3. П1: reactions are fixed material but the
      comfortable base does NOT require chasing reactions or optimizing expensive gases. П2: pillar 4 is a FILTER (if
      value exists it comes from gas + failure changes the world), NOT «extraction is the core by default». П3: pillar 6
      «zero new engine» = nothing beyond the existing sim + already-planned road. Canon repo @87a05a7.
      (b) core-concept-rebuild question map SIGNED — verdict «А» = «подписываю карту» — written as canon-repo QUEUE.md
      @b77571b (replaces the 2026-07-08 draft); full-field version at
      work/canon-maps/core-concept-rebuild-question-map-v0.1.md. 10 nodes in dependency order from the fixed foundations
      (gas sim, reactions, destructible/changeable space): 1 q-ruki (player verbs, МЕХАНИКА) → 2 q-prostranstvo (space as
      a hand, co-frame) → 3 q-motiv → 4 q-bazovaya-petlya (comfortable no-reaction-chase loop, from П1) → 5
      q-reakcii-v-baze → 6 q-proval → 7 q-koop (mechanic-lenses gate) → 8 q-cennost (conditional on motive=value) → 9
      q-fazy → 10 q-obeshanie (synthesis). Bubble/carry/tools/economy/ЛЁГКИЕ/bestiary/roster/title/old-canon all PARKED
      with explicit wake-nodes, nothing lost. Owner-approved first route = node 1 q-ruki via local/canon-forge (Кузница
      v2), node 2 admissible as co-frame; next CALL c-forge-q-ruki-001 ready. No canon card frozen (INDEX still empty).
      TREE/CHARTER untouched. Gap rule: a forge session hitting a hidden prerequisite / unclear question / wrong
      answer-shape / owner «не туда» checkpoints a gap_event back to the map, never invents canon. Superseded old route:
      local/canon-cartography served its purpose; work/design-labs/gas-spatial-form-001.md stays draft-only, no Q1
      verdict. PROCESS SHELL «Кузница v2» (installed 2026-07-09 s-process-canon-forge-v2-001) unchanged: canon-forge → v2
      wrapper; canon-status/design-lab/mechanic-forge → superseded stubs (mechanic-lenses BINDING); canon-cartography
      retained v1.
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
  CALL c-forge-q-ruki-001 → work/c-forge-q-ruki-001-call.md

END_OF_FILE: live/indie-game-development/NOW.md
