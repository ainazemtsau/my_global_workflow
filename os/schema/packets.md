# Schema: packets

Two packet types exist (KERNEL §4). Both are plain markdown blocks designed to be carried by any relay: pasted by the owner today, routed by an orchestrator later. A packet must be self-contained: the receiver should never have to ask "what did you mean".

## CALL

```markdown
CALL <call-id>
to: session | research | executor        # who runs it
direction: <direction-id>
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
parent: <session-id>                     # for children: where the result returns
surface: <optional routing hint: chatgpt | claude | cli | any>
```

**CALL hygiene.** `goal`/`context`/`boundaries` never restate or paraphrase the play's procedure — the play file is the only procedure source. A CALL that summarizes steps ("one card at a time", "ask first") invites the session to follow the paraphrase instead of the play; the writer bounces such CALLs at collect/apply time.

Executor CALLs (`to: executor`) add `repo: <logical org/repo identity; never a filesystem path>` and `kind: engineering | mechanical`:
Every `kind: engineering` CALL also carries exactly one normalized `phase: SETUP | PLAN | EXECUTE | BUILD | RE-SYNC` plus `worktree: <absolute target path>`. The worktree is the only filesystem identity used for contract reads, checks and execution; `repo` is labeling/routing only. Missing or unknown phase/worktree is invalid. `SETUP` is legal only while the target lacks a complete installed root run-contract plus readable validation stamp: it performs PROJECT_SETUP's interactive stack interview, initializes or finishes git/contract/toolchain while preserving existing files, and may not implement a product feature. SETUP is the sole phase with no branch/base requirement; an initialized target rejects it. Every PLAN/EXECUTE/BUILD/RE-SYNC additionally carries exact `branch: <name>` and authoritative `base: <sha>`. PLAN is the owner-interactive plan leg and stops at approval; EXECUTE/BUILD is the separate fresh feature implementation leg; RE-SYNC only installs a newer engineering contract into an initialized behind product and may not implement the product feature. PLAN/EXECUTE/BUILD/RE-SYNC against an uninitialized target is invalid. PLAN/EXECUTE/BUILD also require the assigned worktree's current contract stamp and zero phase-entry check; a behind initialized target must use RE-SYNC first. Every PLAN/EXECUTE/BUILD carries `change-id: <id> | n/a-light` plus `validation-toolchain-manifest-hash: <sha256>`; omission or prose self-labeling never grants N/A. The toolchain hash is over ordinal `<repo-relative-path>\t<base-git-blob-id>` rows plus final LF for the regular-file trust roots explicitly enumerated by base `validation.config` (config itself, the handoff command, and every directly loaded helper/schema); dynamic/unlisted loads, symlink/reparse roots, outside-worktree resolution, path substitution or additions are invalid. Every PLAN also carries `preexisting-plan-diff: none | <ordinal repo-relative path list>` exactly equal to `git diff --name-only <base>..HEAD`; every listed path must be under `docs/**` or the same-id `openspec/changes/<id>/**`, never production/tests/toolchain. `n/a-light` PLAN requires both `preexisting-plan-diff: none` and an independently empty non-archived G0 trigger scan. Every EXECUTE/BUILD also carries the remaining six explicit handoff fields: `testability: openspec/changes/<same-id>/TESTABILITY.md | n/a-light`, `testability-blob: <git-blob-id> | n/a-light`, `baseline-commit: <same sha as base>`, `input-manifest-hash: <sha256> | n/a-light`, `complete-sweep: yes | n/a-light`, and `verdict: GREEN | n/a-light`. The real-id forms travel together and require that same non-archived G0-frozen change; `testability-blob` is the external attestation of the complete committed TESTABILITY bytes because that file is intentionally excluded from its recursive input manifest. The `n/a-light` execution forms, including `testability-blob: n/a-light`, travel together and are valid only when the assigned worktree contains zero non-archived `openspec/changes/<id>/` folders with a frozen spec. Missing values, mixed real/sentinel forms, aliases such as `BUILD-only`, a path/id/base mismatch, or a mismatched/unsafe preexisting plan diff are invalid.
- `engineering` — a business task in a product repo. The agent owns design and implementation; evidence = commits/PR + check output (tests, build). Conventions and the run contract live in that repo's AGENTS.md/CLAUDE.md, not in the OS. `goal`/`done_when` stay business-level — hygiene extends to architecture; `context` may point to the direction's `work/` design-exploration docs as input evidence for the planner, never as a binding spec. A direction's first engineering CALL while no initialized product repo exists is repo setup — interactive (stack interview), its `context` points to `os/engineering/PROJECT_SETUP.md` and `os/engineering/profiles/`.
- `mechanical` — apply one complete RESULT's declared state-change intent to fresh `live/**` (the writer role), including semantic rebase of stale bases. A bare `state_changes` section is incomplete. Interpretation is bounded to preserving compatible concurrent state; never invent outcomes or evidence. Apply, commit, report the commit hash.

## RESULT

```markdown
RESULT <session-id> (call: <call-id>)
direction: <direction-id>   play: <play>   node/task: <...>
outcome: |
  <what is now true that wasn't — in the world, not "I analyzed">
evidence: |
  <proof matching done_when: artifact paths, commit/PR links, check output,
   source links. A claim without evidence is not an outcome.>
state_changes: |
  <exact edits: NOW.md task statuses, TREE.md node changes, files added to work/.
   Includes CALLs issued by this session, for NOW.md → open_calls.
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
  <ready CALL for the continuation | awaiting_decision | return-to-parent <id>>
```

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
