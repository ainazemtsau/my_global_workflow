# Schema: direction state files

Templates for the six state file types (KERNEL §3). Values may be in the owner's language; keep keys and statuses in English. Keep every file on one screen where possible — these files are read at the start of every session, so their size is a tax on everything. Soft ceiling: ~150 lines per file; `audit` flags anything past it as hygiene drift and routes to `repair`.

**Pointers, not evidence.** The writer saves every full RESULT verbatim to `history/<date>-<session-id>.md` (KERNEL §2) — that is already the durable record of an owner's exact words, a session's full rationale, or a decision's evidence. CHARTER.md, TREE.md, NOW.md, and LOG.md never re-paste that content: they hold a one-line pointer to the history/ file that proves it. A field not in this file's template below (e.g. a free-form running narrative) is schema drift, not a legitimate extension — `audit` flags it.

## CHARTER.md

```markdown
# <Direction name>   (id: <direction-id>)

owner_approved: <date> — history/<file>.md   # one line, pointer only (G9); never inline the owner's quotes here

mission: <1-2 sentences: the outcome this direction exists for>

success_criteria:        # 2-4, measurable, dated where possible
  - <criterion>

constraints:
  - <hard limits: time/week, money, health, values>

lenses:                  # competencies this direction must not go blind on
  - product              # adjust per direction; 3-5 lenses
  - audience
  - business

premortem:               # ≥5 distinct failure reasons → response
  - reason: <...>
    response: <mitigation | kill_by candidate | accepted_risk>

outside_view: <paragraph: 2-3 reference cases and what they imply>

edges:                   # 3-5 concrete owner advantages; each cites one past fact proving it
  - <edge — provenance: <fact>>

risk_posture: explore    # explore | guarded — sets the evidence burden (shape reads it);
                         # guarded covers safety-critical until such a direction exists

repos:                   # product repositories, if any
  - <org/repo>: <what it is>
```

## TREE.md

```markdown
# Goal tree: <direction-id>

owner_approved: <date> — history/<file>.md   # one line, pointer only (G9); a later approval appends a new line, never a paragraph

- id: g-root
  goal: <mission as an outcome>
  children:
    - id: g-xxxx          # stable 4-hex id, never reused
      goal: <verifiable change in the world, not an activity>
      done_when: <how we'll know>
      why: <one line: how this node leads to the parent's success>   # mandatory, G9
      # detail: history/<file>.md   # optional ref to the planning session's full rationale
      status: parked      # parked | shaped | active | parallel | done | dropped
      # shaped/active nodes add:
      # appetite: <e.g. 2w>
      # kill_by: <metric + threshold + date>
      children: []        # expand only when a node approaches activation
```

Rules: outcomes only — tasks never appear here (G2). Exactly one non-root node may be `active`: the node in `NOW.bet` (G1). A node currently advanced outside that bet is `parallel`, appears in `NOW.tracks`, and gains no tasks or second appetite from that status. Width ≤7 open children per node. `dropped` nodes keep one line with the reason — pruning is information. Every non-root node carries its one-line `why`; the full rationale is already stored in the planning session's history file — store rich, load minimal, fetch detail on demand.

## NOW.md

```markdown
# NOW: <direction-id>          updated: <date> by <session-id>

bet:
  node: g-xxxx
  goal: <copied from tree — recitation>
  appetite: 2w (started <date>)
  kill_by: <metric + threshold + date>
  forecast: <earliest signal + what we expect to see>   # set in shape; review checks it
  against: <strongest case against + switch trigger>
  cut_list:                    # what this bet deliberately does NOT include
    - <cut item>
  lens_verdicts:
    product: <task ids | not_needed: reason>
    audience: <...>
    business: <...>

tasks:                         # ≤3 active (G1); each ≤ half a focused day
  - id: t-1
    goal: <...>
    done_when: <verifiable>
    status: open               # open | active | blocked | done
    # blocked adds: unblock_when: <...>

track_wip_limit: 3            # required with tracks; positive, owner-approved
tracks:                        # OPTIONAL; required when >1 workstream is current
  - id: core                   # stable short id; owner may say the id or label
    label: "Основная разработка"
    mode: primary              # exactly one primary; others parallel
    for: g-xxxx                # approved node | recurring | local process; has done_when
    # outcome_dispatch: true   # optional; at most one track, owner-approved

open_calls:                    # all outstanding work; authoritative CALL frontier
  - id: c-117
    track: core                # required in track-mode
    status: ready              # ready | waiting | blocked | paused
    to: executor               # session | research | executor
    for: t-2                   # task / recurring / node it serves
    issued: <date>
    call: work/c-117-call.md    # self-contained CALL artifact
    # parent: c-116            # child only; same-track parent CALL id
    # request_kind: outcome    # auxiliary cross-track disposition request
    # requested_by: control    # track with owner-approved outcome_dispatch
    # waiting adds: waiting_on: [c-117-a, c-117-b]  # child/event ids
    # receipts: [history/<return-result>.md]         # bounded child/outcome return pointers
    # blocked adds: unblock_when: <one-line condition>
    # paused adds: paused_by: <owner-verdict history pointer>
    # note: <optional one-line pointer/context; never an evidence block>

recurring:                     # standing obligations that outlive bets; ≤3 per direction
  - id: r-1                    # adding/removing an entry is an owner decision (G7)
    goal: <e.g. "devlog post">
    done_when: <verifiable>
    cadence: weekly            # pulse checks: today vs last_done + cadence
    lens: audience
    last_done: <date>

decisions:                     # the owner's inbox; answered items move to history
  - id: d-1                    # id + track required in track-mode
    track: core
    q: <question>
    options: [<a>, <b>, <c>]
    recommendation: <a, because ...>
```

NOW hygiene rules: NOW.md is hot state, not an archive. Keep long evidence in `history/`, `work/`, or `knowledge/`; NOW keeps one-line pointers only. `open_calls` contains only outstanding CALLs and is the sole dispatch source; returned, done, superseded, or cancelled calls leave it for LOG/history. `decisions` contains only pending owner decisions. No field outside this template — a running narrative field (e.g. `current_truth`) is schema drift: the latest `history/` file holds detail and NOW points to it. The removed pre-migration `next` field has no authority: OPEN, writer, collect, and digest never read or write it. Its presence alone does not block an unrelated RESULT apply; repair deletes it and first registers any still-outstanding sole CALL/pointer in `open_calls`.

The repair clause above is the sole migration exception: it may inspect residue to recover a still-outstanding CALL, never to choose work.

Label normalization for uniqueness: trim, Unicode case-fold, and collapse internal whitespace.

Track-mode rules: `tracks` is a compact grouping index, not another planning hierarchy. `track_wip_limit` is a positive owner-approved integer. A track occupies one WIP slot when it has a non-paused ordinary root or pending decision; waiting/blocked count, while children and outcome requests do not add slots. Occupancy cannot exceed the limit. Track ids and normalized current labels are unique. Every `for` resolves to an approved node/recurring/local scope with done_when. Exactly one entry is `mode: primary`; while a bet exists its `for` names `bet.node`, and between bets it carries the selected review/shape route. Each other entry is `parallel`; a parallel tree node uses `status: parallel`, never `active`, and gains no tasks or authority from the track. Every open call and decision has a stable id and names an existing track. Each track has at most one ordinary root call (no `parent` or `request_kind`); every child names an existing same-track parent, appears in that parent's `waiting_on`, and has acyclic ancestry ending at the root. A returning child clears only its id, removes it from direct-parent `waiting_on`, and adds its history pointer to parent `receipts`; the last return makes that parent `ready`. `ready` means dispatchable, `waiting` has non-empty child/event `waiting_on`, `blocked` carries `unblock_when`, and `paused` requires an owner pause. Full CALLs/evidence live in the pointed artifact/history. Every current track has an ordinary root or pending decision; a track with neither retires. Adding a track cannot bypass G1/G2, owner gates, CALL budget, WIP limit, or product-repo conflict rules.

At most one track may carry owner-approved `outcome_dispatch: true`. Only its ordinary root RESULT may add or expire `request_kind: outcome` rows. Such a row is auxiliary, `ready`, `to: session`, has no `parent`, names a different existing target track and its authorized `requested_by` track, matches the target ordinary root's `for`, and does not count as either track's root. Both tracks must retain non-paused ordinary roots, so both already occupy WIP; there is at most one open outcome request per target. A target RESULT's `outcome` starts with `ACCEPT|COUNTER|BLOCKED`, clears the request and appends its history receipt to both tracks' current roots without changing their statuses or meaning. The requester may expire its own open request with a recorded reason and a receipt on the target root; pausing or retiring either track dispositions its requests first. Adding/removing dispatch authority remains an owner decision.

Recurring rules: entries are NOT tasks (G1/G2 untouched — they have their own ≤3 budget). Only pulse instantiates a due entry, as a ready work CALL in its decision batch; pulse never executes it. A recurring run that can't finish closes with the reason; `last_done` stays unchanged and pulse re-raises it next time.

Open-calls rules: this is how a fresh session on ANY platform sees what is outstanding and who waits for whom — the dispatch source and recovery point after a crashed chat or provider switch. A closing RESULT lists issued CALLs with their track/status; the writer records them by stable call id and preserves unrelated calls. A returning RESULT clears its own entry immediately and may issue one or several successors. Pulse flags entries older than budget. If a chat died, restart that ready call; a runtime's `running` flag is cache, not state authority.

**Call identity.** Call ids are unique within the direction and never reused after leaving hot state; a checkpoint successor gets a new id, and child ids namespace under their issuing call.

**Track lifecycle.** Track kinds/names are never predefined. A RESULT may create a track only from the owner's cited instruction/approval, with a new stable id, human label, primary|parallel mode, approved `for` scope, and a root call or decision. Later RESULTs add/clear calls, block/pause the root, or retire the track by id; creation, retirement, WIP-limit changes, outcome-dispatch authority, and primary handoff remain owner decisions, while ordinary call progression does not. Labels may change without changing identity. Retirement removes the hot row/calls/decisions after honest disposition; LOG/history preserve the lineage. A later unrelated workstream gets a new id, never a recycled one.

**Frontier routing.** Named-track input resolves its sole actionable ready call/pending decision; if several exist, the session shows a compact choice with a recommendation. Unnamed "продолжаем" does the same across the direction: one actionable item opens, several produce grouped choices without state mutation, and none reports waiting/blocked/paused causes. "Что можно делать" renders every ready call grouped by track plus concise waiting/blocked/paused counts. List order and recommendations are never persisted selection.

## LOG.md

Append-only, newest first, one line per session — literally one line, ≤2 short sentences. The session's full outcome, numbers, and rationale already live in the linked `history/` file; LOG is an index into it, not a second summary:

```
2026-06-12 s-041 work t-3: трейлер-сценарий готов и принят → history/2026-06-12-s-041.md
2026-06-11 s-040 review g-12ab: bet met; дерево +2 узла (audience) → history/2026-06-11-s-040.md
```

Track-mode inserts the track id after session-id (`2026-07-17 canon-c117-a1 canon work ...`); legacy lines stay valid.

Archival: entry count alone eventually crosses the soft ceiling even with short lines — that's expected, not a defect. When `repair` trims a LOG.md past the ceiling, it keeps the most recent entries (roughly the newest half of the ceiling) and moves everything older **verbatim** — never rewritten, this is cold storage, not a second editorial pass — into `history/LOG-archive-<direction-id>.md`. LOG.md keeps exactly one pointer line at its oldest (bottom) position: `archived: history/LOG-archive-<direction-id>.md — sessions before <date>`. A later rotation appends to the same archive file and bumps that one date. No play reads the archive file by default; it exists to be opened or grepped on demand.

## history/

One file per session: `history/<date>-<session-id>.md` containing the full RESULT packet verbatim. Never edited after writing.

## knowledge/

One file per durable learning: `knowledge/<topic>.md`

```markdown
# <claim in one line>
accepted: <date>   read_by: <which play/lens reads this, when>   status: current | stale
<3-10 lines: the substance, with links to evidence in history/ or work/>
```

An entry without a real `read_by` consumer does not get written (pulse enforces staleness).

## work/

Products of the direction (documents, scans, assets). Large binaries (.blend, art, video, builds) do not go into git directly: use git-lfs or external storage, leaving a small `.md` pointer in work/ with the link and access note. Git holds what is diff-able.

## Truncation guard

Every state file ends with a trailer line `END_OF_FILE: <path>`. The writer maintains the trailer on every file it writes. A session that reads a state file without its trailer must treat the file as truncated by the transport: say so and do not rely on the unseen tail.

END_OF_FILE: os/schema/direction-files.md
