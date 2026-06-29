RESULT s-zara-operate-contract-repair-after-markdown-reset-001 (call: c-zara-operate-contract-repair-after-markdown-reset-001)
direction: solmax   play: repair   node/task: g-zara-operate-contract/repair

outcome: |
  Repair approved by owner and ready for mechanical writer application.

  Exact desync:
  - Direction OS NOW.md still routed g-zara-operate-contract through stale t-1
    executor work to create product-repo evidence at:
    openspec/changes/g-zara-operate-contract/acceptance-matrix.md
  - Zaratusta product repo main now contains the Markdown-only personal manager
    contract foundation merged in PR #2 at commit:
    b9c735c4b06e95e1039c35d8422e0839fd4a9e27
  - The reset removed OpenSpec/npm/TypeScript/runtime scaffold from the active
    product surface and made README.md, AGENTS.md, contracts/, examples/,
    checks/markdown-foundation-checklist.md, docs/decisions/, and docs/history/
    the current foundation.
  - Therefore NOW.next was stale and must be replaced.

  Owner approved repair option A:
  - remove stale open_call c-zara-operate-contract-t1-product-repo-matrix-evidence-002;
  - do not mark t-1 or t-2 done by repair;
  - activate t-3 as independent verification against current product repo main;
  - replace NOW.next with c-zara-operate-contract-reset-main-verify-001.

evidence: |
  Owner confirmation:
  - Owner message in-session: "repair-вариант A"

  Direction OS evidence read:
  - os/KERNEL.md: sessions do not write state directly; RESULT carries
    state_changes; done requires evidence; G5 verification applies.
  - os/plays/repair.md: repair names the contradiction, reconstructs newest-first,
    proposes corrected state, then confirms with the owner before applying.
  - live/solmax/NOW.md: active_bet b-zara-operate-contract-002 is active.
  - live/solmax/NOW.md: route_status was
    g-zara-operate-contract_active_t1_ready.
  - live/solmax/NOW.md: t-1 was active and still required product-repo acceptance
    matrix evidence mapping W20/A1-A13 without W19 HOW selection.
  - live/solmax/NOW.md: open_calls and NOW.next still routed to
    c-zara-operate-contract-t1-product-repo-matrix-evidence-002, targeting
    openspec/changes/g-zara-operate-contract/acceptance-matrix.md.
  - live/solmax/TREE.md: g-zara-operate-contract remains active with kill_by
    2026-07-05 and threshold requiring independent verification of product-repo
    evidence against A1-A13 and W19 HOW firewall.
  - live/solmax/LOG.md tail: 2026-06-28 shape activated the bet; 2026-06-29
    corrected handoff still said product-repo matrix evidence was missing and
    routed to the stale executor call.

  Product repo evidence read:
  - GitHub PR #2 metadata: [codex] Reset to Markdown-only manager foundation;
    merged=true; merged_at 2026-06-29T07:00:32Z; merge_commit_sha
    b9c735c4b06e95e1039c35d8422e0839fd4a9e27.
  - PR #2 body states the reset removed npm package files, TypeScript source,
    tests, scripts, CI workflow, OpenSpec W0/RLK files, seeded ledger, old
    RESULT/REVIEW/SPEC/PROGRESS files, and local scratch scaffold.
  - PR #2 body states the reset added Markdown foundation: README, agent contract,
    separated contracts, operating examples, manual checklist and supersession
    history.
  - README.md says Zaratusta is a Markdown-only product repo for the owner's
    personal manager contract layer and is not an app, runtime agent, API,
    database, scheduler, automation, storage engine, vendor adapter or exact
    schema.
  - README.md names the current foundation: contracts/manager-role.md,
    contracts/workspace-boundaries.md, contracts/source-context.md,
    contracts/process-contracts.md, contracts/owner-context.md,
    contracts/context-loading.md, examples/operating-examples.md and
    checks/markdown-foundation-checklist.md.
  - checks/markdown-foundation-checklist.md says no package.json, src/, tests/,
    scripts/, .github/workflows/, openspec/, features/ledger.jsonl, TypeScript
    config, lint config or executable validation is part of the active product
    surface.
  - Current fetch_file for
    openspec/changes/g-zara-operate-contract/acceptance-matrix.md on product repo
    main returned 404 Not Found.
  - Current GitHub search for "acceptance matrix" / "A1 A13 W19 W20 acceptance
    matrix" in product repo returned no results.

state_changes: |
  live/solmax/NOW.md:
  - Replace:
      route_status: g-zara-operate-contract_active_t1_ready
    with:
      route_status: g-zara-operate-contract_markdown_reset_pending_independent_verify

  - In tasks, keep t-1 status: active.

  - In tasks, replace/add t-1 progress_note with exactly:
      Repair session s-zara-operate-contract-repair-after-markdown-reset-001
      found NOW/product-repo desync after product repo PR #2 merged
      Markdown-only foundation reset at
      b9c735c4b06e95e1039c35d8422e0839fd4a9e27. The old target
      openspec/changes/g-zara-operate-contract/acceptance-matrix.md is stale
      because OpenSpec is no longer part of the active product surface. Do not
      continue c-zara-operate-contract-t1-product-repo-matrix-evidence-002.
      Current main contains Markdown foundation evidence in README.md, AGENTS.md,
      contracts/, examples/, checks/markdown-foundation-checklist.md,
      docs/decisions/0001-markdown-only-reset.md and docs/history/. Completion of
      t-1 is not claimed until independent verification decides whether current
      main sufficiently maps A1-A13 or needs a Markdown-surface executor repair.

  - In tasks, keep t-2 status: pending.

  - In tasks, add t-2 progress_note exactly:
      Product repo PR #2 appears to have materialized a Markdown manager contract
      foundation, but t-2 completion is not claimed by repair. Independent
      verification must check the current main evidence against t-2 done_when and
      the W20/A1-A13 + W19 firewall before any task is marked done.

  - In tasks, change t-3 status from pending to active.

  - In open_calls, remove the item whose id is:
      c-zara-operate-contract-t1-product-repo-matrix-evidence-002

  - In open_calls, add this item:
      id: c-zara-operate-contract-reset-main-verify-001
      to: session
      for: t-3
      issued: 2026-06-29
      note: |
        Independent verification of product repo main after PR #2 Markdown-only
        reset. This replaces the stale t-1 executor route to the removed OpenSpec
        path. Verifier must not mark t-1/t-2 done unless product-repo evidence
        satisfies their done_when and the active bet kill_by threshold. If current
        main lacks explicit A1-A13 coverage or smuggles HOW, verifier routes the
        exact repair against the current Markdown surface, not old npm/TS/OpenSpec
        scaffold.

  - Replace NOW.next with exactly this CALL:
      CALL c-zara-operate-contract-reset-main-verify-001
      to: session
      direction: solmax
      play: work
      node: g-zara-operate-contract
      task: t-3
      goal: |
        Independently verify whether Zaratusta product repo main after PR #2
        Markdown-only reset satisfies the active bet's W20/A1-A13 contract-pack
        evidence and W19 HOW firewall, or route the exact repair.
      context: |
        Active bet: b-zara-operate-contract-002.
        Product repo: github.com/ainazemtsau/zaratusta.
        Product repo reset evidence:
        - merged PR: https://github.com/ainazemtsau/zaratusta/pull/2
        - main commit / merge commit:
          b9c735c4b06e95e1039c35d8422e0839fd4a9e27
        - branch used: codex/markdown-only-foundation-reset

        Direction state:
        - live/solmax/NOW.md
        - live/solmax/TREE.md
        - live/solmax/LOG.md
        - live/solmax/work/converge-g-zara-operate-contract.md
        - live/solmax/history/2026-06-28-s-zara-operate-contract-shape-002.md
        - live/solmax/history/2026-06-29-s-zara-operate-contract-repair-after-markdown-reset-001.md

        Product repo current foundation:
        - README.md
        - AGENTS.md
        - CLAUDE.md
        - contracts/manager-role.md
        - contracts/workspace-boundaries.md
        - contracts/source-context.md
        - contracts/process-contracts.md
        - contracts/owner-context.md
        - contracts/context-loading.md
        - examples/operating-examples.md
        - checks/markdown-foundation-checklist.md
        - docs/decisions/0001-markdown-only-reset.md
        - docs/history/2026-06-16-runtime-scaffold-superseded.md

        Repair finding:
        - Previous NOW.next targeted
          openspec/changes/g-zara-operate-contract/acceptance-matrix.md.
        - That path is stale after the Markdown-only reset; OpenSpec/npm/TS/W0/RLK
          scaffold is not active.
        - Do not continue old scaffold work.
        - Do not infer t-1 or t-2 done from the merge alone.
      boundaries: |
        Do not modify Direction OS repo or product repo.
        Read product repo main and Direction OS state only.
        Do not treat old npm/TypeScript/OpenSpec/W0/RLK scaffold as active.
        Do not require a specific product-repo file layout as the only possible
        pass condition.
        Do not select UI, API, database, runtime agent, scheduler, automation,
        storage engine, vendor integration, exact schema, exact file layout or a
        generic topic/domain blacklist.
        Preserve Direction OS and other repos as read-only sources by default.
      done_when: |
        - Verdict covers t-1, t-2 and t-3 criteria against current product-repo
          main evidence.
        - PASS requires A1-A13 covered, zero hard failures on topic-open rule,
          write boundary, owner approval/side-effect boundary and W19 HOW firewall,
          no generic domain/topic blacklist, no Direction OS write path, and no
          DB/API/runtime/storage/schema/cadence/vendor/scheduler/automation chosen
          as contract.
        - FAIL names exact missing/contradictory evidence and routes:
          product artifact gap -> executor repair against current Markdown surface;
          WHAT contradiction -> converge;
          hidden HOW/layout/schema/runtime temptation -> shape/review cut, not
          silent acceptance.
        - Next route is ready: on PASS, mark verified tasks and route to shape
          g-zara-operate-state; on FAIL, route the exact repair/bounce.
      return: |
        RESULT with product repo evidence read, verdict per A1-A13/W19, task status
        recommendations for t-1/t-2/t-3, exact repair route if failed, LOG line and
        next CALL.
      budget: one focused session
      parent: s-zara-operate-contract-repair-after-markdown-reset-001
      surface: any

  live/solmax/LOG.md:
  - Append exactly this line before END_OF_FILE:
      - 2026-06-29 — repair g-zara-operate-contract: NOW.next was stale after Zaratusta PR #2 Markdown-only reset; owner approved option A; old t-1 OpenSpec acceptance-matrix executor route removed; next is independent verification of product repo main reset evidence against W20/A1-A13 and W19 HOW firewall. → history/2026-06-29-s-zara-operate-contract-repair-after-markdown-reset-001.md

  live/solmax/history/:
  - Add this RESULT as:
      live/solmax/history/2026-06-29-s-zara-operate-contract-repair-after-markdown-reset-001.md

captures:
  - Product repo reset may have replaced the separate A1-A13 acceptance matrix with a manual foundation checklist; verifier should decide whether explicit A-row coverage is still missing or sufficiently represented.
  - Future executor calls after product reset should target the current Markdown surface and avoid naming removed OpenSpec paths.
  - This desync came from product-repo main changing after a Direction OS executor handoff; pulse/review may later need a guard that product-repo reset commits trigger Direction OS repair before continuing open_calls.

decisions_needed: []

play_check:
  - "1 Name the contradiction: done — NOW.next/open_call/t-1 target an OpenSpec acceptance-matrix route; product repo main is now Markdown-only reset where OpenSpec/npm/TS scaffold is not active."
  - "2 Reconstruct: done — read NOW.md, TREE.md, LOG.md tail, recent history, PR #2 metadata/diff evidence and current product repo Markdown foundation files."
  - "3 Propose corrected state: done — proposed NOW/LOG repair removes stale open_call, adds current-main verification open_call, activates t-3 verification and supplies a next CALL against current main reset evidence."
  - "4 Confirm: done — owner approved in-session: \"repair-вариант A\"."
  - "5 Friction: skipped — this appears to be a one-off product-repo reset overtaking an open Direction OS call; captured for later if it recurs."

log: |
  repair g-zara-operate-contract: NOW/product-repo desync after Zaratusta PR #2 Markdown-only reset repaired by owner-approved option A; stale OpenSpec executor route replaced with independent current-main verification.

next: |
  CALL c-zara-operate-contract-reset-main-verify-001
  to: session
  direction: solmax
  play: work
  node: g-zara-operate-contract
  task: t-3
  goal: |
    Independently verify whether Zaratusta product repo main after PR #2
    Markdown-only reset satisfies the active bet's W20/A1-A13 contract-pack
    evidence and W19 HOW firewall, or route the exact repair.
  context: |
    Active bet: b-zara-operate-contract-002.
    Product repo: github.com/ainazemtsau/zaratusta.
    Product repo reset evidence:
    - merged PR: https://github.com/ainazemtsau/zaratusta/pull/2
    - main commit / merge commit:
      b9c735c4b06e95e1039c35d8422e0839fd4a9e27
    - branch used: codex/markdown-only-foundation-reset

    Direction state:
    - live/solmax/NOW.md
    - live/solmax/TREE.md
    - live/solmax/LOG.md
    - live/solmax/work/converge-g-zara-operate-contract.md
    - live/solmax/history/2026-06-28-s-zara-operate-contract-shape-002.md
    - live/solmax/history/2026-06-29-s-zara-operate-contract-repair-after-markdown-reset-001.md

    Product repo current foundation:
    - README.md
    - AGENTS.md
    - CLAUDE.md
    - contracts/manager-role.md
    - contracts/workspace-boundaries.md
    - contracts/source-context.md
    - contracts/process-contracts.md
    - contracts/owner-context.md
    - contracts/context-loading.md
    - examples/operating-examples.md
    - checks/markdown-foundation-checklist.md
    - docs/decisions/0001-markdown-only-reset.md
    - docs/history/2026-06-16-runtime-scaffold-superseded.md

    Repair finding:
    - Previous NOW.next targeted
      openspec/changes/g-zara-operate-contract/acceptance-matrix.md.
    - That path is stale after the Markdown-only reset; OpenSpec/npm/TS/W0/RLK
      scaffold is not active.
    - Do not continue old scaffold work.
    - Do not infer t-1 or t-2 done from the merge alone.
  boundaries: |
    Do not modify Direction OS repo or product repo.
    Read product repo main and Direction OS state only.
    Do not treat old npm/TypeScript/OpenSpec/W0/RLK scaffold as active.
    Do not require a specific product-repo file layout as the only possible
    pass condition.
    Do not select UI, API, database, runtime agent, scheduler, automation,
    storage engine, vendor integration, exact schema, exact file layout or a
    generic topic/domain blacklist.
    Preserve Direction OS and other repos as read-only sources by default.
  done_when: |
    - Verdict covers t-1, t-2 and t-3 criteria against current product-repo
      main evidence.
    - PASS requires A1-A13 covered, zero hard failures on topic-open rule,
      write boundary, owner approval/side-effect boundary and W19 HOW firewall,
      no generic domain/topic blacklist, no Direction OS write path, and no
      DB/API/runtime/storage/schema/cadence/vendor/scheduler/automation chosen
      as contract.
    - FAIL names exact missing/contradictory evidence and routes:
      product artifact gap -> executor repair against current Markdown surface;
      WHAT contradiction -> converge;
      hidden HOW/layout/schema/runtime temptation -> shape/review cut, not
      silent acceptance.
    - Next route is ready: on PASS, mark verified tasks and route to shape
      g-zara-operate-state; on FAIL, route the exact repair/bounce.
  return: |
    RESULT with product repo evidence read, verdict per A1-A13/W19, task status
    recommendations for t-1/t-2/t-3, exact repair route if failed, LOG line and
    next CALL.
  budget: one focused session
  parent: s-zara-operate-contract-repair-after-markdown-reset-001
  surface: any
END_OF_FILE: live/solmax/history/2026-06-29-s-zara-operate-contract-repair-after-markdown-reset-001.md
