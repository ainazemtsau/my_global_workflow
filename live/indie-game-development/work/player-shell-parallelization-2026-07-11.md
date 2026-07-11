# Research brief — parallel Player Shell (2026-07-11)

status: non-canonical research; no product BUILD is authorized by this brief
direction: indie-game-development / g-9c41

## Bounded question

Can the basic player-controlled character start in parallel now, remain connectable to multiplayer, and avoid the
current Phase 0, checksum/Core, visual and canon surfaces?

## Established

- The current M1 road already needs player tracking; the older Gas Lab P2 discussion names a WASD capsule plus live
  Sc-sense dose. That gives the idea a natural home inside M1, not a new top-level track. The historical P2 section is
  not current authority and cannot authorize BUILD.
- Current NOW carries a 13-leg appetite and the rolling-wave tasks Lv-ingest, M1-A0 and M1-GAS-PROBE. No Player Shell
  task or ready CALL exists. The older approved M1 shape still shows the pre-exception 11-leg/A1 picture, so the
  current route must be reconciled before inserting work.
- The product has a real actor-pose transport/parity seam: TickInput carries actor id plus integer pose/volume, FishNet
  round-trips it, and the separate player digest detects divergence. It does not yet have a production player
  controller, authoritative locomotion, spawn/ownership contract or two-machine player proof.
- Sc-sense remains unwired into the live SimInstance tick. The debug capsule is paced from Unity frame time; it is
  owner-eye evidence, not authoritative multiplayer movement.
- The active product venues are not free interchangeable folders. Phase 0 owns dev, visual work is preserved on dev2,
  and the checksum/Core line has its own venue. Product policy defaults to one persistent dev worktree; an additional
  lab/player worktree therefore needs an explicit project-level exception, not an implicit worktree-per-feature rule.

## Recommendation

Do not open a new top-level character track and do not start BUILD from this research checkpoint. Run one fresh,
owner-present shape/repair-style reconciliation that makes the controller an explicit part of the current M1 road and
resolves three things before dispatch:

1. **Budget/home:** charge the work to existing M1 player-tracking intent, with no silent appetite extension.
2. **Scope:** choose between a thin pose-publisher shell and an engine-free deterministic PlayerCommand→motor slice.
3. **Venue:** reuse the persistent dev venue only when it is explicitly free/paused, or record a project-level
   exception for a dedicated lab/player venue; never reuse an occupied dev2/Core venue.

Candidate split for that shape to test, not a frozen implementation:

- **P2a — Player Shell:** local walk/look/camera, local-ownership/input-source seam, fixed-tick sampling and a quantized
  actor-footprint output; unique new player subtree, prefab, sandbox and tests. It may claim only
  multiplayer-shaped/connectable.
- **P2b — live integration:** command-vs-pose authority, deterministic collision/tick order, SimInstance + committed
  Sc-sense wiring, level PlayerSpawn contract, FishNet gameplay entity and the real two-machine proof.

P2a is fireable only after its PLAN proves an exact file manifest and current-diff disjointness. Until then the safe
boundary is a hypothesis, not a BUILD authorization. Hot exclusions are Core/Field, TickInput, SimInstance,
PlayerSense/GasSenseCapsuleDebug, Net/FishNet, Topology/GasView/Render, Packages, ProjectSettings and existing shared
scenes/prefabs.

## Worktree and Unity rule

- Git worktrees support isolated working directories, but product policy decides whether a new one is allowed.
- A Unity project root must keep its own ignored Library/cache; never share Library or open one folder in two Editors.
- Asset and `.meta` files travel together; unique new asset paths avoid scene/prefab merge fights.
- Parallelize code and headless checks. Serialize merge slots and owner-eye/Editor gates by default. Multiple Editors or
  MCP-controlled instances require a clean-folder/UnityLockfile, RAM and endpoint-addressing smoke check first.

## Owner choice

- **A — fold P2a into current M1 (recommended):** first reconcile/shape, then dispatch only the proven disjoint slice.
- **B — create a separate player track:** gives its own appetite, but duplicates an M1 obligation and adds governance.
- **C — wait for the sequential player-tracking step:** safest operationally, but gives up available parallel planning.

## Evidence and confidence

Local authority: `NOW.md`; `work/poligon-m1-shape-2026-07-10.md`;
`work/board/dashboard.html`; `knowledge/g9c41-sc-sense-delivered-unwired.md`; product-relative
`Assets/GasCoopGame/Core/Sim/TickInput.cs`, `Assets/GasCoopGame/Core/Sim/SimInstance.cs`,
`Assets/GasCoopGame/Adapters/GasView/GasSenseCapsuleDebug.cs`, and FishNet convergence tests.

External primary sources:

- Git linked worktrees: https://git-scm.com/docs/git-worktree.html
- Unity Asset Database / per-project Library cache: https://docs.unity3d.com/kr/current/Manual/AssetDatabase.html
- Unity YAML Smart Merge: https://docs.unity3d.com/kr/current/Manual/SmartMerge.html
- FishNet basic client-authoritative movement (the easy path, not automatically compatible with this project's
  input-lockstep authority): https://fish-networking.gitbook.io/docs/tutorials/getting-started/moving-your-player-around

Three independent explorers converged on the same architecture boundary. The first same-family refutation pass exposed
overclaims about immediate BUILD and automatic worktree permission; the revised pass left governance/venue routing
standing and scope deliberately inconclusive until PLAN. These are in-session pre-passes, not binding fresh-session G5.

END_OF_FILE: live/indie-game-development/work/player-shell-parallelization-2026-07-11.md
