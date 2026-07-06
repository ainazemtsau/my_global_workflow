CALL c-design-lab-gas-interaction-gameplay-001
to: session
direction: indie-game-development
play: local/design-lab
node: g-d3a8
surface: any / repo root `C:\my_global_workflow_worktrees\indie-game-development`

goal: |
  Explore gas interaction as playable gameplay before any canon-forge freeze.

  The session should determine which playable gas interaction situations, if any, prove that gas is the core gameplay system before cargo/containment continues.

  The result may be:
  - ready canon-forge CALL;
  - blocker CALL;
  - map repair CALL;
  - parent reopen CALL;
  - visual check CALL;
  - grey-box/prototype CALL;
  - checkpoint with captures only.

context: |
  Read:
  - live/indie-game-development/plays/design-lab.md
  - live/indie-game-development/work/canon-maps/gas-interaction-map.md
  - live/indie-game-development/work/design-labs/_template.md
  - live/indie-game-development/knowledge/mechanic-lenses.md

  Also read canon repo / canon files as needed:
  - questions/q-gas-role.md
  - questions/q-gas-value-forms.md
  - questions/q-field-capture-principles.md
  - questions/q-cargo-containment-principles.md
  - questions/q-floor-board-kernel.md
  - questions/q-floor-loop.md
  - questions/q-floor-gas-work-verbs.md
  - questions/q-field-legibility.md
  - questions/q-regime-push-rules.md
  - questions/q-cargo-containment.md
  - questions/q-return-liability-pressure-model.md
  - questions/q-two-player-floor-greybox-proof.md
  - maps/World.md

  Process locks:
  - Do not use hardcoded counts.
  - Do not freeze canon directly from MAP.
  - Use owner-facing plain language first.
  - Every term must translate into gameplay: player wants / sees / does / risks / changes.
  - If blocker appears, stop and route to blocker.
  - If old parent canon appears technically coherent but bad for gameplay, route to parent reopen/repair.

  Parent design locks:
  - Gas is structured field, not uniform fog.
  - Gas physically spreads through simulation; sources/leaks/vents/jets/flows matter.
  - Gas can have anomalous/flagship forms, but no true agency/creature-AI by default unless canon is explicitly reopened.
  - Reactions must use finite outcome grammar, not N² table.
  - Visible gas can be collected, but value is state-window over raw volume.
  - Cargo is unbanked custody until safe return.
  - Paper canon does not certify fun.

boundaries: |
  Do not freeze gas canon in this Design Lab session unless the route explicitly produces a separate canon-forge CALL.
  Do not solve exact gas roster, exact gas families, exact reaction table, exact damage numbers, exact downed/revive rules, exact destruction model, exact container stats, exact tools, exact controls, economy, balance, implementation, final VFX, or grey-box verdict.
  Do not write abstract labels as results.
  Do not answer with fixed-count anchor cases.
  Do not make cargo/containment the center.
  Do not make anomaly into creature AI.
  Do not hide behind technical prose.

done_when: |
  One Design Lab work result exists with:
  - central question in plain language;
  - relevant map slice;
  - current understanding in owner-readable language;
  - explored playable situations or models;
  - failed/rejected directions;
  - blockers, side dependencies, parent reopen candidates, and visual-check need if any;
  - lab verdict;
  - next self-contained CALL.

  The result must be understandable without reading YAML.

return: |
  RESULT with readable Russian owner summary first, then machine RESULT block.
  Include proposed work/design-labs note content in state_changes.
  Include next CALL.

budget: one session

END_OF_FILE: live/indie-game-development/work/c-design-lab-gas-interaction-gameplay-001-call.md
