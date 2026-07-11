# RESULT — s-work-unity65-mac-closecheck-001 (2026-07-11)

## Owner summary

Unity 6000.5.3f1 подходит проекту на текущей mid-cycle стадии, и сделанную миграцию разумно довести. Но candidate
`codex/unity-6.5-migration-plan@df1e5ca` сейчас не merge-ready: проверка нашла незаявленное изменение FishNet wire
format, нарушение независимости тестов, нерелевантную mutation, незакрытые serialization warnings и отсутствующие
closing gates. Живые Mac-проверки тоже пока невоспроизводимы. CALL оставлен открытым; merge не выполнялся.

Рекомендация владельцу — `A / revised`: принять coordinated wire break с обязательным protocol-version gate,
провести отдельный repair/closeout и мержить только после полностью зелёных ворот. Альтернативы: сохранить 32-bit
wire через собственное mapping или остаться на 6.3 LTS. Фактических слов владельца A/B/C в сессии не было.

```text
RESULT s-work-unity65-mac-closecheck-001 (call: owner-plain-unity65-merge-review-2026-07-11)
direction: indie-game-development   play: work   node/task: g-9c41/c-exec-unity65-mac-001
outcome: |
  CHECKPOINT / AWAITING OWNER VERDICT. Direction OS main синхронизирован и опубликован @2190d7a. В продукте
  origin/main == origin/dev == a644e5db; dev2 полностью является предком main и не требует отдельного merge.
  Candidate codex/unity-6.5-migration-plan@df1e5ca чист и на пять коммитов впереди базы; dirty owner main checkout
  не тронут. Переход на Unity 6000.5.3f1 рекомендован стратегически, но текущий candidate опровергнут как
  merge-ready и оставлен невлитым. c-exec-unity65-mac-001 остаётся открытым до owner A/B/C и полного repair/closeout.
evidence: |
  Strategic source: Unity release support states that Update releases are production-ready and preferred for new
  and mid-cycle productions, while 6.3 LTS is for live service / production lock:
  https://unity.com/releases/unity-6/support. Exact 6000.5.3f1 release (2026-07-08) and known issues:
  https://unity.com/releases/editor/whats-new/6000.5.3f1.
  Done_when 1 — PARTIAL: ProjectSettings/ProjectVersion.txt pins 6000.5.3f1 and package/settings migration is
  committed. Additional package-lock upgrades still lack the frozen spec's required closing-report explanation.
  Done_when 2 — PARTIAL: committed Odin 4.0.2.1, MCP 0.83.1 and Dungeon Architect behavior evidence exists; the
  recorded Net assembly contains real Tugboat host/client tests. Current live MCP is reachable and Editor is idle,
  but tests-run now reports no matching target assembly/class/method, so final-tip reproducibility is not established.
  Done_when 3 — REFUTED AS SCOPED: first-party EntityId, DA lookup and explicit NetworkObserver runtime-copy
  ownership implementation survived same-family refutation. Separately, SceneLookupData.Handle changed int→ulong
  and is serialized in FishNet scene broadcasts; the new test proves only new↔new roundtrip. CALL boundaries forbid
  networking protocol changes and contain no owner-ack for this deviation. Unity documents EntityId as opaque and
  its raw bit arrangement as upgrade-sensitive: https://docs.unity3d.com/6000.5/Documentation/ScriptReference/EntityId.html.
  Done_when 4 — REFUTED: Logs/Editor.log contains 49 unique UAC1001/UAC1002/UAC1005/UAC1006/UAC1009/UAC1010
  serialization diagnostics across Dungeon Architect/FishNet without message-by-message disposition. Fresh-Library
  evidence was committed before later source fixes 883f2ee and 76307d6.
  Done_when 5 — REFUTED: direct Mac run built Core but finished 1522 passed / 6 failed / 1528 total because six
  existing tests cannot launch `powershell`; their selector checks `pwsh.exe` and otherwise falls back to
  `powershell`, neither present on this Mac. Git history also shows a96de31 introduced production and the new
  Unity65MigrationAcceptanceTests together, while 883f2ee changed that acceptance oracle; frozen tasks require a
  separate test-author and forbid builder edits. Frozen byte-digest tests were also edited instead of STOP.
  Done_when 6 — INCONCLUSIVE: prior committed EditMode/host-client/RenderGraph evidence is plausible, but it predates
  late fixes and current MCP discovery cannot reproduce the target run. No final raw TestResults artifact is committed.
  Done_when 7 — REFUTED: mutation-c-exec-unity65-mac-001.json targets unchanged CoarseSectorGraph.cs rather than
  migration diff; review records Codex GPT builder and GPT reviewer, lacks required Refuted-register, and is not the
  fresh cross-family G5 named by CALL. docs/results/c-exec-unity65-mac-001.md is absent, BUILD ledger rows are
  unchecked, and tools/check.ps1 -Deliver must fail statically. Local PowerShell is unavailable. A fresh Claude/Opus
  read-only G5 attempt returned 401 Invalid authentication credentials, so same-family pre-passes were not promoted.
  Done_when 8 — REFUTED: no delivered SHA/closing report/handoff exists; Windows remains unstarted. Base a644e5db
  pins Unity 6000.3.17f1, while the recorded local rollback Editor is 6000.4.7f1, so exact rollback still needs proof
  or installation of 6000.3.17f1.
  Same-family independent pre-passes: two verdict sets each found 6 REFUTED / 2 SURVIVED-INTRA-FAMILY; merge-focused
  pre-pass found 5 REFUTED / 2 SURVIVED-INTRA-FAMILY / 1 INCONCLUSIVE. These are non-binding; fresh cross-family G5
  remains mandatory on the repaired final tip.
state_changes: |
  live/indie-game-development/NOW.md: set updated to `2026-07-11 by s-work-unity65-mac-closecheck-001`; update only
  open_calls entity c-exec-unity65-mac-001 note with checkpoint tip/blockers and keep it pending; append pending
  decision d-unity65-mac-revision-route-001 with A/B/C and recommendation A. Preserve every task, other open_call,
  existing decision, recurring entry and NOW.next.
  live/indie-game-development/LOG.md: append exactly the log line below once.
  live/indie-game-development/work/board/dashboard.html: regenerate the Unity open-work card, owner decision batch
  and 2026-07-11 journal from merged NOW+LOG; preserve unrelated sections.
  Save this full RESULT once at
  live/indie-game-development/history/2026-07-11-s-work-unity65-mac-closecheck-001.md.
  No product repo, task status, TREE.md, CHARTER.md, knowledge, NOW.next, merge, branch push or Windows change.
captures:
  - Existing Mac test harness searches `pwsh.exe` and falls back to `powershell`; a fresh independent test-author must
    make executable selection portable instead of relying on a machine-local shim.
  - Frozen telemetry digest expectations encode checkout EOL while generic measurement JSON has no eol attribute;
    a fresh test-author must make the byte-invariant explicitly Mac/Windows stable.
  - If owner chooses A, mixed old/new FishNet clients need an explicit protocol-version rejection path; silent
    compatibility is not claimed.
decisions_needed:
  - q: d-unity65-mac-revision-route-001 — choose the route after refutation of the Unity 6000.5.3f1 Mac candidate.
    options: ["A — revised: continue 6.5, accept coordinated FishNet wire break with a protocol-version gate, repair/closeout, then merge only on green", "B — revised-conservative: continue 6.5 but preserve 32-bit wire through owned token mapping, then full repair/closeout", "C — rejected: remain on Unity 6.3 LTS and park the branch"]
    recommendation: "A, because this is a mid-cycle project with no evidenced live-client compatibility burden, the core migration is already complete, and coordinated versioning is cheaper than introducing a new mapping layer."
play_check:
  - 1 Recite: done — проверено ровно одно открытое инженерное обязательство c-exec-unity65-mac-001 против его восьми done_when; цель владельца: «стоит ли нам обновляться, эту ветку мержить с обновлением для Unity».
  - 2 Owner inputs: done — это не owner-content artifact; использованы текущие слова владельца «стоит ли нам обновляться» и «если да, то тогда это лучше сделать», но требуемого A/B/C verdict после панели в сессии нет.
  - 3 Do the work: done — workflow/product refs синхронизированы; frozen PLAN/CALL/spec/tasks, five-commit diff, evidence, logs and gates audited; three read-only same-family refutation children merged; live Core/MCP probes run; official Unity support/release sources checked.
  - 4 Self-check: done — все восемь done_when получили отдельный disposition и evidence; administrative omissions separated from protocol/test-independence/reproducibility failures. Binding fresh cross-family G5 explicitly remains unavailable, not imitated.
  - 5 Close: done as checkpoint — owner brief presented with A/B/C and recommendation A; no owner verdict appeared, so the same engineering CALL remains pending and no merge/repair starts.
log: 2026-07-11 — work/checkpoint (g-9c41/Unity-6.5 close-check, s-work-unity65-mac-closecheck-001): переход на 6000.5.3f1 рекомендован, но df1e5ca refuted как merge-ready из-за FishNet wire deviation, test-independence/gate/evidence дыр и невоспроизводимых Mac ворот; c-exec-unity65-mac-001 оставлен открытым, d-unity65-mac-revision-route-001 ждёт owner A/B/C. → history/2026-07-11-s-work-unity65-mac-closecheck-001.md
next: |
  awaiting_decision d-unity65-mac-revision-route-001. Owner may answer A, B or C in a fresh session. No repair,
  branch push or merge begins before those words; primary NOW.next remains work/c-exec-unity65-mac-001-call.md.
```

END_OF_FILE: live/indie-game-development/history/2026-07-11-s-work-unity65-mac-closecheck-001.md
