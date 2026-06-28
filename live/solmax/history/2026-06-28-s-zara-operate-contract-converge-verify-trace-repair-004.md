RESULT s-zara-operate-contract-converge-verify-trace-repair-004 (call: c-zara-operate-contract-converge-verify-trace-repair-004)
direction: solmax   play: converge-verify   node/task: g-zara-operate-contract

outcome: |
  Verification verdict: PASS.

  The repaired g-zara-operate-contract WHAT is verified after the 2026-06-28
  trace/copyability repair.

  Row failures: none.

  The repaired trace surface is clean:
  - W2 acceptance no longer cites missing G2[explainable]; it now traces to
    valid G2[bounded], G3[auditable], G11[auditable] and G12[copiable].
  - W6 answer no longer cites missing G9[source-backed]; it now traces to
    valid G9[read-not-own] and G10[source-backed], alongside the existing
    owner-override/topic-open/safety traces.
  - W13 answer no longer cites missing G9[source-backed]; it now traces to
    valid G9[context-loaded] and G10[source-backed].
  - W17 answer no longer cites missing G9[source-backed]; it now traces to
    valid G9[read-not-own], G9[context-loaded] and retained valid
    G10[source-backed].

  The owner-boundary model remains intact:
  - no generic domain/topic blacklist;
  - topic work is allowed through process/source/context;
  - Zaratusta writes only to its own workspace/repo by default;
  - Direction OS and other repos/directions/projects remain read-only sources
    by default;
  - future non-Zaratusta writes require explicit narrow integration/procedure.

  W20/A1-A13 remains shape-copyable, topic-open and HOW-clean. Shape may copy
  W20/A1-A13 into Definition-of-Ready or executor done_when, while carrying W19
  routed choices as the PLAN agenda.

evidence: |
  Source state read:
  - os/KERNEL.md.
  - os/plays/converge-verify.md.
  - os/schema/packets.md.
  - live/solmax/CHARTER.md.
  - live/solmax/TREE.md.
  - live/solmax/NOW.md.
  - live/solmax/LOG.md.
  - live/solmax/work/converge-g-zara-operate-contract.md.
  - live/solmax/history/2026-06-26-s-zara-operate-contract-shape-001.md.
  - live/solmax/history/2026-06-26-s-zara-operate-contract-converge-owner-boundary-002.md.
  - live/solmax/history/2026-06-27-s-zara-operate-contract-converge-verify-owner-boundary-002.md.
  - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-trace-repair-003.md.

  Claim attacked:
  - Proposition 1: the repaired question set is COMPLETE enough for shape.
  - Proposition 2: no repaired answer leans on an unresolved question, invalid
    glossary trace, backward contradiction, hidden HOW, generic domain/topic
    blacklist or uncopied owner-boundary assumption.

  Independent oracle used for this repaired run:
  - id: cv-operating-manager-process-source-workspace-contract-v2.1
  - node-class: operating-manager authority contract after owner-boundary and
    trace repair
  - checklist:
    OC1 role boundary / anti-monolith
    OC2 allowed authority verbs: decide, ask, propose, route, refuse, escalate
    OC3 effect tiers, owner approval and side-effect gating
    OC4 source integrity, source ownership, read/write status and integration boundary
    OC5 process registry, process creation, process mutation and deep-research route
    OC6 context loading, source registry and missing-context declaration
    OC7 durable owner-context structure
    OC8 entity and commitment semantics: capture/proposal/accepted commitment separation
    OC9 horizon traceability and review/change route
    OC10 escalation, unknowns, source query, research and stop/audit routes
    OC11 high-stakes/source-owned topics: topic-open, source-backed, not a domain blacklist
    OC12 durable state boundary before the state child: no chat-memory-as-state, no OS write
    OC13 external/irreversible/spend/message/send/cross-system effects require approval/integration
    OC14 HOW firewall: only GitHub/Markdown readability is fixed now; exact UI/storage/schema/
         database/engine/scheduler/automation/API/cadence/scoring remains PLAN/later-child
    OC15 shape-copyability and downstream child-consumer binding through W20/A1-A13

  Completeness attack — TREE done_when split atomically:
  - closed WHAT spec -> W1-W20 and W20/A1-A13: PASS.
  - manager authority -> W1-W7, W12-W16, W18, W20: PASS.
  - effect tiers -> W8, W18, W20/A2/A9/A10: PASS.
  - entity model -> W9, W10, W16, W20/A4/A6: PASS.
  - horizon model -> W11, W13, W14: PASS.
  - escalation rules -> W3, W5, W7, W12, W15, W17, W20: PASS.
  - former forbidden-prescription-zone surface -> G10, W8, W17, W20/A3/A12:
    PASS as repaired process/source/workspace semantics, not as a domain blacklist.
  - implementation can build without guessing powers/scope -> W19, W20/A1-A13: PASS.
  - unsplit compound criteria: none.

  Completeness attack — independent oracle mapping:
  - OC1 role boundary / anti-monolith -> G1, W1, W20/A1: PASS.
  - OC2 authority verbs -> W2-W7 plus W12-W18: PASS.
  - OC3 effect tiers and approval -> G3, W8, W18, W20/A2/A9/A10: PASS.
  - OC4 source integrity/write ownership -> G9, G10, W10, W16, W20/A4/A9: PASS.
  - OC5 process registry/mutation/research -> W5, W15, W20/A7/A8: PASS.
  - OC6 context loading/source registry -> W3, W5, W10, W16, W20/A4/A5: PASS.
  - OC7 owner-context structure -> W9, W16, W20/A6: PASS.
  - OC8 entity/commitment semantics -> W9, W12, W13, W14, W20/A11: PASS.
  - OC9 horizon/review/change route -> W11, W13-W15: PASS.
  - OC10 routing/escalation/research -> W3, W5, W7, W12, W15, W17: PASS.
  - OC11 high-stakes/source-owned topic handling -> G10, W8, W17, W20/A3/A12: PASS.
  - OC12 durable state boundary/no OS write -> W8, W10, W16, W20/A9/A13: PASS.
  - OC13 external/irreversible/spend/cross-system effects -> W8, W18, W20/A10: PASS.
  - OC14 HOW firewall -> W19, W20/A13: PASS.
  - OC15 child-consumer binding -> §COVERAGE child_consumers and W20/A1-A13: PASS.

  Backward-clean attack:
  - Old W0/kernel-first route is not reopened: PASS.
  - LifeReset remains filtered evidence, not automatic authority or wholesale copy: PASS.
  - Direction OS remains read-only for Zaratusta: PASS.
  - Other repos/directions/projects remain read-only sources by default: PASS.
  - Zaratusta default write boundary remains its own workspace/repo: PASS.
  - Future non-Zaratusta writes require explicit narrow integration/procedure: PASS.
  - Owner override and owner approval remain protected: PASS.
  - Generic domain/topic blacklist is not reintroduced by G10/W8/W17/W20-A12: PASS.

  Forward-clean / shape-copyability attack:
  - W20/A1-A13 are copyable and HOW-clean: PASS.
  - A3 and A12 preserve topic-open high-stakes/source-owned handling: PASS.
  - A13 fixes only the owner-clarified first-layer GitHub/Markdown-readable constraint
    and keeps exact UI/storage/vendor/schema/cadence/scoring/scheduler/automation/API
    unchosen: PASS.
  - W2/W6/W13/W17 no longer contain invalid glossary pointers: PASS.
  - Shape can copy W20/A1-A13 into Definition-of-Ready or executor done_when: PASS.
  - Forward-clean overall: PASS.

  Smuggling / trace attack:
  - Current G2 properties are [bounded], [process-routed], [source-backed],
    [override-safe], [no-hidden-power]; active W rows cite only existing G2 properties:
    PASS.
  - Current G3 properties are [tiered], [approval-boundary], [auditable]; active W rows
    cite only existing G3 properties: PASS.
  - Current G9 properties are [read-not-own], [no-scope-capture], [context-loaded],
    [integration-explicit]; active W rows cite only existing G9 properties: PASS.
  - Current G10 properties are [topic-open], [process-routed], [source-backed],
    [workspace-bound], [safety-routed]; active W rows cite only existing G10 properties:
    PASS.
  - Current G11 properties are [auditable], [separate-from-chat], [state-child-owned],
    [owner-context-structured]; active W rows cite only existing G11 properties: PASS.
  - Current G12 properties are [verifiable], [how-free], [copiable],
    [markdown-readable]; active W rows cite only existing G12 properties: PASS.
  - W2 acceptance cites valid G2[bounded], G3[auditable], G11[auditable],
    G12[copiable]: PASS.
  - W6 answer cites valid G9[read-not-own] and G10[source-backed]: PASS.
  - W13 answer cites valid G9[context-loaded] and G10[source-backed]: PASS.
  - W17 answer cites valid G9[read-not-own], G9[context-loaded] and
    G10[source-backed]: PASS.
  - No active WHAT row depends on missing §GLOSSARY properties: PASS.

  FIREWALL attack:
  - No acceptance row requires a specific vendor, framework, UI, database, storage
    backend, exact file layout, exact schema, scheduler, automation, API/subscription
    adapter, cadence, scoring formula or threshold: PASS.
  - The only implementation-facing constraint fixed now is owner-approved
    GitHub/Markdown readability for source registry, process registry,
    owner-context structure, context-loading procedure and examples/tests: PASS.
  - W19 remains the PLAN agenda: PASS.

  Final verdict:
  - complete=PASS.
  - backward_clean=PASS.
  - forward_clean=PASS.
  - smuggling=PASS.
  - row_failures=none.
  - owner_decision_needed=none.
  - next=shape g-zara-operate-contract.

state_changes: |
  - file: live/solmax/work/converge-g-zara-operate-contract.md
    operation: patch
    content: |
      Apply the following exact edits.

      1) Replace header status:

         from:
           status: trace_repaired_pending_converge_verify

         to:
           status: converge_verify_passed_pending_shape

      2) Insert before END_OF_FILE:

         §SIGNOFF: converge-verify passed @ 2026-06-28.
         verify: complete=PASS; backward_clean=PASS; forward_clean=PASS; smuggling=PASS; row_failures=none; oracle=cv-operating-manager-process-source-workspace-contract-v2.1.
         trace_repair_verified:
           - W2 acceptance: valid traces G2[bounded], G3[auditable], G11[auditable], G12[copiable].
           - W6 answer: valid traces G9[read-not-own] and G10[source-backed].
           - W13 answer: valid traces G9[context-loaded] and G10[source-backed].
           - W17 answer: valid traces G9[read-not-own], G9[context-loaded] and G10[source-backed].
         shape_binding:
           copy W20/A1-A13 into Definition-of-Ready or executor done_when unless shape finds a new exact contradiction.
           carry W19 routed choices as PLAN agenda.
           no separate §CONTRACTS section exists in this converge file; W20/A1-A13 are the contract surface for shape.

  - file: live/solmax/NOW.md
    operation: replace
    content: |
      # NOW — solmax
      project:
        name: Zaratusta
        product_repo: github.com/ainazemtsau/zaratusta

      active_bet:
        status: none

      route_status: g-zara-operate-contract_converge_verify_passed_pending_shape

      owner_directive: |
        The first Zaratusta implementation route is g-zara-operate: the LifeReset-derived
        personal operating-manager capability becomes the real Personal Operating System phase
        of Zaratusta, not a PoC and not a separate LifeReset project.

        The owner approved option A on 2026-06-26: g-zara-operate is split into four child
        outcomes:
        - g-zara-operate-contract
        - g-zara-operate-state
        - g-zara-operate-runtime
        - g-zara-operate-evolution

        First child remains g-zara-operate-contract. Shape bounced it back to converge, converge
        repaired the authority WHAT rows that had encoded the wrong forbidden-domain/blacklist
        model, trace repair fixed invalid glossary references, and converge-verify has now passed.

        Preserved owner clarification:
        - Zaratusta manager should not be defined by broad domain prohibitions.
        - The manager may work on any owner-requested domain/topic through the right process
          and source context.
        - The hard boundary is write ownership and side effects: Zaratusta manager writes only
          to its own Zaratusta workspace/repo by default.
        - Other repos/directions/projects are read-only sources by default.
        - Future write access to another system requires an explicit narrow integration/procedure.
        - First implementation layer should be Markdown/GitHub-readable: source registry,
          process registry, owner-context structure, context-loading procedure and examples/tests;
          no DB/API/engine/scheduler/automation now.
        - Deep research is a first-class process/route for creating or improving processes when
          external evidence is needed.

      blocked_reason: |
        No implementation resumes until g-zara-operate-contract is shaped into a bounded bet.
        The repaired WHAT has passed converge-verify:
        - complete=PASS
        - backward_clean=PASS
        - forward_clean=PASS
        - smuggling=PASS
        - row_failures=none

        Shape must copy W20/A1-A13 into Definition-of-Ready or executor done_when unless it finds
        a new exact contradiction. W19 remains the PLAN agenda.

      tasks: []
      recurring: []
      decisions: []
      open_calls: []

      preserved_evidence:
        - live/solmax/CHARTER.md
        - live/solmax/TREE.md
        - live/solmax/LOG.md
        - live/solmax/work/converge-g-zara-operate-contract.md
        - live/solmax/history/2026-06-25-s-zara-remap-001.md
        - live/solmax/history/2026-06-26-s-zara-shape-operate-001b.md
        - live/solmax/history/2026-06-26-s-zara-operate-contract-converge-verify-001.md
        - live/solmax/history/2026-06-26-s-zara-operate-contract-shape-001.md
        - live/solmax/history/2026-06-26-s-zara-operate-contract-converge-owner-boundary-002.md
        - live/solmax/history/2026-06-27-s-zara-operate-contract-converge-verify-owner-boundary-002.md
        - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-trace-repair-003.md
        - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-verify-trace-repair-004.md
        - live/life-reset/CHARTER.md
        - github.com/ainazemtsau/life-reset-manager/SPEC.md
        - github.com/ainazemtsau/zaratusta

      next:
        id: c-zara-operate-contract-shape-002
        to: session
        direction: solmax
        play: shape
        node: g-zara-operate-contract
        goal: |
          Shape g-zara-operate-contract into a bounded implementation bet that preserves the
          verified operating-manager authority WHAT after owner-boundary repair and trace repair.
        context: |
          Read:
          - live/solmax/CHARTER.md
          - live/solmax/TREE.md
          - live/solmax/NOW.md
          - live/solmax/LOG.md
          - live/solmax/work/converge-g-zara-operate-contract.md
          - live/solmax/history/2026-06-26-s-zara-operate-contract-shape-001.md
          - live/solmax/history/2026-06-26-s-zara-operate-contract-converge-owner-boundary-002.md
          - live/solmax/history/2026-06-27-s-zara-operate-contract-converge-verify-owner-boundary-002.md
          - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-trace-repair-003.md
          - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-verify-trace-repair-004.md
          - live/life-reset/CHARTER.md
          - github.com/ainazemtsau/life-reset-manager/SPEC.md

          Converge-verify passed after trace repair:
          - complete=PASS
          - backward_clean=PASS
          - forward_clean=PASS
          - smuggling=PASS
          - row_failures=none

          Copy W20/A1-A13 into Definition-of-Ready or executor done_when unless shape finds a
          new exact contradiction:
          - A1 manager role is separate from source registry, process contracts,
            owner-context structure and state artifacts; no monolithic prompt closes the node.
          - A2 every manager output that changes route/state/commitment carries an authority
            basis, process/source context basis, effect tier and workspace/write boundary.
          - A3 no generic domain/topic blacklist: the manager may work on any owner-requested
            topic through the right process and source context.
          - A4 every source/context item has source id/path/link, owner/scope, read/write
            status, freshness/trust marker and allowed use.
          - A5 every nontrivial operation declares the loaded source/context bundle, missing
            context and route if context is insufficient.
          - A6 owner-context structure represents durable owner facts, preferences, decisions,
            approvals, evidence, unknowns, context summaries and state-change requests inside
            Zaratusta workspace.
          - A7 process registry entries are inspectable contracts with purpose, inputs, outputs,
            authority/effect tier, required source context, owner approval gates and examples/tests.
          - A8 no matching process routes to process draft/research/review; process creation or
            mutation is a proposal or ET2 action with owner approval; hidden self-rewrite is invalid.
          - A9 Direction OS and other repos/directions/projects are read-only sources by default;
            Zaratusta writes only to its own workspace/repo unless an explicit narrow
            integration/procedure is approved.
          - A10 external, irreversible, spend, deletion, message/send or material cross-system
            effects require explicit scoped owner approval before effect.
          - A11 intake/planning/logging preserve commitment semantics: captures are not commitments;
            plans distinguish proposal from accepted commitment and name displacement; log responses
            are bounded to loaded context.
          - A12 high-stakes/source-owned requests are routed by process/source/context: examples/tests
            must show answer/summarize/draft/track/route behavior without topic refusal, while
            unsourced source-owned instructions and unapproved side effects are blocked before effect.
          - A13 first implementation layer is GitHub/Markdown-readable source registry, process
            registry, owner-context structure, context-loading procedure and examples/tests; exact
            UI/storage/vendor/schema/cadence/scoring/scheduler/automation/API choices remain
            unchosen at this layer.

          No separate §CONTRACTS section exists in the converge file; W20/A1-A13 are the contract
          surface to preserve.

          Treat W19 routed choices as PLAN agenda, not as WHAT:
          - exact UI/channel/surface
          - exact storage/schema/file layout/database
          - exact engine/vendor/framework/API/subscription adapter
          - exact horizon durations/cadence/month/12-week model
          - exact non-caving weighing/scoring policy and thresholds
          - exact implementation of state writer and replay
          - exact research procedure mechanics
          - exact automation/scheduler/spend controls
          - exact external integration procedure for future non-Zaratusta writes
          - exact source registry/process registry/owner-context file layout

          Preserve child-consumer edges:
          - g-zara-operate-state consumes W8-W10, W16, W18, W20.
          - g-zara-operate-runtime consumes W1-W20.
          - g-zara-operate-evolution consumes W15, W18-W20.
        boundaries: |
          Do not implement or modify the product repository.
          Do not reopen the old W0/kernel-first route.
          Do not copy LifeReset wholesale.
          Do not reintroduce a generic domain/topic blacklist.
          Do not change the owner-approved rule that the manager may work on any owner-requested
          topic through the right process and source context.
          Do not weaken the write boundary: Zaratusta writes only to its own workspace/repo by
          default; other repos/directions/projects remain read-only sources by default; future
          writes elsewhere require explicit narrow integration/procedure.
          Do not choose UI, storage engine, database, exact schema, exact cadence, scoring,
          automation, scheduler, vendor, framework or API/subscription adapter.
          Do not convert W19 HOW/PLAN choices into WHAT unless shape finds a contradiction that
          must bounce to converge.
        done_when: |
          An owner-approved bounded bet for g-zara-operate-contract exists with appetite, kill_by,
          cut list, lens sweep and tasks that include the riskiest assumption.
          Shape copies W20/A1-A13 into the bet's Definition-of-Ready or executor done_when and
          carries W19 as PLAN agenda.
          If any verified WHAT row becomes inconsistent during shape, the exact row is bounced to
          converge instead of guessed.
        return: |
          RESULT with approved bet or exact bounce, TREE/NOW/LOG state_changes, evidence, and
          next ready work/verify route.
        budget: one shape session

      END_OF_FILE: live/solmax/NOW.md

  - file: live/solmax/LOG.md
    operation: append
    content: |
      - 2026-06-28 — converge-verify g-zara-operate-contract trace repair: PASS. Complete/backward-clean/forward-clean/smuggling all passed; W2/W6/W13/W17 no longer cite missing glossary properties; W20/A1-A13 remains shape-copyable, topic-open and HOW-clean. Next → shape g-zara-operate-contract. → history/2026-06-28-s-zara-operate-contract-converge-verify-trace-repair-004.md

  - file: live/solmax/history/2026-06-28-s-zara-operate-contract-converge-verify-trace-repair-004.md
    operation: create
    content: |
      Store this complete RESULT packet verbatim.

captures:
  - Promote proposed checklist `cv-operating-manager-process-source-workspace-contract-v2.1` to a future knowledge/canon entry for operating-manager authority-contract converge-verify runs; this session does not write knowledge/.

decisions_needed: []

play_check:
  - 1 Recite the claim: done — attacked the two required propositions: completeness of the repaired question set, and absence of unresolved/smuggled assumptions after trace repair.
  - 2 Attack completeness with independent oracle: done — used/authored `cv-operating-manager-process-source-workspace-contract-v2.1`, split TREE done_when atomically, mapped OC1-OC15 plus node criteria to W1-W20 and W20/A1-A13; complete=PASS.
  - 3 Attack smuggling: done — checked W1-W20/W20-A1-A13 active glossary references, W2/W6/W13/W17 trace repair, owner-boundary preservation, forward copyability and FIREWALL; backward_clean=PASS, forward_clean=PASS, smuggling=PASS.
  - 4 Close: done — verdict PASS; state_changes include §SIGNOFF insertion, NOW route to shape, LOG append and history creation; next CALL is shape g-zara-operate-contract with W20/A1-A13 and W19 PLAN agenda.

log: converge-verify g-zara-operate-contract trace repair: PASS; W2/W6/W13/W17 glossary traces repaired and W20/A1-A13 remains shape-copyable/HOW-clean; next shape.

next: |
  CALL c-zara-operate-contract-shape-002
  to: session
  direction: solmax
  play: shape
  node: g-zara-operate-contract
  goal: |
    Shape g-zara-operate-contract into a bounded implementation bet that preserves the
    verified operating-manager authority WHAT after owner-boundary repair and trace repair.
  context: |
    Read:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md
    - live/solmax/LOG.md
    - live/solmax/work/converge-g-zara-operate-contract.md
    - live/solmax/history/2026-06-26-s-zara-operate-contract-shape-001.md
    - live/solmax/history/2026-06-26-s-zara-operate-contract-converge-owner-boundary-002.md
    - live/solmax/history/2026-06-27-s-zara-operate-contract-converge-verify-owner-boundary-002.md
    - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-trace-repair-003.md
    - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-verify-trace-repair-004.md
    - live/life-reset/CHARTER.md
    - github.com/ainazemtsau/life-reset-manager/SPEC.md

    Converge-verify passed after trace repair:
    - complete=PASS
    - backward_clean=PASS
    - forward_clean=PASS
    - smuggling=PASS
    - row_failures=none

    Copy W20/A1-A13 into Definition-of-Ready or executor done_when unless shape finds a
    new exact contradiction. No separate §CONTRACTS section exists in the converge file;
    W20/A1-A13 are the contract surface to preserve.

    Treat W19 routed choices as PLAN agenda, not as WHAT:
    exact UI/channel/surface; exact storage/schema/file layout/database; exact engine/vendor/
    framework/API/subscription adapter; exact horizon durations/cadence/month/12-week model;
    exact non-caving weighing/scoring policy and thresholds; exact implementation of state
    writer and replay; exact research procedure mechanics; exact automation/scheduler/spend
    controls; exact external integration procedure for future non-Zaratusta writes; exact
    source registry/process registry/owner-context file layout.

    Preserve child-consumer edges:
    - g-zara-operate-state consumes W8-W10, W16, W18, W20.
    - g-zara-operate-runtime consumes W1-W20.
    - g-zara-operate-evolution consumes W15, W18-W20.
  boundaries: |
    Do not implement or modify the product repository.
    Do not reopen the old W0/kernel-first route.
    Do not copy LifeReset wholesale.
    Do not reintroduce a generic domain/topic blacklist.
    Do not change the owner-approved rule that the manager may work on any owner-requested
    topic through the right process and source context.
    Do not weaken the write boundary: Zaratusta writes only to its own workspace/repo by
    default; other repos/directions/projects remain read-only sources by default; future
    writes elsewhere require explicit narrow integration/procedure.
    Do not choose UI, storage engine, database, exact schema, exact cadence, scoring,
    automation, scheduler, vendor, framework or API/subscription adapter.
    Do not convert W19 HOW/PLAN choices into WHAT unless shape finds a contradiction that
    must bounce to converge.
  done_when: |
    An owner-approved bounded bet for g-zara-operate-contract exists with appetite, kill_by,
    cut list, lens sweep and tasks that include the riskiest assumption.
    Shape copies W20/A1-A13 into the bet's Definition-of-Ready or executor done_when and
    carries W19 as PLAN agenda.
    If any verified WHAT row becomes inconsistent during shape, the exact row is bounced to
    converge instead of guessed.
  return: |
    RESULT with approved bet or exact bounce, TREE/NOW/LOG state_changes, evidence, and
    next ready work/verify route.
  budget: one shape session
END_OF_FILE: live/solmax/history/2026-06-28-s-zara-operate-contract-converge-verify-trace-repair-004.md
