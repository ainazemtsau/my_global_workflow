id: s-solmax-operating-substrate-scope-boundary-architecture-forge-001
direction: solmax
play: local/architecture-forge
node/task: g-operating-substrate/scope-boundary
call: c-solmax-operating-substrate-scope-boundary-architecture-forge-001
parent: s-solmax-operating-substrate-architecture-cartography-001-owner-sign
status: done

outcome: |
  Owner approved the first operating-substrate architecture/spec card:
  operating-substrate-scope-boundary-001.

  Frozen scope/boundary answer:
  - Operating-substrate is for abstract customizable AI-process construction.
  - It is not only for owner/project management.
  - It is not only for Zaratusta-like systems.
  - It is not a generic all-AI framework.
  - It is not a pre-frozen component structure.
  - It exists to help construct, reason about, test and evolve different deep
    custom AI-interaction processes, such as Health-like, Zaratusta-like,
    game/productive-play-like, Direction-OS-like and future processes, without
    making any one consumer artifact authoritative.

  Critical owner correction accepted:
  - Candidate elements such as durable state, history, current context,
    procedures, invocation rules, source/evidence links, GitHub/Markdown
    continuation and proof harnesses are NOT frozen by this card.
  - Those are downstream investigation areas.
  - The structure itself must still be designed, justified and proven in later
    cards.

evidence: |
  Owner approved the cartography map before this forge:
    "Так, ну в принципе, с картой согласен. Просто не всё сейчас однозначно,
    там некоторые вопросы кажутся, может, где-то избыточными, но, возможно,
    при прояснении в них появится смысл, поэтому я, в принципе, с ней
    согласен, можем с ней дальше двигаться."

  Owner corrected the initial scope direction in this forge:
    "мы делаем абстрактный процесс"
    "мы не можем сказать, для чего он будет"
    "Возможность построить любой процесс, либо добавлять новые"
    "глубокая кастомизация"
    "Единственное, что различается, это какую структуру данных хранишь и какие
    условно процедуры вызываешь"
    "это должно быть адаптировано для разных задач"

  Owner rejected premature structure freezing:
    "не факт, что такая структура будет"
    "мы должны определить эту структуру саму ещё, что надо, что не надо"
    "Нам нужна абстрактная вещь"
    "Я не хочу, чтобы он становился авторитетным в какую-то структуру"
    "Должно всё быть рассмотрено, должна структура быть построена, как она будет
    работать, почему она будет работать, какие доказательства, что это работает"

  Owner final approval:
    "Approve v2"

  Source-state evidence preserved:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md
    - live/solmax/work/operating-substrate-scope-boundary-cartography-001.md
    - live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md
    - live/solmax/history/2026-07-06-s-solmax-zaratusta-pause-operating-substrate-route-001.md
    - live/solmax/history/2026-07-06-s-solmax-operating-substrate-placement-decision-001.md
    - live/solmax/history/2026-07-06-s-solmax-operating-substrate-umbrella-placement-repair-001.md
    - live/indie-game-development/plays/canon-forge.md as procedural analogy only

accepted_card: |
  Path:
    live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md

  Content:

    # Operating-substrate architecture card — scope/boundary

    status: accepted
    accepted_at: 2026-07-08
    session: s-solmax-operating-substrate-scope-boundary-architecture-forge-001
    call: c-solmax-operating-substrate-scope-boundary-architecture-forge-001
    card_id: operating-substrate-scope-boundary-001
    graph_nodes:
      - q01_system_class
      - q02_boundary_rule

    owner_approval:
      words: |
        Approve v2
      correction_words: |
        "мы делаем абстрактный процесс"
        "мы не можем сказать, для чего он будет"
        "Возможность построить любой процесс, либо добавлять новые"
        "глубокая кастомизация"
        "не факт, что такая структура будет"
        "мы должны определить эту структуру саму ещё, что надо, что не надо"
        "Я не хочу, чтобы он становился авторитетным в какую-то структуру"
        "Должно всё быть рассмотрено, должна структура быть построена, как она будет
        работать, почему она будет работать, какие доказательства, что это работает"

    question: |
      For what class of systems/processes does operating-substrate exist, and by
      what rule do we separate reusable substrate from consumer-specific
      policy/behavior?

    frozen_answer: |
      Operating-substrate exists for abstract customizable AI-process construction.

      It is an abstract basis for building different deep processes of
      interaction with AI: Health-like, Zaratusta-like, game-choice/productive-
      play-like, Direction-OS-like and future processes where the domain changes
      but similar architectural tasks, failures and proof needs repeat.

      This card does NOT freeze a concrete process structure.

      In particular, it does not assert that every process must have a fixed
      set of components such as durable state, history, current context,
      procedures, invocation rules, source/evidence links, GitHub/Markdown
      continuation, test harnesses or any equivalent list. Those are candidate
      investigation areas for later cards.

      The frozen invariant is:

      Substrate must provide a reusable way to design, reason about, test and
      evolve custom AI-processes without making any one consumer's structure
      authoritative.

      Therefore substrate is not a ready structure of a process. It is the level
      at which structures of processes are discovered, justified, tested and
      evolved.

    in_scope: |
      In-scope examples are evidence anchors, not authority:

      1. Health-like process
         A process where AI helps conduct health-related work. This card does
         not decide what state, checks, procedures, safety gates or proof this
         process needs.

      2. Zaratusta-like process
         A process where AI attempts to support or lead a deeper personalized
         interaction. Zaratusta is a failure-case and source of evidence: clean
         surface artifacts were insufficient to prove live behavior.

      3. Game-choice / productive-play process
         A different domain that may still need a recurring customized AI
         interaction rather than one-off answers.

      4. Direction-OS-like process
         A workflow/process example with useful practices, such as bounded
         sessions, state, gates, handoff and result discipline. Current
         Direction OS mechanics remain evidence/source material, not substrate
         authority.

      5. Future arbitrary custom AI-processes
         Any process where the owner wants to construct a stable form of AI
         interaction rather than rely on an ad hoc prompt or one-off chat.

    not_frozen: |
      This card does not freeze:

      - whether the process must have durable state;
      - what "state" means;
      - whether history/current context/procedures are required concepts;
      - how procedures are represented;
      - when procedures are invoked;
      - what source/evidence model exists;
      - what "continue from another chat" technically requires;
      - GitHub/Markdown as permanent substrate;
      - a test harness or proof model;
      - repo/product/backend;
      - live interface;
      - source/context loading;
      - owner/user decision gates;
      - multi-agent/tool/provider boundary.

      Even if GitHub/Markdown is the current practical carrier, this card does
      not make that carrier an architecture law.

    boundary_rule: |
      A thing belongs to substrate only if it is about building custom
      AI-processes across domains, not about one consumer's chosen process.

      Substrate may own:
      - a method for discovering what structure a process needs;
      - criteria for separating reusable process-construction patterns from
        local domain content;
      - a way to evaluate whether a proposed process structure works;
      - a way to avoid repeating known failure modes across Health/Zaratusta/
        game/etc.;
      - vocabulary for comparing candidate structures, without making the
        vocabulary final;
      - proof/research discipline for later cards.

      Consumer owns:
      - actual process structure;
      - actual domain data;
      - actual interaction rhythm;
      - actual procedures, if procedures exist;
      - actual state shape, if state exists;
      - actual safety/policy rules;
      - actual sources;
      - actual interface behavior;
      - actual proof scenarios for that domain.

      Promotion rule:
      A candidate element can become a substrate invariant only after a later
      owner-approved card shows that:
      1. it is necessary across the class of custom AI-process construction,
         not merely useful in one consumer;
      2. it does not smuggle in Health, Zaratusta or Direction OS specifics;
      3. it can be expressed abstractly enough to support different process
         structures;
      4. it has proof/research anchors showing why it works;
      5. owner explicitly approves it.

      Therefore "state", "history", "procedures", "sources", "tests" and
      similar elements are candidate investigation areas, not accepted structure.

    rejected_alternatives: |
      1. Freeze generic component list now
         Rejected because it would make state/history/procedures/evidence
         authoritative before the structure is designed and proven.

      2. Substrate = owner/project operating process
         Rejected because scope is broader: Health, games, Zaratusta-like and
         arbitrary custom AI-processes may all use it.

      3. Substrate = copy Direction OS best practices
         Rejected because Direction OS is evidence, not authority.

      4. Substrate = fix Zaratusta
         Rejected because Zaratusta is a failure-case/source, not the whole
         substrate.

      5. Substrate = generic all-AI framework
         Rejected because the target is not every AI use; it is reusable
         construction of deep custom AI-processes.

    downstream_questions_kept_open: |
      The following remain open:

      - What abstract process structure is needed?
      - What counts as state?
      - Whether history/current context/procedures are required concepts.
      - How process continuation from another chat works.
      - What proof/test environment is needed.
      - How GitHub/Markdown should work now.
      - When/if web-service or URL carrier matters.
      - How Health-like, Zaratusta-like and game-like examples become proof
        cases.
      - What exact cards q03-q14 should become after this scope correction.

    proof_research_anchors_needed_next: |
      This card creates proof pressure but not a test plan.

      Needed next:

      1. Comparable-process analysis
         Take 2-3 different processes, e.g. Health, Zaratusta-like,
         game/productive-play, and identify repeated problems without assuming
         the same structure.

      2. Structure-discovery card
         Decide how substrate discovers/designs the needed process structure
         instead of pre-freezing a component list.

      3. Proof-environment question
         Define what kind of testing/proof can show that a proposed process
         structure actually works, avoiding the Zaratusta failure where surface
         completeness was insufficient.

      4. Current carrier card
         Decide how GitHub/Markdown can serve as the initial practical medium
         without becoming permanent authority.

    gate: |
      PASS.

      The card freezes only the scope/boundary rule. It does not design the full
      substrate, does not answer downstream state/procedure/call/interface/
      source/proof/repo questions, does not create implementation, does not pick
      a repo/backend, does not change the Direction OS kernel, and does not copy
      current Zaratusta or Direction OS artifacts as authority.

    END_OF_FILE: live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md

state_changes: |
  No repository files were modified by this session.

  Apply the following exact Direction OS state changes.

  1) Add file:
     live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md

     Content:
     Use accepted_card.Content from this RESULT exactly, starting at:
       # Operating-substrate architecture card — scope/boundary
     and ending at:
       END_OF_FILE: live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md

  2) live/solmax/NOW.md

     Replace route_status with:
       route_status: operating_substrate_scope_boundary_card_approved_structure_discovery_next

     In owner_directive, preserve the existing umbrella-placement and current
     cartography checkpoint text, then append this paragraph:

       Current scope/boundary card:
       - Owner approved operating-substrate-scope-boundary-001.
       - Frozen scope: operating-substrate is for abstract customizable
         AI-process construction, not only owner/project processes and not only
         Zaratusta-like systems.
       - Frozen boundary: substrate may define reusable ways to discover, reason
         about, test and evolve process structures across domains; it must not
         freeze any one consumer's structure as authority.
       - Not frozen: concrete process structure, state/history/procedure/source/
         evidence/test/repo/backend model. Candidate elements such as state,
         history, procedures, sources and tests remain downstream investigation
         areas.
       - Owner correction: "не факт, что такая структура будет"; "мы должны
         определить эту структуру саму ещё"; "Я не хочу, чтобы он становился
         авторитетным в какую-то структуру".
       - Next route is a structure-discovery architecture/research step: compare
         2-3 processes and decide how substrate should discover/design the
         needed process structure without pre-freezing a component list.

     Preserve:
       active_bet:
         status: none

       tasks: []
       recurring: []
       decisions: []
       open_calls: []

     In preserved_evidence, append these items if absent:
       - live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md
       - owner approval in chat for operating-substrate scope/boundary card v2: "Approve v2"
       - owner correction in chat: "не факт, что такая структура будет ... мы должны определить эту структуру саму ещё ... Я не хочу, чтобы он становился авторитетным в какую-то структуру"

     Replace NOW.next with:
       next: work/calls/c-solmax-operating-substrate-structure-discovery-architecture-forge-001.md

  3) live/solmax/work/calls/c-solmax-operating-substrate-structure-discovery-architecture-forge-001.md

     Add this file with exactly this content:

       CALL c-solmax-operating-substrate-structure-discovery-architecture-forge-001
       to: session
       direction: solmax
       play: local/architecture-forge
       node: g-operating-substrate
       goal: |
         One owner-approved architecture/spec card defines how the operating
         substrate discovers/designs the needed structure of a custom AI-process
         without pre-freezing generic components as authority.
       context: |
         Parent approved card:
         - live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md

         Owner approval words:
         - "Approve v2"

         Owner correction preserved:
         - "не факт, что такая структура будет"
         - "мы должны определить эту структуру саму ещё, что надо, что не надо"
         - "Нам нужна абстрактная вещь"
         - "Я не хочу, чтобы он становился авторитетным в какую-то структуру"
         - "Должно всё быть рассмотрено, должна структура быть построена, как она будет работать, почему она будет работать, какие доказательства, что это работает"
         - "какая-то тестовую среду нам сделать так, чтобы понемногу понимать, что мы структуру, которую делаем, она работает"

         Frozen parent scope:
         - Operating-substrate is for abstract customizable AI-process construction.
         - It is not only owner/project processes.
         - It is not only Zaratusta-like systems.
         - It is not a generic all-AI framework.
         - It is not a pre-frozen component list.

         Frozen parent boundary:
         - Substrate may define reusable ways to discover, reason about, test and
           evolve process structures across domains.
         - Concrete process structure remains consumer-specific unless later
           promoted by an owner-approved card with proof/research anchors.
         - Candidate elements such as state, history, procedures, source/evidence
           and tests are investigation areas, not accepted substrate structure.

         Sources:
         - live/solmax/CHARTER.md
         - live/solmax/TREE.md
         - live/solmax/NOW.md
         - live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md
         - live/solmax/work/operating-substrate-scope-boundary-cartography-001.md
         - live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md
         - any owner-provided Health-like process context if available in-session
       boundaries: |
         Do not design the full operating substrate.
         Do not freeze a final state/history/procedure/source/evidence schema.
         Do not create implementation code.
         Do not create a detailed test harness.
         Do not select or create a substrate product repo.
         Do not change Direction OS kernel.
         Do not copy Health, Zaratusta or Direction OS artifacts as authority.
         Use examples only to compare repeated problems and candidate structure needs.
       done_when: |
         One owner-approved architecture/spec card exists for structure-discovery
         only: it defines how to determine what structure a custom AI-process
         needs, what evidence is sufficient to promote candidate components, and
         what remains consumer-specific. No final process structure, schema,
         procedure catalogue, proof harness, carrier/backend or repo is frozen.
       return: |
         RESULT with the accepted structure-discovery architecture card, owner
         approval evidence, exact state_changes, rejected alternatives,
         downstream questions, gap_event if blocked, and next CALL.
       budget: one focused session
       parent: s-solmax-operating-substrate-scope-boundary-architecture-forge-001
       surface: chatgpt

       END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-structure-discovery-architecture-forge-001.md

  4) live/solmax/LOG.md

     Append this line before END_OF_FILE:

       - 2026-07-08 — architecture forge operating-substrate scope/boundary: owner approved card operating-substrate-scope-boundary-001. Scope is abstract customizable AI-process construction, not only owner/project processes and not a pre-frozen component list. State/history/procedure/source/evidence/test/repo/backend remain downstream; next route is structure-discovery architecture forge. → history/2026-07-08-s-solmax-operating-substrate-scope-boundary-architecture-forge-001.md

  5) live/solmax/history/

     Add:
       live/solmax/history/2026-07-08-s-solmax-operating-substrate-scope-boundary-architecture-forge-001.md

     Content:
       This full RESULT.

  6) CHARTER/TREE consistency note

     Do not edit live/solmax/CHARTER.md or live/solmax/TREE.md in this RESULT.

     Rationale:
     - Existing CHARTER/TREE still say "AI-led stateful owner/project processes".
     - The approved card broadens/repairs that wording to "abstract customizable
       AI-process construction".
     - However, exact CHARTER/TREE text was not presented as a separate
       owner-approved artifact in this session.
     - A later repair or review session may propose exact CHARTER/TREE wording
       if needed under G9.
     - Until then, NOW.md and the accepted card carry the newer scope/boundary
       interpretation for this route.

rejected_alternatives: |
  - Freeze generic component list now.
    Rejected because owner explicitly corrected that the structure is not known
    yet and must not become authoritative before investigation/proof.

  - Substrate = owner/project operating process.
    Rejected because owner broadened scope to arbitrary/custom AI-processes:
    Health-like, game-like, Zaratusta-like and other processes.

  - Substrate = live personal manager only.
    Rejected because it overfits the Zaratusta failure and misses the abstract
    process-construction layer.

  - Substrate = copy Direction OS or Zaratusta.
    Rejected because current artifacts are evidence/source material, not
    authority.

  - Substrate = generic all-AI framework.
    Rejected because the target is deep custom AI-process construction, not
    every AI use.

  - GitHub/Markdown as permanent architecture law.
    Rejected because GitHub/Markdown may be the current practical carrier, but
    carrier/backend boundaries remain downstream.

child_downstream_questions: |
  Immediate next:
  - How does substrate discover/design the needed structure of a custom
    AI-process without pre-freezing generic components?

  Preserved downstream questions:
  - What counts as state, if state is needed?
  - Whether history/current context/procedures are required concepts.
  - How process continuation from another chat works.
  - What proof/test environment is needed.
  - How GitHub/Markdown should work now.
  - When/if web-service or URL carrier matters.
  - How Health-like, Zaratusta-like and game-like examples become proof cases.
  - How source/context loading works.
  - How owner/user decisions and safety gates work.
  - How multi-agent/provider/tool boundaries work.
  - How repo/artifact boundaries are chosen later.
  - Whether the approved scope correction requires a cartography rebalance after
    the structure-discovery card.

gap_event: null

captures:
  - Exact CHARTER/TREE wording may need a later G9-approved repair because the accepted scope broadens prior state wording from "AI-led stateful owner/project processes" to "abstract customizable AI-process construction".
  - Health-like process is now a key example/evidence anchor, but no Health-specific details should be invented without owner-provided context.
  - The owner wants some proof/test environment eventually, but this session did not create a detailed harness or test plan.

decisions_needed: []

play_check:
  - "1 Frame: done — exact q01/q02 question, parent locks, must-decide and must-not-decide were restated."
  - "2 Diverge (owner): done — options were presented; owner corrected the direction with: 'мы делаем абстрактный процесс' and 'мы не можем сказать, для чего он будет'."
  - "3 Draft: done — v2 card drafted after owner correction; it freezes scope/boundary only and demotes state/history/procedure/evidence to candidate investigation areas."
  - "4 Gate: done — previous draft failed for premature structure freezing; v2 passed because it does not answer downstream state/procedure/call/interface/source/proof/repo questions."
  - "5 Freeze & grow (owner): done — owner signed with exact words: 'Approve v2'. Rejected alternatives and downstream questions are recorded."
  - "6 Close & route: done — next CALL routes to structure-discovery architecture forge; no implementation, repo selection, detailed harness or Direction OS kernel change is activated."

log: |
  architecture forge operating-substrate scope/boundary: owner approved card
  operating-substrate-scope-boundary-001. Scope is abstract customizable
  AI-process construction, not only owner/project processes and not a pre-frozen
  component list. State/history/procedure/source/evidence/test/repo/backend
  remain downstream; next route is structure-discovery architecture forge.

next: |
  work/calls/c-solmax-operating-substrate-structure-discovery-architecture-forge-001.md

END_OF_FILE: live/solmax/history/2026-07-08-s-solmax-operating-substrate-scope-boundary-architecture-forge-001.md