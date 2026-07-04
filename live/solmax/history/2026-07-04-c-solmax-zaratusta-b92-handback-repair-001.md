RESULT c-solmax-zaratusta-b92-handback-repair-001 (call: c-solmax-zaratusta-b92-handback-repair-001)
direction: solmax   play: repair   node/task: g-zara-operate/repair

outcome: |
  Reconciled first-hand product evidence b92de14/469e699 against current
  solmax state without marking any Direction OS task done.

  Repair verdict:
  - Product evidence is real: Zaratusta main is b92de14eedda436e06a6de457f50aae483b7c631,
    and the product history includes 469e6996ea120073168bf350d54cf8e56135f30d
    ("Add Markdown operating manager v1 surface").
  - Product evidence is not writer-applicable Direction OS state by itself.
  - Current live/solmax has no matching active_bet task or open_call for
    c-zara-operate-markdown-manager-v1-t2-001 / operating-manager-v1.
  - The product-authored next CALL id is not accepted as authoritative.
  - The safe repair outcome is to record b92/469 as untracked product evidence
    requiring owner decision before route/state import.

evidence: |
  Direction OS state checked first-hand:
  - live/solmax/NOW.md:
    - active_bet.status is none.
    - tasks is [].
    - recurring is [].
    - decisions contains open D-zara-operate-next-bet-001.
    - open_calls is [].
    - preserved_evidence does not include b92de14/469e699 operating-manager-v1 evidence.
    - next is work/calls/c-zara-operate-state-shape-001.md.
  - live/solmax/work/calls/c-zara-operate-state-shape-001.md:
    - CALL is for play shape on node g-zara-operate-state.
    - Activation condition says run only after owner resolves
      D-zara-operate-next-bet-001 with option A.
  - live/solmax/TREE.md:
    - g-zara-operate-contract is done.
    - g-zara-operate-state, g-zara-operate-runtime and
      g-zara-operate-evolution remain parked.
  - live/solmax/LOG.md:
    - latest applied solmax entry is the 2026-07-02 review-bounce repair
      closing g-zara-operate-contract and opening the next-bet decision.

  Product repo checked first-hand, read-only:
  - GitHub compare b92de14eedda436e06a6de457f50aae483b7c631..main returned
    identical; b92de14 is current Zaratusta main.
  - GitHub compare 469e6996ea120073168bf350d54cf8e56135f30d..b92de14 returned
    status ahead by 2, behind by 0; b92de14 includes that product line.
  - GitHub compare 79578ac87c73591000409f9f82a3bb4d0e33aa5b..b92de14 returned
    status ahead by 2, behind by 0; b92de14 also includes the previously
    verified contract evidence line.
  - Commit 469e6996ea120073168bf350d54cf8e56135f30d message:
    "Add Markdown operating manager v1 surface".
  - Commit b92de14eedda436e06a6de457f50aae483b7c631 message:
    "Merge remote-tracking branch 'origin/main'"; conflicts in README.md and
    checks/markdown-foundation-checklist.md resolved in the merge.
  - Product files read at b92de14:
    - README.md.
    - AGENTS.md.
    - checks/markdown-foundation-checklist.md.
    - checks/w20-a1-a13-acceptance-map.md.
    - contracts/operating-manager-v1.md.
    - contracts/operating-manager-v1-source-basis.md.
    - docs/decisions/0002-operating-manager-v1-surface.md.
  - Product evidence substance:
    - README.md now lists operating-manager-v1.md,
      operating-manager-v1-source-basis.md, examples, W20/A1-A13 map,
      manual checklist and decision 0002 as current foundation.
    - README.md says the repo is not app/runtime/API/database/scheduler/
      automation/storage engine/vendor adapter/exact schema.
    - operating-manager-v1.md defines a Markdown process contract, not runtime
      code, storage architecture, automation, UI, API or permanent file layout.
    - operating-manager-v1.md state touchpoints are required meanings/interfaces
      only, not exact permanent storage file/schema/database/future layout.
    - decision 0002 says the v1 surface is accepted for the current Markdown
      product surface and future runtime/storage/UI/automation/integration work
      remains a separate owner-approved route.
    - AGENTS.md still ends with "return changed files plus commit or PR evidence
      and the relevant manual check output"; it does not yet carry the v10
      Direction OS product-handback contract.

  Maintenance evidence checked first-hand:
  - my_global_workflow commit 217ab671cd6fac4c6724bc78eebed5028a23b6ae
    added product-handback bridge v10.
  - Its maintenance text says product-repo exit reports are evidence, not
    writer-applicable state packets.
  - It specifically says current Zaratusta result b92de14/469e699 is not
    writer-applicable and must route through repair/carry-back to reconcile
    against live/solmax before any state update.

state_changes: |
  Apply the following exact Direction OS state changes.

  1) live/solmax/NOW.md

  Do not change active_bet.status.
  Do not add tasks.
  Do not mark any task done.
  Do not change TREE.md.
  Do not accept c-zara-operate-markdown-manager-v1-t2-001 as NOW.next or open_call.

  In live/solmax/NOW.md, replace:

      route_status: g-zara-operate-contract_done_next_bet_decision_open

  with:

      route_status: g-zara-operate-contract_done_b92_product_evidence_untracked_awaiting_owner_decision

  In live/solmax/NOW.md, under decisions, keep the existing
  D-zara-operate-next-bet-001 item unchanged, then append this new decision item:

      - id: D-zara-operate-b92-handback-001
        status: open
        created: 2026-07-04
        q: |
          How should Direction OS treat the untracked Zaratusta product evidence
          b92de14/469e699 for Markdown operating-manager-v1?
        facts: |
          Current live/solmax state has active_bet.status none, tasks [],
          open_calls [], open D-zara-operate-next-bet-001, and NOW.next pointing
          to work/calls/c-zara-operate-state-shape-001.md, which is conditional
          on owner choosing option A for g-zara-operate-state.

          Product repo main is b92de14eedda436e06a6de457f50aae483b7c631.
          Product commit 469e6996ea120073168bf350d54cf8e56135f30d adds the
          Markdown operating-manager-v1 surface. Product files at b92 include:
          README.md, AGENTS.md, checks/markdown-foundation-checklist.md,
          checks/w20-a1-a13-acceptance-map.md,
          contracts/operating-manager-v1.md,
          contracts/operating-manager-v1-source-basis.md, and
          docs/decisions/0002-operating-manager-v1-surface.md.

          The product evidence says Operating Manager v1 is a Markdown process
          surface and explicitly does not choose runtime code, storage
          architecture, UI, API, database, automation, vendor, scheduler,
          external integration, exact schema or exact future layout. State
          touchpoints are meanings/interfaces only, not durable-state
          implementation.

          Maintenance commit 217ab671 (product-handback bridge v10) says product
          repo exit reports are evidence, not writer-applicable state packets.
          It specifically classifies current b92de14/469e699 as not
          writer-applicable and requiring repair/carry-back before any state
          update.

          Therefore b92/469 cannot close any Direction OS task by itself and the
          product-authored next CALL c-zara-operate-markdown-manager-v1-t2-001
          is not authoritative.
        terms: |
          untracked evidence = real product repo change that is not currently
            tied to a live/solmax active task/open_call.
          carry-back = a Direction OS session verifies/reconciles product report
            evidence and emits an OS RESULT with state_changes.
          accepted evidence = product evidence preserved for later OS use; this
            is not the same as marking a task or bet done.
          route-changing owner correction = an owner decision that changes which
            child/node should be shaped next.
        options:
          - |
            A (recommended): record b92/469 as accepted untracked evidence for
            future shaping/review, but do not mark any task done and do not
            change TREE. Keep D-zara-operate-next-bet-001 as the governing
            next-bet decision; if owner chooses state, b92/469 becomes source
            input, not proof that durable state is done.
            bad_because: the already-created operating-manager-v1 surface is not
              immediately promoted into the active route.
          - |
            B: treat b92/469 plus the product decision text as a route-changing
            owner correction and run a follow-up repair/shape decision to revise
            the next child from state-first toward a Markdown operating-manager-v1
            review/runtime route.
            bad_because: without explicit owner confirmation in Direction OS,
              this can bypass the durable-state prerequisite and blur product
              evidence with owner-approved OS route.
          - |
            C: reject or park b92/469 as route-violating product work and route
            only a product-repo cleanup/resync.
            bad_because: discards useful Markdown process-surface work that
              appears boundary-clean and already merged to product main.
        recommendation: |
          A, because it preserves real product evidence while maintaining OS
          lifecycle gates: no task is closed without a matching active
          task/open_call and first-hand evidence, and the owner still decides
          whether the next bet remains state-first or changes route.

  In live/solmax/NOW.md, under preserved_evidence, append these items if absent:

      - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631
      - github.com/ainazemtsau/zaratusta@469e6996ea120073168bf350d54cf8e56135f30d
      - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/contracts/operating-manager-v1.md
      - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/contracts/operating-manager-v1-source-basis.md
      - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/docs/decisions/0002-operating-manager-v1-surface.md
      - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/examples/operating-manager-v1-examples.md
      - live/solmax/history/2026-07-04-c-solmax-zaratusta-b92-handback-repair-001.md

  Leave NOW.next unchanged as:

      work/calls/c-zara-operate-state-shape-001.md

  Rationale: the current pointer is a valid self-contained OS CALL artifact but
  remains conditional on D-zara-operate-next-bet-001 option A; this repair adds
  D-zara-operate-b92-handback-001 and returns awaiting_decision rather than
  replacing NOW.next with the product-authored CALL.

  2) live/solmax/LOG.md

  Append this line before END_OF_FILE:

      - 2026-07-04 — repair g-zara-operate b92 handback: checked Zaratusta product main b92de14 and commit 469e699 first-hand; evidence is real Markdown operating-manager-v1 surface, but current NOW has no matching active task/open_call and product next CALL is not authoritative. Recorded b92/469 as untracked evidence requiring owner decision D-zara-operate-b92-handback-001; no tasks/TREE marked done. → history/2026-07-04-c-solmax-zaratusta-b92-handback-repair-001.md

  3) live/solmax/history/

  Add this full RESULT as:

      live/solmax/history/2026-07-04-c-solmax-zaratusta-b92-handback-repair-001.md

captures:
  - Zaratusta product repo AGENTS.md at b92 still has old handback wording: it asks for changed files plus commit/PR/manual check evidence, but not Direction OS carry-back fields from contract v10. This is already noted as §Re-sync owed by maintenance commit 217ab671 and should be handled in a separate authorized product-resync route.
  - Product docs now assert an owner-approved correction that full Markdown operating-manager-v1 is the first useful surface, not state-only; Direction OS should not treat that assertion as route-changing until the owner confirms it inside OS state.

decisions_needed:
  - id: D-zara-operate-b92-handback-001
    q: |
      Как Direction OS должен трактовать untracked b92/469 evidence:
      просто сохранить как evidence, пересмотреть next route, или отвергнуть/park?
    why_it_matters: |
      Это блокирует следующий корректный шаг. Если принять product evidence как
      route-changing без owner confirmation, OS обойдёт active task/open_call
      lifecycle. Если игнорировать evidence, можно потерять полезную уже
      смерженную Markdown surface работу.
    facts: |
      live/solmax сейчас: active_bet none; tasks []; open_calls []; открыт
      D-zara-operate-next-bet-001; NOW.next указывает на state-shape CALL,
      который запускается только при выборе owner option A.

      Zaratusta main сейчас b92de14; commit 469e699 добавил Markdown
      operating-manager-v1 surface. Evidence проверена напрямую. Product docs
      говорят, что v1 surface не выбирает runtime/storage/UI/API/database/
      automation/vendor/exact schema/layout, а state touchpoints являются только
      meanings/interfaces.

      Maintenance v10 говорит: product reports are evidence, not OS RESULTs;
      current b92/469 is not writer-applicable until carry-back repair
      reconciles it against live/solmax.
    terms: |
      untracked evidence = реальное изменение product repo без matching
        active task/open_call в NOW.
      carry-back = OS-сессия, которая проверяет product report и выпускает
        writer-applicable RESULT.
      accepted evidence != task done.
    options:
      - |
        A: сохранить b92/469 как accepted untracked evidence, не закрывая задач
        и не меняя TREE; затем решить D-zara-operate-next-bet-001.
        bad_because: v1 surface не становится немедленно текущей ставкой.
      - |
        B: считать b92/469 поводом пересмотреть next-bet route в сторону
        Markdown operating-manager-v1 review/runtime route.
        bad_because: может обойти durable-state prerequisite без явных owner
        words в OS.
      - |
        C: reject/park b92/469 как route violation и заняться только cleanup /
        product handback resync.
        bad_because: вероятно выбрасывает полезную boundary-clean работу.
    recommendation: |
      A, потому что это единственный вариант, который сохраняет evidence и не
      нарушает OS lifecycle gates.

play_check:
  - "1 Name the contradiction: done — current NOW has active_bet none, tasks [], open_calls [], open next-bet decision and conditional state-shape next, while product repo has merged b92/469 operating-manager-v1 evidence and a product-authored next CALL."
  - "2 Reconstruct: done — read NOW.md, TREE.md, CHARTER.md, LOG tail, recent history, current state-shape CALL, product commits/files at b92/469/795, commit status/workflow absence, and maintenance v10 handback bridge."
  - "3 Propose corrected state: done — proposed no task/TREE closure, route_status update, preserved_evidence additions, a new owner decision D-zara-operate-b92-handback-001, LOG line, and history record."
  - "4 Confirm: blocked/awaiting owner — repair reaches a route decision: whether to preserve b92/469 as evidence only, use it to revise next route, or park/reject it. No owner words in this session authorize a route-changing import."
  - "5 Friction: skipped — the OS hole was already logged and addressed by maintenance commit 217ab671 / contract v10; remaining product-side AGENTS.md resync is captured, not acted on in this repair."

log: |
  repair g-zara-operate b92 handback: checked Zaratusta product main b92de14 and commit 469e699 first-hand; evidence is real Markdown operating-manager-v1 surface, but current NOW has no matching active task/open_call and product next CALL is not authoritative. Recorded b92/469 as untracked evidence requiring owner decision D-zara-operate-b92-handback-001; no tasks/TREE marked done.

next: |
  awaiting_decision
END_OF_FILE: live/solmax/history/2026-07-04-c-solmax-zaratusta-b92-handback-repair-001.md
