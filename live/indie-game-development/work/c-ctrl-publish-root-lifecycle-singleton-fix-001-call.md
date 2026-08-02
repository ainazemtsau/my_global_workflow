# CALL — c-ctrl-publish-root-lifecycle-singleton-fix-001

to: executor
kind: engineering
repo: ainazemtsau/GasCoopGame
engineering_contract: 35
direction: indie-game-development
track: переноска
node: g-6b13
task: c-1b
parent: c-exec-rules-layer-and-single-walker-001
issued: 2026-08-02 by s-repair-g-6b13-a1b-plan-route-and-tooling-separation-001
status: ready
basis: main/origin-main `c75015a8`; source patch `ad42b2d8`; U3 PLAN line `7c5fc5a6` → `ad42b2d8` → `f7387751`, verified 2026-08-02
slot: repository-prescribed WIN-CTRL route; WIN-U3 may be touched only to incorporate the published main and prove the feature diff

## goal

Publish the already reviewed `root-lifecycle-check.ps1` singleton-frozen-entry fix as an independent
tooling change on actual product `main`, then make the U3 a-1b line include that current main so the
feature diff contains only its PLAN/spec/ADR/receipt artifacts. Preserve the accepted PLAN authority.

## context

This is task c-1b, a separate tooling task created from the owner's instruction to detach the fix
from a-1b. The a-1b PLAN leg produced `7c5fc5a6` (frozen PLAN/spec/ADR) and `f7387751` (PLAN receipts).
Between them, `ad42b2d8` changes only `tools/root-lifecycle-check.ps1` (+26/-3 effective diff) and
was independently reviewed GREEN. The owner accepted PLAN and ADR-E-0019 by content but said:
“BUILD пока не запускать: сначала исправить Direction-маршрут и отделить ad42b2d8 от задачи
a-1b.” This CALL is that separation leg. It is not feature execution.

The source commit cannot be fast-forwarded into main because its parent includes the a-1b PLAN.
The repository's own AGENTS.md and control-slot contract remain authority for publishing and slot
transport. Frozen commits `7c5fc5a6` and `f7387751` are evidence and must not be rewritten.

## boundaries

- No gameplay, Unity scene, PAIR-CANDIDATE, PAIR-FREEZE, BUILD, VALIDATE, or feature REPORT work.
- Do not change PLAN/spec/ADR/PLAN receipts, `Assets/**`, `core/**`, `validation.config`, or any checker
  other than the exact `tools/root-lifecycle-check.ps1` fix already evidenced by `ad42b2d8`.
- No rebase/reset/history rewrite of the U3 PLAN line. If the independent publication cannot be
  incorporated while preserving `7c5fc5a6` and `f7387751`, return one exact ESCALATE instead.

## done_when

1. Actual `origin/main` contains a standalone commit whose product change is exactly the reviewed
   singleton-frozen-entry tooling fix, with the repository-required checks GREEN.
2. U3 incorporates that current main without rewriting `7c5fc5a6` or `f7387751`; its diff against
   main contains no `tools/**`, `validation.config`, or checker change attributable to a-1b.
3. All touched control/slot checkouts are clean, leases are closed, and the HOME evidence names the
   exact main commit, U3 tip, ancestry/diff commands, and check results.

## return

HOME to `indie-game-development`, parent `c-exec-rules-layer-and-single-walker-001`: exact published
main SHA/readback, exact U3 SHA, proof that both accepted PLAN commits still resolve and were not
rewritten, scoped diff output, checks, slot/lease state, and any blocker. Do not launch the parent.

## budget

One control leg. No product-feature budget and no BUILD.

END_OF_FILE: live/indie-game-development/work/c-ctrl-publish-root-lifecycle-singleton-fix-001-call.md
