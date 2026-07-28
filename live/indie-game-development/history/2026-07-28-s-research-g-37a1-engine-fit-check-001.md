# RESULT s-research-g-37a1-engine-fit-check-001

call: c-research-g-37a1-engine-fit-check-001
direction: indie-game-development
play: research
node/task: g-37a1/engine-fit-check

outcome: |
  The bounded engine-fit check is complete against product commit
  `1a6373b84b6bf4da95a24efc3015e23b9ba5d419` (`main`, clean before and
  after inspection). All seventeen requirements are answered; none is UNKNOWN.

  VERDICT RULE USED HERE:
  - SATISFIED TODAY means the required invariant already exists at the named
    commit. It does not mean a complete playable core exists.
  - NEEDS A FIX means the requirement can be added by wiring or extending the
    current contracts without replacing one of the four named layers.
  - NEEDS A REWRITE OF LAYER (d) means the current immutable/static
    structure-generation path must be replaced by a runtime, tick-stamped,
    state-preserving topology transaction. It does NOT mean deleting the
    per-cell transport, determinism/replication, or render contracts.
  - Sizes are focused engineering days, not calendar forecasts. A gross size
    includes shared prerequisites needed if that row were taken alone; a
    marginal size is the row-specific remainder after those prerequisites.
    Gross row sizes must not be summed.

  SHARED PRICE BASIS:
  - S0, finish the authoritative static near-gas route through integration:
    10-18 days. The dashboard still marks L2, C1, M0, L3, I1, L4, L5, L6 and
    I2 not started (`docs/gas-simulation/dashboard.html:389-397`).
  - S1, runtime gas/topology route R0 -> E1 -> D1 -> P1 if selected -> T1 ->
    X1 -> LAB/I3: 18-32 days. This is the shared layer-(d) replacement slice
    (`docs/gas-simulation/PROGRAM.md:71-80,228-260`).
  - S2, playable shell (body, arbitrary digging input/collision, integrated
    scene and build): 10-18 days.
  - S3, experiment rig, readability, air/death presentation: 6-12 days.
  - S4, production co-op integration and a real second-machine proof: 5-10
    days. This extends the edges of layer (b); it does not rewrite layer (b).
  - S5, owner evidence capture: 0.5-1 engineering day plus at least two
    calendar days, because the requirement itself asks for different days.

  SEVENTEEN ROWS:

  1. Double-click build, no Unity/console, repeat launch.
     VERDICT: NEEDS A FIX. Size: 2-4 days after an integrated gameplay scene
     exists; depends on S0/S2, a player-build entry point, packaging and a
     repeat-launch smoke check.
     TRUE-OF-SOLVER: no solver limit is involved. Build Settings enables only
     `Assets/Scenes/SampleScene.unity`, and that scene contains only Main
     Camera, Directional Light and Global Volume
     (`ProjectSettings/EditorBuildSettings.asset:8-9`;
     `Assets/Scenes/SampleScene.unity:135,271,388`). The product program says
     gas validators and character scenes remain separate and SampleScene is
     the sole default scene (`docs/gas-simulation/PROGRAM.md:169-177`). A
     repository-wide search found no BuildPipeline/BuildPlayer entry point.
     OLD-CONCEPT-PARAMETER: none; scene/build availability is not a cell-size,
     pocket-size, occupancy or step-rate question.

  2. Body walks, jumps, falls and stands on ground.
     VERDICT: NEEDS A FIX. Size: 3-6 days; depends on a deterministic body
     source, gravity/jump/ground collision, and the diggable world.
     TRUE-OF-SOLVER: no gas-solver limit. The body source calls itself a
     planar, single-machine, non-deterministic placeholder
     (`Assets/GasCoopGame/Adapters/Characters/InputBodyStateSource.cs:8-12`)
     and applies `new Vector3(move.x, 0f, move.y)`
     (`.../InputBodyStateSource.cs:60-65`). The prefab has a CapsuleCollider
     and that source (`.../PlayerCapsule.prefab:955,1051`) but no Rigidbody
     or CharacterController; the reaction API supplies only knockdown/get-up
     no-ops (`Assets/GasCoopGame/Characters/BodyReactions.cs:44-48,62-68`).
     OLD-CONCEPT-PARAMETER: none; this is gameplay-body work.

  3. Climb out by the same digging plus jump; no ready ladders/lifts.
     VERDICT: NEEDS A REWRITE OF LAYER (d), structure/topology. Layer (b),
     determinism-and-replication, is NOT implicated. Gross size: 25-45 days;
     marginal size: 2-4 days after S1/S2 for step geometry, grounding and
     climb acceptance.
     TRUE-OF-SOLVER: the coarse route permits only a PRE-DECLARED breachable
     surface (`Assets/GasCoopGame/Core/Field/Topology/Coarse/CoarseBreachLayer.cs:10,37-48`),
     while the voxel field can only wake an already-open face and rejects a
     closed/void face (`Assets/GasCoopGame/Core/Field/Voxel/VoxelField.cs:811-824`).
     Current authority calls for topology replacement and tick-stamped
     destruction (`docs/gas-simulation/PROGRAM.md:249-255`). Transport (a)
     and replication (b) remain reusable; the body still needs row 2.
     OLD-CONCEPT-PARAMETER: cell size and step rate change stair granularity,
     not the absence of runtime solid-to-open mutation.

  4. Death returns immediately at zero cost.
     VERDICT: NEEDS A FIX. Size: 1-2 days after rows 2 and 15; depends on an
     authoritative death trigger, spawn/reset semantics and a delay/cost knob.
     TRUE-OF-SOLVER: no solver limit. The character surface ends at
     knockdown/get-up (`BodyReactions.cs:44-48,62-68`), and a product search
     found no player death/health/respawn path.
     OLD-CONCEPT-PARAMETER: zero cost and immediate return are new gameplay
     settings, not inherited simulation limits.

  5. Every contested number is externally changeable without rebuilding;
     restart and compare.
     VERDICT: NEEDS A FIX. Size: 3-5 days; depends on the integrated build and
     a versioned runtime configuration surface with compare receipts.
     TRUE-OF-SOLVER: lab numbers are serialized fields, including continuous
     source, tick interval, steps per visual tick and two-type preview
     (`Assets/GasCoopGame/Adapters/GasView/VoxelSandboxDirector.cs:61,65,70,73`),
     but they are scene/Inspector controls. The legacy UI says the scene is
     Inspector-driven and draws no OnGUI controls
     (`Assets/GasCoopGame/Adapters/GasView/GasDemoPlumeControls.cs:347`).
     No built-player config/file/command-line loader consumes them.
     OLD-CONCEPT-PARAMETER: the 0.12-second tick, six steps, 25/50 cm default
     and source flags are old lab parameters. Editor editability does not
     satisfy reachability from a built player.

  6. Arbitrary digging where the player chooses; rock costs time.
     VERDICT: NEEDS A REWRITE OF LAYER (d), structure/topology. Layer (b) is
     NOT implicated. Gross size: 22-40 days; marginal size: 4-8 days after S1
     for targeting, material/time cost, collision projection and rejection.
     TRUE-OF-SOLVER: a gameplay-code search found no digging/excavation/mining/
     carve/backfill implementation. The coarse breach path is pre-declared
     (`.../CoarseBreachLayer.cs:10,37-48`), and the coarse solver is an
     interim tests-only tier scheduled for replacement
     (`Assets/GasCoopGame/Core/Field/Coarse/CoarseField.cs:1-3`). Dynamic
     structure is assigned to T1/X1 (`PROGRAM.md:249-255`).
     OLD-CONCEPT-PARAMETER: voxel resolution changes cost/fidelity; it cannot
     turn a pre-declared breach graph into arbitrary excavation.

  7. Value is below; players dig down and sideways.
     VERDICT: NEEDS A REWRITE OF LAYER (d), structure/topology. Layer (b) is
     NOT implicated. Gross size: 23-42 days; marginal size: 1-2 days after row
     6 for vertical targeting, gravity/collision and value placement.
     TRUE-OF-SOLVER: row 6's static topology limit applies, and the body source
     has no vertical input or gravity (`InputBodyStateSource.cs:60-65`).
     Transport (a) already works in a 3D lattice and is not the rewrite target.
     OLD-CONCEPT-PARAMETER: cell dimensions affect slope/step resolution only.

  8. Dug material is not put back.
     VERDICT: NEEDS A REWRITE OF LAYER (d), structure/topology. Layer (b) is
     NOT implicated. Gross size: 23-41 days; marginal size: 0.5-1 day after
     row 6 to make excavation monotonic and reject fill/backfill commands.
     TRUE-OF-SOLVER: no digging state exists today. Structural mutation and
     atomic failure semantics belong to T1/X1 (`PROGRAM.md:249-255`).
     OLD-CONCEPT-PARAMETER: none; no-backfill is a topology invariant.

  9. Breach is an event; wider cut is stronger; concrete behavior is a
     setting; first breach is not instant death.
     VERDICT: NEEDS A REWRITE OF LAYER (d), structure/topology. Layer (b) is
     NOT implicated; layer (a) is retained and layer (c) need not be replaced.
     Gross size: 30-54 days, the largest single-row gross price; marginal
     event/setting/death-cap work after S0/S1 is 3-6 days.
     TRUE-OF-SOLVER: graded aperture already ships. Structure projection uses
     open sub-face count as conductivity
     (`Assets/GasCoopGame/Core/Field/Structure/StructureGasProjection.cs:14-18`),
     and transport multiplies by it
     (`Assets/GasCoopGame/Core/Field/Voxel/VoxelField.cs:1545,1565-1568`).
     Runtime closed-to-open mutation does not ship: conductivity notification
     is wake-only and rejects non-open faces (`.../VoxelField.cs:811-824`).
     PROGRAM assigns dynamic conductivity to D1 and structural replacement to
     T1/X1 (`docs/gas-simulation/PROGRAM.md:237-255`). Non-lethal first breach
     also depends on row 15 and the row-5 rig.
     OLD-CONCEPT-PARAMETER: absolute seconds depend on cell size, tick interval,
     aperture and pocket size. Resolution is parameterized
     (`.../VoxelResolution.cs:20,46,87-90`) and wall-clock interval is an
     adapter field (`.../VoxelSandboxDirector.cs:65`). Wider-cut ordering is
     solver truth; a particular burst timescale is not.

  10. Substance motion obeys its law and never uses player position.
      VERDICT: SATISFIED TODAY. Size: 0 days for this invariant.
      TRUE-OF-SOLVER: gas Step has no actor-position input; PlayerSense is a
      downstream read. The contract test requires divergent actor positions to
      leave the gas meaning checksum identical while changing player digest
      (`tests/GasCoopGame.Core.Tests/Field/Sense/PlayerSenseTestContracts.cs:965-977`).
      The test was read, not run, under this CALL's boundary.
      OLD-CONCEPT-PARAMETER: tick rate, resolution and pocket dimensions affect
      speed/shape, not whether player position enters transport.

  11. No sinks; gas leaving a pocket remains in the workings.
      VERDICT: NEEDS A REWRITE OF LAYER (d), structure/topology. Layer (b) is
      NOT implicated; layer (a)'s fixed-grid mass transfer is retained. Gross
      size: 20-37 days; marginal size after S1: 2-5 days for the removed-cell
      gas policy, conservation checks and rejection/rollback proofs.
      TRUE-OF-SOLVER: within a fixed lattice transport moves bounded mass, but
      the public generation change publishes a complete replacement
      (`Assets/GasCoopGame/Core/Field/NearGas/NearGasSimulation.cs:55-95`)
      built from a new zero field plus initial mass/emitters
      (`.../NearGasSimulation.cs:225-236`); it does not migrate live gas.
      PROGRAM forbids silent reset and requires an explicit removed-cell policy
      (`docs/gas-simulation/PROGRAM.md:44,249-255`).
      OLD-CONCEPT-PARAMETER: the sandbox's default continuous source is an old
      scenario setting, not proof of a solver sink. With no emitters or
      consuming reactions, the missing truth is state-preserving topology.

  12. Total substance is finite and fixed before the build.
      VERDICT: NEEDS A FIX. Size: 0.5-1 day after the playable scenario exists;
      depends on finite initial masses, an empty emitter set and no consuming/
      producing reactions in the core scenario.
      TRUE-OF-SOLVER: generation owns immutable initial-mass and emitter lists
      (`Assets/GasCoopGame/Core/Field/NearGas/NearGasDefinition.cs:63-83,136-183`),
      and an emitter is ALWAYS-ON if present
      (`Assets/GasCoopGame/Core/Field/Sources/ContinuousGasEmitterSpec.cs:3-4`).
      A finite scenario therefore needs no layer rewrite.
      OLD-CONCEPT-PARAMETER: the sandbox requests a continuous source by
      default (`.../VoxelSandboxDirector.cs:61`). That is an old scenario
      default, not a solver constraint.

  13. Every pocket is enterable; only air cost differs; an empty pocket is
      safe; two kinds are visibly distinct.
      VERDICT: NEEDS A FIX. Size: 2-4 days after rows 11, 14 and 15; depends on
      two finite pure-pocket presets, two visible palettes, empty-pocket damage
      clearing and outsider readability.
      TRUE-OF-SOLVER: the render ABI stores density plus one dominant type per
      cell (`Assets/GasCoopGame/Render/Contracts/GridViewLayout.cs:4-9`), and
      the adapter exposes distinct primary/secondary colors
      (`Assets/GasCoopGame/Adapters/GasView/RealGasViewSource.cs:324-329`).
      That supports two separately seeded pocket kinds without rewriting render
      layer (c). A minority kind mixed into a dominant cell can be hidden, so
      the first proof must use pure pockets or add a separate cue.
      OLD-CONCEPT-PARAMETER: `twoTypePreview = false` is an adapter default
      (`.../VoxelSandboxDirector.cs:73`); the old twelve-kind envelope is
      irrelevant to a two-gas core.

  14. Rock reveals pocket presence and approximate size before cutting.
      VERDICT: NEEDS A FIX. Size: 3-6 days after layer (d); depends on
      authoritative pocket metadata/adjacency and a rock-facing cue with
      outsider legibility.
      TRUE-OF-SOLVER: the frozen gas texel exposes density, dominant type,
      front and warning only (`.../GridViewLayout.cs:4-9`), with no pre-cut
      pocket-size channel. This does not require render-layer (c) replacement:
      rock presentation can consume topology metadata outside the gas ABI.
      OLD-CONCEPT-PARAMETER: lookahead distance and granularity are row-5
      settings, not solver limits.

  15. Air is a counter; different kinds drain it at meaningfully different
      rates.
      VERDICT: NEEDS A FIX. Size: 1-3 days after body integration; depends on
      authoritative air state, per-kind rate settings, visible presentation
      and the row-4 death hook.
      TRUE-OF-SOLVER: PlayerSense returns per-actor, per-type exposure and dose
      (`Assets/GasCoopGame/Core/Field/Sense/PlayerSense.cs:141-155,330-345,482-499`).
      The only non-test consumer is a debug capsule printing exposure/dose in
      OnGUI (`Assets/GasCoopGame/Adapters/GasView/GasSenseCapsuleDebug.cs:106-107,560-564`),
      not a gameplay air counter.
      OLD-CONCEPT-PARAMETER: drain rates and their gap are new gameplay knobs;
      existing gas metadata or tick interval is not the design answer.

  16. Network foundation from the first line; start solo and on two machines.
      VERDICT: NEEDS A FIX. Size: 5-10 days after gameplay/topology commands are
      frozen; depends on command codecs, one coordinator, solo/host launch and
      a true second-machine built-player proof.
      TRUE-OF-SOLVER: layer (b) has an engine-free lockstep input seam and
      input-complete barrier (`Assets/GasCoopGame/Core/Sim/ITickInputBus.cs:6-15`)
      plus a FishNet reliable-ordered host relay
      (`Assets/GasCoopGame/Net/FishNet/FishNetTickInputBus.cs:12-15`) carrying
      actor poses (`.../FishNetTickInputBus.cs:91-101,249-264`). Source tests
      assert pose/dose convergence and true-host topology
      (`Assets/Tests/EditMode/Net/FishNetConvergenceTests.cs:176-260`), but
      were not run here. Net code has no gas/dig/topology integration, and
      PROGRAM says LAB/I3 is not production co-op and still needs a coordinator
      plus edge codecs (`docs/gas-simulation/PROGRAM.md:259-260`). Layer (b)
      is preserved and extended, not rewritten.
      OLD-CONCEPT-PARAMETER: none; peer topology and command coverage are
      contract/integration facts.

  17. Owner plays on different days and says keep/change/cut.
      VERDICT: NEEDS A FIX. Size: 0.5-1 engineering day plus at least two
      calendar days after rows 1-16; depends on repeatable build/config,
      captured run identity and two owner-play receipts.
      TRUE-OF-SOLVER: no solver limit. The only enabled build scene is the
      empty SampleScene (`ProjectSettings/EditorBuildSettings.asset:8-9`),
      while PROGRAM puts runnable integration proof at LAB/I3
      (`docs/gas-simulation/PROGRAM.md:256-260`). No current artifact can
      carry this evidence.
      OLD-CONCEPT-PARAMETER: none; this is an evidence lifecycle requirement.

evidence: |
  PRODUCT IDENTITY AND BOUNDARY:
  - Product repository: GasCoopGame.
  - Exact commit: `1a6373b84b6bf4da95a24efc3015e23b9ba5d419`.
  - Final read: `main...origin/main`, clean.
  - No product file was written; no branch/worktree was created; Unity, builds,
    tests and players were not run. Source assertions are static evidence, not
    fresh GREEN runtime evidence.

  ABSENCE SEARCH RECEIPTS AT THAT COMMIT:
  - no BuildPipeline/BuildPlayer/BuildTarget entry point across product C#,
    PowerShell, shell and CI YAML;
  - no gameplay digging/excavate/mining/carve/backfill implementation under
    `Assets/GasCoopGame/**/*.cs`;
  - no Gas/NearGas/VoxelField/PlayerSense/Dig/Topology/Character reference in
    Net and Core/Sim command integration;
  - no built-player config-file, StreamingAssets, PlayerPrefs or command-line
    consumer for contested sandbox settings;
  - no player death/respawn/health/air-counter gameplay path.

  FOUR REQUIRED FIRST-HAND RE-VERIFICATIONS:
  1. CONFIRMED - coarse breach accepts only pre-declared surfaces
     (`CoarseBreachLayer.cs:10,37-48`); it cannot express arbitrary digging.
  2. CONFIRMED - resolution is parameterized: constructor and integer-multiple
     validation are at `VoxelResolution.cs:20-46`; Default 25/50 and OneToOne
     50/50 are at `VoxelResolution.cs:87-90`. Defaults are old parameters.
  3. CONFIRMED - graded conductivity ships: open sub-face count is projected at
     `StructureGasProjection.cs:14-18`; transfer uses it at
     `VoxelField.cs:1545,1565-1568`.
  4. CONFIRMED AS SOURCE/TEST CONTRACT, NOT FRESHLY EXECUTED - per-actor/type
     exposure/dose exists at `PlayerSense.cs:141-155,330-345,482-499`; actor
     poses travel at `FishNetTickInputBus.cs:91-101,249-264`; byte-identity,
     dose and convergence assertions are at
     `PlayerSenseTestContracts.cs:965-977` and
     `FishNetConvergenceTests.cs:176-260`.

  ADDITIONAL V5/V6/V7 RECHECKS:
  - V5 confirmed: render stores one dominant type per cell
    (`GridViewLayout.cs:4-9`), while pure types can use distinct palettes
    (`RealGasViewSource.cs:324-329`).
  - V6 confirmed: SampleScene is the sole enabled empty default
    (`EditorBuildSettings.asset:8-9`; `SampleScene.unity:135,271,388`), with
    no build automation found.
  - V7 confirmed: body source is planar and single-machine
    (`InputBodyStateSource.cs:8-12,60-65`), with no jump/gravity controller.

confidence: |
  HIGH for repository identity, file/line observations, the four required
  re-verifications, the one satisfied invariant, the absent integrated venue,
  and the absent runtime solid-to-open mutation.

  MEDIUM-HIGH that all six rewrite verdicts implicate only layer (d). Current
  product authority itself names atomic topology replacement and tick-stamped
  destruction at T1/X1 while preserving transport/publication. A different
  approved architecture could move that boundary but cannot make today's
  static path satisfy the rows.

  LOW-MEDIUM for day ranges. They are dependency-structured sizes, not
  calibrated forecasts: no playable-core plan exists, no Unity run was
  allowed, and many PROGRAM milestones remain unstarted. The spread is wide
  and the direction forecast remains `no_basis`.

limits: |
  This check prices the approved two-gas core only. Liquid remains headroom and
  was not priced. It does not decide whether the engine stays, a layer is
  removed, a requirement is cut, or the concept changes.

  Nothing here is fresh runtime proof. A built integrated scene, R0 decisions
  for command order and removed-cell gas, completed T1/X1, and a real
  second-machine player run would tighten or overturn sizes. A changed
  owner-approved requirement set or replacement of PROGRAM authority requires
  a new check.

state_changes: |
  Against fresh `live/indie-game-development/NOW.md`:
  - set `updated` to `2026-07-28 by s-research-g-37a1-engine-fit-check-001`;
  - remove `open_calls[c-research-g-37a1-engine-fit-check-001]` only and
    preserve every other call;
  - add a CURRENT routing comment beside the issues heading that makes the
    remaining no-owner frontier `c-converge-g-37a1-core-rows-001` explicit;
  - replace the fourth `direction_forecast.drivers` entry's dispatched/open
    engine-check paragraph with a completed-result paragraph carrying the
    1/10/6/0 counts, layer-(d)-only rewrite result, 50-90-day deduplicated
    spread, named product commit and this history receipt; keep forecast status
    `no_basis`, target, basis, other drivers and update_when unchanged;
  - upsert issue `i-engine-fit-decision-ladder` without changing its owner
    ruling, issue text or route: set `review_when` to carry the completed
    matrix and say owner step 5 waits for the independently required step 3,
    and append this receipt plus product commit to `evidence`;
  - in decision `d-post-verify-route-001`, add a current `progress` field
    recording step 4 COMPLETE, step 2 still dispatched, step 3 still following
    step 2, and steps 5/6 still owner legs; preserve its historical note.
  Preserve CHARTER.md, TREE.md, tasks, recurring, all other issues, decisions
  and calls unchanged.

  Append the `log` line below once to `LOG.md` and save this complete RESULT
  as `history/2026-07-28-s-research-g-37a1-engine-fit-check-001.md`. Maintain
  all `END_OF_FILE` trailers.

captures:
  - At shape, price shared dependency slices S0-S5 rather than seventeen
    independent tasks; summing gross row prices double-counts topology/venue.
  - Row 9 is most expensive because it joins unfinished static gas, layer-(d)
    runtime replacement, the built-player rig and the air/death consumer.
  - Row 14 needs an authoritative topology read model for rock cues; it does
    not by itself require changing the frozen gas render ABI.

decisions_needed: []

play_check:
  - 1 Recite: done - one bounded question was restated as seventeen exact
    verdict rows, file/line evidence, named layers, sizes/dependencies and a
    two-minute roll-up inside one read-only session.
  - 2 Investigate: done - product main was inspected first-hand at exact commit
    `1a6373b84b6bf4da95a24efc3015e23b9ba5d419`; four prior findings and
    V5/V6/V7 were rechecked; no product mutation, build, Unity run, worktree,
    branch, test run or subagent occurred.
  - 3 Confidence: done - solver truths, old parameters, static evidence, sizing
    inference, confidence, limits and answer-changing evidence are separated;
    no UNKNOWN was needed.
  - 4 Close: done - all seventeen rows carry exactly one admitted verdict, all
    six rewrite rows name layer (d) and explicitly exclude layer (b), and this
    returns to `i-engine-fit-decision-ladder` without an engine-fate verdict.

log: 2026-07-28 | s-research-g-37a1-engine-fit-check-001 | research | direction | g-37a1/engine-fit-check: at product commit 1a6373b8 the seventeen engine-blind core requirements price as 1 satisfied today, 10 fixes, 6 rewrites of structure/topology layer (d), 0 impossible in co-op on Unity/C#; determinism/replication layer (b) is preserved, the deduplicated spread is 50-90 focused engineering days plus at least two owner-play calendar days, and breach behavior is the most expensive row; this is input to the owner's later ladder verdict, not that verdict. -> history/2026-07-28-s-research-g-37a1-engine-fit-check-001.md

next: |
  return-to-parent i-engine-fit-decision-ladder

roll_up: |
  SATISFIED TODAY: 1/17 (row 10).
  NEEDS A FIX: 10/17 (rows 1, 2, 4, 5, 12, 13, 14, 15, 16, 17).
  NEEDS A REWRITE: 6/17 (rows 3, 6, 7, 8, 9, 11), all and only layer (d),
  structure/topology; layer (b), determinism-and-replication, is NOT implicated.
  Layers (a) and (c) also receive no rewrite verdict.
  IMPOSSIBLE IN CO-OP ON UNITY AND C#: 0/17. UNKNOWN: 0/17.
  DEDUPLICATED TOTAL: 50-90 focused engineering days plus at least two calendar
  days for owner play on different days. This is a price spread, not a delivery
  forecast and not a sum of gross row estimates.
  MOST EXPENSIVE ROW: 9, breach behavior - 30-54 gross days because it crosses
  S0 static completion, S1 runtime topology, settings rig and air/death; its
  marginal work after shared prerequisites is 3-6 days.
  ENGINE FATE: deliberately not decided here.

END_OF_FILE: live/indie-game-development/history/2026-07-28-s-research-g-37a1-engine-fit-check-001.md
