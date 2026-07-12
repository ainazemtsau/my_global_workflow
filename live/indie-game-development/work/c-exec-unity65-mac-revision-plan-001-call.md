# CALL c-exec-unity65-mac-revision-plan-001 — Unity 6.5 Mac migration revision PLAN

to: executor
direction: indie-game-development
node: g-9c41
repo: github.com/ainazemtsau/GasCoopGame
kind: engineering
phase: PLAN
issued: 2026-07-12 (s-work-unity65-mac-route-a-001)
parent: s-work-unity65-mac-route-a-001

goal: |
  У Mac-миграции на точную Unity 6000.5.3f1 есть owner-approved revised plan, который делает принятую
  несовместимость FishNet scene-handle wire явной и version-gated, восстанавливает независимые доказательства
  и превращает существующий candidate в честно спланированный вход для отдельной BUILD-сессии без заявления
  о готовности к merge или delivery.

context: |
  Owner resolved d-unity65-mac-revision-route-001 with actual words `A` on 2026-07-12:
  `owner-ack:owner-chat-2026-07-12-unity65-route-a`.

  Option A means exactly: continue Unity 6000.5.3f1; accept the coordinated FishNet scene-handle wire change
  `int -> ulong` for same-version peers; add an explicit protocol-version incompatibility gate so mixed old/new
  builds reject rather than silently misread; repair every close-check finding; merge only after all gates are green.
  It is not a waiver for any other networking change or delivery gate.

  Read the Direction OS close-check:
  `/Users/antoninozemcev/codex-windows/my_global_workflow/live/indie-game-development/history/2026-07-11-s-work-unity65-mac-closecheck-001.md`.

  Product committed evidence is the candidate tip `df1e5caec09556b781dad7fb703fbc5e1438f4e0`, five commits over
  `origin/main == origin/dev == a644e5db538d1102f726630d6a4ac2f3f1bdcf5a`; `origin/dev2` is already an
  ancestor of main. The existing frozen authority is change `c-exec-unity65-mac-001` at PLAN commit `7969f36`.
  Preserve it as historical evidence; it explicitly prohibited networking-protocol changes and therefore cannot
  silently authorize the owner-approved revision after the fact.

  Close-check findings that the revised plan must account for:
  - the accepted `SceneLookupData.Handle int -> ulong` broadcast change needs a protocol-version rejection contract;
  - builder and production changes were committed together with acceptance tests, and builder later edited those
    tests plus pre-existing frozen tests, so independence cannot be restored by relabelling or ticking the ledger;
  - the Mac harness searches `pwsh.exe` and then `powershell`, producing 1522/1528 on this Mac;
  - frozen telemetry byte hashes encode checkout EOL without an explicit cross-platform JSON EOL rule;
  - 49 unique UAC serialization diagnostics need class-by-class disposition, not a blanket non-gating label;
  - fresh-Library/import and Unity test evidence predates late source fixes, while current MCP discovery finds no
    target tests;
  - recorded mutation targeted unchanged `CoarseSectorGraph.cs`, not the migration diff;
  - review evidence lacks the required refuted register/fix-class records and is not binding fresh-session G5;
  - closing report, all-passing ledger, exact rollback proof and green `tools/check.ps1 -Deliver` are absent;
  - Claude authentication returned 401, so any explicitly cross-family check remains unavailable until restored.

  Product contract is synced to v19: PLAN and BUILD are separate sessions. The PLAN must be detailed but simple,
  owner-readable, and stop at owner approval. It writes no production code and commissions/authors no RED tests.

  launch:
    lane: E — temporary Mac toolchain/network migration, same work as c-exec-unity65-mac-001
    venue: /Users/antoninozemcev/codex-windows/GasCoopGame_codex @ codex/unity-6.5-migration-plan; PLAN artifacts only
    machine: MacBook
    base: origin/main @a644e5db; committed candidate @df1e5ca
    conflict_surface: openspec/docs planning authority only; no production/test/package/scene edits
    depends_on: [owner-ack:owner-chat-2026-07-12-unity65-route-a]
    merge_queue: none — PLAN only; BUILD/merge slot is assigned only after plan approval
    gates: owner approves the readable plan; BUILD G5 remains a separate fresh session after implementation

  The venue currently has unrelated uncommitted owner/editor changes in `.vscode/settings.json` and
  `Assets/GasCoopGame/Levels/GasLab/Flow/CoopSmallSGF.asset`. They are not candidate evidence and must remain
  untouched, unstaged, uncleaned and uncommitted. If planning cannot proceed without disturbing them, STOP and return.

boundaries: |
  PLAN only. Do not write production code, package/settings changes, acceptance/negative-control tests, test
  harness fixes, evidence runs, closing reports, ledger pass marks, review fixes, merge commits or pushes.

  The owner approval is narrow: only the already-observed FishNet scene-handle width incompatibility plus an
  explicit mixed-version rejection gate. Do not change game design, gas/core meaning, save data, scene content,
  visual direction, RenderGraph ABI, general network semantics or supported peer topology.

  Do not silently rewrite the old frozen PLAN/spec/tasks/ADR as though they had always allowed the wire change.
  Define a traceable successor or explicit amendment authority. Do not call existing builder-authored tests
  independent, waive missing gates, or substitute source scans for real runs. Windows execution remains out of scope.

  Required unavailable tooling is a STOP under contract v16. No machine-local shim, reduced-fidelity substitute or
  assumed owner waiver is permitted.

done_when: |
  1. A detailed but simple owner-readable revision plan names every technical decision and why, presents the
     player/operator-visible mixed-version rejection behavior, and receives the owner's actual approval words;
     without approval the leg returns a checkpoint and does not freeze.
  2. New traceable planning authority explicitly supersedes or amends the relevant old decisions without erasing
     the frozen c-exec-unity65-mac-001 history; it carries a single approach token, updated spec-silence audit,
     deliverable coverage, failure-first ledger and ADR ownership.
  3. The plan freezes the narrow protocol contract: same-version 6000.5.3f1 peers use the full-width handle path;
     mixed protocol versions reject before scene-broadcast decoding; no compatibility with old builds is claimed;
     every other networking invariant remains unchanged.
  4. The plan restores role independence honestly: a fresh post-freeze test-author derives RED acceptance and
     negative controls from only the revised spec; the later builder may not edit them. Existing builder-authored
     or modified tests receive an explicit keep/replace/delete disposition rather than being relabelled.
  5. Every close-check class has a named failing ledger row and evidence venue: portable PowerShell selection,
     cross-platform EOL invariant, package-change explanation, serialization-warning disposition, final-tip clean
     import/test discovery, FishNet same-version host/client + mixed-version rejection, diff-relevant mutation or
     explicit owner decision if structurally N/A, review/refuted-register/fix-class sweeps, binding fresh G5,
     closing report, exact rollback, all-passing ledger and `tools/check.ps1 -Deliver`.
  6. The committed PLAN diff contains only the new planning authority and records the preserved dirty-file boundary;
     no BUILD/test/merge begins. The return supplies the frozen commit and enough contract detail for Direction OS
     to issue a separate fresh BUILD CALL.

return: |
  Return the readable revision plan, technical decisions and cuts; exact planning artifact paths and commit;
  the owner's approval words or a checkpoint awaiting them; confirmation that no production/tests/dirty files were
  touched; and the proposed BUILD contract inputs. Direction OS, not the planner, issues the later BUILD CALL.

budget: one focused PLAN session; zero BUILD work

END_OF_FILE: live/indie-game-development/work/c-exec-unity65-mac-revision-plan-001-call.md
