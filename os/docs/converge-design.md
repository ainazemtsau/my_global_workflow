# CONVERGE — design rationale (v5)

The durable record of why the converge layer exists and how it is shaped. The procedure itself lives in the plays (`os/plays/converge*.md`); this file is the reasoning any session or direction reads to understand the *why*. Status: GENERAL — promoted to `os/plays/` by owner decision (2026-06-14), available to every direction (current and future) like any core play. First real run pending on g-9c41 (heavy); health's first use will be its next non-trivial node (training-activity, currently parked).

## The gap it closes

Between a TREE node (a coarse outcome + a multi-criterion done_when) and the executor CALL there was no layer that decomposes the node into the design questions that must be answered before anyone can build it correctly, resolves them with the owner, and hands the executor a spec whose answers are *used*, not re-invented.

Witness: node g-9c41 has a 9-criterion done_when, but shape jumped straight to tasks; the real binding spec (ADR-0003 — quantization step Q, divergence threshold, settle-N, keyframe-K, clamps, wire format) got invented at TASK time by the executor, re-derived from a ~170-line NOW.md `next:` block that dies with the bet. The owner only noticed "we'd gone somewhere primitive" once code started.

## Core insight: convergence is recursive (fractal), not one-shot

Decisions crystallize at MULTIPLE levels of decomposition. The witness values (Q/N/K/…) are NOT in the node's done_when and NOT bets of the node-level approach — they are internal parameters of the *chunked-delta stream mechanism*, forced only once that mechanism is committed (at work/PLAN time), one level below the node. A layer that converges once-per-node before tasks cannot see them.

So convergence must re-fire on each committed mechanism, each time minting that mechanism's own forced questions. This is the load-bearing fix; everything else is machinery around it. (Two independent design passes — the prior chat's v3.1 and this one — arrived at recursion independently, which is evidence the shape is right.)

## The layer: three plays, one flow

`ordinary build node → readiness router → (verified/OFF → shape | otherwise converge → [converge-arch] → converge-verify → shape) → executor/PLAN`

`specification outcome → owner-authority work → fresh converge-verify → narrow review(done) → next ordinary node`

- **converge** (TIER + DEFINE + RESOLVE) — type the node by risk (ceremony is a ceiling); lock disputed terms mechanically; resolve the WHAT as a cited node-on-paper. Questions derive from THREE sources: every done_when criterion, every cross-node edge, and MECHANISM DECOMPOSITION (each committed mechanism atomically split into the parameters it forces, recursively). HOW magnitudes/formats are firewalled `→ PLAN`; acceptance PROPERTIES and owner-owned design facts are owner-signed WHAT.
- **converge-arch** (DECLARE + DECOMPOSE + ARCHITECT) — only for sibling-bearing or heavy nodes. Consumer-driven cross-node contracts in observable terms; heavy nodes work high-risk architecture as a refuted option chain into an architecture-on-paper that rides PLAN as input evidence, never into done_when.
- **converge-verify** — a SEPARATE refutation session. For a build node it attacks set completeness and unresolved dependencies before shape. For `outcome_kind: specification` it attacks the exact owner-approved artifact against atomic done_when plus an independent oracle; PASS reaches narrow review, never shape. It answers or repairs nothing.

## What is new vs the salvaged v3.1 base

v3.1 already had triage-by-risk, mechanical Define, cited node-on-paper, the WHAT/HOW firewall, contracts, and recursive architecture questions. v5 keeps v4's four deltas below and adds only the specification-outcome boundary described later; the ordinary build flow is unchanged:

1. **Separate refutation session** (`converge-verify`). v3.1 folded verification into grep-closure + the owner gate + a same-session gap-hunt — a self-check, which cannot catch the assumption the author never knew he made. Verification is now a different session with an independent oracle.
2. **Mechanism decomposition made mechanical** (converge step 3). Any committed mechanism (chosen approach, or a mechanism locked in done_when) is atomically split into one question per internal parameter — so Q/N/K are *derived*, not dependent on how deeply the architect happened to decompose.
3. **Retrofit / import-already-decided** (converge step 1). A mid-flight node imports settled decisions from `history/` as born-closed rows (`source: history/<id>`), so converge frames only the genuine gap instead of re-litigating what the owner already decided. Needed because the first real run (g-9c41) is a retrofit and `knowledge/` is empty.
4. **Self-certifying handoff** (play_check lines: `converge_coverage`, `contract_coverage`, `verify_target`, `verify`). The writer checks evidence shape, not truth. Ordinary activation still requires build PASS or exact `converge OFF — because …`; specification closure instead requires exact artifact identity, owner receipt and a later fresh specification PASS before review may mark the parked node done.

## WHAT/HOW boundary (decision D-0)

Architecture VALUES (Q magnitude, wire format, keyframe cadence) do NOT live in direction state — they stay HOW, decided in PLAN as ADRs in the product repo, per CONTOUR. converge freezes only acceptance PROPERTIES (e.g. "divergence bounded by the quantization step", the dual-guarantee kill-gate, min-spec budgets) and the observable cross-node contract; it NAMES the HOW questions and routes them to an early, owner-present PLAN. "Defined down to architecture" means PLAN arrives with a complete WHAT + a named HOW agenda + competitive research and RATIFIES, instead of inventing late. The owner's surprise was a WHEN/completeness problem, not an architecture-location problem.

## Derivability — honestly

- No-white-spots = three-source coverage closure (done_when + edges + mechanism decomposition), re-checked by converge-verify against an independent oracle. Mechanical for what is named; bounded, not absolute (a dimension invisible to all three sources and the refutation still escapes — but that needs three independent misses, and it surfaces as a blocked closure, not a silent green).
- No-answer-by-assuming-an-uncovered-question = by construction for CITED dependencies (a resolved row exists only with an answer, so an open question is unciteable) + a separate refutation pass for UNCITED smuggled assumptions. Rigorous discipline, not a closed proof. State it in this true shape to the owner.

## Canon & reuse

Frozen answers, contracts, and decision-class checklists promote to `knowledge/` (tagged `serves:<node>`, `read_by:` naming plays/node-classes), so a later node starts from canon. Decision history lives three ways: inline rejected-options in the row, the supersession chain, and the full RESULT in `history/`. The live assembly surface is `work/converge-<node>.md` (a product doc, grep-able, not a 7th state type). Authorship rule held: converge proposes canon; review/pulse promote it.

## Specification-outcome boundary

This is an outcome classification, not a Canon workflow. Map may mark a card `outcome_kind: specification` only when the exact versioned owner-approved specification itself exhausts done_when. One untracked owner-present `work` CALL uses whatever authority contour the direction names; an executor cannot choose/approve its content. The node stays parked. Fresh converge-verify checks the artifact independently; narrow review closes it under G5/G9. No controller, seventh state file, new status, active bet, task, track or shape is introduced. Any later implementation is a separate ordinary build outcome and re-enters readiness.

## Generality (scale-down)

For build outcomes the spine is TRIAGE → DEFINE → RESOLVE → VERIFY → copy into shape/PLAN. Converge-arch and ARCHITECT are the engineering-heavy predicate. A trivial build node may triage OFF. A specification outcome does not triage as a build node: its authority artifact is the terminus and follows the boundary above.

## Fit to physics

All core plays remain ≤600 words and KERNEL ≤1500. No seventh state-file/packet type or engineering gate. The route reuses work, converge-verify, review, G5, G9 and G10. Build DoR remains wired; specification verification adds a distinct typed handoff. Direction-specific authority contours and oracles stay direction-local.

## Open decisions (carried to the owner)

- D-1 three plays vs two: landed on three (converge / converge-arch / converge-verify) — the separate verify is load-bearing and indie has the local-play budget.
- D-2 canon forcing-function (handoff blocked until WHAT promoted to knowledge/): deferred with the adapter edit; first runs prove the shape before enforcement is wired.
- D-3 general vs engineering-only: built general (the spine), engineering-heavy parts predicate-skipped; promoted to `os/plays/` immediately by owner decision (all directions + future ones get it), rather than waiting for a second direction's proof.

## Validation & hardening

Built via two multi-agent passes (5 independent architectures → adversarial critique → synthesis; then a 3-reviewer validation of the authored plays incl. a dogfood run on g-9c41). The dogfood caught four retrofit-first-run gaps, now fixed in the plays: (a) converge-verify's independent oracle is authored from first principles on a first run when no knowledge/ checklist exists — an empty oracle is a BLOCKED close, never auto-PASS; (b) an imported born-closed row that NAMES a mechanism still runs Resolve 3(c) decomposition (closing a mechanism never closes its parameters) — without this, a retrofit swallows the chunked-delta stream and never mints Q/N/K; (c) a row carrying both an acceptance property AND a HOW magnitude (the witness "divergence = Q") SPLITS — property → G7 WHAT, magnitude → PLAN — never routed whole; (d) history import is scanned and the imported ids listed in a play_check line so a missed prior decision is visible, not silent.

## Slicing / first run

1. (this build) author converge / converge-arch / converge-verify + this doc; clean the v3.1 hanging state. [done]
2. First real run = a fresh session: TIER + FRAME (converge) on g-9c41 as a RETROFIT — import settled decisions, derive the question set incl. the chunked-delta mechanism's Q/N/K as `→ PLAN` rows; output work/converge-g-9c41.md. The success test: converge reproduces, as named questions, exactly the values the executor invented ad hoc.
3. Resolve one question per chat; converge-arch for the grid↔gas contract; build-target converge-verify; then shape with acceptance/contracts + PLAN-agenda.
4. Converge-readiness DoR is wired in the writer (2026-06-16); wire the acceptance/contract-row copy-check when that first handoff needs it.

END_OF_FILE: os/docs/converge-design.md
