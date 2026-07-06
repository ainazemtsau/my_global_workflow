# NOW — indie-game-development
updated: 2026-07-06 by s-design-lab-process-repair-001

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
  - id: c-visual-006
    to: executor
    for: g-7e15 / Stage 2 (Паспорт типа + шипучий режим)
    issued: 2026-07-06
    call: work/c-visual-006-stage2-call.md
    note: |
      FIRE-READY (s-work-055; owner sign-off clarified s-work-056): render-only Stage 2 —
      per-type passport schema (8-channel + 96→128B layout-ADR) + consume the merged W1b
      read-API + real half-res; payoff = two-colour PREVIEW. Owner clarification: «шипучий
      режим» = ONLY the two-colour preview label (NO extra bubbling/particle/boiling FX);
      the base passport is required for every gas; reserve an extensible render-only
      attachment path for later per-gas modules, but build NONE in Stage 2. Fire in a FRESH
      GasCoopGame_dev_2 (reset to @26dd062 first), owner-present PLAN, PARALLEL to c-021.
      ZERO Core/** edit (STOP if it needs one).
  - id: c-design-lab-gas-interaction-gameplay-001
    to: session
    for: g-d3a8 / gas-interaction-gameplay design lab
    issued: 2026-07-06
    call: work/c-design-lab-gas-interaction-gameplay-001-call.md
    note: |
      Design Lab process is installed and verified. Next gas interaction work must run through
      local/design-lab before any canon-forge freeze. Purpose: explore playable gas interaction
      situations in plain owner-readable language, detect blockers / side dependencies / parent
      reopen risks, and output the correct next route. No hardcoded counts, no abstract label
      freezing, no cargo/containment continuation as the center.

recurring: []

parallel_tracks:
  - id: g-7e15
    track: VISUAL / GASG
    state: active — Stage 1 DONE (owner-tested OK @26dd062); NEXT = Stage 2 (c-visual-006, see open_calls;
      owner-clarified s-work-056 = preview-label only, base passport for every gas, extension path reserved).
    plan: work/gas-visual-plan-v2-2026-07-02.md
  - id: g-d3a8
    track: canon/design
    state: parked — next open call = c-design-lab-gas-interaction-gameplay-001; gas-interaction work now goes through local/design-lab before canon-forge; baseline history/s-canon-visual-style-minimal-gas-stage-001.md
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
  owner-gated. Parallel visual track = c-visual-006 (open_calls).

END_OF_FILE: live/indie-game-development/NOW.md
