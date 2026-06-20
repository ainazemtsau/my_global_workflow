# NOW — life-reset

active_bet:
  id: g-lr-weekly-operating-graph
  status: active
  appetite: |
    One runtime-bootstrap wave before any real weekly operation. This bet may
    preserve architecture evidence, create/select the separate runtime
    repository/workspace, minimally initialize it, and then accept the first
    Weekly Contract there. Direction OS must not become the weekly/daily runtime.
  kill_by: >
    2026-06-21: if a separate Life-reset Runtime v0 repository/workspace cannot
    be created or selected and minimally initialized before Sunday planning,
    stop and review/simplify. Do not compensate by running the Weekly Contract
    inside Direction OS.
  goal: >
    A minimal Weekly Operating Graph v0 is prepared and connected to a separate
    Life-reset Runtime v0 repository/workspace. Direction OS remains the control
    plane that shapes, repairs, reviews and evolves the runtime; the runtime
    owns Weekly Contracts, daily operation artifacts, lightweight checkpoints,
    process/technique candidates and provider-facing runtime instructions.
  done_when:
    - The architecture evidence already produced in work/ is preserved but no
      longer treated as proof that the runtime substrate exists.
    - A concrete separate runtime repository/workspace exists or is selected and
      is minimally initialized.
    - The runtime substrate states the control-plane/runtime split.
    - The runtime substrate has an obvious place for Weekly Contracts and
      runtime evidence/checkpoints.
    - The first real Weekly Contract is created inside the initialized runtime
      substrate, not in Direction OS.
    - Direction OS records only runtime pointer, summary/evidence pointers,
      owner acceptance and next governing CALL.
    - Life-reset imports only summaries from health/game/Solmax and does not
      become the source of truth for their raw data or tasks.
  evidence_preserved:
    - live/life-reset/work/weekly-operating-graph-dry-run-v0.md
    - live/life-reset/work/sunday-planning-packet-v0.md
    - live/life-reset/work/life-reset-runtime-boundary-v0.md
    - live/life-reset/history/2026-06-20-s-life-reset-runtime-boundary-001.md
  repair_note: |
    2026-06-20: owner rejected the route that jumped from boundary decision to
    Weekly Contract. The missing step is concrete runtime substrate creation or
    selection. The old t-1/t-2 artifacts remain evidence; the active task list is
    reset to runtime-bootstrap work.
  cut_list:
    - No treating live/life-reset Direction OS state as the ongoing weekly/daily
      runtime.
    - No accepting a Weekly Contract before the separate runtime
      repository/workspace exists and is minimally initialized.
    - No permanent provider, chat, repo, board or external-tool architecture
      beyond the reversible v0 runtime repository/workspace decision already
      approved by the owner.
    - No full daily runtime protocol and no selected productivity technique.
    - No process/activity modules and no full backlog system.
    - No Solmax/W0 work.
    - No nutrition, training, medical or psychiatric prescription.
    - No game-production or health-core tasks authored by life-reset.
    - No automation.
  lens_sweep:
    - weekly-execution: >
        Needs work only after runtime substrate exists; first contract must live
        in that substrate, not in Direction OS.
    - daily-discipline: >
        Not a full task. Runtime may reserve a future place for daily artifacts,
        but no daily protocol is built in this bet.
    - cross-direction-integration: >
        Needs boundary clarity: source directions provide summaries/links; raw
        health/game/Solmax state stays with its source direction.
    - improvement-and-learning: >
        Runtime may name future process/technique registry locations, but no
        registry or practice selection is built now.
    - spirit-and-transcendence: >
        Not needed as a task. Spiritual ideas may later become runtime/process
        candidates.
    - inner-work-and-disclosure: >
        Not needed as a task. No inner-work protocol is prescribed here.
    - fatherhood-and-example: >
        Not needed as a separate task. Family constraints can enter the future
        Weekly Contract.
    - system-quality: >
        Core lens: separate control plane from runtime, preserve portability and
        prevent stale packets from becoming active route.
    - safety: >
        Needs work as boundaries and kill criteria: simplify on overload, do
        not intensify discipline into harm, and route clinical/medical matters
        outside life-reset.
  assumptions:
    - The architecture artifacts are useful as evidence but must not drive the
      next route by themselves.
    - A separate runtime workspace can be minimal Markdown and reversible.
    - Direction OS can govern the runtime through summaries/pointers without
      copying runtime daily data.
  forecast: >
    A runtime-substrate-first repair should stop the repeated Weekly Contract
    jump and make the next session mechanically obvious: create/select/init the
    separate runtime workspace first.
  against: >
    The strongest case against is repo/setup creep. The next task must create
    only enough substrate to host the first Weekly Contract and future evidence.

tasks:
  - id: t-1
    node: g-lr-weekly-operating-graph
    status: open
    kind: session
    goal: >
      The separate Life-reset Runtime v0 repository/workspace exists or is
      selected, is minimally initialized, and is ready to host the first Weekly
      Contract.
    done_when:
      - A concrete runtime repository/workspace path or URL is recorded.
      - The runtime substrate exists locally or is explicitly selected with the
        exact setup blocker/unblock condition recorded.
      - It states that Direction OS is the control plane and the runtime owns
        Weekly Contracts and daily/runtime artifacts.
      - It has at least minimal Markdown locations for Weekly Contracts,
        runtime evidence/checkpoints and provider-facing runtime instructions.
      - It does not contain copied raw health/game/Solmax data.
      - No Weekly Contract is accepted in this task.
    tests_assumption: >
      The approved separate runtime substrate can be made concrete before any
      real weekly planning.

  - id: t-2
    node: g-lr-weekly-operating-graph
    status: open
    kind: session
    goal: >
      The initialized runtime substrate has the minimal operating instructions
      needed for ChatGPT Project, Claude Web, Codex and Claude Code to use it
      without treating chat history or Direction OS as the runtime state.
    done_when:
      - Provider/runtime instructions exist in the runtime substrate or are
        linked from it.
      - They state the session/write-request/writer split.
      - They state where Weekly Contracts and runtime evidence live.
      - They state that Direction OS receives only summaries/pointers/RESULTs.
      - They do not define daily protocols, modules, automation or permanent
        tooling beyond v0.

  - id: t-3
    node: g-lr-weekly-operating-graph
    status: open
    kind: session
    goal: >
      The first real Weekly Contract is created inside the initialized runtime
      substrate, with Direction OS recording only summary/evidence and the next
      governing CALL.
    done_when:
      - The contract exists in the runtime substrate/path established by t-1.
      - It contains refreshed source snapshots, capacity assumptions, selected
        slices, explicit cuts, backlog/candidate handling and the change rule.
      - It records owner acceptance.
      - Direction OS stores only a summary/pointer/RESULT, not raw daily
        runtime logs.
      - It does not choose permanent tooling or prescribe health/game/Solmax
        work outside their source directions.

recurring: []

open_calls:
  - id: c-life-reset-runtime-substrate-001
    to: session
    for: t-1
    issued: 2026-06-20
    note: >
      Create, select or minimally initialize the separate Life-reset Runtime v0
      repository/workspace before any Weekly Contract is accepted.

decisions: []

next: |
  CALL c-life-reset-runtime-substrate-001
  to: session
  direction: life-reset
  play: work
  node: g-lr-weekly-operating-graph
  task: t-1
  goal: |
    The separate Life-reset Runtime v0 repository/workspace exists or is
    selected, is minimally initialized, and is ready to host the first Weekly
    Contract.
  context: |
    Read:
    - live/life-reset/NOW.md
    - live/life-reset/CHARTER.md
    - live/life-reset/TREE.md
    - live/life-reset/work/life-reset-runtime-boundary-v0.md
    - live/life-reset/work/sunday-planning-packet-v0.md
    - live/life-reset/work/weekly-operating-graph-dry-run-v0.md
    - os/KERNEL.md
    - os/plays/work.md
    - os/adapters/coding-agent.md

    Owner decision already recorded: Life-reset Runtime v0 uses a separate
    repository/workspace. Direction OS remains the control plane. The previous
    route to a Weekly Contract was repaired because the runtime substrate did
    not yet exist.

    Preserve these as evidence/templates only:
    - live/life-reset/work/life-reset-runtime-boundary-v0.md
    - live/life-reset/work/sunday-planning-packet-v0.md
    - live/life-reset/work/weekly-operating-graph-dry-run-v0.md
  boundaries: |
    Do not create or accept the first Weekly Contract in this CALL.
    Do not run daily operation.
    Do not store runtime contracts, daily logs, cards or checkpoints in
    Direction OS.
    Do not continue Solmax/W0.
    Do not prescribe nutrition, training, medical or psychiatric treatment.
    Do not shape other life-reset nodes.
    Do not build daily runtime, process/activity modules, automation or a full
    backlog.
    Do not copy raw health/game/Solmax data into the runtime.
    Do not choose permanent tooling beyond the reversible v0 separate
    repository/workspace substrate.
  done_when: |
    - A concrete runtime repository/workspace path or URL is recorded.
    - The runtime substrate exists locally or is explicitly selected with the
      exact setup blocker/unblock condition recorded.
    - It states that Direction OS is the control plane and the runtime owns
      Weekly Contracts and daily/runtime artifacts.
    - It has at least minimal Markdown locations for Weekly Contracts,
      runtime evidence/checkpoints and provider-facing runtime instructions.
    - It does not contain copied raw health/game/Solmax data.
    - No Weekly Contract is accepted in this task.
  return: |
    RESULT with runtime substrate pointer, initialized artifact list or exact
    blocker, state_changes and next CALL.
  budget: one focused setup session
  surface: Codex or Claude Code preferred

END_OF_FILE: live/life-reset/NOW.md
