# History — player controller parallel refinement

session: s-research-player-shell-parallel-002 (Codex; play: research; checkpoint awaiting owner route)
direction: indie-game-development / g-9c41 / d-player-shell-parallel-001

## Owner summary

Технически контроллер действительно можно вынести вперёд, но не как «готового анимированного сетевого игрока».
Честный параллельный кусок — code-driven Controller Foundation в новом subtree; выбор реального rig+clips идёт
отдельным research. Конкретный Animator и вся network/Sc-sense интеграция остаются после выбора ассета и authority.
BUILD не открыт: нужен owner-вариант А, явная арифметика 13 легов и проверенная lab-площадка.

```text
RESULT s-research-player-shell-parallel-002 (call: owner-plain-player-controller-parallel-2026-07-11)
direction: indie-game-development   play: research   node/task: g-9c41/d-player-shell-parallel-001
outcome: |
  CHECKPOINT / RECOMMENDATION REFINED, PRODUCT BUILD NOT AUTHORIZED. The owner's narrower premise is technically
  sound: a code-driven Controller Foundation can likely run in parallel with current P0/P1 on a strictly isolated
  new-files-only surface. A complete animated multiplayer player cannot. The quality-preserving route separates a
  formal P2a local controller/motor from parallel read-only selection of the actual licensed rig and locomotion clips;
  concrete Humanoid/Animator contracts wait for that asset evidence, and multiplayer/live integration remains P2b.
evidence: |
  Direction authority: NOW.md has a fixed 13-leg appetite, three current rolling-wave tasks, no Player task/CALL and
  the pending d-player-shell-parallel-001 decision; the M1 shape already gives player tracking a natural M1-5 home.
  Product evidence from three independent read-only inspections: Input System 1.19.0 is installed and active, but the
  project has no product humanoid FBX/Avatar, .anim, Animator Controller or .inputactions asset; TickInput carries only
  an optional integer actor footprint and FishNetTickInput broadcasts are explicitly not a NetworkObject/prediction
  player entity. CharacterController.Move accepts an explicit motion delta constrained by collision, while Unity root
  motion applies clip-derived displacement to the GameObject; FishNet prediction requires ownership plus
  replicate/reconcile and is therefore a later authority decision. Primary sources:
  https://docs.unity3d.com/jp/current/ScriptReference/CharacterController.Move.html ;
  https://docs.unity3d.com/kr/current/ScriptReference/Animator-applyRootMotion.html ;
  https://fish-networking.gitbook.io/docs/guides/features/prediction/creating-code/controlling-an-object .
  Nominal group: 3/3 explorers found the same no-assets / local-controller-only boundary. Final same-family refutation:
  isolated controller feasibility survived 2/3 and was INCONCLUSIVE 1/3 pending exact manifest/preflight; the concrete
  early Animator contract was REFUTED/narrowed, leaving only an asset-neutral motor-state + GraphicsRoot socket;
  multiplayer exclusions survived 3/3; governance survived but exact 13-leg fold/cut/reallocation remains unresolved.
  These are non-binding in-session pre-passes, not a binding fresh-session G5.
state_changes: |
  PATCH live/indie-game-development/work/player-shell-parallelization-2026-07-11.md with the owner's narrowed premise,
  the Controller Foundation versus rig-selection split, the animation/authority exclusions and refined A/B/C choice.
  live/indie-game-development/NOW.md: set updated to `2026-07-11 by s-research-player-shell-parallel-002`; UPSERT
  pending decision d-player-shell-parallel-001 to the refined A/B/C options below; preserve the bet, appetite, tasks,
  open_calls, all other decisions, recurring and primary next exactly as fresh current state.
  live/indie-game-development/LOG.md: append exactly the `log:` line below once.
  Save this full RESULT once at
  live/indie-game-development/history/2026-07-11-s-research-player-shell-parallel-002.md.
  Regenerate the d-player-shell-parallel-001 card and today's journal in
  live/indie-game-development/work/board/dashboard.html from the refined decision and log.
  No CHARTER.md, TREE.md, task status, open_call, NOW.next or product-repo change.
captures:
  - Candidate P2a surface: code-driven CharacterController capsule, walk/look/camera/grounding, immutable input-command
    snapshot, injectable local-control gate, asset-neutral motor-state, quantized pose output, own prefab/vacuum scene/tests.
  - P2a hot exclusions: Core, Net, SimInstance, GasView, Topology, Packages, ProjectSettings and every existing scene;
    exact manifest and fresh active-diff comparison remain dispatch gates, not assumed facts.
  - Animation asset work can run independently now as read-only selection/licensing/import research; no Animator
    parameter names, blend tree, Humanoid offsets or final feel are frozen before a real rig+clips pass the import proof.
  - P2b retains FishNet ownership/prediction/reconcile, spawn, real-level collision, Sc-sense/SimInstance wiring and
    two-machine evidence; P2a must never claim deterministic or multiplayer-ready.
  - Exact appetite arithmetic is unresolved: the owner-present reconciliation must name which existing M1 leg is
    folded, cut or reallocated; "not a fourteenth leg" alone is insufficient.
decisions_needed:
  - q: d-player-shell-parallel-001 — should the narrow controller foundation start in parallel now?
    options: ["A: bring a formal P2a Controller Foundation forward inside current M1 and run rig/animation asset selection separately in parallel; no BUILD before reconciliation and a ready CALL", "B: run only rig/animation asset selection now and keep controller BUILD sequential", "C: wait for the sequential M1 player-tracking step"]
    recommendation: "A. It captures real technical parallelism without pretending the absent rig, animation or network authority is done. The reconciliation must explicitly solve the 13-leg fold/cut/reallocation, exact manifest and lab exception/preflight."
play_check:
  - 1 Recite: done — one bounded refinement question, return = quality/parallelism verdict and exact boundary, budget = one read-only research session.
  - 2 Investigate: done — re-read current state and prior brief, checked product assets/packages/code/venues through three independent explorers, checked current Unity/FishNet primary docs, then ran a three-validator refutation pass.
  - 3 Confidence: done — established no-assets/input/pose facts were separated from inferred controller feasibility; the Animator overclaim was removed and manifest/appetite/venue limits remain explicit.
  - 4 Close: done as checkpoint — refined owner decision remains pending, no task/CALL/BUILD opened, and Phase 0 remains the primary direction next.
log: 2026-07-11 — research/checkpoint (g-9c41/player-shell-parallel, s-research-player-shell-parallel-002): owner-уточнение разделило честный параллельный P2a Controller Foundation от преждевременной animation/network интеграции: code-driven capsule/input/pose можно вынести в новый subtree, а rig+clips сначала выбираются отдельным research; BUILD ждёт owner «А», арифметику 13 легов и lab-preflight. → history/2026-07-11-s-research-player-shell-parallel-002.md
next: |
  awaiting_decision d-player-shell-parallel-001; primary direction next remains
  work/c-exec-lv-ingest-phase0-call.md. If the owner answers A / «запускаем», a fresh owner-present shape/repair-style
  reconciliation must explicitly resolve leg arithmetic, exact manifest and venue preflight, then issue a fire-ready
  P2a executor CALL; product BUILD does not start from this checkpoint.
```

END_OF_FILE: live/indie-game-development/history/2026-07-11-s-research-player-shell-parallel-002.md
