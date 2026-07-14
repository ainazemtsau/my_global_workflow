CALL c-solmax-operating-substrate-first-process-creator-t4-health-reclamation-f-hr-r01-bounded-repair-010
to: executor
direction: solmax
node: g-operating-substrate-first-process-creator
task: t-4
repo: C:/projects/solmax-operating-substrate
kind: engineering

goal: |
  The current Health Reclamation candidate has only F-HR-R01's two false Q2
  projection classifications corrected and its direct repair evidence aligned,
  while all existing behavior, history and candidate-only lifecycle state are
  preserved and the changed candidate is ready for a separate fresh
  refutation.

context: |
  Work in the exact product worktree:
  C:/projects/solmax-operating-substrate

  Required clean base:
  b23eb0bb208a6b2344043ac472621093132dadc9
  on branch codex/health-reclamation-candidate-build.

  The product validation.config and Direction engineering contract are both
  version 21. Read the product root and packs/ AGENTS.md files before acting.

  Binding owner-approved contour:
  C:/my_global_workflow_worktrees/solmax/live/solmax/work/health-reclamation-f-hr-r01-repair-plan-v1.md

  Complete RED_READY packet, 28 explicit skeletons and zero unresolved or
  inferred cells:
  C:/my_global_workflow_worktrees/solmax/live/solmax/work/health-reclamation-f-hr-r01-repair-red-readiness.md

  Binding Q2 architecture source:
  C:/my_global_workflow_worktrees/solmax/live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-classification-001.md

  Product evidence:
  - docs/reviews/review-health-reclamation-v1.md
  - RESULT.md
  - packs/health-reclamation/verification/scope-coverage.md
  - docs/results/health-reclamation-v1-self-check.md
  - packs/health-reclamation/policy.md
  - packs/process-creator/procedures/02-discover-and-classify.md

  Review 007 found exactly one blocker:
  F-HR-R01, invariant/class
  Q2 atomic-classification / evidence-integrity defect. It localized the class
  to OP-HR01 and KH-HR01. The owner approved only this repair:
  "A — исправляем только две классификации в правильном репозитории, сохраняя весь текущий прогрес"

  Correct semantic outcome:
  - OP-HR01 classifies the Health rule for accepting bounded current owner
    choices as a process-pack declaration owned by the Health Reclamation
    pack; the owner remains current input/source and legitimate decision or
    variation owner, never owner-wide profile truth.
  - KH-HR01 classifies the Health routing rule for applicable qualified-human
    judgment as a process-pack declaration owned by the Health Reclamation
    pack; the qualified human remains the external bounded source and authority
    holder, never a sixth architecture class.

boundaries: |
  Work only in C:/projects/solmax-operating-substrate. Do not write Direction
  OS state.

  Before editing, require exact clean HEAD b23eb0b and contract v21. Any drift
  returns BLOCKED without a partial repair.

  The complete product diff is limited to exactly three existing paths:
  - packs/health-reclamation/verification/scope-coverage.md, only stable rows
    OP-HR01 and KH-HR01;
  - docs/results/health-reclamation-v1-self-check.md, only the directly
    affected Q2/REVIEW-2/sweep statements and F-HR-R01 class+sweep record;
  - RESULT.md, only to align the current repair handback.

  No new file and no fourth changed path are allowed. Preserve
  docs/reviews/review-health-reclamation-v1.md byte-for-byte as historical
  OPEN/BLOCKING FAIL evidence. Do not author a new review in this repair leg.

  Do not change Health behavior, policy, contract, routing, continuation,
  procedures, scenarios, owner intent or research. Do not change kernel/,
  services/, adapters/, packs/process-creator/, tools/, openspec/,
  validation.config or repository contracts. Do not introduce a reusable
  service, owner profile, new class, schema, scanner, parser, semantic gate,
  dependency, CI or infrastructure.

  Do not read, import, cite as authority or work in legacy Direction Health,
  Health AI, Health HQ or live/health. Do not request health information,
  research or a repeated process description. No personal health data may
  enter the repo or report.

  Do not admit, activate, invoke, run or close the process; do not perform an
  external effect; do not close t-4, change Direction state, extend appetite or
  promote structural/useful-live/reliability/reuse claims.

  If a new class sibling, semantic need, spec amendment or fourth path appears,
  stop and return that one exact blocker instead of expanding scope.

done_when: |
  RED-readiness rows R01-R28 each have an explicit MET disposition with named
  evidence at the repair HEAD and zero blank, inferred, unresolved or n/a
  cells.

  OP-HR01 and KH-HR01 each carry exactly one of Q2's five accepted primary
  classes: process-pack declaration. Owner current choices remain bounded
  current source/input and qualified-human judgment remains bounded external
  source/authority. Neither becomes owner-profile, kernel, reusable-service,
  adapter or a sixth class.

  The base-to-repair changed-path set is exactly the three allowed paths.
  Within scope-coverage.md only OP-HR01 and KH-HR01 change. The self-check
  reconciles only the affected Q2 and class-sweep evidence. RESULT.md records
  the current author repair without claiming a binding fresh verdict.

  The fix report carries, for F-HR-R01, the exact invariant/class token and a
  complete sweep record for OP-HR01, KH-HR01 and every checked sibling
  disposition. Any sibling outside the approved diff blocks rather than being
  fixed here.

  Review 007 remains byte-identical historical FAIL evidence. The preserved
  commit chain remains reachable. Health behavior artifacts, HR-01..HR-17,
  S01..S16, F-A01..F-A06, kernel, Process Creator, services, adapters, tooling,
  OpenSpec and contract stamp remain unchanged.

  Current product status is explicit:
  - review 007: historical structural FAIL at its reviewed basis;
  - repaired candidate: awaiting separate fresh structural refutation, not
    PASS;
  - admission and activation: NOT_PERFORMED;
  - useful-live behavior, recurring reliability and demonstrated reuse:
    NOT_YET_PROVEN;
  - t-4: unchanged and active in Direction OS.

  At the repair HEAD all commands exit zero and exact output is recorded:
  - python tools/check.py
  - python tools/selfcheck.py
  - python tools/check.py --deliver

  The repair commit and report return to Solmax with a complete handoff for a
  later distinct fresh read-only refutation. This executor neither authors that
  review nor the next Direction OS CALL.

return: |
  Return one complete Direction OS engineering RESULT containing:

  - base, branch, repair commit/HEAD, ancestry and clean-status evidence;
  - exact changed paths plus complete hunk-level diff containment;
  - one explicit MET or BLOCKED line with named evidence for every RED row
    R01-R28 and the final unresolved/inferred/n/a counts;
  - exact OP-HR01 and KH-HR01 semantic reconciliation;
  - F-HR-R01 invariant/class and full sweep record required by fix-class
    closure;
  - confirmation that review 007 and all protected semantics/history remain
    unchanged;
  - exact output and exit status for all three repository commands;
  - explicit sources used, legacy-Health exclusion, no-personal-data statement,
    assumptions, cuts, cost and remaining-budget assessment;
  - explicit candidate-only/not-admitted/not-activated/not-run/not-useful-live/
    not-reliability-proven/not-reuse-proven statement; and
  - route back to Solmax to commission a separate fresh read-only refutation of
    the repair commit.

  Do not author the downstream Direction CALL from the product repository.

budget: |
  At most the unchanged 0.25 focused-execution-day bounded repair reserve.
  No extension, no mandatory cut and no scope expansion.

parent: s-solmax-operating-substrate-first-process-creator-t4-health-reclamation-f-hr-r01-red-preflight-009
surface: codex

END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-first-process-creator-t4-health-reclamation-f-hr-r01-bounded-repair-010.md
