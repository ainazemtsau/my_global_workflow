RESULT s-life-reset-map-evidence-001 (call: c-life-reset-map-evidence-001)
direction: life-reset
play: research
node/task: g-life-reset-root

outcome: |
  map_evidence research is available for the first life-reset map session.

  The research compares three coherent architectures:

  - GTD-centered review shell: strongest for capture, trusted inventory and
    weekly review, but weak for cross-direction WIP control and explicit
    drift/recovery states.
  - Kanban-centered pull shell: strongest for daily execution, blockers and WIP
    visibility, but strategically thin for outcomes, incubation and portable
    continuation state.
  - Hybrid direction-contract shell: strongest fit across the requested scope,
    if compressed hard enough to avoid ceremony overload.

  Recommendation: use a minimal hybrid direction-contract shell for map:

  - small outcomes map with directional statuses;
  - accepted Weekly Contract as operating heart;
  - tiny Daily Execution board with default WIP = 1;
  - split backlog with separate incubator;
  - thin review queue and decisions log;
  - portable continuation packet.

  Confidence: moderate. Strong on structure and operating-kernel evidence;
  weaker on owner-specific health/life-reset adapter details because the deep
  research session reported that it could not separately retrieve the approved
  life-reset state and discrete health workflow-graph evidence.

evidence: |
  Owner provided the deep-research report on 2026-06-19:
  "Life-Reset Operating Architecture Evidence Report".

  The report claims decision-relevant support from:

  - internal Direction OS / Clean Workflow Runtime concepts: accepted state is
    not chat transcript, active front stays small, route changes require review,
    continuation packets preserve portable state, and documents count only when
    they unlock work, decide, validate or remove blockers;
  - the canonical game-development state pattern: one primary route, support
    tracks, watched/parked tracks and review queue rather than flat equality;
  - GTD Weekly Review and action-choice criteria;
  - weekly planning experiment evidence;
  - progress-monitoring meta-analysis;
  - implementation-intention evidence;
  - cognitive-offloading and reminder evidence;
  - habit-formation reviews;
  - Kanban WIP/flow guidance;
  - OpenAI state-management / long-running-agent guidance.

  Source transport limitation:
  the pasted report contains ChatGPT/Deep Research citation markers
  (`filecite`/`cite`) and source names, not durable URLs inside this repo.
  The evidence is sufficient for the next owner co-created map session, but any
  later hard claim should preserve or replace those citations with durable
  source links.

  Key risk evidence from the report:
  copying the full node-heavy, artifact-heavy Direction OS structure into
  everyday life would likely become too heavy. The map should preserve the
  acceptance/review/portable-state discipline while keeping the human-facing
  life-reset shell compact.

state_changes: |
  UPDATE live/life-reset/NOW.md:
  - replace next CALL c-life-reset-map-evidence-001 with CALL
    c-life-reset-map-001 for play: map on node g-life-reset-root.
  - carry the research recommendation and candidate outcomes into the CALL
    context.
  - keep active_bet status none, tasks [], recurring [], open_calls [] and
    decisions [] unchanged.

  APPEND live/life-reset/LOG.md:
  - 2026-06-19 - research: map_evidence report supports a minimal hybrid
    direction-contract shell; next is owner co-created top-level map.

  No CHARTER.md or TREE.md changes.

captures:
  - Research candidate: trusted weekly control exists.
  - Research candidate: portable state survives chat changes.
  - Research candidate: health has a low-burden operating loop.
  - Research candidate: game development has a protected proof lane.
  - Research candidate: backlog and incubator are separated.
  - Research candidate: review decisions happen on purpose.
  - Recommended architecture: minimal hybrid direction-contract shell.
  - Alternative rejected as complete solution: pure GTD-centered review shell.
  - Alternative rejected as complete solution: pure Kanban-centered pull shell.
  - Risk to preserve for map: ceremony density can kill life-reset before a real week is run.
  - Citation hygiene: later durable knowledge should replace transported Deep Research citation markers with stable source links.

decisions_needed: []

play_check:
  - '1 Recite: done - research target was c-life-reset-map-evidence-001; expected return was findings, dated sources, confidence/limits, map candidates, captures and a ready map CALL; budget was one deep-research-capable session.'
  - '2 Investigate: done - owner provided the external deep-research report dated 2026-06-19 covering GTD-centered, Kanban-centered and hybrid architectures, operating states, burdens, risks, falsification conditions and candidate map outcomes.'
  - '3 Confidence: done - report separates established evidence from inference at a usable level and states moderate confidence, with lower confidence where approved life-reset and health evidence was not directly retrievable by that session.'
  - '4 Close: done - findings are normalized into this RESULT, state_changes move NOW.next to a ready map CALL, and captures preserve candidate outcomes and risks.'

log: |
  2026-06-19 research c-life-reset-map-evidence-001: evidence supports a
  minimal hybrid direction-contract shell; next is owner co-created top-level
  map.

next: |
  CALL c-life-reset-map-001
  to: session
  direction: life-reset
  play: map
  node: g-life-reset-root
  goal: |
    Produce the first owner-approved top-level goal map for life-reset, grounded
    in the approved frame state and the map_evidence research result.
  context: |
    Read:
    - live/life-reset/CHARTER.md
    - live/life-reset/TREE.md
    - live/life-reset/NOW.md
    - live/life-reset/history/2026-06-19-s-life-reset-map-evidence-001.md
    - os/KERNEL.md
    - os/plays/map.md

    The map_evidence research recommends a minimal hybrid direction-contract
    shell: small outcomes map, accepted Weekly Contract, WIP-limited Daily
    Execution board, split backlog/incubator, thin review queue/decision log
    and portable continuation packet. It compares GTD-centered, Kanban-centered
    and hybrid architectures, with moderate confidence.

    Research candidates, not accepted TREE nodes:
    - trusted weekly control exists;
    - portable state survives chat changes;
    - health has a low-burden operating loop;
    - game development has a protected proof lane;
    - backlog and incubator are separated;
    - review decisions happen on purpose.

    The research also flags a core risk: copying too much ceremony from the
    Direction OS/kernel patterns into everyday life would make the system too
    heavy before a real week is run.
  boundaries: |
    Do not continue Solmax/W0.
    Do not prescribe nutrition, training, medical or psychiatric treatment.
    Do not select a permanent provider, chat, repo or external-tool architecture.
    Do not create tasks, choose an active bet or shape any node.
    Do not split below the top-level map.
    Do not treat research candidates as already accepted owner decisions.
  done_when: |
    TREE.md holds an owner-approved top-level life-reset map under
    g-life-reset-root, every non-root node has a one-line why, and NOW.md points
    to the recommended shape CALL.
  return: |
    RESULT with the approved TREE.md changes, rejected/parked candidates,
    captures, log line and next shape CALL.
  budget: one map session

END_OF_FILE: live/life-reset/history/2026-06-19-s-life-reset-map-evidence-001.md
