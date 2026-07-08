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
