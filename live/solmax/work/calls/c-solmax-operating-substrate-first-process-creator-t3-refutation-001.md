CALL c-solmax-operating-substrate-first-process-creator-t3-refutation-001
to: executor
direction: solmax
node: g-operating-substrate-first-process-creator
task: t-3
repo: ainazemtsau/solmax-operating-substrate
kind: engineering

goal: |
  The Process Creator candidate frozen at
  d915789baffd13893a9fee1e7cb4b1eb74a02604 has an independent recorded
  structural evidence package sufficient for the owner's binding disposition,
  with every hard failure explicitly surfaced and no structural claim promoted
  into admission, activation, useful-live behavior or demonstrated reuse.

context: |
  This is the binding fresh-session KERNEL-G5 / t-3 refutation leg. The BUILD
  author and its non-binding author-assistance review do not satisfy it.

  Product repository and frozen review target:

  - github.com/ainazemtsau/solmax-operating-substrate
  - accepted BUILD base: 890a40dce8b1d7836bc48cd8db566fd7ff26383c
  - candidate content: 6ca5539a60a24d96b27cb2677e605c582f5f0161
  - final BUILD handback / reviewed-commit:
    d915789baffd13893a9fee1e7cb4b1eb74a02604
  - main and origin/main matched that HEAD when the handback checkpoint was
    verified.

  Read the product AGENTS.md, REVIEW.md, RESULT.md, validation.config, the full
  packs/process-creator/ tree, docs/results/process-creator-v1-self-check.md,
  docs/adr/ADR-0002-process-creator-materialization.md and
  openspec/changes/process-creator-v1/ before judging. Product REVIEW.md
  requires a fresh reviewer from a model family other than the BUILD author;
  record the concrete separation, or stop as blocked rather than self-certify.

  Binding Direction OS sources:

  - live/solmax/NOW.md: t-2, t-3, scope_contract, cut_list and kill_by;
  - live/solmax/work/operating-substrate/process-creator-materialization-plan-v1.md;
  - live/solmax/work/calls/c-solmax-operating-substrate-first-process-creator-t2-materialization-build-001.md;
  - live/solmax/history/2026-07-12-s-solmax-operating-substrate-first-process-creator-t1-repo-binding-repair-001.md;
  - live/solmax/work/operating-substrate/cards/operating-substrate-core-invariant-001.md;
  - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-classification-001.md;
  - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-relationship-001.md;
  - live/solmax/work/operating-substrate/cards/operating-substrate-process-pack-instantiation-001.md;
  - live/solmax/work/operating-substrate/cards/operating-substrate-shared-owner-context-001.md;
  - live/solmax/work/operating-substrate/cards/operating-substrate-persistence-history-001.md;
  - live/solmax/work/operating-substrate/cards/operating-substrate-routing-procedure-001.md.

  The BUILD report claims all 19 functions and all active t-2 promises have
  file/section evidence. It records two repaired author-assistance findings:
  F-A01 (Q2 recovery meaning missing from atomic classification) and F-A02
  (mandatory-capability rebinding mislabeled as a degraded route). Both fixes
  and their sibling sweeps are specifically in scope for refutation.

  The BUILD handback is accepted only as author evidence. The original BUILD
  open_call remains pending until this fresh review evidence and the later
  owner's actual structural verdict exist.

boundaries: |
  Review the frozen d915789 target; do not substitute a moving main snapshot.
  Do not count BUILD self-checks or author-assistance review as independent
  evidence.

  Do not admit or activate the Process Creator, perform useful-live work, claim
  demonstrated reuse, create Evidence-to-Decision as a separate pack, change
  kernel/services/adapters content, freeze Q8-Q12, add CI or semantic scanners,
  or write Direction OS state.

  Do not repair candidate semantics inside this refutation leg. A newly found
  in-scope defect produces the precise reject/block/kill disposition and a
  named repair route. Product writes are limited to recorded independent review
  evidence, the refuted register if applicable, and the closing RESULT review
  status/evidence update.

  The CALL is permission to produce refutation evidence, not an owner verdict.
  After the handback, a Solmax session must present the evidence to the owner
  and stop for the owner's actual binding disposition words.

done_when: |
  A fresh cross-family reviewer records
  docs/reviews/review-process-creator-v1.md against reviewed-commit
  d915789baffd13893a9fee1e7cb4b1eb74a02604 with file:line evidence and one
  explicit recommendation:

  - admitted and ready for bounded owner disposition;
  - rejected with a repairable process-pack defect;
  - rejected with an implementation-mapping defect;
  - blocked by one concrete named architecture gap; or
  - killed because the owner-facing creator flow is bureaucratic.

  The review attempts to refute, rather than confirm:

  - Q1-Q7 inheritance;
  - all 19 scope_contract rows and every active t-2 promise;
  - REVIEW.md items 1-10;
  - F-A01 and F-A02 fixes plus their class/sibling sweeps;
  - source and evidence sufficiency;
  - bootstrap activation authority, authoritative definition state/effect
    ownership and validated apply;
  - no silent input, no-route or capability fallback;
  - information/result/continuation integrity and active-work compatibility;
  - implementation neutrality and no consumer leakage; and
  - the owner-facing anti-bureaucracy property.

  Every finding records invariant/class, exact site, in-scope status and
  disposition. Every refuted finding carries the required G5 marker and
  REFUTED.md register entry; the report carries refuted-register: none only
  when there are zero refuted rows. A historical F-A01/F-A02 closure is accepted
  only after the reviewer verifies its fix and sibling sweep against current
  files. A hard unresolved failure prevents an admissible recommendation and
  names the current owner and route.

  The review keeps three claims separate:

  - structural_admissibility: recommended PASS or FAIL, pending owner verdict;
  - useful_live_behavior: NOT_YET_PROVEN;
  - demonstrated_substrate_reuse: NOT_YET_PROVEN.

  RESULT.md cites the recorded review evidence and states that the owner verdict,
  admission and activation remain pending. `python tools/check.py`,
  `python tools/selfcheck.py` and `python tools/check.py --deliver` are rerun at
  the review HEAD and their exact local outputs are returned. No CI evidence is
  used.

return: |
  Return one complete Direction OS engineering RESULT with:

  - reviewed-commit, review commit/final HEAD and diff summary;
  - review-evidence: docs/reviews/review-process-creator-v1.md, finding counts,
    dispositions, rounds, G5 provenance and refuted-register status;
  - the Q1-Q7, PC-01..PC-19, t-2 promise and REVIEW 1-10 reconciliation;
  - F-A01/F-A02 fix-and-sweep verification;
  - exact new finding evidence and the single recommended disposition;
  - exact local command outputs;
  - explicit structural/useful-live/reuse separation;
  - assumptions, cuts, cost, unresolved obligations and current owners; and
  - route back to Solmax for the owner-readable binding disposition.

  Do not author the next Direction OS CALL from the product repo.

budget: |
  At most 0.25 focused execution day inside the unchanged bet appetite. No
  extension, new spend or mandatory cut.

parent: s-solmax-operating-substrate-first-process-creator-t2-build-handback-checkpoint-001
surface: any

END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-first-process-creator-t3-refutation-001.md
