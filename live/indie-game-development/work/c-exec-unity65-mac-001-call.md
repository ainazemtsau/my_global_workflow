# CALL c-exec-unity65-mac-001 - Unity 6.5 Mac migration BUILD

to: executor
direction: indie-game-development
node: g-9c41
repo: github.com/ainazemtsau/GasCoopGame
kind: engineering
phase: BUILD
issued: 2026-07-11 (s-work-unity65-migration-plan-001)

goal: |
  Mac development checkout runs the project on exact Unity 6000.5.3f1 with all scripts compiling,
  required vendor integrations operational, and the approved migration evidence green.

context: |
  Frozen product PLAN commit: 7969f36a3a717c5f4a91d4b12d837bae1487be81 on local branch
  `codex/unity-6.5-migration-plan` in
  `/Users/antoninozemcev/codex-windows/GasCoopGame_codex`.

  Read the committed planning authority:
  - openspec/changes/c-exec-unity65-mac-001/PLAN.md;
  - openspec/changes/c-exec-unity65-mac-001/proposal.md;
  - openspec/changes/c-exec-unity65-mac-001/specs/toolchain/spec.md;
  - openspec/changes/c-exec-unity65-mac-001/tasks.md;
  - docs/adr/ADR-E-0010-c-exec-unity65-mac-001-unity-65-mac-migration.md.

  Owner verdict: `owner-ack:owner-chat-2026-07-11-unity65-plan-approved`, actual words `ok`.
  Product contract is synced to v19. This is the fresh BUILD session required by that contract.

  Installed Mac tools:
  - Unity 6000.5.3f1 arm64 at `/Applications/Unity/Hub/Editor/6000.5.3f1/Unity.app`;
  - Unity 6000.4.7f1 retained for rollback;
  - Homebrew dotnet@8 8.0.128 side-by-side with .NET 10.

  Disposable reconnaissance only (never a delivery checkout):
  `/Users/antoninozemcev/codex-windows/GasCoopGame_unity65_probe`, detached at a644e5d.
  Its `Logs/Editor.log` recorded the actual 6000.5.3f1 import and grouped compile failures.
  The owner's dirty main checkout must remain untouched.

boundaries: |
  BUILD only from the frozen planning artifacts. Do not edit PLAN.md, proposal.md, frozen spec,
  tasks.md, ADR-E-0010, or independently-authored acceptance/negative-control tests.

  Mac only. Do not install, edit, or validate the Windows machine in this session. Do not change game
  design, gas simulation meaning, networking protocol, save data, scene content, visual direction, or
  the current RenderGraph ABI. Do not disable or remove Odin, Unity MCP, FishNet/GameKit, or Dungeon
  Architect to obtain a green compile. Do not use source-text scans as engine/package/render behavior
  evidence.

  A required Unity/MCP/vendor installer/license path becoming unavailable, an unplanned paid/new
  dependency, or a required deviation from the frozen FishNet ownership/package decisions is a STOP
  under contract v16 and returns to the owner. Do not open or edit the dirty main checkout.

done_when: |
  1. Exact Unity `6000.5.3f1` and the reviewed Unity 6.5 package/settings migration are committed;
     local/generated noise is absent.
  2. Odin `4.0.2.1`, current stable Unity MCP dependencies/server, FishNet/GameKit, and Dungeon
     Architect compile and pass their named live-Editor smokes without disabling features.
  3. First-party, Dungeon Architect, and FishNet InstanceID migrations preserve full identity,
     object lookup, and runtime-copy ownership semantics; no raw/sign heuristic remains.
  4. A fresh-Library Mac import has zero C# compile errors and no unresolved behavior-loss or
     serialization warning.
  5. The pre-existing Mac HLSL path failure is fixed portably; all 1575 existing headless tests plus
     independent new acceptance/negative-control tests and normal repo gates pass.
  6. Unity EditMode/PlayMode plus Odin, MCP, Dungeon Architect, FishNet host/client, and gas RenderGraph
     smokes have recorded run evidence; source scan is not used as behavior proof.
  7. Frozen-change mutation, review, fix-class sweeps, fresh cross-family G5, closing report, and
     `check.ps1 -Deliver` gates are green at the reviewed tip.
  8. The handoff records Mac delivered SHA, exact Editor/package lock, rollback path, assumptions/cuts,
     and a ready but unstarted Windows follow-up; Windows creates no work in this BUILD.

return: |
  Return the Mac BUILD handoff with commits/PR, exact Editor and resolved package versions, grouped diff,
  clean-import and compile transcript, headless/Unity/vendor smoke results, mutation/review/fresh-G5
  evidence, closing-report path, assumptions/cuts, and rollback instructions. Reconcile every done_when
  bullet explicitly. Record the Windows follow-up as not started; Direction OS decides its later call.

budget: one focused half-day; retry cap and non-convergence rules from the product contract apply

END_OF_FILE: live/indie-game-development/work/c-exec-unity65-mac-001-call.md
