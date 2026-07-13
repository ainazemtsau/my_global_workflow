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
Every `kind: engineering` packet carries explicit `packet-stage: intent|finalized`, one normalized `phase: SETUP|PLAN|EXECUTE|BUILD|RE-SYNC`, and `worktree: <absolute target path>`; `repo` remains logical routing only. PLAN also carries `plan-stage: author|verdict`. Missing/unknown/stage-incompatible identity is invalid.
Every engineering handoff has two explicit packet stages. A session returns `packet-stage: intent` with author-owned business/stable identity only. During RESULT apply, writer performs the sole allowed deterministic finalization: it re-reads current external state, adds only the enumerated writer-owned observations/receipts below, runs the phase gate, persists `packet-stage: finalized` in NOW/open_calls, and only then may emit payload. This is meaning-preserving materialization, not permission to change goal/done_when/base/acceptance/manifest. Session-supplied or guessed writer fields bounce.
A finalization receipt preimage is canonical LF bytes of the complete intent plus exact resolved worktree, observed branch/base-authority/HEAD, applicable inventory/toolchain/TESTABILITY/plan/RED/progress identities and pre-check clean status; it excludes the receipt field itself and checker exit/output. Separate `writer-observation-hash` covers mode/command, exit and before/after status hashes. On collect only a persisted finalized CALL is runnable; changed external state makes it stale and renders STOP for fresh writer finalization.
Adapter bootstrap is a separate Direction transaction before product install, not a guessed SETUP field: after stack interview, an adapter-author RESULT creates one declared `work/validation-adapters/<stack>-v21.*` artifact from the pinned OS corpus; a fresh read-only adapter-review RESULT tries to refute canonical materialization; writer applies/commits both and records the accepted path/mode/blob in history. Only a later SETUP/RE-SYNC intent may cite that ancestral event. Adapter author, reviewer and product installer/checker session cannot be the same; missing review/event or changed blob stops before product writes.
- SETUP intent is branch/base-free and carries exact `setup-install-manifest` rows of either `create:<path>|class|external-source-mode|external-source-blob` or `overlay:<path>|class|pre-mode|pre-blob|post-mode|post-blob|exact-patch-hash`, plus externally pinned `os-conformance-corpus-blob`, `valid-specimen-hash` and a writer-accepted adapter event/path/mode/blob. Create collision fails. Overlay preimage/postimage or exact patch is writer-pinned; unspecified bytes remain protected. If interview changes it, return an amended intent and stop before writes. Writer finalization adds target state/git, canonical protected inventory count/hash and a random `conformance-bootstrap-challenge`; protected means every pre-existing entry not named by a valid overlay.
- PLAN/EXECUTE/BUILD/RE-SYNC intents carry exact branch/base and `base-authority: sha:<sha>|ref:<ref>@<observed-sha>`; base equals that SHA. PLAN/EXECUTE/BUILD also carry stable parent acceptance source/hash. Ref must resolve; offline uses the Direction-pinned SHA, never HEAD. RE-SYNC authority is contract-only and never a feature base.
- `PLAN/author` intent carries change-id, exact entry diff, installed toolchain identity, and `validation-conformance-receipt` plus its writer-owned `history/<path>@<commit>` event; writer resolves that event independently for the checker authority environment. It never asks for or accepts an owner verdict. Pinned plan produces a terminal PLAN-GATED checkpoint with `plan-candidate-head`, `plan-observation-hash` over exact mode/command/zero exit and clean before/after status, and `plan-receipt-hash` over that observation plus candidate HEAD/base/acceptance/toolchain/conformance/typed TESTABILITY mode/blob/manifest. During checkpoint apply, writer independently reruns/recomputes both, saves them in Direction `history/`, commits that event, and only then persists/emits a separate finalized `PLAN/verdict` CALL carrying `plan-receipt-event: history/<path>@<writer-commit>` plus the same candidate/receipt. The verdict session presents that exact candidate and returns the owner's actual words; its RESULT is necessarily later because its CALL did not exist before the writer commit. A conformance/plan receipt first appearing in a product/verdict RESULT, verdict in `PLAN/author`, event commit not ancestral to the verdict RESULT, packet edit, nonzero/tampered observation, or candidate/receipt mismatch is invalid. Only after this check may writer finalize EXEC.
- Fresh EXECUTE intent carries the exact plan receipt/candidate/writer-event commit and stable execution identities, but no run/pre-execution receipt. Writer finalization verifies that event is ancestral to the separate verdict CALL/RESULT and that the verdict cites it, then verifies candidate content, adds deterministic `run-id`, `pre-red-head`, `pre-execution-receipt-hash` and observation hash, persists them, and emits. Resume BUILD intent carries prior finalized run/pre-execution/plan receipts, RED oracle revision and exact accepted progress commit/ledger; writer finalizes only current resume observations.
- Real-id execution also carries exact result path and typed TESTABILITY/manifest evidence; coordinated light sentinel never removes base/acceptance/result/toolchain/run identity. The first RED receipt records author role/session, `parent-head == pre-red-head`, checkpoint R, exact test/oracle-registration-only delta, manifest/discovery/filter and expected failing status; R is the direct child or terminal commit of an explicitly declared test-author-only chain. Later independent revisions parent the exact accepted progress head and have the same path-only rule.
- RE-SYNC intent carries exact create/overlay contract/toolchain/seeded-fixture/doc manifest plus external corpus/specimen and writer-accepted adapter event/path/mode/blob. Entry is initialized-behind, clean exact branch and HEAD==base. Install mode receives only the writer challenge, never a not-yet-created final receipt. Writer runs bootstrap install cases, derives an opaque bootstrap receipt, runs every non-install phase with that receipt including missing/wrong/cross-phase seeds, then derives and persists the final conformance receipt and performs a receipt-binding smoke excluded from its preimage. All later PLAN/EXECUTE/BUILD CALLs carry that final receipt byte-identically. SETUP/RE-SYNC return also verifies installed HEAD/toolchain, every create/overlay pre/post/patch, and all protected bytes; path equality alone is insufficient.
Product reports never contain their own blob/commit. Handback receipts are saved through Direction RESULT history; missing routing stdout remains reconstructible by the declared D/A rule.
Every non-install engineering CALL carries both `validation-conformance-receipt` and ancestral writer-owned `validation-conformance-event: history/<path>@<commit>` byte-identically through close; writer resolves the event independently and supplies its value as checker authority. A receipt without that event, changed across phases, or first introduced by a product RESULT is invalid.
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
