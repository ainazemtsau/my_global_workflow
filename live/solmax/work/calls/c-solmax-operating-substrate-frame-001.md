CALL c-solmax-operating-substrate-frame-001
to: session
direction: solmax
play: frame
goal: |
  A new reusable operating-substrate architecture effort is framed for
  AI-led stateful owner/project processes.
context: |
  Current route decision:
  - Zaratusta Operating Manager live-use/product repair is paused.
  - The current Zaratusta Markdown operating-manager-v1 layer is evidence,
    not authority.
  - The first ChatGPT Project live-use trial failed: it produced
    state/intake/handback bureaucracy instead of a useful live personal
    manager flow.

  Owner intent:
  - The problem is broader than Zaratusta.
  - Similar stateful AI process projects may exist or emerge: Zaratusta,
    HLCI/PHL-like systems, Direction-OS/workflow-like systems and future
    owner/project managers.
  - The owner wants a reusable abstraction / architecture for such systems,
    not another local prompt patch.

  Required topics to preserve:
  - abstract state model;
  - procedure model;
  - calls between procedures;
  - live owner interface vs internal state/audit/reporting layer;
  - source/context loading;
  - owner questions and assumptions;
  - one chat = one task / bounded session rules;
  - multi-agent operation with ChatGPT, Codex, Claude and possibly other
    models;
  - architecture of where this substrate applies and how projects use it;
  - testability from the start: scenario tests, transcript tests, test data
    sets or a future test repository/harness for AI systems;
  - small-step development without losing architectural coherence.

  Important boundary:
  - Do not plan the whole architecture in this CALL's context.
  - The next session should frame the work and decide how it sits in the
    TREE/state before detailed design begins.

  Evidence to consider:
  - Zaratusta live-use failure transcript supplied by owner.
  - Zaratusta product repo artifacts as failed/partial evidence.
  - Direction OS principles that already work, including one session/one
    task, CALL/RESULT, durable state, gates and review.
  - Indie Game / GasCoopGame process felt more structured because its
    development structure was explicit.
  - HLCI/PHL should be considered as comparable stateful-process projects if
    the owner provides or points to their context.

boundaries: |
  Do not repair Zaratusta product repo in this session.
  Do not create implementation code.
  Do not create a detailed test plan yet.
  Do not change Direction OS kernel in this session.
  Do not mix the product behavior layer with the development-process layer.
  Do not treat current Zaratusta artifacts as authority.
  Keep the work at the framing/planning-entry level: what is the new
  architecture effort, why it exists, where it applies, and how the next
  Direction OS work should proceed.

done_when: |
  The reusable operating-substrate effort is framed enough for Direction OS
  to continue: its purpose, scope, non-goals, success criteria, constraints,
  lenses or evaluation axes, relationship to Zaratusta/HLCI/workflow-like
  projects, and first next route are clear. The session also determines what
  TREE change is needed and what owner decision, if any, is required before
  adding/activating the new node.

return: |
  RESULT with proposed state_changes for NOW/TREE/LOG/history, any owner
  decisions needed, captured requirements, and next CALL.

budget: one focused session
parent: s-solmax-zaratusta-pause-operating-substrate-route-001
surface: chatgpt

END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-frame-001.md
