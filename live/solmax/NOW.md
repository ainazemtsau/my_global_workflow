# NOW — solmax

project:
  name: Zaratusta
  product_repo: github.com/ainazemtsau/zaratusta

active_bet:
  status: none

map_status: mapped_pending_shape

owner_directive: |
  Zaratusta is not a PoC. Its first real subsystem is a Personal
  Operating System built specifically for the owner.

  The system begins from the former LifeReset concept but every inherited
  entity, process and rule must be analysed independently. Nothing moves
  into the new design merely because it existed before.

  Initial execution should remain Markdown-first where practical, with AI
  assistants acting as interpreters of explicit process contracts. No
  hidden assumptions: missing information becomes a stated assumption,
  an owner question or bounded research.

active_route:
  first_node: g-zara-operate
  order:
    - g-zara-operate
    - g-zara-substrate
    - g-zara-expand
  rationale: |
    First build one coherent owner-facing personal system. Then extract
    reusable capability contracts from demonstrated needs. Only then
    broaden Zaratusta into additional exocortex capabilities.

tasks: []
recurring: []
decisions: []
open_calls: []

preserved_evidence:
  - live/solmax/CHARTER.md
  - live/solmax/TREE.md
  - live/solmax/history/s-map-001.md
  - live/solmax/history/s-shape-001.md
  - live/life-reset/CHARTER.md
  - live/life-reset/LOG.md
  - live/life-reset/history/
  - live/life-reset/work/
  - github.com/ainazemtsau/life-reset-manager
  - github.com/ainazemtsau/zaratusta
  - history/2026-06-25-s-zara-remap-001.md

blocked_reason: |
  No product implementation resumes until g-zara-operate is shaped.

  The node is intentionally a complete-system outcome and may need
  owner-approved child outcomes before tasks are valid. The former
  LifeReset implementation and the old W0 RLK scaffold are evidence only.

next:
  id: c-zara-shape-operate-001
  to: session
  direction: solmax
  play: shape
  node: g-zara-operate
  goal: |
    g-zara-operate has an owner-approved bounded route to implementation
    that preserves the complete Personal Operating System outcome without
    collapsing it into a monolithic prompt or an unbounded bet.
  context: |
    Read:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md
    - history/2026-06-25-s-zara-remap-001.md
    - live/life-reset/CHARTER.md
    - live/life-reset/LOG.md
    - live/life-reset/work/
    - github.com/ainazemtsau/life-reset-manager
    - github.com/ainazemtsau/zaratusta

    Owner requirements:

    - This is not a PoC. Build the real personal system for the owner.
    - A partial week planner is not independently useful; the complete
      minimum must eventually operate coherently.
    - The system contains separately inspectable process contracts rather
      than one compressed instruction.
    - Likely internal concerns include manager identity/authority,
      work-entity model, planning horizons, execution/tracking/review,
      durable state/context/writer, and research/process evolution.
      These are candidates, not pre-approved child nodes.
    - Multi-week courses/projects/programs must exist without requiring a
      separate direction.
    - Logging must produce a bounded context-sensitive operational
      response, not merely save text or dump all state.
    - Research routing, one-task-one-chat where appropriate, long-lived
      logging chats, scoped context and a uniform writer pattern are
      required design concerns.
    - Start Markdown-first; AI is the interpreter. Code requires a
      demonstrated need.
    - Every LifeReset mechanism must be independently assessed.
    - Unknowns and assumptions must be explicit.

    Next-route options already considered by map:

    A. Shape g-zara-operate first — selected and recommended because it
       creates the first real owner-facing system.
    B. Shape g-zara-substrate first — rejected for now because it repeats
       architecture-first sequencing.
    C. Shape g-zara-expand first — rejected because it creates capability
       sprawl before the coordinating system exists.
  boundaries: |
    Do not implement or modify the product repository.
    Do not resume the old W0 RLK route.
    Do not copy the former LifeReset specification wholesale.
    Do not hard-code a 12-week cycle, month model, task taxonomy, journal
    model or response policy without evidence and owner decision.
    Do not hide assumptions inside tasks or architecture.
    Do not reduce the node to a single large prompt.
    Do not declare an isolated week/day/state component equivalent to the
    complete Personal Operating System.
    Do not prescribe medical, psychiatric, nutrition or training
    treatment.
  done_when: |
    One of the following owner-approved outcomes exists:

    A. A bounded active bet for g-zara-operate that passes applicable
       shape gates and has a ready first work CALL.

    B. If g-zara-operate is too large for one valid bet, an owner-approved
       split into 2-4 child outcome nodes, each with goal, done_when,
       status and why, plus a recommended first child and its ready next
       CALL.

    Unknown or disputed load-bearing terms are not guessed. If they block
    Definition-of-Ready, the result routes the selected child to
    converge/research with a self-contained CALL.
  return: |
    RESULT with the approved bet or child split, exact TREE/NOW/LOG
    state_changes, evidence and the next ready CALL.
  budget: one shape session

END_OF_FILE: live/solmax/NOW.md
