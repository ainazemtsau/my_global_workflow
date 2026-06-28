# s-visual-005 — gas-VISUAL track (g-7e15): drift reconcile + look-development replan + process fix

date: 2026-06-28
play: research → reconcile + forward-replan (owner-initiated track review; KERNEL §2 / read-only-exception → owner «добро» to record)
node: g-7e15 (VISUAL parallel track — G1 intact, g-9c41 bet untouched)
owner-present: yes (chose A; said «добро»)

## Trigger

Owner: "хочу пообщаться про визуализацию … мы много задач выполнили и ничего не возвращалось/не записывалось … сначала меня всё устраивало, но сейчас как будто топчемся на месте, добавляются технологии, но всё блекло … возможно требований нет, нужно сначала пообщаться … посмотри сам проект (работа в GasCoopGame_dev_2)."

## What was found (investigation)

**Drift (verified first-hand).** OS recorded `c-visual-001` as `queued`/"owner starts it when he chooses" and the only
visual history was planning/research (s-visual-001..004, s-research-gas-visual-tech-001). In reality the leg was BUILT
foundation→S1(smoke-bomb, owner-approved)→S3(per-type colour + warning edge)→S5(real-data swap) and merged to
GasCoopGame **origin/main three times**; S6 (look-development) is a pushed WIP on dev2. The ENGINE track came home as
RESULTs every leg (s-work-019/023/026) — the visual track never did. That asymmetry IS the drift; it is the source of
the owner's "топчемся вслепую / ничего не записывалось".

- git first-hand: origin/main tip `2e24a24`; `merge-base --is-ancestor 9780713 origin/main` = YES
  (`9780713` = "Merge dev2 into main: c-visual-001 S5 — RealGasViewSource real-data swap"); dev2 tip `dc4c225`
  ("c-visual-001 S6 WIP (checkpoint, NOT delivered)"), pushed on origin/dev2. OS repo clean @7516016.
- S5 delivery evidence (`GasCoopGame_dev_2/RESULT.md`, read first-hand): -Deliver inner GREEN 1022/1022, mutation 76%
  ≥70, independent spec-only test-author (39 RED), 6-lens adversarial review, ZERO `Core/**` edit (977 sim tests
  unchanged), owner-eye SIGNED 2026-06-28 «облако читается хорошо, верится что это газ». ADRs 0012/0013/0014/0015.

**Plateau (diagnosed).** ~half = the drift above (work invisible to governance). ~half = only ~3 of ~10 look levers are
built and the BOX sandbox mis-leads the eye — NOT the visual ceiling. Live-confirmed (read-only `script-execute` +
`screenshot-game-view`): the Unity editor the owner had open was the **engine** worktree `GasCoopGame_dev`'s debug
sandbox — `VoxelSandboxDirector` voxel cubes + yellow jet cells + wind arrows, `gasSource=False` — **not the gas visual
at all**. The gas visual (volumetric `GasUber` raymarch body, `RealGasViewSource`, the 4-concept `GasConceptPresets`
switcher) lives in dev2. The owner's instinct ("the scene interferes with evaluation") is correct.

**Root cause of the plateau (process).** g-7e15's done_when is a spectacle+menace bar, but the only per-slice gate was
LEGIBILITY ("colour=type, denser=more opaque, a visible edge") — a flat, technically-correct blob passes it. There was
no aesthetic TARGET and no "does it move toward great-looking gas" gate, so tech accreted while the look stalled. The
sibling tracks (canon-forge / marketing-forge) both diverge on a felt direction the owner picks, then gate on CRAFT —
the two pieces the visual track skipped.

Diagnosis workflow: `wf_bb4f7ebd-1bf` (3 agents — shader-look-audit + drift-ledger + process-gap), corroborated by the
live read-only Unity inspection.

## Owner decision

Chose **A** (visual-direction-first) + «добро» to record. Felt TARGET (references-for-a-feeling, NOT a spec): gas = the
game's HEART/JEWEL → especially cool/unique; each TYPE has its own CHARACTER (noise/motion/light, not just colour),
tunable to its state; low-poly = the WORLD, not a cap on the gas. The dev-side forward plan
(`GasCoopGame docs/gas-visual-stage-plan.md §S6+`: gas-lab open-space FIRST → P1 levers → per-type character + optional
particle accents, «Feel» plugin candidate) is adopted as the official forward plan.

## RESULT

```
RESULT
session: s-visual-005
direction: indie-game-development
play: research → reconcile + forward-replan
node: g-7e15 (VISUAL parallel track — G1 intact, g-9c41 bet untouched)

outcome: |
  The gas-VISUAL track was diagnosed and BROUGHT HOME after ~2 days of off-contour drift; its process was fixed.
  - DRIFT (verified first-hand): OS recorded c-visual-001 as "queued/not started" while the leg was actually BUILT
    foundation→S1→S3→S5 and merged to GasCoopGame origin/main (S5 @9780713, ancestor of main tip 2e24a24); S6 look-dev
    is a pushed WIP on dev2 (@dc4c225, NOT merged). Zero build RESULTs had come home; the engine track came home every
    leg — the asymmetry is the drift.
  - PLATEAU diagnosis (owner «топчемся/блекло»): ~half DRIFT + ~half only ~3 of ~10 look levers built + the BOX sandbox
    mis-leads the eye — NOT the ceiling. Live-confirmed the open editor was the ENGINE worktree debug cubes, not the gas
    visual (which lives in dev2).
  - Owner chose A (visual-direction-first) + «добро». Felt TARGET captured: gas = the game's HEART/JEWEL → especially
    cool/unique; each TYPE has its own CHARACTER (noise/motion/light, not just colour), tunable to its state; low-poly =
    the WORLD, not a cap on the gas.

evidence: |
  - git first-hand: origin/main tip 2e24a24; merge-base --is-ancestor 9780713 origin/main = YES; dev2 tip dc4c225
    "S6 WIP (NOT delivered)", pushed.
  - S5 delivery (GasCoopGame_dev_2/RESULT.md, first-hand): -Deliver GREEN 1022/1022, mutation 76% ≥70, independent
    spec-only test-author (39 RED), 6-lens adversarial review, ZERO Core/** edit (977 sim tests unchanged), owner-eye
    SIGNED 2026-06-28. ADRs 0012/0013/0014/0015.
  - Forward plan durable: GasCoopGame docs/gas-visual-stage-plan.md §S6+ (gas-lab → P1 levers → character/particles;
    «Feel» candidate; ~3/10 levers used). Diagnosis workflow wf_bb4f7ebd-1bf + live read-only Unity inspection.

state_changes: |
  NOW.md: c-visual-001 status queued→DELIVERED (+ S6-WIP record); g-7e15.next reset STRUCTURE-FIRST→LOOK-DEVELOPMENT
  (felt TARGET + gas-lab→P1-levers→character forward plan via the dev stage-plan doc + the PROCESS FIX: slices come
  HOME + a 2nd owner-eye «moves toward the JEWEL» axis + the off-contour DECISIONS); writer-notes VISUAL line + PUSH
  list updated. LOG.md append. history/s-visual-005.md saved. NO TREE/CHARTER change (G9 not triggered); G1 intact.

captures:
  - Status enum has no 'track' value for parallel tracks — recurring friction; maintenance candidate.
  - Per-type CHARACTER as DATA needs reserved 96B GpuGasParams fields OR a layout-ADR — surface at the character slice.
  - Engine debug sandbox (dev: VoxelSandboxDirector cubes) vs gas VISUAL (dev2: RealGasViewSource + GasConceptPresets)
    are different scenes in different worktrees — don't confuse engine forced-flow cubes for the gas visual.
  - "Come home + aesthetic gate" generalizing to a kernel/play change = maintenance (≥2 FRICTION; kept track-level now).

decisions_needed: []   # owner chose A + «добро»; gas-lab micro-decisions are next-leg PLAN decisions.

play_check:
  - Recite — restated the owner's concern (visual drift + plateau; review/replan the process): DONE.
  - Investigate — OS state + live read-only Unity + dev2 code/plan/git + RESULT.md + a 3-agent diagnosis workflow: DONE
    (resolved from research into reconcile + forward-replan once drift confirmed + owner approved recording).
  - Confidence — established (drift + S5 merge verified first-hand) separated from proposal (the aesthetic gate +
    forward plan = owner-endorsed, not yet built): DONE.
  - Close — RESULT brings the track home + forward replan + process fix + captures + next CALL: DONE.
    (owner) owner chose A and said «добро» — his actual words.

log: research→reconcile (g-7e15 VISUAL): brought the off-contour visual track HOME — c-visual-001 queued→DELIVERED
  (S5 in origin/main @9780713, S6 WIP dev2 @dc4c225, verified first-hand); diagnosed «топчемся» = half drift + half only
  ~3/10 look levers + box scene (NOT the ceiling); owner chose A + «добро»; recorded felt TARGET (gas=jewel,
  character-per-type), the gas-lab→P1-levers→character forward plan (spec = GasCoopGame docs/gas-visual-stage-plan.md
  §S6+), and a PROCESS fix (come-home + «moves toward the JEWEL» owner-eye gate).

next:
  call: c-visual-002
  goal: The gas's LOOK is developed toward the JEWEL target — in a dedicated open-space gas-lab the gas reads as a wow,
    non-default volumetric cloud the owner signs as clearly moving toward «особенно круто», box-scene artifacts gone.
  context: GasCoopGame docs/gas-visual-stage-plan.md §S6+; delivered seam/body ADR-0012/13/14/15; S6 WIP dev2 @dc4c225;
    felt target + process fix in NOW g-7e15.
  boundaries: render-only (R13 — zero Core/** edit; sim untouched, 977 tests green); LOOK-FIRST (perf S4 deferred);
    per-type CHARACTER + particle accents (Feel) = a LATER leg; gas-spread stages later; 96B layout frozen.
  done_when: opens with a PLAN (owner present); a gas-lab open-space scene exists; the P1 levers build incrementally;
    owner-eye signs «двигает к жемчужине» alongside the green stride/seam headless checks; the RESULT comes HOME.
  return: a RESULT routed home (status + evidence + owner-eye aesthetic sign + the next look slice).
  budget: ~40–60 min/day owner-gated build-gaps; a fresh GasCoopGame_dev_2 session.
END_OF_RESULT
```

END_OF_FILE: live/indie-game-development/history/s-visual-005.md
