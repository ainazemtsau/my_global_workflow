RESULT s-zara-operate-markdown-manager-v1-full-shape-repair-001 (call: owner-writer-bounce-2026-07-05)
direction: solmax   play: repair   node/task: g-zara-operate-state/repair

outcome: |
  Writer-bounce repaired in packet form; no repository files were modified by
  this session.

  The previous shape RESULT was not mechanically applicable because:
  - it changed live/solmax/TREE.md without a writer-detectable owner_approved
    marker for the TREE diff;
  - it activated g-zara-operate-state without a converge-verify RESULT and without
    a play_check triage line explicitly saying converge OFF;
  - it wrote NOW.next as a nested object while current NOW hygiene requires either
    a CALL packet or a one-line pointer to a self-contained CALL artifact under
    work/;
  - it issued the first executor CALL while leaving open_calls empty.

  Corrected repair outcome:
  - preserve the owner-approved choice: option A, the bet as written;
  - add an explicit owner_approved marker and owner words for the TREE activation;
  - explicitly mark Definition-of-Ready as converge OFF by triage, with the route
    authority and reason;
  - activate b-zara-operate-markdown-manager-v1-full-surface-001 under
    g-zara-operate-state;
  - write NOW.next as one line:
    work/calls/c-zara-operate-markdown-manager-v1-full-surface-t1-001.md;
  - add that self-contained work/ CALL artifact;
  - record the issued executor CALL in NOW.open_calls.

evidence: |
  Writer-bounce evidence from owner:
  - "Не применил RESULT. Это writer-bounce по G10/G9, без изменений файлов и без commit."
  - "TREE.md меняется, но в RESULT нет явного owner_approved mark."
  - "Shape активирует g-zara-operate-state, но Definition-of-Ready не закрыт:
     нет converge-verify RESULT для этого node и нет строки
     triage: <type> — converge OFF — because ... в play_check."
  - "Новый NOW.md не проходит NOW hygiene: next: записан как вложенный объект
     id/to/..., а writer-rule принимает либо CALL packet, либо one-line pointer
     на self-contained CALL artifact under work/. Плюс следующий executor CALL
     выдан, но open_calls: []."
  - "Нужен исправленный RESULT/repair, который явно закрывает эти три пункта."

  Current state checked after bounce:
  - live/solmax/NOW.md still has active_bet.status none, tasks [], recurring [],
    decisions [], open_calls [], and next:
    work/calls/c-zara-operate-markdown-manager-v1-full-shape-001.md.
  - live/solmax/TREE.md still has g-zara-operate-state status: parked.
  - live/solmax/NOW.md already records accepted baseline evidence:
    - Zaratusta authority-contract substrate:
      79578ac87c73591000409f9f82a3bb4d0e33aa5b.
    - Zaratusta operating-manager-v1 Markdown surface:
      b92de14eedda436e06a6de457f50aae483b7c631,
      including commit 469e6996ea120073168bf350d54cf8e56135f30d.
  - live/solmax/NOW.md and LOG route repair state that the next bet must close
    the full Markdown operating-manager-v1 workspace/state surface, not a
    state/replay-only, converge-only, check-only, or manual-use route.

  Owner approval used for TREE activation:
  - owner_approved: true
  - owner_words: "A"
  - This approved option A shown in the shape close: activate the bet as written,
    with appetite 3 focused days, three tasks, full required Markdown surface
    scope, kill_by 2026-07-11, cut list, lens sweep, and next executor CALL.

state_changes: |
  Apply the following exact Direction OS state changes.

  Do not apply the bounced RESULT
  s-zara-operate-markdown-manager-v1-full-shape-001 as previously emitted.
  Apply this repair RESULT instead.

  1) live/solmax/TREE.md

  owner_approved marker for this TREE diff:
    owner_approved: true
    owner_words: |
      A

  In live/solmax/TREE.md:

  - In top-level owner_approved.evidence, append this list item if absent:
      - '2026-07-05: owner approved activating g-zara-operate-state as the full Markdown operating-manager-v1 workspace/state surface bet. Owner words: "A".'

  - For node root.children[g-zara-operate].children[g-zara-operate-state],
    replace exactly:
      status: parked
    with:
      status: active
      appetite: 3 focused days
      kill_by: |
        metric: independent verification of the Zaratusta Markdown
          operating-manager-v1 workspace/state surface against the full required
          surface list, W20/A1-A13, W19 HOW firewall, workspace/effect boundaries
          and handback expectations
        threshold: |
          By 2026-07-11, t-3 must PASS with all required surfaces covered:
          inbox/intake, backlog/open loops, current operating state, week/day,
          reviews, decisions/commitments, source/context, audit/replay, process
          mutation, examples/checks and handback/reporting. PASS requires zero hard
          failures on capture/commitment semantics, owner approval gates, read/write
          boundaries, no OS write path, no generic topic blacklist, no DB/API/
          runtime/storage engine/vendor/scheduler/automation/exact future schema
          chosen as contract, and handback evidence returned for Direction OS
          carry-back.
        date: 2026-07-11

  - Leave g-zara-operate-state goal, done_when and why unchanged.
  - Do not change g-zara-operate parent status.
  - Do not change g-zara-operate-contract, g-zara-operate-runtime or
    g-zara-operate-evolution.
  - Do not add, drop or reorder TREE nodes.

  2) live/solmax/NOW.md

  Replace the whole file with:

      # NOW — solmax
      project:
        name: Zaratusta
        product_repo: github.com/ainazemtsau/zaratusta

      active_bet:
        id: b-zara-operate-markdown-manager-v1-full-surface-001
        node: g-zara-operate-state
        status: active
        appetite: 3 focused days
        started: 2026-07-05
        kill_by:
          date: 2026-07-11
          metric: |
            Independent verification of the Zaratusta Markdown operating-manager-v1
            workspace/state surface against full required surface coverage, W20/A1-A13,
            W19 HOW firewall, workspace/effect boundaries, and handback/reporting
            expectations for Direction OS carry-back.
          threshold: |
            PASS only if t-3 verifies product-repo evidence with all required surfaces
            covered: inbox/intake, backlog/open loops, current operating state, week/day,
            reviews, decisions/commitments, source/context, audit/replay, process
            mutation, examples/checks and handback/reporting.

            PASS requires zero hard failures on capture != commitment, proposal !=
            accepted commitment, accepted commitment != completed work, owner approval
            gates, read/write boundaries, side-effect boundaries, topic-open/
            source-context routing, no generic topic blacklist, and no Direction OS
            write path.

            PASS also requires no UI/channel/app surface, API/model vendor/framework/
            subscription adapter, database/storage engine/replay engine/durable writer/
            executable ledger, scheduler, automation, spend controls, external
            integrations, exact permanent schema, or future non-Markdown architecture
            selected as contract.
        forecast: |
          Likely to pass if executor treats the work as a Markdown product surface
          with verifiable examples/checks, not as architecture. The baseline contracts
          already contain the behavioral model; the missing layer is concrete
          workspace/state surface and end-to-end coverage.
        against: |
          This does not prove real recurring use. It also does not complete runtime,
          automation, UI/API, database/storage, or autonomous product readiness.
        definition_of_ready: |
          triage: owner-route-corrected-full-markdown-layer — converge OFF — because
          the owner-corrected route is not a fresh unsettled WHAT-spec node: the
          authority contract is already closed, b92/469 is accepted baseline evidence,
          and the next bounded bet is explicitly the full Markdown operating-manager-v1
          workspace/state surface. The model-bearing HOW choices remain cut, and t-1
          is the early risk gate for coverage before broad implementation.
        cut_list:
          - UI/channel/app surface.
          - API/model vendor/framework/subscription adapter.
          - Database, storage engine, replay engine, durable writer, executable ledger.
          - Scheduler, automation, spend controls, external integrations.
          - Direction OS write path.
          - Exact permanent schema or future non-Markdown architecture.
          - Real owner dogfood week/day operation as acceptance; this bet makes the
            Markdown layer ready, runtime/dogfood comes after verification/review.
          - Product self-development process; Zaratusta repo guardrails do not become
            product direction.
        lens_sweep:
          extensibility: task_required — t-1/t-2 must keep the layer Markdown-only
            and avoid permanent runtime/storage/schema choices.
          real_depth: task_required — t-2/t-3 must cover multi-step operating rhythm,
            not passive memory lookup.
          agent_buildability: task_required — two executor increments plus independent
            verification, each with commit/PR or refutation evidence.
          daily_use_dogfood: task_required_bounded — t-2 must create an owner-operable
            surface; actual recurring dogfood is cut to the next route after review.
          privacy_trust_safety: task_required — t-2/t-3 must preserve Zaratusta-only
            writes, read-only external sources, and owner approval before external/
            irreversible/spend/deletion/message/cross-system effects.
          cost_discipline: task_required_negative_check — no API/vendor/automation/
            spend-bearing implementation is selected.
        riskiest_assumption: |
          A minimal Markdown workspace/state pack can cover the full operating loop
          deeply enough for later runtime/dogfood, while still not choosing a database,
          replay engine, runtime, permanent schema, or app surface.
        next_if_true: |
          Review this bet for closure, then decide the next route: runtime/dogfood
          or evolution.
        next_if_false: |
          Missing surface -> repair executor task.
          WHAT contradiction -> converge.
          HOW-smuggling -> rollback/revert product change and review the cut boundary.

      route_status: g-zara-operate-state_active_t1_ready

      owner_directive: |
        The first Zaratusta implementation route is g-zara-operate: the LifeReset-derived
        personal operating-manager capability becomes the real Personal Operating System
        phase of Zaratusta, not a PoC and not a separate LifeReset project.

        Owner-approved split from 2026-06-26 remains: g-zara-operate-contract,
        g-zara-operate-state, g-zara-operate-runtime, g-zara-operate-evolution.

        Preserved operating boundary: topic-open through process/source/context; writes
        default only to the Zaratusta workspace/repo; other repos/directions/projects
        are read-only sources by default; future non-Zaratusta writes require explicit
        narrow integration/procedure; deep research is a first-class process route.

        Owner correction in c-solmax-zaratusta-markdown-manager-v1-route-repair-004:
        the next bet must not narrow to state/replay/converge-only work. It must
        shape and then implement the full Markdown operating-manager-v1 layer:
        inbox/intake, backlog/open loops, week/day, reviews, current state,
        source/context, audit/replay, process mutation, examples/checks and handback
        rules. Quality remains priority; this layer must be complete in Markdown
        before later app/runtime/automation work.

        Owner approved option A in the writer-bounced shape exchange: activate the bet
        as written with appetite 3 focused days, full required Markdown surface scope,
        three tasks, risk gate first, kill_by 2026-07-11, cut list, lens sweep and
        first executor CALL.

      tasks:
        - id: t-1
          kind: executor
          status: active
          goal: |
            Create the product-repo full-surface coverage scaffold that tests the
            riskiest assumption before broad implementation.
          done_when: |
            Product repo commit/PR contains a Markdown-readable coverage scaffold
            mapping every required surface to concrete product artifacts/checks:
            inbox/intake, backlog/open loops, current operating state, week/day,
            reviews, decisions/commitments, source/context, audit/replay, process
            mutation, examples/checks and handback/reporting. The scaffold identifies
            reused baseline files, files needing creation/update, W19/HOW not-chosen
            items, and any missing required surface before t-2 proceeds.
          evaluator: independent verification in t-3
          rollback: |
            Revert or repair any scaffold that narrows the route to state/replay-only,
            check-only, manual-use prose, or that smuggles forbidden HOW choices.

        - id: t-2
          kind: executor
          status: open
          goal: |
            Implement the full minimal Markdown operating-manager-v1 workspace/state
            layer in the Zaratusta product repo.
          done_when: |
            Product repo commit/PR creates or updates the minimal Markdown artifacts,
            templates, contracts, examples and checks needed to operate the complete
            v1 layer across inbox/intake, backlog/open loops, current state, week/day,
            reviews, decisions/commitments, source/context, audit/replay, process
            mutation, examples/checks and handback/reporting. No forbidden HOW choice,
            generic topic blacklist or Direction OS write path is introduced.
          evaluator: independent verification in t-3
          rollback: |
            Revert or repair any product-repo artifact that weakens W20/A1-A13,
            violates workspace/effect boundaries, introduces a Direction OS write
            path, or smuggles W19/HOW choices.

        - id: t-3
          kind: session
          status: open
          goal: |
            Independently try to refute that the product repo now contains the full
            Markdown operating-manager-v1 workspace/state surface.
          done_when: |
            Verifier reads the product repo commit/PR evidence from t-1 and t-2 plus
            the accepted baseline files. PASS requires all required surfaces covered,
            W20/A1-A13 preserved, W19 HOW firewall clean, workspace/effect boundaries
            preserved, no Direction OS write path, topic-open/source-context handling
            intact, no generic topic blacklist and no forbidden implementation choice.
            FAIL names exact missing/contradictory rows and routes product gap to
            repair executor task, WHAT contradiction to converge, and HOW-smuggling
            to rollback/review cut.
          evaluator: n/a

      recurring: []
      decisions: []

      open_calls:
        - id: c-zara-operate-markdown-manager-v1-full-surface-t1-001
          to: executor
          for: t-1
          issued: 2026-07-05
          note: full-surface coverage scaffold in Zaratusta product repo

      preserved_evidence:
        - live/solmax/CHARTER.md
        - live/solmax/TREE.md
        - live/solmax/LOG.md
        - live/solmax/work/converge-g-zara-operate-contract.md
        - live/solmax/history/2026-07-04-c-solmax-zaratusta-markdown-manager-v1-route-repair-004.md
        - live/solmax/work/calls/c-zara-operate-markdown-manager-v1-full-shape-001.md
        - live/solmax/history/2026-07-05-s-zara-operate-markdown-manager-v1-full-shape-repair-001.md
        - live/solmax/work/calls/c-zara-operate-markdown-manager-v1-full-surface-t1-001.md
        - github.com/ainazemtsau/zaratusta@79578ac87c73591000409f9f82a3bb4d0e33aa5b
        - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631
        - github.com/ainazemtsau/zaratusta@469e6996ea120073168bf350d54cf8e56135f30d
        - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/contracts/operating-manager-v1.md
        - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/contracts/operating-manager-v1-source-basis.md
        - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/docs/decisions/0002-operating-manager-v1-surface.md
        - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/examples/operating-manager-v1-examples.md

      next: work/calls/c-zara-operate-markdown-manager-v1-full-surface-t1-001.md
      END_OF_FILE: live/solmax/NOW.md

  3) live/solmax/work/calls/c-zara-operate-markdown-manager-v1-full-surface-t1-001.md

  Add this file with exactly this content:

      CALL c-zara-operate-markdown-manager-v1-full-surface-t1-001
      to: executor
      direction: solmax
      play: work
      node: g-zara-operate-state
      task: t-1
      repo: github.com/ainazemtsau/zaratusta
      kind: engineering
      goal: |
        The Zaratusta product repo has a Markdown-readable full-surface coverage
        scaffold for the complete operating-manager-v1 workspace/state layer.
      context: |
        Active bet:
        - b-zara-operate-markdown-manager-v1-full-surface-001
        - node: g-zara-operate-state
        - task: t-1
        - appetite: 3 focused days
        - kill_by: 2026-07-11

        Direction OS context to read:
        - live/solmax/CHARTER.md
        - live/solmax/TREE.md
        - live/solmax/NOW.md
        - live/solmax/LOG.md
        - live/solmax/history/2026-07-04-c-solmax-zaratusta-markdown-manager-v1-route-repair-004.md
        - live/solmax/history/2026-07-05-s-zara-operate-markdown-manager-v1-full-shape-repair-001.md
        - live/solmax/work/calls/c-zara-operate-markdown-manager-v1-full-shape-001.md

        Product baseline evidence:
        - github.com/ainazemtsau/zaratusta@79578ac87c73591000409f9f82a3bb4d0e33aa5b
        - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631
        - github.com/ainazemtsau/zaratusta@469e6996ea120073168bf350d54cf8e56135f30d

        Product files to read at current main before editing:
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

        Required full surface to map:
        - inbox/intake: owner input capture, triage, missing context, not silently
          turning capture into commitment.
        - backlog/open loops: deferred items, waiting items, research routes,
          rejected/superseded assumptions, next decision point.
        - current operating state: current week/day, accepted commitments, protected
          commitments, current objective, current constraints.
        - week flow: week plan, protected items, routine, wishes/new volume, cuts,
          accepted/proposed status.
        - day flow: day start, protected items, main objective, next action,
          disruption rebuild, free log, day close.
        - reviews: day review and week review, including evidence, misses, protected
          item status, process conclusions and next gates.
        - decisions/commitments: capture vs proposal vs accepted commitment vs
          completed work.
        - source/context: loaded basis, missing context, source permissions,
          freshness/trust and allowed use.
        - audit/replay: enough Markdown trace to reconstruct why a plan, decision
          or review exists, without choosing a DB/runtime/replay engine.
        - process mutation: owner-approved recipe/process changes only; no hidden
          self-mutation.
        - examples/checks: manual examples and checklist covering the whole flow
          end-to-end.
        - handback/reporting: product report must return Direction OS carry-back
          evidence, not a product-authored next CALL.

        Preserve:
        - operating-manager-v1 is a Markdown product layer.
        - Topic handling remains open through process/source/context.
        - Direction OS and other repos/projects are read-only sources by default.
        - Zaratusta writes only to its own workspace/repo unless a future narrow
          integration/procedure is approved.
        - External, irreversible, spend, deletion, message/send or cross-system
          effects require explicit scoped owner approval before effect.
        - W20/A1-A13 and the W19 HOW firewall remain binding unless a fresh converge
          or owner-approved route explicitly changes WHAT.
      boundaries: |
        Do not modify the Direction OS repo or any non-Zaratusta repo.
        Do not route to manual-use-now.
        Do not narrow this to state/replay-only, converge-only, check-only,
        verification-only or manual-use prose.
        Do not cut inbox/intake, backlog/open loops, current state, week/day,
        reviews, decisions/commitments, source/context, audit/replay, process
        mutation, examples/checks or handback from the coverage scaffold.
        Do not implement UI/channel/API/vendor/scheduler/automation/spend controls.
        Do not choose database/storage engine/app runtime/vendor/API.
        Do not choose exact permanent schema or future non-Markdown architecture.
        Do not create any Direction OS write path.
        Do not introduce a generic topic/domain blacklist.
        Do not claim runtime, automation, dogfood, app readiness, or full autonomous
        product readiness.
        Keep all changes inside the Markdown product surface.
      done_when: |
        - Product repo commit/PR contains a Markdown-readable coverage scaffold
          mapping every required surface to concrete product artifacts/checks:
          inbox/intake, backlog/open loops, current operating state, week/day,
          reviews, decisions/commitments, source/context, audit/replay, process
          mutation, examples/checks and handback/reporting.
        - Scaffold identifies which existing baseline files are reused and which
          Markdown artifacts/templates/contracts/examples/checks need creation or
          update.
        - Scaffold marks W19/HOW items explicitly not chosen: UI/channel/app,
          API/vendor/framework, DB/storage/replay engine/durable writer,
          scheduler/automation/spend controls/external integration, exact permanent
          schema/future non-Markdown architecture.
        - Scaffold preserves W20/A1-A13, topic-open source/context handling,
          Zaratusta-only writes, read-only external repos/sources by default, and
          owner approval before external/irreversible/spend/deletion/message/
          cross-system effects.
        - Scaffold is sufficient for an independent verifier to catch missing
          required surfaces before t-2 implementation proceeds.
      return: |
        RESULT with:
        - product repo commit or PR reference;
        - changed files;
        - concise manual check output against checks/markdown-foundation-checklist.md
          and checks/w20-a1-a13-acceptance-map.md;
        - explicit table of required surfaces -> artifact/check coverage;
        - explicit W19/HOW not-chosen check;
        - any gaps or risks found;
        - no product-authored Direction OS state changes or next CALL.
      budget: half focused day
      parent: s-zara-operate-markdown-manager-v1-full-shape-repair-001
      surface: cli

      END_OF_FILE: live/solmax/work/calls/c-zara-operate-markdown-manager-v1-full-surface-t1-001.md

  4) live/solmax/LOG.md

  Append this line before END_OF_FILE:

      - 2026-07-05 — repair g-zara-operate-state shape writer-bounce: added explicit owner_approved marker for TREE activation using owner words "A", recorded converge OFF triage for Definition-of-Ready, fixed NOW.next to one-line work/calls pointer, and registered the issued t-1 executor CALL in open_calls. Active bet b-zara-operate-markdown-manager-v1-full-surface-001 is ready for executor t-1. → history/2026-07-05-s-zara-operate-markdown-manager-v1-full-shape-repair-001.md

  5) live/solmax/history/

  Add this full RESULT as:

      live/solmax/history/2026-07-05-s-zara-operate-markdown-manager-v1-full-shape-repair-001.md

captures:
  - The bounced shape packet was substantively correct but missed writer-detectable mechanical fields: TREE owner_approved marker, converge-OFF triage, NOW.next pointer hygiene and open_calls registration.
  - Later runtime/dogfood remains cut from this bet and should only be shaped after the Markdown layer is implemented, independently verified and reviewed.

decisions_needed: []

play_check:
  - "triage: owner-route-corrected-full-markdown-layer — converge OFF — because the owner-corrected next bet is a bounded implementation shape over accepted baseline evidence, not a fresh unsettled WHAT-spec node: g-zara-operate-contract is done, b92/469 operating-manager-v1 Markdown surface is accepted baseline, the owner explicitly required the full Markdown layer rather than state-only/converge-only/check-only work, and model-bearing HOW choices remain cut while t-1 tests coverage first."
  - "1 Name the contradiction: done — writer rejected the prior shape RESULT because TREE activation lacked explicit owner_approved mark, Definition-of-Ready lacked converge OFF triage, NOW.next was a nested object instead of a one-line work/ pointer or CALL packet, and the issued executor CALL was absent from open_calls."
  - "2 Reconstruct: done — current repo state after bounce still has active_bet.status none, tasks [], open_calls [], NOW.next pointing to the full-shape CALL, and g-zara-operate-state parked; owner approval for the bet is the prior in-session word \"A\"."
  - "3 Propose corrected state: done — add TREE owner_approved marker/evidence, activate g-zara-operate-state with appetite/kill_by, replace NOW with active bet + t-1/t-2/t-3 + open_calls, create self-contained work/calls t-1 artifact, and set NOW.next to the one-line pointer."
  - "4 Confirm: done — owner supplied the writer-bounce and requested an исправленный RESULT/repair; the repair does not change the approved bet substance and carries owner approval words \"A\" for the TREE activation."
  - "5 Friction: skipped — this is a one-off packet-format/writer-hygiene correction after bounce; no new OS rule is applied here."

log: |
  repair g-zara-operate-state shape writer-bounce: added explicit owner_approved marker for TREE activation using owner words "A", recorded converge OFF triage for Definition-of-Ready, fixed NOW.next to one-line work/calls pointer, and registered the issued t-1 executor CALL in open_calls.

next: |
  CALL c-zara-operate-markdown-manager-v1-full-surface-t1-001
  to: executor
  direction: solmax
  play: work
  node: g-zara-operate-state
  task: t-1
  repo: github.com/ainazemtsau/zaratusta
  kind: engineering
  goal: |
    The Zaratusta product repo has a Markdown-readable full-surface coverage
    scaffold for the complete operating-manager-v1 workspace/state layer.
  context: |
    Active bet:
    - b-zara-operate-markdown-manager-v1-full-surface-001
    - node: g-zara-operate-state
    - task: t-1
    - appetite: 3 focused days
    - kill_by: 2026-07-11

    Direction OS context to read:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md
    - live/solmax/LOG.md
    - live/solmax/history/2026-07-04-c-solmax-zaratusta-markdown-manager-v1-route-repair-004.md
    - live/solmax/history/2026-07-05-s-zara-operate-markdown-manager-v1-full-shape-repair-001.md
    - live/solmax/work/calls/c-zara-operate-markdown-manager-v1-full-shape-001.md

    Product baseline evidence:
    - github.com/ainazemtsau/zaratusta@79578ac87c73591000409f9f82a3bb4d0e33aa5b
    - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631
    - github.com/ainazemtsau/zaratusta@469e6996ea120073168bf350d54cf8e56135f30d

    Product files to read at current main before editing:
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

    Required full surface to map:
    - inbox/intake: owner input capture, triage, missing context, not silently
      turning capture into commitment.
    - backlog/open loops: deferred items, waiting items, research routes,
      rejected/superseded assumptions, next decision point.
    - current operating state: current week/day, accepted commitments, protected
      commitments, current objective, current constraints.
    - week flow: week plan, protected items, routine, wishes/new volume, cuts,
      accepted/proposed status.
    - day flow: day start, protected items, main objective, next action,
      disruption rebuild, free log, day close.
    - reviews: day review and week review, including evidence, misses, protected
      item status, process conclusions and next gates.
    - decisions/commitments: capture vs proposal vs accepted commitment vs
      completed work.
    - source/context: loaded basis, missing context, source permissions,
      freshness/trust and allowed use.
    - audit/replay: enough Markdown trace to reconstruct why a plan, decision
      or review exists, without choosing a DB/runtime/replay engine.
    - process mutation: owner-approved recipe/process changes only; no hidden
      self-mutation.
    - examples/checks: manual examples and checklist covering the whole flow
      end-to-end.
    - handback/reporting: product report must return Direction OS carry-back
      evidence, not a product-authored next CALL.

    Preserve:
    - operating-manager-v1 is a Markdown product layer.
    - Topic handling remains open through process/source/context.
    - Direction OS and other repos/projects are read-only sources by default.
    - Zaratusta writes only to its own workspace/repo unless a future narrow
      integration/procedure is approved.
    - External, irreversible, spend, deletion, message/send or cross-system
      effects require explicit scoped owner approval before effect.
    - W20/A1-A13 and the W19 HOW firewall remain binding unless a fresh converge
      or owner-approved route explicitly changes WHAT.
  boundaries: |
    Do not modify the Direction OS repo or any non-Zaratusta repo.
    Do not route to manual-use-now.
    Do not narrow this to state/replay-only, converge-only, check-only,
    verification-only or manual-use prose.
    Do not cut inbox/intake, backlog/open loops, current state, week/day,
    reviews, decisions/commitments, source/context, audit/replay, process
    mutation, examples/checks or handback from the coverage scaffold.
    Do not implement UI/channel/API/vendor/scheduler/automation/spend controls.
    Do not choose database/storage engine/app runtime/vendor/API.
    Do not choose exact permanent schema or future non-Markdown architecture.
    Do not create any Direction OS write path.
    Do not introduce a generic topic/domain blacklist.
    Do not claim runtime, automation, dogfood, app readiness, or full autonomous
    product readiness.
    Keep all changes inside the Markdown product surface.
  done_when: |
    - Product repo commit/PR contains a Markdown-readable coverage scaffold
      mapping every required surface to concrete product artifacts/checks:
      inbox/intake, backlog/open loops, current operating state, week/day,
      reviews, decisions/commitments, source/context, audit/replay, process
      mutation, examples/checks and handback/reporting.
    - Scaffold identifies which existing baseline files are reused and which
      Markdown artifacts/templates/contracts/examples/checks need creation or
      update.
    - Scaffold marks W19/HOW items explicitly not chosen: UI/channel/app,
      API/vendor/framework, DB/storage/replay engine/durable writer,
      scheduler/automation/spend controls/external integration, exact permanent
      schema/future non-Markdown architecture.
    - Scaffold preserves W20/A1-A13, topic-open source/context handling,
      Zaratusta-only writes, read-only external repos/sources by default, and
      owner approval before external/irreversible/spend/deletion/message/
      cross-system effects.
    - Scaffold is sufficient for an independent verifier to catch missing
      required surfaces before t-2 implementation proceeds.
  return: |
    RESULT with:
    - product repo commit or PR reference;
    - changed files;
    - concise manual check output against checks/markdown-foundation-checklist.md
      and checks/w20-a1-a13-acceptance-map.md;
    - explicit table of required surfaces -> artifact/check coverage;
    - explicit W19/HOW not-chosen check;
    - any gaps or risks found;
    - no product-authored Direction OS state changes or next CALL.
  budget: half focused day
  parent: s-zara-operate-markdown-manager-v1-full-shape-repair-001
  surface: cli