# NearGas L1B — frozen child acceptance

frozen: 2026-07-16
owner_verdict: `accepted`
status: owner-approved acceptance only; no product PLAN, SURFACE-FREEZE, RED or BUILD is approved by this artifact
read_by: L1B-PLAN, L1B-Capture, L1B-Classify, L1B-Trace and L1B-G5 before judging any NearGas L1B evidence

## Authority basis and current truth

- Direction basis: `NOW.md`; `history/2026-07-16-s-shape-near-gas-l1b-001.md`;
  `history/2026-07-15-s-work-near-gas-l1-experimental-close-001.md`; and
  `knowledge/g9c41-m1-integrated-proof-is-atomic.md`.
- Product basis was read first-hand from clean GasCoopGame `main == origin/main @ c4409e7b` on 2026-07-16.
  Delivered L1a `400ef8ec` is its ancestor and product contract v26 is present.
- `docs/neargas-L1-decisions.md` remains the only current L1a execution authority. It assigns L1b exactly five
  internal observation families: retry snapshot, fault injection, handler classification, kernel rows and loopback
  trace. The retired v22 prose/RED carrier is not an authority or fallback and was not used to restore a surface.
- Current actual path anchors are `NearGasSimulation.ReplaceGeneration` (private candidate, then `_current` publish)
  and `NearGasSimulation.Step`: validate generation/tick → continuous sources → mass events → impulses → reaction
  pass → sparse kernel → result construction → `CommitPreparedStep` → completed-count commit.
- L1a is `DELIVERED`; L1B is not delivered. L1B can prove internal instrumentability only. Poligon M1 still closes
  only through one integrated common scene.

The commit ids above are evidence bases, not freshness locks. Every product leg re-reads fresh product authority and
returns a checkpoint if this actual path or the five-family assignment has changed.

## Terms and one acceptance rule

**Actual L1a path** means the production `NearGasSimulation` instance reached through its public
`ReplaceGeneration`/`Step` entry points. A direct `VoxelField` call, legacy loopback, mirror model, replay, fixture-only
implementation or post-hoc reconstruction is a surrogate even when it produces the same numbers.

**Passive observer** means that with the deliberate fault stimulus disabled, observer-on and observer-off twins keep
the same exception behavior, generation current/stale relations, `AppliedTickIndex`, `CompletedStepCount`,
`FlowResult`, authoritative masses, semantic operation order and atomic commit. Observation payload never feeds back
into admission, handler choice, kernel choice, result construction or commit. Wall-clock equality is not claimed.

**Acceptance rule:** all five family positives must pass on the actual path, every planted negative must be caught,
and every surrogate, observer-effect or excluded-capability control must receive RED. One failed family means L1B
`NOT MET`; four green families cannot compensate for the fifth.

## Evaluator

The mechanical evaluator is an independent test-side oracle. It invokes production public entry points, derives
expected values independently of the observer payload, compares observer-on/off twins and emits a separate verdict
for each of the five families. `CaptureLegacyAudit` may be an auxiliary post-run comparison but cannot be the source
of retry completeness, handler invocation, kernel rows or trace provenance.

The eventual concrete carrier and product-internal access surface belong to the owner-present PLAN. They may not
weaken this acceptance or add a sixth family. Binding close remains a separate fresh Direction G5 session that reruns
first-hand evidence and tries to refute every family plus the cuts; an in-session or builder review cannot replace it.

## Five-family dependency map

| Family | Owns exactly | Depends on | Must not substitute |
|---|---|---|---|
| Retry snapshot | retry-relevant committed state across reject/retry | actual generation/tick; fault injection only as a stimulus | public count/mass or a mirror snapshot |
| Fault injection | actual semantic-site reach and operation-local selector lifecycle | real `ReplaceGeneration`/`Step` call | a harness throw or programmable global fault framework |
| Handler classification | actual invoked handler identity, kind and phase | the current generation's real reaction pass | static registration/type-map inspection |
| Kernel rows | actual side/face/bias rows in canonical kernel order | the real sparse-kernel pass | topology-derived rows, totals or direct-kernel harness |
| Loopback trace | correlation/order of the preceding four facts with result/commit | all four upstream family records on actual L1a instances | recomputing or replacing any upstream fact |

There is no cycle: loopback consumes the other four records; it never creates their truth. Fault injection stimulates
the retry failure case but does not certify retry-snapshot completeness.

## Acceptance matrix — exactly 5/5

### 1. Retry snapshot

- **Observable fact:** a deep, read-only snapshot bound to the actual current generation and expected tick contains
  every mutable value that can affect retrying the same input: generation lifecycle, completed count, authoritative
  field state and kernel-owned/pending retry state. The PLAN must inventory that closure; an omitted value is failure.
- **Falsifiable positive oracle:** on a non-trivial valid input, plant an accepted pre-commit fault after private work
  has begun. The actual snapshot immediately before the attempt equals the actual snapshot after rejection. Disable
  the operation-local fault and retry the identical owned input: exactly one Step commits and its result/state equals
  an independently run clean twin.
- **Planted-negative oracle:** corrupt or omit one retry-relevant component, and separately substitute a copied mirror
  for the post-reject actual snapshot. The evaluator must report retry-snapshot RED in both cases.
- **Evidence source:** boundary capture from the same production `NearGasSimulation` generation/tick, corroborated by
  its public read/result and the independent clean twin.
- **Forbidden inference:** unchanged public count/mass, an input clone, an FNV value or a test DTO alone does not prove
  complete retry state.

### 2. Fault injection

- **Observable fact:** the selected stable semantic site is reached exactly once inside the actual production call;
  the selector belongs to that operation and cannot persist as mutable global/runtime authority.
- **Falsifiable positive oracle:** the PLAN-frozen site inventory includes at least one replacement pre-publish site
  and one Step post-staging/pre-commit site. Selecting each site yields an exact hit record and the expected throw
  before public commit; live state stays unchanged and the next ordinary call inherits no fault.
- **Planted-negative oracle:** select a wrong/unreachable site, misreport the reached site, and separately throw the
  same exception from a wrapper before entering production. The evaluator must report fault-injection RED.
- **Evidence source:** site provenance recorded inside the real `ReplaceGeneration`/`Step` execution plus the public
  call's exception/state evidence; exception text by itself is insufficient.
- **Forbidden inference:** a harness exception does not prove the production site. Callbacks, exception factories,
  persistent controllers, mutable static switches and alternate algorithms are forbidden substitutes.

### 3. Handler classification

- **Observable fact:** the actual candidate-owned handler object that executes in the reaction pass is classified by
  generation/tick, outcome-vs-telegraph phase, kind and concrete Core type.
- **Falsifiable positive oracle:** a deterministic valid generation makes one known outcome handler and one delayed
  telegraph handler reachable while keeping another registered handler unreachable. Observation reports exactly the
  invoked objects in the correct phases/kinds and never reports the registered-but-uninvoked control; observer-on/off
  twins have identical authoritative results.
- **Planted-negative oracle:** swap outcome/telegraph phase, kind or type, and separately report every registered
  handler as if invoked. The evaluator must report handler-classification RED.
- **Evidence source:** actual invocation inside the current generation's production reaction pass, bound to its
  generation/tick, compared with a fixture-derived expectation independent of the observation.
- **Forbidden inference:** immutable handler type maps, rule registration, final mass or a reaction result do not prove
  which handler object executed.

### 4. Kernel rows

- **Observable fact:** the actual sparse pass exposes the exact rows it evaluates, including stable face/side identity,
  the bias/direction decision and canonical row order, all bound to generation/tick.
- **Falsifiable positive oracle:** an asymmetric non-trivial fixture has an independently derived non-empty exact row
  set. The production `PrepareSparseStep` observation matches it row-for-row while observer-on/off twins keep the same
  `FlowResult` and committed state.
- **Planted-negative oracle:** omit, duplicate or reorder a row, swap its side/face, or flip its bias/direction. The
  evaluator must report kernel-rows RED for every planted corruption.
- **Evidence source:** the real sparse-kernel evaluation reached by `NearGasSimulation.Step`, not a second kernel run.
- **Forbidden inference:** topology alone, final mass, aggregate transfer totals, checksum agreement or a direct
  `VoxelField` harness cannot establish which rows the actual L1a pass evaluated.

### 5. Loopback trace

- **Observable fact:** one deterministic internal trace correlates retry snapshot, fault site, handler classification,
  kernel rows, generation/tick, result and commit order from real `NearGasSimulation` instances.
- **Falsifiable positive oracle:** two fresh production instances receive the same owned definition/input scenario.
  Their traces and authoritative public results/states agree exactly, contain every expected upstream family record
  and preserve the frozen L1a order. A no-fault observer-off twin remains semantically identical.
- **Planted-negative oracle:** drop or reorder one record, bind one record to the wrong generation/tick, and plant one
  peer divergence. The evaluator must halt/report loopback-trace RED at the first mismatch.
- **Evidence source:** raw trace from public production calls plus the four upstream actual-path records; agreement is
  checked independently rather than assumed.
- **Forbidden inference:** the existing legacy `LockstepLoopback`, a direct `VoxelField` pair or a replay-only trace is
  surrogate. Internal loopback is not real network, multiplayer, gameplay, co-op or M1 evidence.

## Five-family adversarial dry-run

| Family | Actual-path positive | Surrogate control | Observer-effect control | Excluded-capability control | Required disposition |
|---|---|---|---|---|---|
| Retry snapshot | reject leaves full actual snapshot unchanged; retry equals clean twin | mirror/test DTO can mimic public values | observed retry changes result/state/order | needs C1 digest, L2 bounds or persistence | positive GREEN; every control RED |
| Fault injection | exact production site hit once; next call clean | wrapper/harness throws the same exception | selector persists or changes fault-off execution | needs global fault framework or workers | positive GREEN; every control RED |
| Handler classification | exact invoked set; registered-uninvoked absent | static map is reported as invocation | wrapper changes handler identity/order/result | needs Unity/DI-wide telemetry | positive GREEN; every control RED |
| Kernel rows | actual non-empty rows match independent asymmetric oracle | topology/direct-kernel reconstruction matches totals | reporting changes enumeration, flow or commit | needs L2/performance/general telemetry | positive GREEN; every control RED |
| Loopback trace | two actual instances agree and all four records correlate | legacy loopback/replay agrees without L1a calls | trace drives a branch or changes result/order | needs real network, Unity or common scene | positive GREEN; every control RED |

The dry-run is an acceptance-logic refutation, not delivery evidence: today the five L1b observation surfaces do not
exist. Its result is that no named false-green class can satisfy the artifact; product work must later produce first-
hand evidence and the fresh G5 must try these controls for real.

## Rollback, kill and cuts

- The owner-present PLAN must pin a fresh current-v26 product baseline (today's read-only reference is `c4409e7b`)
  and keep the L1b observation delta removable without reverting delivered L1a. On any observer-effect or gate RED,
  roll back only that L1b delta and rerun the L1a gates; never restore or execute v22.
- Kill without extension when acceptance/evidence is below 5/5, any family needs a cut capability, observation changes
  semantics/order/atomicity, fresh G5 refutes a family, three focused days are consumed, or the 2026-07-24 review fires.
  L1a remains `DELIVERED`; L1B becomes `NOT MET` with the failed family named.
- Cuts remain: no L2 resource admission/work-memory/performance ceiling; no C1 committed digest/checksum authority;
  no Unity cutover/debug UI/gameplay wiring; no workers/concurrency; no S4, Level/DA/PGG, common scene, real network or
  two-machine proof; no general telemetry/export/persistence/replay framework.

## Owner decision and routing

The owner saw the readable 5/5 brief and answered exactly `accepted`. This freezes the acceptance; it does not approve
a product PLAN or any later carrier/RED/BUILD.

Fresh concurrent Direction authority `work/gascoopgame-worktree-protocol-v2.md` requires its HELD product protocol
installer to return HOME before the first L1B product executor CALL. Therefore this session does not author, register
or launch the L1B PLAN CALL. `L1B-PLAN` stays blocked until
`c-exec-gascoopgame-worktree-protocol-v2-001` returns; only then may a fresh session derive a current-product PLAN CALL
from this frozen artifact and the post-install authority.

END_OF_FILE: live/indie-game-development/work/neargas-l1b-acceptance.md
