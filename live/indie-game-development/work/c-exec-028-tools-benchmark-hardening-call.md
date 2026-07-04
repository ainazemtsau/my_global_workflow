CALL c-exec-028
to: executor
kind: engineering
direction: indie-game-development
node: g-9c41
repo: C:\projects\Unity\GasCoopGame_dev
surface: cli
goal: |
  GasCoopGame's tooling can no longer be silently POISONED or silently BYPASSED by a [Category]-tagged
  test. Two closed holes, strictly ADDITIVE (no existing green gate weakened; every currently-delivered
  leg still delivers):
  (1) DF-2 — tools/mutation.ps1 no longer runs the [Category("Benchmark")] wall-clock fixture on its
      Stryker passes (today it stalls EVERY mutation leg ~30 min); the exclusion is self-contained — no
      manual step, no PERSISTENT dirty-tree window, crash-safe restore.
  (2) d-benchmark-category-gate-001 — a [Category]-EXCLUDED test can no longer silently never-run in ANY
      gate: the Benchmark category gains a force-DISCOVER counterpart (category-AWARE, non-executing),
      AND the committed scaling-matrix artifact is pinned by internal-consistency asserts so a stale /
      hand-edited matrix FAILS.

context: |
  - Owner picked "tools/ leg first" 2026-07-04 (NOW.decisions d-nextcall-tooling-vs-c021-001, option 1),
    folding DF-2 + d-benchmark-category-gate-001 into this one leg BEFORE c-exec-021 pays the tax again.
    This CALL is hardened against the real tooling (framing check wf_bb467c7b-c63); the file:line anchors
    below are load-bearing.
  - Backlog source (the direction owns this CALL; the builder does NOT author it):
    C:\projects\Unity\GasCoopGame\docs\DEFERRED-FINDINGS.md §DF-2 (mechanism, repro) + NOW.decisions
    d-benchmark-category-gate-001 (findings F4/F5 from the c-exec-024 G5).
  - DF-2 mechanism: tools/mutation.ps1 runs dotnet-stryker on the CORE project (-p) via the WHOLE headless
    test project (-tp tests/GasCoopGame.Core.Tests). Stryker.NET 4.6.0 has NO test-case filter (verified),
    so the benchmark fixture (tests/.../Field/Voxel/ScKernelScalingBenchmark.cs:33 `[TestFixture,
    Category("Benchmark")]`, a 196k-cell wall-clock matrix) runs on every instrumented + coverage pass →
    ~10-30 min stall, testhost 1300+ CPU-s. Introduced by c-exec-024's 3691f9d ([Explicit] → Category
    Benchmark). check.ps1:88 already excludes it from the normal run via --filter "TestCategory!=Benchmark";
    Stryker cannot. The benchmark TYPE has NO code reference anywhere (only header comments in
    ScKernelScalingMatrixSchemaTests.cs:6-10, which reads the JSON, not the type), and the test project uses
    the SDK default compile glob (no <Compile Include>, no EnableDefaultCompileItems override) — so physically
    MOVING the .cs out of the project tree cleanly excludes it and moving it back restores, with no compile
    breakage. Stryker copies the project to its own sandbox and builds from then-current source (no --no-build),
    so relocating BEFORE `& dotnet stryker` (mutation.ps1:62) is sufficient.
  - Why [Category("Benchmark")] not [Explicit]: hygiene.ps1:96 BANS [Ignore]/[Explicit] and :195 bans
    Assert.Ignore/Assume in headless tests. The [Category("Benchmark")] tag is the CORRECT opt-out and STAYS.
  - Gate-integrity hole (d-benchmark-category-gate-001): check.ps1:88 excludes BOTH NegativeControl AND
    Benchmark from the main run. NegativeControl has a FORCE-EXECUTE counterpart (check.ps1:145-154 a dedicated
    -Deliver pass that RUNS the category to a TRX + tools/negative-control-check.ps1 reading that TRX). ⚠ That
    execute-then-read-TRX shape is CORRECT for NegativeControl (fast oracles) but is EXACTLY WRONG to copy for
    Benchmark: running `dotnet test --filter "TestCategory=Benchmark"` executes the ~30-min matrix — moving
    DF-2's tax onto -Deliver. Do NOT mirror check.ps1:145-154 for Benchmark. Benchmark has NO counterpart today
    — that is the class to close, with a NON-executing, category-AWARE gate (below).
  - Category-AWARE is required and NON-trivial: empirically on this repo's SDK/locale (dotnet 10.x, ANSI/ru),
    `dotnet test --list-tests --filter "TestCategory=Benchmark"` returns in seconds (good — no execution) but
    prints ALL ~1341 tests by BARE METHOD NAME with the --filter fully IGNORED and NO category annotation
    (the same --list-tests-ignores-filter quirk negative-control-check.ps1:11-14 documents). So a
    grep-the-name-in-`--list-tests` gate is CATEGORY-BLIND: it passes identically whether the test is
    [Category("Benchmark")], mistagged [Category("Bench")], or untagged — it can never go RED on a mistag →
    vacuous. The buildable category-AWARE model is tools/hygiene.ps1:81-102 (a build-time SOURCE-SCAN that
    enumerates *.cs and regex-detects attributes structurally, no execution) OR reflection over the built test
    DLL's NUnit CategoryAttribute. Use one of those.
  - Matrix-freshness hole: tests/.../ScKernelScalingMatrixSchemaTests.cs pins STRUCTURE only, never re-derives
    numbers → a stale/hand-edited matrix passes. The committed matrix
    docs/measurements/c-exec-023-kernel-scaling-matrix.json flooded_hangar block is internally derivable and
    BIT-EXACT today: ms_per_tick_peak=88.8165; weak_peer_x2_ms=177.633 (==2×peak); weak_peer_x4_ms=355.266
    (==4×peak); ms_per_tick_peak==max(ms_by_roster[].ms_per_tick); over_budget=true. ⚠ over_budget is true ONLY
    via the weak-peer projection: peak 88.8165 is UNDER budget_high_ms=100; the flag is derivable ONLY as
    (weak_peer_x2_ms 177.633 > budget_high_ms 100). A peak-based over_budget assert evaluates false==true and
    RETRO-FAILS the committed green matrix — see done_when for the exact pinned rule.
  - Toolchain constraint (HARD): Windows PowerShell 5.1 ONLY (no pwsh/PS7 on PATH), ASCII-only in BOM-less .ps1
    (non-ASCII breaks parse under the ANSI codepage — docs/FRICTION.md).
  - Contour: GasCoopGame AGENTS.md (repo now at contract v14). Base = current GasCoopGame main @e0e4f5a (v14).

boundaries: |
  - INFRA ONLY: tools/**, validation.config, tests/.../Field/Voxel/ScKernelScalingMatrixSchemaTests.cs (the
    consistency asserts + their RED control fixture), docs/adr/**, docs/reviews/**, docs/DEFERRED-FINDINGS.md
    (mark DF-2 resolved). NO Core/Field/sim code, NO goldens, NO tick path, NO new FEATURE test. Engine worktree
    GasCoopGame_dev — NEVER dev_2.
  - CONTOUR = the c-exec-024/026/027 infra pattern: do NOT create a frozen openspec/changes/c-exec-028-*/ folder.
    That folder is the trigger for the whole per-change -Deliver battery (check.ps1:218-361: v10 review-evidence +
    v11 negative-control-coverage + v13 refuted-register + v14 fix-class-closure + spec-silence + a REQUIRED
    mutation-c-exec-028 score ≥ floor). With no frozen folder, that battery is N/A by absence — the clean route
    the last three infra legs took. The leg's OWN evidence is still: independent RED-test-author FIRST + a
    fresh-session G5 + an ADR + a docs/reviews/review-c-exec-028-*.md record.
  - Property-layer v12 stays N/A by TOKEN-ABSENCE (builder-controlled, coverage-check.ps1:166-169 +
    validation.config): this is INFRA, NOT a core algorithm — do NOT declare `change-class = core algorithm`
    anywhere, and do NOT manufacture a `## Property coverage` table for a .ps1/test change.
  - ADDITIVE / no-weaken (the hard invariant): the existing check.ps1 exclusions STAY (benchmark correctly
    measure-only; NegativeControl stays force-EXECUTED); the [Category("Benchmark")] tag STAYS. Do NOT delete the
    benchmark, re-tag it [Explicit] (hygiene bans it), remove the check.ps1 Benchmark exclusion, or
    force-EXECUTE the benchmark on -Deliver. If a new gate would retro-fail an already-delivered leg →
    GRANDFATHER it in validation.config (owner-governed), never loosen.
  - mutation.ps1 DF-2 fix mechanism = a filesystem MOVE/RENAME of the KNOWN explicit path
    tests/.../ScKernelScalingBenchmark.cs (byte-identity is INHERENT to a move — do NOT copy-rewrite, which
    risks a CRLF/BOM change under PS 5.1; a Get-FileHash belt-and-suspenders check, if kept, captures the hash
    BEFORE the move, no md5sum). Compute stash source+dest as ABSOLUTE paths anchored on $repo (mutation.ps1:34)
    BEFORE the run; capture the relocate state in a script-scope var; restore in a try/finally using those
    absolute paths, guarded by Test-Path (idempotent — restore only if currently relocated) so a crash mid-Stryker
    cannot strand the file. Prefer the single hardcoded path over a repo-wide category grep; if a grep is used,
    restore MUST be driven by the exact captured list, never a re-scan.
  - "No PERSISTENT dirty window" is the promise (try/finally restores byte-identically even on crash). A transient
    in-run dirty tree is ACCEPTABLE — mutation.ps1 is a validate-time step never run concurrently with -Deliver
    (check.ps1 READS the mutation artifact at :238, it never invokes mutation.ps1). If a ZERO-window mechanism is
    cheaply available (a Stryker mutate-glob that structurally cannot reach the benchmark, or a copy-to-temp test
    project), prefer it; otherwise the relocate is fine.
  - STOP + surface as an owner decision (do not silently restructure) if: the self-contained exclusion needs a
    PERSISTENT test-project split; OR a category-AWARE discovery cannot be built without executing the matrix.

done_when: |
  DF-2 (mutation.ps1): a scoped mutation run over the core no longer executes ScKernelScalingBenchmark on any
  Stryker pass and completes without the ~30-min stall; the exclusion is self-contained (absolute-path MOVE +
  Test-Path-guarded try/finally restore, crash-safe, byte-identical) with NO persistent dirty window; an
  independent-author RED self-test proves the benchmark is ABSENT from Stryker's DISCOVERED test set during the run
  (read Stryker's own test enumeration / mutation-report if 4.6.0 exposes it; fall back to a filesystem-relocated
  assert only if it does not) — RED before the fix, GREEN after; a real scoped mutation run still records a VALID
  non-vacuous CORE score afterward (regression witness that mutation.ps1 still scores correctly — this does NOT
  require a c-exec-028 mutation artifact).
  Gate-integrity A — Benchmark force-DISCOVER counterpart (category-AWARE, NON-executing): a gate proves the
  benchmark test is PRESENT + COMPILED + CORRECTLY-TAGGED [Category("Benchmark")] + IS-COLLECTED by the runner —
  built as a SOURCE-SCAN (mirror hygiene.ps1:81-102) or reflection over the built test DLL's NUnit
  CategoryAttribute; NOT via `dotnet test --list-tests` (category-blind here) and NOT via a category-filtered
  EXECUTION run (that re-runs the matrix). It does NOT claim to prove runtime "would-run" (unobservable without
  executing — that stays covered by the documented manual `--filter FullyQualifiedName~ScKernelScalingBenchmark`
  regeneration). The gate FAILS when the tagged test is absent/undiscovered/mistagged; its -SelfTest seeds a
  MISTAG (flip the actual token Benchmark→Bench) and proves RED, GREEN on the well-formed case; wired into
  check.ps1 -Deliver.
  General-rule enforcement (concrete, non-self-referential): a consistency check parses ONLY the actual dotnet-test
  invocation at check.ps1:88 — split its --filter argument on '&', extract each `TestCategory!=<X>` clause, and
  require each <X> to have a counterpart (NegativeControl = force-EXECUTE, already present; Benchmark = force-DISCOVER,
  added here). Comment strings and other .cs/.ps1 mentions of "TestCategory!=..." are OUT of parse scope; its
  -SelfTest includes a DECOY (a `TestCategory!=Foo` inside a comment MUST NOT trigger, and a real bare uncountered
  exclusion MUST go RED). The broader "every future exclusion needs a counterpart" principle is also recorded in the
  ADR as a convention.
  Gate-integrity B — matrix freshness: ScKernelScalingMatrixSchemaTests gains internal-consistency asserts a
  stale/hand-edited matrix FAILS: weak_peer_x2_ms == 2×ms_per_tick_peak, weak_peer_x4_ms == 4×ms_per_tick_peak
  (float tolerance), ms_per_tick_peak == max(ms_by_roster[].ms_per_tick), and over_budget == (weak_peer_x2_ms >
  budget_high_ms) — using the x2 PROJECTION specifically; peak alone is UNDER budget and MUST NOT be the comparand
  (a peak-based rule retro-fails the committed green matrix). Cheap extra pin if available:
  all_cores_naive_split.flooded_ms_peak == flooded_hangar.ms_per_tick_peak (closes the duplicate-peak drift).
  Independent-author RED control = a deliberately inconsistent matrix fixture the asserts reject.
  Closure: tools/check.ps1 -Deliver GREEN end-to-end on the repo as-is (new self-tests pass AND every currently-
  delivered leg still delivers — grandfather if needed, transcript attached); validation.config updated if a
  grandfather list is added; ADR-P-0005 (confirmed free) records the tooling hardening + the general convention; a
  FRESH-session G5 refutes that each new seeded-miss / RED control truly goes RED-without-fix / GREEN-with-fix (not a
  self-authored green), recorded in docs/reviews/review-c-exec-028-*.md. INDEPENDENT RED test-author FIRST on every
  new assertion (author writes the failing self-tests/asserts from THIS CALL; the builder makes them pass and may not
  edit them). Mark DF-2 resolved in docs/DEFERRED-FINDINGS.md.

return: |
  RESULT routed HOME to indie-game-development/g-9c41: commits + the full check.ps1 -Deliver transcript (green,
  showing the new self-tests + the benchmark force-DISCOVER pass + any grandfather-skip lines), the new/edited
  scripts (mutation.ps1, the benchmark discoverability gate + the check.ps1:88 exclusion-consistency check, check.ps1
  wiring), the schema-test consistency asserts + their RED control, ADR-P-0005, and the fresh-session G5 record.
  Include a timing note proving the mutation run no longer stalls. dev→main merge + push OWNER-GATED. next = return to
  g-9c41: the bench-tax is cleared; the road resumes at c-exec-021 (Sc-reactions) — re-harden + §Re-sync (repo at v14)
  + fill §PENDING, fire in a fresh owner-present PLAN.

budget: |
  One small infra leg (two tools/ scripts + one test file + an ADR). Honor the STOP-clauses in boundaries rather
  than silently restructuring or re-introducing the 30-min tax on -Deliver.

parent: s-work-043

END_OF_FILE: live/indie-game-development/work/c-exec-028-tools-benchmark-hardening-call.md
