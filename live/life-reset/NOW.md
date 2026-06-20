# NOW — life-reset

active_bet:
  id: g-lr-weekly-operating-graph
  status: active
  appetite: |
    Through Sunday evening planning on 2026-06-21: three small session tasks,
    no extension.
  kill_by: >
    2026-06-21: if Sunday planning cannot produce a minimal accepted Weekly
    Contract for 2026-06-22..2026-06-28 with source snapshots, capacity,
    selected slices, explicit cuts, a change rule and the session->writer rule,
    without selecting permanent tooling or building daily runtime/modules, stop
    and review/simplify instead of extending.
  goal: >
    A minimal Weekly Operating Graph v0 is prepared from the dry-run, adapted
    to the existing Direction OS session/writer model, and used on Sunday
    evening to accept the first real Weekly Contract for 2026-06-22..2026-06-28.
  done_when:
    - A small Sunday planning packet v0 exists and points to the larger dry-run
      instead of duplicating it.
    - The real Weekly Contract for 2026-06-22..2026-06-28 is accepted by the owner.
    - The contract records source snapshots, capacity, selected slices, explicit
      cuts and a rule for changing the week.
    - ChatGPT Project and Claude Web are treated as session surfaces that emit
      RESULT/write requests; Codex and Claude Code can act as writer surfaces.
    - Life-reset imports only summaries from health/game/Solmax and does not
      become the source of truth for their raw data or tasks.
    - A continuation CALL exists for the first selected weekly slice or the
      next honest life-reset action after the contract is accepted.
  cut_list:
    - No permanent provider, chat, repo, board or external-tool architecture.
    - No full daily runtime protocol and no selected productivity technique.
    - No process/activity modules and no full backlog system.
    - No Solmax/W0 work.
    - No nutrition, training, medical or psychiatric prescription.
    - No game-production or health-core tasks authored by life-reset.
    - No automation; Markdown/chat packets are enough for v0.
    - No plan beyond the first real week.
  lens_sweep:
    - weekly-execution: >
        Needs work through t-1 and t-2: the planning packet and first accepted
        Weekly Contract are the core of this bet.
    - daily-discipline: >
        Not a full task. Daily runtime is a later node; this bet only keeps a
        minimal continuation/change rule so the week can start.
    - cross-direction-integration: >
        Needs work through t-1/t-2 source snapshots from game, health, Solmax
        and life-reset without taking ownership.
    - improvement-and-learning: >
        Needs light work: new ideas can be captured/cut in the contract, but no
        registry, module or practice-selection system is built here.
    - spirit-and-transcendence: >
        Not needed as a task. Spiritual ideas may be captured as candidates but
        are not shaped into a practice in this bet.
    - inner-work-and-disclosure: >
        Not needed as a task. Owner state may inform capacity, but no inner-work
        protocol is prescribed.
    - fatherhood-and-example: >
        Not needed as a separate task. Family constraints and values can enter
        capacity/cuts in the Weekly Contract.
    - system-quality: >
        Needs work through t-1/t-3: keep the packet small, provider-portable and
        aligned with existing Direction OS adapters instead of inventing new
        tooling.
    - safety: >
        Needs work as boundaries and kill criteria: simplify on overload, do
        not intensify discipline into harm, and route clinical/medical matters
        outside life-reset.
  assumptions:
    - The weekly graph can stay small enough to help Sunday planning instead
      of becoming planning bureaucracy.
    - The existing session/writer model is enough for ChatGPT, Claude Web,
      Codex and Claude Code without choosing a permanent provider architecture.
    - Source-direction summaries can guide the week without life-reset taking
      ownership of game, health or Solmax state.
    - The owner will accept explicit cuts as part of the contract rather than
      treating them as failure.
  forecast: >
    A small Sunday packet should let the first real week be accepted without
    building tooling, daily methods or modules first.
  against: >
    The strongest case against is that the planning packet keeps expanding into
    a general life OS, or that provider/project setup distracts from accepting
    the actual week.

tasks:
  - id: t-1
    node: g-lr-weekly-operating-graph
    status: open
    kind: session
    goal: >
      A small Sunday planning packet v0 for the first real Weekly Contract
      exists and is ready for owner use.
    done_when:
      - live/life-reset/work/sunday-planning-packet-v0.md exists.
      - It contains only the Sunday inputs, source snapshot fields,
        candidate/card fields, cut/change rule, session/writer rule and owner
        acceptance checklist needed for the first contract.
      - It references live/life-reset/work/weekly-operating-graph-dry-run-v0.md
        as evidence instead of copying the full dry-run.
      - It explicitly cuts permanent tooling, daily-method selection, modules,
        full backlog, Solmax/W0 and source-direction ownership.
      - It is usable from ChatGPT Project, Claude Web, Codex or Claude Code via
        the existing Direction OS adapters and RESULT/write-request flow.
    tests_assumption: >
      The weekly graph can stay small enough to help Sunday planning instead
      of becoming planning bureaucracy.

  - id: t-2
    node: g-lr-weekly-operating-graph
    status: open
    kind: session
    goal: >
      The first real Weekly Contract for 2026-06-22..2026-06-28 is accepted by
      the owner.
    done_when:
      - live/life-reset/work/week-2026-06-22-contract-v0.md exists.
      - It contains refreshed source snapshots, capacity assumptions, selected
        slices, explicit cuts, backlog/candidate handling and the change rule.
      - It records owner acceptance.
      - It does not choose permanent tooling or prescribe health/game/Solmax
        work outside their source directions.

  - id: t-3
    node: g-lr-weekly-operating-graph
    status: open
    kind: session
    goal: >
      The accepted week has a minimal continuation packet and next CALL so it
      can be run from any approved session surface.
    done_when:
      - The accepted contract contains or links a minimal tracker/continuation
        view with selected, doing, blocked, done, cut and review-evidence lanes.
      - ChatGPT/Claude Web behavior is explicit: session only, emits RESULT or
        write request when durable state must change.
      - Codex/Claude Code writer behavior is explicit: apply RESULT state
        changes mechanically and return the next CALL.
      - NOW.next points to the first selected weekly slice or the next honest
        life-reset action after the contract.

recurring: []

open_calls:
  - id: c-life-reset-weekly-graph-t1-packet-001
    to: session
    for: t-1
    issued: 2026-06-20
    note: >
      Prepare the small Sunday planning packet v0 from the existing dry-run and
      provider/session-writer audit; do not build permanent tooling or daily
      runtime.

decisions: []

next: |
  CALL c-life-reset-weekly-graph-t1-packet-001
  to: session
  direction: life-reset
  play: work
  node: g-lr-weekly-operating-graph
  task: t-1
  goal: |
    A small Sunday planning packet v0 for the first real Weekly Contract exists
    and is ready for owner use.
  context: |
    Read:
    - live/life-reset/CHARTER.md
    - live/life-reset/TREE.md
    - live/life-reset/NOW.md
    - live/life-reset/work/weekly-operating-graph-dry-run-v0.md
    - os/adapters/SESSION_PAYLOAD.md
    - os/adapters/chatgpt-project.md
    - os/adapters/claude-project.md
    - os/adapters/coding-agent.md
    - os/KERNEL.md
    - os/plays/work.md

    The owner approved the v0 architecture: ChatGPT Project and Claude Web can
    run as session surfaces; durable writes go through RESULT/write requests to
    Codex or Claude Code writers. Codex may also act as a session and then as
    its own writer under the coding-agent adapter.

    Existing evidence:
    - The large dry-run already explores game/health/Solmax imports, tracker
      lanes, cuts, blockers, reset behavior and review.
    - This task should condense that into a small Sunday packet rather than
      expanding the system.
  boundaries: |
    Do not continue Solmax/W0.
    Do not prescribe nutrition, training, medical or psychiatric treatment.
    Do not select a permanent provider, chat, repo or external-tool architecture.
    Do not build daily runtime, process/activity modules, automation or a full
    backlog.
    Do not shape other life-reset nodes.
    Do not turn life-reset into the source of truth for health or game tasks.
  done_when: |
    - live/life-reset/work/sunday-planning-packet-v0.md exists.
    - It contains only the Sunday inputs, source snapshot fields,
      candidate/card fields, cut/change rule, session/writer rule and owner
      acceptance checklist needed for the first contract.
    - It references live/life-reset/work/weekly-operating-graph-dry-run-v0.md
      as evidence instead of copying the full dry-run.
    - It explicitly cuts permanent tooling, daily-method selection, modules,
      full backlog, Solmax/W0 and source-direction ownership.
    - It is usable from ChatGPT Project, Claude Web, Codex or Claude Code via
      the existing Direction OS adapters and RESULT/write-request flow.
  return: |
    RESULT with the packet path, evidence, state_changes and next CALL for the
    Sunday contract session.
  budget: one focused session
  surface: any session surface; Codex/Claude Code may write only after RESULT

END_OF_FILE: live/life-reset/NOW.md
