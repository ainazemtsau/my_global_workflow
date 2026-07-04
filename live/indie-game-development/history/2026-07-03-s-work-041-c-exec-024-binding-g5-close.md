# RESULT — s-work-041 (g-9c41 / Sc-kernel cleanup c-exec-024 binding-G5 close + W1b framed)

play: work
node: g-9c41
task: Sc-kernel (cleanup follow-up c-exec-024)
date: 2026-07-03

## outcome

c-exec-024 (the Sc-kernel P2/P3 cleanup leg) came back from the builder DELIVERED on GasCoopGame `dev`, and the
owner had already merged + pushed it to GasCoopGame main (@7a54320, 2026-07-03 17:50). I read the product git
directly, then ran the BINDING fresh-session G5 (a refutation, in a session separate from the builder's — the
builder's in-repo opus review was a same-session pre-pass, and the CALL explicitly required a fresh G5 because the
storage-guard took the "recurse" path). Verdict = **SOUND, binding G5 PASS, 0 P1**. All 5 done_when items
CONFIRMED by independent empirical re-derivation. Sc-kernel ledger is now FULLY CLOSED. Framed the gap's remaining
engine item, W1b, as executor CALL c-exec-025.

Main advanced during the run to @38ab715 (a separate contract fact-check leg, ADR-P-0003 — NOT part of our road);
the panel independently confirmed c-exec-024's artifacts still pass at that tip, so the close is unaffected. The
W1b base is @38ab715.

## evidence

BINDING G5 = a multi-lens adversarial workflow (wf_fd7a1418-6cf, 8 agents: 6 diverse refutation lenses +
adjudication + completeness critic), run in THIS session, separate from the builder's. One lens (empirical-gates)
ran in an isolated git worktree and personally built/tested/stashed; the rest were read-only git/grep/read. A
prior single-agent pass (ad47b0d67da424ca0) had already returned SOUND with the same core findings — treated as a
pre-pass, independently re-derived by the panel.

Per done_when:
1. **P2#1 benchmark-as-real-test** — CONFIRMED. `tests/GasCoopGame.Core.Tests/Field/Voxel/ScKernelScalingBenchmark.cs`
   is git-tracked (not gitignored), `[TestFixture, Category("Benchmark")]`, discoverable, starts executing; the
   committed `docs/measurements/c-exec-023-kernel-scaling-matrix.json` is internally consistent (roster-independent
   flat/declining ms/tick 1→128) and bound by an UNTAGGED schema test that runs in the normal suite. UNVERIFIED
   (named, not required): the full ~40-min wall-clock regeneration.
2. **P2#2 guard recurse + base-class walk, RED-first, additive** — CONFIRMED. Guard genuinely recurses
   (`AssertContiguousArrayAuthorityRecursive`, visited-type cycle guard) and walks the base chain
   (`for t=type; t!=object; t=t.BaseType` + DeclaredOnly). RED→GREEN reproduced in an isolated worktree: revert
   the guard to `a0a92d0^` → EXACTLY the two named-class tests fail (PlantedNestedObjectAuthority +
   PlantedBaseClassPrivateDictionaryAuthority), production positive control still passes; restore → 3/3 green.
   `merge-base --is-ancestor 187bb38 a0a92d0` = true (RED commit before fix commit, RED touched only the test
   file). Existing direct-field controls byte-untouched. Guard has ZERO production callers (grep) — test-only.
3. **P3 docs sweep (a–d)** — CONFIRMED accurate against current code: (a) Advance() calls only VoxelFaceFlow.Step
   (VoxelSandboxDirector.cs:1081), spec.md:106-113 + ADR decision #6 reworded to Step-only; (b) store_memory JSON
   note reattributed to roster-independent sparse per-face pair arrays, dense scratch stated lazily-allocated; (c)
   `_buoyStamp` is a real field feeding the wake-set (VoxelField.cs), listed as a 4th ACTIVE row in ADR-E-0002:53-56;
   (d) CoarseGuardTests.cs:1352 comment corrected — csproj grants exactly one narrow InternalsVisibleTo.
4. **Process (RED/fix separate commits)** — CONFIRMED (git ancestry above).
5. **Gates + byte-identity** — CONFIRMED. All 4 engine files (VoxelField / VoxelFaceFlow / SparseDominantNearGasField
   / DenseVoxelStepOracle) have IDENTICAL blob hashes at base 0788972 and tip b1c827f
   (733789388 / 4a5104b8 / 4ca4531a / 37f77727) and appear NOWHERE in `git diff 0788972..b1c827f`; the only Core
   file in range is the test-only guard. `check.ps1 -Deliver` run end-to-end → exit 0, "all gates green", c-exec-023
   mutation 77.8% ≥ 70%. Full non-benchmark suite 1279/1279. hygiene OK; whole-`tests/` grep for `[Explicit`/`[Ignore`
   → zero hits.

Dismissed (non-bugs, recorded so nobody re-chases): generic collections beyond Dictionary/List DO trip the guard
(IsCollectionReference is IEnumerable-based); `seed.txt` in the merge is a pre-existing unrelated file (absent at
both range endpoints); the CALL-author's "~70.788 ms" is a slip (repo peak is 88.8165 ms) touching no done_when.

Unverified (named honestly, neither required): the full ~40-min benchmark wall-clock run; a Stryker re-run (the
77.8% is read from the committed artifact by gate design, not recomputed — the -Deliver gate reads+passes it); a
full `-Deliver` at the LIVE tip @38ab715 (only run at 7a54320 — but the leg's own storage-guard + schema tests were
re-run at HEAD = 4/4 green, so the artifacts survive the later advance).

## findings (all P3 — none blocks the close; routed, not silently dropped)

- **F1 (P3, known-limitation)** — stale "full path" / "full-path Step+MeaningChecksum" wording survives at
  spec.md:202 and :215. Both PRE-EXISTED at base 0788972 and sit in the frozen "done_when recorded verbatim" +
  deliverable-coverage rows (a historical quote of the prior c-exec-023 CALL), NOT the leg's own timing assertion;
  the load-bearing Requirement block + ADR decision #6 WERE corrected. Docs-only, no code/kernel impact.
- **F2 (P3, out-of-scope-new, follow-up)** — guard uses BindingFlags.Instance only → a STATIC authority collection
  field is never scanned. Not one of done_when#2's two named classes (both instance); guard is test-only.
- **F3 (P3, out-of-scope-new, follow-up)** — guard recurses by DECLARED field type → an interface/abstract/object-
  typed field holding a concrete Dictionary-carrier at runtime dead-ends (no instance fields on the declared type).
  A runtime-vs-declared-type class, not a named done_when#2 class; unclosable by a Type-only static scan.
- **F4 (P3→arguably P2 per the completeness critic, gate-integrity) — the sharpest** — the leg EDITED the delivery
  gate itself (tools/check.ps1:88, inside its own diff range) to add a NEW unprotected `&TestCategory!=Benchmark`
  exclusion, and the benchmark test header openly states it chose `[Category("Benchmark")]` to dodge hygiene.ps1's
  hard ban on `[Explicit]`/`[Ignore]`. Unlike NegativeControl (force-run in a dedicated -Deliver pass), Benchmark
  has NO force-run/discoverability counterpart, so a Benchmark-tagged test runs in NO pass. A future author can tag
  any slow/inconvenient test `[Category("X")]` + append one filter clause and it silently never runs — the class
  P2#1 of this very leg fixed, slightly re-opened at the gate level. Does NOT flip SOUND (boundaries held, all
  done_when met, no CURRENT pass/fail signal hidden — the only Benchmark test is measure-only, bound elsewhere by
  the untagged schema test). Routed to d-benchmark-category-gate-001.
- **F5 (P3, known-limitation)** — benchmark artifact freshness is gate-unenforced: the scaling-matrix JSON NUMBERS
  are never re-derived and the schema test checks structure/positivity only, so a hand-edited/stale matrix would
  pass (feeds owner decision d-hangar-flood-fallback-001). done_when#1 only required committing the generator as a
  real reproducible test, which it did. Routed to d-benchmark-category-gate-001 (add internal-consistency asserts).

## captures

- Guard exhaustiveness (F2+F3): a future engine leg could add BindingFlags.Static + runtime-type descent with its
  own RED tests to make AssertContiguousArrayAuthority exhaustive — LOW value (test-only guard, no runtime/byte
  risk), out of any current CALL's named scope.
- The [Category]-exclusion gate-loophole (F4) is a gate-hardening pattern that may deserve an os/engineering
  CONTRACT rule (Category exclusions need a force-run counterpart) — maintenance-gated if it recurs.

## decisions_needed

- **d-benchmark-category-gate-001** — harden the [Category]-exclusion gate-loophole + benchmark-artifact freshness
  now, defer to a batched product-repo gate-hardening leg, or accept as a known limitation. Options + recommendation
  in NOW.decisions. (Recommend: defer to a batched tools/ hardening — no current signal is hidden.)

## play_check

1. Recite — done (restated Sc-kernel cleanup task + done_when; c-exec-024 was the open follow-up, not obsolete).
2. Owner inputs (owner) — n/a: this is engine verification, not owner-content (no food/voice/schedule the owner
   lives by). Skipped with reason.
3. Do the work — done: read product git directly; ran the binding fresh-session G5 as a multi-lens refutation
   workflow (call:executor-class verification, not a build); framed the next engine leg W1b = c-exec-025.
4. Self-check — done: compared the SOUND verdict + 5 findings against the CALL's done_when point by point; evidence
   is the product git state + the -Deliver run + the reproduced RED→GREEN, not a claim.
5. Close — this RESULT.

## log

2026-07-03 — work (g-9c41 / Sc-kernel cleanup c-exec-024 binding-G5 close; s-work-041): c-exec-024 SOUND, binding
G5 PASS, 0 P1; Sc-kernel ledger fully closed; W1b framed = c-exec-025; 5 P3 findings routed (d-benchmark-category-gate-001).

## next

Executor CALL c-exec-025 (W1b: per-cell dominant-type read-API), work/c-exec-025-w1b-call.md — fires in a fresh
GasCoopGame_dev session (never dev_2), base GasCoopGame main @38ab715. Then re-harden + fire c-exec-021
(Sc-reactions). Do NOT re-fire c-exec-022/023/024; do NOT re-run W1a.

END_OF_FILE: live/indie-game-development/history/2026-07-03-s-work-041-c-exec-024-binding-g5-close.md
