CALL c-solmax-operating-substrate-scope-boundary-architecture-forge-001
to: session
direction: solmax
play: local/architecture-forge
node: g-operating-substrate
goal: |
  One owner-approved architecture/spec card freezes only the operating-substrate
  scope/boundary rule enough for downstream substrate questions to be forged
  without copying consumer-specific artifacts as authority.
context: |
  Owner approved the first operating-substrate scope/boundary cartography map
  as a working graph.

  Owner approval words:
  "Так, ну в принципе, с картой согласен. Просто не всё сейчас однозначно,
  там некоторые вопросы кажутся, может, где-то избыточными, но, возможно,
  при прояснении в них появится смысл, поэтому я, в принципе, с ней
  согласен, можем с ней дальше двигаться."

  Approved cartography artifact:
  - live/solmax/work/operating-substrate-scope-boundary-cartography-001.md

  Parent locks:
  - Solmax is an umbrella direction.
  - Zaratusta is the first product/application branch, first consumer,
    failure-case and evidence source.
  - Operating-substrate is a sibling architecture/spec route for AI-led
    stateful owner/project processes.
  - Substrate is not a Zaratusta product child.
  - Current Zaratusta and Direction OS artifacts are evidence/source material,
    not authority and not a ready specification.
  - ChatGPT must not autonomously design the whole substrate.
  - The route uses owner-led cartography/forge: one question/card at a time.
  - Some graph nodes may later prove ambiguous or redundant; keep the
    gap/rebalance rule active.

  Forge handoff from cartography:
  - primary nodes: q01_system_class and q02_boundary_rule
  - plain question:
    "For what class of systems/processes does operating substrate exist, and
    by what rule do we separate reusable substrate invariants from
    consumer-specific policy/behavior?"
  - why now:
    This is the hard prerequisite for all downstream state/procedure/call/
    interface/source/proof/repo questions.
  - must decide:
    In-scope class, explicit near/out-of-scope edge cases, and boundary
    criteria for substrate invariant vs consumer-specific policy.
  - must not decide:
    State schema, procedure model, call protocol, live interface, source
    loading, proof harness, repo, implementation or product repair.
  - expected answer shape:
    taxonomy + invariant.
  - first owner question:
    "Какие 2-3 examples точно должны count as in-scope, which tempting
    examples should not count, and what rule separates reusable substrate from
    local consumer behavior?"
  - return_to_graph_if:
    Owner cannot classify Zaratusta/HLCI/Direction-OS-like examples, the
    boundary rule cannot explain why current artifacts are evidence not
    authority, a graph node proves wrongly shaped/redundant in a way that
    affects the first card, or downstream nodes need a different system class.

  Sources:
  - live/solmax/CHARTER.md
  - live/solmax/TREE.md
  - live/solmax/NOW.md
  - live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md
  - live/solmax/history/2026-07-06-s-solmax-zaratusta-pause-operating-substrate-route-001.md
  - live/solmax/history/2026-07-06-s-solmax-operating-substrate-placement-decision-001.md
  - live/solmax/history/2026-07-06-s-solmax-operating-substrate-umbrella-placement-repair-001.md
  - live/indie-game-development/plays/canon-forge.md as procedural analogy only.
boundaries: |
  Do not design the full operating substrate.
  Do not answer downstream graph nodes q03-q14 except as context.
  Do not create implementation code.
  Do not create a detailed test plan or harness.
  Do not change Direction OS kernel.
  Do not activate an implementation bet.
  Do not select or create a substrate product repo.
  Do not copy current Zaratusta or Direction OS artifacts into substrate as
  authority.
  Do not repair Zaratusta product repo.
done_when: |
  One owner-approved architecture/spec card exists for operating-substrate
  scope/boundary only; it records the owner's words, rejected alternatives,
  downstream questions kept open, and proof/research anchors needed next. No
  downstream state/procedure/call/interface/source/proof/repo answer is frozen.
return: |
  RESULT with the accepted scope/boundary architecture card, owner approval
  evidence, exact state_changes, rejected alternatives, child/downstream
  questions, gap_event if blocked, and next CALL.
budget: one focused session
parent: s-solmax-operating-substrate-architecture-cartography-001-owner-sign
surface: chatgpt

END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-scope-boundary-architecture-forge-001.md
