# History — PuppetMaster impact on the parallel player route

session: s-research-player-shell-puppetmaster-003 (Codex; play: research; checkpoint awaiting owner route)
direction: indie-game-development / g-9c41 / d-player-shell-parallel-001

## Owner summary

PuppetMaster существенно меняет порядок, но не отменяет параллельность. Production-контроллер больше не является
безопасным первым BUILD: active ragdoll может владеть root при падении/подъёме, а setup затрагивает physical rig,
assembly boundary и collision layers. Рекомендуемый первый ход — disposable ≤half-day P2a0 authority-spike в lab;
controller, сеть и sensing-pose замораживаются только после verdict. BUILD ждёт owner-вариант А и named appetite fold.

```text
RESULT s-research-player-shell-puppetmaster-003 (call: owner-plain-player-shell-puppetmaster-2026-07-11)
direction: indie-game-development   play: research   node/task: g-9c41/d-player-shell-parallel-001
outcome: |
  CHECKPOINT / RECOMMENDATION REVISED, PRODUCT BUILD NOT AUTHORIZED. PuppetMaster materially changes the first safe
  player slice but not its technical independence from current P0/P1. A production CharacterController/collider/
  grounding/feel and sensing-pose schema should not be frozen before active-ragdoll root authority is tested. The
  recommended parallel start is now a disposable <=half-day P2a0 Puppet Authority Spike; production controller,
  networking and gameplay consequences follow only from its verdict.
evidence: |
  Local primary evidence: `C:\Users\Anton\AppData\Roaming\Unity\Asset Store-5.x\RootMotion\ScriptingPhysics\
  PuppetMaster.unitypackage` exists (49,189,760 bytes), embedded ReadMe = 1.4, but PuppetMaster/RootMotion/FinalIK is
  absent from current GasCoopGame main/dev/dev2/core. The current Asset Store release is 1.5 (2026-04-10; Unity 6000.x
  compatible). Embedded vendor source/manual shows a dual animated Target + physical Puppet rig; muscle Rigidbody/
  ConfigurableJoint pinning; `Puppet/Unpinned/GetUp`; collision and scripted AddForceAtPosition; and `canMoveTarget`,
  which allows targetRoot movement during physical recovery. Cached 1.4 has no asmdef/asmref or runtime DLL, while its
  default setup expects controller/ragdoll layers with mutual collision disabled. The old bundled Mirror demo makes
  lose-balance/get-up server authoritative and syncs rigidbody state while unpinned; it is precedent, not FishNet code.
  Current TickInput carries only an integer actor AABB, not knockdown/root/bone state; NOW/M1 keep Sc-damage HELD.
  Primary web sources: https://marketplace.unity.com/packages/tools/physics/puppetmaster-48977 ;
  https://rootmotion.freshdesk.com/support/solutions/articles/77000057786-faq ;
  https://docs.unity3d.com/es/2021.1/Manual/ScriptCompilationAssemblyDefinitionFiles.html ;
  https://docs.unity3d.com/jp/current/Manual/physics-optimization-cpu-manual-simulation.html ;
  https://fish-networking.gitbook.io/docs/guides/features/prediction/creating-code/controlling-an-object .
  Two substantive independent explorers plus first-hand parent package inspection converged. Refutation round 1 found
  the missing full-time active-ragdoll fork; round 2 rejected an overlarge locomotion+network spike; the final narrowed
  P2a0 scope survived 3/3 same-family validators. These are non-binding in-session pre-passes, not fresh-session G5.
state_changes: |
  ADD live/indie-game-development/work/puppetmaster-player-authority-2026-07-11.md as the non-canonical research brief.
  PATCH live/indie-game-development/work/player-shell-parallelization-2026-07-11.md with a supersession pointer to the
  PuppetMaster research brief.
  live/indie-game-development/NOW.md: set updated to `2026-07-11 by s-research-player-shell-puppetmaster-003`; UPSERT
  pending decision d-player-shell-parallel-001 to the revised A/B/C options below; preserve bet, appetite, tasks,
  open_calls, all other decisions, recurring and primary next exactly as fresh current state.
  live/indie-game-development/LOG.md: append exactly the `log:` line below once.
  Save this full RESULT once at
  live/indie-game-development/history/2026-07-11-s-research-player-shell-puppetmaster-003.md.
  Regenerate the d-player-shell-parallel-001 card and today's journal in
  live/indie-game-development/work/board/dashboard.html from the revised decision and log.
  No CHARTER.md, TREE.md, task status, open_call, NOW.next or product-repo change.
captures:
  - P2a0 timebox: import/compile current PuppetMaster in disposable lab; bundled demo rig; synthetic rock/point
    impulse; prove Puppet->Unpinned->GetUp; compare controller-root-always versus upright-controller/knockdown-pelvis.
  - Full-time active-ragdoll locomotion remains a live owner-intent candidate, but P2a0 gives it only a feasibility/
    kill probe; any survivor becomes separately shaped work rather than hidden controller scope.
  - P2a0 returns only a candidate authoritative-state inventory for controller/proxy, hybrid handoff and full physics;
    it implements no FishNet and does not claim a minimal network protocol.
  - Before verdict, only design-level raw input intent, generic control-enable and dynamic camera-target concepts remain;
    no production controller, collider/grounding/feel, Animator/Puppet API or sensing-volume schema is frozen.
  - Cached PuppetMaster is 1.4 while current is 1.5; cached package has no asmdef and standard setup expects physics
    layers/matrix. Version/seat, assembly containment and settings strategy are explicit preflight/PLAN questions.
  - Synthetic impact is architecture evidence only. Sc-damage, gas explosion/debris damage, health and incapacitation
    remain HELD and require their own later owner-shaped consequence contract.
decisions_needed:
  - q: d-player-shell-parallel-001 — should PuppetMaster authority be probed before any production controller BUILD?
    options: ["A: run the disposable <=half-day P2a0 Puppet Authority Spike now; production controller waits for its verdict while rig/animation research may continue in parallel", "B: build the code-driven controller first and integrate PuppetMaster later", "C: wait for the sequential M1 player step and final rig"]
    recommendation: "A. It preserves real P0/P1 parallelism while testing the now load-bearing root-authority risk before creating production rework. Reconciliation must name the existing M1 leg being folded/cut and authorize the lab/version/license/assembly/physics preflight."
play_check:
  - 1 Recite: done — one bounded question, return = whether PuppetMaster changes the parallel route and the smallest quality-safe first slice, budget = one research session.
  - 2 Investigate: done — inspected current state, prior controller brief, cached PuppetMaster archive/source/demos/integrations, product import/settings facts and current RootMotion/Unity/FishNet primary docs; ran independent explorers and three refutation rounds.
  - 3 Confidence: done — established plugin/import/source constraints were separated from architecture inference; two successful refutations were folded into a final half-day-fit spike that survived 3/3 validators.
  - 4 Close: done as checkpoint — owner decision remains pending; no task/CALL/plugin import/BUILD/Sc-damage or product change opened; Phase 0 remains primary next.
log: 2026-07-11 — research/checkpoint (g-9c41/player-shell+PuppetMaster, s-research-player-shell-puppetmaster-003): PuppetMaster 1.4 найден в cache, в product не импортирован; active-ragdoll root authority ломает controller-first/new-files-only premise, поэтому рекомендуемый parallel start заменён на ≤half-day disposable P2a0 authority spike (A↔B handoff + C kill-probe), без network/damage/merge; ждёт owner «А», named 13-leg fold и lab-preflight. → history/2026-07-11-s-research-player-shell-puppetmaster-003.md
next: |
  awaiting_decision d-player-shell-parallel-001; primary direction next remains
  work/c-exec-lv-ingest-phase0-call.md. If the owner answers A / «запускаем PuppetMaster-spike», a fresh owner-present
  shape/repair-style reconciliation must explicitly name the displaced/folded M1 leg, authorize the disposable venue
  and preflight, then issue one half-day P2a0 executor CALL; no product BUILD starts from this checkpoint.
```

END_OF_FILE: live/indie-game-development/history/2026-07-11-s-research-player-shell-puppetmaster-003.md
