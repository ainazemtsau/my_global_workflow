CALL c-exec-030
to: executor
kind: engineering
direction: indie-game-development
node: g-9c41
repo: C:\projects\Unity\GasCoopGame_dev
surface: cli
goal: |
  GasCoopGame's per-leg deliverables stop causing MERGE CONFLICTS when parallel legs (dev / dev_2) land on
  main, and the deliver gate can no longer be bypassed by STAGED-but-uncommitted changes. Two additive fixes,
  same surface (check.ps1 / deliver tooling); no existing green gate weakened:
  (1) RESULT-per-leg — the single root RESULT.md that EVERY leg rewrites becomes one file PER leg, so two
      parallel legs never touch the same file (today they collide → manual "consolidate RESULT").
  (2) DF-5 (P1 gate-integrity) — the -Deliver gate sees STAGED changes, closing the review-evidence bypass.

context: |
  - Owner-approved 2026-07-04: after deciding NOT to split the visual track into its own OS direction
    (indie-game-development stays the umbrella), the product-repo merge conflicts are the real remaining pain.
    The owner named RESULT.md conflicts specifically. Batched with DF-5 because both touch tools/check.ps1.
  - ROOT CAUSE (RESULT-per-leg): a single root RESULT.md (~13.6 KB) is REWRITTEN by every leg. Two parallel
    legs both edit it → merge conflict + manual consolidation. Git witnesses on main:
    f43aa39 "Fix parallel-leg collisions on dev … consolidated RESULT"; e0e4f5a "… RESULT consolidated";
    f43aa39 also "renumber throw-atomicity ADR-E-0004->0005" (two legs grabbed the same ADR number — the same
    shared-counter class). check.ps1 -Deliver reads RESULT.md for the RESULT field-gate (v1 report-handback).
  - ROOT CAUSE (DF-5): tools/check.ps1:64 Assert-NoUnstagedTrackedChanges checks only `git diff-files`
    (ignores the INDEX/staged), and tools/review-check.ps1:90 accounts only commits in Reviewed-commit..HEAD —
    so a STAGED (not-yet-committed) source/tool/test change can pass -Deliver absent from review evidence.
    Full mechanism + recommended fix: docs/DEFERRED-FINDINGS.md §DF-5.
  - SEQUENCING: base on current GasCoopGame main. The c-exec-029 (DF-10) work is on dev @a82ee4f NOT yet merged
    (owner-gated) — let that merge land FIRST, then run this leg on the clean main tip, so this leg does not
    itself become the parallel-collision it exists to remove.
  - Contour = the c-024/026/028 INFRA pattern (repo at contract v14; a §Re-sync to v15/v16/v17 is a SEPARATE
    owed leg — do NOT fold it here). NO frozen openspec/changes/<id>/ folder → the v12/per-change battery is
    N/A by absence. The leg's own evidence is still: independent RED test-author FIRST + a fresh-session G5 +
    an ADR + a docs/reviews/review-c-exec-030-*.md record.

boundaries: |
  - INFRA ONLY: tools/** (check.ps1, review-check.ps1, any new helper), the RESULT convention + its consumers,
    .gitattributes, docs/** (RESULT relocation, DEFERRED-FINDINGS mark DF-5 resolved), docs/adr/**. NO Core/
    Field/sim code, NO goldens, NO tick path, NO new FEATURE test. Engine worktree GasCoopGame_dev — NEVER dev_2.
  - ADDITIVE / no-weaken (hard invariant): the RESULT field-gate stays AS STRONG (it just reads the per-leg
    file instead of the root file); the review-evidence gate gets STRICTER (now also catches staged), never
    looser; NegativeControl/Benchmark exclusions + all v10–v14 gates stay intact. If a new check would
    retro-fail an already-delivered leg → GRANDFATHER in validation.config (owner-governed), never loosen.
  - RESULT-per-leg mechanism = a filesystem convention change (root RESULT.md → docs/results/<changeId>.md or
    equivalent) + updating check.ps1's RESULT field-gate to read the per-leg file. Migrate the existing root
    RESULT.md content to its owning leg's file (do not silently drop history).
  - Append-only ledgers (DEFERRED-FINDINGS.md, docs/FRICTION.md) MAY get `merge=union` in .gitattributes — ONLY
    for genuinely append-only files (NOT RESULT.md, which is rewritten → union would concat garbage).
  - ADR numbering collision (parallel legs grab the same next number): address as a CONVENTION (e.g. id keyed to
    changeId/date, or a per-namespace note), NOT a heavy mechanism. Lowest-priority of the three; a note + the
    convention is enough.
  - STOP + surface as an owner decision if: RESULT-per-leg needs a change to the frozen RESULT SCHEMA / field
    set (it should not — same fields, new location); OR the DF-5 staged-diff guard would retro-fail a currently
    green leg without a clean grandfather.

done_when: |
  RESULT-per-leg: the root RESULT.md is retired in favor of ONE file per leg (docs/results/<changeId>.md or
  equivalent), each leg writes only its own; a scripted check proves two DIFFERENT legs' RESULT files do NOT
  overlap in path (no shared-file collision); check.ps1 -Deliver's RESULT field-gate reads the CURRENT leg's
  per-leg file and still enforces every required field (an independent RED self-test: a per-leg RESULT missing a
  required field → -Deliver FAILS; well-formed → passes). Existing root RESULT.md content migrated to its owning
  leg's file (no history dropped).
  Append-only ledgers: DEFERRED-FINDINGS.md + docs/FRICTION.md carry `merge=union` in .gitattributes (or an
  equivalent per-leg-fragment scheme); a note records that RESULT.md is deliberately NOT union (rewritten).
  ADR numbering: a recorded convention that removes the shared-counter collision (id by changeId/date or
  per-namespace), with a one-line ADR/README note; no two future parallel legs need a manual renumber.
  DF-5 (P1): check.ps1 -Deliver FAILS on a non-empty STAGED diff for the guarded roots (or review-check.ps1
  accounts for staged changes) — a staged guarded source/tool/test change can no longer pass -Deliver absent
  from review evidence; an independent RED self-test proves it (a staged guarded change → -Deliver RED before
  the fix, GREEN/accounted after); DF-5 marked resolved in docs/DEFERRED-FINDINGS.md.
  Closure: check.ps1 -Deliver GREEN end-to-end on the repo as-is (new self-tests pass AND every currently-
  delivered leg still delivers — grandfather if needed, transcript attached); ADR-P-000N (next free) records the
  convention + the DF-5 hardening; a FRESH-session G5 refutes each new seeded-miss / RED control (RED-without-fix
  / GREEN-with-fix), recorded in docs/reviews/review-c-exec-030-*.md. INDEPENDENT RED test-author FIRST on every
  new assertion (builder makes them pass, may not edit them).

return: |
  RESULT routed HOME to indie-game-development/g-9c41: commits + the full check.ps1 -Deliver transcript (green,
  showing the per-leg RESULT field-gate + the DF-5 staged-diff self-test + any grandfather-skip lines), the
  new/edited scripts, .gitattributes, the migrated RESULT layout, ADR-P-000N, and the fresh-session G5 record.
  Show two mock parallel legs' RESULT files not colliding. dev→main merge + push OWNER-GATED. next = return to
  g-9c41: parallel-leg merge conflicts cleared + DF-5 closed; the road resumes at c-exec-021 (Sc-reactions).

budget: |
  One small infra leg (check.ps1 + review-check.ps1 + a RESULT relocation + .gitattributes + an ADR). Honor the
  STOP-clauses rather than touching the RESULT schema or weakening a gate.

parent: s-work-049

END_OF_FILE: live/indie-game-development/work/c-exec-030-result-per-leg-and-df5-call.md
