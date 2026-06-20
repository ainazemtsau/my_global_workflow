# NOW — life-reset

active_bet:
  id: g-lr-weekly-operating-graph
  status: active
  appetite: |
    One runtime-architecture bootstrap wave before any real weekly operation.
    This bet creates/selects the separate Life-reset Runtime v0 repository or
    workspace and puts the actual runtime architecture skeleton there. It does
    not run a week and does not create a concrete week contract.
  kill_by: >
    2026-06-21: if a separate Life-reset Runtime v0 repository/workspace cannot
    be created or selected and populated with the runtime architecture skeleton,
    stop and review/simplify. Do not compensate by running weekly/daily
    operation inside Direction OS.
  goal: >
    A separate Life-reset Runtime v0 repository/workspace exists and contains
    the architecture skeleton for the personal weekly/daily operating system.
    Direction OS remains the control plane that shapes, repairs, reviews and
    evolves that runtime; the runtime owns weekly/daily operation artifacts,
    state schemas, process/technique lifecycle, provider-facing instructions
    and later concrete week contracts.
  done_when:
    - The architecture evidence already produced in work/ is preserved but no
      longer treated as implementation.
    - A concrete separate runtime repository/workspace exists or is selected.
    - That runtime substrate contains the approved v0 architecture skeleton for
      the actual operating process.
    - The architecture skeleton covers at least: control-plane/runtime boundary,
      state layout, free-form intake, weekly graph model, daily runtime kernel,
      process/technique registry, research/experiment lifecycle,
      checkpoint/logging, weekly review/mutation loop, provider/session/writer
      behavior and source-direction boundaries.
    - No concrete Weekly Contract is created in this bet before the architecture
      skeleton is accepted as ready for pilot.
    - Direction OS records only runtime pointer, architecture summary/evidence,
      owner acceptance and next governing CALL.
    - Life-reset imports only summaries from health/game/Solmax and does not
      become the source of truth for their raw data or tasks.
  evidence_preserved:
    - live/life-reset/work/weekly-operating-graph-dry-run-v0.md
    - live/life-reset/work/sunday-planning-packet-v0.md
    - live/life-reset/work/life-reset-runtime-boundary-v0.md
    - live/life-reset/history/2026-06-20-s-life-reset-runtime-boundary-001.md
  repair_note: |
    2026-06-20: owner rejected task wording that kept turning the next step
    into a provider-instruction task or a near-term "Weekly Contract". The
    correct next step is full runtime architecture bootstrap in a separate
    repository/workspace. Weekly Contract means a later concrete accepted plan
    for a real week; it is not the architecture itself.
  cut_list:
    - No treating live/life-reset Direction OS state as the ongoing weekly/daily
      runtime.
    - No creating or accepting a concrete Weekly Contract in the current next
      CALL.
    - No reducing the runtime architecture to provider-facing instructions
      alone.
    - No permanent provider, chat, board or external-tool architecture beyond
      the already approved separate v0 repository/workspace substrate.
    - No selected productivity technique before the process/technique lifecycle
      exists.
    - No process/activity modules as working modules in this bet.
    - No Solmax/W0 work.
    - No nutrition, training, medical or psychiatric prescription.
    - No game-production or health-core tasks authored by life-reset.
    - No automation.
  lens_sweep:
    - weekly-execution: >
        Needs architecture work: define the weekly graph/contract model in the
        runtime skeleton, but do not create a concrete week yet.
    - daily-discipline: >
        Needs architecture work: define the daily runtime kernel and free-form
        intake/logging model, but do not operate a real day yet.
    - cross-direction-integration: >
        Needs architecture work: source directions provide summaries/links; raw
        health/game/Solmax state stays with its source direction.
    - improvement-and-learning: >
        Needs architecture work: process/technique registry plus
        research/trial/review lifecycle are part of the runtime skeleton.
    - spirit-and-transcendence: >
        Not implemented as a practice now; runtime architecture can preserve
        future candidate hooks.
    - inner-work-and-disclosure: >
        Not implemented as a protocol now; runtime architecture can preserve
        future candidate hooks and safety boundaries.
    - fatherhood-and-example: >
        Not a separate module now; runtime architecture can allow family/value
        constraints to enter future weekly planning.
    - system-quality: >
        Core lens: separate control plane from runtime, preserve portability,
        keep source of truth explicit, and prevent stale packets from becoming
        active route.
    - safety: >
        Needs architecture boundaries: simplify on overload, do not intensify
        discipline into harm, and route clinical/medical matters outside
        life-reset.
  assumptions:
    - The prior architecture discussion can be recovered from the committed
      evidence artifacts without redoing research.
    - A separate runtime workspace can start as Markdown architecture and still
      be substantial enough to support later real operation.
    - Direction OS can govern the runtime through summaries/pointers without
      copying runtime daily data.
  forecast: >
    A runtime-architecture-first repair should stop the repeated premature
    Weekly Contract jump and make the next session mechanically obvious:
    create/select the runtime repo/workspace and put the actual architecture
    skeleton there.
  against: >
    The strongest case against is repo/setup creep. The next task must create
    the runtime substrate and architecture skeleton, not build automation,
    modules or a concrete week.

tasks:
  - id: t-1
    node: g-lr-weekly-operating-graph
    status: open
    kind: session
    goal: >
      The separate Life-reset Runtime v0 repository/workspace exists or is
      selected and contains the runtime architecture skeleton.
    done_when:
      - A concrete runtime repository/workspace path or URL is recorded.
      - The runtime substrate exists locally or is explicitly selected with the
        exact setup blocker/unblock condition recorded.
      - It contains architecture files or documents for the v0 runtime skeleton.
      - The skeleton covers control-plane/runtime boundary, state layout,
        weekly graph model, daily runtime kernel, free-form intake,
        process/technique registry, research/experiment lifecycle,
        checkpoint/logging, review/mutation loop, provider/session/writer
        behavior and source-direction boundaries.
      - It does not contain copied raw health/game/Solmax data.
      - No concrete Weekly Contract is created or accepted in this task.
    tests_assumption: >
      The approved separate runtime substrate can carry the actual architecture
      skeleton before any real weekly planning.

  - id: t-2
    node: g-lr-weekly-operating-graph
    status: open
    kind: session
    goal: >
      The runtime architecture skeleton is audited against the owner-discussed
      cases without running a real week.
    done_when:
      - The audit checks ordinary/high-capacity day, low-capacity day, mid-day
        change, free-form voice log, provider switch, technique trial/review,
        source-direction import and new-idea capture.
      - The audit identifies gaps or confirms the skeleton is ready for a first
        pilot.
      - Any required architecture patch is made in the runtime substrate.
      - No concrete Weekly Contract is created or accepted in this task.

  - id: t-3
    node: g-lr-weekly-operating-graph
    status: open
    kind: session
    goal: >
      The first pilot-planning CALL is ready for the initialized runtime, with
      Direction OS holding only runtime pointer, architecture summary and
      governance state.
    done_when:
      - Direction OS records the runtime pointer and architecture summary.
      - The next CALL explicitly starts the first pilot only after the runtime
        architecture is accepted.
      - The CALL names the runtime substrate as the place where future concrete
        week artifacts live.
      - It does not prescribe health/game/Solmax work outside their source
        directions.

recurring: []

open_calls:
  - id: c-life-reset-runtime-architecture-001
    to: session
    for: t-1
    issued: 2026-06-20
    note: >
      Create/select the separate Life-reset Runtime v0 repository/workspace and
      put the actual runtime architecture skeleton there. Do not create a
      concrete Weekly Contract.

decisions: []

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
    - live/life-reset/work/weekly-operating-graph-dry-run-v0.md
    - live/life-reset/work/sunday-planning-packet-v0.md
    - os/KERNEL.md
    - os/plays/work.md
    - os/adapters/coding-agent.md

    Owner decision already recorded: Life-reset Runtime v0 uses a separate
    repository/workspace. Direction OS remains the control plane. The previous
    route was repaired because it jumped to a concrete Weekly Contract before
    the runtime architecture existed.

    Meaning:
    - Weekly Contract = later concrete accepted plan for a real week.
    - It is not the runtime architecture and must not be created in this CALL.
    - "Provider instructions" are only one component of the runtime skeleton,
      not a standalone next task.
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
    Do not reduce the task to provider-facing instructions alone; provider
    behavior is only one part of the architecture skeleton.
  done_when: |
    - A concrete runtime repository/workspace path or URL is recorded.
    - The runtime substrate exists locally or is explicitly selected with the
      exact setup blocker/unblock condition recorded.
    - It contains architecture files or documents for the v0 runtime skeleton.
    - The skeleton covers control-plane/runtime boundary, state layout, weekly
      graph model, daily runtime kernel, free-form intake, process/technique
      registry, research/experiment lifecycle, checkpoint/logging,
      review/mutation loop, provider/session/writer behavior and
      source-direction boundaries.
    - It does not contain copied raw health/game/Solmax data.
    - No concrete Weekly Contract is created or accepted in this task.
  return: |
    RESULT with runtime substrate pointer, architecture artifact list or exact
    blocker, state_changes and next CALL.
  budget: one focused architecture/bootstrap session
  surface: Codex or Claude Code preferred

END_OF_FILE: live/life-reset/NOW.md
