# CALL c-exec-033 — Sc-typing: ENV-DERIVED GAS IDENTITY WITH ACCUMULATE-WITH-HYSTERESIS (ENGINE-ONLY)

**STATUS: READY — framed 2026-07-08.** This is the next g-9c41 character-road slice after Sc-reactions. Sc-reactions is DELIVERED, MERGED, and PUSHED to GasCoopGame `main` @484084a (`origin/dev` @f5ba86a, `origin/main` @484084a). This CALL opens a fresh **owner-present PLAN** session in `GasCoopGame_dev`. **PLAN and BUILD are mandatory separate sessions** (engineering contract v19): the PLAN leg ends at owner approval, writes no product code, and commissions no RED tests. A fresh BUILD session starts with an **independent RED test-author first**.

## Direction / road position / base

Direction: indie-game-development / g-9c41 / **Sc-typing** — Sc-types → Sc-weight → Sc-rep → Sc-kernel → Sc-reactions → **Sc-typing** → Sc-damage.

- **Base:** GasCoopGame `main` at-or-after @484084a (post-Sc-reactions merge). Firing on a pre-Sc-reactions base is a STOP.
- **Repo / session:** fresh `GasCoopGame_dev` executor PLAN session, owner present; branch `dev` → `main` only after green and owner-gated.
- **Canon:** `knowledge/g9c41-gas-engine-SPEC.md` §5 dynamic typing + Fact 4 sparse-dominant model; `work/gas-reaction-typing-design-2026-06-30.md`; `work/audit-gas-sim-plan-2026-07-02.md` findings types-mixing-3/4; `history/2026-07-02-s-shape-prep-screactions-001.md` owner decision (e): Sc-typing immediately after Sc-reactions, accumulate-with-hysteresis over instant flip.
- **Engineering contract:** `os/engineering/CONTRACT_VERSION current: 19`; `os/engineering/CONTOUR.md` roles/cycle. If product `validation.config` is <19 at tip, mirror the v19 run-contract clause and bump before approving the PLAN. If mechanical gates are unexpectedly <18, STOP and do a re-sync first.
- **Lock:** ADR-0002 input-lockstep is not reopened. No host-broadcast, no real-2-PC gate, no float authoritative path.
- **ADR:** bind the next free ADR-E-* at the product tip and record siblings in the RESULT.

## Goal

Gas can change **identity** from its environment in the sparse-dominant store: a gas cell reads an authoritative committed-revision env vector, accumulates exposure toward data-defined thresholds, and only after hysteresis crossing flips its dominant type stamp with exact mass conservation. The owner sees in the engine debug view that sustained conditions convert gas predictably, while noisy threshold-adjacent conditions do **not** strobe A↔C. Temperature-keyed rows stay dormant until the deferred temp→gas feedback exists; density/neighbour/reaction-front channels may be exercised now if the PLAN confirms they are live.

**Approach token:** `env-derived-identity-accumulator-hysteresis`.

A delivered artifact whose recorded `approach:` differs — especially an instant env-threshold flip, a same-tick env read, a per-type hardcode branch, or a domain-wide sweep of all gas cells — is a self-authored substitution and needs an owner-ack token. Otherwise STOP-escalate.

## Model Constraints

1. **REGIME vs IDENTITY stays clean.** REGIME means a derived read ("angrier in heat") that moves no mass and folds no new checksum member. IDENTITY means discrete A→C conversion; it is the only thing this slice builds.
2. **Accumulator, not instant flip.** Owner decision 2026-07-02: accumulate-with-hysteresis wins over instant flip. The accumulator is a replicated per-cell field, cell-keyed, SKIP-ZERO, separate from mass/type stamp members. Clamp and hysteresis are data-defined.
3. **Committed env vector only.** Env channels come from already-authoritative state and are read at committed revision with a one-tick lag. Same-tick cross-layer reads are forbidden.
4. **Wake without domain sweep.** Env-delta/reaction-front wake sources must enqueue affected gas cells into the active set. Sleeping saturated gas must respond when its relevant committed environment changes, but Sc-typing must not reintroduce a per-tick sweep over all gas-bearing cells.
5. **Stamp flip is atomic and mass-exact.** Threshold crossing changes dominant type / overlay contents by a canonical gather-then-apply pass. A thrown tick leaves the field byte-unchanged. No silent leak, saturation, wrap, or dense-plane fallback.
6. **Typing rules are data.** Env channels, thresholds, hysteresis bands, source/target TypeIds, dormant-row flags, and accumulator schema fold into the session handshake hash canonically. Unknown channel/TypeId/row kind is a loud build error.
7. **Single-reactant env-response rows get semantics here.** Sc-reactions admitted such rows as schema-only; this slice defines and tests their firing semantics through the accumulator. It does not redesign reactions.
8. **Spawn typing if reachable.** If a generic-parent / typeless spawn path exists at the tip, it reads the committed env and becomes a type through the same data rows. If no production spawn path exists, the PLAN records a minimal headless fixture and keeps runtime spawn hookup out unless cheap and owner-approved.

## Boundaries / STOP

- NO visual/shader/look work; dev2/g-7e15 untouched.
- NO damage/body/loot/wall effects; Sc-damage owns consequences to players/objects and the temp sink.
- NO temp→gas feedback build here; temperature-keyed typing rows are dormant until `d-tempfeedback-001` re-enters at Sc-damage.
- NO instant flip side door, no threshold strobe, no same-tick env read.
- NO domain-wide gas scan as the normal typing engine.
- NO new gas physics beyond identity conversion; no cross-type capacity law; no far-tier / Coarse/ behavior change.
- NO dense `[species][cell]` planes, no stored velocity/inertia, no float on authoritative path.
- NO type-set hardcode dispatch (`if/switch/enum` over TypeId pairs or type identities). Hygiene scans are allowed as discipline checks; do not add a new source-text scanner as behavior evidence.
- A required tool/harness unavailable (Unity Editor, MCP, headless license, etc.) = STOP and ask the owner to launch it; no workaround without explicit written owner-ack.

## Done When

1. **PLAN, owner present, contract v19:** re-sync FIRST; produce a detailed-but-simple owner-readable PLAN in plain language. The PLAN records: (i) change class = core algorithm + user-perceivable behavior property; (ii) the owner-signed observable property ("sustained env exposure converts, noisy boundary does not strobe"); (iii) env channel set for this slice and which rows are dormant; (iv) accumulator schema/member bit and fold discipline; (v) active-set wake source; (vi) stamp/mass atomicity; (vii) ContentHash fold; (viii) property table; (ix) spec-silence audit / escape-class walk / refuted-register walk; (x) ADR-E number; (xi) 2-3 test gases and scenarios. PLAN approval closes the PLAN session. No product code and no RED tests in PLAN.
2. **Independent RED test-author first in BUILD:** a separate test-author reads only the frozen spec/PLAN and writes failing acceptance tests before the builder codes. Builder may not edit those tests.
3. **Accumulator + hysteresis behavior:** sustained env exposure crosses threshold after the expected ticks and flips A→C; sub-threshold exposure does not; a noisy value around the threshold does not strobe; clamp/hysteresis are exact. Negative controls prove instant-flip and non-hysteretic implementations fail.
4. **Committed-revision env read:** a same-tick env mutation does not affect typing until the next committed tick. A planted same-tick read fails.
5. **Active-set wake:** env-delta/reaction-front wake enqueues affected gas cells without a full gas-domain sweep; a sleeping gas cell under a changed relevant env channel accumulates after wake. Dormant temperature rows do not fire.
6. **Checksum member:** accumulator folds as a new cell-keyed SKIP-ZERO MeaningChecksum member with isolation and distinctness REDs. Mass/type stamp changes fold under their existing members. Byte-identical no-typing golden still reproduces.
7. **Handshake hash:** typing rows + env channel registry + thresholds + hysteresis + dormant flags fold canonically. REDs: divergence for changed thresholds/targets/channels; convergence for authoring order; length/count guard prevents aliasing; unknown ids throw loudly.
8. **Atomic mass/stamp conversion:** conversion is mass-exact across dominant/overlay lanes; thrown/out-of-range rows leave the field byte-unchanged; no wrap/saturate/drop.
9. **Spawn typing disposition:** production spawn path is either implemented through the same data rows and tested, or explicitly recorded as not present/fixture-only with no silent promise. Generic parent never appears as a live gameplay type unless owner-approved.
10. **No-regression + scans:** loopback determinism green over typed scenarios; zero-float and int-overflow scans cover new authoritative code; type-hardcode scan scope honestly covers the typing path as a secondary tripwire; no new source scanner is used as behavior evidence.
11. **Deliver gates:** `check.ps1 -Deliver` GREEN at the tip contract version (v19 honored; mechanical gates through v18 confirmed or re-synced), mutation >=70 on new Core, negative-control pass, property-layer pass for core algorithm, review-evidence recorded and fresh, refuted-register and fix-class-closure satisfied, cited artifacts exist, RESULT.md = DELIVERED.
12. **Fresh-session G5:** separate fresh refutation, different model family if available, cannot refute: accumulator-not-instant, committed-revision env read, wake-without-sweep, cell-keyed checksum member, handshake fold, atomic mass/stamp conversion, dormant temperature rows, no dense/float/type-hardcode regressions. In-session pre-pass is not the binding G5.
13. **Owner-eye confidence:** owner sees an engine debug scenario where sustained conditions convert a gas identity, noisy boundary does not flicker, and the result is understandable enough to carry forward to Sc-damage. Owner-eye is recorded separately from BUILD existence.

## Return

A RESULT routed HOME to Direction OS with:

- outcome and evidence (commits, `check.ps1 -Deliver` transcript, mutation/negative-control/property results, review file, G5 verdict/family, loopback hashes, RED-control trips);
- the owner-approved PLAN decisions (i)-(xi);
- the chosen ADR-E number and siblings;
- explicit disposition for every done_when bullet above;
- owner-eye notes;
- assumptions/cuts/cost;
- `next:` back to the direction.

dev→main merge + push are owner-gated. On GREEN and close verification, road rolls to **Sc-damage**.

## Budget

Mandatory split: **PLAN session** (owner-readable plan, owner approval, no code/no red tests) → **fresh BUILD session** (independent RED test-author first, then build). If BUILD is too large for one focused half-day, split by machinery:

- Leg 1: accumulator schema/member + handshake fold + committed-revision env read + no-typing byte identity.
- Leg 2: active-set wake + stamp/mass conversion + spawn disposition + owner-eye scenario.

END_OF_FILE: live/indie-game-development/work/c-exec-033-sc-typing-call.md
