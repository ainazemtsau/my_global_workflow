CALL c-solmax-operating-substrate-first-process-creator-t2-f-r01-ledger-correction-001
to: executor
direction: solmax
node: g-operating-substrate-first-process-creator
task: t-2
repo: ainazemtsau/solmax-operating-substrate
kind: engineering

goal: |
  The Process Creator candidate's required coverage ledger coherently records
  the actual status of its scope evidence and is ready for a new independent
  t-3 refutation, without any admission, activation, useful-live or reuse
  claim.

context: |
  The owner made the binding route decision on 2026-07-13:

  "Исправляем F‑R01 и возвращаем на свежую проверку Yeah."

  The prior fresh cross-family t-3 review is durable historical evidence, not
  a mutable target:

  - reviewed BUILD commit:
    d915789baffd13893a9fee1e7cb4b1eb74a02604;
  - review/result HEAD:
    ea254929ff60324e96633573a084c7c990e7f8b7 on local branch
    codex/process-creator-v1-t3-refutation; it is unpushed;
  - review evidence:
    docs/reviews/review-process-creator-v1.md;
  - confirmed finding F-R01:
    packs/process-creator/verification/scope-coverage.md:22-24 says that
    supporting OPEN integration items remain and the overall ledger is FAIL,
    while lines 141-150 says every relevant integration row is closed and the
    overall ledger is PASS. SC-06/09/10/11 are PASS at lines 128 and 131-133.

  The review confirmed no hard semantic failure: Q1-Q7, PC-01..PC-19 (with
  PC-15 legitimately DEFINED_ONLY), active t-2 promises, REVIEW.md items 1-10
  and the F-A01/F-A02 closures survived refutation. F-R01 is a repairable
  evidence-integrity defect, not permission to promote the candidate.

  Read the current product AGENTS.md, REVIEW.md, RESULT.md, validation.config,
  full packs/process-creator tree, relevant prior BUILD evidence, and the
  current review artifact before acting. The synchronized contract version is
  20 in both Direction OS and the product validation.config.

  Binding Direction OS sources:

  - live/solmax/NOW.md (t-2, t-3, scope_contract, cut_list and kill_by);
  - live/solmax/work/operating-substrate/process-creator-materialization-plan-v1.md;
  - live/solmax/work/calls/c-solmax-operating-substrate-first-process-creator-t2-materialization-build-001.md;
  - live/solmax/history/2026-07-13-s-solmax-operating-substrate-first-process-creator-t3-refutation-checkpoint-001.md.

boundaries: |
  Work only in the product repository. Do not write Direction OS state.

  Make the minimum bounded correction needed to reconcile F-R01. Do not alter
  Q1-Q7 semantics, Process Creator procedures, kernel/, services/, adapters/,
  consumer policy, or the approved candidate scope. Do not add CI, scanners,
  paid infrastructure, API spend, a schema, provider semantics or an external
  effect.

  Preserve the existing independent review as historical evidence. Do not
  edit its finding away, claim it was wrong, or author the next independent
  review in this repair leg. A fresh t-3 reviewer must separately examine the
  repaired changed path after this executor returns.

  Do not report the candidate admitted, activated, useful-live, reusable, or
  structurally approved. Do not extend appetite or cut mandatory functionality.

done_when: |
  The coverage ledger's top-level snapshot, its rows and its final conclusion
  no longer contradict each other and accurately describe the actual SC-06,
  SC-09, SC-10 and SC-11 evidence status.

  The correction preserves the separation between author BUILD evidence,
  independent structural disposition, useful-live behavior and demonstrated
  reuse. It contains no false PASS/admission statement and leaves the candidate
  explicitly awaiting a fresh independent t-3 review.

  The product change set and closing result identify the correction commit,
  every changed file, why the old contradictory statements were reconciled,
  and why this repair does not itself establish an independent review result.

  At the correction HEAD, all three existing local commands pass with exact
  output recorded:

  - python tools/check.py
  - python tools/selfcheck.py
  - python tools/check.py --deliver

  No kernel, service, adapter, substantive Process Creator semantic or
  Direction OS change is present.

return: |
  Return one complete Direction OS engineering RESULT containing:

  - correction commit/HEAD, base identity, diff summary and changed paths;
  - exact F-R01 reconciliation with current file/section evidence;
  - confirmation that the historical review was preserved and no fresh review
    was self-authored;
  - exact outputs of all three local commands;
  - explicit candidate-only/not-admitted/not-activated/not-useful-live/not-reuse
    statement;
  - assumptions, cuts (none for mandatory scope), cost, remaining-budget
    assessment, unresolved obligations and current owners; and
  - route back to Solmax to issue a new fresh independent t-3 refutation CALL.

  Do not author the next Direction OS CALL from the product repo.

budget: |
  At most the 0.25 focused-execution-day bounded repair reserve inside the
  unchanged first Process Creator bet. No extension and no mandatory cut.

parent: s-solmax-operating-substrate-first-process-creator-f-r01-repair-route-001
surface: cli

END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-first-process-creator-t2-f-r01-ledger-correction-001.md
