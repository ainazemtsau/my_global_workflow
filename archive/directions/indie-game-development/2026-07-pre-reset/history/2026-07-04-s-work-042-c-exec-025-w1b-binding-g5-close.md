# RESULT — s-work-042 (g-9c41 / W1b c-exec-025 binding-G5 close + emergent c-026/c-027 sweep)

play: work
node: g-9c41
task: (gap-filler mini-CALL c-exec-025 — not a bet task; open_calls close)
date: 2026-07-04

## outcome

The builder handed back c-exec-025 (W1b — the per-cell dominant-type read seam) DELIVERED + MERGED + PUSHED
(GasCoopGame `origin/main` @e0e4f5a, contract v14), `dev == main`. I read the product git directly (not the
handback's word) and ran the BINDING fresh-session G5 — a refutation, in a session separate from the builder's
review. The handback under-described the window: THREE clusters landed on main since the W1b base @38ab715 —
c-exec-025 (W1b), **c-exec-026** (§Re-sync of the os/engineering contract v11→v14, ADR-P-0004, @a08860e — the
handback did not name it) and c-exec-027 ×2 (two emergent PRE-EXISTING P1s the c-025 owner-review surfaced OUTSIDE
the c-025 diff, fixed in child sessions and merged autonomously in the product repo). c-026 and c-027 had had NO
direction-side G5; this session is their first independent scrutiny.

**Verdict = SOUND, 0 P1, 0 P2, 2 P3-defer.** The Sc-kernel→Sc-reactions GAP is now CLEAR. c-exec-025 closes; the
road resumes at c-exec-021 (Sc-reactions), pending one small sequencing decision (a tools/ hardening leg first?).

## evidence

BINDING G5 = a multi-lens adversarial workflow (wf_44257b08-dfe, 11 agents: 8 refutation lenses planned +
adjudication + completeness critic). 5 lenses reported; the 3 W1b-core lenses (byte-identity / encapsulation /
correctness) died on StructuredOutput conformance, so this session re-derived those three claims FIRST-HAND rather
than trust the builder — recorded below. This is stated honestly per the completeness critic (verdict
SOUND-WITH-CAVEATS; the one material caveat — no independent full-solution suite run — is mitigated: the builder's
`check.ps1 -Deliver` is committed GREEN and I re-derived the load-bearing subsets).

Per c-exec-025 done_when:
1. **Read-only accessor + sentinel + encapsulation-safe** — CONFIRMED first-hand. `DominantTypeIdOrEmpty(cell)`
   returns `int` (dominant TypeId ≥0, or `NoDominantTypeId` = -1 = `SparseDominantCellRecord.EmptyType`, outside
   TypeId's legal domain — `TypeId(-1)` never constructed); `TryGetDominantTypeId(cell, out TypeId)` returns
   `bool` + a value-type `TypeId`. `TypeId` is a `readonly struct`, `SparseDominantCellRecord` a `struct` returned
   BY VALUE; `VoxelField` delegates to the PRIVATE `_near` store which never escapes. No array/store handle leaks.
   (SparseDominantNearGasField.cs:229-262, VoxelField.cs:435-461, TypeId.cs:6, SparseDominantCellRecord.cs:7.)
2. **Correct dominant + independent RED-first** — CONFIRMED. RED-first VERIFIED by lens w1b-red-first: test-only
   commit `390dbad` ("independent RED acceptance + negative-control tests (spec-only)") is a strict git ancestor of
   build-to-green `e517388`; the accessors did not exist at 390dbad → the tests could not compile at RED (compile-
   failure = the strongest red). Full-domain sentinel VERIFIED first-hand: the near store is sized to the FULL cell
   domain (`_slotByCell = new int[cellCount]`, `cellCount = dense.CellCount`, all init -1; `CheckCell` bounds on
   `_cellCount`), so a valid in-domain empty cell hits `slot<0 → NoDominantTypeId` — the throw-instead-of-sentinel
   hole I probed for DOES NOT EXIST (VoxelField's `_grid.CellCount` bound and near's `CheckCell` cover the same
   domain). EMPIRICAL: `dotnet test --filter DominantRead|Atomicity` → **48 passed, 0 failed, 141 ms** at @e0e4f5a.
3. **Byte-identity** — CONFIRMED first-hand. `git diff --name-only 38ab715 e0e4f5a`: NO golden/fixture/blob/baseline
   changed (the only `.json` are `docs/measurements/mutation-*.json` — score artifacts); NO tick-authority file
   (SparseStep/Kernel/Step) touched. The two accessor sites are purely additive read methods (no write path).
4. **-Deliver GREEN + fresh G5 + owner-eye** — -Deliver committed GREEN (RESULT.md land-consolidation; prior
   1279/1279). This RESULT is the fresh-session G5. Owner-eye: the merge was already owner-gated in the product
   session (handback: MERGED + PUSHED).
5. **§Re-sync stamped** — the repo advanced v11→v14 via c-exec-026 (below); W1b rode onto v14. Confirmed
   `synced_contract_version 14` in validation.config.

Emergent legs (independently re-verified by the G5, 0 P1/P2):
- **c-exec-026 §Re-sync v11→v14** (lens c026-resync-completeness, refuted=false): all three new gates
  (v12 property-layer in coverage-check.ps1; v13 refuted-register-check.ps1 + escape-class walk; v14
  fix-class-check.ps1) are absorbed AND actually INVOKED by check.ps1 -Deliver, each with a seeded-miss self-test
  the lens EXECUTED and confirmed fails-on-bad-fixture (not present-but-inert). The one real bug — v14 gate a
  production no-op via a `$null`-coerced param — was caught by the builder's OWN G5 and fixed @e1bbf9d BEFORE the
  merge, so it does not survive at head. `synced_contract_version` = 14 (validation.config, its canonical home).
- **c-exec-027 topology-overflow-guard (ADR-E-0004)** (lens c027-topology-overflow, refuted=false): the base
  `TopologyConformance.Check` inclusive-max guard is arithmetically correct (long-widened, `>= int.MaxValue`, no
  off-by-one, ordered before the derive/overlap consumers); an independent whole-Core sweep found no unguarded
  sibling inclusive-max site; 17 acceptance + 4 negative-control tests pass.
- **c-exec-027 throw-atomicity (ADR-E-0005)** (lens c027-throw-atomicity): the 3-site stage-locals/commit-after-
  success fix is CORRECT and the 4th sibling (MaterializeDue) throw is provably unreachable. Adjudicated finding
  below.

## findings (2 × P3-defer — neither a live defect)

- **P3-a (topology doc nit, defer)**: review-c-exec-027-topology-overflow #8 calls `RectDecomposition.GridRect`
  "long-safe" while DF-1 (secondary) calls it "unchecked int arithmetic". GridRect is DEAD code (zero `.Width/
  .Height/.Area` consumers in Core), honestly deferred → fold into the DF-1 leg when it wakes. Does not weaken the
  fix-class closure.
- **P3-b (v14 gate satisfied by archiving, not by a sweep — defer + capture for maintenance)**: the v14
  fix-class-closure gate — the mechanism built specifically for the owner's "review loops every task" pain — was
  satisfied for the throw-atomicity leg by ARCHIVING the change out of the gate's walk scope (the owner-decided
  "v12–v14 apply to new work, v11-built work is exempt by archiving" path), NOT by a recorded machine-checkable
  `sweep:` line. `fix-class-check.ps1 -ChangeId` exits 1 on the review file; `grep -c sweep` = 0. Inert NOW (the
  4th sibling's throw is unreachable), but the archive-on-land move silently voids the reopen-tripwire for a class
  with a live DEFERRED sibling. The very first real exercise of the v14 gate was bypassed by the exemption — a
  signal about the mechanism, not a product defect. Routed to `captures` (maintenance/FRICTION candidate; ties
  d-benchmark-category-gate-001 option 3 and the handback-underspecified FRICTION already parked @4a08767).

## state_changes

- NOW.md header: `updated: 2026-07-04 by s-work-042`.
- NOW.md `bet.current_truth`: rewritten — W1b + c-026 + c-027×2 MERGED (@e0e4f5a, v14); Sc-kernel→Sc-reactions GAP
  CLEAR; binding-G5 SOUND (s-work-042, wf_44257b08-dfe), 0 P1/P2, 2 P3-defer; route-home backlog (DF-1/DF-2/
  task_441a3b58) recorded; next = re-harden + fire c-exec-021 pending d-nextcall-tooling-vs-c021-001.
- NOW.md `next_slices` bullet 1: W1b FRAMED → DELIVERED+MERGED, gap CLEAR, c-exec-021 next.
- NOW.md `open_calls`: c-exec-025 open block removed → closed-comment cluster added for c-025 / c-026 / c-027-topology
  / c-027-throw (delivered+merged, binding-G5 SOUND). c-visual-004 + c-exec-021 unchanged.
- NOW.md `decisions`: d-benchmark-category-gate-001 status note folds DF-2 as converging evidence (every leg hit it →
  the tools/ leg is overdue); NEW d-nextcall-tooling-vs-c021-001 (sequencing).
- NOW.md `history_pointers`: + this session.
- NOW.md `next`: rewritten (gap clear; road = c-exec-021; recommend tools/ leg first; latent DF-1/task_441a3b58 with
  wake triggers).
- LOG.md: append s-work-042 line.
- No TREE/CHARTER change (G9 n/a). No bet task marked done (W1b is a gap-filler mini-CALL, not a t-N task) → the
  writer-G10 "last task done → review CALL" lifecycle does not apply. G1 intact (one active bet; ≤3 active tasks).

## captures

- v14 fix-class-closure gate can be voided by archive-on-land exemption when a fixed class has a live DEFERRED
  sibling (the reopen-tripwire never fires) — maintenance/FRICTION candidate; ties d-benchmark-category-gate-001
  opt.3 + FRICTION @4a08767. Do NOT act inline.
- c-exec-026 CALL file trailer says `c-exec-026-resync-v12-v13-call.md` but the file is `...-v12-v13-v14-call.md`
  (END_OF_FILE mismatch) — a writer nit to fix on the next touch of that file.

## decisions_needed

- id: d-nextcall-tooling-vs-c021-001
  q: |
    The Sc-kernel→Sc-reactions gap is clear; the road's pre-agreed next is c-exec-021 (Sc-reactions). But DF-2
    (tools/mutation.ps1 [Category("Benchmark")] poisons Stryker) hit EVERY mutation leg so far (~30-min manual
    relocate/restore workaround each time), and c-exec-021 will run mutation too. DF-2 shares the exact
    [Category("Benchmark")] surface as the already-open d-benchmark-category-gate-001. Slot a small tools/
    hardening leg first, or fire c-exec-021 now?
  options:
    - Tools/ hardening leg FIRST (fold DF-2 + d-benchmark-category-gate-001: give [Category] exclusions a force-run
      counterpart + add scaling-matrix consistency asserts). Bad-because: delays the feature road ~half a day.
      [recommended — small, self-contained, overdue (every leg hit it), clears the tax before c-021's mutation gate].
    - Fire c-exec-021 NOW, tools/ leg batched later. Bad-because: c-021's mutation gate hits the Stryker poison →
      the manual workaround + a transient dirty-tree window again.
    - Fire c-021 now, fold DF-2 into c-021's own tooling touch. Bad-because: mixes an infra fix into a feature leg
      (scope creep, muddied diff).
  recommendation: |
    Option 1. DF-2 is small, self-contained, and overdue — every mutation leg has paid the ~30-min tax, and c-021
    is another mutation-heavy leg. Folding d-benchmark-category-gate-001 into the same tools/ pass closes the whole
    [Category("Benchmark")] surface at once. DF-1 (P1-latent, no caller) and task_441a3b58 (unreachable) stay
    tracked-deferred with wake triggers, NOT in this leg.
- (still pending, unchanged) d-marketing-wake-001; d-coop-interdependence-repin-001.

## play_check

- 1 OPEN / reconcile: done — read product git directly; main=origin/main=@e0e4f5a (v14), dev==main; found the c-026
  §Re-sync + c-027×2 clusters the handback under-described; found the c-026-open_calls drift.
- 2 binding G5: done — wf_44257b08-dfe (8 lenses + adjudication + critic); 3 W1b-core lenses died on output-
  conformance → re-derived first-hand (byte-identity / encapsulation / full-domain sentinel / 48 tests green).
  Verdict SOUND, 0 P1, 0 P2, 2 P3-defer.
- 3 absorb / state_changes: done — see state_changes (open_calls close, current_truth, next_slices, decisions,
  history_pointers, next; LOG line).
- 4 CLOSE: done — RESULT emitted as final message; sequencing decision surfaced as a Russian brief; then writer-apply
  + commit (this repo, agent-CLI self-writer after RESULT). OS commit LOCAL; push owner-gated.

log: work c-exec-025: W1b read-seam binding-G5 SOUND (s-work-042, 0 P1/P2, 2 P3-defer); c-026 §Re-sync v11→v14 + c-027×2 re-verified SOUND; Sc-kernel→Sc-reactions gap CLEAR; next=c-exec-021 pending tools/-leg sequencing

next: |
  awaiting_decision d-nextcall-tooling-vs-c021-001. Default road (if the owner picks "fire c-021"): re-harden
  c-exec-021 (Sc-reactions) — run its §Re-sync sweep (repo now at v14, NOT v11 — the CALL body's base assumption
  is stale) + full fire-time re-hardening, fill §PENDING from the Sc-kernel/W1b RESULTs, then fire in a fresh
  GasCoopGame_dev session (owner-present PLAN). If "tools/ leg first": a small GasCoopGame tools/ hardening CALL
  folding DF-2 + d-benchmark-category-gate-001, then c-exec-021. Do NOT re-fire c-022/023/024/025/026/027; do NOT
  re-run W1a. CALENDAR: July demo-road shape 2026-07-10..15 (d-demo-road-001).

END_OF_FILE: live/indie-game-development/history/2026-07-04-s-work-042-c-exec-025-w1b-binding-g5-close.md
