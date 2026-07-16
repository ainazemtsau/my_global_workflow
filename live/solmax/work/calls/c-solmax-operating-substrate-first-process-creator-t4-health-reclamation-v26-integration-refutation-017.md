CALL c-solmax-operating-substrate-first-process-creator-t4-health-reclamation-v26-integration-refutation-017
to: session
direction: solmax
play: work
node: g-operating-substrate-first-process-creator
task: t-4

goal: |
  The terminal-contract-v26 Health Reclamation integration candidate has one
  binding evidence-backed PASS or FAIL disposition and Solmax has one
  trustworthy route forward from that exact committed product state.

context: |
  Run in a NEW Codex task/session. This CALL is self-contained; do not rely on
  the task that performed the Re-sync or merge.

  Direction state and current engineering authority:
  - C:/my_global_workflow_worktrees/solmax/live/solmax/NOW.md
  - C:/my_global_workflow_worktrees/solmax/live/solmax/TREE.md
  - C:/my_global_workflow_worktrees/solmax/live/solmax/CHARTER.md
  - C:/my_global_workflow_worktrees/solmax/os/engineering/CONTRACT_VERSION
  - C:/my_global_workflow_worktrees/solmax/os/engineering/PROJECT_SETUP.md
  - C:/my_global_workflow_worktrees/solmax/os/engineering/CONTOUR.md
  - C:/my_global_workflow_worktrees/solmax/os/engineering/VALIDATION.md
  - C:/my_global_workflow_worktrees/solmax/os/engineering/
    OBLIGATION_INVENTORY.md
  - C:/my_global_workflow_worktrees/solmax/os/engineering/profiles/
    markdown-substrate.md

  Product repository:
  C:/projects/solmax-operating-substrate-v26-integration

  Exact product identities:
  - integration branch:
    codex/health-reclamation-v26-integration-candidate
  - integration HEAD:
    7ed7903045bef2c4b49124c61b98c9ebf3e7232a
  - first parent / unchanged active remote basis:
    3ee6914fd4973ebe947cb89c37f0f144cfdafdee
  - second parent / terminal-v26 product main:
    7bbc73d725f6d82028bde396d7764ec13145f977
  - Direction v26 source:
    2a46d7753ea9463df5b07513bab330f870202768
  - pre-repair Health basis:
    b23eb0bb208a6b2344043ac472621093132dadc9
  - historical non-authoritative repair commits:
    f77ad75c737b89685df3771c859bc49b51946f7c and
    3af27e66e88b764c702d53c3279cb1352cd4d134
  - product closing evidence: RESULT.md at integration HEAD

  Expected Health objects, all inherited unchanged from 3ee6914:
  - packs/health-reclamation tree:
    e0fc759293422fc63cfd630f409e11bbe0efd70b
  - openspec/changes/health-reclamation-v1 tree:
    a0bc445f8b1585b224fb997813740519cb1d297b
  - openspec/changes/health-reclamation-f-hr-r01-repair tree:
    cfd4d48ca2b9c3fd1eb515b1e15b82a8862158e9
  - docs/adr/ADR-0003-health-reclamation-materialization.md blob:
    a8a4a97e087b2fe76662d5cdce158de8f5ec9032
  - docs/results/health-reclamation-v1-self-check.md blob:
    c6d3cfc5742bbaf7a89493fe38e4266e993a918b
  - docs/reviews/review-health-reclamation-v1.md blob:
    41d1c21d38113a7ab44aafd64deef4e06278d3cd
  - historical v22 handoff-template blob:
    72a9b8e59c3dd0c6c9d73c9fb67e5b8b66870813

  Direction CALLs 013 and 016 were pinned to contract v22. The owner's live
  instruction superseded them after terminal v26 Re-sync; they are history,
  not authority for this review or any later BUILD.

boundaries: |
  Read-only review. Do not modify either repository.

  Do not execute CALL 013 or CALL 016, restore the retired v22 carrier, perform
  OP-HR01/KH-HR01 repair, continue F-HR-R01 BUILD, admit or activate Health
  Reclamation, run the process, perform an external effect, close t-4, change
  appetite, or promote useful-live, reliability or reuse claims.

  Do not use legacy Direction Health, Health AI, Health HQ or live/health as
  authority. Do not request, read or expose personal health information.

  Treat the product RESULT, green commands, merge commit and prior reviews as
  claims to attack. Honest markdown N/A is allowed only where the compiled
  product-code or eligible G2 source subject is actually absent.

  No owner verdict is requested.

done_when: |
  A fresh session returns exactly one binding verdict:

  - PASS: integration HEAD 7ed7903 faithfully contains terminal product main
    v26, honestly applies every applicable v23-v26 Re-sync disposition, and
    leaves Health Reclamation feature semantics/artifacts unchanged; or
  - FAIL: every defect names authority, exact path/line or Git evidence,
    consequence and one bounded repair.

  PASS requires evidence for every cluster:

  1. Exact branch, clean status, HEAD 7ed7903 and its two ordered parents.
  2. Both 7bbc73d and 3ee6914 are ancestors; f77ad75, 3af27e6 and b23eb0b
     remain reachable; the original remote Health branch still points to
     3ee6914.
  3. `validation.config` records contract and inventory version 26, ceiling
     239 and source 2a46d77; that source resolves to current 26 and inventory
     blob 811163dca06656a06d589e92ba397f71c6bd2583.
  4. V23 compiled SURFACE-FREEZE is explicit N/A only because no compiled
     product-code/compiler subject exists; v24 mutation scope/diff identity is
     explicit N/A only because no eligible G2 compiled source exists.
  5. Current root and nearest-wins authorities contain the terminal markdown
     route, not the retired v22 RED-FREEZE carrier. The committed v22 template
     and repair-plan artifacts remain byte-identical historical evidence and
     cannot launch BUILD.
  6. The first-parent diff contains only AGENTS.md, packs/AGENTS.md, REVIEW.md,
     openspec/README.md, validation.config, docs/FRICTION.md, tools/check.py,
     tools/selfcheck.py and RESULT.md.
  7. All named Health trees/blobs equal the expected values above; a direct
     3ee6914..HEAD diff over README.md, packs/README.md, the Health pack,
     both Health OpenSpec trees, the Health ADR, self-check and review is empty.
  8. Fresh reruns exit zero with exact output:
     - python tools/check.py
     - python tools/selfcheck.py
     - python tools/check.py --deliver
  9. Product status remains candidate-only: no repair, admission, activation,
     process run, useful-live proof, reliability proof or reuse proof.

  The RESULT identifies this as binding fresh-session KERNEL-G5, not an
  in-session pre-pass.

  Routing is executable:
  - on PASS, clear CALL 017 with the binding evidence and return one complete
    standalone v26-based Direction CALL for the next bounded pre-BUILD Health
    disposition; no BUILD starts unless that later CALL explicitly authorizes
    it under current authority;
  - on FAIL, clear CALL 017 with the binding failure evidence and return one
    complete standalone bounded repair CALL.

return: |
  Return one complete Direction OS RESULT with PASS or FAIL, attempted
  refutations, exact refs/paths/lines/hashes/outputs, lifecycle limits,
  binding-fresh-session status, exact NOW state_changes preserving t-4 and
  appetite, and one complete self-contained next CALL.

budget: |
  One bounded fresh read-only refutation inside the already-fixed appetite.
  No new reserve and no extension.

surface: codex

END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-first-process-creator-t4-health-reclamation-v26-integration-refutation-017.md
