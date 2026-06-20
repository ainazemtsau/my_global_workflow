# RESULT — review g-9c41 (Wave 2) — s-review-002 (2026-06-20)

play: review · node: g-9c41 · binding fresh-session G5 (separate from the work sessions s-work-007/009/012/016).

## outcome

Wave-2 bet of g-9c41 CLOSED by an independent fresh-session G5 review (20-agent adversarial refutation fan-out
[wf_8a98eab6-60a] + first-hand re-derivation of the headless gate). VERDICT = **SUBSTANTIVELY MET /
PARTIALLY-MET-AS-WORDED** with honest deviations: done_when (2),(4),(8) MET (survived refutation); (5) CUT-HONEST;
(1),(3),(6),(7) PARTIALLY-MET; plus a gate-honesty correction (NOW.md rounded "dotnet test 431/431" up to
"-Deliver GREEN incl. coverage/spec-silence" 3×; strong-checks never ran — deviation-close per RESULT cut #5).
NOT a failure: the bet's PURPOSE (kill the riskiest assumption + inform the owner) was achieved — the riskiest
assumption (novel band-solver determinism + replication) is proven, and the internal proof did its job (it
informed the owner, triggering d-gasmodel-redesign-001). The gas-model doc recommendation (дорога A+, not B) was
independently adversarially CONFIRMED: 3 angles, NO dealbreaker, A+ strengthened on all axes, §K repo-overlay
9/11 claims code-grounded, B reopens the solved net-determinism problem; §G load-probes INCOMPLETE → +4 added.
Node g-9c41 stays ACTIVE (multi-wave); the next bet AWAITS the owner's road decision (A+/B/C).

## evidence

- **First-hand gate re-derivation**: `dotnet test GasCoopGame.Core.slnx -c Release` at HEAD main a89b36b (clean) →
  **431/431 PASS** (re-ran live; did not trust the flag).
- **Refutation matrix** (committed evidence in both repos, per item):
  - (1) PARTIALLY-MET — §7-#2 battery invariants asserted only on 1–8-sector chains (CoarseSolverBatteryTests);
    at ~3,136 sectors only timing (g9c41-t1-bench.json: 1.06ms ≤ 8ms ceiling, emitter-computed not gated) +
    structure + the ANALYTICAL BS1 quiescence certificate; CR3 float-mutant negative control non-vacuous
    (CoarseReplicationTests T25 / CoarseBandStep.Reduce). Scale = 3,136 (within frozen 3000–3600).
  - (2) MET — CoarseBreachReplicationTests T21/T23/T24/T25 per-layer bit-exact incl. breach tick; temperature IS
    in the replicated+hashed path (CoarseBreachReconstructionHarness _tempEnc / ComputeGasHash / MaxDiv).
  - (3) PARTIALLY-MET (2nd skeptic confirmed) — real-DA(SGF) proven only at 6 sectors (t-4-da-output.json, no
    replication, owner-eye); hundreds-of-rooms (208) + CR2-lossless-across-breach proven only on SYNTHETIC t-2
    topology — never united in one run; real breach+CR2 never exercised on the real-DA level.
  - (4) MET — single field-sampling oracle OR1/OR3 cross-peer over CR1-reconstructed state + omitted-region negative.
  - (5) CUT-HONEST — t-2 ships temperature plane-6 replicated; c-exec-007 cancelled; owner-acked (d-t3-defer-001).
  - (6) PARTIALLY-MET (2nd skeptic confirmed) — met only vs the owner-lowered internal-proof bar + 2 owner-acked
    deviations (d-grid-sgf-001, d-rn2cut-001) + 1 caveated sign-off; load-bearing SnapGridFlowRoomReader is in
    Assets/ (no csproj/slnx), zero headless tests, mutation scope = CoarseFillProjection.cs only → the gate is
    structurally incapable of covering the reader; owner checklist L1–L3 "confirmed с оговоркой".
  - (7) PARTIALLY-MET — keyframe-inclusive basis ✓ + named assumptions (A8.5) ✓ + under-clamp ~×3 headroom ✓
    (g9c41-t1-scale-arithmetic.json, recomputed from first principles), but ">=2 independent recomputes" holds
    only for the memory figure (two trivially-equal forms); bandwidth gets one; under-clamp rests on a 1.6s
    keyframe cadence materially more generous per-cell than the V2-1 ~11k-cell ceiling implies.
  - (8) MET — clean 1-player parity + hash discipline.
- **Gate-honesty cross-check** — NOW.md lines 68/296/402 overstated the t-4 close as "-Deliver GREEN
  (...hygiene/coverage/spec-silence)"; RESULT.md line 3 + cut #5 say "NOT a clean -Deliver-green delivery".
  Disclosed in body (owner caveat, deviations named) — overstated headline over an honest body. CORRECTED.
- **Gas-model A+ adversarial confirmation** (3 angles, code+math, no dealbreaker): network-determinism SOUND &
  proven-in-code (FloatMutant CR3 control, followers reconstruct-not-recompute, host+2c bit-exact under fault);
  §K 9/11 claims hold exactly vs code (2 over-statements of fidelity/scale, not fabrications); §G real but
  INCOMPLETE → +4 mandatory probes; host-migration the top open chunk.
- **Forecast-surprise** — wrong-mechanism for "satisfaction" (transport+consistency proven ≠ feels resolved) +
  optimistic on "terminus = showable artifact" (re-scoped to non-showable internal proof).

## state_changes (APPLIED by this session as its own writer; committed locally, push owner-gated)

- NOW.md: (1) active_bet.phase prepended with the WAVE-2 CLOSED (s-review-002) record + per-item verdict +
  forecast-surprise + gate-honesty correction; node stays ACTIVE, no active bet (between waves). (2) Gate-honesty
  repair — all 3 "-Deliver GREEN (...)" occurrences replaced with accurate "dotnet test 431/431 GREEN [⚠ review
  correction: strong-checks NOT run — deviation-close; mutation CoarseFillProjection-only + stale; SGF reader
  uncovered]". (3) decision_inbox d-gasmodel-redesign-001 → "PUT TO OWNER (A+/B/C, rec A+)" + review findings +
  §G+4 probes + host-migration split. (4) next → awaiting_decision (A+/B/C) → conditional shape CALL.
- LOG.md: appended the s-review-002 line.
- knowledge/: created g9c41-wave2-aplus-over-b-code-grounded.md, g9c41-wave2-gload-probes-incomplete-plus4.md,
  g9c41-wave2-coarse-proof-not-resolution.md.
- history/: this file.

## captures

- Home-cleanup follow-up (GasCoopGame, NOT this session): re-spec R1 Grid→SnapGridFlow + openspec apply/archive
  of openspec/changes/c-exec-011-t4-coarse-gas-render/ (d-grid-sgf-001).
- Home-cleanup follow-up: correct the stale ADR-0005/0007 "separate-layer = t-3 obligation" wording (d-t3-defer-001).
- Carry: FishNet real-UDP owner-run residual stays non-gating (binding gate = headless+loopback); resolve at an A+ net leg.
- Add-back/ratio observation: T2-detail cut was correctly SEQUENCED (the coarse proof generated the fine-tier
  requirement); RN2-machine cut (d-rn2cut-001) left the SGF reader with no automated coverage = owed-back coverage
  when R1 re-freezes. Cuts are NOT too timid this wave (the coarse-only readability ceiling — owner "не всё понятно"
  — is a real cost).

## decisions_needed

- **d-gasmodel-redesign-001** — Road for the gas-model redesign / next g-9c41 bet — A+, B, or C?
  - A+ (RECOMMENDED): grow the proven integer graph core into the target model (front + interest-grain +
    resident-gas damage law + reactions + edge-destructibility). No dealbreaker; strengthened on all axes; §K 9/11
    code-grounded; nothing proven wasted. Honest cost: multi-wave → re-shape past 2026-07-24; no new showable
    footage for weeks; host-migration still open.
  - B: continuous-field rewrite. Rejected — reopens the solved-expensive net-determinism problem; discards
    Wave-1/2; highest money-gate risk.
  - C: a 1–2-wk bounded continuous-field net-replication probe before deciding. Only if the owner still doubts A+;
    likely just rediscovers that a deterministic continuous field must be integer-discretized (= A+ with extra steps).
  - recommendation: **A+**.
- **d-review-treediff-001** — Approve the review's tree diff (G9), or route the bigger commercial restructure to map?
  - Approve the FOCUSED cards now: (a) ADD a host-resilience/host-migration outcome under g-9c41; (b) REWORD
    g-9c41 wave_plan so Wave 3 = A+-basis with §G(+4) load-probes as a HARD pre-bet gate; (c) EXPAND g-d3a8 —
    free-species bounded by the wire cap.
  - Route the storefront-footage restructure (root map_order edge withdrawn, g-5b07 #1 footage-half unsourced,
    g-2f8c #2 "teeth", reinstating the "first showable artifact" node) to a dedicated map session.
  - recommendation: **Approve (a)–(c) now + open the map follow-up for the commercial-track restructure.**

## play_check

1. Verify by refutation — DONE (20-agent adversarial G5 + first-hand gate re-derivation 431/431; verdict
   partially-met-as-worded; forecast-surprise named: wrong-mechanism + optimistic).
2. Harvest per lens — DONE (all 6 CHARTER lenses; biggest: commercial guarantee withdrawn, depth must come from
   the model, host-migration unowned).
3. Update the tree — PROPOSED, owner approval PENDING (G9) — diff in decisions_needed (d-review-treediff-001);
   bigger commercial restructure routed to a map session. No TREE edits applied.
4. Add-back check — DONE (cuts well-calibrated/not-too-timid; T2-tier cut correctly sequenced; RN2 cut left
   SGF-reader coverage owed — captures; ratio observation logged).
5. Knowledge — DONE (3 promotions, each with read_by).
6. Select next — DONE — decision PUT to owner (G7): A+/B/C + rec A+; honest tensions surfaced (multi-wave past
   wall, footage gap, host-migration, §G+4 probes, sandbox-first).
7. Close — RESULT emitted; Wave-2 bet closed with verdict; NOW.md cleaned + gate corrected; writer applied the
   non-G9 state_changes + committed locally.

## log

2026-06-20 — review (g-9c41 Wave 2, s-review-002): Wave-2 bet CLOSED by fresh-session G5 (20-agent adversarial
refutation + first-hand 431/431 gate re-derivation). VERDICT = substantively-met / partially-met-as-worded.
Gas-model дорога A+ independently adversarially CONFIRMED; §G load-probes hardened with +4. 3 knowledge
promotions. Node g-9c41 stays active; next bet AWAITS owner road A+/B/C (rec A+) + tree-diff approval.

## next

awaiting_decision (owner picks the road A+/B/C + approves the tree diff). ON OWNER APPROVAL OF A+: shape the
FIRST A+ bet of g-9c41 (re-framed past 2026-07-24; basis = work/gas-model-design-full-2026-06-20.md §K) — the
HARDENED §G load-probes (§G's 7 + the review's 4 added mandatory probes) as the pre-bet kill-gate, then the
first real layer (integer geodesic front + interest-grain), with host-migration as a named spike;
d-sandbox-001 harness may sequence first (owner Q3). Full CALL in NOW.md `next`.

END_OF_FILE: live/indie-game-development/history/s-review-002.md
