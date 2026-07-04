RESULT c-solmax-zaratusta-markdown-manager-v1-route-repair-004 (call: owner-route-correction-2026-07-04)
direction: solmax   play: repair   node/task: g-zara-operate/repair

outcome: |
  Repaired the route wording after the previous assistant response incorrectly
  narrowed the next work toward state/replay/converge.

  The owner clarified that the next bet must close the full Markdown
  operating-manager-v1 layer that had already been discussed: not a slice, not
  a check-only leg, and not state-only. The required scope includes inbox,
  week/day, reviews, open loops/backlog, current state, source/context, audit/
  replay, and process mutation surface.

  Corrected next route:
  - Supersede the direct state-shape/state-converge route as too narrow.
  - Keep b92de14/469e699 as accepted baseline product evidence.
  - Route next to a shape CALL for the full Markdown operating-manager-v1
    workspace/state surface.
  - Do not claim app/runtime/API/database/automation/full autonomous product
    readiness before executor implementation + independent verification + review.

evidence: |
  Current GitHub state checked in the prior repair read:
  - live/solmax/NOW.md records accepted baseline evidence:
    - authority-contract substrate at
      github.com/ainazemtsau/zaratusta@79578ac87c73591000409f9f82a3bb4d0e33aa5b
    - operating-manager-v1 Markdown surface at
      github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631,
      including commit 469e6996ea120073168bf350d54cf8e56135f30d.
  - live/solmax/NOW.md records owner clarification from
    c-solmax-zaratusta-b92-state-route-repair-002:
    do not use an incomplete/manual reduced version; quality and full readiness
    matter; route state-first/full-readiness, not manual-use-now.
  - live/solmax/NOW.md currently points next to
    work/calls/c-zara-operate-state-shape-001.md.
  - live/solmax/work/calls/c-zara-operate-state-shape-001.md is still framed
    around g-zara-operate-state and durable state/replay boundaries.
  - Product evidence at b92 includes operating-manager-v1 Markdown contracts,
    source basis, examples, checklist and decision 0002, but not yet the full
    owner-operating Markdown workspace/file structure the owner is demanding
    for actual readiness.

  Owner correction in this session:
  - "в следующем бет мы закрываем полностью ... то, что мы договорились с Markdown"
  - "не кусок какой-то, не проверка"
  - "должно быть именно ... недели, и дни, и review, и inbox, и всё"

  Diagnosis:
  - The previous repair overcorrected into a state/replay route.
  - The real next bet should complete the full Markdown operating-manager-v1
    workspace/state layer, with all owner-operating flows included.
  - State/replay/audit remain included, but only as part of the full Markdown
    manager surface, not as a narrowed standalone slice.

state_changes: |
  Apply the following exact Direction OS state changes.

  If RESULT c-solmax-zaratusta-state-route-repair-003 has not been applied yet,
  do not apply it. This RESULT supersedes that route.

  1) live/solmax/NOW.md

  Keep active_bet.status as:

      active_bet:
        status: none

  In active_bet.note, keep the existing accepted baseline evidence for
  79578ac, b92de14 and 469e699. Replace any route-repair paragraph that says
  the next route is state-converge or state-shape with this paragraph:

      Route repair:
      The previous state-only/state-converge route is superseded. The next bet
      must close the full Markdown operating-manager-v1 workspace/state surface
      that the owner clarified: inbox/intake, backlog/open loops, current
      operating state, week/day, reviews, decisions/commitments, source/context,
      audit/replay, process mutation and examples/checks. This is the complete
      current Markdown product layer, not app/runtime/API/database/automation.

  Replace route_status with:

      route_status: g-zara-operate-contract_done_b92_baseline_accepted_markdown_manager_v1_full_shape_ready

  Keep:

      tasks: []
      recurring: []
      decisions: []
      open_calls: []

  In owner_directive, keep the existing text and append this paragraph:

      Owner correction in c-solmax-zaratusta-markdown-manager-v1-route-repair-004:
      the next bet must not narrow to state/replay/converge-only work. It must
      shape and then implement the full Markdown operating-manager-v1 layer:
      inbox/intake, backlog/open loops, week/day, reviews, current state,
      source/context, audit/replay, process mutation, examples/checks and
      handback rules. Quality remains priority; this layer must be complete in
      Markdown before later app/runtime/automation work.

  In preserved_evidence, append these items if absent:

      - live/solmax/history/2026-07-04-c-solmax-zaratusta-markdown-manager-v1-route-repair-004.md
      - live/solmax/work/calls/c-zara-operate-markdown-manager-v1-full-shape-001.md

  Replace NOW.next with exactly:

      next: work/calls/c-zara-operate-markdown-manager-v1-full-shape-001.md

  2) live/solmax/work/calls/c-zara-operate-markdown-manager-v1-full-shape-001.md

  Add this file with exactly this content:

      CALL c-zara-operate-markdown-manager-v1-full-shape-001
      to: session
      direction: solmax
      play: shape
      node: g-zara-operate-state
      goal: |
        An owner-approved bounded bet card exists for completing the full
        Markdown operating-manager-v1 workspace/state surface in Zaratusta.
      context: |
        Route authority:
        - c-solmax-zaratusta-b92-state-route-repair-002 accepted b92de14/469e699
          as baseline Markdown operating-manager-v1 evidence.
        - owner-route-correction-2026-07-04 clarified that the next bet must
          not narrow to state/replay-only, converge-only, or check-only work.
        - The next bet must close the full Markdown operating-manager-v1 layer
          that was discussed: inbox/intake, backlog/open loops, current
          operating state, week/day, reviews, decisions/commitments,
          source/context, audit/replay, process mutation and examples/checks.

        Current direction state:
        - live/solmax/CHARTER.md
        - live/solmax/TREE.md
        - live/solmax/NOW.md
        - live/solmax/LOG.md

        Closed prerequisite:
        - g-zara-operate-contract is done.
        - Accepted authority-contract baseline:
          github.com/ainazemtsau/zaratusta@79578ac87c73591000409f9f82a3bb4d0e33aa5b
        - Accepted operating-manager-v1 Markdown baseline:
          github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631,
          including commit 469e6996ea120073168bf350d54cf8e56135f30d.

        Product baseline evidence to use:
        - README.md
        - AGENTS.md
        - checks/w20-a1-a13-acceptance-map.md
        - checks/markdown-foundation-checklist.md
        - contracts/manager-role.md
        - contracts/workspace-boundaries.md
        - contracts/source-context.md
        - contracts/process-contracts.md
        - contracts/owner-context.md
        - contracts/context-loading.md
        - contracts/operating-manager-v1.md
        - contracts/operating-manager-v1-source-basis.md
        - examples/operating-examples.md
        - examples/operating-manager-v1-examples.md
        - docs/decisions/0001-markdown-only-reset.md
        - docs/decisions/0002-operating-manager-v1-surface.md

        Required bet scope:
        - inbox/intake: owner input capture, triage, missing context, not
          silently turning capture into commitment.
        - backlog/open loops: deferred items, waiting items, research routes,
          rejected/superseded assumptions, next decision point.
        - current operating state: current week/day, accepted commitments,
          protected commitments, current objective, current constraints.
        - week flow: week plan, protected items, routine, wishes/new volume,
          cuts, accepted/proposed status.
        - day flow: day start, protected items, main objective, next action,
          disruption rebuild, free log, day close.
        - reviews: day review and week review, including evidence, misses,
          protected item status, process conclusions and next gates.
        - decisions/commitments: capture vs proposal vs accepted commitment vs
          completed work.
        - source/context: loaded basis, missing context, source permissions,
          freshness/trust and allowed use.
        - audit/replay: enough trace to reconstruct why a plan/decision/review
          exists, without choosing a DB/runtime engine.
        - process mutation: owner-approved recipe/process changes only; no
          hidden self-mutation.
        - examples/checks: manual examples and checklist covering the whole
          flow end-to-end.
        - handback/reporting: product report must return Direction OS carry-back
          evidence under handback v10 expectations, not a product-authored next
          CALL.

        Product facts to preserve:
        - operating-manager-v1 is a Markdown product layer.
        - Topic handling remains open through process/source/context.
        - Direction OS and other repos/projects are read-only sources by default.
        - Zaratusta writes only to its own workspace/repo unless a future narrow
          integration/procedure is approved.
        - External, irreversible, spend, deletion, message/send or cross-system
          effects require explicit scoped owner approval before effect.
      boundaries: |
        Do not route to manual-use-now.
        Do not route to state/replay-only, converge-only, check-only or
        verification-only work.
        Do not cut inbox/intake, backlog/open loops, week/day, reviews,
        current state, decisions/commitments, source/context, audit/replay,
        process mutation, examples/checks or handback from the bet.
        Do not modify product repo in the shape session.
        Do not implement UI/channel/API/vendor/scheduler/automation/spend
        controls.
        Do not choose database/storage engine/app runtime/vendor/API.
        Exact Markdown files/paths/templates may be included in the v1 product
        surface if the bet makes them the minimal Markdown layer, but they must
        not be represented as future database/app schema or permanent non-
        Markdown architecture.
        Do not create any Direction OS write path.
        Do not claim app/runtime/automation/full autonomous product readiness
        before executor implementation, independent verification and review.
        Preserve W20/A1-A13 and the W19 HOW firewall unless a fresh converge or
        owner-approved route explicitly changes WHAT.
      done_when: |
        Shape produces one owner-approvable bet card for the full Markdown
        operating-manager-v1 workspace/state surface with:
        - appetite;
        - kill_by;
        - cut list with at least one real cut;
        - lens sweep;
        - riskiest assumption task;
        - no more than 3 active tasks;
        - first executor CALL ready.

        The bet must include product work that creates/updates the Markdown
        workspace/file structure and checks all required flows:
        inbox/intake, backlog/open loops, current state, week/day, reviews,
        decisions/commitments, source/context, audit/replay, process mutation,
        examples/checks and handback.

        The bet must not be accepted if it narrows to only state replay, only
        audit, only checklist, only converge, or only manual-use prose.
      return: |
        RESULT with owner-approved shape state_changes, exact active_bet,
        task list, cut list, lens sweep, kill_by and next executor CALL.
      budget: one focused shape session
      parent: c-solmax-zaratusta-markdown-manager-v1-route-repair-004
      surface: chatgpt

      END_OF_FILE: live/solmax/work/calls/c-zara-operate-markdown-manager-v1-full-shape-001.md

  3) live/solmax/work/calls/c-zara-operate-state-shape-001.md

  Leave the old file in place as historical/superseded evidence.
  Do not use it as NOW.next.
  Do not delete it.

  4) live/solmax/work/calls/c-zara-operate-state-converge-001.md

  If this file exists from c-solmax-zaratusta-state-route-repair-003, leave it
  in place as historical/superseded evidence.
  Do not use it as NOW.next.
  Do not delete it.

  5) live/solmax/TREE.md

  No edit in this repair. Current TREE remains:
  - g-zara-operate-contract is done.
  - g-zara-operate-state is not done.
  - g-zara-operate-runtime is not done.
  - g-zara-operate-evolution is not done.

  Note for the next shape session:
  - The bet is carried under g-zara-operate-state because the immediate product
    work is the Markdown workspace/state surface, including week/day/review/
    inbox artifacts as durable operating state objects.
  - Runtime/dogfood remains a later review/shape outcome after the Markdown
    layer is implemented and verified.

  6) live/solmax/LOG.md

  Append this line before END_OF_FILE:

      - 2026-07-04 — repair g-zara-operate Markdown manager v1 route: superseded the too-narrow state-only/state-converge route. Owner clarified the next bet must close the full Markdown operating-manager-v1 layer — inbox/intake, backlog/open loops, current state, week/day, reviews, decisions/commitments, source/context, audit/replay, process mutation, examples/checks and handback — not a slice or verification-only leg. NOW.next → work/calls/c-zara-operate-markdown-manager-v1-full-shape-001.md. → history/2026-07-04-c-solmax-zaratusta-markdown-manager-v1-route-repair-004.md

  7) live/solmax/history/

  Add this full RESULT as:

      live/solmax/history/2026-07-04-c-solmax-zaratusta-markdown-manager-v1-route-repair-004.md

captures:
  - The previous state-converge repair was too narrow for the owner's intended next bet; future route repairs must preserve the owner-required full Markdown manager surface instead of splitting immediately into a state-only leg.
  - Later runtime/app/automation can only start after the full Markdown manager v1 layer is implemented, independently verified and reviewed.

decisions_needed: []

play_check:
  - "1 Name the contradiction: done — current route points at state-only/state-shape/converge work, while owner clarified the next bet must close the full Markdown operating-manager-v1 layer including weeks, days, review, inbox and the rest."
  - "2 Reconstruct: done — used current NOW baseline b92/469 state, current state-shape route, owner clarification, and product baseline evidence for operating-manager-v1."
  - "3 Propose corrected state: done — replace NOW.next with a full Markdown-manager-v1 shape CALL, preserve b92/469 evidence, supersede state-only/converge route, leave TREE honest."
  - "4 Confirm: done — owner route words: \"в следующем бет мы закрываем полностью ... то, что мы договорились с Markdown\", \"не кусок какой-то, не проверка\", and \"недели, и дни, и review, и inbox, и всё\"."
  - "5 Friction: skipped — this is a route correction inside the already-known handback/routing problem class; no OS rule change is applied here."

log: |
  repair g-zara-operate Markdown manager v1 route: superseded the too-narrow state-only/state-converge route. Owner clarified the next bet must close the full Markdown operating-manager-v1 layer — inbox/intake, backlog/open loops, current state, week/day, reviews, decisions/commitments, source/context, audit/replay, process mutation, examples/checks and handback — not a slice or verification-only leg. NOW.next → work/calls/c-zara-operate-markdown-manager-v1-full-shape-001.md.

next: |
  work/calls/c-zara-operate-markdown-manager-v1-full-shape-001.md

END_OF_FILE: live/solmax/history/2026-07-04-c-solmax-zaratusta-markdown-manager-v1-route-repair-004.md
