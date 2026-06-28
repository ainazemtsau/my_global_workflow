RESULT s-canon-cargo-containment-principles-002 (call: c-canon-cargo-containment-principles-002)
direction: indie-game-development   play: local/canon-forge   node/task: g-d3a8/q-cargo-containment-principles
outcome: |
  `q-cargo-containment-principles` is frozen in the canon repo.

  Owner direction and sign:
  - Step 2 choice: "я выбираю A + constrained C"
  - Step 6 freeze sign: "Морозь как есть"

  Canon answer:
  containment is readable custody / preservation pressure on an unbanked captured state-window, not container management.
  Captured value can preserve, pressure, leak, spoil, stabilize, release, break, or be lost before safe return. Loss must
  be legible and attributable; deliberate release can be correct play; valuable cargo creates constrained return pressure,
  but not every cargo item becomes a bespoke mini-boss.

  Explicit deferrals:
  exact inventory UI, container stats, capacity numbers, equipment stats, prices, balance, carry verbs, exact tools,
  controls, room verbs, co-op roles, floor loop, expedition macrocycle, save/recovery implementation, and implementation
  architecture remain deferred.

  Child graph:
  - new `q-release-as-choice` spawned;
  - existing `q-cargo-containment` linked downstream for concrete carry/container/co-op/macrocycle work;
  - existing `q-field-legibility` linked to containment-state reads;
  - existing `q-expedition-macrocycle` linked to return-pressure / safe-return banking boundary;
  - existing `q-coop-shape` linked to containment substrate while remaining deferred.

  `q-coop-shape` remains deferred. `q-expedition-loop` remains paused until `q-depth-grammar`, `q-coop-shape`, and
  `q-expedition-macrocycle` are complete; `q-depth-grammar` is complete, `q-coop-shape` and `q-expedition-macrocycle`
  remain incomplete.

evidence: |
  Owner evidence:
  - Step 2 owner words: "я выбираю A + constrained C"
  - Step 6 owner words: "Морозь как есть"

  Canon repo evidence:
  - Repo: `C:\projects\gas_coop_game_canon`
  - Commit: `2498005 canon: freeze cargo containment principles`
  - Frozen card: `questions/q-cargo-containment-principles.md`
  - New child question: `questions/q-release-as-choice.md`
  - Linked open questions: `questions/q-cargo-containment.md`, `questions/q-field-legibility.md`,
    `questions/q-expedition-macrocycle.md`, `questions/q-coop-shape.md`
  - MOC updated: `maps/World.md`

  Gate evidence:
  - Parent consistency: passes `q-gas-value-forms`, `q-between-expeditions-progression`, and
    `q-field-capture-principles`.
  - Mechanic paper gate: grows from shared gas field + field capture + safe-return banking; creates a non-dominant
    carry/stabilize/push/release/return decision family; pulls toward greed/fear-together; requires field-readable loss.
  - Anti-solo: not certified here; hard co-op remains explicitly deferred to `q-coop-shape`.
  - Fun: not certified; grey-box two-player test not run. Card is paper-clean / UNVERIFIED, not fun-certified.

state_changes: |
  Apply mechanically. Canon repo changes are already committed locally in `C:\projects\gas_coop_game_canon` at `2498005`.

  1. Direction OS repo: append to `live/indie-game-development/LOG.md`:

     2026-06-28 — canon-forge frozen (g-d3a8/q-cargo-containment-principles, s-canon-cargo-containment-principles-002): owner chose A + constrained C and signed "Морозь как есть". Frozen canon: containment = readable custody/preservation pressure on an unbanked captured state-window, not container management; captured value can preserve/pressure/leak/spoil/stabilize/release/break/get lost before safe return; loss must be legible; deliberate release can be correct play; valuable cargo creates constrained return pressure, not a bespoke mini-boss. Exact UI/capacity/container stats/carry verbs/co-op/floor loop/macrocycle/save/recovery/implementation deferred. Canon repo commit 2498005; spawned q-release-as-choice; linked q-cargo-containment, q-field-legibility, q-expedition-macrocycle, q-coop-shape. q-coop-shape remains deferred; q-expedition-loop remains paused until q-depth-grammar + q-coop-shape + q-expedition-macrocycle are complete. → history/s-canon-cargo-containment-principles-002.md

  2. Direction OS repo: create `live/indie-game-development/history/s-canon-cargo-containment-principles-002.md`
     containing this full RESULT.

  3. Direction OS repo: `NOW.md` untouched.

  4. Direction OS repo: `TREE.md` untouched.

  5. Direction OS repo: `CHARTER.md` untouched.

  6. Direction OS repo: `knowledge/` untouched.
     No cross-cutting knowledge promotion proposed; the canon card is the source for downstream canon questions.

  7. Canon repo `C:\projects\gas_coop_game_canon`: committed local change `2498005 canon: freeze cargo containment principles`.
     Changed files: `questions/q-cargo-containment-principles.md`, `questions/q-release-as-choice.md`,
     `questions/q-cargo-containment.md`, `questions/q-field-legibility.md`, `questions/q-expedition-macrocycle.md`,
     `questions/q-coop-shape.md`, `maps/World.md`.

captures:
  - Future after macrocycle/floor-loop shape: `q-return-pressure-events` — categories of return pressure caused by valuable cargo, without event tables now.
  - `q-containment-state-language` was not spawned as a separate child; route through `q-field-legibility` first to avoid duplicate legibility nodes.

decisions_needed: []

play_check:
  - 1 Frame: done — exact question inherited from checkpoint; parents carried: `q-gas-value-forms`, `q-between-expeditions-progression`, `q-field-capture-principles`; area mechanic.
  - 2 Diverge (owner): done — owner chose "я выбираю A + constrained C".
  - 3 Draft: done — compact canon answer written as invariants + prose; exact UI/container/carry/co-op/macrocycle/implementation left deferred.
  - 4 Gate: done — paper mechanic gate clean; anti-solo and grey-box fun explicitly not certified here.
  - 5 Illustrate: skipped — structural mechanic-principle card; no image needed.
  - 6 Freeze & grow (owner): done — owner signed "Морозь как есть"; status frozen in canon repo commit `2498005`; child graph grown.

log: 2026-06-28 — canon-forge frozen q-cargo-containment-principles: A + constrained C signed; containment = readable state-window custody / preservation pressure; canon repo commit 2498005; next q-coop-shape.

next: |
  CALL c-canon-coop-shape-001
  to: session
  direction: indie-game-development
  play: local/canon-forge
  node: g-d3a8
  question: q-coop-shape
  parent: s-canon-cargo-containment-principles-002
  surface: any / repo root `C:\my_global_workflow_worktrees\indie-game-development`

  goal: |
    A frozen canon answer exists for how gas, captured value, containment, return pressure, depth readiness, rescue/failure,
    and shared field consequences create structural co-op interdependence rather than solo-with-friends.

  context: |
    Read:
    - canon repo `questions/q-coop-shape.md`
    - frozen parents: `q-north-star`, `q-gas-role`, `q-the-city`, `q-full-game-descent-arc`,
      `q-between-expeditions-progression`, `q-depth-grammar`, `q-cargo-containment-principles`
    - `live/indie-game-development/knowledge/mechanic-lenses.md`

    Required inherited facts:
    - North Star: co-op-first, not solo-completable by design; "risked it and pulled it out together".
    - Gas role: effects are non-local; greed/risk is tied through the shared field.
    - Between expeditions: value banks only after safe return; full-team wipe without prepared recovery can collapse campaign.
    - Depth grammar: readiness includes return discipline, containment, recovery, route/protocol/team competence.
    - Cargo containment: captured value creates readable return pressure; deliberate release can be correct; exact carry UI,
      container stats, floor loop and implementation remain deferred.

  boundaries: |
    Do not solve exact floor loop, expedition macrocycle, inventory UI, carry controls, container stats, equipment stats,
    prices, balance, save/recovery implementation, or implementation architecture.
    Do not make co-op a declared vibe; it must be structurally not solo-with-friends.
    Do not import `s-canon-015` inside-floor placeholders as accepted mechanics.
    Do not certify fun without a later two-player grey-box.

  done_when: |
    A local/canon-forge RESULT contains:
    1. owner-chosen direction with owner words cited;
    2. compact canon answer for `q-coop-shape`;
    3. mechanic craft gate result, including anti-solo refutation status;
    4. child questions forced by the answer;
    5. explicit statement that `q-expedition-loop` remains paused unless `q-expedition-macrocycle` is also complete;
    6. exact state_changes only through RESULT.

  return: |
    RESULT with owner evidence, canon answer/checkpoint, proposed child question graph, captures/decisions_needed, exact
    state_changes, and next CALL.

  budget: one session

END_OF_FILE: live/indie-game-development/history/s-canon-cargo-containment-principles-002.md
