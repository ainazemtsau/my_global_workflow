RESULT s-canon-cargo-containment-principles-checkpoint-001 (call: c-canon-cargo-containment-principles-001)
direction: indie-game-development   play: local/canon-forge   node/task: g-d3a8/q-cargo-containment-principles
outcome: |
  Checkpoint produced for `q-cargo-containment-principles`.

  The question is framed and ready for owner direction, but canon is NOT frozen because local/canon-forge step 2 is an owner step:
  the owner must choose, mix, or steer one of the proposed directions before draft/freeze.

  Framed question:
  `q-cargo-containment-principles` asks how a captured gas state-window/sample-stake is held, leaks, spoils, stabilizes,
  releases, breaks, carries value, creates return pressure, and can be lost before safe return — without defining exact
  inventory UI, container stats, capacity numbers, equipment stats, prices, balance, exact carry verbs, co-op roles, floor loop,
  save/recovery implementation, or implementation architecture.

  Area:
  mechanic.

  Frozen inherited parents named:
  - `q-gas-value-forms`
  - `q-between-expeditions-progression`
  - `q-field-capture-principles`

  Required inherited facts carried forward:
  - `q-field-capture-principles`: field capture collects a bounded visible state-window/sample-stake, not raw volume; visible
    gas is collectible by default; regime follows current conditions; anti-vacuum lock = state-window over volume.
  - `q-gas-value-forms`: collected gas is not automatic loot; value depends on state/regime/stability/purity/push risk/
    containment/safe return; core chain = collect → read state → carry as-is or regime-push → stabilize/spoil/surge →
    return/lose → banked readiness.
  - `q-between-expeditions-progression`: value banks only after safe return; before return it can be lost, spoiled, released,
    broken, mixed wrongly, or not delivered.
  - `q-gas-role`: gas is one substrate; face/regime follows current conditions.
  - `q-base-logistics-labs-factories`: canisters/cassettes exist for samples/calibration/emergency isolation/delivery; raw
    gas is not the main product.
  - `q-coop-shape` remains deferred.
  - `q-expedition-loop` remains paused until `q-depth-grammar`, `q-coop-shape`, and `q-expedition-macrocycle` are complete.

  Owner-facing direction options checkpointed:

  A. `containment = readable state-window custody / preservation pressure`.
     Captured gas value is a readable state-window under custody. Containment asks whether the held state is preserved,
     pressured, leaking, spoiled, stabilized, deliberately released, broken, lost, or returned. The player reads why the
     state is degrading or holding: incompatible conditions, route stress, damage, over-push, bad mixing, time/pressure, or
     conscious release. Carrying gas is not busywork; it is a greed/fear decision about whether the state is worth protecting,
     pushing, dumping, or banking. Bad because: less visually dramatic than option C unless later legibility/visual nodes
     make it punchy. Recommendation: choose A, with a limited C-style return-pressure clause.

  B. `containment = industrial custody chain`.
     Captured gas value moves through a custody chain: capture, seal, isolate, transport, hand off, bank. Focus is on
     cassettes/canisters, seals, emergency isolation, calibration, lab delivery, and industrial believability. Bad because:
     this risks premature inventory/container taxonomy, procedural busywork, base logistics, and exact equipment stats.

  C. `containment = return antagonist`.
     The valuable captured state becomes a source of return pressure: it leaks, reacts with route conditions, threatens
     contamination, raises retreat tension, and turns “go home” into the second act of the find. Bad because: it can overstate
     every cargo item as a bespoke mini-boss, and can prematurely solve floor loop/co-op pressure.

  Recommended owner choice:
  A + constrained C:
  “containment is not container management; it is readable preservation pressure on an unbanked state-window.”

  Compact canon answer:
  Not frozen. Blocked by owner step 2. Candidate answer after owner approval should likely say:
  - captured gas value lives in a held state-window, not in generic volume or container stats;
  - containment is the readable lifecycle of that state-window before safe return;
  - valuable cargo can preserve, leak, spoil, stabilize, release, break, mix wrongly, surge, or be lost;
  - loss is caused by legible mismatch, damage, greed, route pressure, bad stabilization, bad release, or incompatible conditions,
    not arbitrary punishment;
  - carrying gas should create meaningful return pressure, not pure busywork;
  - deliberate release can be a valid tactical/greed/fear decision, not only failure;
  - safe return is the banking boundary;
  - exact UI, capacity, equipment, prices, balance, carry verbs, co-op roles, floor loop, save/recovery, and implementation remain
    deferred.

evidence: |
  Play/rules evidence:
  - `local/canon-forge` step 2 is explicitly `(owner)`: propose 3 directions; owner picks/mixes/steers; AI never freezes invented
    lore.
  - `local/canon-forge` step 6 is also `(owner)`: owner signs before frozen status.
  - Kernel G10 requires play_check to cover steps and owner steps to cite owner words or mark why skipped.

  Source evidence read:
  - Canon repo `questions/q-cargo-containment-principles.md`: status open; area mechanic; depends_on:
    `q-gas-value-forms`, `q-between-expeditions-progression`, `q-field-capture-principles`; question asks how captured gas result
    is held, carried, leaks, spoils, stabilizes, releases, or is lost before safe return without inventory UI/container stats/exact
    carry verbs/co-op solution.
  - Canon repo `questions/q-gas-value-forms.md`: frozen; visible gas can be collected; collected gas is not automatic loot; value
    depends on state/stability/purity/regime/return; raw gas is not the main product; central chain includes carry/stabilize/spoil/
    surge/return/lose/banked readiness.
  - Canon repo `questions/q-between-expeditions-progression.md`: frozen; before safe return captured gas/sample/result/data/cargo
    remains unbanked stake and can be lost/spoiled/released/broken/mixed wrongly/not delivered; safe return banks readiness.
  - Canon repo `questions/q-field-capture-principles.md`: frozen; capture takes a bounded state-window, not room volume; regime
    follows current conditions; capture does not finish value; open child `q-cargo-containment-principles` is explicitly the next
    question for how the captured state-window is held/leaks/spoils/stabilizes/releases/carries/gets lost.
  - `TREE.md` node `g-d3a8`: canon/design truth is a parked parallel canon track, not the active build bet; canon-forge works one
    question at a time and is not a second active bet.
  - `CHARTER.md` lenses applied at paper altitude: core gameplay depth, co-op-first, technical feasibility, scope/production, and
    anti-tech-demo pressure.

  Owner evidence from current CALL:
  - question: `q-cargo-containment-principles`
  - parent: `s-canon-field-capture-principles-001`
  - goal: owner wants an answer for how a captured gas state-window is held, leaks, spoils, stabilizes, releases, breaks, carries
    value, creates return pressure, and can be lost before safe return.
  - boundaries: do not define exact inventory UI, container stats, capacity numbers, equipment stats, prices, balance, exact carry
    verbs, exact tools, controls, room verbs, co-op roles, floor loop, expedition macrocycle, save/recovery implementation, or
    implementation architecture; do not make carrying gas pure busywork; do not make failure/loss arbitrary; do not solve
    `q-coop-shape`; do not treat `s-canon-015` inside-floor ideas as accepted mechanics.

state_changes: |
  Apply mechanically. This session did not edit either repo.

  1. Direction OS repo: append to `live/indie-game-development/LOG.md`:

     2026-06-27 — canon-forge CHECKPOINT (g-d3a8/q-cargo-containment-principles, s-canon-cargo-containment-principles-checkpoint-001): question framed as mechanic canon for how captured bounded gas state-window is held/leaks/spoils/stabilizes/releases/breaks/carries value/creates return pressure/can be lost before safe return. Inherited frozen parents named: q-gas-value-forms, q-between-expeditions-progression, q-field-capture-principles (+ q-gas-role/base-logistics facts). Step 2 owner choice is required before draft/freeze. Proposed directions: A containment as readable state-window custody/preservation pressure (RECOMMENDED, with limited return-pressure flavor), B industrial custody chain, C return antagonist. No canon repo changes; q-coop-shape remains deferred; q-expedition-loop remains paused until q-depth-grammar + q-coop-shape + q-expedition-macrocycle are complete. → history/s-canon-cargo-containment-principles-checkpoint-001.md

  2. Direction OS repo: create `live/indie-game-development/history/s-canon-cargo-containment-principles-checkpoint-001.md`
     containing this full RESULT.

  3. Direction OS repo: `NOW.md` untouched.

  4. Direction OS repo: `TREE.md` untouched.

  5. Direction OS repo: `CHARTER.md` untouched.

  6. Direction OS repo: `knowledge/` untouched.
     No cross-cutting knowledge promotion proposed from a checkpoint.

  7. Canon repo `C:\projects\gas_coop_game_canon`: no file changes.
     `questions/q-cargo-containment-principles.md` remains open until owner chooses direction and signs freeze.

captures:
  - Potential future child: `q-containment-state-language` — the readable labels/sensory language for preserved/leaking/spoiled/stabilized/released/broken states, without UI implementation.
  - Potential future child: `q-release-as-choice` — when deliberate release/dump/vent is a valid tactical decision rather than only failure, without exact verbs/tools.
  - Potential future child: `q-return-pressure-events` — broad categories of return pressure caused by valuable cargo, without floor loop or encounter tables.

decisions_needed:
  - q: Which containment direction should be drafted into canon for `q-cargo-containment-principles`?
    options:
      - A: containment as readable state-window custody / preservation pressure.
      - B: containment as industrial custody chain.
      - C: containment as return antagonist.
      - mix: A + constrained C.
    recommendation: Choose A + constrained C, because it preserves the inherited state-window/value/return canon, avoids inventory-stat busywork, and still gives cargo meaningful return pressure.

play_check:
  - 1 Frame: done — question framed; area named as mechanic; inherited frozen parents named: `q-gas-value-forms`, `q-between-expeditions-progression`, `q-field-capture-principles`; inherited facts from `q-gas-role` and `q-base-logistics-labs-factories` carried as constraints.
  - 2 Diverge (owner): blocked/checkpointed — 3 directions proposed; no owner pick yet. Owner words available from CALL set the task and boundaries but do not choose A/B/C: “how a captured gas state-window is held, leaks, spoils, stabilizes, releases, breaks, carries value, creates return pressure, and can be lost before safe return” and “Do not make carrying gas pure busywork. Do not make failure/loss arbitrary.”
  - 3 Draft: skipped — requires owner direction from step 2.
  - 4 Gate: skipped — requires a draft.
  - 5 Illustrate: skipped — structural mechanic-principle node; no image needed at checkpoint.
  - 6 Freeze & grow (owner): skipped — requires owner sign after draft/gate; no frozen canon emitted.

log: canon-forge checkpoint q-cargo-containment-principles: framed containment question and proposed A/B/C directions; awaiting owner choice; no canon freeze.

next: |
  awaiting_decision: choose direction for `q-cargo-containment-principles`.

  After owner chooses, run:

  CALL c-canon-cargo-containment-principles-002
  to: session
  direction: indie-game-development
  play: local/canon-forge
  node: g-d3a8
  question: q-cargo-containment-principles
  parent: s-canon-cargo-containment-principles-checkpoint-001
  surface: any / repo root `C:\my_global_workflow_worktrees\indie-game-development`

  goal: |
    Continue `q-cargo-containment-principles` from checkpoint after owner chose the containment direction. Draft, gate, and
    if owner signs, freeze a compact canon answer for how captured gas state-windows are held, leak, spoil, stabilize, release,
    break, carry value, create return pressure, and can be lost before safe return.

  context: |
    Read:
    - live/indie-game-development/history/s-canon-cargo-containment-principles-checkpoint-001.md
    - canon repo questions/q-cargo-containment-principles.md
    - frozen parents: q-gas-value-forms, q-between-expeditions-progression, q-field-capture-principles
    - inherited facts: q-gas-role, q-base-logistics-labs-factories
    Owner must provide one of:
    - A
    - B
    - C
    - A + constrained C
    - own mixed/edited direction

  boundaries: |
    Do not define exact inventory UI, container stats, capacity numbers, equipment stats, prices, balance, exact carry verbs,
    exact tools, controls, room verbs, co-op roles, floor loop, expedition macrocycle, save/recovery implementation, or
    implementation architecture.
    Do not make carrying gas pure busywork.
    Do not make failure/loss arbitrary.
    Do not solve `q-coop-shape`.
    Do not treat s-canon-015 inside-floor ideas as accepted mechanics.

  done_when: |
    A local/canon-forge result contains:
    1. owner-chosen direction with owner words cited;
    2. compact canon answer for `q-cargo-containment-principles`;
    3. craft gate result;
    4. child questions forced by the answer;
    5. explicit statement that `q-coop-shape` remains deferred;
    6. explicit statement that `q-expedition-loop` remains paused until `q-depth-grammar`, `q-coop-shape`, and
       `q-expedition-macrocycle` are complete;
    7. exact state_changes only through RESULT.

  return: |
    RESULT with owner evidence, canon answer/checkpoint, proposed child question graph, captures/decisions_needed, exact
    state_changes, and next CALL.

  budget: one session

END_OF_FILE: live/indie-game-development/history/s-canon-cargo-containment-principles-checkpoint-001.md
