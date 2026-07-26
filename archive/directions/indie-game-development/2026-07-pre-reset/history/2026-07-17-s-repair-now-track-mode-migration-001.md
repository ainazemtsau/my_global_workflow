RESULT s-repair-now-track-mode-migration-001 (call: owner-directive-now-track-mode-migration-001)
direction: indie-game-development   track: core   play: repair   node/task: direction/now-track-mode-migration
owner_approved: 2026-07-17 — owner exact verdict «A» approved the presented track map, primary/default split, CALL statuses, TREE transitions and track_wip_limit 6.

outcome: |
  Legacy single-frontier NOW migrated to current track-mode with seven owner-readable tracks. `core` is the sole
  primary track for the unchanged g-9c41 NearGas L1B bet; `canon` carries the unchanged default
  `c-research-extraction-concept-landscape-001`. Owner-approved `track_wip_limit` is 6 and current occupancy is 6/6.

  All eight outstanding CALL ids, the full current bet, all six task ids/statuses, pending decision
  `d-m1-min-spec-hardware-001` and the default were preserved. No CALL was consumed, closed, completed or launched.
  No bet/task/node was newly declared done. Long legacy evidence was retained in existing CALL/history/knowledge
  artifacts; the already-registered but missing character Leg 2 artifact was materialized as PAUSED / NOT RUNNABLE.

  CALL status tally is exactly `ready 3 / waiting 0 / blocked 3 / paused 2`. It comes only from explicit current-NOW
  witnesses: READY for Level, extraction and marketing; HELD/NON-RUNNABLE for Unity runner; HELD for Sc-damage;
  LOCKED for visual; and the later track-wide owner PAUSE for both character CALLs. The Leg 2 repair/G5 dependency
  remains recorded under the pause and becomes relevant only after an explicit owner resume.

evidence: |
  Owner first received a concrete proposal naming all seven tracks and human labels, `core` as primary, every CALL
  assignment, status tally, WIP limit/occupancy and four TREE status transitions. Owner's complete verdict was exact
  text `A`; no broader close or execution authority was inferred.

  Fresh pre-apply Git evidence: NOW blob `e7ee45c75c66bac4ad0cb7001b97c3064c9601b5`; TREE blob
  `5aa8eabf75c87807e52fe66765bb12056650c4a0`. Legacy NOW contained exactly these outstanding ids and none was
  removed: `c-exec-level-module-standard-v1-lv0-plan-001`, `c-research-extraction-concept-landscape-001`,
  `c-exec-unity65-mac-revision-002-build-001`, `c-shape-sc-damage-001`, `c-visual-009`, `c-marketing-wake-001`,
  `c-exec-char-v2-reaction-core-repair-002`, `c-exec-char-v2-body-rig-ragdoll-build-001`.

  Explicit witnesses in legacy NOW: Level `READY PARALLEL`; extraction `READY PARALLEL`; marketing `READY`;
  Unity `HELD / NON-RUNNABLE`; Sc-damage `HELD until ready canon spec`; visual `LOCKED`; character repair
  `PAUSED BY OWNER — «можно поставить на паузу». Do not dispatch or mutate character track.` That track-wide pause
  is later and more specific for dispatch than the body-rig's retained `HELD until repair + G5` prerequisite.

  `history/2026-07-16-s-repair-level-lv0-parallel-launch-001.md` preserves the owner's clarification that NOW.bet /
  NOW.next is priority/default rather than a global lock. `history/2026-07-16-s-work-gascoopgame-worktree-protocol-v2-blocked-001.md`
  preserves the owner pause. The body-rig scope and mandatory C1–C4 carry-forwards are frozen in
  `work/c-plan-characters-002-plan.md` and `knowledge/g6d4e-char-v2-leg1-reaction-core.md`.

  Occupancy was computed by the current schema: core (blocked root + pending decision), level (ready root), canon
  (ready root), damage (blocked root), visual (blocked root) and marketing (ready root) each occupy one slot;
  characters has a paused root and paused child, so occupies zero. Total = 6, not above limit 6.

state_changes: |
  live/indie-game-development/NOW.md:
    - MIGRATE legacy single-frontier state to track-mode with `track_wip_limit: 6` and seven unique tracks:
      core/primary, level, canon, damage, visual, marketing and characters/parallel.
    - PRESERVE the g-9c41 NearGas L1B bet field-for-field, all six task ids/statuses, all eight open CALL ids,
      pending min-spec decision and logical default; normalize default to `next.call` and add stable decision id/track.
    - ADD track/status/call pointers and required unblock/pause/dependency fields. Compact legacy evidence blocks to
      one-line pointers without deleting their authoritative CALL/history/knowledge sources.
    - RECORD status tally ready 3 / waiting 0 / blocked 3 / paused 2; preserve character repair dependency under pause.
  live/indie-game-development/TREE.md:
    - ADD the one-line G9 `owner_approved` pointer for this exact owner verdict.
    - KEEP g-9c41 `active`; SET g-d3a8, g-7e15, g-6d4e and g-2f8c to schema-current `parallel`.
    - ADD no fake TREE nodes for the local Level/DA/PGG or Sc-damage scopes.
  live/indie-game-development/work/c-exec-char-v2-body-rig-ragdoll-build-001-call.md:
    - MATERIALIZE the already-registered recovery CALL from the frozen plan/current evidence as PAUSED / NOT
      RUNNABLE, with explicit resume + repair-002 + binding-G5 + fresh-authority dispatch gates and C1–C4.
  live/indie-game-development/work/board/dashboard.html:
    - REGENERATE the owner panel with seven human track names, primary/default distinction, CALL status tally,
      WIP 6/6, current open-work badges, glossary and a 17.07 Journal row; preserve five open findings.
    - KEEP only the latest three calendar days (17/16/15 July) in the Journal render; older evidence remains in LOG.
  live/indie-game-development/LOG.md:
    - APPEND the declared `log:` line once before the EOF trailer.
  live/indie-game-development/history/:
    - ADD `2026-07-17-s-repair-now-track-mode-migration-001.md` with this full RESULT and exact EOF trailer.
  live/indie-game-development/CHARTER.md, knowledge/, os/**, canon and product repos:
    - NO CHANGE.

captures: []

decisions_needed: []

play_check:
  - "1 Name the contradiction: done — current OS supports track-mode but live NOW was still a legacy single frontier, so parallel CALLs had no schema-valid track/status/WIP dispatch index."
  - "2 Reconstruct: done — re-read fresh NOW/TREE, all eight CALL routes, status witnesses, latest history, default, decision, bet/tasks, current schema, product dispatch authority and declared owner-panel rules."
  - "3 Propose corrected state: done — presented seven labeled tracks, core primary, exact CALL mapping/status tally, WIP limit 6 with occupancy 6/6, default preservation and TREE transitions before writing."
  - "4 Confirm (owner): done — owner actual verdict was exact `A`, approving the presented proposal including the G9 TREE edits and WIP limit; no close or execution verdict was inferred."
  - "5 Friction: done — the underlying single-frontier/parallel-dispatch rule defect is already recorded and fixed in current OS ancestry by commits 227f33e and 418f6f6; this leg repairs only live state, so no duplicate FRICTION entry or os/** edit was made."

log: 2026-07-17 — repair/track-mode (direction/now-track-mode, s-repair-now-track-mode-migration-001): legacy NOW migrated to seven-track frontier with WIP 6/6; all eight CALLs, the current bet, pending decision and extraction default preserved, statuses = ready 3 / blocked 3 / paused 2, and nothing launched or closed. → history/2026-07-17-s-repair-now-track-mode-migration-001.md

next: |
  call: c-research-extraction-concept-landscape-001
  track: canon
  status: ready
  artifact: work/c-research-extraction-concept-landscape-001-call.md

END_OF_FILE: live/indie-game-development/history/2026-07-17-s-repair-now-track-mode-migration-001.md
