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
      status: parked      # parked | shaped | active | done | dropped
      # shaped/active nodes add:
      # appetite: <e.g. 2w>
      # kill_by: <metric + threshold + date>
      children: []        # expand only when a node approaches activation
```

Rules: outcomes only — tasks never appear here (G2). One `active` node per direction (G1). Width ≤7 open children per node. `dropped` nodes keep one line with the reason — pruning is information. Every non-root node carries its one-line `why`; the full rationale is already stored in the planning session's history file — store rich, load minimal, fetch detail on demand.

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

open_calls:                    # in-flight registry: issued CALLs awaiting their RESULT
  - id: c-117
    to: executor               # session | research | executor
    for: t-2                   # task / recurring / node it serves
    issued: <date>
    note: "прототип в репо игры"

recurring:                     # standing obligations that outlive bets; ≤3 per direction
  - id: r-1                    # adding/removing an entry is an owner decision (G7)
    goal: <e.g. "devlog post">
    done_when: <verifiable>
    cadence: weekly            # pulse checks: today vs last_done + cadence
    lens: audience
    last_done: <date>

decisions:                     # the owner's inbox; answered items move to history
  - q: <question>
    options: [<a>, <b>, <c>]
    recommendation: <a, because ...>

next:                          # ready-to-send CALL for the next session
  <CALL packet, see packets.md>
```

NOW hygiene rules: NOW.md is hot state, not an archive. Keep long evidence in `history/`, `work/`, or `knowledge/`; NOW keeps one-line pointers only. `open_calls` contains only CALLs still awaiting RESULT; returned, done, superseded, or cancelled calls leave this list and live in LOG/history. `decisions` contains only pending owner decisions; answered decisions move to history or a linked work/knowledge artifact. `next` is exactly one CALL packet, or one line pointing to a self-contained CALL artifact under `work/` (for example `CALL: work/c-117-call.md`), never a status digest. No field outside this template — a running narrative field (e.g. an invented `current_truth`) is the same schema drift as an inlined `owner_approved` quote block: `bet.goal` states the outcome, the latest `history/` file states the current status, and NOW points to it in one line.

Recurring rules: entries are NOT tasks (G1/G2 untouched — they have their own ≤3 budget). Only pulse instantiates a due entry, as a ready work CALL in its decision batch; pulse never executes it. A recurring run that can't finish closes with the reason; `last_done` stays unchanged and pulse re-raises it next time.

Open-calls rules: this is how a fresh session on ANY platform sees what is already running and who waits for whom — the recovery point after a crashed chat or a provider switch. A closing RESULT lists the CALLs it issued in `state_changes`; the writer records them here; a returning RESULT clears its entry immediately. Pulse flags entries older than their budget. If a chat died mid-work: nothing is lost except its unwritten conversation — restart from `NOW.next` or the relevant open_calls entry.

## LOG.md

Append-only, newest first, one line per session — literally one line, ≤2 short sentences. The session's full outcome, numbers, and rationale already live in the linked `history/` file; LOG is an index into it, not a second summary:

```
2026-06-12 s-041 work t-3: трейлер-сценарий готов и принят → history/2026-06-12-s-041.md
2026-06-11 s-040 review g-12ab: bet met; дерево +2 узла (audience) → history/2026-06-11-s-040.md
```

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
