# Schema: direction state files

Templates for the six state file types (KERNEL §3). Values may be in the owner's language; keep keys and statuses in English. Keep every file on one screen where possible — these files are read at the start of every session, so their size is a tax on everything.

## CHARTER.md

```markdown
# <Direction name>   (id: <direction-id>)

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

repos:                   # product repositories, if any
  - <org/repo>: <what it is>
```

## TREE.md

```markdown
# Goal tree: <direction-id>

- id: g-root
  goal: <mission as an outcome>
  children:
    - id: g-xxxx          # stable 4-hex id, never reused
      goal: <verifiable change in the world, not an activity>
      done_when: <how we'll know>
      status: parked      # parked | shaped | active | done | dropped
      # shaped/active nodes add:
      # appetite: <e.g. 2w>
      # kill_by: <metric + threshold + date>
      children: []        # expand only when a node approaches activation
```

Rules: outcomes only — tasks never appear here (G2). One `active` node per direction (G1). Width ≤7 open children per node. `dropped` nodes keep one line with the reason — pruning is information.

## NOW.md

```markdown
# NOW: <direction-id>          updated: <date> by <session-id>

bet:
  node: g-xxxx
  goal: <copied from tree — recitation>
  appetite: 2w (started <date>)
  kill_by: <metric + threshold + date>
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

decisions:                     # the owner's inbox; answered items move to history
  - q: <question>
    options: [<a>, <b>, <c>]
    recommendation: <a, because ...>

next:                          # ready-to-send CALL for the next session
  <CALL packet, see packets.md>
```

## LOG.md

Append-only, newest first, one line per session:

```
2026-06-12 s-041 work t-3: трейлер-сценарий готов и принят → history/2026-06-12-s-041.md
2026-06-11 s-040 review g-12ab: bet met; дерево +2 узла (audience) → history/2026-06-11-s-040.md
```

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

END_OF_FILE: os/schema/direction-files.md
