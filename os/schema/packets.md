# Schema: packets

Two packet types exist (KERNEL §4). Both are plain markdown blocks designed to be carried by any relay: pasted by the owner today, routed by an orchestrator later. A packet must be self-contained: the receiver should never have to ask "what did you mean".

## CALL

```markdown
CALL <call-id>
to: session | research | executor        # who runs it
direction: <direction-id>
track: <track-id>                        # required when NOW.md uses track-mode
play: <frame|map|shape|converge|converge-arch|converge-verify|day|work|guide|review|research|pulse|repair|local/<name>>   # for sessions
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
parent: <parent-call-id>                 # same-lane child; legacy may name parent session
surface: <optional routing hint: chatgpt | claude | cli | any>
engineering_contract: <N | legacy:<origin-call-id> | re-sync:<N>>  # engineering only; see below
```

**CALL hygiene.** `goal`/`context`/`boundaries` never restate or paraphrase the play's procedure — the play file is the only procedure source. A CALL that summarizes steps ("one card at a time", "ask first") invites the session to follow the paraphrase instead of the play; the writer bounces such CALLs at collect/apply time.

**Grounds are not authority.** A CALL's instructions bind; the GROUNDS it states for them do not — a derivation, a `path:line` citation, a count, "the next free id". The receiver re-derives every ground its work would freeze into an artifact, corrects a wrong one there and reports the correction; a right instruction with a wrong ground is carried out, never justified by that ground. Copying a ground onward because the CALL asserted it is how a false fact reaches a frozen document (witnessed 2026-07-30 on `c-exec-g-37a1-gas-rest-amend-001`: a floor's stated theorem bound, a `validation.config` line range, a free ADR number and a literal count were all wrong while every instruction was right).

A specification-authoring CALL is the only no-bet `work` exception: `to: session`, no track/task, `node`/`for` resolves to a parked node card marked `outcome_kind: specification`, and done_when names the exact versioned owner-approved artifact. Checkpoints continue same-node work; completion keeps the node parked and opens fresh `converge-verify`; PASS opens narrow review, never shape. Executor CALLs may support mechanics/research but cannot select or approve the specification's owner-content.

Executor CALLs (`to: executor`) add `repo: <org/repo>` and `kind: engineering | mechanical`:
- `engineering` — a business task in a product repo. The agent owns design and implementation; evidence = commits/PR + check output (tests, build). Conventions and the run contract live in that repo's AGENTS.md/CLAUDE.md, not in the OS. `goal`/`done_when` stay business-level — hygiene extends to architecture; `context` may point to the direction's `work/` design-exploration docs as input evidence for the planner, never as a binding spec. A direction's first engineering CALL while no initialized product repo exists is repo setup — interactive (stack interview), its `context` points to `os/engineering/PROJECT_SETUP.md` and `os/engineering/profiles/`.
- `mechanical` — apply one complete RESULT's declared state-change intent to fresh `live/**` (the writer role), including semantic rebase of stale bases. A bare `state_changes` section is incomplete. Interpretation is bounded to preserving compatible concurrent state; never invent outcomes or evidence. Apply, commit, report the commit hash.

**Engineering contract pin (v29+).** Every newly issued root `kind: engineering` CALL carries the current integer
`engineering_contract`; every Direction successor of that root inherits it. An issued pin keeps its feature route/gates
through Re-sync; v34 process-close is the sole control-plane exception. A CALL already registered as an open call when v29 lands may return unmarked; its first
later successor uses `legacy:<origin-call-id>` and later successors preserve that marker. `legacy:` is invalid on a new
root. A bounded `re-sync:<N>` CALL may only install contract N and stamp the repo; it runs under the repo's pre-upgrade
contract and cannot carry product-feature work. The writer validates a return against its pinned/originating contract,
never against requirements added after issuance. The legacy snapshot is exactly the unmarked engineering CALLs already
registered as open calls when v29 activates; no later unmarked root is legal. A legacy return may only close/checkpoint its leg or
issue a same-leg legacy successor; it never atomically opens Re-sync or an unrelated integer-pinned root. A later
Direction transaction may issue `re-sync:<N>` while older roots remain open: Re-sync changes repo authority only and
neither consumes/retargets them nor rewrites active artifacts. After Re-sync HOME, new roots may coexist with them; each
The CALL pin selects its feature route.

**Frozen-authority replacement (v34+).** A PLAN/carrier/RED replan is not a backward same-leg successor. After Re-sync,
this control-plane close may release any non-released v30+ root while its feature work remains judged under the original
pin; no v34 feature gate is retroactive. It commits salvage and the product receipt releases the old root as `replaced`,
naming its planned `replaced_by`; it runs no downstream delivery gates and returns `REPLACED` HOME. A later Direction `repair` atomically swaps the
old root's open call card for a new current-pinned root. The new CALL names `replaces`, `resume_from` (earliest affected
stage), clean committed `basis`, and exact `carry`/`stale` dispositions. It preserves business goal/done_when unless
cited owner words change them. Old commits/manifests/ref remain evidence; superseded files are absent from replacement
checkout/gates. Replacement is not delivery, never marks the task done, cannot bundle Re-sync, and transfers no
uncommitted draft. No semantic parser judges carry: the fresh stage/reviewer checks exact inputs and meaning normally.

Routing follows that pin. Each v29/legacy executor stage closes with its current HOME handback; Direction consumes it
and issues continuation. V30-v34 roots stay registered from PLAN through REPORT/ESCALATE/REPLACED while the repo runner
launches each declared stage as a separate fresh session. Its compact committed receipt records lifecycle, stage, exact
inputs/outputs, verdict, evidence, retry, eligibility, closing lease and replacement dispositions. Receipts are not CALL/RESULT
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
  <exact edits: task/track card statuses, node card changes, files added to work/,
   knowledge/ entries added by the KERNEL §2 `knowledge` move (schema: direction-files.md).
   Includes CALLs issued by this session with track/status, as call cards to register,
   and clears the returning call.
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
log: <one line — this leg's journal entry, recorded by `osctl leg close`>
next: |
  <one new local continuation CALL registered by state_changes | awaiting_decision | return-to-parent <id> | return-to-owner>
```

**Lane routing.** When the direction has tracks, each CALL, RESULT and pending decision names one. Tracks are execution lanes under the one active bet, never future goals or parallel strategies; their `for` resolves to that bet/node/task or a recurring obligation. Each lane has at most one parentless root CALL. A child names an existing same-lane parent, appears in its `waiting_on`, inherits budget, and has acyclic ancestry. Its RESULT clears only itself, adds the history receipt to the direct parent, and makes that parent ready only after the last wait clears. A RESULT may issue one same-position successor plus children. Other call ids survive semantic rebase. `RESULT.next` hands off only a local continuation/decision/parent return/owner return; it is not copied into NOW and cannot select foreign work.

An owner/runtime-confirmed launch may change an existing open call card's status `ready → running` without changing the CALL; `running` is durable duplicate-launch prevention, not a new packet or progress claim. It requires a `started` evidence pointer, is never dispatchable, and returns normally. Resetting `running → ready` requires an explicit lost/cancelled-run receipt; elapsed time alone never resets or relaunches it.

**State-change rebase semantics.** The authoritative per-operation merge and
replay rules are `os/adapters/coding-agent.md` Role 1. Optional blob/SHA/commit
ids, expected old text and exact anchors are bases that let the writer derive a three-way delta;
they are not freshness locks. The writer re-reads current state, applies only
the packet's declared intent by stable path/id/key, and preserves concurrent
changes outside that intent. `Preserve unchanged` refers to the current value
after rebase. A stale base alone never invalidates a RESULT; an ambiguous delta,
invalid/incomplete packet or local `next` handoff, or mutually exclusive meanings for
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
  t-2 → done; clear c-117; register c-118 ready.
  work/: + trailer-script.md
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
