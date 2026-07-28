# RESULT — s-shape-g-37a1-core-bet-001

play: shape · node: g-37a1 · direction: indie-game-development · date: 2026-07-28

Step 6 of the owner's six-step route — the last one — is closed. `g-37a1` becomes the active bet.

---

## What the owner decided, in his own words

**Appetite.** «я бы поставил пока то, что мы до 10 августа. Но мы делаем столько ног, сколько надо» ·
«давай до 10 как пессимистичный срок» · «если мы не сделаем то, что мы определили до 10 августа,
качественно, то значит, у нас что-то проблемы с процессами». He also withdrew his own earlier
one-leg-per-day figure as a guess: «Это я с потолка сказал».

**Lanes.** «WIP =5» · «приоритет я буду отдавать сначала симуляции топологии» · «остальные в таком
фоновом режиме… если не буду занят симуляцией топологии, буду смотреть другие» · «Ты не знаешь, что
буду пять запускать, я буду смотреть по загруженности».

**Camera.** «Делаем по умолчанию первое. Ну, типа теоретически, может потом на третье перенесём…
я сейчас бы пока взял, чтобы не распыляться, как первое лицо, тем более на бумаге мы сильно не
проверим удобность этого.» Reason for a possible later move, recorded as a design fact rather than
hesitation: procedural animation, and falling in particular, may read better from third person.

**Purchase threshold** (replacing this leg's own empty phrase «невероятный профит»): «если там даже
150 долларов, если нам это экономит… что-то около недели, то уже стоит того… под невероятным имеется
в виду, что если это закрывает какую-то фичу, да, и нам не надо это делать.»

**On the coarse tier:** «если он не участвует в функционале, то вырезать, естественно.»

**Approval:** «Да» on the exact bet screen.

---

## What this leg found, and it came out of his objections rather than out of analysis

**1. The product has two gas tiers and one of them is dead.** `Core/Field/Coarse/CoarseField.cs:1-3`:
«INTERIM far-tier — scheduled for DELETION/replacement at S4 … build new gas behaviour on the NEAR
tier … **No runtime consumer** since c-exec-013 ZERO-LEGACY; tests only.» The only implemented breach
mechanic, `Topology/Coarse/CoarseBreachLayer.cs`, materialises a **PRE-DECLARED breachable surface**
(`PortalIsBreachable`) — literally the authored panel he struck in criterion 2 — and it lives in that
dead tier. **So there is no breach mechanic to fight.** The live tier holds only a wake hook,
`VoxelField.NotifyConductivityChanged`, whose own comment says «the breach mechanic itself is NOT built
here (S5); only the hook is», and which rejects a closed face because a closed face has no entry in the
open-face index. Consequence: a cut this leg had priced as painful costs nothing.

**2. The genuinely live and unsolved item is much narrower — region identity.** Every cell carries a
region whose stable id is **geometry-derived**, and those ids are folded into the meaning checksum two
machines compare (`VoxelField.cs:903-923`). Continuous digging merges and splits regions every few
seconds, so «stable id derived from geometry» is not stable, and the co-op comparison rests on it.

**3. Chunk addressing is a condition of interactive digging today, not a hedge for a future big world.**
Changing the world means deriving a new immutable structure and remapping mass onto it; the only
existing path publishes a complete replacement built from a new ZERO field
(`NearGas/NearGasSimulation.cs:55-95,225-236`) — the reset. A flat array over the whole section rebuilds
the world on every cut. Chunk addressing appears in none of the eight seams, which were all written for
one small fixed section.

**4. Two of this leg's own claims were wrong and he refuted both first.** Voxel Play 4 is a CUBIC
Minecraft-style engine with chunks, meshes and colliders; `Surface Nets` is an optional visual smoothing
that leaves the logical voxel data untouched. The false «smoothed-voxel» claim came from our own state
file, which had folded chat 3's PROPOSAL to hide cubicity into a property of the plugin; both copies are
corrected in place, and the money recommendation built on it is withdrawn. And
`docs/gas-simulation/PROGRAM.md` is DOWNGRADED from binding plan to evidence of the old concept: its D1
speaks of «door openness» and its T1 migrates the whole grid with scratch for old and candidate copies
at once — right for a rare structural event in a static factory, wrong for a game whose core verb
removes cells continuously.

**What did NOT move.** Branch 2 is confirmed rather than reopened: transport, conductivity as the count
of open sub-faces, integer determinism and the mass/structure split are all real, all read first-hand
and all preserved. No requirement line, no criterion and no closed ruling was touched.

**A process failure he caught.** He asked whether the three-task ceiling was a defect blocking parallel
work. It was, in both halves — and two maintenance legs had already fixed both the same day
(`3d796c41` makes `shape` OFFER lanes and their WIP limit; `07355aa9` makes the number the owner's).
The MAINTENANCE REQUEST this leg had drafted is therefore moot and is not raised.

---

```
RESULT
session: s-shape-g-37a1-core-bet-001
play: shape
node: g-37a1
outcome: checkpoint=false; the node is shaped and becomes the active bet on the owner's exact-text approval

evidence:
  - owner_approval: "Да" on the exact bet screen (appetite to 2026-08-10; five lanes; four ready calls plus blocked co-op; cut list; lens verdicts; kill_by)
  - owner_words_appetite: "я бы поставил пока то, что мы до 10 августа. Но мы делаем столько ног, сколько надо" / "давай до 10 как пессимистичный срок" / "если мы не сделаем то, что мы определили до 10 августа, качественно, то значит, у нас что-то проблемы с процессами"
  - owner_words_lanes: "WIP =5" / "приоритет я буду отдавать сначала симуляции топологии" / "остальные в таком фоновом режиме"
  - owner_words_camera: "Делаем по умолчанию первое... я сейчас бы пока взял, чтобы не распыляться, как первое лицо, тем более на бумаге мы сильно не проверим удобность этого"
  - owner_words_purchase_threshold: "если там даже 150 долларов, если нам это экономит, ну, условно, там что-то около недели, то уже стоит того... под невероятным имеется в виду, что если это закрывает какую-то фичу, да, то есть, и нам не надо это делать"
  - owner_words_coarse: "если он не участвует в функционале, то вырезать, естественно"
  - first_hand_product_read (read-only, commit 1a6373b8):
      Core/Field/Coarse/CoarseField.cs:1-3 — "INTERIM far-tier - scheduled for DELETION/replacement at S4 ... build new gas behaviour on the NEAR tier ... No runtime consumer since c-exec-013 ZERO-LEGACY; tests only."
      Core/Field/Topology/Coarse/CoarseBreachLayer.cs:33-50 — breach requires a PRE-DECLARED breachable surface (PortalIsBreachable); the authored-panel breach the owner rejected, living in the dead tier
      Core/Field/Voxel/VoxelField.cs:806-824 — NotifyConductivityChanged is a WAKE-ONLY hook touching no mass; "the breach mechanic itself is NOT built here (S5); only the hook is"; a closed face is REJECTED
      Core/Field/Voxel/VoxelField.cs:903-923 — region stable ids are geometry-derived and are folded into the meaning checksum
      Core/Field/Voxel/CellGrid.cs:7-14,20-31 — the grid is the immutable STRUCTURE; mass state lives separately in VoxelField
      Core/Field/Structure/StructureGasProjection.cs:18 — conductivity = COUNT of open sub-faces (requirements line 9 already physically present)
      Core/Field/NearGas/NearGasSimulation.cs:55-95,225-236 — the only existing world-change path publishes a complete replacement from a new ZERO field
      docs/gas-simulation/PROGRAM.md:237-256 — D1 "door openness", T1 whole-grid migration: old-concept framing, DOWNGRADED to evidence
  - concept material: work/concept-chats-answers-g-37a1.md:754-789 — Voxel Play 4 is cubic with chunks/meshes/colliders; Surface Nets is an OPTIONAL visual smoothing that does not change logical voxel data; refutes NOW.md's "the smoothed-voxel one"
  - os maintenance already landed: 3d796c41 (shape must offer lanes and their owner-set WIP limit), 07355aa9 (the WIP number is the owner's, not a hard-coded three)

state_changes:
  TREE.md:
    - g-37a1: status parked -> active; appetite and kill_by added; goal, all fifteen done_when criteria and why UNCHANGED
    - owner_approved: shape approval entry appended, quoting his words
  NOW.md:
    - updated: 2026-07-28 by s-shape-g-37a1-core-bet-001
    - bet: null -> the g-37a1 bet (goal, appetite, kill_by with threshold + date + next_if_true/false, forecast, against, cut_list, lens_verdicts for all six CHARTER lenses)
    - tasks: [] -> t-1..t-5 (t-5 blocked with unblock_when)
    - track_wip_limit: 5; tracks: t-sim, t-body, t-venue, t-render, t-coop
    - open_calls: five lane roots added (four ready, t-coop blocked)
    - issues: i-core-topology-live-vs-dead-tier-001 added
    - decisions: d-core-geometry-and-view-001 open half ANSWERED (first person); d-topology-backend-purchase-001 added (open, track t-render, his own threshold)
    - direction_forecast: one driver added; status stays no_basis
    - the "smoothed-voxel" claim corrected in place in both of its homes
  LOG.md: one line appended (newest first)
  history/2026-07-28-s-shape-g-37a1-core-bet-001.md: this file
  work/: five CALL files, each self-contained with absolute product paths

captures:
  - NOW.md hygiene: direction_forecast.drivers is 7 against a schema max of 4, and open_calls retains done/cancelled entries by an earlier deliberate decision; together they make the file ~81k tokens. Not this leg's job; route via a later review or repair.
  - Licence fact for anyone reading references while building topology: qhdwight/voxelfield is GPL-3.0 and unusable as a source for a paid product; jedjoud10/VoxelTerrain states no licence at all.
  - The owner asked to CUT CHARTER lens 3 ("реально ли одному разработчику") and questioned lens 4 ("новый одобренный канон"). Both are CHARTER and belong to `frame`. This leg argued for reformulation rather than deletion and routed it; nothing was changed here.

decisions_needed: []

play_check:
  G1: one active bet; five active tasks against the owner-set WIP limit of 5; one ordinary root per lane
  G3: appetite fixed BEFORE any solution talk, in his own words, and never extended
  G4: done_when from the card; kill_by carries a threshold AND a date, with next_if_true / next_if_false stated
  G6: cut list has real cuts, one of which genuinely hurts (eighteen of twenty knobs leave the running game); a verdict for every one of CHARTER's six lenses, none skipped; the riskiest assumption gets the first call in the priority lane
  G7: the money question is left OPEN with his own threshold as its acceptance rule, not decided by the leg
  G9: TREE change on his exact-text "Да"; the fifteen criteria and the sixteen requirement lines are untouched
  step_3_approaches: three structurally different approaches were generated and ranked on equal footing (own grid + generated colliders; Voxel Play 4 as the world; own grid with grid-sampling collision and no generated colliders). The owner's own brought approach (buy Voxel Play 4) was NOT privileged; it survives as the render backend candidate and is settled by t-4 on his threshold.
  note: d-october-route-charter and d-air-counter-visibility-001 stay untracked deliberately — the first is frame-level and outside the bet, the second is explicitly outside the core and off the critical path

log: g-37a1 is the active bet - appetite to 10 August, five lanes at WIP 5, and the coarse tier turns out to be dead code so there is no breach mechanic to fight, only one to build

next: c-work-g-37a1-topology-boundary-001 (lane t-sim, his priority) - plus c-exec-g-37a1-body-first-person-001, c-exec-g-37a1-venue-packaged-player-001 and c-work-g-37a1-render-backend-decision-001 dispatchable in parallel; c-exec-g-37a1-coop-two-machines-001 blocked on the dig-command contract
```

END_OF_FILE: live/indie-game-development/history/2026-07-28-s-shape-g-37a1-core-bet-001.md
