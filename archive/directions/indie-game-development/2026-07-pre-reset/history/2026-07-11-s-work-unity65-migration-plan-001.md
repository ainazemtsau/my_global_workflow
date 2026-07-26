RESULT s-work-unity65-migration-plan-001 (call: owner-unity65-migration-plan-001)
direction: indie-game-development   play: work   node/task: g-9c41/Unity-6.5-migration-PLAN

outcome: |
  Mac готов к отдельному Unity 6.5 BUILD: exact Unity 6000.5.3f1 arm64 и .NET 8 установлены,
  disposable clean probe открыл проект и дал фактическую карту совместимости, а owner-approved
  подробный PLAN/spec/ledger/ADR заморожен в product commit 7969f36. Выпущен self-contained Mac-only
  BUILD CALL c-exec-unity65-mac-001; Windows сознательно не начат.

evidence: |
  1. `/Applications/Unity/Hub/Editor/6000.5.3f1/Unity.app/Contents/MacOS/Unity -version` вернул
     `6000.5.3f1`; Hub install завершился code 0. Unity 6000.4.7f1 оставлен для rollback.
  2. Homebrew `dotnet@8 8.0.128` установлен side-by-side; `Microsoft.NETCore.App 8.0.28` доступен.
  3. Probe `/Users/antoninozemcev/codex-windows/GasCoopGame_unity65_probe` был detached на a644e5d;
     Unity log зафиксировал Editor revision c2eb47b3a2a9, 2222 scripts, 3334 non-scripts и Safe Mode.
  4. 422 unique compile diagnostics сведены к корневым группам: Unity MCP 353, Odin 46,
     FishNet/GameKit 18, first-party InstanceID 4, Dungeon Architect InstanceID 1.
  5. Автомиграция probe показала exact package/settings diff: URP 17.5, uGUI 2.5, Test Framework
     1.7, AI Navigation 2.0.13, Newtonsoft 3.2.2, Physics Core 2D и Package Manager schema.
  6. Mac headless baseline реально запустился после установки .NET 8: 1524/1575 pass; все 51 fail
     имеют один pre-existing Windows-path root в HlslLayoutParser (`Assets\\...`).
  7. Product commit `7969f36a3a717c5f4a91d4b12d837bae1487be81` (`Freeze
     c-exec-unity65-mac-001 PLAN`) содержит только PLAN.md, proposal.md, frozen spec, tasks.md и
     ADR-E-0010; product worktree clean, branch ahead origin/main by one planning commit.
  8. Owner verdict on the presented BUILD plan: `ok` (2026-07-11). Earlier owner direction also says
     Mac first, then Windows, and accepted the recommendation to target 6000.5.3f1.
  9. No production code, RED/acceptance tests, Unity/package settings, Windows files, merge, or push
     were performed in this PLAN session. Dirty main checkout was not edited or opened in Unity.

state_changes: |
  1. ADD `live/indie-game-development/work/c-exec-unity65-mac-001-call.md` with the exact BUILD CALL
     saved by this result.
  2. NOW.md: updated-by -> s-work-unity65-migration-plan-001; INSERT c-exec-unity65-mac-001 as the
     first pending open_call; SET next -> `CALL: work/c-exec-unity65-mac-001-call.md`.
  3. APPEND this result's one-line log to LOG.md.
  4. SAVE this full RESULT to
     `live/indie-game-development/history/2026-07-11-s-work-unity65-migration-plan-001.md`.
  5. Existing bet tasks/statuses/unblock conditions, existing open_calls, TREE.md, CHARTER.md,
     knowledge/**, os/**, dirty product main, and Windows: no change.

captures:
  - Windows Unity 6000.5.3f1 migration is a separate post-Mac executor leg on the same delivered SHA;
    it starts only after Mac delivery/review and must produce no platform-only tracked diff.

decisions_needed: []

play_check:
  - 1 Recite: done - g-9c41 needs a working Mac Unity toolchain before the Poligon product legs can
    use the Editor; done_when was an owner-approved, evidence-backed Mac-first migration plan and handoff.
  - 2 Owner inputs (owner): done - this is owner-operated machine/project infrastructure; owner words
    used were `Я принимаю твою рекомендацию, можешь работать по ней`, approval of the presented plan
    was `ok`, and the owner personally accepted Unity's 2026-06-30 Editor Software Terms.
  - 3 Do the work: done - installed exact Editor/.NET runtime, ran an isolated real import, grouped
    failures, produced the owner-readable plan, and froze PLAN/spec/ledger/ADR @7969f36; no BUILD ran.
  - 4 Self-check: done - Editor version/install, disk, clean worktree, package diff, compile groups,
    headless baseline, contract v19, frozen artifacts, and PLAN/BUILD separation were checked directly.
  - 5 Close: done - owner approved with `ok`; one fresh Mac-only BUILD CALL is ready and Windows is deferred.

log: 2026-07-11 — work/plan (g-9c41/Unity-6.5, s-work-unity65-migration-plan-001): Unity 6000.5.3f1 и .NET 8 установлены на Mac; clean probe подтвердил шесть корневых групп миграции, owner «ok» утвердил Mac-first PLAN, frozen product PLAN @7969f36 и BUILD CALL c-exec-unity65-mac-001 выпущены; Windows оставлен отдельным post-Mac leg. → history/2026-07-11-s-work-unity65-migration-plan-001.md

next: |
  CALL c-exec-unity65-mac-001
  -> live/indie-game-development/work/c-exec-unity65-mac-001-call.md

END_OF_FILE: live/indie-game-development/history/2026-07-11-s-work-unity65-migration-plan-001.md
