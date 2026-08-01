# Schema: direction state files

Templates for the six state file types (KERNEL §3). Keys/statuses stay English; values may use the owner's language. Hot files should fit roughly one screen; audit flags files past ~150 lines. Full rationale, owner words and evidence live in `history/`/`work/`; hot state keeps pointers.

## CHARTER.md

```markdown
# <Direction name>   (id: <direction-id>)

owner_approved: <date> — history/<file>.md
mission: <1-2 sentences>

success_criteria:
  - <2-4 measurable outcomes, dated where possible>

constraints:
  - <hard limits: time, money, health, values>

lenses: [product, audience, business]   # 3-5, direction-specific

premortem:
  - reason: <at least 5 distinct failure reasons>
    response: <mitigation | kill_by candidate | accepted_risk>

outside_view: <2-3 reference cases and sequencing implication>

edges:
  - <3-5 owner advantages, each with proving fact>

risk_posture: explore                  # explore | guarded
repos:
  - <org/repo>: <role>
```

## TREE.md

```markdown
# Goal tree: <direction-id>

owner_approved: <date> — history/<file>.md

- id: g-root
  goal: <mission as outcome>
  done_when: <verifiable>
  children:
    - id: g-xxxx
      goal: <outcome, not activity>
      done_when: <verifiable>
      why: <one line: contribution to parent>
      # outcome_kind: specification  # only when the approved spec artifact itself exhausts done_when
      status: parked              # parked | shaped | active | done | dropped
      # shaped/active add appetite + kill_by
      # detail: history/<file>.md
      children: []
```

Rules: outcomes only; tasks never appear here. At most one non-root node is `active`: `NOW.bet.node`. Future objectives stay visible as `parked|shaped`; they are not execution lanes. Width ≤7 open children per node. Every non-root node has `why`. A dropped node keeps a compact reason/pointer; Git/history hold removed detail. `outcome_kind: specification` is an optional owner-approved card field; absence means ordinary build outcome. Its done_when ends at one exact versioned owner-approved specification, not implementation.

## NOW.md

```markdown
# NOW: <direction-id>          updated: <date> by <session-id>

bet: null                     # legal between objectives
# OR:
bet:
  node: g-xxxx
  goal: <recitation from TREE>
  appetite: 2w (started <date>)
  kill_by: <threshold + date/event>
  forecast: <earliest signal + expected observation>
  against: <strongest contrary case + switch trigger>
  cut_list: [<real exclusions>]
  lens_verdicts:
    product: <task ids | not_needed: reason>
    audience: <...>
    business: <...>

tasks:                         # [] when bet:null; active ≤ the owner-set WIP limit
  - id: t-1
    goal: <outcome>
    done_when: <verifiable>
    status: open               # open | active | blocked | done
    # blocked adds unblock_when

direction_forecast:
  status: no_basis             # no_basis | forecast
  target: <one explicit dated success criterion>
  as_of: <date>
  basis: <history/work/source pointer or exact missing basis>
  drivers: [<major up/down drivers, max 4>]
  update_when: <material evidence/date that forces recompute>
  # status: forecast additionally requires:
  # chance: 35%                # central estimate; not completion percent
  # range: 20-50%
  # confidence: low            # low | medium | high
  # calibration: <empirical reference class/source + denominator>

issues:                         # unresolved only; compact, not a task backlog
  - id: i-ab12                  # stable, never reused
    issue: <one factual problem/unknown>
    level: objective            # direction | roadmap | objective | execution
    route: review               # frame | map | shape | review | work | repair | pulse
    review_when: <date/event>
    evidence: <history/work/knowledge pointer>
    # blocks: <stable node/task/call>

track_wip_limit: 4             # present only with tracks; owner-set, no fixed ceiling
tracks:                         # optional execution lanes inside the current bet
  - id: gameplay
    label: "Gameplay proof"
    for: t-1                    # current bet node/task, or recurring id

open_calls:
  - id: c-117
    track: gameplay             # required when tracks exist
    status: ready               # ready | running | waiting | blocked | paused
    to: executor                # session | research | executor
    for: t-1
    issued: <date>
    call: work/c-117-call.md
    # parent: c-116             # same-lane child
    # waiting_on: [c-117-a]
    # receipts: [history/<result>.md]
    # started: <date/time — launch receipt>     # running
    # unblock_when: <condition>                 # blocked
    # paused_by: <owner history pointer>        # paused
    # note: <one-line context/pointer>

recurring:
  - id: r-1
    goal: <standing obligation>
    done_when: <verifiable>
    cadence: weekly
    lens: audience
    last_done: <date>

decisions:
  - id: d-1
    track: gameplay             # required when tracks exist
    q: <question>
    options: [a, b, c]
    recommendation: <a, because ...>
```

### NOW hygiene

NOW is current state, not a diary. `open_calls`, `issues` and `decisions` contain only unresolved items. Returned/done/cancelled items leave hot state for LOG/history. No free-form running narrative and no removed `next` selector: `RESULT.next` is handoff transport only.

`bet: null` is normal between objectives. Then `tasks: []`, and no non-recurring execution track/CALL may exist; one untracked `frame|map|converge|converge-arch|converge-verify|shape|review|repair` CALL may be the planning frontier. The sole extra legal frontier is `to: session, play: work` for a parked `outcome_kind: specification`: no track/task, exact node in `for`, owner-authority artifact in done_when. It is planning, not an execution lane. The daily adviser may name a conversational focus, but only shape activates a stored build bet.

### Specification outcomes

Map marks the exact approved card `outcome_kind: specification` only when its versioned owner-approved artifact fully satisfies done_when. The node remains `parked`: untracked owner-authority `work` authors the artifact and records exact owner words; a later fresh `converge-verify` refutes it; narrow `review` may then mark it `done`. No active bet, task, track, new status, executor content verdict, or shape exists in this route. A failed verification returns to the authoring CALL. An ordinary successor returns to the activation-readiness router.

### Direction forecast

The forecast estimates one explicit dated direction target, not percentage of tasks finished. `no_basis` is required when no defensible dated basis exists. Numeric chance/range are legal only with a cited empirical reference class or local calibrated denominator plus uncertainty; model intuition alone is not calibration. Update only after material evidence and, in a day chat, explicit owner save words. Do not force daily movement or monotonic improvement. History/LOG records each saved prior estimate; NOW holds only the latest.

### Issues

An issue is a problem/unknown that cannot safely disappear and is not yet admitted work. It needs a route owner and `review_when`; otherwise it is noise and is not saved. Ideas go to captures/TREE, owner choices to decisions, tasks to the active bet, OS defects to MAINTENANCE/FRICTION — not issues. At the trigger, day/pulse routes it: resolve, merge, promote through its owning play, or drop with reason. Removing an issue requires its id plus disposition/evidence in RESULT/history. Issues do not authorize execution or count as progress.

### Execution lanes

Tracks are a routing index for parallel execution inside one active bet, never a strategic hierarchy. Every non-recurring track `for` resolves to the current bet node/task; every call/decision names an existing track when tracks are present. A positive owner-approved WIP limit caps lanes with a non-paused root/decision; occupancy cannot exceed it. Each lane has at most one ordinary parentless root. Children are same-lane, acyclic, listed in direct parent `waiting_on`; return clears only the child, appends its receipt, and makes parent ready only when the last wait clears. Every current lane has a root or decision. Only `shape` creates a lane and only `review` retires it, at the close of the bet it serves; creating/retiring a lane or changing its limit needs cited owner words. Future objectives remain in TREE; unrelated urgent work first routes through review/map/repair.

`ready` is dispatchable. `running` requires an exact owner/runtime launch receipt and is not reoffered. `waiting` has live `waiting_on`; `blocked` has `unblock_when`; `paused` has `paused_by`. Exact lost/cancelled words may move matching `running → ready`; time/silence never does. Call ids are unique forever; a continuation gets a new id.

### Recurring/frontier

Recurring entries are not bet tasks and are capped at 3. Only pulse instantiates due work; incomplete runs do not advance `last_done`.

`open_calls` is the sole durable dispatch frontier. A fresh session resolves named lane/call directly; `продолжаем` opens the sole ready call/decision, shows choices if several, or reports blocks/issues/planning route if none. `что можно делать` shows ready calls plus concise non-ready counts. List order/recommendation is never persisted strategy.

## LOG.md

Newest first, one line/≤2 short sentences per leg with a history pointer. It is an index, not a second summary.

When over the soft ceiling, repair keeps roughly the newest half-ceiling and moves older lines verbatim into `history/LOG-archive-<direction-id>.md`. LOG keeps one bottom pointer: `archived: ... — sessions before <date>`. Later rotations append to that same archive.

## history/

One immutable file per leg: `history/<date>-<session-id>.md`, full RESULT verbatim.

## knowledge/

```markdown
# <claim>
accepted: <date>   read_by: <play/lens and trigger>   status: current | stale
<3-10 lines + evidence pointers>
```

No real `read_by` consumer means no knowledge entry.

## work/

Outputs/evidence, not state. Large binaries use LFS/external storage with a small pointer.

## Truncation guard

Every state file ends with `END_OF_FILE: <path>`. Missing trailer means truncated transport; do not rely on unseen tail.

END_OF_FILE: os/schema/direction-files.md
