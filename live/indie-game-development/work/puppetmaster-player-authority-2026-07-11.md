# Research brief — PuppetMaster impact on the parallel player route (2026-07-11)

status: non-canonical research; no product BUILD, plugin import or Sc-damage work is authorized by this brief
direction: indie-game-development / g-9c41 / d-player-shell-parallel-001

## Bounded question

Does the owner's plan to rely heavily on procedural/physics animation through PuppetMaster change the conclusion that
a controller foundation can start safely in parallel with current P0/P1?

## Answer

Yes, it changes the **first slice**, but it does not remove technical parallelism. A production CharacterController,
collider/grounding/feel and actor-pose schema should no longer be frozen first. The quality-safe parallel start is a
disposable **P2a0 Puppet Authority Spike** that proves who owns player position across upright, hit, knockdown and
recovery states. Production player code follows only from that verdict.

PuppetMaster is not merely an Animator effect. It is an active PhysX ragdoll system: an animated/procedural Target rig
drives a physical Puppet made of Rigidbodies, ConfigurableJoints and colliders through muscles and pinning. It can
release pins on impact, enter `Puppet / Unpinned / GetUp`, apply force to individual muscles and, depending on
`canMoveTarget`, move the target root during physical recovery. It still needs a target pose source; it does not by
itself prove final locomotion animation or full physics locomotion.

## Established local facts

- `C:\Users\Anton\AppData\Roaming\Unity\Asset Store-5.x\RootMotion\ScriptingPhysics\PuppetMaster.unitypackage`
  exists (49,189,760 bytes). Its embedded ReadMe says version 1.4. It is not imported in current main/dev/dev2/core
  product worktrees; no current prefab, code or assembly depends on it.
- The current Asset Store release is 1.5 (2026-04-10) and lists Unity 6000.0/6000.4 compatibility. The product uses
  Unity 6000.3.17f1. Prefer refreshed 1.5; cached 1.4 is admissible only after an isolated compile/runtime proof.
- The cached package contains bundled humanoid/demo rigs, controllers, animations, impacts, get-up scenes and old
  Mirror/Photon/KCC/Starter Assets integrations. Those demos can test the authority mechanism before a final art rig
  exists, but cannot prove final collider fit, joint limits, mass, stride or feel.
- Cached 1.4 contains no `.asmdef`/`.asmref` or precompiled runtime DLL. Unity assemblies defined by asmdef cannot use
  types in predefined assemblies, so production packaging needs an explicit vendor-asmdef/default-assembly decision.
- PuppetMaster's normal setup separates controller and ragdoll layers and expects their mutual collisions disabled in
  the Physics Layer Collision Matrix. The current product has no such custom layers. Therefore the earlier
  `Player/** only; no ProjectSettings` claim is no longer proven. Runtime collision-ignore or another containment may
  avoid shared settings, but the spike/PLAN must decide rather than assume either result.
- PuppetMaster uses float PhysX forces and multiple muscle Rigidbodies. Fixed stepping improves reproducibility, but
  Unity documents additional challenges to true PhysX determinism. It cannot simply become the existing integer
  lockstep truth or be folded into the gas MeaningChecksum.
- The package's old Mirror demo is precedent, not reusable FishNet code: server controls lose-balance/get-up state;
  remote clients do local physics; rigidbody state is synchronized while the puppet is not fully pinned. FishNet still
  needs a fresh authority/prediction/reconcile decision.
- Current M1 explicitly tracks the player without damage and keeps Sc-damage HELD. A synthetic rock or point impulse
  may falsify physics architecture in the spike; it does not authorize gas explosion damage, health or incapacitation.

## First spike — bounded to one half-day

1. In a disposable, explicitly authorized lab venue, refresh PuppetMaster to 1.5 or prove cached 1.4 compiles and runs
   under Unity 6000.3. If import/assembly/layer setup consumes the timebox, checkpoint and split immediately.
2. Use a bundled demo humanoid, a minimal target locomotion, one Rigidbody rock and one scripted point impulse.
3. Prove the visible/state cycle `Puppet → Unpinned → GetUp` and record canonical root/position at every transition.
4. Compare only the two implementable root-handoff candidates A and B below.
5. Give full-time physics locomotion C a cheap feasibility/kill probe: run/inspect the vendor mechanism and list the
   custom actuation plus continuous network truth it would require. Do not build it inside this spike.
6. Return an authoritative-state inventory for A/B/C. No FishNet implementation and no claim that the inventory is the
   minimal network protocol.
7. No vendor or ProjectSettings merge, no product controller API, no final-rig tuning and no gameplay consequence.

## Authority candidates

| Candidate | Upright authority | Knockdown/recovery authority | What the spike learns | Main risk |
|---|---|---|---|---|
| A — proxy/cosmetic | Controller/capsule always | Controller/proxy state; puppet reacts visually | Whether hits read well without physical root handoff | Visual body and gameplay position can disagree |
| B — hybrid handoff | Controller while upright | Pelvis/puppet during `Unpinned/GetUp`, then explicit return | Whether root transfer is stable, camera-safe and recoverable | State/network handoff complexity |
| C — full active-ragdoll | Physical puppet/pelvis continuously | Same physical authority | Whether the owner-intended physics-led locomotion is even plausible | Custom locomotor, prediction/bandwidth and performance become a separate architecture |

Likely starting hypothesis, not a decision: B best matches «удар реально сбивает» while retaining ordinary responsive
locomotion; A is the cheaper fallback; C is kept alive only through the bounded kill-probe.

## What remains safe before the verdict

Only design-level concepts: raw device-neutral input intent (`move/look/buttons`), a generic control-enable gate and a
dynamic camera-target provider. Do not yet build or freeze desired acceleration/forces, grounding, capsule dimensions,
camera offsets/smoothing, Animator/Puppet API, quantized sensing volume or a network pose schema.

## Operational and governance gates

- The spike is technically independent of P0/P1 but still consumes product effort. Owner-present reconciliation must
  name the existing M1 leg that is folded/cut/reallocated; it cannot become a silent fourteenth leg.
- The dedicated lab/player venue needs an explicit exception, clean base, no UnityLockfile, version/seat check, compile
  baseline, RAM and MCP endpoint-identity smoke.
- A production merge is a later decision. Until the spike verdict, vendor files, assembly containment and local Physics
  settings remain disposable lab evidence only.

## Sources and confidence

Local primary artifact: cached PuppetMaster 1.4 package, especially embedded `DoxygenManualPuppetMaster.cs`,
`PuppetMaster.cs`, `BehaviourPuppet.cs`, `BehaviourPuppetDamage.cs` and the old Mirror `NetworkPuppet.cs` integration.

External primary sources:

- PuppetMaster current listing/version/compatibility: https://marketplace.unity.com/packages/tools/physics/puppetmaster-48977
- RootMotion FAQ (role, PhysX-only, performance, manual simulation):
  https://rootmotion.freshdesk.com/support/solutions/articles/77000057786-faq
- Unity assembly-definition boundary:
  https://docs.unity3d.com/es/2021.1/Manual/ScriptCompilationAssemblyDefinitionFiles.html
- Unity manual physics simulation/determinism limit:
  https://docs.unity3d.com/jp/current/Manual/physics-optimization-cpu-manual-simulation.html
- FishNet prediction/reconcile reference:
  https://fish-networking.gitbook.io/docs/guides/features/prediction/creating-code/controlling-an-object

Two substantive independent explorers plus first-hand parent inspection of the cached package converged on the same
root-authority, assembly and physics-layer hazards. Refutation round 1 exposed the missing full-time active-ragdoll
fork; round 2 exposed an overlarge locomotion+network spike; the final narrowed P2a0 scope survived three of three
same-family validators. These are in-session pre-passes, not a binding fresh-session G5.

## Owner choice

- **A — run P2a0 now (recommended):** disposable authority spike first; production controller only after its verdict;
  rig/animation research may continue in parallel.
- **B — controller first:** build code-driven controller now and integrate PuppetMaster later; highest rework risk.
- **C — wait:** postpone both until the sequential M1 player step and a final rig.

END_OF_FILE: live/indie-game-development/work/puppetmaster-player-authority-2026-07-11.md
