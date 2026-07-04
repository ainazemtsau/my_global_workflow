# RESULT — s-work-043 (g-9c41 / c-exec-028 tools-benchmark hardening CALL framed)

play: work (framing the next executor CALL)
node: g-9c41
date: 2026-07-04

## outcome

Owner answered d-nextcall-tooling-vs-c021-001 → **option 1 ("tools/ лег первым")**. Framed the executor CALL
**c-exec-028** — a small GasCoopGame infra leg that folds DF-2 (mutation.ps1 [Category("Benchmark")] Stryker
poison) + d-benchmark-category-gate-001 (the [Category]-exclusion gate loophole + scaling-matrix freshness) —
to be fired BEFORE c-exec-021 so the mutation tax is cleared first. The CALL is grounded in the real tooling and
adversarially hardened; it did NOT execute (no pwsh here; the leg runs the full contour in a fresh
GasCoopGame_dev session with an independent RED test-author + a fresh G5).

## evidence

CALL = work/c-exec-028-tools-benchmark-hardening-call.md (canonical packets.md executor shape). Grounded first-hand
in the product repo @e0e4f5a (v14): tools/mutation.ps1 (whole-test-project Stryker, no test filter — the DF-2
mechanism), tools/check.ps1:88 (the NegativeControl+Benchmark exclusion) + :145-154 (the NegativeControl
force-EXECUTE counterpart Benchmark lacks), tools/hygiene.ps1:96/195 (the [Explicit]/Assert.Ignore ban that forced
[Category("Benchmark")]), tools/negative-control-check.ps1 (the pattern + the --list-tests-ignores-filter quirk),
ScKernelScalingBenchmark.cs:33 ([TestFixture, Category("Benchmark")], combined attribute), ScKernelScalingMatrixSchemaTests.cs
(structure-only), and the committed matrix (flooded_hangar consistency verified BIT-EXACT).

Adversarial hardening = wf_bb467c7b-c63 (4 lenses reading the real tooling, trying to break the draft CALL). It
returned NO construction blockers to the leg itself but caught, and I FOLDED, real framing defects that would have
mis-built the leg:
- **BLOCKER folded** — the draft pointed the builder at check.ps1:145-154 (the NegativeControl force-EXECUTE path) as
  the Benchmark counterpart's model; mirroring it literally would `dotnet test --filter TestCategory=Benchmark` →
  RUN the ~30-min matrix on every -Deliver, moving DF-2's tax onto the gate. Re-anchored to a category-AWARE
  NON-executing gate (source-scan à la hygiene.ps1:81-102, or DLL CategoryAttribute reflection).
- **BLOCKER folded** — `dotnet test --list-tests` is category-BLIND on this SDK/locale (prints bare method names,
  --filter ignored), so a name-in-list gate is vacuous (can't go RED on a mistag). Required a category-aware source;
  the -SelfTest mistag seed must flip the real token (Benchmark→Bench) and prove RED.
- **should-fix folded** — over_budget must be pinned as (weak_peer_x2_ms > budget_high_ms), NOT peak-based (peak
  88.8165 < budget 100 → a peak rule retro-fails the committed green matrix); the relocate mechanism = a filesystem
  MOVE of the known path with ABSOLUTE-path Test-Path-guarded restore (not a copy-rewrite, CRLF/BOM risk; not a
  repo-wide grep); v12/openspec-battery stays N/A by NOT freezing a spec folder (the c-024/026/027 pattern) and by
  not declaring change-class=core-algorithm; the general-rule gate parses ONLY check.ps1:88's live --filter arg
  (comments out of scope, decoy self-test) to avoid a self-referential/vacuous meta-gate.
- Confirmed clean: ADR-P-0005 free; matrix pins bit-exact (no retro-fail); only excluded categories are
  NegativeControl (has counterpart) + Benchmark (this leg adds one), Property is not excluded (no counterpart owed);
  benchmark TYPE has no code reference (relocate is compile-safe).

## state_changes

- NOW.md header → s-work-043.
- NOW.md decisions: d-nextcall-tooling-vs-c021-001 → ANSWERED (option 1, owner 2026-07-04).
- NOW.md open_calls: + c-exec-028 (open, executor, work/c-exec-028-tools-benchmark-hardening-call.md).
- NOW.md next_slices[0] + next + current_truth: c-exec-028 is the immediate next; c-exec-021 after it.
- NOW.md history_pointers + LOG.md += s-work-043. work/ + c-exec-028-tools-benchmark-hardening-call.md.
- No TREE/CHARTER change (G9 n/a). No bet task added (c-028 is an infra gap-filler CALL, tracked in open_calls).
  G1 intact (one active bet; ≤3 active tasks). The CALL is a NON-core-algorithm infra leg → NOT executed here.

## captures
- (carried) v14 fix-class-closure gate can be voided by archive-on-land exemption — maintenance/FRICTION candidate.

## decisions_needed
- (none new). Still pending owner from prior: d-marketing-wake-001, d-coop-interdependence-repin-001.

## play_check
- 1 OPEN: done — owner answer = option 1 ("tools/ лег первым"); read real tools/ (mutation.ps1, check.ps1,
  hygiene.ps1, negative-control-check.ps1, benchmark + schema test, committed matrix).
- 2 draft: done — work/c-exec-028-tools-benchmark-hardening-call.md drafted grounded in the tooling.
- 3 harden: done — wf_bb467c7b-c63 (4 lenses); 2 blockers + 7 should-fix folded into the CALL; clean confirmations recorded.
- 4 CLOSE: done — RESULT final; writer-apply + commit (agent-CLI self-writer after RESULT). OS commit LOCAL; push owner-gated.

log: work c-exec-028: framed + hardened the tools/ benchmark-hardening CALL (DF-2 + d-benchmark-category-gate-001) after owner picked "tools/ leg first"; wf_bb467c7b-c63 caught 2 blockers (force-EXECUTE trap / --list-tests category-blindness) + 7 should-fix, all folded; next = fire c-028 in a fresh GasCoopGame_dev session, then c-exec-021

next: |
  Fire c-exec-028 in a FRESH GasCoopGame_dev session (owner runs it; engine worktree, never dev_2; full contour —
  independent RED test-author first, -Deliver green, fresh-session G5, dev→main merge owner-gated). On its GREEN +
  binding G5 → the bench-tax is cleared; return to g-9c41 and re-harden + fire c-exec-021 (Sc-reactions): §Re-sync
  (repo at v14, not v11) + full fire-time re-hardening + fill §PENDING, fire in a fresh owner-present PLAN. Do NOT
  re-fire c-022..027; do NOT re-run W1a. CALENDAR: July demo-road shape 2026-07-10..15 (d-demo-road-001).

END_OF_FILE: live/indie-game-development/history/2026-07-04-s-work-043-c-exec-028-tools-hardening-framed.md
