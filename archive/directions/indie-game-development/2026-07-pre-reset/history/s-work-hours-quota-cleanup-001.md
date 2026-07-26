RESULT s-work-hours-quota-cleanup-001 (call: owner-plain-2026-06-29-hours-cleanup)
direction: indie-game-development   play: work   node/task: g-7e15 + charter/hours-cleanup
outcome: |
  Fixed-hour quota wording is no longer active instruction in the current direction state.
  The charter now says the game is the owner's primary work direction without a fixed weekly hour quota.
  The visual track now says it has a secondary cadence in engine build-gaps without a fixed hour quota.
evidence: |
  Verified no matches for current numeric hour-quota phrases in:
  - live/indie-game-development/CHARTER.md
  - live/indie-game-development/TREE.md
  - live/indie-game-development/NOW.md
  - live/indie-game-development/work/c-visual-002-call.md

  Search used:
  rg -n "80–90|40–60|min/day|h/week|hours/week|hours\/week|12h/day|часов|часа" <current files>

  END_OF_FILE trailers checked on all edited state/work files.
state_changes: |
  CHARTER.md:
  - Constraints / Time: replaced the "80–90 hours/week" line with "primary work direction; scheduling is capacity-based, not a fixed hour quota."
  - Owner edges / Availability: replaced the "80–90 hours/week" proof line with "primary work focus without treating any fixed weekly hour count as a requirement."
  - Pre-mortem #12: replaced "80–90 hours/week" failure mode with "a fixed-hour or crunch expectation."
  - owner_approved: owner said "давай его уберем".

  TREE.md:
  - g-7e15 detail: replaced "SECONDARY to g-9c41, ~40–60 min/day" with "SECONDARY to g-9c41, with no fixed hour quota."
  - owner_approved: owner said "давай его уберем".

  NOW.md:
  - parallel_tracks / g-7e15 appetite: replaced "~40–60 min/day in the engine's build-gaps (≈3–5 h/week)" with "secondary visual cadence in the engine's build-gaps; no fixed hour quota."
  - historical owner-steer note: replaced "~12h/day" with "long agent sessions" so the live state no longer normalizes a daily hour count.

  work/c-visual-002-call.md:
  - budget & rigor: replaced "~40-60 min/day owner-gated build-gaps" with "Secondary visual-track cadence in owner-gated engine build-gaps; no fixed hour quota."

  LOG.md:
  - appended this session log line.

  history/:
  - added history/s-work-hours-quota-cleanup-001.md.
captures:
  - Future planning should express cadence as priority/capacity/appetite, not fixed daily or weekly hour requirements.
decisions_needed: []
play_check:
  - 1 Recite: done — task restated as removing accidental fixed-hour requirements from active state.
  - 2 Owner inputs (owner): done — owner explicitly requested "ОЧЕНЬ КРУТО! но как то много часов у нас видимо где то затесалось требования про часы давай его уберем".
  - 3 Do the work: done — replaced all current numeric hour-quota phrasing found in CHARTER/TREE/NOW/c-visual-002-call.
  - 4 Self-check: done — rg found no current numeric hour-quota matches in the edited active files; END_OF_FILE trailers intact.
  - 5 Close: done — state cleanup recorded here, with next set to return to current work.
log: work/cleanup (g-7e15 + charter): removed fixed-hour quota wording from current state and the visual CALL; CHARTER/TREE owner-approved.
next: |
  return-to-current-work: Sc-weight executor CALL remains the engine next; visual S2 / minimalist visual direction remains available as a separate owner-chosen follow-up.

END_OF_FILE: live/indie-game-development/history/s-work-hours-quota-cleanup-001.md
