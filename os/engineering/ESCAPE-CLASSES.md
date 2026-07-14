# Escape-class registry — the question list that grows itself

A single, cross-kind, accumulating list of the **defect-classes** a product property can be
violated by. Its job is to stop the SAME kind of blind spot from recurring across waves and across
different kinds of feature (sim logic, netcode, audio, save/load, UI, economy, visuals).

It is the answer to one problem: a test can only catch what the spec NAMES, and a spec-silence audit
authored fresh each time relies on the author *remembering* the class — so the same class escapes
again on the next feature, even a feature of a different kind. (Witness: the height-band silence
audit already said "uniform vs gradient field, asymmetry" verbatim and STILL missed end-state and
derived-overflow — FRICTION 90.) A closed list that every audit must WALK converts "the author
remembered" into "every class we have ever been bitten by was discharged."

This is **not** a 7th state file and **not** a new gate — it is an `os/engineering` doc, governed by
`CONTRACT_VERSION` like a profile. The vocabulary is kept **kind-agnostic** on purpose: a class minted
from a numeric solver must pre-arm save/load and audio before either is built (FRICTION 88 lesson —
generalize the vocabulary or another direction reads it as "not about us").

## How it is consumed (front-load)

The PLAN spec-silence audit (CONTOUR §b) **walks this list row-by-row** and marks each class
`addressed | n/a because <reason>` for the feature at hand. An unmarked class is a deliver FAIL, the
same way a missing audit section is (the strong-check deliver dependency — PROJECT_SETUP §Strong-check;
ENABLED in a product repo only after its §Re-sync wires the walk into the deliver check).

For each surfaced must-hold property the audit names not only a **catcher** but the **regime/conditions
under which it must hold** — environment/platform, accumulated time or input count, the transition
*path* (not only the settled endpoints), fault/version — and confirms the catcher actually EXERCISES
that regime. A catcher that exists and can go red but only runs the nominal instant (one host, one
tick, the sampled input) is the same hole as a prose-only gate: green where the bug does not live.

The per-node-class decision-class checklists `converge-verify` authors in each direction's `knowledge/`
(converge-verify.md:14) SHOULD seed from this registry first, then add kind-specific rows — that is
what makes an accumulated class reach a node-class no one has built yet. (Not yet wired into
converge-verify.md — its budget is 598/600 and the cross-link crosses the direction↔engineering
boundary; a review/pulse promotion + FRICTION-watch follow-up, not claimed as enforced.)

## How it grows (the ratchet — never the same class twice)

A defect that reaches a **late stage** (owner-eye / independent review / post-merge) is named by the
**INVARIANT it violates, never its surface site** (`Min+Extent-1 overflow` is a site; *derived/interval
arithmetic can exceed type range* is the class — so its sibling `loZ+OpeningSize` is the SAME class,
not a new escape) and appended here, with its witness. **A single past-the-test-author escape is a
sufficient trigger** for the append (MAINTENANCE step 6) — this is the one place the ≥2-friction
threshold is waived, because the whole point is that a class cannot be allowed a second escape.

## Registry

Format: `Class (invariant) | Standing question the §b audit must answer for this feature | Catcher hint | Witness`.

### Witnessed (a real escape justifies the row)

| Class (invariant) | Standing question | Catcher hint | Witness |
|---|---|---|---|
| **End-state / termination / settle predicate** | Does this have an end state? Is "comes to rest / halts / converges / does not oscillate forever" named, or only the per-step behavior? | property test that runs to rest and asserts the rest predicate (not just one step) | g-9c41 voxel tier — front oscillated; canon "bring to rest" never transcribed; caught by owner-eye |
| **Derived / interval arithmetic overflow (not only stored values)** | Every place numbers are ADDED or DERIVED (`a+b`, `Min+Extent-1`, `lo+size`), not only where stored — can it exceed type range at the boundary? | property test over boundary/extreme coordinates, not fixed fixtures | g-9c41 — stored-mass overflow audited, derived coord/interval overflow missed; caught by code-review |
| **Stored-value domain-safety** | Can a stored value over/underflow or leave its legal domain? | bounds property test | g-9c41 MaxCellMass (the original silence audit covered this) |
| **Multi-actor / one-tick conflict / seam (empty / one / many; single→multi)** | With >1 concurrent actor or at a seam, do conflicting inputs in one tick stay correct? Are empty/one/many exercised? | multi-actor / conflicting-input property test, not a single-actor happy path (G2) | FRICTION 82 seal/breach precedence on multiple peers; 82(a) "no gate guarantees seam scenarios" |
| **Invariants on failure / guard / throw paths** | A guard that can throw — does the tick stay atomic and conserving ON the throw path, not only on success? | invariants property-tested on ALL paths incl. exception (G2); fix-is-a-change RED test before the fix | FRICTION 94/96 — `CheckedCell` guard lost mass on throw; per-species→per-transfer→per-tick 3× |
| **Value-bearing field == its source (meaning, not form)** | Does a measured/value-bearing field equal what it claims (bytes sent, not offered)? Tested for MEANING, not just presence? | assert field == source; G4 intent-vs-source | FRICTION 82 `onWirePayloadBytes` (offered vs sent) |
| **User-perceivable behavior is an owner-signed property** | Does the user see/hear/feel/read this? If so the observable behavior is an owner-signed acceptance property, not a builder default. | owner-eye + committed golden reference; named at PLAN | FRICTION 88 height-band distribution |
| **Oracle empty / weak / mis-targeted — the acceptance test has demonstrated power to fail** | Does each acceptance property have a COMMITTED negative control (a deliberately-wrong impl) its own test goes RED against — or can the test pass a trivial/wrong implementation (an ABSENT property with no code to mutate, an assertion measuring the wrong quantity, a non-strict comparison a constant satisfies)? | committed negative control per property (test-author-authored, RED against the wrong impl; `-Deliver` NegativeControl pass — VALIDATION §Oracle-soundness) | "test green but empty" cluster 2026-07: telemetry measured the wrong quantity (147f701), fork-split satisfiable by pure diffusion (5d77267), `>=` admits a constant (c7d89e0) — ALL green through G2 mutation; RECURRED 2026-07-04 on the FIX side (dev_2/c-visual-004: scan-oracles still satisfied by `/* */` block comments, a commented-out include, a raw-text check AFTER a `//`-only fix — same class, per-instance fix → contract v14 fix-class-closure) — but for a BEHAVIOR/render claim the scan-oracle's real fix is DELETION (wrong-venue row below), not a stronger negative control; hardening a scanner is the arms race (contract v17) |
| **Order-dependence / non-determinism (permutation-invariance)** | Does this outcome (a hash, an aggregate, a derived id) claim to be independent of collection iteration/insertion order? Is that tested with ≥2 orders of the SAME set, not one fixed-order sample? | permutation-metamorphic property test: same set inserted in ≥2 different orders, assert equal output (VALIDATION §Property-layer) | g-9c41 c-exec-006 t-2 — a topology hash keyed to insertion order, not the set's content, surfaced at code-review round 7-8 (`e4d0089`/`c3b85bd`) — the test-author's pre-code tests sampled one order and missed it |
| **Wrong-venue evidence / self-written proxy scanner (execution, not text)** | Is ANY behavior / render / acceptance claim evidenced by a source-text scan or a self-written scanner/parser instead of EXECUTING the real venue (compiled EditMode/PlayMode run, live-engine MCP query, real headless test) or owner-eye? A text check is legal ONLY as a declared non-behavioral wiring-smoke (`File.Exists` + trivial substring, NO acceptance property, NO negative control, NO property test). | real-venue run / live-engine MCP query / real headless test + owner-eye for the look; DELETE any self-written source scanner — NEVER add a negative-control to harden it (that IS the arms-race engine; a scan-oracle's fix is deletion, not a stronger control) — VALIDATION §Behavior evidence by venue | GasCoopGame dev_2 GasVisual — a 1728-line C#/HLSL/ShaderLab `SourceScanText.cs` + ~2000 lines of `*ScanTests.cs` + ~44 negative-controls (a 245-line suite guarding the scanner itself), ~3900 lines grown as v11/v12/v14 discipline hardened a TEXT SCANNER; proves text-presence, not render behavior; owner-caught 2026-07-04 (same root as the v14 c-visual-004 comment-variant arms race, one layer down) |

### Predicted (armed from the cross-kind stress-test; no live witness yet — kept transparent so the ratchet promotes them on first real hit)

| Class (invariant) | Standing question | Catcher hint | Witness |
|---|---|---|---|
| **Regime-narrow catcher** | Does the property hold only at the nominal instant/one host, or must it hold across platform / accumulated time / fault / version? Does the catcher EXERCISE that regime? | differential / soak / fault-injected catcher (bounded-divergence or invariant-held-over-N), ≥2 environments / accumulated time | predicted — stress-test wf_00feac76 (2026-06-25): netcode cross-host drift, audio many-source masking |
| **Emergent property discharged by a point sample** | Is this property emergent over a space/distribution (not a single point)? A single golden-ref or one scenario cannot discharge it. | sweeping/sampled catcher with a recorded sampling axis (golden-ref → golden-**set**) | predicted — wf_00feac76: economy degeneracy, audio under load |
| **Transition / trajectory (wrong intermediate state between correct endpoints)** | Between two correct states is there a path? Can a wrong/null/observable intermediate occur (async load, one-frame gap, in-flight input, interpolation, fade)? Endpoint correctness ≠ path correctness. | interval-spanning catcher (assert across the window, not at settle; frame-sequence, not a single still) | predicted — wf_00feac76: UI focus during screen transition |
| **Cross-spec meaning-drift of an unchanged-shape field** | A value crossing a frozen seam (persisted/wire/shared constant) whose MEANING was redefined by a sibling spec since this one froze — same name/type/shape, different meaning? | when a seam value's meaning changes, re-open every consumer's relevant acceptance row | predicted — wf_00feac76: save-version migration reads redefined `mass` |
| **Catcher-soundness (oracle shares the implementation's misreading)** | If the catcher is an oracle that re-derives the answer (solver, reference sim), is it derived INDEPENDENTLY of the implementation, not from the same spec sentence? | independent second derivation (test-author independence / fresh-family G5) | predicted — wf_00feac76: procgen solvability oracle shares the connectivity misread |

### Witnessed (continued)

| Class (invariant) | Standing question | Catcher hint | Witness |
|---|---|---|---|
| **Evidence-class integrity / prose testability is not authored RED** | Are mixed rows split and is each atomic obligation classified once as behavioral RED or real non-test evidence? Does every behavioral obligation exist in the one independent immutable RED commit, while process order, structural review, owner verdicts and final gates stay outside the test numerator? | separate RED-FREEZE commit plus the repo-native compiler/test runner, then a fresh artifact-backed refutation; BUILD pins and reuses the reviewed commit | GasCoopGame NearGas v21: binding semantic review reported 29/29, but EXECUTE-003 returned 0/29 and no commit because AR-01/06/12/13 were process/structural/gate obligations and F5/CsCheck still required guessed executable APIs |

## Honest ceiling (do not over-claim)

This forces the right *question* and a fail-capable catcher that fires where the bug lives. It does
NOT buy: (1) a first, genuinely-novel class still escapes once — the guarantee is "never the same
class twice," never "never"; (2) presence ≠ truth — the gate checks each class is MARKED and each
catcher NAMED, not that the mark is honest or the regime correctly judged (only the independent review
and the owner eye verify that, and both sample, both later); (3) a confidently-WRONG spec (a wrong rest
predicate) passes faithfully — this attacks silence and mismatch, not authored error; (4) classification
altitude stays human judgment (too narrow → the sibling reads as new; too broad → unactionable).

END_OF_FILE: os/engineering/ESCAPE-CLASSES.md
