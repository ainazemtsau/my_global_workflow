# s-work-034 — work (g-9c41 / Sc-reactions / framing) — 2026-06-30

In response to: CALL c-frame-021 (NOW.next; owner «продолжаем по indie-game-development»).
Job: frame + adversarially harden the Sc-reactions executor CALL (c-exec-021). The direction frames it; the builder does NOT.
Outcome artifact: live/indie-game-development/work/c-exec-021-call.md (387 lines, END_OF_FILE-trailered).

## Owner-facing summary (as delivered)

Framing session — no engine touched. Wrote and adversarially hardened the brief (c-exec-021) for the next build session.
The slice: gases finally REACT — when two reactant types co-reside in a cell, the gas TELEGRAPHS (warns) then BANGS, as a
shared, deterministic, in-checksum event a second player feels. All data-driven: a new gas type = 0 new code branches.

Hardening (12 lenses → 40 findings → verify + direction adjudication) caught things that would have shipped wrong:
- The old ReactionLayer is a Wave-2 LOCKED openspec contract, not free dead code — the draft's "delete it" would have
  silently broken a locked spec with all gates green. → default cut+pin; delete only after a live-spec amendment.
- ADR-0020 is already taken on dev2 (verified) → engine takes ADR-0021 (the Sc-weight collision, not repeated).
- The co-op axis was framed as "byte-identical on both endpoints" = consistency, which canon §6 п.5 distinguishes from
  interdependence and which the determinism gates already guarantee → reframed to a NON-LOCAL consequence (the bang reaches a
  cell the reactants didn't occupy).
- N²-dispatch if-chain, telegraph distinctness RED, handshake-hash convergence + reactant-set canonicalization, non-atomic
  EmitImpulse, shove-vs-settle-envelope, and a machinery-based split — all folded.

Routed to the owner (not resolved here): d-coop-interdependence-repin-001 stays OPEN; the CALL has the owner ratify the
fold-home at the executor PLAN (owner present), not silently enacted.

Next: a fresh GasCoopGame_dev session opens c-exec-021 with a PLAN → builds → returns RESULT home; merge owner-gated.

## RESULT (verbatim)

```
RESULT
session: s-work-034
direction: indie-game-development
play: work
node: g-9c41
task: Sc-reactions
in_response_to: CALL c-frame-021

outcome: |
  The Sc-reactions executor CALL (c-exec-021) is FRAMED + adversarially HARDENED and ready as a
  self-contained artifact at work/c-exec-021-call.md, for a fresh GasCoopGame_dev session to open with
  a PLAN (owner present). Goal = integer chemistry between weight-class gas types (co-resident reactants
  → telegraph → bang as a shared in-checksum coarse event), data-driven so a new type = 0 new code
  branches, determinism preserved (ADR-0002 not reopened), the full gate battery. The builder did NOT
  author it (the direction framed it). The Sc-reactions task stays ACTIVE (the build is next).

evidence: |
  - Artifact: work/c-exec-021-call.md (END_OF_FILE-trailered), grounded first-hand in GasCoopGame main
    @61b7923 real code (GasTypeRegistry/ComputeContentHash, MeaningMembers next-free-bit 1<<6,
    VoxelField/VoxelFaceFlow dense [species][cell] gather-then-apply, VoxelImpulse/EmitImpulse,
    type-hardcode-scan.ps1 v8, openspec/specs/sim-core/spec.md Wave-2 lock).
  - Adversarial hardening: workflow wf_86b1f6d0-bda — 12 attack lenses → 40 findings → refute-verify.
    The verify-phase fan-out hit transient server-side rate-limiting twice; the direction adjudicated the
    unverified findings FIRST-HAND against the canon SPEC + the real product code (not assumed).
  - Must-fixes folded (each grounded): (1) old ReactionLayer/GridEventKind.Reaction/ReactionHeat is a
    Wave-2 LOCKED openspec contract (spec.md:153-172) — flipped delete→recorded-cut+pin, live-spec check,
    locked-contract delete = STOP; (2) ADR-0020 already taken on dev2 (verified: ADR-0020-gas-visual-w1a)
    → ADR-0021 + mechanical git-ls-tree verification; (3) co-op axis reframed from consistency (canon
    §6 п.5) to a NON-LOCAL shared consequence (bang reaches a cell the reactants didn't occupy); (4)
    if(a==X&&b==Y) pair-chain added to the N² falsifier; (5) handshake-hash needs a CONVERGENCE RED +
    two-level reactant-set canonicalization + rule-count length-guard; (6) EmitImpulse is not
    atomic/canonical → canonical field-derived order + validate-all-atomic or compute in-pass; (7)
    telegraph fold needs a DISTINCTNESS RED keyed by cell coord; (8) same-tick cascade needs an explicit
    TICK-COUNT oracle (depth-N→N ticks); (9) split re-fractured along MACHINERY (handshake/dispatch leg
    vs telegraph-member leg).
  - Should-fixes folded: telegraph STORED-vs-DERIVED is the PLAN's call (appetite relief); shove bounded
    inside the c-020 settle envelope; conservation RED = cell-total-across-planes (not per-species);
    per-plane MaxCellMass must THROW not saturate; mix-overlay STOP scoped to a parallel species-mix
    structure only (the telegraph IS canon's "mix-overlay при реакции"); dense-rep canon bridge
    (SPEC.md:50 delegates rep to Sc-types→dense); apply-phase permutation control; handshake obligation
    reframed placement→determinism (registry-absorbed vs sibling-hash = PLAN's call); d-coop routed to
    owner ratification AT the PLAN.
  - Refuted (NOT folded): a "shared buoyancy/_bias register" STOP (buoyancy is DERIVED, touches neither
    _bias nor EmitImpulse — the real interaction is the additive desiredMove settle-envelope, folded
    instead); the next=Sc-damage pointer as a method-leak (it echoes recorded road-shape/canon).
  - Self-check vs c-frame-021 done_when: artifact exists + hardened; goal = integer reactions between
    weight-class types (telegraph+bang, co-op pressure); per-type DATA not code-branching; determinism
    preserved; full gate battery; ready for a fresh dev PLAN. PASS.

state_changes:
  - create work/c-exec-021-call.md (the hardened CALL).
  - NOW.md: updated→s-work-034; bet.current_truth (c-exec-021 framed+hardened, road rolls Sc-reactions→
    Sc-damage); tasks[Sc-reactions].status_note (CALL framed+hardened, ratify d-coop at PLAN); open_calls
    +c-exec-021 (executor); history_pointers +Sc-reactions-CALL-framed; next→executor handoff c-exec-021.
  - LOG.md append s-work-034 line.
  - history/s-work-034.md create (this file).

captures:
  - Cross-track ADR numbering collides every engine/visual slice (0012, 0016, 0019, would-be 0020) — the
    root is no single ADR-number ledger across dev/dev2. c-021 handles its own number (ADR-0021); a durable
    fix (one ADR-number ledger or a track-prefixed scheme) is worth triaging at a pulse/maintenance pass.
  - The hardening-workflow verify-phase fan-out hit transient server rate-limiting twice (34/40 verifies
    failed once). The direction self-adjudicated. If recurrent, cap the verify concurrency or stage
    verifies in smaller batches in the workflow process (codex-sidecar/workflow note).

decisions_needed: []
  # d-coop-interdependence-repin-001 stays OPEN in NOW.decisions (not resolved this session); routed to
  # the c-exec-021 PLAN for owner ratification. No new decision raised.

play_check:
  - step1 Recite: done — restated Sc-reactions goal + done_when + the active bet g-9c41.
  - step2 Owner inputs (owner): N/A — the artifact is a machine CALL, not owner-content (food/voice/
    schedule); no owner inputs needed; the owner's real participation is the executor PLAN; the open
    d-coop decision is routed there for ratification, not resolved here.
  - step3 Do the work: done — framed c-exec-021 + ran adversarial-hardening workflow wf_86b1f6d0-bda
    (budget-sanctioned) + adjudicated the rate-limited findings first-hand; folded must/should-fixes.
  - step4 Self-check: done — compared the artifact to c-frame-021 done_when point by point (PASS).
  - step5 Close: this RESULT; next = the executor CALL.

log: "framed + hardened c-exec-021 (Sc-reactions); next = fresh GasCoopGame_dev PLAN; ADR-0021."

next:
  CALL c-exec-021 → executor (GasCoopGame_dev); open work/c-exec-021-call.md with a PLAN (owner present),
  RATIFY d-coop-interdependence-repin-001's fold-home, build integer chemistry, return RESULT HOME.
  dev→main merge + push owner-gated. Split along the machinery seam if the PLAN finds it oversized.

END_OF_RESULT
```

END_OF_FILE: live/indie-game-development/history/s-work-034.md
