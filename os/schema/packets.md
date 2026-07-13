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
Every `kind: engineering` packet carries explicit `packet-stage: intent|finalized`, one normalized `phase: SETUP|RE-SYNC|PLAN|EXECUTE|BUILD`, `worktree: <absolute target path>`, and literal `contract-authority: direction-os://live/os/engineering/CONTRACT_VERSION`; session-supplied authority fields are invalid and `repo` is logical routing only. Writer finalization adds the absent-from-intent row `contract-authority-resolver: {schema:1,kind:git-moving-ref,repo-id:https://github.com/ainazemtsau/my_global_workflow,remote-url:https://github.com/ainazemtsau/my_global_workflow,authority-ref:refs/heads/main,authority-path:os/engineering/CONTRACT_VERSION}`. It freshly queries that exact remote/ref, fetches the observed SHA, and reads the authority path from that object. Current/wt/local-main/tracking refs are never authority; a common-dir object is readable only after equality with the fresh remote SHA, and there is no remote-less fallback. Writer/finalizer/collect and executor repeat this rule independently; CALL/env/product cannot override it. SETUP/RE-SYNC author/review pin an equivalent product-native resolver, install installs it, and post-install proves equality. A finalized packet carries remote/ref@observed-SHA plus query/fetch evidence, exact authority observation, and product state `absent|uninitialized|initialized|initialized-corrupt`. Uninitialized is virgin only when both run-contract and stamp are absent and reachable product+Direction history proves no prior install/trust marker. Initialized-corrupt carries trusted recovered ordinal or `none` plus exact reason. SETUP carries `setup-stage`; RE-SYNC carries `resync-stage: adapter-author|adapter-review|install` and `resync-entry-reason: lower|current-invalid`; PLAN carries `plan-stage`; EXECUTE/BUILD carry execution mode. Deliver/close remain immutable BUILD handback modes.
Every engineering handoff has two explicit packet stages. A session returns `packet-stage: intent` with author-owned business/stable identity only. During RESULT apply, writer performs the sole allowed deterministic finalization: it re-reads current external state, adds only the enumerated writer-owned observations/receipts below, runs the phase gate, persists `packet-stage: finalized` in NOW/open_calls, and only then may emit payload. This is meaning-preserving materialization, not permission to change goal/done_when/base/acceptance/manifest. Session-supplied or guessed writer fields bounce.
A finalization receipt preimage is canonical LF bytes of the complete intent plus exact writer-owned resolver row, resolved locator/repo-id/ref/path/mode/blob/current authority identity, product entry observation, worktree, branch/base-authority/HEAD, applicable inventory/toolchain/TESTABILITY/plan/RED/progress identities and pre-check clean status; it excludes the receipt field, checker result and volatile observed ref SHA/query-fetch evidence. Separate `writer-observation-hash` records remote/ref@observed-SHA, mode/command, query/fetch evidence, exit and before/after status hashes. Those finalized CALL, receipt and entry observation bytes are immutable across install execution/retry. Unresolvable remote query/fetch/object is `STOP - CONTRACT AUTHORITY UNAVAILABLE`; packet/env/product override is invalid. On collect only a persisted finalized CALL is runnable; changed resolver semantics or authority path/mode/blob/current makes it stale, while unrelated authority-tip advance with unchanged path/mode/blob/current does not. Audit/digest without a finalized CALL derive the same canonical resolver ephemerally for that read only and never persist packet authority.

The phase/recovery matrix is exact after install-recovery precedence. An open immutable install plus its exact inner marker resumes first; absent SETUP also resumes its exact declared empty sibling temp-root as the atomic first marker state solely to create the zero-byte inner marker. No other unmarked/nonempty temp-root is resumable. If live advanced, recovery may finish only the pinned manifest/Git transaction, then returns `MANIFEST-RECONCILED` under that same CALL: it consumes the old open call only after terminal proof, preserves old receipt plus reconcile observation, emits no current/feature receipt, freshly resolves live, and opens lower/current-invalid or reports future/unavailable. Without recovery ancestry, unavailable authority is `STOP - CONTRACT AUTHORITY UNAVAILABLE`. Exact absent target with accessible pinned parent admits SETUP. Existing virgin admits SETUP only when it is a clean initialized non-bare Git worktree with pinned branch/HEAD/index/inventory, both contract/stamp absent, and reachable product+Direction history proving no prior marker; non-git, unborn, dirty or unprovable state is `STOP - TARGET COLLISION/CORRUPT`. Every existing target, including a syntactically complete pair, enumerates all reachable matching marker+receipt install events in product HEAD and Direction ancestry, requires one linear nondecreasing ordinal chain, and selects its unique descendant-most/highest event. When any trusted event exists, on-disk ordinal must equal that recovered ordinal; mismatch is initialized-corrupt and routes by recovered lower/equal/higher, never by the rolled-back disk value. Incomparable/conflicting/decreasing events stop corrupt. Incomplete/malformed pair, or both absent with prior history, is likewise corrupt. Recovered lower routes RE-SYNC `lower`, equal routes `current-invalid`, higher is future STOP; no trustworthy ordinal is `STOP - CONTRACT STATE CORRUPT`. A complete lower with no trusted history routes `lower`; stamp equal is current-valid only with matching accepted event/receipt and installed identities, otherwise `current-invalid`; only current-valid admits feature phases. Higher never downgrades and stale packets never refresh.

Install interruption is the sole entry-observation exception. Writer persists `install-nonce` as exactly 128 random bits encoded 32 lowercase hex, `intent-sha256` over canonical-LF intent bytes, and `ordinary-manifest-sha256` over RFC8785 JSON after rows are sorted by platform-normalized path then operation. A platform-normalized path is unique across the entire manifest regardless of operation; create+delete, overlay+delete, any other cross-operation reuse, and case-equivalent duplicates are invalid. Marker/temp/finalized-CALL/receipt fields are excluded. `attempt-id` is lowercase SHA-256 of the exact UTF-8/LF frame `direction-os-install-attempt-v1\nintent-sha256:<64hex>\nordinary-manifest-sha256:<64hex>\ninstall-nonce:<32hex>\n`. Writer derives every marker/temp path from that id and only then hashes the finalized receipt; recursive/self-derived input is invalid. Initial execution requires marker absent and ordinary rows exact preimage/absence. Exact empty absent-SETUP sibling temp-root is the sole first-marker exception and may only create the inner atomic zero-byte marker. Create/overlay writes exact postimage to a declared same-filesystem temp, fsyncs, then atomic-renames/replaces. With matching inner marker, exact temp may finish and a torn/wrong byte sequence at that declared unique temp may be removed and regenerated; undeclared temp or final-row third state stops. Completion removes declared temps and retains marker as protected history. Each execution/retry emits separate RFC8785 `install-reconcile-observation` plus lowercase SHA-256 containing immutable CALL receipt, retry session id, fresh live observation, marker/row/Git/protected pre+post, action and outcome. It never recomputes entry values or refinalizes the CALL.

Ordinary install manifest rows are `create|overlay|delete`. Delete is legal only for contract/tool retirement and records exact class/path/pre-mode/pre-blob/post=absent. It atomically renames exact preimage to a declared same-filesystem quarantine temp, fsyncs, then removes it. Matching-marker retry admits exact preimage, exact quarantine, or absent. A wrong/torn declared quarantine may be removed and regenerated only when the exact preimage is independently reconstructible from the pinned pre-HEAD/blob; otherwise it is a third state. Missing/wrong unreconstructible preimage, undeclared deletion, or any delete of production, feature or independently-authored acceptance-test bytes is RED. Deleted paths remain enumerated under protected-inventory proof.

Every finalized install also journals Git state: pre ref/HEAD/index logical tree, exact post tree, branch, deterministic commit metadata/OID, unique temp index, and declared ref/index lock paths. Existing-repo install post commit has exactly one parent equal to pinned pre-HEAD; absent repo-bootstrap alone is parentless. Wrong or multiple parents fail. After file postimages, retry may build/rebuild the temp index, materialize the exact content-addressed commit (an unreachable exact object is harmless), compare-and-swap the ref from exact pre to post, install the exact terminal index, and require clean state. Matching inner marker admits only pre/post HEAD/ref and declared Git temp/lock states; the exact empty absent first-marker root may only create its inner marker. A stale declared lock may be removed only after the prior installer is gone and exclusive-open succeeds; third ref/HEAD/index/protected-Git state stops.

SETUP bootstrap is limited to exact absent or virgin uninitialized state and has legal pre-install stages. `SETUP/interview` is branch/base-free/read-only and records either accessible-parent+absent-target inventory or the readable virgin existing inventory plus selected stack/profile blobs. Only after its writer event may `SETUP/adapter-author` return the declared source `work/validation-adapters/<stack>-v21.*` plus output-manifest artifact with exact path/mode/blob identities. Writer persists that RESULT/bundle plus a normal finalization CALL; a fresh distinct `SETUP/adapter-review` verifies exact bundle, writer resolver row, equivalent proposed product-native resolver identity and native tool identities read-only and returns acceptance. `SETUP/install` later cites the full ancestral chain; author, reviewer and installer/checker are pairwise distinct, and any earlier product write is invalid.
- SETUP/install intent carries ordinary `create|overlay|delete` rows, external corpus/specimen, accepted adapter and proposed product-native resolver identity; writer finalization adds the canonical resolver, nonce/hashes, marker/temp and Git journal rows. Delete is contract/tool retirement only. SETUP is branch/base-free. Absent entry also carries `repo-bootstrap` pinning canonical parent-chain path/case/reparse, target absence, object format, initial branch, remotes and deterministic root commit. Atomic creation of unique sibling `<target>.direction-os-<attempt-id>.tmp` is the first marker state: exact empty unmarked directory under the same open CALL may only receive the zero-byte inner marker; nonempty unmarked stops. After inner marker, while target remains absent, an exact owned partial temp-root may be discarded and rebuilt from the pinned manifest/Git journal. Publish by atomic rename only after exact clean parentless repo verification; target+temp, foreign target, wrong marker, reparse/case collision or parent drift fails. Existing virgin route requires the pinned clean initialized Git entry above and uses exact inventory pre/post. The next PLAN pins writer-observed setup HEAD.
- PLAN/EXECUTE/BUILD and every RE-SYNC substage carry exact branch/base and `base-authority: sha:<sha>|ref:<ref>@<observed-sha>`; base equals that SHA. PLAN/EXECUTE/BUILD also carry stable parent acceptance source/hash. Ref must resolve; offline uses the Direction-pinned SHA, never HEAD. RE-SYNC authority is contract-only and never a feature base.
- `PLAN/author` intent carries change-id, exact entry diff, installed toolchain and final conformance authority, but no future TESTABILITY pin or PLAN receipt; it never accepts owner verdict. Planner returns an ungated PLAN-CANDIDATE at exact P with the declared packet plus TESTABILITY binding contract and no source/test/oracle delta. Writer persists that event and a normal pending mechanical finalization CALL. A fresh finalizer creates finalized `PLAN/binding-validator` carrying P, candidate event and TESTABILITY pins. That distinct product-read-only session derives the obligation union independently, generates scratch-only probes and returns the first possible PLAN-GATED receipt. Its persisted GREEN event plus another fresh finalizer create `PLAN/verdict`. Only the owner's explicit `accepted` words for exact unchanged P/TESTABILITY/receipt plus a later fresh finalizer create EXEC; `revised|split` starts a new candidate and full binding validation, while `rejected` creates no EXEC. Required ancestry is `C-plan-call < W-plan-candidate < W-binding-validator-call < W-plan-receipt < W-verdict-call < W-verdict-result(accepted exact P) < W-execute-call`. A bare edit, self-validation, future pin at entry, receipt before validator, product write, missing full RESULT/history/LOG, bare-id `NOW.next`, double finalization, verdict/child mismatch or missing/non-ancestral event is invalid.
- This finalization transaction is generic. Whenever a writer commit creates an event that a child CALL must cite by `path@commit` - setup interview/adapter acceptance, final conformance, PLAN receipt/owner verdict, or accepted RED/progress/revision/light progress - that commit contains only the stable mechanical finalization CALL. The finalized child is created by a fresh RESULT/state_changes transaction in a strict descendant commit. `NOW.next` always remains a CALL/pointer; there is no special bare `finalize` command.
- Fresh EXECUTE intent carries the exact plan receipt/candidate/writer-event commit, an explicit accepted owner verdict for those unchanged bytes and stable execution identities, but no run/pre-execution receipt. Writer finalization verifies that event is ancestral to the separate verdict CALL/RESULT, that the verdict says accepted rather than revised/split/rejected and cites the identical P/TESTABILITY/receipt, then verifies candidate content, adds deterministic `run-id`, `pre-red-head`, `pre-execution-receipt-hash` and observation hash, persists them, and emits. Resume BUILD intent carries prior finalized run/pre-execution/plan receipts, RED oracle revision and exact accepted progress commit/ledger; writer finalizes only current resume observations.
- Real-id execution also carries exact result path and typed TESTABILITY/manifest evidence; coordinated light sentinel never removes base/acceptance/result/toolchain/run identity. The first RED receipt records author role/session, `parent-head == pre-red-head`, checkpoint R, exact test/oracle-registration-only delta, manifest/discovery/filter and expected failing status; R is the direct child or terminal commit of an explicitly declared test-author-only chain. Later independent revisions parent the exact accepted progress head, have the same path-only rule and preserve original frozen obligation assertions/mapping/acceptance; they may add or repair only a variant under that unchanged meaning.
- RE-SYNC substages use one exact `resync-entry-reason: lower|current-invalid`, clean first-entry branch/base and `HEAD==base`. Author/review are distinct and read-only. Writer-finalized install alone carries canonical resolver, equivalent product-native identity, executable attempt fields, marker/row/Git journal, create/overlay/delete manifest, corpus and accepted events, and may write. Same immutable open install reconciles only through its marker and separate reconcile observation despite allowed pre/post HEAD/stamp drift. Fresh-current return verifies resolver equality, every create/overlay/delete postcondition, protected inventory, deterministic terminal HEAD/index/clean state and toolchain/conformance identity before final receipt/smoke. Authority-advanced return is only `MANIFEST-RECONCILED` with exact terminal manifest/Git proof, old receipt and reconcile observation; writer consumes that call and freshly routes without current/feature receipt. Wrong resolver/marker, packet override, noncanonical remote/ref, query/fetch failure, recursive id, undeclared temp, final-row/ref/HEAD/index third state, cross-install replay, wrong delete or identity collision fails.
Product reports never contain their own blob/commit. Deliver/close evidence is handback data under the immutable BUILD CALL, is saved through Direction RESULT history, and never becomes a session-invented phase receipt. Missing routing stdout remains reconstructible by the declared D/A rule.
Every post-install PLAN/EXECUTE/BUILD CALL carries both `validation-conformance-receipt` and ancestral writer-owned `validation-conformance-event: history/<path>@<commit>` byte-identically through close; writer resolves the event independently and supplies its value as checker authority. SETUP/RE-SYNC author and review substages precede that final receipt. A receipt without its event, changed across post-install phases, or first introduced by a product RESULT is invalid.
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
