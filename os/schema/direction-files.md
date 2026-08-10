# Schema: direction state files

Templates for the five state file types (KERNEL §3). Keys/statuses stay English; values may use the owner's language. Hot files should fit roughly one screen; audit flags files past ~150 lines. Full rationale, owner words and evidence live in `history/`/`work/`; hot state keeps pointers.

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

## cards/

State lives in `live/<direction-id>/cards/` — one entity, one file, `<id>.md`. Kinds: `bet` · `node` · `task` · `call` · `issue` · `decision` · `recurring` · `track`; a top-level key with no assigned home keeps its own `extra` card named after the key, so nothing is lost silently. Carrier names lead with `_` — `_kind`, `_pos`, `_parent`, `_bet` — so an owner field may be named anything, including `kind` and `status`.

A card is a short YAML header between `---` lines, then `## <name>` body blocks, then the `END_OF_FILE:` trailer. Header values are single-line and short; anything longer, multi-line, or a list/dict is a body block, lists and dicts under a YAML fence. `_pos` is the place among same-kind siblings; for a `node` the place is among siblings under the same `_parent`.

Every card carries a `## журнал` block: its own history, newest first, one line/≤2 short sentences per leg — `<date> · <what changed> · <history pointer or commit>`. It is an index, not a second summary; `osctl check` states the line count of a journal past 20 — as a fact, with no advice attached. The count is NOT stated for `node` and `bet`: the ceiling only means something where the card leaves hot state by its own `card close`, and those two are closed by `review` after several waves. Journals are append-only in every kind; there is no trim command and none is wanted, because a rewritable journal is a rewritable record.

Known head fields, one list for every kind — `osctl check` names any head field outside it and `card unset` removes it. It is a visibility rule, not a ban: forbidding unknown keys outright would break running legs, and the promise that they were "impossible" was false for six weeks while eight live tasks carried `order` beside `_pos` with different values.

`id` · `_kind` · `_pos` · `_parent` · `_bet` · `status` · `label` · `hook` · `detail` · `by` · `outcome_kind` · `goal` · `why` · `appetite` · `kill_by` · `track` · `for` · `to` · `issued` · `call` · `description` · `description_by` · `label_by` · `opened` · `node` · `level` · `route` · `evidence` · `review_when` · `blocks` · `repo` · `engineering_contract` · `play` · `slot` · `basis` · `closed` · `cadence` · `lens` · `last_done` · `about` · `asks` · `from` · `source` · `parent` · `waiting_on` · `receipts` · `started` · `unblock_when` · `paused_by` · `note` · `superseded_by` · `at` · `updated`

Terminal status `superseded` — this card was overtaken by another, which is a different fact from abandoned. It is written only by `repair`, only through `card close --status superseded --superseded-by <id>`, and the command refuses it without the successor: without naming what overtook it, the status says no more than `dropped`. It stamps `superseded_by` and `at`.

State changes only through `osctl`: `card new|set|block|unset|close|reopen`, `log add`, `leg close`. A card is never hand-edited. `card close` writes the reason into the journal and moves the file to `cards/closed/` in the same format; `card reopen` returns it. A closed card reads exactly like a live one, so closing loses nothing. `card new` refuses a card without the human fields it enforces — `label` and `hook` on a `node`, `description` on a `call` — so no card shows the owner a machine id.

The direction journal is assembled from these journals plus `git log`: the commit message is the journal line. Full leg reports stay in `history/`.

### node

```markdown
---
id: g-xxxx
_kind: node
_parent: g-0c26             # absent on the root
_pos: 3                     # place among siblings
label: <short human name>
hook: <one line: what this is>
status: parked              # parked | shaped | active | done | dropped
# by: 2026-08-31            # date the goal must be MET by — ONLY when the owner named it
# outcome_kind: specification  # only when the approved spec artifact itself exhausts done_when
# shaped/active add appetite + kill_by
# detail: history/<file>.md
---

## goal
<outcome, not activity>
## done_when
<verifiable>
## why
<contribution to parent>
```

The goal tree is the set of `node` cards: `_parent` says whose child a node is, `_pos` its place among siblings. Rules: outcomes only; tasks are never `node` cards. At most one non-root node is `active`: `NOW.bet`. Future objectives stay visible as `parked|shaped`; they are not execution lanes. Width ≤7 open children per node. Every non-root node has `why`. A dropped node keeps a compact reason/pointer; Git/history hold removed detail. `outcome_kind: specification` is an optional owner-approved card field; absence means ordinary build outcome. Its done_when ends at one exact versioned owner-approved specification, not implementation.

### bet

One card while a bet is open; none between objectives (`NOW.bet: null`).

```markdown
---
id: bet-g-xxxx
_kind: bet
node: g-xxxx
opened: <date>
---

## goal
<recitation from the node card>
## appetite
2w (started <date>)
## kill_by
<threshold + date/event>
## forecast
<earliest signal + expected observation>
## against
<strongest contrary case + switch trigger>
## cut_list
<real exclusions>
## lens_verdicts
product: <task ids | not_needed: reason>
audience: <...>
business: <...>
```

### task

No `task` card exists while `NOW.bet` is null; active ≤ the owner-set WIP limit.

```markdown
---
id: t-1
_kind: task
_bet: g-xxxx
status: open                # open | active | blocked | done
# blocked adds unblock_when
---

## goal
<outcome>
## done_when
<verifiable>
```

### issue

Unresolved only; a pointer card, not a task backlog or an archive.

```markdown
---
id: i-ab12                  # stable, never reused
_kind: issue
level: objective            # direction | roadmap | objective | execution
route: review               # frame | map | shape | review | work | repair | pulse
evidence: <history/work/knowledge pointer>
# blocks: <stable node/task/call>
---

## issue
<one factual problem/unknown>
## review_when
<date/event>
```

### track, call, decision

```markdown
---
id: gameplay
_kind: track
label: "Gameplay proof"
for: t-1                    # current bet node/task, or recurring id
---
```

```markdown
---
id: c-117
_kind: call
_bet: g-xxxx
track: gameplay             # required when tracks exist
status: ready               # ready | running | waiting | blocked | paused
to: executor                # session | research | executor
for: t-1
issued: <date>
call: work/c-117-call.md
description: <one line: what this call is for>
# parent: c-116             # same-lane child
# waiting_on: [c-117-a]
# receipts: [history/<result>.md]
# started: <date/time — launch receipt>     # running
# unblock_when: <condition>                 # blocked
# paused_by: <owner history pointer>        # paused
# note: <one-line context/pointer>
---
```

```markdown
---
id: d-1
_kind: decision
track: gameplay             # required when tracks exist
about: g-5a7c               # the card this belongs to; omit for the whole direction
---

## q
<question>
## options
<a, b, c>
## recommendation
<a, because ...>
```

### question

An open question with no options yet. `about` is what makes it findable, `asks` is
who owes the answer. `osctl context` puts owner-owed ones at the top of any leg
whose working set contains the `about` card, so he meets the question in chat
instead of in a file he never opens. A capture needing his word is this card, never
prose in a report: 395 capture lines accumulated in `history/`, and the one play
that reads them ran once in 213 legs.

```markdown
---
id: q-cargo-hits-player-001
_kind: question
about: g-5a7c               # omit for the whole direction
asks: владелец              # владелец | нога — who owes the answer
opened: <date>
---

## q
<the question in the words it was asked>
## why_it_matters
<what stalls, or gets invented, while it stays unanswered>
```

### idea

The other half of the same capture: content nobody is committed to build. An idea
is **never a requirement** — no leg may treat one as a `done_when` line, and no bet
absorbs one without the owner's word. `from` is load-bearing: his own deferred
content and a leg's invention must never become indistinguishable, which is the
failure the approval registry exists to prevent. `source` points at the report the
idea came from, so the reasoning survives without being copied.

Closes with `card close --status taken|dropped`: `taken` names the card that
absorbed it, `dropped` names why.

```markdown
---
id: idea-music-box-001
_kind: idea
about: g-5a7c               # omit for the whole direction
from: владелец              # владелец | нога — whose idea this is
source: history/2026-08-08-s-repair-g-5a7c-wave-reshape-001.md
opened: <date>
---

## idea
<one short paragraph: what it is>
## his_words
<verbatim quote — only when it exists; never paraphrased into one>
```

### recurring

```markdown
---
id: r-1
_kind: recurring
cadence: weekly
lens: audience
last_done: <date>
---

## goal
<standing obligation>
## done_when
<verifiable>
```

### extra

A top-level key with no assigned home keeps its own card named after the key. Two exist: `owner_approved`, the approval registry, which is never dropped; and `direction_forecast`.

```markdown
---
id: direction_forecast
_kind: extra
---

## direction_forecast
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
```

## NOW.md

A pointer to the direction, and nothing longer.

```markdown
# NOW: <direction-id>

bet: g-xxxx                    # id of the active bet's node card, or null
track_wip_limit: 4             # present only with tracks; owner-set, no fixed ceiling

END_OF_FILE: live/<direction-id>/NOW.md
```

Everything NOW once carried as sections — tasks, open_calls, issues, decisions, recurring, tracks, direction_forecast — is a card in `cards/`.

### Hot state hygiene

Live cards are current state, not a diary. `call`, `issue` and `decision` cards stay live only while unresolved. Returned/done/cancelled entities leave hot state by `osctl card close`; their journals and `history/` hold the record. No free-form running narrative and no removed `next` selector: `RESULT.next` is handoff transport only.

`bet: null` is normal between objectives. Then no live `task` card exists, and no non-recurring execution track/CALL may exist; one untracked `frame|map|converge|converge-arch|converge-verify|shape|review|repair` CALL may be the planning frontier. The sole extra legal frontier is `to: session, play: work` for a parked `outcome_kind: specification`: no track/task, exact node in `for`, owner-authority artifact in done_when. It is planning, not an execution lane. The daily adviser may name a conversational focus, but only shape activates a stored build bet.

### Specification outcomes

Map marks the exact approved card `outcome_kind: specification` only when its versioned owner-approved artifact fully satisfies done_when. The node remains `parked`: untracked owner-authority `work` authors the artifact and records exact owner words; a later fresh `converge-verify` refutes it; narrow `review` may then mark it `done`. No active bet, task, track, new status, executor content verdict, or shape exists in this route. A failed verification returns to the authoring CALL; a second failed verification ends that loop into one owner decision instead of a third round. An ordinary successor returns to the activation-readiness router.

### Direction forecast

The forecast estimates one explicit dated direction target, not percentage of tasks finished. `no_basis` is required when no defensible dated basis exists. Numeric chance/range are legal only with a cited empirical reference class or local calibrated denominator plus uncertainty; model intuition alone is not calibration. Update only after material evidence and, in a day chat, explicit owner save words. Do not force daily movement or monotonic improvement. History and the card's own journal record each saved prior estimate; the card holds only the latest.

### Issues

An issue is a problem/unknown that cannot safely disappear and is not yet admitted work. It needs a route owner and `review_when`; otherwise it is noise and is not saved. Ideas go to captures/`node` cards, owner choices to decisions, tasks to the active bet, OS defects to MAINTENANCE/FRICTION — not issues. At the trigger — or earlier, when a leg's own evidence settles it — day, pulse, or a leg whose play is named in the row's `route` **and whose own `Writes:` line covers issues — an unqualified state line counts, a line qualified to other sections does not** routes it: resolve, merge, promote through its owning play, or drop with reason. The play's `Writes:` line is the grant; this schema never hands a play authority that line withholds, and a `route` naming no play at all, or one barred from `live/**`, hands out nothing. Rows those routes carry stay closable by day/pulse. Removing an issue requires its id plus disposition/evidence in RESULT/history; closing is an ordinary state change, not an owner-approval event. A card is a pointer, never an archive: template keys only, `issue`/`review_when` ≤2 short sentences each, `evidence` pointers only, ~800 characters per card outside its `## журнал`. Owner words, analysis and enumerated findings stay in `history/`/`work/`; a settled durable fact goes to `knowledge/` — never into a new key on the row. The pointer form is guidance for rows written from 2026-08-05 on: `audit` flags a row past it by id, nothing bounces on its shape. Rows written on or before 2026-08-05 stay valid unchanged; no migration is required, they are never retro-illegal, and their shape is never a reason to clear, compact or repair them (repair play, Removal boundary). Issues do not authorize execution or count as progress.

### Execution lanes

Tracks are a routing index for parallel execution inside one active bet, never a strategic hierarchy. Every non-recurring track `for` resolves to the current bet node/task; every call/decision names an existing track when tracks are present. A positive owner-approved WIP limit caps lanes with a non-paused root/decision; occupancy cannot exceed it. Each lane has at most one ordinary parentless root. Children are same-lane, acyclic, listed in direct parent `waiting_on`; return clears only the child, appends its receipt, and makes parent ready only when the last wait clears. Every current lane has a root or decision. Only `shape` creates a lane and only `review` retires it, at the close of the bet it serves; creating/retiring a lane or changing its limit needs cited owner words. Future objectives remain `node` cards; unrelated urgent work first routes through review/map/repair.

`ready` is dispatchable. `running` requires an exact owner/runtime launch receipt and is not reoffered. `waiting` has live `waiting_on`; `blocked` has `unblock_when`; `paused` has `paused_by`. Exact lost/cancelled words may move matching `running → ready`; time/silence never does. Call ids are unique forever; a continuation gets a new id.

### Recurring/frontier

Recurring entries are not bet tasks and are capped at 3. Only pulse instantiates due work; incomplete runs do not advance `last_done`.

Live `call` cards are the sole durable dispatch frontier. A fresh session resolves named lane/call directly; `продолжаем` opens the sole ready call/decision, shows choices if several, or reports blocks/issues/planning route if none. `что можно делать` shows ready calls plus concise non-ready counts. List order/recommendation is never persisted strategy.

## history/

One immutable file per leg: `history/<date>-<session-id>.md`, full RESULT verbatim. `osctl leg close` writes that file and the matching journal line on every named entity as one move. Direction LOG lines written before the move stay verbatim in `history/LOG-archive-<direction-id>.md`.

## knowledge/

```markdown
# <claim>
accepted: <date>   read_by: <play/lens and trigger>   status: current | stale
<3-10 lines + evidence pointers>
```

No real `read_by` consumer means no knowledge entry.

**Who writes.** Any leg may ADD an entry through the KERNEL §2 `knowledge` move. `review` and `pulse` additionally merge, retire and set `status: stale`. The converge family (`converge`, `converge-arch`, `converge-verify`) never writes here: it imports canon born-closed, so minting its own would be self-certification — it proposes to review/pulse as before.

**What qualifies — three tests, all required.**

- **Sourced.** Every load-bearing line cites the owner's exact words (quote plus its `history/` leg id) or a resolvable artifact (`path:line`, SHA, run output). A line the leg reasoned out is not knowledge: it stays a `capture`, or an issue with its answerer named. This is the same outside-source test `converge` applies to an `answered` row.
- **Durable.** The claim is expected to outlive the current bet. Operational facts owned by another authority — repo paths, branches, worktrees, slot state, tool versions — are read from that authority at use time, never frozen here (witness: FRICTION 2026-07-16, mutable venue paths copied into knowledge produced two competing dispatch systems).
- **Consumed.** `read_by` names a real play/lens and the trigger at which it is read.

**What this replaces.** A settled owner-approved fact — including one about work that is not the current bet — belongs here. Not on an `issue` card, which holds a problem or unknown, not a fact, and not ad-hoc keys invented on an issue or a `node` card. Not only inside a `history/` RESULT, which a later leg can reach only by sweeping. Entries written before this rule stay valid unchanged; no migration is required.

**Staleness is the invalidation condition.** `status: stale` means the basis moved: a stale entry is never imported born-closed, it is re-asked or retired. Any leg that finds the basis moved records that; `review`/`pulse` decide retire-versus-rewrite.

## work/

Outputs/evidence, not state. Being outside state, it is outside `osctl`: CALL briefs and `work/converge-*.md` documents stay hand-written files. Large binaries use LFS/external storage with a small pointer.

## Truncation guard

Every state file ends with `END_OF_FILE: <path>`. Missing trailer means truncated transport; do not rely on unseen tail.

END_OF_FILE: os/schema/direction-files.md
