# CALL c-exec-021 — CONTINUATION (reaction-engine completion): finish leg 1 → leg 2

**STATUS: READY TO FIRE — a re-planning continuation of c-exec-021, authored 2026-07-06 (s-work-057) after the
executor checkpoint returned. Owner directive "D+A" (2026-07-06, recorded in dev commit `0de6cbe`): the completed
groundwork is committed on `dev` (NOT merged, owner-gated); the reaction-ENGINE completion goes to THIS separate
re-planning session. Phase = a SHORT owner-present PLAN (the enumerated open decisions ONLY — the frozen
`work/c-exec-021-call.md` spec + the executor's `openspec/changes/c-exec-021-sc-reactions/` PLAN.md + ADR-E-0006
STAND, not re-opened), then EXECUTE leg-1-finish (the 10 RED → GREEN) → leg 2.**

## Base / where the leg is (verified FIRST-HAND 2026-07-06, s-work-057)

- **Base = GasCoopGame `dev @0a95f01`** (two c-021 commits on `main @26dd062`, contract v18; `main` has since moved
  to `0dd823b`, a docs-only commit — confirm at the §Re-sync). **NOT merged** (owner-gated).
- **DONE + verified** (4-agent adversarial pass over the real `dev` code, wf_f85e9ed7-786):
  - Owner-present PLAN 2026-07-06 (Q1–Q4 ratified) + ADR-E-0006 + frozen spec/proposal/tasks authored.
  - The reaction ENGINE core is BUILT and its **central obligation holds — CONFIRMED**: reactions resolve through a
    GENERIC data-index keyed by a canonical `ReactantKey` (sorted+deduped, `Of(A,B)==Of(B,A)`), branching only on an
    int rule-Tier; outcomes dispatch through a generic `Dictionary<int,IReactionOutcomeHandler>` registry. **ZERO
    type-pair dispatch** (no switch/enum, no `(int,int)`-keyed dict, no `[,]`-by-TypeId) anywhere on the reaction
    surface. The `NEW-TYPE-IS-DATA` / `NEW-OUTCOME-IS-DATA` anti-cheat REDs are genuine (independent test-author,
    builder-immutable, RED-before-build). Approach token `data-driven-reaction-rules-telegraph-then-bang` is honest
    (the TELEGRAPH DELAY is data-plumbed only — leg-2 behaviour, as the split intends).
  - Independent RED battery in place (Firing / NewType / NewOutcome / Handshake / Mass / OverflowJunction /
    ByteIdentity / Determinism / NegativeControl / Property / fixtures + `ReactionAssertions`).
  - KIT groundwork: `SeedMass/Mass` → registered-TypeId-addressed (new `GasTypeRegistry.TryIndexOf`; positional folds
    preserved via `MassByIndex`); `LockstepLoopback` seeds via `TypeIdAt`; ~60 call-sites across 15 test files;
    `SingleRoom(extentZ:1)` → a sealed 1×1×1 cell.
  - **Non-reaction suite 1343/1343 GREEN; the 13-entry byte-identity KILL goldens are BYTE-IDENTICAL** (constants
    unchanged `26dd062`→`0a95f01`; the edits are the SAFE call-site-rewrite class, NOT a rebaseline). No STOP-class
    rebaseline anywhere in the diff.
- **RED = exactly 10 reaction tests** (all under `tests/GasCoopGame.Core.Tests/Field/Reactions/`). leg-1 EXEC is
  genuinely in progress — the admission clamp, the throw-demotion, the config-K path, and the skip-zero widened fold
  are NOT built yet; the REDs are correct RED-before-build.

## The 10 RED — CORRECTED disposition (the checkpoint prose was imprecise in two places; corrections verified first-hand)

### A. PLAN decisions (owner-present, SMALL — this is the "re-planning" scope)

1. **Single-cell N-type overflow — `NTypeJunction(5)`, `NTypeJunction(8)`.** The store is K=4 (`SparseDominantCellRecord`
   = 1 dominant + 3 overlay, `MaxPositiveTypes=4`). **Correction:** the multi-cell `AdmissionClamp` test and the
   zone-level junction assertions only demand *no-throw + conservation* — an ADMISSION CLAMP satisfies them with K=4
   UNCHANGED (spec §7 explicitly allows "degrades by the signed mass-conserving policy"). **Only the `SingleCellGrid`
   `NTypeJunction(5/8)` genuinely forces >4 mass into ONE cell with no neighbour** — and there the CURRENT failure is a
   **SEED-time throw** (`SeedMass`→`AddMassByType`→`AddMassOrThrow`→`SparseDominantCellRecord.AddMass`, throw at
   `SparseDominantCellRecord.cs:142`), before `Step` runs. DECIDE for the single-cell case:
   - **(i) RECOMMENDED — widen per-cell K via CONFIG** to hold N=8 (record ~8→12 ints). This is what done_when #8
     ("K raise = data-only RED") + ADR-E-0006 §7 already lean toward; the `KRaise_IsDataOnly` test exists precisely to
     prove it. **Mandatory partner = decision 2 (skip-zero fold).**
   - (ii) FALLBACK — a same-cell signed mass-conserving overflow policy (keep K small; adds a merge law + a
     believability question), IF widening K objects against the weak-hardware record-size ceiling
     (d-hangar-flood-fallback-001 / SPEC §6 п.2).
2. **Skip-zero widened fold — the byte-identity STOP-guard (confirm, do not "choose").** `MeaningChecksum` today folds
   a FIXED 4 TypeId + 4 Amount lanes per active cell UNCONDITIONALLY (`SparseDominantNearGasField.cs:301-320`) and folds
   `_speciesCount` (`:298`). If K is widened, the widened fold **MUST skip the new empty lanes** so the frozen 13-entry
   golden stays BYTE-IDENTICAL. **REGENERATING / REBASELINING A COMMITTED GOLDEN = STOP-escalate** (frozen CALL §per-tick
   checksum; the golden files carry "REBASELINING IS FORBIDDEN"). Owner confirms skip-zero, never a rebaseline.
3. **`SeedMass` public-contract nod.** Demoting the loud throw to a non-flow invariant assert (ADR §7) means `SeedMass`
   becomes **non-throwing (clamp) on a full cell** on the flow/seed paths (`CanAccept`-gated, `SparseDominantCellRecord.cs:67-78`,
   today only wired into `TryAddMass`, NOT the seed/reaction path). That is a public-contract behaviour change — owner nod.
   The loud assert stays for non-flow direct-API abuse (done_when #8: planted direct-API abuse still trips the demoted assert).

### B. Test-author owner-acks (the "A" cluster — capture the `owner-ack:esc-…` token owner-present at the PLAN; do NOT fabricate)

4. **finding-4 — `ProductOverMaxCellMass`, `FifthCoResidentType_ExceedingLaneCap`.** Both use
   `Assert.Throws<System.Exception>`, which NUnit 3.14 matches by EXACT type; the engine throws the *derived*
   `ArgumentOutOfRangeException` (`:84`) / `InvalidOperationException` (`:142`) — **correct per spec** (spec pins no
   exception type). Fix (test-author): `Assert.Catch<Exception>` (loosest) or pin the derived type. Engine is right.
5. **finding-5 — `FullConsumeToZero_LeavesNoStaleTypeId` — RECLASSIFIED: this is NOT an engine bug.** ⚠ The checkpoint's
   "stale-TypeId / wider-record engine bug" label is **REFUTED first-hand** (the pass ran it live): the post-reaction
   record is BYTE-IDENTICAL to a fresh product-only record (no stale TypeId), mass conserved to the bit. The ONLY
   divergent checksum member is TypeId, driven by `registry.ContentHash()`. Root cause = the TEST builds its "equivalent"
   `freshField` with `TwoReactantRegistry(threshold:100)` while the reacted field uses `threshold:1` → different rule
   threshold → different ContentHash → legitimate divergence. Rebuilding `freshField` at `threshold:1` makes the two
   checksums EXACTLY equal. **DO NOT let the builder hunt a phantom mass-leak.** Fix (test-author): match the fresh
   field's registry threshold to the reacted field's (or derive it from the reacted field's own registry). The existing
   token `owner-ack:esc-c-exec-021-fullconsume-test-assertion-2026-07-06` covered the *reacted-field* edit — confirm it
   extends to the `freshField` registry edit or mint a one-line extension (the test file is builder-immutable).
6. **finding-6 (NEW — the checkpoint missed it) — `KRaise_IsDataOnly` test-design.** As written it compares roster-2 vs
   roster-12, and `_speciesCount` (2 vs 12) is folded into the checksum → it CONFLATES per-cell-K identity with roster
   width and would fail on the speciesCount axis regardless of the lane skip-zero. Re-shape (test-author): hold roster
   width CONSTANT while raising per-cell K, so the test isolates the K-is-data claim.

### C. Straight EXECUTE — already decided in ADR-E-0006 §7, no owner input needed (finish leg 1)

7. **Build the admission clamp** (slot-then-lane via the existing `CanAccept` predicate; clamp-denied mass stays in
   source, conserved, no throw on flow/seed, canonical order) → greens `AdmissionClamp_GatesSlotFirst…`,
   `GrenadeSeedBloom_…CanonicalOrder`, `MultiActorJunctionOneTick`.
8. **Demote the loud throw** to a non-flow invariant assert (per decision 3).
9. **`ThrowAtomicityAllExitPaths`** — atomic (field byte-unchanged) across ALL exit paths (seed / clamp / reaction).

### D. Scan-scope gap (done_when #3 — surfaced by the verification, not in the checkpoint)

10. The `type-hardcode-scan.ps1` roots ONLY on `Core/Field/Types` (covers the RESOLVER `Types/Reactions/*`) but NOT
    `Core/Field/Voxel/Reactions` (the ENGINE — `ReactionEngine.cs`, `VoxelField.Reactions.cs`). The engine half's
    no-pair-dispatch property rests on tests + review, NOT the mechanical scan. done_when #3 requires the mechanical
    falsifier to cover the reaction code's ACTUAL location → **extend the scan** with a `Voxel/Reactions`-scoped root or
    whitelist variant **+ a planted-violation self-test** (Voxel can NOT be blind-appended — `VoxelKernelDefect` enum at
    `VoxelFaceFlow.cs:123` would false-positive), OR correct the scan's honesty header to state the engine half is
    test/review-covered (the c-020 honesty-note precedent). The frozen far-tier stays outside the scan.

## Then — leg 2 (unchanged from the frozen CALL / PLAN.md split)

STORED telegraph (`MeaningMembers.Telegraph = 1<<6`, SKIP-ZERO, cell-keyed, ISOLATION + DISTINCTNESS REDs) + the
chain one-tick oracle + the `PressureShove` outcome (rides `EmitImpulse`, canonical order, validate-all-atomic,
Strength/Ttl bounded so combined `desiredMove` settles — carry the c-020 over-strength settle RED) + the owner-eye
scenes. The wave branch stays DEFERRED (substrate absent — ADR-E-0006, `owner-ack:c-exec-021-wave-fork-deferred…`).
The `ReactionLayer` delete stays DEFERRED (Wave-2 LOCK, owner Q2, `owner-ack:c-exec-021-reactionlayer-delete-deferred…`).

### Owner design input (2026-07-06) — the telegraph is an EXTENSIBLE "unstable window", NOT a hardcoded blink

Owner directive for the leg-2 telegraph shape (recorded here so the fire-time PLAN builds it extensible, not a
single hardcoded "blink"). Owner words (meaning verbatim): the warning is «нестабильное короткое состояние, окно»
before something happens — «разные должны типа быть, для этого разные обработчики, разное визуально»; «не
захардкоджено, что он должен просто мигать … это мы потом можем любые туда добавить». Requirement:

1. **The "unstable window" is a per-cell PENDING STATE that is data-driven + extensible — the same pattern already
   proven for the OUTCOME registry (kind id → handler, zero core branches).** A new kind of warning is added later as
   DATA + its own handler — the engine carries the state; it does NOT hardcode "blink". Different reactions →
   different pending kinds → different look.
2. **The LOOK (blink / fade-out / glow / …) lives on the VISUAL track (g-7e15), reading the per-cell pending state —
   near-free on the engine.** The engine's job is only to expose, deterministically, "cell X has reaction R pending,
   phase P, T ticks left"; the visual layer maps `(kind, phase) → a look`. So "warnings look different" costs the
   engine ~nothing beyond storing the state.
3. **Reserve a BOUNDED multi-phase slot** (owner's two-stage idea: two gases blink → players add a third gas that
   "calms" it → maybe blink → fade → …). The "add a third gas to calm it" is just ANOTHER reaction rule that mutates
   the pending state — conceptually free (it IS the reaction mechanism). Multi-phase = a small bounded PHASE field in
   the pending state + a per-rule phase table (DATA).
4. **Owner perf gate (his exact constraint):** BUILD the minimal version now (one phase = the basic pending window +
   the extensible seam) and add richer/multi-phase behaviour later **as DATA — ONLY if it stays near-free** («если
   практически бесплатно … можно; если стоит хоть каких-то ресурсов — не надо, ограничение примем»). The real cost is
   NOT CPU — it is (a) determinism (the pending/phase state rides the lockstep checksum → must be SKIP-ZERO, cell-keyed,
   so an idle scene stays byte-identical) and (b) design/test/believability combinatorics (phases × reactions). So the
   phase count stays a small bounded int; unbounded phase chains are a STOP.
5. **The leg-2 PLAN decides + records (owner-present):** what the per-cell pending state carries (pending-kind ref +
   bounded phase + countdown), the extension seam (a `pending-kind → handler` registry mirroring the outcome
   registry, or a note why the outcome registry itself absorbs it), which look(s) the visual track reads, and the
   honest near-free perf verdict per (4). Minimal-now / extensible-slot / richer-as-data-later.

## done_when

Unchanged — the frozen `work/c-exec-021-call.md` §done_when battery #2–#13 (this continuation adds NO new done_when;
it FINISHES the ones the 10 RED tests already encode). Concretely for the fire session: the §Re-sync CONFIRM at the
`dev @0a95f01` tip → the SHORT owner-present PLAN resolving decisions 1–3 + capturing the acks 4–6 with real
`owner-ack:esc-…` tokens → EXECUTE 7–10 + leg 2 → **all 10 reaction REDs GREEN, the 13-entry golden still byte-identical**
→ `check.ps1 -Deliver` GREEN (build + headless + zero-float + int-overflow + type-hardcode incl. the extended engine root
+ mutation ≥70 on the new Core + spec-silence + deliverable-coverage + negative-control + property + review-evidence) →
independent review (different model family) + fresh-session binding G5 COULD-NOT-REFUTE → `docs/results/c-exec-021.md`
DELIVERED, routed HOME. dev→main merge/push OWNER-GATED.

## boundaries (carried from the frozen CALL) + one reinforced STOP

Everything in `work/c-exec-021-call.md` §boundaries holds (no type-set hardcode dispatch; no same-tick cascade / no
overflow telegraph-bypass; no temperature/damage/body/wall; no env-typing mechanism; no cross-type mass-capacity change;
no visual hookup; no GridEvent bus/enum edit; no frozen far-tier touch; no float; no dense-planes revert; ADR-0002 not
reopened). **REINFORCED:** if decision 1 lands on widening K, the widened MeaningChecksum fold MUST keep the frozen
13-entry golden byte-identical via SKIP-ZERO — **any path that would REBASELINE a committed golden is a mandatory STOP +
escalate**, never a builder default.

## return

A RESULT routed HOME (the OS owns the next CALL): outcome + evidence (the 10-RED→GREEN transcript, `-Deliver`
transcript, mutation json, review + G5 verdicts, the 3 PLAN decisions recorded, the 3 test-author `owner-ack:esc-…`
tokens, the extended type-hardcode scan evidence, leg-2 telegraph/shove REDs, owner-eye verdicts with TIER-ladder
routing) + findings for the planner. dev→main merge + push OWNER-GATED. On GREEN → the road rolls to **Sc-typing**
(then Sc-damage).

## budget

The continuation of an already-split trip: leg-1-FINISH (decisions 1–3 + acks 4–6 + EXECUTE 7–10 — the 10 RED → GREEN)
then leg 2 (telegraph SM + shove + owner-eye). Keep the PLAN SHORT — the frozen spec/ADR stand; the PLAN only resolves
the enumerated open items. Do NOT bundle the STORED telegraph member + the full handshake fold + the multi-tick chain
oracle into one blob (frozen CALL §budget — mandatory split holds). Test-types scope stays tight.

END_OF_FILE: live/indie-game-development/work/c-exec-021-continuation-call.md
