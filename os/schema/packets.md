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
surface: <optional routing hint: chatgpt | claude | cli | any>
```

**CALL hygiene.** `goal`/`context`/`boundaries` never restate or paraphrase the play's procedure — the play file is the only procedure source. A CALL that summarizes steps ("one card at a time", "ask first") invites the session to follow the paraphrase instead of the play; the writer bounces such CALLs at collect/apply time.

Executor CALLs (`to: executor`) add `repo: <org/repo>` and `kind: engineering | mechanical`:
- `engineering` — a business task in a product repo. The agent owns design and implementation; evidence = commits/PR + check output (tests, build). Conventions and the run contract live in that repo's AGENTS.md/CLAUDE.md, not in the OS. `goal`/`done_when` stay business-level — hygiene extends to architecture; `context` may point to the direction's `work/` design-exploration docs as input evidence for the planner, never as a binding spec. A direction's first engineering CALL while no initialized product repo exists is repo setup — interactive (stack interview), its `context` points to `os/engineering/PROJECT_SETUP.md` and `os/engineering/profiles/`.
- `mechanical` — apply one complete RESULT's declared state-change intent to fresh `live/**` (the writer role), including semantic rebase of stale bases. A bare `state_changes` section is incomplete. Interpretation is bounded to preserving compatible concurrent state; never invent outcomes or evidence. Apply, commit, report the commit hash.

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
  <one continuation CALL whose status is in state_changes | awaiting_decision | return-to-parent <id>>
```

**Track routing.** Legacy single-track directions may omit `track`. Once `NOW.md` has `tracks`, every newly issued CALL, RESULT, and pending decision names one; a pre-migration CALL may inherit its unique track from the authoritative `open_calls` entry with the same id. Each track has at most one parentless root CALL. A child names an existing same-track parent, appears in that parent's `waiting_on`, inherits its budget, and has acyclic ancestry to the root. Its RESULT clears only the child id, adds the history receipt to the direct parent, and makes that parent ready only after its last wait id clears. A RESULT may issue one same-position successor plus children: a root successor stays root; a child successor keeps its parent. Other call ids survive semantic rebase. `RESULT.next` is one recommended continuation, not the queue. If the returning call was `NOW.next`, state_changes selects its valid successor/default (or `awaiting_decision`); otherwise the default stays put unless explicitly changed.

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
