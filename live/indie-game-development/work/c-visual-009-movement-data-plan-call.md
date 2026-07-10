# CALL c-visual-009 — Stage 3.5 Movement-Data Contract (PLAN ONLY)

> FIRE-READY 2026-07-10 after `c-visual-008` reached its frozen
> `stop-needs-new-data` branch. This is a fresh owner-present engineering PLAN,
> not a continuation of render tuning and not a BUILD session.

- direction: indie-game-development
- node: g-7e15 (VISUAL / GASG)
- play: work (executor PLAN leg — simulation-derived visual movement contract)
- repo: C:\projects\Unity\GasCoopGame_dev_2
- kind: engineering
- change_id: c-visual-009
- runs_in: a FRESH GasCoopGame PLAN session only; STOP after explicit owner approval and return to Direction OS before any BUILD
- planning_base: current `origin/main` at PLAN start; observed `origin/main@a644e5db` on 2026-07-10, while the existing `dev2@a48883b5` c-visual-008 plan branch was stale/diverged and held untracked closure evidence
- parent: s-work-066-c-visual-008-stop-route

## goal

An owner-approved frozen technical contract defines the smallest honest simulation-derived movement seam that lets the
existing gas body read as moving, and sequences the remaining half-resolution blur and dense-core repair without
opening Stage 4.

## context

- `c-visual-008` is terminal `STUCK / stop-needs-new-data`, not delivered. Its stronger render-only candidate made
  motion visible and smoother, but owner-eye read a solid dense center emitting moving wisps at the sides. Half-res
  blur remained. The owner stopped further shader curl/noise tuning rather than strengthen an independent fake flow.
- Primary handoff evidence in the product checkout:
  - `docs/results/c-visual-008.md`;
  - `docs/measurements/c-visual-008-render-evidence.md`;
  - `docs/measurements/c-visual-008-owner-eye-checklist.md`;
  - `docs/measurements/c-visual-008-owner-choices.md`;
  - frozen `openspec/changes/c-visual-008/**` and
    `docs/adr/ADR-V-0002-c-visual-008-stage35-render-polish.md`.
- At handoff, the rejected C#/renderer candidate had been removed. The tracked working-tree diff was empty, but the
  c-visual-008 RESULT, diagnostics/media and independent acceptance test were still untracked closure material; they
  are evidence, not a shippable candidate and not a clean-checkout claim.
- The delivered visual contract exposes current `GridView`, `GasParams`, type count, bounds and readiness through
  `IGasViewSource`. `GridView` remains `R=density`, `G=dominant type`, `B=front strength`, `A=warning`; it contains no
  signed movement direction. `GpuGasParams` remains the existing 128-byte ABI.
- Core already appears to expose signed per-face `Flux(cell, face, species)`. The PLAN must verify that fact and its
  semantics against current `origin/main`; it is a candidate source for a new read-only visual resource, not authority
  to add a second simulation law.
- Previous/current simulation-derived density plus tick identity may smooth discrete presentation. By itself it cannot
  claim directional flow, and a stationary unchanged density pair cannot explain internal body motion. Evidence
  therefore leans toward flux-derived movement for coherent directional body motion, with density history potentially
  complementary rather than a mutually exclusive substitute; the PLAN owns the final architecture decision.
- The half-res blur/upsample defect and dense-core shaping defect are render-only in principle and distinct from the
  missing movement-data seam. The PLAN must make their sequencing explicit rather than silently absorb them.
- Direction source: `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\gas-visual-plan-v2-2026-07-02.md`.

## scope

The frozen plan must choose and fully specify one honest movement contract after comparing:

1. previous/current simulation-derived density snapshots with tick identity and render interpolation, including the
   exact problem this can and cannot solve; and
2. a separate read-only visual movement resource derived from existing signed per-face flux, including whether density
   history/tick interpolation is also required for presentation continuity.

For the selected contract, the plan must make plain-language and technical decisions for source ownership, snapshot
lifetime, tick identity, buffering/interpolation, cell/face/species representation, bounds/resolution, stale or missing
data behavior, GPU upload/performance budget, lockstep/network implications, checksum boundary, and the rule preventing
render data from feeding back into simulation.

The plan must also decide whether half-res blur/upsample and dense-core shaping are:

- a separate render-only leg after the movement seam, or
- inseparable from the same BUILD, with specific evidence showing why coupling is necessary.

## boundaries

- PLAN ONLY: no product code, shader, renderer asset, scene, acceptance-test, BUILD, review or delivery edits.
- No new gas physics, solver law, velocity simulation, gameplay state, reaction, damage, Sc-sense or networking
  semantics.
- Do not repurpose `GridView.B`, change any GridView channel meaning, hide movement in an existing field, or extend
  `GpuGasParams` inside this plan. A separate resource may be specified, not built.
- No GPU/read-only visual feedback into Core, no render state in authoritative checksums, and no requirement to network
  cosmetic data independently when it can be derived locally from authoritative simulation state.
- Do not resume shader curl/noise tuning, blur repair, dense-core shaping, particles/VFX, full-res fallback or Stage 4.
- Do not call `c-visual-008` delivered, adopt its rejected candidate, or treat its unmatched-camera/stale-cost evidence
  as acceptance proof.
- Preserve and reconcile the untracked c-visual-008 closure evidence before changing checkout/branch state; do not
  silently delete it or carry its independent test into c-visual-009 as if newly authored.
- Current `origin/main` is authority. The PLAN must not assume `dev2@a48883b5` or the old `9d6f8ded`/`defade72` notes
  are the current integration base.
- The owner must approve the readable plan with actual words. A planner recommendation is not approval.

## done_when

- Current product base and actual current movement/view APIs are recorded from latest `origin/main`; the stale/diverged
  c-visual-008 plan branch and untracked evidence receive an explicit disposition.
- A detailed but simple owner-readable `c-visual-009` plan compares both candidate contracts on equal footing, selects
  one, states why it wins, and states whether density history is the solution, a complementary layer, or unnecessary.
- The selected seam specifies source semantics, ownership/lifetime, tick/frame coherence, representation, buffering,
  multi-species handling, performance/upload budget, deterministic/read-only boundaries, missing-data behavior and
  failure mode without inventing new physics or false flow.
- Acceptance properties can distinguish coherent movement of the gas body from moving detail over a solid center;
  evidence design includes same-regime live Unity/MCP traces and owner-eye A/B, source-to-visual direction honesty,
  onset continuity, boundary/placement honesty and measured cost.
- The plan gives an explicit yes/no sequencing decision for half-res upsample/blur and dense-core shaping, with rationale
  and separate acceptance boundaries if split. Any later change id remains Direction OS's responsibility.
- Owner approval words/token are recorded; owner-readable PLAN plus frozen spec/tasks/ADR artifacts exist under
  `c-visual-009` and contain no product/test/BUILD changes.
- The PLAN session stops and returns to Direction OS. No BUILD begins in the same session.

## return

Return the owner-approved PLAN handoff: current base SHA, selected movement contract and rejected alternative,
density-history role, blur/dense-core split verdict, artifact paths/commit, owner approval words/token, and proof that
no code/shader/scene/test BUILD work occurred. `c-visual-009` remains open; Direction OS assigns the later BUILD route
or revision.

## budget & rigor

One owner-present PLAN session. Detailed architecture and evidence design, zero BUILD. If current-main inspection
invalidates the handoff premise, STOP with the exact contradiction rather than normalizing it.

END_OF_FILE: live/indie-game-development/work/c-visual-009-movement-data-plan-call.md
