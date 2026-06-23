# converge-g-9c41 — formed question set (RETROFIT, FORM pass)

> 🔴 **SUPERSEDED (s-research-017, 2026-06-22).** Netcode/replication-модель этого дока (host single-writer + chunked-delta +
> «клиенты реконструируют, не считают сами») и band-graph масштаб ПЕРЕКРЫТЫ локом 2026-06-22 (input-lockstep; одно целочисл.
> cell-модель; газ 50см-global; room-rollup обязателен) → `work/dev-plan-graph-2026-06-22.md` +
> `gas-cellsize-levelscale-2026-06-22.md` §1-§12. Файл = Wave-1/2 converge-ИСТОРИЯ (метод/контракты валидны), НЕ активный
> неткод-авторитет.

> **Status: FORM pass only (checkpoint).** This document FORMS the converge question-set for node
> g-9c41 and stops. Per CALL c-converge-001 boundaries it does NOT answer open questions with the
> owner, does NOT run converge-arch / converge-verify / shape, and decides NO HOW value. Open rows
> staying `open` is EXPECTED here — forward-clean (`rg -c open` = 0) is the exit criterion of the
> later resolve+verify passes, not this one. The active bet (t-1/t-2/t-3, c-exec-003) is untouched;
> this is a parallel retrofit on the same node.

## Header — triage & import

```
triage: HEAVY — converge ON — because model? YES (the chunked-delta gas stream is model-bearing:
        a wrong stub is fatal and it defines the networked product) AND contract? YES (consumes/
        produces across 4 siblings g-d3a8/g-7e15/g-5b07/g-e6f2 + DA/PGG generators) AND decomposes
        into subsystems (field / stream / render-seam / ingestion / scale tier).
mode:   RETROFIT — node g-9c41 is active/in-flight (bet committed s-shape-003); import settled
        decisions born-closed (step 1), frame only what is still open.
imported_from: [history/s-shape-003 (d-arch-001 a–e, R5/R12/R13/R14/R15, vendor=FishNet, cut_list),
                history/s-work-004 (kill-gate "A" dual guarantee + reconstruction/anti-gaming facts),
                history/s-work-003 via NOW.md (t-1 GREEN core/seam contracts)]
knowledge_scan: knowledge/ EMPTY (no canon yet) — imports come from history/ only.
next_movement: heavy + sibling-bearing -> converge-arch for the grid↔gas / gas-type-seam / render-
               seam / ingestion contracts; the mechanism-parameter rows route to PLAN/ADR-0003.
```

**HARDENING NOTE (design-doc fix b, load-bearing).** The imported kill-gate "A" (I6–I11) NAMES the
chunked-delta mechanism and its dual guarantee. Per Resolve 3(c), *closing a mechanism never closes
its parameters*: importing "A" closes the PROPERTIES (bit-exactness, bounded divergence, settle
convergence, both-clamps-engaged) but leaves every internal MAGNITUDE (Q, deadband, the two clamps,
N, K, channel reliability, …) OPEN as → PLAN rows in §WHAT-C. This is exactly the witness fix — without
it a retrofit would swallow the stream and never mint Q/N/K.

---

## §GLOSSARY — disputed terms (read 2+ ways on disk)

Seeded mechanically from done_when + lens nouns; only terms read 2+ ways qualify (miner pass
wf_cfafde76-73f). TERM-PROPERTY RULE: a §WHAT line cites a term only for a property in its row.

| id | term | meaning-here (load-bearing properties) | competing readings (on-disk) |
|---|---|---|---|
| G:chunk | chunk (chunked-delta / dirty-chunk / chunk-grid) | quantized delta unit streamed host→client; only CHANGED chunks sent; carries a revision + resolution-key; on-wire BYTE size is the first honest measurement; per-tick dirty-COUNT is the environment-independent number | WIRE-UNIT (0.6–6 KB payload, NOW p4) vs SPATIAL CELL-GROUP / storage block (brief §3.5/§3.6 "chunked-хранилище слоёв", "256 чанков") vs CHUNK-GRID profile (NOW "chunk grid, total chunk count") |
| G:topology-change | topology change / revision | fires deterministically on an agreed tick; two rooms merge / breach portals added; carries a topology-revision exposed by debug surfaces; consistency must hold ACROSS it | DESTRUCTION-DRIVEN (TREE goal, root #4) vs SCRIPTED-BREACH-ONLY no destruction system (NOW cut_list, t-2) vs STATIC-GRAPH portals on immutable volumes (brief §3.7) |
| G:consistency | consistency / consistent gas behavior | the owner-signed acceptance oracle; **signed "A"** = BOTH readings at once, in TWO runs | PER-TICK BIT-EXACT lossless (s-work-004 (i)) vs BOUNDED-DIVERGENCE-≤Q + converge-at-settle lossy (s-work-004 (ii)) |
| G:meta-gas | meta-gas / gas / gas type | two-level: meta-gas = behavior archetype (own handler behind extension seam) / gas = pure config; R15 layered params; R5 field-transported | BEHAVIOR-ARCHETYPE+seam (#4, R15) vs FIELD-TRANSPORTED-config R5-refined (AGENT_SUBSTRATE removed — supersedes brief §3.3) vs DESIGN-ROSTER gameplay-job (sibling g-d3a8) |
| G:coarse-tier | coarse simulation tier / band sim / coarse truth | DESIGNED + ARITHMETIC-VALIDATED (not built) to hold ~200×200×40 m, ≥1000 volumes within min-spec budgets; clip rendered FROM band state | SECTOR-BAND GRAPH 2–3 bands (brief §3.1, approach) vs DAY-ONE 1-sector/2-band degrading to scalar-per-volume (cut_list, brief §5) vs ARITHMETIC-PAPER-ONLY for this node (#9) |
| G:min-spec | min-spec profile / class | 8GB-VRAM 60-class GPU + 16GB RAM (NOT the dev 4090); gates perf (#1), render ms-budget (#6), scale budgets (#9) | HARDWARE acceptance floor (#1) vs CHEAP-VALIDATION proxy (3060 / capped) vs UNMEASURED ARITHMETIC anchor pending micro-bench (brief §4/§7) |
| G:agent-drivable | agent-drivable / agent | harness machine-drivable: headless, deterministic seeds, machine-readable telemetry, no sprawl | HARNESS-DRIVER (#5) vs AI-SELF-PLAY actor (g-d3a8 #5) vs VISION/RED-TEAM/BUILD-VALIDATE LLM (g-7e15 #2, model_routing) vs the REMOVED AGENT_SUBSTRATE gas (R5) |
| G:harness | validation harness / harness scene | headless, deterministic seeds, machine-readable telemetry, NO scene sprawl; hosts the hash check; supports product-visuals for the clip | NET-CONSISTENCY HASH-RIG (brief §5, t-1) vs FIXED PRODUCT-SCENE SET (#5) vs CLIP/RENDER STAGE (#8, g-7e15 #1/#5) |
| G:destruction | destruction / spatial change / destruction-driven | node needs ≥1 destruction-DRIVEN topology change; the bet delivers a scripted breach (no destruction system) | DESTRUCTION SYSTEM gameplay-depth (charter lens 2, #3, pre-mortem #3) vs SCRIPTED-BREACH stand-in (cut_list) vs SPATIAL-CHANGE root-level OR (root #4) |
| G:replication | replication model | LOCKED: host single-writer field + chunked-delta; entity ghosts only for players/objects; GPU never authoritative | SINGLE-WRITER chunked-delta FIELD (t-2) vs LOCKSTEP inputs-only (t-1, ADR-0002) vs ENTITY GHOSTS for non-gas — THREE coexisting planes, must not conflate |
| G:render-slice | render proof slice / stylization | timeboxed ≤2wk; locks the stylization hypothesis (default quantized volumetrics) + render-pipeline decision behind a SEAM; ms-budget on min-spec; clip from band state, no T2 | SEAM-LOCK decision artifact (#6) vs CLIP-PRODUCING render (brief §5/§8) vs DOWNSTREAM g-7e15 visual-identity pipeline (g-7e15 #4 — g-9c41 only locks the seam) |
| G:player-count | player count / player-hosted / 1-player / co-op | clean 1-player must run; count = first-class CONFIG input, no bots; fantasy range 2–4 co-op-first | CONFIG-INPUT parametric (#7, g-d3a8) vs FIXED 3-PEER net-spike topology (t-2: 1 host + 2 clients) vs PLAYER-HOSTED listen topology (R12) |
| G:ingestion | procedural generators / ingestion adapter (DA / PGG) | REPLACEABLE adapter is the WHAT (seam survives); generator behind it is HOW; DA day-one minimum, PGG parked | NAIVE day-one adapter ~100–300 objects vs FULL occupancy+1000-object gate (bet-2) vs REPLACEABLE-SEAM proven on DA alone (PGG behind same seam) |
| G:settle | settle / quiescence point | the tick at which lossy client MUST equal host bit-exact; defines C8's predicate N + the non-vacuous post-breach settle assertion | NETWORK quiescence (dirty-chunks==0 for N ticks) vs PHYSICAL re-equilibration after breach (brief §3.1/§3.5 merged rooms relax) vs HASH-equality convergence — conflated in the "settle/keyframe" kill-gate wording; resolve must also sign that post-breach physical re-equilibration is GUARANTEED to produce a network-quiescence settle (else C8's assertion can fail to fire) |
| G:temperature | температура / energy | **RESOLVED 2026-06-14 (s-converge-002):** a thin DYNAMIC LAYER in the core — own data structure + minimal optimized sim, sibling of gas, on the grid event/revision bus (subscribes to events, can feed/read reactions); in core to PROVE layer-extensibility + cross-system interaction, NOT for gameplay/aesthetics | STATIC field for stratification/R4 contract (brief §3.8) vs THIN DYNAMIC LAYER for architecture proof (owner R2/R3) vs NONE — resolved = thin dynamic layer (see §RESOLVED-1) |

`canon_proposed (glossary ids -> review/pulse promote to knowledge/)`: G:chunk, G:consistency,
G:replication, G:coarse-tier, G:topology-change (the net-consistency vocabulary t-3 + future net work
will read). converge proposes; review/pulse promote (authorship rule).

---

## §WHAT — flat question set (one question / line)

Tags: `answered` (born-closed import, cited source) · `open→PLAN` (HOW magnitude/format — ADR-0003) ·
`open→G7` (owner-owned design/acceptance fact — a later resolve pass signs) · `open→arch`
(cross-node contract — converge-arch). A row carrying both a property and a magnitude SPLITS (the
property half may be `answered`, the magnitude half `open→PLAN`). No row is signed in this FORM pass.

### §WHAT/IMPORTS — born-closed (answered, decided before this node converged)

| id | the decided WHAT | tag | source |
|---|---|---|---|
| I1 | Replication LOCKED: host = single authoritative writer of the gas field; clients RECONSTRUCT without running the sim; entity ghosts only for players/objects; GPU never authoritative for networked state. *(NAMES the mechanism → params decompose in §WHAT-C.)* | answered | history/s-shape-003 (node #2) + history/s-work-004 (THE PIVOT) |
| I2 | The gas field rides OUR OWN custom chunked-delta channel ALONGSIDE FishNet — a SECOND plane, never retrofitted into `ITickInputBus` (input-only). | answered | history/s-shape-003 (R14) + NOW boundaries |
| I3 | Network vendor = FishNet; model locked, vendor swappable; no P6 / vendor re-open in this leg. | answered | history/s-shape-003 |
| I4 | Engine-free pure-C# integer-only authoritative core (R13); determinism contract (no float/double, `unchecked`, seeded RNG, pinned little-endian hash order, stable input order); 8 core tests + golden vector green. | answered | history/s-shape-003 (R13) + s-work-003 via NOW |
| I5 | 3-mode composition root (pure-local / local host-loop / networked) chosen at the DI root (`CreateNetworked(seed,localPeerId,injectedBus)`); player count = first-class config; no bots/AI companions. | answered | history/s-shape-003 (R13/R14) + node #7 |
| I6 | Kill-gate "A" = the DUAL guarantee defines "consistency holds" (resolves p2-vs-p3 as TWO runs, not one). *(NAMES the mechanism → params decompose.)* | answered | history/s-work-004 |
| I7 | Lossless (i): deadband OFF → per-tick host-vs-each-client reconstructed-field-cell hash BIT-EXACT over the whole run incl. the breach (the correctness oracle). | answered | history/s-work-004 + NOW p2 |
| I8 | Lossy (ii): deadband + both clamps ON → divergence BOUNDED every tick + convergence to bit-exact at settle/keyframe. *(PROPERTY closed; magnitudes Q/N/K/deadband/clamps stay open in §WHAT-C.)* | answered | history/s-work-004 + NOW p3 |
| I9 | Hash domain = reconstructed FIELD CELLS only (Fnv1a64 pinned LE, reused from t-1) — NOT whole `SimState.Hash()` (folds Delta+RNG the non-simulating client lacks); breach-affected cells inside the domain. | answered | history/s-work-004 + NOW p2 |
| I10 | Anti-gaming: lossless (p2) and lossy (p3) MUST share the SAME reconstruction code path. | answered | NOW p3 |
| I11 | All THREE flow controls (deadband + per-client clamp + aggregate host clamp) must exist and be engaged together (a silently-disabled clamp = FAIL). *(PROPERTY; the three magnitudes stay open.)* | answered | NOW p3 + history/s-work-004 |
| I12 | R5-refined: special/anomalous gases are FIELD-TRANSPORTED by the same simulation, NOT agents/enemies/self-directed; distinguished by params+visual+effects; AGENT_SUBSTRATE + velocity-intent REMOVED from the concept. | answered | history/s-shape-003 (R5) |
| I13 | R15: layered gas params — shared parent params for ALL gases (density, per-cell packing, spread speed) + per-meta-gas own params + per-meta-gas visual procedurally generated from params; specific gas = pure config. | answered | history/s-shape-003 (R15) |
| I14 | R12: one player hosts; no dedicated server, ever (decided, not researched). | answered | history/s-shape-003 (R12) |
| I15 | d-arch-001(a): the far/coarse tier is always-on, NEVER frozen; 1 Hz cold-rung counts as never-frozen. *(10/5/1 Hz ladder magnitude → PLAN, bet-2.)* | answered | history/s-shape-003 |
| I16 | d-arch-001(b): far-consequence latency bound = sim ≤100 ms / perceived 100–300 ms. | answered | history/s-shape-003 |
| I17 | d-arch-001(c): stratification = 2–3 bands + a derived interface height (N bands = config). *(band-count magnitude → PLAN.)* | answered | history/s-shape-003 |
| I18 | d-arch-001(d): SUPERSEDED by the R5 reframe — scalar source/sink driver day-one; velocity/agent removed (not merely deferred). | answered | history/s-shape-003 |
| I19 | d-arch-001(e): the perception-ceiling question is answered inside the render slice (criterion 6). | answered | history/s-shape-003 |
| I20 | Late-join / join-baseline is OUT of t-2 scope: all 3 peers present from tick 0; only the revision/keyframe baseline FORM is declared; mid-run join → bet-2. | answered | NOW boundaries |
| I21 | Node-vs-bet scope (cut_list): physical destruction → scripted-breach event only (no destruction system); T2 / sector-subdivision / freq-ladder / DA occupancy+1000-object gate → bet-2; PGG / 2nd generator → parked; tick rate = 10 Hz day-one. ⚠ **PARTIALLY SUPERSEDED 2026-06-14 (s-converge-002):** "scripted-breach only" → RESOLVED-2 (real CONTROLLED breach); cut_list "day-one static temperature field" → RESOLVED-1 (thin DYNAMIC temperature layer). Other cuts (T2/sector/freq-ladder/DA-gate/PGG/10Hz) STAND. | answered (partial supersede) | history/s-shape-003 (cut_list) + history/s-converge-002 |
| I22 | Process: the G0 ledger is frozen BEFORE build, default-FAIL (every entry opened failing, flipped only on opened evidence), builder never edits ledger/spec/criteria/config. | answered | NOW (leg_opens_with + Process) |
| I23 | Replication criterion-2 sub-clause: rollback/lockstep is bounded to AT MOST one 1–2-week timeboxed spike; inputs ride lockstep (ADR-0002), the field never as inputs; the P6 spike (FishNet↔NGO, last-resort rollback) is the only escape, not an extend. | answered | history/s-shape-003 (node #2) + NOW kill_by (P6 1–2wk timebox) + ADR-0002 via NOW |

### §WHAT-C — mechanism decomposition: chunked-delta gas stream (the witness rows)

The node's done_when #2 LOCKS "chunked-delta gas stream"; atomically split into one question per
internal parameter (recursive sub-mechanisms re-split). **These are the values ADR-0003 would invent
ad hoc** — minted HERE as named questions instead. Each row shows the PROPERTY side (often `answered`
via I6–I11) and the MAGNITUDE side (`open→PLAN`).

| id | parameter / forced question | property side | magnitude side | tag |
|---|---|---|---|---|
| C1 | integer/fixed-point field-cell representation (bit-width / fractional scale) so "bit-exact" is well-defined | exact integer truth, no float in authoritative state →G:consistency[lossless], cites I4 | repr / bit-width / scale | **open→PLAN** (prop answered I4) |
| C2 | quantization step **Q** applied to a cell delta before the wire | deterministic one-way quant; recon error/cell ≤ Q; quantized values never overwrite host truth | numeric Q | **open→PLAN** |
| C3 | divergence threshold/bound (lossy mode) — **THE WITNESS SPLIT** | bounded EVERY tick; a provable consequence of deadband+quant, not a tuned knob (cites I8); any tick > bound = recon bug →G:consistency[lossy] | value (recommend = Q) | **split: prop answered I8 · magnitude open→PLAN** |
| C4 | deadband magnitude (suppress-small-change threshold) | OFF = lossless oracle / ON = lossy mode (cites I7,I8); shared recon path (I10) | numeric deadband | **open→PLAN** (prop answered I7/I8) |
| C5 | per-client bandwidth clamp | engaged, hard-bounded per client (cites I11) | ~150 KB/s | **open→PLAN** (prop answered I11) |
| C6 | aggregate host bandwidth clamp (across all clients) | engaged, hard-bounded aggregate — the binding uplink limit (cites I11) | ~250–300 KB/s | **open→PLAN** (prop answered I11) |
| C7 | gas-plane channel reliability (unreliable-sequenced vs reliable) — **its OWN decision, not a carryover** | a 2nd plane whose reliability is decided on merits, not inherited from the input bus's reliable design; correctness under the chosen mode must be proven (cites I2) | unreliable-seq vs reliable + config | **split: prop open→G7 · magnitude open→PLAN** |
| C8 | settle predicate **N** (dirty-chunks==0 for N ticks) →G:settle | client converges to bit-exact at every settle incl. post-breach; ≥1 real quiescence settle asserted (non-vacuous) (cites I8); resolve must confirm post-breach physical re-equilibration GUARANTEES a network-quiescence settle (else the non-vacuous assertion can fail to fire) →G:settle[network-quiescence] | numeric N | **open→PLAN** (prop answered I8) |
| C9 | keyframe cadence **K** (or quiescence-only) | IF in scope, post-keyframe tick is bit-exact (≥1 non-vacuous); ELSE keyframes out of t-2 = a signed scope boundary | numeric K | **split: prop open→G7(scope) · magnitude open→PLAN** |
| C10 | wire / delta payload format + resolution key | each chunk carries a resolution key (unambiguous across tiers); on-wire byte size = the honest first measurement; the FORM survives to the band sim | header/encoding byte layout (fp32/8-bit day-one; fp16 OUT) | **split: prop open→G7-light · magnitude open→PLAN** |
| C11 | single-writer-per-(layer×phase) + phase ordering | IF hard-gated, exactly one writer per (layer×phase), proven by a NEGATIVE/seeded-violation test (2nd writer rejected → red), not happy-path | phase table / write-lease form | **split: prop open→G7 · magnitude open→PLAN** |
| C12 | revision barrier / change-feed form | REAL exercised contracts (p1-gated, not prose); out-of-order/stale chunk never applied; recover to bit-exact at next settle; survives to band sim →G:chunk[revision] | revision-counter width / barrier encoding | **split: prop open→G7(+p1) · magnitude open→PLAN** |
| C13 | chunk loss/reorder fault-injection scope (inject in t-2 vs defer to t-3) | inject → unreliable-path correctness RETIRED; defer → p2 downgrades to clean-channel round-trip, gap-recovery still defined (recommend inject) | seeded drop/reorder schedule | **split: scope open→G7 · magnitude open→PLAN** |
| C14 | min-resend interval per chunk (per-chunk rate limiter) — *converge-DERIVED: NOT in NOW's enumerated ADR-0003 list; resolve confirms or drops* | a hot chunk cannot saturate the channel; deterministic send schedule | interval (ticks/ms) | **open→PLAN** |
| C15 | frozen toy-field scene profile (room count, chunk grid, total chunk count) | FROZEN, committed as config/seed; sceneProfileHash pins it; t-3 reuses byte-for-byte; exercised through the REAL registry+feed →G:chunk[chunk-grid] | the concrete counts (decode brief "32/12/2" = scene size ≠ peers) | **split: prop open→G7(repro) · magnitude open→PLAN** |
| C16 | reproducibility constants (seed, run length, breach tick, target-tick) | breach fires same tick on all peers (lockstep broadcast); target-tick = MAX aggregate dirty-chunk tick (worst-case, not cherry-picked); validator-reproducible via dotnet+golden vector | seed / runTicks / breachTick / targetTick / pinned 10 Hz (rate answered I21) | **split: prop open→G7(repro) · magnitude open→PLAN** |
| C17 | peer count = exactly 1 host + 2 clients = 3 peers | oracle topology fixed; host = single writer, clients reconstruct; distinct from scene size | 3 | **answered** (NOW Reproducibility) |
| C18 | measurement artifact schema + named path (honest dirty-chunk wire bytes + dirty-rate) | honest PEAK-through-breach (NOT steady, NO clamp verdict — t-3); both modes emit distinct non-empty artifacts covering the breach range (dropped mode = FAIL); 0.6–6 KB = logged sanity ref only, not a gate | schema fields + path (e.g. docs/measurements/) | **split: prop open→G7(acceptance) · magnitude open→PLAN** |
| C19 | **client-side reconstruction arithmetic determinism** (smuggled inside I1/I4 — folded from verify) — the host core is integer-deterministic (I4) but the CLIENT reconstructs on a SEPARATE path (dequantize→apply→accumulate); bit-exact host-vs-client (I7) + bounded \|client−host\| (I8) BOTH require the client recon arithmetic itself be integer-deterministic + cross-platform-stable | no float dequant; pinned accumulation order; I10 only shares the path across MODES, never asserts the path is deterministic | the dequant/accumulate representation | **split: prop open→G7 · magnitude open→PLAN** |
| C20 | **client chunk apply-order / keyframe-vs-delta interleave canonicalization** (deeper than C12 — folded from verify) — C12 fixes WHICH revision wins, not the order a client applies multiple in-revision non-conflicting chunks within one tick, nor keyframe-vs-same-tick-delta interleave; I9 hashes reconstructed cells, so values must be apply-order-INDEPENDENT or a canonical client apply-order pinned (else two clients diverge with NO stale/out-of-order fault) | host hash order (I9) + host write discipline (C11) pinned; CLIENT apply-order is NOT | canonical apply-order / interleave rule | **split: prop open→G7 · magnitude open→PLAN** |
| C21 | **layer registry contract** (distinct from C12's revision feed — folded from verify; NOW p1 gates "layer registry + revision feed" as TWO contracts, brief §3.9 component #2) | REAL exercised (p1-gated, not prose); one layer per registration; survives to the band sim →G:chunk[storage] | registry schema / layer-key form | **split: prop open→G7(+p1) · magnitude open→PLAN** |
| C22 | **lossy reconstruction mass-error bound** (crit-3 ↔ stream interaction — folded from verify) — bounded PER-CELL divergence (C3, \|client−host\|≤Q) does NOT imply bounded TOTAL-MASS error: N deadband-suppressed cells each ≤Q sum to N·Q aggregate drift (the brief §3.5 FATAL-2 remainder-bucket exists for exactly this) | must decide whether lossy recon CONSERVES mass exactly / within a stated bound, or only DISPLAYS it (A2.2); contract survives to band sim | the conservation bound / remainder-bucket form | **split: prop open→G7 · magnitude open→PLAN** |

*(Cross-refs, not re-opened: hash-domain = I9 (answered); client-reconstructs-without-sim = I1
(answered, but its determinism is now C19); late-join scope = I20 (answered).)*

### §WHAT-A — per-criterion questions (not already a mechanism param or import)

| id | question | tag | cites |
|---|---|---|---|
| A1.1 | the canonical min-spec floor as an acceptance target (GPU class/VRAM/RAM/CPU) — hard floor vs extrapolated class? | open→G7 | G:min-spec[hardware] |
| A1.2 | which metrics constitute "targets met" (host gas-tick ms, frame ms, memory residency, bandwidth)? | open→G7 (set) | crit 1 |
| A1.3 | the per-tick gas-sim ms-budget value on min-spec (brief ≤4 ms, or ≤6–8 ms) | open→PLAN | G:min-spec |
| A1.4 | acceptance rule that makes a capped/3060-proxy measurement count as "met" | split: prop open→G7 · method open→PLAN | G:min-spec[cheap-validation] |
| A1.5 | is perf measured under breach-load (worst-case) or steady, and which scene/tick is binding? | split: prop open→G7 · scene open→PLAN | crit 1 |
| A1.6 | day-one perf bar scope — toy-field + band state only, or full coarse tier? | open→G7 | I21 |
| A1.7 | **whole-frame min-spec budget closure** (crit-1 ↔ crit-9 interaction — folded from verify): A1.3 (gas ms) + A5.3 (render ms) + A8.3 (coarse-tier tick ms) + B12 (sim/visual split) are NOT independent — all draw on ONE min-spec 60-class frame (anchor UNMEASURED, K-species ×2–4); does the SUM fit one frame on the SAME profile crit-9 validates at ≥1000 volumes? crit-1 "perf met" and crit-9 "scale arithmetic" are scored against the SAME envelope and can contradict | split: prop open→G7 (single-envelope, no double-spend) · magnitudes open→PLAN | crit 1 ↔ crit 9, G:min-spec |
| A3.1 | what does a meta-gas handler implement / read-view / write (the extension-seam contract)? | open→arch | G:meta-gas[archetype-seam] |
| A3.2 | the "pure config / data-alone" schema — what fields, what is forbidden from carrying code? | open→PLAN | G:meta-gas[config] |
| A3.3 | "a third gas type lands by data alone and passes the harness" — the binding declarativeness acceptance test | open→G7 | crit 4 |
| A3.4 | stable integer species ids (config, not declaration order) for deterministic wire/hash/replay | open→PLAN | I4 |
| A3.5 | day-one scope of criterion 4 — is the two-level model exercised (toy) or only its FORM declared, real handlers deferred? | open→G7 | I21 |
| A2.1 | which debug surfaces must exist and what each exposes (mass / flows / tick / topology revision) | split: prop open→G7 · format open→PLAN | crit 3, G:topology-change[revision] |
| A2.2 | mass-conservation invariant (host mass vs reconstructed) exposed so a violation is visible — acceptance property? | open→G7 | crit 3 |
| A2.3 | the "video" deliverable for crit 3 (debug-overlay consistency capture) vs the crit-8 spectacular clip; who captures (MCP/owner)? | split: prop open→G7 · pipeline open→PLAN | crit 3 |
| A2.4 | binding evidence split: dotnet in-memory PRIMARY vs FishNet/PlayMode transport CONFIRMATION (may wait for owner without failing the leg) | open→G7 | NOW/s-decide-001 |
| A4.1 | the fixed scene set the harness must contain (room-chain / ventilation / vertical-shaft) + count — the anti-sprawl binding set | split: prop open→G7 · count open→PLAN | G:harness, crit 5 |
| A4.2 | "agent-drivable" operationally — runs launchable+assertable by an agent (Unity MCP / dotnet test) with no manual steps | open→G7 | G:agent-drivable |
| A4.3 | "no scene sprawl" as an enforceable rule (one scene set; _scratch never committed; dev-worktree only) | split: prop open→G7 · rule open→PLAN | G:harness |
| A5.1 | the stylization hypothesis (default quantized volumetrics) + what "locked" requires (read-at-a-glance vs feasibility-only) | open→G7 | G:render-slice |
| A5.2 | the render-pipeline decision behind the seam (URP/HDRP/custom) + what the seam guarantees so it swaps without touching sim | open→arch | G:render-slice |
| A5.3 | the render ms-budget value on min-spec class | open→PLAN | G:min-spec |
| A5.4 | timebox ≤2 wk + the cut/fallback if exceeded (cannot eat the G3 window) | open→G7 | crit 6 |
| A5.5 | which scene/state feeds the slice (scripted breach → heavy gas pours/fills bottom-up) — the binding render-proof scenario | split: prop open→G7 · scene open→PLAN | crit 6 |
| A5.6 | is the render slice in the day-one bet (clip ~2026-07-10 needs an explicit owner) + the boundary to g-7e15's full visual identity | open→G7 | crit 6, G:render-slice |
| A6.1 | what a "clean 1-player session" must demonstrate (1-player parity, same determinism/hash discipline) | open→G7 | G:player-count |
| A6.2 | the 1-player path composition (host-loop stream path vs direct field read) — single-writer/reconstruct identical? | open→PLAN | I5 |
| A7.1 | the "spectacular" acceptance bar = owner's explicit gamer-eye verdict; owner is sole acceptor | open→G7 | crit 8 |
| A7.2 | milestone-as-gate sequencing — first clip opens the parallel tracks (g-7e15 / g-5b07 slice / g-e6f2) | open→G7 | root map_order |
| A7.3 | AI-generated imagery/video FORBIDDEN in the clip (real captured footage only; AI editing/captions OK) | open→G7 | g-e6f2 policy |
| A8.1 | the canonical R1 scale profile to validate against (~200×200×40 m, ≥1000 volumes, volume mix) | split: prop open→G7 · numbers open→PLAN | crit 9, G:coarse-tier |
| A8.2 | the coarse-tier representation whose scale is validated (sector-band graph, shared geometry, derived interface heights) | open→arch | G:coarse-tier |
| A8.3 | the three budgets the arithmetic must satisfy on min-spec (memory residency, coarse tick ms, far-summary bandwidth) + each value | split: prop open→G7 · magnitudes open→PLAN | crit 9, G:min-spec |
| A8.4 | the bandwidth arithmetic must use the MEASURED dirty-chunk size (C18), not an assumed value | split: prop open→G7 · value open→PLAN | C18 |
| A8.5 | what evidence standard makes the arithmetic "validated" (≥2 independent recomputes, named assumptions, uncertainty ranges) | open→G7 | crit 9 (guarded) |
| A8.6 | memory-residency invariant (coarse state L3-resident <~4 MB) at K=4 and K=8 species | split: prop open→G7 (L3/cache-resident invariant) · magnitudes open→PLAN | crit 9 |
| A8.7 | is the quasi-steady pressure-closure solve (sealed room + source → outflow) part of the validated coarse architecture or out of day-one scope? | open→arch | crit 9 (brief §3.1 fix) |
| A8.8 | the per-band ENERGY/TEMPERATURE state dimension (folded from verify): coarse-column state = masses-by-species (K) + energy/temperature; a static temperature/energy field is MANDATORY day-one (brief §3.1/§3.8; cut_list keeps a static temperature field, cuts only dynamic thermics) — the crit-9 memory arithmetic (~0.75 MB @K=4) already includes it, so it must be named | split: prop open→G7/arch (validated state dimension) · per-band-vs-per-species magnitude open→PLAN | crit 9, G:coarse-tier |

### §WHAT-B — cross-node edges (consumer-driven contracts → mostly converge-arch)

| id | edge | observable contract question | tag |
|---|---|---|---|
| B1 | g-9c41→g-d3a8 | gas-type EXTENSION SEAM: what handler interface must a new meta-gas archetype implement; what may it read/write? | open→arch |
| B2 | g-9c41→g-d3a8 | third-gas-by-DATA-ALONE config surface (R15 layered params): which properties are config vs need a handler; is "passes the harness" the guaranteed acceptance? | split: arch + open→G7 |
| B3 | g-9c41→g-d3a8 | simulability capability set + named EXCLUSIONS (no agent/self-directed per R5, no velocity-intent day-one) the grammar is checked against | open→arch |
| B4 | g-9c41→g-d3a8 | reaction / mixing-into-new-gas registry contract (declarative intensive-threshold reactions, consequence-event outputs) | open→arch |
| B5 | g-9c41→g-d3a8 | consequence/event plane contract (typed events: location/magnitude/species, proximity-INDEPENDENT, revisioned, outrun lossy chunks) + latency bound (cites I16) | open→arch |
| B6 | g-9c41→g-d3a8 | agent-self-play harness interface over EXECUTABLE gas configs (the 2nd validation lane); minimum core capability + day-one vs later | open→arch |
| B7 | g-9c41←g-d3a8 | co-op roles / asymmetric responsibilities the core's player-count-config + host-authoritative model must support | open→G7 |
| B8 | g-9c41→g-d3a8 | flagship/anomalous special-gas CUSTOM-driver/visual contract + out-of-scope (AGENT_SUBSTRATE parked, velocity-intent gated) | open→arch |
| B9 | g-9c41→g-7e15 | render-pipeline SEAM (locked by crit 6) the visual pipeline sits behind; what it exposes so visuals are a DERIVATION of sim state | open→arch |
| B10 | g-9c41→g-7e15 | R15 procedural-visual params source (per-meta-gas visual from params): which params drive distinguishability; read from published field state? | open→arch |
| B11 | g-9c41→g-7e15 | sim-state READ MODEL the visual pipeline samples (IGasReadModel published-revision, sub-band height interpolation, resolution key) | open→arch |
| B12 | g-9c41↔g-7e15 | min-spec ms-budget SPLIT between sim and visual layer; who owns the boundary | split: arch + open→G7 |
| B13 | g-9c41→g-7e15 | vision-agent blind-check GROUND TRUTH (machine-readable: how many gases / where danger / where flow) the clip is compared against | open→arch |
| B14 | g-9c41→g-7e15 | flagship menace motion — is the threat-conveying silhouette/motion a guaranteed derivation of sim state or g-7e15-authored on top? | open→G7 |
| B15 | g-9c41→g-5b07 | clip artifact form (the ~2026-07-10 first clip): resolution/format/capture path; product-visuals vs debug overlay | open→PLAN |
| B16 | g-9c41→g-5b07 | the minimum solo-startable playable slice the free co-op demo consumes from the clean 1-player core | split: arch + open→G7 |
| B17 | g-9c41→g-5b07 | distributable build / the gap between harness direct-connect and the demo+Steam-Playtest netcode | split: arch + open→G7 |
| B18 | g-9c41→g-5b07 | is the first clip the milestone that opens the Steam-page slice; does ~2026-07-10 leave runway for page-by-08-31 / Oct-5 demo? | open→G7 |
| B19 | g-9c41→g-5b07 | does min-spec playability (crit 1) back the demo quality gate ("a janky demo skips the fest")? | split: arch + open→G7 |
| B20 | g-9c41→g-e6f2 | does the harness produce a STEADY supply of real captured footage as a dev byproduct at the cadence's rate without heroics? | split: arch + open→G7 |
| B21 | g-9c41→g-e6f2 | agent-drivable programmatic capture from harness scenes, within the real-footage-only lane (AI imagery FORBIDDEN) | split: arch + open→G7 |
| B22 | g-9c41→g-e6f2 | monthly FFF-style tech-post material (telemetry, debug surfaces, measured numbers) as a dev byproduct | answered (byproduct of crit 3/5) |
| B23 | g-9c41→root | is the riskiest-assumption proof (networked chunked-delta multi-gas consistency under breach) the evidence the moat is real? | open→G7 |
| B24 | g-9c41→root | core-fantasy demonstration split: which of {co-op, gas+grid, destruction, distinct gases, expedition pressure} are proven HERE vs re-homed to g-d3a8? | split: arch + open→G7 |
| B25 | g-9c41→root | reusable-tech-asset property (R4: engine-free, Unity-package-portable, Burst/Jobs behind a seam) — what makes "reusable" checkable? | split: arch + open→G7 |
| B26 | g-9c41→root | owner pride bar — is owner acceptance of the core's technical strength a recorded verdict on playable evidence? | open→G7 |
| B27 | g-9c41←DA | ingestion contract (TopologyDocument: volumes/portals/surfaces/anchors with sillZ; vertical from authoring-convention since DA Cell.Bounds is 2D X-Z): mandatory day-one (naive ~100–300) vs bet-2 (occupancy + 1000-gate) | split: arch + open→PLAN |
| B28 | g-9c41←PGG | does PGG fill the SAME TopologyDocument through the replaceable adapter; replaceability proven on DA alone, PGG parked behind the seam | open→arch (parked) |
| B29 | g-9c41←vendor | transport-adapter swap contract (default FishNet, fallback NGO/NfE no tree change; gas decoupled from vendor input plane) | open→arch |
| B30 | g-9c41→destruction-consumer | breach→topology-change consumer contract (scripted breach only day-one, no destruction SYSTEM; breach adds vertical portals at tick N+1); full destructibility = a separate large unresolved edge parked to a later node | split: arch + open→G7(scope) |
| B31 | g-9c41→{g-7e15,g-d3a8} **shared** | **one NORMATIVE field-sampling / ExposureQuery formula** (brief contract #4): the single sub-band interpolation (band masses + interface → concentration at height z) read by THREE consumers — the visual read model (B11), far-AI "is-it-lethal-here" ExposureQuery, and player-near seeding — so g-7e15 crit-2 (vision-agent vs sim state) and g-d3a8 crit-5 (self-play over configs) sample the SAME oracle and agree (same point→same concentration regardless of consumer/tier). A single contract living in two siblings' done_when, named by neither node alone | open→arch (cross-cutting invariant) |

---

## §COVERAGE MAP — three-source closure (every criterion + edge + mechanism parameter → a row)

**(a) done_when criteria → rows** (no white spots):

| criterion | covered by |
|---|---|
| 1 — min-spec performance | A1.1–A1.6 |
| 2 — replication model locked + chunked-delta | I1, I2, I3, I11, **I23** (model + rollback/lockstep spike bound) + **§WHAT-C C1–C22** (the parameters the locked model forces) |
| 3 — 2+ clients consistent across topology change + debug surfaces | I6–I11 (consistency oracle) + C3, C8, C9, C13, **C19, C20, C22** (settle/divergence/keyframe/fault + client-recon determinism + apply-order + lossy mass-bound) + A2.1–A2.4 (debug surfaces, mass invariant, video, evidence split) + G:topology-change, G:settle |
| 4 — declarative two-level gas types | I12, I13 (R5/R15) + A3.1–A3.5 + B1, B2 |
| 5 — reusable agent-drivable harness | I4, I5 + A4.1–A4.3 + C15, C18, **C21** (scene profile, telemetry schema, layer registry) |
| 6 — render proof slice locks stylization + seam | I19 + A5.1–A5.6 + B9 |
| 7 — clean 1-player, count = config, no bots | I5, I14 + A6.1–A6.2 |
| 8 — first spectacular clip milestone | A7.1–A7.3 + B15, B18 *(B20 is e6f2 steady-cadence, NOT the milestone — dropped)* |
| 9 — scale architecture (R1) arithmetic-validated | I15, I16, I17 (always-on / latency / stratification) + A8.1–A8.8 (incl. energy/temperature state dim) + A1.7 (whole-frame budget closure) + B30 (topology) + C18 (measured chunk size feeds bandwidth arithmetic) |

**(b) cross-node edges → rows:** B1–B31 (g-d3a8: B1–B8; g-7e15: B9–B14; g-5b07: B15–B19; g-e6f2:
B20–B22; root: B23–B26; DA/PGG/vendor: B27–B29; destruction-consumer: B30; **shared field-sampling
oracle: B31**). No sibling edge unmapped.

**(c) mechanism parameters → rows:** chunked-delta stream fully decomposed in §WHAT-C C1–C22
(I9/I1/I20 cross-referenced for hash-domain / reconstruct / late-join). Recursive sub-mechanisms split:
deadband+quantization (C2,C3,C4), flow-control clamps (C5,C6), the channel (C7), keyframe/resend
recovery (C8,C9,C13), the chunk wire format (C10), write discipline (C11), the fabric contracts =
**layer registry (C21) + revision barrier/change-feed (C12)** (two contracts, per NOW p1 — not one),
**client-side reconstruction determinism (C19) + apply-order canonicalization (C20)** (the second,
client code path I1/I4 left implicit), and **lossy mass-conservation (C22)**. No parameter folded
silently into a closed mechanism (design-doc fix b honored).

### WITNESS CHECK — the success test (does the set name as QUESTIONS exactly the ADR-0003 ad-hoc values?)

Each value PLAN would freeze ad hoc in ADR-0003 (extracted independently from NOW.md
`next.leg_opens_with`, s-work-004, converge-design.md) → the row that now NAMES it as a question:

| ADR-0003 ad-hoc value | named here as | kind |
|---|---|---|
| integer/fixed-point field representation | **C1** | magnitude→PLAN |
| quantization step Q | **C2** | magnitude→PLAN |
| divergence threshold (property "bounded by quant step") | I8 / **C3** property | property→G7 (answered) |
| divergence threshold value = Q | **C3** magnitude | magnitude→PLAN |
| deadband magnitude | **C4** | magnitude→PLAN |
| per-client clamp (~150 KB/s) | **C5** | magnitude→PLAN |
| aggregate host clamp (~250–300 KB/s) | **C6** | magnitude→PLAN |
| gas-plane channel reliability (unreliable-seq vs reliable) | **C7** | own-decision→PLAN/G7 |
| settle predicate N | **C8** | magnitude→PLAN |
| keyframe cadence K (or quiescence-only) | **C9** | magnitude→PLAN / scope |
| wire byte-format + resolution key | **C10** | magnitude→PLAN |
| single-writer-per-(layer×phase) + phase ordering | **C11** | property→G7 / form→PLAN |
| revision barrier / change-feed form | **C12** | property→G7 / form→PLAN |
| fault-injection scope (inject t-2 vs defer t-3) | **C13** | scope→G7 |
| frozen scene profile (rooms, chunk grid, total) | **C15** | magnitude→PLAN |
| reproducibility constants (seed, run, breach, target-tick) | **C16** | magnitude→PLAN |
| peer count = 1 host + 2 clients | **C17** | answered |
| measurement schema + path (bytes + dirty-rate) | **C18** | magnitude→PLAN |
| late-join out of scope | I20 | answered (scope) |
| dual-guarantee kill-gate "A" | I6 | property (answered) |
| lossless (i) bit-exact incl. breach | I7 | property (answered) |
| lossy (ii) bounded-divergence + settle-converge | I8 | property (answered) |
| hash domain = reconstructed field cells only | I9 | property (answered) |
| same reconstruction code path (anti-gaming) | I10 | property (answered) |
| client reconstructs without running the sim | I1 | property (answered) |
| tick rate pinned 10 Hz day-one | I21 / C16 | answered |
| 0.6–6 KB sanity-only, no clamp verdict in t-2 | C18 property | answered (scope) |
| G0 ledger frozen / default-FAIL / builder-can't-edit | I22 | process (answered) |
| rollback/lockstep ≤ one 1–2-wk spike (crit-2 sub-clause) | I23 | property (answered) |
| layer registry (a contract distinct from the revision feed) | C21 | property→G7 / form→PLAN |
| revision barrier / change-feed = REAL exercised contracts | C12 (p1-gated) | property→G7 |

**Verdict: PASS (mechanical), independently confirmed.** A separate adversarial verify pass
(wf_f79c2059-b21: coverage / witness / firewall / completeness, attacking the set) found `missing_values:
[]` against an independently-rebuilt gold list — every value ADR-0003 would invent ad hoc IS present as
a named row: the previously-decided properties as `answered` imports (I1–I23), every open MAGNITUDE
(Q, deadband, both clamps, N, K, channel reliability, wire format, scene profile, repro constants,
fault-injection) as an `open→PLAN`/scope row in §WHAT-C. The values are no longer invented at task time;
they are the converge set's open agenda for PLAN.

**Beyond the gold list (the layer earning its keep):** the verify pass surfaced FOUR forced parameters
that even the hardened c-exec-003 CALL left implicit inside `answered` rows — C19 (client-side recon
arithmetic determinism), C20 (client apply-order canonicalization), C22 (lossy mass-conservation bound),
C21 (the layer registry as a contract distinct from the revision feed) — plus C14 (min-resend, converge-
derived). These are NOT in NOW's enumerated ADR-0003 list; the decomposition (not the success bar) caught
them. A real ADR-0003 hits C19/C20/C22 immediately. This is the layer doing exactly its job: catching
what a same-session self-check would have smuggled. *(Honest scope of "PASS": this is the FORM-pass
mechanical coverage claim, hardened by one adversarial pass. The FULL independent-oracle completeness
sweep + "no answer leans on an uncovered question" trace is the separate converge-verify session — NOT
run here, per boundary.)*

---

## §ROUTE — next + the live-build sequencing risk (⚠ surfaced to owner)

The next movement is **converge-arch** (heavy + sibling-bearing: the B-rows are consumer-driven cross-node
contracts) and **resolve-one-question-at-a-time** for the open→G7 rows; converge-verify gates shape later.

**⚠ Sequencing risk (verify pass, → owner decision d-converge-001).** The bulk of the OPEN rows are
`open→PLAN` magnitudes (C1–C22) — and those are **exactly** the values the ALREADY-DISPATCHED `c-exec-003`
leg will freeze in ADR-0003 (`NOW.next.leg_opens_with` enumerates Q/N/K/clamps/scene-profile/repro). This
retrofit set was authored in PARALLEL to that in-flight build (CALL boundary: don't touch the bet). So
ADR-0003 could freeze C1–C22 **before** this converge set (and the converge-arch B-row properties they must
satisfy — the shared field-sampling oracle B31, the lossy mass bound C22, client-recon determinism C19/C20)
is consumed — letting PLAN re-invent precisely what this pass exists to pre-empt. This is the FIRST-RUN
demonstration question the design doc names (slice #2): does converge merely *reproduce* the ad-hoc list as
a proof, or does it *feed* the live ADR-0003? Touching the bet is an owner call → `decisions_needed`.

## §RESOLVED — owner sign-off (2026-06-14, session s-converge-002)

`§SIGNOFF: owner approved RESOLVE (temperature + destruction + extensibility) @ 2026-06-14 — "да, A" +
R1–R13 confirmed (voice, this session).` Three design questions closed below. They re-shape the bet →
shape card c-shape-004 (owner approved the DIRECTION "A"; the specific re-shaped done_when needs G9
in-session approval). HOW magnitudes still → PLAN; reaction CONTENT stays g-d3a8.

**RESOLVED-1 — TEMPERATURE** (supersedes I21 "static field day-one"; closes A8.8; new term G:temperature):
Temperature is a **thin DYNAMIC LAYER** in the core — its own data structure + its own minimal optimized
sim, a sibling of gas (R2/R3), **not static**. It talks only through the grid event/revision bus: events
(reaction / gas-spread / breach, by coordinates) flow through the grid; temperature **subscribes** and
responds — rises then decays (R4). Its job in the core is to **prove the layered architecture supports
adding layers + cross-system interaction** (R5), **not** gameplay/aesthetics — temperature gameplay design
→ g-d3a8 (R1). Only in this form (R6). *Grounding:* the seam already anticipates it — reaction batches
carry enthalpy and reactions read a temperature window (brief §3.2), so temperature↔reactions is a natural
loop; keep the sim TRIVIAL (scalar rise/decay). Sim structure/magnitude → PLAN.

**RESOLVED-2 — DESTRUCTION** (supersedes I21 "scripted-breach only"; B30; G:destruction/G:topology-change
"scripted" reading): **No scripted breach.** Real but **CONTROLLED, LOCAL** destructibility in the core: a
destructible wall is breached (explosion / player) → a hole opens → topology changes → gas flows out
(R7/R8). Few walls, count TBD. **No collapse / structural physics / level-wide change** (R9). Shards/
fragments (tied to loot-with-gas carry, trip-over) = deferred super-extra (R10). *Grounding:* maps exactly
onto the designed topology-change = "add a breach portal between immutable volumes" (brief §3.7) — only the
TRIGGER changes from scripted to real-controlled; no architecture change needed.

**RESOLVED-3 — EXTENSIBILITY** (R11/R12/R13, governing principle): everything in the core is built so ALL
of it can be extended later (each system, esp. temperature, gains functionality). **Healthy form
(owner-confirmed):** make the **SEAMS/abstractions extensible** (cheap to extend later); keep
**IMPLEMENTATIONS minimal now** (do NOT build future functionality early — that breaks G3 / the 24.07
wall). No scripted finals; simplest impls only for tests. *Grounding:* already the spine — engine-free
core, layer registry + named extension points (a new layer/driver plugs in without core edits), R4
"asset survives the concept".

## §RESOLVED-4 — INTER-LAYER READ MODEL (2026-06-16, s-decide-003 / folded at c-converge-003)

`§SIGNOFF: owner confirmed the inter-layer read architecture + the temperature→gas feedback deferral @
2026-06-16 (s-decide-003, voice/text — «все понятно со всем полностью согласен»).` Recorded here because it is
the SEAM that holds the deferred feedback open (it resolves the verify watch-item "don't foreclose feedback")
and the model XL1's read-ready seam references instead of restating inline.

**The architecture (owner-confirmed).** The GRID is the shared coordinate/address space + the cell→room/sector
OWNERSHIP map + the event BUS + the revision/commit CLOCK — it is NOT a data router / god-object (the one
correction to the owner's first "grid routes the data" model is "grid carries ADDRESSES + ownership, not the
data values"). Each layer publishes, on a COMMITTED revision: (notification-shaped) typed EVENTS — discrete
"something happened at grid-cell/sector c" — and a (queryable) READ-MODEL — "value at grid-cell c as of revision
r" — that translates grid-coords into the layer's OWN internal representation. (Delivery — synchronous pull vs
subscription — is → PLAN, per XL1.) Consumers subscribe/query in GRID coordinates against a COMMITTED revision;
they NEVER touch another layer's internals or its live mid-tick state (this is what keeps
cross-layer reads deterministic + network-consistent). This collapses N×N pairwise adapters → N (one
grid-addressed read-model per source layer, shared by all consumers) and handles HETEROGENEOUS resolution
(temperature answers a per-cell query from per-room storage; the coarse gas tier answers from band storage).
**It MATCHES the already-authored OR1/OR2 (the single field-sampling oracle) + GG2 (geometry/band sovereignty)**
— the same shape, generalized from "the gas read oracle" to "every layer publishes a read oracle." **Forward
constraint (cheap, not code — carry into Wave-2 design):** the read seam must let a layer read another layer's
field at ANY resolution on a committed revision; do NOT optimize the band solver into a corner that forecloses
later temperature→gas feedback. Magnitudes (read-model encoding, phase ordering, cross-tier mapping) → PLAN.

## §SIGNOFF — partial (resolve in progress)

G7 owner gates batched into AT MOST THREE points (one per gated movement):

- `§SIGNOFF: Define (glossary readings) — PENDING` (a resolve pass signs the remaining disputed-term readings).
- `§SIGNOFF: Resolve (WHAT acceptance) — PARTIAL` — temperature / destruction / extensibility SIGNED 2026-06-14 (s-converge-002, see §RESOLVED); remaining open→G7 rows still pending.
- `§SIGNOFF: converge-arch (cross-node contracts) — PENDING` (the B-rows ride converge-arch).

Remaining open rows are still the deliverable for later resolve/arch/verify; converge-verify NOT run.

## play_check (FORM pass)

- `triage: HEAVY — converge ON — model? YES · contract? YES · decomposes? YES` (done; verify-confirmed SOUND)
- `mode: RETROFIT — imports born-closed before framing the gap; Resolve-3c kept Q/N/K open under the imported kill-gate` (done)
- `imported: [s-shape-003 (d-arch-001 a–e, R5/R12/R13/R14/R15, vendor, cut_list, node #2 rollback-spike, ADR-0002 via NOW), s-work-004 (kill-gate A + reconstruction facts), s-work-003 via NOW]` → I1–I23 (done)
- `define: §GLOSSARY 14 disputed terms, mechanically seeded, on-disk second readings cited (G:settle added in hardening)` (done)
- `resolve: §WHAT formed — imports I1–I23, mechanism C1–C22, criteria A1–A8 (incl. A1.7 budget-closure, A8.8 energy/temp), edges B1–B31; one question/line, tagged, cited; NONE signed (boundary)` (done)
- `converge_coverage: every done_when criterion 1–9 + every cross-node edge (B1–B31) + every chunked-delta parameter (C1–C22) → a §WHAT row or covered_by (see §COVERAGE MAP)` (done)
- `witness_check: PASS (mechanical), adversarially confirmed (missing_values: []) — the set names as QUESTIONS exactly the ADR-0003 ad-hoc values; +4 forced params beyond the gold list (C19/C20/C21/C22)` (done)
- `canon_proposed: [G:chunk, G:consistency, G:replication, G:coarse-tier, G:topology-change, G:settle]` (proposed; review/pulse promote)
- `hardening: internal adversarial pass (wf_f79c2059-b21, 4 verifiers) folded — 2 blockers (C19,C20), 3 majors (I23,C21,A8.8 / B31 / C22), minors (A8.6 split, B20 phantom, C14 reclass, G:settle) + the live-build sequencing risk (→ d-converge-001)` (done)
- `close & route: NOT a full close — FORM-pass checkpoint; next = converge-arch (grid↔gas / gas-type seam / render seam / ingestion / B31 oracle) AND/OR resolve-one-at-a-time; ⚠ §ROUTE sequencing decision d-converge-001 surfaced (feed live c-exec-003 PLAN before ADR-0003 freezes C1–C22?). converge-verify gates shape later.` (checkpoint)
- `verify (the converge-verify PLAY): DEFERRED to a separate session (boundary — not run here); the internal hardening pass above is a self-check, NOT the independent-oracle converge-verify`
- `forward_clean: NO — open rows are the intended FORM-pass output, not a defect`

---

## §CONTRACTS (converge-arch pass — c-converge-002, 2026-06-16)

> **What this is.** The DECLARE/DECOMPOSE/ARCHITECT output of converge-arch (heavy + sibling-bearing). It
> turns the §WHAT-B edges (and the internal grid↔gas + cross-layer seams) into CONSUMER-DRIVEN OBSERVABLE
> contracts: the consumer states what flows, which way, on what trigger, in behavioral terms; every HOW
> (push/poll, wire/byte format, cadence, layout, magnitude) is routed `→PLAN`. All contracts sit ABOVE the
> locked Wave-1 foundation (GasCoopGame ADR-0004 §LOCK + ADR-0003 v2 C1–C22) and NONE re-opens it. The heavy
> architecture-on-paper (ARCH-1v2, brief v2) rides PLAN as INPUT EVIDENCE — recorded in
> `work/converge-g-9c41-arch.md`, never copied into done_when. Built + hardened by a 15-agent in-session
> pre-pass (wf_c4e09962-08f: 6 drafters → 6 adversarial firewalls → 3 cross-cutting critics); fixes folded.
> The BINDING independent refutation is the separate `converge-verify` session (NOT run here — boundary).
>
> Per-contract legend: **ID — title** · B-rows · *consumer ← producer* · trigger · OBSERVABLE (no HOW) ·
> acceptance · `→PLAN` (the HOW) · bounds (open→PLAN C/A rows it constrains) · build-order · fork/canon.

### A. Ingestion adapter / TopologyDocument (B27–B29) — PRIMARY

- **IN1 — Structure-ingestion (TopologyDocument).** B27. *TopologyCore (#1) ← structure generator behind the
  replaceable adapter (DA day-one).* trigger: level (re)generation / scene load (not per-tick). **OBSERVABLE:**
  TopologyCore requires a complete static structure description sufficient to sectorize geometrically AND to
  support exact-source-tracking + on-entry reconstruction — volumes {stable id, archetype incl. hangar/
  openSpace, bounds extent, free volume, floor/ceiling extent}, portals {position, facing, opening size,
  **lower-edge height above floor** = the fact that lets a low opening vent heavy gas first}, surfaces
  {vertical span, **breachable** flag}, anchors, subdivision intent; ids **logically identical + deterministic
  across peers** from the same generation; vertical carried explicitly even where the generator API is 2D.
  Self-contained: TopologyCore sectorizes + runs seal/closure with ZERO gas-domain inputs. acceptance:
  re-ingest same level → logically-identical ids + identical vertical extents on every peer; sectorization-
  complete with zero gas inputs. `→PLAN`: occupancy present/absent day-one (optional naive ~100–300 vs bet-2
  occupancy+1000-gate); occupancy encoding/basisCellSize; AABB struct layout; doc serialization; subdivision
  threshold magnitudes. bounds: B27, A8.1, A8.7. build: produced-now-consumed-later (DA behind seam day-one —
  not dangling). canon: TopologyDocument-ingestion (read_by TopologyCore + DA/PGG adapters). *[fix: "byte-
  identical ids" → "logically identical" — byte layout belongs to the LOCKED wire, not this contract.]*
- **IN2 — Adapter-replaceability invariant.** B27/B28. *TopologyCore ← the replaceable adapter seam.* trigger:
  a generator swap. **OBSERVABLE:** the structure is defined ENTIRELY by the TopologyDocument contract (IN1),
  never by the generator's identity/internals; swapping the generator (DA→PGG→any) changes only WHICH document
  is produced, never its shape; replaceability demonstrated on the DAY-ONE generator alone (PGG parked behind
  the SAME seam; population OUT of scope now per d-generator-001). acceptance (black-box): any two conforming
  producers of the same logical level → identical sectorization + seal verdicts; the SOLE admission gate is a
  conformance check (sectorization-complete + deterministic), the day-one generator passing it is sufficient.
  `→PLAN`: adapter interface signature; conformance check site/test-vectors; whether PGG population maps to
  occupancy vs a later doc extension. bounds: B28, A8.7. build: internal. canon: ingestion-adapter-
  replaceability. *[fix: black-box acceptance — dropped the white-box "no generator-specific branch".]*
- **IN3 — Transport-vendor swap.** B29. *g-9c41 networked core ← transport vendor (FishNet default / NGO|NfE
  fallback) behind a transport-adapter.* trigger: a vendor swap. **OBSERVABLE:** swapping the vendor causes NO
  change to the component tree, the gas-field stream plane, or any gas/domain contract; the gas field rides a
  SECOND own plane never retrofitted onto the vendor's input/entity transport; no vendor type named outside the
  adapter. acceptance: a vendor swap leaves the tree + gas/domain contracts unchanged AND the gas-consistency
  oracle (lossless+lossy under drop/delay/reorder) passes identically. `→PLAN`: adapter signature; default/
  fallback config; channel-reliability config knobs around the LOCKED unreliable-sequenced mode; per-vendor
  binding. bounds: B29, I3, C7. build: internal. canon: transport-vendor-decoupling.

### B. grid↔gas internal seam (PRIMARY)

- **GG1 — Topology-change feed.** internal #1→#3. *GasDomain ← TopologyAuthority.* trigger: a committed
  topology change (revision advances). **OBSERVABLE:** on every topology change GasDomain receives the changed
  sectors + new adjacency (added/removed portals), each labelled with the topology-revision, on a SINGLE agreed
  tick every peer observes identically; between changes geometry/adjacency are immutable; change-sets are
  self-describing (a consumer at revision r given the change-set to r+1 reaches r+1 with no host-private state)
  + replayable. acceptance: determinism-of-tick (every peer reports the same tick a revision takes effect);
  revision-monotonic (strictly increasing, no unreconstructable gap); replay-identity. `→PLAN`: push-vs-poll;
  deferred-commit P1→P2 (the agreed-tick mechanism); change-set encoding + revision-counter width; feed
  reliability; cadence; replay history depth. bounds: C12, C16, A2.1. build: internal. canon: G:topology-change
  (read_by TopologyCore + GasDomain). **NOTE:** this topology-revision is the SECTOR/adjacency sibling counter
  (brief §3.4 "external revision = published tick"), DISTINCT from the LOCKED per-(layerKey,chunkIndex) field
  barrier — not in conflict.
- **GG2 — Geometry/band sovereignty split.** internal #1→#3. **OBSERVABLE:** every change-set is purely
  geometric, keyed by sector id — never names a band/species/mass/concentration; GasDomain attaches its own
  per-sector band state to a sector id and the attachment survives non-destructive topology changes; conversely
  NO GasDomain field is an input to producing a change-set (TopologyCore computes the next change-set with zero
  gas knowledge). acceptance: independence-of-domains (perturb gas → identical change-set stream); vocabulary-
  closure (no gas field in the change-set schema); key-stability (a sector id survives a non-destructive change
  so band state isn't orphaned). `→PLAN`: geometric field list; sector-id encoding; band-state indexing. bounds:
  A3.4, C21. build: internal. canon: Sovereignty (geometry-only, keyed by sector id).
- **GG3 — Real controlled breach → vertical portals.** B30/RESOLVED-2. internal #1→#3 (GasDomain consumer).
  trigger: a real controlled LOCAL breach (explosion/player) on a breachable surface; no scripted, no collapse.
  **OBSERVABLE:** on the agreed topology-change tick, one+ NEW portals appear in the affected sectors' adjacency,
  each with a breach-portal identity that is deterministic + stable (same breach/inputs → same identity on every
  peer + across replay; present in snapshot + change-set); after applied, gas transport across the new portal is
  enabled; the breach changes geometry only. acceptance: breach-causes-flow (no outflow before, an outflow path
  on the first tick after applied); identity-determinism; same-tick agreement (inherits GG1). `→PLAN`: breach-
  portal id encoding (surfaceId,ordinal); deferred-commit timing; portal geometric byte layout; #breachable
  walls day-one (count TBD per RESOLVED-2); the orifice/sill flow MECHANISM. bounds: C16, B30, A8.x sillZ flow.
  build: internal. canon: **G:topology-change[breach] — ONE shared line with CS1** (read_by g-9c41 +
  destruction-consumer).
- **GG4 — Band-handoff support (OWNER-SIGNED, see §SIGNOFF-BH).** band-handoff steer + R10. internal #1→#3.
  trigger: (a) a source/emitter exists in a coarse-simulated sector; (b) a player enters → fine detail demanded.
  **OBSERVABLE (resolved per owner):** GasDomain can pin an emitter/source to an EXACT intra-sector location +
  identity, preserved across non-destructive topology changes, AND on player-entry reconstruct a local field
  that is roughly right in amount + accumulation RATE + direction + which corner — to a **LOOSE gameplay
  tolerance** (a few cells; metric exactness is NOT measured), with the **coarse tier as the source of truth
  for amount AND rate**. acceptance (firm — GAMEPLAY-BINDING, owner 2026-06-16): (1) **NO visible jerk/twitch in
  the gas at ANY time** — not on the coarse↔fine handoff, not on the first frame on entry, and not from anything
  computed OFF-SCREEN that surfaces on entry (reading gas is the CORE mechanic → any visible jerk = broken); (2)
  **believable amount + rate**: on return after being away, the gas QUANTITY matches what the player would expect
  from the source strength he observed + elapsed time (no jump to half-full when ~quarter is expected) — the
  coarse tier evolves the gas at a believable, GRADUAL rate while unobserved (gradual top-up per the owner's
  «чуть-чуть дозаполнится» signoff; any non-decreasing / curve-shape constraint is NOT baked here → PLAN/g-d3a8),
  and entering/leaving changes only the spatial DETAIL, never the amount or its rate; (3) a weak corner source
  reads in the right corner; (4)
  source-survival across non-destructive topology change. The geometry the seam
  exposes must SUFFICE for this; the reconstruction mechanism is not prescribed. `→PLAN`: the 3-tier prep-window
  mechanism (owner HINT: coarse=truth / intermediate prep-window within a radius / fine close-up — a hunch, not
  a lock); hints-vs-replay; the few-cells tolerance magnitude; how source-accumulation is hinted while coarse;
  burn-in/seeding to achieve no-pop; seam smoothing. bounds: A8.1/A8.2, C15, C22, CR1/CR2, B27 occupancy. build:
  internal. canon: band-handoff continuity. *(twin of OR4 — same owner decision, one §SIGNOFF.)* *(C22 + CR1/CR2
  added c-converge-003: "amount never changes crossing tiers" depends on the lossy mass bound AND on coarse↔fine
  agreement, which needs the coarse tier replicated + consistent — F1.)*

### C. B31 — the ONE normative field-sampling / ExposureQuery oracle (the cross-cutting invariant; PRIMARY)

- **OR1 — Single-oracle field sampling.** B31/B11. *g-7e15 visual read model + g-d3a8 far-AI ExposureQuery ←
  g-9c41 GasDomain (IGasReadModel).* trigger: any consumer samples concentration at a point for a published
  revision. **OBSERVABLE:** ONE published read view; any two consumers querying the SAME point at the SAME
  published revision get the SAME concentration for the SAME species — regardless of consumer AND regardless of
  which tier (fine/intermediate/coarse) is the thinnest open level there; the answer is a pure function of
  (point, species, revision). acceptance: cross-consumer agreement (visual read view == ExposureQuery at the
  same point); a NAMED cross-tier agreement test at points where the thinnest-open-level differs; determinism.
  `→PLAN`: the sub-band interpolation math; whether/how it composes across a resolution boundary; agreement
  tolerance (bit-exact vs ε); resolution-key encoding; push-vs-pull; memory layout. bounds: C1, C10, A1.7/B12,
  A8.8. build: produced-now-consumed-later. canon: IGasReadModel single-oracle invariant (read_by g-7e15 crit-2
  + g-d3a8 crit-5). **HIGH-RISK property authored observable-first: if PLAN cannot satisfy it at a seam → a
  BLOCKED contract, not a silent green.**
- **OR2 — Point-resolution rule (thinnest open level).** B31/B11. *all three consumers ← GasDomain.*
  **OBSERVABLE:** a point covered by several levels answers from the THINNEST open level (fine > intermediate >
  coarse band); the selection is part of the contract (a consumer never chooses a tier, never sees a different
  tier than another consumer for the same point); exactly one concentration per (point,species,revision); which
  level supplied it is observable. acceptance: single-valued; precedence-honored (fine inside an open window,
  coarse outside); consumer-independence; no gaps (coarse = floor). `→PLAN`: precedence structure; window-
  boundary/seam assignment; resolution-key scheme. bounds: C10, A8.2, T3>T2>T1s budgets. build: internal. canon:
  point-resolution (thinnest-open-level).
- **OR3 — ExposureQuery = volume integral of the one oracle.** B31. *g-d3a8 far-AI lethality + self-play
  (crit-5) ← GasDomain.* **OBSERVABLE:** exposure for an actor occupying a VOLUME = aggregating the same
  per-point concentration (OR1) over the actor's volume via the same resolution rule (OR2); the far-AI verdict
  and a self-play run on the same actor/revision/config get the SAME exposure; never reads a private/differently-
  resolved state. acceptance: ExposureQuery over a degenerate (point) volume == OR1 point answer; self-
  consistency across runs + across the two g-d3a8 lanes; tier-independence for a straddling actor; a named
  volume-sum cross-check. `→PLAN`: integration/quadrature; actor-volume representation; exposure units/dose; the
  **lethality threshold = g-d3a8 design content + a PLAN number, NOT this contract**; pull vs subscription.
  bounds: C22, A8.6, C1. build: produced-now-consumed-later. canon: ExposureQuery = volume integral.
- **OR4 — Player-near seeding agrees on entry (band-handoff, OWNER-SIGNED).** B31. *g-9c41 band-handoff seeding
  ← GasDomain.* The B31-side twin of GG4 — resolved together (§SIGNOFF-BH): opening a fine window changes
  RESOLUTION not the ANSWER to a LOOSE gameplay tolerance, with NO visible shimmer; a weak corner source is
  roughly right on arrival; the coarse oracle is the source of truth the fine tier derives from. acceptance
  (firm — GAMEPLAY-BINDING, owner 2026-06-16, same as GG4): NO visible jerk/twitch EVER (handoff, first frame,
  or off-screen-computed state surfacing on entry) since gas-reading is the core mechanic; **believable amount +
  rate** on return (the gas quantity matches the observed source strength + elapsed time — no jump; crossing
  tiers changes only spatial detail, never amount/rate); source fidelity (right corner); conservation consistent
  with the read view's mass accounting. `→PLAN`: seeding
  mechanism (reconstruct-from-source / replay / spatial-hints — brief §3.5); burn-in; coarse-source accumulation
  hint; tolerance magnitude. bounds: C22, §3.5 window-drag/burn-in, A8.8. build: produced-now-consumed-later.
  canon: band-handoff continuity.

### D. Cross-layer interaction + extensibility seam (done_when #10 — the WHITE SPOT the miner gap-hunt caught; NEW)

- **XL1 — Cross-layer interaction seam (multi-layer SINK consistency at coarse scale + read-ready seam).**
  *(re-scoped c-converge-003 per d-tempfeedback-001 — feedback DEFERRED.)* done_when #10 + RESOLVED-1 +
  §RESOLVED-4 (inter-layer read model) + the LOCKED cross-layer contract. INTERNAL: GasDomain/ReactionLayer
  (LayerKey 0) PUBLISHES reaction/breach/gas-changed GridEvents (the LOCKED gas/breach-sourced enum); the
  temperature layer (LayerKey 1) SUBSCRIBES + responds as a SINK. trigger: a layer publishes a GridEvent another
  layer consumes within a tick. **OBSERVABLE:** ≥2 independent layers ride ONE seam and are networked-consistent
  TOGETHER at Wave-2 COARSE scale — the non-simulating client reconstructs a consistent MULTI-LAYER field (both
  gas and temperature held to the lossless bit-exact + lossy bounded-divergence oracle at settle, per the LOCK's
  CellHash.FoldLayer-per-layer, now exercised at COARSE scale not only the Wave-1 toy scene); the gas→temperature
  SINK interaction is OBSERVABLE (a reaction/heat event drives the temperature layer's response, measurable at
  the firing tick). PLUS the grid-addressed READ-READY seam (§RESOLVED-4): a layer's field can be READ on a
  COMMITTED revision via a grid-addressed read-model — a consumer queries "value at grid-cell c as of revision r"
  in GRID coordinates, the layer translates to its own representation internally (temperature answers a per-cell
  query from per-room storage), and NO consumer touches another layer's internals or live mid-tick state.
  acceptance: under the load oracle, BOTH layers' reconstructed cells stay host==clients at every settle AT
  COARSE SCALE — this coarse-scale per-layer consistency is DISCHARGED by CR1/CR2/CR3 read PER LAYER (incl. the
  coarse temperature layer, §H PER-LAYER note), NOT by §T12 (fine Wave-1 toy scene only); a suppressed-event
  negative oracle shows the sink interaction is real; the read seam answers a cross-layer grid-coord query on a
  committed revision deterministically (a live-state / wrong-revision read is rejected). `→PLAN`: the cross-layer
  phase ordering + commit rule; per-layer Q/N magnitudes; the read-model
  encoding + the **cross-TIER coordinate mapping** (how a grid query resolves at coarse-sector vs fine-cell
  representations at the tier resolving there); pull-vs-subscription. bounds: C11, C12, C19/C20, A8.8,
  §RESOLVED-4, CR1/CR2. build: internal.
  **MECHANISM → §RESOLVED-4 + PLAN.** *(trimmed c-converge-003 — the pub/sub + read-model communication model is
  recorded ONCE in §RESOLVED-4 and its magnitudes route to PLAN, not restated as contract prose here; this closes
  the verify firewall-borderline note on the old MECHANISM paragraph.)*
  **NOTE — consistency obligation DECIDED (not an open fork):** the binding obligation = BOTH layers consistent
  together (done_when #10 "networked-consistent together" + RESOLVED-1). §T12 HOLDS for the FINE Wave-1 layer
  only; the coarse-scale temperature-sink consistency is DERIVED from CR1/CR2/CR3 generalized PER LAYER (§H), NOT
  directly from §T12. The cheaper "gas-only + host-derived temperature" reading weakens crit-10 + contradicts the
  LOCK → rejected.
  **NOTE — FEEDBACK DEFERRED (d-tempfeedback-001, owner-confirmed 2026-06-16, s-decide-003):** temperature→gas
  FEEDBACK is DEFERRED to a later wave (post-g-d3a8 — the per-gas-type heat rule is game design worked in
  parallel; building it now = guaranteed rework; nothing in the Wave-2 spine depends on it). This wave's
  cross-layer interaction is the gas→temperature SINK ONLY, so the locked GridEventKind enum (gas/breach-sourced)
  is UNTOUCHED, no temperature-sourced event exists, and the verify F2 collision DISSOLVES: temperature stays a
  pure sink → ADR-0004 §T12 + C21 byte-identical HOLD. FORWARD PATH (named, not built): when feedback is later
  introduced it is EITHER read-based-in-phase-order (the gas reaction phase READS temperature via §RESOLVED-4's
  read seam; enum untouched) OR event-based (which SHALL SURFACE the locked-GridEventKind extension, exactly like
  the barrier-table re-size, never silent in PLAN). FORWARD CONSTRAINT (cheap, carry into Wave-2 design): the
  read seam must let a layer read another layer's field at ANY resolution on a committed revision — do NOT
  optimize the band solver into a corner that forecloses later feedback. The crit-10 "feedback interaction"
  tightening shape folded in is RE-SCOPED to this deferral; the TREE crit-10 rewording (NAME the deferral, don't
  silently drop it) is the SHAPE's G9 job (c-shape-wave2), NOT edited here. canon: G:cross-layer-consistency
  (read_by FieldFabric + GasDomain + the temperature layer).
- **XL2 — Layer-registry extensibility ("a new layer plugs in without core edits").** done_when #10 +
  RESOLVED-3 + C21. INTERNAL: a new independent layer registers on FieldFabric (#2) and rides the shared
  transactional multi-layer commit + revision feed. trigger: a new layer/driver registered at composition/load.
  **OBSERVABLE:** a temperature-CLASS WHOLE layer (distinct from a within-gas species handler — GT1) registers
  via the layer registry (one layer per registration, keyed by LayerKey asc) and participates in the shared
  store + revision feed WITHOUT editing FieldFabric or any other layer's files (file-level isolation = the
  extensibility proof). acceptance: a gas-only run reproduces the goldens; a gas+new-layer run keeps the gas
  trajectory byte-identical + an RNG-conservation guard proves the new layer consumed zero gas RNG (the Wave-1
  C21 proof, generalized); a third DEMONSTRATIVE layer plugs in with no core edit (crit-10 extensibility proof —
  the demonstrative layer is an INDEPENDENT / non-feedback layer, so the byte-identical invariant holds). `→PLAN`:
  registry schema / layer-key form; the barrier table re-size for >2 layers (the LOCK requires re-sizing the
  [layerCount=2,chunkCount=4] table — a HOW this contract forces); per-layer store attach. bounds: C21, C11, LOCK
  barrier-table sizing. build: internal. **NOTE:** distinct from GT1 (the gas-DOMAIN species handler that writes
  source/sink INTO the gas field); XL2 is the FieldFabric-kernel WHOLE-LAYER registration seam — the two were
  conflated in the first draft; separated here. canon: G:layer-registry-extensibility (read_by FieldFabric + any
  future layer author).
  **NOTE — F2 byte-identical contradiction DISSOLVED (re-scoped c-converge-003 per d-tempfeedback-001):** the
  verify flagged "gas+new-layer keeps gas byte-identical (C21 generalized)" as contradicting XL1's required
  feedback. With feedback DEFERRED, temperature is a pure SINK → gas-with-temperature == gas-only (locked C21
  holds LITERALLY: temp consumes zero gas RNG, gas hash byte-identical), so the isolation proof is COHERENT as
  authored — for INDEPENDENT / sink layers. No re-baseline is required under the deferral. The byte-identical
  invariant is the extensibility test for an INDEPENDENT layer; a FEEDBACK layer (post-g-d3a8) legitimately
  CHANGES the gas trajectory, so ITS isolation proof has a DIFFERENT shape ("the change equals exactly the
  contracted feedback and nothing else") — named here as a later-wave concern, not built now.

### E. Gas-type extension seam (B1–B6, B8; consumer g-d3a8 — SECONDARY)

- **GT1 — Meta-gas handler seam.** B1/B3. *g-d3a8 ← GasDomain (SpeciesDriverRegistry #9 + IDriverReadView +
  phase scheduler).* **OBSERVABLE:** any meta-gas handler g-d3a8 supplies, at registration DECLARES the layers/
  species it owns + read/write scopes; at run time is the SOLE writer of its declared layers within its phase,
  READS the world only via a phase-consistent POST-TRANSPORT read-view, and CONTRIBUTES only scalar source/sink
  on its owned species (may not mutate other layers/topology/committed truth); a handler writing outside its
  declared scope/phase is REJECTED; the world view is the same regardless of which other handlers are present.
  acceptance: phase isolation (disjoint-layer handlers identical alone or together); out-of-scope write rejected
  by a negative test; determinism of the seam. `→PLAN`: phase count/ordering; write-lease/token structure; read-
  view copy mechanism/layout; owned-layer count caps; registration-record encoding. bounds: A3.1, A3.4, C11,
  C21. build: produced-now-consumed-later. canon: G:meta-gas-seam.
- **GT2 — Data-alone config + harness acceptance.** B2. **OBSERVABLE:** a gas reusing an existing archetype is
  expressible as DATA ALONE (shared-parent params + per-meta-gas params + per-meta-gas procedural visual, R15) —
  no config field carries code; a gas needing behavior the archetypes can't express is the observable trigger to
  add a handler (GT1); binding acceptance = a third gas type by data alone lands + PASSES THE HARNESS with no
  core edit; a config smuggling behavior outside the property set is rejected. `→PLAN`: config schema fields/
  types; value ranges/defaults; procedural-visual param encoding; species-id scheme; serialization. bounds: A3.2,
  A3.3, A3.4, A3.5. build: produced-now-consumed-later. canon: G:gas-config-acceptance. *[fix: "packing density",
  not "per-cell packing", to keep the example behavioral, not a layout commitment.]*
- **GT3 — Declarative reaction registry.** B4. **OBSERVABLE:** reactions DECLARED in INTENSIVE terms
  (concentration fractions + a temperature/energy window) so the SAME rule fires identically at coarse-band or
  fine-cell scale, with hysteresis (anti-chatter); each region's reaction evaluated at exactly ONE level per
  tick (no double-count); outputs = species-mass changes applied conservatively with all same-tick changes +
  typed consequence events (GT4); a reaction changing a species' class just edits the local mixture (no desync
  surface). acceptance: level-independence; exclusivity (a region under coarse+fine counted once, provable by a
  would-double-count test); conservation within the stated bound when summed with transport. `→PLAN`: threshold/
  hysteresis magnitudes (+3K/−1.5K class); rate caps (per-second); stoichiometric batch encoding; arbiter sort
  key + scaling; enthalpy/radiative constants. bounds: A2.2, C22, A8.8. build: produced-now-consumed-later.
  canon: G:reaction-intensive.
- **GT4 — Consequence/event plane.** B5. **OBSERVABLE:** consequence events are typed + SELF-CONTAINED (location/
  magnitude/species) so a consumer needs NO field state; proximity-INDEPENDENT; carry a publication revision
  (baseline-at-R + events-after-R recovery); guaranteed to reach consumers AHEAD of the lossy field
  reconstruction of the same change (systematically outrun lossy chunks; never on the gas stream); end-to-end
  latency BOUNDED. acceptance: a no-field-state consumer reconstructs the consequence from the event alone; under
  field-stream loss/delay the event still arrives before/independently of the field depiction; ordering/revision
  lets a missed consumer recover exactly; observable within the latency bound. `→PLAN`: the latency-bound NUMBER
  (sim ≤100 ms / perceived 100–300 ms, I16); event encoding + revision-counter width; delivery channel/
  reliability (RPC/ghost); baseline+delta encoding; queue sizing. bounds: A2.1, C12, I16. build: produced-now-
  consumed-later. canon: G:event-plane. **NOTE:** rides the LOCKED revisioned cross-layer GridEvent bus +
  reliable feed (not re-opened). This is the OUTBOUND gameplay-consequence plane to g-d3a8 — DISTINCT from XL1
  (the in-core gas↔temperature subscription).
- **GT5 — Flagship custom-driver + named exclusions.** B8. **OBSERVABLE:** a flagship gas may ship a CUSTOM
  driver via the SAME seam (GT1) and carry per-meta-gas visual params from which its look is DERIVED (published
  so a visual consumer renders it from sim state, not a side channel); day-one the seam admits ONLY field-
  transported gases — a gas hitting an excluded capability (agent/self-directed substrate; directed-velocity
  intent) is REJECTED at registration with the exclusion named, never silently degraded. acceptance: a flagship
  custom-driver passes the same seam acceptance as GT1 + renders only from published params; an excluded-
  capability request is rejected; the excluded modes carry no day-one implementation. `→PLAN`: capability-
  declaration encoding; driver-state blob format; procedural-visual param ranges; **whether agent-substrate
  persists as a declared-but-unbuilt MODE (brief §5) or is fully REMOVED per the R5 reframe (I12)** — see fork;
  velocity-gating wiring. bounds: A3.1, A3.4, R15, I12. build: produced-now-consumed-later. **owner_fork
  (parked-sibling, DEFAULT taken):** agent-substrate as a first-class 2nd registration pathway vs forever-parked
  single field pathway → DEFAULT = single field pathway, agent-substrate not a day-one shape (per I12/R5
  "AGENT_SUBSTRATE removed", risk-#1 gating); the 2nd-pathway question is deferred to **g-d3a8's own converge**,
  NOT a Wave-2 fork. canon: G:gas-exclusions-dayone.
- **(B6 self-play lane) — RECLASSIFIED, not a separate cross-node contract.** The agent-self-play validation
  lane is a g-9c41-INTERNAL validation discipline (harness + asserting agent both inside g-9c41's test surface).
  Its cross-node observable (same config → same answer in self-play as in the live read model) is already carried
  by OR3 (ExposureQuery self-consistency across the two g-d3a8 lanes) + GT2 (harness acceptance). Recorded as a
  g-9c41-internal acceptance row (crit-5 lane), not a converge-arch contract. *[fix: the firewall critic flagged
  the drafted K5 as a producer-side spec wearing a contract label — demoted here.]*

### F. Render-pipeline seam (B9–B14; consumer g-7e15 — SECONDARY)

- **RN1 — Read-model + pipeline-swap seam.** B11/B9. *g-7e15 ← GasDomain read model (the B31 oracle).*
  **OBSERVABLE:** the visual pipeline samples sim state ONLY through the published read model — it asks the SAME
  normative B31 oracle (REFERENCE by name; the formula is NOT restated here) and gets concentrations/species at a
  point for the current published revision, tagged with the revision + the resolution level that answered;
  choosing/swapping the concrete render pipeline (URP/HDRP/custom, A5.2) changes no producer-side type/signature/
  behavior. acceptance: B31 same-point-same-answer; replacing the render pipeline with the sim build unchanged
  leaves every read-model sample identical; every sample self-describes its revision + resolving level. `→PLAN`:
  push-vs-poll; sample-result layout; resolutionKey encoding + tier thresholds; the interpolation form; cadence;
  the URP/HDRP/custom pick. bounds: A5.2, A5.1, Q/band/tier C-rows. build: produced-now-consumed-later. canon:
  visual-reads-via-published-read-model. *[fix: the B31 formula was inlined in the draft — removed; reference by
  name only.]*
- **RN2 — Visuals are a derivation of sim state (blind-check).** B13/B14/B9. **OBSERVABLE:** for any captured
  moment g-9c41 exposes a machine-readable ground-truth readout (derived from the read model): how many gases +
  where, where it's dangerous (lethal-exposure regions via ExposureQuery), where gas flows; the visual output
  (incl. flagship menace silhouette + motion) must be a DERIVATION of this state — a blind vision-agent reading
  the rendered clip agrees with the ground truth; menace motion is sim-driven, NOT hand-staged VFX. acceptance:
  blind-check over a captured clip matches the ground-truth readout; same revision sequence → same blind-check
  verdict (reproducible from state). `→PLAN`: ground-truth artifact schema; blind-check tolerances; lethal-
  exposure threshold; clip resolution/format/path (g-5b07 B15); the stylization amplitude g-7e15 may add. bounds:
  A5.5, A5.1, A7.1 (only on a derived-not-faked clip), lethal-exposure C-row. build: produced-now-consumed-later.
  **owner_fork (parked-sibling, DEFAULT taken):** menace-motion STRICT derivation (g-7e15 may only stylize an
  existing sim-driven motion) vs HYBRID (bounded authored secondary motion on top) → DEFAULT = STRICT (crit-6
  default, safer claim); deferred to **g-7e15's converge**, NOT a Wave-2 fork. canon: visuals-derive-from-state.
- **RN3 — Per-meta-gas visual params from the driver read-view.** B10. **OBSERVABLE:** per meta-gas at a sampled
  point, g-9c41 publishes (via IDriverReadView) the param set that makes the gas visually DISTINGUISHABLE (R15:
  shared-parent + per-meta-gas + procedural-visual params), read from sim config/driver state, NOT invented in
  the renderer; a config-only new gas surfaces its distinguishability params with no producer code change; two
  distinct meta-gases yield distinguishable param sets (the property the RN2 "how many gases" blind-check relies
  on). acceptance: which params are exposed is a function of config (a data-alone gas exposes visuals with zero
  producer/renderer edit); read-view phase-consistent (no torn cross-species reads); distinct gases →
  distinguishable params. `→PLAN`: visual param schema field list; ranges/defaults; the procedural-visual
  generation function (g-7e15-side HOW); read-view layout/cadence. bounds: A3.2, A3.4, R15, A3.1. build: produced-
  now-consumed-later. canon: per-gas-visual-from-published-params.
- **RN4 — Shared min-spec frame budget.** B12. *g-7e15 (visual layer) + g-9c41 (sim layer) — two-sided
  boundary.* **OBSERVABLE:** sim-side and visual-side draw on ONE shared min-spec frame budget that is NOT
  double-spent; the sum is evaluated against a single frame envelope on the SAME profile crit-9 validates scale
  against (ties A1.7); there is a single named owner of the sim/visual boundary, accountable that the two shares
  fit one frame. acceptance: on the binding min-spec profile + worst-case scene, sim-side + visual-side time fit
  one envelope (no double-spend), scored against the same envelope crit-9 uses; exactly one accountable owner so
  a regression in one layer can't silently consume the other's share. `→PLAN`: the frame-budget number + the sim/
  visual split (A1.3 gas-ms, A5.3 render-ms); A8.3 coarse-tier tick ms + K-species multiplier; binding profile/
  proxy method (A1.4); binding scene (A1.5); **the frame-rate/FPS target**. bounds: A1.7, A1.3, A5.3, A8.3, A1.5.
  build: parked-edge. **owner_fork (DEFAULT taken):** the boundary OWNER = g-9c41 (sim owns the envelope + names
  the boundary, visual layer is claimant) vs a neutral whole-frame owner above both nodes → DEFAULT = g-9c41 owns
  sim-side + names the boundary (natural; ties A1.7); the neutral-owner option is deferred to the A1.7/crit-1↔
  crit-9 closure. canon: shared-frame-budget-single-owner. *[fix: "60-class" (a 60-FPS rate) leaked into the
  observable — removed; the FPS target → PLAN.]*

### G. Completeness sweep — remaining edges (TREE-completeness, honestly classified)

- **CS1 — Breach → topology-change consumer (B30, external).** *destruction-consumer (a PARKED later node =
  full destructibility) ← g-9c41 TopologyCore + GasDomain.* SAME observable shape + canon as GG3 (a real
  controlled local breach = a geometry-only topology-change change-set adding vertical portal(s), deterministic
  id, gas flows after; ONE local breach mechanism day-one, no destruction SYSTEM). acceptance: same-breach →
  same-adjacency + same-revision on all peers (deterministic); gas across the new portal consistent host↔clients
  at settle (cites the LOCKED barrier + breach-affected cells in the hash domain); a breach opening no adjacency
  is a defect. `→PLAN`: breach-portal id encoding; deferred-commit timing; breachable surfaces + count; trigger
  wiring (explosion/damage threshold); revision-counter width; **the lockstep-broadcast delivery mechanism**.
  bounds: C12, C16, A2.1. build: **dangling:destruction-consumer** — the breach PRODUCER half is internal to
  g-9c41 day-one; the full-destructibility CONSUMER is a separate large unresolved edge PARKED to a later node
  (named, not dropped; producer exists first). canon: shared G:topology-change[breach] with GG3 (ONE line).
  *[fix: "lockstep-broadcast" moved to →PLAN — only the determinism property stays in the contract.]*
- **CS2 — Co-op roles capability (B7) — G7 acceptance row, NOT a data contract.** g-d3a8 (parked) asserts which
  asymmetric-role shapes the core must not preclude; g-9c41 confirms the host-authoritative + count-as-config
  model SUPPORTS them: any role expressible as a distinct per-client INPUT/COMMAND stream + a distinct per-client
  INTEREST/view is supported (all players are non-authoritative input sources against one host writer; no role is
  a second authoritative field writer); a role needing a second field authority is OUT, surfaced as an owner
  conflict. build: parked-edge G7 (a capability/acceptance fact a resolve pass signs; no cross-node data flows
  here). No canon (one node parked).
- **CS3 — Cross-build protocol/schema version handshake (ORACLE-NMTL class 22) — EXPLICITLY DEFERRED to the
  g-5b07 distributable-build edge (capture folded c-converge-003).** Wave-2 harness is SINGLE-BUILD: all peers
  run the SAME build from tick 0 (I20 late-join OUT), so no cross-version negotiation exists to contract now.
  When the distributable demo / Steam-Playtest build (g-5b07 B17) introduces peers on DIFFERENT builds, a
  protocol/schema version handshake becomes a real contract (the wire header + GridEventKind enum + barrier-table
  shape are the versioned surface). NAMED as a deferral, not silently dropped; no day-one data flow. build:
  parked-edge (consumer = g-5b07). No canon (deferred). *(Makes ORACLE-NMTL class 22 an EXPLICIT named deferral
  rather than the implicit B17+I20 one the verify flagged.)*
- **Honest non-contracts (named for tree-completeness, deliberately NOT manufactured into data contracts):**
  B15 (clip artifact form) = open→PLAN render/capture magnitude (A2.3/A5.5/A7.x). B16/B17/B19 (min solo-startable
  slice / distributable build / min-spec backs demo quality) = g-5b07 open→G7 acceptance rows that CONSUME
  existing real contracts (crit-7 clean-1-player A6.1/A6.2 + crit-1 min-spec) — they mint no new cross-node data
  shape. B18 (first-clip-as-Steam-milestone) = root map_order milestone/sequencing G7. B20/B21 (steady real-
  footage byproduct / agent-drivable capture) = g-e6f2 acceptance rows riding the already-real harness
  (crit-5/A4.x) + the real-footage-only policy (A7.3). B22 = ANSWERED (byproduct of crit 3/5). B23/B24/B25/B26
  (moat-real / core-fantasy split / reusable-tech-asset / pride) = root owner ACCEPTANCE verdicts (open→G7);
  B24/B25's arch-flavored half is already covered by the engine-free/portable R4 contract (#13 + crit-9).
  Manufacturing data contracts for these would itself be a firewall error (inventing observable shape where only
  a milestone/acceptance question exists).

### H. Coarse-tier network replication + consistency (ADDED c-converge-003, 2026-06-16 — F1 repair; PRIMARY)

> **What this closes.** converge-verify Finding F1: the set LOCKED + contracted the FINE chunked-delta stream and
> the LOCAL read-model (OR1/OR2/OR3) but never declared whether/how the COARSE band tier reaches clients nor to
> what consistency standard — yet crit-3 (clients consistent at scale), crit-9 (~11k on-wire keyframe-inclusive
> cells), OR2-on-a-client ("coarse=floor, consumer-independence"), and GG4/OR4 ("amount never changes crossing
> tiers") all lean on it. Declared OBSERVABLE-FIRST; the standard is DERIVED from already-signed properties + the
> LOCK (no new owner G7 fork — see the DECIDED/DERIVED NOTEs); every magnitude / plane / interest-scheme → PLAN.
> Nothing re-opens the LOCK: CR3 APPLIES the locked I4/C1 integer-exactness discipline to the new tier, and CR1's
> locked-stream carrier option follows the LOCK's OWN "any Wave-2 layer/grid extension SHALL re-size the table"
> instruction (a surfaced re-size, never a silent reject).
>
> **PER-LAYER (folded c-converge-003 hardening pre-pass).** CR1/CR2/CR3 apply to EVERY coarse layer — coarse gas
> AND the coarse TEMPERATURE layer (its per-band energy/temperature state, A8.8) — not gas alone. This is the
> obligation that DISCHARGES XL1's coarse-scale "both layers consistent together" acceptance: the coarse
> temperature layer's host==client consistency at scale is DERIVED from CR1/CR2/CR3 read per-layer, NOT from the
> locked §T12 (which proves only the FINE Wave-1 toy scene — C15: 16 temp cells). The read seam (PULL, §RESOLVED-4)
> and the replicated authoritative coarse state (PUSH, CR1/CR2/CR3) are DISTINCT obligations — the coarse
> temperature layer is covered on BOTH, never assumed-covered because the read seam exists.

- **CR1 — Coarse-tier replication reaches clients (NOT host-only).** crit-3 / crit-9 + OR2. *every client-side
  consumer (visual read model RN1; any client-resident far-AI / ExposureQuery OR3) ← host coarse band state, PER
  LAYER (coarse gas AND the coarse temperature layer — see the §H PER-LAYER note).* trigger: the coarse tier
  advances / a committed revision publishes coarse changes. **OBSERVABLE:** the coarse band-tier authoritative
  state is replicated host→clients so that, for any (point, layer, committed revision) a client-side consumer is
  ENTITLED to query under OR2/OR3, the coarse state it reads equals the host's. COVERAGE FLOOR (this IS the
  observable, NOT →PLAN): a consumer's interest set MUST cover every (point, layer, revision) it is entitled to
  query — NO entitled gap; the relevance scheme may scope WHAT each client holds but may NEVER exclude an entitled
  query. Consumer-independence holds ACROSS THE NETWORK over the OVERLAP of entitlement sets (two clients with
  different windowed interest agree wherever both are entitled; a client visual and the host-side AI agree at the
  same point + revision) — coarse is the floor OR2 promises ON EVERY PEER for what that peer is entitled to, not
  just on the host. acceptance: a client-side coarse read of an ENTITLED (point, layer, revision) == the host's at
  the same committed revision; a client-resident far-AI querying a host-coarse region it is ENTITLED to sees NO
  gap (OR2 consumer-independence holds peer-to-peer over entitlement-overlap, not only host-local); the on-wire
  coarse cell-count crit-9 sizes IS this replicated state. `→PLAN`: carrier (locked-stream resolutionKey vs a
  separate coarse plane — if the locked stream is chosen, any NEW coarse resolutionKey value AND the barrier-table
  re-size SHALL be SURFACED as locked-wire-enum / table extensions per the LOCK, NEVER silently assigned in PLAN);
  per-client interest-management / relevance MECHANISM (whole-level vs windowed — ORACLE-NMTL class 20; HOW the
  entitlement set is computed/streamed, subject to the coverage floor above) + how a newly-entered region is
  correct on arrival (constrained by GG4/OR4 no-jerk, NOT free); coarse delta-vs-keyframe granularity; cadence.
  bounds: crit-3, crit-9, OR2, OR3, GG4/OR4, C10 resolutionKey. build: internal (produces the on-wire coarse
  state crit-9 sizes; consumed by OR1/OR2/RN1/OR3 ON CLIENTS + GG4/OR4). canon: coarse-tier-replication (read_by
  GasDomain + the temperature layer + every client-side read-model consumer). **NOTE — host-only DECIDED-OUT (not
  an open fork):** WHOLE-host-only is refuted by the two premises that do the work — (1) the core mechanic is
  reading gas in far/adjacent regions a client renders FROM coarse, and (2) OR1/OR2/RN1 consumer-independence is
  meaningless if consumers on different peers hold divergent coarse state for what they are BOTH entitled to;
  crit-9's owner-approved on-wire sizing CORROBORATES (is consistent with, does not alone decide) coarse being on
  the wire. What is NOT foreclosed and lives in the →PLAN interest space: a far region may be host-only UNTIL a
  consumer becomes entitled to it (relevance-scoped replication) — the coverage floor only forbids an ENTITLED
  gap. The owner may override at shape, but replicates-for-the-entitled is a derivation from signed facts, not a
  manufactured fork.
- **CR2 — Coarse-tier consistency standard = the locked DUAL guarantee, generalized PER LAYER.** crit-3 +
  I7/I8/I10. **OBSERVABLE:** every replicated coarse LAYER (coarse gas AND the coarse temperature layer) is held
  to the SAME dual-standard SHAPE as the locked fine stream — (i) LOSSLESS: a per-tick host==client BIT-EXACT
  correctness oracle over the authoritative coarse cells under the locked CellHash.FoldLayer-per-layer hash
  DISCIPLINE (deadband off) — the reference oracle that VALIDATES the reconstruction path; (ii) LOSSY production:
  bounded per-cell divergence ≤ a coarse quant-step every tick + convergence to bit-exact at settle/keyframe; both
  modes SHARE ONE reconstruction path (anti-gaming, I10 generalized). CROSS-TIER agreement at a coarse↔fine window
  boundary (the amount a coarse region holds == what a fine window produces there when it opens) is the OR1
  cross-tier observable (REFERENCE OR1 by name + the coarse mass bound below) — so GG4/OR4 amount-invariance cites
  a closed-or-explicitly-BLOCKED contract, never a silent green. The owner-signed band-handoff LOOSE tolerance
  (few cells, «никто точность измерять не будет») is the gameplay face of the LOSSY production mode; the
  no-jerk-EVER / believable-amount-rate firmness (GG4/OR4) is the settle / believable-rate face. acceptance:
  lossless oracle bit-exact every tick incl. across a COARSE topology change; lossy bounded every tick + ≥1
  non-vacuous bit-exact settle; one shared recon path proven (lossless+lossy identical path). `→PLAN`: the coarse
  quant-step Q_coarse; the divergence bound; the coarse settle predicate / keyframe cadence; the coarse lossy
  mass-conservation bound (C22 generalized — the coarse AGGREGATE-mass bound stays open→PLAN exactly as the fine
  C22 is, NOT a smuggled guarantee); the coarse↔fine seam-composition math (OR1); the coarse tier's per-layer
  layer/chunk addressing within the FoldLayer discipline (the table re-size is the LOCK's OWN SHALL-re-size,
  →PLAN). bounds: I7/I8/I10, C3/C4/C8/C9/C22, OR1, crit-3, GG4/OR4. build: internal. canon: coarse-tier-
  consistency (dual guarantee). **NOTE — standard DERIVED (not an open fork):** the dual guarantee is THIS
  project's consistency methodology (Wave-1 I6–I11). The lossless oracle is NOT a production cost the owner's
  loose gameplay tolerance argues against — it is a deadband-OFF TEST INSTRUMENT: because lossless and lossy SHARE
  one reconstruction path (I10 anti-gaming), the lossless oracle is what proves that shared path produces the
  CORRECT value, not merely a value inside a self-referential bound (a lossy-only standard is itself falsifiable
  but cannot establish correctness of the path PRODUCTION uses). Dropping it would WEAKEN the locked Wave-1
  correctness methodology; applying it to the new tier IS that methodology, not a new owner decision. (The owner's
  loose tolerance maps to the LOSSY production mode, which is the only mode players see.)
- **CR3 — Coarse authoritative state is EXACT (resolves the latent float-Patankar ↔ locked-integer conflict).**
  I4 + C1 + the verify latent-conflict. **OBSERVABLE:** the coarse tier's AUTHORITATIVE, replicated, hashed state
  — for EVERY coarse layer (gas AND the coarse temperature layer's per-band energy/temperature state, A8.8) — is
  exact integer/fixed-point — the locked I4/C1 "no float in authoritative state" discipline applied to the
  coarse tier; whatever coarse integrator PLAN picks (incl. the brief's exponential-relaxation Patankar scheme)
  reduces its output DETERMINISTICALLY to that exact authoritative state BEFORE it is hashed or put on the wire;
  a raw float/double is NEVER the authoritative or on-wire coarse value. Because only the HOST runs the solver and
  clients RECONSTRUCT from exact wire values (I1), cross-host/client float determinism is NOT required — only
  host-side determinism for reproducibility. acceptance: the authoritative coarse cell type is integer/fixed-point
  (no float in the hashed/replicated state, mirroring C1); a NEGATIVE test that a non-deterministically-reduced
  float path FAILS the host==client lossless oracle (CR2-i). `→PLAN`: the coarse cell representation (bit-width /
  fixed-point scale); whether the solver is integer-native or float-then-deterministic-quantize; the reduction
  rule; host-side reproducibility of the solve. bounds: I4, C1, C19, CR2. build: internal. canon:
  coarse-state-exactness. **NOTE:** this EXTENDS the LOCK's discipline to a new tier, it does NOT re-open it — and
  it forecloses the verify's three silent PLAN escapes (i host-only / ii float-hash-breaks-bit-exact / iii
  un-named coarse divergence bound).

`§SIGNOFF: converge-arch DECLARE — SIGNED-in-part @ 2026-06-16 (c-converge-002).`

**§SIGNOFF-BH — band-handoff (GG4/OR4) — OWNER-SIGNED 2026-06-16 (voice, this session).** Echoed owner verdict:
precision is NOT metrically important («точность не сильно важна», «примерно»; «никто точность измерять,
естественно, не будет»; «погрешность даже 10 клеток… несколько клеток подряд» — a few cells, loose); the
coarse simulation = the source of truth («грубо, симуляция… наш источник истины»), which within a radius
«разворачивается во второй слой… и третий» (his 3-tier hint: coarse-truth / prep-window / fine close-up — a
HUNCH routed to PLAN, not a lock); the player must APPROXIMATELY see the strength + main corner + that a weak
source accumulates slowly («он примерно должен видеть… главный угол»; left, came back, «газ не будет заполнен
всю комнату, он там чуть-чуть дозаполнится»); HARD requirement: «никаких подрагиваний… это 100%» (no shimmer/
pop on the handoff); «не нужно что-то прям дорогое… с геймплейной точки зрения». Owner flagged «охренеть как
важно» — OPEN to deeper tightening at the Wave-2 shape (so this signs the contract STRENGTH; the mechanism +
tolerance magnitude stay PLAN and the owner may revisit in-shape). **CLARIFIED 2026-06-16 (same session, owner
voice):** the requirement is GAMEPLAY-binding, not only metric — (a) NO visible jerk/twitch in the gas EVER,
including state computed OFF-SCREEN that surfaces on entry, because reading gas is the CORE mechanic; (b)
believable amount AND rate on return — the coarse tier (the source of truth) accumulates at a plausible, GRADUAL
rate (gloss corrected c-converge-003: owner signed «чуть-чуть дозаполнится» = gradual / no-jump, NOT strictly
non-decreasing; curve-shape → PLAN/g-d3a8) so the gas QUANTITY matches what the player expected from the source
strength he saw + elapsed time (no jump to half-full when ~quarter expected); crossing tiers changes only spatial
DETAIL, never amount or rate. Folded
into GG4 + OR4 acceptance.

**Decided this leg (not open forks):**
- XL1 cross-layer consistency = (a) BOTH layers consistent together (done_when #10 "networked-consistent
  together" + ADR-0004 §T12 + RESOLVED-1); the cheaper gas-only reading rejected (weakens crit-10 + contradicts
  the LOCK).
- Parked-sibling forks declared with DEFAULTS, deferred to the sibling's OWN converge (NOT Wave-2 forks; owner
  may override there): GT5 agent-substrate = single field pathway (I12/R5); RN2 menace-motion = strict derivation
  (crit-6 default); RN4 frame-boundary owner = g-9c41 owns sim-side + names the boundary (A1.7).

**Still PENDING (resolve-pass G7 rows, not converge-arch contracts):** CS2 (co-op roles capability) + the
B15–B26 non-contracts are owner-owned acceptance/milestone rows a later resolve/shape pass signs.

## play_check (converge-arch pass)

- `declare: §CONTRACTS — every TREE g-9c41 interaction + internal seam → a contract or an honest non-contract
  classification (IN/GG/OR/XL/GT/RN/CS families); B1–B31 all mapped; consumer-driven observable; HOW→PLAN; no
  contract re-opens the LOCKED foundation (firewall-verified).` (done)
- `decompose (heavy): the 6 §3.9 components sketched; internal seams → internal contracts (GG1–GG4, XL1–XL2 in-
  core); GT1 (gas-domain species handler) vs XL2 (FieldFabric whole-layer registry) separated — they were
  conflated.` (done)
- `architect (heavy): the high-risk architecture-on-paper = brief v2 ARCH-1v2, imported born-closed, rides PLAN
  as input-evidence (recorded in work/converge-g-9c41-arch.md); the emergent contract-architecture high-risk
  questions (B31 cross-tier composition OR1; multi-layer consistency XL1; band-handoff GG4/OR4) authored
  observable-first with HOW→PLAN; one miner gap-hunt caught the cross-layer/extensibility white spot (XL1/XL2).`
  (done)
- `contract_coverage: every TREE interaction → a §CONTRACTS entry — YES (B1–B31 + internal grid↔gas + cross-
  layer seams; build-order named for every produced-now-consumed-later / dangling edge).` (done)
- `arch_open: 0 — the brief's picks are imported born-closed; emergent contract properties authored observable-
  first (a PLAN failure surfaces as a BLOCKED contract, not a silent green).` (done)
- `arch_in_context_only: PASS — no architecture pick leaked into done_when; architecture-on-paper rides PLAN
  context only.` (done)
- `owner decisions (G7): band-handoff SIGNED in-session (voice); cross-layer consistency decided on done_when
  #10 + LOCK; 3 parked-sibling forks declared with defaults + deferred; batched, not scattered.` (done)
- `canon_proposed: two-sided contract canon (read_by both nodes) proposed per promotable contract; review/pulse
  promote (NOT written to knowledge/).` (done)
- `hardening: 15-agent in-session pre-pass (wf_c4e09962-08f: 6 drafters → 6 adversarial firewalls → 3 cross-
  cutting critics); fixes folded (render-K1 formula-inline, render-K4 FPS leak, ingestion-K1 byte-identical,
  ingestion-K2 white-box, gas-K2 packing wording, gas-K6 I12-supersede, completeness-K1 lockstep-broadcast,
  self-play-lane reclassification, breach-canon dedupe); the cross-layer/extensibility WHITE SPOT (XL1/XL2)
  caught + added. This is an IN-SESSION pre-pass (same-session helpers), NOT the binding refutation.`
- `verify (the converge-verify PLAY): DEFERRED to a separate fresh session (boundary) — the next CALL.`
- `close & route: CHECKPOINT — next = converge-verify (independent refutation of the contract set) → then
  c-shape-wave2 consumes the VERIFIED contracts.`

## §VERIFY (converge-verify pass — c-converge-verify, 2026-06-16) — VERDICT: BLOCKED CLOSE

> The BINDING independent refutation (G5 lifted to spec) — a SEPARATE fresh session attacking the §CONTRACTS
> set, NOT the 15-agent in-session pre-pass (that was a same-session self-check). Attacked on FOUR axes
> (CALL c-converge-verify): (1) COMPLETENESS — independent oracle; (2) FIREWALL — no observable leaks HOW;
> (3) NO-LEANING — no acceptance leans on a question open elsewhere; (4) NO-LOCK-REOPEN — no contract
> silently redefines wire/barrier/cross-layer-GridEvent/cell-hash. The LOCK was checked against the VERBATIM
> ADR-0004 §LOCK + ADR-0003 C1–C22 (read-only). Verify REFUTES; it writes no new contracts — a real gap is a
> blocked close + a NAMED repair bounced to converge-arch (c-converge-003). NO `§SIGNOFF: converge-verify
> passed` is written (holes found); a clean re-run after the repair gates shape CONSUMING the contracts.

### ORACLE-NMTL — independent contract-class checklist (AUTHORED from first principles this session)

`knowledge/` held no node-class checklist (an empty oracle = BLOCKED close, never auto-PASS), so the oracle
was authored from first principles + competing precedents — NOT the brief / converge-arch sources (that
shares the prover's blind spot). Precedents: authoritative client-server delta-netcode (Quake/Source/
Overwatch), chunked single-writer atmospherics (SS13/SS14, Stationeers, Noita), data-oriented layered ECS,
LOD / streaming engines. The 25 contract classes a networked **multi-TIER multi-LAYER host-authoritative
field-simulation core serving sibling consumers** must expose, and the §CONTRACTS coverage:

| # | contract class | §CONTRACTS entry | verdict |
|---|---|---|---|
| 1 | ingestion / source boundary | IN1, IN2 | ✓ |
| 2 | transport-vendor decoupling | IN3 | ✓ |
| 3 | authority / replication model (FINE) | I1 (locked) + IN3 | ✓ (foundation) |
| 4 | FINE-tier state repr / quantization / wire | locked C1, C2, C10 | ✓ |
| 5 | FINE-tier consistency / recovery (divergence/settle/keyframe/fault) | locked C3/C4/C8/C9/C12/C13/C22 | ✓ |
| 6 | **COARSE-tier network replication + consistency obligation** | — | **✗ FAIL → F1** |
| 7 | multi-resolution read-model / sampling oracle | OR1, OR2, OR3, RN1 | ✓ |
| 8 | cross-tier composition (seam agreement) | OR1 (observable-first; BLOCKED-not-green) | ✓ |
| 9 | layer-registry extensibility | XL2 | ⚠ (F2) |
| 10 | inter-layer interaction / event bus | XL1 + locked GridEvent bus | ⚠ (F2) |
| 11 | topology mutation (breach) | GG1, GG3, CS1 | ✓ |
| 12 | geometry ↔ domain sovereignty | GG2 | ✓ |
| 13 | tier-transition / band-handoff continuity | GG4, OR4 (owner-signed) | ✓ |
| 14 | behavior / content extension (species handlers) | GT1, GT2, GT5 | ✓ |
| 15 | domain-rules registry (reactions) | GT3 | ✓ |
| 16 | outbound consequence / event plane | GT4 | ✓ |
| 17 | shared resource / perf budget envelope | RN4 + A1.7 | ✓ |
| 18 | render read-model seam | RN1, RN2, RN3 | ✓ |
| 19 | time / tick / determinism | locked C16, I4 | ✓ (foundation) |
| 20 | per-client interest / relevance management | folded into GG4 + OR2 observable; mechanism →PLAN | ⚠ (part of F1) |
| 21 | lifecycle / late-join / session-join | I20 (OUT) + keyframe recovery | ✓ (named deferral) |
| 22 | protocol / schema version handshake (cross-build) | B17 non-contract + I20 | ✓ (implicit deferral — capture) |
| 23 | persistence / serialization | cut ("save/load → none") | ✓ (named cut) |
| 24 | security / authority-validation | CS2 + co-op-friends N/A | ✓ (honest non-contract) |
| 25 | observability / debug-surface (cross-node) | RN2 + GT4 + B22 | ✓ |

`canon_proposed`: **ORACLE-NMTL** → propose to knowledge/ (serves: g-9c41 + future networked-sim nodes;
read_by: converge-verify of this node-class). converge-verify PROPOSES; review/pulse promote (verify never
writes knowledge/).

### Finding F1 — NO coarse-tier network-replication contract (COMPLETENESS FAIL + NO-LEANING FAIL)

The set LOCKED the FINE chunked-delta stream (table `[layerCount=2,chunkCount=4]`) and contracted the
read-model (OR1/OR2/OR3 = local sampling, not network) — but NEVER declares whether/how the COARSE band tier
replicates host→clients, nor to what consistency standard. Four weight-bearing places lean on this UNCITED:
- **crit-3** "clients consistent" — proven in Wave 1 on the FINE toy scene, not the coarse tier at scale;
- **crit-9** on-wire ~11k keyframe-inclusive cells (knowledge/g9c41-wave1-hold-mechanism-lossy-projection)
  implies the coarse tier IS what's on the wire at scale — yet no contract states it;
- **OR2** "coarse = floor, no gaps, consumer-independence" — on a CLIENT this requires coarse state to be
  PRESENT on the client (else a far-AI / visual consumer on a client sees a gap where the host sees coarse →
  consumer-independence violated). OR2 leans on an uncited "coarse reaches every client-side consumer";
- **GG4/OR4** "amount never changes crossing tiers" — needs coarse↔fine mass agreement (C22/OR3) atop the
  same unresolved decision.
LATENT CONFLICT: the brief's exponential-relaxation Patankar coarse integrator is typically FLOAT; if coarse
replicates-and-hashes in the locked `CellHash.FoldLayer` host==client bit-exact, a float solver breaks
integer-determinism (I4/LOCK). Uncontracted, PLAN gets three silent escapes: (i) coarse host-only → breaks
OR2 on clients; (ii) coarse replicates with a float solver → breaks bit-exact crit-3; (iii) PLAN invents a
coarse-tier divergence bound that no contract names. **This is exactly the "gone somewhere primitive on the
scale claim, unnoticed" the converge layer exists to prevent.**
REPAIR (→ converge-arch c-converge-003, not authored here): declare a COARSE-tier-replication contract
observable-first — coarse reaches every client-side consumer (vs host-only); carrier (locked-stream
resolutionKey vs a separate plane); consistency standard (bit-exact / bounded-divergence / host-only) +
coarse-solver determinism obligation; HOW (plane / granularity / interest-management) → PLAN.

### Finding F2 — XL1 feedback vs the locked pure-sink proofs (NO-LOCK-REOPEN + internal contradiction)

LOCK (verbatim ADR-0004): §T12 "temperature is a pure sink with no feedback to gas, so it always converges";
C21 "gas+temp keeps gas hash byte-identical"; `ReactionHeat=32` pinned "so a Wave-2 author cannot silently
move the reconstructed-Temperature trajectory"; `GridEventKind{GasChanged=1,Breach=2,Reaction=3}` (all
gas/breach-sourced). XL1 (crit-10 tightening) requires a FEEDBACK interaction (NOT a sink). Two unreconciled
collisions:
1. **Literal contradiction.** XL2 accepts "gas+new-layer run keeps the gas trajectory byte-identical (the
   Wave-1 C21 proof, generalized)". Once feedback is on, gas-with-temp ≠ gas-only — generalizing C21
   "byte-identical to the gas-only golden" while feedback exists is incoherent. Must split: byte-identical
   isolation-proof = the 3rd DEMONSTRATIVE layer (XL2); trajectory-changing feedback = gas↔temperature
   (XL1); the Wave-1 sink / `ReactionHeat=32` / C21 stays a FROZEN control.
2. **LOCK point.** XL1's MECHANISM paragraph describes pub/sub. A feedback FROM temperature to gas needs a
   temperature-SOURCED event — absent from the locked enum (gas/breach only). So feedback is either
   (a) event-based → silently extends the locked `GridEventKind` enum (a LOCK change that must be SURFACED,
   like the barrier-table resize), or (b) read-based (the gas reaction phase reads temperature via a
   phase-consistent read-view; phase-ordering → PLAN; enum untouched). XL1 routes "phase ordering" to PLAN
   (read-based) yet its MECHANISM says pub/sub (event-based) — neither XL1 nor the LOCK reconciles this.
REPAIR (→ c-converge-003): XL1 states feedback = read-based-in-phase-order (enum untouched; Wave-1 sink =
frozen control) OR event-based (SURFACE the enum extension, never silent in PLAN); re-baseline XL2 isolation
(demonstrative layer == gas+temp, NOT == gas-only).

### Axes that passed CLEAN (balance)

- **FIREWALL — PASS (1 borderline note).** Observables route HOW (push/poll, format, cadence, layout,
  magnitude) to `→PLAN`; the pre-pass already removed the FPS leak, byte-identical-ids, and the inlined B31
  formula. Borderline: the XL1 MECHANISM paragraph carries a communication model, but it restates LOCKED
  foundation + routes the open HOW → not a NEW smuggle (capture: trim it at the repair).
- **NO-LOCK-REOPEN — PASS except F2.** XL2 names the `[2,4]` table and routes the resize to PLAN — exactly
  per the LOCK's own instruction ("any Wave-2 layer/grid extension SHALL re-size the table"), NOT a re-open.
  GG1 correctly separates the sector/adjacency revision from the locked per-(layerKey,chunkIndex) barrier.
  XL1 references (does not redefine) the locked `CellHash.FoldLayer`.
- **OR1 cross-tier (CALL special focus) — PASS** (modulo F1's "does coarse reach the client"): authored
  observable-first with the explicit "not satisfiable at a seam → BLOCKED contract, not silent green"
  discipline; OR2 thinnest-open-level precedence makes cross-CONSUMER agreement exact and routes the
  cross-TIER tolerance to PLAN.
- **GG4 / OR4 band-handoff (CALL special focus) — PASS:** owner-signed "no jerk EVER" + "believable amount/
  rate" are PROPERTIES (owner is the named acceptor), magnitudes → PLAN. Minor (capture): GG4's bounds list
  omits C22 though its acceptance depends on the lossy mass bound; the OR4 twin cites C22.

### play_check (converge-verify pass)

- `1 recite: two propositions stated (set COMPLETE; no answer leans/leaks)` (done)
- `2 attack-completeness: ORACLE-NMTL authored from first principles + precedents (NOT brief/converge-arch),
  named, proposed as canon; 25 classes mapped; FAIL=1 (F1 coarse-tier replication)` (done)
- `3 attack-smuggling: firewall PASS (HOW→PLAN; XL1 MECHANISM borderline, not new); no-leaning FAIL=1 (=F1
  uncited coarse-replication lean); no-lock-reopen PASS except F2; checked vs verbatim ADR-0004/ADR-0003`
  (done)
- `4 close: BLOCKED — next = c-converge-003 (repair to converge-arch carrying F1+F2); verify re-runs after
  re-close; NO §SIGNOFF: converge-verify passed written; not two-strikes (first bounce of these rows)`
  (done)

## §REPAIR (converge-arch repair pass — c-converge-003, 2026-06-16) — F1 CLOSED, F2 DISSOLVED

> The converge-arch REPAIR of the two converge-verify findings (the §VERIFY BLOCKED close above), folding owner
> decision d-tempfeedback-001 (s-decide-003). Observable-first, HOW→PLAN, nothing re-opens the LOCK. The contracts
> are EDITED IN PLACE (the canonical set shape consumes stays in §CONTRACTS — section H is new, XL1/XL2/GG4 carry
> "re-scoped/added c-converge-003" markers, §RESOLVED-4 is new); this section records the provenance + the
> re-mapped oracle + the sign-off. The BINDING re-refutation is a FRESH converge-verify session (the next CALL) —
> this repair is NOT self-certified.

**F1 — CLOSED.** New §CONTRACTS section H (CR1/CR2/CR3): CR1 declares coarse-tier replication reaches every
client-side consumer (host-only DECIDED-OUT via crit-9 owner-approved + the core mechanic + OR1/OR2 cross-peer
consumer-independence — not a manufactured fork); CR2 sets the consistency standard = the locked DUAL guarantee
(lossless bit-exact oracle + lossy bounded-divergence-converging-at-settle) generalized to the coarse tier
(DERIVED from the project's own Wave-1 methodology I6–I11, not a new owner decision); CR3 resolves the latent
float-Patankar ↔ locked-integer conflict by requiring the coarse AUTHORITATIVE / hashed / on-wire state be EXACT
integer/fixed-point (the locked I4/C1 discipline extended to the new tier — float may be only a transient internal
computation deterministically reduced before hashing). This forecloses the verify's three silent PLAN escapes
(host-only / float-hash / un-named coarse bound). The four weight-bearing leans (crit-3, crit-9, OR2-on-a-client,
GG4/OR4) now cite CR1/CR2/CR3. **No G7 fork raised** — the standard derived cleanly from signed properties + the
LOCK (the CALL's fork condition "if NOT derivable cleanly" was not met).

**F2 — DISSOLVED via d-tempfeedback-001 (feedback DEFERRED), XL1/XL2 re-scoped IN PLACE.** The owner deferred
temperature→gas feedback (post-g-d3a8), so temperature stays a pure SINK → the locked §T12 + C21 byte-identical
HOLD, the locked GridEventKind enum is UNTOUCHED (no temperature-sourced event), and the XL2-vs-XL1 byte-identical
contradiction disappears. XL1 re-scoped: multi-layer SINK consistency AT COARSE SCALE + the grid-addressed
READ-READY seam (§RESOLVED-4); the crit-10 "feedback interaction" requirement re-scoped to a NAMED deferral + the
forward path (read-based enum-untouched OR event-based-with-SURFACED-enum-extension — a later wave's call) + the
forward constraint (read seam reads any resolution on a committed revision; don't foreclose feedback); the
firewall-borderline MECHANISM paragraph TRIMMED to §RESOLVED-4 + PLAN. XL2: the byte-identical isolation is
coherent as authored for INDEPENDENT/sink layers (no re-baseline needed under the deferral); a feedback layer's
different isolation proof named as a later-wave concern. §RESOLVED-4 records the owner-confirmed inter-layer read
architecture (grid = addresses+ownership+bus+commit-clock NOT a data router; per-layer push-events + pull-read-
model on committed revisions; matches OR1/OR2 + GG2).

**Minors folded:** C22 (+CR1/CR2) added to GG4 bounds (its "amount never changes crossing tiers" depends on the
lossy mass bound AND on coarse↔fine agreement; OR4 twin already cited C22). XL1 MECHANISM trimmed (above).
Cross-build version-handshake made an EXPLICIT named deferral (CS3) to the g-5b07 edge.

**ORACLE-NMTL re-map (the classes that were not clean at verify):**

| # | class | at verify | after repair |
|---|---|---|---|
| 6 | COARSE-tier network replication + consistency | ✗ FAIL (F1) | **✓ CR1, CR2, CR3** |
| 9 | layer-registry extensibility | ⚠ (F2) | **✓ XL2 (coherent under the deferral)** |
| 10 | inter-layer interaction / event bus | ⚠ (F2) | **✓ XL1 (sink + read-ready) + §RESOLVED-4 + locked bus** — ✓ CONTINGENT on c-shape-wave2 G9 rewording crit-10 to NAME the feedback deferral (the sink reading already satisfies the literal frozen crit-10; the narrow re-verify must CONFIRM this, not assume shape did it) |
| 20 | per-client interest / relevance | ⚠ (part of F1) | **✓ CR1 COVERAGE FLOOR (interest set ⊇ entitled-query set = the observable, not bare routing); OR2 consumer-independence scoped to entitlement-overlap; relevance MECHANISM →PLAN** |
| 22 | protocol/schema version handshake | ✓ (implicit) | **✓ CS3 (explicit named deferral)** |

All 25 classes covered; the other 20 were already ✓ at verify and are untouched.

**Hardening fold (in-session adversarial pre-pass wf_b5e55d56-406, 7 agents, 4 verify axes + a no-fork-derivation
challenge).** Verdict: the no-fork derivation HOLDS (adjudicated — the coarse lossless oracle is the locked I10
anti-gaming TEST INSTRUMENT, not a new owner cost; host-only refuted by the core mechanic + cross-peer consumer-
independence), so NO G7 fork is raised. Two MUST-FIX holes — both at the seams the repair itself touched — were
found and folded: (1) **CR1 interest-set floor** — CR1 gated coarse equality on an undefined "interest set" with
no lower bound, re-opening the F1 OR2-on-a-client hole one level down (a client-resident far-AI entitled to a far
region could fall outside its interest set); folded a COVERAGE FLOOR (interest set ⊇ entitled-query set) as the
observable + scoped OR2 consumer-independence to entitlement-overlap. (2) **XL1 coarse-temperature per-layer** —
the F2 re-scope widened XL1 to "both layers consistent AT COARSE SCALE" but CR1/CR2/CR3 were gas-scoped and §T12
proves only the fine toy scene (the "gone primitive on the scale claim" anti-pattern, re-introduced for
temperature); folded PER-LAYER (CR1/CR2/CR3 apply to the coarse temperature layer too) + qualified the §T12
citation. Nits folded: the resolutionKey SURFACED-extension guard (symmetric with the barrier-table + GridEventKind
discipline); "monotone"→"gradual" (the contract over-stated the owner's «чуть-чуть дозаполнится» signoff — a
faithfulness correction, NOT a re-litigation, in GG4 + CR2 + the §SIGNOFF-BH echo, curve-shape →PLAN/g-d3a8);
§RESOLVED-4 push/pull → semantic categories (delivery →PLAN); CR2 C22-ambiguity + cross-tier seam-agreement made
explicit (GG4/OR4 amount-invariance now cites OR1 + the coarse mass bound honestly); CR1 host-only NOTE leans on
the two load-bearing premises with crit-9 demoted to corroboration; class-10 ✓ marked contingent on the shape's
crit-10 rewording. This is a SAME-SESSION pre-pass — the binding refutation is the next fresh converge-verify.

## §SIGNOFF (converge-arch repair pass — c-converge-003)

`§SIGNOFF: converge-arch REPAIR (F1 coarse-tier replication + F2 re-scope) — SIGNED-in-part @ 2026-06-16
(c-converge-003).` F1 closed observable-first (CR1/CR2/CR3), standard DERIVED — no new owner fork. F2 dissolved
under owner decision d-tempfeedback-001 (feedback deferred); XL1/XL2 re-scoped in place; §RESOLVED-4 carries the
owner-confirmed read architecture (s-decide-003). HOW magnitudes → PLAN throughout; nothing re-opens the LOCK
(CR3 extends I4/C1; CR1 follows the LOCK's own SHALL-re-size; XL1 leaves the GridEventKind enum + §T12 + C21
untouched). The BINDING independent refutation is the next FRESH converge-verify session (NOT self-certified here).

## play_check (converge-arch repair pass — c-converge-003)

- `declare: F1 → §CONTRACTS section H (CR1 reaches-clients / CR2 dual-guarantee standard / CR3 exact-state);
  XL1/XL2 re-scoped in place under d-tempfeedback-001; GG4 bounds + CS3 version-handshake folded. Every new
  contract consumer-driven + observable; HOW→PLAN.` (done)
- `decompose: the coarse-tier replication seam is the NETWORK face of the already-decomposed coarse tier — CR1
  (carrier/interest →PLAN) / CR2 (standard) / CR3 (representation) split atomically; no new sub-node minted.`
  (done)
- `architect: the one emergent high-risk question (the coarse consistency STANDARD + the float/integer conflict)
  worked observable-first and DERIVED from signed properties + the LOCK (recorded in work/converge-g-9c41-arch.md
  §EMERGENT Q5); no architecture-on-paper leaked into done_when.` (done)
- `contract_coverage: every TREE interaction → a §CONTRACTS entry — YES; the F1 coarse-replication white spot now
  CR1–CR3; ORACLE-NMTL 25/25 covered (re-map above).` (done)
- `arch_open: 0 — F1 standard derived (no open fork); F2 dissolved by an EXISTING owner decision
  (d-tempfeedback-001), not a new one.` (done)
- `arch_in_context_only: PASS — no pick in done_when; the architecture rides PLAN context.` (done)
- `owner decisions (G7): none newly raised — F1 derived; F2 folds the already-made d-tempfeedback-001. No
  scattered / auto-decided fork. (Owner reachable only if a real coarse-standard fork had opened — it did not.)`
  (done)
- `hardening: focused in-session adversarial pre-pass (wf_b5e55d56-406, 7 agents) on the 4 verify axes +
  F1-closed/F2-dissolved + the derivation-validity / no-fork challenge + ORACLE-NMTL re-map; verdict = no fork
  (derivation holds) + 2 must-fix (CR1 interest-floor, XL1 per-layer coarse-temperature) + nits — ALL folded
  (see §REPAIR Hardening fold). This is a SAME-SESSION pre-pass, NOT the binding refutation.`
- `verify (the converge-verify PLAY): DEFERRED to the next FRESH session (boundary) — the next CALL.`
- `close & route: next = a NARROW fresh converge-verify on the repaired set (section H + re-scoped XL1/XL2 +
  §RESOLVED-4 + minors) → then c-shape-wave2 consumes the VERIFIED contracts.`

## §VERIFY-2 (converge-verify RE-RUN — c-converge-verify-002, 2026-06-16) — VERDICT: PASSED CLEAN

> The narrow BINDING re-refutation (G5, a SEPARATE fresh session — NOT the c-converge-003 repair session, NOT
> its in-session pre-pass wf_b5e55d56-406) of the REPAIRED surface: §CONTRACTS section H (CR1/CR2/CR3), re-scoped
> XL1/XL2, §RESOLVED-4, GG4 bounds (C22/CR1/CR2), CS3. Attacked on the FOUR axes — firewall + no-lock-reopen
> NARROWED to the new/edited entries; NO-LEANING + consumer-independence RE-TRACED across every contract citing a
> CR-row or §RESOLVED-4 — with the three CALL-mandated adjudications, then each finding adversarially
> cross-examined to kill plausible-but-wrong holes. ORACLE-NMTL reused (still proposed canon). Checked vs the
> VERBATIM LOCK (s-converge-verify-001 §APPENDIX). RESULT: 0 BLOCK-severity holes survive; the F1 closure and the
> F2 dissolution HOLD; the repaired set is VERIFIED. 4 non-blocking CAPTUREs carried forward to c-shape-wave2 / PLAN.

### Re-run method
Independent fan-out (14 agents): one skeptic per axis/adjudication prompted to BREAK the set, each finding
cross-examined by a second independent skeptic prompted to REFUTE it (default-refuted unless it survives a
charitable read). The fresh main session is the BINDING reviewer; it adjudicated every finding against the
verbatim LOCK + the contracts — NOT by vote. One BLOCK was proposed (no-leaning, on the CR1 coverage floor) and
adjudicated DOWN to CLEAN; the only surviving items are 4 non-blocking CAPTUREs.

### Four axes — all PASS (on the repaired surface)
- **COMPLETENESS — PASS.** ORACLE-NMTL 25/25 independently re-confirmed (not by trusting the §REPAIR re-map):
  class 6 (CR1/CR2/CR3) closes all three F1 silent PLAN escapes (host-only / float-hash-breaks-bit-exact /
  un-named coarse divergence bound); class 9 (XL2 coherent under the sink — locked C21 byte-identical holds
  LITERALLY for independent/sink layers); class 10 (XL1 sink + §RESOLVED-4 + locked bus — adjudication 3); class
  20 (CR1 coverage floor + OR2 entitlement-overlap — adjudication 1); class 22 (CS3 explicit named deferral). No
  oracle class missed now that coarse replication is explicit — the tier-transition / newly-entitled-region race
  is covered by COMPOSITION (CR1 coverage floor + GG4/OR4 no-jerk-on-entry + class 13), not uncontracted. Atomic
  split of the compound criteria: crit-3 (all clauses → I6–I11 + CR1/CR2 + GG1/GG3 + A2.x + C16 + B15), crit-10
  (all clauses → adjudication 3), crit-9 (7/8 map; the c-review-001 keyframe-inclusive bandwidth basis carried by
  the crit-9 text + knowledge/g9c41-wave1-hold-mechanism-lossy-projection + CR1/CR2 — see CAPTURE V2-1).
- **FIREWALL — PASS (new/edited entries).** Observables carry properties/shapes; every HOW (push/poll, wire/byte
  format, cadence, layout, magnitude) routes →PLAN. The XL1 MECHANISM-paragraph trim (the verify-001 borderline)
  is REAL — moved to §RESOLVED-4 + PLAN; §RESOLVED-4 keeps delivery (sync-pull vs subscription) →PLAN. Closest
  borderline = CR3 naming "integer/fixed-point" in its observable — CONFIRMED CLEAN: it names the LOCKED I4/C1
  integer-only-authoritative discipline EXTENDED to the new tier (a frozen invariant, not a fresh HOW); the open
  representation magnitude (bit-width, scale, integer-native vs float-then-quantize, the reduction rule) is →PLAN.
  (Parallel to verify-001's XL1-MECHANISM borderline.)
- **NO-LEANING — PASS.** The four F1 leans now cite CR1/CR2/CR3 (crit-3 → CR1/CR2 bounds; crit-9 → CR1 "the
  on-wire coarse cell-count crit-9 sizes IS this replicated state"; OR2-on-a-client → CR1 peer-to-peer
  consumer-independence; GG4/OR4 amount-invariance → CR1/CR2/C22 + OR1). CR1/CR2/CR3's OWN foundations trace to
  cited/locked/signed facts (CR2 → I7/I8/I10; CR3 → I1/I4/C1/C19; CR1 host-only-decided-out → the owner-signed
  read-gas core mechanic + OR1/OR2 consumer-independence + crit-9 corroboration). A BLOCK was proposed here (CR1
  leans on the undefined term "entitled-query set", untraceable for the RN1 visual consumer) and ADJUDICATED
  DOWN: the floor is a UNIVERSALLY-QUANTIFIED falsifiable observable (it holds for-all-entitled-queries without a
  closed-form entitlement set), and the proposed fix (pin each consumer's query domain inside the contract) would
  itself be a FIREWALL LEAK — confirming the contract is RIGHT to route the entitlement MECHANISM →PLAN. (→ CAPTURE
  V2-2.)
- **NO-LOCK-REOPEN — PASS (new/edited entries, vs verbatim LOCK).** CR1 carrier: a NEW coarse resolutionKey value
  AND the barrier-table re-size are SURFACED as locked-wire-enum / table extensions per the LOCK's own "SHALL
  re-size" (the standard verify-001 already blessed for XL2), never silently assigned. CR3 EXTENDS the I4/C1
  no-float-in-authoritative-state discipline + references (does not redefine) CellHash.FoldLayer + the [2,4]
  table. XL1 (feedback deferred) leaves GridEventKind + §T12 + C21 UNTOUCHED (temperature pure sink; no
  temperature-sourced event). §RESOLVED-4 reads only COMMITTED revisions (never live mid-tick state) — preserves
  the locked single-writer-per-(LayerKey,phase) determinism. XL2 table-resize surfaced. CS3 names the future
  versioned surface (wire header + GridEventKind + barrier-table) without redefining it.

### The three mandated adjudications
1. **Class-20 interest-set COVERAGE FLOOR — GENUINELY ✓ (a closed observable, NOT a deferral).** It escapes both
   horns of the dilemma: (a) "entitled" is NOT OR2's "answer everywhere" — OR2 is a tier-RESOLUTION floor (no
   queried point falls below coarse to undefined), NOT a spatial-entitlement-everywhere claim — so there is no
   whole-level-replication mandate and no inconsistency with the "host-only UNTIL a consumer becomes entitled"
   note; (b) it is NOT a tautology — entitlement is set UPSTREAM by gameplay role (actor position per OR3 /
   render view), INDEPENDENT of the network relevance mechanism the floor constrains. The floor ("interest set ⊇
   entitled-query set; the relevance scheme may scope WHAT a client holds but may NEVER exclude an entitled
   query") is a falsifiable invariant (construct an actor entitled per OR3 to region R, omit R from the stream,
   the client far-AI sees a gap → FAIL) — teeth, testable once PLAN fixes the entitlement computation. → CAPTURE
   V2-2 (keep "entitled" anchored to gameplay-reach, never the streamed window).
2. **Coarse-temperature PER-LAYER discharge of XL1 — GENUINE ✓.** CR1/CR2/CR3 carry the per-layer obligation
   INLINE (not only the §H header): each names "the coarse temperature layer('s per-band energy/temperature
   state, A8.8)". The discharge is real: coarse temperature HAS a defined coarse state (A8.8); the sink
   (gas-reaction-driven) runs HOST-only and its authoritative coarse result replicates, the client RECONSTRUCTS
   from exact wire (I1) — no hidden client re-sim; the coarse obligation is DERIVED from CR1/CR2/CR3 per-layer,
   NOT from §T12 (explicitly dis-anchored — §T12 proves only the FINE 16-cell toy scene); PUSH (CR1/CR2/CR3) and
   PULL (§RESOLVED-4 read seam) are DISTINCT obligations and the PULL-on-a-client is FED BY the CR1-replicated
   PUSH state (stated, not assumed). → CAPTURE V2-3 (exercise the COARSE per-band temperature READ in PLAN tests).
3. **Class-10 ✓ CONTINGENCY — GENUINE ✓, INDEPENDENTLY CONFIRMED (per the CALL: "CONFIRM, not assume shape did
   it").** The literal frozen crit-10 splits into 10a (≥2 layers ride ONE seam, networked-consistent together →
   XL1 + XL2), 10b (a cross-layer interaction observable, "reaction/heat → temperature responds" → XL1 SINK —
   this is the gas→temperature direction; FEEDBACK is the REVERSE arrow, NOT named by the frozen text), 10c (a
   new layer plugs in without core edits → XL2), 10d (a REAL controlled wall-breach → GG3 / CS1). All four are
   covered NOW by the sink-only set. The "feedback" requirement was a beyond-frozen-text tightening a prior shape
   was to fold in — now deferred (d-tempfeedback-001). So contract coverage vs the LITERAL frozen crit-10 is
   COMPLETE; the contingency is NOT circular (a clean verify UNBLOCKS shape, then shape rewords crit-10 as its G9
   TREE-honesty job, downstream). The verdict is therefore NON-contingent from the contract gate's standpoint.
   → CAPTURE V2-4 / forward mandate.

### CAPTUREs (non-blocking — carried to c-shape-wave2 / PLAN; verify writes no contracts)
- **V2-1 (crit-9 bandwidth basis):** the crit-9 PLAN/validation pass must compute coarse-grid bandwidth from the
  ON-WIRE keyframe-inclusive basis (~11k lossy cells — the crit-9 refined text + the knowledge file + CR1/CR2
  coarse-keyframe-cadence →PLAN), NOT A8.4's literal "measured dirty-chunk size" (a delta-only number = the
  ~5.3× optimistic basis the c-review-001 refinement rejects). A8.4 + the §COVERAGE-MAP crit-9 row are STALE
  w.r.t. the post-FORM-pass crit-9 refinement and should be freshened at the next converge-arch / audit touch
  (outside this verify's write scope).
- **V2-2 (entitlement anchoring):** keep CR1's "entitled" anchored to gameplay-reach (actor position / render
  view per OR2/OR3), never silently re-bound to the streamed interest window (which would degrade the coverage
  floor to a tautology); the "a client far-AI/visual querying an entitled region sees no gap" acceptance is the
  teeth.
- **V2-3 (coarse temperature read):** exercise the COARSE per-band temperature PULL (read-model on a committed
  revision) at coarse scale in PLAN tests, mirroring the coarse PUSH CR1/CR2/CR3 mandate — not only the fine
  per-room read the §RESOLVED-4 illustration shows.
- **V2-4 (crit-10 TREE honesty):** c-shape-wave2 G9 rewords TREE done_when #10 to NAME the temperature→gas
  feedback deferral (d-tempfeedback-001) so the done_when stops implying feedback — non-gating; a TREE-honesty
  obligation, NOT a contract gate. The sink already satisfies the literal frozen crit-10 (confirmed).

### play_check (converge-verify re-run)
- `1 recite: two propositions stated (repaired set COMPLETE; no answer leans/leaks)` (done)
- `2 attack-completeness: ORACLE-NMTL (reused, re-proposed canon) 25/25 independently re-confirmed; crit-3/9/10
  atomically split, all clauses map (crit-9 keyframe-basis = CAPTURE V2-1, non-blocking); no missed class — PASS`
  (done)
- `3 attack-smuggling: firewall PASS (HOW→PLAN; CR3 integer-discipline borderline confirmed clean; XL1
  MECHANISM-trim real); no-leaning PASS (four F1 leans now cite CR1/CR2/CR3; CR1/CR2/CR3 trace to locked/signed;
  the proposed BLOCK on the "entitled" term adjudicated DOWN — the floor is a falsifiable observable, the
  proposed fix would itself be a firewall leak); no-lock-reopen PASS (CR1/CR3 surface extensions per the LOCK's
  SHALL-re-size; XL1 leaves enum/§T12/C21 untouched; §RESOLVED-4 reads committed-only) — checked vs verbatim
  ADR-0004 §LOCK + ADR-0003 C1–C22` (done)
- `3b adjudications: (1) interest-set coverage floor GENUINELY ✓; (2) coarse-temperature per-layer discharge
  GENUINE ✓; (3) class-10 ✓ INDEPENDENTLY CONFIRMED (sink satisfies the literal frozen crit-10) — rewording is a
  forward TREE-honesty mandate, non-gating` (done)
- `4 close: PASSED CLEAN — §SIGNOFF written; 0 BLOCKs; 4 non-blocking CAPTUREs forwarded; next = c-shape-wave2
  CONSUMES the VERIFIED contracts. Not two-strikes (F1/F2 re-closed; this re-verify passes clean)` (done)

## §SIGNOFF — converge-verify

`§SIGNOFF: converge-verify passed @ 2026-06-16 (c-converge-verify-002).` The repaired §CONTRACTS set (section H
CR1/CR2/CR3 + re-scoped XL1/XL2 + §RESOLVED-4 + GG4 bounds + CS3) passes an independent fresh-session refutation
across all four axes with the three mandated adjudications resolved as GENUINE ✓ and ZERO BLOCK-severity holes.
Shape (c-shape-wave2) MAY now CONSUME the contracts as VERIFIED — copy the §CONTRACTS acceptance + the §WHAT
`acceptance` rows into the executor done_when (binding by G5) and carry the `→PLAN` rows as the PLAN-agenda, plus
the 4 CAPTUREs (esp. V2-4 = the crit-10 G9 rewording).

END_OF_FILE: live/indie-game-development/work/converge-g-9c41.md
