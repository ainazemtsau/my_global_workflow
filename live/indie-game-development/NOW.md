# NOW — indie-game-development
updated: 2026-07-07 by s-work-061-frame-c-visual-007-stage3

bet:
  node: g-9c41
  goal: |
    Networked co-op gas CORE on the character road: Sc-types → Sc-weight → Sc-rep →
    Sc-kernel → Sc-reactions → Sc-typing → Sc-damage. Delivered + merged to GasCoopGame
    main through W1b (base @26dd062, contract v18); immediate next = Sc-reactions
    (c-exec-021). Far-tier S3/S4/S5 scale plumbing parked until levels get big.
    Latest session: s-work-057 (c-exec-021 executor checkpoint reconciled; see LOG.md / history/).
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
      Integer chemistry on the sparse-dominant overlap front (explicit-SET > AXIS >
      env-conditioned DEFAULT > identity; telegraph+bang gameplay-load-bearing; layered
      mass-conserving overflow). ENGINE-ONLY. Shaped slice + forks (a)–(f) closed in
      the CALL: work/c-exec-021-call.md. leg-1 groundwork committed on dev@0a95f01 (owner
      D+A 2026-07-06, NOT merged); engine completion continues via
      work/c-exec-021-continuation-call.md.
    done_when: |
      The GasCoopGame_dev RESULT satisfies the c-exec-021 gate battery (fire-time
      §Re-sync + full re-harden vs real code, split trip). Fires via a fresh
      owner-present PLAN session (open_call c-exec-021).
    status: active
    unblock_when: owner launches a fresh GasCoopGame_dev re-planning PLAN session for the
      c-021 continuation (work/c-exec-021-continuation-call.md, base dev@0a95f01)

open_calls:
  - id: c-exec-021
    to: executor
    for: g-9c41 / Sc-reactions
    issued: 2026-06-30
    call: work/c-exec-021-call.md
    note: |
      CHECKPOINT RETURNED (executor sessions 1-2 → reconciled s-work-057, verified first-hand
      + 4-agent adversarial pass wf_f85e9ed7-786). Owner-present PLAN Q1-Q4 + ADR-E-0006 done;
      generic NO-PAIR-DISPATCH engine CONFIRMED; independent RED battery in place; groundwork
      committed dev@0a95f01 (owner D+A 2026-07-06, NOT merged); non-reaction 1343/1343 GREEN +
      13-entry byte-identity goldens INTACT. 10 reaction tests RED = engine-completion gaps.
      Continuation = a re-planning PLAN per owner D+A → work/c-exec-021-continuation-call.md
      (base dev@0a95f01). Frozen spec + PLAN.md + ADR-E-0006 STAND (not re-opened).
  - id: c-canon-gas-interaction-playable-anchors-001
    to: session
    for: g-d3a8 / q-gas-interaction-playable-anchors
    issued: 2026-07-06
    call: work/c-canon-gas-interaction-playable-anchors-001-call.md
    note: |
      Design Lab `s-design-lab-gas-interaction-gameplay-001` routed gas-interaction gameplay
      to canon-forge. Purpose: freeze owner-readable scenario grammar for playable gas interaction
      proof-candidates before cargo/containment continues. Inherit lab verdict: source/flow,
      active-condition push/stabilize, reaction front, quench/release/control, anomalous field
      rescue, and cargo leak as bridge only. No fixed-count case list, no cargo-center, no anomaly
      creature-AI, no exact roster/table/tools/containers, no fun certification; paper result remains
      UNVERIFIED until later two-player grey-box.
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

recurring: []

parallel_tracks:
  - id: g-7e15
    track: VISUAL / GASG
    state: active — Stage 2 DONE (c-visual-006 delivered on GasCoopGame_dev_2 dev2@6dbdddd; owner-eye/play-mode passed; real two-type preview + gas passport + half-res path; not pushed/merged by this close). Stage 3 FRAMED + FIRE-READY as c-visual-007: one-pearl/hero gas polish + natural-jet fix + LP1 re-test; visual-only/dev_2; owes §Re-sync v19 first.
    plan: work/gas-visual-plan-v2-2026-07-02.md
  - id: g-d3a8
    track: canon/design
    state: parked — design-lab complete (s-design-lab-gas-interaction-gameplay-001); next open call = c-canon-gas-interaction-playable-anchors-001; freeze playable gas interaction scenario grammar before cargo/containment continues; baseline history/s-canon-visual-style-minimal-gas-stage-001.md
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
  CALL: work/c-exec-021-continuation-call.md — fire the c-exec-021 CONTINUATION (reaction-engine
  completion) in a FRESH owner-present GasCoopGame_dev re-planning PLAN, base dev@0a95f01. Short PLAN
  (single-cell overflow: widen-K vs same-cell policy + skip-zero-keeps-golden STOP-confirm + SeedMass-clamp
  nod + 3 test-author acks) → EXECUTE leg-1-finish (10 RED → GREEN) → leg 2. dev→main merge/push
  owner-gated. Parallel visual track: c-visual-007 is open for visual-only Stage 3; primary target remains this c-exec-021 continuation.

END_OF_FILE: live/indie-game-development/NOW.md
