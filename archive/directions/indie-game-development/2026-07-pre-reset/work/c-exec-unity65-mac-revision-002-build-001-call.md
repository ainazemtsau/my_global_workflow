CALL c-exec-unity65-mac-revision-002-build-001
to: executor
direction: indie-game-development
node: g-9c41
repo: github.com/ainazemtsau/GasCoopGame
kind: engineering
phase: BUILD
issued: 2026-07-12 (s-repair-unity65-mac-revision-002-route-001)
parent: c-exec-unity65-mac-revision-002

goal: |
  Repository gates run locally through one cross-platform .NET 8 entry point without mandatory PowerShell,
  preserve every existing green/red gate meaning and seeded-miss protection, and are independently evidenced
  as a delivered prerequisite without starting the Unity/FishNet revision-001 BUILD.

context: |
  Product venue:
  `/Users/antoninozemcev/codex-windows/GasCoopGame_codex`
  branch `codex/unity-6.5-migration-plan`
  frozen PLAN commit `7a3e7470a3b6175542dc0a2f23152798f2aa8dd1`
  parent `8a344e97da10da417d76c0a3e7534bec0a0f7c96`
  change id `c-exec-unity65-mac-revision-002`
  approach `lan-local-dotnet-gates-adapter-only`.

  Binding planning authority:
  - `openspec/changes/c-exec-unity65-mac-revision-002/PLAN.md`
  - `openspec/changes/c-exec-unity65-mac-revision-002/proposal.md`
  - `openspec/changes/c-exec-unity65-mac-revision-002/specs/toolchain/spec.md`
  - `openspec/changes/c-exec-unity65-mac-revision-002/tasks.md`
  - `docs/adr/ADR-E-0012-c-exec-unity65-mac-revision-002-lan-local-dotnet-gates.md`

  The owner approved the frozen PLAN on 2026-07-12 with actual words
  `Одобряю PLAN c-exec-unity65-mac-revision-002`. The PLAN-only commit contains five planning files and no
  runner, test, wrapper, package, configuration, Unity, evidence-run, merge, or push change.

  This change is a prerequisite for, not a continuation of,
  `c-exec-unity65-mac-revision-001`. After this runner is independently delivered, Direction OS must issue a
  separate fresh CALL before the Unity/FishNet BUILD may resume. This CALL is registered as a non-priority
  parallel track; the direction's default `NOW.next` remains Phase 0.

  The checkout contains unrelated unstaged owner/editor changes in `.vscode/settings.json` and
  `Assets/GasCoopGame/Levels/GasLab/Flow/CoopSmallSGF.asset`. They must remain untouched, unstaged,
  uncleaned, and uncommitted.

  Contract v19 applies. PLAN and BUILD are separate sessions. BUILD begins with a fresh independent test-author
  reading only the frozen revision-002 spec; the builder may not edit those tests, the spec, or the ledger.

boundaries: |
  Do not change Unity, packages, FishNet, scene handles, application protocol, gameplay, gas/core behavior,
  rendering, scenes, saves, authority, ordering, reliability, timing, supported peer topology, late join,
  matchmaking, host migration, or the LAN-only game boundary.

  Do not add a cloud gate service, remote telemetry, an HTTP/API dependency, automatic restore/download,
  a new shell dependency, a new test framework, or a policy simplification disguised as portability work.

  Do not edit the frozen PLAN/spec/ledger/ADR or the fresh independent acceptance/negative-control tests.
  Historical plans, ADRs, results, measurements, and their recorded PowerShell commands remain history.

  Required unavailable local tooling is a STOP. No network fallback, implicit restore, shim, reduced-fidelity
  substitute, source-scan proxy, or assumed waiver is allowed.

  Do not start or resume `c-exec-unity65-mac-revision-001`; do not run Unity/FishNet evidence, Windows
  validation, merge, or push. Preserve the two unrelated dirty owner/editor files exactly.

done_when: |
  1. A fresh test-author reads only the frozen revision-002 spec and first commits RED headless acceptance tests
     plus one negative control for every machine-checkable property token; ancestry proves the builder never
     edits them, the frozen spec, or the ledger.
  2. One BCL-only `net8.0` executable at `tools/GasCoopGame.Gates/GasCoopGame.Gates.csproj` owns the canonical
     `check`, `check --deliver`, named-gate, mutation, and self-test commands. Canonical runs need no PowerShell,
     shell, cloud/network service, telemetry, automatic restore, or download.
  3. Real headless and black-box temporary-repository evidence proves complete parity and ordering for the inner
     and deliver paths: all current hygiene/scan/mutation/coverage/escape/review/result/TRX/git gate families,
     every seeded-miss fixture, guarded roots, category counterpart rules, frozen-change discovery,
     N/A/grandfather behavior, baselines, and stale-artifact rejection retain their meanings and cannot false-green.
  4. Every current `tools/*.ps1` entry point remains only as a thin optional adapter to one named runner command;
     optional `.sh`/`.cmd` adapters preserve supported legacy arguments, stdout/stderr, and exit status. No adapter
     owns repository policy, and the canonical runner never invokes a shell adapter.
  5. Missing command-specific local prerequisites fail non-zero and name the prerequisite without implicit
     restore/download. Path/root/symlink handling rejects escapes; negative-control TRX is recreated fresh;
     mutation JSON and other hashed/parsed text artifacts satisfy the frozen UTF-8-without-BOM/LF byte contract.
  6. Active invocation text in `AGENTS.md`, `CLAUDE.md`, `validation.config`, `openspec/README.md`,
     `openspec/CHANGE_SPEC_TEMPLATE.md`, and active developer instructions names the canonical .NET command;
     historical evidence remains unchanged and `docs/FRICTION.md` receives the migration fact.
  7. Diff-relevant mutation is non-vacuous; independent final-tip review records scope/site/disposition,
     refuted-register markers, and class+sweep closure; a separate binding fresh-session G5 tries to refute the
     reviewed tip. Final local `check` and `check --deliver`, all negative controls, the frozen ledger, rollback
     proof, and `docs/results/c-exec-unity65-mac-revision-002.md` are green and mutually reconciled.
  8. The returned evidence confirms the two unrelated dirty files were preserved and that Unity/FishNet
     revision-001 BUILD, Windows validation, merge, and push did not start. Delivery of revision-002 opens only a
     future Direction-OS decision to issue a separate fresh revision-001 resume CALL.

return: |
  Return the final product commit and branch; exact changed-file summary; independent test-author and immutable-test
  ancestry; opened transcripts/artifacts for every done_when item; complete gate-family/seeded-miss and adapter
  parity records; local-prerequisite, path, stale-artifact, and byte-contract evidence; mutation, review,
  refuted-register, fix-class sweep, and binding fresh-session G5 evidence; closing-result path; exact rollback
  proof; all-green ledger and canonical `check --deliver` output; assumptions/cuts; confirmation that both dirty
  owner files, revision-001 BUILD, Unity/FishNet evidence, Windows validation, merge, and push were untouched.
  On any required unavailable tool or unresolved gate, return a checkpoint naming the blocker and leave delivery
  unclaimed.

budget: one focused runner BUILD/delivery session; non-priority; no revision-001 BUILD, Windows validation, merge, or push

END_OF_FILE: live/indie-game-development/work/c-exec-unity65-mac-revision-002-build-001-call.md
