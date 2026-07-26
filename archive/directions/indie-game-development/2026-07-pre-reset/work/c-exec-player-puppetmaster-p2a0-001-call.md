# CALL c-exec-player-puppetmaster-p2a0-001 — PuppetMaster authority suitability spike

> ⚠️ contract: drift-unknown — C:\projects\Unity\GasCoopGame validation.config was not readable from this
> Direction-bound session. Current OS engineering contract = v19. Executor reads the stamp first and runs §Re-sync
> before any lab mutation when synced_contract_version < 19.

to: executor
direction: indie-game-development
kind: engineering
repo: C:\projects\Unity\GasCoopGame
node: g-9c41
task: M1-P2a0
goal: |
  Для сетевого игрока с физическими ударами существует доказанный и отрефутированный verdict о пригодности
  PuppetMaster и о том, кто владеет gameplay-позицией в upright, hit, knockdown и recovery; production controller
  не заморожен до этого verdict.
context: |
  Owner chose route A on 2026-07-11: «В принципе, согласен», then explicitly asked the workflow to lead and to
  account for multiplayer constraints. Read first:
  C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\puppetmaster-player-authority-2026-07-11.md
  and work/player-puppetmaster-p2a0-start-2026-07-11.md in the same direction folder.

  Established inputs, to verify rather than assume: cached PuppetMaster 1.4 exists; current researched release is
  1.5; product Unity is 6000.3.17f1; plugin is not imported in current product branches; cached package has no asmdef;
  standard setup expects separate controller/ragdoll collision layers; PhysX is not the integer lockstep truth.
  Candidate A keeps controller/root authoritative and puppet cosmetic. Candidate B hands authority from controller
  upright to pelvis/puppet while Unpinned/GetUp and back explicitly. Candidate C keeps the physical puppet authoritative
  full-time and receives only a bounded feasibility/kill probe.

  This spike is charged to the existing M1-5 player-tracking leg. It is not a fourteenth product leg. The current
  rolling-wave task M1-GAS-PROBE is deferred from the three-slot window, not cancelled.
boundaries: |
  Disposable evidence only: no production controller API, final collider/grounding/camera feel, final art rig tuning,
  gas or explosion consequence, health/incapacitation, FishNet implementation, full bone replication, Core/** edit,
  vendor/settings merge or main/dev/dev2 mutation. Do not claim cross-peer PhysX determinism. A synthetic Rigidbody
  rock or point impulse is architecture evidence, not Sc-damage authorization.

  Unity-MCP is mandatory where capable. If Unity/MCP, Asset Store entitlement, plugin refresh, editor identity or lab
  opening needs the owner, STOP early and return one click-by-click owner action; no workaround. If import, compile,
  assembly containment or layer setup consumes the half-day, return a checkpoint instead of shrinking the proof.
done_when: |
  1. Preflight records fresh origin/main, contract-version status, worktree list, clean disposable lab assignment,
     no UnityLockfile/competing editor, RAM/MCP endpoint identity, plugin version/seat and a green baseline. Create
     C:\projects\Unity\GasCoopGame_lab on branch lab from the launch base only if absent and safe.
  2. PuppetMaster 1.5 compiles/runs on Unity 6000.3, or cached 1.4 has an explicit compile/runtime proof and limitations;
     vendor/default-assembly versus asmdef containment and collision-layer strategy are recorded, not silently merged.
  3. A bundled humanoid plus minimal target locomotion visibly completes Puppet → Unpinned → GetUp under one rock and
     one scripted point impulse. Evidence records target root, controller/capsule root and pelvis position/owner at every
     transition, with two short comparable clips or equivalent frame-by-frame capture.
  4. Candidate A and B are both exercised. Candidate C receives a cheap feasibility/kill probe only. The report states
     for each: gameplay root owner by state, handoff/correction rule, camera/collider consequence, failure mode and an
     explicit keep/cut verdict.
  5. Multiplayer suitability matrix states, for A/B/C, what must be host/server authoritative; what may be predicted or
     locally simulated; the minimum candidate state inventory for remote peers; correction/teleport/get-up hazards;
     bandwidth/performance risk; and whether a separate two-peer FishNet proof is mandatory. It does not pretend this
     inventory is the final minimal protocol.
  6. A decision brief recommends A, B, C or PuppetMaster rejection for this game, names falsifiers and names exactly one
     next bounded proof. If B or C survives, production controller stays blocked until a separate two-peer authority
     proof. A fresh independent G5/refutation attempts to break the recorded mechanism and network inference.
  7. Lab compile/smoke checks and evidence are committed only on the disposable lab branch. RESULT routes home with no
     product merge request and no claim that player controller, networking or damage is delivered.
return: |
  RESULT with preflight facts, exact plugin/Unity versions, lab commit, transition table, A/B/C matrix, clips/captures,
  multiplayer authority inventory, fresh-refutation verdict, recommendation and the one next bounded proof. State
  every owner action separately. Never author the next CALL in the product repo.
budget: <= half-day; checkpoint immediately if setup consumes the proof budget

launch:
  lane: C
  venue: C:\projects\Unity\GasCoopGame_lab (branch lab, Unity editor 3; create only after preflight)
  machine: PC
  base: origin/main @a644e5db538d1102f726630d6a4ac2f3f1bdcf5a; re-sync required, moved tip means record/reconcile first
  conflict_surface: disposable lab scene, vendor import/assembly containment and local collision setup only; no Core/product merge
  depends_on: []
  merge_queue: none — evidence branch is disposable
  gates: fresh independent G5 on the spike inference; owner-eye is a later batched A/B/C verdict over two short clips

END_OF_FILE: live/indie-game-development/work/c-exec-player-puppetmaster-p2a0-001-call.md
