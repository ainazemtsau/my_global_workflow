CALL c-solmax-operating-substrate-first-process-creator-t4-health-reclamation-v22-resync-recovery-013
to: executor
direction: solmax
node: g-operating-substrate-first-process-creator
task: t-4
repo: C:/projects/solmax-operating-substrate
kind: engineering

goal: |
  The operating-substrate product has a clean, reviewable contract-v22
  recovery candidate whose Health Reclamation content is still at the
  pre-F-HR-R01-repair basis, while the v21 repair attempt remains reachable
  and explicitly non-authoritative, so later work can enter the required
  artifact-backed RED path without losing progress.

context: |
  Work in the product repository at:
  C:/projects/solmax-operating-substrate

  Freshly observed state before this CALL was issued:
  - clean branch codex/health-reclamation-candidate-build;
  - current HEAD:
    3af27e66e88b764c702d53c3279cb1352cd4d134;
  - repair-content commit:
    f77ad75c737b89685df3771c859bc49b51946f7c;
  - pre-repair reviewed basis:
    b23eb0bb208a6b2344043ac472621093132dadc9;
  - product validation.config: synced_contract_version 21;
  - Direction os/engineering/CONTRACT_VERSION: current 22.

  Contract v22 landed in Direction commit
  d18be6e779533932d59383834801dcb0ba850514 on 2026-07-14, before the
  product commits above were created on 2026-07-15. CALL 010 required exact
  contract v21 and fail-fast on drift, so its product handoff was bounced and
  did not close F-HR-R01.

  Current v22 authorities:
  - C:/my_global_workflow_worktrees/solmax/os/engineering/CONTRACT_VERSION
    log entry 22;
  - C:/my_global_workflow_worktrees/solmax/os/engineering/PROJECT_SETUP.md
    section Re-sync and current Done-when;
  - C:/my_global_workflow_worktrees/solmax/os/engineering/CONTOUR.md;
  - C:/my_global_workflow_worktrees/solmax/os/engineering/VALIDATION.md;
  - C:/my_global_workflow_worktrees/solmax/os/engineering/profiles/markdown-substrate.md.

  Product authorities and evidence:
  - root AGENTS.md and packs/AGENTS.md;
  - validation.config;
  - docs/FRICTION.md;
  - openspec/ guidance and templates;
  - tools/check.py and tools/selfcheck.py;
  - docs/reviews/review-health-reclamation-v1.md;
  - docs/results/health-reclamation-v1-self-check.md;
  - packs/health-reclamation/verification/scope-coverage.md;
  - RESULT.md and git history at b23eb0b, f77ad75 and 3af27e6.

  The owner approved the recovery route after the writer surfaced the drift:
  "Сделай этот репейр."

  The original owner-approved F-HR-R01 contour remains unchanged: only the
  OP-HR01 and KH-HR01 Q2 classifications may eventually be corrected, with
  all prior Health Reclamation progress preserved. This CALL does not perform
  that correction.

boundaries: |
  Work only in C:/projects/solmax-operating-substrate. Do not write Direction
  OS state.

  This is one product §Re-sync and recovery-baseline candidate leg. Do not
  perform the OP-HR01 or KH-HR01 repair, author the later RED-FREEZE artifact,
  review or accept the repaired candidate, admit or activate Health
  Reclamation, invoke or run the process, or perform an external effect.

  Preserve f77ad75 and 3af27e6 as reachable evidence. Do not delete, rewrite,
  squash or conceal their history, and do not describe them as accepted,
  delivered, structural PASS or authoritative.

  The recovery candidate must retain the pre-repair Health Reclamation
  semantics from b23eb0b. Contract re-sync may change repo-local workflow,
  validation, friction and report surfaces, but not Health behavior, policy,
  routing, procedures, scenarios, classifications, research or owner intent.

  Translate contract v22 honestly for the markdown/procedure substrate. Do
  not create a semantic parser, regex/content scanner, schema compiler,
  conformance proxy, fake compiled-code test layer, new dependency or CI.
  Python remains limited to concrete wiring checks. The existing owner choice
  of in-loop local validation and no CI remains binding.

  Do not read, import or cite legacy Direction Health, Health AI, Health HQ or
  live/health as authority. Do not request health information, research or a
  repeated process description. No personal health data may enter the repo or
  report.

  Before mutation, require a clean worktree and verify that b23eb0b, f77ad75
  and 3af27e6 remain reachable. If a clean pre-repair recovery basis cannot be
  produced without losing those commits, changing Health semantics or
  exceeding the fixed appetite, return one exact BLOCKED reason without a
  partial candidate.

done_when: |
  A committed, clean product candidate is ready for a separate fresh
  read-only refutation of the v22 re-sync and recovery containment. It is not
  accepted merely because the author checks pass.

  validation.config records synced_contract_version 22. Every repo-local
  workflow authority affected by v22 consistently requires:
  - PLAN, RED-FREEZE, binding artifact-backed RED refutation and BUILD as
    separate sessions;
  - every mixed obligation split and every atomic obligation classified once
    as behavioral-red or evidence-only;
  - only behavioral-red obligations in the test numerator;
  - one immutable independent test/test-support RED commit and exact real
    command diagnostics before BUILD;
  - a fresh review that tries to refute that committed artifact;
  - BUILD pinned to and reusing the reviewed RED commit without rewriting it;
  - prose tables, skeleton counts, semantic dry-runs and partial suites never
    acting as BUILD authority.

  The markdown-substrate translation remains honest: semantic meaning is
  judged by the AI author, fresh reviewer and owner, never by a new script.
  Code-only gates remain explicitly n/a where they truly have no subject, and
  concrete repository checks have a seeded-miss/negative-control where v22
  makes one applicable. No semantic proxy or CI is introduced.

  Product docs/FRICTION.md records the v21-after-v22 execution drift and the
  bounded §Re-sync response. The repo's current guidance no longer presents
  the v21 prose RED_READY route as authority for later product mutation.

  At the recovery candidate HEAD:
  - packs/health-reclamation/** is byte-equivalent to b23eb0b;
  - docs/results/health-reclamation-v1-self-check.md is byte-equivalent to
    b23eb0b;
  - docs/reviews/review-health-reclamation-v1.md remains blob
    41d1c21d38113a7ab44aafd64deef4e06278d3cd;
  - review 007 remains historical OPEN/BLOCKING structural FAIL evidence;
  - OP-HR01 and KH-HR01 remain at the pre-repair basis pending a legitimate
    later RED-FREEZE/review/repair chain;
  - no Health behavior, policy, procedure, scenario, owner-input or research
    artifact changed.

  f77ad75 and 3af27e6 remain reachable through durable git refs and are named
  in RESULT.md only as non-authoritative attempted-repair evidence. The return
  gives exact reachability commands and results.

  The candidate diff is limited to the repo-local v22 §Re-sync, recovery
  containment, friction and current handoff surfaces. It contains no Health
  pack change and no kernel, Process Creator, service or adapter semantic
  change.

  This author leg is explicitly a light contract/recovery candidate with no
  frozen feature change. Its returned evidence carries the exact line:
  `review: n/a — light change`, followed by an explicit
  `AWAITING_SEPARATE_FRESH_REFUTATION` status. A later Direction session owns
  the fresh review CALL; this executor does not author it.

  At the final candidate HEAD all commands exit zero and exact output is
  recorded:
  - python tools/check.py
  - python tools/selfcheck.py
  - python tools/check.py --deliver

  Product status remains candidate-only, not admitted, not activated, not
  run, not useful-live-proven, not reliability-proven and not reuse-proven.
  Direction t-4 and appetite are not changed by the product executor.

return: |
  Return one complete Direction OS engineering RESULT containing:

  - starting refs, branch/worktree identity, recovery candidate commit/HEAD,
    ancestry and clean-status evidence;
  - exact changed paths and complete hunk-level containment;
  - a line-by-line mapping of contract v22 into the product authorities and
    the honest markdown-substrate gate translation;
  - validation.config v22 evidence and any concrete seeded-miss result;
  - exact byte/tree comparison proving the named Health surfaces equal
    b23eb0b and review 007 remains unchanged;
  - exact reachability evidence for f77ad75 and 3af27e6 plus their explicit
    non-authoritative disposition;
  - exact output and exit status for all three repository commands;
  - `review: n/a — light change` and
    `AWAITING_SEPARATE_FRESH_REFUTATION`;
  - sources used, legacy-Health exclusion, no-personal-data statement,
    assumptions, cuts, cost and fixed-appetite assessment;
  - explicit no-repair/no-admission/no-activation/no-run/no-useful-live/
    no-reliability/no-reuse statement; and
  - return-to-parent Solmax for a separate fresh read-only refutation of the
    re-sync candidate before any RED-FREEZE leg is commissioned.

  Do not author the downstream Direction CALL from the product repository.

budget: |
  One bounded executor checkpoint using only whatever remains inside the
  already-fixed three-focused-day bet appetite. No new reserve and no
  extension. If this leg cannot complete without exceeding that fixed
  appetite, return BLOCKED before mutation.

parent: s-solmax-operating-substrate-first-process-creator-t4-health-reclamation-v22-route-repair-012
surface: codex

END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-first-process-creator-t4-health-reclamation-v22-resync-recovery-013.md
