RESULT s-work-066-c-visual-008-stop-route (call: c-visual-008 handoff)
direction: indie-game-development   play: work   node/task: g-7e15/c-visual-008

outcome: |
  c-visual-008 has a terminal Direction-OS disposition of STUCK / stop-needs-new-data, explicitly NOT DELIVERED.
  Its frozen cutoff worked: render-only detail became visible and smoother, but owner-eye rejected the solid dense
  center emitting side wisps, while half-res blur remained. No visual candidate is adopted and Stage 4 stays closed.
  The returned executor call is removed from in-flight state and c-visual-009 is opened as a separate PLAN-only
  engineering call to choose an honest simulation-derived movement contract and decide the later blur/dense-core split.

evidence: |
  Product evidence read first-hand from C:\projects\Unity\GasCoopGame_dev_2:
  - `docs/results/c-visual-008.md`: status STUCK, NOT DELIVERED; stronger curl candidate rejected; movement-data STOP.
  - `docs/measurements/c-visual-008-owner-eye-checklist.md`: owner token
    `owner-chat-2026-07-10-motion-seam-stop`, `FakeFlow: true`, `AuthoritativeDensityMoved: false`, final disposition
    `stop-needs-new-data`.
  - `docs/measurements/c-visual-008-render-evidence.md`: current IGasViewSource/GridView lacks signed movement;
    Core has a promising signed per-face `Flux(cell, face, species)` read; blur and solid-center shaping are separate
    render-only defects.
  - `docs/measurements/c-visual-008-owner-choices.md`: no candidate adopted; preview cadence smoother but insufficient.
  - Frozen `openspec/changes/c-visual-008/specs/gas-visual/spec.md` and ADR-V-0002 explicitly require STOP instead of
    fake flow when current view data is insufficient.
  - Product git: `dev2@a48883b5` (`Record c-visual-008 visual repair plan`); no tracked working-tree diff, but status
    lists the c-visual-008 RESULT, diagnostics/media and independent acceptance test as untracked closure material.
    Current `origin/main` was `a644e5db`, so the c-visual-008 plan branch is stale/diverged and cannot be assumed as the
    next planning base.
  - User/product report: Core build GREEN (0 warnings/errors); Stage35 acceptance 11 passed / 4 expected non-delivery
    failures; result-check and Deliver intentionally not green. These are guardrails against a false delivery claim.

  c-visual-008 CALL done_when reconciliation:
  1. PLAN/BUILD separation: recorded by frozen PLAN at a48883b5; no same-session delivery is claimed.
  2. Requested product base: NOT MET against the later/main state; stale-base fact is explicit and becomes c-visual-009
     preflight, so it cannot support delivery.
  3. Baseline/A-B: diagnostic clips/stills exist untracked; no accepted change, and clarity stills were not camera-matched.
  4. Honest stationary idle life: NOT MET; owner rejected fake-flow read.
  5. Motion onset: smoother diagnostic cadence, but honest body motion was not achieved; the CALL's alternative STOP
     branch fired and routes missing movement data.
  6. Clarity: half-res softness remains and evidence limitations are named; no accepted clarity repair.
  7. Honesty/Core boundary: no fake directional jet or hidden channel was adopted; rejected product candidate removed;
     tracked working-tree diff empty.
  8. RESULT/measurements: exist as untracked closure evidence at the named paths.
  9. Checks: result-check/normal/Deliver are not green, deliberately preventing delivery; no green claim is made.
  10. Return routing: movement-data PLAN required before Stage 4; supplied as
      `work/c-visual-009-movement-data-plan-call.md`.

  owner-ack:owner-chat-2026-07-10-motion-seam-stop — owner rejected further render-only patching and requested a
  separate PLAN plus a Direction-OS-assigned change id/CALL.
  review-evidence: n/a — terminal STOP / NOT DELIVERED; no done claim, adopted implementation or delivery review.
  G5: not claimed or waived; G5 is required for a later done/delivery claim, not for recording this blocked outcome.

state_changes: |
  live/indie-game-development/work/:
    - add `c-visual-009-movement-data-plan-call.md` as the self-contained PLAN-only executor CALL.
  live/indie-game-development/NOW.md:
    - set `updated: 2026-07-10 by s-work-066-c-visual-008-stop-route`;
    - remove returned open_call `c-visual-008`;
    - add open_call `c-visual-009` for g-7e15 Stage 3.5 movement-data PLAN;
    - update g-7e15 parallel-track state with the c-visual-008 terminal STOP, c-visual-009 route and Stage 4 closed;
    - add c-visual-009 to `next` under other ready fronts; preserve c-exec-lv-ingest-phase0-001 as recommended engine
      next and preserve all unrelated/canon calls, decisions and state.
  live/indie-game-development/LOG.md:
    - append the s-work-066 one-line record.
  live/indie-game-development/history/:
    - add `2026-07-10-s-work-066-c-visual-008-stop-route.md` with this RESULT.
  TREE.md / CHARTER.md: no change.

captures:
  - c-visual-008 closure docs/media/test are untracked in the stale dev2 checkout; c-visual-009 PLAN must preserve and explicitly reconcile them before any checkout transition.
  - Evidence suggests density history may be a cadence layer alongside flux-derived movement rather than the sole movement contract; the owner-approved product PLAN decides.

decisions_needed: []

play_check:
  - 1 Recite: done — c-visual-008 served g-7e15's simulation-derived visual goal; its own frozen contract made stop-needs-new-data a valid terminal blocked outcome, not delivery.
  - 2 Owner inputs (owner): done/skipped as non-owner-content — owner supplied the binding route in this handoff: "Создать отдельную PLAN-сессию" and "Новый change id и следующий CALL должен назначить Direction OS"; no personal preference was guessed.
  - 3 Do the work: done — reconciled the STOP evidence, assigned c-visual-009 and authored the self-contained PLAN-only executor CALL without designing/building the product solution in Direction OS.
  - 4 Self-check: done — all c-visual-008 done_when bullets have explicit dispositions; stale base and untracked evidence are surfaced; no delivery/G5/clean-worktree overclaim; the new CALL covers both movement candidates and the blur/dense-core split.
  - 5 Close: done — c-visual-008 leaves in-flight state only as terminal blocked history, c-visual-009 opens, primary engine next and unrelated canon state remain unchanged, and Stage 4 stays closed.

log: |
  2026-07-10 — work/route (g-7e15/c-visual-008, s-work-066): c-visual-008 accepted only as terminal stop-needs-new-data, NOT DELIVERED — smoother visible render detail still read as a solid center emitting side wisps and half-res blur remained; c-visual-009 opened as a PLAN-only movement-data contract over current main, with density-history vs flux-derived read-only seam and blur/dense-core split to decide before any BUILD or Stage 4. → history/2026-07-10-s-work-066-c-visual-008-stop-route.md

next: |
  CALL c-visual-009 → work/c-visual-009-movement-data-plan-call.md

END_OF_FILE: live/indie-game-development/history/2026-07-10-s-work-066-c-visual-008-stop-route.md
