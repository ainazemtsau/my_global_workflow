# converge-g-9c41-arch — converge-arch ARCHITECT record (heavy node, c-converge-002)

> The ARCHITECT step of converge-arch (heavy node). Its job is NOT to re-run the architecture — that is
> already a product (brief v2, ARCH-1v2). This file records: (1) the binding architecture-on-paper as
> IMPORTED-BORN-CLOSED input evidence to PLAN; (2) the small set of EMERGENT contract-architecture high-risk
> questions this leg surfaced + their disposition (authored observable-first, HOW→PLAN); (3) the miner
> gap-hunt result. No pick here leaks into done_when — the architecture rides the executor/PLAN CALL's
> `context` as input evidence only (`arch_in_context_only: PASS`). The binding refutation is converge-verify.

## §ARCHITECTURE-ON-PAPER (imported born-closed — rides PLAN as input evidence, NOT re-opened)

The high-risk architecture for the coarse band sim + grid + windows is ALREADY worked and signed as a
product: **work/research-g-9c41-core-architecture-2026-06-12-v2.md (ARCH-1v2 — "sector-band graph + clipped
windows")**. It was derived + refuted by a 26-agent two-workflow pass and scored by 3 independent judges:
**A (ARCH-1v2) 8.5–8.7** vs **B macro-voxels 3.5–4** (gas seeps through sub-cell walls, sinks through
floors — kills R7) vs **C room-graph 5.5–6** (no advancing gas front in a corridor; unimodal hint mis-places
gas; cost-illusion). The refuted option chains + flip-conditions live in brief §0/§6/§11; the numerical-
physics fatal-defect fixes (quasi-steady pressure closure; exponential-relaxation Patankar integrator;
remainder-bucket conservation) in §3.1/§3.5; the 13-contract / 6-component anti-god-object layout in §3.9.

converge-arch IMPORTS these born-closed (like the FORM pass imported I1–I23): it does not re-derive them.
PLAN (the Wave-2 band-sim ADR) RATIFIES them and commits the binding ADR; if the paper-best fails in code,
PLAN escalates back. The §CONTRACTS in `work/converge-g-9c41.md` are authored ABOVE this architecture, in
observable terms, so PLAN picks the HOW magnitudes that satisfy the contracts.

## §EMERGENT CONTRACT-ARCHITECTURE QUESTIONS (worked observable-first this leg; magnitudes → PLAN)

Only HIGH-RISK / shape-defining questions that the CONTRACTS surfaced and that the brief did not already
nail are worked here. Each is authored as an OBSERVABLE (a checkable property + a named test), with the math/
magnitude routed to PLAN — so a PLAN failure surfaces as a BLOCKED contract, not a silent green.

| # | emergent question (high-risk) | disposition / pick | refuted-status |
|---|---|---|---|
| Q1 | Does ONE normative sub-band interpolation formula compose ACROSS a resolution boundary so the same point answers consistently whether resolved by a fine cell or a coarse band (same-point→same-answer at a seam)? | **single-oracle** — OR1/OR2/OR3 declare it observable-first (a named cross-tier agreement test at seam points; thinnest-open-level precedence). The formula internals → PLAN. | brief contract #4 (IGasReadModel) already commits the single normative formula + ExposureQuery-as-its-volume-integral; the OPEN risk is composition across the seam (brief §7 risk #4/#5) → authored as OR1's seam test, not solved. |
| Q2 | When gas (L0) + temperature (L1) are BOTH live on the shared FieldFabric, in what phase order + under what cross-layer revision/commit rule does a reaction-generated GridEvent on gas become a temperature-layer write, such that the lossless/lossy consistency oracle holds ACROSS BOTH LAYERS TOGETHER and the client reconstructs a consistent MULTI-LAYER field? | **both-layers-consistent-together** — XL1. The obligation is DECIDED (not an open fork): done_when #10 "networked-consistent together" + ADR-0004 §T12 (temperature already consistent at settle for the Wave-1 sink) + RESOLVED-1. The phase-ordering/commit rule for a FEEDBACK interaction (crit-10 tightening) → PLAN. | the cheaper "gas-only consistent + host-derived temperature client need not reconstruct" reading was considered + REJECTED (weakens crit-10, contradicts the LOCK). |
| Q3 | Can a WHOLE new layer (temperature-class) register on the FieldFabric kernel and ride the shared transactional commit + revision feed WITHOUT editing the kernel or any other layer — distinct from a within-gas species handler? | **layer-registry extensibility** — XL2 (C21 generalized: one layer per registration; the Wave-1 RNG-conservation guard generalized; a 3rd demonstrative layer for crit-10). The registry schema + the >2-layer barrier-table resize → PLAN. | the first draft CONFLATED this with the gas-domain species handler seam (GT1); separated here — they are two different seams. |
| Q4 | What does "correct on arrival / track sources exactly" observably PROMISE when a player enters a coarse-simulated region (band-handoff)? | **OWNER-SIGNED** (GG4/OR4, §SIGNOFF-BH): loose spatial tolerance (a few cells, not metric) + exact source/emitter tracking + coarse tier = source of truth + FIRM no-shimmer on the handoff. The 3-tier prep-window mechanism is the owner's HINT → PLAN; the tolerance magnitude → PLAN. | owner resolved in-session (voice); none of the three pre-framed strength options fit cleanly — the answer is a blend (loose-spatial + exact-source + firm-no-pop). |

## §MINER GAP-HUNT ("which architecture/contract question did we NOT ask?")

The gas-centric first draft mapped every cross-node edge but left **g-9c41's own done_when #10 unmapped**:
the in-core **gas↔temperature cross-layer interaction seam** (a layer publishes a GridEvent, another layer
subscribes + responds, both networked-consistent together) and the **whole-layer registry extensibility**
("a new layer plugs in without core edits"). These are the heart of the re-shaped node and the single
highest-risk architecture proof — yet no drafted family contracted them (Family-4 GT4 EventPlane is the
OUTBOUND gameplay-consequence plane to g-d3a8, a DIFFERENT edge). The cross-cutting completeness critic
caught it; both are now contracted (XL1, XL2), so a Wave-2 PLAN cannot re-invent the multi-layer phase-
ordering/consistency rule ad hoc.

## §SIGNOFF — Architect (heavy)

`§SIGNOFF: converge-arch ARCHITECT — SIGNED-in-part @ 2026-06-16 (c-converge-002).` Q1 signed via the OR1
contract (observable-first); Q2/Q3 decided on done_when #10 + the LOCK + C21; Q4 OWNER-SIGNED (voice, see
§SIGNOFF-BH in work/converge-g-9c41.md). The architecture-on-paper (ARCH-1v2) is imported born-closed and
rides PLAN as input evidence — `arch_in_context_only: PASS`. The BINDING independent refutation of the whole
set is the separate converge-verify session (NOT run here — boundary).

END_OF_FILE: live/indie-game-development/work/converge-g-9c41-arch.md
