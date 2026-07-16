CALL c-solmax-operating-substrate-first-process-creator-t4-health-reclamation-v26-bounded-build-018
to: executor
direction: solmax
node: g-operating-substrate-first-process-creator
task: t-4
repo: C:/projects/solmax-operating-substrate-v26-integration
kind: engineering

goal: |
  The terminal-v26 Health Reclamation candidate contains exactly the approved
  OP-HR01 and KH-HR01 Q2 classification corrections, its directly affected
  evidence is internally aligned, every other semantic/history/lifecycle
  surface is preserved, and the committed candidate is ready for one later
  fresh actual-diff refutation.

context: |
  Run in a fresh Codex task in:
  C:/projects/solmax-operating-substrate-v26-integration

  Required product identity:
  - branch: codex/health-reclamation-v26-integration-candidate
  - clean start HEAD: 7ed7903045bef2c4b49124c61b98c9ebf3e7232a
  - first parent / unchanged Health basis: 3ee6914fd4973ebe947cb89c37f0f144cfdafdee
  - terminal-v26 parent: 7bbc73d725f6d82028bde396d7764ec13145f977
  - pre-repair Health basis: b23eb0bb208a6b2344043ac472621093132dadc9

  Current product workflow authority is repo-local:
  AGENTS.md, packs/AGENTS.md, REVIEW.md, openspec/README.md and
  validation.config at the required start. Contract v26 keeps full-packet
  semantic readiness for Markdown but retires the v22 RED-FREEZE prose carrier.

  Binding fresh PASS and Direction repair authority:
  - C:/my_global_workflow_worktrees/solmax/live/solmax/history/
    2026-07-16-s-solmax-operating-substrate-first-process-creator-t4-v26-readiness-pass-019.md
  - C:/my_global_workflow_worktrees/solmax/live/solmax/work/
    health-reclamation-f-hr-r01-repair-plan-v1.md
  - C:/my_global_workflow_worktrees/solmax/live/solmax/work/
    health-reclamation-f-hr-r01-repair-red-readiness.md
  - C:/my_global_workflow_worktrees/solmax/live/solmax/work/
    operating-substrate/cards/
    operating-substrate-service-zone-classification-001.md

  Owner-approved outcome:
  "A — исправляем только две классификации в правильном репозитории, сохраняя
  весь текущий прогрес"

  Exact repair meaning:
  - OP-HR01: the Health rule is one process-pack declaration normatively owned
    by the Health Reclamation pack. The owner remains the bounded current
    input/source, decision owner and variation owner. The choice is not
    owner-profile truth, is not silently persisted and is not reused across
    processes.
  - KH-HR01: the Health routing rule is one process-pack declaration
    normatively owned by the Health Reclamation pack. The applicable qualified
    human remains the bounded external source and authority holder. The pack
    gains no professional authority and no sixth architecture class exists.

  Historical docs/reviews/review-health-reclamation-v1.md remains the
  byte-identical original FAIL evidence. The committed v22 repair OpenSpec,
  PLAN/RED artifacts and inventories are reachable history only; they neither
  launch nor block this terminal-v26 BUILD.

boundaries: |
  Work only in the named product repository. Do not write Direction OS state.

  Before editing, require the exact branch, clean HEAD 7ed7903 and contract/
  inventory version 26. Any mismatch returns one exact blocker without partial
  edits.

  The complete start-to-BUILD product-content diff is limited to exactly these
  three existing paths:
  1. packs/health-reclamation/verification/scope-coverage.md — change only the
     OP-HR01 and KH-HR01 rows.
  2. docs/results/health-reclamation-v1-self-check.md — reconcile only the
     directly affected Q2 atomic-ownership row, REVIEW item 2 row,
     duplicate-primary-owner/sibling-sweep row, and F-HR-R01 repair/sweep
     evidence.
  3. RESULT.md — replace the integration handoff with an honest bounded BUILD
     closing report for the new candidate commit.

  No new file and no fourth product path are allowed. Preserve
  docs/reviews/review-health-reclamation-v1.md byte-for-byte at blob
  41d1c21d38113a7ab44aafd64deef4e06278d3cd. Do not author the later review in
  this BUILD.

  Do not modify any other Health pack, procedure, scenario, OpenSpec, ADR,
  kernel, Process Creator, service, adapter, tooling, validation, dependency or
  workflow authority. Do not create another PLAN, PLAN-AMEND, RED/SURFACE
  artifact, obligation inventory, recipe ledger, parser, scanner, schema or
  conformance proxy.

  Do not use legacy Direction Health, Health AI, Health HQ or live/health as
  authority or input. Do not request, read, infer or record personal health
  information.

  Do not admit, activate, invoke or run Health Reclamation; perform no external
  effect; close no Direction task; change no appetite; and promote no
  useful-live, reliability or reuse claim.

  If the full sibling sweep finds another material Q2 classification defect,
  if a broader semantic change is needed, or if a fourth path is required,
  stop and return that one concrete blocker rather than expanding scope.

done_when: |
  The repair starts from exact clean HEAD 7ed7903 on the named branch and ends
  in one new descriptive commit with a clean worktree.

  OP-HR01 and KH-HR01 each have exactly one accepted primary Q2 class:
  process-pack declaration, with the Health Reclamation pack as primary
  normative owner. Their owner/source/decision/variation/authority boundaries
  match the exact meanings in context and create neither owner-profile truth
  nor a sixth class.

  A semantic read of every row in the current primary-ownership projection
  records that only OP-HR01 and KH-HR01 are the repaired siblings. The BUILD
  reports the checked class family and stops rather than fixing any newly found
  sibling.

  The complete 7ed7903-to-BUILD changed-path set is exactly the three allowed
  paths. Scope coverage changes only the two stable rows. Self-check changes
  only the four named evidence targets. RESULT.md changes only to report the
  bounded repair candidate and its evidence.

  All non-target Health/product surfaces are unchanged from 7ed7903. In
  particular, review 007 remains at blob 41d1c21d, the original behavior
  OpenSpec and Health semantics are unchanged, and the historical v22 repair
  packet is not rewritten or treated as current launch authority.

  Product status remains explicit and separate:
  - repaired candidate: awaiting one fresh actual-diff structural refutation;
  - original review 007: historical FAIL at its reviewed basis;
  - admission, activation and process run: NOT_PERFORMED;
  - useful-live behavior, recurring reliability and demonstrated reuse:
    NOT_YET_PROVEN.

  RESULT.md contains outcome, evidence, assumptions, cuts, cost,
  manual-acceptance and next; it names the exact start, identifies final HEAD
  as the commit containing the report, and records changed paths/hunks,
  F-HR-R01 class and sibling sweep, preservation evidence, command outputs and
  candidate-only limits. It does not claim the pending fresh review was already
  performed. The external engineering handback supplies the exact final SHA,
  because a commit cannot contain its own hash.

  At final HEAD all of these exit zero and their exact stdout is recorded:
  - python tools/check.py
  - python tools/selfcheck.py
  - python tools/check.py --deliver
  - git diff --check

  The actual committed candidate diff, final SHA and complete evidence return
  to Solmax for one separate fresh read-only refutation. The BUILD author does
  not author that review or any downstream Direction CALL.

return: |
  Return one complete engineering RESULT with:
  - branch, start, final commit, ancestry and clean-status evidence;
  - exact changed paths and complete hunk containment;
  - exact OP-HR01/KH-HR01 before/after meaning;
  - the complete sibling-sweep disposition and F-HR-R01 invariant/class;
  - hashes or diffs proving every protected surface and review 007 unchanged;
  - exact stdout, stderr disposition and exit status for all four commands;
  - sources used, assumptions, cuts, cost and remaining-budget assessment;
  - explicit no-personal-data and candidate-only lifecycle limits; and
  - route back to Solmax for the later fresh actual-diff review.

  Do not author the downstream Direction CALL from the product repository.

budget: |
  At most the unchanged 0.25 focused-execution-day bounded repair reserve.
  No extension, new reserve, mandatory cut or scope expansion.

parent: s-solmax-operating-substrate-first-process-creator-t4-v26-readiness-pass-019
surface: codex

END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-first-process-creator-t4-health-reclamation-v26-bounded-build-018.md
