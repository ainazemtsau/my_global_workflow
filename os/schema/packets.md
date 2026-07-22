# Schema: packets

Two packet types exist (KERNEL §4). Both are plain markdown blocks designed to be carried by any relay: pasted by the owner today, routed by an orchestrator later. A packet must be self-contained: the receiver should never have to ask "what did you mean".

## CALL

```markdown
CALL <call-id>
to: session | research | executor        # who runs it
direction: <direction-id>
track: <track-id>                        # required when NOW.md uses track-mode
play: <frame|map|shape|converge|converge-arch|converge-verify|work|guide|review|research|pulse|repair|local/<name>>   # for sessions
node: <g-xxxx>  task: <t-N> | recurring: <r-N>          # when applicable
goal: |
  <the outcome to produce — not the method>
context: |
  <pointers: live/<dir>/NOW.md, specific files, links, prior findings.
   Enough to start working without questions.>
boundaries: |
  <out of scope; what must not be touched or decided here>
done_when: |
  <verifiable condition>
return: |
  <expected format of the RESULT's outcome/evidence>
budget: <e.g. one session | 2h | 15 tool calls>
parent: <parent-call-id>                 # track child; legacy may name parent session
request_kind: outcome                   # auxiliary cross-track disposition request only
requested_by: <track-id>                # owner-approved outcome-dispatch track
surface: <optional routing hint: chatgpt | claude | cli | any>
engineering_contract: <N | legacy:<origin-call-id> | re-sync:<N>>  # engineering only; see below
```

**CALL hygiene.** `goal`/`context`/`boundaries` never restate or paraphrase the play's procedure — the play file is the only procedure source. A CALL that summarizes steps ("one card at a time", "ask first") invites the session to follow the paraphrase instead of the play; the writer bounces such CALLs at collect/apply time.

Executor CALLs (`to: executor`) add `repo: <org/repo>` and `kind: engineering | mechanical`:
- `engineering` — a business task in a product repo. The agent owns design and implementation; evidence = commits/PR + check output (tests, build). Conventions and the run contract live in that repo's AGENTS.md/CLAUDE.md, not in the OS. `goal`/`done_when` stay business-level — hygiene extends to architecture; `context` may point to the direction's `work/` design-exploration docs as input evidence for the planner, never as a binding spec. A direction's first engineering CALL while no initialized product repo exists is repo setup — interactive (stack interview), its `context` points to `os/engineering/PROJECT_SETUP.md` and `os/engineering/profiles/`.
- `mechanical` — apply one complete RESULT's declared state-change intent to fresh `live/**` (the writer role), including semantic rebase of stale bases. A bare `state_changes` section is incomplete. Interpretation is bounded to preserving compatible concurrent state; never invent outcomes or evidence. Apply, commit, report the commit hash.

**Engineering contract pin (v29+).** Every newly issued root `kind: engineering` CALL carries the current integer
`engineering_contract`; every Direction successor of that root inherits it. An issued integer-pinned root keeps its
route through later Re-sync. A CALL already registered in `open_calls` when v29 lands may return unmarked; its first
later successor uses `legacy:<origin-call-id>` and later successors preserve that marker. `legacy:` is invalid on a new
root. A bounded `re-sync:<N>` CALL may only install contract N and stamp the repo; it runs under the repo's pre-upgrade
contract and cannot carry product-feature work. The writer validates a return against its pinned/originating contract,
never against requirements added after issuance. The legacy snapshot is exactly the unmarked engineering CALLs already
in `open_calls` when v29 activates; no later unmarked root is legal. A legacy return may only close/checkpoint its leg or
issue a same-leg legacy successor; it never atomically opens Re-sync or an unrelated integer-pinned root. A later
Direction transaction may issue `re-sync:<N>` while older roots remain open: Re-sync changes repo authority only and
neither consumes/retargets them nor rewrites active artifacts. After Re-sync HOME, new roots may coexist with them; each
CALL's pin, never the latest stamp, selects its route.

Routing follows that pin. Each v29/legacy executor stage closes with its current HOME handback; Direction consumes it
and issues continuation. V30/v31 roots stay registered from PLAN through REPORT while the repo runner launches each
declared stage as a separate fresh session. Its compact committed receipt records lifecycle, stage, exact product/process
inputs and outputs, verdict, evidence, retry class/count, eligibility and closing lease. Receipts are not CALL/RESULT
packets and never touch `live/**`. V31 shares `ACTIVE | PRESERVED-PAUSED | RELEASED` across discovery, apply, mutation
and Deliver: paused is custody-only until re-admitted; released is terminal; Boolean fields accept JSON booleans only.
It retries only the earliest stage invalidated
by an exact input change and serializes closing as evidence → RESULT/mirrors → gates → RELEASED commit → publish/readback.
HOME returns only at gated REPORT or genuine ESCALATE; only Direction issues a later Direction CALL.

## RESULT

```markdown
RESULT <session-id> (call: <call-id>)
direction: <direction-id>   track: <track-id>   play: <play>   node/task: <...>
outcome: |
  <what is now true that wasn't — in the world, not "I analyzed">
evidence: |
  <proof matching done_when: artifact paths, commit/PR links, check output,
   source links. A claim without evidence is not an outcome.>
state_changes: |
  <exact edits: NOW.md task/track statuses, TREE.md node changes, files added to work/.
   Includes CALLs issued by this session with track/status, for NOW.md → open_calls,
   clears the returning call, and explicitly selects a new default when required.
   Written with stable targets and explicit postconditions so a mechanical
   executor needs only the bounded merge judgment defined below.>
captures:
  - <one line each: emergent work/ideas for later triage>
decisions_needed:
  - q: <question>  options: [a, b]  recommendation: <a, because ...>
play_check:
  - <step# name>: done | skipped <why>
  # one line per play step; steps the play marks (owner) cite the owner's
  # actual words (his answer, verdict, or explicit waiver) — gate G10
log: <one line for LOG.md>
next: |
  <one continuation CALL whose status is in state_changes | awaiting_decision | return-to-parent <id> | return-to-requester <track-id>>
```

**Track routing.** Legacy single-track directions may omit `track`. Once `NOW.md` has `tracks`, every newly issued CALL, RESULT, and pending decision names one; a pre-migration CALL may inherit its unique track from the authoritative `open_calls` entry with the same id. Each track has at most one ordinary parentless root CALL. A child names an existing same-track parent, appears in that parent's `waiting_on`, inherits its budget, and has acyclic ancestry to the root. Its RESULT clears only the child id, adds the history receipt to the direct parent, and makes that parent ready only after its last wait id clears. A RESULT may issue one same-position successor plus children: a root successor stays root; a child successor keeps its parent. Other call ids survive semantic rebase. `RESULT.next` is one recommended continuation, not the queue. If the returning call was `NOW.next`, state_changes selects its valid successor/default (or `awaiting_decision`); otherwise the default stays put unless explicitly changed.

**Bounded cross-track outcome request.** At most one owner-approved track per direction may carry `outcome_dispatch: true`. Its ordinary root may issue or expire an auxiliary CALL with `request_kind: outcome`, `requested_by: <that-track>`, a different target `track`, `to: session`, `play: work`, and no `parent`; its registered `for` matches that target's ordinary root. Both requester and target ordinary roots remain non-paused while it is open, so both tracks already occupy WIP. The request is not a root/child, adds no WIP slot, never mutates or replaces the target root, and at most one may be open per target track. Its CALL asks only whether one observable need fits the target's current lawful route: `context` names the source, need, useful date/event and miss consequence; `done_when` names outcome and proof; no technical HOW. Its `return` defines the three disposition meanings and required evidence so the carried CALL stays self-contained. The target RESULT's `outcome` starts with exactly `ACCEPT` (need/proof/date fit), `COUNTER` (equivalent outcome plus trade-off) or `BLOCKED` (blocker plus unblock proof), issues no successor and changes no plan/product. This is a target-track operational disposition, not owner approval; any separate owner-verdict request still needs the owner's words. Its RESULT clears the request, appends that history receipt to the current ordinary roots of both tracks, and uses `next: return-to-requester <track-id>`. The authorized requester may instead expire its still-open request by id with an explicit reason; the expiry receipt is appended to the target root and is not a target disposition. Pausing or retiring either track first returns or expires its requests.

**State-change rebase semantics.** The authoritative per-operation merge and
replay rules are `os/adapters/coding-agent.md` Role 1. Optional blob/SHA/commit
ids, expected old text and exact anchors are bases that let the writer derive a three-way delta;
they are not freshness locks. The writer re-reads current state, applies only
the packet's declared intent by stable path/id/key, and preserves concurrent
changes outside that intent. `Preserve unchanged` refers to the current value
after rebase. A stale base alone never invalidates a RESULT; an ambiguous delta,
invalid/incomplete packet or `next` CALL, or mutually exclusive meanings for
the same semantic field after those merge rules still does.

## Worked example (compressed)

```markdown
CALL c-117
to: session   direction: indie-game   play: work   node: g-12ab   task: t-2
goal: |
  Сценарий 40-секундного трейлера по вертикальному слайсу.
context: |
  live/indie-game/NOW.md; work/concept.md; knowledge/genre-marketing.md
  (вывод: в жанре конвертят геймплейные хуки в первые 5 сек).
boundaries: |
  Не трогаем стиль арта; не планируем съёмку — только сценарий.
done_when: |
  Сценарий поscene-но в work/trailer-script.md; хук в первых 5 сек;
  владелец принял.
return: файл + 3 строки обоснования структуры
budget: one session
```

```markdown
RESULT s-042 (call: c-117)
direction: indie-game   play: work   node/task: g-12ab/t-2
outcome: |
  Сценарий трейлера готов: 7 сцен, геймплейный хук (газовая цепная
  реакция) в первых 4 секундах.
evidence: |
  work/trailer-script.md; структура согласована с владельцем в сессии.
state_changes: |
  NOW.md: t-2 → done. work/: + trailer-script.md
captures:
  - идея: gif-нарезка сцены 3 для devlog — кандидат в задачи audience-линзы
decisions_needed: []
play_check:
  - 1 recite: done
  - 2 do the work: done
  - 3 self-check: done (сверка по done_when попунктно)
  - 4 close: done (владелец принял: "хук отличный, берём")
log: work t-2: сценарий трейлера готов и принят
next: |
  CALL c-118: to: session, play: work, task: t-3 (запись черновика
  трейлера по сценарию), context: work/trailer-script.md, ...
```

END_OF_FILE: os/schema/packets.md
