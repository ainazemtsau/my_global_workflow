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
Every `kind: engineering` packet carries explicit `packet-stage: intent|finalized`, one normalized `phase: SETUP|RE-SYNC|PLAN|EXECUTE|BUILD`, `worktree: <absolute target path>`, and a stable `contract-authority` locator for the live Direction-OS `os/engineering/CONTRACT_VERSION`; `repo` remains logical routing only. Finalized packets additionally carry writer-owned `contract-version`, exact `contract-authority-observation` (resolved repo/commit/path/mode/blob/current ordinal) and `product-contract-version` observation. The executor independently re-resolves the stable authority before its first write and requires the live ordinal/blob, packet ordinal and product stamp to be exactly equal; missing, unreadable, behind, future or an older already-finalized packet stops for RE-SYNC. Only SETUP may observe no initialized product stamp, and only RE-SYNC may observe an initialized unequal stamp. SETUP also carries `setup-stage: interview|adapter-author|adapter-review|install`; PLAN carries `plan-stage: author|binding-validator|verdict`; EXECUTE/BUILD carry `execution-mode: fresh|resume`. Deliver and close are terminal read-only `gate-mode: deliver|close` observations of the same immutable finalized BUILD CALL, not phases and not new CALL identities: the CALL's `phase`, `execution-mode`, writer block and entry `head` stay byte-identical while current D/A/result/archive facts live only in the handback projection. Missing/unknown/stage-incompatible identity or a deliver/close mutation of CALL bytes is invalid.
Every engineering handoff has two explicit packet stages. A session returns `packet-stage: intent` with author-owned business/stable identity only. During RESULT apply, writer performs the sole allowed deterministic finalization: it re-reads current external state, adds only the enumerated writer-owned observations/receipts below, runs the phase gate, persists `packet-stage: finalized` in NOW/open_calls, and only then may emit payload. This is meaning-preserving materialization, not permission to change goal/done_when/base/acceptance/manifest. Session-supplied or guessed writer fields bounce.
A finalization receipt preimage is canonical LF bytes of the complete intent plus exact resolved live contract-authority/product-version observations, worktree, branch/base-authority/HEAD, applicable inventory/toolchain/TESTABILITY/plan/RED/progress identities and pre-check clean status; it excludes the receipt field itself and checker exit/output. Separate `writer-observation-hash` covers mode/command, exit and before/after status hashes. On collect only a persisted finalized CALL is runnable; changed external state, including a changed live contract authority, makes it stale and renders STOP for fresh writer finalization.
SETUP bootstrap has legal pre-install stages. `SETUP/interview` is branch/base-free, read-only, requires no adapter or install manifest, and returns a Direction RESULT recording exact target inventory plus selected stack/profile blobs; any product write is invalid. Only after its writer event may `SETUP/adapter-author` return one declared adapter bundle from the pinned OS corpus: exactly the source `work/validation-adapters/<stack>-v21.*` plus its output-manifest artifact, with both path/mode/blob identities explicit. Writer commits that author RESULT/bundle plus a normal mechanical finalization CALL; a fresh finalizer RESULT creates `SETUP/adapter-review` in a strict descendant commit. That fresh read-only review refutes canonical materialization and returns the accepted exact source and manifest path/mode/blob identities. Adapter author, reviewer and installer/checker are distinct. `SETUP/install` is later and cites the ancestral interview, author and review events; missing/stale event, missing bundle member or changed blob stops before product writes.
- SETUP/install intent carries exact rows of either `create:<path>|class|external-source-mode|external-source-blob` or `overlay:<path>|class|pre-mode|pre-blob|post-mode|post-blob|exact-patch-hash`, plus externally pinned corpus/specimen and accepted adapter. It is branch/base-free. Create collision fails; overlay preimage/postimage/patch is pinned; every unspecified entry remains protected. Writer finalization adds target/git, canonical protected inventory and random bootstrap challenge.
- PLAN/EXECUTE/BUILD/RE-SYNC intents carry exact branch/base and `base-authority: sha:<sha>|ref:<ref>@<observed-sha>`; base equals that SHA. PLAN/EXECUTE/BUILD also carry stable parent acceptance source/hash. Ref must resolve; offline uses the Direction-pinned SHA, never HEAD. RE-SYNC authority is contract-only and never a feature base.
- `PLAN/author` intent carries change-id, exact entry diff, installed toolchain and final conformance authority, but no future TESTABILITY pin or PLAN receipt; it never accepts owner verdict. Planner returns an ungated PLAN-CANDIDATE at exact P with the declared packet plus TESTABILITY binding contract and no source/test/oracle delta. Writer persists that event and a normal pending mechanical finalization CALL. A fresh finalizer creates finalized `PLAN/binding-validator` carrying P, candidate event and TESTABILITY pins. That distinct product-read-only session derives the obligation union independently, generates scratch-only probes and returns the first possible PLAN-GATED receipt. Its persisted GREEN event plus another fresh finalizer create `PLAN/verdict`. Only the owner's explicit `accepted` words for exact unchanged P/TESTABILITY/receipt plus a later fresh finalizer create EXEC; `revised|split` starts a new candidate and full binding validation, while `rejected` creates no EXEC. Required ancestry is `C-plan-call < W-plan-candidate < W-binding-validator-call < W-plan-receipt < W-verdict-call < W-verdict-result(accepted exact P) < W-execute-call`. A bare edit, self-validation, future pin at entry, receipt before validator, product write, missing full RESULT/history/LOG, bare-id `NOW.next`, double finalization, verdict/child mismatch or missing/non-ancestral event is invalid.
- This finalization transaction is generic. Whenever a writer commit creates an event that a child CALL must cite by `path@commit` - setup interview/adapter acceptance, final conformance, PLAN receipt/owner verdict, or accepted RED/progress/revision/light progress - that commit contains only the stable mechanical finalization CALL. The finalized child is created by a fresh RESULT/state_changes transaction in a strict descendant commit. `NOW.next` always remains a CALL/pointer; there is no special bare `finalize` command.
- Fresh EXECUTE intent carries the exact plan receipt/candidate/writer-event commit, an explicit accepted owner verdict for those unchanged bytes and stable execution identities, but no run/pre-execution receipt. Writer finalization verifies that event is ancestral to the separate verdict CALL/RESULT, that the verdict says accepted rather than revised/split/rejected and cites the identical P/TESTABILITY/receipt, then verifies candidate content, adds deterministic `run-id`, `pre-red-head`, `pre-execution-receipt-hash` and observation hash, persists them, and emits. Resume BUILD intent carries prior finalized run/pre-execution/plan receipts, RED oracle revision and exact accepted progress commit/ledger; writer finalizes only current resume observations.
- Real-id execution also carries exact result path and typed TESTABILITY/manifest evidence; coordinated light sentinel never removes base/acceptance/result/toolchain/run identity. The first RED receipt records author role/session, `parent-head == pre-red-head`, checkpoint R, exact test/oracle-registration-only delta, manifest/discovery/filter and expected failing status; R is the direct child or terminal commit of an explicitly declared test-author-only chain. Later independent revisions parent the exact accepted progress head, have the same path-only rule and preserve original frozen obligation assertions/mapping/acceptance; they may add or repair only a variant under that unchanged meaning.
- RE-SYNC intent carries exact create/overlay contract/toolchain/seeded-fixture/doc manifest plus external corpus/specimen and writer-accepted adapter event/path/mode/blob. Entry is initialized-behind, clean exact branch and HEAD==base. Install mode receives only the writer challenge, never a not-yet-created final receipt. Writer runs bootstrap install cases, derives an opaque bootstrap receipt, runs every non-install phase with that receipt including missing/wrong/cross-phase seeds, then derives and persists the final conformance receipt and performs a receipt-binding smoke excluded from its preimage. All later PLAN/EXECUTE/BUILD CALLs carry that final receipt byte-identically. SETUP/RE-SYNC return also verifies installed HEAD/toolchain, every create/overlay pre/post/patch, and all protected bytes; path equality alone is insufficient.
Product reports never contain their own blob/commit. Deliver/close evidence is handback data under the immutable BUILD CALL, is saved through Direction RESULT history, and never becomes a session-invented phase receipt. Missing routing stdout remains reconstructible by the declared D/A rule.
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
