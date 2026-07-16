RESULT s-solmax-operating-substrate-first-process-creator-t4-terminal-v26-resync-checkpoint-017 (call: owner-direct-terminal-v26-resync-017)
direction: solmax   play: work   node/task: g-operating-substrate-first-process-creator/t-4

outcome: |
  Product main and the active Health Reclamation leg now have non-rewriting
  terminal engineering-contract-v26 lineage.

  Product origin/main advanced from v25 commit 66c6c43 to v26 commit 7bbc73d.
  A separate integration candidate was created from exact remote active HEAD
  3ee6914 and merged v26 main as second parent at 7ed7903; both product branches
  are pushed and the original active remote branch remains unchanged.

  The v22-pinned Direction CALLs 013 and 016 are obsolete under the owner's
  live Re-sync instruction. They leave the pending registry as superseded, not
  completed, and one self-contained v26 binding refutation CALL 017 is ready.

  Direction t-4 remains active. Appetite, Health semantics, admission,
  activation, process execution and all useful-live/reliability/reuse limits
  are unchanged. Feature BUILD remains stopped.

evidence: |
  Product main Re-sync:
  - isolated clean worktree:
    C:/projects/solmax-operating-substrate-resync-v25;
  - old origin/main and commit parent:
    66c6c431b81b0d688f305a2c8004d74accfd67f3;
  - v26 main commit, local and remote:
    7bbc73d725f6d82028bde396d7764ec13145f977;
  - its changed paths are only RESULT.md, docs/FRICTION.md and
    validation.config.

  Product active-leg integration:
  - source remote branch remained
    codex/health-reclamation-candidate-build at
    3ee6914fd4973ebe947cb89c37f0f144cfdafdee;
  - new pushed branch:
    codex/health-reclamation-v26-integration-candidate;
  - integration HEAD, local and remote:
    7ed7903045bef2c4b49124c61b98c9ebf3e7232a;
  - ordered parents:
    3ee6914fd4973ebe947cb89c37f0f144cfdafdee and
    7bbc73d725f6d82028bde396d7764ec13145f977;
  - ancestry checks returned exit 0 for 7bbc73d, 3ee6914, f77ad75, 3af27e6
    and b23eb0b;
  - first-parent diff has exactly nine workflow/report paths: AGENTS.md,
    packs/AGENTS.md, REVIEW.md, openspec/README.md, validation.config,
    docs/FRICTION.md, tools/check.py, tools/selfcheck.py and RESULT.md.

  Contract-v26 provenance and terminal dispositions:
  - Direction source 2a46d7753ea9463df5b07513bab330f870202768
    resolves to `current: 26`;
  - its OBLIGATION_INVENTORY blob is
    811163dca06656a06d589e92ba397f71c6bd2583 with N=239;
  - product validation.config records synced_contract_version 26,
    obligation_inventory_version 26, obligation_ceiling 239 and that exact
    source commit;
  - v23 compiled SURFACE-FREEZE is explicit N/A: the tracked tree contains no
    compiled product-source candidate;
  - v24 mutation scope/diff identity is explicit N/A: no eligible G2 compiled
    source exists and no mutation run was claimed;
  - current root and nearest-wins authorities no longer use the retired v22
    RED-FREEZE carrier; its committed template/repair artifacts remain history.

  Health Reclamation containment at 7ed7903:
  - direct diff from 3ee6914 over README.md, packs/README.md, all Health pack
    files, both Health OpenSpec trees, the Health ADR, self-check and review is
    empty (exit 0);
  - packs/health-reclamation tree:
    e0fc759293422fc63cfd630f409e11bbe0efd70b;
  - health-reclamation-v1 OpenSpec tree:
    a0bc445f8b1585b224fb997813740519cb1d297b;
  - F-HR-R01 repair OpenSpec tree:
    cfd4d48ca2b9c3fd1eb515b1e15b82a8862158e9;
  - Health ADR blob: a8a4a97e087b2fe76662d5cdce158de8f5ec9032;
  - Health self-check blob:
    c6d3cfc5742bbaf7a89493fe38e4266e993a918b;
  - Health review blob:
    41d1c21d38113a7ab44aafd64deef4e06278d3cd;
  - historical v22 handoff-template blob:
    72a9b8e59c3dd0c6c9d73c9fb67e5b8b66870813.

  Fresh final product commands at both v26 main and integration candidate:
  - `python tools/check.py` ->
    `GATE: PASS (inner-loop; 6 concrete checks, 0 failures)`;
  - `python tools/selfcheck.py` -> all 12 probes ok, `SELFCHECK: PASS`;
  - `python tools/check.py --deliver` ->
    `GATE: PASS (deliver; 7 concrete checks, 0 failures)`;
  - `git diff --check` -> exit 0 with no output.

  Direction worktree authority was merged non-rewriting to v26 at
  5d415045c575e2703139e82af718279788f38d58, with parents 94bcc6d and
  2a46d77; local alternative v24 history remains reachable while current
  os/engineering and writer consumers equal published v26.

  Owner live instruction contained the exact terms "terminal Re-sync",
  "feature BUILD" and "v26-based Direction CALL". This checkpoint implements
  that routing: the old v22 calls are superseded, t-4 stays active, and BUILD
  remains stopped pending CALL 017 and its binding result.

  review: n/a - light change

state_changes: |
  Applied against fresh NOW.md base blob
  50ab3c1259233fdb6b6e55e6eceb5523eb587b49 after Direction v26 merge
  5d415045c575e2703139e82af718279788f38d58:

  - NOW.md route_status: set
    operating_substrate_first_process_creator_t4_health_reclamation_v22_resync_recovery_pending
    ->
    operating_substrate_first_process_creator_t4_health_reclamation_v26_integration_refutation_pending.
  - NOW.md open_calls: remove v22-pinned pending ids 013 and 016 as explicitly
    owner-superseded; neither is marked done and both remain in history.
  - NOW.md open_calls: add pending
    c-solmax-operating-substrate-first-process-creator-t4-health-reclamation-v26-integration-refutation-017.
  - Create the complete self-contained CALL artifact at
    live/solmax/work/calls/c-solmax-operating-substrate-first-process-creator-t4-health-reclamation-v26-integration-refutation-017.md.
  - Set NOW.next to that CALL artifact.
  - NOW.md task t-4: preserve status active, budget, goal, done_when and
    rollback unchanged.
  - NOW.md active_bet: preserve status, appetite, allocation, kill_by and
    extension_allowed false unchanged.
  - No TREE.md, CHARTER.md, task status, appetite, Health lifecycle or product
    feature change.

captures: []

decisions_needed: []

play_check:
  - '1 Recite: done - terminal v26 Re-sync and checkpoint/reissue serve active bet g-operating-substrate-first-process-creator/t-4; v22 CALL 016 is obsolete rather than runnable.'
  - '2 Owner inputs: skipped - this is engineering routing, not owner-content; owner authority is the live instruction using the exact terms "terminal Re-sync", "feature BUILD" and "v26-based Direction CALL".'
  - '3 Do the work: done - product main v26 commit 7bbc73d and non-rewriting integration merge 7ed7903 were committed, validated and pushed; Direction v26 authority was merged at 5d41504.'
  - '4 Self-check: done - ancestry, provenance, v23/v24 dispositions, nine-path containment, byte-identical Health objects, clean status and all three repository gates were checked first-hand.'
  - '5 Close: done - checkpoint preserves t-4/appetite/lifecycle, supersedes v22 calls without marking them done, and opens only fresh read-only v26 CALL 017; no BUILD continuation.'

log: - 2026-07-16 - work t-4 terminal v26 Re-sync checkpoint (s-solmax-operating-substrate-first-process-creator-t4-terminal-v26-resync-checkpoint-017): product main 7bbc73d and Health integration candidate 7ed7903 are pushed on contract v26 with unchanged Health artifacts; v22 CALLs 013/016 are superseded, t-4/appetite stay active, and binding v26 CALL 017 is next. -> history/2026-07-16-s-solmax-operating-substrate-first-process-creator-t4-terminal-v26-resync-checkpoint-017.md

next: |
  live/solmax/work/calls/c-solmax-operating-substrate-first-process-creator-t4-health-reclamation-v26-integration-refutation-017.md

END_OF_FILE: live/solmax/history/2026-07-16-s-solmax-operating-substrate-first-process-creator-t4-terminal-v26-resync-checkpoint-017.md
