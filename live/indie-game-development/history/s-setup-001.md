# REPORT — s-setup-001 (executor / repo bootstrap, 2026-06-13) — c-setup-001 DONE

Engineering executor REPORT for `c-setup-001` (repo bootstrap per `os/engineering/PROJECT_SETUP.md`),
applied as state by the agent-CLI writer. Setup of the re-created product repo is **DONE**, gates
green locally and in CI; t-1 is unblocked.

```yaml
RESULT s-setup-001 (call: c-setup-001)
direction: indie-game-development   kind: engineering (repo bootstrap)   node/task: g-9c41 / t-1 (precondition)
state: DONE
outcome: |
  The product repo GasCoopGame was RE-CREATED from scratch through the OS engineering process and
  passes the PROJECT_SETUP done-when bar. Architecture (ADR-0001): all game logic in an engine-free
  C# core (Assets/GasCoopGame/Core, asmdef noEngineReferences:true) compiled headless by
  core/GasCoopGame.Core.csproj (netstandard2.1); Unity = render/input/transport adapters only
  (R13/R14). The dependency-boundary gate is the headless core build itself (a Unity reference in
  core fails dotnet build — proven with a seeded violation). Headless tests (net8.0, NUnit) + a
  test-hygiene gate + a self-ignoring _scratch + core CI on every PR. Owner's dev-worktree workflow
  encoded in AGENTS.md. The old codex-native-execution-layer harness + Unity 6.4 tech stream are
  retired. Owner-delegated technical choices were decided with plain rationale (core netstandard2.1,
  tests net8.0; PlayMode-CI/formatter/hooks/evaluator deferred). Byproduct os/engineering/profiles/
  unity.md created. The OS-vs-repo dual-harness maintenance flag is resolved (standardized on OS).
evidence: |
  PROJECT_SETUP done-when checklist (with evidence):
  - [x] one-command check green LOCALLY (pwsh tools/check.ps1 -> build + 3/3 tests + hygiene, exit 0)
        AND in CI (GitHub Actions core-ci run 27459845620 on main @5fe3b3b, and the dev run, both success).
  - [x] dependency-boundary check exists & FAILS on a seeded violation: a `using UnityEngine;` in core
        -> `dotnet build core` error CS0246, exit 1; removed -> exit 0.
  - [x] engine-free core builds & tests HEADLESS via dotnet, ZERO Unity refs (GasCoopGame.Core.dll
        netstandard2.1; GasCoopGame.Core.Tests net8.0, 3/3 pass).
  - [x] root AGENTS.md (run contract + dev-worktree workflow + commands, <=150 lines); module
        AGENTS.md at Assets/GasCoopGame/Core/.
  - [x] REVIEW.md, validation.config, docs/adr/ADR-0001-stack.md, docs/FRICTION.md, openspec/ exist.
  - [x] _scratch/ self-ignores; a seeded file is git-ignored (git check-ignore confirms).
  - [x] test-hygiene gate fails on a seeded assertion-free test (exit 1); passes clean (exit 0).
  - [x] os/engineering/profiles/unity.md created (byproduct, in state_changes -> workflow repo).
  - [deferred] Unity PlayMode CI (needs Unity license/GameCI); formatter (dotnet format/.editorconfig);
        notification hooks; evaluator subagent. Recorded, not done — out until needed.
  Commits: product repo dev @ee047eb (setup) -> merged to main @5fe3b3b (CI green); pushed origin.
  Unity 6.3 LTS = 6000.3.17f1. Owner physically created the clean Unity project; agent scaffolded the rest.
state_changes: |
  live/indie-game-development/NOW.md:
    - active_tasks t-1: status `blocked_on c-setup-001` -> `ready` (setup done; CI green).
    - open_calls: c-setup-001 CLEARED (DONE); c-frame-002 kept.
    - next: the c-setup-001 CALL -> c-exec-002 (the t-1 build CALL on the clean repo).
  os/engineering/profiles/unity.md: CREATED (the byproduct stack profile; first unity profile).
  live/indie-game-development/LOG.md: append the setup line -> history/s-setup-001.md.
  live/indie-game-development/history/: + s-setup-001.md (this REPORT).
  No TREE.md / CHARTER.md change; active_bet g-9c41 unchanged (appetite/kill_by intact).
captures:
  - "RESOLVED: OS-CONTOUR-vs-codex-harness dual-engineering maintenance flag (s-work-001) — closed by re-creating the repo on the OS contour; codex layer retired with the old setup."
  - "FRAME touch-up (c-frame-002): CHARTER.md still says 'product repo not yet canonized'; it IS canonized now — GasCoopGame, OS-aligned, Unity 6.3 LTS. Canonize on the next charter edit."
  - "Tiny CI friction: GitHub deprecation warning — actions/checkout@v4 + setup-dotnet@v4 move to Node 24 (forced 2026-06-16). Bump action versions in core-ci.yml at convenience (non-blocking)."
  - "Deferred setup items to pick up later: formatter (dotnet format + .editorconfig) — recommended first in t-1; Unity PlayMode CI (license); notification hooks; evaluator subagent."
decisions_needed: []
log: "2026-06-13 — setup (executor, g-9c41/t-1 precondition): product repo RE-CREATED via PROJECT_SETUP (Unity 6.3 LTS); engine-free core + headless dotnet build/test + boundary gate (proven) + hygiene + _scratch + core CI; AGENTS.md run contract + dev-worktree workflow; ADR-0001; profiles/unity.md. Gates GREEN local + CI (main @5fe3b3b). c-setup-001 DONE; t-1 unblocked. next = c-exec-002. -> history/s-setup-001.md"
next: |
  CALL c-exec-002 (the t-1 build CALL) — see live/indie-game-development/NOW.md `next` for the full
  packet: engine-free deterministic sim-core + 3-mode composition root + FishNet host+2-headless-client
  per-tick hash handshake on a trivial field + honest FishNet verdict; work in the dev worktree, merge
  to main when green; FishNet dependency needs owner approval in PLAN; budget one focused half-day;
  Fable-5 window (closes 2026-06-22).
```

END_OF_FILE: live/indie-game-development/history/s-setup-001.md
