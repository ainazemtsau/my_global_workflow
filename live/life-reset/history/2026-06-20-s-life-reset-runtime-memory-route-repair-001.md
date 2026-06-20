RESULT s-life-reset-runtime-memory-route-repair-001 (call: c-life-reset-runtime-memory-route-repair-001)
direction: life-reset   play: repair   node/task: g-lr-weekly-operating-graph

outcome: |
  The active runtime-architecture route now requires Data / Memory / Retrieval
  as a first-class layer before the runtime architecture skeleton can be
  accepted for pilot. The next runtime architecture CALL requires
  DATA_MODEL.md, MEMORY_POLICY.md, INDEX_SCHEMA.md and RETRIEVAL.md, states
  that the runtime repository/workspace is the durable source of truth rather
  than ChatGPT/Claude memory, and includes retrieval acceptance cases for past
  weeks, decisions, techniques, captured ideas and process progress.

evidence: |
  Owner-approved correction in the CALL:
  - The runtime must work across future chats/providers without relying on
    hidden chat memory.
  - The assistant should retrieve past weeks, decisions, process results,
    topic history and relevant details without loading the whole repository
    into context.
  - The runtime architecture skeleton must include Data / Memory / Retrieval
    as a first-class layer.

  Updated files:
  - live/life-reset/NOW.md: active_bet done_when, t-1 done_when and NOW.next
    now require the Data / Memory / Retrieval layer, DATA_MODEL.md,
    MEMORY_POLICY.md, INDEX_SCHEMA.md and RETRIEVAL.md; NOW.next states the
    runtime repo/workspace is source of truth and provider memory is interface
    context only.
  - live/life-reset/NOW.md: NOW.next includes retrieval acceptance cases:
    "what happened two weeks ago?", "what did we decide about X?", "how did
    technique Y perform?", "what ideas were captured about Z?", "show process
    P progress over a month".
  - live/life-reset/work/life-reset-runtime-data-memory-retrieval-requirements-v0.md
    records the data/memory/retrieval requirements and boundaries.
  - os/FRICTION.md logs the repeated route-repair pattern for future
    maintenance consideration.

state_changes: |
  NOW.md:
  - Add Data / Memory / Retrieval to the active_bet architecture coverage.
  - Add DATA_MODEL.md, MEMORY_POLICY.md, INDEX_SCHEMA.md and RETRIEVAL.md as
    required first-class architecture files before pilot planning.
  - Add live/life-reset/work/life-reset-runtime-data-memory-retrieval-requirements-v0.md
    to evidence_preserved.
  - Extend t-1 done_when with source-of-truth and retrieval requirements:
      runtime repo/workspace is source of truth;
      ChatGPT/Claude memory is interface context only;
      retrieval cases cover past weeks, decisions, techniques, captured ideas
      and process progress.
  - Extend NOW.next context, boundaries and done_when with the same
    Data / Memory / Retrieval requirements.

  work/:
  - Add live/life-reset/work/life-reset-runtime-data-memory-retrieval-requirements-v0.md
    to record source-of-truth, required architecture files, retrieval
    acceptance cases and boundaries.

  LOG.md:
  - Append the repair line for this data/memory/retrieval route correction.

  os/FRICTION.md:
  - Append one line noting the repeated g-lr-weekly-operating-graph route
    repair and the omitted data/memory/retrieval requirements as a watching
    candidate for future OS maintenance.

  history/:
  - Add this file:
    live/life-reset/history/2026-06-20-s-life-reset-runtime-memory-route-repair-001.md.

captures: []

decisions_needed: []

play_check:
  - "1 Name the contradiction: done — NOW.next required a runtime architecture skeleton, but did not require durable Data / Memory / Retrieval; the CALL's owner-approved correction says the runtime must not rely on hidden provider memory."
  - "2 Reconstruct: done — latest LOG/history shows repeated repairs away from Weekly Contract/provider-instruction shortcuts; TREE root already requires durable state for provider/chat continuation; boundary artifact says chat history is interface context only, not durable state."
  - "3 Propose corrected state: done — NOW/t-1/NOW.next now require DATA_MODEL.md, MEMORY_POLICY.md, INDEX_SCHEMA.md and RETRIEVAL.md, plus explicit retrieval acceptance cases and source-of-truth language."
  - "4 Confirm: done — the CALL supplies the owner-approved correction and required addition; no new owner decision remains."
  - "5 Friction: done — os/FRICTION.md logs the repeated route-repair pattern for future maintenance."

log: "repair: made Data / Memory / Retrieval a required first-class layer of the runtime architecture route; next c-life-reset-runtime-architecture-001 must include DATA_MODEL.md, MEMORY_POLICY.md, INDEX_SCHEMA.md and RETRIEVAL.md."

next: |
  CALL c-life-reset-runtime-architecture-001
  to: session
  direction: life-reset
  play: work
  node: g-lr-weekly-operating-graph
  task: t-1
  goal: |
    The separate Life-reset Runtime v0 repository/workspace exists or is
    selected and contains the runtime architecture skeleton.
  context: |
    Read:
    - live/life-reset/NOW.md
    - live/life-reset/CHARTER.md
    - live/life-reset/TREE.md
    - live/life-reset/work/life-reset-runtime-boundary-v0.md
    - live/life-reset/work/life-reset-runtime-data-memory-retrieval-requirements-v0.md
    - live/life-reset/work/weekly-operating-graph-dry-run-v0.md
    - live/life-reset/work/sunday-planning-packet-v0.md
    - os/KERNEL.md
    - os/plays/work.md
    - os/adapters/coding-agent.md

    Owner decision already recorded: Life-reset Runtime v0 uses a separate
    repository/workspace. Direction OS remains the control plane. The previous
    route was repaired because it jumped to a concrete Weekly Contract before
    the runtime architecture existed.

    Data / Memory / Retrieval repair:
    The runtime must work across future chats/providers without relying on
    hidden ChatGPT/Claude memory. The runtime repository/workspace is the
    durable source of truth for runtime artifacts, data, memory, indexes and
    retrieval. Provider chat memory is interface context only.

    Meaning:
    - Weekly Contract = later concrete accepted plan for a real week.
    - It is not the runtime architecture and must not be created in this CALL.
    - "Provider instructions" are only one component of the runtime skeleton,
      not a standalone next task.
    - Data / Memory / Retrieval is a first-class runtime architecture layer,
      not a later optional feature.
  boundaries: |
    Do not create or accept a concrete Weekly Contract in this CALL.
    Do not run daily operation.
    Do not store runtime contracts, daily logs, cards or checkpoints in
    Direction OS.
    Do not continue Solmax/W0.
    Do not prescribe nutrition, training, medical or psychiatric treatment.
    Do not shape other life-reset nodes.
    Do not build process/activity modules, automation or a full backlog.
    Do not copy raw health/game/Solmax data into the runtime.
    Do not rely on provider memory as the source of truth.
    Do not reduce the task to provider-facing instructions alone; provider
    behavior is only one part of the architecture skeleton.
  done_when: |
    - A concrete runtime repository/workspace path or URL is recorded.
    - The runtime substrate exists locally or is explicitly selected with the
      exact setup blocker/unblock condition recorded.
    - It contains architecture files or documents for the v0 runtime skeleton.
    - The skeleton covers control-plane/runtime boundary, state layout, Data /
      Memory / Retrieval layer, weekly graph model, daily runtime kernel,
      free-form intake, process/technique registry, research/experiment
      lifecycle, checkpoint/logging, review/mutation loop,
      provider/session/writer behavior and source-direction boundaries.
    - The runtime architecture skeleton includes DATA_MODEL.md,
      MEMORY_POLICY.md, INDEX_SCHEMA.md and RETRIEVAL.md as first-class files.
    - DATA_MODEL.md defines the durable runtime entities needed to recover past
      weeks, decisions, process results, topic history and relevant details
      without loading the whole repository into context.
    - MEMORY_POLICY.md states what the runtime stores, what it summarizes, what
      it never stores, and that ChatGPT/Claude memory is not source of truth.
    - INDEX_SCHEMA.md defines retrieval indexes/tags/links for bounded lookup
      across weeks, decisions, techniques, processes, topics and source
      summaries.
    - RETRIEVAL.md defines query flows and acceptance cases for:
        "what happened two weeks ago?"
        "what did we decide about X?"
        "how did technique Y perform?"
        "what ideas were captured about Z?"
        "show process P progress over a month"
    - It does not contain copied raw health/game/Solmax data.
    - No concrete Weekly Contract is created or accepted in this task.
  return: |
    RESULT with runtime substrate pointer, architecture artifact list or exact
    blocker, state_changes and next CALL.
  budget: one focused architecture/bootstrap session
  surface: Codex or Claude Code preferred

END_OF_FILE: live/life-reset/history/2026-06-20-s-life-reset-runtime-memory-route-repair-001.md
