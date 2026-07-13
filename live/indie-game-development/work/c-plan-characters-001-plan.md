# FROZEN PLAN — c-plan-characters-001 · трек g-6d4e «Игровые персонажи»

- status: FROZEN 2026-07-13 by s-plan-characters-v1-freeze-001
- node: g-6d4e (character presentation/embodiment track; parallel track, NOT a 2nd bet)
- owner approvals (in-session, cite):
  - order + socket-as-spine: «порядок ок» (implied by «Вариант 1» after the 3-wave brief)
  - first build leg: «Вариант 1»
  - freeze: «замораживай»
- canonical P2a0 verdict (single source): GasCoopGame origin/main@0e9eed02
  docs/results/c-exec-player-puppetmaster-p2a0-lean-spike-build-001.md

## 1. Track roadmap (owner-approved order)

The spine is the **socket** — a stable adapter-seam. The player prefab exposes a fixed contract; scenes plug
in to place/read a player, and the position behind the socket is fed by a SWAPPABLE source. This satisfies the
drop-in requirement from wave 1 and lets the core slot in later with zero prefab/scene change.

| Wave | Delivers | Built in | Waits on engine? |
|---|---|---|---|
| **В1** | Socket (authoritative-position seam) + drop-in controllable capsule + follow-camera. Any scene drops the prefab in → walk around. | presentation g-6d4e, GasCoopGame_dev | No — placeholder position source |
| **В2** | Body: low-poly rig + procedural locomotion + cosmetic PuppetMaster ragdoll; reaction/knockdown/get-up behaviour fills the declared hooks. ≈80% of the character feel. | presentation g-6d4e, GasCoopGame_dev | No — same placeholder |
| **В3** | Grid-ballistics (CORE): body flies → grid-collide → bounce → rest → get-up (Ф1); chains + loot/doors (Ф2). Prefab UNCHANGED — it just starts reading its position from real physics through the same socket. | CORE g-9c41 slice + 2-machine FishNet | **Yes** — needs core route (NearGas L1→…→I2) delivering grid+Step+lockstep |

First build leg (owner: Вариант 1) = **В1 only** (de-risk the socket cheaply before hanging a rig on it).
В2 immediately after; В3 is core work, scheduled when the engine delivers its foundation.

## 2. В1 — FROZEN spec (builder-ready)

**Deliverable.** A reusable player prefab + a stable adapter-seam such that any scene drops the prefab in and
gets a controllable player, whose authoritative position is driven through the seam by a swappable source. В1
ships a placeholder source (local input → movement); the real g-9c41 core position swaps in later with ZERO
prefab/scene change.

**The socket contract (stable from day 1).**
- Spawn/place: a scene drops the prefab (or calls a spawner) → a player appears.
- Authoritative body pose = a READ-ONLY view the prefab consumes each frame from an injected source
  (`IAuthoritativeBodyState`-style seam: position + facing; pull model — presentation reads latest, smooths).
  В1 source = placeholder (from input). Core source later. Builder owns exact C# surface.
- Reaction / knockdown / get-up: DECLARED in the contract as hooks, **no-op stubs in В1** (В2 fills behaviour) —
  so the interface other threads see is stable now.

**Owner-eye acceptance (the binding gate — owner runs PlayMode; Unity Personal = no headless PlayMode/CI):**
1. Drop the prefab into an empty test scene, press Play → player spawns, moves (WASD/gamepad), camera follows.
2. Drop the same prefab into a SECOND empty scene → works with no extra wiring (drop-in proven for other threads).
3. Decouple proof (the riskiest-assumption test — the reason В1 goes first): swap the placeholder source for a
   trivial scripted-path source; the capsule follows the path with the prefab UNTOUCHED → the socket really
   decouples the character from the position provider.

**Automatic gate (headless / EditMode logic, runs in the local .NET gate — no game launch):** the socket logic
is EditMode-testable and MUST be green: spawn places a player; the prefab consumes an injected source; swapping
the source implementation moves the player with no prefab edit; drop-in into a second scene composes.

**Independent test-author RED first (project builder-quality rule).** An independent test-author writes the
EditMode RED tests above FROM this spec BEFORE the builder builds; the builder cannot edit them.

**Boundaries (В1 explicitly does NOT include).** No character model/rig (primitive capsule); no ragdoll;
reaction/get-up are no-op hooks; no real physics/core/grid-ballistics; no networking (single machine); no gas;
no merge to main until owner-eye GREEN.

**Build location / routing.** Fresh GasCoopGame_dev session on a CLEAN worktree of the builder's choosing;
do NOT assign/clean/touch the occupied GasCoopGame_dev / GasCoopGame_core worktrees (foreign uncommitted work).
BUILD = Opus/Claude Code; VALIDATE = Codex read-only gate-runner (not authority; binding = gates + evidence +
owner-eye). OS dictates no branch/path/SHA.

## 3. Shape hygiene (G6)

- Cut list (≥1 real cut): (a) grid-ballistics / real physics DEFERRED to a g-9c41 core slice (В3); (b) rig,
  model, ragdoll, reaction/get-up BEHAVIOUR DEFERRED to В2; (c) networking DEFERRED (В3/FishNet).
- Riskiest assumption tested first: "the socket actually decouples presentation from the position provider" —
  proven by acceptance #3 + the swap-source EditMode test, before any rig is attached.
- Lens sweep: core_gameplay_depth — В1 is the reusable player other M1-5..7 work drops in; commercial_traction /
  audience_workflow — a droppable character feeds later capture scenes; coop_first — untouched (network is В3);
  technical_feasibility — de-risks the presentation↔core seam early; scope_production — solo-scope held (capsule,
  no content).

## 4. Downstream (captured, NOT built here)

- Grid-ballistics = g-9c41 CORE slice (Ф1 single body first ≈80% feel; Ф2 chains + loot/doors); blocked on the
  core route delivering grid+Step+lockstep; own slice PLAN later.
- Mandatory network leg: 2-machine FishNet proof that "authoritative grid-ballistics + local cosmetic ragdoll"
  stays consistent across machines; queue with the grid-ballistics core slice.

END_OF_FILE: live/indie-game-development/work/c-plan-characters-001-plan.md
